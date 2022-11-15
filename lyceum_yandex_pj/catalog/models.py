from catalog.validators import validate_text
from core.models import BaseCatalog, SlugMixin
from django.core.validators import (MaxValueValidator, MinValueValidator)
from django.db import models
from django.db.models.query import Prefetch


class Tag(BaseCatalog, SlugMixin):
    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.name


class Category(BaseCatalog, SlugMixin):
    weight = models.SmallIntegerField(default=100,
                                      validators=[MinValueValidator(0),
                                                  MaxValueValidator(32767)
                                                  ],
                                      verbose_name='вес')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ItemPublishedManager(models.Manager):
    def published(self):
        return (self.get_queryset()
                    .filter(is_published=True)
                    .order_by('name')
                    .select_related('category')
                    .prefetch_related(Prefetch('tag',
                                      queryset=Tag.objects
                                                  .filter(is_published=True)
                                                  .only('name'))
                                      )
                )


class Item(BaseCatalog):
    is_on_main = models.BooleanField(verbose_name='на главной', default=False)
    text = models.TextField(verbose_name='описание',
                            validators=[
                                validate_text('превосходно', 'роскошно')])
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='items',
                                 verbose_name='категория')
    tag = models.ManyToManyField(Tag,
                                 related_name='items',
                                 verbose_name='теги')

    objects = ItemPublishedManager()

    # def get_item_url(self):
    #     return reverse('catalog:item_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class PhotoItem(models.Model):
    image = models.ImageField(verbose_name='фото')
    item = models.OneToOneField(Item,
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = 'превью товара'


class PhotosItem(models.Model):
    image = models.ImageField()
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             related_name='photos')

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = 'фото товара'
        verbose_name_plural = 'фотогалерея товаров'
