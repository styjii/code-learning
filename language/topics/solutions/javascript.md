# ✅ Corrigés : exercices JavaScript

> Corrigés du document `javascript_1.md` : **20 défis de fonctions**, **50 exercices de variables et de types**, **30 exercices de conditions** et **34 exercices de boucles**. Chaque bloc de code a été **exécuté avec Node.js 22** ; les résultats attendus sont vérifiés par des `assert`.
>
> 💡 Essayez d'abord seul : il existe presque toujours plusieurs bonnes solutions.

## 📑 Sommaire

[0. Prérequis](#0-prérequis) · [Partie 1 : défis](#partie-1--défis-de-fonctions) · [Partie 2 : variables et types](#partie-2--variables-et-types-de-données) · [Partie 3 : conditions](#partie-3--conditions) · [Partie 4 : boucles](#partie-4--boucles-et-itérations)

---

## 0. Prérequis

Pour que ces corrigés soient **autovérifiés**, ils utilisent le module `assert` de Node.js : si un résultat est faux, le programme s'arrête avec une erreur. Si rien ne s'affiche, tout est correct.

```js
import assert from "node:assert/strict";

assert.equal(1 + 1, 2); // égalité stricte (===) ; échoue sinon
assert.deepEqual([1, 2], [1, 2]); // égalité profonde (tableaux, objets)
```

Pour les exercices interactifs, on utilise le module de saisie `entree.js` de l'énoncé (valable dans le navigateur et dans Node.js) :

```js
// fichier: entree.js
// entree.js : saisie utilisable dans le navigateur et dans Node.js
const estNavigateur =
    typeof window !== "undefined" && typeof window.prompt === "function";
let rl = null;
let lignes = null; // itérateur asynchrone : met les lignes en mémoire, même si elles arrivent d'avance

/** Pose une question. Renvoie la réponse (texte), ou `null` si l'utilisateur annule. */
export async function demander(question) {
    if (estNavigateur) return window.prompt(question);

    if (!rl) {
        const { createInterface } = await import("node:readline");
        rl = createInterface({ input: process.stdin });
        lignes = rl[Symbol.asyncIterator]();
    }
    process.stdout.write(`${question} `);
    const { value, done } = await lignes.next();
    return done ? null : value;
}

/** À appeler en fin de programme dans Node.js, sinon il ne s'arrête pas. */
export function fermer() {
    rl?.close();
}
```

---

# Partie 1 : défis de fonctions

## Défi 1 : passagers du bus

```js
import assert from "node:assert/strict";

// Pour chaque arrêt [montent, descendent], on ajoute les uns et on retire les autres
function nombrePassagers(arrets) {
    return arrets.reduce((total, [montent, descendent]) => total + montent - descendent, 0);
}

assert.equal(nombrePassagers([[10, 0], [3, 5], [5, 8]]), 5);
assert.equal(nombrePassagers([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]), 17);
assert.equal(nombrePassagers([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]), 21);
```

## Défi 2 : compter les moutons

```js
import assert from "node:assert/strict";

// `=== true` écarte `null`, `undefined` et `false`
const compterMoutons = (troupeau) => troupeau.filter((m) => m === true).length;

const troupeau = [
    true, true, true, false, true, true, true, true, true,
    false, true, false, true, false, false, true, true,
    true, true, true, false, false, true, true,
];

assert.equal(compterMoutons(troupeau), 17);
assert.equal(compterMoutons([true, null, undefined, false, true]), 2);
```

## Défi 3 : retirer premier et dernier caractères

```js
import assert from "node:assert/strict";

// slice(1, -1) : du 2ᵉ caractère jusqu'à l'avant-dernier
const retirerExtremites = (phrase) => phrase.slice(1, -1);

assert.equal(retirerExtremites("Ceci est une phrase"), "eci est une phras");
```

## Défi 4 : supprimer les chiffres

```js
import assert from "node:assert/strict";

// /\d/g : « chaque chiffre » (g = global : toutes les occurrences, pas seulement la première)
const nettoyerChaine = (texte) => texte.replace(/\d/g, "");

assert.equal(nettoyerChaine("! !"), "! !");
assert.equal(nettoyerChaine("123456789"), "");
assert.equal(nettoyerChaine("(E3at m2e2!!)"), "(Eat me!!)");
assert.equal(
    nettoyerChaine("Wh7y can't we3 bu1y the goo0d software3? #cheapskates3"),
    "Why can't we buy the good software? #cheapskates",
);
```

## Défi 5 : doubler chaque caractère

```js
import assert from "node:assert/strict";

// [...texte] découpe par caractères Unicode (les emojis restent entiers, contrairement à split(""))
const doublerCaracteres = (texte) => [...texte].map((c) => c + c).join("");

assert.equal(doublerCaracteres("String"), "SSttrriinngg");
assert.equal(doublerCaracteres("Hello World"), "HHeelllloo  WWoorrlldd"); // l'espace est doublé aussi
assert.equal(doublerCaracteres("1234!_ "), "11223344!!__  ");
```

## Défi 6 : supprimer les doublons et trier

```js
import assert from "node:assert/strict";

// Set supprime les doublons ; le tri DOIT recevoir une fonction de comparaison numérique
const supprimerDoublons = (nombres) => [...new Set(nombres)].sort((a, b) => a - b);

assert.deepEqual(supprimerDoublons([1, 1, 2, 4, 5, 2, 1, 2, 3, 5, 5, 5]), [1, 2, 3, 4, 5]);
assert.deepEqual(supprimerDoublons([10, 9, 2, 10]), [2, 9, 10]);
assert.deepEqual([10, 9, 2].sort(), [10, 2, 9]); // ⚠️ sans comparateur : tri alphabétique !
```

## Défi 7 : à qui le tour ?

```js
import assert from "node:assert/strict";

function prochainJoueur(joueur, victoire) {
    if (victoire) return joueur; // le gagnant rejoue
    return joueur === "black" ? "white" : "black";
}

assert.equal(prochainJoueur("black", false), "white");
assert.equal(prochainJoueur("white", true), "white");
assert.equal(prochainJoueur("white", false), "black");
```

## Défi 8 : calculer le pourboire

```js
import assert from "node:assert/strict";

const POURCENTAGES = { terrible: 0, poor: 5, good: 10, great: 15, excellent: 20 };

function calculerPourboire(addition, service) {
    const cle = service.toLowerCase();
    // Object.hasOwn évite les faux positifs comme "constructor" ou "toString"
    if (!Object.hasOwn(POURCENTAGES, cle)) return "Rating not recognised";
    return Math.ceil((addition * POURCENTAGES[cle]) / 100);
}

assert.equal(calculerPourboire(20, "ExcellEnt"), 4);
assert.equal(calculerPourboire(26.95, "goOd"), 3);
assert.equal(calculerPourboire(20, "hi"), "Rating not recognised");
assert.equal(calculerPourboire(20, "constructor"), "Rating not recognised");
assert.equal(calculerPourboire(100, "terrible"), 0);
```

## Défi 9 : `accum`

```js
import assert from "node:assert/strict";

// Le caractère d'indice i est répété i + 1 fois : 1 majuscule + i minuscules
function accum(texte) {
    return [...texte]
        .map((c, i) => c.toUpperCase() + c.toLowerCase().repeat(i))
        .join("-");
}

assert.equal(accum("abcd"), "A-Bb-Ccc-Dddd");
assert.equal(accum("RqaEzty"), "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy");
assert.equal(accum("cwAt"), "C-Ww-Aaa-Tttt");
```

## Défi 10 : compter comme la tribu Arara

```js
import assert from "node:assert/strict";

// Chaque paire = un « adak » ; un reste impair ajoute « anane »
function compterArara(nombre) {
    const mots = Array(Math.floor(nombre / 2)).fill("adak");
    if (nombre % 2 === 1) mots.push("anane");
    return mots.join(" ");
}

assert.equal(compterArara(1), "anane");
assert.equal(compterArara(2), "adak");
assert.equal(compterArara(3), "adak anane");
assert.equal(compterArara(8), "adak adak adak adak");
```

## Défi 11 : valider un code PIN

```js
import assert from "node:assert/strict";

// ^ et $ : le motif doit couvrir TOUTE la chaîne ; \d{4}|\d{6} : 4 ou 6 chiffres
const validerPIN = (pin) => /^(\d{4}|\d{6})$/.test(pin);

assert.equal(validerPIN("1234"), true);
assert.equal(validerPIN("123456"), true);
assert.equal(validerPIN("12345"), false);
assert.equal(validerPIN("a234"), false);
assert.equal(validerPIN("1234\n"), false); // le « $ » de JavaScript n'accepte pas le saut de ligne final
```

## Défi 12 : `toJadenCase`

```js
import assert from "node:assert/strict";

const enMajuscule = (mot) => mot.charAt(0).toUpperCase() + mot.slice(1);

// ✅ Bonne pratique : une simple fonction
const enJadenCase = (texte) => texte.split(" ").map(enMajuscule).join(" ");

// ⚠️ Exercice demandé : étendre le prototype (à éviter dans du vrai code)
String.prototype.toJadenCase = function () {
    return enJadenCase(String(this)); // `this` est un objet String : on le convertit
};

assert.equal("this is a sentence".toJadenCase(), "This Is A Sentence");
assert.equal(enJadenCase("this is a sentence"), "This Is A Sentence");
```

## Défi 13 : compter les voyelles

```js
import assert from "node:assert/strict";

// match renvoie null s'il n'y a aucune correspondance : d'où `?? []`
const compterVoyelles = (texte) => (texte.match(/[aeiou]/gi) ?? []).length;

assert.equal(compterVoyelles("This is a sentence"), 6);
assert.equal(compterVoyelles("rhythm"), 0);
```

## Défi 14 : choix de repas

```js
import assert from "node:assert/strict";

const inscrits = [
    { firstName: "Noah", meal: "vegetarian" },
    { firstName: "Anna", meal: "standard" },
    { firstName: "Ramona", meal: "vegan" },
    { firstName: "George", meal: "vegetarian" },
];

// Approche 1 : reduce
function compterRepas(liste) {
    return liste.reduce((compteurs, { meal }) => {
        compteurs[meal] = (compteurs[meal] ?? 0) + 1;
        return compteurs;
    }, {});
}

// Approche 2 : Object.groupBy (ES2024, Node.js 21+) puis comptage de chaque groupe
function compterRepasGroupBy(liste) {
    const groupes = Object.groupBy(liste, ({ meal }) => meal);
    return Object.fromEntries(Object.entries(groupes).map(([repas, gens]) => [repas, gens.length]));
}

const attendu = { vegetarian: 2, standard: 1, vegan: 1 };
assert.deepEqual(compterRepas(inscrits), attendu);
assert.deepEqual(compterRepasGroupBy(inscrits), attendu);
```

## Défi 15 : effet compteur

```js
import assert from "node:assert/strict";

// Pour chaque chiffre c : un tableau [0, 1, …, c] (c + 1 éléments)
const effetCompteur = (chiffres) =>
    [...chiffres].map((c) => Array.from({ length: Number(c) + 1 }, (_, i) => i));

assert.deepEqual(effetCompteur("1250"), [[0, 1], [0, 1, 2], [0, 1, 2, 3, 4, 5], [0]]);
```

## Défi 16 : le nombre le plus long

```js
import assert from "node:assert/strict";

const nombreDeChiffres = (n) => String(Math.abs(n)).length; // abs : le signe « - » n'est pas un chiffre

// `>` strict : en cas d'égalité, on garde le premier
const nombreLePlusLong = (nombres) =>
    nombres.reduce((meilleur, n) => (nombreDeChiffres(n) > nombreDeChiffres(meilleur) ? n : meilleur));

assert.equal(nombreLePlusLong([1, 10, 100]), 100);
assert.equal(nombreLePlusLong([-100, 25, 7]), -100);
assert.equal(nombreLePlusLong([12, 34]), 12); // égalité : le premier
```

## Défi 17 : le mot le plus court

```js
import assert from "node:assert/strict";

const longueurMotCourt = (phrase) => Math.min(...phrase.split(/\s+/).map((mot) => mot.length));

assert.equal(longueurMotCourt("bitcoin take over the world maybe who knows perhaps"), 3);
```

## Défi 18 : le mot le plus long

```js
import assert from "node:assert/strict";

// `>=` : à longueur égale, le mot courant remplace le précédent, donc on garde le dernier
const motLePlusLong = (phrase) =>
    phrase.split(/\s+/).reduce((meilleur, mot) => (mot.length >= meilleur.length ? mot : meilleur), "");

assert.equal(motLePlusLong("a b c d e fgh"), "fgh");
assert.equal(motLePlusLong("aa bb c"), "bb");
```

## Défi 19 : image en niveaux de gris

```js
import assert from "node:assert/strict";

const enNiveauxDeGris = (image) =>
    image.map((ligne) =>
        ligne.map(([r, v, b]) => {
            const gris = Math.round((r + v + b) / 3);
            return [gris, gris, gris];
        }),
    );

const image = [
    [[123, 231, 12], [56, 43, 124]],
    [[78, 152, 76], [64, 132, 200]],
];

assert.deepEqual(enNiveauxDeGris(image), [
    [[122, 122, 122], [74, 74, 74]],
    [[102, 102, 102], [132, 132, 132]],
]);
```

## Défi 20 : carré de chaque chiffre

```js
import assert from "node:assert/strict";

const carresDesChiffres = (nombre) =>
    Number([...String(nombre)].map((c) => Number(c) ** 2).join(""));

assert.equal(carresDesChiffres(9119), 811181);
```

---

# Partie 2 : variables et types de données

## 3.1 Déclarer et manipuler

### V1 : corriger le code

Les erreurs : `Alice` et `Painting` ne sont **pas entourés de guillemets** (JavaScript cherche des variables de ce nom : `ReferenceError`), et `var` est à remplacer par `const`.

```js
const name = "Alice";
const age = 20; // ou "twenty" si vous voulez garder une chaîne : mais un nombre est plus logique
const hobby = "Painting";

console.log(`Mon nom est ${name}, j'ai ${age} ans et j'aime ${hobby}.`);
```

### V2 : quiz de type

**Réponse : B (`string`)** : les guillemets font de `"42"` une chaîne.

### V3 : présentation personnelle

```js
const firstName = "Alice";
const favoriteNumber = 7;
const city = "Antananarivo";

console.log(`Salut ! Je suis ${firstName}, j'habite à ${city} et mon nombre préféré est ${favoriteNumber}.`);
```

### V4 : déclarer et réassigner

```js
import assert from "node:assert/strict";

const name = "Alice";

let age = 30;
age = 31; // réassignation : possible avec `let`
assert.equal(age, 31);

// Plusieurs variables en une instruction (possible, mais une par ligne est plus lisible)
let firstName = "Alice", lastName = "Martin", country = "Madagascar", isMarried = false;
assert.equal(`${firstName} ${lastName}`, "Alice Martin");
```

### V5 : `const` et `let`

```js
import assert from "node:assert/strict";

const PI = 3.14;
let radius = 5;
const aire = PI * radius ** 2;
assert.equal(aire, 78.5);

// Modifier une constante lève une TypeError
assert.throws(() => {
    PI = 3;
}, { name: "TypeError", message: "Assignment to constant variable." });
```

### V6 : `typeof`

```js
import assert from "node:assert/strict";

assert.equal(typeof "texte", "string");
assert.equal(typeof 42, "number");
assert.equal(typeof true, "boolean");
assert.equal(typeof undefined, "undefined");
assert.equal(typeof null, "object"); // ⚠️ bogue historique du langage, conservé pour la compatibilité
assert.equal(typeof [1, 2], "object"); // un tableau est un objet : utilisez Array.isArray
assert.equal(Array.isArray([1, 2]), true);
assert.equal(typeof function () {}, "function");
assert.equal(typeof 10n, "bigint");
assert.equal(typeof Symbol("x"), "symbol");
```

### V7 : échanger deux variables

```js
import assert from "node:assert/strict";

let a = 1, b = 2;

// Avec une variable temporaire
let temp = a; a = b; b = temp;
assert.deepEqual([a, b], [2, 1]);

// Avec la déstructuration
[a, b] = [b, a];
assert.deepEqual([a, b], [1, 2]);
```

### V8 : valeurs par défaut (`||` contre `??`)

```js
import assert from "node:assert/strict";

const avecOu = (v) => v || "Invité";
const avecNullish = (v) => v ?? "Invité";

// `||` remplace TOUTES les valeurs « fausses » ; `??` seulement null et undefined
assert.equal(avecOu(""), "Invité");
assert.equal(avecNullish(""), ""); // la chaîne vide est conservée
assert.equal(avecOu(0), "Invité");
assert.equal(avecNullish(0), 0); // zéro est conservé
assert.equal(avecOu(null), "Invité");
assert.equal(avecNullish(null), "Invité");
assert.equal(avecOu(undefined), "Invité");
assert.equal(avecNullish(undefined), "Invité");
```

> ✅ Utilisez `??` quand `0`, `""` ou `false` sont des valeurs **légitimes** (une quantité de 0, un champ volontairement vide).

### V9 : `null` contre `undefined`

```js
import assert from "node:assert/strict";

let vide = null; // « aucune valeur », volontaire
let nonDefinie; // « pas encore de valeur » : undefined

assert.equal(vide == nonDefinie, true); // == fait des conversions : null et undefined sont « égaux »
assert.equal(vide === nonDefinie, false); // === compare aussi les types : différents
```

### V10 : portée et fermetures

```js
import assert from "node:assert/strict";

let x = 10;
function externe() {
    let x = 20;
    return function interne() {
        return x;
    };
}
assert.equal(externe()(), 20); // la fermeture se souvient du x de `externe`, pas du x global (10)

// Prolongement : hoisting et zone morte temporelle
assert.equal(a, undefined); // `var` est « hissée » : elle existe déjà, valant undefined
var a = 1;
assert.throws(() => b, ReferenceError); // `let` est dans la « zone morte » avant sa déclaration
let b = 2;
assert.equal(x + a + b, 13);
```

## 3.2 Nombres

### V11 à V13 : opérations, arrondis, aléatoire

```js
import assert from "node:assert/strict";

// V11
assert.equal(7 + 3, 10);
assert.equal(7 - 3, 4);
assert.equal(7 * 3, 21);
assert.equal(7 / 2, 3.5); // en JavaScript, / donne un résultat décimal (pas de division entière)
assert.equal(15 % 4, 3); // reste
assert.equal(2 ** 10, 1024); // puissance

// V12 : arrondis
assert.deepEqual([Math.floor(4.7), Math.ceil(4.7), Math.round(4.7), Math.trunc(4.7)], [4, 5, 5, 4]);
assert.deepEqual([Math.floor(-4.7), Math.ceil(-4.7), Math.round(-4.7), Math.trunc(-4.7)], [-5, -4, -5, -4]);
// Pour les négatifs : floor va vers le bas (-5), trunc coupe simplement les décimales (-4)
assert.equal((4.7).toFixed(1), "4.7"); // toFixed renvoie une CHAÎNE

// V13 : nombre aléatoire
const entre1et100 = Math.floor(Math.random() * 100) + 1;
assert.ok(entre1et100 >= 1 && entre1et100 <= 100);

// Entier entre min et max INCLUS
const entierAleatoire = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;
for (let i = 0; i < 1000; i++) {
    const n = entierAleatoire(3, 6);
    assert.ok(Number.isInteger(n) && n >= 3 && n <= 6);
}
```

### V14 : conversions de types

```js
import assert from "node:assert/strict";

assert.equal(String(123), "123");
assert.equal((123).toString(), "123");
assert.equal(Number("123"), 123);
assert.equal(parseInt("123", 10), 123); // toujours préciser la base (10)
assert.equal(Boolean("true"), true);

// Différences entre les trois conversions numériques
assert.ok(Number.isNaN(Number("12px"))); // Number est strict : toute la chaîne doit être numérique
assert.equal(parseInt("12px", 10), 12); // parseInt s'arrête au premier caractère invalide
assert.equal(parseFloat("3.14abc"), 3.14);

// ⚠️ Piège : toute chaîne non vide est « vraie », même "false" ou "0"
assert.equal(Boolean("false"), true);
assert.equal(Boolean("0"), true);
assert.equal(Boolean(""), false);
```

### V15 : `NaN` et validation numérique

```js
import assert from "node:assert/strict";

// isNaN convertit d'abord en nombre : "hello" devient NaN, donc true (trompeur)
assert.equal(isNaN("hello"), true);
assert.equal(isNaN(123), false);
// Number.isNaN ne convertit pas : elle ne renvoie true que pour la valeur NaN elle-même
assert.equal(Number.isNaN("hello"), false);
assert.equal(Number.isNaN(NaN), true);

// Valide qu'un TEXTE saisi est un nombre : attention à "" et " " (Number("") vaut 0 !)
function estNombre(saisie) {
    return saisie.trim() !== "" && Number.isFinite(Number(saisie));
}

assert.equal(estNombre("42"), true);
assert.equal(estNombre("3.14"), true);
assert.equal(estNombre(""), false);
assert.equal(estNombre("   "), false);
assert.equal(estNombre("12px"), false);
assert.equal(estNombre("Infinity"), false);
```

### V16 à V21 : petits calculs

```js
import assert from "node:assert/strict";

const celsiusEnFahrenheit = (c) => (c * 9) / 5 + 32; // V16
const interetsSimples = (capital, taux, duree) => (capital * taux * duree) / 100; // V17
const ageEnJours = (annees) => annees * 365; // V18 (sans années bissextiles)
const prixRemise = (prix, remisePct) => prix * (1 - remisePct / 100); // V19

const TAUX_EUR = 0.92; // V20 : taux FICTIF pour 1 USD, défini à un seul endroit
const usdEnEur = (usd) => usd * TAUX_EUR;

const imc = (poids, taille) => poids / taille ** 2; // V21

assert.equal(celsiusEnFahrenheit(100), 212);
assert.equal(celsiusEnFahrenheit(0), 32);
assert.equal(interetsSimples(1000, 5, 2), 100);
assert.equal(ageEnJours(30), 10950);
assert.equal(prixRemise(1000, 25), 750);
assert.equal(usdEnEur(100), 92);
assert.equal(imc(70, 1.75).toFixed(1), "22.9");
```

### V22 : précision des décimaux

```js
import assert from "node:assert/strict";

assert.notEqual(0.1 + 0.2, 0.3); // 0.30000000000000004 : les nombres sont stockés en binaire

// Solution 1 : arrondir le résultat à un nombre raisonnable de décimales
const additionSure = (a, b) => Number((a + b).toFixed(10));
assert.equal(additionSure(0.1, 0.2), 0.3);

// Solution 2 : comparer avec une tolérance plutôt que de tester l'égalité exacte
const presqueEgaux = (a, b) => Math.abs(a - b) < Number.EPSILON * Math.max(1, Math.abs(a), Math.abs(b));
assert.equal(presqueEgaux(0.1 + 0.2, 0.3), true);

// Solution 3 : travailler en entiers (centimes) pour l'argent
assert.equal((10 + 20) / 100, 0.3);
```

### V23 : grands nombres et `BigInt`

```js
import assert from "node:assert/strict";

assert.equal(Number.MAX_SAFE_INTEGER, 9007199254740991);
// Au-delà, les entiers ne sont plus représentés exactement : ...993 n'existe pas
assert.equal(Number.MAX_SAFE_INTEGER + 2, 9007199254740992);
assert.equal(9007199254740991n + 2n, 9007199254740993n); // BigInt : exact

function factorielleBig(n) {
    let r = 1n;
    for (let i = 2n; i <= BigInt(n); i++) r *= i;
    return r;
}
assert.equal(factorielleBig(25), 15511210043330985984000000n);

// Avec des Number, 25! n'est pas représentable exactement (au-delà de ~9 × 10^15, il manque des chiffres)
let approx = 1;
for (let i = 2; i <= 25; i++) approx *= i;
assert.notEqual(BigInt(approx), factorielleBig(25));
// ⚠️ On ne peut pas mélanger BigInt et Number : 1n + 1 lève une TypeError
assert.throws(() => 1n + 1, TypeError);
```

### V24 : nombre en toutes lettres (0–9999)

```js
import assert from "node:assert/strict";

const UNITES = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf",
    "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize"];
