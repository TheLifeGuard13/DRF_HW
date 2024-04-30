import typing

from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = "Upload fixtures from files to DB"

    def handle(self, *args: typing.Any, **options: typing.Any) -> None:
        call_command("loaddata", "materials/fixtures/users_data.json")
