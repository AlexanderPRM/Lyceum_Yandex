# Generated by Django 3.2.16 on 2022-12-04 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_auto_20221203_1402"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "категория", "verbose_name_plural": "категории"},
        ),
        migrations.AlterField(
            model_name="photositem",
            name="image",
            field=models.ImageField(upload_to="", verbose_name="фото"),
        ),
    ]
