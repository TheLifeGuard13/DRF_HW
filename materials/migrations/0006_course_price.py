# Generated by Django 5.0.4 on 2024-05-09 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0005_subscription"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="price",
            field=models.PositiveIntegerField(default="10000", verbose_name="Цена курса"),
        ),
    ]
