from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import NULLABLE, PAYMENT_METHOD_CHOICES
from materials.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Почта")

    phone = models.CharField(max_length=35, **NULLABLE, verbose_name="Телефон")
    avatar = models.ImageField(upload_to="users/", **NULLABLE, verbose_name="Аватар")
    city = models.CharField(max_length=50, **NULLABLE, verbose_name="Город")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payment(models.Model):
    """
    Модель платежей
    """

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, default="", on_delete=models.CASCADE, **NULLABLE, verbose_name="Владелец"
    )
    payment_date = models.DateTimeField(**NULLABLE, auto_now_add=True, verbose_name="Дата платежа")
    paid_course = models.ForeignKey(Course, on_delete=models.SET, **NULLABLE, verbose_name="Оплаченный курс")
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.SET, **NULLABLE, verbose_name="Оплаченный урок")
    payment_amount = models.FloatField(**NULLABLE,)
    payment_method = models.CharField(max_length=150, choices=PAYMENT_METHOD_CHOICES, verbose_name="Вариант оплаты")

    def __str__(self) -> str:
        return f"{self.owner}"

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"
        ordering = ("-payment_date",)
