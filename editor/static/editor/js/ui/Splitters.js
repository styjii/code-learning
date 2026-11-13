/**
 * Séparateurs ajustables des éditeurs Web et TypeScript :
 *   - « split-main »    : entre le panneau de code et le panneau de résultat ;
 *   - « split-console » : entre l'aperçu et la console du bas.
 *
 * Glisser-déposer (souris, doigt, stylet), clavier (flèches) et double clic pour revenir à la taille par défaut.
 * Les tailles sont gardées en proportion (localStorage) et recalées dans les bornes quand la fenêtre change.
 * Le verrou (menu « Disposition et délai ») désactive tout redimensionnement, sans toucher aux tailles actuelles.
 * Sur l'éditeur Python (pas de séparateurs dans la page) l'initialisation ne fait rien.
 */
const $ = (id) => document.getElementById(id);

const KEYS = { main: "editor-split-main", console: "editor-split-console", lock: "editor-resize-locked" };
const MIN_PANE = 140;      // px : taille minimale du panneau de code et du panneau de résultat
const MIN_CONSOLE = 130;   // px : console, dans son état le plus bas
const MIN_PREVIEW = 160;   // px : aperçu, quand la console est agrandie à la main
const KEY_STEP = 24;       // px par appui sur une flèche

const read = (key) => { try { return localStorage.getItem(key); } catch { return null; } };
const write = (key, value) => {
    try { if (value == null) localStorage.removeItem(key); else localStorage.setItem(key, value); } catch { /* stockage bloqué */ }
};
const clamp = (value, low, high) => Math.min(Math.max(value, low), high);
const storedRatio = (key) => { const value = parseFloat(read(key)); return value > 0.05 && value < 0.95 ? value : null; };

export class Splitters {
    static #locked = false;
    static #handles = [];

