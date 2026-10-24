import { IDENTIFIER, VOID_ELEMENTS, elementLabel, quoteString, truncate } from "./ValueFormatter.js";

/**
 * Affiche les « objets distants » produits par console-runtime.js comme la console de Chrome :
 * aperçu coloré sur une ligne, arbre dépliable (construit à la demande), indices des tableaux,
 * [[Prototype]], Map/Set avec leurs [[Entries]], éléments DOM, fonctions, erreurs…
 */

const PREVIEW_PROPS = 5;        // propriétés montrées dans l'aperçu d'un objet, d'une Map, d'un Set
const PREVIEW_CHARS = 280;      // budget de caractères d'un aperçu avant d'ajouter « … »

const h = (tag, className, text) => {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
};

/* ------------------------------------------------------------------ *
 * Aperçus : liste de morceaux de texte colorés (cc-*), puis rendu DOM
 * ------------------------------------------------------------------ */

class Tokens {
    constructor() { this.list = []; this.length = 0; }

    /** @param {"open"|"closed"} [only] morceau visible seulement quand le nœud est déplié / replié */
    add(text, cls = "", only = "") {
        this.list.push({ text, cls, only });
        if (!only) this.length += text.length;
        return this;
    }

    render(parent) {
        for (const { text, cls, only } of this.list) {
            if (!cls && !only) { parent.append(document.createTextNode(text)); continue; }
            parent.append(h("span", [cls, only ? `cc-when-${only}` : ""].filter(Boolean).join(" "), text));
        }
        return parent;
    }
}

function fnLabel(node) {
    if (node.kind === "class") return `class ${node.name || "(anonymous)"}`;
    const star = node.kind === "gen" || node.kind === "asyncgen" ? "*" : "";
    const prefix = node.kind === "async" || node.kind === "asyncgen" ? "async " : "";
    return `${prefix}ƒ${star} ${node.name}(${node.params})`;
}

function keyText(key, quoted) {
    if (key && typeof key === "object") return key.v;                      // Symbol(x)
    if (!quoted || IDENTIFIER.test(key) || /^\d+$/.test(key)) return key;
    return quoteString(key);
}

function previewFunction(node, depth, t) {
    if (depth > 0 || !node.src) return t.add(fnLabel(node), "cc-fn");
    // Au premier niveau : le code source, « ƒ » remplaçant le mot-clé function (comme DevTools).
    const match = node.src.match(/^(async\s+)?function\b\s*(\*)?\s*/);
    if (!match) return t.add(node.src);
    t.add(`${match[1] || ""}ƒ${match[2] || ""}`, "cc-fn");
    return t.add(` ${node.src.slice(match[0].length)}`);
}

function previewArray(node, depth, t) {
    const named = node.cls !== "Array";
    if (depth > 0) return t.add(named ? `${node.cls}(${node.n})` : node.n === 0 ? "[]" : `Array(${node.n})`);
    if (named) t.add(`${node.cls}(${node.n}) `);
    else if (node.n > 1) t.add(`(${node.n}) `);
    t.add("[");
    if (node.lazy) {
        t.add("…");
    } else {
        for (let i = 0; i < node.items.length; i++) {
            if (i) t.add(", ");
            if (t.length > PREVIEW_CHARS * 2) { t.add("…"); break; }
            previewValue(node.items[i], depth + 1, t);
        }
        if (node.more && t.length <= PREVIEW_CHARS * 2) t.add(", …");
    }
    return t.add("]");
}

function previewObject(node, depth, t) {
    if (node.ref) t.add(`<ref *${node.ref}> `, "cc-ref");
    const name = node.cls && node.cls !== "Object" ? `${node.cls} ` : "";
    const rows = node.props || [];
    const hasProps = node.lazy ? node.nk > 0 : rows.length > 0;

    if (node.special === "promise") return t.add("Promise {…}");
    if (node.prim !== undefined) {
        t.add(`${name}{`);
        previewValue(node.prim, depth + 1, t);
        return t.add("}");
    }
    if (node.lazy || depth > 0) return t.add(name + (hasProps ? "{…}" : "{}"));

    t.add(`${name}{`);
    let shown = 0;
    for (const row of rows) {
        if (shown >= PREVIEW_PROPS || t.length > PREVIEW_CHARS) break;
        if (shown++) t.add(", ");
        t.add(keyText(row.k, true), "cc-key");
        t.add(": ");
        if (row.acc) t.add("(...)", "cc-acc");
        else previewValue(row.v, depth + 1, t);
    }
    if (rows.length > shown || node.more) t.add(shown ? ", …" : "…");
    return t.add("}");
}

