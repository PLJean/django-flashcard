var empty_card = null;
var card_counter = 0;

$(document).on('click', '.delete-btn', function(e) {
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

function setEmptyCard(index) {
    console.log('Setting up empty card.');
    empty_card = $('.card').eq(index);
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

// function deleteCard(event) {
//     var deleteCard = $(this);
//
//     console.log(deleteCard.attr('class'));
//     deleteCard.remove();
//     var counter = deleteCard.find('.counter');
//     // console.log(counter);
//     var allCards = $('.row.card');
//     // console.log(allCards.length);
//     console.log(deleteCard);
//     for (var i = counter + 1; i < allCards.length; i++) {
//         console.log(i);
//         var counter = allCards.find('.counter');
//         console.log(counter);
//         counter.html(i - 1);
//     }
//
//     // $(this).parent().parent().remove();
//     console.log('Fin.');
// }