const DIZAINES = ["", "", "vingt", "trente", "quarante", "cinquante", "soixante"];

// 1 à 99
function moinsDeCent(n) {
    if (n < 17) return UNITES[n];
    if (n < 20) return `dix-${UNITES[n - 10]}`;
    if (n < 70) {
        const d = Math.floor(n / 10), u = n % 10;
        if (u === 0) return DIZAINES[d];
        return u === 1 ? `${DIZAINES[d]} et un` : `${DIZAINES[d]}-${UNITES[u]}`;
    }
    if (n < 80) return n === 71 ? "soixante et onze" : `soixante-${moinsDeCent(n - 60)}`;
    if (n === 80) return "quatre-vingts"; // pluriel : rien ne suit
    return `quatre-vingt-${moinsDeCent(n - 80)}`;
}

// 1 à 999
function moinsDeMille(n) {
    const c = Math.floor(n / 100), reste = n % 100;
    if (c === 0) return moinsDeCent(reste);
    let texte = c === 1 ? "cent" : `${UNITES[c]} cent`;
    if (reste === 0) return c > 1 ? `${texte}s` : texte; // « deux cents » mais « deux cent un »
    return `${texte} ${moinsDeCent(reste)}`;
}

function enLettres(n) {
    if (!Number.isInteger(n) || n < 0 || n > 9999) throw new RangeError("Nombre hors de la plage 0–9999");
    if (n === 0) return "zéro";
    const m = Math.floor(n / 1000), reste = n % 1000;
    const milliers = m === 0 ? "" : m === 1 ? "mille" : `${UNITES[m]} mille`; // « mille » est invariable
    const unites = reste === 0 ? "" : moinsDeMille(reste);
    return [milliers, unites].filter(Boolean).join(" ");
}

