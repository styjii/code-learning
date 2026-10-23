/**
 * Exécute du JavaScript dans un Web Worker : isolé de la page (pas d'accès au DOM)
 * et interruptible en cas de boucle infinie.
 *
 * Messages sortants : {type: "log", kind, text} · {type: "done"} · {type: "error", text, hint?}
 */
const post = (message) => self.postMessage(message);
const quote = (s) => `'${s.replace(/\\/g, "\\\\").replace(/'/g, "\\'")}'`;

function inspect(value, depth = 0, seen = new Set()) {
    switch (typeof value) {
        case "string": return depth ? quote(value) : value;
        case "bigint": return `${value}n`;
        case "symbol": return value.toString();
        case "function": return `[Function${value.name ? `: ${value.name}` : " (anonymous)"}]`;
        case "undefined": return "undefined";
        case "object": break;
        default: return String(value);
    }
    if (value === null) return "null";
    if (value instanceof Error) return depth ? `[${value.name}: ${value.message}]` : `${value.name}: ${value.message}`;
    if (seen.has(value)) return "[Circular]";
    if (depth > 3) return Array.isArray(value) ? "[Array]" : "[Object]";

    seen.add(value);
    let out;
    if (Array.isArray(value)) {
        const items = value.slice(0, 100).map((x) => inspect(x, depth + 1, seen));
        if (value.length > 100) items.push(`… ${value.length - 100} de plus`);
        out = items.length ? `[ ${items.join(", ")} ]` : "[]";
    } else if (value instanceof Map) {
        out = `Map(${value.size}) { ${[...value].map(([k, v]) => `${inspect(k, depth + 1, seen)} => ${inspect(v, depth + 1, seen)}`).join(", ")} }`;
    } else if (value instanceof Set) {
        out = `Set(${value.size}) { ${[...value].map((x) => inspect(x, depth + 1, seen)).join(", ")} }`;
    } else if (value instanceof Date) {
        out = value.toISOString();
    } else {
        const keys = Object.keys(value);
        const name = value.constructor && value.constructor.name !== "Object" ? `${value.constructor.name} ` : "";
        const props = keys.map((k) => `${/^[A-Za-z_$][\w$]*$/.test(k) ? k : quote(k)}: ${inspect(value[k], depth + 1, seen)}`);
        out = keys.length ? `${name}{ ${props.join(", ")} }` : `${name}{}`;
    }
    seen.delete(value);
    return out;
}

const format = (args) => args.map((a) => (typeof a === "string" ? a : inspect(a))).join(" ");

for (const [method, kind] of [["log", "out"], ["info", "out"], ["debug", "out"], ["trace", "out"],
                              ["dir", "out"], ["table", "out"], ["warn", "warn"], ["error", "err"]]) {
    console[method] = (...args) => post({ type: "log", kind, text: format(args) });
}
console.clear = () => {};
console.group = (...args) => { if (args.length) console.log(...args); };
console.groupEnd = () => {};

// console.time/count/assert : sans ça, leur sortie partait dans la console du worker (invisible),
// alors que les exemples async/await s'en servent pour comparer séquentiel et parallèle.
const chronos = new Map();
const compteurs = new Map();
const duree = (label) => {
    if (!chronos.has(label)) return null;
    const ms = performance.now() - chronos.get(label);
    return ms >= 1000 ? `${(ms / 1000).toFixed(3)} s` : `${ms.toFixed(3)} ms`;
};
console.time = (label = "default") => { chronos.set(String(label), performance.now()); };
console.timeLog = (label = "default", ...data) => {
    const d = duree(String(label));
    if (d === null) console.warn(`Le minuteur « ${label} » n'existe pas.`);
    else console.log(`${label}: ${d}`, ...data);
};
console.timeEnd = (label = "default") => {
    console.timeLog(label);
    chronos.delete(String(label));
};
console.count = (label = "default") => {
    const n = (compteurs.get(String(label)) ?? 0) + 1;
    compteurs.set(String(label), n);
    console.log(`${label}: ${n}`);
};
console.countReset = (label = "default") => { compteurs.delete(String(label)); };
console.assert = (condition, ...args) => {
    if (!condition) console.error(args.length ? `Assertion échouée : ${format(args)}` : "Assertion échouée");
};

// Fonctions du navigateur sans équivalent dans un worker
self.alert = (message) => console.log(`[alert] ${message}`);
self.confirm = () => false;
self.prompt = () => { console.warn("prompt() n'est pas disponible dans cet exécuteur."); return null; };

// Suivi des minuteurs : on attend leur fin avant de déclarer l'exécution terminée.
const active = new Set();
const { setTimeout: nativeSetTimeout, clearTimeout: nativeClearTimeout,
        setInterval: nativeSetInterval, clearInterval: nativeClearInterval } = self;

self.setTimeout = (fn, ms, ...args) => {
    if (typeof fn !== "function") return nativeSetTimeout(fn, ms);
    const id = nativeSetTimeout((...a) => { active.delete(id); fn(...a); }, ms, ...args);
    active.add(id);
    return id;
};
self.setInterval = (fn, ms, ...args) => {
    const id = nativeSetInterval(fn, ms, ...args);
    active.add(id);
    return id;
};
self.clearTimeout = (id) => { active.delete(id); nativeClearTimeout(id); };
self.clearInterval = (id) => { active.delete(id); nativeClearInterval(id); };

// Suivi des opérations asynchrones en cours (requêtes réseau et lecture de leur corps).
// Sans cela, un code comme « (async () => { await fetch(url) })(); » rend la main aussitôt, les
// minuteurs sont vides, « done » est envoyé et le worker est détruit avant la réponse : le
// résultat n'apparaît jamais. On renvoie la promesse issue de finally() : si personne ne la gère,
// l'erreur reste signalée comme « unhandledrejection » (et n'est pas avalée par le suivi).
let pending = 0;
const track = (promise) => {
    pending++;
    return promise.finally(() => { pending--; });
};
if (typeof self.fetch === "function") {
    const nativeFetch = self.fetch.bind(self);
    self.fetch = (...args) => track(nativeFetch(...args));
}
if (typeof Response === "function") {
    for (const method of ["json", "text", "blob", "arrayBuffer", "formData"]) {
        const native = Response.prototype[method];
        if (typeof native !== "function") continue;
        Response.prototype[method] = function (...args) { return track(native.apply(this, args)); };
    }
}

function reportError(error) {
    const name = error?.name ?? "Error";
    const message = error?.message ?? String(error);
    const needsDom = typeof document === "undefined" && /\b(document|window|localStorage|sessionStorage|navigator)\b/.test(message);
    post({
        type: "error",
        text: `${name}: ${message}`,
        hint: needsDom ? "Ce code utilise le navigateur (DOM) : essayez-le dans l'éditeur HTML/CSS/JS." : undefined,
    });
}

self.addEventListener("unhandledrejection", (event) => reportError(event.reason));
self.addEventListener("error", (event) => { event.preventDefault(); reportError(event.error ?? new Error(event.message)); });

self.onmessage = async ({ data: { code } }) => {
    const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;
    try {
        const module = { exports: {} };
        await new AsyncFunction("exports", "module", code)(module.exports, module);
        const waitForTimers = () => (active.size === 0 && pending === 0 ? post({ type: "done" }) : nativeSetTimeout(waitForTimers, 30));
        waitForTimers();
    } catch (error) {
        reportError(error);
    }
};
