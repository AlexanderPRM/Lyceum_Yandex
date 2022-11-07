from django.http import HttpResponse
from django.shortcuts import render


def item_list(request):
    context = {}
    return render(request,
                  template_name='pages/catalog/main.html',
                  context=context)


def item_detail(request, pk):
    return HttpResponse('Подробнее о элементе {}'. format(pk))
