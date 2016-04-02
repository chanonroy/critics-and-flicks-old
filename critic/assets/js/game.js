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

// ------------------ Stop Carousel -------------------------------------

$('.bar').hover(
  function() {
    $(this).addClass("bar-roll");
  },
  function() {
    $(this).removeClass("bar-roll");
  }
);

$('.bar').on("click",
  function() {
    $('.bar .bar-on').removeClass("bar-on");
  },
  function() {
    $(this).addClass("bar-on");
  }
);
