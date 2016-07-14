from django import forms

from .models import Set, Card


class CardForm(forms.ModelForm):
    front = forms.CharField(widget=forms.TextInput, label='')
    back = forms.CharField(widget=forms.TextInput, label='')

    class Meta:
        model = Card
        fields = ['front', 'back']


