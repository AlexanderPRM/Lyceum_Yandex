from django.shortcuts import render


def description(request):
    context = {}
    return render(request,
                  template_name='pages/about/main.html',
                  context=context)
