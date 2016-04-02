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

// ------------------ Navigation Bar for Movies --------------------------

$('.bar').hover(
  function() {
    $(this).addClass("bar-roll");
  },
  function() {
    $(this).removeClass("bar-roll");
  }
  ).on("click", function() {
    $(this).addClass("bar-on");
    $(this).siblings().removeClass("bar-on");
    var panelId = $(this).attr('data-panelid');
  }
);
