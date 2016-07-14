from django.http import HttpResponse
from django.contrib import messages
from .models import Set, Card
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
    # if len(current_cards) == 0:

    # logger.info(msg='sup')
    current_set_id = set_id

    return render(request, 'flash_card/set.html', {'set_id': set_id, 'all_sets': all_sets, 'cards': current_cards})


# def create_set(request):
#     # todo set creation
#     Set.objects.create()
#
#     edit_set(request)


def edit_set(request, set_id):
    global all_sets, current_cards, current_set_id
    CardFormSet = formset_factory(CardForm)
    extra_rows = 1
    initial_data = {
        'form-TOTAL_FORMS': len(current_cards) + extra_rows,
        'form-INITIAL_FORMS': len(current_cards),
        'form-MAX_NUM_FORMS': '',
    }

    for i in range(initial_data['form-TOTAL_FORMS'] - extra_rows):
        front_string = 'form-' + str(i) + '-front'
        back_string = 'form-' + str(i) + '-back'
        initial_data[front_string] = current_cards[i].front
        initial_data[back_string] = current_cards[i].back

    formset = CardFormSet(initial_data)
    # formset.is_valid()
    return render(request, 'flash_card/edit.html', {
        'all_sets': all_sets, 'cards': current_cards, 'set_id': current_set_id, 'formset': formset,
    })


def save_set(request, set_id):
    if request.method == 'POST':
        # Set.objects.get(id=set_id).card_set.all().delete()
        flash_cards = Set.objects.get(id=set_id)
        flash_cards.card_set.all().delete()
        # print(request.POST['form-0-front'])
        print(flash_cards.card_set.all())
        i = 0
        while True:
            form_front_string = 'form-' + str(i) + '-front'
            form_back_string = 'form-' + str(i) + '-back'
            if form_front_string not in request.POST or form_back_string not in request.POST:
                break
            if request.POST[form_front_string] != '' and request.POST[form_back_string] != '':
                Card.objects.create(
                    front=request.POST[form_front_string],
                    back=request.POST[form_back_string],
                    set_id=set_id
                )
            i += 1
        # print(set.card_set.all())

    return show_set(request, set_id)

