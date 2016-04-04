// ------------------ Nav Bar Fix After Scroll -------------------------

$(window).scroll(function() {
    if ($(window).scrollTop() > 150 ){
        $('.navbar-fixed-top').addClass('show');
    } else {
        $('.navbar-fixed-top').removeClass('show');
    }
});

// ------------------ Stop Bootstrap Carousel --------------------------

$('#quote-carousel').carousel({
    pause: true,
    interval: false
});


$(document).ready(function () {
  $('#quote-carousel').find('.item').first().addClass('active');
});

// ---------------------- Flickity Carousel --------------------------

$('#slides').flickity({
  // options
  wrapAround: true,
  prevNextButtons: false,
});