document.addEventListener('DOMContentLoaded', function() {
    function filterStatus(status) {
        const cards = document.querySelectorAll('.card');
        cards.forEach(card => {
            const statusText = card.querySelector('.status-text').textContent;
            if (statusText === status || status === 'All') {
                card.style.display = 'flex';
            } else {
                card.style.display = 'none';
            }
        });
    }

    function searchProject() {
        const searchInput = document.getElementById('search-input').value.toLowerCase();
        const cards = document.querySelectorAll('.card');
        cards.forEach(card => {
            const projectTitle = card.querySelector('h2').textContent.toLowerCase();
            if (projectTitle.includes(searchInput)) {
                card.style.display = 'flex';
            } else {
                card.style.display = 'none';
            }
        });
        return false;
    }

    function loadMoreProjects() {
        alert('Load more projects...');
    }

    document.getElementById('load-more-btn').addEventListener('click', loadMoreProjects);

    document.querySelector('.form-inline').addEventListener('submit', function(event) {
        event.preventDefault();
        searchProject();
    });

    window.filterStatus = filterStatus;
    window.searchProject = searchProject;
});