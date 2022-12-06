from django import forms
from catalog.models import Item

from rating.models import ItemRating


class RateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    def save(self, user, item):
        rating = self.cleaned_data["rate"]
        rate = ItemRating.objects.filter(user=user, item=item)
        if rate:
            rate.update(rate=rating)
        else:
            item = Item.objects.get(id=item)
            ItemRating.objects.create(user=user, rate=rating, item=item)

    class Meta:
        model = ItemRating
        fields = ("rate",)
        help_texts = {
            "rate": "выберите оценку",
        }
