from django import forms

from .models import Set, Card


class SetForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput, label='')

    class Meta:
        model = Set
        fields = ['name']


class CardForm(forms.ModelForm):
    front = forms.CharField(widget=forms.TextInput, label='')
    back = forms.CharField(widget=forms.TextInput, label='')

    class Meta:
        model = Card
        fields = ['front', 'back']


