import { CodeBlockUtils } from "./codeBlockUtils/CodeBlockUtils.js";
import { MarkdownEnhancer } from "./markdownEnhancer/MarkdownEnhancer.js";
import { PageOutline } from "./outline/PageOutline.js";
import { RunnableBlocks } from "./runner/RunnableBlocks.js";
import { ScrollToTop } from "./scroll/ScrollToTop.js";
import { SearchDialog } from "./search/SearchDialog.js";
import { SectionNav } from "./sections/SectionNav.js";
import { MenuControls } from "./ui/MenuControls.js";

/** Initialise les modules de la page de cours une fois le DOM prêt. */
document.addEventListener("DOMContentLoaded", () => {
    MenuControls.init();
    ScrollToTop.init();
    MarkdownEnhancer.init();
    CodeBlockUtils.initCodeBlockHeaders();
    RunnableBlocks.init();

    const sections = new SectionNav();
    new PageOutline().init();      // écoute « section:change » : à brancher avant sections.init()
    new SearchDialog(sections).init();
    sections.init();
});
