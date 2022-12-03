from django.shortcuts import render
from feedback.forms import FeedBackForm
from django.core.mail import send_mail
from django.shortcuts import redirect


def feedback(request):
    email = request.user.email
    print(email)
    if request.user.is_authenticated:
        form = FeedBackForm(request.POST or None, mail=email)
    else:
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
            fail_silently=False
        )
        form.save()
        return redirect('feedback:feedback')
    return render(
                request,
                template_name='pages/feedback.html',
                context=context)
