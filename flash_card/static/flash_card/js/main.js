function newCard() {
    var empty_card = $('#empty_row').clone();
    // remove empty_row attribute
    empty_card.removeAttr('id')
    // add new_row attribute
    empty_card.attr('class', 'row card new_row');
    $('#set-formset').append(empty_card[0].outerHTML);
}
