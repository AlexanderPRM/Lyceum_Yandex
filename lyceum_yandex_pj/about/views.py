from django.shortcuts import render
from django.http import HttpResponse


def description(request):
    context = {}
    return render(request, template_name='pages/about/main.html', context=context)
