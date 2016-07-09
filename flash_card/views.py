from django.http import HttpResponse
from django.contrib import messages
from .models import Set
from django.shortcuts import render

all_sets = {}
current_cards = {}
current_set_id = -1


def index(request):
    global all_sets
    all_sets = get_all_sets(request)

    return render(request, 'flash_card/index.html', {'all_sets' : all_sets})

def get_all_sets(request):
    return Set.objects.all()

def show_set(request, set_id):
    global all_sets, current_cards, current_set_id
    current_cards = Set.objects.get(id=set_id).card_set.all()
    current_set_id = set_id

    return render(request, 'flash_card/set.html', {'set_id': set_id, 'all_sets': all_sets, 'cards': current_cards})

# def add_set(request):
#     # todo set creation
#     Set.objects.create()
#
#     edit_set(request)
#
# def edit_set(request):
#     global all_sets, current_cards, current_set_id
#     return render(request, 'flash_card/edit.html', {'all_sets': all_sets, 'cards': current_cards, 'set_id': current_set_id})
#
def save_set(request, set_id):
    return show_set(request, set_id)