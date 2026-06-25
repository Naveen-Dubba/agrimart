import os
import glob

auth_js_content = """
document.addEventListener('DOMContentLoaded', () => {
    const userStr = localStorage.getItem('user');
    if (userStr) {
        try {
            const user = JSON.parse(userStr);
            const accountLinks = document.querySelectorAll('a[href="login.html"]');
            accountLinks.forEach(link => {
                const spans = link.querySelectorAll('span');
                if (spans.length >= 2) {
                    spans[0].textContent = 'Welcome,';
                    spans[1].textContent = user.name;
                    link.href = '#'; 
                    link.addEventListener('click', (e) => {
                        e.preventDefault();
                        if (confirm('Do you want to logout?')) {
                            localStorage.removeItem('user');
                            window.location.reload();
                        }
                    });
                }
            });
        } catch (e) {}
    }
});
"""

register_html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register - Agrimart</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script>
        tailwind.config = { theme: { extend: { colors: { agrigreen: '#406b03', agrilight: '#6aaf08', } } } }
    </script>
</head>
<body class="bg-gray-50 text-gray-800 font-sans smooth-scroll pt-32 flex flex-col min-h-screen">

    <header class="fixed top-0 w-full z-50 bg-white shadow-sm border-t-4 border-agrigreen">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
            <div class="flex items-center justify-between">
                <a href="index.html" class="flex flex-col">
                    <span class="text-3xl font-extrabold text-agrigreen flex items-center gap-2">
                        <i class="fa-solid fa-leaf"></i> AGRIMART
                    </span>
                    <span class="text-xs text-gray-500 font-semibold tracking-wide">Farm Equipment | Green Care | Services</span>
                </a>
                <div class="flex items-center space-x-6">
                    <a href="login.html" class="flex items-center gap-2 cursor-pointer text-agrigreen transition">
                        <div class="bg-gray-100 p-3 rounded-full text-agrigreen"><i class="fa-solid fa-user"></i></div>
                        <div class="hidden sm:block">
                            <span class="text-sm text-gray-500 block">Account</span>
                            <span class="font-bold">Sign In</span>
                        </div>
                    </a>
                </div>
            </div>
        </div>
    </header>

    <main class="flex-1 max-w-md mx-auto px-4 py-12 w-full">
        <div class="bg-white p-8 rounded-xl shadow-md border border-gray-200">
            <h2 class="text-3xl font-bold text-center text-gray-800 mb-6">Create Account</h2>
            <form id="registerForm">
                <div class="mb-4">
                    <label class="block text-sm font-medium text-gray-700 mb-1">Full Name</label>
                    <input type="text" id="name" required class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-agrigreen focus:ring-1 focus:ring-agrigreen" placeholder="John Doe">
                </div>
                <div class="mb-4">
                    <label class="block text-sm font-medium text-gray-700 mb-1">Email Address</label>
                    <input type="email" id="email" required class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-agrigreen focus:ring-1 focus:ring-agrigreen" placeholder="farmer@example.com">
                </div>
                <div class="mb-6">
                    <label class="block text-sm font-medium text-gray-700 mb-1">Password</label>
                    <input type="password" id="password" required class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-agrigreen focus:ring-1 focus:ring-agrigreen" placeholder="********">
                </div>
                <button type="submit" class="w-full bg-agrigreen text-white font-bold py-3 rounded-md hover:bg-green-800 transition">Register</button>
                <div id="registerError" class="text-red-500 text-sm mt-2 hidden"></div>
            </form>
            <p class="mt-4 text-center text-sm text-gray-600">Already have an account? <a href="login.html" class="text-agrigreen font-bold hover:underline">Sign in here</a></p>
        </div>
    </main>

    <footer class="bg-gray-900 text-gray-400 py-12 mt-auto">
        <div class="max-w-7xl mx-auto px-4 text-center">
            <h2 class="text-2xl font-bold text-white mb-4">Agrimart</h2>
            <p>&copy; 2026 Agrimart. All rights reserved.</p>
        </div>
    </footer>
    
    <script>
        document.getElementById('registerForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            try {
                const res = await fetch('/api/auth/register', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ name, email, password })
                });
                const data = await res.json();
                if (res.ok) {
                    localStorage.setItem('user', JSON.stringify(data));
                    window.location.href = 'index.html';
                } else {
                    const errDiv = document.getElementById('registerError');
                    errDiv.textContent = data.error || 'Registration failed';
                    errDiv.classList.remove('hidden');
                }
            } catch (err) {
                console.error(err);
            }
        });
    </script>
</body>
</html>
"""

# 1. Write auth.js
with open('auth.js', 'w', encoding='utf-8') as f:
    f.write(auth_js_content)

# 2. Write register.html
with open('register.html', 'w', encoding='utf-8') as f:
    f.write(register_html_content)

# 3. Update all html files to include auth.js before </body>
for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'auth.js' not in content:
        content = content.replace('</body>', '<script src="auth.js"></script>\n</body>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

# 4. Update login.html specifically for actual login
with open('login.html', 'r', encoding='utf-8') as f:
    login_content = f.read()

# Replace the form part
old_form = '<form onsubmit="event.preventDefault(); window.location.href=\'index.html\';">'
new_form = '''<form id="loginForm">
                <div class="mb-4">
                    <label class="block text-sm font-medium text-gray-700 mb-1">Email Address</label>
                    <input type="email" id="email" required class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-agrigreen focus:ring-1 focus:ring-agrigreen" placeholder="farmer@example.com">
                </div>
                <div class="mb-6">
                    <label class="block text-sm font-medium text-gray-700 mb-1">Password</label>
                    <input type="password" id="password" required class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-agrigreen focus:ring-1 focus:ring-agrigreen" placeholder="********">
                </div>
                <button type="submit" class="w-full bg-agrigreen text-white font-bold py-3 rounded-md hover:bg-green-800 transition">Sign In</button>
                <div id="loginError" class="text-red-500 text-sm mt-2 hidden"></div>
            </form>
            <script>
                document.getElementById('loginForm').addEventListener('submit', async (e) => {
                    e.preventDefault();
                    const email = document.getElementById('email').value;
                    const password = document.getElementById('password').value;
                    try {
                        const res = await fetch('/api/auth/login', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ email, password })
                        });
                        const data = await res.json();
                        if (res.ok) {
                            localStorage.setItem('user', JSON.stringify(data));
                            window.location.href = 'index.html';
                        } else {
                            const errDiv = document.getElementById('loginError');
                            errDiv.textContent = data.error || 'Login failed';
                            errDiv.classList.remove('hidden');
                        }
                    } catch (err) {
                        console.error(err);
                    }
                });
            </script>'''

# Also change 'Register here' link
old_link = 'href="#" class="text-agrigreen font-bold hover:underline">Register here'
new_link = 'href="register.html" class="text-agrigreen font-bold hover:underline">Register here'

import re
# We need to replace the form content up to the submit button
# Actually, the string replacement above might fail if the form content is slightly different.
# Let's do a regex replacement for the entire form element.
login_content = re.sub(r'<form onsubmit=.*?</form>', new_form, login_content, flags=re.DOTALL)
login_content = login_content.replace(old_link, new_link)

with open('login.html', 'w', encoding='utf-8') as f:
    f.write(login_content)

print("Setup complete")
