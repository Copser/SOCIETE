function init_reviews() {
    $('.review_container .on_map_review').on('mousedown', function() {
        if (screen && screen.width > 800) {
            $('.review_container .on_map_review').css("z-index", 3);
            $(this).css("z-index", 4);
            //$(this).detach().insertAfter('.review_container .on_map_review:last');
        }
    });
}
