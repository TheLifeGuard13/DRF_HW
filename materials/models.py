from django.db import models

from config.settings import NULLABLE


class Course(models.Model):
    """
    Модель Курса
    """

    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(**NULLABLE, verbose_name="Описание")
    preview = models.ImageField(upload_to="courses/", **NULLABLE, verbose_name="Превью")

    def __str__(self) -> str:
        return f"{self.name}"

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

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
