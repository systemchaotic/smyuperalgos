// main.js

document.addEventListener('DOMContentLoaded', (event) => {
    console.log('DOM fully loaded and parsed');
});

function login() {
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({username, password}),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = '/dashboard';
        } else {
            alert('Invalid username or password');
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function register() {
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({username, password}),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = '/login';
        } else {
            alert('Registration failed');
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}