/**
 * Éditeur de démonstration du hero : suit le pointeur (reflet lumineux via --mx / --my, une mise à jour par image)
 * et rend l'aperçu interactif : le bouton « Découvrir » incrémente le compteur du composant affiché.
 * La lévitation et le halo au survol sont purement CSS (voir style.css).
 */
export class HeroEditor {
    static init() {
        const ide = document.querySelector("[data-ide]");
        if (!ide) return;

        const finePointer = matchMedia("(hover: hover) and (pointer: fine)").matches;
        if (finePointer) {
            let frame = 0;
            ide.addEventListener("pointermove", (event) => {
                if (frame) return;
                frame = requestAnimationFrame(() => {
                    frame = 0;
                    const rect = ide.getBoundingClientRect();
                    ide.style.setProperty("--mx", `${(((event.clientX - rect.left) / rect.width) * 100).toFixed(1)}%`);
                    ide.style.setProperty("--my", `${(((event.clientY - rect.top) / rect.height) * 100).toFixed(1)}%`);
                });
            });
        }

        const button = ide.querySelector("[data-ide-cta]");
        const label = ide.querySelector("[data-ide-count]");
        let count = 0;
        button?.addEventListener("click", () => {
            count += 1;
            if (!label) return;
            label.hidden = false;
            label.textContent = `Compteur : ${count}`;
            label.classList.remove("is-pop");
            void label.offsetWidth;
            label.classList.add("is-pop");
        });
    }
}
