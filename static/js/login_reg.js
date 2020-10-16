$(document).ready(function(){
    $('#create').prop('disabled', true)
    $('.detail').hide()
    $('.detail-tag').click(function() {
        $('.detail').toggle()
    })
    $('.detail2').hide()
    $('.detail-tag2').click(function() {
        $('.detail2').toggle()
    })

    $(document).on('input', '#first_name', function(){
        var data = $('#reg_form').serialize()
        $.ajax({
            method: "POST",
            url: "/nameFormat/first_name/",
            data: data
        }).done(function(res) {
            $('#first_name_msg').html(res)
        })
    });
    $('#first_name').focusout(function(){
        var data = $('#reg_form').serialize()
        $.ajax({
            method: "POST",
            url: "/nameFormat/first_name/",
            data: data
        }).done(function(res) {
            $('#first_name_msg').html(res)
        })
    });
    $(document).on('input', '#last_name', function(){
        var data = $('#reg_form').serialize()
        $.ajax({
            method: "POST",
            url: "/nameFormat/last_name/",
            data: data
        }).done(function(res) {
            $('#last_name_msg').html(res)
        })
    });
    $('#last_name').focusout(function(){
        var data = $('#reg_form').serialize()
        $.ajax({
            method: "POST",
            url: "/nameFormat/last_name/",
            data: data
        }).done(function(res) {
            $('#last_name_msg').html(res)
        })
    });

    $(document).on('input', '#email', function(){
        var data = $('#reg_form').serialize()
        $.ajax({
            method: "POST",
            url:"/emailCheck/",
            data: data
        })
        .done(function(res){
            $('#email_msg').html(res)
        })
    })
    $('#email').focusout(function(){
        var data = $('#reg_form').serialize()
        $.ajax({
            method: "POST",
            url: "/emailCheck/",
            data: data
        }).done(function(res) {
            $('#email_msg').html(res)
        })
    });
    $(document).on('input', '#user_id', function(){
        var data = $('#reg_form').serialize()
        $.ajax({
            method: "POST",
            url:"/userIdCheck/",
            data: data
        })
        .done(function(res){
            $('#user_id_msg').html(res)
        })
    })
    $('#user_id').focusout(function(){
        var data = $('#reg_form').serialize()
        $.ajax({
            method: "POST",
            url: "/userIdCheck/",
            data: data
        }).done(function(res) {
            $('#user_id_msg').html(res)
        })
    });
    $(document).on('input', '#password', function(){
        var data = $('#reg_form').serialize()
        $.ajax({
            method: "POST",
            url:"/passwordCheck/",
            data: data
        })
        .done(function(res){
            $('#password_msg').html(res)
        })
    })
    $('#password').focusout(function(){
        var data = $('#reg_form').serialize()
        $.ajax({
            method: "POST",
            url: "/passwordCheck/",
            data: data
        }).done(function(res) {
            $('#password_msg').html(res)
        })
    });
    $(document).on('input', '#confirm', function() {
        $('#create').prop('disabled', false)
    });
    $('#login_id').focusout(function(){
        var data = $('#login_form').serialize()
        $.ajax({
            method: "POST",
            url: "/loginIdCheck/",
            data: data
        }).done(function(res) {
            $('#login_id_msg').html(res)
        })
    });
    $('.btn-nav').click(function() {
        history.back()
    })
    $('.btn-refresh').click(function() {
        location.reload()
    })
})