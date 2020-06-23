$(document).ready(function(){
    $('.food_list button').mouseover(function(){
        $(this).css('background-color','#fff');
        $(this).css('color','#8dc4d8');
    });

    $('.food_list button').mouseleave(function(){
        $(this).css('background-color','transparent');
        $(this).css('color','#fff');
    });

    $('#submit').click(function(){
        var rbc = $('input#rbc').val();
        var pt = $('input#pt').val();
        var wbc = $('input#wbc').val();

        $('.modal_back').css('display','block');

        if(rbc<500||pt<20000||wbc<20000){
            $('.modal3').css('display','block');
        }else if(rbc<1000||pt<50000||wbc<60000){
            $('.modal2').css('display','block');
        }else{
            $('.modal1').css('display','block');
        }
    });

    $('.close').click(function(){
        $('.modal_back').css('display','none');
        $('.modal1').css('display','none');
        $('.modal2').css('display','none');
        $('.modal3').css('display','none');
    });
});