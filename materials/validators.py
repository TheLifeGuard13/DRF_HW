from rest_framework.exceptions import ValidationError


class UrlValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value) -> None:
        temp_value = dict(value).get(self.field)
        allowed_server = "@youtube.com"
        if temp_value is not None and allowed_server not in temp_value:
            raise ValidationError(f"Ссылка должна быть только с сервиса Youtube или отсутствовать")
