from django.db import models
from core.models import BaseCatalog
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator
from catalog.validators import validate_text


class Tag(BaseCatalog):
    slug = models.SlugField(max_length=200,
                            unique=True,
                            verbose_name='Слаг',
                            help_text='Используйте только цифры, '
                                      'буквы латиницы и символы - и _',
                            validators=[
                                RegexValidator(
                                    regex='^[a-z0-9]+(?:[_|-][a-z0-9]+)*$')]
                            )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Category(BaseCatalog):
    slug = models.SlugField(max_length=200,
                            unique=True,
                            verbose_name='Слаг',
                            help_text='Используйте только цифры, '
                                      'буквы латиницы и символы - и _',
                            validators=[
                                RegexValidator(
                                    regex='^[a-z0-9]+(?:[_|-][a-z0-9]+)*$',)])
    weight = models.SmallIntegerField(default=100,
                                      validators=[MinValueValidator(0),
                                                  MaxValueValidator(32767)
                                                  ],
                                      verbose_name='Вес')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Item(BaseCatalog):
    text = models.TextField(verbose_name='Описание',
                            validators=[
                                validate_text('превосходно', 'роскошно')])
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='items',
                                 verbose_name='Категория')
    tag = models.ManyToManyField(Tag,
                                 related_name='items',
                                 verbose_name='Теги')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class PhotoItem(models.Model):
    image = models.ImageField()
    item = models.OneToOneField(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фото товара'


class PhotosItem(models.Model):
    image = models.ImageField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фотогалерея товаров'
