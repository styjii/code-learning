import { ValueFormatter } from "./ValueFormatter.js";
import { ValueRenderer } from "./ValueRenderer.js";

/**
 * Renders console messages and groups into the DOM.
 */
export class ConsoleRenderer {
    constructor(rootEl) {
        this.rootEl = rootEl;
        this.groupStack = [];
    }

    get targetContainer() {
        return this.groupStack.length > 0
            ? this.groupStack[this.groupStack.length - 1]
            : this.rootEl;
    }

    /**
     * Clears all console output and resets the internal group stack.
     * Removes all rendered console content from the DOM.
     */
    clear() {
        this.rootEl.innerHTML = "";
        this.groupStack = [];
    }

    /**
     * Logs a console message of the given type to the console output.
     * Supports standard log types, groups, tables, counts, timers, etc.
     * 
     * @param {string} type - The type of console message (log, table, group, etc.).
     * @param {Array} args - Arguments to render inline for standard logs or groups.
     * @param {any} data - Data used for rendering tables.
     * @param {Array<string>} columns - Optional column headers for tables.
     * @param {string} label - Optional label for count/time messages.
     */
    logMessage(type, args = [], data = null, columns = null, label = null) {
        const container = this.targetContainer;
        const line = document.createElement("div");
        line.className = `console-line ${type}`;

        switch (type) {
            case "table":
                this._renderTable(line, data, columns);
                break;

            case "group":
            case "groupCollapsed":
                this._startGroup(args, type === "group");
                return;

            case "groupEnd":
                this._endGroup();
                return;

            case "count":
            case "countReset":
            case "time":
            case "timeEnd":
                const labelDiv = document.createElement("div");
                labelDiv.className = "console-label";
                labelDiv.textContent = `${type} ${label ? `(${label})` : ""}`;
                line.appendChild(labelDiv);
                break;

            default:
                const inlineContainer = document.createElement("span");
                inlineContainer.className = "console-inline";
                args.forEach((arg, idx) => {
                    inlineContainer.appendChild(ValueRenderer.render(arg));
                    if (idx < args.length - 1) {
                        inlineContainer.appendChild(document.createTextNode(", "));
                    }
                });
                line.appendChild(inlineContainer);
        }

        container.appendChild(line);
        this.rootEl.scrollTop = this.rootEl.scrollHeight;
    }

    _startGroup(args, isOpen) {
        const groupContainer = document.createElement("details");
        groupContainer.className = "console-group";
        groupContainer.open = isOpen;

        const summary = document.createElement("summary");
        summary.textContent = args.map((arg) => ValueFormatter.format(arg)).join(" ");
        groupContainer.appendChild(summary);

        this.targetContainer.appendChild(groupContainer);
        this.groupStack.push(groupContainer);
    }

    _endGroup() {
        this.groupStack.pop();
    }

    _renderTable(line, data, columns) {
        if (!data) return;

        const table = document.createElement("table");
        table.className = "console-table";

        const rows = Array.isArray(data)
            ? data.map((item, i) =>
                typeof item === "object"
                    ? { "(index)": i, ...item }
                    : { "(index)": i, value: item }
            )
            : Object.entries(data).map(([k, v]) => ({ key: k, value: v }));

        if (rows.length === 0) return;

        const headers = columns || Object.keys(rows[0]);
        const thead = document.createElement("thead");
        const trHead = document.createElement("tr");
        headers.forEach((header) => {
            const th = document.createElement("th");
            th.textContent = header;
            trHead.appendChild(th);
        });
        thead.appendChild(trHead);
        table.appendChild(thead);

        const tbody = document.createElement("tbody");
        rows.forEach((row) => {
            const tr = document.createElement("tr");
            headers.forEach((header) => {
                const td = document.createElement("td");
                td.appendChild(ValueRenderer.render(row[header]));
                tr.appendChild(td);
            });
            tbody.appendChild(tr);
        });
        table.appendChild(tbody);
        line.appendChild(table);
    }
}
