/**
 * DropdownEvents handles dropdown toggling behavior for navigation menus.
 * - Toggle open/close on click
 * - Close menus on outside click or Escape
 * - Keep an open menu inside the viewport (narrow screens, long labels)
 */
export class DropdownEvents {
    /**
     * Shifts a menu horizontally so that it never leaves the screen.
     * Phones in portrait use full-width sheets (CSS), where the shift is 0.
     * @param {HTMLElement} menu An open `.drop-menu`
     */
    static keepInViewport(menu) {
        const margin = 8;
        menu.style.setProperty("--shift-x", "0px");
        const rect = menu.getBoundingClientRect();
        const width = document.documentElement.clientWidth;
        let shift = 0;
        if (rect.right > width - margin) shift = width - margin - rect.right;
        if (rect.left + shift < margin) shift = margin - rect.left;
        menu.style.setProperty("--shift-x", `${Math.round(shift)}px`);
    }

    /**
     * Binds dropdown toggle behavior for navigation.
     */
    static bind() {
        const triggers = document.querySelectorAll(".drop > .navlink");
        triggers.forEach((trigger) => {
            const menu = trigger.parentElement.querySelector(".drop-menu");

            trigger.addEventListener("click", (e) => {
                e.stopPropagation();
                document.querySelectorAll(".drop-menu.show").forEach((openMenu) => {
                    if (openMenu !== menu) {
                        openMenu.classList.remove("show");
                    }
                });
                menu.classList.toggle("show");
                trigger.setAttribute("aria-expanded", String(menu.classList.contains("show")));
                if (menu.classList.contains("show")) DropdownEvents.keepInViewport(menu);
            });

            menu.querySelectorAll("li").forEach((item) => {
                item.addEventListener("click", () => {
                    menu.classList.remove("show");
                });
            });
        });

        const closeAll = () => {
            document.querySelectorAll(".drop-menu.show").forEach((menu) => {
                menu.classList.remove("show");
                menu.parentElement.querySelector(":scope > .navlink")?.setAttribute("aria-expanded", "false");
            });
        };
        document.addEventListener("click", closeAll);
        document.addEventListener("keydown", (e) => { if (e.key === "Escape") closeAll(); });
        // Rotation de l'appareil / redimensionnement : un menu ouvert serait mal placé.
        window.addEventListener("resize", closeAll);
    }
}
