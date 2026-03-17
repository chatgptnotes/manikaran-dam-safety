/**
 * Water Network Particle Animation
 * Creates flowing blue particles with connecting lines
 * evoking water flow and dam monitoring networks.
 */
(function () {
    const canvas = document.getElementById('heroCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    let width, height, particles, animationId;
    const PARTICLE_COUNT_FACTOR = 0.00006; // particles per pixel
    const CONNECTION_DIST = 150;
    const MOUSE_RADIUS = 200;
    let mouse = { x: -9999, y: -9999 };

    function resize() {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
    }

    class Particle {
        constructor() {
            this.reset();
        }
        reset() {
            this.x = Math.random() * width;
            this.y = Math.random() * height;
            this.size = Math.random() * 2.5 + 0.5;
            this.speedX = (Math.random() - 0.5) * 0.4;
            this.speedY = (Math.random() - 0.5) * 0.3 - 0.1; // slight upward drift (like bubbles)
            this.opacity = Math.random() * 0.5 + 0.2;
            // Water-themed blue colors
            const hue = 195 + Math.random() * 30; // 195-225 range (cyan to blue)
            const sat = 70 + Math.random() * 30;
            const light = 55 + Math.random() * 25;
            this.color = `hsla(${hue}, ${sat}%, ${light}%, ${this.opacity})`;
            this.baseOpacity = this.opacity;
            // Subtle sinusoidal drift
            this.driftPhase = Math.random() * Math.PI * 2;
            this.driftSpeed = 0.002 + Math.random() * 0.003;
            this.driftAmp = 0.2 + Math.random() * 0.3;
        }
        update() {
            this.driftPhase += this.driftSpeed;
            this.x += this.speedX + Math.sin(this.driftPhase) * this.driftAmp;
            this.y += this.speedY + Math.cos(this.driftPhase * 0.7) * this.driftAmp * 0.5;

            // Mouse interaction — gentle repulsion
            const dx = this.x - mouse.x;
            const dy = this.y - mouse.y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            if (dist < MOUSE_RADIUS) {
                const force = (1 - dist / MOUSE_RADIUS) * 0.8;
                this.x += dx / dist * force;
                this.y += dy / dist * force;
            }

            // Wrap around edges
            if (this.x < -20) this.x = width + 20;
            if (this.x > width + 20) this.x = -20;
            if (this.y < -20) this.y = height + 20;
            if (this.y > height + 20) this.y = -20;
        }
        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fillStyle = this.color;
            ctx.fill();

            // Glow effect for larger particles
            if (this.size > 1.5) {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size * 3, 0, Math.PI * 2);
                const glow = ctx.createRadialGradient(
                    this.x, this.y, this.size * 0.5,
                    this.x, this.y, this.size * 3
                );
                glow.addColorStop(0, `hsla(210, 80%, 65%, ${this.baseOpacity * 0.15})`);
                glow.addColorStop(1, 'transparent');
                ctx.fillStyle = glow;
                ctx.fill();
            }
        }
    }

    function drawConnections() {
        for (let i = 0; i < particles.length; i++) {
            for (let j = i + 1; j < particles.length; j++) {
                const dx = particles[i].x - particles[j].x;
                const dy = particles[i].y - particles[j].y;
                const dist = Math.sqrt(dx * dx + dy * dy);
                if (dist < CONNECTION_DIST) {
                    const opacity = (1 - dist / CONNECTION_DIST) * 0.12;
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(particles[j].x, particles[j].y);
                    ctx.strokeStyle = `rgba(96, 165, 250, ${opacity})`;
                    ctx.lineWidth = 0.6;
                    ctx.stroke();
                }
            }
        }
    }

    // Slow-moving wave overlay
    let wavePhase = 0;
    function drawWaves() {
        wavePhase += 0.005;
        ctx.beginPath();
        ctx.moveTo(0, height);
        for (let x = 0; x <= width; x += 4) {
            const y = height * 0.85
                + Math.sin(x * 0.003 + wavePhase) * 20
                + Math.sin(x * 0.007 + wavePhase * 1.3) * 10;
            ctx.lineTo(x, y);
        }
        ctx.lineTo(width, height);
        ctx.closePath();
        const grad = ctx.createLinearGradient(0, height * 0.8, 0, height);
        grad.addColorStop(0, 'rgba(37, 99, 235, 0.03)');
        grad.addColorStop(1, 'rgba(37, 99, 235, 0.08)');
        ctx.fillStyle = grad;
        ctx.fill();
    }

    function animate() {
        ctx.clearRect(0, 0, width, height);
        drawWaves();
        particles.forEach(p => { p.update(); p.draw(); });
        drawConnections();
        animationId = requestAnimationFrame(animate);
    }

    function init() {
        resize();
        const count = Math.max(40, Math.floor(width * height * PARTICLE_COUNT_FACTOR));
        particles = Array.from({ length: count }, () => new Particle());
        animate();
    }

    window.addEventListener('resize', () => {
        cancelAnimationFrame(animationId);
        resize();
        const count = Math.max(40, Math.floor(width * height * PARTICLE_COUNT_FACTOR));
        particles = Array.from({ length: count }, () => new Particle());
        animate();
    });

    canvas.addEventListener('mousemove', e => {
        mouse.x = e.clientX;
        mouse.y = e.clientY;
    });
    canvas.addEventListener('mouseleave', () => { mouse.x = -9999; mouse.y = -9999; });

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
