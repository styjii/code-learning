/**
 * Changement d'onglet par clic ou par Ctrl+1 / Ctrl+2 / Ctrl+3 (HTML, CSS, TypeScript).
 */
export class TsTabsEvents {
    /** @param {import("../TsEditorManager.js").TsEditorManager} editorManager */
    static bind(editorManager) {
        document.querySelectorAll(".tab").forEach((tab) => {
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
                case "3": editorManager.switchTab("ts"); break;
            }
        });
    }
}
