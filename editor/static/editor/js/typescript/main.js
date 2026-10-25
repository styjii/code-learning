import "../utils/csrf.js"; // doit être chargé en premier (jeton CSRF sur les fetch)
import { EditorConfigManager } from "../editors/EditorConfigManager.js";
import { patchPassiveTouchStart } from "../editors/utils.js";
import { ConsoleManager } from "../console/ConsoleManager.js";
import { state } from "./state.js";
import { TsEditorManager } from "./TsEditorManager.js";
import { TsEditorBinder } from "./TsEditorBinder.js";
import { TsProjectManager } from "./TsProjectManager.js";
import { TsSettingsBinder } from "./TsSettingsBinder.js";
import { bindAllEvents } from "./events/index.js";

patchPassiveTouchStart();

// Le gestionnaire de préférences Monaco (retour à la ligne, raccourcis...) est celui de l'éditeur Web,
// appliqué aux éditeurs de cette page.
const configManager = new EditorConfigManager(state);
export const editorManager = new TsEditorManager(configManager);

/**
 * Entry point for initializing the TypeScript editor UI, editors, projects, and event listeners.
 */
document.addEventListener("DOMContentLoaded", () => {
    editorManager.initializeEditors(async () => {
        await TsProjectManager.fetchAll();
        TsEditorBinder.bindChangeListeners();
        configManager.registerCommands();
        editorManager.switchTab("html");
    });

    TsSettingsBinder.bindListeners();
    bindAllEvents(editorManager);
    window.addEventListener("message", ConsoleManager.handleMessage);
    ConsoleManager.init();
});
