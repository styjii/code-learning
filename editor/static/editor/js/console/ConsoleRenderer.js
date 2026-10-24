import { previewText, renderArg, renderCell, renderValue } from "./ValueRenderer.js";
import { sanitizeCss } from "./ValueFormatter.js";

const h = (tag, className, text) => {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
};

/** Valeur numérique d'un nœud pour %d / %i / %f. */
function numberOf(node, kind) {
    if (typeof node === "number") return kind === "f" ? node : Math.trunc(node);
    if (typeof node === "string") return kind === "f" ? parseFloat(node) : parseInt(node, 10);
    if (node && node.$t === "num") return Number(node.v);
    if (node && node.$t === "big") return `${node.v}n`;
    return NaN;
}

/**
 * Affiche les messages de console façon Chrome DevTools : lignes colorées (log, info, warn, error),
 * valeurs dépliables, groupes, tableaux, compteurs, minuteurs, remplacements « %s %d %o %c ».
 * Les messages arrivent déjà sérialisés (voir console-runtime.js).
 */
export class ConsoleRenderer {
    /**
     * @param {HTMLElement} rootEl conteneur des lignes
     * @param {{maxRows?: number}} [options] maxRows : au-delà, les plus anciennes lignes sont supprimées
     */
    constructor(rootEl, { maxRows = 1000 } = {}) {
        this.rootEl = rootEl;
        this.maxRows = maxRows;
        this.stack = [];
        this.rowCount = 0;
        rootEl.classList.add("cc");
    }

    get container() {
        return this.stack.length ? this.stack[this.stack.length - 1].body : this.rootEl;
    }

    /** Efface tout (la page peut aussi avoir vidé le conteneur elle-même : on resynchronise). */
    clear() {
        this.rootEl.replaceChildren();
        this.stack = [];
        this.rowCount = 0;
    }