function previewCollection(node, depth, t, label) {
    if (depth > 0 || node.lazy) return t.add(`${label}(${node.n})${node.lazy && depth === 0 ? " {…}" : ""}`);
    t.add(`${label}(${node.n}) {`);
    const list = label === "Map" ? node.entries : node.items;
    let shown = 0;
    for (const entry of list) {
        if (shown >= PREVIEW_PROPS || t.length > PREVIEW_CHARS) break;
        if (shown++) t.add(", ");
        if (label === "Map") {
            previewValue(entry[0], depth + 1, t);
            t.add(" => ");
            previewValue(entry[1], depth + 1, t);
        } else {
            previewValue(entry, depth + 1, t);
        }
    }
    if (list.length > shown || node.more) t.add(shown ? ", …" : "…");
    return t.add("}");
}

function openTag(node, t) {
    t.add("<", "cc-tag").add(node.tag, "cc-tag-name");
    for (const [name, value] of node.attrs || []) {
        t.add(" ").add(name, "cc-attr-name").add("=", "cc-tag");
        t.add(`"${truncate(value, 120)}"`, "cc-attr-value");
    }
    return t.add(">", "cc-tag");
}

/** Un élément n'est dépliable que s'il contient autre chose qu'un simple texte (comme dans Chrome). */
function domExpandable(node) {
    if (!node.kids || !node.kids.length) return false;
    return !(node.nt === 1 && node.nkids === 1 && node.kids[0].nt === 3);
}

function previewDom(node, depth, t) {
    switch (node.nt) {
        case 3: return t.add(`"${truncate(node.text.trim(), 120)}"`, "cc-text-node");
        case 8: return t.add(`<!--${truncate(node.text, 120)}-->`, "cc-comment");
        case 10: return t.add(`<!DOCTYPE ${node.text}>`, "cc-tag");
        case 9: return t.add("#document", "cc-tag");
        case 11: return t.add("#document-fragment", "cc-tag");
        default: break;
    }
    if (depth > 0) return t.add(elementLabel(node), "cc-tag-name");

    openTag(node, t);
    if (VOID_ELEMENTS.has(node.tag)) return t;
    if (!node.nkids) return t.add(`</${node.tag}>`, "cc-tag");

    // Replié : <p>texte</p> ou <div>…</div> ; déplié : seulement la balise ouvrante (la fermante est en bas).
    const only = domExpandable(node) ? "closed" : "";
    const first = node.kids && node.kids[0];
    if (node.nkids === 1 && first && first.nt === 3) t.add(truncate(first.text.trim(), 120), "cc-text-node", only);
    else t.add("…", "", only);
    return t.add(`</${node.tag}>`, "cc-tag", only);
}

function previewValue(node, depth, t) {
    if (node === null) return t.add("null", "cc-null");
    switch (typeof node) {
        case "string": return t.add(quoteString(truncate(node, 100)), "cc-string");
        case "number": return t.add(String(node), "cc-number");
        case "boolean": return t.add(String(node), "cc-boolean");
        default: break;
    }
    switch (node.$t) {
        case "undef": return t.add("undefined", "cc-undef");
        case "num": return t.add(node.v, "cc-number");
        case "big": return t.add(`${node.v}n`, "cc-number");
        case "sym": return t.add(node.v, "cc-symbol");
        case "str": return t.add(quoteString(truncate(node.v, 100)), "cc-string");
        case "date": return t.add(node.v, "cc-date");
        case "re": return t.add(node.v, "cc-regexp");
        case "circ": return t.add(`[Circular *${node.id}]`, "cc-ref");
        case "empty": return t.add(`empty × ${node.n}`, "cc-empty");
        case "err": return t.add(depth > 0 ? `${node.name}: ${node.message}` : node.stack, "cc-error-text");
        case "fn": return previewFunction(node, depth, t);
        case "arr": return previewArray(node, depth, t);
        case "obj": return previewObject(node, depth, t);
        case "map": return previewCollection(node, depth, t, "Map");
        case "set": return previewCollection(node, depth, t, "Set");
        case "dom": return previewDom(node, depth, t);
        case "proto": return t.add(node.cls === null ? "null" : node.cls);
        case "entries": return t.add(`Array(${node.list.length + (node.more || 0)})`);
        case "entry": {
            t.add("{");
            previewValue(node.k, 1, t);
            t.add(" => ");
            previewValue(node.v, 1, t);
            return t.add("}");
        }
        default: return t.add(String(node.$t));
    }
}

