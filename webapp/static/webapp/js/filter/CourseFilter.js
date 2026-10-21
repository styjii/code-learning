/**
 * Filtre le catalogue de cours par catégorie et par texte.
 */
export class CourseFilter {
    static init() {
        const input = document.getElementById("course-search");
        const chips = Array.from(document.querySelectorAll(".chip"));
        const groups = Array.from(document.querySelectorAll(".catalog-group"));
        const empty = document.getElementById("no-results");
        if (!input || !groups.length) return;

        let category = "all";

        const normalize = (text) =>
            text.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");

        const apply = () => {
            const query = normalize(input.value.trim());
            let visibleTotal = 0;

            groups.forEach((group) => {
                const inCategory = category === "all" || group.dataset.category === category;
                let visible = 0;

                group.querySelectorAll(".card").forEach((card) => {
                    const match = inCategory && normalize(card.dataset.search).includes(query);
                    card.hidden = !match;
                    if (match) visible++;
                });

                group.hidden = visible === 0;
                visibleTotal += visible;
            });

            if (empty) empty.hidden = visibleTotal > 0;
        };

        input.addEventListener("input", apply);
        chips.forEach((chip) => {
            chip.addEventListener("click", () => {
                category = chip.dataset.filter;
                chips.forEach((c) => c.classList.toggle("is-active", c === chip));
                apply();
            });
        });
    }
}
