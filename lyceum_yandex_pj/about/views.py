# from django.shortcuts import render
from django.http import HttpResponse


def description(request):
    return HttpResponse('О Проекте')
