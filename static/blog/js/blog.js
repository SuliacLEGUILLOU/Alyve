$(document).ready(function() {
    
    $(window).scroll(function() {
        if($(window).scrollTop() >= 60) {
            $('a.navbar-brand').css('font-size', '1.5em');
        }
        else {
            $('a.navbar-brand').css('font-size', '3em');
        }
    })
})