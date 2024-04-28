from django.db import models


class Course(models.Model):
    """
    Модель Курса
    """

    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    preview = models.ImageField(upload_to="courses/", null=True, blank=True, verbose_name="Превью")

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Lesson(models.Model):
    """
    Модель Урока
    """

    header = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    preview = models.ImageField(upload_to="lessons/", null=True, blank=True, verbose_name="Превью")
    url = models.CharField(max_length=150, verbose_name="Ссылка")

    def __str__(self) -> str:
        return f"{self.header}"

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
