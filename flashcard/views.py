from .models import Set, Card
from django.shortcuts import render
from .forms import CardForm, SetForm
from django.forms import formset_factory
from django.core import serializers
from random import randrange
from django.http import HttpResponse


all_sets = {}
current_cards = {}
current_set_id = -1
empty_card_index = 0
admin = False

# Showing the page
def index(request):
    global all_sets
    all_sets = Set.objects.all()
    set_lens = []
    for set in all_sets:
        # Subtract one from the length for the empty card.
        set_lens.append(len(set.card_set.all()) - 1)

    return render(request, 'flashcard/index.html', {'all_sets' : all_sets, 'set_lens': set_lens, 'admin': admin})

# Flashcard set page
def show_set(request, set_id):
    global all_sets, current_cards, current_set_id
    set = Set.objects.get(id=set_id)
    current_cards = set.card_set.all()
    title = set.name

    current_set_id = set_id

    return render(request, 'flashcard/set.html', {
        'set_id': set_id, 'cards': current_cards, 'title': title, 'empty_card_index': 0, 'color': set.color, 'admin': admin
    })


def create_set(request):
    if admin is False:
        return HttpResponse('')

    def random_color():
        color = '%x' % randrange(16777215)
        c_len = len(color)
        if c_len < 6:
            color = '0' * (6- c_len) + color

        return color

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
    color = random_color()
    title_form = SetForm(initial={'name': '', 'color': color})

    return render(request, 'flashcard/edit.html', {
        'cards': current_cards, 'set_id': set_id, 'title_form': title_form, 'formset': formset,
        'empty_card_index': empty_card_index, 'create': 1, 'color': color, 'admin': admin
    })


def edit_set(request, set_id):
    global current_set_id
    if admin is False:
        return HttpResponse('')

    set = Set.objects.get(id=set_id)
    current_cards = set.card_set.all()
    card_form_set = formset_factory(CardForm)

    initial_data = {
        'form-TOTAL_FORMS': len(current_cards),
        'form-INITIAL_FORMS': len(current_cards),
        'form-MAX_NUM_FORMS': '',
        'form-0-front': '',
        'form-0-back': '',
    }

    for i in range(1, initial_data['form-TOTAL_FORMS']):
        front_string = 'form-' + str(i) + '-front'
        back_string = 'form-' + str(i) + '-back'
        initial_data[front_string] = current_cards[i].front
        initial_data[back_string] = current_cards[i].back

    formset = card_form_set(initial_data)
    title_form = SetForm(initial={'name': Set.objects.get(id=set_id).name, 'color': set.color})
    # formset.is_valid()
    return render(request, 'flashcard/edit.html', {
        'set_id': current_set_id, 'title_form': title_form, 'formset': formset,
        'empty_card_index': empty_card_index, 'create': 0, 'color': set.color, 'admin': admin
    })


def save_set(request, set_id, create):
    if request.method == 'POST':
        print("Create: ", type(create))
        # Check if create is 1 (create new set) or a 0 (edit an old set)
        if int(create):
            flashcards_data = Set.objects.create(
                name=request.POST['name'],
                color=request.POST['color'][1:]     # Removing the '#' from the beginning of the hex
            )
            set_id = flashcards_data.id

        else:
            print('Dropping old set')
            flashcards_data = Set.objects.get(id=set_id)
            flashcards_data.name = request.POST['name']
            flashcards_data.color = request.POST['color'][1:]   # Removing the '#' from the beginning of the hex
            flashcards_data.save()
            flashcards = flashcards_data.card_set.all()
            flashcards.delete()

        Card.objects.create(
            set_id=set_id,
            front='',
            back=''
        )
        print(flashcards_data.card_set.all())

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


def flip(request, set_id):
    flashcards = serializers.serialize("json", Set.objects.get(id=set_id).card_set.all())
    return render(request, 'flashcard/flip.html', {
        'cards': flashcards, 'set_id': set_id, 'admin': admin
    })


def learn(request, set_id):
    flashcards_data = Set.objects.get(id=set_id)
    flashcards = serializers.serialize("json", flashcards_data.card_set.all())
    return render(request, 'flashcard/learn.html', {
        'title': flashcards_data.name, 'cards': flashcards, 'set_id': set_id, 'admin': admin
    })


def export(request, set_id):
    flashcards_data = Set.objects.get(id=set_id)
    flashcards = flashcards_data.card_set.all()
    return render(request, 'flashcard/export.html', {
        'title': flashcards_data.name, 'cards': flashcards[1:], 'set_id': set_id, 'admin': admin
    })

