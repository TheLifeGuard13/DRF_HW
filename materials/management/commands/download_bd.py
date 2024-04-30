import typing

from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = "Download fixtures to files from all apps"

    def handle(self, *args: typing.Any, **options: typing.Any) -> None:
        call_command("dumpdata", "auth", "-o", "materials/fixtures/auth_data.json")
        call_command("dumpdata", "users", "-o", "materials/fixtures/users_data.json")
        call_command("dumpdata", "materials", "-o", "materials/fixtures/materials_data.json")
