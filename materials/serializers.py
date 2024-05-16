from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson, Subscription
from materials.validators import UrlValidator


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [UrlValidator(field="url")]


class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(source="lesson_set", many=True, read_only=True)
    lessons_in_course_count = SerializerMethodField()
    is_subscribed = SerializerMethodField()
    subscribers = SubscriptionSerializer(source='course_for_subscription', many=True, read_only=True)

    def get_lessons_in_course_count(self, obj):
        return obj.lesson_set.all().count()

    def get_is_subscribed(self, obj):
        request = self.context.get("request")
        user = None
        if request:
            user = request.user
        return obj.course_for_subscription.filter(subscriber=user).exists()

    class Meta:
        model = Course
        fields = "__all__"
