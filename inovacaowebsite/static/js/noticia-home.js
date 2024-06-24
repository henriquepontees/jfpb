function verMais(button) {
    const cardText = button.previousElementSibling;
    if (cardText.style.display === '-webkit-box') {
        cardText.style.display = 'block';
        button.textContent = 'Ver menos';
    } else {
        cardText.style.display = '-webkit-box';
        button.textContent = 'Ver mais...';
    }
}

document.addEventListener("DOMContentLoaded", function() {
    const truncatedElements = document.querySelectorAll('.truncated');
    truncatedElements.forEach(element => {
        const fullText = element.textContent;
        element.style.display = '-webkit-box';  // Ensure it starts in truncated mode
        if (element.scrollHeight > element.clientHeight) {
            element.nextElementSibling.classList.remove('hiddenn');
        } else {
            element.style.display = 'block';  // Show full text if it fits
        }
    });
});