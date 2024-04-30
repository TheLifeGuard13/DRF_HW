from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson
from users.models import Payment


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(source="lesson_set", many=True)

    class Meta:
        model = Course
        fields = "__all__"


class LessonsInCourseSerializer(serializers.ModelSerializer):
    lessons_in_course_count = SerializerMethodField()

    def get_lessons_in_course_count(self, obj):
        return obj.lesson_set.all().count()

    class Meta:
        model = Course
        fields = ('name', 'description', 'preview', 'lessons_in_course_count', )


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
