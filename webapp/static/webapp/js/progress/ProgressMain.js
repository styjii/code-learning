import { dismiss, setProgress, updateProgress } from "./ProgressUtils.js";

/**
 * Prépare les pages de cours une par une et affiche la progression.
 * Gère l'annulation, les erreurs réseau/serveur et la reprise.
 */
export class ProgressMain {
    /**
     * @param {{total: number, endpoint: string}} options
     */
    constructor({ total, endpoint }) {
        this.ctx = {
            container: document.getElementById("progress-container"),
            bar: document.getElementById("progress-bar"),
            cancelBtn: document.getElementById("cancel-btn"),
            spinner: document.querySelector("#progress-container .spinner"),
            statusText: document.querySelector("#progress-container .progress-status"),
            total,
            endpoint,
            processedCount: 0,
            cancelled: false,
        };
    }

    async loadNext() {
        const ctx = this.ctx;
        if (ctx.cancelled) return;

        try {
            const res = await fetch(`${ctx.endpoint}?index=${ctx.processedCount}`);
            const data = await res.json();

            if (data.status === "ok") {
                ctx.processedCount++;
                updateProgress(ctx, `${data.title} prêt (${ctx.processedCount}/${ctx.total})`, ctx.processedCount, ctx.total);
                requestAnimationFrame(() => this.loadNext());
            } else if (data.status === "done") {
                this.finish();
            } else {
                throw new Error(data.message || "Erreur inconnue");
            }
        } catch (error) {
            this.fail(error);
        }
    }

    finish() {
        const ctx = this.ctx;
        setProgress(ctx.bar, 100);
        ctx.spinner.hidden = true;
        ctx.cancelBtn.hidden = true;
        ctx.statusText.textContent = "Tous les cours sont prêts.";
        dismiss(ctx.container);
    }

    fail(error) {
        const ctx = this.ctx;
        ctx.spinner.hidden = true;
        ctx.statusText.textContent = `Échec de la préparation : ${error.message}`;
        ctx.container.classList.add("is-error");
        ctx.cancelBtn.textContent = "Réessayer";
        ctx.cancelBtn.onclick = () => {
            ctx.container.classList.remove("is-error");
            ctx.spinner.hidden = false;
            ctx.cancelBtn.textContent = "Annuler";
            this.bindCancel();
            this.loadNext();
        };
    }

    bindCancel() {
        const ctx = this.ctx;
        ctx.cancelBtn.onclick = () => {
            ctx.cancelled = true;
            ctx.spinner.hidden = true;
            ctx.cancelBtn.hidden = true;
            ctx.statusText.textContent = "Préparation annulée (les cours se chargeront à l'ouverture).";
            dismiss(ctx.container, 2500);
        };
    }

    start() {
        const ctx = this.ctx;
        if (!ctx.container || !ctx.bar || !ctx.cancelBtn) return;
        this.bindCancel();
        this.loadNext();
    }
}
