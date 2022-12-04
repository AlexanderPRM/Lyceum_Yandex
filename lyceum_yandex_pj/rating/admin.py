from django.contrib import admin

from rating.models import ItemRating


@admin.register(ItemRating)
class CategoryAdmin(admin.ModelAdmin):
    ...
