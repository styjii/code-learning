/**
 * DropdownEvents handles dropdown toggling behavior for navigation menus.
 * - Toggle open/close on click
 * - Close menus on outside click
 */
export class DropdownEvents {
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
            });

            menu.querySelectorAll("li").forEach((item) => {
                item.addEventListener("click", () => {
                    menu.classList.remove("show");
                });
            });
        });

        document.addEventListener("click", () => {
            document.querySelectorAll(".drop-menu.show").forEach((menu) => {
                menu.classList.remove("show");
            });
        });
    }
}
