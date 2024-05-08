from django.urls import path
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials.views import (CourseViewSet, LessonCreateAPIView,
                             LessonDestroyAPIView, LessonListAPIView,
                             LessonRetrieveAPIView, LessonUpdateAPIView, SubscriptionCreateAPIView)

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create', LessonCreateAPIView.as_view(), name='create_lesson'),
    path('lesson/', LessonListAPIView.as_view(), name='list_lesson'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='get_lesson'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='update_lesson'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='delete_lesson'),
    path('subscription/create', SubscriptionCreateAPIView.as_view(), name='create_subscription'),
] + router.urls
