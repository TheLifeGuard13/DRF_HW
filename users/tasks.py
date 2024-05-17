from celery import shared_task
from datetime import datetime, timedelta
from users.models import User
import pytz
from django.conf import settings


@shared_task
def block_inactive_user():
    """ Блокировка пользователя если он не заходил более 30 календарных дней на платформу """
    zone = pytz.timezone(settings.TIME_ZONE)
    now = datetime.now(zone)
    expiration_date = now - timedelta(days=30)
    users_list = User.objects.all()
    for users in users_list:
        if not users.last_login:
            users.last_login = now
        if users.last_login < expiration_date:
            users.is_active = False
        users.save()
