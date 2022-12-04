from django import forms

from rating.models import ItemRating


class RateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.mail = kwargs.pop('mail', None)
        self.text = kwargs.pop('text', None)
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = ItemRating
        fields = ('rate', )
        help_texts = {
            'rate': 'выберите оценку',
        }
