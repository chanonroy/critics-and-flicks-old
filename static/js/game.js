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
  prevNextButtons: false
});

// TODO: find solution to stop the video
// $('.flickity-page-dots').click(function() {
//     $('.video').get(0).stopVideo();
// });

// ---------------------- Sweet JS --------------------------

document.querySelector('.real').onclick = function(){
	swal({
    type: "success",
    title: "Good Job!",
    text: 'You guessed the right movie.',
    animation: "slide-from-top",
    confirmButtonText: "Next"
}, function(){
    window.location.reload();
    // $.ajax({
    //     url: "",
    //     success: function(data) {
    //     $('#slides').html(data);
    //     }
    // });
    });
};
$('.blank').on('click', function(){
    swal({
    type: "error",
    title: "Oh No!",
    text: 'You guessed the wrong movie.',
    animation: "slide-from-top",
    confirmButtonText: "Next"
}, function(){
    window.location.reload();
    });
});