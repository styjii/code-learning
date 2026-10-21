import { editorManager } from "../main.js";

/**
 * TabsEvents handles editor tab switching through clicks and keyboard shortcuts.
 * - Ctrl+1,2,3 switches tabs
 * - Clicking tab buttons switches tabs
 */
export class TabsEvents {
    /**
     * Binds tab click and keyboard shortcut events.
     */
    static bind() {
        document.querySelectorAll(".tab").forEach(tab => {
            tab.addEventListener("click", (e) => {
                const id = e.currentTarget.id.replace("-tab", "").trim();
                editorManager.switchTab(id);
            });
        });

        document.addEventListener("keydown", (e) => {
            if (!e.ctrlKey) return;
            switch (e.key) {
                case "1": editorManager.switchTab("html"); break;
                case "2": editorManager.switchTab("css"); break;
                case "3": editorManager.switchTab("js"); break;
            }
        });
    }
}
