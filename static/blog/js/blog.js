(function() {

    try {
        if (contentWarning !== undefined) {
            alertify.confirm('Attention !', contentWarning.content, () => {
                document.querySelectorAll('.hidden img').forEach(e => { e.style.display = 'block' })
            }, () => {})
        }

        /*document.querySelector('#hidden-image-display-all').addEventListener('click', function() {
            let images = document.querySelectorAll('.hidden img')
            images.forEach(element => { element.style.display = 'block' });
        })*/
    }
    catch(err) {
    }

})()
