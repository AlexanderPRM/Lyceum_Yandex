# Generated by Django 3.2.16 on 2022-11-28 14:58

import catalog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_alter_item_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(validators=[catalog.validators.validate_text], verbose_name='описание'),
        ),
    ]
