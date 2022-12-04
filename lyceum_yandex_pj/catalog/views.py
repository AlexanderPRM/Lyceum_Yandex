from django.shortcuts import get_object_or_404, render

from .models import Item


def item_list(request):
    items = Item.objects.published_item()
    context = {
        'items': items
    }
    return render(request, 'pages/catalog/main.html', context)


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {'item': item}
    return render(
        request,
        template_name='pages/catalog/item_detail.html',
        context=context
        )
