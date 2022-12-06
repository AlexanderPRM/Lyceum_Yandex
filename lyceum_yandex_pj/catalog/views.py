from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.shortcuts import redirect

from catalog.models import Item
from rating.models import ItemRating
from rating.forms import RateForm


class ItemList(ListView):
    model = Item
    template_name = "pages/catalog/main.html"
    context_object_name = "items"

    def get_queryset(self):
        return Item.objects.published_item()


class ItemDetail(DetailView, UpdateView):
    model = Item
    template_name = "pages/catalog/item_detail.html"
    form_class = RateForm

    def get_initial(self, **kwargs):
        initial = super(ItemDetail, self).get_initial(**kwargs)
        try:
            initial["rate"] = ItemRating.objects.get(
                item__pk=self.kwargs["pk"], user__pk=self.request.user.id
            ).rate
        except ObjectDoesNotExist:
            pass
        return initial

    def get_context_data(self, **kwargs):
        context = super(ItemDetail, self).get_context_data(**kwargs)
        context["avg_rate"] = ItemRating.objects.item_avg_rate(
            item_pk=kwargs["object"].id
        )
        if self.request.user.is_authenticated:
            context["user_rate"] = ItemRating.objects.get_user_rate(
                user_pk=self.request.user.id, item_pk=kwargs["object"].id
            )
        else:
            context["user_rate"] = None
        return context

    def form_valid(self, form):
        form.save(self.request.user, self.kwargs["pk"])
        return redirect("catalog:item_detail", self.kwargs["pk"])
