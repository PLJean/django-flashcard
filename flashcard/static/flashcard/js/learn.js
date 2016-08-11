var current_cards = null;
var current_index = 1;
var incorrect;
var correct;

// Adds ability to press enter to answer question
$('#answer-input').keypress(function(event) {
    if (event.which == 13) {
        answerLearn();
    }
});

// Adds ability to press enter to go to next question
$('#next-btn').keypress(function(event) {
    if (event.which == 13) {
        nextLearn();
    }
});

function playLearn(cards) {
    // Remove empty card from cards list
    var empty_card = cards.splice(0, 1);
    incorrect = 0;
    correct = 0;
    current_index = 1;
    // Shuffle array
    cards = shuffleArray(cards);

    // Add empty card back to the original list
    cards.unshift(empty_card);
    current_cards = cards;

    $('#word-container').html(current_cards[current_index]['fields']['back']);
    $('#remaining-count').html(current_cards.length - 1);
    $('#correct-count').html(0);
    $('#incorrect-count').html(0);
}

function answerLearn() {
    var result;
    var question = current_cards[current_index]['fields']['back'];
    var answer = current_cards[current_index]['fields']['front'];
    console.log("Question: " + question);
    console.log("Answer: " + answer);
    if($('#answer-input').val() == answer) {
        correct += 1;
        $('#correct-count').html(correct);
        $('#next-container').html('<a id="next-btn" class="btn btn-default" onclick="nextLearn()">Next</a>');
        result = 'CORRECT!';
    } else {
        incorrect += 1;
        $('#incorrect-count').html(incorrect);
        $('#next-container').html('<input id="correct-answer-input">');
        // $('#correct-answer-input').change(function () {
        //     console.log($(this).text());
        // });
        $('#correct-answer-input').bind('input', function () {
            console.log("Typed: " + $(this).val());
            if($(this).val() == answer) {
                nextLearn();
            }
        });
        result = 'Incorrect. Copy the answer below to continue.';
    }

    if (current_index < current_cards.length) {
        $('#result').html(result);
        $('#question').html('Q: ' + question);
        $('#correct-answer').html('A: ' + answer);
        $('#learn-container').hide();
        $('#result-container').show();
    }
}

function nextLearn() {
    console.log(current_index);
    if (current_index < current_cards.length - 1) {
        current_index += 1;
        var question = current_cards[current_index]['fields']['back'];
        $('#next-container').html('');
        $('#word-container').html(question);
        $('#answer-input').val('');
        $('#result-container').hide();
        $('#learn-container').show();
    } else {
        $('#result-container').hide();
        $('#score-container').hide();
        console.log("Correct: " + correct);
        console.log("Incorrect: " + incorrect);
        console.log("Length: " + current_cards.length);
        if (correct == current_cards.length - 1) {
            $('#info-end').html('Good job!');
        } else {
            $('#info-end').html('Keep trying!');
        }

        $('#correct-count-end').html('Correct: ' + correct);
        $('#incorrect-count-end').html('Incorrect: ' + incorrect);
        $('#next-container-end').html('<a id="redo-btn" class="btn btn-default" onclick="location.reload()">Redo</a>');
        $('#end-container').show();
    }

}