from django.http import HttpResponse
# from django.shortcuts import render


def item_list(request):
    return HttpResponse('Список<br>Предметов')


def item_detail(request, pk):
    return HttpResponse('Подробнее о элементе {}'. format(pk))