    static init() {
        const main = $("main-editor");
        const output = $("output-container");
        const mainHandle = $("split-main");
        const consoleHandle = $("split-console");
        const editor = $("editor-container");
        const dock = $("console-dock");
        if (!main || !output || !editor || !dock || !mainHandle || !consoleHandle) return;

        Splitters.#handles = [mainHandle, consoleHandle];

        Splitters.#bind(mainHandle, {
            key: KEYS.main,
            axis: () => (getComputedStyle(main).flexDirection.startsWith("row") ? "x" : "y"),
            // Taille du panneau de code = distance entre le bord du conteneur et le pointeur.
            pointerSize: (event, axis) => {
                const rect = main.getBoundingClientRect();
                return axis === "x" ? event.clientX - rect.left : event.clientY - rect.top;
            },
            current: (axis) => {
                const rect = editor.getBoundingClientRect();
                return axis === "x" ? rect.width : rect.height;
            },
            total: (axis) => {
                const rect = main.getBoundingClientRect();
                return axis === "x" ? rect.width : rect.height;
            },
            bounds: (total) => [MIN_PANE, total - MIN_PANE],
            // Flèches : la poignée suit la flèche (droite / bas = le code grandit).
            keys: (axis) => (axis === "x" ? { grow: "ArrowRight", shrink: "ArrowLeft" } : { grow: "ArrowDown", shrink: "ArrowUp" }),
            apply: (ratio) => {
                main.style.setProperty("--editor-size", `${(ratio * 100).toFixed(3)}%`);
                main.dataset.sized = "";
            },
            clear: () => {
                main.style.removeProperty("--editor-size");
                delete main.dataset.sized;
            },
            observe: main,
        });

        Splitters.#bind(consoleHandle, {
            key: KEYS.console,
            axis: () => "y",
            // Taille de la console = distance entre le pointeur et le bas du panneau de résultat.
            pointerSize: (event) => output.getBoundingClientRect().bottom - event.clientY,
            current: () => dock.getBoundingClientRect().height,
            total: () => output.getBoundingClientRect().height,
            bounds: (total) => [MIN_CONSOLE, total - ($("control-button")?.offsetHeight ?? 0) - MIN_PREVIEW],
            keys: () => ({ grow: "ArrowUp", shrink: "ArrowDown" }),
            apply: (ratio) => output.style.setProperty("--console-size", `${(ratio * 100).toFixed(3)}%`),
            clear: () => output.style.removeProperty("--console-size"),
            observe: output,
        });

        $("lock-resize")?.addEventListener("click", () => Splitters.setLocked(!Splitters.#locked));
        Splitters.setLocked(read(KEYS.lock) === "1", false);
    }

    static get locked() {
        return Splitters.#locked;
    }

    /** Verrouille (true) ou déverrouille (false) le redimensionnement ; le choix est mémorisé. */
    static setLocked(locked, persist = true) {
        Splitters.#locked = locked;
        for (const handle of Splitters.#handles) {
            handle.setAttribute("aria-disabled", String(locked));
            handle.tabIndex = locked ? -1 : 0;
        }
        const item = $("lock-resize");
        if (item) {
            item.setAttribute("aria-checked", String(locked));
            const pill = item.querySelector("[data-lock-indicator]");
            if (pill) pill.textContent = locked ? "Oui" : "Non";
        }
        if (persist) write(KEYS.lock, locked ? "1" : "0");
    }

    static #bind(handle, spec) {
        let ratio = storedRatio(spec.key);

        const setRatio = (value, persist) => {
            ratio = value;
            spec.apply(ratio);
            handle.setAttribute("aria-valuenow", String(Math.round(ratio * 100)));
            if (persist) write(spec.key, ratio.toFixed(4));
        };

        // Remet la taille mémorisée dans les bornes actuelles (rotation de l'écran, fenêtre plus petite).
        const refresh = () => {
            const axis = spec.axis();
            handle.dataset.axis = axis;
            handle.setAttribute("aria-orientation", axis === "x" ? "vertical" : "horizontal");
            if (ratio == null) return;
            const total = spec.total(axis);
            const [low, high] = spec.bounds(total);
            if (!total || high < low) return;
            setRatio(clamp(ratio, low / total, high / total), false);
        };

        const moveTo = (size, persist) => {
            const axis = spec.axis();
            const total = spec.total(axis);
            const [low, high] = spec.bounds(total);
            if (!total || high < low) return;
            setRatio(clamp(size, low, high) / total, persist);
        };

        handle.addEventListener("pointerdown", (event) => {
            if (Splitters.#locked || event.button !== 0) return;
            event.preventDefault();
            const axis = spec.axis();
            handle.setPointerCapture(event.pointerId);
            handle.dataset.dragging = "";
            document.body.dataset.resizing = axis;

            const move = (moveEvent) => moveTo(spec.pointerSize(moveEvent, axis), false);
            const end = () => {
                handle.removeEventListener("pointermove", move);
                handle.removeEventListener("pointerup", end);
                handle.removeEventListener("pointercancel", end);
                delete handle.dataset.dragging;
                delete document.body.dataset.resizing;
                if (ratio != null) write(spec.key, ratio.toFixed(4));
            };
            handle.addEventListener("pointermove", move);
            handle.addEventListener("pointerup", end);
            handle.addEventListener("pointercancel", end);
        });

        handle.addEventListener("keydown", (event) => {
            if (Splitters.#locked) return;
            const axis = spec.axis();
            const { grow, shrink } = spec.keys(axis);
            if (event.key !== grow && event.key !== shrink) return;
            event.preventDefault();
            moveTo(spec.current(axis) + (event.key === grow ? KEY_STEP : -KEY_STEP), true);
        });

        handle.addEventListener("dblclick", () => {
            if (Splitters.#locked) return;
            ratio = null;
            spec.clear();
            handle.removeAttribute("aria-valuenow");
            write(spec.key, null);
        });

        new ResizeObserver(refresh).observe(spec.observe);
        if (ratio != null) spec.apply(ratio);
        refresh();
    }
}
