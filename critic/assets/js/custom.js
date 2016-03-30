// ------------------ Nav Bar Fix After Scroll -------------------------

$(window).scroll(function() {
    if ($(window).scrollTop() > 150 ){
        $('.navbar-fixed-top').addClass('show');
    } else {
        $('.navbar-fixed-top').removeClass('show');
    }
});

// ------------------ Stop Carousel -------------------------------------

$(document).ready(function() {
    //Set the carousel options
    $('#quote-carousel').carousel({
        pause: true,
        interval: false
    });
});

// ------------------ Navigation Bar (Smooth Scroll) -------------------------
$(function() {
    $('a[href*="#"]:not([href="#"])').click(function() {
        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
            if (target.length) {
                $('html, body').animate({
                    scrollTop: target.offset().top
                }, 1000);
                return false;
            }
        }
    });
});