# Generated by Django 3.2.16 on 2022-11-06 16:00

import catalog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20221106_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(validators=[catalog.validators.validate_text], verbose_name='Описание'),
        ),
    ]
