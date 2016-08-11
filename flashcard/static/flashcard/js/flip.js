$(function($) {
  $("#card").flip();
});

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