assert.equal(enLettres(0), "zéro");
assert.equal(enLettres(21), "vingt et un");
assert.equal(enLettres(71), "soixante et onze");
assert.equal(enLettres(80), "quatre-vingts");
assert.equal(enLettres(91), "quatre-vingt-onze");
assert.equal(enLettres(100), "cent");
assert.equal(enLettres(200), "deux cents");
assert.equal(enLettres(234), "deux cent trente-quatre");
assert.equal(enLettres(1000), "mille");
assert.equal(enLettres(1234), "mille deux cent trente-quatre");
assert.equal(enLettres(3080), "trois mille quatre-vingts");
assert.equal(enLettres(9999), "neuf mille neuf cent quatre-vingt-dix-neuf");
```

## 3.3 Chaînes de caractères

### V25 à V27 : concaténation, accès, méthodes

```js
import assert from "node:assert/strict";

// V25
const nom = "Alice", age = 30;
assert.equal("Hello" + " " + "World", "Hello World");
assert.equal("Hello".concat(" ", "World"), "Hello World");
assert.equal(`${"Hello"} ${"World"}`, "Hello World");
assert.equal(`Bonjour, je m'appelle ${nom} et j'ai ${age} ans.`, "Bonjour, je m'appelle Alice et j'ai 30 ans.");

// V26
const mot = "JavaScript";
assert.equal(mot.length, 10);
assert.equal(mot[0], "J");
assert.equal(mot[Math.floor(mot.length / 2)], "c"); // caractère du milieu (indice 5)
assert.equal(mot.at(-1), "t"); // .at(-1) : dernier caractère
assert.equal(mot[mot.length - 1], "t"); // équivalent à l'ancienne

