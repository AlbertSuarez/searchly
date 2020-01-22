// Init
$('#error-message').hide();
$('#success-message').hide();
$('#card-result').hide();
$('.form #input-content').hide();

// Animations
$('#form-card').hide();
setTimeout(function() {$('#form-card').transition('scale');}, 250);

// Form retrieving
function getFieldValueInput(fieldId) {
    return $(".form input[name=" + fieldId + "]").val();
}

function getFieldValueCheckbox(fieldId) {
    return $(".form input[name=" + fieldId + "]").is(':checked');
}

function getFieldValueSelect(fieldId) {
    return $(".form select[name=" + fieldId + "]").val();
}

// Message
$('#error-message .close').on('click', function() {$('#error-message').transition('horizontal flip');})
$('#success-message .close').on('click', function() {$('#success-message').transition('horizontal flip');})

function showErrorMessage(message) {
    if ($('#success-message').is(":visible")) {
        $('#success-message').transition('horizontal flip');
    }
    $('.error-messsage-text').html(message);
    if ($('#error-message').is(":hidden")) {
        $('#error-message').transition('horizontal flip');
    }
}

function showSuccessMessage(message) {
    if ($('#error-message').is(":visible")) {
        $('#error-message').transition('horizontal flip');
    }
    $('.success-messsage-text').html(message);
    if ($('#success-message').is(":hidden")) {
        $('#success-message').transition('horizontal flip');
    }
}

// Checkbox
$('.form .checkbox').checkbox();
$('.form .checkbox').checkbox({
    onChecked: function () {
        if ($('#by-song').is(':checked')) {
            $('#input-content').hide();
            $('#input-song').show();
        } else {
            $('#input-song').hide();
            $('#input-content').show();
        }
    }
});

// Ajax
function callApi(endpoint, method, formData) {
    $('.form').addClass('loading');
    if (method == 'POST') {
        formData = JSON.stringify(formData);
    }
    $.ajax({
        type: method,
        url: endpoint,
        data: formData,
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(data) {
            $('#form-card').transition('scale');
            if (data.error) {
                showErrorMessage(data.message);
            } else {
                // Show result
            }
            setTimeout(function() {$('#card-result').transition('slide down');}, 500);
        },
        error: function() {
            showErrorMessage('Try again, please.');
        },
        complete: function() {
            $('.form').removeClass('loading');
        }
    });
}

// Form
$('.form button').on('click', function() {
    $('#error-message').hide();
    if ($('#by-song').is(':checked')) {
        bySong = getFieldValueInput('bySong')
        if (!bySong) {
            showErrorMessage('No song specified.');
        } else {
            formData = {'song_id': bySong};
            callApi('/api/v1/similarity/by_song', 'GET', formData);
        }
    } else {
        byContent = getFieldValueInput('byContent');
        if (!byContent) {
            showErrorMessage('No content specified.');
        } else {
            formData = {'content': byContent};
            callApi('/api/v1/similarity/by_content', 'POST', formData);
        }
    }
});

// Refresh button
$('.try-another-one').on('click', function() {
    location.reload();
});
