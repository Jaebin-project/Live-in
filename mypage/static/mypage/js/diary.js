$(document).ready(function(){
    $('.comment_page button').click(function(){
        $('.modal_back').css('display','block');
        $('.modal').css('display','block');
    });

    $('#close').click(function(){
        $('.modal_back').css('display','none');
        $('.modal').css('display','none');
    });
});