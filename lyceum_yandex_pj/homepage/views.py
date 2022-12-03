from django.shortcuts import render
from catalog.models import Item


def home(request):
    items = Item.objects.item_on_main_page()
    context = {
        'items': items
    }
    return render(request, 'pages/homepage/main.html', context)
