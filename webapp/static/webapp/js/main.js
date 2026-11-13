/**
 * Point d'entrée de l'accueil : navigation, catalogue à onglets, animations d'apparition,
 * éditeur de démonstration et préparation du contenu.
 */
import { CatalogTabs } from "./catalog/CatalogTabs.js";
import { HeroEditor } from "./effects/HeroEditor.js";
import { ScrollReveal } from "./effects/ScrollReveal.js";
import { NavMenu } from "./ui/NavMenu.js";
import { ProgressMain } from "./progress/ProgressMain.js";

document.addEventListener("DOMContentLoaded", () => {
    NavMenu.init();
    CatalogTabs.init();
    HeroEditor.init();
    ScrollReveal.init();

    const container = document.getElementById("progress-container");
    if (container) {
        const total = parseInt(container.dataset.total ?? "0", 10);
        new ProgressMain({ total, endpoint: container.dataset.endpoint }).start();
    }
});
