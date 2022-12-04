from django.views.generic.edit import FormView
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse_lazy

from feedback.forms import FeedBackForm


class FeedbackPage(FormView):
    template_name = 'pages/feedback.html'
    form_class = FeedBackForm
    success_url = reverse_lazy('feedback:feedback')

    def form_valid(self, form):
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
        messages.success(
            self.request, 'Сообщение отправлено,'
            'мы вас очень ценим(нет)')
        return super(FeedbackPage, self).form_valid(form)
