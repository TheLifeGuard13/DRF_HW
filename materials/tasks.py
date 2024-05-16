import typing

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from materials.models import Subscription


@shared_task
def send_updates(item: typing.Any) -> typing.Any:
    """Отправляет уведомления обновлениях курсов на почту подписчикам."""
    active_subscriptions = Subscription.objects.filter(course=item)
    if active_subscriptions:
        for item in active_subscriptions:
            send_mail(subject=f'Обновление курса {item.course.name}',
                      message=f'Информируем, что курс {item.course.name} обновлен',
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[item.subscriber.email],
                      fail_silently=False)
