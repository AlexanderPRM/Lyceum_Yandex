from django import forms
from .models import FeedBack
# from django.forms.widgets import EmailInput


class FeedBackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = FeedBack
        fields = ('text', 'mail')
        labels = {
                'mail': 'Ваша почта',
                'text': 'Содержимое обращения'}
        help_texts = {
            'text': 'В этом поле введите текст своего обращения.',
            'mail': 'Введите вашу почту.'
        }
        # widgets = {'text': forms.TextInput(attrs={'class': 'form-control'})}
