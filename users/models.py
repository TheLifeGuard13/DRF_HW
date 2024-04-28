from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Почта")

    phone = models.CharField(max_length=35, null=True, blank=True, verbose_name="Телефон")
    avatar = models.ImageField(upload_to="users/", null=True, blank=True, verbose_name="Аватар")
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name="Город")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
