# Generated by Django 5.0.4 on 2024-04-30 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_payment_payment_date"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="payment",
            options={"ordering": ("-payment_date",), "verbose_name": "платеж", "verbose_name_plural": "платежи"},
        ),
    ]
