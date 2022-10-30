from django.db import models


class BaseCatalog(models.Model):
    name = models.CharField(
                max_length=150,
                help_text='Имя не должно превышать 150 символов',
                verbose_name='Имя'
                )
    is_published = models.BooleanField(
                                verbose_name='Опубликовано',
                                default=True
                                )

    class Meta:
        abstract = True
