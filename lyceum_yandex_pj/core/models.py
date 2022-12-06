from django.db import models
from django.core.validators import RegexValidator


class BaseCatalog(models.Model):
    name = models.CharField(
        max_length=150,
        help_text="Имя не должно превышать 150 символов",
        verbose_name="Имя",
    )
    is_published = models.BooleanField(verbose_name="Опубликовано", default=True)

    class Meta:
        abstract = True


class SlugMixin(models.Model):
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name="слаг",
        help_text="Используйте только цифры, " "буквы латиницы и символы - и _",
        validators=[
            RegexValidator(
                regex="^[a-z0-9]+(?:[_|-][a-z0-9]+)*$",
            )
        ],
    )

    class Meta:
        abstract = True
