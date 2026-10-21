/**
 * Améliorations du contenu Markdown : ancres de titres, tableaux défilants, liens externes.
 */
export class MarkdownEnhancer {
    static init() {
        MarkdownEnhancer.addHeadingAnchors();
        MarkdownEnhancer.wrapTables();
        MarkdownEnhancer.markExternalLinks();
    }

    static addHeadingAnchors() {
        document.querySelectorAll(".markdown-body :is(h2, h3, h4)").forEach((heading) => {
            if (!heading.id || heading.classList.contains("section-title")) return;
            const anchor = document.createElement("a");
            anchor.className = "heading-anchor";
            anchor.href = `#${heading.id}`;
            anchor.setAttribute("aria-label", "Lien vers ce titre");
            anchor.textContent = "#";
            heading.appendChild(anchor);
        });
    }

    static wrapTables() {
        document.querySelectorAll(".markdown-body table").forEach((table) => {
            if (table.parentElement.classList.contains("table-scroll")) return;
            const wrapper = document.createElement("div");
            wrapper.className = "table-scroll";
            table.replaceWith(wrapper);
            wrapper.appendChild(table);
        });
    }

    static markExternalLinks() {
        document.querySelectorAll('.markdown-body a[href^="http"]').forEach((link) => {
            link.target = "_blank";
            link.rel = "noopener noreferrer";
        });
    }
}
