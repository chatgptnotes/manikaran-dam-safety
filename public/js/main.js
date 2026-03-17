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
    toggle.addEventListener('click', () => {
        navLinks.classList.toggle('open');
        toggle.classList.toggle('active');
    });
    navLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('open');
            toggle.classList.remove('active');
        });
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
        const origText = btn.innerHTML;
        btn.disabled = true;
        btn.innerHTML = '<span class="btn-spinner"></span> Sending...';

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
            btn.innerHTML = origText;
        }
    });
}

/* ─── AI-Powered Hero Content (Gemini) ─── */
const aiInsight = document.getElementById('aiInsight');
const aiFact = document.getElementById('aiFact');

if (aiInsight || aiFact) {
    // Fallback content pool
    const fallbackInsights = [
        'Where sensors meet safety — guarding India\'s lifelines.',
        'Every drop monitored. Every life protected.',
        'The silent digital guardians of a billion lives.',
        'Intelligence flows where water flows.',
        'Turning data streams into safe water streams.',
    ];
    const fallbackFacts = [
        'Less than 15% of India\'s 5,334 large dams have adequate safety instrumentation.',
        'Over 1,137 dams in India are more than 50 years old and lack continuous monitoring.',
        'The Dam Safety Act 2021 mandates real-time monitoring for every large dam in India.',
        'India\'s canal networks lose 35-45% of water before it reaches farmers.',
        '24/7 automated monitoring can detect anomalies days before they become critical.',
    ];

    let currentIdx = 0;

    function setContent(insight, fact) {
        if (aiInsight) {
            aiInsight.classList.remove('ai-text-visible');
            setTimeout(() => {
                aiInsight.textContent = insight;
                aiInsight.classList.add('ai-text-visible');
            }, 400);
        }
        if (aiFact) {
            aiFact.classList.remove('ai-text-visible');
            setTimeout(() => {
                aiFact.textContent = fact;
                aiFact.classList.add('ai-text-visible');
            }, 600);
        }
    }

    async function fetchAIContent() {
        try {
            const res = await fetch('/api/ai-hero');
            const data = await res.json();
            if (data.success) {
                setContent(data.insight, data.fact);
                return;
            }
        } catch { /* fall through to fallback */ }

        // Fallback
        setContent(
            fallbackInsights[currentIdx % fallbackInsights.length],
            fallbackFacts[currentIdx % fallbackFacts.length]
        );
        currentIdx++;
    }

    // Initial load
    fetchAIContent();

    // Rotate every 12 seconds
    setInterval(fetchAIContent, 12000);
}

/* ─── Smooth page transitions ─── */
document.querySelectorAll('a[href^="/"]').forEach(link => {
    link.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href === window.location.pathname) return;
        e.preventDefault();
        document.body.classList.add('page-exit');
        setTimeout(() => { window.location.href = href; }, 300);
    });
});

/* ─── Counter animation for stats ─── */
const counters = document.querySelectorAll('[data-count]');
if (counters.length) {
    const countObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !entry.target.dataset.counted) {
                entry.target.dataset.counted = 'true';
                const target = entry.target.dataset.count;
                const isNum = /^\d+$/.test(target);
                if (isNum) {
                    let current = 0;
                    const end = parseInt(target, 10);
                    const step = Math.max(1, Math.floor(end / 60));
                    const timer = setInterval(() => {
                        current += step;
                        if (current >= end) {
                            current = end;
                            clearInterval(timer);
                        }
                        entry.target.textContent = current.toLocaleString();
                    }, 20);
                } else {
                    entry.target.textContent = target;
                }
            }
        });
    }, { threshold: 0.3 });
    counters.forEach(c => countObserver.observe(c));
}
