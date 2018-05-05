(function() {
    try {
        document.querySelector('#modal-hidden-image').modal('show');

        document.querySelector('#hidden-image-display-all').addEventListener('click', function() {
            document.querySelector('#modal-hidden-image').modal('hide');
            document.querySelectorAll('.hidden img').forEach(function(e) {
                e.style.display = "block"
            })
        })
    }
    catch(err) {}

})
