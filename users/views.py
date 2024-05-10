from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny

from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer
from users.services import create_stripe_product, create_stripe_price, create_stripe_session


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(owner=self.request.user)
        product_name = payment.paid_course.name
        stripe_product = create_stripe_product(product_name)
        amount_in_usd = payment.paid_course.price
        stripe_price = create_stripe_price(stripe_product, amount_in_usd)
        session_id, payment_link = create_stripe_session(stripe_price)
        payment.payment_amount = amount_in_usd
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filterset_fields = ("paid_course", "paid_lesson", "payment_method", )
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["payment_date", "payment_amount", ]


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
