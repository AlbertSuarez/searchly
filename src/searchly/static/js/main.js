$(document).ready(function() {
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

    // Slick
    function enableSlick() {
        $('.single-item').slick({
            dots: true,
            infinite: true,
            autoplay: true,
            autoplaySpeed: 3000
        });
    }

    // Result
    function generateSimilarityResult(artist_name, song_name, artist_url, song_url, percentage) {
        return `<div>` +
            `<h2 class="ui header centered"><a href="${artist_url}" target="_blank">${artist_name}</a></h3>\n` +
            `<h3 class="ui header centered"><a href="${song_url}" target="_blank">${song_name}</a></h4>\n` +
            `<div class="ui horizontal statistics">` +
                `<div class="statistic"><div class="value">${percentage}</div><div class="label">%</div></div>` +
            `</div` +
        `</div>`
    }

    // Message
    $('#error-message .close').on('click', function() {$('#error-message').transition('horizontal flip');})
    $('#success-message .close').on('click', function() {$('#success-message').transition('horizontal flip');})

    function showErrorMessage(message) {
        if ($('#success-message').is(":visible")) {
            $('#success-message').transition('horizontal flip');
        }
        $('.error-message-text').html(message);
        if ($('#error-message').is(":hidden")) {
            $('#error-message').transition('horizontal flip');
        }
    }

    function showSuccessMessage(message) {
        if ($('#error-message').is(":visible")) {
            $('#error-message').transition('horizontal flip');
        }
        $('.success-message-text').html(message);
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

    // Dropdown
    $('#input-song .dropdown')
        .dropdown({
            apiSettings: {
                onResponse: function(apiResponse) {
                    var response = {success: !apiResponse.error, results: []};
                    if (response.success) {
                        $.each(apiResponse.response.results, function(index, item) {
                            response.results.push({
                                name: item.name,
                                value: item.id,
                                text: item.name
                            });
                        });
                    }
                    return response;
                },
                url: '/api/v1/song/search?query={query}'
            },
            minCharacters: 4,
            placeholder: 'Song and/or Artist name'
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
                if (data.error) {
                    showErrorMessage(data.message);
                } else {
                    $('#form-card').transition('scale');
                    $.each(data.response.similarity_list, function(x, i) {
                        divResult = generateSimilarityResult(i.artist_name, i.song_name, i.artist_url, i.song_url, i.percentage);
                        $('.single-item').slick('slickAdd', divResult);
                    });
                    setTimeout(function() {$('#card-result').transition('slide down');}, 500);
                }
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
            bySong = getFieldValueSelect('bySong')
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

    // Enable Slick
    enableSlick();
});