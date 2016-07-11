from django.forms import ModelForm

from .models import Set, Card


class CardForm(ModelForm):

    class Meta:
        model = Card
        fields = ['front', 'back']


