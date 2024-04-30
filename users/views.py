from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from materials.serializers import PaymentSerializer
from users.models import Payment


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filterset_fields = ("paid_course", "paid_lesson", "payment_method", )
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["payment_date", "payment_amount", ]