/** Texte brut d'une valeur, pour « %s » et les cellules simples. */
export function previewText(node) {
    if (typeof node === "string") return node;
    const t = new Tokens();
    previewValue(node, 1, t);
    return t.list.filter((part) => !part.only).map((part) => part.text).join("");
}

/* ------------------------------------------------------------------ *
 * Arbre : lignes enfants construites au premier dépliage
 * ------------------------------------------------------------------ */

function expandable(node) {
    if (node === null || typeof node !== "object") return false;
    switch (node.$t) {
        case "arr": case "map": case "set": return !node.lazy;
        case "obj": return !node.lazy && node.special !== "promise";
        case "fn": return !node.lazy && !!node.props;
        case "proto": return !!node.props;
        case "dom": return domExpandable(node);
        case "entries": case "entry": return true;
        default: return false;
    }
}

const prop = (key, value, options = {}) => renderValue(value, { key, depth: 1, ...options });

function noteRow(text) {
    const row = h("div", "cc-prop cc-note");
    row.append(h("span", "cc-spacer"), h("span", "cc-dim", text));
    return row;
}

function propFromRow(row) {
    if (row.acc) {
        const line = h("div", "cc-prop");
        line.append(h("span", "cc-spacer"), h("span", `cc-key${row.n ? " cc-dim" : ""}`, keyText(row.k, false)), ": ",
            h("span", "cc-acc", "(...)"));
        line.title = row.acc.get ? "Propriété accessible par un getter" : "Propriété avec setter";
        return line;
    }
    return prop(keyText(row.k, false), row.v, { dim: !!row.n, index: typeof row.k === "string" && /^\d+$/.test(row.k) });
}

function buildChildren(node) {
    const frag = document.createDocumentFragment();
    const protoRow = () => { if (node.proto) frag.append(prop("[[Prototype]]", node.proto, { dim: true })); };

    switch (node.$t) {
        case "arr": {
            let index = 0;
            for (const item of node.items) {
                if (item && item.$t === "empty") {
                    frag.append(prop(String(index), item, { index: true, dim: true }));
                    index += item.n;
                } else {
                    frag.append(prop(String(index++), item, { index: true }));
                }
            }
            if (node.more) frag.append(noteRow(`… ${node.more} éléments de plus`));
            for (const row of node.props || []) frag.append(propFromRow(row));
            frag.append(prop("length", node.n, { dim: true }));
            protoRow();
            break;
        }
        case "map":
        case "set": {
            frag.append(prop("size", node.n));
            frag.append(prop("[[Entries]]", node.$t === "map"
                ? { $t: "entries", kind: "map", list: node.entries, more: node.more }
                : { $t: "entries", kind: "set", list: node.items, more: node.more }));
            protoRow();
            break;
        }
        case "entries": {
            node.list.forEach((entry, i) => {
                frag.append(prop(String(i), node.kind === "map" ? { $t: "entry", k: entry[0], v: entry[1] } : entry, { index: true }));
            });
            if (node.more) frag.append(noteRow(`… ${node.more} entrées de plus`));
            break;
        }
        case "entry":
            frag.append(prop("key", node.k), prop("value", node.v));
            break;
        case "obj": {
            for (const row of node.props) frag.append(propFromRow(row));
            if (node.prim !== undefined) frag.append(prop("[[PrimitiveValue]]", node.prim, { dim: true }));
            if (node.more) frag.append(noteRow(`… ${node.more} propriétés de plus`));
            protoRow();
            break;
        }
        case "fn": {
            for (const row of node.props) frag.append(propFromRow(row));
            frag.append(prop("[[Prototype]]", { $t: "proto", cls: "ƒ ()" }, { dim: true }));
            break;
        }
        case "proto": {
            for (const row of node.props) frag.append(propFromRow(row));
            protoRow();
            break;
        }
        case "dom": {
            for (const kid of node.kids) frag.append(renderValue(kid, { depth: 0, block: true }));
            if (node.more) frag.append(noteRow(`… ${node.more} nœuds de plus`));
            break;
        }
        default: break;
    }
    return frag;
}

