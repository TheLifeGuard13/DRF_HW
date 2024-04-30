# import json
#
# from django.conf import settings
# from django.core.management import BaseCommand
# from django.db import connection
#
# from config.settings import FIXTURES_DATA_PATH
# from materials.models import Course, Lesson
# from users.models import Payment, User
#
#
# class Command(BaseCommand):
#
#     @staticmethod
#     def json_read_payments():
#         """Здесь мы получаем данные из фикстуры с платежами"""
#         with open(FIXTURES_DATA_PATH, encoding='utf-8') as file:
#             data = json.load(file)
#             return [data for data in data if data['model'] == 'users.payment']
#
#     def handle(self, *args, **options):
#         # Удаляем все платежи
#         with connection.cursor() as cursor:
#             cursor.execute(f'TRUNCATE TABLE users_payment RESTART IDENTITY CASCADE;')
#
#         # Создайте списки для хранения объектов
#         payments_for_create = []
#
#         # Обходим все значения платежей из фикстуры для получения информации об одном объекте
#         for payment in Command.json_read_payments():
#             payments_for_create.append(Payment(owner="",
#                                                payment_date=payment['fields']['payment_date'],
#                                                paid_course=Course.objects.get(pk=payment['fields']['paid_course']),
#                                                paid_lesson=Lesson.objects.get(pk=payment['fields']['paid_lesson']),
#                                                payment_amount=payment['fields']['payment_amount'],
#                                                payment_method=payment['fields']['payment_method']))
#
#         # Создаем объекты в базе с помощью метода bulk_create()
#         Payment.objects.bulk_create(payments_for_create)
