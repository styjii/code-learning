# 🟨 Exercices JavaScript

> Quatre séries d'exercices (défis de fonctions, variables et types, conditions, boucles), regroupées, **dédoublonnées** et classées par difficulté. Le code vise le JavaScript moderne (ES2022+) et fonctionne dans le **navigateur** comme dans **Node.js**.

## 📑 Sommaire

1. [Contexte d'exécution et conventions](#1-contexte-dexécution-et-conventions)
2. [Partie 1 : défis de fonctions](#2-partie-1--défis-de-fonctions)
3. [Partie 2 : variables et types de données](#3-partie-2--variables-et-types-de-données)
4. [Partie 3 : conditions](#4-partie-3--conditions)
5. [Partie 4 : boucles et itérations](#5-partie-4--boucles-et-itérations)
6. [Récapitulatif des changements](#6-récapitulatif-des-changements)

**Légende** : 🟢 débutant · 🟡 intermédiaire · 🔴 avancé · ➕ ajouté dans cette version

---

## 1. Contexte d'exécution et conventions

### Navigateur ou Node.js ?

Le même JavaScript ne dispose pas des mêmes outils selon l'endroit où il s'exécute :

| | 🌐 Navigateur | 🟢 Node.js (20 ou plus récent) |
| --- | --- | --- |
| Saisie | `prompt()` | module `node:readline/promises` |
| Message | `alert()`, `console.log()` | `console.log()` |
| Objet global | `window` | `globalThis` |
| Lancer un fichier | `<script type="module">` | `node fichier.js` (avec `"type": "module"` dans `package.json` pour `import` / `await` au niveau supérieur) |

> ⚠️ **`prompt()` et `alert()` n'existent pas dans Node.js** : le code planterait avec `ReferenceError`. Pour les exercices interactifs, utilisez ce petit module de saisie qui marche dans les deux contextes :

```js
// entree.js : saisie utilisable dans le navigateur et dans Node.js (version simplifiée)
const estNavigateur =
    typeof window !== "undefined" && typeof window.prompt === "function";
let rl = null;

/** Pose une question. Renvoie la réponse (texte), ou `null` si l'utilisateur annule. */
export async function demander(question) {
    if (estNavigateur) return window.prompt(question);

    if (!rl) {
        const { createInterface } = await import("node:readline/promises");
        rl = createInterface({ input: process.stdin, output: process.stdout });
    }
    try {
        return await rl.question(`${question} `);
    } catch {
        return null;
    }
}

/** À appeler en fin de programme dans Node.js, sinon il ne s'arrête pas. */
export function fermer() {
    rl?.close();
}
```

```js
// Exemple d'utilisation
import { demander, fermer } from "./entree.js";

const nom = (await demander("Votre nom ?")) ?? "Invité";
console.log(`Bonjour, ${nom} !`);
fermer();
```

> 💡 Dans les énoncés ci-dessous, « demandez à l'utilisateur » signifie « utilisez `demander()` ». La valeur lue est **toujours du texte** : convertissez-la avec `Number(...)` si besoin.

### Bonnes pratiques modernes

| Ancien réflexe | À privilégier aujourd'hui |
| --- | --- |
| `var` | **`const`** par défaut, **`let`** si la variable est réassignée |
| `"a" + b + "c"` | Gabarits de chaînes : `` `a${b}c` `` |
| `valeur \|\| "défaut"` | `valeur ?? "défaut"` (ne remplace que `null` et `undefined`) |
| `a && a.b && a.b.c` | Chaînage optionnel : `a?.b?.c` |
| Boucle `for` à indice | `for...of`, `map`, `filter`, `reduce` |
| `==` | **`===`** (comparaison stricte) |

### Convention des défis

Pour chaque défi de la partie 1 : écrivez la fonction, puis vérifiez-la avec les appels fournis (le résultat attendu est indiqué en commentaire).

---

## 2. Partie 1 : défis de fonctions

Vingt défis courts. Chaque fonction doit **retourner** son résultat (et non l'afficher).

### Défi 1 : passagers du bus 🟢

Un bus passe dans une ville et prend ou dépose des passagers à chaque arrêt. On vous donne une liste de tableaux `[montent, descendent]`. Au premier arrêt, personne ne descend (la seconde valeur vaut `0`). Renvoyez le nombre de personnes restant dans le bus après le dernier arrêt.

```javascript
function nombrePassagers(arrets) {
    // votre code ici
}

console.log(nombrePassagers([[10, 0], [3, 5], [5, 8]])); // 5
console.log(nombrePassagers([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]])); // 17
console.log(nombrePassagers([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]])); // 21
```

---

### Défi 2 : compter les moutons 🟢

Comptez les moutons (`true`) présents dans un tableau. Les entrées invalides (`null`, `undefined`, `false`) ne comptent pas.

```javascript
function compterMoutons(troupeau) {
    // votre code ici
}

const troupeau = [
    true, true, true, false, true, true, true, true, true,
    false, true, false, true, false, false, true, true,
    true, true, true, false, false, true, true,
];

console.log(compterMoutons(troupeau)); // 17
console.log(compterMoutons([true, null, undefined, false, true])); // 2
```

---

### Défi 3 : retirer premier et dernier caractères 🟢

Renvoyez une chaîne privée de son premier et de son dernier caractère.

```javascript
function retirerExtremites(phrase) {
    // votre code ici
}

console.log(retirerExtremites("Ceci est une phrase")); // "eci est une phras"
```

---

### Défi 4 : supprimer les chiffres 🟢

Supprimez tous les chiffres d'un texte, mais conservez les espaces, la ponctuation et les caractères spéciaux.

```javascript
function nettoyerChaine(texte) {
    // votre code ici
}

console.log(nettoyerChaine("! !")); // "! !"
console.log(nettoyerChaine("123456789")); // ""
console.log(nettoyerChaine("(E3at m2e2!!)")); // "(Eat me!!)"
console.log(nettoyerChaine("Wh7y can't we3 bu1y the goo0d software3? #cheapskates3"));
// "Why can't we buy the good software? #cheapskates"
```

> 💡 Piste : expression régulière avec `replace` et le drapeau `g`.

---

### Défi 5 : doubler chaque caractère 🟢

Renvoyez une chaîne où chaque caractère est répété une fois.

```javascript
function doublerCaracteres(texte) {
    // votre code ici
}

console.log(doublerCaracteres("String")); // "SSttrriinngg"
console.log(doublerCaracteres("Hello World")); // "HHeelllloo WWoorrlldd"
console.log(doublerCaracteres("1234!_ ")); // "11223344!!__  "
```

---

### Défi 6 : supprimer les doublons et trier 🟢

Supprimez les doublons d'une liste de nombres et renvoyez-la triée par ordre croissant.

```javascript
function supprimerDoublons(nombres) {
    // votre code ici
}

console.log(supprimerDoublons([1, 1, 2, 4, 5, 2, 1, 2, 3, 5, 5, 5])); // [1, 2, 3, 4, 5]
console.log(supprimerDoublons([10, 9, 2, 10])); // [2, 9, 10]
```

> ⚠️ `tableau.sort()` **sans fonction de comparaison** trie par ordre alphabétique : `[10, 9, 2]` devient `[10, 2, 9]`. Utilisez `.sort((a, b) => a - b)`. Pour supprimer les doublons, pensez à `Set`.

---

### Défi 7 : à qui le tour ? 🟢

Deux joueurs, « black » et « white », jouent plusieurs manches. Un joueur qui gagne une manche commence la suivante ; s'il la perd, c'est l'autre qui commence. Étant donné le joueur courant et le résultat (`true` = victoire), indiquez qui commence la manche suivante.

```javascript
function prochainJoueur(joueur, victoire) {
    // votre code ici
}

console.log(prochainJoueur("black", false)); // "white"
console.log(prochainJoueur("white", true)); // "white"
console.log(prochainJoueur("white", false)); // "black"
```

---

### Défi 8 : calculer le pourboire 🟡

Calculez le pourboire à donner selon le montant de l'addition et la qualité du service :

| Service | Pourboire |
| --- | :-: |
| Terrible | 0 % |
| Poor | 5 % |
| Good | 10 % |
| Great | 15 % |
| Excellent | 20 % |

- La qualité de service est **insensible à la casse**.
- Si elle n'est pas reconnue, renvoyez `"Rating not recognised"`.
- Arrondissez le résultat **à l'entier supérieur**.

```javascript
function calculerPourboire(addition, service) {
    // votre code ici
}

console.log(calculerPourboire(20, "ExcellEnt")); // 4
console.log(calculerPourboire(26.95, "goOd")); // 3
console.log(calculerPourboire(20, "hi")); // "Rating not recognised"
```

---

### Défi 9 : `accum` 🟡

Transformez une chaîne : chaque caractère est répété *n* fois (où *n* est sa position, en commençant à 1), le premier caractère de chaque bloc est en majuscule et les blocs sont séparés par des tirets.

```javascript
function accum(texte) {
    // votre code ici
}

console.log(accum("abcd")); // "A-Bb-Ccc-Dddd"
console.log(accum("RqaEzty")); // "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
console.log(accum("cwAt")); // "C-Ww-Aaa-Tttt"
```

> Remarquez la majuscule au début de chaque bloc, le nombre croissant de lettres et les tirets.

---

### Défi 10 : compter comme la tribu Arara 🟡

La tribu Arara compte ainsi : 1 = « anane », 2 = « adak », 3 = « adak anane », 4 = « adak adak »… Autrement dit, chaque paire est un « adak », et un éventuel reste impair ajoute « anane » à la fin. Convertissez un nombre dans ce langage.

```javascript
function compterArara(nombre) {
    // votre code ici
}

console.log(compterArara(1)); // "anane"
console.log(compterArara(3)); // "adak anane"
console.log(compterArara(8)); // "adak adak adak adak"
```

---

### Défi 11 : valider un code PIN 🟡

Un code PIN de distributeur doit comporter **exactement 4 ou 6 chiffres**, et rien d'autre. Renvoyez `true` s'il est valide, sinon `false`.

```javascript
function validerPIN(pin) {
    // votre code ici
}

console.log(validerPIN("1234")); // true
console.log(validerPIN("12345")); // false
console.log(validerPIN("a234")); // false
```

---

### Défi 12 : `toJadenCase` 🟡

Ajoutez une méthode `toJadenCase` à `String.prototype` qui met en majuscule la première lettre de chaque mot d'une phrase.

```javascript
// votre code ici

console.log("this is a sentence".toJadenCase()); // "This Is A Sentence"
```

> ⚠️ **Contexte** : modifier les objets natifs (`String.prototype`, `Array.prototype`…) est **déconseillé** dans du vrai code : cela peut entrer en conflit avec d'autres bibliothèques ou avec de futures versions du langage. Réalisez l'exercice pour comprendre les prototypes, puis écrivez aussi la version fonction `enJadenCase(texte)`, qui est la bonne pratique.

---

### Défi 13 : compter les voyelles 🟢

Comptez les voyelles (`a`, `e`, `i`, `o`, `u`) d'une chaîne.

```javascript
function compterVoyelles(texte) {
    // votre code ici
}

console.log(compterVoyelles("This is a sentence")); // 6
```

---

### Défi 14 : choix de repas 🟡

Des développeurs se sont inscrits à votre meetup. Renvoyez un objet indiquant combien de fois chaque repas a été choisi.

```javascript
function compterRepas(inscrits) {
    // votre code ici
}

const inscrits = [
    { firstName: "Noah", lastName: "M.", country: "Switzerland", continent: "Europe", age: 19, language: "C", meal: "vegetarian" },
    { firstName: "Anna", lastName: "R.", country: "Liechtenstein", continent: "Europe", age: 52, language: "JavaScript", meal: "standard" },
    { firstName: "Ramona", lastName: "R.", country: "Paraguay", continent: "Americas", age: 29, language: "Ruby", meal: "vegan" },
    { firstName: "George", lastName: "B.", country: "England", continent: "Europe", age: 81, language: "C", meal: "vegetarian" },
];

console.log(compterRepas(inscrits));
// { vegetarian: 2, standard: 1, vegan: 1 }  (l'ordre des clés n'a pas d'importance)
```

> 💡 Deux approches : `reduce`, ou la méthode récente `Object.groupBy()` (ES2024, Node.js 21+) suivie d'un comptage des éléments de chaque groupe.

---

### Défi 15 : effet compteur 🟡

À partir d'une chaîne de chiffres, renvoyez un tableau imbriqué où chaque chiffre est remplacé par un tableau comptant de 0 jusqu'à ce chiffre.

```javascript
function effetCompteur(chiffres) {
    // votre code ici
}

console.log(effetCompteur("1250")); // [[0,1], [0,1,2], [0,1,2,3,4,5], [0]]
```

---

### Défi 16 : le nombre le plus long 🟡

Renvoyez le nombre qui a le plus de chiffres. En cas d'égalité, renvoyez le **premier**.

```javascript
function nombreLePlusLong(nombres) {
    // votre code ici
}

console.log(nombreLePlusLong([1, 10, 100])); // 100
console.log(nombreLePlusLong([-100, 25, 7])); // -100
```

> 💡 Réfléchissez au signe `-` : il ne doit pas compter comme un chiffre.

---

### Défi 17 : le mot le plus court 🟢

Renvoyez la **longueur** du mot le plus court d'une phrase.

```javascript
function longueurMotCourt(phrase) {
    // votre code ici
}

console.log(longueurMotCourt("bitcoin take over the world maybe who knows perhaps")); // 3
```

---

### Défi 18 : le mot le plus long 🟢

Renvoyez le mot le plus long d'une phrase. En cas d'égalité, renvoyez le **dernier**.

```javascript
function motLePlusLong(phrase) {
    // votre code ici
}

console.log(motLePlusLong("a b c d e fgh")); // "fgh"
console.log(motLePlusLong("aa bb c")); // "bb"
```

---

### Défi 19 : image en niveaux de gris 🟡

Une image est un tableau 2D de pixels RVB (chaque pixel est `[R, V, B]`). Convertissez-la en niveaux de gris en remplaçant chaque composante par la **moyenne arrondie** (`Math.round`) des trois valeurs du pixel.

```javascript
function enNiveauxDeGris(image) {
    // votre code ici
}

const image = [
    [[123, 231, 12], [56, 43, 124]],
    [[78, 152, 76], [64, 132, 200]],
];

console.log(enNiveauxDeGris(image));
// [
//     [[122, 122, 122], [74, 74, 74]],
//     [[102, 102, 102], [132, 132, 132]],
// ]
```

---

### Défi 20 : carré de chaque chiffre 🟡

Élevez chaque chiffre d'un nombre au carré et concaténez les résultats.

```javascript
function carresDesChiffres(nombre) {
    // votre code ici
}

console.log(carresDesChiffres(9119)); // 811181
```

---

## 3. Partie 2 : variables et types de données

### 3.1 Déclarer et manipuler des variables

#### Exercice V1 : corriger le code 🟢

Ce code est cassé. **Corrigez les erreurs** pour qu'il fonctionne, et remplacez `var` par `const` ou `let`.

```javascript
var name = Alice;
var age = "twenty";
var hobby = Painting;

console.log("My name is " + name + " I am " + age + " years old, and I enjoy " + hobby);
```

> ⚠️ **Contexte** : dans un navigateur, `var name` au niveau global crée `window.name`, une propriété qui convertit toujours sa valeur en chaîne. Une raison de plus d'éviter `var`.

#### Exercice V2 : quiz de type 🟢

Quel est le type de la variable suivante ?

```javascript
let x = "42";
```

A. `number` · B. `string` · C. `boolean` · D. `undefined`

<details>
<summary>Réponse</summary>

**B** : `string`. Les guillemets font de `"42"` une chaîne, pas un nombre.

</details>

#### Exercice V3 : présentation personnelle 🟢

1. Créez `firstName` (chaîne), `favoriteNumber` (nombre) et `city` (chaîne).
2. Avec un **gabarit de chaîne**, construisez le message : *« Salut ! Je suis [prénom], j'habite à [ville] et mon nombre préféré est [nombre]. »*
3. Affichez-le dans la console.

#### Exercice V4 : déclarer et réassigner 🟢

1. Déclarez une variable `name` contenant votre prénom.
2. Déclarez `age` avec un nombre, puis réassignez-lui une nouvelle valeur.
3. Déclarez `firstName`, `lastName`, `country`, `age` et `isMarried` en **une seule instruction**.

> 💡 Déclarer plusieurs variables sur une ligne est possible, mais une variable par ligne est plus lisible.

#### Exercice V5 : `const` et `let` 🟢

1. Créez une constante `PI` valant `3.14` et une variable `radius` valant `5`, puis calculez l'aire du cercle.
2. Essayez de modifier la constante (`PI = 3`). Quelle erreur apparaît ?

#### Exercice V6 : vérifier les types avec `typeof` 🟢

Utilisez `typeof` sur : une chaîne, un nombre, un booléen, `null`, `undefined`, un tableau, une fonction. ➕ Ajoutez `10n` (BigInt) et `Symbol("x")`.

> ❓ Pourquoi `typeof null` renvoie-t-il `"object"` ? Comment reconnaître un vrai tableau (`Array.isArray`) ?

#### Exercice V7 : échanger deux variables 🟢

Échangez les valeurs de `a` et `b`, d'abord avec une variable temporaire, puis avec la **déstructuration** (`[a, b] = [b, a]`).

#### Exercice V8 : valeurs par défaut (`||` contre `??`) 🟡

1. Créez une variable qui vaut `"Invité"` si le nom saisi est vide (utilisez `||`).
2. Faites la même chose avec `??`.
3. Testez avec `""`, `0`, `null` et `undefined`. Dans quels cas les deux opérateurs diffèrent-ils ?

#### Exercice V9 : `null` contre `undefined` 🟢

Affectez `null` à une variable et `undefined` à une autre, puis comparez-les avec `==` et `===`. Expliquez les résultats.

#### Exercice V10 : portée et fermetures 🟡

Prédisez la sortie, puis vérifiez :

```js
let x = 10;

function externe() {
    let x = 20;
    function interne() {
        console.log(x);
    }
    return interne;
}

const fn = externe();
fn(); // ??
```

<details>
<summary>Réponse</summary>

**`20`** : `interne` « se souvient » de la variable `x` de la fonction `externe` (c'est une *fermeture*, ou *closure*), pas de celle du niveau global.

</details>

➕ Prolongement : prédisez la sortie de `console.log(a)` avant `var a = 1;`, puis avant `let b = 2;`. Que se passe-t-il, et pourquoi (*hoisting* et *zone morte temporelle*) ?

---

### 3.2 Nombres

#### Exercice V11 : opérations de base 🟢

Calculez la somme, la différence, le produit et le quotient de deux nombres. Utilisez aussi `%` (par exemple le reste de `15 / 4`) et `**` (puissance).

#### Exercice V12 : arrondis 🟢

Appliquez `Math.floor()`, `Math.ceil()`, `Math.round()` et `Math.trunc()` à `4.7` puis à `-4.7`. Que remarquez-vous pour les négatifs ? Affichez `4.7` avec une décimale grâce à `toFixed(1)`.

#### Exercice V13 : nombres aléatoires 🟢

1. Générez un nombre aléatoire entre 1 et 100.
2. Écrivez `entierAleatoire(min, max)` qui renvoie un entier entre `min` et `max` **inclus**.

#### Exercice V14 : conversions de types 🟡

1. Convertissez un nombre en chaîne avec `String()` et `.toString()`.
2. Convertissez `"123"` en nombre avec `Number()` et `parseInt()`.
3. Convertissez `"true"` en booléen, `"123"` en nombre et `123` en chaîne.
4. Comparez `Number("12px")`, `parseInt("12px")` et `parseFloat("3.14abc")`.

> ⚠️ Piège : `Boolean("false")` vaut **`true`**, car toute chaîne non vide est « vraie ».

#### Exercice V15 : `NaN` et validation numérique 🟡

1. Testez `isNaN("hello")` et `isNaN(123)`, puis expliquez les résultats.
2. Comparez avec `Number.isNaN("hello")` : pourquoi cette fonction est-elle plus fiable ?
3. Écrivez `estNombre(saisie)` qui valide qu'un texte saisi est un nombre valide (attention à la chaîne vide et aux espaces).

#### Exercice V16 : convertisseur de température 🟢

Convertissez des degrés Celsius en Fahrenheit : `F = (C × 9/5) + 32`.

#### Exercice V17 : intérêts simples 🟢

À partir du capital, du taux et de la durée, calculez les intérêts :

```js
const interets = (capital * taux * duree) / 100;
```

#### Exercice V18 : âge en jours 🟢

Demandez l'âge en années et convertissez-le en jours (sans tenir compte des années bissextiles).

#### Exercice V19 : prix après remise 🟢

Prix d'origine : 1000. Remise : 25 %. Calculez le prix final.

#### Exercice V20 : convertisseur de devises 🟢

Avec un taux **fictif** stocké dans une constante (par exemple `const TAUX_EUR = 0.92;` pour 1 USD), demandez un montant en dollars et convertissez-le en euros. Pourquoi ne faut-il pas écrire le taux « en dur » à plusieurs endroits ?

#### Exercice V21 : indice de masse corporelle (IMC) 🟢

Demandez la taille (en mètres) et le poids (en kg), puis calculez `poids / (taille * taille)`. *(La classification se fait à l'exercice C15.)*

#### Exercice V22 : précision des décimaux 🔴

JavaScript a des problèmes de précision décimale : `0.1 + 0.2` ne vaut pas `0.3`. Écrivez `additionSure(a, b)` qui additionne deux décimaux correctement :

```js
additionSure(0.1, 0.2); // 0.3
```

> 💡 Pistes : travailler sur des entiers (multiplier par 100), arrondir avec `toFixed` puis `Number`, ou comparer avec `Number.EPSILON`.

#### Exercice V23 : grands nombres et `BigInt` ➕ 🟡

1. Affichez `Number.MAX_SAFE_INTEGER` puis `Number.MAX_SAFE_INTEGER + 2`. Que constatez-vous ?
2. Refaites le calcul avec des `BigInt` (`9007199254740991n + 2n`).
3. Calculez `25!` avec des `Number`, puis avec des `BigInt`.

#### Exercice V24 : nombre en toutes lettres 🔴

Convertissez `1234` en `"mille deux cent trente-quatre"` (limitez-vous à la plage 0–9999).

---

### 3.3 Chaînes de caractères

#### Exercice V25 : concaténation et gabarits 🟢

Joignez `"Hello"` et `"World"` en `"Hello World"` de trois façons : `+`, `concat()` et gabarit de chaîne. Écrivez une phrase avec des variables : `` `Bonjour, je m'appelle ${name} et j'ai ${age} ans.` ``.

#### Exercice V26 : longueur et accès aux caractères 🟢

Pour `"JavaScript"`, affichez la longueur, puis le premier, le caractère du milieu et le dernier (essayez `.at(-1)` pour le dernier).

#### Exercice V27 : méthodes essentielles 🟢

Réalisez ces sept manipulations :

1. Mettre une chaîne en majuscules, puis en minuscules.
2. Supprimer les espaces de `"   hello   "` avec `.trim()`.
3. Extraire `"Script"` de `"JavaScript"` avec `.slice()` (puis avec `.substring()`).
4. Remplacer `"dog"` par `"cat"` dans `"The dog barked"` (`.replace()`, puis `.replaceAll()`).
5. Découper `"apple,banana,orange"` en tableau avec `.split()`.
6. Vérifier que `"JavaScript"` contient `"Script"` avec `.includes()`.
7. Répéter `"ha"` cinq fois avec `.repeat()`.

#### Exercice V28 : prénom et nom 🟢

À partir de `"John Doe"`, extrayez `John` et `Doe` (avec `split` et la déstructuration).

#### Exercice V29 : validateur d'e-mail 🟡

Vérifiez qu'une chaîne contient `"@"` et `"."` et se termine par `".com"`.

> ℹ️ Il s'agit d'un contrôle simplifié : une vraie validation d'e-mail passe par un message de confirmation.

#### Exercice V30 : générateur de nom d'utilisateur 🟡

À partir du nom complet `"John Smith"`, créez `john.smith23` (le nombre est aléatoire ou saisi).

#### Exercice V31 : initiales 🟡

À partir de `"Harry James Potter"`, affichez `"H.J.P."`.

#### Exercice V32 : abréviation 🟡

Transformez `"Internationalization"` en `"I18n"` (première lettre, nombre de lettres intermédiaires, dernière lettre).

#### Exercice V33 : masquer un numéro de carte 🟡

`"1234567812345678"` devient `"************5678"` (essayez `padStart`).

#### Exercice V34 : pluriel 🟢

Si `nombre === 1`, affichez `"1 article"`, sinon `"X articles"`.

#### Exercice V35 : chaîne vide ? 🟢

Écrivez une fonction qui renvoie `true` si une chaîne est vide **ou ne contient que des espaces**.

#### Exercice V36 : inverser 🟡

1. Inversez `"JavaScript"` pour obtenir `"tpircSavaJ"`.
2. Inversez l'ordre des mots : `"hello world"` devient `"world hello"`.

#### Exercice V37 : palindromes 🟡

Écrivez `estPalindrome(texte)` :

1. 🟢 pour un mot simple (`"radar"`) ;
2. 🟡 pour une phrase qui **ignore la ponctuation et la casse** :

```js
estPalindrome("A man, a plan, a canal: Panama"); // true
```

#### Exercice V38 : compression de chaîne 🔴

Compressez `"aaabbbbcc"` en `"a3b4c2"` (**codage par plages**, *run-length encoding*). Écrivez aussi la fonction inverse.

#### Exercice V39 : anagrammes 🟡

Vérifiez que deux chaînes sont des anagrammes (mêmes caractères dans un ordre différent).

#### Exercice V40 : `split` sans `.split()` 🔴

Écrivez `decouper(texte, separateur)` qui imite `texte.split(separateur)`.

#### Exercice V41 : caractère le plus fréquent 🟡

Trouvez le caractère le plus fréquent d'une chaîne et son nombre d'occurrences.

---

### 3.4 Structures de données et logique

#### Exercice V42 : déstructuration, `spread` et `rest` ➕ 🟡

1. Extrayez `nom` et `age` d'un objet avec la déstructuration, avec une valeur par défaut pour `age`.
2. Copiez un tableau et un objet avec `...` (opérateur *spread*), puis modifiez la copie. L'original change-t-il ?
3. Écrivez `somme(...nombres)` avec un paramètre *rest*.
4. Comparez la copie superficielle (`...`) et `structuredClone()` sur un objet imbriqué.

#### Exercice V43 : égalité profonde 🔴

Écrivez `egaliteProfonde(a, b)` qui renvoie `true` si deux valeurs sont profondément égales (objets ou tableaux imbriqués).

```js
console.log(egaliteProfonde({ a: 1 }, { a: 1 })); // true
console.log(egaliteProfonde([1, 2], [1, 2])); // true
console.log(egaliteProfonde({ a: [1, { b: 2 }] }, { a: [1, { b: 3 }] })); // false
```

#### Exercice V44 : détecter le type 🟡

Écrivez `obtenirType(valeur)` qui renvoie `"null"`, `"array"`, `"object"`, `"number"`, `"string"`, `"boolean"` ou `"undefined"`.

```js
console.log(obtenirType([])); // "array"
console.log(obtenirType(null)); // "null"
console.log(obtenirType("hello")); // "string"
```

#### Exercice V45 : Fibonacci avec mémoïsation 🔴

Écrivez une fonction récursive `fib(n)` qui utilise la **mémoïsation** (un `Map` qui garde les résultats déjà calculés). Comparez son temps avec la version naïve pour `n = 40`.

#### Exercice V46 : évaluateur d'expressions 🔴

Écrivez une fonction qui analyse `"3 + 5 * 2"` et renvoie le bon résultat (`13`), **sans** `eval()`.

> 💡 `eval()` exécute n'importe quel code : c'est une faille de sécurité. Piste : traitez d'abord les `*` et `/`, puis les `+` et `-` (priorité des opérateurs).

#### Exercice V47 : casse de titre avec exceptions 🟡

Mettez en majuscule la première lettre de chaque mot, **sauf** les petits mots (`the`, `and`, `of`…), sauf s'il s'agit du premier mot.

```js
enTitre("the lord of the rings"); // "The Lord of the Rings"
```

---

### 3.5 Mini-projets

#### Exercice V48 : fonction `saluer` 🟢

Écrivez `saluer(nom)` qui renvoie `"Bonjour, Alice !"` lorsqu'on l'appelle avec `"Alice"`.

#### Exercice V49 : compteur de caractères 🟢

Demandez un texte et affichez son nombre de caractères (avec puis sans les espaces).

#### Exercice V50 : mini-quiz de calcul 🟢

Posez la question « Combien font 5 + 7 ? » et vérifiez la réponse (rappel : la saisie est du texte).

---

## 4. Partie 3 : conditions

> 📌 À maîtriser : `if / else if / else`, `switch`, l'opérateur ternaire `cond ? a : b`, la comparaison stricte `===`, les opérateurs logiques `&&`, `||`, `!` et `??`.

### 4.1 Niveau de base

#### Exercice C1 : pair ou impair 🟢

Demandez un nombre et indiquez s'il est pair ou impair (`7` → `"Impair"`).

#### Exercice C2 : positif, négatif ou nul 🟢

Demandez un nombre et déterminez s'il est positif, négatif ou nul.

#### Exercice C3 : tranche d'âge 🟢

Pour un âge donné, affichez « Enfant » (0–12), « Adolescent » (13–19), « Adulte » (20–64) ou « Senior » (65+).

#### Exercice C4 : le plus grand de deux nombres 🟢

Prenez deux nombres et affichez le plus grand.

#### Exercice C5 : année bissextile 🟢

Demandez une année et indiquez si elle est bissextile.

> Une année est bissextile si elle est divisible par 4 **et** (non divisible par 100 **ou** divisible par 400).

### 4.2 Niveau intermédiaire

#### Exercice C6 : calculateur de note 🟡

Pour une note sur 100, affichez la mention : A (90–100), B (80–89), C (70–79), D (60–69), F (< 60).

➕ **Bonus** : affinez avec les « + » et « − », selon ce tableau :

| Note | Mention | Note | Mention | Note | Mention |
| :-: | :-: | :-: | :-: | :-: | :-: |
| 97–100 | A+ | 87–89 | B+ | 77–79 | C+ |
| 93–96 | A | 83–86 | B | 73–76 | C |
| 90–92 | A− | 80–82 | B− | 70–72 | C− |
| 67–69 | D+ | 63–66 | D | 60–62 | D− |
| 0–59 | F | | | | |

#### Exercice C7 : voyelle ou consonne 🟢

Prenez une seule lettre de l'alphabet et déterminez s'il s'agit d'une voyelle (`a, e, i, o, u`) ou d'une consonne.

#### Exercice C8 : système de connexion 🟡

Écrivez en dur un nom d'utilisateur et un mot de passe. Demandez les deux et vérifiez qu'ils correspondent.

> 🔐 Dans une vraie application, on ne stocke **jamais** un mot de passe en clair dans le code : on conserve son empreinte (*hash*).

#### Exercice C9 : calculatrice simple 🟡

Demandez deux nombres et un opérateur (`+`, `-`, `*`, `/`). Utilisez un `switch` pour effectuer l'opération, et gérez la division par zéro.

#### Exercice C10 : feu tricolore 🟢

Prenez une couleur (`rouge`, `orange`, `vert`) et affichez ce que doit faire le conducteur : « Stop », « Ralentir » ou « Avancer ».

### 4.3 Niveau avancé

#### Exercice C11 : type de triangle 🟡

Demandez les longueurs de trois côtés. Vérifiez d'abord que le triangle est **valide** (inégalité triangulaire : chaque côté est plus petit que la somme des deux autres), puis déterminez s'il est **équilatéral** (3 côtés égaux), **isocèle** (2 côtés égaux) ou **scalène** (3 côtés différents).

#### Exercice C12 : intervalle avec exceptions 🟡

Vérifiez qu'un nombre est compris entre 50 et 100 **sans** être divisible par 5 ni par 7.

#### Exercice C13 : rôles et permissions 🟡

Trois rôles existent : `admin` (lire, écrire, supprimer), `editor` (lire, écrire) et `viewer` (lire seulement). Si le rôle est invalide, refusez l'accès.

#### Exercice C14 : salutation selon l'heure 🟢

Pour une heure (0–23), affichez : « Bonne nuit » (0–5), « Bonjour » (6–11), « Bon après-midi » (12–17), « Bonsoir » (18–21), « Bonne nuit » (22–23). Utilisez uniquement `if / else`.

#### Exercice C15 : catégorie d'IMC 🟡

À partir de l'IMC calculé à l'exercice V21, classez le résultat : Insuffisance pondérale (< 18,5), Normal (18,5–24,9), Surpoids (25–29,9), Obésité (≥ 30).

#### Exercice C16 : FizzBuzz avec variantes 🟡

Pour les nombres de 1 à 100 :

- divisible par 3 : afficher `Fizz` ;
- divisible par 5 : afficher `Buzz` ;
- divisible par 3 **et** 5 : afficher `FizzBuzz` ;
- si le nombre contient un 3 : ajouter ` (chanceux)` ;
- si le nombre est divisible par 7 : ajouter ` (suspect)`.

```text
3  → Fizz (chanceux)
15 → FizzBuzz
21 → Fizz (suspect)
```

#### Exercice C17 : validateur de date 🔴

Pour un jour, un mois et une année, vérifiez que la date existe (mois de longueurs différentes, années bissextiles).

> ⚠️ Piège : `new Date(2025, 1, 31)` ne signale pas d'erreur, il « déborde » vers le 3 mars (les mois commencent à 0 en JavaScript). Une technique consiste à recréer la date puis à vérifier que le jour, le mois et l'année n'ont pas changé.

#### Exercice C18 : force d'un mot de passe 🟡

Classez un mot de passe :

- **Faible** : moins de 6 caractères ;
- **Moyen** : au moins 6 caractères, avec lettres et chiffres ;
- **Fort** : au moins 8 caractères, avec lettres, chiffres et symboles (`!@#$%`).

Utilisez des expressions régulières ou des `if / else` imbriqués.

#### Exercice C19 : trier trois nombres 🟡

Prenez trois nombres et affichez-les dans l'ordre croissant avec uniquement des `if / else` (pas de tableau, pas de `sort()`).

#### Exercice C20 : médiane de trois nombres 🟡

Trouvez la **médiane** de trois nombres différents, c'est-à-dire celui du milieu une fois triés (`3, 8, 5` → `5`).

### 4.4 Scénarios réalistes

#### Exercice C21 : convertisseur de devises avec frais 🟡

Convertissez un montant en dollars vers une autre monnaie avec un taux fixe (constante). Ajoutez des frais de **2 %** **uniquement** si le montant dépasse 1000.

#### Exercice C22 : éligibilité à une bourse 🟡

Un étudiant est éligible si **toutes** ces conditions sont réunies :

```text
( moyenne > 3,5   OU   ( moyenne > 3,0  ET  activités extrascolaires ) )   ET   revenu familial < 50 000
```

Affichez s'il est éligible. *(L'énoncé d'origine était ambigu sur la priorité du « OU » et du « ET » : les parenthèses ci-dessus lèvent le doute.)*

#### Exercice C23 : remises imbriquées 🟡

- Si le client est **membre** : plus de 500 de dépenses → 20 % ; sinon plus de 100 → 10 % ; sinon → 5 %.
- Sinon : aucune remise.

#### Exercice C24 : signe du zodiaque 🟡

À partir d'un `jour` et d'un `mois`, affichez le signe correspondant :

| Signe | Période | Signe | Période |
| --- | --- | --- | --- |
| Capricorne | 22 déc. – 19 janv. | Cancer | 21 juin – 22 juil. |
| Verseau | 20 janv. – 18 fév. | Lion | 23 juil. – 22 août |
| Poissons | 19 fév. – 20 mars | Vierge | 23 août – 22 sept. |
| Bélier | 21 mars – 19 avr. | Balance | 23 sept. – 22 oct. |
| Taureau | 20 avr. – 20 mai | Scorpion | 23 oct. – 21 nov. |
| Gémeaux | 21 mai – 20 juin | Sagittaire | 22 nov. – 21 déc. |

#### Exercice C25 : permis de conduire 🟢

Demandez l'âge et un score de vue (0 à 10). Il faut au moins 18 ans et une vue de 6,0 ou plus. Affichez « Admissible », « Améliorez votre vue » ou « Trop jeune ».

#### Exercice C26 : retrait au distributeur 🟡

À partir d'un montant à retirer et d'un solde :

- refuser si le solde est insuffisant ;
- refuser si le montant n'est pas un multiple de 100 ;
- appliquer des **frais de 10 unités**.

Affichez le nouveau solde ou un message d'erreur.

#### Exercice C27 : format 12 heures 🟡

Convertissez une heure du format 24 h au format 12 h avec AM/PM : `13:15` → `1:15 PM`. Pensez à `00:xx` et `12:xx`.

#### Exercice C28 : politique de mot de passe 🟡

Vérifiez qu'un mot de passe a au moins 8 caractères, une majuscule, un chiffre et un caractère spécial. Affichez **chaque règle non respectée**, ou « Mot de passe fort » si tout est bon.

### 4.5 Compléments

#### Exercice C29 : valeurs « vraies » et « fausses » ➕ 🟡

Prédisez, puis vérifiez, le résultat de `if (valeur)` pour : `0`, `""`, `" "`, `"0"`, `[]`, `{}`, `null`, `undefined`, `NaN`, `-1`. Dressez la liste complète des valeurs « fausses » (*falsy*) de JavaScript.

#### Exercice C30 : clauses de garde ➕ 🟡

Réécrivez une fonction avec trois `if` imbriqués en utilisant des **retours anticipés** (*guard clauses*) : testez d'abord les cas d'erreur et sortez avec `return`. Comparez la lisibilité.

---

## 5. Partie 4 : boucles et itérations

### 5.1 Niveau de base

#### Exercice B1 : de 1 à 10 🟢

Affichez les nombres de 1 à 10.

#### Exercice B2 : nombres pairs jusqu'à 20 🟢

Affichez tous les nombres pairs de 1 à 20.

#### Exercice B3 : somme de 1 à N 🟢

Demandez `N` et affichez la somme des nombres de 1 à `N`.

#### Exercice B4 : table de multiplication 🟢

Demandez un nombre `n` et affichez sa table de multiplication (jusqu'à 10).

#### Exercice B5 : compte à rebours 🟢

Affichez les nombres de 10 à 1.

#### Exercice B6 : nombres impairs de 1 à 50 🟢

Affichez tous les nombres impairs de 1 à 50.

#### Exercice B7 : carrés de 1 à 10 🟢

Affichez `1 4 9 16 25 … 100`.

#### Exercice B8 : compte à rebours par pas de 5 🟢

Affichez `100, 95, 90, …, 0`.

#### Exercice B9 : somme des pairs jusqu'à N 🟢

Pour `n = 20`, affichez `2 + 4 + … + 20 = 110`.

#### Exercice B10 : l'alphabet avec les codes ASCII 🟢

Affichez `A` à `Z` (indice : `String.fromCharCode(65)` donne `"A"`).

### 5.2 Niveau intermédiaire

#### Exercice B11 : factorielle 🟡

Calculez la factorielle d'un nombre avec une boucle.

#### Exercice B12 : suite de Fibonacci 🟡

Affichez les `n` premiers nombres de la suite de Fibonacci. *(Voir l'exercice V45 pour la version récursive avec mémoïsation.)*

#### Exercice B13 : compter les chiffres 🟡

Comptez le nombre de chiffres d'un nombre.

#### Exercice B14 : somme des chiffres 🟡

Calculez la somme des chiffres d'un nombre (`%` et division entière).

#### Exercice B15 : nombre premier 🟡

Écrivez `estPremier(n)` avec une boucle. Optimisez en arrêtant la recherche à `√n`.

#### Exercice B16 : puissance sans `Math.pow()` 🟡

Pour `base = 2` et `exposant = 4`, calculez `2 × 2 × 2 × 2 = 16` avec une boucle.

#### Exercice B17 : nombre parfait 🟡

Un nombre parfait est égal à la somme de ses diviseurs (lui-même exclu) : `28 = 1 + 2 + 4 + 7 + 14`.

#### Exercice B18 : inverser une chaîne avec une boucle 🟡

`"hello"` devient `"olleh"`. *(Comparez avec l'exercice V36.)*

#### Exercice B19 : tous les chiffres sont pairs ? 🟡

`248` → `true` ; `243` → `false`.

#### Exercice B20 : somme de factorielles 🟡

Pour `4` : `1! + 2! + 3! + 4! = 33`.

### 5.3 Niveau difficile

#### Exercice B21 : nombre d'Armstrong 🔴

Vérifiez qu'un nombre est un nombre d'Armstrong (`153 = 1³ + 5³ + 3³`).

#### Exercice B22 : motif en triangle 🟡

Affichez ce motif avec des boucles imbriquées :

```text
*
**
***
****
*****
```

#### Exercice B23 : palindrome numérique 🔴

Vérifiez qu'un nombre est un palindrome (`121`, `1331`) **par calcul** (restes et divisions), sans transformer le nombre en chaîne.

#### Exercice B24 : PGCD 🔴

Trouvez le plus grand commun diviseur de deux nombres avec l'algorithme d'Euclide, dans une boucle.

#### Exercice B25 : PPCM 🔴

Trouvez le plus petit commun multiple de deux nombres avec une boucle (indice : `ppcm = a × b / pgcd`).

#### Exercice B26 : motif en pyramide 🔴

```text
    *
   ***
  *****
 *******
*********
```

#### Exercice B27 : binaire vers décimal 🔴

Convertissez `"1101"` en `13` avec une boucle.

#### Exercice B28 : suite de Collatz 🔴

Pour `6`, affichez `6 3 10 5 16 8 4 2 1`. Règles : si `n` est pair, `n / 2` ; sinon `n × 3 + 1` ; on répète jusqu'à `n = 1`.

#### Exercice B29 : nombres premiers de 1 à 100 🔴

Affichez tous les nombres premiers de 1 à 100 en réutilisant `estPremier()` (exercice B15).

#### Exercice B30 : jeu de devinette 🔴

Avec une boucle, laissez l'utilisateur deviner un nombre secret jusqu'à ce qu'il le trouve (« trop grand » / « trop petit »).

### 5.4 Compléments

#### Exercice B31 : choisir sa boucle ➕ 🟢

Affichez les nombres de 1 à 5 avec `for`, avec `while`, puis avec `do...while`. Dans quel cas `do...while` est-elle la seule adaptée ? *(Exemple : redemander une saisie jusqu'à ce qu'elle soit valide.)*

#### Exercice B32 : `for...of`, `for...in` et `Object.entries` ➕ 🟡

1. Parcourez un tableau avec `for...of`, puis avec `.entries()` pour obtenir aussi l'indice.
2. Parcourez les clés d'un objet avec `for...in`, puis avec `Object.entries()`.
3. Pourquoi ne faut-il pas utiliser `for...in` sur un tableau ?

#### Exercice B33 : `break`, `continue` et étiquettes ➕ 🟡

1. Affichez les nombres de 1 à 20, mais **sautez** les pairs (`continue`).
2. Cherchez le premier multiple de 7 supérieur à 50 et **arrêtez** la boucle (`break`).
3. Sortez de deux boucles imbriquées d'un coup avec une **étiquette**.

#### Exercice B34 : réécrire avec `map`, `filter` et `reduce` ➕ 🟡

Réécrivez sans boucle `for` : (a) le carré de chaque élément d'un tableau (`map`) ; (b) les nombres pairs d'un tableau (`filter`) ; (c) la somme d'un tableau (`reduce`). Enchaînez ensuite les trois sur `[1, 2, 3, 4, 5, 6]`.

---

## 6. Récapitulatif des changements

| Problème de l'original | Correction |
| --- | --- |
| Énoncés mélangeant français et anglais (défis 9 et 13) | Tout est en français |
| `prompt()` / `alert()` seuls (inexistants dans Node.js) | Module `entree.js` et contexte d'exécution documenté |
| Numérotation dupliquée (la section « Conditions » repartait à 1, 2, 3, 4) | Numérotation continue : V, C, B |
| Titres cassés (`#### 10. **BMI Calculator`, `#### 14. **Fibonacci…`) | Titres corrigés |
| Exercices répétés (palindrome ×3, voyelles ×2, majuscules ×3, mot le plus long ×2, pair/impair ×2, nombre premier ×3, IMC ×2, type de variable ×2, notes ×2) | Fusionnés ou renvoyés les uns vers les autres |
| Énoncé ambigu de la bourse (priorité `OU` / `ET`) | Expression logique explicite |
| Tableau des mentions « + / − » incomplet (« Continue for B, C, D, F ») | Tableau complet |
| `var`, `==`, `\|\|` comme seules références | Bonnes pratiques modernes (`const`, `let`, `===`, `??`, `?.`) |
| Notions absentes | `BigInt`, déstructuration, `spread`, `structuredClone`, truthy/falsy, clauses de garde, `for...of`, `map` / `filter` / `reduce` |
