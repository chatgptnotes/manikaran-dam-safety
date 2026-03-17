/* ─── Navbar scroll effect ─── */
const navbar = document.getElementById('navbar');
if (navbar) {
    window.addEventListener('scroll', () => {
        navbar.classList.toggle('scrolled', window.scrollY > 40);
    });
}

/* ─── Mobile nav toggle ─── */
const toggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');
if (toggle && navLinks) {
    toggle.addEventListener('click', () => navLinks.classList.toggle('open'));
    navLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => navLinks.classList.remove('open'));
    });
}

/* ─── Scroll-triggered fade-in ─── */
const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.1 });
document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

/* ─── Contact form handler ─── */
const form = document.getElementById('enquiryForm');
const successBox = document.getElementById('formSuccess');
if (form) {
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const btn = form.querySelector('button[type="submit"]');
        btn.disabled = true;
        btn.textContent = 'Sending...';

        const data = Object.fromEntries(new FormData(form));
        try {
            const res = await fetch('/api/enquiry', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            const json = await res.json();
            if (json.success) {
                form.style.display = 'none';
                if (successBox) successBox.classList.add('show');
            } else {
                alert(json.error || 'Something went wrong. Please try again.');
            }
        } catch {
            alert('Network error. Please try again.');
        } finally {
            btn.disabled = false;
            btn.textContent = 'Send Enquiry';
        }
    });
}
