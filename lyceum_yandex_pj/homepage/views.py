from django.shortcuts import render


def home(request):
    context = {}
    return render(request,
                  template_name='pages/homepage/main.html',
                  context=context)
