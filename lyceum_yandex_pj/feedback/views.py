from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect

from feedback.forms import FeedBackForm


def feedback(request):
    form = FeedBackForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST' and form.is_valid():
        text = form.cleaned_data['text']
        mail = form.cleaned_data['mail']
        send_mail(
            'Здравствуйте, админ. Вам пришла обратная связь.',
            text,
            mail,
            ['nathan920@yandex.ru'],
            fail_silently=True
        )
        form.save()
        messages.success(request, 'Сообщение отправлено,'
                                  'мы вас очень ценим(нет)')
        return redirect('feedback:feedback')
    return render(
        request,
        template_name='pages/feedback.html',
        context=context
        )
