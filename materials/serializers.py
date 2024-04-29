from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
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


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
