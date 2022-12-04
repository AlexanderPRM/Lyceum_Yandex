from django.core.validators import (MaxValueValidator, MinValueValidator)
from django.db import models

from catalog.validators import ContainsOneOfWorldValidator
from core.models import BaseCatalog, SlugMixin


class CategoryManager(models.Manager):
    def published_cat(self):
        return (self.get_queryset().filter(is_published=True))


class TagManager(models.Manager):
    def published_tags(self):
        return (self.get_queryset().filter(is_published=True))


class ItemManager(models.Manager):
    def published_item(self):
        return (
            self.get_queryset()
                .filter(is_published=True)
                .select_related('category')
                .order_by('category__name', 'name')
                .prefetch_related(
                    models.Prefetch('tags',
                                    queryset=Tag.objects.published_tags())))

    def item_on_main_page(self):
        return (self.get_queryset()
                    .filter(is_on_main=True, is_published=True)
                    .order_by('name')
                    .select_related('category')
                    .prefetch_related(
                        models.Prefetch('tags',
                                        queryset=Tag.objects.published_tags(
                                        ))))

    def item_detail(self, pk):
        return (self.get_queryset()
                    .filter(is_published=True, pk=pk)
                    .select_related('category')
                    .prefetch_related(
                        models.Prefetch('tags',
                                        queryset=Tag.objects.published_tags(
                                        ))))


class Tag(BaseCatalog, SlugMixin):
    objects = TagManager()

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.name


class Category(BaseCatalog, SlugMixin):
    weight = models.SmallIntegerField(
                            default=100,
                            validators=[
                                        MinValueValidator(0),
                                        MaxValueValidator(32767)
                                        ],
                            verbose_name='вес')

    objects = CategoryManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Item(BaseCatalog):
    is_on_main = models.BooleanField(verbose_name='на главной', default=False)
    text = models.TextField(
        verbose_name='описание',
        validators=[
                    ContainsOneOfWorldValidator(
                                        'превосходно',
                                        'роскошно'
                                        )
                    ]
            )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='категория'
        )
    tags = models.ManyToManyField(
        Tag,
        related_name='items',
        verbose_name='теги'
        )

    objects = ItemManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class PhotoItem(models.Model):
    image = models.ImageField(verbose_name='фото')
    item = models.OneToOneField(
        Item,
        on_delete=models.CASCADE
        )

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = 'превью товара'


class PhotosItem(models.Model):
    image = models.ImageField(verbose_name='фото')
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='photos'
        )

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = 'фото товара'
        verbose_name_plural = 'фотогалерея товаров'
