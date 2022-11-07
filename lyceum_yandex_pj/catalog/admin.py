from django.contrib import admin
from catalog.models import Item, Category, Tag, PhotoItem, PhotosItem
from sorl.thumbnail import get_thumbnail
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin


class ItemAdmin(SummernoteModelAdmin):
    list_display = ('name', 'is_published', 'img_thumb')
    list_editable = ('is_published',)
    list_display_links = ('name',)
    filter_horizontal = ('tag',)
    summernote_fields = ('text',)

    def get_img(self, obj):
        print(self)
        return get_thumbnail(obj.photoitem.image,
                             "300x300",
                             crop='center',
                             qualify=51)

    def img_thumb(self, obj):
        if obj.photoitem.item:
            return mark_safe(f'<img src="{self.get_img(obj).url}">')
        return "Нет изображения"

    img_thumb.short_description = 'Превью'
    img_thumb.allow_tags = True


admin.site.register(Item, ItemAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'weight')
    list_editable = ('is_published',)
    list_display_links = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_editable = ('is_published',)
    list_display_links = ('name',)


@admin.register(PhotoItem)
class PhotoItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'image')
    list_editable = ('image',)


@admin.register(PhotosItem)
class PhotosItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'image', 'img_thumb')
    list_editable = ('image',)
    readonly_fields = ('img_thumb',)

    def get_img(self, obj):
        return get_thumbnail(obj.image, "300x300", crop='center', qualify=51)

    def img_thumb(self, obj):
        return mark_safe(f'<img src="{self.get_img(obj).url}">')
        # return "Нет изображения"

    img_thumb.short_description = 'Превью'
    img_thumb.allow_tags = True
