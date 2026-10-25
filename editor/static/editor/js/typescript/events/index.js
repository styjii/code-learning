import { DropdownEvents } from "../../events/DropdownEvents.js";
import { ModalEvents } from "../../events/ModalEvents.js";
import { TsToolbarEvents } from "./TsToolbarEvents.js";
import { TsTabsEvents } from "./TsTabsEvents.js";
import { TsProjectEvents } from "./TsProjectEvents.js";
import { TsZipEvents } from "./TsZipEvents.js";
import { TsOptionsEvents } from "./TsOptionsEvents.js";

/**
 * Branche tous les événements de l'interface. Les menus déroulants et les fenêtres modales sont
 * ceux de l'éditeur Web (indépendants du langage).
 * @param {import("../TsEditorManager.js").TsEditorManager} editorManager
 */
export function bindAllEvents(editorManager) {
    TsToolbarEvents.bind();
    TsTabsEvents.bind(editorManager);
    DropdownEvents.bind();
    ModalEvents.bind();
    TsProjectEvents.bind();
    TsZipEvents.bind();
    TsOptionsEvents.bind();
}
