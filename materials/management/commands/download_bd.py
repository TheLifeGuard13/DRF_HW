import typing

from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = "Download fixtures to files from all apps"

    def handle(self, *args: typing.Any, **options: typing.Any) -> None:
        call_command("dumpdata", "auth.group", "-o", "materials/fixtures/group_data.json")
        call_command("dumpdata", "users.payment", "-o", "materials/fixtures/payment_data.json")
        call_command("dumpdata", "users.user", "-o", "materials/fixtures/user_data.json")
        call_command("dumpdata", "materials.course", "-o", "materials/fixtures/course_data.json")
        call_command("dumpdata", "materials.lesson", "-o", "materials/fixtures/lesson_data.json")