// V27 : les sept manipulations
assert.equal("Hello".toUpperCase(), "HELLO");
assert.equal("Hello".toLowerCase(), "hello");
assert.equal("   hello   ".trim(), "hello");
assert.equal("JavaScript".slice(4, 10), "Script");
assert.equal("JavaScript".substring(4, 10), "Script");
assert.equal("The dog barked, the dog ran".replace("dog", "cat"), "The cat barked, the dog ran"); // une seule
assert.equal("The dog barked, the dog ran".replaceAll("dog", "cat"), "The cat barked, the cat ran"); // toutes
assert.deepEqual("apple,banana,orange".split(","), ["apple", "banana", "orange"]);
assert.equal("JavaScript".includes("Script"), true);
assert.equal("ha".repeat(5), "hahahahaha");
```

### V28 à V35 : manipulations pratiques

```js
import assert from "node:assert/strict";

// V28 : split + déstructuration
const [prenom, nomFamille] = "John Doe".split(" ");
assert.deepEqual([prenom, nomFamille], ["John", "Doe"]);

// V29 : e-mail (contrôle simplifié)
const emailValide = (e) => e.includes("@") && e.includes(".") && e.endsWith(".com");
assert.equal(emailValide("alice@example.com"), true);
assert.equal(emailValide("alice@example.org"), false);
assert.equal(emailValide("alice.example.com"), false);

// V30 : nom d'utilisateur
const nomUtilisateur = (complet, nombre) => `${complet.toLowerCase().replace(" ", ".")}${nombre}`;
assert.equal(nomUtilisateur("John Smith", 23), "john.smith23");

// V31 : initiales
const initiales = (nomComplet) =>
    nomComplet.split(" ").map((m) => `${m[0].toUpperCase()}.`).join("");
assert.equal(initiales("Harry James Potter"), "H.J.P.");

// V32 : abréviation « i18n »
const abreviation = (mot) => (mot.length <= 2 ? mot : `${mot[0]}${mot.length - 2}${mot.at(-1)}`);
assert.equal(abreviation("Internationalization"), "I18n");
assert.equal(abreviation("ab"), "ab");

// V33 : masquer un numéro de carte
const masquer = (carte) => carte.slice(-4).padStart(carte.length, "*");
assert.equal(masquer("1234567812345678"), "************5678");

// V34 : pluriel (comme dans l'énoncé : singulier seulement pour 1)
const articles = (n) => (n === 1 ? "1 article" : `${n} articles`);
assert.equal(articles(1), "1 article");
assert.equal(articles(3), "3 articles");
// Nuance : en français, 0 s'accorde au singulier ("0 article") ; utilisez `Math.abs(n) < 2`.
// Pour du vrai multilingue : Intl.PluralRules.

// V35 : vide ou uniquement des espaces
const estVideOuBlanc = (s) => s.trim() === "";
assert.equal(estVideOuBlanc(""), true);
assert.equal(estVideOuBlanc("   \t\n"), true);
assert.equal(estVideOuBlanc(" a "), false);
```

### V36 et V37 : inverser et palindromes

```js
import assert from "node:assert/strict";

// V36
const inverser = (s) => [...s].reverse().join(""); // [...s] gère les emojis, contrairement à split("")
const inverserMots = (s) => s.split(" ").reverse().join(" ");
assert.equal(inverser("JavaScript"), "tpircSavaJ");
assert.equal(inverserMots("hello world"), "world hello");

// V37 : palindromes
const estPalindromeSimple = (mot) => mot === inverser(mot);

// \p{L} = lettre Unicode, \p{N} = chiffre Unicode (le drapeau u active ces classes)
function estPalindrome(texte) {
    const utiles = [...texte.toLowerCase()].filter((c) => /[\p{L}\p{N}]/u.test(c)).join("");
    return utiles === inverser(utiles);
}

assert.equal(estPalindromeSimple("radar"), true);
assert.equal(estPalindromeSimple("hello"), false);
assert.equal(estPalindrome("A man, a plan, a canal: Panama"), true);
assert.equal(estPalindrome("Was it a car or a cat I saw?"), true);
assert.equal(estPalindrome("hello"), false);
```

### V38 : compression par plages

```js
import assert from "node:assert/strict";

// (.)\1* : un caractère suivi de ses répétitions immédiates
const compresser = (s) => s.replace(/(.)\1*/gs, (bloc, c) => c + bloc.length);

// (\D)(\d+) : un caractère non numérique suivi d'un nombre
const decompresser = (s) => s.replace(/(\D)(\d+)/g, (_, c, n) => c.repeat(Number(n)));

assert.equal(compresser("aaabbbbcc"), "a3b4c2");
assert.equal(decompresser("a3b4c2"), "aaabbbbcc");
assert.equal(decompresser(compresser("abc")), "abc"); // "a1b1c1" : la compression n'est pas toujours plus courte
// Limite : si le texte d'origine contient des chiffres, la décompression devient ambiguë.
```

### V39 à V41 : anagrammes, `split` manuel, caractère fréquent

```js
import assert from "node:assert/strict";

// V39
const cle = (s) => [...s.toLowerCase().replace(/\s/g, "")].sort().join("");
const sontAnagrammes = (a, b) => cle(a) === cle(b);
assert.equal(sontAnagrammes("Listen", "Silent"), true);
assert.equal(sontAnagrammes("Chien", "Niche"), true);
assert.equal(sontAnagrammes("abc", "abd"), false);

// V40 : imiter String.prototype.split
function decouper(texte, separateur) {
    if (separateur === "") return [...texte];
    const morceaux = [];
    let debut = 0;
    let i;
    while ((i = texte.indexOf(separateur, debut)) !== -1) {
        morceaux.push(texte.slice(debut, i));
        debut = i + separateur.length;
    }
    morceaux.push(texte.slice(debut));
    return morceaux;
}
for (const [t, s] of [["a,b,c", ","], ["a--b--c", "--"], ["abc", ""], ["", ","], [",a,", ","]]) {
    assert.deepEqual(decouper(t, s), t.split(s));
}

// V41 : caractère le plus fréquent
function plusFrequent(texte) {
    const compteurs = new Map();
    for (const c of texte) compteurs.set(c, (compteurs.get(c) ?? 0) + 1);
    let meilleur = { caractere: "", occurrences: 0 };
    for (const [caractere, occurrences] of compteurs) {
        if (occurrences > meilleur.occurrences) meilleur = { caractere, occurrences };
    }
    return meilleur;
}
assert.deepEqual(plusFrequent("abracadabra"), { caractere: "a", occurrences: 5 });
```

## 3.4 Structures de données et logique

### V42 : déstructuration, `spread` et `rest`

```js
import assert from "node:assert/strict";

// 1. Déstructuration avec valeur par défaut
const { nom, age = 18 } = { nom: "Alice" };
assert.deepEqual([nom, age], ["Alice", 18]);

// 2. Copies avec spread
const original = { a: 1, interne: { x: 1 } };
const tableau = [1, 2, 3];
const copieTab = [...tableau, 4];
const copieObj = { ...original, a: 2 };
assert.deepEqual(tableau, [1, 2, 3]); // l'original ne change pas
assert.equal(original.a, 1);

// 3. Paramètre rest
const somme = (...nombres) => nombres.reduce((s, n) => s + n, 0);
assert.equal(somme(1, 2, 3, 4), 10);

// 4. Copie superficielle contre copie profonde
copieObj.interne.x = 99; // l'objet imbriqué est PARTAGÉ avec l'original !
assert.equal(original.interne.x, 99);

const profonde = structuredClone(original);
profonde.interne.x = 0;
assert.equal(original.interne.x, 99); // la copie profonde est indépendante
assert.equal(copieTab.length, 4);
```

### V43 : égalité profonde

```js
import assert from "node:assert/strict";
import { isDeepStrictEqual } from "node:util";

function egaliteProfonde(a, b) {
    if (a === b || (Number.isNaN(a) && Number.isNaN(b))) return true;
    if (typeof a !== "object" || typeof b !== "object" || a === null || b === null) return false;
    if (Array.isArray(a) !== Array.isArray(b)) return false;

    const clesA = Object.keys(a);
    const clesB = Object.keys(b);
    if (clesA.length !== clesB.length) return false;
    return clesA.every((k) => Object.hasOwn(b, k) && egaliteProfonde(a[k], b[k]));
}

assert.equal(egaliteProfonde({ a: 1 }, { a: 1 }), true);
assert.equal(egaliteProfonde([1, 2], [1, 2]), true);
assert.equal(egaliteProfonde({ a: [1, { b: 2 }] }, { a: [1, { b: 3 }] }), false);
assert.equal(egaliteProfonde({ a: 1 }, { a: 1, b: 2 }), false);
assert.equal(egaliteProfonde([], {}), false);
assert.equal(egaliteProfonde(NaN, NaN), true);
// Cette version ne gère ni les dates, ni les Map/Set : en vrai code, utilisez `isDeepStrictEqual`
assert.equal(isDeepStrictEqual({ a: [1, { b: 2 }] }, { a: [1, { b: 2 }] }), true);
```

### V44 : détecter le type

```js
import assert from "node:assert/strict";

