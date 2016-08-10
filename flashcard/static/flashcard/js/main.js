$(document).ready(function () {
    var empty_card = null;
    var empty_card_index = 0;
    $(document).on('click', '.delete-card-btn', function() {
        var delCard = $(this).parent();
        console.log(delCard);
        var delCounter = delCard.find('.counter');
        var allCards = $('.card');

        // Loop through cards after deleted card, and renumber the html within the counter class div (old - 1)
        for (var i = parseInt(delCounter.eq(0).html()) + 1; i < allCards.length; i++) {
            var oldCounter = allCards.eq(i).find('.counter').eq(0);
            var newNum = parseInt(oldCounter.html()) - 1;
            oldCounter.html('' + newNum);
        }

        delCard.remove();
    });
    
    $(document).on('click', 'delete-set-btn', function() {
        var delSet = $(this).parent();
        console.log(delSet);
    })
});

function setEmptyCard(index) {
    console.log('Setting up empty card.');
    empty_card = $('.card').eq(index);
    empty_card.attr('id', 'empty_card');
    // console.log(empty_card);
}

function newCard() {

    // Subtract one from card_count because of empty card template
    // console.log(card_count);
    var new_card = empty_card.clone();
    console.log(new_card);
    // remove empty_row attribute
    new_card.removeAttr('id');

    // add new_row attribute
    // new_card.attr('class', 'row card container-fluid new_row');

    // Changing card counter
    var counter = new_card.find('.counter');
    var card_count = $('.card').length - 1;
    card_count += 1;
    counter.html(card_count);

    // Changing card front id and name
    var front = new_card.find('#id_form-0-front');
    front.attr('id',   'id_form-' + card_count + '-front');
    front.attr('name', 'form-' + card_count + '-front');
    // console.log(front.attr('id'));
    // console.log(front.attr('name'));

    // Changing card back id and name
    var back = new_card.find('#id_form-0-back');
    back.attr('id',   'id_form-' + card_count + '-back');
    back.attr('name', 'form-' + card_count + '-back');
    // console.log(back.attr('id'));
    // console.log(back.attr('name'));
    $('#set-formset').append(new_card[0].outerHTML);
}

function shuffleArray(array) {
    for (var i = array.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
    return array;
}

function playFlip(cards) {
    // Remove empty card from cards list
    var empty_card = cards.splice(0, 1);
    current_index = 1;
    // Shuffle array
    cards = shuffleArray(cards);

    // Add empty card back to the original list
    cards.unshift(empty_card);
    current_cards = cards;
    $('#front-content').html(current_cards[1]['fields']['front']);
    $('#back-content').html(current_cards[1]['fields']['back']);
    $('#card-index').html(current_index + " of " + (current_cards.length - 1));
}

function prevFlip() {
    // Decrease index if in range
    if (current_index > 1)
        current_index -= 1;

    // Reset if the index is out of range
    if (current_index < 1)
        current_index = 1;

    else if (current_index > current_cards.length - 1)
        current_index = current_cards.length - 1;

    console.log(current_index);
    $('#front-content').html(current_cards[current_index]['fields']['front']);
    $('#back-content').html(current_cards[current_index]['fields']['back']);
    $('#card-index').html(current_index + " of " + (current_cards.length - 1));
}

function nextFlip() {
    // Increase index if in range
    if (current_index < current_cards.length - 1)
        current_index += 1;

    // Reset if the index is out of range
    if (current_index < 1)
        current_index = 1;

    else if (current_index > current_cards.length - 1)
        current_index = current_cards.length - 1;

    console.log(current_index);
    $('#front-content').html(current_cards[current_index]['fields']['front']);
    $('#back-content').html(current_cards[current_index]['fields']['back']);
    $('#card-index').html(current_index + " of " + (current_cards.length - 1));
}


