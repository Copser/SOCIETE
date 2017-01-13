$(document).ready(function(){

    $("#showlogin").click(function(){
        $("#loginModal").modal('show');
    });

    $('.thumb').hover(function(){
        $(this).find('.caption').css('opacity','1');
    }, function(){
        $(this).find('.caption').css('opacity','0');
    });

    $('.carousel').carousel({
        interval: 1800
    });

    $('img.lazy').lazyload();

    $('div.lazy').lazyload({
        effect : 'fadeIn'
    });
    
    $('select').select2();

});