function obtenirType(valeur) {
    if (valeur === null) return "null";
    if (Array.isArray(valeur)) return "array";
    return typeof valeur; // "object", "number", "string", "boolean", "undefined", "function"…
}

assert.equal(obtenirType([]), "array");
assert.equal(obtenirType(null), "null");
assert.equal(obtenirType("hello"), "string");
assert.equal(obtenirType({}), "object");
assert.equal(obtenirType(undefined), "undefined");
assert.equal(obtenirType(3), "number");
assert.equal(obtenirType(true), "boolean");
```

### V45 : Fibonacci avec mémoïsation

```js
import assert from "node:assert/strict";

function fib(n, memo = new Map()) {
    if (n < 2) return n;
    if (memo.has(n)) return memo.get(n); // déjà calculé : on ne refait pas
    const resultat = fib(n - 1, memo) + fib(n - 2, memo);
    memo.set(n, resultat);
    return resultat;
}

const fibNaive = (n) => (n < 2 ? n : fibNaive(n - 1) + fibNaive(n - 2));

assert.equal(fib(10), 55);
assert.equal(fib(50), 12586269025);

let debut = performance.now();
fib(40);
const tempsMemo = performance.now() - debut;
debut = performance.now();
assert.equal(fibNaive(32), 2178309); // 32 suffit pour sentir la différence
const tempsNaif = performance.now() - debut;
console.log(`mémoïsée : ${tempsMemo.toFixed(2)} ms, naïve (n = 32) : ${tempsNaif.toFixed(0)} ms`);
```

### V46 : évaluateur d'expressions (sans `eval`)

```js
import assert from "node:assert/strict";

// Gère + - * / avec priorité de * et /, nombres positifs ou décimaux, espaces libres
function evaluer(expression) {
    const jetons = expression.match(/\d+(?:\.\d+)?|[+\-*/]/g);
    if (!jetons || jetons.join("") !== expression.replace(/\s/g, "") || jetons.length % 2 === 0) {
        throw new SyntaxError(`Expression invalide : « ${expression} »`);
    }

    // Passe 1 : on effectue tout de suite les * et / ; on garde des termes à additionner
    const termes = [Number(jetons[0])];
    const signes = [];
    for (let i = 1; i < jetons.length; i += 2) {
        const operateur = jetons[i];
        const nombre = Number(jetons[i + 1]);
        if (operateur === "*") termes[termes.length - 1] *= nombre;
        else if (operateur === "/") termes[termes.length - 1] /= nombre;
        else {
            signes.push(operateur);
            termes.push(nombre);
        }
    }

    // Passe 2 : les additions et soustractions, de gauche à droite
    return signes.reduce((total, signe, i) => (signe === "+" ? total + termes[i + 1] : total - termes[i + 1]), termes[0]);
}

assert.equal(evaluer("3 + 5 * 2"), 13);
assert.equal(evaluer("10 - 4 - 3"), 3);
assert.equal(evaluer("2 * 3 + 4 * 5"), 26);
assert.equal(evaluer("100 / 4 / 5"), 5);
assert.equal(evaluer("1.5 + 2.5"), 4);
assert.equal(evaluer("7"), 7);
assert.throws(() => evaluer("3 +"), SyntaxError);
assert.throws(() => evaluer("3 + abc"), SyntaxError);
```

> ⚠️ Cette version n'accepte pas les nombres négatifs ni les parenthèses ; pour cela, il faut un vrai analyseur (algorithme *shunting-yard* ou analyse récursive descendante).

### V47 : casse de titre avec exceptions

```js
import assert from "node:assert/strict";

const PETITS_MOTS = new Set(["the", "and", "of", "a", "an", "in", "on", "at", "to", "for", "or"]);

const enTitre = (texte) =>
    texte
        .split(" ")
        .map((mot, i) =>
            i > 0 && PETITS_MOTS.has(mot.toLowerCase())
                ? mot.toLowerCase()
                : mot.charAt(0).toUpperCase() + mot.slice(1).toLowerCase(),
        )
        .join(" ");

assert.equal(enTitre("the lord of the rings"), "The Lord of the Rings");
assert.equal(enTitre("a tale OF two cities"), "A Tale of Two Cities");
```

## 3.5 Mini-projets

### V48 à V50

```js
import assert from "node:assert/strict";

// V48
const saluer = (nom) => `Bonjour, ${nom} !`;
assert.equal(saluer("Alice"), "Bonjour, Alice !");

// V49 : avec puis sans les espaces
const compterCaracteres = (texte) => ({
    total: texte.length,
    sansEspaces: texte.replace(/\s/g, "").length,
});
assert.deepEqual(compterCaracteres("Bonjour tout le monde"), { total: 21, sansEspaces: 18 });

// V50 : la saisie est du TEXTE : on convertit avant de comparer
const verifierReponse = (saisie) => saisie !== null && Number(saisie.trim()) === 5 + 7;
assert.equal(verifierReponse("12"), true);
assert.equal(verifierReponse(" 12 "), true);
assert.equal(verifierReponse("57"), false); // "5" + "7" concaténés : le piège classique
assert.equal(verifierReponse(null), false);
```

Version interactive du quiz (V50) :

```js
// @stdin: 12
import { demander, fermer } from "./entree.js";

const reponse = await demander("Combien font 5 + 7 ?");
console.log(reponse !== null && Number(reponse.trim()) === 12 ? "Bravo !" : "Raté.");
fermer();
```

---

# Partie 3 : conditions

## 4.1 Niveau de base

### C1 à C5

```js
import assert from "node:assert/strict";

// C1 : -3 % 2 vaut -1 (pas 1) : on teste donc `=== 0` plutôt que `=== 1`
const parite = (n) => (n % 2 === 0 ? "Pair" : "Impair");
assert.equal(parite(7), "Impair");
assert.equal(parite(-3), "Impair");
assert.equal(parite(0), "Pair");

// C2
function signe(n) {
    if (n > 0) return "Positif";
    if (n < 0) return "Négatif";
    return "Nul";
}
assert.deepEqual([signe(5), signe(-2), signe(0)], ["Positif", "Négatif", "Nul"]);

// C3
function trancheAge(age) {
    if (age < 0) throw new RangeError("Âge négatif");
    if (age <= 12) return "Enfant";
    if (age <= 19) return "Adolescent";
    if (age <= 64) return "Adulte";
    return "Senior";
}
assert.deepEqual([trancheAge(5), trancheAge(15), trancheAge(40), trancheAge(70)], ["Enfant", "Adolescent", "Adulte", "Senior"]);

// C4
const plusGrand = (a, b) => (a > b ? a : b); // ou Math.max(a, b)
assert.equal(plusGrand(3, 9), 9);

// C5 : divisible par 4 ET (non divisible par 100 OU divisible par 400)
const estBissextile = (annee) => (annee % 4 === 0 && annee % 100 !== 0) || annee % 400 === 0;
assert.deepEqual([estBissextile(2024), estBissextile(2023), estBissextile(1900), estBissextile(2000)], [true, false, false, true]);
```

## 4.2 Niveau intermédiaire

### C6 : calculateur de note (avec « + » et « − »)

```js
import assert from "node:assert/strict";

// Table triée du seuil le plus haut au plus bas : le premier seuil atteint gagne
const SEUILS = [
    [97, "A+"], [93, "A"], [90, "A-"],
    [87, "B+"], [83, "B"], [80, "B-"],
    [77, "C+"], [73, "C"], [70, "C-"],
    [67, "D+"], [63, "D"], [60, "D-"],
];

function mention(note) {
    if (!(note >= 0 && note <= 100)) throw new RangeError("La note doit être comprise entre 0 et 100");
    return SEUILS.find(([min]) => note >= min)?.[1] ?? "F";
}

// Version simple (A à F) : on retire simplement le « + » ou le « − »
const mentionSimple = (note) => mention(note)[0];

assert.deepEqual([mention(100), mention(96), mention(92), mention(88), mention(84), mention(60), mention(59)], ["A+", "A", "A-", "B+", "B", "D-", "F"]);
assert.deepEqual([mentionSimple(95), mentionSimple(85), mentionSimple(75), mentionSimple(65), mentionSimple(10)], ["A", "B", "C", "D", "F"]);
assert.throws(() => mention(101), RangeError);
assert.throws(() => mention(NaN), RangeError);
```

### C7 à C10

```js
import assert from "node:assert/strict";

// C7
function voyelleOuConsonne(lettre) {
    if (!/^[a-z]$/i.test(lettre)) return "Ce n'est pas une lettre";
    return "aeiou".includes(lettre.toLowerCase()) ? "Voyelle" : "Consonne";
}
assert.deepEqual([voyelleOuConsonne("e"), voyelleOuConsonne("T"), voyelleOuConsonne("5")], ["Voyelle", "Consonne", "Ce n'est pas une lettre"]);

// C8 : (démonstration seulement ! En vrai : empreinte du mot de passe, jamais le texte en clair)
const IDENTIFIANT = "admin";
const MOT_DE_PASSE = "secret123";
const seConnecter = (id, mdp) => id === IDENTIFIANT && mdp === MOT_DE_PASSE;
assert.equal(seConnecter("admin", "secret123"), true);
assert.equal(seConnecter("admin", "faux"), false);

