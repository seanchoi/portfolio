$('.modal-background').hide()

$('.contact').click(function(){
    $('.modal-background').show()
})
$('.dm-cancel').click(function(){
    $('.modal-background').hide()
    location.reload()
})