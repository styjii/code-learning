#!/usr/bin/env bash
# Vérifications d'une Pull Request avec GitHub CLI (gh).
#
# Usage : .github/scripts/pr-checks.sh <numéro-de-PR>
# Variables : GH_TOKEN et GH_REPO (obligatoires, « propriétaire/dépôt »),
#             LABELS_ENABLED=1 pour poser des étiquettes (0 pour les PR venant d'un fork : jeton en lecture seule),
#             REPORT_FILE (défaut : pr-report.md).
# Code de sortie : 1 si une vérification bloquante échoue, 0 sinon (les avertissements ne bloquent pas).
set -euo pipefail

PR="${1:?numéro de Pull Request requis}"
: "${GH_REPO:?GH_REPO requis}"
REPORT="${REPORT_FILE:-pr-report.md}"

errors=0
warnings=0
report=""
ok()   { report+="- ✅ $1"$'\n'; }
warn() { report+="- ⚠️ $1"$'\n'; warnings=$((warnings + 1)); }
fail() { report+="- ❌ $1"$'\n'; errors=$((errors + 1)); }

# --- Données de la PR (le titre et le corps ne sont jamais passés au shell comme code) ---
title=$(gh pr view "$PR" --json title --jq .title)
body=$(gh pr view "$PR" --json body --jq .body)
read -r additions deletions changed is_draft < <(
    gh pr view "$PR" --json additions,deletions,changedFiles,isDraft \
        --jq '[.additions, .deletions, .changedFiles, .isDraft] | @tsv'
)
# L'API pagine : fonctionne aussi pour les très grosses PR (« gh pr diff » échoue au-delà de 20 000 lignes).
files=$(gh api --paginate "repos/${GH_REPO}/pulls/${PR}/files" --jq '.[].filename')

has() { grep -Eq "$1" <<<"$files"; }

# --- 1. Fichiers qui ne doivent jamais être versionnés (bloquant) ---
forbidden=$(grep -E '(^|/)(\.env|db\.sqlite3)$|__pycache__/|\.pyc$' <<<"$files" || true)
if [ -n "$forbidden" ]; then
    fail "Fichiers à ne pas versionner (secrets, base de données, caches) : $(tr '\n' ' ' <<<"$forbidden")"
else
    ok "Aucun fichier sensible (\`.env\`, \`db.sqlite3\`, caches Python)."
fi

# --- 2. Titre et description ---
if [ "${#title}" -lt 10 ]; then
    warn "Titre trop court : décrivez le changement en au moins 10 caractères."
else
    ok "Titre renseigné."
fi
if [ -z "${body//[[:space:]]/}" ]; then
    warn "Description vide : expliquez le pourquoi et comment tester."
else
    ok "Description renseignée."
fi

# --- 3. Taille ---
total=$((additions + deletions))
if [ "$changed" -gt 50 ] || [ "$total" -gt 1500 ]; then
    warn "PR volumineuse ($changed fichiers, $total lignes modifiées) : elle sera difficile à relire, pensez à la scinder."
else
    ok "Taille raisonnable ($changed fichiers, $total lignes modifiées)."
fi

# --- 4. Code modifié sans test ---
tests_re='(^|/)(tests?\.py|test_[^/]*\.py|tests/)'
code=$(grep -E '\.(py|js)$' <<<"$files" | grep -Ev "$tests_re|/migrations/|^\.github/" || true)
if [ -n "$code" ] && ! has "$tests_re"; then
    warn "Du code a changé mais aucun test n'a été ajouté ou modifié."
elif [ -n "$code" ]; then
    ok "Le code modifié s'accompagne de tests."
fi

[ "$is_draft" = "true" ] && report+="- ℹ️ PR en brouillon."$'\n'

# --- 5. Étiquettes selon les dossiers touchés ---
labels=()
has '^editor/'                           && labels+=("editor")
has '^(language|core)/'                  && labels+=("cours")
has '^(webapp|accounts|config|templates|static)/' && labels+=("site")
has '^[^/]+\.md$|^language/topics/'      && labels+=("docs")
has "$tests_re"                          && labels+=("tests")
has '^\.github/'                         && labels+=("ci")

if [ "${#labels[@]}" -gt 0 ] && [ "${LABELS_ENABLED:-0}" = "1" ]; then
    for label in "${labels[@]}"; do
        gh label create "$label" --force --color "1d76db" --description "Ajoutée automatiquement" >/dev/null
        gh pr edit "$PR" --add-label "$label" >/dev/null
    done
    report+="- 🏷️ Étiquettes : $(IFS=,; echo "${labels[*]}")"$'\n'
fi

# --- Rapport ---
{
    echo "### Vérifications de la Pull Request"
    echo
    printf '%s' "$report"
    echo
    echo "_${errors} erreur(s), ${warnings} avertissement(s)._"
} > "$REPORT"

cat "$REPORT"
[ -n "${GITHUB_STEP_SUMMARY:-}" ] && cat "$REPORT" >> "$GITHUB_STEP_SUMMARY"
exit $((errors > 0 ? 1 : 0))