// C9 : calculatrice avec switch
function calculer(a, operateur, b) {
    switch (operateur) {
        case "+": return a + b;
        case "-": return a - b;
        case "*": return a * b;
        case "/":
            if (b === 0) throw new RangeError("Division par zéro");
            return a / b;
        default:
            throw new SyntaxError(`Opérateur inconnu : ${operateur}`);
    }
}
assert.equal(calculer(6, "*", 7), 42);
assert.equal(calculer(9, "/", 3), 3);
assert.throws(() => calculer(1, "/", 0), RangeError);
assert.throws(() => calculer(1, "%", 2), SyntaxError);

// C10
function feu(couleur) {
    switch (couleur.toLowerCase()) {
        case "rouge": return "Stop";
        case "orange": return "Ralentir";
        case "vert": return "Avancer";
        default: return "Couleur inconnue";
    }
}
assert.deepEqual([feu("Rouge"), feu("orange"), feu("vert"), feu("bleu")], ["Stop", "Ralentir", "Avancer", "Couleur inconnue"]);
```

## 4.3 Niveau avancé

### C11 à C15

```js
import assert from "node:assert/strict";

// C11 : validité (inégalité triangulaire) PUIS type
function typeTriangle(a, b, c) {
    const valide = a > 0 && b > 0 && c > 0 && a + b > c && a + c > b && b + c > a;
    if (!valide) return "Invalide";
    if (a === b && b === c) return "Équilatéral";
    if (a === b || b === c || a === c) return "Isocèle";
    return "Scalène";
}
assert.deepEqual(
    [typeTriangle(3, 3, 3), typeTriangle(3, 3, 5), typeTriangle(3, 4, 5), typeTriangle(1, 2, 10), typeTriangle(0, 1, 1)],
    ["Équilatéral", "Isocèle", "Scalène", "Invalide", "Invalide"],
);

// C12
const dansIntervalle = (n) => n >= 50 && n <= 100 && n % 5 !== 0 && n % 7 !== 0;
assert.deepEqual([dansIntervalle(51), dansIntervalle(55), dansIntervalle(56), dansIntervalle(101)], [true, false, false, false]);

// C13 : table des permissions
const PERMISSIONS = { admin: ["lire", "écrire", "supprimer"], editor: ["lire", "écrire"], viewer: ["lire"] };
function autorise(role, action) {
    if (!Object.hasOwn(PERMISSIONS, role)) return false; // rôle invalide : accès refusé
    return PERMISSIONS[role].includes(action);
}
assert.equal(autorise("admin", "supprimer"), true);
assert.equal(autorise("editor", "supprimer"), false);
assert.equal(autorise("viewer", "lire"), true);
assert.equal(autorise("pirate", "lire"), false);
assert.equal(autorise("constructor", "lire"), false);

// C14 : uniquement if / else
function salutation(heure) {
    if (heure < 0 || heure > 23) return "Heure invalide";
    if (heure <= 5) return "Bonne nuit";
    else if (heure <= 11) return "Bonjour";
    else if (heure <= 17) return "Bon après-midi";
    else if (heure <= 21) return "Bonsoir";
    else return "Bonne nuit";
}
assert.deepEqual([salutation(3), salutation(9), salutation(15), salutation(20), salutation(23)], ["Bonne nuit", "Bonjour", "Bon après-midi", "Bonsoir", "Bonne nuit"]);

// C15 : catégorie d'IMC
function categorieIMC(imc) {
    if (imc < 18.5) return "Insuffisance pondérale";
    if (imc < 25) return "Normal";
    if (imc < 30) return "Surpoids";
    return "Obésité";
}
assert.deepEqual([categorieIMC(17), categorieIMC(22.9), categorieIMC(27), categorieIMC(31)], ["Insuffisance pondérale", "Normal", "Surpoids", "Obésité"]);
```

### C16 : FizzBuzz avec variantes

```js
import assert from "node:assert/strict";

function fizzbuzz(n) {
    let texte = (n % 3 === 0 ? "Fizz" : "") + (n % 5 === 0 ? "Buzz" : "");
    if (texte === "") texte = String(n);
    if (String(n).includes("3")) texte += " (chanceux)";
    if (n % 7 === 0) texte += " (suspect)";
    return texte;
}

assert.equal(fizzbuzz(3), "Fizz (chanceux)");
assert.equal(fizzbuzz(15), "FizzBuzz");
assert.equal(fizzbuzz(21), "Fizz (suspect)");
assert.equal(fizzbuzz(1), "1");
assert.equal(fizzbuzz(7), "7 (suspect)");
assert.equal(fizzbuzz(63), "Fizz (chanceux) (suspect)");
console.log(Array.from({ length: 15 }, (_, i) => fizzbuzz(i + 1)).join(" | "));
```

### C17 : validateur de date

```js
import assert from "node:assert/strict";

const estBissextile = (a) => (a % 4 === 0 && a % 100 !== 0) || a % 400 === 0;

