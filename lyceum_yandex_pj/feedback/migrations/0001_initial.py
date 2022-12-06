# Generated by Django 3.2.16 on 2022-11-21 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FeedBack",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(verbose_name="Содержимое")),
                (
                    "mail",
                    models.EmailField(max_length=150, verbose_name="Почта"),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
