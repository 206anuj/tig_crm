document.addEventListener('DOMContentLoaded', function() {
    // Get the current URL path
    const currentPath = window.location.pathname.split('/').pop();

    // Select all nav links
    const navLinks = document.querySelectorAll('.nav_item');

    // Iterate over nav links and add the active class to the current link
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
});