// Calcul direct : évite les pièges de l'objet Date (mois de 0 à 11, débordement automatique)
function dateValide(jour, mois, annee) {
    if (![jour, mois, annee].every(Number.isInteger) || mois < 1 || mois > 12 || jour < 1) return false;
    const joursParMois = [31, estBissextile(annee) ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    return jour <= joursParMois[mois - 1];
}

assert.equal(dateValide(29, 2, 2024), true);
assert.equal(dateValide(29, 2, 2023), false);
assert.equal(dateValide(29, 2, 1900), false);
assert.equal(dateValide(31, 4, 2025), false);
assert.equal(dateValide(31, 12, 2025), true);
assert.equal(dateValide(1, 13, 2025), false);
assert.equal(dateValide(0, 1, 2025), false);

// Le piège de Date : pas d'erreur, mais un débordement vers le mois suivant
assert.equal(new Date(2025, 1, 31).getMonth(), 2); // « 31 février » devient le 3 mars
```

### C18 et C19 : mot de passe et tri de trois nombres

```js
import assert from "node:assert/strict";

// C18
function forceMotDePasse(mdp) {
    const lettres = /[a-z]/i.test(mdp);
    const chiffres = /\d/.test(mdp);
    const symboles = /[!@#$%]/.test(mdp);
    if (mdp.length >= 8 && lettres && chiffres && symboles) return "Fort";
    if (mdp.length >= 6 && lettres && chiffres) return "Moyen";
    return "Faible";
}
assert.deepEqual(
    [forceMotDePasse("abc"), forceMotDePasse("abc123"), forceMotDePasse("abc12345"), forceMotDePasse("abc123!@")],
    ["Faible", "Moyen", "Moyen", "Fort"],
);

// C19 : trois comparaisons suffisent (tri par échanges), sans tableau ni sort()
function trierTrois(a, b, c) {
    if (a > b) [a, b] = [b, a];
    if (b > c) [b, c] = [c, b];
    if (a > b) [a, b] = [b, a];
    return `${a} ${b} ${c}`;
}
assert.equal(trierTrois(3, 1, 2), "1 2 3");
assert.equal(trierTrois(9, 8, 7), "7 8 9");
assert.equal(trierTrois(5, 5, 1), "1 5 5");
```

### C20 : médiane de trois nombres

```js
import assert from "node:assert/strict";

// Le médian est celui pour lequel (x − autre1) et (autre2 − x) ont le même signe
function mediane3(a, b, c) {
    if ((a - b) * (c - a) >= 0) return a;
    if ((b - a) * (c - b) >= 0) return b;
    return c;
}

assert.equal(mediane3(3, 8, 5), 5);
// Vérification exhaustive contre un tri
for (const [a, b, c] of [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1], [4, 4, 9]]) {
    assert.equal(mediane3(a, b, c), [a, b, c].sort((x, y) => x - y)[1]);
}
```

## 4.4 Scénarios réalistes

### C21 à C23

```js
import assert from "node:assert/strict";

// C21 : frais de 2 % seulement au-dessus de 1000
const TAUX = 0.92;
const convertirAvecFrais = (usd) => {
    const montant = usd * TAUX;
    return usd > 1000 ? montant * 0.98 : montant;
};
assert.equal(convertirAvecFrais(100), 92);
assert.equal(Math.round(convertirAvecFrais(2000) * 100) / 100, 1803.2);

// C22 : parenthèses explicites pour la priorité du OU et du ET
const eligibleBourse = (moyenne, extrascolaire, revenu) =>
    (moyenne > 3.5 || (moyenne > 3.0 && extrascolaire)) && revenu < 50000;
assert.equal(eligibleBourse(3.8, false, 40000), true);
assert.equal(eligibleBourse(3.2, true, 40000), true);
assert.equal(eligibleBourse(3.2, false, 40000), false);
assert.equal(eligibleBourse(3.8, true, 60000), false);

// C23 : remises imbriquées
function remise(estMembre, depenses) {
    if (!estMembre) return 0;
    if (depenses > 500) return 20;
    if (depenses > 100) return 10;
    return 5;
}
assert.deepEqual([remise(true, 600), remise(true, 200), remise(true, 50), remise(false, 600)], [20, 10, 5, 0]);
```

### C24 : signe du zodiaque

```js
import assert from "node:assert/strict";

// [mois, jour de début, signe], dans l'ordre de l'année. Avant le 20 janvier : Capricorne.
const DEBUTS = [
    [1, 20, "Verseau"], [2, 19, "Poissons"], [3, 21, "Bélier"], [4, 20, "Taureau"],
    [5, 21, "Gémeaux"], [6, 21, "Cancer"], [7, 23, "Lion"], [8, 23, "Vierge"],
    [9, 23, "Balance"], [10, 23, "Scorpion"], [11, 22, "Sagittaire"], [12, 22, "Capricorne"],
];

function signeZodiaque(jour, mois) {
    const date = mois * 100 + jour; // 25 mars → 325 : comparaison simple
    let signe = "Capricorne"; // du 1er au 19 janvier
    for (const [m, j, nom] of DEBUTS) {
        if (date >= m * 100 + j) signe = nom;
    }
    return signe;
}

assert.equal(signeZodiaque(19, 1), "Capricorne");
assert.equal(signeZodiaque(20, 1), "Verseau");
assert.equal(signeZodiaque(18, 2), "Verseau");
assert.equal(signeZodiaque(25, 3), "Bélier");
assert.equal(signeZodiaque(21, 11), "Scorpion");
assert.equal(signeZodiaque(21, 12), "Sagittaire");
assert.equal(signeZodiaque(31, 12), "Capricorne");
```

### C25 à C28

```js
import assert from "node:assert/strict";

// C25
function permis(age, vue) {
    if (age < 18) return "Trop jeune";
    return vue >= 6 ? "Admissible" : "Améliorez votre vue";
}
assert.deepEqual([permis(17, 10), permis(20, 5), permis(20, 6)], ["Trop jeune", "Améliorez votre vue", "Admissible"]);

// C26 : retrait avec frais de 10
const FRAIS = 10;
function retirer(montant, solde) {
    if (montant % 100 !== 0) return { ok: false, message: "Le montant doit être un multiple de 100" };
    if (montant + FRAIS > solde) return { ok: false, message: "Solde insuffisant" };
    return { ok: true, solde: solde - montant - FRAIS };
}
assert.deepEqual(retirer(200, 500), { ok: true, solde: 290 });
assert.equal(retirer(150, 500).ok, false);
assert.equal(retirer(500, 500).message, "Solde insuffisant"); // 500 + 10 de frais > 500

// C27 : 24 h vers 12 h
function en12h(heure24) {
    const [h, m] = heure24.split(":").map(Number);
    const suffixe = h >= 12 ? "PM" : "AM";
    const h12 = h % 12 === 0 ? 12 : h % 12; // 0 h et 12 h donnent 12
    return `${h12}:${String(m).padStart(2, "0")} ${suffixe}`;
}
assert.deepEqual([en12h("13:15"), en12h("00:05"), en12h("12:00"), en12h("09:30"), en12h("23:59")], ["1:15 PM", "12:05 AM", "12:00 PM", "9:30 AM", "11:59 PM"]);

// C28 : liste de TOUTES les règles non respectées
function reglesNonRespectees(mdp) {
    const erreurs = [];
    if (mdp.length < 8) erreurs.push("au moins 8 caractères");
    if (!/[A-Z]/.test(mdp)) erreurs.push("une majuscule");
    if (!/\d/.test(mdp)) erreurs.push("un chiffre");
    if (!/[^A-Za-z0-9]/.test(mdp)) erreurs.push("un caractère spécial");
    return erreurs;
}
assert.deepEqual(reglesNonRespectees("Abcdef1!"), []);
assert.deepEqual(reglesNonRespectees("abc"), ["au moins 8 caractères", "une majuscule", "un chiffre", "un caractère spécial"]);
```

## 4.5 Compléments

### C29 : valeurs « vraies » et « fausses »

```js
import assert from "node:assert/strict";

const attendu = [
    [0, false], ["", false], [" ", true], ["0", true], [[], true],
    [{}, true], [null, false], [undefined, false], [NaN, false], [-1, true],
];
for (const [valeur, estVrai] of attendu) {
    assert.equal(Boolean(valeur), estVrai);
}

// Les seules valeurs « fausses » : false, 0, -0, 0n, "", null, undefined, NaN
const fausses = [false, 0, -0, 0n, "", null, undefined, NaN];
assert.ok(fausses.every((v) => !v));
// ⚠️ Un tableau vide et un objet vide sont VRAIS (contrairement à d'autres langages)
```

### C30 : clauses de garde

```js
import assert from "node:assert/strict";

// ❌ Avant : trois niveaux d'imbrication
function remiseImbriquee(utilisateur, panier) {
    if (utilisateur) {
        if (utilisateur.actif) {
            if (panier.length > 0) {
                return panier.length * 2;
            } else {
                return 0;
            }
        } else {
            return 0;
        }
    } else {
        return 0;
    }
}

// ✅ Après : on traite d'abord les cas d'erreur et on sort tôt
function remiseAvecGardes(utilisateur, panier) {
    if (!utilisateur) return 0;
    if (!utilisateur.actif) return 0;
    if (panier.length === 0) return 0;
    return panier.length * 2;
}

for (const [u, p] of [[null, [1]], [{ actif: false }, [1]], [{ actif: true }, []], [{ actif: true }, [1, 2, 3]]]) {
    assert.equal(remiseAvecGardes(u, p), remiseImbriquee(u, p)); // même comportement, code plus plat
}
```

---

# Partie 4 : boucles et itérations

## 5.1 Niveau de base

### B1 à B10

```js
import assert from "node:assert/strict";

const afficher = (liste) => console.log(liste.join(" "));

// B1 : de 1 à 10
{ const r = []; for (let i = 1; i <= 10; i++) r.push(i); afficher(r); assert.equal(r.length, 10); }

// B2 : pairs de 1 à 20
{ const r = []; for (let i = 2; i <= 20; i += 2) r.push(i); afficher(r); assert.equal(r.at(-1), 20); }

// B3 : somme de 1 à N
const sommeJusqua = (n) => { let s = 0; for (let i = 1; i <= n; i++) s += i; return s; };
assert.equal(sommeJusqua(100), 5050);

// B4 : table de multiplication
const table = (n) => { const l = []; for (let i = 1; i <= 10; i++) l.push(`${n} × ${i} = ${n * i}`); return l; };
assert.equal(table(7)[8], "7 × 9 = 63");

// B5 : 10 à 1
{ const r = []; for (let i = 10; i >= 1; i--) r.push(i); afficher(r); assert.equal(r[0], 10); }

// B6 : impairs de 1 à 50
{ const r = []; for (let i = 1; i <= 50; i += 2) r.push(i); assert.equal(r.length, 25); assert.equal(r.at(-1), 49); }

// B7 : carrés de 1 à 10
{ const r = []; for (let i = 1; i <= 10; i++) r.push(i * i); afficher(r); assert.equal(r.at(-1), 100); }

// B8 : de 100 à 0 par pas de 5
{ const r = []; for (let i = 100; i >= 0; i -= 5) r.push(i); assert.equal(r.length, 21); assert.equal(r.at(-1), 0); }

// B9 : somme des pairs jusqu'à N
const sommePairs = (n) => { let s = 0; for (let i = 2; i <= n; i += 2) s += i; return s; };
assert.equal(sommePairs(20), 110);

// B10 : alphabet (A = code 65)
{ let a = ""; for (let code = 65; code <= 90; code++) a += String.fromCharCode(code); assert.equal(a, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"); }
```

## 5.2 Niveau intermédiaire

### B11 à B20

```js
import assert from "node:assert/strict";

// B11 : factorielle
function factorielle(n) {
    let r = 1;
    for (let i = 2; i <= n; i++) r *= i;
    return r;
}
assert.equal(factorielle(5), 120);
assert.equal(factorielle(0), 1);

// B12 : n premiers termes de Fibonacci
function fibonacci(n) {
    const suite = [];
    let [a, b] = [0, 1];
    for (let i = 0; i < n; i++) {
        suite.push(a);
        [a, b] = [b, a + b];
    }
    return suite;
}
assert.deepEqual(fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]);

// B13 : nombre de chiffres
function nombreDeChiffres(n) {
    n = Math.abs(n);
    let compte = 1; // 0 a un chiffre
    while (n >= 10) {
        n = Math.floor(n / 10);
        compte++;
    }
    return compte;
}
assert.deepEqual([nombreDeChiffres(0), nombreDeChiffres(7), nombreDeChiffres(12345), nombreDeChiffres(-100)], [1, 1, 5, 3]);

// B14 : somme des chiffres
function sommeDesChiffres(n) {
    n = Math.abs(n);
    let somme = 0;
    while (n > 0) {
        somme += n % 10; // dernier chiffre
        n = Math.floor(n / 10); // on le retire
    }
    return somme;
}
assert.equal(sommeDesChiffres(1234), 10);

// B15 : nombre premier : il suffit de tester les diviseurs jusqu'à √n
function estPremier(n) {
    if (!Number.isInteger(n) || n < 2) return false;
    for (let d = 2; d * d <= n; d++) {
        if (n % d === 0) return false;
    }
    return true;
}
assert.deepEqual([2, 3, 4, 17, 18, 97, 1, 0, -5].map(estPremier), [true, true, false, true, false, true, false, false, false]);

// B16 : puissance sans Math.pow
function puissance(base, exposant) {
    let r = 1;
    for (let i = 0; i < exposant; i++) r *= base;
    return r;
}
assert.equal(puissance(2, 4), 16);
assert.equal(puissance(5, 0), 1);

// B17 : nombre parfait (28 = 1 + 2 + 4 + 7 + 14)
function estParfait(n) {
    if (n < 2) return false;
    let somme = 0;
    for (let d = 1; d <= n / 2; d++) {
        if (n % d === 0) somme += d;
    }
    return somme === n;
}
assert.deepEqual([6, 28, 496, 12, 1].map(estParfait), [true, true, true, false, false]);

// B18 : inverser avec une boucle
function inverserBoucle(texte) {
    let r = "";
    for (let i = texte.length - 1; i >= 0; i--) r += texte[i];
    return r;
}
assert.equal(inverserBoucle("hello"), "olleh");

// B19 : tous les chiffres sont pairs
function tousPairs(n) {
    n = Math.abs(n);
    do {
        if ((n % 10) % 2 !== 0) return false;
        n = Math.floor(n / 10);
    } while (n > 0);
    return true;
}
assert.deepEqual([248, 243, 0, 2].map(tousPairs), [true, false, true, true]);

// B20 : somme des factorielles 1! + 2! + … + n!
function sommeFactorielles(n) {
    let somme = 0, f = 1;
    for (let i = 1; i <= n; i++) {
        f *= i; // on réutilise la factorielle précédente
        somme += f;
    }
    return somme;
}
assert.equal(sommeFactorielles(4), 33);
```

## 5.3 Niveau difficile

### B21 à B29

```js
import assert from "node:assert/strict";

// B21 : Armstrong (153 = 1³ + 5³ + 3³)
function estArmstrong(n) {
    const chiffres = [...String(n)].map(Number);
    const k = chiffres.length;
    return chiffres.reduce((s, c) => s + c ** k, 0) === n;
}
assert.deepEqual([153, 370, 9474, 154, 10].map(estArmstrong), [true, true, true, false, false]);

// B22 : triangle d'étoiles
function triangle(n) {
    const lignes = [];
    for (let i = 1; i <= n; i++) {
        let ligne = "";
        for (let j = 0; j < i; j++) ligne += "*"; // boucles imbriquées
        lignes.push(ligne);
    }
    return lignes;
}
assert.deepEqual(triangle(5), ["*", "**", "***", "****", "*****"]);

// B23 : palindrome numérique PAR CALCUL (sans passer par une chaîne)
function estPalindromeNumerique(n) {
    if (n < 0) return false;
    let original = n, inverse = 0;
    while (n > 0) {
        inverse = inverse * 10 + (n % 10);
        n = Math.floor(n / 10);
    }
    return inverse === original;
}
assert.deepEqual([121, 1331, 123, 7, 0, -121].map(estPalindromeNumerique), [true, true, false, true, true, false]);

// B24 : PGCD (algorithme d'Euclide)
function pgcd(a, b) {
    while (b !== 0) [a, b] = [b, a % b];
    return Math.abs(a);
}
assert.equal(pgcd(48, 18), 6);
assert.equal(pgcd(17, 5), 1);

// B25 : PPCM = a × b / PGCD
const ppcm = (a, b) => (a === 0 || b === 0 ? 0 : Math.abs(a * b) / pgcd(a, b));
assert.equal(ppcm(4, 6), 12);

// B26 : pyramide
function pyramide(n) {
    const lignes = [];
    for (let i = 1; i <= n; i++) lignes.push(" ".repeat(n - i) + "*".repeat(2 * i - 1));
    return lignes;
}
assert.deepEqual(pyramide(3), ["  *", " ***", "*****"]);
console.log(pyramide(5).join("\n"));

// B27 : binaire vers décimal
function binaireEnDecimal(texte) {
    let r = 0;
    for (const bit of texte) {
        if (bit !== "0" && bit !== "1") throw new SyntaxError("Chaîne non binaire");
        r = r * 2 + Number(bit); // on décale d'un cran puis on ajoute le bit
    }
    return r;
}
assert.equal(binaireEnDecimal("1101"), 13);
assert.equal(binaireEnDecimal("0"), 0);
assert.equal(parseInt("1101", 2), 13); // la fonction intégrée

// B28 : suite de Collatz
function collatz(n) {
    const suite = [n];
    while (n !== 1) {
        n = n % 2 === 0 ? n / 2 : 3 * n + 1;
        suite.push(n);
    }
    return suite;
}
assert.deepEqual(collatz(6), [6, 3, 10, 5, 16, 8, 4, 2, 1]);

// B29 : nombres premiers de 1 à 100 (réutilise estPremier de B15)
function estPremier(n) {
    if (n < 2) return false;
    for (let d = 2; d * d <= n; d++) if (n % d === 0) return false;
    return true;
}
const premiers = [];
for (let n = 1; n <= 100; n++) if (estPremier(n)) premiers.push(n);
assert.equal(premiers.length, 25);
assert.equal(premiers.at(-1), 97);
```

### B30 : jeu de devinette

```js
// @stdin: 50\nabc\n25\n37
import { demander, fermer } from "./entree.js";

async function devinette(secret = Math.floor(Math.random() * 100) + 1) {
    let essais = 0;
    while (true) {
        const saisie = await demander("Votre proposition (1-100) ?");
        if (saisie === null) return null; // abandon
        const proposition = Number(saisie);
        if (saisie.trim() === "" || !Number.isInteger(proposition) || proposition < 1 || proposition > 100) {
            console.log("Entrez un entier entre 1 et 100.");
            continue; // saisie invalide : l'essai n'est pas compté
        }
        essais++;
        if (proposition === secret) {
            console.log(`Bravo ! Trouvé en ${essais} essai(s).`);
            return essais;
        }
        console.log(proposition > secret ? "Trop grand !" : "Trop petit !");
    }
}

const essais = await devinette(37); // secret imposé pour pouvoir tester ; sans argument, il est aléatoire
fermer();
if (essais !== 3) throw new Error(`attendu 3 essais, obtenu ${essais}`);
```

## 5.4 Compléments

### B31 à B34

```js
import assert from "node:assert/strict";

// B31 : les trois boucles
const a = [], b = [], c = [];
for (let i = 1; i <= 5; i++) a.push(i);
let j = 1; while (j <= 5) { b.push(j); j++; }
let k = 1; do { c.push(k); k++; } while (k <= 5);
assert.deepEqual([a, b, c], [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]);
// do...while s'exécute AU MOINS une fois : idéale pour « redemander tant que la saisie est invalide »
let tours = 0; do { tours++; } while (false);
assert.equal(tours, 1);

// B32 : for...of, for...in, Object.entries
const fruits = ["pomme", "poire"];
const indices = [];
for (const [i, fruit] of fruits.entries()) indices.push(`${i}:${fruit}`);
assert.deepEqual(indices, ["0:pomme", "1:poire"]);

const personne = { nom: "Alice", age: 30 };
const cles = []; for (const cle in personne) cles.push(cle);
assert.deepEqual(cles, ["nom", "age"]);
assert.deepEqual(Object.entries(personne), [["nom", "Alice"], ["age", 30]]);
// ⚠️ for...in sur un tableau parcourt les CLÉS (des chaînes "0", "1"…) et aussi les propriétés ajoutées
const tab = [10, 20]; tab.extra = "x";
const clesTab = []; for (const cle in tab) clesTab.push(cle);
assert.deepEqual(clesTab, ["0", "1", "extra"]);

// B33 : break, continue et étiquettes
const impairs = []; for (let i = 1; i <= 20; i++) { if (i % 2 === 0) continue; impairs.push(i); }
assert.equal(impairs.length, 10);

let premierMultiple;
for (let i = 51; ; i++) { if (i % 7 === 0) { premierMultiple = i; break; } }
assert.equal(premierMultiple, 56);

let trouve = null;
exterieure: for (let x = 1; x <= 9; x++) {
    for (let y = 1; y <= 9; y++) {
        if (x * y === 42) { trouve = [x, y]; break exterieure; } // sort des DEUX boucles
    }
}
assert.deepEqual(trouve, [6, 7]);

// B34 : sans boucle for
const nombres = [1, 2, 3, 4, 5, 6];
assert.deepEqual(nombres.map((n) => n * n), [1, 4, 9, 16, 25, 36]);
assert.deepEqual(nombres.filter((n) => n % 2 === 0), [2, 4, 6]);
assert.equal(nombres.reduce((s, n) => s + n, 0), 21);
// Enchaînés : somme des carrés des nombres pairs
assert.equal(nombres.filter((n) => n % 2 === 0).map((n) => n * n).reduce((s, n) => s + n, 0), 56);
```

---

## 🧾 Récapitulatif

| Partie | Notions démontrées |
| --- | --- |
| Défis | `reduce`, `Set`, expressions régulières, `Object.groupBy`, `Object.hasOwn`, `Math.round` / `ceil` |
| Variables et types | `const` / `let`, `??` contre `\|\|`, conversions et pièges, `BigInt`, précision décimale, déstructuration, `structuredClone`, mémoïsation |
| Conditions | `switch`, tables de correspondance, clauses de garde, parenthèses explicites, pièges de `Date` |
| Boucles | `for` / `while` / `do...while`, `for...of` / `for...in`, `break` / `continue` / étiquettes, `map` / `filter` / `reduce` |
