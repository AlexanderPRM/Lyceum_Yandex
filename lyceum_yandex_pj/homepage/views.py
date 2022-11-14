from catalog.models import Item
from django.shortcuts import render


def home(request):
    context = {'items': Item.objects.published()
                            .filter(is_on_main=True)
                            .only('name', 'category__name', 'text')}
    return render(request,
                  template_name='pages/homepage/main.html',
                  context=context)
