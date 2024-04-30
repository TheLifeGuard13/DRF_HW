from django.urls import path

from users.apps import UsersConfig
from users.views import PaymentCreateAPIView, PaymentListAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('payment/create', PaymentCreateAPIView.as_view(), name='create_payment'),
    path('payment/', PaymentListAPIView.as_view(), name='list_payment'),
]
