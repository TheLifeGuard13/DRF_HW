from django.conf import settings
from django.db import models

from config.settings import NULLABLE


class Course(models.Model):
    """
    Модель Курса
    """

    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(**NULLABLE, verbose_name="Описание")
    preview = models.ImageField(upload_to="courses/", **NULLABLE, verbose_name="Превью")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, default="", on_delete=models.CASCADE, **NULLABLE, verbose_name="Владелец"
    )
    price = models.PositiveIntegerField(default="10000", verbose_name="Цена курса")

    def __str__(self) -> str:
        return f"{self.name}, {self.price}"

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Lesson(models.Model):
    """
    Модель Урока
    """

    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(**NULLABLE, verbose_name="Описание")
    preview = models.ImageField(upload_to="lessons/", **NULLABLE, verbose_name="Превью")
    url = models.CharField(max_length=150, **NULLABLE, verbose_name="Ссылка")
    course = models.ForeignKey(Course, on_delete=models.SET, **NULLABLE, verbose_name="Курс")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, default="", on_delete=models.CASCADE, **NULLABLE, verbose_name="Владелец"
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"


class Subscription(models.Model):
    """
    Модель Подписки
    """

    course = models.ForeignKey(Course, on_delete=models.SET, **NULLABLE, verbose_name="Курс",
                               related_name="course_for_subscription")
    subscriber = models.ForeignKey(
        settings.AUTH_USER_MODEL, default="", on_delete=models.CASCADE, **NULLABLE, verbose_name="Подписчик")

    def __str__(self) -> str:
        return f"{self.course}, {self.subscriber}"

    class Meta:
        verbose_name = "подписка"
        verbose_name_plural = "подписки"
