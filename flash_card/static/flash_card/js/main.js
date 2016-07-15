function newCard() {
    // Subtract one from card_count because of empty card template
    var card_count = $('.row.card').length - 1;
    console.log(card_count);
    var empty_card = $('#empty_row').clone();

    // remove empty_row attribute
    empty_card.removeAttr('id');

    // add new_row attribute
    empty_card.attr('class', 'row card new_row');

    var counter = empty_card.find('.counter');
    counter.html(card_count + 1);
    $('#set-formset').append(empty_card[0].outerHTML);
}

function deleteCard(event) {
    var target = event.target || event.srcElement;
    target.parentElement.parentElement.remove();
}
