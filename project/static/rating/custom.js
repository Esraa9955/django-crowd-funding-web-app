// custom.js
$(document).ready(function() {
    $('.star-rating .star').on('click', function() {
        var rating = $(this).data('value');
        $('#rating-input').val(rating);
        $('.star-rating .star').removeClass('selected');
        $(this).addClass('selected').prevAll().addClass('selected');
    });
});
