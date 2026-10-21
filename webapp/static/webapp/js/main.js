/**
 * Point d'entrée de l'accueil : filtre du catalogue + préparation du contenu.
 */
import { CourseFilter } from "./filter/CourseFilter.js";
import { ProgressMain } from "./progress/ProgressMain.js";

document.addEventListener("DOMContentLoaded", () => {
    CourseFilter.init();

    const container = document.getElementById("progress-container");
    if (container) {
        const total = parseInt(container.dataset.total ?? "0", 10);
        new ProgressMain({ total, endpoint: container.dataset.endpoint }).start();
    }
});
