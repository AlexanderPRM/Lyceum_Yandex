from django.shortcuts import get_object_or_404, render
from .models import Item, Category


def item_list(request):
    context = {'items': Item.objects.published().order_by('category')
                            .only('name', 'category', 'text'),
               'categories': Category.objects.all().order_by('-name')}
    return render(request,
                  template_name='pages/catalog/main.html',
                  context=context)


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {'item': item}
    return render(request,
                  template_name='pages/catalog/item_detail.html',
                  context=context)