    #sync() {
        if (!this.rootEl.firstElementChild || (this.stack.length && !this.stack[this.stack.length - 1].body.isConnected)) {
            this.stack = [];
            if (!this.rootEl.firstElementChild) this.rowCount = 0;
        }
    }

    /** Point d'entrée : un message {type, args, label, count, text, columns, stack}. */
    add(message) {
        this.#sync();
        const { type } = message;
        const args = message.args || [];

        switch (type) {
            case "clear":
                this.clear();
                this.#row("log", [h("span", "cc-dim", "Console was cleared")], { muted: true });
                return;
            case "group":
            case "groupCollapsed":
                this.#startGroup(args, type === "group");
                return;
            case "groupEnd":
                this.stack.pop();
                return;
            case "table":
                this.#table(message);
                return;
            case "count":
                this.#row("log", [h("span", "cc-text", `${message.label}: ${message.count}`)]);
                return;
            case "time":
                this.#row("log", [h("span", "cc-text", `${message.label}: ${message.text}`), ...this.#withSpace(this.#render(args))]);
                return;
            case "assert":
                this.#row("error", [h("span", "cc-text", args.length ? "Assertion failed: " : "Assertion failed"), ...this.#render(args)]);
                return;
            case "trace": {
                const nodes = args.length ? this.#render(args) : [h("span", "cc-text", "console.trace")];
                if (message.stack) nodes.push(h("span", "cc-stack", `\n${message.stack}`));
                this.#row("log", nodes);
                return;
            }
            case "dir":
            case "dirxml":
                this.#row("log", args.length ? [renderArg(args[0])] : []);
                return;
            default: {
                const kind = ["info", "warn", "error", "debug"].includes(type) ? type : "log";
                this.#row(kind, this.#render(args), { key: message.muted ? null : this.#key(kind, args), muted: !!message.muted });
            }
        }
    }

    /** Ajoute une ligne personnalisée (ex. champ de saisie d'input()) et la renvoie. */
    addCustomRow(node, type = "log") {
        this.#sync();
        return this.#row(type, [node]);
    }

    /* ---------- Rendu des arguments ---------- */

    #withSpace(nodes) {
        return nodes.length ? [document.createTextNode(" "), ...nodes] : [];
    }

    /** Applique les remplacements « %s %d %i %f %o %O %c %% » du premier argument chaîne. */
    #render(args) {
        const nodes = [];
        let rest = args;
        const first = args[0];
        if (typeof first === "string" && first.includes("%") && args.length > 1) {
            const formatted = this.#format(first, args);
            nodes.push(...formatted.nodes);
            rest = formatted.rest;
        }
        for (const arg of rest) {
            if (nodes.length) nodes.push(document.createTextNode(" "));
            nodes.push(renderArg(arg));
        }
        if (!nodes.length && !args.length) nodes.push(document.createTextNode(""));
        return nodes;
    }

    #format(format, args) {
        const nodes = [];
        let used = 1;
        let style = "";
        let buffer = "";
        const flush = () => {
            if (!buffer) return;
            const span = h("span", "cc-text", buffer);
            if (style) span.style.cssText = style;
            nodes.push(span);
            buffer = "";
        };

        const pattern = /%([sdifoOc%])/g;
        let last = 0;
        let match;
        while ((match = pattern.exec(format))) {
            buffer += format.slice(last, match.index);
            last = pattern.lastIndex;
            const spec = match[1];
            if (spec === "%") { buffer += "%"; continue; }
            if (used >= args.length) { buffer += match[0]; continue; }
            const arg = args[used++];
            if (spec === "s") buffer += typeof arg === "string" ? arg : previewText(arg);
            else if (spec === "d" || spec === "i") buffer += String(numberOf(arg, "i"));
            else if (spec === "f") buffer += String(numberOf(arg, "f"));
            else if (spec === "c") { flush(); style = sanitizeCss(typeof arg === "string" ? arg : ""); }
            else { flush(); nodes.push(renderArg(arg)); }          // %o / %O : valeur dépliable
        }
        buffer += format.slice(last);
        flush();
        return { nodes, rest: args.slice(used) };
    }

    #key(kind, args) {
        try {
            const key = `${kind}\u0000${JSON.stringify(args)}`;
            return key.length < 4000 ? key : null;
        } catch {
            return null;
        }
    }

    /* ---------- Lignes ---------- */

    /**
     * @param {string} type log | info | warn | error | debug
     * @param {Node[]} nodes contenu de la ligne
     * @param {{key?: string|null, muted?: boolean}} [options] key : des lignes identiques consécutives
     *   sont regroupées derrière un compteur, comme dans Chrome.
     */
    #row(type, nodes, { key = null, muted = false } = {}) {
        const container = this.container;
        const last = container.lastElementChild;

        if (key && last && last.classList.contains("cc-row") && last._ccKey === key) {
            last._ccCount += 1;
            let badge = last.querySelector(":scope > .cc-badge");
            if (!badge) {
                badge = h("span", "cc-badge");
                last.prepend(badge);
            }
            badge.textContent = String(last._ccCount);
            badge.title = `${last._ccCount} messages identiques`;
            return last;
        }

        const row = h("div", `cc-row cc-${type}${muted ? " cc-muted" : ""}`);
        row.style.setProperty("--lvl", String(this.stack.length));
        row._ccKey = key;
        row._ccCount = 1;
        const content = h("span", "cc-content");
        content.append(...nodes);
        row.append(content);

        const stick = this.rootEl.scrollHeight - this.rootEl.scrollTop - this.rootEl.clientHeight < 30;
        container.append(row);
        this.rowCount += 1;
        this.#trim();
        if (stick) this.rootEl.scrollTop = this.rootEl.scrollHeight;
        return row;
    }

    #trim() {
        while (this.rowCount > this.maxRows && this.rootEl.firstElementChild) {
            this.rootEl.firstElementChild.remove();
            this.rowCount -= 1;
        }
    }

    /* ---------- Groupes ---------- */

    #startGroup(args, open) {
        const wrap = h("div", `cc-group${open ? " cc-open" : ""}`);
        const header = h("div", "cc-row cc-log cc-group-head");
        header.style.setProperty("--lvl", String(this.stack.length));
        const arrow = h("span", "cc-arrow cc-gutter-arrow");
        arrow.setAttribute("role", "button");
        arrow.setAttribute("tabindex", "0");
        arrow.setAttribute("aria-expanded", String(open));
        arrow.setAttribute("aria-label", "Replier ou déplier le groupe");
        const content = h("span", "cc-content cc-group-title");
        content.append(...(args.length ? this.#render(args) : [h("span", "cc-text", "console.group")]));
        header.append(arrow, content);

        const body = h("div", "cc-group-body");
        wrap.append(header, body);
        const toggle = () => {
            const willOpen = !wrap.classList.contains("cc-open");
            wrap.classList.toggle("cc-open", willOpen);
            arrow.setAttribute("aria-expanded", String(willOpen));
        };
        header.addEventListener("click", () => {
            if (window.getSelection && String(window.getSelection()).length) return;
            toggle();
        });
        arrow.addEventListener("keydown", (event) => {
            if (event.key === "Enter" || event.key === " ") { event.preventDefault(); toggle(); }
        });

        const stick = this.rootEl.scrollHeight - this.rootEl.scrollTop - this.rootEl.clientHeight < 30;
        this.container.append(wrap);
        this.rowCount += 1;
        this.stack.push({ body });
        if (stick) this.rootEl.scrollTop = this.rootEl.scrollHeight;
    }

    /* ---------- console.table ---------- */

    #table(message) {
        const model = this.#tableModel(message.args[0], message.columns);
        if (!model) {
            this.add({ type: "log", args: message.args });
            return;
        }
        const table = h("table", "cc-table");
        const head = h("tr");
        for (const title of model.headers) head.append(h("th", "", title));
        const thead = h("thead");
        thead.append(head);
        table.append(thead);

        const body = h("tbody");
        for (const row of model.rows) {
            const tr = h("tr");
            row.forEach((cell, i) => {
                const td = h("td", i === 0 ? "cc-table-index" : "");
                if (cell !== undefined) td.append(i === 0 ? document.createTextNode(cell) : renderCell(cell));
                tr.append(td);
            });
            body.append(tr);
        }
        table.append(body);
        this.#row("log", [table]);
    }

    /** Construit {headers, rows} à partir d'un tableau, d'un objet, d'une Map ou d'un Set. */
    #tableModel(node, columns) {
        if (!node || typeof node !== "object" || node.lazy) return null;
        const keyOf = (k) => (k && typeof k === "object" ? k.v : String(k));

        if (node.$t === "map") {
            return {
                headers: ["(iteration index)", "Key", "Values"],
                rows: node.entries.map(([k, v], i) => [String(i), k, v]),
            };
        }
        if (node.$t === "set") {
            return { headers: ["(iteration index)", "Values"], rows: node.items.map((v, i) => [String(i), v]) };
        }

        let entries;
        if (node.$t === "arr") {
            entries = [];
            let index = 0;
            for (const item of node.items) {
                if (item && item.$t === "empty") { index += item.n; continue; }
                entries.push([String(index++), item]);
            }
        } else if (node.$t === "obj" && node.props) {
            entries = node.props.filter((row) => !row.acc).map((row) => [keyOf(row.k), row.v]);
        } else {
            return null;
        }

        // Colonnes : union des clés des lignes-objets ; « Values » pour les valeurs primitives.
        const cellsOf = (value) => {
            if (value && value.$t === "obj" && value.props) return new Map(value.props.filter((r) => !r.acc).map((r) => [keyOf(r.k), r.v]));
            if (value && value.$t === "arr" && value.items) return new Map(value.items.map((v, i) => [String(i), v]));
            return null;
        };
        const keys = [];
        let hasValues = false;
        const parsed = entries.map(([index, value]) => {
            const cells = cellsOf(value);
            if (!cells) {
                hasValues = true;
            } else {
                for (const key of cells.keys()) if (!keys.includes(key)) keys.push(key);
            }
            return [index, cells, value];
        });

        const headers = columns && columns.length ? columns : keys;
        const rows = parsed.map(([index, cells, value]) => {
            const row = [index, ...headers.map((key) => cells?.get(key))];
            if (hasValues) row.push(cells ? undefined : value);
            return row;
        });
        return { headers: ["(index)", ...headers, ...(hasValues ? ["Values"] : [])], rows };
    }
}
