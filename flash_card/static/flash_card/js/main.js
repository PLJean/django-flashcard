var empty_card = null;
var card_counter = 0;

function setEmptyCard(index) {
    console.log('Setting up empty card.');
    empty_card = $('.row.card').eq(index);
    empty_card.attr('id', 'empty_card');
    // console.log(empty_card);
}

function setCardCounter(num) {
    card_counter = num;
}

function newCard() {

    // Subtract one from card_count because of empty card template
    // console.log(card_count);
    var new_card = empty_card.clone();
    console.log(new_card);
    // remove empty_row attribute
    new_card.removeAttr('id');

    // add new_row attribute
    new_card.attr('class', 'row card container-fluid new_row');

    // Changing card counter
    var counter = new_card.find('.counter');
    var card_count = $('.row.card').length - 1;
    card_count += 1;
    counter.html(card_count);

    // Changing card front id and nameE
    var front = new_card.find('#id_form-0-front');
    front.attr('id',   'id_form-' + card_count + '-front');
    front.attr('name', 'form-' + card_count + '-front');
    console.log(front.attr('id'));
    console.log(front.attr('name'));

    // Changing card back id and name
    var back = new_card.find('#id_form-0-back');
    back.attr('id',   'id_form-' + card_count + '-back');
    back.attr('name', 'form-' + card_count + '-back');
    console.log(back.attr('id'));
    console.log(back.attr('name'));
    $('#set-formset').append(new_card[0].outerHTML);
}

function deleteCard(event) {
    var target = event.target || event.srcElement;
    target.parentElement.parentElement.remove();
}
