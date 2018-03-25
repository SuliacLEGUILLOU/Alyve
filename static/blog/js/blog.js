$(document).ready(function() {
    
    $(window).scroll(function() {
        if($(window).scrollTop() >= 60) {
            $('a.navbar-brand').css('font-size', '1.5em');
        }
        else {
            $('a.navbar-brand').css('font-size', '3em');
        }
    })
    
    try {
        $('#modal-hidden-image').modal('show');

        document.querySelector('#hidden-image-display-all').addEventListener('click', function() {
            $('#modal-hidden-image').modal('hide');
            document.querySelectorAll('.hidden img').forEach(function(e) {
                e.style.display = "block"
            })
        })
    }
    catch(err) {}

})
