from django.contrib import admin
from feedback.models import FeedBack


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('text', 'mail', 'created_on')
    list_display_links = ('text',)
