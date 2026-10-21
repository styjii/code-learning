/**
 * Utilitaires d'affichage de la progression.
 */

/** @param {HTMLElement} bar @param {number} percent valeur de 0 à 100 */
export function setProgress(bar, percent) {
    bar.style.width = `${Math.min(Math.max(percent, 0), 100)}%`;
}

/** Met à jour la barre et le texte d'état. */
export function updateProgress(ctx, message, current, total) {
    ctx.statusText.textContent = message;
    setProgress(ctx.bar, total ? Math.round((current / total) * 100) : 0);
}

/** Masque le bandeau avec un fondu puis le retire du DOM. */
export function dismiss(container, delay = 1500) {
    setTimeout(() => {
        container.classList.add("is-leaving");
        setTimeout(() => container.remove(), 400);
    }, delay);
}
