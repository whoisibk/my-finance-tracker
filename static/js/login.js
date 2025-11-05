const loginTab = document.getElementById('login-tab');
const signupTab = document.getElementById('signup-tab');
const loginForm  = document.getElementById('login-form');
const signupForm  = document.getElementById('signup-form');

//when login tab is clicked
loginTab.addEventListener('click', ()=>{
    loginTab.classList.add('active');
    loginForm.classList.add('active');
    signupTab.classList.remove('active');
    signupForm.classList.remove('active');
});

signupTab.addEventListener('click', ()=>{
    loginTab.classList.remove('active');
    loginForm.classList.remove('active');
    signupTab.classList.add('active');
    signupForm.classList.add('active');
});

// Wait for the document to be fully loaded
document.addEventListener("DOMContentLoaded", function() {

// --- Function to close an alert ---
function closeAlert(alert) {
    // 1. Start the fade-out by removing the 'show' class
    alert.classList.remove('show');

    // 2. Wait for the CSS transition to finish (500ms)
    //    Then, remove the alert from the page entirely.
    alert.addEventListener('transitionend', function() {
    alert.remove();
    });
}

// --- Part 1: Auto-fade alerts after 5 seconds ---
const autoFadeAlerts = document.querySelectorAll('.custom-alert.show');

autoFadeAlerts.forEach(function(alert) {
    setTimeout(function() {
    closeAlert(alert);
    }, 3500); // 
});

// --- Part 2: Allow closing by clicking the 'x' button ---
const closeButtons = document.querySelectorAll('.close-btn');

closeButtons.forEach(function(button) {
    button.addEventListener('click', function(event) {
    // Get the parent alert (the div.custom-alert)
    const alertToClose = event.target.closest('.custom-alert');
    if (alertToClose) {
        closeAlert(alertToClose);
    }
    });
});

});
