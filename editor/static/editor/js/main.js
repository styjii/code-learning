import { EditorConfigManager } from "./editors/EditorConfigManager.js";
import { MonacoEditorManager } from "./editors/MonacoEditorManager.js";
import { patchPassiveTouchStart } from "./editors/utils.js";
import { ProjectManager } from "./projects/ProjectManager.js";
import { EditorBinder } from "./editors/EditorBinder.js";
import { SettingsBinder } from "./projects/SettingsBinder.js";
import { ConsoleManager } from "./console/ConsoleManager.js";
import { bindAllEvents } from "./events/index.js";

patchPassiveTouchStart();

const configManager = new EditorConfigManager();
export const editorManager = new MonacoEditorManager(configManager);

/**
 * Entry point for initializing the editor UI, editors, projects, and event listeners.
 */
document.addEventListener("DOMContentLoaded", () => {
    editorManager.initializeEditors(async () => {
        await ProjectManager.fetchAll();
        EditorBinder.bindChangeListeners();
        configManager.registerCommands();
        editorManager.switchTab("html");
    });

    SettingsBinder.bindListeners();
    bindAllEvents();
    window.addEventListener("message", ConsoleManager.handleMessage);
    ConsoleManager.init();
});
