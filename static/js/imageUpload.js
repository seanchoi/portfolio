$(document).ready(function() {

$(".upload_images_ajax").click(function () {
    $("#fileupload").click();
  });

$("#fileupload").fileupload({
    dataType: 'json',
    done: function (e, data) {
        var imgLimit = 4
        var imgCount = $('.upload_img_circle').length;
        if (imgCount < imgLimit){  
            if (data.result.is_valid) {
            $(".upload_img-wrap").prepend(
            "<div class='upload_img_circle'><img class='upload_img' src='" + data.result.url + "'></div>"
            )
        }
    }
}
})

$('.clear_images').click(function(){
    clearThumbnails(this);
});
function clearThumbnails(self) {
    $.ajax({
        method: "GET",
        url: $(self).prev().attr('value'),
    }).done(function(){        
        $('.upload_img-wrap').empty()        
    })
}

// slider
var slideCount = $('#slider .first_ul li').length;
var slideWidth = $('#slider .first_ul li').width();
var slideHeight = $('#slider .first_ul li').height();
var sliderUlWidth = slideCount * slideWidth;
$('#slider').css({ width: slideWidth, height: slideHeight });
$('#slider .first_ul').css({ width: sliderUlWidth, marginLeft: - slideWidth });
$('#slider .first_ul li:last-child').prependTo('#slider .first_ul');
function moveLeft() {
    $('#slider .first_ul').animate({
        left: + slideWidth
    }, 200, function () {
        $('#slider .first_ul li:last-child').prependTo('#slider .first_ul');
        $('#slider .first_ul').css('left', '');
    });
};

function moveRight() {
    $('#slider .first_ul').animate({
        left: - slideWidth
    }, 200, function () {
        $('#slider .first_ul li:first-child').appendTo('#slider .first_ul');
        $('#slider .first_ul').css('left', '');
    });
};
$('.control_prev').click(function () {
    moveLeft();
});
$('.control_next').click(function () {
    moveRight();
});

})