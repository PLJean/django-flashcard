from django import forms

from .models import Set, Card


class CardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ['front', 'back']


