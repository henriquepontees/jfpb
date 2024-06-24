document.addEventListener("DOMContentLoaded", function() {
    var modal = document.getElementById("imageModal");
    var modalImg = document.getElementById("modalImage");
    var imgLinks = document.querySelectorAll(".image-link");
    var currentIndex = 0;

    function showModal(index) {
        var img = imgLinks[index].querySelector("img");
        modal.style.display = "block";
        modalImg.src = img.src;
    }

    imgLinks.forEach(function(link, index) {
        link.addEventListener("click", function(event) {
            event.preventDefault();
            currentIndex = index;
            showModal(currentIndex);
        });
    });

    var span = document.getElementsByClassName("close")[0];
    span.onclick = function() {
        modal.style.display = "none";
    };

    var next = document.getElementsByClassName("next")[0];
    var prev = document.getElementsByClassName("prev")[0];

    next.onclick = function() {
        currentIndex = (currentIndex + 1) % imgLinks.length;
        showModal(currentIndex);
    };

    prev.onclick = function() {
        currentIndex = (currentIndex - 1 + imgLinks.length) % imgLinks.length;
        showModal(currentIndex);
    };

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };
});
