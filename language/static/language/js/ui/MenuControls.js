/**
 * Menus de la barre du haut : tiroir des sections (mobile) et sélecteur de cours.
 */
export class MenuControls {
    static init() {
        MenuControls.initSidebar();
        MenuControls.initSwitcher();
    }

    static initSidebar() {
        const toggle = document.getElementById("menu-toggle");
        const backdrop = document.getElementById("backdrop");

        const setOpen = (open) => {
            document.body.classList.toggle("sidebar-open", open);
            toggle.setAttribute("aria-expanded", String(open));
            backdrop.hidden = !open;
        };

        toggle.addEventListener("click", () => setOpen(!document.body.classList.contains("sidebar-open")));
        backdrop.addEventListener("click", () => setOpen(false));
        document.addEventListener("sidebar:close", () => setOpen(false));
        document.addEventListener("keydown", (e) => {
            if (e.key === "Escape" && document.body.classList.contains("sidebar-open")) setOpen(false);
        });
    }

    static initSwitcher() {
        const button = document.getElementById("switcher-btn");
        const panel = document.getElementById("switcher-panel");

        const setOpen = (open) => {
            panel.hidden = !open;
            button.setAttribute("aria-expanded", String(open));
            if (open) panel.querySelector(".is-current")?.scrollIntoView({ block: "center" });
        };

        button.addEventListener("click", (e) => { e.stopPropagation(); setOpen(panel.hidden); });
        document.addEventListener("click", (e) => { if (!panel.contains(e.target)) setOpen(false); });
        document.addEventListener("keydown", (e) => {
            if (e.key === "Escape" && !panel.hidden) { setOpen(false); button.focus(); }
        });
    }
}
