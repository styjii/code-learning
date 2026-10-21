/**
 * Bouton « retour en haut » et barre de progression de lecture.
 */
export class ScrollToTop {
    static init() {
        const button = document.getElementById("scrollToTopBtn");
        const bar = document.getElementById("reading-bar");
        let ticking = false;

        const update = () => {
            const top = window.scrollY;
            const max = document.documentElement.scrollHeight - window.innerHeight;
            if (button) button.hidden = top < 500;
            if (bar) bar.style.width = max > 0 ? `${Math.min(100, (top / max) * 100)}%` : "0";
            ticking = false;
        };

        window.addEventListener("scroll", () => {
            if (!ticking) { requestAnimationFrame(update); ticking = true; }
        }, { passive: true });
        button?.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
        document.addEventListener("section:change", update);
        update();
    }
}
