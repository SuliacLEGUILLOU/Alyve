$(document).ready(function() {
    try {
        $('#modal-hidden-image').modal('show');

        $('#hidden-image-display-all').addEventListener('click', function() {
            $('#modal-hidden-image').modal('hide');
            $('.hidden img').forEach(function(e) {
                e.style.display = "block"
            })
        })
    }
    catch(err) {
        console.log(err)
    }

})
