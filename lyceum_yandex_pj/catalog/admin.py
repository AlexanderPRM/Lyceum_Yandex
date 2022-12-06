from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.models import Attachment
from sorl.thumbnail import get_thumbnail

from catalog.models import Category, Item, PhotoItem, PhotosItem, Tag


class PhotoItemInline(admin.TabularInline):
    model = PhotoItem


class PhotosItemInline(admin.TabularInline):
    model = PhotosItem


class ItemAdmin(SummernoteModelAdmin):
    list_display = ("id", "name", "is_published", "img_thumb")
    list_editable = ("is_published",)
    list_display_links = ("name",)
    filter_horizontal = ("tags",)
    summernote_fields = ("text",)
    inlines = (PhotoItemInline, PhotosItemInline)

    def get_img(self, obj):
        return get_thumbnail(
            obj.photoitem.image, "300x300", crop="center", qualify=51
        )

    def img_thumb(self, obj):
        if obj.photoitem.item:
            return mark_safe(f'<img src="{self.get_img(obj).url}">')
        return "Нет изображения"

    img_thumb.short_description = "Превью"
    img_thumb.allow_tags = True


admin.site.register(Item, ItemAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_published", "weight")
    list_editable = ("is_published",)
    list_display_links = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "is_published")
    list_editable = ("is_published",)
    list_display_links = ("name",)


@admin.register(PhotosItem)
class PhotosItemAdmin(admin.ModelAdmin):
    list_display = ("item", "image", "img_thumb")
    list_editable = ("image",)
    readonly_fields = ("img_thumb",)

    def get_img(self, obj):
        return get_thumbnail(obj.image, "300x300", crop="center", qualify=51)

    def img_thumb(self, obj):
        return mark_safe(f'<img src="{self.get_img(obj).url}">')

    img_thumb.short_description = "Превью"
    img_thumb.allow_tags = True


admin.site.unregister(Attachment)
