/**
 * Exécute du JavaScript dans un Web Worker : isolé de la page (pas d'accès au DOM)
 * et interruptible en cas de boucle infinie.
 *
 * Messages sortants : {type: "console", msg} · {type: "done"} · {type: "error", text, msg, hint?}
 */
const post = (message) => self.postMessage(message);

// Sérialisation et méthodes de console partagées avec l'éditeur HTML/CSS/JS : les valeurs partent sous
// forme d'arbres que la page affiche comme la console de Chrome (voir editor/js/console/). Dans l'iframe
// du DomRunner, le script est déjà chargé par la page.
if (!self.ConsoleRuntime) importScripts("../../../editor/js/console/console-runtime.js");
ConsoleRuntime.install(console, (message) => post({ type: "console", msg: message }));

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
        msg: ConsoleRuntime.errorMessage(error),
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
