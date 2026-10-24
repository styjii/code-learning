/**
 * console-runtime.js : côté « exécution » de la console façon Chrome DevTools.
 *
 * Script classique (pas un module) chargé là où le code de l'utilisateur tourne : iframe d'aperçu de
 * l'éditeur, Web Worker et iframe d'exécution des blocs du cours. Il fait deux choses :
 *
 *  1. sérialise n'importe quelle valeur JavaScript en un arbre JSON (« objet distant ») que la page
 *     peut afficher et déplier : classes, Map/Set, getters, références circulaires, nœuds DOM…
 *  2. installe une console (log, table, group, count, time, trace…) qui poste ces arbres.
 *
 * Format d'un nœud : une chaîne, un booléen, un nombre fini ou null sont eux-mêmes ; tout le reste est
 * un objet portant « $t » (undef, num, big, sym, str, fn, arr, obj, map, set, date, re, err, dom, circ,
 * proto, empty). Voir ValueRenderer.js pour la lecture.
 */
(function (root) {
    "use strict";
    if (root.ConsoleRuntime) return;

    const LIMITS = { depth: 6, props: 100, items: 100, string: 20000, nodes: 4000, source: 3000, kids: 60, proto: 4 };
    const fnToString = Function.prototype.toString;
    const objToString = Object.prototype.toString;

    const clip = (text, max = LIMITS.string) =>
        text.length > max ? { $t: "str", v: text.slice(0, max), len: text.length } : text;
    const isNative = (fn) => {
        try { return /\{\s*\[native code\]\s*\}\s*$/.test(fnToString.call(fn)); } catch { return true; }
    };
    const tagOf = (value) => { try { return objToString.call(value).slice(8, -1); } catch { return "Object"; } };

    /** Nom du constructeur, trouvé le long de la chaîne de prototypes (comme DevTools). */
    function ctorName(value) {
        try {
            let current = value;
            for (let i = 0; current && i < 30; i++) {
                const desc = Object.getOwnPropertyDescriptor(current, "constructor");
                if (desc && typeof desc.value === "function" && desc.value.name) return desc.value.name;
                current = Object.getPrototypeOf(current);
            }
        } catch { /* proxy hostile */ }
        return "Object";
    }

    /** Extrait la liste des paramètres du texte source d'une fonction ; détecte les fonctions fléchées. */
    function parseSignature(src) {
        const single = src.match(/^(?:async\s+)?([\w$]+)\s*=>/);
        if (single) return { params: single[1], arrow: true };
        const start = src.indexOf("(");
        if (start === -1) return { params: "", arrow: false };
        let depth = 0, end = -1;
        for (let i = start; i < src.length; i++) {
            const ch = src[i];
            if (ch === "(") depth++;
            else if (ch === ")" && --depth === 0) { end = i; break; }
        }
        if (end === -1) return { params: "", arrow: false };
        const arrow = src.slice(end + 1).trimStart().startsWith("=>");
        return { params: src.slice(start + 1, end).replace(/\s+/g, " ").trim(), arrow };
    }

    function newContext() {
        return { nodes: 0, refs: 0, ancestors: new Map() };
    }

    function serializeFunction(fn, ctx, depth, shallow) {
        let src = "";
        try { src = fnToString.call(fn); } catch { /* ignore */ }
        let kind = "fn";
        if (/^class\b/.test(src)) kind = "class";
        else if (/^async\s*(?:function\s*)?\*/.test(src)) kind = "asyncgen";
        else if (/^async\b/.test(src)) kind = "async";
        else if (/^function\s*\*|^\*/.test(src)) kind = "gen";
        const { params, arrow } = kind === "class" ? { params: "", arrow: false } : parseSignature(src);

        const node = {
            $t: "fn", name: String(fn.name || ""), kind, params, arrow,
            native: isNative(fn), len: Number(fn.length) || 0,
            src: src.length > LIMITS.source ? `${src.slice(0, LIMITS.source)}…` : src,
        };
        if (shallow || depth >= LIMITS.depth) { node.lazy = true; return node; }

        const rows = [
            { k: "length", v: node.len, n: true },
            { k: "name", v: node.name, n: true },
        ];
        if (!arrow && kind !== "async" && Object.prototype.hasOwnProperty.call(fn, "prototype")) {
            try { rows.push({ k: "prototype", v: serializeValue(fn.prototype, ctx, depth + 1, true), n: true }); } catch { /* ignore */ }
        }
        appendOwnProperties(fn, rows, ctx, depth, (key) => ["length", "name", "prototype", "arguments", "caller"].includes(key));
        node.props = rows;
        return node;
    }

    /**
     * Ajoute les propriétés propres (énumérables) d'un objet sous forme de lignes {k, v | acc, n}.
     * @param {(key: string|symbol) => boolean} [skip] clés à ignorer
     * @returns {number} nombre total de propriétés énumérables (même au-delà de la limite d'affichage)
     */
    function appendOwnProperties(target, rows, ctx, depth, skip) {
        let keys;
        try { keys = Reflect.ownKeys(target); } catch { return 0; }
        let total = 0, added = 0;
        for (const key of keys) {
            if (skip && skip(key)) continue;
            let desc;
            try { desc = Object.getOwnPropertyDescriptor(target, key); } catch { continue; }
            if (!desc || !desc.enumerable) continue;
            total++;
            if (added >= LIMITS.props) continue;
            const row = { k: typeof key === "symbol" ? { $t: "sym", v: key.toString() } : key };
            if (desc.get || desc.set) row.acc = { get: !!desc.get, set: !!desc.set };
            else row.v = serializeValue(desc.value, ctx, depth + 1);
            rows.push(row);
            added++;
        }
        return total;
    }

    /** Propriétés « de plateforme » (Event, URL, …) : lues par for…in car portées par le prototype. */
    function appendPlatformProperties(target, rows, ctx, depth) {
        let count = 0;
        try {
            for (const key in target) {
                if (count >= 60) break;
                let value;
                try { value = target[key]; } catch { continue; }
                if (typeof value === "function") continue;
                rows.push({ k: key, v: serializeValue(value, ctx, depth + 1) });
                count++;
            }
        } catch { /* ignore */ }
    }

    /** « [[Prototype]] » : déplié seulement pour les prototypes écrits par l'utilisateur. */
    function serializeProto(value, ctx, depth, level = 0) {
        let proto;
        try { proto = Object.getPrototypeOf(value); } catch { return null; }
        if (proto === null) return { $t: "proto", cls: null };

        const ctor = (() => { try { return Object.getOwnPropertyDescriptor(proto, "constructor")?.value; } catch { return undefined; } })();
        const native = typeof ctor !== "function" || isNative(ctor);
        // Prototype natif : son propre nom (Map, Set, Error…) ; prototype d'une classe écrite par
        // l'utilisateur : le nom de son parent (« Object » si la classe n'étend rien), comme DevTools.
        const label = Array.isArray(proto) ? "Array(0)" : native ? ctorName(proto) : labelOfPrototype(proto);
        if (native || level >= LIMITS.proto || depth >= LIMITS.depth) return { $t: "proto", cls: label };

        const rows = [];
        let keys = [];
        try { keys = Reflect.ownKeys(proto); } catch { /* ignore */ }
        for (const key of keys) {
            let desc;
            try { desc = Object.getOwnPropertyDescriptor(proto, key); } catch { continue; }
            if (!desc) continue;
            const row = { k: typeof key === "symbol" ? { $t: "sym", v: key.toString() } : key, n: !desc.enumerable };
            if (desc.get || desc.set) row.acc = { get: !!desc.get, set: !!desc.set };
            else if (typeof desc.value === "function") row.v = serializeFunction(desc.value, ctx, depth + 1, true);
            else row.v = serializeValue(desc.value, ctx, depth + 1);
            rows.push(row);
        }
        return { $t: "proto", cls: label, props: rows, proto: serializeProto(proto, ctx, depth + 1, level + 1) };
    }

    /** DevTools affiche comme libellé le nom du constructeur du *parent* du prototype. */
    function labelOfPrototype(proto) {
        let parent;
        try { parent = Object.getPrototypeOf(proto); } catch { return "Object"; }
        if (parent === null) return "Object";
        return ctorName(parent);
    }

    function serializeDom(node, ctx, depth) {
        const nt = node.nodeType;
        if (nt === 3 || nt === 8) return { $t: "dom", nt, text: clip(node.nodeValue || "", 2000) };
        if (nt === 10) return { $t: "dom", nt, text: node.name };
        const out = { $t: "dom", nt };
        if (nt === 1) {
            out.tag = node.localName;
            out.attrs = Array.from(node.attributes, (a) => [a.name, a.value]);
        } else if (nt === 11) {
            out.tag = "#document-fragment";
        }
        const children = Array.from(node.childNodes || []).filter((c) => c.nodeType !== 3 || /\S/.test(c.nodeValue || ""));
        out.nkids = children.length;
        if (children.length && depth < LIMITS.depth && ctx.nodes < LIMITS.nodes) {
            ctx.nodes++;
            out.kids = children.slice(0, LIMITS.kids).map((c) => serializeDom(c, ctx, depth + 1));
            if (children.length > LIMITS.kids) out.more = children.length - LIMITS.kids;
        }
        return out;
    }

    function serializeError(error, ctx, depth) {
        let stack = "";
        try { stack = String(error.stack || ""); } catch { /* ignore */ }
        const name = String(error.name || "Error");
        const message = String(error.message ?? "");
        // Firefox/Safari : la pile n'inclut pas l'en-tête « Nom: message »
        if (!stack || !stack.includes(message)) stack = `${name}${message ? `: ${message}` : ""}${stack ? `\n${stack}` : ""}`;
        const node = { $t: "err", name, message, stack: clip(stack, 8000), cls: ctorName(error) };
        if (error.cause !== undefined && depth < LIMITS.depth) node.cause = serializeValue(error.cause, ctx, depth + 1);
        return node;
    }

    function serializeValue(value, ctx, depth = 0, shallow = false) {
        switch (typeof value) {
            case "string": return clip(value);
            case "boolean": return value;
            case "number":
                if (Number.isFinite(value) && !Object.is(value, -0)) return value;
                return { $t: "num", v: Object.is(value, -0) ? "-0" : String(value) };
            case "undefined": return { $t: "undef" };
            case "bigint": return { $t: "big", v: value.toString() };
            case "symbol": return { $t: "sym", v: value.toString() };
            case "function": return serializeFunction(value, ctx, depth, shallow);
            default: break;
        }
        if (value === null) return null;

        // Référence circulaire : seulement si l'objet est un ancêtre (un objet partagé n'est pas circulaire).
        const ancestor = ctx.ancestors.get(value);
        if (ancestor) {
            if (!ancestor.id) { ancestor.id = ++ctx.refs; ancestor.node.ref = ancestor.id; }
            return { $t: "circ", id: ancestor.id };
        }

        try {
            return serializeObject(value, ctx, depth, shallow);
        } catch {
            return { $t: "obj", cls: "Object", lazy: true, nk: 0 };
        }
    }

    function serializeObject(value, ctx, depth, shallow) {
        if (typeof Node !== "undefined" && value instanceof Node) return serializeDom(value, ctx, depth);
        if (value === root || (typeof Window !== "undefined" && value instanceof Window)) {
            return { $t: "obj", cls: "Window", lazy: true, nk: 0 };
        }
        if (value instanceof Date) return { $t: "date", v: Number.isNaN(value.getTime()) ? "Invalid Date" : String(value) };
        if (value instanceof RegExp) return { $t: "re", v: String(value) };
        if (value instanceof Error || tagOf(value) === "Error") {
            ctx.ancestors.set(value, { node: {}, id: 0 });
            const node = serializeError(value, ctx, depth);
            ctx.ancestors.delete(value);
            return node;
        }

        const isArray = Array.isArray(value);
        const isTyped = !isArray && typeof ArrayBuffer !== "undefined" && ArrayBuffer.isView(value) && tagOf(value) !== "DataView";
        const isMap = value instanceof Map;
        const isSet = value instanceof Set;
        const cls = ctorName(value);
        const size = isArray || isTyped ? value.length : isMap || isSet ? value.size : 0;

        // Seuils : trop profond ou trop de nœuds => aperçu non dépliable.
        if (shallow || depth >= LIMITS.depth || ctx.nodes >= LIMITS.nodes) {
            if (isArray || isTyped) return { $t: "arr", cls, n: size, lazy: true };
            if (isMap) return { $t: "map", n: size, lazy: true };
            if (isSet) return { $t: "set", n: size, lazy: true };
            let nk = 0; try { nk = Object.keys(value).length; } catch { /* ignore */ }
            return { $t: "obj", cls, nk, lazy: true };
        }
        ctx.nodes++;

        let node;
        if (isArray || isTyped) node = { $t: "arr", cls, n: size, items: [] };
        else if (isMap) node = { $t: "map", n: size, entries: [] };
        else if (isSet) node = { $t: "set", n: size, items: [] };
        else if (typeof Promise !== "undefined" && value instanceof Promise) node = { $t: "obj", cls: "Promise", special: "promise", props: [] };
        else node = { $t: "obj", cls, props: [] };

        ctx.ancestors.set(value, { node, id: 0 });
        try {
            if (isArray || isTyped) {
                let i = 0;
                const limit = Math.min(size, LIMITS.items);
                while (i < limit) {
                    if (isArray && !(i in value)) {         // trous d'un tableau creux : « empty × n »
                        let run = 0;
                        while (i + run < size && !(i + run in value)) run++;
                        node.items.push({ $t: "empty", n: run });
                        i += run;
                        continue;
                    }
                    node.items.push(serializeValue(value[i], ctx, depth + 1));
                    i++;
                }
                if (size > LIMITS.items) node.more = size - LIMITS.items;
                const extra = [];
                appendOwnProperties(value, extra, ctx, depth, (key) => typeof key === "string" && (/^\d+$/.test(key) || key === "length"));
                if (extra.length) node.props = extra;
            } else if (isMap) {
                let i = 0;
                for (const [k, v] of value) {
                    if (i++ >= LIMITS.items) { node.more = size - LIMITS.items; break; }
                    node.entries.push([serializeValue(k, ctx, depth + 1), serializeValue(v, ctx, depth + 1)]);
                }
            } else if (isSet) {
                let i = 0;
                for (const v of value) {
                    if (i++ >= LIMITS.items) { node.more = size - LIMITS.items; break; }
                    node.items.push(serializeValue(v, ctx, depth + 1));
                }
            } else {
                const total = appendOwnProperties(value, node.props, ctx, depth);
                if (total > node.props.length) node.more = total - node.props.length;
                if (!node.props.length && cls !== "Object" && cls !== "Promise") {
                    const proto = Object.getPrototypeOf(value);
                    const ctor = proto && Object.getOwnPropertyDescriptor(proto, "constructor")?.value;
                    if (typeof ctor === "function" && isNative(ctor)) appendPlatformProperties(value, node.props, ctx, depth);
                }
                if (tagOf(value) === "Number" || tagOf(value) === "String" || tagOf(value) === "Boolean") {
                    node.prim = serializeValue(value.valueOf(), ctx, depth + 1);
                }
            }
            node.proto = serializeProto(value, ctx, depth);
        } finally {
            ctx.ancestors.delete(value);
        }
        return node;
    }

    function serialize(value) {
        return serializeValue(value, newContext());
    }

    /** Sérialise tous les arguments d'un appel avec un budget de nœuds partagé. */
    function serializeArgs(list) {
        const ctx = newContext();
        return Array.prototype.map.call(list, (value) => {
            ctx.ancestors = new Map();
            return serializeValue(value, ctx);
        });
    }

    /** Pile d'appels sans les cadres internes de la console. */
    function cleanStack(stack, skip) {
        const lines = String(stack || "").split("\n");
        const frames = lines.filter((line) => /^\s*at\s|@/.test(line));
        return frames.slice(skip).join("\n");
    }

    /** Version texte brute d'un message (secours si aucun afficheur riche n'est disponible). */
    function toText(message) {
        const one = (node) => {
            if (node === null) return "null";
            if (typeof node !== "object") return String(node);
            switch (node.$t) {
                case "undef": return "undefined";
                case "num": case "big": case "sym": case "date": case "re": return node.v;
                case "str": return node.v;
                case "fn": return `ƒ ${node.name}(${node.params})`;
                case "err": return node.stack;
                case "arr": return `(${node.n}) [${(node.items || []).map(one).join(", ")}]`;
                case "map": return `Map(${node.n})`;
                case "set": return `Set(${node.n})`;
                case "dom": return node.tag ? `<${node.tag}>` : "#node";
                default: return node.cls && node.cls !== "Object" ? `${node.cls} {…}` : "{…}";
            }
        };
        const parts = (message.args || []).map(one);
        if (message.type === "count") return `${message.label}: ${message.count}`;
        if (message.type === "time") return `${message.label}: ${message.text}`;
        return parts.join(" ");
    }

    const formatDuration = (ms) => (ms >= 1000 ? `${(ms / 1000).toFixed(3)} s` : `${ms.toFixed(3)} ms`);

    /**
     * Remplace les méthodes de « con » par des versions qui postent des messages structurés.
     * @param {Console} con
     * @param {(message: object) => void} post
     * @param {{mirror?: boolean}} options mirror : appelle aussi la console native (aperçu de l'éditeur).
     */
    function install(con, post, { mirror = false } = {}) {
        const native = {};
        for (const name of ["log", "info", "debug", "warn", "error", "trace", "assert", "count", "countReset", "dir",
            "dirxml", "group", "groupCollapsed", "groupEnd", "time", "timeEnd", "timeLog", "clear", "table"]) {
            if (typeof con[name] === "function") native[name] = con[name].bind(con);
        }
        const forward = (name, ...args) => { if (mirror && native[name]) { try { native[name](...args); } catch { /* ignore */ } } };
        const send = (type, extra) => post(Object.assign({ __console: true, type }, extra));

        const counts = new Map();
        const timers = new Map();

        for (const type of ["log", "info", "debug", "warn", "error"]) {
            con[type] = (...args) => { send(type, { args: serializeArgs(args) }); forward(type, ...args); };
        }
        con.trace = (...args) => {
            send("trace", { args: serializeArgs(args), stack: cleanStack(new Error().stack, 1) });
            forward("trace", ...args);
        };
        con.assert = (condition, ...args) => {
            if (!condition) send("assert", { args: serializeArgs(args) });
            forward("assert", condition, ...args);
        };
        con.dir = (value) => { send("dir", { args: serializeArgs([value]) }); forward("dir", value); };
        con.dirxml = (...args) => { send("dirxml", { args: serializeArgs(args) }); forward("dirxml", ...args); };
        con.table = (data, columns) => {
            send("table", {
                args: serializeArgs([data]),
                columns: Array.isArray(columns) ? columns.map(String) : undefined,
            });
            forward("table", data, columns);
        };
        con.group = (...args) => { send("group", { args: serializeArgs(args) }); forward("group", ...args); };
        con.groupCollapsed = (...args) => { send("groupCollapsed", { args: serializeArgs(args) }); forward("groupCollapsed", ...args); };
        con.groupEnd = () => { send("groupEnd"); forward("groupEnd"); };
        con.clear = () => { send("clear"); forward("clear"); };

        con.count = (label = "default") => {
            label = String(label);
            const count = (counts.get(label) ?? 0) + 1;
            counts.set(label, count);
            send("count", { label, count });
            forward("count", label);
        };
        con.countReset = (label = "default") => {
            label = String(label);
            if (counts.has(label)) counts.set(label, 0);
            else send("warn", { args: [`Count for '${label}' does not exist`] });
            forward("countReset", label);
        };

        con.time = (label = "default") => {
            label = String(label);
            if (timers.has(label)) send("warn", { args: [`Timer '${label}' already exists`] });
            else timers.set(label, performance.now());
            forward("time", label);
        };
        const elapsed = (label, type, end, data) => {
            label = String(label);
            if (!timers.has(label)) { send("warn", { args: [`Timer '${label}' does not exist`] }); return; }
            const ms = performance.now() - timers.get(label);
            if (end) timers.delete(label);
            send("time", { label, ms, text: formatDuration(ms), args: serializeArgs(data) });
            forward(type, label, ...data);
        };
        con.timeEnd = (label = "default") => elapsed(label, "timeEnd", true, []);
        con.timeLog = (label = "default", ...data) => elapsed(label, "timeLog", false, data);
    }

    /** Message d'erreur non interceptée (window.onerror) ou de promesse rejetée, au format DevTools. */
    function errorMessage(error, { inPromise = false } = {}) {
        const prefix = inPromise ? "Uncaught (in promise)" : "Uncaught";
        return { __console: true, type: "error", args: [prefix, serialize(error)], uncaught: true };
    }

    root.ConsoleRuntime = { serialize, serializeArgs, install, errorMessage, toText, formatDuration, LIMITS };
})(typeof globalThis !== "undefined" ? globalThis : self);
