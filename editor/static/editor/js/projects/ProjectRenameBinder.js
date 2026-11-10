/**
 * Interface de renommage du projet courant dans la modale « Projets » : un crayon placé à côté du
 * libellé ouvre un champ de saisie (Entrée ou ✓ pour valider, Échap ou ✕ pour annuler).
 *
 * Partagé par l'éditeur Web et l'éditeur TypeScript : le gestionnaire de projets passé à ``bind``
 * doit exposer ``rename(newName)`` -> ``{ ok, unchanged?, message? }``.
 */
export class ProjectRenameBinder {
    /**
     * @param {{rename: (name: string) => Promise<{ok: boolean, unchanged?: boolean, message?: string}>}} manager
     */
    static bind(manager) {
        const modal = document.getElementById("project-controls");
        const view = document.getElementById("project-current");
        const label = document.getElementById("project-current-name");
        const row = document.getElementById("rename-row");
        const input = document.getElementById("rename-input");
        const openBtn = document.getElementById("rename-btn");
        const confirmBtn = document.getElementById("rename-confirm");
        const cancelBtn = document.getElementById("rename-cancel");
        const feedback = document.getElementById("rename-feedback");
        const success = document.getElementById("rename-success");
        if (!view || !row || !input || !openBtn) return;

        let busy = false;

        const showError = (message) => {
            feedback.textContent = message;
            feedback.style.display = "block";
            success.style.display = "none";
        };
        const clearMessages = () => {
            feedback.style.display = "none";
            success.style.display = "none";
        };

        const startEditing = () => {
            clearMessages();
            input.value = label.textContent;
            view.hidden = true;
            row.hidden = false;
            input.focus();
            input.select();
        };

        const stopEditing = () => {
            row.hidden = true;
            view.hidden = false;
        };

        const submit = async () => {
            if (busy) return; // Entrée + clic rapprochés : un seul PATCH
            busy = true;
            confirmBtn.disabled = true;
            try {
                const result = await manager.rename(input.value);
                if (!result.ok) {
                    showError(result.message ?? "Renommage impossible. Réessayez.");
                    input.focus();
                    return;
                }
                stopEditing();
                if (!result.unchanged) {
                    feedback.style.display = "none";
                    success.style.display = "block";
                }
                openBtn.focus();
            } finally {
                busy = false;
                confirmBtn.disabled = false;
            }
        };

        openBtn.addEventListener("click", startEditing);
        confirmBtn.addEventListener("click", submit);
        cancelBtn.addEventListener("click", () => { stopEditing(); clearMessages(); openBtn.focus(); });

        input.addEventListener("keydown", (e) => {
            if (e.key === "Enter") {
                e.preventDefault();
                submit();
            } else if (e.key === "Escape") {
                // Échap annule d'abord l'édition ; la modale, elle, ne se ferme pas (ModalEvents écoute window).
                e.preventDefault();
                e.stopPropagation();
                stopEditing();
                clearMessages();
                openBtn.focus();
            }
        });

        // Changement de projet (liste, création, suppression) : l'édition en cours ne concerne plus le bon projet.
        // Le renommage réussi déclenche aussi cet événement ; stopEditing est alors sans effet de bord.
        document.addEventListener("project:current-changed", () => {
            if (!busy) { stopEditing(); }
        });

        // Fermeture de la modale : on la rouvre toujours en mode lecture, sans message périmé.
        if (modal) {
            new MutationObserver(() => {
                if (!modal.classList.contains("active")) { stopEditing(); clearMessages(); }
            }).observe(modal, { attributes: true, attributeFilter: ["class"] });
        }
    }
}