/**
 * Rend une valeur.
 * @param {*} node nœud distant
 * @param {{key?: string|null, dim?: boolean, index?: boolean, depth?: number, top?: boolean, block?: boolean}} options
 *   top : valeur au premier niveau d'un message (inline) · key : ligne « clé: valeur » de l'arbre
 *   block : ligne autonome sans clé (enfants d'un élément DOM)
 */
export function renderValue(node, { key = null, dim = false, index = false, depth = 0, top = false, block = false } = {}) {
    const tokens = new Tokens();
    previewValue(node, depth, tokens);
    const asRow = key !== null || block;
    const open = expandable(node);

    const preview = h("span", "cc-preview");
    tokens.render(preview);
    if (dim) preview.classList.add("cc-dim");

    if (!open) {
        if (!asRow) return preview;
        const row = h("div", "cc-prop");
        row.append(h("span", "cc-spacer"));
        if (key !== null) row.append(h("span", `cc-key${index ? " cc-index" : ""}${dim ? " cc-dim" : ""}`, key), ": ");
        row.append(preview);
        return row;
    }

    const outer = h(top ? "span" : "div", `cc-node${asRow ? " cc-prop" : ""}${top ? " cc-top" : ""}`);
    const head = h(top ? "span" : "div", "cc-head");
    const arrow = h("span", "cc-arrow");
    arrow.setAttribute("role", "button");
    arrow.setAttribute("tabindex", "0");
    arrow.setAttribute("aria-expanded", "false");
    arrow.setAttribute("aria-label", "Déplier");
    head.append(arrow);
    if (key !== null) head.append(h("span", `cc-key${index ? " cc-index" : ""}${dim ? " cc-dim" : ""}`, key), ": ");
    head.append(preview);

    const children = h("div", "cc-children");
    outer.append(head, children);
    if (node.$t === "dom" && node.nt === 1 && !VOID_ELEMENTS.has(node.tag)) {
        const close = h("div", "cc-close-tag");
        close.append(h("span", "cc-spacer"), h("span", "cc-tag", "</"), h("span", "cc-tag-name", node.tag), h("span", "cc-tag", ">"));
        outer.append(close);
    }

    let built = false;
    const toggle = (force) => {
        const willOpen = force === undefined ? !outer.classList.contains("cc-open") : force;
        if (willOpen && !built) { children.append(buildChildren(node)); built = true; }
        outer.classList.toggle("cc-open", willOpen);
        arrow.setAttribute("aria-expanded", String(willOpen));
        arrow.setAttribute("aria-label", willOpen ? "Replier" : "Déplier");
    };
    head.addEventListener("click", () => {
        if (window.getSelection && String(window.getSelection()).length) return;   // sélection de texte en cours
        toggle();
    });
    arrow.addEventListener("keydown", (event) => {
        if (event.key === "Enter" || event.key === " ") { event.preventDefault(); toggle(); }
        else if (event.key === "ArrowRight") toggle(true);
        else if (event.key === "ArrowLeft") toggle(false);
    });
    return outer;
}

export function renderError(node) {
    const span = h("span", "cc-error-text", node.stack);
    if (node.cause) {
        span.append(document.createTextNode("\nCaused by: "));
        span.append(node.cause.$t === "err" ? renderError(node.cause) : renderArg(node.cause));
    }
    return span;
}

/**
 * Argument de premier niveau d'un message : les chaînes sont affichées telles quelles (sans
 * guillemets), les erreurs avec leur pile, tout le reste comme valeur dépliable.
 */
export function renderArg(node) {
    if (typeof node === "string") return h("span", "cc-text", node);
    if (node && node.$t === "str") return h("span", "cc-text", `${node.v}… (${node.len} caractères)`);
    if (node && node.$t === "err") return renderError(node);
    return renderValue(node, { top: true });
}

/** Cellule de console.table : aperçu court, comme dans un objet. */
export function renderCell(node) {
    const span = h("span", "cc-preview");
    const tokens = new Tokens();
    previewValue(node, 1, tokens);
    return tokens.render(span);
}
