var cardTemplate = '<div class="container-fluid">' +
    '<div class="row card">' +
    '<div id="card-content">' +
    '<div class="col-lg-1 counter">{{ forloop.counter }}</div>' +
    '<div class="col-lg-5"><input type="text"</div>' +
    '<div class="col-lg-5"> <input type="text"">' +
    '</div></div></div></div>';


function toggleList() {
    $('#set_list').css('display', 'block');
    $('#set_form').css('display', 'none');
}

function toggleForm() {
    $('#set_list').css('display', 'none');
    $('#set_form').css('display', 'block');
}

function newRow() {
    $('.container-form').append(cardTemplate);
}