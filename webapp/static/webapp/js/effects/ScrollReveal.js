/**
 * Apparition progressive des sections : les éléments [data-reveal] passent de « transparent, légèrement plus bas »
 * à leur place (classe .is-visible) quand ils entrent dans l'écran. Seules opacity et transform sont animées
 * (voir style.css) ; --d décale le départ pour créer une cascade.
 */
export class ScrollReveal {
    static init() {
        const items = Array.from(document.querySelectorAll("[data-reveal]"));
        const show = (el) => el.classList.add("is-visible");
        if (!("IntersectionObserver" in window) || matchMedia("(prefers-reduced-motion: reduce)").matches) {
            items.forEach(show);
            return;
        }
        const observer = new IntersectionObserver((entries) => {
            for (const entry of entries) {
                if (!entry.isIntersecting) continue;
                show(entry.target);
                observer.unobserve(entry.target);
            }
        }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
        items.forEach((el) => observer.observe(el));
    }
}
