from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson
from materials.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [UrlValidator(field="url")]


class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(source="lesson_set", many=True, read_only=True)
    lessons_in_course_count = SerializerMethodField()

    def get_lessons_in_course_count(self, obj):
        return obj.lesson_set.all().count()

    class Meta:
        model = Course
        fields = "__all__"
