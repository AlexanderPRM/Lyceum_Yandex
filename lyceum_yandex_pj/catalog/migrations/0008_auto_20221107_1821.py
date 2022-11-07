# Generated by Django 3.2.16 on 2022-11-07 15:21

import catalog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_item_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photoitem',
            options={'verbose_name': 'Фото товара', 'verbose_name_plural': 'Фото товара'},
        ),
        migrations.AlterModelOptions(
            name='photositem',
            options={'verbose_name': 'Фото товара', 'verbose_name_plural': 'Фотогалерея товаров'},
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(validators=[catalog.validators.validate_text], verbose_name='Описание'),
        ),
    ]
