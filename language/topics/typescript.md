<div align="center">

# 🔷 TypeScript — Guide complet

**Du premier type aux génériques, aux frameworks et à la configuration moderne**

*Mis à jour pour TypeScript 6.0 / 7.0 (octobre 2026)*

</div>

---

## 🧰 Outils

| Ressource | Lien |
| --- | --- |
| 📝 Exercices | [exercises](/language/exercises/typescript) |
| ✅ Solutions | [solutions](/language/solutions/typescript) |
| 📘 Documentation officielle | [typescriptlang.org](https://www.typescriptlang.org/docs/) |
| 🧪 Bac à sable en ligne | [TypeScript Playground](https://www.typescriptlang.org/play) |

---

## 🗂️ Sommaire

**🟢 Niveau débutant**

1. [Introduction à TypeScript](#1-introduction-à-typescript)
2. [Types de base](#2-types-de-base)
3. [Fonctions et annotations de types](#3-fonctions-et-annotations-de-types)
4. [Tableaux et tuples](#4-tableaux-et-tuples)
5. [Énumérations (`enum`) et alternatives](#5-énumérations-enum-et-alternatives)
6. [Interfaces](#6-interfaces)
7. [Alias de types, unions et types littéraux](#7-alias-de-types-unions-et-types-littéraux)

**🟡 Niveau intermédiaire**

8. [Classes et programmation orientée objet](#8-classes-et-programmation-orientée-objet)
9. [Génériques](#9-génériques)
10. [Modules et espaces de noms](#10-modules-et-espaces-de-noms)
11. [Types avancés](#11-types-avancés)
12. [Fichiers de déclaration de types](#12-fichiers-de-déclaration-de-types)

**🔴 Niveau avancé**

13. [Types utilitaires](#13-types-utilitaires)
14. [Décorateurs](#14-décorateurs)
15. [Programmation asynchrone](#15-programmation-asynchrone)
16. [Manipuler le DOM](#16-manipuler-le-dom)
17. [Mixins et composition](#17-mixins-et-composition)
18. [TypeScript et frameworks front-end](#18-typescript-et-frameworks-front-end)
19. [TypeScript côté serveur](#19-typescript-côté-serveur)
20. [Configuration du projet (`tsconfig.json`)](#20-configuration-du-projet-tsconfigjson)
21. [Linting et formatage](#21-linting-et-formatage)

**⭐ Bonus**

22. [TypeScript et bases de données](#22-typescript-et-bases-de-données)
23. [TypeScript et tests](#23-typescript-et-tests)
24. [Nouveautés par version et bonnes pratiques](#24-nouveautés-par-version-et-bonnes-pratiques)

> 💡 **Légende** : *(ajout)* = notion absente du guide d'origine ; *(à jour)* = pratique moderne remplaçant une ancienne ; *(TS x.y)* = version qui introduit la fonctionnalité.

---

# 🟢 Niveau débutant

---

# 1. Introduction à TypeScript

## 1.1 Qu'est-ce que TypeScript ?

**TypeScript** (TS) est un **sur-ensemble typé de JavaScript**, créé par Microsoft (Anders Hejlsberg, 2012). Tout code JavaScript valide est du TypeScript valide ; TypeScript y ajoute un **système de types statiques** vérifié **avant l'exécution**.

```text
 code .ts ──▶ vérification des types ──▶ (suppression des types) ──▶ code .js ──▶ exécution
                (erreurs à la compilation)                              (navigateur, Node.js…)
```

> ℹ️ Les types **n'existent plus à l'exécution** : ils sont **effacés**. TypeScript ne remplace donc pas la validation des données externes (API, formulaires), voir [section 19](#19-typescript-côté-serveur).

## 1.2 Pourquoi l'utiliser ?

| Avantage | Détail |
| --- | --- |
| 🐞 **Erreurs détectées tôt** | `undefined is not a function`, fautes de frappe, mauvais arguments… repérés avant l'exécution |
| 💡 **Éditeur très puissant** | Autocomplétion, navigation, renommage sûr, documentation en ligne |
| 📖 **Code auto-documenté** | Les types décrivent le contrat des fonctions et des données |
| 🔧 **Refactorisation sûre** | Le compilateur liste tout ce qui casse |
| 🏗️ **Grands projets** | Équipes nombreuses, bibliothèques, API stables |
| 🔄 **Adoption progressive** | On peut migrer un projet JS fichier par fichier |

## 1.3 L'état de TypeScript en 2026 *(à jour)*

| Version | Date | Points marquants |
| --- | --- | --- |
| **5.x** | 2023–2025 | Décorateurs standard, `satisfies`, `using`, `NoInfer`, prédicats de type inférés, `--erasableSyntaxOnly` |
| **6.0** | mars 2026 | **Dernière version basée sur le code JavaScript** : « version passerelle ». **Nouveaux défauts** (`strict: true`, `module: esnext`, `types: []`…) et nombreuses **dépréciations** |
| **7.0** | juillet 2026 | **Compilateur natif écrit en Go** (projet *Corsa*) : vérification et compilation **beaucoup plus rapides**, parallélisme, moins de mémoire. Ne prend en charge **aucune** des options dépréciées en 6.0 |

Conséquences pratiques :

- Le **langage** lui-même change peu : les types que vous écrivez restent les mêmes.
- La **configuration** (`tsconfig.json`) change : voir [section 20](#20-configuration-du-projet-tsconfigjson).
- Pour exécuter du TypeScript sans compiler, les runtimes modernes **effacent les types** eux-mêmes (voir 1.5).

## 1.4 Installer TypeScript

Prérequis : **Node.js** (version LTS récente) et un gestionnaire de paquets (npm, pnpm, yarn, bun).

```bash
node --version
npm install -D typescript          # installation PAR PROJET (recommandée)
npx tsc --version
```

> ✅ Préférez une installation **locale au projet** (`-D`) à une installation globale : tous les développeurs et la CI utilisent ainsi la même version.

### Compilateur natif (TypeScript 7)

Le nouveau compilateur est distribué dans le paquet `typescript` lui-même (la version 7 a remplacé l'aperçu `@typescript/native-preview` / `tsgo`). La commande reste **`tsc`**.

```bash
npm install -D typescript@latest
npx tsc -p .
```

## 1.5 Écrire et exécuter un premier fichier

```typescript
// bonjour.ts
function saluer(nom: string): string {
    return `Bonjour, ${nom} !`;
}

console.log(saluer("Alice"));
// saluer(42);   // ❌ Erreur : l'argument de type 'number' n'est pas assignable au paramètre de type 'string'
```

| Méthode | Commande | Usage |
| --- | --- | --- |
| **Compiler un fichier** | `npx tsc bonjour.ts` → `bonjour.js` *(⚠️ voir la note ci-dessous)* | Essais rapides |
| **Compiler le projet** | `npx tsc` (ou `npx tsc -p .`) selon `tsconfig.json` | Production, bibliothèques |
| **Vérifier seulement** | `npx tsc --noEmit` | CI, éditeur (les types sont validés, rien n'est généré) |
| **Mode surveillance** | `npx tsc --watch` | Développement |
| **Exécuter directement** | `node bonjour.ts` *(Node.js 22.18+ / 24 : effacement des types intégré)* | Scripts, serveurs simples |
| **Exécuter avec `tsx`** | `npx tsx bonjour.ts` | Scripts, outils, développement (Node.js) |
| **Deno / Bun** | `deno run bonjour.ts` · `bun bonjour.ts` | Exécutent TS nativement |

> ⚠️ **Depuis TypeScript 6/7**, si un `tsconfig.json` existe, `tsc bonjour.ts` **échoue** avec l'erreur *TS5112* (le fichier de configuration serait ignoré en silence). Utilisez `tsc` ou `tsc -p .` pour compiler le projet, ou `tsc --ignoreConfig bonjour.ts` pour compiler un fichier isolé avec les options par défaut.

> ⚠️ L'exécution directe (**Node.js**, `tsx`, Bun…) **supprime les types sans les vérifier** : lancez `tsc --noEmit` pour vérifier. Le **mode « effaçable »** (`--erasableSyntaxOnly`, TS 5.8) interdit les syntaxes TypeScript qui produisent du code (`enum`, `namespace`, propriétés de paramètres de constructeur) afin de rester compatible avec cet effacement simple.

## 1.6 Démarrer un projet

```bash
mkdir mon-projet && cd mon-projet
npm init -y
npm install -D typescript @types/node
npx tsc --init                       # génère un tsconfig.json commenté
```

```text
mon-projet/
├── src/
│   └── index.ts
├── dist/               ← sortie compilée (ignorée par Git)
├── package.json
└── tsconfig.json
```

Voir la [section 20](#20-configuration-du-projet-tsconfigjson) pour une configuration complète.

## 1.7 Les outils du quotidien

| Outil | Rôle |
| --- | --- |
| **VS Code** | Support TypeScript natif (le meilleur éditeur pour TS) |
| **TypeScript Playground** | Essayer du code en ligne |
| **tsx**, **Node.js**, **Bun**, **Deno** | Exécuter du TS |
| **Vite**, **esbuild**, **SWC** | Compiler / empaqueter (suppriment les types, ne les vérifient pas) |
| **typescript-eslint**, **Prettier**, **Biome** | Qualité et formatage |
| **Vitest**, **Jest** | Tests |

## 1.8 Résumé

- TypeScript = JavaScript + **types statiques** ; il **disparaît** à l'exécution.
- `tsc --noEmit` **vérifie** ; les autres outils **exécutent ou empaquettent**.
- Version actuelle : **TS 7** (compilateur natif) ; **TS 6** a préparé le terrain.

---

# 2. Types de base

## 2.1 Les types primitifs

```typescript
let nom: string = "Alice";
let age: number = 30;                 // entiers, flottants, NaN, Infinity
let actif: boolean = true;
let grand: bigint = 9007199254740993n;
let id: symbol = Symbol("id");
let rien: null = null;
let indefini: undefined = undefined;
```

> ✅ Écrivez les types en **minuscules** (`string`, `number`) et **jamais** `String`, `Number`, `Boolean`, `Object` (objets enveloppes, source d'erreurs).

## 2.2 Inférence de types

TypeScript **déduit** le type à partir de la valeur : n'annotez que lorsque c'est utile.

```typescript
let ville = "Paris";        // string (inféré)
const pi = 3.14;            // 3.14 (type littéral, car const)
let nombres = [1, 2, 3];    // number[]
const personne = { nom: "Alice", age: 30 };   // { nom: string; age: number }

ville = 42;                 // ❌ 'number' n'est pas assignable à 'string'
```

| Quand annoter ? | Exemple |
| --- | --- |
| **Paramètres** de fonction (toujours) | `(a: number, b: number)` |
| Valeur initiale **absente** | `let total: number;` |
| **Retour** de fonctions publiques / exportées | `function f(): string` |
| Quand le type inféré est **trop large ou trop étroit** | `let x: string \| null = null;` |

## 2.3 Types spéciaux

### `any` : l'échappatoire (à éviter)

Désactive la vérification : une valeur `any` accepte tout et **contamine** le code environnant.

```typescript
let x: any = "texte";
x = 42;
x.nimporteQuoi();           // ✅ accepté par le compilateur, ❌ plantage à l'exécution
```

### `unknown` : la version sûre

On peut y mettre n'importe quoi, mais il faut le **vérifier** avant de l'utiliser.

```typescript
function traiter(valeur: unknown) {
    // valeur.toUpperCase();          // ❌ Erreur : valeur est de type 'unknown'
    if (typeof valeur === "string") {
        console.log(valeur.toUpperCase());    // ✅ restreint à string
    }
}
const donnees: unknown = JSON.parse('{"a": 1}');
```

### `void`, `never`, `object`

```typescript
function journaliser(message: string): void { console.log(message); }       // ne retourne rien

function echouer(message: string): never { throw new Error(message); }      // ne retourne JAMAIS

function infinie(): never { while (true) {} }

let obj: object = { a: 1 };            // tout non-primitif (rarement utile : préférez un type précis)
let quelconque: {} = 5;                // ⚠️ {} = tout sauf null et undefined
```

| Type | Signification |
| --- | --- |
| `any` | Aucune vérification ❌ |
| `unknown` | Valeur inconnue : à **restreindre** avant usage ✅ |
| `void` | Une fonction qui ne renvoie rien |
| `never` | Valeur **impossible** (erreur, boucle infinie, cas exhaustif) |

> ✅ Activez **`noImplicitAny`** (inclus dans `strict`) : TypeScript refuse alors les `any` implicites. Préférez toujours **`unknown`** à `any`.

## 2.4 `null` et `undefined` en mode strict

Avec `strictNullChecks` (inclus dans `strict`, **activé par défaut depuis TS 6.0**), `null` et `undefined` ne sont **pas** assignables aux autres types.

```typescript
let nom: string = null;                  // ❌ Erreur
let nomOuNull: string | null = null;     // ✅ le « peut être nul » est explicite

function longueur(s: string | null): number {
    return s?.length ?? 0;               // chaînage optionnel + fusion nulle
}

const element = document.querySelector("#titre");   // HTMLElement | null
element.textContent = "Salut";                       // ❌ 'element' est peut-être 'null'
if (element) element.textContent = "Salut";          // ✅
element!.textContent = "Salut";                      // ⚠️ assertion non nulle : à manier avec prudence
```

## 2.5 Assertions de type

Dire au compilateur « je sais mieux que toi » (aucun effet à l'exécution, **aucune conversion**) :

```typescript
const entree = document.getElementById("nom") as HTMLInputElement;
const valeur = (donnees as { id: number }).id;
const forcer = valeur as unknown as string;     // double assertion : dernier recours
```

> ⚠️ Une assertion **n'est pas** une vérification : si vous vous trompez, le programme plante à l'exécution. Préférez la **restriction de type** (`if`, `typeof`, `instanceof`, validation de schéma).

## 2.6 `as const` et `satisfies` *(ajout)*

```typescript
// as const : valeurs littérales + readonly en profondeur
const direction = { haut: "UP", bas: "DOWN" } as const;
// { readonly haut: "UP"; readonly bas: "DOWN" }
type Direction = (typeof direction)[keyof typeof direction];     // "UP" | "DOWN"

const niveaux = ["debug", "info", "erreur"] as const;
type Niveau = (typeof niveaux)[number];                           // "debug" | "info" | "erreur"

// satisfies (TS 4.9) : vérifie la conformité SANS élargir le type inféré
type Couleurs = Record<string, string | number[]>;
const palette = {
    rouge: [255, 0, 0],
    vert: "#00ff00",
} satisfies Couleurs;

palette.rouge.map(c => c * 2);       // ✅ reste connu comme number[]
palette.vert.toUpperCase();          // ✅ reste connu comme string
```

## 2.7 Types propres aux objets et fonctions (aperçu)

```typescript
let utilisateur: { nom: string; age?: number } = { nom: "Alice" };
let additionner: (a: number, b: number) => number = (a, b) => a + b;
let ids: number[] = [1, 2, 3];
let paire: [string, number] = ["Alice", 30];
```

Détails dans les sections suivantes.

---

# 3. Fonctions et annotations de types

## 3.1 Annoter paramètres et retour

```typescript
function additionner(a: number, b: number): number {
    return a + b;
}

const multiplier = (a: number, b: number): number => a * b;
const saluer = (nom: string): void => console.log(`Salut ${nom}`);
```

Le type de retour est **inféré** ; l'annoter explicitement sur les fonctions **publiques** documente le contrat et accélère le compilateur.

## 3.2 Paramètres optionnels, par défaut et *rest*

```typescript
function presenter(nom: string, age?: number): string {       // age : number | undefined
    return age !== undefined ? `${nom} (${age} ans)` : nom;
}

function saluer(nom: string, salutation: string = "Bonjour"): string {   // type inféré : string
    return `${salutation}, ${nom}`;
}

function somme(...nombres: number[]): number {
    return nombres.reduce((total, n) => total + n, 0);
}

const [a, b] = [1, 2] as const;
```

> Les paramètres **optionnels** viennent **après** les obligatoires.

## 3.3 Types de fonctions

```typescript
type Operation = (a: number, b: number) => number;     // alias de type fonction
const addition: Operation = (a, b) => a + b;            // les types de a et b sont inférés

interface Comparateur {                                  // interface appelable
    (a: string, b: string): number;
}

function appliquer(f: (x: number) => number, valeur: number): number { return f(valeur); }
appliquer(x => x * 2, 5);                                // callback : types inférés
```

## 3.4 Surcharges de fonctions

Plusieurs **signatures** pour une même implémentation :

```typescript
function formater(valeur: string): string;
function formater(valeur: number, decimales: number): string;
function formater(valeur: string | number, decimales?: number): string {      // implémentation (non visible de l'extérieur)
    return typeof valeur === "string" ? valeur.trim() : valeur.toFixed(decimales ?? 2);
}

formater("  x ");          // ✅
formater(3.14159, 2);      // ✅
// formater(3.14);         // ❌ aucune surcharge ne correspond
```

> 💡 Si possible, préférez un **type union** ou des **génériques** aux surcharges (plus simples).

## 3.5 Le paramètre `this`

```typescript
interface Bouton { etiquette: string; }

function afficher(this: Bouton) {
    console.log(this.etiquette);            // `this` est typé
}
```

## 3.6 Restriction de type (*narrowing*) et gardes de type

TypeScript **affine** le type selon les tests effectués :

```typescript
function afficher(valeur: string | number | null) {
    if (valeur === null) return;                       // null éliminé
    if (typeof valeur === "string") {
        valeur.toUpperCase();                          // string
    } else {
        valeur.toFixed(2);                             // number
    }
}

if (x instanceof Date) { /* Date */ }
if ("nom" in objet) { /* objet possède nom */ }
if (Array.isArray(valeur)) { /* tableau */ }
```

### Gardes de type personnalisées (*type predicates*)

```typescript
interface Chat { miauler(): void }
interface Chien { aboyer(): void }

function estChat(animal: Chat | Chien): animal is Chat {
    return "miauler" in animal;
}

const animaux: (Chat | Chien)[] = [];
const chats = animaux.filter(estChat);                         // Chat[]

// TS 5.5 : prédicats INFÉRÉS dans les cas simples
const nombres = [1, undefined, 3].filter(x => x !== undefined);   // number[] (plus besoin d'annoter)
```

### Fonctions d'assertion

```typescript
function assert(condition: unknown, message: string): asserts condition {
    if (!condition) throw new Error(message);
}
function assertEstString(v: unknown): asserts v is string {
    if (typeof v !== "string") throw new TypeError("Chaîne attendue");
}
```

## 3.7 Valeur de retour `never` et exhaustivité

```typescript
type Forme = { type: "cercle"; rayon: number } | { type: "carre"; cote: number };

function aire(f: Forme): number {
    switch (f.type) {
        case "cercle": return Math.PI * f.rayon ** 2;
        case "carre":  return f.cote ** 2;
        default: {
            const _exhaustif: never = f;        // erreur de compilation si un cas est oublié
            return _exhaustif;
        }
    }
}
```

## 3.8 Fonctions génériques (aperçu)

```typescript
function premier<T>(elements: T[]): T | undefined { return elements[0]; }
```

Voir [section 9](#9-génériques).

---

# 4. Tableaux et tuples

## 4.1 Tableaux

```typescript
let nombres: number[] = [1, 2, 3];
let noms: Array<string> = ["Alice", "Bob"];          // syntaxe générique équivalente
let mixte: (string | number)[] = ["a", 1];
let matrice: number[][] = [[1, 2], [3, 4]];
let vide: string[] = [];                              // ⚠️ sans annotation : any[] implicite ou never[]

nombres.push(4);
// nombres.push("5");       // ❌ erreur de type
```

### Méthodes typées

```typescript
const doubles = nombres.map(n => n * 2);              // number[]
const pairs = nombres.filter(n => n % 2 === 0);       // number[]
const somme = nombres.reduce((total, n) => total + n, 0);
const premier = nombres.find(n => n > 1);             // number | undefined
```

### Tableaux en lecture seule

```typescript
const figes: readonly number[] = [1, 2, 3];
// figes.push(4);            // ❌ 'push' n'existe pas sur un tableau readonly
type Fige = ReadonlyArray<string>;
function lire(valeurs: readonly string[]) { /* ne peut pas modifier */ }
```

> ✅ Déclarez **`readonly`** les paramètres tableau que la fonction ne modifie pas.

### Accès sûr aux indices : `noUncheckedIndexedAccess`

```typescript
const t: string[] = ["a"];
const x = t[5];         // type : string (⚠️ en réalité undefined)
// Avec "noUncheckedIndexedAccess": true  →  string | undefined  (recommandé)
```

## 4.2 Tuples

Un **tuple** est un tableau de **longueur et de types fixés** par position.

```typescript
let personne: [string, number] = ["Alice", 30];
const [nom, age] = personne;                          // décomposition typée
// personne = [30, "Alice"];                          // ❌ ordre incorrect
// personne = ["Alice", 30, true];                    // ❌ longueur incorrecte

let optionnel: [string, number?] = ["Alice"];                  // élément optionnel
let reste: [string, ...number[]] = ["notes", 12, 15, 9];       // éléments variables
let nomme: [nom: string, age: number] = ["Alice", 30];         // étiquettes (documentation)
let figee: readonly [number, number] = [1, 2];
```

Usages typiques : valeurs de retour multiples, paires clé/valeur, **hooks React** (`[valeur, setter]`).

```typescript
function minMax(valeurs: number[]): [min: number, max: number] {
    return [Math.min(...valeurs), Math.max(...valeurs)];
}
const [mini, maxi] = minMax([3, 1, 4]);
```

> ⚠️ `push()` fonctionne sur un tuple (non readonly) sans vérifier la longueur : utilisez `readonly [..]` pour l'interdire.

---

# 5. Énumérations (`enum`) et alternatives

## 5.1 Enums numériques

```typescript
enum Direction {
    Haut,        // 0
    Bas,         // 1
    Gauche,      // 2
    Droite       // 3
}
let d: Direction = Direction.Haut;
Direction[0];                          // "Haut"  (correspondance inverse : propre aux enums NUMÉRIQUES)

enum Statut { Actif = 1, Inactif, Banni = 10 }      // valeurs explicites
```

## 5.2 Enums de chaînes

```typescript
enum Role {
    Admin = "ADMIN",
    Editeur = "EDITEUR",
    Lecteur = "LECTEUR",
}

function peutModifier(role: Role): boolean {
    return role === Role.Admin || role === Role.Editeur;
}
```

Les enums de chaînes sont **plus lisibles** à l'exécution et dans les journaux (pas de correspondance inverse).

## 5.3 `const enum` et `declare enum`

```typescript
const enum Couleur { Rouge = "R", Vert = "V" }       // remplacé en ligne à la compilation (pas d'objet généré)
```

> ⚠️ `const enum` pose des problèmes avec les outils qui compilent fichier par fichier (`isolatedModules`, Vite, esbuild, SWC, Babel) : **évitez-le** dans du code partagé ou publié.

## 5.4 Les alternatives modernes aux enums *(à jour)*

Les enums génèrent du **code JavaScript** (ce n'est pas du pur « effacement de types ») et sont **interdits en mode `erasableSyntaxOnly`**. Beaucoup de projets préfèrent :

### Union de littéraux

```typescript
type Role = "admin" | "editeur" | "lecteur";
let r: Role = "admin";
// r = "root";              // ❌
```

### Objet `as const` + type dérivé

```typescript
const Role = {
    Admin: "ADMIN",
    Editeur: "EDITEUR",
    Lecteur: "LECTEUR",
} as const;

type Role = (typeof Role)[keyof typeof Role];       // "ADMIN" | "EDITEUR" | "LECTEUR"

Object.values(Role);                                // itérable à l'exécution ✅
```

| | `enum` | Union de littéraux | Objet `as const` |
| --- | --- | --- | --- |
| Code généré | ✅ (objet) | ❌ | ✅ (objet) |
| Itérable à l'exécution | ✅ | ❌ | ✅ |
| Mode `erasableSyntaxOnly` | ❌ interdit | ✅ | ✅ |
| Interopérabilité JS | Moyenne | **Excellente** | **Excellente** |
| Recommandation | Code existant | **Défaut** | Quand on a besoin des valeurs |

---

# 6. Interfaces

## 6.1 Définir une interface

Une **interface** décrit la **forme** d'un objet (propriétés, méthodes). TypeScript utilise un **typage structurel** : un objet est compatible s'il a les bonnes propriétés, quelle que soit son origine (*duck typing*).

```typescript
interface Utilisateur {
    id: number;
    nom: string;
    email?: string;               // optionnelle
    readonly creeLe: Date;        // lecture seule
}

const alice: Utilisateur = { id: 1, nom: "Alice", creeLe: new Date() };
// alice.creeLe = new Date();     // ❌ propriété en lecture seule
// const bob: Utilisateur = { id: 2 };          // ❌ propriétés manquantes
```

> ℹ️ Les littéraux d'objet subissent un **contrôle de propriétés excédentaires** : `{ id: 1, nom: "A", creeLe: d, extra: true }` est refusé directement (mais accepté s'il passe par une variable intermédiaire).

## 6.2 Méthodes, fonctions et signatures d'index

```typescript
interface Calculatrice {
    additionner(a: number, b: number): number;       // méthode
    reset: () => void;                               // propriété de type fonction
}

interface Dictionnaire {
    [cle: string]: number;                           // signature d'index
}
const stock: Dictionnaire = { pommes: 10 };

interface Compare { (a: string, b: string): number; }     // interface appelable
interface Constructible { new (nom: string): Utilisateur; } // interface « constructeur »
```

## 6.3 Héritage d'interfaces

```typescript
interface Personne { nom: string; age: number; }
interface Employe extends Personne { poste: string; }
interface Manager extends Employe, Journalisable { equipe: Employe[]; }   // héritage multiple
```

## 6.4 Implémentation par une classe

```typescript
interface Imprimable { imprimer(): void; }

class Rapport implements Imprimable {
    imprimer() { console.log("Impression…"); }
}
```

## 6.5 Fusion de déclarations (*declaration merging*)

Deux interfaces de même nom **fusionnent** (propre aux interfaces, pas aux alias) :

```typescript
interface Config { url: string; }
interface Config { delai: number; }
const c: Config = { url: "x", delai: 5 };      // les deux propriétés sont requises
```

Utile pour **étendre des types de bibliothèques** ([section 12](#12-fichiers-de-déclaration-de-types)).

## 6.6 `interface` ou `type` ?

| | `interface` | `type` |
| --- | --- | --- |
| Objets | ✅ | ✅ |
| Unions, intersections, tuples, primitives | ❌ | ✅ |
| Types conditionnels / mappés | ❌ | ✅ |
| Fusion de déclarations | ✅ | ❌ |
| `extends` / `implements` | ✅ (messages d'erreur plus lisibles) | via intersections `&` |
| Performance du compilateur | Légèrement meilleure sur les grands arbres d'héritage | — |

> ✅ **Règle pratique** : `interface` pour décrire des **formes d'objets** et des contrats de classes ; `type` pour **tout le reste** (unions, tuples, utilitaires). L'essentiel est la **cohérence** dans le projet.

---

# 7. Alias de types, unions et types littéraux

## 7.1 Alias de types

```typescript
type ID = number | string;
type Point = { x: number; y: number };
type Rappel = (erreur: Error | null, donnees?: string) => void;
type Matrice = number[][];

const p: Point = { x: 1, y: 2 };
```

## 7.2 Types union (`|`) : « l'un OU l'autre »

```typescript
type Resultat = string | number;
function afficherId(id: ID) {
    console.log(typeof id === "string" ? id.toUpperCase() : id.toFixed(0));
}
```

### Unions discriminées (*discriminated unions*) ⭐

Un champ **commun** (la « balise ») permet de restreindre précisément le type :

```typescript
type Requete =
    | { etat: "chargement" }
    | { etat: "succes"; donnees: string[] }
    | { etat: "erreur"; message: string };

function afficher(r: Requete): string {
    switch (r.etat) {
        case "chargement": return "…";
        case "succes":     return r.donnees.join(", ");        // donnees disponible
        case "erreur":     return r.message;                    // message disponible
    }
}
```

C'est le moyen idiomatique de modéliser des **états** (et d'éviter les combinaisons impossibles).

## 7.3 Types intersection (`&`) : « l'un ET l'autre »

```typescript
type Identifiable = { id: number };
type Horodate = { creeLe: Date; modifieLe: Date };
type Article = Identifiable & Horodate & { titre: string };
```

## 7.4 Types littéraux

```typescript
type Taille = "S" | "M" | "L" | "XL";
type De = 1 | 2 | 3 | 4 | 5 | 6;
type Methode = "GET" | "POST" | "PUT" | "DELETE";

let t: Taille = "M";
// t = "XXL";                // ❌

function requete(url: string, methode: Methode = "GET") {}

const config = { methode: "GET" };           // methode : string (élargi !)
requete("/x", config.methode);               // ❌ string non assignable à Methode
const config2 = { methode: "GET" } as const; // ✅ type littéral préservé
```

## 7.5 Types littéraux de gabarit (*template literal types*)

```typescript
type Evenement = "clic" | "survol";
type Gestionnaire = `on${Capitalize<Evenement>}`;       // "onClic" | "onSurvol"
type Route = `/api/${string}`;
let r: Route = "/api/utilisateurs";                      // ✅
```

## 7.6 Restriction (*narrowing*) : récapitulatif

| Technique | Exemple |
| --- | --- |
| `typeof` | `typeof x === "string"` |
| `instanceof` | `x instanceof Date` |
| `in` | `"nom" in x` |
| Égalité / vérité | `x === null`, `if (x)` |
| Propriété discriminante | `x.etat === "succes"` |
| Garde personnalisée | `estChat(x)` |
| `Array.isArray` | |

## 7.7 `type` ou `interface` ?

Voir [6.6](#66-interface-ou-type-). Les alias sont **indispensables** pour les unions, intersections, tuples et types calculés.

---

# 🟡 Niveau intermédiaire

---

# 8. Classes et programmation orientée objet

## 8.1 Définir une classe

```typescript
class Personne {
    // Propriétés (déclarées et typées)
    nom: string;
    age: number;

    constructor(nom: string, age: number) {
        this.nom = nom;
        this.age = age;
    }

    saluer(): string {
        return `Bonjour, je suis ${this.nom}`;
    }
}

const alice = new Personne("Alice", 30);
alice.saluer();
```

## 8.2 Modificateurs d'accès

| Modificateur | Accessible depuis |
| --- | --- |
| `public` (par défaut) | Partout |
| `protected` | La classe et ses **sous-classes** |
| `private` | La classe seule (vérifié **à la compilation** uniquement) |
| **`#champ`** | La classe seule, **garanti à l'exécution** (privé natif ECMAScript) |

```typescript
class CompteBancaire {
    public titulaire: string;
    private solde: number = 0;          // TypeScript : privé à la compilation
    #pin: string;                       // JavaScript : réellement privé
    protected devise = "EUR";
    readonly numero: string;            // assignable uniquement à la déclaration ou dans le constructeur

    constructor(titulaire: string, numero: string, pin: string) {
        this.titulaire = titulaire;
        this.numero = numero;
        this.#pin = pin;
    }

    deposer(montant: number): void {
        if (montant <= 0) throw new RangeError("Montant invalide");
        this.solde += montant;
    }

    get soldeActuel(): number { return this.solde; }       // accesseur (getter)
    set pin(nouveau: string) { this.#pin = nouveau; }      // mutateur (setter)
}

const c = new CompteBancaire("Alice", "FR76", "1234");
// c.solde;      // ❌ privé
// c.#pin;       // ❌ erreur de syntaxe hors de la classe
```

> ✅ Pour de **vraies** données privées (sécurité, encapsulation garantie), utilisez **`#champ`**. `private` n'est qu'une contrainte de compilation (contournable avec `as any` ou `obj["solde"]`).

## 8.3 Propriétés de paramètres (raccourci de constructeur)

```typescript
class Produit {
    constructor(
        public readonly id: number,
        public nom: string,
        private prix: number,
    ) {}                                // déclare ET initialise les propriétés
}
```

> ⚠️ Cette syntaxe génère du code : elle est **interdite avec `--erasableSyntaxOnly`**. Dans ce cas, déclarez les propriétés explicitement.

## 8.4 Propriétés et méthodes statiques

```typescript
class Compteur {
    static total = 0;
    static incrementer(): number { return ++Compteur.total; }
    static { /* bloc d'initialisation statique */ }
}
Compteur.incrementer();
```

## 8.5 Héritage

```typescript
class Animal {
    constructor(protected nom: string) {}
    parler(): string { return `${this.nom} fait du bruit`; }
}

class Chien extends Animal {
    constructor(nom: string, private race: string) {
        super(nom);                        // obligatoire avant d'utiliser `this`
    }

    override parler(): string {            // `override` (TS 4.3) : erreur si la méthode parente n'existe pas
        return `${this.nom} aboie`;
    }
}
```

> ✅ Activez **`noImplicitOverride`** : le mot-clé `override` devient obligatoire, ce qui évite de redéfinir une méthode par accident (ou de casser la redéfinition après un renommage).

## 8.6 Classes abstraites

```typescript
abstract class Forme {
    abstract aire(): number;                                // doit être implémentée
    decrire(): string { return `Aire : ${this.aire().toFixed(2)}`; }
}

class Cercle extends Forme {
    constructor(private rayon: number) { super(); }
    aire(): number { return Math.PI * this.rayon ** 2; }
}
// new Forme();       // ❌ impossible d'instancier une classe abstraite
```

## 8.7 Implémenter des interfaces

```typescript
interface Serialisable { versJson(): string; }
interface Identifiable { readonly id: number; }

class Article implements Serialisable, Identifiable {
    constructor(public readonly id: number, public titre: string) {}
    versJson() { return JSON.stringify(this); }
}
```

## 8.8 Le mot-clé `accessor` et la classe comme type

```typescript
class Etat {
    accessor compteur = 0;               // TS 4.9 / décorateurs standard : getter/setter automatiques
}

const p: Personne = new Personne("A", 1);       // le nom de la classe est AUSSI un type
const construire: new (n: string, a: number) => Personne = Personne;    // le constructeur
```

## 8.9 Typage structurel : attention aux surprises

Deux classes de même forme sont compatibles, **sauf** si elles ont des membres `private` / `#privés` :

```typescript
class A { x = 1; }
class B { x = 1; }
const a: A = new B();        // ✅ même structure
```

## 8.10 Principes et bonnes pratiques

- **Composition plutôt qu'héritage** profond (voir [section 17](#17-mixins-et-composition)).
- Programmez **vers des interfaces** (injection de dépendances, tests).
- Rendez les propriétés `readonly` quand elles ne changent pas.
- Dans du code récent, les **fonctions + types** remplacent souvent les classes ; gardez les classes pour les entités à **état et comportement** (et les frameworks qui les imposent : Angular, NestJS).

---

# 9. Génériques

## 9.1 Le problème

Écrire du code **réutilisable** pour plusieurs types **sans perdre la sécurité de typage** (`any` perd l'information).

```typescript
function identite(x: any): any { return x; }       // ❌ le type d'entrée est perdu
function identiteSure<T>(x: T): T { return x; }     // ✅ T est « capturé »

const a = identiteSure("texte");     // T = string
const b = identiteSure(42);          // T = number
const c = identiteSure<boolean>(true);   // T explicite
```

## 9.2 Fonctions génériques

```typescript
function premier<T>(elements: T[]): T | undefined { return elements[0]; }
function paire<A, B>(a: A, b: B): [A, B] { return [a, b]; }

const x = premier([1, 2, 3]);            // number | undefined
const p = paire("a", 1);                 // [string, number]

const cles = <T extends object>(o: T) => Object.keys(o) as (keyof T)[];
```

> Dans un fichier `.tsx`, écrivez `<T,>(x: T) => …` ou `<T extends unknown>` pour éviter l'ambiguïté avec JSX.

## 9.3 Contraintes : `extends`

```typescript
interface AvecLongueur { length: number }

function longueur<T extends AvecLongueur>(x: T): number { return x.length; }
longueur("texte");          // ✅
longueur([1, 2, 3]);        // ✅
// longueur(42);            // ❌ number n'a pas de length

function lire<T, K extends keyof T>(objet: T, cle: K): T[K] { return objet[cle]; }
lire({ nom: "A", age: 3 }, "age");        // number
// lire({ nom: "A" }, "x");               // ❌ "x" n'est pas une clé
```

## 9.4 Interfaces et alias génériques

```typescript
interface Reponse<T> {
    donnees: T;
    statut: number;
    erreur?: string;
}
const r: Reponse<{ id: number; nom: string }> = { donnees: { id: 1, nom: "A" }, statut: 200 };

type Resultat<T, E = Error> = { ok: true; valeur: T } | { ok: false; erreur: E };

type Pagine<T> = { elements: T[]; page: number; total: number };
```

## 9.5 Classes génériques

```typescript
class Pile<T> {
    private elements: T[] = [];
    empiler(x: T): void { this.elements.push(x); }
    depiler(): T | undefined { return this.elements.pop(); }
    get taille(): number { return this.elements.length; }
}

const pile = new Pile<number>();
pile.empiler(1);

interface Depot<T extends { id: number }> {
    trouver(id: number): Promise<T | undefined>;
    sauvegarder(entite: T): Promise<void>;
}
```

## 9.6 Valeurs par défaut des paramètres de type

```typescript
interface Evenement<T = string> { nom: string; charge: T }
const e: Evenement = { nom: "x", charge: "texte" };           // T = string
const f: Evenement<number> = { nom: "y", charge: 42 };
```

## 9.7 Paramètres de type `const` *(TS 5.0, ajout)*

```typescript
function creer<const T extends readonly unknown[]>(valeurs: T): T { return valeurs; }
const t = creer(["a", "b"]);         // readonly ["a", "b"]  (au lieu de string[])
```

## 9.8 `NoInfer` *(TS 5.4, ajout)*

Empêche d'inférer `T` depuis un argument donné :

```typescript
function creerSignal<T extends string>(valeurs: T[], defaut: NoInfer<T>) {}
creerSignal(["rouge", "vert"], "bleu");     // ❌ "bleu" n'est pas dans les valeurs
```

## 9.9 Variance explicite *(ajout)*

Annotations `in` / `out` pour documenter / accélérer :

```typescript
interface Producteur<out T> { produire(): T }       // covariant
interface Consommateur<in T> { consommer(x: T): void }   // contravariant
```

## 9.10 Exemple concret : fonction de requête typée

```typescript
async function getJson<T>(url: string): Promise<T> {
    const reponse = await fetch(url);
    if (!reponse.ok) throw new Error(`HTTP ${reponse.status}`);
    return (await reponse.json()) as T;          // ⚠️ T n'est PAS vérifié à l'exécution
}

interface Utilisateur { id: number; nom: string }
const utilisateur = await getJson<Utilisateur>("/api/users/1");
```

> ⚠️ Le paramètre de type est une **promesse du développeur**, pas une garantie : validez les données reçues avec un schéma (Zod, Valibot…), voir [section 19](#19-typescript-côté-serveur).

---

# 10. Modules et espaces de noms

## 10.1 Modules ES (la norme)

Tout fichier contenant un `import` ou un `export` de niveau supérieur est un **module** avec sa propre portée.

```typescript
// mathematiques.ts
export const PI = 3.14159;
export function additionner(a: number, b: number): number { return a + b; }
export interface Point { x: number; y: number }
export type ID = string | number;
export default class Calculatrice { /* … */ }
```

```typescript
// main.ts
import Calculatrice, { PI, additionner as plus } from "./mathematiques.js";
import * as maths from "./mathematiques.js";
import type { Point, ID } from "./mathematiques.js";      // import UNIQUEMENT de types (effacé)
import { type Point as P, additionner } from "./mathematiques.js";
```

> ⚠️ Avec les **modules ES natifs** (`"module": "nodenext"`), les imports relatifs doivent inclure l'**extension de sortie** (`./fichier.js`, même pour un fichier `.ts`). Avec un **bundler** (`"moduleResolution": "bundler"`), on peut l'omettre. TS 5.7 propose `--rewriteRelativeImportExtensions` pour écrire des imports en `.ts`.

### Réexporter

```typescript
export { additionner } from "./mathematiques.js";
export * from "./utilitaires.js";
export type { Point } from "./types.js";
```

### Imports de types : `verbatimModuleSyntax` *(à jour)*

L'option **`verbatimModuleSyntax`** impose `import type` pour les types et garantit que ce qui est écrit est ce qui est généré : c'est la configuration moderne recommandée (elle remplace `importsNotUsedAsValues` et `preserveValueImports`).

## 10.2 CommonJS et ES modules

| | ES modules | CommonJS |
| --- | --- | --- |
| Syntaxe | `import` / `export` | `require()` / `module.exports` |
| `"module"` TypeScript | `esnext`, `nodenext`, `preserve` | `commonjs` |
| Statut | **Standard** | Historique (Node.js) |

Pour Node.js, utilisez `"module": "nodenext"` et `"type": "module"` dans `package.json` (ou l'extension `.mts`). Voir [section 20](#20-configuration-du-projet-tsconfigjson).

## 10.3 Importer du JSON et des ressources

```typescript
import config from "./config.json" with { type: "json" };       // attributs d'import (⚠️ plus `assert`)
// tsconfig : "resolveJsonModule": true
```

## 10.4 Espaces de noms (*namespaces*) : historique

Les `namespace` (anciennement « modules internes ») regroupaient du code **dans un même fichier global**, avant l'arrivée des modules ES.

```typescript
namespace Utilitaires {
    export function journaliser(message: string): void { console.log(message); }
    export namespace Maths {
        export const carre = (x: number) => x * x;
    }
}
Utilitaires.journaliser("Salut");
Utilitaires.Maths.carre(4);
```

> 📌 **À jour** :
> - **Évitez les `namespace` dans du nouveau code** : utilisez des **modules ES**. Ils génèrent du code et sont **interdits en mode `erasableSyntaxOnly`**.
> - TypeScript 6.0 **déprécie l'ancienne syntaxe `module Nom { }`** (utilisez le mot-clé `namespace`).
> - Les `declare namespace` restent **légitimes** dans les fichiers `.d.ts` pour décrire des bibliothèques globales.

| | **Module ES** | **Namespace** |
| --- | --- | --- |
| Portée | Fichier | Bloc global / fusionnable |
| Syntaxe | `import` / `export` | `namespace` + `export` |
| Chargement | Natif, *tree-shaking* | Concaténation / balises `<script>` |
| Usage conseillé | ✅ **Toujours** | Seulement pour du code hérité ou des `.d.ts` |

## 10.5 Imports dynamiques et chemins

```typescript
const { default: marked } = await import("marked");            // chargement à la demande
```

Alias de chemins (`@/…`) : voir [section 20.4](#204-alias-de-chemins-paths).

---

# 11. Types avancés

## 11.1 `keyof`, `typeof` et types indexés

```typescript
interface Utilisateur { id: number; nom: string; email: string }

type Cle = keyof Utilisateur;                  // "id" | "nom" | "email"
type TypeNom = Utilisateur["nom"];             // string
type Tous = Utilisateur[keyof Utilisateur];    // string | number

const config = { port: 3000, hote: "localhost" };
type Config = typeof config;                   // { port: number; hote: string }

const jours = ["lun", "mar"] as const;
type Jour = (typeof jours)[number];            // "lun" | "mar"

type ElementDe<T> = T extends readonly (infer E)[] ? E : never;
```

## 11.2 Types mappés (*mapped types*)

Transforment chaque propriété d'un type :

```typescript
type EnLectureSeule<T> = { readonly [K in keyof T]: T[K] };
type Optionnel<T> = { [K in keyof T]?: T[K] };
type Nullable<T> = { [K in keyof T]: T[K] | null };

// Modificateurs : + / - pour ajouter ou retirer readonly et ?
type Mutable<T> = { -readonly [K in keyof T]: T[K] };
type Requis<T> = { [K in keyof T]-?: T[K] };

// Renommage des clés avec `as`
type Getters<T> = {
    [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};
type G = Getters<{ nom: string; age: number }>;
// { getNom: () => string; getAge: () => number }

// Filtrer des clés
type SansFonctions<T> = { [K in keyof T as T[K] extends Function ? never : K]: T[K] };
```

## 11.3 Types conditionnels

```typescript
type EstString<T> = T extends string ? "oui" : "non";
type A = EstString<"x">;     // "oui"
type B = EstString<42>;      // "non"

// Distributifs sur les unions
type SansNull<T> = T extends null | undefined ? never : T;
type C = SansNull<string | null>;       // string

// Pour empêcher la distribution : [T] extends [U]
type EstNever<T> = [T] extends [never] ? true : false;
```

## 11.4 `infer` : extraire un type

```typescript
type TypeRetour<T> = T extends (...args: any[]) => infer R ? R : never;
type R = TypeRetour<() => string>;                 // string

type ContenuPromesse<T> = T extends Promise<infer U> ? U : T;
type P = ContenuPromesse<Promise<number>>;         // number

type Parametres<T> = T extends (...args: infer P) => any ? P : never;
type PremierArg<T extends unknown[]> = T extends [infer Premier, ...unknown[]] ? Premier : never;
```

## 11.5 Types littéraux de gabarit et manipulation de chaînes

```typescript
type Evenements = "clic" | "survol";
type Handlers = { [E in Evenements as `on${Capitalize<E>}`]: () => void };

type Majuscule = Uppercase<"abc">;      // "ABC"  (aussi Lowercase, Capitalize, Uncapitalize)

type ParametreRoute<S extends string> =
    S extends `${string}:${infer P}/${infer Reste}` ? P | ParametreRoute<`/${Reste}`> :
    S extends `${string}:${infer P}` ? P : never;
type Params = ParametreRoute<"/users/:id/posts/:postId">;    // "id" | "postId"
```

## 11.6 Types récursifs

```typescript
type JSONValeur = string | number | boolean | null | JSONValeur[] | { [cle: string]: JSONValeur };

type ProfondementPartiel<T> = {
    [K in keyof T]?: T[K] extends object ? ProfondementPartiel<T[K]> : T[K];
};
```

## 11.7 `satisfies`, `as const` et inférence avancée

Voir [2.6](#26-as-const-et-satisfies-ajout). Autres outils : l'opérateur `typeof` sur les valeurs, `ReturnType<typeof fonction>`, `Awaited<T>`.

## 11.8 Gardes d'exhaustivité et types marqués (*branded types*) *(ajout)*

```typescript
type EuroMontant = number & { readonly __marque: "EUR" };
type IdUtilisateur = string & { readonly __marque: "IdUtilisateur" };

const euros = (n: number) => n as EuroMontant;
function payer(m: EuroMontant) {}
payer(euros(10));
// payer(10);         // ❌ un number nu n'est pas un EuroMontant
```

Utile pour distinguer des valeurs de même type primitif (identifiants, unités).

## 11.9 Conseils

- Commencez **simple** : n'écrivez des types complexes que lorsqu'ils éliminent réellement des erreurs.
- Nommez et **commentez** les types utilitaires ; testez-les (section 23).
- Préférez les **utilitaires intégrés** ([section 13](#13-types-utilitaires)).

---

# 12. Fichiers de déclaration de types

## 12.1 Qu'est-ce qu'un fichier `.d.ts` ?

Un fichier de **déclaration** (`.d.ts`) décrit **uniquement des types** (aucun code exécutable). Il permet à TypeScript de connaître la forme d'une bibliothèque **écrite en JavaScript**.

| Source des types | Où |
| --- | --- |
| **Inclus dans le paquet** | Champ `"types"` du `package.json` (la plupart des bibliothèques modernes) ✅ |
| **DefinitelyTyped** | Paquets `@types/xxx` |
| **Vos propres déclarations** | Fichiers `.d.ts` du projet |

## 12.2 Générer des déclarations

```json
{ "compilerOptions": { "declaration": true, "declarationMap": true, "emitDeclarationOnly": false } }
```

`tsc` génère un `.d.ts` pour chaque `.ts`. Avec `isolatedDeclarations` (TS 5.5), la génération peut se faire fichier par fichier, plus rapidement.

## 12.3 DefinitelyTyped : `@types`

```bash
npm install -D @types/node @types/express @types/lodash
```

> 📌 **À jour (TS 6.0)** : l'option **`types` vaut `[]` par défaut** : les paquets `@types/*` **ne sont plus chargés automatiquement**. Listez ceux dont vous avez besoin :
> ```json
> { "compilerOptions": { "types": ["node", "vitest/globals"] } }
> ```
> Les `import` explicites (`import express from "express"`) continuent de charger leurs types sans passer par `types`.

## 12.4 Où TypeScript cherche-t-il les types ?

1. Les types fournis par le **paquet** (`"types"` / `"exports"` dans `package.json`).
2. Les paquets **`@types/…`** listés dans `types` (ou imports explicites).
3. Les fichiers `.d.ts` inclus par `include` / `files` et les `typeRoots`.

## 12.5 Écrire ses propres déclarations

### Module sans types

```typescript
// types/ancienne-lib.d.ts
declare module "ancienne-lib" {
    export function faire(x: number): string;
    export const version: string;
    export default function creer(options?: { debug?: boolean }): void;
}

declare module "*.svg" {                 // fichiers non-code importés par un bundler
    const url: string;
    export default url;
}
declare module "*.module.css" {
    const classes: Record<string, string>;
    export default classes;
}
```

### Variables et fonctions globales

```typescript
// types/global.d.ts
declare const VERSION_APP: string;                   // injectée par le bundler
declare function ga(commande: string, ...args: unknown[]): void;

interface Window { dataLayer: unknown[]; monApp: { version: string } }   // fusion avec l'interface globale
```

### Étendre les types d'une bibliothèque (*module augmentation*)

```typescript
// types/express.d.ts
import "express";

declare module "express-serve-static-core" {
    interface Request {
        utilisateur?: { id: number; role: "admin" | "membre" };
    }
}
```

> ⚠️ Un fichier `.d.ts` **sans** `import`/`export` est **global** ; avec `import`/`export` c'est un **module** (les déclarations n'y sont plus globales : utilisez `declare global { … }`).

```typescript
export {};
declare global {
    interface Array<T> { dernier(): T | undefined }
}
```

## 12.6 Configuration

```json
{
    "compilerOptions": { "typeRoots": ["./node_modules/@types", "./types"], "skipLibCheck": true },
    "include": ["src", "types"]
}
```

`skipLibCheck: true` accélère la compilation en ne vérifiant pas les `.d.ts` des dépendances.

## 12.7 Conseils

- **Ne modifiez jamais** `node_modules/@types` : utilisez l'augmentation.
- Gardez les `.d.ts` **petits et ciblés** ; rangez-les dans un dossier `types/`.
- Si une bibliothèque n'a pas de types : cherchez `@types/…`, sinon écrivez un `declare module` minimal, puis améliorez-le.
- Pour publier une bibliothèque, générez et distribuez ses `.d.ts` (`"types"` et `"exports"` dans `package.json`).

---

# 🔴 Niveau avancé

---

# 13. Types utilitaires

## 13.1 Les types intégrés

| Utilitaire | Rôle | Exemple |
| --- | --- | --- |
| `Partial<T>` | Toutes les propriétés **optionnelles** | `Partial<Utilisateur>` |
| `Required<T>` | Toutes **obligatoires** | `Required<Config>` |
| `Readonly<T>` | Toutes **en lecture seule** | `Readonly<Point>` |
| `Pick<T, K>` | **Sélectionne** des propriétés | `Pick<U, "id" \| "nom">` |
| `Omit<T, K>` | **Exclut** des propriétés | `Omit<U, "motDePasse">` |
| `Record<K, V>` | Objet de clés `K` → valeurs `V` | `Record<string, number>` |
| `Exclude<U, E>` | Retire de l'union `U` les membres assignables à `E` | `Exclude<"a" \| "b", "a">` → `"b"` |
| `Extract<U, E>` | Garde les membres de `U` assignables à `E` | |
| `NonNullable<T>` | Retire `null` et `undefined` | |
| `ReturnType<F>` | Type de retour d'une fonction | `ReturnType<typeof f>` |
| `Parameters<F>` | Tuple des paramètres | |
| `ConstructorParameters<C>` / `InstanceType<C>` | Pour les classes | |
| `Awaited<T>` | Type « déballé » d'une promesse | `Awaited<Promise<string>>` → `string` |
| `NoInfer<T>` | Bloque l'inférence *(TS 5.4)* | |
| `ThisParameterType<F>` / `OmitThisParameter<F>` | Manipulent `this` | |
| `Uppercase` / `Lowercase` / `Capitalize` / `Uncapitalize` | Chaînes littérales | |

```typescript
interface Utilisateur {
    id: number;
    nom: string;
    email: string;
    motDePasse: string;
}

type MiseAJour = Partial<Omit<Utilisateur, "id">>;            // modification : tout optionnel sauf id retiré
type UtilisateurPublic = Omit<Utilisateur, "motDePasse">;
type Resume = Pick<Utilisateur, "id" | "nom">;
type ParId = Record<number, Utilisateur>;
type Permissions = Record<"lire" | "ecrire" | "supprimer", boolean>;

function mettreAJour(id: number, changements: Partial<Utilisateur>) { /* … */ }

async function charger() { return { ok: true, donnees: [1, 2] }; }
type Charge = Awaited<ReturnType<typeof charger>>;            // { ok: boolean; donnees: number[] }
```

## 13.2 Combiner des utilitaires

```typescript
type PartielProfond<T> = { [K in keyof T]?: T[K] extends object ? PartielProfond<T[K]> : T[K] };
type RendreOptionnel<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>;
type Valeurs<T> = T[keyof T];
type CleDeType<T, V> = { [K in keyof T]: T[K] extends V ? K : never }[keyof T];
type Fusion<A, B> = Omit<A, keyof B> & B;
type Aplati<T> = { [K in keyof T]: T[K] } & {};      // simplifie l'affichage d'intersections
```

## 13.3 Cas d'usage

| Besoin | Solution |
| --- | --- |
| Formulaire de **modification** | `Partial<T>` |
| Masquer des champs sensibles | `Omit<T, "motDePasse">` |
| DTO de création sans `id` | `Omit<T, "id" \| "creeLe">` |
| Table de correspondance | `Record<Cle, Valeur>` |
| Typer le résultat d'une fonction | `ReturnType<typeof f>` / `Awaited<…>` |
| Props d'un composant dérivées d'un autre | `ComponentProps<typeof X>` (React) |

## 13.4 Écrire ses propres utilitaires

```typescript
type Egaux<A, B> = (<T>() => T extends A ? 1 : 2) extends (<T>() => T extends B ? 1 : 2) ? true : false;
type Tests = Egaux<Pick<{ a: 1; b: 2 }, "a">, { a: 1 }>;     // true
```

Testez vos types avec `expectTypeOf` (Vitest) ou la bibliothèque `tsd` : [section 23.5](#235-tester-les-types).

---

# 14. Décorateurs

## 14.1 Deux versions à connaître *(à jour)*

Un **décorateur** est une fonction qui **observe ou modifie** une classe ou un membre, avec la syntaxe `@decorateur`.

| | **Décorateurs standard** (TC39) | **Décorateurs « expérimentaux »** (historiques) |
| --- | --- | --- |
| Activation | **Aucune** (TS 5.0+) | `"experimentalDecorators": true` |
| Signature | `(valeur, contexte)` | `(cible, nomPropriete, descripteur)` |
| Décorateurs de **paramètres** | ❌ (non standard) | ✅ |
| Métadonnées (`emitDecoratorMetadata`) | ❌ (pour l'instant) | ✅ |
| Utilisés par | Nouveau code, bibliothèques récentes | **Angular, NestJS, TypeORM**… (toujours basés sur l'ancienne version) |

> ⚠️ Les deux ne sont **pas compatibles**. Vérifiez ce qu'exige votre framework avant de choisir.

## 14.2 Décorateurs standard (TS 5.x)

### Décorateur de classe

```typescript
function journalise<T extends new (...args: any[]) => object>(cible: T, contexte: ClassDecoratorContext) {
    console.log(`Classe ${String(contexte.name)} définie`);
    return class extends cible {
        constructor(...args: any[]) { super(...args); console.log("Instance créée"); }
    };
}

@journalise
class Service {}
```

### Décorateur de méthode

```typescript
function chronometre<This, Args extends unknown[], Ret>(
    cible: (this: This, ...args: Args) => Ret,
    contexte: ClassMethodDecoratorContext<This, (this: This, ...args: Args) => Ret>,
) {
    return function (this: This, ...args: Args): Ret {
        const debut = performance.now();
        try { return cible.call(this, ...args); }
        finally { console.log(`${String(contexte.name)} : ${(performance.now() - debut).toFixed(1)} ms`); }
    };
}

class Calcul {
    @chronometre
    lourd(n: number): number { let s = 0; for (let i = 0; i < n; i++) s += i; return s; }
}
```

### Décorateur de champ et `accessor`

```typescript
function valeurParDefaut<T>(defaut: T) {                      // fabrique de décorateur
    return function (_: undefined, contexte: ClassFieldDecoratorContext) {
        return (valeurInitiale: T | undefined) => valeurInitiale ?? defaut;
    };
}

class Options {
    @valeurParDefaut(8080) port?: number;
}
```

### Contexte et initialiseurs

Le **contexte** (`context`) donne `kind` (`"class"`, `"method"`, `"field"`…), `name`, `static`, `private`, `addInitializer()` (code exécuté à l'initialisation), `metadata`.

```typescript
function lie(_: unknown, contexte: ClassMethodDecoratorContext) {
    contexte.addInitializer(function (this: any) { this[contexte.name] = this[contexte.name].bind(this); });
}
```

## 14.3 Décorateurs expérimentaux (hérités)

```json
{ "compilerOptions": { "experimentalDecorators": true, "emitDecoratorMetadata": true } }
```

```typescript
function Controller(prefixe: string): ClassDecorator {          // fabrique + décorateur de classe
    return (cible) => { Reflect.defineMetadata("prefixe", prefixe, cible); };
}

function Get(chemin: string): MethodDecorator {
    return (cible, cle, descripteur) => { /* enregistrer la route */ };
}

function Valide(cible: Object, cle: string | symbol, indice: number) { /* décorateur de paramètre */ }

@Controller("/users")
class UsersController {
    @Get("/")
    liste() { return []; }
}
```

Les bibliothèques de **métadonnées** (`reflect-metadata`) permettent de lire des informations de type à l'exécution (injection de dépendances, validation, ORM).

## 14.4 Cas d'usage

| Usage | Exemple |
| --- | --- |
| **Journalisation / mesure** | `@chronometre`, `@journalise` |
| **Injection de dépendances** | `@Injectable()` (Angular, NestJS) |
| **Routage** | `@Controller()`, `@Get()` |
| **Validation** | `@IsEmail()` (class-validator) |
| **Persistance** | `@Entity()`, `@Column()` (TypeORM) |
| **Mémoïsation, anti-rebond** | `@memo`, `@debounce` |

## 14.5 Bonnes pratiques

- Gardez les décorateurs **simples et sans effets de bord cachés**.
- Documentez leur comportement (ils sont « magiques »).
- Pour du nouveau code **sans framework imposé**, préférez les décorateurs **standard** ; ou des **fonctions d'ordre supérieur** / **composition**, souvent plus explicites.

---

# 15. Programmation asynchrone

## 15.1 Promesses typées

Une `Promise<T>` représente une valeur de type `T` disponible **plus tard**.

```typescript
function attendre(ms: number): Promise<void> {
    return new Promise((resolve) => setTimeout(resolve, ms));
}

function chargerNombre(): Promise<number> {
    return new Promise((resolve, reject) => {
        Math.random() > 0.5 ? resolve(42) : reject(new Error("Échec"));
    });
}

chargerNombre()
    .then((n) => n * 2)              // Promise<number>
    .catch((e: unknown) => console.error(e))
    .finally(() => console.log("Terminé"));
```

## 15.2 `async` / `await`

Une fonction `async` **retourne toujours une promesse** ; le type de retour s'annote `Promise<T>`.

```typescript
interface Utilisateur { id: number; nom: string }

async function chargerUtilisateur(id: number): Promise<Utilisateur> {
    const reponse = await fetch(`https://api.exemple.com/users/${id}`);
    if (!reponse.ok) throw new Error(`HTTP ${reponse.status}`);          // fetch ne rejette pas sur un 404
    return (await reponse.json()) as Utilisateur;
}

const u = await chargerUtilisateur(1);        // await de haut niveau dans un module ES
```

## 15.3 Gérer les erreurs : `unknown`

Avec `strict` (`useUnknownInCatchVariables`), la variable du `catch` est de type **`unknown`** : il faut la **restreindre**.

```typescript
try {
    await chargerUtilisateur(1);
} catch (erreur) {                                    // unknown
    if (erreur instanceof Error) {
        console.error(erreur.message);
    } else {
        console.error("Erreur inconnue", erreur);
    }
}

function messageDErreur(e: unknown): string {
    return e instanceof Error ? e.message : String(e);
}
```

### Le motif « résultat » plutôt que les exceptions (option)

```typescript
type Resultat<T, E = Error> = { ok: true; valeur: T } | { ok: false; erreur: E };

async function essayer<T>(promesse: Promise<T>): Promise<Resultat<T>> {
    try { return { ok: true, valeur: await promesse }; }
    catch (e) { return { ok: false, erreur: e instanceof Error ? e : new Error(String(e)) }; }
}

const r = await essayer(chargerUtilisateur(1));
if (r.ok) console.log(r.valeur.nom); else console.error(r.erreur.message);
```

## 15.4 Exécution parallèle

```typescript
// Séquentiel (lent) : attend A avant de lancer B ❌
const a = await chargerUtilisateur(1);
const b = await chargerUtilisateur(2);

// Parallèle ✅ : les types sont conservés dans un tuple
const [u1, u2] = await Promise.all([chargerUtilisateur(1), chargerUtilisateur(2)]);

const resultats = await Promise.allSettled([chargerUtilisateur(1), chargerUtilisateur(2)]);
for (const r of resultats) {
    if (r.status === "fulfilled") console.log(r.value.nom);
    else console.error(r.reason);
}

const premier = await Promise.race([chargerUtilisateur(1), attendre(1000).then(() => null)]);
const nimporte = await Promise.any([p1, p2]);               // première réussite
```

## 15.5 Annulation et délai d'expiration

```typescript
async function chargerAvecDelai(url: string, ms = 5000): Promise<unknown> {
    const reponse = await fetch(url, { signal: AbortSignal.timeout(ms) });
    return reponse.json();
}

const controleur = new AbortController();
fetch(url, { signal: controleur.signal });
controleur.abort();
```

## 15.6 Typer les API asynchrones

```typescript
type Asynchrone<T> = T extends (...args: infer A) => infer R ? (...args: A) => Promise<Awaited<R>> : never;

interface Depot<T> {
    trouver(id: number): Promise<T | undefined>;
    lister(): Promise<readonly T[]>;
}

async function* paginer<T>(charger: (page: number) => Promise<T[]>): AsyncGenerator<T[], void, void> {
    for (let page = 1; ; page++) {
        const lot = await charger(page);
        if (lot.length === 0) return;
        yield lot;
    }
}
for await (const lot of paginer(chargerPage)) console.log(lot.length);
```

## 15.7 Rappels (*callbacks*) et événements typés

```typescript
type Rappel<T> = (erreur: Error | null, donnees?: T) => void;

import { promisify } from "node:util";
const lireFichier = promisify(fs.readFile);          // transforme un callback Node en promesse
// ou : import { readFile } from "node:fs/promises";
```

## 15.8 Programmation réactive avec RxJS

```typescript
import { fromEvent, debounceTime, map, distinctUntilChanged, switchMap } from "rxjs";
import { ajax } from "rxjs/ajax";

const champ = document.querySelector<HTMLInputElement>("#recherche")!;
fromEvent(champ, "input").pipe(
    debounceTime(300),
    map(() => champ.value),
    distinctUntilChanged(),
    switchMap((texte) => ajax.getJSON<{ resultats: string[] }>(`/api/recherche?q=${texte}`)),
).subscribe(({ resultats }) => console.log(resultats));
```

Utile pour des **flux d'événements** (saisie, WebSockets) ; Angular l'utilise massivement. Pour de simples requêtes, `async/await` suffit.

## 15.9 Bonnes pratiques

- **Toujours** gérer les erreurs (`try/catch`, `.catch`) ; jamais de promesse « flottante » (règle ESLint `no-floating-promises`).
- Paralléliser avec `Promise.all` les tâches **indépendantes**.
- Ne **pas** utiliser `await` dans `forEach` : employez `for...of` ou `Promise.all(tableau.map(...))`.
- **Valider** les données reçues (le type générique de `json()` n'est qu'une promesse).
- Définir des **délais d'expiration** et permettre l'**annulation**.

---

# 16. Manipuler le DOM

## 16.1 Typer les éléments

La bibliothèque `lib.dom` décrit tous les éléments (`HTMLInputElement`, `HTMLButtonElement`, `HTMLCanvasElement`…). Activez-la : `"lib": ["es2023", "dom", "dom.iterable"]`.

```typescript
const bouton = document.getElementById("envoyer");            // HTMLElement | null
const champ = document.querySelector("#nom");                  // Element | null

// Générique : précise le type attendu (sans assertion)
const entree = document.querySelector<HTMLInputElement>("#nom");
if (entree) console.log(entree.value);

// Le nom de balise donne le type exact
const lien = document.querySelector("a");                      // HTMLAnchorElement | null
const toutes = document.querySelectorAll<HTMLLIElement>("li"); // NodeListOf<HTMLLIElement>
const canvas = document.createElement("canvas");               // HTMLCanvasElement
```

## 16.2 Gestion de la valeur `null`

```typescript
const titre = document.querySelector("h1");
// titre.textContent = "x";                    // ❌ possiblement null
if (titre) titre.textContent = "Bonjour";      // ✅ restriction
titre?.classList.add("actif");                  // ✅ chaînage optionnel

function requis<T extends Element>(selecteur: string): T {       // utilitaire : échoue explicitement
    const el = document.querySelector<T>(selecteur);
    if (!el) throw new Error(`Élément introuvable : ${selecteur}`);
    return el;
}
const app = requis<HTMLDivElement>("#app");
```

> ⚠️ Évitez l'assertion non nulle `!` : un utilitaire qui lève une erreur claire est plus sûr.

## 16.3 Événements typés

```typescript
const bouton = requis<HTMLButtonElement>("#envoyer");

bouton.addEventListener("click", (e: MouseEvent) => {              // e est inféré : MouseEvent
    console.log(e.clientX, e.clientY);
});

const entree = requis<HTMLInputElement>("#nom");
entree.addEventListener("input", (e) => {
    const cible = e.target as HTMLInputElement;                   // e.target : EventTarget | null
    console.log(cible.value);
    // ou : e.currentTarget.value  (currentTarget est typé comme l'élément écouté)
});

document.addEventListener("keydown", (e: KeyboardEvent) => {
    if (e.key === "Escape") { /* … */ }
});

document.querySelector<HTMLFormElement>("form")?.addEventListener("submit", (e: SubmitEvent) => {
    e.preventDefault();
    const donnees = new FormData(e.target as HTMLFormElement);
    console.log(Object.fromEntries(donnees));
});
```

| Événement | Type |
| --- | --- |
| `click`, `mousemove` | `MouseEvent` |
| `pointerdown` | `PointerEvent` |
| `keydown`, `keyup` | `KeyboardEvent` |
| `input`, `change` | `Event` / `InputEvent` |
| `submit` | `SubmitEvent` |
| Personnalisé | `CustomEvent<T>` |

## 16.4 Événements personnalisés typés

```typescript
interface EvenementsApp { "panier:ajout": CustomEvent<{ id: number }> }

declare global {
    interface HTMLElementEventMap extends EvenementsApp {}
}

document.addEventListener("panier:ajout", (e) => console.log(e.detail.id));        // typé
document.dispatchEvent(new CustomEvent("panier:ajout", { detail: { id: 7 } }));
```

## 16.5 Créer et modifier des éléments

```typescript
function creer<K extends keyof HTMLElementTagNameMap>(
    balise: K,
    proprietes: Partial<HTMLElementTagNameMap[K]> = {},
): HTMLElementTagNameMap[K] {
    return Object.assign(document.createElement(balise), proprietes);
}

const lien = creer("a", { href: "/accueil", textContent: "Accueil" });     // HTMLAnchorElement
document.body.append(lien);
```

## 16.6 Observateurs et API du navigateur

`IntersectionObserver`, `ResizeObserver`, `MutationObserver`, `localStorage` (valeurs `string | null`), `fetch`, `FormData`, `URLSearchParams`, `AbortController`… sont tous typés.

```typescript
const stockage = {
    lire<T>(cle: string, defaut: T): T {
        try { return JSON.parse(localStorage.getItem(cle) ?? "null") ?? defaut; }
        catch { return defaut; }
    },
    ecrire<T>(cle: string, valeur: T): void { localStorage.setItem(cle, JSON.stringify(valeur)); },
};
```

## 16.7 Bonnes pratiques

- Utilisez `querySelector<T>()` plutôt que des assertions `as`.
- Préférez `textContent` à `innerHTML` (sécurité XSS).
- Pour des interfaces non triviales, utilisez un **framework** ou des **composants web** (voir sections 17 et 18).

---

# 17. Mixins et composition

## 17.1 Pourquoi ?

L'héritage simple limite les classes à **un seul parent**. Les **mixins** ajoutent des comportements réutilisables à plusieurs classes ; la **composition** assemble des objets plutôt que d'empiler des héritages.

> *« Préférez la composition à l'héritage. »*

## 17.2 Mixins de classes

```typescript
type Constructeur<T = {}> = new (...args: any[]) => T;

function Horodate<TBase extends Constructeur>(Base: TBase) {
    return class extends Base {
        creeLe = new Date();
        modifieLe = new Date();
        toucher() { this.modifieLe = new Date(); }
    };
}

function Activable<TBase extends Constructeur>(Base: TBase) {
    return class extends Base {
        actif = false;
        activer() { this.actif = true; }
        desactiver() { this.actif = false; }
    };
}

class Utilisateur {
    constructor(public nom: string) {}
}

const UtilisateurAvance = Activable(Horodate(Utilisateur));     // composition de mixins
const u = new UtilisateurAvance("Alice");
u.activer();
u.toucher();
console.log(u.nom, u.actif, u.creeLe);                            // types combinés ✅
```

## 17.3 Mixins avec contraintes

```typescript
interface AvecNom { nom: string }

function Salutation<TBase extends Constructeur<AvecNom>>(Base: TBase) {
    return class extends Base {
        saluer() { return `Bonjour ${this.nom}`; }       // `nom` est garanti par la contrainte
    };
}
```

## 17.4 Composition par objets et fonctions

```typescript
interface PeutVoler { voler(): string }
interface PeutNager { nager(): string }

const volant = (nom: string): PeutVoler => ({ voler: () => `${nom} vole` });
const nageant = (nom: string): PeutNager => ({ nager: () => `${nom} nage` });

function canard(nom: string): PeutVoler & PeutNager {
    return { ...volant(nom), ...nageant(nom) };
}
canard("Donald").voler();
```

### Composition par délégation (injection)

```typescript
class Journal { ecrire(msg: string) { console.log(msg); } }

class Service {
    constructor(private readonly journal: Journal) {}           // on « possède » un Journal, on ne l'« est » pas
    executer() { this.journal.ecrire("Exécution"); }
}
```

## 17.5 Pièges

| Piège | Remède |
| --- | --- |
| Conflits de noms entre mixins | Nommer précisément, tester |
| Ordre d'application (le dernier gagne) | Documenter l'ordre |
| Difficile à lire / déboguer | Rester sobre : 2–3 mixins maximum |
| Mixins et `private` / `#champs` | Les types anonymes de classes avec membres privés exportés posent problème (`declaration: true`) |

## 17.6 Mixins ou composition ?

| Besoin | Choix |
| --- | --- |
| Ajouter des **méthodes/état** à plusieurs classes | Mixins |
| Assembler des **comportements indépendants** | Composition d'objets |
| Remplacer un comportement à l'exécution | Délégation / stratégie (injection) |
| Hiérarchie claire « est un » | Héritage |

---

# 18. TypeScript et frameworks front-end

## 18.1 Démarrer un projet : **Vite**

> 📌 **À jour** : `create-react-app` est **déprécié** (plus maintenu). Utilisez **Vite** ou le méta-framework de votre choix (Next.js, Remix/React Router, Nuxt, SvelteKit, Astro, Angular CLI).

```bash
npm create vite@latest mon-app -- --template react-ts        # ou vue-ts, svelte-ts, vanilla-ts
cd mon-app && npm install && npm run dev
```

> ℹ️ Vite **ne vérifie pas** les types (il les efface) : exécutez `tsc --noEmit` (ou `vue-tsc --noEmit`) dans vos scripts et la CI.

## 18.2 React

### Composants et props

```tsx
import { useState, useRef, useEffect, type ReactNode, type ChangeEvent } from "react";

interface BoutonProps {
    etiquette: string;
    variante?: "primaire" | "secondaire";
    onClic?: () => void;
    children?: ReactNode;
}

function Bouton({ etiquette, variante = "primaire", onClic, children }: BoutonProps) {
    return (
        <button className={variante} onClick={onClic}>
            {etiquette}{children}
        </button>
    );
}
```

> ✅ **Typez les props avec une interface** et une fonction ordinaire ; `React.FC` n'est plus nécessaire (et n'apporte plus d'avantage).
> Avec **React 19**, `ref` est une **prop ordinaire** (`ref?: Ref<HTMLInputElement>`) ; `forwardRef` n'est plus requis pour les nouveaux composants.

### Hooks

```tsx
interface Utilisateur { id: number; nom: string }

function Profil() {
    const [utilisateur, setUtilisateur] = useState<Utilisateur | null>(null);     // type explicite quand la valeur initiale est null
    const [compteur, setCompteur] = useState(0);                                  // number (inféré)
    const champ = useRef<HTMLInputElement>(null);

    useEffect(() => {
        const controleur = new AbortController();
        fetch("/api/me", { signal: controleur.signal })
            .then((r) => r.json() as Promise<Utilisateur>)
            .then(setUtilisateur)
            .catch(() => {});
        return () => controleur.abort();
    }, []);

    const surChangement = (e: ChangeEvent<HTMLInputElement>) => setCompteur(Number(e.target.value));

    return (
        <>
            <input ref={champ} onChange={surChangement} />
            <p>{utilisateur?.nom ?? "Chargement…"} — {compteur}</p>
        </>
    );
}
```

### Composants génériques et `useReducer`

```tsx
interface ListeProps<T> {
    elements: readonly T[];
    rendu: (element: T) => ReactNode;
    cle: (element: T) => string | number;
}
function Liste<T>({ elements, rendu, cle }: ListeProps<T>) {
    return <ul>{elements.map((e) => <li key={cle(e)}>{rendu(e)}</li>)}</ul>;
}

type Action = { type: "incrementer" } | { type: "fixer"; valeur: number };      // union discriminée
function reducteur(etat: number, action: Action): number {
    switch (action.type) {
        case "incrementer": return etat + 1;
        case "fixer": return action.valeur;
    }
}
```

Types utiles : `ComponentProps<typeof X>`, `PropsWithChildren`, `ReactNode`, `MouseEvent<HTMLButtonElement>`, `FormEvent`, `CSSProperties`. **Context** : `createContext<Valeur | null>(null)` + hook personnalisé qui vérifie la présence du fournisseur.

## 18.3 Angular

Angular est **écrit en TypeScript** et le **requiert**.

```bash
npm install -g @angular/cli
ng new mon-app
```

```typescript
import { Component, Injectable, inject, signal, computed, input } from "@angular/core";
import { HttpClient } from "@angular/common/http";

interface Tache { id: number; titre: string; faite: boolean }

@Injectable({ providedIn: "root" })
export class TacheService {
    private readonly http = inject(HttpClient);
    lister() { return this.http.get<Tache[]>("/api/taches"); }        // Observable<Tache[]>
}

@Component({
    selector: "app-compteur",
    standalone: true,
    template: `<button (click)="incrementer()">{{ valeur() }} (double : {{ double() }})</button>`,
})
export class CompteurComponent {
    initial = input<number>(0);                       // entrée typée basée sur les signaux
    valeur = signal(0);
    double = computed(() => this.valeur() * 2);
    incrementer() { this.valeur.update((v) => v + 1); }
}
```

À retenir (versions récentes) : **composants autonomes** (*standalone*, par défaut), **signaux** (`signal`, `computed`, `input()`, `output()`), `inject()`, nouvelle syntaxe de contrôle de flux (`@if`, `@for`). Mode **strict** activé par défaut dans les nouveaux projets. Les **décorateurs** d'Angular reposent sur la version « expérimentale » ([section 14](#14-décorateurs)).

## 18.4 Vue

```bash
npm create vue@latest          # choisir « TypeScript »
```

```vue
<script setup lang="ts">
import { ref, computed } from "vue";

interface Props { titre: string; compteurInitial?: number }
const props = withDefaults(defineProps<Props>(), { compteurInitial: 0 });      // props typées par une interface
const emit = defineEmits<{ (e: "change", valeur: number): void }>();

const compteur = ref<number>(props.compteurInitial);
const double = computed(() => compteur.value * 2);

function incrementer(): void {
    compteur.value++;
    emit("change", compteur.value);
}
</script>

<template>
    <button @click="incrementer">{{ titre }} : {{ compteur }} ({{ double }})</button>
</template>
```

Utilisez **`vue-tsc`** pour la vérification des types (`vue-tsc --noEmit`) et l'extension **Vue (Volar)** dans VS Code.

## 18.5 Autres frameworks

| Framework | Notes TypeScript |
| --- | --- |
| **Next.js**, **Remix / React Router**, **Astro**, **Nuxt**, **SvelteKit** | TS intégré, routes et données typées |
| **Svelte** | `<script lang="ts">`, runes typées |
| **Solid**, **Qwik**, **Lit** (composants web) | TS de premier ordre |

## 18.6 Bonnes pratiques

- Activez `strict` ; typez les **props**, **états** et **événements**.
- Dérivez les types des **données d'API** d'un schéma (OpenAPI, Zod, tRPC, GraphQL Codegen) plutôt que de les réécrire à la main.
- Ne castez pas (`as`) les réponses : **validez-les**.
- Utilisez les **unions discriminées** pour les états d'interface (`chargement | succes | erreur`).

---

# 19. TypeScript côté serveur

## 19.1 Node.js avec TypeScript

```bash
mkdir api && cd api
npm init -y
npm install express
npm install -D typescript @types/node @types/express tsx
npx tsc --init
```

### Exécuter du TypeScript

| Besoin | Outil |
| --- | --- |
| Développement avec rechargement | `tsx watch src/index.ts` · `node --watch src/index.ts` (Node récent) |
| Exécution directe sans dépendance | `node src/index.ts` (effacement des types, Node.js 22.18+/24) |
| Production | Compiler (`tsc`) puis `node dist/index.js` |
| ~~`ts-node`~~ | Moins utilisé aujourd'hui (plus lent, configuration ESM délicate) |

```json
{
    "type": "module",
    "scripts": {
        "dev": "tsx watch src/index.ts",
        "typecheck": "tsc --noEmit",
        "build": "tsc",
        "start": "node dist/index.js"
    }
}
```

## 19.2 Express (v5)

```typescript
// src/index.ts
import express, { type Request, type Response, type NextFunction } from "express";

const app = express();
app.use(express.json());

interface Utilisateur { id: number; nom: string }
const utilisateurs: Utilisateur[] = [{ id: 1, nom: "Alice" }];

// Request<Params, ResBody, ReqBody, Query>
app.get("/users/:id", (req: Request<{ id: string }>, res: Response<Utilisateur | { erreur: string }>) => {
    const u = utilisateurs.find((x) => x.id === Number(req.params.id));
    if (!u) return void res.status(404).json({ erreur: "Introuvable" });
    res.json(u);
});

app.post("/users", async (req: Request<{}, Utilisateur, { nom: string }>, res) => {
    const nouveau = { id: utilisateurs.length + 1, nom: req.body.nom };
    utilisateurs.push(nouveau);
    res.status(201).json(nouveau);
});

app.use((err: unknown, _req: Request, res: Response, _next: NextFunction) => {       // gestion d'erreurs centralisée
    console.error(err);
    res.status(500).json({ erreur: "Erreur interne" });
});

app.listen(3000, () => console.log("Serveur sur http://localhost:3000"));
```

> ℹ️ **Express 5** transmet automatiquement au gestionnaire d'erreurs les rejets des gestionnaires `async` ; avec Express 4, il fallait un enrobage ou `next(err)`.
> 💡 `req.body` n'est **pas vérifié** à l'exécution : validez-le (section 19.5).

Alternatives modernes très typées : **Fastify**, **Hono**, **Elysia**, **tRPC** (types partagés client-serveur sans génération de code).

## 19.3 NestJS

Framework **TypeScript d'abord** (architecture modulaire inspirée d'Angular : modules, contrôleurs, services, injection de dépendances).

```bash
npm i -g @nestjs/cli
nest new mon-api
```

```typescript
import { Controller, Get, Post, Body, Param, ParseIntPipe, Injectable, NotFoundException, Module } from "@nestjs/common";
import { IsString, MinLength } from "class-validator";

export class CreerUtilisateurDto {
    @IsString() @MinLength(2)
    nom!: string;
}

@Injectable()
export class UtilisateursService {
    private readonly donnees: { id: number; nom: string }[] = [];

    trouver(id: number) {
        const u = this.donnees.find((x) => x.id === id);
        if (!u) throw new NotFoundException(`Utilisateur ${id} introuvable`);
        return u;
    }
    creer(dto: CreerUtilisateurDto) {
        const u = { id: this.donnees.length + 1, ...dto };
        this.donnees.push(u);
        return u;
    }
}

@Controller("users")
export class UtilisateursController {
    constructor(private readonly service: UtilisateursService) {}       // injection de dépendances

    @Get(":id")
    un(@Param("id", ParseIntPipe) id: number) { return this.service.trouver(id); }

    @Post()
    creer(@Body() dto: CreerUtilisateurDto) { return this.service.creer(dto); }
}

@Module({ controllers: [UtilisateursController], providers: [UtilisateursService] })
export class UtilisateursModule {}
```

NestJS s'appuie sur les décorateurs **expérimentaux** et `emitDecoratorMetadata` ([section 14](#14-décorateurs)).

## 19.4 Gestion des erreurs côté serveur

```typescript
export class ErreurHttp extends Error {
    constructor(public readonly statut: number, message: string, options?: ErrorOptions) {
        super(message, options);                // ErrorOptions : { cause } (ES2022)
        this.name = new.target.name;
    }
}
export class NonTrouve extends ErreurHttp { constructor(ressource: string) { super(404, `${ressource} introuvable`); } }
export class RequeteInvalide extends ErreurHttp { constructor(detail: string) { super(400, detail); } }

app.use((err: unknown, _req: Request, res: Response, _next: NextFunction) => {
    if (err instanceof ErreurHttp) return void res.status(err.statut).json({ erreur: err.message });
    console.error(err);
    res.status(500).json({ erreur: "Erreur interne" });
});
```

## 19.5 Valider les données : types **et** exécution *(ajout)*

Les types sont **effacés** : une API qui reçoit `{ "age": "abc" }` ne plante pas à la compilation. Utilisez un **schéma** qui valide à l'exécution **et** produit le type TypeScript :

```typescript
import { z } from "zod";                          // ou Valibot, ArkType…

const CreerUtilisateur = z.object({
    nom: z.string().min(2),
    email: z.email(),
    age: z.number().int().min(0).optional(),
});
type CreerUtilisateur = z.infer<typeof CreerUtilisateur>;       // type dérivé du schéma ✅

app.post("/users", (req, res) => {
    const resultat = CreerUtilisateur.safeParse(req.body);
    if (!resultat.success) return void res.status(400).json({ erreurs: resultat.error.issues });
    const donnees: CreerUtilisateur = resultat.data;           // entièrement typé ET validé
    res.status(201).json(donnees);
});
```

Valider aussi : variables d'environnement (`process.env.X` est `string | undefined`), fichiers de configuration, réponses d'API tierces.

## 19.6 Bonnes pratiques serveur

- Séparez **routes → services → accès aux données**.
- Typez les **DTO** (entrées/sorties) et validez-les.
- Centralisez la **gestion d'erreurs** ; ne renvoyez jamais de traces de pile au client.
- Configurez `"types": ["node"]` et la bonne version de `target` / `lib`.
- Vérifiez les types **en CI** : `tsc --noEmit`.

---

# 20. Configuration du projet (`tsconfig.json`)

## 20.1 Rôle

Le fichier **`tsconfig.json`** indique la **racine du projet**, **quels fichiers** compiler et **avec quelles options**. `npx tsc --init` en génère un.

```json
{
    "compilerOptions": { /* options */ },
    "include": ["src"],
    "exclude": ["node_modules", "dist"]
}
```

## 20.2 Nouveaux défauts de TypeScript 6.0 *(à jour)*

| Option | Défaut avant | **Défaut en TS 6.0** |
| --- | --- | --- |
| `strict` | `false` | **`true`** |
| `module` | `commonjs` | **`esnext`** |
| `target` | `es5` (ancien) | **version ES de l'année (`es2025`)** |
| `types` | tous les `@types/*` auto-chargés | **`[]`** (à lister explicitement) |
| `rootDir` | racine des sources calculée | **`.`** (dossier du `tsconfig`) |
| `noUncheckedSideEffectImports` | `false` | **`true`** |
| `esModuleInterop`, `allowSyntheticDefaultImports` | `false` | **toujours `true`** (`false` déprécié) |

### Options **dépréciées** en 6.0 (et **supprimées** en 7.0)

| Option dépréciée | Remplacement |
| --- | --- |
| `target: "es5"`, `downlevelIteration` | `es2015` et plus (utilisez un transpileur si besoin) |
| `moduleResolution: "node"` (node10) et `"classic"` | `"bundler"` ou `"nodenext"` |
| `module: "amd"`, `"umd"`, `"system"`, `"none"` | `esnext` / `nodenext` + bundler |
| `baseUrl` | `paths` avec des chemins relatifs |
| `outFile` | Un bundler (Vite, esbuild…) |
| `alwaysStrict: false` | `strict` |
| Syntaxe `module Nom {}` (namespaces) | `namespace Nom {}` |
| `import … assert { type: "json" }` | `import … with { type: "json" }` |

Pour migrer progressivement : `"ignoreDeprecations": "6.0"` (⚠️ **TypeScript 7.0 ne prend plus en charge** ces options : corrigez-les avant de passer au compilateur natif).

## 20.3 Options essentielles

| Catégorie | Option | Rôle |
| --- | --- | --- |
| **Cible** | `target` | Version de JavaScript générée (`es2022`, `es2023`, `esnext`) |
| | `lib` | Bibliothèques de types disponibles (`["es2023", "dom", "dom.iterable"]`) |
| **Modules** | `module` | Système de modules : `nodenext` (Node.js), `esnext` / `preserve` (bundlers) |
| | `moduleResolution` | `nodenext` ou `bundler` |
| | `verbatimModuleSyntax` | `import type` obligatoire pour les types ✅ |
| | `isolatedModules` | Garantit la compatibilité avec Vite, esbuild, SWC, Babel |
| | `resolveJsonModule` | Importer du JSON |
| **Sorties** | `outDir`, `rootDir` | Dossiers de sortie / source |
| | `noEmit` | Ne génère rien (vérification seule) |
| | `declaration`, `declarationMap`, `sourceMap` | Déclarations et cartes sources |
| | `incremental`, `composite` | Compilation incrémentale, projets liés |
| **Rigueur** | **`strict`** | Active l'ensemble des vérifications strictes ✅ |
| | `noUncheckedIndexedAccess` | `t[i]` vaut `T \| undefined` ✅ |
| | `exactOptionalPropertyTypes` | Distingue `?:` de `\| undefined` |
| | `noImplicitOverride` | `override` obligatoire ✅ |
| | `noImplicitReturns`, `noFallthroughCasesInSwitch` | Retours et `switch` explicites |
| | `noUnusedLocals`, `noUnusedParameters` | Code mort (souvent laissé à ESLint) |
| | `erasableSyntaxOnly` | Interdit `enum`, `namespace`, propriétés de paramètres (TS 5.8) |
| **Divers** | `skipLibCheck` | Ignore la vérification des `.d.ts` des dépendances (plus rapide) |
| | `types`, `typeRoots` | Paquets de types ambiants |
| | `paths` | Alias de chemins |
| | `jsx` | `react-jsx`, `preserve`… |
| | `allowJs`, `checkJs` | Mélanger JS et TS |

### Ce que contient `strict`

`noImplicitAny`, `strictNullChecks`, `strictFunctionTypes`, `strictBindCallApply`, `strictPropertyInitialization`, `noImplicitThis`, `useUnknownInCatchVariables`, `alwaysStrict`.

## 20.4 Alias de chemins (`paths`)

```json
{
    "compilerOptions": {
        "paths": {
            "@/*": ["./src/*"],
            "@composants/*": ["./src/composants/*"]
        }
    }
}
```

```typescript
import { Bouton } from "@composants/Bouton";
```

> ⚠️ `paths` n'affecte **que la vérification des types** : le chemin doit aussi être résolu à l'**exécution** (alias de **Vite**/**webpack**, `tsx`, ou **`imports` de `package.json`**, standard Node.js). Depuis TS 6.0, `baseUrl` est **déprécié** : les chemins de `paths` sont relatifs au `tsconfig.json`.

```json
// package.json — alias natifs de Node.js, reconnus par TypeScript
{ "imports": { "#utils/*": "./src/utils/*.js" } }
```

## 20.5 Résolution des modules

| `moduleResolution` | Quand l'utiliser |
| --- | --- |
| **`nodenext`** | Applications / bibliothèques **Node.js** (ESM et CommonJS) : extensions obligatoires dans les imports relatifs |
| **`bundler`** | Code empaqueté par **Vite, webpack, esbuild…** : imports sans extension, `exports` du `package.json` |
| ~~`node` / `node10`~~ | **Déprécié** |
| ~~`classic`~~ | **Déprécié** |

## 20.6 Configurations types

### Application Node.js

```json
{
    "compilerOptions": {
        "target": "es2023",
        "lib": ["es2023"],
        "module": "nodenext",
        "types": ["node"],
        "outDir": "dist",
        "rootDir": "src",
        "strict": true,
        "noUncheckedIndexedAccess": true,
        "noImplicitOverride": true,
        "verbatimModuleSyntax": true,
        "isolatedModules": true,
        "skipLibCheck": true,
        "sourceMap": true
    },
    "include": ["src"]
}
```

### Application front-end (Vite)

```json
{
    "compilerOptions": {
        "target": "es2023",
        "lib": ["es2023", "dom", "dom.iterable"],
        "module": "esnext",
        "moduleResolution": "bundler",
        "jsx": "react-jsx",
        "types": ["vite/client"],
        "noEmit": true,
        "strict": true,
        "noUncheckedIndexedAccess": true,
        "verbatimModuleSyntax": true,
        "isolatedModules": true,
        "skipLibCheck": true,
        "paths": { "@/*": ["./src/*"] }
    },
    "include": ["src"]
}
```

## 20.7 Héritage et projets multiples

```json
// tsconfig.base.json
{ "compilerOptions": { "strict": true, "skipLibCheck": true } }

// tsconfig.json
{ "extends": "./tsconfig.base.json", "compilerOptions": { "outDir": "dist" }, "include": ["src"] }
```

Les **références de projets** (`"references": [{ "path": "../lib" }]`, `"composite": true`, `tsc -b`) accélèrent les **monorepos**. Des bases prêtes à l'emploi existent : `@tsconfig/node24`, `@tsconfig/strictest`, `@tsconfig/recommended`.

## 20.8 Erreurs fréquentes

| Problème | Solution |
| --- | --- |
| *Cannot find module* / types de Node introuvables | Ajouter `@types/node` **et** `"types": ["node"]` (TS 6+) |
| Imports relatifs en erreur avec `nodenext` | Ajouter l'extension `.js` |
| `import x from "cjs"` sans valeur par défaut | `esModuleInterop` (toujours actif en 6.0) |
| Alias `@/…` résolu par TS mais pas à l'exécution | Configurer le bundler / `imports` |
| Vite compile, mais `tsc` échoue | Normal : Vite ne vérifie pas ; corrigez les erreurs de type |
| `"moduleResolution": "node"` : option dépréciée | Passer à `bundler` / `nodenext` |
| Erreur **TS5112** avec `tsc fichier.ts` | Un `tsconfig.json` est présent : utilisez `tsc -p .` ou `--ignoreConfig` |
| Erreurs *« Option … has been removed »* avec TS 7 | Retirer / remplacer l'option dépréciée en 6.0 (voir 20.2) |
| Beaucoup d'erreurs après la mise à jour vers TS 6 | `strict` est maintenant actif : corriger, ou `"strict": false` temporairement |

## 20.9 TypeScript 7 et le compilateur natif *(à jour)*

- Même **commande `tsc`**, mêmes types, mais un compilateur écrit en **Go** : **plusieurs fois plus rapide**, avec un **vérificateur parallèle**.
- Il **ne supporte pas** les options dépréciées en 6.0 ni l'ancienne **API de compilateur** JavaScript (« Strada ») : les outils qui l'utilisent (certaines règles ESLint avec types, générateurs de code, plugins) doivent s'adapter ; gardez TypeScript 6 installé en parallèle si besoin.
- Le service de langage (VS Code, Visual Studio…) bénéficie du même gain : complétion et diagnostics plus réactifs sur les gros projets.

---

# 21. Linting et formatage

## 21.1 Pourquoi ?

| Outil | Rôle |
| --- | --- |
| **Compilateur** (`tsc`) | Vérifie les **types** |
| **Linter** (ESLint + typescript-eslint) | Détecte les **mauvaises pratiques** et bugs probables |
| **Formateur** (Prettier, Biome) | Impose un **style** uniforme |

> 📌 **TSLint est abandonné** depuis 2019 : utilisez **typescript-eslint**.

## 21.2 ESLint avec typescript-eslint (configuration « flat »)

```bash
npm install -D eslint @eslint/js typescript-eslint
```

```javascript
// eslint.config.mjs
import eslint from "@eslint/js";
import tseslint from "typescript-eslint";

export default tseslint.config(
    { ignores: ["dist/", "coverage/"] },
    eslint.configs.recommended,
    tseslint.configs.strictTypeChecked,           // règles « avec types » (plus puissantes)
    tseslint.configs.stylisticTypeChecked,
    {
        languageOptions: {
            parserOptions: { projectService: true, tsconfigRootDir: import.meta.dirname },
        },
        rules: {
            "@typescript-eslint/no-explicit-any": "error",
            "@typescript-eslint/no-floating-promises": "error",
            "@typescript-eslint/consistent-type-imports": "error",
            "@typescript-eslint/no-unused-vars": ["error", { argsIgnorePattern: "^_" }],
        },
    },
    { files: ["**/*.mjs", "**/*.js"], extends: [tseslint.configs.disableTypeChecked] },
);
```

> ℹ️ Les anciens fichiers `.eslintrc.*` sont **remplacés** par le format « flat » `eslint.config.*` (par défaut depuis ESLint 9).

```json
{ "scripts": { "lint": "eslint .", "lint:fix": "eslint . --fix" } }
```

### Règles à retenir

| Règle | Intérêt |
| --- | --- |
| `no-explicit-any`, `no-unsafe-*` | Éviter la contagion de `any` |
| `no-floating-promises`, `no-misused-promises` | Promesses non traitées |
| `consistent-type-imports` | `import type` |
| `switch-exhaustiveness-check` | Exhaustivité des `switch` |
| `no-unnecessary-condition` | Conditions toujours vraies/fausses |
| `strict-boolean-expressions` | Conditions explicites |

## 21.3 Prettier

```bash
npm install -D prettier eslint-config-prettier
```

```json
// .prettierrc
{ "semi": true, "singleQuote": false, "trailingComma": "all", "printWidth": 100, "tabWidth": 4 }
```

```json
{ "scripts": { "format": "prettier --write .", "format:check": "prettier --check ." } }
```

Avant / après :

```typescript
// Avant
function addition(a:number,b:number){return a+b}
const utilisateur={nom:"Alice",age:30,email:"alice@exemple.com",roles:["admin","editeur"],actif:true}

// Après
function addition(a: number, b: number) {
    return a + b;
}
const utilisateur = {
    nom: "Alice",
    age: 30,
    email: "alice@exemple.com",
    roles: ["admin", "editeur"],
    actif: true,
};
```

> ✅ **ESLint** s'occupe de la **qualité**, **Prettier** du **formatage** : ajoutez `eslint-config-prettier` pour éviter les conflits entre les deux.

## 21.4 Alternative tout-en-un : Biome

**Biome** (écrit en Rust) remplace ESLint **et** Prettier dans un seul outil, très rapide ; ses règles « avec types » sont moins complètes que celles de typescript-eslint.

```bash
npm install -D --save-exact @biomejs/biome
npx biome init && npx biome check --write .
```

## 21.5 Intégration à l'éditeur et à la CI

```json
// .vscode/settings.json
{
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.codeActionsOnSave": { "source.fixAll.eslint": "explicit" },
    "typescript.tsdk": "node_modules/typescript/lib"
}
```

```json
{ "scripts": { "verifier": "tsc --noEmit && eslint . && prettier --check ." } }
```

**Hooks Git** : `lint-staged` + `husky` (ou `lefthook`) exécutent lint et format uniquement sur les fichiers modifiés avant chaque commit.

## 21.6 Organisation type d'un projet

```text
mon-projet/
├── src/
├── tests/
├── .vscode/settings.json
├── eslint.config.mjs
├── .prettierrc
├── .editorconfig
├── tsconfig.json
└── package.json
```

---

# ⭐ Bonus

---

# 22. TypeScript et bases de données

## 22.1 Principes

- Typez les **modèles** (entités) **et** les **résultats de requêtes**.
- Les types TypeScript **ne vérifient pas** ce que renvoie la base : préférez des outils qui **génèrent les types depuis le schéma** (Prisma, Drizzle, Kysely, générateurs SQL) ou validez les lignes (Zod).
- Utilisez toujours des **requêtes paramétrées** (anti-injection SQL).

## 22.2 PostgreSQL avec `pg`

```bash
npm install pg
npm install -D @types/pg
```

```typescript
import { Pool } from "pg";

const pool = new Pool({ connectionString: process.env.DATABASE_URL });

interface Utilisateur { id: number; nom: string; email: string }

export async function trouverParEmail(email: string): Promise<Utilisateur | undefined> {
    const { rows } = await pool.query<Utilisateur>(
        "SELECT id, nom, email FROM utilisateurs WHERE email = $1",     // paramètre lié : jamais de concaténation
        [email],
    );
    return rows[0];
}

export async function creer(nom: string, email: string): Promise<Utilisateur> {
    const { rows } = await pool.query<Utilisateur>(
        "INSERT INTO utilisateurs (nom, email) VALUES ($1, $2) RETURNING id, nom, email",
        [nom, email],
    );
    return rows[0]!;
}

// Transaction
const client = await pool.connect();
try {
    await client.query("BEGIN");
    // … requêtes …
    await client.query("COMMIT");
} catch (e) {
    await client.query("ROLLBACK");
    throw e;
} finally {
    client.release();
}
```

## 22.3 MongoDB

### Pilote officiel

```typescript
import { MongoClient, ObjectId, type Collection } from "mongodb";

interface Article {
    _id?: ObjectId;
    titre: string;
    tags: string[];
    publieLe: Date;
}

const client = new MongoClient(process.env.MONGODB_URI!);
await client.connect();
const articles: Collection<Article> = client.db("blog").collection<Article>("articles");

await articles.insertOne({ titre: "Hello", tags: ["ts"], publieLe: new Date() });
const recents = await articles.find({ tags: "ts" }).sort({ publieLe: -1 }).limit(10).toArray();    // Article[] (typé)
```

### Mongoose

```typescript
import { Schema, model, type InferSchemaType } from "mongoose";

const schemaUtilisateur = new Schema({
    nom: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    creeLe: { type: Date, default: Date.now },
});

type IUtilisateur = InferSchemaType<typeof schemaUtilisateur>;         // type déduit du schéma
const Utilisateur = model("Utilisateur", schemaUtilisateur);

const u = await Utilisateur.create({ nom: "Alice", email: "alice@exemple.com" });
const trouve = await Utilisateur.findOne({ email: "alice@exemple.com" }).lean();
```

## 22.4 ORM et constructeurs de requêtes

| Outil | Approche | Points forts |
| --- | --- | --- |
| **Prisma** | Schéma `schema.prisma` → **client généré** et typé | Excellente expérience développeur, migrations |
| **Drizzle ORM** | Schéma en **TypeScript**, requêtes proches du SQL | Léger, types précis, sans génération |
| **Kysely** | **Constructeur de requêtes** typé | Contrôle SQL total |
| **TypeORM** | Entités avec **décorateurs** | Très répandu, intégré à NestJS |
| **MikroORM**, **Sequelize**, **Objection** | Alternatives | |

### Prisma (exemple)

```prisma
// prisma/schema.prisma
model Utilisateur {
  id       Int      @id @default(autoincrement())
  email    String   @unique
  nom      String
  articles Article[]
}
model Article {
  id       Int         @id @default(autoincrement())
  titre    String
  auteur   Utilisateur @relation(fields: [auteurId], references: [id])
  auteurId Int
}
```

```typescript
import { PrismaClient } from "@prisma/client";
const prisma = new PrismaClient();

const u = await prisma.utilisateur.create({ data: { email: "a@b.fr", nom: "Alice" } });
const avecArticles = await prisma.utilisateur.findUnique({
    where: { email: "a@b.fr" },
    include: { articles: true },          // le type du résultat inclut `articles`
});
```

### Drizzle (exemple)

```typescript
import { pgTable, serial, text } from "drizzle-orm/pg-core";
import { drizzle } from "drizzle-orm/node-postgres";
import { eq } from "drizzle-orm";

export const utilisateurs = pgTable("utilisateurs", {
    id: serial("id").primaryKey(),
    nom: text("nom").notNull(),
    email: text("email").notNull().unique(),
});
type Utilisateur = typeof utilisateurs.$inferSelect;          // type déduit du schéma
type NouvelUtilisateur = typeof utilisateurs.$inferInsert;

const db = drizzle(process.env.DATABASE_URL!);
const u: Utilisateur[] = await db.select().from(utilisateurs).where(eq(utilisateurs.email, "a@b.fr"));
```

### TypeORM (exemple)

```typescript
import { Entity, PrimaryGeneratedColumn, Column, OneToMany, DataSource } from "typeorm";

@Entity()
export class Utilisateur {
    @PrimaryGeneratedColumn() id!: number;
    @Column() nom!: string;
    @Column({ unique: true }) email!: string;
}

const source = new DataSource({ type: "postgres", url: process.env.DATABASE_URL, entities: [Utilisateur], synchronize: false });
await source.initialize();
const depot = source.getRepository(Utilisateur);
const u = await depot.findOneBy({ email: "a@b.fr" });
```

TypeORM exige les décorateurs **expérimentaux** (`experimentalDecorators`, `emitDecoratorMetadata`) et `strictPropertyInitialization` impose l'opérateur `!` sur les colonnes.

## 22.5 Motif « dépôt » (*repository*) pour découpler

```typescript
interface DepotUtilisateurs {
    trouverParId(id: number): Promise<Utilisateur | undefined>;
    creer(donnees: Omit<Utilisateur, "id">): Promise<Utilisateur>;
}
// Implémentations : PostgresDepot, MemoireDepot (pour les tests)…
```

## 22.6 Bonnes pratiques

- **Migrations versionnées** (Prisma Migrate, Drizzle Kit, Flyway…).
- **Variables d'environnement** pour les URL de connexion (jamais dans le dépôt).
- **Pool de connexions**, transactions pour les opérations multiples, index adaptés.
- Ne renvoyez jamais directement les entités avec des champs sensibles (`Omit<…, "motDePasseHache">`).

---

# 23. TypeScript et tests

## 23.1 Choisir un outil de test

| Outil | Points forts |
| --- | --- |
| **Vitest** ✅ | Très rapide, TypeScript et ESM **natifs**, API compatible Jest, intégré à Vite |
| **Jest** | Très répandu ; nécessite un transformateur (`ts-jest`, `@swc/jest` ou Babel) |
| **`node:test`** | Exécuteur **intégré à Node.js**, sans dépendance |
| **Mocha** (+ Chai, Sinon) | Flexible, modulaire |
| **Playwright**, **Cypress** | Tests de bout en bout (E2E) |

## 23.2 Vitest

```bash
npm install -D vitest
```

```typescript
// src/calculatrice.ts
export function diviser(a: number, b: number): number {
    if (b === 0) throw new RangeError("Division par zéro");
    return a / b;
}
```

```typescript
// src/calculatrice.test.ts
import { describe, it, expect, vi, beforeEach } from "vitest";
import { diviser } from "./calculatrice.js";

describe("diviser", () => {
    it("divise deux nombres", () => {
        expect(diviser(10, 2)).toBe(5);
    });

    it("lève une erreur en cas de division par zéro", () => {
        expect(() => diviser(1, 0)).toThrow(RangeError);
    });

    it.each([[4, 2, 2], [9, 3, 3], [-6, 3, -2]])("diviser(%i, %i) = %i", (a, b, attendu) => {
        expect(diviser(a, b)).toBe(attendu);
    });
});
```

```json
{ "scripts": { "test": "vitest", "test:ci": "vitest run --coverage" } }
```

## 23.3 Jest avec TypeScript

```bash
npm install -D jest @types/jest ts-jest
npx ts-jest config:init
```

```javascript
// jest.config.js
export default { preset: "ts-jest", testEnvironment: "node", testMatch: ["**/*.test.ts"] };
```

L'API (`describe`, `it`, `expect`, `jest.fn()`, `jest.mock()`) est quasi identique ; avec TypeScript 6, ajoutez `"types": ["jest"]` dans le `tsconfig`.

## 23.4 Mocha + Chai

```bash
npm install -D mocha chai tsx @types/mocha @types/chai
```

```typescript
import { expect } from "chai";
import { diviser } from "../src/calculatrice.js";

describe("diviser", () => {
    it("divise", () => { expect(diviser(10, 2)).to.equal(5); });
    it("lève une erreur", () => { expect(() => diviser(1, 0)).to.throw(RangeError); });
});
```

```bash
mocha --import=tsx "tests/**/*.test.ts"
```

## 23.5 Tester les types

Les **types** aussi se testent :

```typescript
import { expectTypeOf, test } from "vitest";

test("types de l'utilitaire", () => {
    expectTypeOf<PartielProfond<{ a: { b: number } }>>().toEqualTypeOf<{ a?: { b?: number } }>();
    expectTypeOf(diviser).parameters.toEqualTypeOf<[number, number]>();
    expectTypeOf(diviser).returns.toBeNumber();
});

// @ts-expect-error : vérifie qu'une erreur de compilation est bien levée
diviser("a", 1);
```

Alternatives : **tsd**, `tsc --noEmit` sur des fichiers `*.test-d.ts`.

## 23.6 Doublures : mocks, stubs, espions

```typescript
import { vi, expect, it } from "vitest";

interface Mailer { envoyer(destinataire: string, sujet: string): Promise<boolean> }

class Inscription {
    constructor(private readonly mailer: Mailer) {}
    async inscrire(email: string) { return this.mailer.envoyer(email, "Bienvenue"); }
}

it("envoie un e-mail de bienvenue", async () => {
    const mailer: Mailer = { envoyer: vi.fn().mockResolvedValue(true) };       // doublure typée par l'interface
    const inscription = new Inscription(mailer);

    expect(await inscription.inscrire("alice@exemple.com")).toBe(true);
    expect(mailer.envoyer).toHaveBeenCalledWith("alice@exemple.com", "Bienvenue");
    expect(mailer.envoyer).toHaveBeenCalledTimes(1);
});
```

| Doublure | Rôle |
| --- | --- |
| **Stub** | Renvoie des valeurs prédéfinies (`mockReturnValue`, `mockResolvedValue`) |
| **Mock** | Vérifie les appels (`toHaveBeenCalledWith`) |
| **Spy** (`vi.spyOn`) | Observe une méthode réelle sans la remplacer |
| **Fake** | Implémentation simplifiée (ex. dépôt en mémoire) |

```typescript
vi.mock("./api.js", () => ({ charger: vi.fn().mockResolvedValue({ id: 1 }) }));       // module entier
vi.useFakeTimers();                                                                    // horloge simulée
```

Outils complémentaires : **MSW** (simuler l'API réseau), `sinon`, `ts-mockito`, `jest-mock-extended`.

## 23.7 Sécurité des types dans les tests

- Programmez **vers des interfaces** et injectez les dépendances : les doublures restent **vérifiées** par le compilateur.
- Évitez `as any` ; préférez `Partial<T>` + une assertion limitée, ou un utilitaire de fabrique de données :

```typescript
function faireUtilisateur(surcharges: Partial<Utilisateur> = {}): Utilisateur {
    return { id: 1, nom: "Alice", email: "alice@exemple.com", ...surcharges };
}
```

- Incluez les tests dans la vérification de types (`tsc --noEmit`) ; ajoutez `"types": ["vitest/globals"]` si vous utilisez les API globales.

## 23.8 Bonnes pratiques

- **Arrange – Act – Assert**, un comportement par test, noms explicites.
- Testez les **cas limites** et les **erreurs**.
- Pas de réseau ni de base réelle dans les tests unitaires ; des **tests d'intégration** séparés (conteneurs de test).
- Visez une couverture **utile** (pas 100 % à tout prix) et exécutez les tests en **CI**.

---

# 24. Nouveautés par version et bonnes pratiques

## 24.1 Chronologie des fonctionnalités

| Version | À retenir |
| --- | --- |
| **4.1** | Types littéraux de gabarit, remappage de clés (`as`) dans les types mappés |
| **4.3–4.4** | `override`, signatures d'index pour les symboles, analyse de flux contrôlée |
| **4.9** | **`satisfies`**, mot-clé `accessor` |
| **5.0** | **Décorateurs standard**, paramètres de type **`const`**, `verbatimModuleSyntax`, `enum` unifiés |
| **5.2** | Déclarations **`using`** / `await using` (gestion de ressources) |
| **5.4** | **`NoInfer`**, meilleure restriction dans les fermetures |
| **5.5** | **Prédicats de type inférés**, `isolatedDeclarations`, vérification des regex |
| **5.7–5.8** | `--rewriteRelativeImportExtensions`, **`--erasableSyntaxOnly`**, support de `require()` d'ESM |
| **6.0** (mars 2026) | **Version passerelle** : `strict` par défaut, `module: esnext`, `types: []`, `target` ES2025 ; nombreuses **dépréciations** ; types de **Temporal** et des API ES récentes (`Promise.try`, méthodes de `Set`…) |
| **7.0** (juillet 2026) | **Compilateur natif (Go)** : vitesse, parallélisme ; options dépréciées supprimées |

## 24.2 Gestion de ressources : `using` *(TS 5.2, ajout)*

```typescript
class Connexion implements Disposable {
    [Symbol.dispose]() { console.log("Connexion fermée"); }
}

function travailler() {
    using connexion = new Connexion();      // libérée automatiquement à la sortie du bloc
    // …
}
```

(Nécessite un runtime qui prend en charge `Symbol.dispose` ou un *polyfill*.)

## 24.3 Bonnes pratiques

| Pratique | Pourquoi |
| --- | --- |
| **`strict: true`** (désormais par défaut) + `noUncheckedIndexedAccess` + `noImplicitOverride` | Capture un maximum d'erreurs |
| **`unknown`** plutôt que `any` ; restreindre avant usage | Sécurité |
| **Unions discriminées** pour modéliser des états | Pas d'états impossibles |
| Préférer **`interface`** pour les formes d'objets, **`type`** pour le reste | Cohérence |
| **Unions de littéraux / `as const`** plutôt qu'`enum` | Moins de code généré, compatibilité effaçable |
| **`import type`** + `verbatimModuleSyntax` | Imports prévisibles |
| **Valider les données externes** (Zod, Valibot) | Les types disparaissent à l'exécution |
| Typer **entrées et sorties** des fonctions publiques | Contrats clairs |
| Éviter les assertions `as` et `!` | Elles contournent le compilateur |
| `tsc --noEmit` **en CI** | Vite, esbuild et `tsx` ne vérifient pas les types |
| Garder TypeScript et `@types/*` **à jour** | Corrections et nouvelles fonctionnalités |

## 24.4 Ressources

- 📘 **Documentation officielle** : <https://www.typescriptlang.org/docs/>
- 📗 **TypeScript Handbook** et **notes de version** : <https://www.typescriptlang.org/docs/handbook/release-notes/overview.html>
- 🧪 **Playground** : <https://www.typescriptlang.org/play>
- 📙 **Type Challenges** (exercices de types) : <https://github.com/type-challenges/type-challenges>
- 🧰 **DefinitelyTyped** : <https://github.com/DefinitelyTyped/DefinitelyTyped>
- 🛠️ **typescript-eslint** : <https://typescript-eslint.io>
- 📕 *Effective TypeScript* — Dan Vanderkam

---

<div align="center">

*Bon code, et que vos types soient toujours justes ! 🔷*

</div>
