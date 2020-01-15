(function ($) {
    $.fn.uniformHeight = function () {
        var maxHeight = 0,
            wrapper,
            wrapperHeight;

        return this.each(function () {

            // Applying a wrapper to the contents of the current element to get reliable height
            wrapper = $(this).wrapInner('<div class="wrapper" />').children('.wrapper');
            wrapperHeight = wrapper.outerHeight();

            maxHeight = Math.max(maxHeight, wrapperHeight);

            // Remove the wrapper
            wrapper.children().unwrap();

        }).height(maxHeight);
    }
})(jQuery);

$(function() {
    $('#movie').typeahead([
      {
        name: 'movies',
        remote: {
            url: '/api/search/%QUERY',
            maxParallelRequests: 6,
            rateLimitFn: 'throttle'
        },
        template: '<h4>{{value}} <small>({{year}})</h4>',
        engine: Hogan,
        limit: 10
      }
    ]);

    $('#movie').on('typeahead:selected', function (object, datum) {
       $('input[name=tmdb_id]').val(datum.id);

       $('#selected_movie').show('slow');
       $('#selected_movie_image').attr('src', datum.poster);
       $('#selected_movie_title').text(datum.value);
       $('#selected_movie_year').text(datum.year);
    });

    $('.thumbnail.grid').uniformHeight();

    $(window).resize(function () {
        $('.thumbnail.grid').uniformHeight();
    });
});

var add_movie_to_list = function(list_id, tmdb_id) {
    $("#lists_add_movie_" + tmdb_id + " #list_id").val(list_id);
    $("#lists_add_movie_" + tmdb_id).submit();
}
