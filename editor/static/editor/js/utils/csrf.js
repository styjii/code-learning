/**
 * Ajoute automatiquement le jeton CSRF de Django aux requêtes d'écriture vers le même site.
 *
 * Le cookie « csrftoken » est posé par la page de l'éditeur (ensure_csrf_cookie). Les appels
 * fetch() existants n'ont ainsi pas besoin d'être modifiés un par un.
 */
const SAFE_METHODS = new Set(["GET", "HEAD", "OPTIONS", "TRACE"]);

function csrfToken() {
    const cookie = document.cookie.split("; ").find((row) => row.startsWith("csrftoken="));
    return cookie ? decodeURIComponent(cookie.split("=")[1]) : "";
}

const nativeFetch = window.fetch.bind(window);

window.fetch = (input, init = {}) => {
    const method = (init.method ?? (input instanceof Request ? input.method : "GET")).toUpperCase();
    if (!SAFE_METHODS.has(method)) {
        const headers = new Headers(init.headers ?? (input instanceof Request ? input.headers : undefined));
        if (!headers.has("X-CSRFToken")) headers.set("X-CSRFToken", csrfToken());
        init = { ...init, headers, credentials: "same-origin" };
    }
    return nativeFetch(input, init);
};
