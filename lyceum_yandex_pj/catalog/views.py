from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from catalog.models import Item
from rating.models import ItemRating
from rating.forms import RateForm


class ItemList(ListView):
    model = Item
    template_name = 'pages/catalog/main.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.published_item()


class ItemDetail(UpdateView, DetailView):
    model = ItemRating
    template_name = 'pages/catalog/item_detail.html'
    context_object_name = 'item'
    form_class = RateForm

    def get_context_data(self, **kwargs):
        context = super(ItemDetail, self).get_context_data(**kwargs)
        context['avg_rate'] = ItemRating.objects.item_avg_rate(
            item_pk=kwargs['object'].id
            )
        if self.request.user.is_authenticated:
            context['user_rate'] = ItemRating.objects.get_user_rate(
                user_pk=self.request.user.id,
                item_pk=kwargs['object'].id
                )
            context['form'] = RateForm()
            context['item'] = Item.objects.get(pk=kwargs['object'].id)
        else:
            context['user_rate'] = None
        return context
