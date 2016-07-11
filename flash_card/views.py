from django.http import HttpResponse
from django.contrib import messages
from .models import Set
from django.shortcuts import render
from .forms import CardForm
from django.forms import formset_factory
import logging

# import django
# django.setup()

all_sets = {}
current_cards = {}
current_set_id = -1
# logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def index(request):
    global all_sets
    all_sets = get_all_sets(request)

    return render(request, 'flash_card/index.html', {'all_sets' : all_sets})


def get_all_sets(request):
    return Set.objects.all()


def show_set(request, set_id):
    global all_sets, current_cards, current_set_id
    current_cards = Set.objects.get(id=set_id).card_set.all()
    logger.info(msg='sup')
    current_set_id = set_id

    return render(request, 'flash_card/set.html', {'set_id': set_id, 'all_sets': all_sets, 'cards': current_cards})


# def add_set(request):
#     # todo set creation
#     Set.objects.create()
#
#     edit_set(request)


def edit_set(request, set_id):
    global all_sets, current_cards, current_set_id
    CardFormSet = formset_factory(CardForm)
    # for card in current_cards:

    initial_data = {
        'form-TOTAL_FORMS': len(current_cards),
        'form-INITIAL_FORMS': len(current_cards),
        'form-MAX_NUM_FORMS': '',
    }

    for i in range(initial_data['form-TOTAL_FORMS']):
        front_string = 'form-' + str(i) + '-front'
        back_string = 'form-' + str(i) + '-back'
        initial_data[front_string] = current_cards[i].front
        initial_data[back_string] = current_cards[i].back

    formset = CardFormSet(initial_data)

    return render(request, 'flash_card/edit.html', {'all_sets': all_sets, 'cards': current_cards, 'set_id': current_set_id, 'formset': formset})


def save_set(request, set_id):
    return show_set(request, set_id)