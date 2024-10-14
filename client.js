// client.js
document.getElementById('home-button').addEventListener('click', () => window.location.href = '/');
document.getElementById('student-login').addEventListener('click', () => window.location.href = '/acadamy/acadamy.html');
document.getElementById('tutor-login').addEventListener('click', () => window.location.href = '/acadamy/acadamy.html');

function showLoginForm(role) {
    document.getElementById('student-login-form').style.display = role === 'student' ? 'block' : 'none';
    document.getElementById('tutor-login-form').style.display = role === 'tutor' ? 'block' : 'none';
    document.getElementById('student-registration-form').style.display = 'none';
    document.getElementById('tutor-registration-form').style.display = 'none';
}

function showRegistrationForm(role) {
    document.getElementById('student-login-form').style.display = 'none';
    document.getElementById('tutor-login-form').style.display = 'none';
    document.getElementById('student-registration-form').style.display = role === 'student' ? 'block' : 'none';
    document.getElementById('tutor-registration-form').style.display = role === 'tutor' ? 'block' : 'none';
}

function login(username, password, role) {
    fetch('/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password, role })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = data.redirect; // Redirect to the appropriate dashboard
        } else {
            alert(data.message);
        }
    });
}

function register(username, password, role) {
    fetch(`/register/${role}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        if (data.success) {
            showLoginForm(role); // Show login form after successful registration
        }
    });
}
