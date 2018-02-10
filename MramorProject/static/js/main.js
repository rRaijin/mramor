$(document).ready(function () {
    function heightFix() {
        $('.parallax-main-head').css('height', $(window).height());
    };

    heightFix();

    $(window).resize(function () {
        heightFix();
    });

    $('.header-slider').bxSlider({
        auto: true,
        controls: false,
        mode: 'fade',
        randomStart: true,
        pager: false,
    });

});


$(window).load(function() {
        $(".loaderInner").fadeOut();
        $(".loader").delay(600).fadeOut("slow");
    }
);