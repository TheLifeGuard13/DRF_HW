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

    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    preview = models.ImageField(upload_to="lessons/", null=True, blank=True, verbose_name="Превью")
    url = models.CharField(max_length=150, null=True, blank=True, verbose_name="Ссылка")
    course = models.ForeignKey(Course, on_delete=models.SET, null=True, blank=True, verbose_name="Курс")

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
