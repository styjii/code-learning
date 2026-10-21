# 🟨 Projets JavaScript en ligne de commande

> Deux petits projets pour s'entraîner aux bases de JavaScript : un **jeu de devinette** et une **liste de tâches**. Le code est écrit en JavaScript moderne (ES2022+) et fonctionne aussi bien dans le **navigateur** que dans **Node.js**.

## 📑 Sommaire

1. [Avant de commencer : les contextes d'exécution](#1-avant-de-commencer--les-contextes-dexécution)
2. [Module partagé : `utils.js`](#2-module-partagé--utilsjs)
3. [Projet 1 : le jeu de devinette](#3-projet-1--le-jeu-de-devinette)
4. [Projet 2 : la liste de tâches](#4-projet-2--la-liste-de-tâches)
5. [Concepts abordés](#5-concepts-abordés)
6. [Pour aller plus loin](#6-pour-aller-plus-loin)

---

## 1. Avant de commencer : les contextes d'exécution

L'original utilisait la fonction `prompt()`. Or **`prompt()` n'existe que dans le navigateur** : dans Node.js, le code planterait avec `ReferenceError: prompt is not defined`. Le même code JavaScript se comporte donc différemment selon son **contexte d'exécution** :

| | 🌐 Navigateur | 🟢 Node.js |
| --- | --- | --- |
| Saisie utilisateur | `window.prompt()` (boîte de dialogue) | module `node:readline/promises` |
| Affichage | `console.log()` → console des outils de développement (F12) | `console.log()` → terminal |
| Objet global | `window` | `globalThis` / `process` |
| Modules ES | `<script type="module">` | `"type": "module"` dans `package.json` |
| Stockage | `localStorage` | module `node:fs` |

> 💡 Pour ne pas dupliquer cette différence dans chaque projet, elle est **isolée dans un seul fichier** (`utils.js`, section suivante). Les deux projets l'importent et restent identiques dans les deux contextes.

### Prérequis et lancement

**Dans Node.js** (version 20 ou plus récente, c'est-à-dire une version LTS actuelle) :

```text
mon-projet/
├── package.json
├── utils.js
├── jeu.js
└── taches.js
```

```json
{
    "type": "module"
}
```

```bash
node jeu.js      # Jeu de devinette
node taches.js   # Liste de tâches
```

**Dans le navigateur** :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Projets JavaScript</title>
</head>
<body>
    <p>Ouvrez la console (F12) et répondez aux boîtes de dialogue.</p>
    <script type="module" src="jeu.js"></script>
</body>
</html>
```

> ⚠️ Les modules ES sont bloqués si la page est ouverte directement (`file://`). Servez le dossier avec un petit serveur local, par exemple `npx serve` ou `python -m http.server`, puis ouvrez `http://localhost:...`.

---

## 2. Module partagé : `utils.js`

Ce module regroupe tout ce qui est commun aux deux projets : **poser une question** (quel que soit le contexte) et **valider un nombre entier**.

```js
// utils.js : fonctions communes aux deux projets

const estNavigateur =
    typeof window !== "undefined" && typeof window.prompt === "function";

let interfaceLecture = null; // Interface readline (Node.js uniquement)
let fermeture = null;        // Promesse résolue quand l'entrée se ferme

/**
 * Pose une question à l'utilisateur.
 * @param {string} question
 * @returns {Promise<string|null>} La réponse, ou `null` si l'utilisateur annule
 *          (bouton « Annuler », Ctrl+C ou Ctrl+D).
 */
export async function demander(question) {
    if (estNavigateur) {
        return window.prompt(question); // `null` si annulé
    }

    if (!interfaceLecture) {
        const { createInterface } = await import("node:readline/promises");
        interfaceLecture = createInterface({
            input: process.stdin,
            output: process.stdout,
        });
        fermeture = new Promise((resolve) =>
            interfaceLecture.once("close", () => resolve(null))
        );
    }

    try {
        return await Promise.race([
            interfaceLecture.question(`${question} `),
            fermeture,
        ]);
    } catch {
        return null; // Interface déjà fermée
    }
}

/**
 * Convertit un texte en entier compris entre `min` et `max`.
 * @returns {number|null} L'entier, ou `null` si la saisie est invalide.
 */
export function analyserEntier(texte, min, max) {
    if (texte.trim() === "") return null; // Number("") vaudrait 0 !

    const nombre = Number(texte);
    return Number.isInteger(nombre) && nombre >= min && nombre <= max
        ? nombre
        : null;
}

/** Libère l'entrée du terminal (sinon Node.js ne se termine pas). */
export function fermer() {
    interfaceLecture?.close();
}
```

**Points à retenir**

- `async` / `await` : la saisie est **asynchrone** dans Node.js (`readline`), donc `demander()` renvoie une promesse. Dans le navigateur, `prompt()` est synchrone, mais `await` fonctionne aussi sur une valeur ordinaire, d'où une seule façon d'écrire le code.
- `import()` dynamique : le module `readline` n'est chargé que dans Node.js, jamais dans le navigateur.
- `Number.isInteger()` rejette `3.5`, `NaN` et `Infinity`, ce que `isNaN()` seul ne faisait pas.

---

## 3. Projet 1 : le jeu de devinette

### Description

- Le programme choisit un **nombre aléatoire entre 1 et 100**.
- Après chaque proposition, il indique si le nombre est **trop grand**, **trop petit** ou **trouvé**.
- Le joueur dispose de **10 essais maximum**.
- À la fin de chaque partie, le **score** est affiché et le joueur peut **rejouer**.

### Code : `jeu.js`

```js
// Jeu de devinette
import { demander, analyserEntier, fermer } from "./utils.js";

const MIN = 1;
const MAX = 100;
const ESSAIS_MAX = 10;

/** Joue une partie et renvoie son résultat. */
async function jouerUnePartie() {
    const secret = Math.floor(Math.random() * (MAX - MIN + 1)) + MIN;
    let essais = 0;

    console.log(
        `\nJ'ai choisi un nombre entre ${MIN} et ${MAX}. ` +
        `Vous avez ${ESSAIS_MAX} essais.`
    );

    while (essais < ESSAIS_MAX) {
        const saisie = await demander(
            `Essai ${essais + 1}/${ESSAIS_MAX} : votre proposition ?`
        );

        if (saisie === null) {
            console.log("Partie abandonnée.");
            return { statut: "abandon", essais };
        }

        const proposition = analyserEntier(saisie, MIN, MAX);
        if (proposition === null) {
            console.log(`⚠️ Entrez un nombre entier entre ${MIN} et ${MAX}.`);
            continue; // Saisie invalide : l'essai n'est pas compté
        }

        essais++;

        if (proposition === secret) {
            console.log(`🎉 Bravo ! Trouvé en ${essais} essai(s).`);
            return { statut: "gagne", essais };
        }

        console.log(proposition > secret ? "📈 Trop grand !" : "📉 Trop petit !");
    }

    console.log(`😢 Perdu ! Le nombre était ${secret}.`);
    return { statut: "perdu", essais };
}

/** Demande au joueur s'il veut rejouer. */
async function veutRejouer() {
    const reponse = await demander("Rejouer ? (oui/non)");
    return ["oui", "o", "yes", "y"].includes(reponse?.trim().toLowerCase());
}

async function main() {
    let parties = 0;
    let victoires = 0;
    let meilleurScore = null; // Plus petit nombre d'essais pour gagner

    try {
        do {
            const { statut, essais } = await jouerUnePartie();
            if (statut === "abandon") break;

            parties++;
            if (statut === "gagne") {
                victoires++;
                meilleurScore = Math.min(meilleurScore ?? Infinity, essais);
            }

            console.log(
                `📊 Score : ${victoires} victoire(s) sur ${parties} partie(s)` +
                (meilleurScore !== null
                    ? ` — meilleur résultat : ${meilleurScore} essai(s)`
                    : "")
            );
        } while (await veutRejouer());
    } finally {
        fermer();
    }

    console.log("Merci d'avoir joué, à bientôt !");
}

main();
```

### Ce qui a été corrigé par rapport à l'original

- **`prompt()` seul** : remplacé par `demander()`, qui fonctionne dans le navigateur et dans Node.js.
- **Plantage à l'annulation** : `prompt(...).toLowerCase()` faisait planter le programme quand l'utilisateur annulait (`null.toLowerCase()`). Le chaînage optionnel `?.` règle le problème.
- **Variable détournée** : `guessedCorrectly = true` servait aussi à signaler l'abandon. La fonction renvoie désormais un **statut explicite** (`gagne`, `perdu`, `abandon`).
- **Valeur codée en dur** : « 10 essais » était écrit dans le texte *et* dans le code ; les constantes `MIN`, `MAX` et `ESSAIS_MAX` évitent cette duplication.
- **Nombres décimaux acceptés** : `3.5` passait la validation ; `Number.isInteger()` le refuse.
- **Score manquant** : la description promettait un score, mais le code n'affichait que le nombre d'essais. Un bilan de session (victoires et meilleur résultat) est maintenant affiché.

---

## 4. Projet 2 : la liste de tâches

### Description

- L'utilisateur peut **ajouter**, **afficher**, **terminer** et **supprimer** des tâches.
- L'application tourne en boucle jusqu'à ce qu'il choisisse de **quitter**.
- Chaque tâche est un **objet** `{ description, terminee }` stocké dans un **tableau**.

### Code : `taches.js`

```js
// Liste de tâches en ligne de commande
import { demander, analyserEntier, fermer } from "./utils.js";

const taches = [];

function afficherMenu() {
    console.log("\n=== 📝 LISTE DE TÂCHES ===");
    console.log("1. Ajouter une tâche");
    console.log("2. Afficher les tâches");
    console.log("3. Marquer une tâche comme terminée");
    console.log("4. Supprimer une tâche");
    console.log("5. Quitter");
}

function afficherTaches() {
    if (taches.length === 0) {
        console.log("Aucune tâche pour le moment.");
        return;
    }

    console.log("\nVos tâches :");
    taches.forEach(({ description, terminee }, i) => {
        console.log(`${i + 1}. ${terminee ? "[✓]" : "[ ]"} ${description}`);
    });
}

/** Affiche la liste puis demande un numéro. Renvoie un indice, ou `null`. */
async function choisirTache(question) {
    if (taches.length === 0) {
        console.log("Aucune tâche disponible.");
        return null;
    }

    afficherTaches();
    const saisie = await demander(question);
    if (saisie === null) return null;

    const numero = analyserEntier(saisie, 1, taches.length);
    if (numero === null) {
        console.log("⚠️ Numéro invalide.");
        return null;
    }
    return numero - 1; // Numéro affiché → indice du tableau
}

async function ajouterTache() {
    const description = (await demander("Nouvelle tâche :"))?.trim();

    if (!description) {
        console.log("⚠️ La tâche ne peut pas être vide.");
        return;
    }

    taches.push({ description, terminee: false });
    console.log(`✅ Tâche ajoutée : « ${description} »`);
}

async function terminerTache() {
    const indice = await choisirTache("Numéro de la tâche terminée :");
    if (indice === null) return;

    taches[indice].terminee = true;
    console.log(`✅ Tâche ${indice + 1} marquée comme terminée.`);
}

async function supprimerTache() {
    const indice = await choisirTache("Numéro de la tâche à supprimer :");
    if (indice === null) return;

    const [supprimee] = taches.splice(indice, 1);
    console.log(`🗑️ Tâche supprimée : « ${supprimee.description} »`);
}

async function main() {
    let enCours = true;

    try {
        while (enCours) {
            afficherMenu();
            const choix = await demander("Votre choix (1-5) :");
            if (choix === null) break;

            switch (choix.trim()) {
                case "1":
                    await ajouterTache();
                    break;
                case "2":
                    afficherTaches();
                    break;
                case "3":
                    await terminerTache();
                    break;
                case "4":
                    await supprimerTache();
                    break;
                case "5":
                    enCours = false;
                    break;
                default:
                    console.log("⚠️ Choisissez une option entre 1 et 5.");
            }
        }
    } finally {
        fermer();
    }

    console.log("Au revoir !");
}

main();
```

### Ce qui a été corrigé par rapport à l'original

- **Déclarations `let` dans les `case`** : `let newTask`, `let doneIndex`, etc. étaient déclarées directement dans un `switch`, ce qui partage la portée entre tous les `case` (risque d'erreurs et règle de lint `no-case-declarations`). Chaque action est maintenant **une fonction** : le `switch` ne fait plus qu'aiguiller.
- **Code répété** : les actions « terminer » et « supprimer » répétaient la même validation de numéro. Elle est factorisée dans `choisirTache()`.
- **Validation trop permissive** : `1.5` était accepté comme numéro de tâche (`tasks[0.5]` → erreur). `analyserEntier()` exige un vrai entier.
- **Pas d'aide à la saisie** : l'utilisateur devait deviner les numéros. La liste est maintenant affichée avant de demander le numéro.
- **Boucle `for` classique** remplacée par `forEach` avec **déstructuration** `({ description, terminee })`, plus lisible.
- **Deux messages d'au revoir** (annulation et option 5) : un seul message final.

---

## 5. Concepts abordés

| Concept | Jeu de devinette | Liste de tâches |
| --- | --- | --- |
| **Variables** (`const` par défaut, `let` si la valeur change) | `secret`, `essais`, `parties` | `taches`, `enCours` |
| **Chaînes** et *template literals* (`` `...${x}` ``) | Messages et invites | Menu, descriptions |
| **Nombres** | `Math.random()`, `Math.floor()`, comptage | Numéros → indices |
| **Booléens** | `enCours`, résultat de `veutRejouer()` | `terminee`, `enCours` |
| **Boucles** | `do...while`, `while` | `while`, `forEach` |
| **Conditions** | `if`, opérateur ternaire `? :` | `switch`, `if` |
| **Fonctions** et **`async` / `await`** | `jouerUnePartie()`, `demander()` | Une fonction par action |
| **Tableaux et objets** | `[...].includes()` | `push`, `splice`, `{ description, terminee }` |
| **Modules ES** (`import` / `export`) | `utils.js` partagé | `utils.js` partagé |
| **Opérateurs modernes** : `?.` et `??` | `reponse?.trim()`, `meilleurScore ?? Infinity` | `(await demander(...))?.trim()` |
| **Déstructuration** | `const { statut, essais } = ...` | `const [supprimee] = ...` |

---

## 6. Pour aller plus loin

- **Sauvegarder les tâches** (le résultat dépend du contexte d'exécution) :

  ```js
  // Navigateur : localStorage (la valeur doit être une chaîne)
  localStorage.setItem("taches", JSON.stringify(taches));
  const sauvegarde = JSON.parse(localStorage.getItem("taches") ?? "[]");
  ```

  ```js
  // Node.js : lecture et écriture d'un fichier JSON
  import { readFile, writeFile } from "node:fs/promises";

  await writeFile("taches.json", JSON.stringify(taches, null, 2), "utf-8");
  const contenu = await readFile("taches.json", "utf-8");
  ```

- **Niveaux de difficulté** : faire varier `MAX` et `ESSAIS_MAX` selon le choix du joueur.
- **Indice supplémentaire** : afficher « chaud / froid » selon l'écart avec le nombre secret.
- **Interface web** : remplacer `prompt()` par un formulaire HTML et des événements (`addEventListener`).
- **Tests** : tester `analyserEntier()` avec le lanceur de tests intégré à Node.js (`node --test`).
- **Annoter le code** avec JSDoc, ou passer à **TypeScript** pour détecter les erreurs de type avant l'exécution.
