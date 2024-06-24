document.getElementById('contactForm').addEventListener('enviar', function(event) {
    var email = document.getElementById('email').value;
    var errorMessage = document.getElementById('error-message');
    var modal = document.getElementById('confirmationModal');
    var confirmButton = document.getElementById('confirmButton');
    var cancelButton = document.getElementById('cancelButton');

    if (!email) {
        errorMessage.style.display = 'block';
        event.preventDefault();
    } else {
        errorMessage.style.display = 'none';
        event.preventDefault();
        modal.style.display = 'block';
    }

    confirmButton.addEventListener('click', function() {
        modal.style.display = 'none';
        console.log(document.getElementById('contactForm'));
        document.getElementById('contactForm').submit();
    });

    cancelButton.addEventListener('click', function() {
        modal.style.display = 'none';
    });
});