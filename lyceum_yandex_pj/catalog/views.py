from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from catalog.models import Item
from rating.models import ItemRating


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

    def get_context_data(self, **kwargs):
        context = super(ItemDetail, self).get_context_data(**kwargs)
        context['avg_rate'] = ItemRating.objects.item_avg_rate(
            item_pk=kwargs['object'].id
            )
        context['user_rate'] = ItemRating.objects.get_user_rate(
            user_pk=self.request.user.id,
            item_pk=kwargs['object'].id
            ) if self.request.user.is_authenticated else None
        return context
