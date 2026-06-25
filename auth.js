
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
