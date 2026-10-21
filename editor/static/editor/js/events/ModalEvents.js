/**
 * ModalEvents handles custom modal open/close interactions:
 * - Opens on button click
 * - Closes on close button, Escape key, or overlay click
 * - Updates ZIP file input display
 */
export class ModalEvents {
    /**
     * Binds modal behavior and file input name display updates.
     */
    static bind() {
        const openButtons = document.querySelectorAll('[data-toggle="custom-modal"]');

        openButtons.forEach((btn) => {
            const targetId = btn.getAttribute("data-target");
            const modalOverlay = document.querySelector(targetId);
            const modal = modalOverlay.querySelector(".custom-modal");
            const modalHeader = modal.querySelector(".custom-modal-header");
            const closeBtn = modalHeader.querySelector(".custom-modal-close");

            btn.addEventListener("click", () => modalOverlay.classList.add("active"));
            closeBtn.addEventListener("click", () => modalOverlay.classList.remove("active"));

            window.addEventListener("keydown", (e) => {
                if (e.key === "Escape") modalOverlay.classList.remove("active");
            });

            window.addEventListener("click", (e) => {
                if (e.target === modalOverlay) modalOverlay.classList.remove("active");
            });

            const zipInput = document.getElementById("zip-input");
            const fileNameSpan = document.getElementById("file-name");
            if (zipInput && fileNameSpan) {
                zipInput.addEventListener("change", function () {
                    fileNameSpan.textContent = this.files.length > 0 ? this.files[0].name : "Aucun fichier";
                });
            }
        });
    }
}
