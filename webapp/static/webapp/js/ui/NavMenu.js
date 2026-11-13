/**
 * Barre de navigation : menu déroulant « Cours », menu burger (mobile) et état « défilé » (fond plus marqué).
 */
export class NavMenu {
    static init() {
        const nav = document.getElementById("site-nav");
        if (!nav) return;

        // Fond de la barre : plus opaque dès que la page a défilé (sentinelle observée, sans écouteur de scroll).
        const sentinel = document.getElementById("top-sentinel");
        if (sentinel && "IntersectionObserver" in window) {
            new IntersectionObserver(([entry]) => nav.classList.toggle("is-stuck", !entry.isIntersecting)).observe(sentinel);
        }

        const drop = document.getElementById("nav-drop");
        const dropBtn = document.getElementById("nav-drop-btn");
        const burger = document.getElementById("nav-burger");
        const panel = document.getElementById("nav-panel");

        const setDrop = (open) => {
            drop?.classList.toggle("is-open", open);
            dropBtn?.setAttribute("aria-expanded", String(open));
        };
        const setBurger = (open) => {
            panel?.classList.toggle("is-open", open);
            burger?.setAttribute("aria-expanded", String(open));
            burger?.setAttribute("aria-label", open ? "Fermer le menu" : "Ouvrir le menu");
        };

        dropBtn?.addEventListener("click", (event) => {
            event.stopPropagation();
            setDrop(!drop.classList.contains("is-open"));
        });
        burger?.addEventListener("click", (event) => {
            event.stopPropagation();
            setBurger(!panel.classList.contains("is-open"));
        });
        // Un lien du menu referme tout ; un clic ailleurs ou Échap aussi.
        nav.addEventListener("click", (event) => {
            if (event.target.closest("a")) { setDrop(false); setBurger(false); }
        });
        document.addEventListener("click", (event) => {
            if (!drop?.contains(event.target)) setDrop(false);
            if (!panel?.contains(event.target) && !burger?.contains(event.target)) setBurger(false);
        });
        document.addEventListener("keydown", (event) => {
            if (event.key !== "Escape") return;
            if (drop?.classList.contains("is-open")) dropBtn.focus();
            setDrop(false);
            setBurger(false);
        });
    }
}
