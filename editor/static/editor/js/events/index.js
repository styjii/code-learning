import { ToolbarEvents } from "./ToolbarEvents.js";
import { TabsEvents } from "./TabsEvents.js";
import { DropdownEvents } from "./DropdownEvents.js";
import { ModalEvents } from "./ModalEvents.js";
import { ProjectEvents } from "./ProjectEvents.js";
import { ZipEvents } from "./ZipEvents.js";

/**
 * Binds all UI-related events for the editor.
 * Combines toolbar, tabs, dropdowns, modals, projects, and ZIP handling.
 */
export function bindAllEvents() {
    ToolbarEvents.bind();
    TabsEvents.bind();
    DropdownEvents.bind();
    ModalEvents.bind();
    ProjectEvents.bind();
    ZipEvents.bind();
}
