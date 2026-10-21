/**
 * Gestion du thème clair / sombre.
 *
 * - Le thème initial est posé par un script inline dans <head> (voir base.html).
 * - Ce module branche le bouton #toggle-theme, mémorise le choix et
 *   émet l'événement « themechange » (utilisé par l'éditeur pour Monaco).
 */
const THEME_KEY = "theme";
const root = document.documentElement;

export function getTheme() {
    return root.getAttribute("data-theme") === "light" ? "light" : "dark";
}

export function setTheme(theme) {
    root.setAttribute("data-theme", theme);
    try {
        localStorage.setItem(THEME_KEY, theme);
    } catch {
        /* stockage indisponible (navigation privée) : on ignore */
    }
    document.dispatchEvent(new CustomEvent("themechange", { detail: theme }));
}

export function toggleTheme() {
    setTheme(getTheme() === "dark" ? "light" : "dark");
}

export function initTheme() {
    document.getElementById("toggle-theme")?.addEventListener("click", toggleTheme);
}
