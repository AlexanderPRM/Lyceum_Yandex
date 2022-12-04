from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Item


class ItemList(ListView):
    model = Item
    template_name = 'pages/catalog/main.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.published_item()


class ItemDetail(DetailView):
    model = Item
    template_name = 'pages/catalog/item_detail.html'
    context_object_name = 'item'
