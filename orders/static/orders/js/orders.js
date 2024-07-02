// orders popup form 

function openPopup_orders() {
    document.getElementById("orders_popup_form").style.display = "block";
    document.getElementById("overlay_orders").style.display = "block";
}

function closePopup_orders() {
    document.getElementById("orders_popup_form").style.display = "none";
    document.getElementById("overlay_orders").style.display = "none";
}



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

// Selection Window account POP UP CODE

function openPopup_selection_order() {
    document.getElementById("selection_window_order").style.display = "block";
    document.getElementById("selection_window_order_overlay").style.display = "block";

}

function closePopup_selection_order() {
    document.getElementById("selection_window_order").style.display = "none";
    document.getElementById("selection_window_account_order").style.display = "none";
}