from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import User


class MaterialTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email="test_email",
            is_staff=True,
            is_superuser=True,
            password="123"
        )
        self.client.force_authenticate(user=self.user)
        self.lesson = Lesson.objects.create(
            name="test_lesson_1",
            owner=self.user
        )
        self.course = Course.objects.create(
            name="test_course_1",
            owner=self.user
        )

    def test_create_lesson(self):
        """ Тестирование создания урока """
        url = reverse("materials:create_lesson")
        data = {
            "name": "test_lesson_2",
            "owner": self.user.pk
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_create_lesson_error(self):
        """ Тестирование создания урока c неправильным url """
        url = reverse("materials:create_lesson")
        data = {
            "name": "test_lesson_3",
            "owner": self.user.pk,
            "url": "123@mail.ru"
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_lesson(self):
        """ Тестирование вывода списка уроков """
        url = reverse("materials:list_lesson")
        response = self.client.get(url)
        data = response.json()
        result = {'count': 1,
                  'next': None,
                  'previous': None,
                  'results': [
                      {
                          'id': self.lesson.pk,
                          'name': self.lesson.name,
                          'description': None,
                          'preview': None,
                          'url': None,
                          'course': None,
                          'owner': self.user.pk
                      }
                  ]
                  }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_retrieve_lesson(self):
        """ Тестирование вывода отдельного урока """
        url = reverse("materials:get_lesson", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)

    def test_update_lesson(self):
        """ Тестирование обновления урока """
        url = reverse("materials:update_lesson", args=(self.lesson.pk,))
        data = {
            "name": "test_lesson_21",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "test_lesson_21")

    def test_delete_lesson(self):
        """ Тестирование удаления урока """
        url = reverse("materials:delete_lesson", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_change_subscription(self):
        """ Тестирование создания/удаления подписки """
        url = reverse("materials:create_subscription")

        new_subscription = {
            "course": self.course.pk,
            "subscriber": 1
        }

        course_response = self.client.get(f"/courses/{self.course.pk}/")
        self.assertEqual(course_response.json().get("is_subscribed"), False)

        response_create = self.client.post(url, data=new_subscription)
        self.assertEqual(response_create.status_code, status.HTTP_200_OK)
        self.assertEqual(Subscription.objects.all().count(), 1)

        course_response = self.client.get(f"/courses/{self.course.pk}/")
        self.assertEqual(course_response.json().get("is_subscribed"), True)

        response_delete = self.client.post(url, data=new_subscription)
        self.assertEqual(response_delete.status_code, status.HTTP_200_OK)
        self.assertEqual(Subscription.objects.all().count(), 0)

        course_response = self.client.get(f"/courses/{self.course.pk}/")
        self.assertEqual(course_response.json().get("is_subscribed"), False)

    def test_create_course(self):
        """ Тестирование создания курса """
        data = {
            "name": "test_course",
            "description": "test_course_description",
            "owner": self.user.pk
        }
        response = self.client.post("/courses/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(),
                         {'id': response.json().get("id"), 'lesson': [], 'lessons_in_course_count': 0,
                          'is_subscribed': False,
                          'name': 'test_course', 'description': 'test_course_description', 'preview': None,
                          'owner': self.user.pk})
        self.assertTrue(Course.objects.all().exists())

    def test_retrieve_course(self):
        """ Тестирование вывода отдельного курса """
        response = self.client.get(f"/courses/{self.course.pk}/")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.course.name)

    def test_delete_course(self):
        """ Тестирование удаления курса """
        response = self.client.delete(f"/courses/{self.course.pk}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.all().count(), 0)
