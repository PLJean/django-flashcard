function newCard() {
    var empty_card = $('#empty_row').clone();
    empty_card.attr('id', 'new_row');
    $('#set-formset').append(empty_card[0].outerHTML);
}
