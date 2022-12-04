from django.views.generic.list import ListView
from catalog.models import Item


class HomePage(ListView):
    template_name = 'pages/homepage/main.html'
    model = Item
    context_object_name = 'items'

    def get_queryset(self):
        return self.model.objects.item_on_main_page()
