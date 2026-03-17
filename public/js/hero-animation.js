/**
 * JalRaksha — Artistic Water Surface Animation
 * Multi-layered canvas animation: flowing waves + luminous particles + gradient mesh
 */
(function () {
    const canvas = document.getElementById('heroCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    let width, height, animId;
    let time = 0;
    let particles = [];
    let mouse = { x: -9999, y: -9999 };

    /* ─── WAVE CONFIG ─── */
    const waves = [
        { amp: 50, freq: 0.004, speed: 0.008, yOff: 0.72, r: 0, g: 119, b: 182, alpha: 0.04 },
        { amp: 35, freq: 0.006, speed: 0.012, yOff: 0.76, r: 0, g: 180, b: 216, alpha: 0.05 },
        { amp: 25, freq: 0.01, speed: 0.018, yOff: 0.80, r: 34, g: 211, b: 238, alpha: 0.04 },
        { amp: 40, freq: 0.003, speed: 0.006, yOff: 0.68, r: 37, g: 99, b: 235, alpha: 0.03 },
        { amp: 18, freq: 0.015, speed: 0.025, yOff: 0.84, r: 96, g: 165, b: 250, alpha: 0.05 },
        { amp: 30, freq: 0.008, speed: 0.014, yOff: 0.74, r: 0, g: 212, b: 255, alpha: 0.03 },
    ];

    /* ─── PARTICLE CLASS ─── */
    class Orb {
        constructor() { this.init(); }
        init() {
            this.x = Math.random() * width;
            this.y = Math.random() * height;
            this.size = Math.random() * 2.5 + 0.5;
            this.vx = (Math.random() - 0.5) * 0.3;
            this.vy = -(Math.random() * 0.2 + 0.05);
            this.phase = Math.random() * Math.PI * 2;
            this.phaseSpeed = 0.003 + Math.random() * 0.005;
            this.drift = 0.15 + Math.random() * 0.25;
            this.baseAlpha = 0.15 + Math.random() * 0.4;
            this.alpha = this.baseAlpha;
            this.hue = 195 + Math.random() * 30;
            this.sat = 70 + Math.random() * 30;
            this.light = 55 + Math.random() * 25;
            this.pulsePhase = Math.random() * Math.PI * 2;
            this.pulseSpeed = 0.01 + Math.random() * 0.02;
        }
        update() {
            this.phase += this.phaseSpeed;
            this.pulsePhase += this.pulseSpeed;
            this.alpha = this.baseAlpha * (0.6 + 0.4 * Math.sin(this.pulsePhase));
            this.x += this.vx + Math.sin(this.phase) * this.drift;
            this.y += this.vy + Math.cos(this.phase * 0.7) * this.drift * 0.3;

            // Mouse attraction (gentle)
            const dx = mouse.x - this.x;
            const dy = mouse.y - this.y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            if (dist < 200 && dist > 0) {
                const force = (1 - dist / 200) * 0.15;
                this.x += dx / dist * force;
                this.y += dy / dist * force;
            }

            if (this.y < -30) { this.y = height + 30; this.x = Math.random() * width; }
            if (this.x < -30) this.x = width + 30;
            if (this.x > width + 30) this.x = -30;
        }
        draw() {
            ctx.save();
            ctx.globalAlpha = this.alpha;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fillStyle = `hsl(${this.hue}, ${this.sat}%, ${this.light}%)`;
            ctx.fill();
            // Glow
            if (this.size > 1.2) {
                const g = ctx.createRadialGradient(this.x, this.y, 0, this.x, this.y, this.size * 6);
                g.addColorStop(0, `hsla(${this.hue}, ${this.sat}%, ${this.light}%, ${this.alpha * 0.3})`);
                g.addColorStop(1, 'transparent');
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size * 6, 0, Math.PI * 2);
                ctx.fillStyle = g;
                ctx.fill();
            }
            ctx.restore();
        }
    }

    /* ─── DRAW WAVES ─── */
    function drawWaves() {
        for (const w of waves) {
            ctx.beginPath();
            const baseY = height * w.yOff;
            ctx.moveTo(0, height);
            for (let x = 0; x <= width; x += 3) {
                const y = baseY
                    + Math.sin(x * w.freq + time * w.speed) * w.amp
                    + Math.sin(x * w.freq * 2.5 + time * w.speed * 1.7) * w.amp * 0.3
                    + Math.sin(x * w.freq * 0.5 + time * w.speed * 0.5) * w.amp * 0.5;
                ctx.lineTo(x, y);
            }
            ctx.lineTo(width, height);
            ctx.closePath();
            const grad = ctx.createLinearGradient(0, baseY - w.amp, 0, height);
            grad.addColorStop(0, `rgba(${w.r}, ${w.g}, ${w.b}, ${w.alpha})`);
            grad.addColorStop(0.5, `rgba(${w.r}, ${w.g}, ${w.b}, ${w.alpha * 1.5})`);
            grad.addColorStop(1, `rgba(${w.r}, ${w.g}, ${w.b}, ${w.alpha * 0.3})`);
            ctx.fillStyle = grad;
            ctx.fill();
        }
    }

    /* ─── DRAW CONNECTIONS ─── */
    function drawConnections() {
        const maxDist = 120;
        for (let i = 0; i < particles.length; i++) {
            for (let j = i + 1; j < particles.length; j++) {
                const dx = particles[i].x - particles[j].x;
                const dy = particles[i].y - particles[j].y;
                const d2 = dx * dx + dy * dy;
                if (d2 < maxDist * maxDist) {
                    const dist = Math.sqrt(d2);
                    const alpha = (1 - dist / maxDist) * 0.08;
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(particles[j].x, particles[j].y);
                    ctx.strokeStyle = `rgba(96, 165, 250, ${alpha})`;
                    ctx.lineWidth = 0.5;
                    ctx.stroke();
                }
            }
        }
    }

    /* ─── DRAW AURORA / GRADIENT LIGHT ─── */
    function drawAurora() {
        const cx1 = width * 0.3 + Math.sin(time * 0.003) * width * 0.15;
        const cy1 = height * 0.3 + Math.cos(time * 0.004) * height * 0.1;
        const g1 = ctx.createRadialGradient(cx1, cy1, 0, cx1, cy1, width * 0.4);
        g1.addColorStop(0, `rgba(37, 99, 235, ${0.06 + Math.sin(time * 0.005) * 0.02})`);
        g1.addColorStop(1, 'transparent');
        ctx.fillStyle = g1;
        ctx.fillRect(0, 0, width, height);

        const cx2 = width * 0.7 + Math.cos(time * 0.002) * width * 0.1;
        const cy2 = height * 0.5 + Math.sin(time * 0.003) * height * 0.15;
        const g2 = ctx.createRadialGradient(cx2, cy2, 0, cx2, cy2, width * 0.35);
        g2.addColorStop(0, `rgba(34, 211, 238, ${0.04 + Math.cos(time * 0.004) * 0.015})`);
        g2.addColorStop(1, 'transparent');
        ctx.fillStyle = g2;
        ctx.fillRect(0, 0, width, height);

        const cx3 = width * 0.5 + Math.sin(time * 0.0025) * width * 0.2;
        const cy3 = height * 0.2 + Math.cos(time * 0.0035) * height * 0.1;
        const g3 = ctx.createRadialGradient(cx3, cy3, 0, cx3, cy3, width * 0.3);
        g3.addColorStop(0, `rgba(0, 180, 216, ${0.03 + Math.sin(time * 0.006) * 0.01})`);
        g3.addColorStop(1, 'transparent');
        ctx.fillStyle = g3;
        ctx.fillRect(0, 0, width, height);
    }

    /* ─── MAIN LOOP ─── */
    function animate() {
        time++;
        ctx.clearRect(0, 0, width, height);
        drawAurora();
        drawWaves();
        particles.forEach(p => { p.update(); p.draw(); });
        drawConnections();
        animId = requestAnimationFrame(animate);
    }

    function resize() {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
    }

    function init() {
        resize();
        const count = Math.max(35, Math.min(80, Math.floor(width * height * 0.00004)));
        particles = Array.from({ length: count }, () => new Orb());
        animate();
    }

    window.addEventListener('resize', () => {
        cancelAnimationFrame(animId);
        resize();
        const count = Math.max(35, Math.min(80, Math.floor(width * height * 0.00004)));
        particles = Array.from({ length: count }, () => new Orb());
        animate();
    });

    canvas.addEventListener('mousemove', e => { mouse.x = e.clientX; mouse.y = e.clientY; });
    canvas.addEventListener('mouseleave', () => { mouse.x = -9999; mouse.y = -9999; });

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
