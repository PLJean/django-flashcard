from django.http import HttpResponse
from django.contrib import messages
from .models import Set, Card
from django.shortcuts import render
from .forms import CardForm, SetForm
from django.forms import formset_factory
import logging

# import django
# django.setup()

all_sets = {}
current_cards = {}
current_set_id = -1
empty_card_index = 0

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)


def index(request):
    global all_sets
    all_sets = get_all_sets(request)

    return render(request, 'flash_card/index.html', {'all_sets' : all_sets})


def get_all_sets(request):
    return Set.objects.all()


def show_set(request, set_id):
    global all_sets, current_cards, current_set_id
    set = Set.objects.get(id=set_id)
    current_cards = set.card_set.all()
    title = set.name
    # if len(current_cards) == 0:

    # logger.info(msg='sup')
    current_set_id = set_id

    return render(request, 'flash_card/set.html', {
        'set_id': set_id, 'all_sets': all_sets, 'cards': current_cards,
        'title': title, 'empty_card_index': 0
    })


def create_set(request):
    card_form_set = formset_factory(CardForm)

    # set_id set to 0 so save_set() will know that the set is brand new
    set_id = 0
    initial_data = {
        'form-TOTAL_FORMS': 6,
        'form-INITIAL_FORMS': 0,
        'form-MAX_FORMS': '',
        'form-0-front': '',
        'form-0-back': '',
    }

    formset = card_form_set(initial_data)
    title_form = SetForm(initial={'name': ''})

    return render(request, 'flash_card/edit.html', {
        'all_sets': all_sets, 'cards': current_cards, 'set_id': set_id,
        'title_form': title_form, 'formset': formset, 'empty_card_index': empty_card_index,
        'create': 1
    })


def edit_set(request, set_id):
    global all_sets, current_cards, current_set_id
    card_form_set = formset_factory(CardForm)

    initial_data = {
        'form-TOTAL_FORMS': len(current_cards),
        'form-INITIAL_FORMS': len(current_cards),
        'form-MAX_NUM_FORMS': '',
        'form-0-front': '',
        'form-0-back': '',
    }

    for i in range(1, initial_data['form-TOTAL_FORMS']):
        print(i)
        front_string = 'form-' + str(i) + '-front'
        back_string = 'form-' + str(i) + '-back'
        initial_data[front_string] = current_cards[i - 1].front
        initial_data[back_string] = current_cards[i - 1].back

    formset = card_form_set(initial_data)
    title_form = SetForm(initial={'name': Set.objects.get(id=set_id).name})
    # formset.is_valid()
    return render(request, 'flash_card/edit.html', {
        'all_sets': all_sets, 'cards': current_cards, 'set_id': current_set_id,
        'title_form': title_form, 'formset': formset, 'empty_card_index': empty_card_index,
        'create': 0
    })


def save_set(request, set_id, create):
    if request.method == 'POST':
        if create:
            flash_cards_data = Set.objects.create(
                name=request.POST['name']
            )
            set_id = flash_cards_data.id

        else:
            flash_cards_data = Set.objects.get(id=set_id)
            flash_cards = flash_cards_data.card_set.all()
            flash_cards.delete()

        flash_cards_data.name = request.POST['name']

        Card.objects.create(
            set_id=set_id,
            front='',
            back=''
        )
        print(flash_cards.card_set.all())

        i = 1
        while True:
            print(i)
            form_front_string = 'form-' + str(i) + '-front'
            form_back_string = 'form-' + str(i) + '-back'
            if form_front_string not in request.POST or form_back_string not in request.POST:
                break

            if request.POST[form_front_string] != '' and request.POST[form_back_string] != '':
                Card.objects.create(
                    set_id=set_id,
                    front=request.POST[form_front_string],
                    back=request.POST[form_back_string],
                )

            i += 1

    return show_set(request, set_id)
