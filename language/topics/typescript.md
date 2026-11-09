# TypeScript — Cours complet

*Du premier type aux génériques, aux frameworks et à la configuration moderne — édition octobre 2026 (TypeScript 6.0 / 7.0)*

**Auteur du plan : guide d'origine · Rédaction du contenu : module d'apprentissage exhaustif**

## Comment utiliser ce cours

Ce document développe, section par section, le plan du guide TypeScript fourni. Il est organisé en trois niveaux (débutant, intermédiaire, avancé) et un bloc bonus. Chaque module suit la même structure : **objectifs**, **cours détaillé** avec définitions et exemples commentés, **pièges courants** et **points clés**.

Conventions : les blocs de code sont autonomes ; les lignes marquées `// ERREUR` ne compilent volontairement pas ; les commentaires expliquent le type inféré.

**Prérequis** : connaître les bases de JavaScript (variables, fonctions, objets, tableaux, classes, promesses). Aucun prérequis en typage.

---

# NIVEAU DÉBUTANT

---

# 1. Introduction à TypeScript

**Objectifs** : comprendre ce qu'est TypeScript, pourquoi il existe, comment il s'installe, se compile et s'exécute, et où il en est en 2026.

## 1.1 Qu'est-ce que TypeScript ?

**TypeScript (TS)** est un langage de programmation développé par Microsoft (équipe d'Anders Hejlsberg, première version publique en 2012). C'est un **sur-ensemble syntaxique et typé de JavaScript** : tout programme JavaScript valide est un programme TypeScript valide, et TypeScript y ajoute :

- un **système de types statiques** (vérifiés avant l'exécution) ;
- des constructions supplémentaires (interfaces, génériques, enums, modificateurs d'accès…) ;
- un **service de langage** qui alimente les éditeurs (autocomplétion, navigation, refactorisation).

**Définitions essentielles**

- **Typage statique** : le type de chaque expression est déterminé et vérifié à la compilation, sans exécuter le programme. À l'opposé, le **typage dynamique** (JavaScript) vérifie les types pendant l'exécution.
- **Compilation (transpilation)** : traduction du code `.ts` en code `.js`. On parle de *transpilation* car la source et la cible sont deux langages de même niveau.
- **Effacement des types** (*type erasure*) : les annotations de types sont **supprimées** du JavaScript généré. À l'exécution, il ne reste aucune trace des types.

```text
code .ts → vérification des types → suppression des types → code .js → exécution
            (erreurs à la compilation)                        (navigateur, Node.js…)
```

**Conséquence capitale** : TypeScript garantit la cohérence **interne** de votre code, pas la forme des données qui entrent à l'exécution (réponse d'API, saisie utilisateur, fichier JSON). Pour cela, il faut une **validation à l'exécution** (voir module 19).

### Le typage structurel

TypeScript est **structurel** (et non nominal) : deux types sont compatibles si leurs **formes** sont compatibles, indépendamment de leur nom ou de leur origine. C'est le *duck typing* vérifié statiquement : « si ça a un `nom` de type `string`, ça convient ».

```typescript
interface Nommable { nom: string }

function saluer(x: Nommable) { return 'Salut ' + x.nom; }

const chien = { nom: 'Rex', race: 'Labrador' };
saluer(chien); // OK : chien possède (au moins) la propriété nom
```

## 1.2 Pourquoi utiliser TypeScript ?

| Avantage | Explication détaillée |
| --- | --- |
| **Détection précoce des erreurs** | Fautes de frappe, arguments manquants, `undefined is not a function` sont signalés dans l'éditeur, avant toute exécution |
| **Autocomplétion et documentation** | L'éditeur connaît la forme de chaque objet et propose les membres valides, avec leur documentation |
| **Code auto-documenté** | La signature `(id: number) => Promise<Utilisateur>` est un contrat lisible et vérifié |
| **Refactorisation sûre** | Renommer ou modifier une signature fait apparaître tous les appels à corriger |
| **Travail en équipe** | Les types servent de spécification partagée entre développeurs et entre modules |
| **Adoption progressive** | On peut migrer un projet JavaScript fichier par fichier (`allowJs`, `checkJs`) |
| **Écosystème** | Des milliers de bibliothèques fournissent leurs types ; les frameworks majeurs (Angular, NestJS, Vue 3, etc.) sont écrits en TypeScript |

**Limites à connaître** : une étape de vérification supplémentaire, une courbe d'apprentissage pour les types avancés, et l'absence de garantie à l'exécution sur les données externes.

## 1.3 L'état de TypeScript en 2026

| Version | Date | Points marquants |
| --- | --- | --- |
| **5.x** | 2023–2025 | Décorateurs standard (5.0), `satisfies` (4.9), `using` (5.2), `NoInfer` (5.4), prédicats de type inférés (5.5), `--erasableSyntaxOnly` (5.8) |
| **6.0** | mars 2026 | Dernière version basée sur le code JavaScript ; « version passerelle » avec **nouveaux défauts** (`strict: true`, `module: esnext`, `types: []`) et de nombreuses **dépréciations** |
| **7.0** | juillet 2026 | **Compilateur natif écrit en Go** (projet *Corsa*) : vérification parallèle, beaucoup plus rapide, moins gourmand en mémoire ; **n'accepte plus** les options dépréciées en 6.0 |

Ce qu'il faut en retenir :

1. Le **langage** (la syntaxe des types) reste stable : ce que vous apprenez ici est valable pour toutes ces versions.
2. La **configuration** change : défauts plus stricts, options historiques supprimées (module 20).
3. La commande reste **`tsc`**.

## 1.4 Installer TypeScript

Prérequis : **Node.js** (version LTS récente) et un gestionnaire de paquets (npm, pnpm, yarn ou bun).

```bash
node --version
npm install -D typescript      # installation locale au projet (recommandée)
npx tsc --version
```

**Pourquoi une installation locale ?** Chaque projet épingle sa version dans `package.json` : développeurs et intégration continue utilisent exactement le même compilateur. Une installation globale (`npm i -g typescript`) provoque des écarts de version entre machines.

Avec TypeScript 7, le compilateur natif est livré dans le paquet `typescript` lui-même (il a remplacé l'aperçu `@typescript/native-preview`, commande `tsgo`) :

```bash
npm install -D typescript@latest
npx tsc -p .
```

## 1.5 Écrire, compiler et exécuter un premier fichier

```typescript
// bonjour.ts
function saluer(nom: string): string {
    return `Bonjour, ${nom} !`;
}

console.log(saluer('Alice'));
// saluer(42); // ERREUR : 'number' n'est pas assignable au paramètre de type 'string'
```

**Les différentes façons de faire tourner du TypeScript**

| Méthode | Commande | Usage |
| --- | --- | --- |
| Compiler le projet | `npx tsc` ou `npx tsc -p .` | Production, bibliothèques |
| Vérifier seulement | `npx tsc --noEmit` | CI, éditeur : valide les types sans rien générer |
| Mode surveillance | `npx tsc --watch` | Développement |
| Exécution native Node.js | `node bonjour.ts` (Node 22.18+ / 24) | Scripts, serveurs simples |
| Exécuteur `tsx` | `npx tsx bonjour.ts` | Scripts et développement |
| Deno / Bun | `deno run bonjour.ts` / `bun bonjour.ts` | Exécutent TS nativement |

**Point d'attention majeur** : les exécuteurs directs (Node.js, `tsx`, Bun, esbuild, Vite, SWC) **suppriment les types sans les vérifier**. Seul `tsc` (ou `vue-tsc`, etc.) vérifie réellement. Dans tout projet sérieux, on lance `tsc --noEmit` en parallèle (script `typecheck`) et en intégration continue.

**Depuis TypeScript 6/7** : si un `tsconfig.json` existe, `tsc fichier.ts` échoue avec l'erreur **TS5112** (la configuration serait ignorée silencieusement). Utilisez `tsc -p .`, ou `tsc --ignoreConfig fichier.ts` pour compiler un fichier isolé avec les options par défaut.

**Mode « effaçable »** : l'option `--erasableSyntaxOnly` (TS 5.8) interdit les syntaxes qui produisent du code JavaScript (`enum`, `namespace`, propriétés de paramètres de constructeur), afin que le code reste exécutable par simple effacement de types.

## 1.6 Démarrer un projet

```bash
mkdir mon-projet && cd mon-projet
npm init -y
npm install -D typescript @types/node
npx tsc --init      # génère un tsconfig.json commenté
```

```text
mon-projet/
├── src/
│   └── index.ts
├── dist/            ← sortie compilée (ignorée par Git)
├── package.json
└── tsconfig.json
```

Le module 20 détaille le `tsconfig.json`.

## 1.7 Les outils du quotidien

| Outil | Rôle |
| --- | --- |
| **VS Code** | Support TypeScript natif, le plus complet |
| **TypeScript Playground** | Essayer du code en ligne, voir le JavaScript généré |
| **tsx, Node.js, Bun, Deno** | Exécuter du TS |
| **Vite, esbuild, SWC** | Compiler et empaqueter (sans vérification) |
| **typescript-eslint, Prettier, Biome** | Qualité et formatage |
| **Vitest, Jest** | Tests |

## Points clés du module 1

- TypeScript = JavaScript + types statiques ; les types **disparaissent** à l'exécution.
- Typage **structurel** : la forme compte, pas le nom.
- `tsc --noEmit` vérifie ; les autres outils exécutent ou empaquettent.
- TS 6 a durci les défauts ; TS 7 est le compilateur natif en Go.

---

# 2. Types de base

**Objectifs** : maîtriser les types primitifs, l'inférence, les types spéciaux (`any`, `unknown`, `void`, `never`), la gestion de `null`/`undefined`, les assertions, `as const` et `satisfies`.

## 2.1 Les types primitifs

JavaScript possède sept types primitifs ; TypeScript les nomme en **minuscules** :

```typescript
let nom: string = 'Alice';
let age: number = 30;                  // entiers, flottants, NaN, Infinity
let actif: boolean = true;
let grand: bigint = 9007199254740993n; // entiers de taille arbitraire
let id: symbol = Symbol('id');         // identifiant unique
let rien: null = null;
let indefini: undefined = undefined;
```

**Règle** : n'utilisez jamais `String`, `Number`, `Boolean`, `Object` (majuscules). Ce sont les **objets enveloppes** de JavaScript, presque jamais voulus, et `Object` accepte presque toute valeur.

`number` ne distingue pas entier et flottant. Pour les entiers de grande taille (identifiants 64 bits), utilisez `bigint`, **non mélangeable** avec `number` dans une opération arithmétique.

## 2.2 L'inférence de types

TypeScript **déduit** les types à partir des valeurs. Annoter partout est inutile et alourdit le code.

```typescript
let ville = 'Paris';          // string
const pi = 3.14;              // 3.14 (type littéral : const ne peut pas changer)
let nombres = [1, 2, 3];      // number[]
const personne = { nom: 'Alice', age: 30 }; // { nom: string; age: number }

// ville = 42; // ERREUR : 'number' n'est pas assignable à 'string'
```

**Élargissement (*widening*)** : un `let` reçoit le type général (`string`), un `const` le type littéral le plus précis (`'Paris'`), car la valeur ne peut plus changer.

| Quand annoter ? | Exemple |
| --- | --- |
| Paramètres de fonction (toujours) | `(a: number, b: number)` |
| Variable sans valeur initiale | `let total: number;` |
| Retour des fonctions exportées | `function f(): string` |
| Quand l'inférence est trop large ou étroite | `let x: string \| null = null;` |

## 2.3 Les types spéciaux

### `any` : l'échappatoire (à éviter)

`any` **désactive** la vérification : on peut tout faire avec, et il se propage (« contamination »). C'est un retour au JavaScript non typé.

```typescript
let x: any = 'texte';
x = 42;
x.nimporteQuoi(); // accepté à la compilation, plante à l'exécution
```

### `unknown` : la version sûre

On peut y ranger n'importe quoi, mais on ne peut **rien en faire** avant de l'avoir **restreint** (*narrowing*).

```typescript
function traiter(valeur: unknown) {
    // valeur.toUpperCase(); // ERREUR : valeur est de type 'unknown'
    if (typeof valeur === 'string') {
        console.log(valeur.toUpperCase()); // OK : restreint à string
    }
}
```

Règle : pour toute donnée dont le type n'est pas connu (résultat de `JSON.parse`, entrée utilisateur, erreur attrapée), utilisez **`unknown`**, pas `any`.

### `void`, `never`, `object`, `{}`

```typescript
function journaliser(msg: string): void { console.log(msg); }   // ne retourne rien d'utile
function echouer(msg: string): never { throw new Error(msg); }  // ne retourne JAMAIS
function boucle(): never { while (true) {} }

let obj: object = { a: 1 }; // tout non-primitif
let q: {} = 5;               // tout sauf null et undefined
```

| Type | Signification | Usage typique |
| --- | --- | --- |
| `any` | Aucune vérification | Migration, dernier recours |
| `unknown` | Valeur inconnue, à restreindre | Données externes, `catch` |
| `void` | Absence de valeur de retour | Fonctions à effet de bord |
| `never` | Valeur impossible | Erreurs, boucles infinies, exhaustivité |

`never` est aussi le **type vide** : une union où l'on a tout éliminé devient `never`, d'où son rôle dans les vérifications d'exhaustivité (3.7).

Activez `noImplicitAny` (inclus dans `strict`) : TypeScript refuse alors les `any` implicites.

## 2.4 `null` et `undefined` en mode strict

Avec `strictNullChecks` (inclus dans `strict`, **activé par défaut depuis TS 6.0**), `null` et `undefined` ne sont **pas** assignables aux autres types. Cela supprime la célèbre « erreur à un milliard de dollars » (déréférencer `null`).

```typescript
// let nom: string = null; // ERREUR
let nomOuNull: string | null = null; // « peut être nul » devient explicite

function longueur(s: string | null): number {
    return s?.length ?? 0; // chaînage optionnel + fusion nulle
}
```

- **Chaînage optionnel `?.`** : court-circuite et renvoie `undefined` si la valeur est `null`/`undefined`.
- **Fusion nulle `??`** : valeur par défaut **uniquement** pour `null`/`undefined` (contrairement à `||` qui réagit aussi à `0`, `''`, `false`).
- **Assertion non nulle `!`** : `element!.textContent` affirme « ceci n'est pas nul » sans vérification ; si c'est faux, plantage à l'exécution. À éviter.

## 2.5 Assertions de type

Une **assertion** (`as`) dit au compilateur « je sais mieux que toi ». **Aucune conversion, aucune vérification** n'a lieu à l'exécution.

```typescript
const brut: unknown = 'Alice';
const nom = brut as string;                 // simple affirmation
const valeur = (JSON.parse('{"id":7}') as { id: number }).id;
const forcer = 5 as unknown as string;      // double assertion : dernier recours
```

Une assertion n'est **pas** un cast au sens d'autres langages. Préférez la **restriction de type** (`typeof`, `instanceof`, `in`, gardes personnalisées, validation de schéma). Les assertions sont acceptables quand vous détenez une information que le compilateur ne peut pas connaître (par exemple le type d'un élément DOM) — et même alors un générique (`querySelector<HTMLInputElement>`) est préférable.

## 2.6 `as const` et `satisfies`

**`as const`** produit des types **littéraux** et rend l'objet **`readonly` en profondeur** :

```typescript
const direction = { haut: 'UP', bas: 'DOWN' } as const;
// { readonly haut: 'UP'; readonly bas: 'DOWN' }
type Direction = (typeof direction)[keyof typeof direction]; // 'UP' | 'DOWN'

const niveaux = ['debug', 'info', 'erreur'] as const;
type Niveau = (typeof niveaux)[number]; // 'debug' | 'info' | 'erreur'
```

**`satisfies`** (TS 4.9) **vérifie** qu'une valeur respecte un type **sans élargir** le type inféré :

```typescript
type Couleurs = Record<string, string | number[]>;

const palette = {
    rouge: [255, 0, 0],
    vert: '#00ff00',
} satisfies Couleurs;

palette.rouge.map(c => c * 2);  // reste connu comme number[]
palette.vert.toUpperCase();     // reste connu comme string
```

Avec une annotation `: Couleurs`, `palette.rouge` serait `string | number[]` et les deux lignes ci-dessus échoueraient. `satisfies` combine **validation** et **précision**.

## 2.7 Aperçu des types composés

```typescript
let utilisateur: { nom: string; age?: number } = { nom: 'Alice' };
let additionner: (a: number, b: number) => number = (a, b) => a + b;
let ids: number[] = [1, 2, 3];
let paire: [string, number] = ['Alice', 30];
```

Chacun est étudié en détail dans les modules suivants.

## Pièges courants

- Croire que `: string` convertit ou valide : ce n'est qu'une promesse au compilateur.
- Utiliser `any` « temporairement » : il contamine tout ce qu'il touche.
- Confondre `void` (fonction sans retour) et `undefined` (valeur).
- Oublier que `typeof null === 'object'` en JavaScript : testez `=== null` explicitement.

## Points clés du module 2

- Laissez l'inférence travailler ; annotez paramètres et API publiques.
- `unknown` > `any`. `never` marque l'impossible.
- Mode strict : `null`/`undefined` sont des types à part entière.
- Assertion ≠ vérification. `as const` fige, `satisfies` valide sans élargir.

---

# 3. Fonctions et annotations de types

**Objectifs** : typer paramètres et retours, utiliser paramètres optionnels, par défaut et *rest*, écrire des surcharges, maîtriser la restriction de type, les gardes et assertions, et l'exhaustivité.

## 3.1 Annoter paramètres et retour

```typescript
function additionner(a: number, b: number): number {
    return a + b;
}
const multiplier = (a: number, b: number): number => a * b;
const saluer = (nom: string): void => console.log(`Salut ${nom}`);
```

Les **paramètres** doivent toujours être annotés (sauf quand le contexte les infère, comme dans un callback). Le **type de retour** est inféré ; l'annoter sur les fonctions publiques documente le contrat, détecte les retours accidentels et accélère le compilateur.

## 3.2 Paramètres optionnels, par défaut et *rest*

```typescript
function presenter(nom: string, age?: number): string {   // age : number | undefined
    return age !== undefined ? `${nom} (${age} ans)` : nom;
}

function saluer(nom: string, salutation = 'Bonjour'): string { // type inféré : string
    return `${salutation}, ${nom}`;
}

function somme(...nombres: number[]): number {
    return nombres.reduce((t, n) => t + n, 0);
}
```

- Un paramètre **optionnel** (`?`) vaut `T | undefined` ; il vient **après** les obligatoires.
- Un paramètre **par défaut** est implicitement optionnel pour l'appelant.
- Un paramètre **rest** (`...x`) collecte les arguments restants dans un tableau (ou un tuple : `...args: [string, number]`).

## 3.3 Types de fonctions

```typescript
type Operation = (a: number, b: number) => number;
const addition: Operation = (a, b) => a + b; // a et b sont inférés

interface Comparateur {            // interface appelable
    (a: string, b: string): number;
}

function appliquer(f: (x: number) => number, valeur: number) { return f(valeur); }
appliquer(x => x * 2, 5);          // typage contextuel : x est number
```

Le **typage contextuel** déduit les types des paramètres d'un callback à partir de l'endroit où il est passé.

**Compatibilité des fonctions** : une fonction avec **moins** de paramètres est assignable à un type de fonction qui en prévoit plus (on peut ignorer des arguments), pas l'inverse. Les types des paramètres sont **contravariants** (avec `strictFunctionTypes`) et le type de retour **covariant**.

## 3.4 Surcharges de fonctions

Plusieurs **signatures** publiques pour une seule **implémentation**, dont la signature n'est pas visible de l'extérieur :

```typescript
function formater(valeur: string): string;
function formater(valeur: number, decimales: number): string;
function formater(valeur: string | number, decimales?: number): string {
    return typeof valeur === 'string' ? valeur.trim() : valeur.toFixed(decimales ?? 2);
}

formater('  x ');       // OK
formater(3.14159, 2);   // OK
// formater(3.14);      // ERREUR : aucune surcharge ne correspond
```

Préférez une **union** ou un **générique** aux surcharges quand c'est possible : elles sont plus simples et se composent mieux. Les surcharges sont utiles quand le **type de retour dépend** des arguments.

## 3.5 Le paramètre `this`

En JavaScript, `this` dépend de l'appel. TypeScript permet de le typer via un **faux premier paramètre** (effacé à la compilation) :

```typescript
interface Bouton { etiquette: string }

function afficher(this: Bouton) {
    console.log(this.etiquette);
}
afficher.call({ etiquette: 'OK' });
```

Avec `noImplicitThis` (dans `strict`), un `this` de type implicite `any` est refusé. Les fonctions fléchées capturent le `this` de leur contexte lexical.

## 3.6 Restriction de type (*narrowing*)

Le compilateur **affine** le type d'une variable selon les tests rencontrés dans le **flux de contrôle** (analyse de flux).

```typescript
function afficher(valeur: string | number | null) {
    if (valeur === null) return;          // null éliminé
    if (typeof valeur === 'string') {
        valeur.toUpperCase();                // string
    } else {
        valeur.toFixed(2);                   // number
    }
}
```

| Technique | Exemple | Restreint… |
| --- | --- | --- |
| `typeof` | `typeof x === 'string'` | Aux primitifs |
| `instanceof` | `x instanceof Date` | Aux classes |
| `in` | `'nom' in x` | Aux objets selon une propriété |
| Égalité | `x === null`, `x === 'a'` | À une valeur |
| Vérité | `if (x)` | Élimine `null`, `undefined`, `0`, `''`, `false` |
| Discriminant | `x.etat === 'succes'` | Aux unions discriminées |
| `Array.isArray` |  | Aux tableaux |

### Gardes de type personnalisées (*type predicates*)

Une fonction dont le retour s'écrit `param is Type` indique au compilateur : « si je renvoie `true`, le paramètre est de ce type ».

```typescript
interface Chat { miauler(): void }
interface Chien { aboyer(): void }

function estChat(a: Chat | Chien): a is Chat {
    return 'miauler' in a;
}

const animaux: (Chat | Chien)[] = [];
const chats = animaux.filter(estChat); // Chat[]

// TS 5.5 : prédicat INFÉRÉ dans les cas simples
const nombres = [1, undefined, 3].filter(x => x !== undefined); // number[]
```

**Attention** : le compilateur **fait confiance** au prédicat. Un prédicat faux (qui renvoie `true` à tort) crée une faille de typage.

### Fonctions d'assertion

Une fonction `asserts` **lève une exception** si la condition échoue ; sinon le type est raffiné pour la suite du code.

```typescript
function assert(condition: unknown, message: string): asserts condition {
    if (!condition) throw new Error(message);
}
function assertString(v: unknown): asserts v is string {
    if (typeof v !== 'string') throw new TypeError('Chaîne attendue');
}

const valeur: unknown = 'texte';
assertString(valeur);
valeur.toUpperCase(); // valeur est string ici
```

## 3.7 `never` et vérification d'exhaustivité

Quand on a traité tous les cas d'une union discriminée, la variable restante est de type `never`. L'affecter à un `never` fait échouer la compilation si un cas est oublié.

```typescript
type Forme =
    | { type: 'cercle'; rayon: number }
    | { type: 'carre'; cote: number };

function aire(f: Forme): number {
    switch (f.type) {
        case 'cercle': return Math.PI * f.rayon ** 2;
        case 'carre':  return f.cote ** 2;
        default: {
            const _exhaustif: never = f; // ERREUR si on ajoute 'triangle' sans le traiter
            return _exhaustif;
        }
    }
}
```

La règle ESLint `switch-exhaustiveness-check` automatise cette vérification.

## 3.8 Aperçu des génériques

```typescript
function premier<T>(elements: T[]): T | undefined { return elements[0]; }
```

`T` est un **paramètre de type** : un « trou » rempli à l'appel. Voir module 9.

## Pièges courants

- Un paramètre optionnel placé avant un paramètre obligatoire : erreur.
- Confondre signature de surcharge et implémentation : l'implémentation n'est pas appelable directement.
- Un prédicat de type incorrect : le compilateur ne le détecte pas.
- `async` sans annoter `Promise<T>` : le type est inféré, mais pensez à l'annoter sur l'API publique.

## Points clés du module 3

- Annotez les paramètres ; inférez ou annotez le retour selon la visibilité.
- Restreignez avec `typeof`, `instanceof`, `in`, discriminants, gardes.
- `never` + `switch` = exhaustivité garantie.
- Surcharges seulement quand le retour dépend des arguments.

---

# 4. Tableaux et tuples

**Objectifs** : typer les tableaux, utiliser les méthodes typées, gérer la lecture seule et l'accès sûr aux indices, et maîtriser les tuples.

## 4.1 Les tableaux

Un tableau TypeScript est une collection **homogène** d'éléments de même type. Deux syntaxes équivalentes :

```typescript
let nombres: number[] = [1, 2, 3];
let noms: Array<string> = ['Alice', 'Bob']; // syntaxe générique
let mixte: (string | number)[] = ['a', 1];  // parenthèses obligatoires pour une union
let matrice: number[][] = [[1, 2], [3, 4]];

nombres.push(4);
// nombres.push('5'); // ERREUR : 'string' non assignable à 'number'
```

**Attention aux tableaux vides** : `const t = []` est inféré `any[]` (évolutif) ou `never[]` selon le contexte. Annotez toujours : `const t: string[] = []`.

**Syntaxe `T[]` ou `Array<T>` ?** Strictement équivalentes. Par convention, `T[]` pour les types simples, `Array<...>` quand le type d'élément est complexe (par exemple `Array<{ id: number; nom: string }>`).

### Méthodes typées et inférence des callbacks

Toutes les méthodes de `Array` sont typées ; les paramètres des callbacks sont inférés.

```typescript
const nombres = [1, 2, 3, 4];

const doubles = nombres.map(n => n * 2);            // number[]
const pairs = nombres.filter(n => n % 2 === 0);     // number[]
const somme = nombres.reduce((t, n) => t + n, 0);   // number
const premier = nombres.find(n => n > 1);           // number | undefined
const existe = nombres.some(n => n > 3);            // boolean
const textes = nombres.map(String);                 // string[]
```

`find` renvoie `T | undefined` : le compilateur vous oblige à gérer l'absence. `reduce` exige un type d'accumulateur cohérent : pour construire un objet, typez la valeur initiale (`reduce<Record<string, number>>(..., {})`).

Méthodes récentes typées en TS 5.x/6 : `toSorted`, `toReversed`, `toSpliced`, `with`, `findLast`, `at`, `flatMap`, `Object.groupBy` (selon `lib`/`target`).

### Tableaux en lecture seule

```typescript
const figes: readonly number[] = [1, 2, 3];
// figes.push(4); // ERREUR : 'push' n'existe pas sur 'readonly number[]'
function lire(valeurs: readonly string[]) { /* ne peut pas modifier */ }

lire(['a', 'b']);       // un tableau mutable est assignable à readonly
```

`readonly T[]` (ou `ReadonlyArray<T>`) retire toutes les méthodes mutatrices. C'est un contrat **à la compilation** : l'objet reste modifiable en JavaScript. Règle d'or : déclarez `readonly` tout paramètre tableau que la fonction ne modifie pas ; cela rend la fonction utilisable avec des tableaux `readonly` et documentée comme « pure ».

### Accès aux indices et `noUncheckedIndexedAccess`

```typescript
const t: string[] = ['a'];
const x = t[5];   // type : string (mais valeur réelle : undefined !)
```

Par défaut, TypeScript suppose que tout indice est valide. Avec **`noUncheckedIndexedAccess: true`**, `t[i]` devient `string | undefined`, ce qui force la vérification. Recommandé pour les projets rigoureux.

```typescript
const v = t[0];
if (v !== undefined) console.log(v.toUpperCase());
for (const s of t) console.log(s.toUpperCase()); // sans risque : pas d'indice
```

### Itération

`for...of` conserve le type d'élément ; `for...in` itère sur des **clés** (`string`) : à éviter pour les tableaux. `Object.entries(obj)` renvoie `[string, T][]`.

## 4.2 Les tuples

Un **tuple** est un tableau de **longueur fixe** dont le type de chaque **position** est connu.

```typescript
let personne: [string, number] = ['Alice', 30];
const [nom, age] = personne;   // décomposition typée : nom string, age number
// personne = [30, 'Alice'];       // ERREUR : ordre incorrect
// personne = ['Alice', 30, true]; // ERREUR : longueur incorrecte
```

### Variantes de tuples

```typescript
let optionnel: [string, number?] = ['Alice'];            // élément optionnel
let reste: [string, ...number[]] = ['notes', 12, 15, 9]; // éléments variables
let nomme: [nom: string, age: number] = ['Alice', 30];   // étiquettes (documentation et aide d'éditeur)
let fige: readonly [number, number] = [1, 2];           // lecture seule
```

- Les **étiquettes** (`nom:`) n'ont aucun effet de typage mais apparaissent dans l'autocomplétion et les messages d'erreur.
- Un tuple peut contenir un **élément reste** n'importe où (`[...string[], number]`).

### Usages typiques

```typescript
function minMax(valeurs: number[]): [min: number, max: number] {
    return [Math.min(...valeurs), Math.max(...valeurs)];
}
const [mini, maxi] = minMax([3, 1, 4]);
```

- **Retours multiples** (alternative légère à un objet quand l'ordre est évident).
- **Paires clé/valeur** (`Object.entries`, `Map`).
- **Hooks React** : `useState` renvoie `[valeur, setter]`.
- **Paramètres** : `Parameters<F>` produit un tuple ; `(...args: [string, number])` type des paramètres rest.

**Piège** : `push()` fonctionne sur un tuple non `readonly` sans vérifier la longueur. Utilisez `readonly [A, B]` pour l'interdire.

**Inférence** : `const t = ['a', 1]` donne `(string | number)[]`, pas un tuple. Pour obtenir un tuple, annotez le type, ou utilisez `as const` (qui produit `readonly ['a', 1]`).

## Points clés du module 4

- `T[]` pour des collections homogènes ; `readonly T[]` pour les paramètres non modifiés.
- `noUncheckedIndexedAccess` rend les accès par indice sûrs.
- Un tuple fixe longueur et type par position ; `as const` ou annotation pour l'obtenir.

---

# 5. Énumérations (`enum`) et alternatives

**Objectifs** : connaître les enums numériques, de chaînes, `const enum`, leurs limites, et savoir choisir entre enum, union de littéraux et objet `as const`.

## 5.1 Enums numériques

Un **`enum`** est un ensemble de **constantes nommées**. Contrairement à presque tout le reste de TypeScript, un enum **génère du code JavaScript** (un objet).

```typescript
enum Direction {
    Haut,    // 0
    Bas,     // 1
    Gauche,  // 2
    Droite   // 3
}

let d: Direction = Direction.Haut;
console.log(Direction[0]); // 'Haut' : correspondance inverse (enums NUMÉRIQUES seulement)

enum Statut { Actif = 1, Inactif, Banni = 10 } // valeurs explicites ; Inactif vaut 2
```

Les membres sont numérotés à partir de `0`, ou de la dernière valeur explicite + 1. Le JavaScript généré contient une fonction auto-invoquée qui remplit l'objet dans les deux sens (nom → valeur et valeur → nom).

**Piège historique** : avant TS 5.0, n'importe quel `number` était assignable à un enum numérique (`let d: Direction = 99` compilait). TS 5.0 a unifié les enums et resserré les vérifications pour les littéraux, mais les enums numériques restent plus laxistes que les unions.

## 5.2 Enums de chaînes

```typescript
enum Role {
    Admin = 'ADMIN',
    Editeur = 'EDITEUR',
    Lecteur = 'LECTEUR',
}

function peutModifier(role: Role): boolean {
    return role === Role.Admin || role === Role.Editeur;
}
```

Avantages : valeurs **lisibles** dans les journaux, le réseau et la base de données ; pas de correspondance inverse. Inconvénient : un enum de chaînes est **nominal** : on ne peut pas passer la chaîne `'ADMIN'` là où `Role` est attendu, il faut `Role.Admin`.

**Enums hétérogènes** (mélange nombres/chaînes) existent mais sont déconseillés.

## 5.3 `const enum` et `declare enum`

```typescript
const enum Couleur { Rouge = 'R', Vert = 'V' }
console.log(Couleur.Rouge); // remplacé en ligne par 'R' : aucun objet généré
```

- **`const enum`** : les usages sont **remplacés par leur valeur** à la compilation, sans objet à l'exécution (plus compact).
- **Problème** : cela exige de connaître la définition de l'enum à la compilation de chaque fichier. Les outils qui compilent **fichier par fichier** (`isolatedModules`, Vite, esbuild, SWC, Babel) ne peuvent pas le garantir. **À éviter** dans le code partagé ou publié.
- **`declare enum`** : décrit un enum défini ailleurs (dans un `.d.ts`).

## 5.4 Les alternatives modernes

Les enums posent trois difficultés : ils **génèrent du code**, ils sont **interdits avec `erasableSyntaxOnly`**, et leur nature **nominale** gêne l'interopérabilité avec du JavaScript ou du JSON.

### Union de littéraux (défaut recommandé)

```typescript
type Role = 'admin' | 'editeur' | 'lecteur';
let r: Role = 'admin';
// r = 'root'; // ERREUR
```

- Aucun code généré, autocomplétion parfaite, compatible JSON.
- Non itérable à l'exécution (le type disparaît).

### Objet `as const` + type dérivé

```typescript
const Role = {
    Admin: 'ADMIN',
    Editeur: 'EDITEUR',
    Lecteur: 'LECTEUR',
} as const;

type Role = (typeof Role)[keyof typeof Role]; // 'ADMIN' | 'EDITEUR' | 'LECTEUR'

Object.values(Role); // itérable à l'exécution
```

On y gagne un **objet itérable** (pour remplir un menu déroulant, valider une entrée) **et** un type, sans syntaxe spéciale : le **même identifiant** sert de valeur et de type (espaces de noms de valeurs et de types distincts).

### Comparatif

|  | `enum` | Union de littéraux | Objet `as const` |
| --- | --- | --- | --- |
| Code généré | Oui | Non | Oui (objet) |
| Itérable à l'exécution | Oui | Non | Oui |
| Mode `erasableSyntaxOnly` | Interdit | Autorisé | Autorisé |
| Interopérabilité JSON/JS | Moyenne | Excellente | Excellente |
| Recommandation | Code existant, Angular/NestJS | **Défaut** | Quand on a besoin des valeurs |

## Points clés du module 5

- Un enum est un **objet réel** : il coûte du code et impose un typage nominal.
- Préférez union de littéraux ou objet `as const`.
- Évitez `const enum` en dehors d'un code compilé d'un bloc.

---

# 6. Interfaces

**Objectifs** : décrire la forme d'objets avec des interfaces, maîtriser propriétés optionnelles, `readonly`, signatures d'index, héritage, implémentation par des classes, fusion de déclarations, et savoir choisir entre `interface` et `type`.

## 6.1 Définir une interface

Une **interface** nomme et décrit la **forme** d'un objet : ses propriétés et leurs types, ses méthodes. Comme le typage est **structurel**, tout objet de forme compatible convient, sans déclaration `implements` explicite.

```typescript
interface Utilisateur {
    id: number;
    nom: string;
    email?: string;          // optionnelle : string | undefined
    readonly creeLe: Date;   // lecture seule
}

const alice: Utilisateur = { id: 1, nom: 'Alice', creeLe: new Date() };
// alice.creeLe = new Date(); // ERREUR : propriété en lecture seule
// const bob: Utilisateur = { id: 2 }; // ERREUR : propriétés manquantes
```

**Contrôle des propriétés excédentaires** (*excess property check*) : un **littéral d'objet** passé directement à un type est refusé s'il contient une propriété inconnue. Le même objet passé via une variable est accepté (le typage structurel autorise les propriétés supplémentaires).

```typescript
const extra = { id: 1, nom: 'A', creeLe: new Date(), admin: true };
const ok: Utilisateur = extra; // accepté
// const ko: Utilisateur = { id: 1, nom: 'A', creeLe: new Date(), admin: true }; // ERREUR
```

`readonly` est une contrainte **de compilation** ; avec `exactOptionalPropertyTypes`, `email?: string` interdit d'assigner explicitement `undefined`.

## 6.2 Méthodes, fonctions, signatures d'index

```typescript
interface Calculatrice {
    additionner(a: number, b: number): number; // syntaxe de méthode
    reset: () => void;                         // propriété de type fonction
}

interface Dictionnaire {
    [cle: string]: number;   // signature d'index : toute clé string → number
}
const stock: Dictionnaire = { pommes: 10 };

interface Comparateur { (a: string, b: string): number; }          // appelable
interface Fabrique { new (nom: string): Utilisateur; }               // constructible
```

- **Syntaxe de méthode vs propriété fonction** : la première est vérifiée de façon **bivariante** pour ses paramètres, la seconde de façon stricte (`strictFunctionTypes`). Pour un contrat strict, préférez la propriété fonction.
- Une **signature d'index** impose que **toutes** les propriétés explicites soient compatibles avec le type d'index.
- Avec `noUncheckedIndexedAccess`, `stock.pommes` devient `number | undefined`.
- Pour un dictionnaire, `Record<string, number>` ou `Map<string, number>` sont souvent préférables.

## 6.3 Héritage d'interfaces

```typescript
interface Personne { nom: string; age: number }
interface Employe extends Personne { poste: string }
interface Journalisable { journaliser(): void }
interface Manager extends Employe, Journalisable { equipe: Employe[] } // héritage multiple
```

`extends` peut résumer des conflits : si deux interfaces parentes déclarent la même propriété avec des types **incompatibles**, l'erreur est signalée. Une sous-interface peut **restreindre** (pas élargir) le type d'une propriété héritée.

Une interface peut aussi étendre un **alias d'objet** ou une **classe** (elle hérite alors des membres, y compris `private`/`protected`, et seules les sous-classes peuvent l'implémenter).

## 6.4 Implémentation par une classe

```typescript
interface Imprimable { imprimer(): void }

class Rapport implements Imprimable {
    imprimer() { console.log('Impression…'); }
}
```

`implements` **vérifie** que la classe respecte le contrat ; il **ne change pas** son type (ne fournit pas les types des paramètres des méthodes implémentées si vous ne les annotez pas).

## 6.5 Fusion de déclarations

Deux interfaces de même nom **fusionnent** (propriété propre aux interfaces) :

```typescript
interface Config { url: string }
interface Config { delai: number }
const c: Config = { url: 'x', delai: 5 }; // les deux propriétés sont requises
```

Ce mécanisme permet d'**étendre des types globaux ou de bibliothèques** (par exemple `interface Window { monApp: ... }`), voir module 12.

## 6.6 `interface` ou `type` ?

| Critère | `interface` | `type` |
| --- | --- | --- |
| Décrire un objet | Oui | Oui |
| Unions, intersections, tuples, primitives | Non | Oui |
| Types conditionnels / mappés | Non | Oui |
| Fusion de déclarations | Oui | Non (erreur de doublon) |
| `extends` / `implements` | Oui, messages d'erreur clairs | Via intersections `&` |
| Performance sur grandes hiérarchies | Légèrement meilleure | — |

**Règle pratique** : `interface` pour les **formes d'objets** et les contrats de classes ; `type` pour **tout le reste**. Ce qui compte le plus est la **cohérence** au sein du projet.

## Points clés du module 6

- Une interface décrit une **forme** ; la compatibilité est structurelle.
- Propriétés optionnelles (`?`), `readonly`, signatures d'index, appelables, constructibles.
- Les interfaces s'étendent, se fusionnent et s'implémentent.

---

# 7. Alias de types, unions et types littéraux

**Objectifs** : créer des alias, composer des types avec unions et intersections, modéliser des états avec les unions discriminées, utiliser les types littéraux et les types littéraux de gabarit.

## 7.1 Alias de types

Un **alias** (`type`) donne un **nom** à n'importe quel type. Il ne crée pas un nouveau type : c'est une étiquette.

```typescript
type ID = number | string;
type Point = { x: number; y: number };
type Rappel = (erreur: Error | null, donnees?: string) => void;
type Matrice = number[][];
```

Avantages : réutilisation, lisibilité, modification en un seul endroit. Un alias peut être **générique** (`type Pagine<T> = { elements: T[]; page: number }`) et **récursif** (module 11).

## 7.2 Types union (`|`) : « l'un OU l'autre »

Une **union** `A | B` décrit une valeur qui est de type `A` **ou** de type `B`. On ne peut utiliser sur une union que ce qui est **commun** à tous ses membres, sauf restriction préalable.

```typescript
type ID = number | string;

function afficherId(id: ID) {
    // id.toUpperCase();  // ERREUR : n'existe pas sur number
    console.log(typeof id === 'string' ? id.toUpperCase() : id.toFixed(0));
}
```

### Unions discriminées

Une **union discriminée** (*discriminated union*, *tagged union*) est une union d'objets qui partagent une propriété **commune de type littéral** : la **balise**. Tester la balise restreint automatiquement le type.

```typescript
type Requete =
    | { etat: 'chargement' }
    | { etat: 'succes'; donnees: string[] }
    | { etat: 'erreur'; message: string };

function afficher(r: Requete): string {
    switch (r.etat) {
        case 'chargement': return '…';
        case 'succes':     return r.donnees.join(', '); // donnees disponible
        case 'erreur':     return r.message;            // message disponible
    }
}
```

C'est **le** motif idiomatique pour modéliser des **états** : on rend les combinaisons impossibles **inexprimables**. Comparez avec `{ chargement: boolean; donnees?: string[]; erreur?: string }`, qui autorise `chargement: true` avec `erreur` renseigné. Combiné avec la vérification d'exhaustivité (3.7), le compilateur signale tout état oublié.

## 7.3 Types intersection (`&`) : « l'un ET l'autre »

Une **intersection** `A & B` décrit une valeur qui possède **toutes** les propriétés de `A` et de `B`.

```typescript
type Identifiable = { id: number };
type Horodate = { creeLe: Date; modifieLe: Date };
type Article = Identifiable & Horodate & { titre: string };
```

Points d'attention : l'intersection de types **incompatibles** produit `never` (par exemple `string & number`), et celle d'objets dont une propriété a des types différents rend cette propriété `never`. Pour composer des objets, `interface ... extends` offre de meilleurs messages d'erreur.

## 7.4 Types littéraux

Un **type littéral** représente **une seule valeur** précise (`'S'`, `42`, `true`). Combinés en union, ils définissent un ensemble fermé de valeurs.

```typescript
type Taille = 'S' | 'M' | 'L' | 'XL';
type De = 1 | 2 | 3 | 4 | 5 | 6;
type Methode = 'GET' | 'POST' | 'PUT' | 'DELETE';

let t: Taille = 'M';
// t = 'XXL'; // ERREUR
```

**Piège de l'élargissement** : dans un objet, une chaîne littérale est élargie en `string`.

```typescript
function requete(url: string, methode: Methode = 'GET') {}

const config = { methode: 'GET' };           // methode : string
// requete('/x', config.methode);             // ERREUR : string non assignable à Methode

const config2 = { methode: 'GET' } as const; // methode : 'GET'
requete('/x', config2.methode);               // OK
```

Trois rempèdes : `as const`, annoter l'objet (`const config: { methode: Methode }`), ou `satisfies`.

## 7.5 Types littéraux de gabarit (*template literal types*)

Ils reprennent la syntaxe des gabarits de chaînes **au niveau des types** et calculent des unions de chaînes.

```typescript
type Evenement = 'clic' | 'survol';
type Gestionnaire = `on${Capitalize<Evenement>}`; // 'onClic' | 'onSurvol'
type Route = `/api/${string}`;
let r: Route = '/api/utilisateurs';

type Marge = `${'haut' | 'bas'}-${'gauche' | 'droite'}`; // produit cartésien : 4 combinaisons
```

Utilitaires de manipulation : `Uppercase`, `Lowercase`, `Capitalize`, `Uncapitalize`. Associés à `infer`, ils permettent d'analyser des chaînes au niveau des types (module 11).

## 7.6 Récapitulatif sur la restriction de type

Les unions n'ont d'intérêt que si l'on sait les **restreindre** (module 3.6) : `typeof`, `instanceof`, `in`, égalité stricte, vérité, propriété discriminante, garde personnalisée, `Array.isArray`.

## 7.7 `type` ou `interface` ?

Voir 6.6. Les alias sont **indispensables** pour unions, intersections, tuples, types calculés et alias de primitives.

## Points clés du module 7

- Union = **ou**, intersection = **et**.
- Union discriminée + `switch` = modélisation d'états sûre et exhaustive.
- Un littéral dans un objet est élargi, sauf `as const`.
- Les types littéraux de gabarit calculent des chaînes au niveau des types.

---

# NIVEAU INTERMÉDIAIRE

---

# 8. Classes et programmation orientée objet

**Objectifs** : écrire des classes typées, maîtriser modificateurs d'accès, accesseurs, propriétés de paramètres, héritage, classes abstraites, `override`, et comprendre le typage structurel des classes.

## 8.1 Définir une classe

Une **classe** est un modèle qui regroupe des **propriétés** (données) et des **méthodes** (comportement). En TypeScript, les propriétés doivent être **déclarées** et typées.

```typescript
class Personne {
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

const alice = new Personne('Alice', 30);
```

**`strictPropertyInitialization`** (dans `strict`) exige que chaque propriété soit initialisée dans le constructeur ou à sa déclaration. Si une valeur est injectée plus tard (frameworks, ORM), on utilise l'**assertion d'affectation définitive** `nom!: string`, ou on rend la propriété optionnelle.

Le **nom d'une classe est à la fois une valeur** (le constructeur) **et un type** (celui de ses instances).

## 8.2 Modificateurs d'accès

| Modificateur | Accessible depuis | Vérifié à |
| --- | --- | --- |
| `public` (défaut) | Partout | — |
| `protected` | La classe et ses sous-classes | Compilation |
| `private` | La classe seule | **Compilation uniquement** |
| `#champ` | La classe seule | **Exécution** (JavaScript natif) |

```typescript
class CompteBancaire {
    public titulaire: string;
    private solde = 0;             // privé pour TypeScript seulement
    #pin: string;                  // vraiment privé (ECMAScript)
    protected devise = 'EUR';
    readonly numero: string;       // assignable à la déclaration ou dans le constructeur

    constructor(titulaire: string, numero: string, pin: string) {
        this.titulaire = titulaire;
        this.numero = numero;
        this.#pin = pin;
    }

    deposer(montant: number): void {
        if (montant <= 0) throw new RangeError('Montant invalide');
        this.solde += montant;
    }

    get soldeActuel(): number { return this.solde; }  // accesseur (getter)
    set pin(nouveau: string) { this.#pin = nouveau; } // mutateur (setter)
}
```

- **Accesseurs** `get`/`set` : se lisent/écrivent comme des propriétés. Sans `set`, la propriété est en lecture seule. Le type du getter et du setter peuvent diverger depuis TS 5.1 (si le getter est assignable au setter).
- `private` est **contournable** (`obj['solde']`, `as any`) et reste visible dans le JavaScript généré. Pour une encapsulation **garantie**, utilisez `#champ`.
- `readonly` est une protection de compilation.

## 8.3 Propriétés de paramètres

Un raccourci qui **déclare et initialise** des propriétés directement depuis les paramètres du constructeur :

```typescript
class Produit {
    constructor(
        public readonly id: number,
        public nom: string,
        private prix: number,
    ) {}
}
```

Cette syntaxe génère du code : elle est **interdite avec `--erasableSyntaxOnly`**. Dans ce cas, déclarez les propriétés explicitement et affectez-les dans le constructeur.

## 8.4 Membres statiques

```typescript
class Compteur {
    static total = 0;
    static incrementer(): number { return ++Compteur.total; }
    static { /* bloc d'initialisation statique : code exécuté une fois */ }
}
Compteur.incrementer();
```

Les membres statiques appartiennent à la **classe**, pas aux instances. Les modificateurs d'accès s'appliquent aussi (`private static`, `static #x`).

## 8.5 Héritage

```typescript
class Animal {
    constructor(protected nom: string) {}
    parler(): string { return `${this.nom} fait du bruit`; }
}

class Chien extends Animal {
    constructor(nom: string, private race: string) {
        super(nom); // obligatoire avant d'utiliser `this`
    }
    override parler(): string {
        return `${this.nom} aboie`;
    }
}
```

- `extends` : la sous-classe hérite des membres `public`/`protected`.
- `super(...)` appelle le constructeur parent ; `super.methode()` appelle la méthode parente.
- **`override`** (TS 4.3) : erreur si la méthode n'existe pas dans le parent. Avec **`noImplicitOverride`**, le mot-clé devient obligatoire pour toute redéfinition, ce qui protège contre les renommages silencieux.
- Une classe ne peut étendre qu'**une seule** classe ; pour combiner des comportements, voir module 17.

## 8.6 Classes abstraites

Une classe **abstraite** ne peut pas être instanciée ; elle définit un squelette, avec des méthodes `abstract` que les sous-classes **doivent** implémenter.

```typescript
abstract class Forme {
    abstract aire(): number;
    decrire(): string { return `Aire : ${this.aire().toFixed(2)}`; }
}

class Cercle extends Forme {
    constructor(private rayon: number) { super(); }
    aire(): number { return Math.PI * this.rayon ** 2; }
}
// new Forme(); // ERREUR : impossible d'instancier une classe abstraite
```

Patron **méthode gabarit** : la classe abstraite décrit l'algorithme (`decrire`) et laisse des étapes (`aire`) aux sous-classes.

## 8.7 Implémenter des interfaces

```typescript
interface Serialisable { versJson(): string }
interface Identifiable { readonly id: number }

class Article implements Serialisable, Identifiable {
    constructor(public readonly id: number, public titre: string) {}
    versJson() { return JSON.stringify(this); }
}
```

Une classe peut implémenter **plusieurs** interfaces. Les interfaces décrivent ce qu'un objet **sait faire**, l'héritage ce qu'il **est**.

## 8.8 Le mot-clé `accessor`, la classe comme type et comme constructeur

```typescript
class Etat {
    accessor compteur = 0; // génère un getter/setter automatique sur un champ privé (décorateurs standard)
}

class Personne { constructor(public nom: string, public age: number) {} }

const p: Personne = new Personne('A', 1);  // le nom de la classe est AUSSI un type
type Constructeur = new (n: string, a: number) => Personne; // type du constructeur
const construire: Constructeur = Personne;
```

Pour obtenir le type de l'instance à partir d'un constructeur générique : `InstanceType<typeof Personne>`.

## 8.9 Typage structurel : les surprises

Deux classes de **même forme** sont compatibles, même sans lien d'héritage :

```typescript
class A { x = 1; }
class B { x = 1; }
const a: A = new B(); // accepté
```

**Exception** : si une classe possède un membre `private`, `protected` ou `#privé`, seules ses sous-classes (ou elle-même) lui sont compatibles : le typage devient alors quasi **nominal** pour cette classe. Technique utile pour empêcher des substitutions accidentelles.

## 8.10 Bonnes pratiques

- **Composition plutôt qu'héritage** profond (module 17).
- Programmez **vers des interfaces** : injection de dépendances, tests.
- Marquez `readonly` les propriétés qui ne changent pas.
- Dans le code récent, des **fonctions et types** remplacent souvent des classes ; gardez les classes pour des entités avec **état et comportement**, et quand un framework l'impose (Angular, NestJS).

## Points clés du module 8

- `private` = compilation ; `#champ` = exécution.
- Propriétés de paramètres = raccourci, mais incompatible avec le mode effaçable.
- `override` + `noImplicitOverride` sécurisent l'héritage.
- Typage structurel : la forme prime, sauf membres privés.

---

# 9. Génériques

**Objectifs** : écrire du code réutilisable sans perdre le typage ; maîtriser paramètres de type, contraintes, valeurs par défaut, classes et interfaces génériques, `const T`, `NoInfer`, variance.

## 9.1 Le problème

Comment écrire une fonction qui marche pour **plusieurs types** tout en **conservant** l'information de type ? `any` la perd.

```typescript
function identite(x: any): any { return x; }   // le type d'entrée est perdu
function identiteSure<T>(x: T): T { return x; } // T est « capturé »

const a = identiteSure('texte');        // T = string
const b = identiteSure(42);             // T = number
const c = identiteSure<boolean>(true);  // T donné explicitement
```

`T` est un **paramètre de type** : une variable **de type**, instanciée à chaque appel, soit par **inférence** (cas général), soit **explicitement** entre chevrons.

## 9.2 Fonctions génériques

```typescript
function premier<T>(elements: T[]): T | undefined { return elements[0]; }
function paire<A, B>(a: A, b: B): [A, B] { return [a, b]; }

const x = premier([1, 2, 3]);   // number | undefined
const p = paire('a', 1);        // [string, number]

const cles = <T extends object>(o: T) => Object.keys(o) as (keyof T)[];
```

Dans un fichier `.tsx`, écrivez `<T,>(x: T) => ...` ou `<T extends unknown>(...)` pour lever l'ambiguïté avec JSX.

**Règle de conception** : un paramètre de type doit apparaître **au moins deux fois** (par exemple en entrée et en sortie) ; sinon, il ne relie rien et un simple type suffit. Un générique utilisé une seule fois est souvent un `unknown` déguisé.

## 9.3 Contraintes : `extends`

Une **contrainte** limite les types acceptables pour `T` et donne accès à leurs membres.

```typescript
interface AvecLongueur { length: number }

function longueur<T extends AvecLongueur>(x: T): number { return x.length; }
longueur('texte');     // OK
longueur([1, 2, 3]);   // OK
// longueur(42);       // ERREUR : number n'a pas de length

function lire<T, K extends keyof T>(objet: T, cle: K): T[K] { return objet[cle]; }
lire({ nom: 'A', age: 3 }, 'age'); // number
// lire({ nom: 'A' }, 'x');         // ERREUR : 'x' n'est pas une clé
```

Le motif `K extends keyof T` est l'un des plus importants : il garantit qu'une clé existe et que le type de retour (`T[K]`) est précis. Un paramètre de type peut en contraindre un autre.

## 9.4 Interfaces et alias génériques

```typescript
interface Reponse<T> {
    donnees: T;
    statut: number;
    erreur?: string;
}
const r: Reponse<{ id: number; nom: string }> = { donnees: { id: 1, nom: 'A' }, statut: 200 };

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

Les membres **statiques** d'une classe générique ne peuvent pas utiliser `T` (il appartient aux instances).

## 9.6 Valeurs par défaut des paramètres de type

```typescript
interface Evenement<T = string> { nom: string; charge: T }
const e: Evenement = { nom: 'x', charge: 'texte' };       // T = string
const f: Evenement<number> = { nom: 'y', charge: 42 };
```

Les paramètres avec défaut viennent **après** ceux sans défaut.

## 9.7 Paramètres de type `const` (TS 5.0)

```typescript
function creer<const T extends readonly unknown[]>(valeurs: T): T { return valeurs; }
const t = creer(['a', 'b']); // readonly ['a', 'b'] au lieu de string[]
```

Ils demandent à l'inférence de conserver les **types littéraux** comme si l'argument avait `as const`.

## 9.8 `NoInfer` (TS 5.4)

`NoInfer<T>` empêche un argument de **participer à l'inférence** de `T`.

```typescript
function creerSignal<T extends string>(valeurs: T[], defaut: NoInfer<T>) {}
creerSignal(['rouge', 'vert'], 'rouge');   // OK
// creerSignal(['rouge', 'vert'], 'bleu'); // ERREUR : 'bleu' n'est pas dans les valeurs
```

Sans `NoInfer`, `T` serait inféré comme `'rouge' | 'vert' | 'bleu'` et l'erreur serait manquée.

## 9.9 Variance et annotations `in` / `out`

La **variance** décrit comment la relation de sous-typage se transmet à travers un type générique :

- **Covariant** (`out T`) : `Producteur<Chat>` est assignable à `Producteur<Animal>` (T n'apparaît qu'en **sortie**).
- **Contravariant** (`in T`) : `Consommateur<Animal>` est assignable à `Consommateur<Chat>` (T n'apparaît qu'en **entrée**).
- **Invariant** : T en entrée **et** en sortie : aucune assignation.

```typescript
interface Producteur<out T> { produire(): T }
interface Consommateur<in T> { consommer(x: T): void }
```

Les annotations explicites documentent l'intention et accélèrent la vérification sur des types complexes.

## 9.10 Exemple concret : requête typée

```typescript
async function getJson<T>(url: string): Promise<T> {
    const reponse = await fetch(url);
    if (!reponse.ok) throw new Error(`HTTP ${reponse.status}`);
    return (await reponse.json()) as T; // T N'EST PAS vérifié à l'exécution
}

interface Utilisateur { id: number; nom: string }
const u = await getJson<Utilisateur>('/api/users/1');
```

Le paramètre de type est ici une **promesse du développeur**, pas une garantie. Validez la réponse avec un schéma (module 19.5).

## Pièges courants

- Spécifier `T` explicitement quand l'inférence suffit.
- Un générique qui n'apparaît qu'une fois.
- Utiliser `T` comme valeur : `T` n'existe qu'à la compilation (`new T()` est impossible).

## Points clés du module 9

- Un générique **relie** des types entre eux (entrée → sortie).
- `extends` contraint ; `K extends keyof T` sécurise l'accès par clé.
- `const T`, `NoInfer`, `in`/`out` : outils de précision.

---

# 10. Modules et espaces de noms

**Objectifs** : organiser le code en modules ES, maîtriser imports/exports (y compris de types), comprendre CommonJS vs ESM, importer du JSON, et situer les `namespace` dans l'histoire.

## 10.1 Les modules ES

Tout fichier contenant un `import` ou un `export` de niveau supérieur est un **module** : il possède sa **propre portée** (ses déclarations ne sont pas globales). Un fichier sans import/export est un **script** dont les déclarations sont globales.

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
import Calculatrice, { PI, additionner as plus } from './mathematiques.js';
import * as maths from './mathematiques.js';           // import d'espace de noms
import type { Point, ID } from './mathematiques.js';   // import de TYPES uniquement (effacé)
import { type Point as P, additionner } from './mathematiques.js'; // import mélangé
```

- **Export nommé** (`export const x`) : plusieurs par module, import entre accolades, renommage avec `as`.
- **Export par défaut** (`export default`) : un seul par module ; le nom est choisi à l'import. Les exports nommés sont généralement préférés (meilleure refactorisation et autocomplétion).
- **`import type`** : garantit que l'import est **effacé** à la compilation (utile pour les cycles, les performances et la clarté).

### Extensions et résolution

Avec les **modules ES natifs** (`"module": "nodenext"`), les imports relatifs doivent inclure l'extension de **sortie** : `./fichier.js` (même si le fichier source est `.ts`), car Node.js ne réécrit pas les chemins. Avec un **bundler** (`"moduleResolution": "bundler"`), on peut omettre l'extension. TS 5.7 propose `--rewriteRelativeImportExtensions` pour écrire `./fichier.ts` dans les sources.

### Réexporter (fichiers « barrel »)

```typescript
export { additionner } from './mathematiques.js';
export * from './utilitaires.js';
export type { Point } from './types.js';
```

Un fichier `index.ts` qui réexporte facilite les imports, mais les gros barrels peuvent ralentir les outils et empêcher l'élagage (*tree shaking*) : à utiliser avec modération.

### `verbatimModuleSyntax`

L'option **`verbatimModuleSyntax`** impose l'usage de `import type` / `export type` pour les types, et garantit que **ce qui est écrit est ce qui est généré** : tout import sans `type` est conservé. Elle remplace `importsNotUsedAsValues` et `preserveValueImports`. C'est la configuration moderne recommandée.

## 10.2 CommonJS et ES modules

|  | ES modules | CommonJS |
| --- | --- | --- |
| Syntaxe | `import` / `export` | `require()` / `module.exports` |
| Chargement | Statique, asynchrone | Dynamique, synchrone |
| `"module"` TypeScript | `esnext`, `nodenext`, `preserve` | `commonjs` |
| Statut | **Standard** | Historique (Node.js) |

Pour Node.js : `"module": "nodenext"` et `"type": "module"` dans `package.json` (ou extension `.mts`/`.mjs`). Avec `nodenext`, TypeScript décide du format de chaque fichier d'après son extension et le `type` du `package.json` le plus proche. Les versions récentes de Node.js permettent aussi `require()` de modules ES synchrones (TS 5.8).

`export =` et `import x = require()` sont des syntaxes **CommonJS** historiques ; `esModuleInterop` (toujours actif depuis TS 6.0) facilite l'import par défaut de modules CommonJS.

## 10.3 Importer du JSON

```typescript
import config from './config.json' with { type: 'json' }; // attributs d'import (remplace `assert`)
// tsconfig : "resolveJsonModule": true
```

Le type du JSON est inféré depuis son contenu.

## 10.4 Imports dynamiques

```typescript
const { default: marked } = await import('marked'); // chargement à la demande
```

Renvoie une `Promise` du module ; permet le découpage de code (*code splitting*) et le chargement conditionnel. Le type du module est préservé.

## 10.5 Espaces de noms (*namespaces*) : historique

Avant les modules ES, les **namespaces** (anciennement « modules internes ») regroupaient du code dans un objet global.

```typescript
namespace Utilitaires {
    export function journaliser(message: string): void { console.log(message); }
    export namespace Maths {
        export const carre = (x: number) => x * x;
    }
}
Utilitaires.Maths.carre(4);
```

**Statut en 2026** :

- **Évitez les `namespace` dans le nouveau code** : utilisez des modules ES. Ils génèrent du code et sont **interdits avec `erasableSyntaxOnly`**.
- TypeScript 6.0 **déprécie l'ancienne syntaxe `module Nom { }`** (utilisez le mot-clé `namespace`).
- Les **`declare namespace`** restent **légitimes** dans les fichiers `.d.ts` pour décrire des bibliothèques globales (module 12).

|  | Module ES | Namespace |
| --- | --- | --- |
| Portée | Fichier | Bloc global, fusionnable |
| Chargement | Natif, élagage possible | Concaténation / balises `<script>` |
| Usage conseillé | **Toujours** | Code hérité ou `.d.ts` |

## 10.6 Alias de chemins

Pour éviter les imports `../../../x`, on définit des alias (`@/...`) ; voir 20.4. Attention : `paths` ne configure **que TypeScript** ; l'exécution doit connaître l'alias aussi.

## Points clés du module 10

- Un fichier avec import/export est un module ; préférez les exports nommés.
- `import type` + `verbatimModuleSyntax` rendent les imports prévisibles.
- Node.js ESM : extensions `.js` obligatoires ; bundler : facultatives.
- Les `namespace` sont hérités ; gardez-les pour les `.d.ts`.

---

# 11. Types avancés

**Objectifs** : maîtriser `keyof`, `typeof`, types indexés, types mappés, conditionnels, `infer`, types littéraux de gabarit, types récursifs et types marqués. Ces outils permettent de **calculer** des types à partir d'autres types.

## 11.1 `keyof`, `typeof` et types indexés

```typescript
interface Utilisateur { id: number; nom: string; email: string }

type Cle = keyof Utilisateur;               // 'id' | 'nom' | 'email'
type TypeNom = Utilisateur['nom'];          // string  (type indexé : « lookup type »)
type Tous = Utilisateur[keyof Utilisateur]; // string | number

const config = { port: 3000, hote: 'localhost' };
type Config = typeof config;                // { port: number; hote: string }

const jours = ['lun', 'mar'] as const;
type Jour = (typeof jours)[number];         // 'lun' | 'mar'
```

- **`keyof T`** : union des **clés** de `T` (sous forme de types littéraux).
- **`typeof valeur`** (dans une position de type) : le **type d'une valeur** existante. Ne pas confondre avec l'opérateur JavaScript `typeof` (qui renvoie une chaîne).
- **`T[K]`** : type de la propriété `K` de `T`. `T[number]` : type des éléments d'un tableau/tuple.

## 11.2 Types mappés (*mapped types*)

Un type mappé **transforme chaque propriété** d'un type : `{ [K in keyof T]: ... }`.

```typescript
type EnLectureSeule<T> = { readonly [K in keyof T]: T[K] };
type Optionnel<T> = { [K in keyof T]?: T[K] };
type Nullable<T> = { [K in keyof T]: T[K] | null };

// Modificateurs : + ajoute, - retire
type Mutable<T> = { -readonly [K in keyof T]: T[K] };
type Requis<T> = { [K in keyof T]-?: T[K] };

// Remappage des clés avec `as`
type Getters<T> = {
    [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};
type G = Getters<{ nom: string; age: number }>;
// { getNom: () => string; getAge: () => number }

// Filtrer des clés (as ... never supprime la clé)
type SansFonctions<T> = {
    [K in keyof T as T[K] extends Function ? never : K]: T[K];
};
```

Les utilitaires `Partial`, `Required`, `Readonly`, `Pick`, `Record` du module 13 sont tous des types mappés. Appliqués à un type paramétré par `keyof T`, ils sont dits **homomorphes** et préservent les modificateurs (`readonly`, `?`) de l'original.

## 11.3 Types conditionnels

Syntaxe : `T extends U ? X : Y`, « si `T` est assignable à `U`, alors `X`, sinon `Y` ».

```typescript
type EstString<T> = T extends string ? 'oui' : 'non';
type A = EstString<'x'>; // 'oui'
type B = EstString<42>;  // 'non'

// Distributifs sur les unions : appliqués à chaque membre
type SansNull<T> = T extends null | undefined ? never : T;
type C = SansNull<string | null>; // string

// Empêcher la distribution en enveloppant : [T] extends [U]
type EstNever<T> = [T] extends [never] ? true : false;
```

**Distributivité** : quand `T` est un paramètre de type **nu** (non enveloppe) et reçoit une union, le conditionnel est appliqué à **chaque membre** puis les résultats sont réunis. C'est ce qui permet à `Exclude<'a'|'b', 'a'>` de donner `'b'`. `never` est l'union vide : un conditionnel distributif sur `never` donne `never`.

## 11.4 `infer` : extraire un type

`infer X` déclare une variable de type **dans la branche `extends`** d'un conditionnel pour **capturer** une partie d'un type.

```typescript
type TypeRetour<T> = T extends (...args: any[]) => infer R ? R : never;
type R = TypeRetour<() => string>;                     // string

type ContenuPromesse<T> = T extends Promise<infer U> ? U : T;
type P = ContenuPromesse<Promise<number>>;             // number

type Parametres<T> = T extends (...args: infer P) => any ? P : never;
type Premier<T extends unknown[]> = T extends [infer P, ...unknown[]] ? P : never;
type ElementDe<T> = T extends readonly (infer E)[] ? E : never;
```

`ReturnType`, `Parameters`, `Awaited` sont définis ainsi. On peut contraindre `infer` : `infer S extends string` (TS 4.7).

## 11.5 Types littéraux de gabarit avancés

Combinés avec `infer` et la récursion, ils analysent des chaînes :

```typescript
type ParametreRoute<S extends string> =
    S extends `${string}:${infer P}/${infer Reste}` ? P | ParametreRoute<`/${Reste}`> :
    S extends `${string}:${infer P}` ? P : never;

type Params = ParametreRoute<'/users/:id/posts/:postId'>; // 'id' | 'postId'

type Handlers = { [E in 'clic' | 'survol' as `on${Capitalize<E>}`]: () => void };
```

C'est la technique derrière les routeurs et clients d'API fortement typés.

## 11.6 Types récursifs

```typescript
type JSONValeur = string | number | boolean | null | JSONValeur[] | { [cle: string]: JSONValeur };

type ProfondementPartiel<T> = {
    [K in keyof T]?: T[K] extends object ? ProfondementPartiel<T[K]> : T[K];
};
```

TypeScript limite la profondeur de récursion (environ 50 niveaux pour les conditionnels, davantage avec une récursion terminale) ; des types trop récursifs ralentissent le compilateur.

## 11.7 Types marqués (*branded types*)

Pour distinguer des valeurs de même type primitif (unités, identifiants), on les « marque » par une intersection phantom :

```typescript
type EuroMontant = number & { readonly __marque: 'EUR' };
type IdUtilisateur = string & { readonly __marque: 'IdUtilisateur' };

const euros = (n: number) => n as EuroMontant;
function payer(m: EuroMontant) { console.log(`Paiement de ${m} EUR`); }

payer(euros(10));
// payer(10); // ERREUR : un number nu n'est pas un EuroMontant
```

La marque n'existe qu'au niveau des types (aucune propriété réelle). On crée les valeurs marquées via des **fonctions de construction** qui valident.

## 11.8 Autres outils

- `satisfies` et `as const` (2.6), l'opérateur `typeof` sur les valeurs, `ReturnType<typeof f>`, `Awaited<T>`.
- **Types `unique symbol`** pour un typage quasi nominal.
- **Signatures d'index** et `Record` (6.2).

## 11.9 Conseils

- Commencez **simple** : un type complexe ne se justifie que s'il élimine réellement des erreurs.
- Nommez et **commentez** les types utilitaires ; testez-les (23.5).
- Préférez les **utilitaires intégrés** (module 13) aux réécritures maison.

## Points clés du module 11

- `keyof`/`typeof`/indexés extraient des types ; mappés les transforment ; conditionnels et `infer` calculent.
- Les conditionnels sont **distributifs** sur les unions nues.
- Les types marqués distinguent des primitifs sans coût à l'exécution.

---

# 12. Fichiers de déclaration de types

**Objectifs** : comprendre les `.d.ts`, utiliser DefinitelyTyped, écrire ses propres déclarations, augmenter des modules et des types globaux.

## 12.1 Qu'est-ce qu'un fichier `.d.ts` ?

Un fichier de **déclaration** (`.d.ts`) contient **uniquement des types** (aucun code exécutable). Il décrit à TypeScript la forme d'une bibliothèque écrite en **JavaScript**, ou publie les types d'une bibliothèque TypeScript.

| Source des types | Où |
| --- | --- |
| Incluse dans le paquet | Champ `"types"` (ou `"exports"`) du `package.json` |
| **DefinitelyTyped** | Paquets `@types/xxx` |
| Vos déclarations | Fichiers `.d.ts` du projet |

## 12.2 Générer des déclarations

```json
{ "compilerOptions": { "declaration": true, "declarationMap": true, "emitDeclarationOnly": false } }
```

`tsc` génère un `.d.ts` par `.ts`. Avec **`isolatedDeclarations`** (TS 5.5), les outils tiers peuvent générer les déclarations **fichier par fichier**, très vite, à condition que les types exportés soient annotés explicitement.

## 12.3 DefinitelyTyped : `@types`

```bash
npm install -D @types/node @types/express @types/lodash
```

**TS 6.0** : l'option **`types` vaut `[]` par défaut** : les paquets `@types/*` ne sont **plus chargés automatiquement**. Listez ceux dont vous avez besoin (surtout les **globaux** : Node, Jest, Vitest) :

```json
{ "compilerOptions": { "types": ["node", "vitest/globals"] } }
```

Les `import` explicites (`import express from 'express'`) chargent leurs types sans passer par `types`.

## 12.4 Où TypeScript cherche-t-il les types ?

1. Les types **fournis par le paquet** (`types` / `exports` dans `package.json`).
2. Les paquets **`@types/...`** listés dans `types` (ou importés explicitement).
3. Les `.d.ts` inclus par `include`/`files` et les `typeRoots`.

## 12.5 Écrire ses propres déclarations

### Module sans types

```typescript
// types/ancienne-lib.d.ts
declare module 'ancienne-lib' {
    export function faire(x: number): string;
    export const version: string;
    export default function creer(options?: { debug?: boolean }): void;
}

declare module '*.svg' {              // fichiers non-code importés par un bundler
    const url: string;
    export default url;
}
declare module '*.module.css' {
    const classes: Record<string, string>;
    export default classes;
}
```

Pour débloquer rapidement une lib sans types : `declare module 'ancienne-lib';` (tout est `any`), puis affinez.

### Variables et fonctions globales

```typescript
// types/global.d.ts
declare const VERSION_APP: string;                  // injectée par le bundler
declare function ga(commande: string, ...args: unknown[]): void;

interface Window { dataLayer: unknown[]; monApp: { version: string } } // fusion de déclarations
```

### Augmentation de modules

```typescript
// types/express.d.ts
import 'express';

declare module 'express-serve-static-core' {
    interface Request {
        utilisateur?: { id: number; role: 'admin' | 'membre' };
    }
}
```

**Règle de portée** : un `.d.ts` **sans** `import`/`export` est **global** ; avec `import`/`export`, c'est un **module** et ses déclarations ne sont plus globales : utilisez `declare global { ... }`.

```typescript
export {};   // force le statut de module
declare global {
    interface Array<T> { dernier(): T | undefined }
}
```

L'implémentation réelle (`Array.prototype.dernier = ...`) doit exister séparément : un `.d.ts` n'ajoute que des types, jamais du comportement.

## 12.6 Configuration

```json
{
    "compilerOptions": { "typeRoots": ["./node_modules/@types", "./types"], "skipLibCheck": true },
    "include": ["src", "types"]
}
```

`skipLibCheck: true` accélère la compilation en ignorant la vérification interne des `.d.ts` de vos dépendances (ne masque pas les erreurs dans **votre** code).

## 12.7 Conseils

- **Ne modifiez jamais** `node_modules/@types` : utilisez l'augmentation.
- Gardez vos `.d.ts` **petits et ciblés** dans un dossier `types/`.
- Bibliothèque sans types : cherchez `@types/...`, sinon écrivez un `declare module` minimal, puis améliorez-le.
- Pour **publier** : générez et distribuez les `.d.ts` (`types` et `exports` dans `package.json`).
- Utilisez les directives triple-barre (`/// <reference types="..." />`) uniquement pour des cas particuliers de fichiers globaux.

## Points clés du module 12

- `.d.ts` = types seulement ; `@types/*` pour les bibliothèques JS ; depuis TS 6, `types` explicite.
- `declare module`, `declare global` et la fusion d'interfaces permettent d'enrichir.
- Un `.d.ts` avec import/export est un module, sans c'est un script global.

---

# NIVEAU AVANCÉ

---

# 13. Types utilitaires

**Objectifs** : connaître et composer tous les types utilitaires intégrés, comprendre comment ils sont construits, et écrire les siens.

## 13.1 Les types intégrés

TypeScript fournit des **types utilitaires** globaux, construits avec les outils du module 11 (mappés, conditionnels, `infer`).

| Utilitaire | Rôle | Exemple |
| --- | --- | --- |
| `Partial<T>` | Toutes les propriétés **optionnelles** | `Partial<Utilisateur>` |
| `Required<T>` | Toutes **obligatoires** (retire `?`) | `Required<Config>` |
| `Readonly<T>` | Toutes **en lecture seule** | `Readonly<Point>` |
| `Pick<T, K>` | **Sélectionne** les propriétés `K` | `Pick<U, 'id' \| 'nom'>` |
| `Omit<T, K>` | **Exclut** les propriétés `K` | `Omit<U, 'motDePasse'>` |
| `Record<K, V>` | Objet de clés `K` vers valeurs `V` | `Record<string, number>` |
| `Exclude<U, E>` | Retire de l'union `U` les membres assignables à `E` | `Exclude<'a' \| 'b', 'a'>` → `'b'` |
| `Extract<U, E>` | Garde les membres de `U` assignables à `E` | `Extract<string \| number, number>` → `number` |
| `NonNullable<T>` | Retire `null` et `undefined` |  |
| `ReturnType<F>` | Type de retour d'une fonction | `ReturnType<typeof f>` |
| `Parameters<F>` | Tuple des paramètres |  |
| `ConstructorParameters<C>` | Paramètres d'un constructeur |  |
| `InstanceType<C>` | Type de l'instance d'une classe |  |
| `Awaited<T>` | Type « déballé » d'une promesse (récursif) | `Awaited<Promise<string>>` → `string` |
| `NoInfer<T>` | Bloque l'inférence (TS 5.4) |  |
| `ThisParameterType<F>` / `OmitThisParameter<F>` | Manipulent `this` |  |
| `Uppercase`, `Lowercase`, `Capitalize`, `Uncapitalize` | Chaînes littérales |  |

### Comment ils sont définis (pour comprendre)

```typescript
type MonPartial<T> = { [K in keyof T]?: T[K] };
type MonPick<T, K extends keyof T> = { [P in K]: T[P] };
type MonRecord<K extends keyof any, V> = { [P in K]: V };
type MonExclude<T, U> = T extends U ? never : T;     // conditionnel distributif
type MonOmit<T, K extends keyof any> = Pick<T, Exclude<keyof T, K>>;
type MonReturnType<T extends (...a: any) => any> = T extends (...a: any) => infer R ? R : any;
```

### Exemple d'ensemble

```typescript
interface Utilisateur {
    id: number;
    nom: string;
    email: string;
    motDePasse: string;
}

type MiseAJour = Partial<Omit<Utilisateur, 'id'>>;      // modification : tout optionnel, sans id
type UtilisateurPublic = Omit<Utilisateur, 'motDePasse'>;
type Resume = Pick<Utilisateur, 'id' | 'nom'>;
type ParId = Record<number, Utilisateur>;
type Permissions = Record<'lire' | 'ecrire' | 'supprimer', boolean>;

async function charger() { return { ok: true, donnees: [1, 2] }; }
type Charge = Awaited<ReturnType<typeof charger>>;       // { ok: boolean; donnees: number[] }
```

**Attention aux nuances**

- `Omit` n'impose **pas** que `K` soit une clé de `T` (pas d'erreur de frappe détectée) : une faute dans `Omit<U, 'motDePasee'>` passe silencieusement. `Pick`, lui, exige `K extends keyof T`.
- `Omit` n'est pas **distributif** sur une union : `Omit<A | B, 'x'>` perd la discrimination. Utilisez un `type OmitDistrib<T, K extends PropertyKey> = T extends unknown ? Omit<T, K> : never`.
- `Readonly`, `Partial` et `Required` sont **superficiels** (premier niveau).
- `Record<string, V>` + `noUncheckedIndexedAccess` donne `V | undefined`.

## 13.2 Combiner des utilitaires

```typescript
type PartielProfond<T> = { [K in keyof T]?: T[K] extends object ? PartielProfond<T[K]> : T[K] };
type RendreOptionnel<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>;
type RendreRequis<T, K extends keyof T> = Omit<T, K> & Required<Pick<T, K>>;
type Valeurs<T> = T[keyof T];
type CleDeType<T, V> = { [K in keyof T]: T[K] extends V ? K : never }[keyof T];
type Fusion<A, B> = Omit<A, keyof B> & B;
type Aplati<T> = { [K in keyof T]: T[K] } & {};  // simplifie l'affichage d'intersections
```

`Aplati` (ou *Prettify*) ne change pas la sémantique mais produit un type d'affichage lisible dans l'éditeur.

## 13.3 Cas d'usage

| Besoin | Solution |
| --- | --- |
| Formulaire de **modification** | `Partial<T>` |
| Masquer des champs sensibles | `Omit<T, 'motDePasse'>` |
| DTO de création sans `id` | `Omit<T, 'id' \| 'creeLe'>` |
| Table de correspondance | `Record<Cle, Valeur>` (exhaustive si `Cle` est une union) |
| Typer le résultat d'une fonction | `ReturnType<typeof f>` / `Awaited<...>` |
| Props d'un composant dérivées d'un autre | `ComponentProps<typeof X>` (React) |
| Figer une configuration | `Readonly<T>` / `as const` |

`Record<Union, V>` est un excellent outil d'**exhaustivité** : si vous ajoutez un membre à l'union, tous les `Record` correspondants signalent l'oubli.

## 13.4 Écrire ses propres utilitaires

```typescript
type Egaux<A, B> =
    (<T>() => T extends A ? 1 : 2) extends (<T>() => T extends B ? 1 : 2) ? true : false;
type Test = Egaux<Pick<{ a: 1; b: 2 }, 'a'>, { a: 1 }>; // true
```

Ce test d'égalité « strict » sert aux tests de types (23.5). Bonnes pratiques : nommer clairement, documenter par un commentaire TSDoc, tester sur des cas limites (`never`, `any`, unions, optionnels, `readonly`).

## Points clés du module 13

- Les utilitaires sont des types mappés/conditionnels : savoir les relire aide à les composer.
- `Pick` vérifie les clés, `Omit` non ; `Omit` n'est pas distributif.
- `Record` sur une union de clés garantit l'exhaustivité.

---

# 14. Décorateurs

**Objectifs** : comprendre les deux générations de décorateurs, écrire des décorateurs standard (classe, méthode, champ), connaître les décorateurs historiques utilisés par Angular/NestJS/TypeORM, et savoir quand les utiliser.

## 14.1 Deux versions à distinguer

Un **décorateur** est une **fonction** appliquée à une classe ou à un de ses membres avec la syntaxe `@nom`, pour **observer, modifier ou remplacer** l'élément décoré.

|  | Décorateurs **standard** (TC39) | Décorateurs **expérimentaux** (historiques) |
| --- | --- | --- |
| Activation | **Aucune** (TS 5.0+) | `"experimentalDecorators": true` |
| Signature | `(valeur, contexte)` | `(cible, nomPropriete, descripteur)` |
| Décorateurs de **paramètres** | Non | Oui |
| Métadonnées de types (`emitDecoratorMetadata`) | Non | Oui |
| Utilisés par | Nouveau code, bibliothèques récentes | **Angular, NestJS, TypeORM**, class-validator |

Les deux modèles sont **incompatibles** : un décorateur écrit pour l'un ne fonctionne pas avec l'autre. Vérifiez ce qu'exige votre framework avant de choisir.

## 14.2 Décorateurs standard (TS 5.x)

Un décorateur standard reçoit la **valeur décorée** (classe, méthode, accesseur…) et un objet **contexte**, et peut **renvoyer un remplaçant**.

### Décorateur de classe

```typescript
function journalise<T extends new (...args: any[]) => object>(
    cible: T,
    contexte: ClassDecoratorContext,
) {
    console.log(`Classe ${String(contexte.name)} définie`);
    return class extends cible {
        constructor(...args: any[]) {
            super(...args);
            console.log('Instance créée');
        }
    };
}

@journalise
class Service {}
new Service();
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

La signature générique préserve les types de la méthode décorée.

### Décorateur de champ et `accessor`

```typescript
function valeurParDefaut<T>(defaut: T) {   // fabrique de décorateur : fonction qui RENVOIE un décorateur
    return function (_: undefined, contexte: ClassFieldDecoratorContext) {
        return (valeurInitiale: T | undefined) => valeurInitiale ?? defaut; // transforme la valeur initiale
    };
}

class Options {
    @valeurParDefaut(8080) port?: number;
}
```

Avec le mot-clé `accessor`, un décorateur peut intercepter `get`/`set` d'un champ (`ClassAccessorDecoratorContext`).

### Contexte et initialiseurs

L'objet **contexte** fournit : `kind` (`'class'`, `'method'`, `'getter'`, `'setter'`, `'field'`, `'accessor'`), `name`, `static`, `private`, `access` (lecture/écriture), `addInitializer()` (code exécuté à l'initialisation) et `metadata` (données partagées entre décorateurs d'une classe).

```typescript
function lie(_: unknown, contexte: ClassMethodDecoratorContext) {
    contexte.addInitializer(function (this: any) {
        this[contexte.name] = this[contexte.name].bind(this);
    });
}

class Bouton {
    etiquette = 'OK';
    @lie cliquer() { console.log(this.etiquette); }
}
const { cliquer } = new Bouton();
cliquer(); // `this` reste lié
```

**Ordre d'évaluation** : les expressions de décorateurs sont évaluées de haut en bas, et les décorateurs eux-mêmes appliqués de **bas en haut** (composition de fonctions) ; membres avant la classe.

## 14.3 Décorateurs expérimentaux (hérités)

```json
{ "compilerOptions": { "experimentalDecorators": true, "emitDecoratorMetadata": true } }
```

```typescript
import 'reflect-metadata';

function Controller(prefixe: string): ClassDecorator {
    return (cible) => { Reflect.defineMetadata('prefixe', prefixe, cible); };
}
function Get(chemin: string): MethodDecorator {
    return (cible, cle, descripteur) => { console.log(`Route GET ${chemin} -> ${String(cle)}`); };
}
function Valide(cible: Object, cle: string | symbol, indice: number) { /* décorateur de paramètre */ }

@Controller('/users')
class UsersController {
    @Get('/') liste() { return []; }
}
```

Avec `emitDecoratorMetadata`, TypeScript émet les **types de conception** (`design:type`, `design:paramtypes`) lus par `reflect-metadata` : c'est le mécanisme de l'**injection de dépendances** d'Angular et NestJS (le conteneur sait quel service injecter d'après le type du paramètre du constructeur).

Ces décorateurs ne sont **pas standard** ; leur avenir dépend de la migration des frameworks.

## 14.4 Cas d'usage

| Usage | Exemple |
| --- | --- |
| Journalisation / mesure | `@chronometre`, `@journalise` |
| Injection de dépendances | `@Injectable()` (Angular, NestJS) |
| Routage | `@Controller()`, `@Get()` |
| Validation | `@IsEmail()` (class-validator) |
| Persistance | `@Entity()`, `@Column()` (TypeORM) |
| Mémoïsation, anti-rebond | `@memo`, `@debounce` |
| Liaison de `this` | `@lie`, `@autobind` |

## 14.5 Bonnes pratiques

- Gardez les décorateurs **simples et sans effets de bord cachés**.
- **Documentez** leur comportement : ils sont « magiques » et rendent le flux moins visible.
- Hors framework imposé, préférez les décorateurs **standard**, ou des **fonctions d'ordre supérieur** et la **composition**, souvent plus explicites.

## Points clés du module 14

- Standard : `(valeur, contexte)`, sans option ; historiques : `experimentalDecorators` + métadonnées.
- Une **fabrique** de décorateur permet de paramétrer (`@Get('/')`).
- Angular, NestJS, TypeORM reposent encore sur l'ancien modèle.

---

# 15. Programmation asynchrone

**Objectifs** : typer promesses, `async`/`await`, erreurs, parallélisme, annulation, générateurs asynchrones, rappels, et connaître RxJS.

## 15.1 Promesses typées

Une **`Promise<T>`** représente une valeur de type `T` disponible **plus tard** (ou une erreur). Trois états : *pending*, *fulfilled*, *rejected*.

```typescript
function attendre(ms: number): Promise<void> {
    return new Promise((resolve) => setTimeout(resolve, ms));
}

function chargerNombre(): Promise<number> {
    return new Promise((resolve, reject) => {
        Math.random() > 0.5 ? resolve(42) : reject(new Error('Échec'));
    });
}

chargerNombre()
    .then((n) => n * 2)                 // Promise<number>
    .catch((e: unknown) => console.error(e))
    .finally(() => console.log('Terminé'));
```

`then` renvoie une nouvelle promesse dont le type dépend de la valeur retournée (aplatie automatiquement si c'est une promesse). Le type `Awaited<T>` modélise ce « déballage ». Le `reason` d'un rejet est de type `any`/`unknown`.

## 15.2 `async` / `await`

Une fonction `async` **renvoie toujours une promesse** ; son type de retour s'écrit `Promise<T>`. `await` suspend la fonction jusqu'à résolution et **déballe** la valeur.

```typescript
interface Utilisateur { id: number; nom: string }

async function chargerUtilisateur(id: number): Promise<Utilisateur> {
    const reponse = await fetch(`https://api.exemple.com/users/${id}`);
    if (!reponse.ok) throw new Error(`HTTP ${reponse.status}`); // fetch ne rejette PAS sur un 404
    return (await reponse.json()) as Utilisateur;
}

const u = await chargerUtilisateur(1); // await de haut niveau, dans un module ES
```

Points à retenir : un `await` de haut niveau (*top-level await*) exige un module ES et `target`/`module` adaptés ; `fetch` ne rejette que sur erreur réseau (testez `reponse.ok`).

## 15.3 Gérer les erreurs

Avec `strict` (`useUnknownInCatchVariables`), la variable du `catch` est de type **`unknown`** : il faut la **restreindre**.

```typescript
try {
    await chargerUtilisateur(-1);
} catch (erreur) {                 // unknown
    if (erreur instanceof Error) console.error(erreur.message);
    else console.error('Erreur inconnue', erreur);
}

function messageDErreur(e: unknown): string {
    return e instanceof Error ? e.message : String(e);
}
```

Tout peut être levé en JavaScript (`throw 'texte'`, `throw 42`) : c'est pourquoi `unknown` est le type honnête.

### Le motif « résultat » (alternative aux exceptions)

```typescript
type Resultat<T, E = Error> = { ok: true; valeur: T } | { ok: false; erreur: E };

async function essayer<T>(promesse: Promise<T>): Promise<Resultat<T>> {
    try { return { ok: true, valeur: await promesse }; }
    catch (e) { return { ok: false, erreur: e instanceof Error ? e : new Error(String(e)) }; }
}

const r = await essayer(chargerUtilisateur(1));
if (r.ok) console.log(r.valeur.nom); else console.error(r.erreur.message);
```

Avantage : l'erreur apparaît **dans le type** et le compilateur oblige à la traiter ; inconvénient : plus verbeux. Les exceptions restent adaptées aux erreurs **inattendues**.

## 15.4 Exécution parallèle

```typescript
// Séquentiel (lent) : attend A avant de lancer B
const a = await chargerUtilisateur(1);
const b = await chargerUtilisateur(2);

// Parallèle : les types sont conservés dans un tuple
const [u1, u2] = await Promise.all([chargerUtilisateur(1), chargerUtilisateur(2)]);

const resultats = await Promise.allSettled([chargerUtilisateur(1), chargerUtilisateur(-1)]);
for (const r of resultats) {
    if (r.status === 'fulfilled') console.log(r.value.nom);
    else console.error(r.reason);
}

const premier = await Promise.race([chargerUtilisateur(1), attendre(1000).then(() => null)]);
const premiereReussite = await Promise.any([chargerUtilisateur(1), chargerUtilisateur(2)]);
```

| Méthode | Comportement |
| --- | --- |
| `Promise.all` | Toutes réussissent, sinon rejette dès la première échec |
| `Promise.allSettled` | Attend toutes ; renvoie l'état de chacune |
| `Promise.race` | La première **terminée** (réussite ou échec) |
| `Promise.any` | La première **réussie** (rejette si toutes échouent) |
| `Promise.try` (ES2025) | Enveloppe une fonction sync/async dans une promesse |

## 15.5 Annulation et délai d'expiration

```typescript
async function chargerAvecDelai(url: string, ms = 5000): Promise<unknown> {
    const reponse = await fetch(url, { signal: AbortSignal.timeout(ms) });
    return reponse.json();
}

const controleur = new AbortController();
const requete = fetch('/api/long', { signal: controleur.signal });
controleur.abort(); // le fetch rejette avec une AbortError
```

`AbortController`/`AbortSignal` est le mécanisme standard d'annulation (fetch, flux, vos propres fonctions via un paramètre `signal?: AbortSignal`).

## 15.6 Itérateurs et générateurs asynchrones

```typescript
async function* paginer<T>(charger: (page: number) => Promise<T[]>): AsyncGenerator<T[], void, void> {
    for (let page = 1; ; page++) {
        const lot = await charger(page);
        if (lot.length === 0) return;
        yield lot;
    }
}

for await (const lot of paginer(chargerPage)) console.log(lot.length);
```

`AsyncGenerator<T, TReturn, TNext>` décrit les valeurs produites, la valeur finale et la valeur reçue par `next()`. `for await...of` consomme tout `AsyncIterable<T>`.

## 15.7 Rappels (*callbacks*) et conversion en promesses

```typescript
import { promisify } from 'node:util';
import * as fs from 'node:fs';

type Rappel<T> = (erreur: Error | null, donnees?: T) => void;
const lireFichier = promisify(fs.readFile);   // convertit un callback Node en promesse
// ou : import { readFile } from 'node:fs/promises';
```

## 15.8 Programmation réactive avec RxJS

```typescript
import { fromEvent, debounceTime, map, distinctUntilChanged, switchMap } from 'rxjs';
import { ajax } from 'rxjs/ajax';

const champ = document.querySelector<HTMLInputElement>('#recherche')!;
fromEvent(champ, 'input').pipe(
    debounceTime(300),
    map(() => champ.value),
    distinctUntilChanged(),
    switchMap((texte) => ajax.getJSON<{ resultats: string[] }>(`/api/recherche?q=${texte}`)),
).subscribe(({ resultats }) => console.log(resultats));
```

Une `Observable<T>` est un **flux** de valeurs dans le temps (plusieurs valeurs, annulable), là où une `Promise<T>` n'en produit qu'**une**. Utile pour saisie, WebSockets, événements ; omniprésent dans Angular. Pour de simples requêtes, `async/await` suffit.

## 15.9 Bonnes pratiques

- **Toujours** gérer les erreurs ; jamais de promesse **flottante** (règle ESLint `no-floating-promises`).
- Paralléliser avec `Promise.all` les tâches **indépendantes**.
- Pas d'`await` dans un `forEach` : utilisez `for...of` ou `Promise.all(tableau.map(...))`.
- **Valider** les données reçues : le type générique de `json()` n'est qu'une promesse.
- Définir des **délais d'expiration** et permettre l'**annulation**.

## Points clés du module 15

- `Promise<T>` et `async` sont typés ; `catch` donne `unknown`.
- `Promise.all` conserve les types dans un tuple.
- `AbortSignal` pour annuler, `async function*` pour flux paginables.

---

# 16. Manipuler le DOM

**Objectifs** : typer les éléments et événements du DOM, gérer `null`, créer des éléments génériques, typer des événements personnalisés et les API du navigateur.

> Les exemples de ce module s'exécutent dans un **navigateur** (ils utilisent `document` et `window`).

## 16.1 Typer les éléments

La bibliothèque de types **`lib.dom`** décrit tout le DOM. Activez-la dans le `tsconfig` : `"lib": ["es2023", "dom", "dom.iterable"]`.

Hiérarchie utile : `EventTarget` → `Node` → `Element` → `HTMLElement` → `HTMLInputElement`, `HTMLButtonElement`, `HTMLCanvasElement`…

```typescript
const bouton = document.getElementById('envoyer');          // HTMLElement | null
const champ = document.querySelector('#nom');                // Element | null

// Générique : précise le type attendu (sans assertion)
const entree = document.querySelector<HTMLInputElement>('#nom');
if (entree) console.log(entree.value);

// Le nom de balise donne le type exact
const lien = document.querySelector('a');                     // HTMLAnchorElement | null
const items = document.querySelectorAll<HTMLLIElement>('li'); // NodeListOf<HTMLLIElement>
const canvas = document.createElement('canvas');              // HTMLCanvasElement
```

Les surcharges de `querySelector('a')` et `createElement('canvas')` s'appuient sur l'interface `HTMLElementTagNameMap` (nom de balise → type). Pour un sélecteur CSS arbitraire (`'#nom'`), TypeScript ne peut pas deviner : on précise via le générique, qui reste une **promesse** du développeur.

## 16.2 Gestion de la valeur `null`

```typescript
const titre = document.querySelector('h1');
// titre.textContent = 'x'; // ERREUR : possiblement null
if (titre) titre.textContent = 'Bonjour';   // restriction
titre?.classList.add('actif');               // chaînage optionnel

function requis<T extends Element>(selecteur: string): T {
    const el = document.querySelector<T>(selecteur);
    if (!el) throw new Error(`Élément introuvable : ${selecteur}`);
    return el;
}
const app = requis<HTMLDivElement>('#app');
```

Évitez l'assertion non nulle `!` : un utilitaire qui lève une erreur **explicite** facilite le débogage et reste sûr au niveau des types.

## 16.3 Événements typés

`addEventListener` est typé par `HTMLElementEventMap` / `DocumentEventMap` / `WindowEventMap` : le nom de l'événement détermine le type de l'objet reçu.

```typescript
const bouton = requis<HTMLButtonElement>('#envoyer');

bouton.addEventListener('click', (e) => {       // e : MouseEvent (inféré)
    console.log(e.clientX, e.clientY);
});

const entree = requis<HTMLInputElement>('#nom');
entree.addEventListener('input', (e) => {
    const cible = e.target as HTMLInputElement;  // e.target : EventTarget | null
    console.log(cible.value);
    console.log(e.currentTarget.value);          // currentTarget : l'élément écouté, bien typé
});

document.addEventListener('keydown', (e: KeyboardEvent) => {
    if (e.key === 'Escape') { /* … */ }
});

document.querySelector<HTMLFormElement>('form')?.addEventListener('submit', (e: SubmitEvent) => {
    e.preventDefault();
    const donnees = new FormData(e.target as HTMLFormElement);
    console.log(Object.fromEntries(donnees));
});
```

**`target` ou `currentTarget` ?** `target` est l'élément qui a **déclenché** l'événement (potentiellement un enfant) ; `currentTarget` est celui qui **porte l'écouteur**. Son type est précis, d'où sa préférence.

| Événement | Type |
| --- | --- |
| `click`, `mousemove` | `MouseEvent` |
| `pointerdown` | `PointerEvent` |
| `keydown`, `keyup` | `KeyboardEvent` |
| `input` | `InputEvent` |
| `change` | `Event` |
| `submit` | `SubmitEvent` |
| `focus`, `blur` | `FocusEvent` |
| `drag*` | `DragEvent` |
| Personnalisé | `CustomEvent<T>` |

## 16.4 Événements personnalisés typés

```typescript
interface EvenementsApp { 'panier:ajout': CustomEvent<{ id: number }> }

declare global {
    interface DocumentEventMap extends EvenementsApp {}  // HTMLElementEventMap pour un élément
}

document.addEventListener('panier:ajout', (e) => console.log(e.detail.id)); // typé
document.dispatchEvent(new CustomEvent('panier:ajout', { detail: { id: 7 } }));
```

Par fusion de déclarations (module 6.5), on enrichit la table des événements connus.

## 16.5 Créer et modifier des éléments

```typescript
function creer<K extends keyof HTMLElementTagNameMap>(
    balise: K,
    proprietes: Partial<HTMLElementTagNameMap[K]> = {},
): HTMLElementTagNameMap[K] {
    return Object.assign(document.createElement(balise), proprietes);
}

const lien = creer('a', { href: '/accueil', textContent: 'Accueil' }); // HTMLAnchorElement
document.body.append(lien);
```

Le générique `K extends keyof HTMLElementTagNameMap` relie la balise au type retourné : `creer('input')` donne `HTMLInputElement`, avec ses propriétés propres (`value`, `type`).

## 16.6 Observateurs et API du navigateur

`IntersectionObserver`, `ResizeObserver`, `MutationObserver`, `localStorage` (valeurs `string | null`), `fetch`, `FormData`, `URLSearchParams`, `AbortController`, `History`, `Canvas`, `WebSocket`, `Web Workers` sont tous typés.

```typescript
const stockage = {
    lire<T>(cle: string, defaut: T): T {
        try { return JSON.parse(localStorage.getItem(cle) ?? 'null') ?? defaut; }
        catch { return defaut; }
    },
    ecrire<T>(cle: string, valeur: T): void {
        localStorage.setItem(cle, JSON.stringify(valeur));
    },
};
```

Ce wrapper reste une **promesse** de type (le JSON stocké pourrait avoir une autre forme) : validez-le si la donnée est critique.

## 16.7 Bonnes pratiques

- `querySelector<T>()` plutôt que des assertions `as`.
- `textContent` plutôt que `innerHTML` pour du texte (prévention XSS).
- Délégation d'événements : un seul écouteur sur un parent, `e.target` restreint par `instanceof HTMLElement`.
- Pour des interfaces non triviales, utilisez un **framework** ou des **composants web** (modules 17 et 18).

## Points clés du module 16

- Les sélecteurs renvoient des types **nullables** : restreignez ou levez une erreur explicite.
- Le nom de l'événement détermine le type du paramètre ; `currentTarget` est bien typé.
- La fusion de déclarations étend les tables d'événements.

---

# 17. Mixins et composition

**Objectifs** : comprendre les limites de l'héritage simple, écrire des mixins de classes typés, composer par objets et par délégation, et savoir choisir.

## 17.1 Pourquoi ?

L'héritage simple limite une classe à **un seul parent** et engendre des hiérarchies rigides (problème du « gorille et de la banane » : on veut une banane, on obtient le gorille et toute la jungle). Deux réponses :

- les **mixins** : ajouter des comportements réutilisables à plusieurs classes ;
- la **composition** : assembler des objets plutôt que d'empiler des héritages.

> « Préférez la composition à l'héritage. »

## 17.2 Mixins de classes

Un **mixin** est une **fonction** qui prend une classe de base et renvoie une classe qui l'étend.

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

const UtilisateurAvance = Activable(Horodate(Utilisateur)); // composition de mixins
const u = new UtilisateurAvance('Alice');
u.activer();
u.toucher();
console.log(u.nom, u.actif, u.creeLe); // les types sont combinés
```

**Comment ça se type** : `Constructeur<T>` décrit n'importe quel constructeur. Le mixin est générique sur `TBase` ; la classe renvoyée a pour type l'**intersection** de `TBase` et des nouveaux membres. Le constructeur du mixin doit accepter `...args: any[]` (exigence du langage).

## 17.3 Mixins avec contraintes

Un mixin peut **exiger** certains membres de la classe de base :

```typescript
interface AvecNom { nom: string }

function Salutation<TBase extends Constructeur<AvecNom>>(Base: TBase) {
    return class extends Base {
        saluer() { return `Bonjour ${this.nom}`; } // `nom` garanti par la contrainte
    };
}

class Personne { constructor(public nom: string) {} }
const PersonneAimable = Salutation(Personne);
new PersonneAimable('Alice').saluer();
// Salutation(class {}); // ERREUR : pas de propriété 'nom'
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
```

On assemble des **capacités** par fusion d'objets ; le type est une **intersection**. Pas de hiérarchie, pas de `this` fragile.

### Composition par délégation (injection)

```typescript
interface Journal { ecrire(msg: string): void }

class Service {
    constructor(private readonly journal: Journal) {} // on « possède » un Journal, on ne l'« est » pas
    executer() { this.journal.ecrire('Exécution'); }
}

new Service({ ecrire: console.log }).executer();
```

Relation **« a un »** (composition) contre **« est un »** (héritage). Avantages : la dépendance est déclarée par une **interface**, remplacable (test, autre implémentation), et le couplage faible.

## 17.5 Pièges

| Piège | Remède |
| --- | --- |
| Conflits de noms entre mixins | Nommer précisément, tester |
| Ordre d'application (le dernier gagne) | Documenter l'ordre |
| Difficile à lire et à déboguer | Rester sobre : 2 à 3 mixins maximum |
| Mixins et membres `private`/`#champs` | Limites avec `declaration: true` (types de classes anonymes) |
| `instanceof` | Un mixin n'ajoute pas d'identité : utiliser `Symbol.hasInstance` ou des gardes |

## 17.6 Mixins ou composition ?

| Besoin | Choix |
| --- | --- |
| Ajouter méthodes et état à plusieurs classes | Mixins |
| Assembler des comportements indépendants | Composition d'objets |
| Remplacer un comportement à l'exécution | Délégation / stratégie (injection) |
| Hiérarchie claire « est un » | Héritage |

## Points clés du module 17

- Un mixin = fonction `Base => class extends Base`, typé avec `Constructeur<T>`.
- La composition d'objets et l'injection de dépendances réduisent le couplage.
- Rester sobre : trop de mixins nuit à la lisibilité.

---

# 18. TypeScript et frameworks front-end

**Objectifs** : démarrer un projet avec Vite, typer React, Angular et Vue, connaître les autres frameworks et adopter les bonnes pratiques de typage d'interface.

## 18.1 Démarrer un projet : Vite

`create-react-app` est **déprécié** (plus maintenu). On utilise **Vite** ou le méta-framework du choix (Next.js, React Router, Nuxt, SvelteKit, Astro, Angular CLI).

```bash
npm create vite@latest mon-app -- --template react-ts   # ou vue-ts, svelte-ts, vanilla-ts
cd mon-app && npm install && npm run dev
```

Vite **ne vérifie pas** les types (il les efface via esbuild/Oxc) : ajoutez `tsc --noEmit` (ou `vue-tsc --noEmit`) à vos scripts et à la CI. Le `tsconfig` d'un projet Vite utilise `moduleResolution: bundler`, `noEmit: true`, `verbatimModuleSyntax` et `isolatedModules` (module 20).

## 18.2 React

### Composants et props

```tsx
import { useState, useRef, useEffect, type ReactNode, type ChangeEvent } from 'react';

interface BoutonProps {
    etiquette: string;
    variante?: 'primaire' | 'secondaire';
    onClic?: () => void;
    children?: ReactNode;
}

function Bouton({ etiquette, variante = 'primaire', onClic, children }: BoutonProps) {
    return <button className={variante} onClick={onClic}>{etiquette}{children}</button>;
}
```

- Typez les **props** par une interface et une **fonction ordinaire** ; `React.FC` n'est plus nécessaire.
- Avec **React 19**, `ref` est une **prop ordinaire** (`ref?: Ref<HTMLInputElement>`) : `forwardRef` n'est plus requis pour les nouveaux composants.
- `ReactNode` : tout ce qui est rendable ; `ReactElement` : un élément JSX ; `PropsWithChildren<P>` ajoute `children`.

### Hooks

```tsx
interface Utilisateur { id: number; nom: string }

function Profil() {
    const [utilisateur, setUtilisateur] = useState<Utilisateur | null>(null); // type explicite si valeur initiale null
    const [compteur, setCompteur] = useState(0);                              // number (inféré)
    const champ = useRef<HTMLInputElement>(null);

    useEffect(() => {
        const controleur = new AbortController();
        fetch('/api/me', { signal: controleur.signal })
            .then((r) => r.json() as Promise<Utilisateur>)
            .then(setUtilisateur)
            .catch(() => {});
        return () => controleur.abort();   // nettoyage
    }, []);

    const surChangement = (e: ChangeEvent<HTMLInputElement>) => setCompteur(Number(e.target.value));

    return (
        <>
            <input ref={champ} onChange={surChangement} />
            <p>{utilisateur?.nom ?? 'Chargement…'} — {compteur}</p>
        </>
    );
}
```

Points : `useState<T | null>(null)` pour une valeur absente au départ ; `useRef<T>(null)` pour une référence DOM (type `RefObject<T | null>`) ; `useReducer` se type avec une **union discriminée** d'actions.

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

type Action = { type: 'incrementer' } | { type: 'fixer'; valeur: number };
function reducteur(etat: number, action: Action): number {
    switch (action.type) {
        case 'incrementer': return etat + 1;
        case 'fixer': return action.valeur;
    }
}
```

Types utiles : `ComponentProps<typeof X>`, `PropsWithChildren`, `ReactNode`, `MouseEvent<HTMLButtonElement>`, `FormEvent`, `CSSProperties`. **Context** : `createContext<Valeur | null>(null)` + un hook personnalisé qui vérifie la présence du fournisseur et lève une erreur sinon.

## 18.3 Angular

Angular est **écrit en TypeScript** et le **requiert**.

```bash
npm install -g @angular/cli
ng new mon-app
```

```typescript
import { Component, Injectable, inject, signal, computed, input } from '@angular/core';
import { HttpClient } from '@angular/common/http';

interface Tache { id: number; titre: string; faite: boolean }

@Injectable({ providedIn: 'root' })
export class TacheService {
    private readonly http = inject(HttpClient);
    lister() { return this.http.get<Tache[]>('/api/taches'); } // Observable<Tache[]>
}

@Component({
    selector: 'app-compteur',
    standalone: true,
    template: `<button (click)="incrementer()">{{ valeur() }} (double : {{ double() }})</button>`,
})
export class CompteurComponent {
    initial = input<number>(0);           // entrée typée basée sur les signaux
    valeur = signal(0);
    double = computed(() => this.valeur() * 2);
    incrementer() { this.valeur.update((v) => v + 1); }
}
```

À retenir (versions récentes) :

- **Composants autonomes** (*standalone*, par défaut), plus de `NgModule` obligatoire.
- **Signaux** : `signal`, `computed`, `effect`, `input()`, `output()`, `model()`.
- **`inject()`** pour l'injection de dépendances ; `HttpClient.get<T>` pour typer les réponses.
- Nouvelle syntaxe de **contrôle de flux** de gabarit (`@if`, `@for`, `@switch`).
- Mode **strict** (TypeScript et gabarits) activé par défaut dans les nouveaux projets.
- Les décorateurs d'Angular reposent sur la version **expérimentale** (module 14).

## 18.4 Vue

```bash
npm create vue@latest   # choisir « TypeScript »
```

```vue
<script setup lang="ts">
import { ref, computed } from 'vue';

interface Props { titre: string; compteurInitial?: number }
const props = withDefaults(defineProps<Props>(), { compteurInitial: 0 });
const emit = defineEmits<{ (e: 'change', valeur: number): void }>();

const compteur = ref<number>(props.compteurInitial);
const double = computed(() => compteur.value * 2);

function incrementer(): void {
    compteur.value++;
    emit('change', compteur.value);
}
</script>

<template>
    <button @click="incrementer">{{ titre }} : {{ compteur }} ({{ double }})</button>
</template>
```

- `defineProps<Props>()` et `defineEmits<...>()` utilisent des **types purs** (pas de déclaration d'exécution).
- `ref<T>()` et `computed()` sont génériques ; `defineModel<T>()` pour `v-model`.
- Utilisez **`vue-tsc`** pour vérifier les types (`vue-tsc --noEmit`) et l'extension **Vue (Volar)** dans VS Code.

## 18.5 Autres frameworks

| Framework | Notes TypeScript |
| --- | --- |
| **Next.js**, **React Router / Remix**, **Astro**, **Nuxt**, **SvelteKit** | TS intégré, routes et données typées |
| **Svelte** | `<script lang="ts">`, runes typées |
| **Solid**, **Qwik**, **Lit** (composants web) | TS de premier ordre |

## 18.6 Bonnes pratiques

- Activez `strict` ; typez **props, états et événements**.
- Dérivez les types des **données d'API** d'un schéma (OpenAPI, Zod, tRPC, GraphQL Codegen) plutôt que de les réécrire.
- Ne castez pas (`as`) les réponses : **validez-les**.
- **Unions discriminées** pour les états d'interface (`chargement | succes | erreur`).
- Placez les types partagés dans un module dédié pour éviter les dépendances circulaires.

## Points clés du module 18

- Vite (ou un méta-framework) pour démarrer ; il ne vérifie pas les types.
- React : interfaces de props, hooks génériques ; Angular : signaux et `inject()` ; Vue : `defineProps<T>()`.
- Les états d'interface se modélisent en unions discriminées.

---

# 19. TypeScript côté serveur

**Objectifs** : configurer et exécuter un projet Node.js en TypeScript, typer une API Express, découvrir NestJS, centraliser les erreurs, et surtout **valider les données à l'exécution**.

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
| Développement avec rechargement | `tsx watch src/index.ts` ou `node --watch src/index.ts` |
| Exécution directe sans dépendance | `node src/index.ts` (effacement des types, Node.js 22.18+/24) |
| Production | Compiler (`tsc`) puis `node dist/index.js` |
| `ts-node` | Moins utilisé aujourd'hui (plus lent, configuration ESM délicate) |

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

Le script `typecheck` est **indispensable** : `tsx` et l'exécution native de Node.js n'effectuent aucune vérification de types.

## 19.2 Express (v5)

```typescript
// src/index.ts
import express, { type Request, type Response, type NextFunction } from 'express';

const app = express();
app.use(express.json());

interface Utilisateur { id: number; nom: string }
const utilisateurs: Utilisateur[] = [{ id: 1, nom: 'Alice' }];

// Request<Params, ResBody, ReqBody, Query>
app.get('/users/:id', (req: Request<{ id: string }>, res: Response<Utilisateur | { erreur: string }>) => {
    const u = utilisateurs.find((x) => x.id === Number(req.params.id));
    if (!u) return void res.status(404).json({ erreur: 'Introuvable' });
    res.json(u);
});

app.post('/users', async (req: Request<{}, Utilisateur, { nom: string }>, res) => {
    const nouveau = { id: utilisateurs.length + 1, nom: req.body.nom };
    utilisateurs.push(nouveau);
    res.status(201).json(nouveau);
});

app.use((err: unknown, _req: Request, res: Response, _next: NextFunction) => {
    console.error(err);
    res.status(500).json({ erreur: 'Erreur interne' });
});

app.listen(3000, () => console.log('Serveur sur http://localhost:3000'));
```

- Les quatre paramètres génériques de `Request<Params, ResBody, ReqBody, Query>` typent l'URL, la réponse, le corps et la chaîne de requête.
- **Les paramètres d'URL sont toujours des `string`** : convertissez et validez.
- **Express 5** transmet automatiquement au gestionnaire d'erreurs les rejets des gestionnaires `async` ; avec Express 4 il fallait `next(err)` ou un enrobage.
- `req.body` **n'est pas vérifié** à l'exécution : le type est une promesse. Validez-le (19.5).

Alternatives très typées : **Fastify** (schémas JSON), **Hono**, **Elysia**, **tRPC** (types partagés client-serveur sans génération de code).

## 19.3 NestJS

Framework **TypeScript d'abord** (architecture modulaire inspirée d'Angular : modules, contrôleurs, services, injection de dépendances).

```bash
npm i -g @nestjs/cli
nest new mon-api
```

```typescript
import { Controller, Get, Post, Body, Param, ParseIntPipe, Injectable, NotFoundException, Module } from '@nestjs/common';
import { IsString, MinLength } from 'class-validator';

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

@Controller('users')
export class UtilisateursController {
    constructor(private readonly service: UtilisateursService) {} // injection de dépendances

    @Get(':id')
    un(@Param('id', ParseIntPipe) id: number) { return this.service.trouver(id); }

    @Post()
    creer(@Body() dto: CreerUtilisateurDto) { return this.service.creer(dto); }
}

@Module({ controllers: [UtilisateursController], providers: [UtilisateursService] })
export class UtilisateursModule {}
```

Concepts : **module** (regroupe), **contrôleur** (routes), **fournisseur/service** (logique, injectable), **pipe** (transformation/validation), **guard** (autorisation), **intercepteur**, **filtre d'exceptions**. NestJS s'appuie sur les décorateurs **expérimentaux** et `emitDecoratorMetadata` (module 14). Le `ValidationPipe` global avec `class-validator` valide les DTO à l'exécution.

## 19.4 Gestion des erreurs côté serveur

```typescript
export class ErreurHttp extends Error {
    constructor(public readonly statut: number, message: string, options?: ErrorOptions) {
        super(message, options);           // ErrorOptions : { cause } (ES2022)
        this.name = new.target.name;
    }
}
export class NonTrouve extends ErreurHttp {
    constructor(ressource: string) { super(404, `${ressource} introuvable`); }
}
export class RequeteInvalide extends ErreurHttp {
    constructor(detail: string) { super(400, detail); }
}

app.use((err: unknown, _req: Request, res: Response, _next: NextFunction) => {
    if (err instanceof ErreurHttp) return void res.status(err.statut).json({ erreur: err.message });
    console.error(err);
    res.status(500).json({ erreur: 'Erreur interne' });
});
```

Principes : des **classes d'erreur** typées avec un statut ; un **gestionnaire centralisé** ; la cause originale conservée (`cause`) ; **jamais** de trace de pile renvoyée au client.

## 19.5 Valider les données : types **et** exécution

Les types sont **effacés** : une API qui reçoit `{ "age": "abc" }` ne plante pas à la compilation. Utilisez un **schéma** qui **valide à l'exécution** et **produit** le type TypeScript, donc une seule source de vérité :

```typescript
import { z } from 'zod';   // ou Valibot, ArkType…

const CreerUtilisateur = z.object({
    nom: z.string().min(2),
    email: z.email(),
    age: z.number().int().min(0).optional(),
});
type CreerUtilisateur = z.infer<typeof CreerUtilisateur>; // type dérivé du schéma

app.post('/users', (req, res) => {
    const resultat = CreerUtilisateur.safeParse(req.body);
    if (!resultat.success) return void res.status(400).json({ erreurs: resultat.error.issues });
    const donnees: CreerUtilisateur = resultat.data;   // entièrement typé ET validé
    res.status(201).json(donnees);
});
```

À valider également :

- les **variables d'environnement** (`process.env.X` vaut `string | undefined`) ;
- les **fichiers de configuration** ;
- les **réponses d'API tierces** ;
- les **messages** d'une file ou d'un WebSocket.

`parse` lève une exception, `safeParse` renvoie un résultat discriminé (`success: true | false`). Les schémas peuvent aussi transformer (`z.coerce.number()`) et fournir des valeurs par défaut.

## 19.6 Bonnes pratiques serveur

- Séparez **routes → services → accès aux données** (architecture en couches).
- Typez les **DTO** (entrées/sorties) et validez-les ; ne renvoyez pas directement les entités de base de données.
- Centralisez la **gestion d'erreurs** et la **journalisation** structurée.
- Configurez `"types": ["node"]` et des `target`/`lib` cohérents avec la version de Node.js.
- Vérifiez les types **en CI** : `tsc --noEmit`.
- Arrêt propre : gérez `SIGTERM`, fermez les connexions.

## Points clés du module 19

- `tsx`/Node exécutent sans vérifier ; `tsc --noEmit` vérifie.
- Les paramètres génériques de `Request` typent l'API, mais ne la **valident** pas.
- Un schéma (Zod) donne validation + type : **source unique de vérité**.

---

# 20. Configuration du projet (`tsconfig.json`)

**Objectifs** : comprendre le rôle de `tsconfig.json`, connaître les défauts de TS 6.0 et les options supprimées en TS 7, maîtriser les options essentielles, la résolution des modules, les alias et l'héritage de configurations.

## 20.1 Rôle

Le fichier **`tsconfig.json`** définit la **racine du projet**, **quels fichiers** sont inclus et **avec quelles options** ils sont compilés. `npx tsc --init` en génère un exemple.

```json
{
    "compilerOptions": { /* options */ },
    "include": ["src"],
    "exclude": ["node_modules", "dist"]
}
```

`include`/`exclude` acceptent des motifs *glob* ; `files` liste des fichiers précis. Le fichier est du JSON **avec commentaires** et virgules finales tolérées.

## 20.2 Nouveaux défauts de TypeScript 6.0

| Option | Défaut avant | **Défaut en TS 6.0** |
| --- | --- | --- |
| `strict` | `false` | **`true`** |
| `module` | `commonjs` | **`esnext`** |
| `target` | `es5` (ancien) | **version ES de l'année (`es2025`)** |
| `types` | tous les `@types/*` auto-chargés | **`[]`** (à lister explicitement) |
| `rootDir` | racine des sources calculée | **`.`** (dossier du `tsconfig`) |
| `noUncheckedSideEffectImports` | `false` | **`true`** |
| `esModuleInterop`, `allowSyntheticDefaultImports` | `false` | **toujours `true`** (`false` déprécié) |

### Options dépréciées en 6.0, supprimées en 7.0

| Option dépréciée | Remplacement |
| --- | --- |
| `target: 'es5'`, `downlevelIteration` | `es2015` ou plus (un transpileur si besoin) |
| `moduleResolution: 'node'` (node10) et `'classic'` | `'bundler'` ou `'nodenext'` |
| `module: 'amd'`, `'umd'`, `'system'`, `'none'` | `esnext` / `nodenext` + bundler |
| `baseUrl` | `paths` avec chemins relatifs |
| `outFile` | Un bundler (Vite, esbuild…) |
| `alwaysStrict: false` | `strict` |
| Syntaxe `module Nom {}` | `namespace Nom {}` |
| `import ... assert { type: 'json' }` | `import ... with { type: 'json' }` |

Pour migrer progressivement vers TS 6 : `"ignoreDeprecations": "6.0"`. **TypeScript 7.0 ne prend plus en charge ces options** : corrigez-les avant de passer au compilateur natif.

## 20.3 Options essentielles

| Catégorie | Option | Rôle |
| --- | --- | --- |
| **Cible** | `target` | Version de JavaScript générée (`es2022`, `es2023`, `esnext`) |
|  | `lib` | Bibliothèques de types disponibles (`['es2023','dom','dom.iterable']`) |
| **Modules** | `module` | `nodenext` (Node.js), `esnext`/`preserve` (bundlers) |
|  | `moduleResolution` | `nodenext` ou `bundler` |
|  | `verbatimModuleSyntax` | `import type` obligatoire pour les types |
|  | `isolatedModules` | Compatibilité avec Vite, esbuild, SWC, Babel |
|  | `resolveJsonModule` | Importer du JSON |
| **Sorties** | `outDir`, `rootDir` | Dossiers de sortie et de source |
|  | `noEmit` | Ne génère rien (vérification seule) |
|  | `declaration`, `declarationMap`, `sourceMap` | Déclarations et cartes sources |
|  | `incremental`, `composite` | Compilation incrémentale, projets liés |
| **Rigueur** | `strict` | Active l'ensemble des vérifications strictes |
|  | `noUncheckedIndexedAccess` | `t[i]` vaut `T \| undefined` |
|  | `exactOptionalPropertyTypes` | Distingue `?:` de `\| undefined` |
|  | `noImplicitOverride` | `override` obligatoire |
|  | `noImplicitReturns`, `noFallthroughCasesInSwitch` | Retours et `switch` explicites |
|  | `noUnusedLocals`, `noUnusedParameters` | Code mort (souvent laissé à ESLint) |
|  | `erasableSyntaxOnly` | Interdit `enum`, `namespace`, propriétés de paramètres (TS 5.8) |
| **Divers** | `skipLibCheck` | Ignore la vérification des `.d.ts` des dépendances |
|  | `types`, `typeRoots` | Paquets de types ambiants |
|  | `paths` | Alias de chemins |
|  | `jsx` | `react-jsx`, `preserve`… |
|  | `allowJs`, `checkJs` | Mélanger JS et TS |

### Ce que contient `strict`

`noImplicitAny`, `strictNullChecks`, `strictFunctionTypes`, `strictBindCallApply`, `strictPropertyInitialization`, `noImplicitThis`, `useUnknownInCatchVariables`, `alwaysStrict`. Les futures options strictes sont ajoutées à `strict` au fil des versions.

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
import { Bouton } from '@composants/Bouton';
```

`paths` n'affecte **que la vérification des types** : le chemin doit aussi être résolu à l'**exécution** (alias de Vite/webpack, `tsx`, ou **`imports` de `package.json`**, standard Node.js). Depuis TS 6.0, `baseUrl` est **déprécié** : les chemins de `paths` sont relatifs au `tsconfig.json`.

```json
// package.json : alias natifs de Node.js, reconnus par TypeScript
{ "imports": { "#utils/*": "./src/utils/*.js" } }
```

## 20.5 Résolution des modules

| `moduleResolution` | Quand l'utiliser |
| --- | --- |
| **`nodenext`** | Applications/bibliothèques **Node.js** (ESM et CommonJS) : extensions obligatoires dans les imports relatifs |
| **`bundler`** | Code empaqueté par **Vite, webpack, esbuild…** : imports sans extension, `exports` du `package.json` |
| `node` / `node10` | **Déprécié** |
| `classic` | **Déprécié** |

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

`extends` fusionne les options (le fichier fils l'emporte ; `include`/`exclude`/`files` **remplacent** ceux du parent). Les **références de projets** (`"references": [{ "path": "../lib" }]`, `"composite": true`, `tsc -b`) accélèrent les **monorepos** par compilation incrémentale. Bases prêtes à l'emploi : `@tsconfig/node24`, `@tsconfig/strictest`, `@tsconfig/recommended`. Pour séparer sources, tests et scripts : plusieurs fichiers (`tsconfig.app.json`, `tsconfig.node.json`) référencés depuis un `tsconfig.json` racine.

## 20.8 Erreurs fréquentes

| Problème | Solution |
| --- | --- |
| *Cannot find module* ou types de Node introuvables | Ajouter `@types/node` **et** `"types": ["node"]` (TS 6+) |
| Imports relatifs en erreur avec `nodenext` | Ajouter l'extension `.js` |
| `import x from 'cjs'` sans valeur par défaut | `esModuleInterop` (toujours actif en 6.0) |
| Alias `@/...` résolu par TS mais pas à l'exécution | Configurer le bundler / `imports` |
| Vite compile, mais `tsc` échoue | Normal : Vite ne vérifie pas ; corrigez les erreurs de type |
| `moduleResolution: node` déprécié | Passer à `bundler` / `nodenext` |
| Erreur **TS5112** avec `tsc fichier.ts` | Un `tsconfig.json` existe : `tsc -p .` ou `--ignoreConfig` |
| *Option ... has been removed* avec TS 7 | Retirer/remplacer l'option dépréciée en 6.0 |
| Beaucoup d'erreurs après la mise à jour vers TS 6 | `strict` est actif : corriger, ou `"strict": false` temporairement |

## 20.9 TypeScript 7 et le compilateur natif

- Même **commande `tsc`**, mêmes types, mais un compilateur écrit en **Go** : **plusieurs fois plus rapide**, avec un vérificateur **parallèle**.
- Il **ne supporte pas** les options dépréciées en 6.0 ni l'ancienne **API de compilateur** JavaScript : les outils qui l'utilisent (certaines règles ESLint avec types, générateurs de code, plugins) doivent s'adapter ; gardez TypeScript 6 installé en parallèle si besoin.
- Le service de langage (VS Code, Visual Studio…) bénéficie du même gain : complétion et diagnostics plus réactifs sur les gros projets.

## Points clés du module 20

- TS 6 : `strict` et `module: esnext` par défaut, `types: []`, de nombreuses dépréciations ; TS 7 les supprime.
- `nodenext` pour Node.js, `bundler` pour les empaqueteurs.
- `paths` ne suffit pas à l'exécution.
- Ajoutez `noUncheckedIndexedAccess`, `noImplicitOverride`, `verbatimModuleSyntax`.

---

# 21. Linting et formatage

**Objectifs** : distinguer vérification de types, linting et formatage ; configurer ESLint (flat config) avec typescript-eslint, Prettier, Biome, l'éditeur et la CI.

## 21.1 Pourquoi ?

| Outil | Rôle |
| --- | --- |
| **Compilateur** (`tsc`) | Vérifie les **types** |
| **Linter** (ESLint + typescript-eslint) | Détecte les **mauvaises pratiques** et bugs probables |
| **Formateur** (Prettier, Biome) | Impose un **style** uniforme |

**TSLint est abandonné depuis 2019** : utilisez **typescript-eslint**.

## 21.2 ESLint avec typescript-eslint (configuration « flat »)

```bash
npm install -D eslint @eslint/js typescript-eslint
```

```javascript
// eslint.config.mjs
import eslint from '@eslint/js';
import tseslint from 'typescript-eslint';

export default tseslint.config(
    { ignores: ['dist/', 'coverage/'] },
    eslint.configs.recommended,
    tseslint.configs.strictTypeChecked,       // règles « avec types » (plus puissantes)
    tseslint.configs.stylisticTypeChecked,
    {
        languageOptions: {
            parserOptions: { projectService: true, tsconfigRootDir: import.meta.dirname },
        },
        rules: {
            '@typescript-eslint/no-explicit-any': 'error',
            '@typescript-eslint/no-floating-promises': 'error',
            '@typescript-eslint/consistent-type-imports': 'error',
            '@typescript-eslint/no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
        },
    },
    { files: ['**/*.mjs', '**/*.js'], extends: [tseslint.configs.disableTypeChecked] },
);
```

Les anciens fichiers `.eslintrc.*` sont **remplacés** par le format « flat » `eslint.config.*` (par défaut depuis ESLint 9). **`projectService`** laisse typescript-eslint s'appuyer sur le service de langage de TypeScript pour obtenir les informations de types (règles « *type-aware* »).

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
| `no-unnecessary-condition` | Conditions toujours vraies ou fausses |
| `strict-boolean-expressions` | Conditions explicites |
| `prefer-readonly`, `no-non-null-assertion` | Immutabilité, pas de `!` |

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
const utilisateur={nom:'Alice',age:30,roles:['admin','editeur'],actif:true}

// Après
function addition(a: number, b: number) {
    return a + b;
}
const utilisateur = {
    nom: 'Alice',
    age: 30,
    roles: ['admin', 'editeur'],
    actif: true,
};
```

**ESLint** s'occupe de la **qualité**, **Prettier** du **formatage** ; `eslint-config-prettier` désactive les règles ESLint de style qui entreraient en conflit. Un fichier `.editorconfig` harmonise indentation et fins de ligne entre éditeurs.

## 21.4 Alternative tout-en-un : Biome

**Biome** (écrit en Rust) remplace ESLint **et** Prettier dans un seul outil, très rapide, avec une configuration unique. Ses règles nécessitant les informations de types sont moins complètes que celles de typescript-eslint.

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

**Hooks Git** : `lint-staged` + `husky` (ou `lefthook`) exécutent lint et format **uniquement sur les fichiers modifiés** avant chaque commit. En **CI**, lancez `verifier` sur chaque requête de fusion : c'est le garde-fou final.

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

## Points clés du module 21

- Trois outils complémentaires : `tsc` (types), ESLint (qualité), Prettier/Biome (style).
- La configuration « flat » remplace `.eslintrc` ; `projectService` active les règles avec types.
- Automatisez : éditeur à la sauvegarde, hooks Git, CI.

---

# BONUS

---

# 22. TypeScript et bases de données

**Objectifs** : typer modèles et résultats de requêtes, utiliser PostgreSQL, MongoDB, les ORM modernes (Prisma, Drizzle, Kysely, TypeORM), le motif dépôt, et appliquer les bonnes pratiques.

## 22.1 Principes

- Typez les **modèles** (entités) **et** les **résultats de requêtes**.
- Les types TypeScript **ne vérifient pas** ce que renvoie réellement la base : préférez des outils qui **génèrent les types depuis le schéma** (Prisma, Drizzle, Kysely avec générateurs) ou validez les lignes (Zod).
- Utilisez toujours des **requêtes paramétrées** : c'est la défense de base contre l'**injection SQL**. Jamais de concaténation de chaînes avec des entrées utilisateur.
- Attention aux conversions : `bigint`/`numeric` de PostgreSQL arrivent souvent en `string`, les dates en `Date` ou `string` selon le pilote.

## 22.2 PostgreSQL avec `pg`

```bash
npm install pg
npm install -D @types/pg
```

```typescript
import { Pool } from 'pg';

const pool = new Pool({ connectionString: process.env.DATABASE_URL });

interface Utilisateur { id: number; nom: string; email: string }

export async function trouverParEmail(email: string): Promise<Utilisateur | undefined> {
    const { rows } = await pool.query<Utilisateur>(
        'SELECT id, nom, email FROM utilisateurs WHERE email = $1', // paramètre lié
        [email],
    );
    return rows[0];
}

export async function creer(nom: string, email: string): Promise<Utilisateur> {
    const { rows } = await pool.query<Utilisateur>(
        'INSERT INTO utilisateurs (nom, email) VALUES ($1, $2) RETURNING id, nom, email',
        [nom, email],
    );
    return rows[0]!;
}
```

Le générique de `query<T>` est une **promesse** : le compilateur ne compare pas `T` aux colonnes sélectionnées.

### Transactions

```typescript
const client = await pool.connect();
try {
    await client.query('BEGIN');
    // … requêtes …
    await client.query('COMMIT');
} catch (e) {
    await client.query('ROLLBACK');
    throw e;
} finally {
    client.release(); // toujours restituer la connexion au pool
}
```

Une **transaction** regroupe plusieurs opérations en un tout atomique (tout réussit ou rien ne change) ; elle exige la **même connexion** pour toutes les requêtes, d'où `pool.connect()`.

## 22.3 MongoDB

### Pilote officiel

```typescript
import { MongoClient, ObjectId, type Collection } from 'mongodb';

interface Article {
    _id?: ObjectId;
    titre: string;
    tags: string[];
    publieLe: Date;
}

const client = new MongoClient(process.env.MONGODB_URI!);
await client.connect();
const articles: Collection<Article> = client.db('blog').collection<Article>('articles');

await articles.insertOne({ titre: 'Hello', tags: ['ts'], publieLe: new Date() });
const recents = await articles.find({ tags: 'ts' }).sort({ publieLe: -1 }).limit(10).toArray(); // Article[]
```

Le type `Collection<Article>` s'applique aux **filtres**, aux **insertions** et aux **résultats** : c'est un typage plus profond qu'avec `pg`.

### Mongoose

```typescript
import { Schema, model, type InferSchemaType } from 'mongoose';

const schemaUtilisateur = new Schema({
    nom: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    creeLe: { type: Date, default: Date.now },
});

type IUtilisateur = InferSchemaType<typeof schemaUtilisateur>; // type déduit du schéma
const Utilisateur = model('Utilisateur', schemaUtilisateur);

const u = await Utilisateur.create({ nom: 'Alice', email: 'alice@exemple.com' });
const trouve = await Utilisateur.findOne({ email: 'alice@exemple.com' }).lean();
```

`lean()` renvoie des objets simples (plus rapides) plutôt que des documents Mongoose.

## 22.4 ORM et constructeurs de requêtes

| Outil | Approche | Points forts |
| --- | --- | --- |
| **Prisma** | Schéma `schema.prisma` → **client généré** typé | Excellente expérience, migrations intégrées |
| **Drizzle ORM** | Schéma en **TypeScript**, requêtes proches du SQL | Léger, types précis, sans génération |
| **Kysely** | **Constructeur de requêtes** typé | Contrôle total du SQL |
| **TypeORM** | Entités avec **décorateurs** | Très répandu, intégré à NestJS |
| **MikroORM**, **Sequelize**, **Objection** | Alternatives |  |

### Prisma

```prisma
// prisma/schema.prisma
model Utilisateur {
  id       Int       @id @default(autoincrement())
  email    String    @unique
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
import { PrismaClient } from '@prisma/client';
const prisma = new PrismaClient();

const u = await prisma.utilisateur.create({ data: { email: 'a@b.fr', nom: 'Alice' } });
const avecArticles = await prisma.utilisateur.findUnique({
    where: { email: 'a@b.fr' },
    include: { articles: true },   // le type du résultat inclut `articles`
});
```

Point fort : le type du résultat **s'adapte** aux options `select`/`include`. Le client est généré par `prisma generate` après chaque changement de schéma.

### Drizzle

```typescript
import { pgTable, serial, text } from 'drizzle-orm/pg-core';
import { drizzle } from 'drizzle-orm/node-postgres';
import { eq } from 'drizzle-orm';

export const utilisateurs = pgTable('utilisateurs', {
    id: serial('id').primaryKey(),
    nom: text('nom').notNull(),
    email: text('email').notNull().unique(),
});
type Utilisateur = typeof utilisateurs.$inferSelect;
type NouvelUtilisateur = typeof utilisateurs.$inferInsert;

const db = drizzle(process.env.DATABASE_URL!);
const u: Utilisateur[] = await db.select().from(utilisateurs).where(eq(utilisateurs.email, 'a@b.fr'));
```

Le **schéma est du code TypeScript** : il sert à la fois de définition de table et de source des types (`$inferSelect`, `$inferInsert`), sans étape de génération.

### TypeORM

```typescript
import { Entity, PrimaryGeneratedColumn, Column, DataSource } from 'typeorm';

@Entity()
export class Utilisateur {
    @PrimaryGeneratedColumn() id!: number;
    @Column() nom!: string;
    @Column({ unique: true }) email!: string;
}

const source = new DataSource({ type: 'postgres', url: process.env.DATABASE_URL, entities: [Utilisateur], synchronize: false });
await source.initialize();
const depot = source.getRepository(Utilisateur);
const u = await depot.findOneBy({ email: 'a@b.fr' });
```

TypeORM exige les décorateurs **expérimentaux** (`experimentalDecorators`, `emitDecoratorMetadata`) ; `strictPropertyInitialization` impose le `!` sur les colonnes. Ne mettez jamais `synchronize: true` en production.

## 22.5 Le motif « dépôt » (*repository*)

Il **isole** l'accès aux données derrière une interface, ce qui facilite les tests et le changement de technologie.

```typescript
interface Utilisateur { id: number; nom: string; email: string }

interface DepotUtilisateurs {
    trouverParId(id: number): Promise<Utilisateur | undefined>;
    creer(donnees: Omit<Utilisateur, 'id'>): Promise<Utilisateur>;
}

class MemoireDepot implements DepotUtilisateurs {   // pour les tests
    private lignes: Utilisateur[] = [];
    async trouverParId(id: number) { return this.lignes.find((u) => u.id === id); }
    async creer(donnees: Omit<Utilisateur, 'id'>) {
        const u = { id: this.lignes.length + 1, ...donnees };
        this.lignes.push(u);
        return u;
    }
}
// Autres implémentations : PostgresDepot, PrismaDepot…
```

La **logique métier** dépend de l'interface `DepotUtilisateurs`, jamais d'un pilote précis (inversion de dépendance).

## 22.6 Bonnes pratiques

- **Migrations versionnées** (Prisma Migrate, Drizzle Kit, Flyway…) : jamais de modification manuelle du schéma en production.
- **Variables d'environnement** pour les chaînes de connexion ; jamais dans le dépôt Git.
- **Pool de connexions**, transactions pour les opérations multiples, **index** adaptés.
- Ne renvoyez jamais directement des entités contenant des champs sensibles (`Omit<..., 'motDePasseHache'>`).
- Pagination, limites et délais d'expiration sur les requêtes.

## Points clés du module 22

- Les types de requêtes ne sont fiables que s'ils **dérivent du schéma** de la base.
- Requêtes paramétrées, transactions, pool de connexions.
- Le motif dépôt découple métier et persistance.

---

# 23. TypeScript et tests

**Objectifs** : choisir un outil de test, écrire des tests unitaires typés (Vitest, Jest, Mocha), tester les types, utiliser des doublures (mocks, stubs, espions) et appliquer les bonnes pratiques.

## 23.1 Choisir un outil de test

| Outil | Points forts |
| --- | --- |
| **Vitest** | Très rapide, TypeScript et ESM **natifs**, API compatible Jest, intégré à Vite |
| **Jest** | Très répandu ; nécessite un transformateur (`ts-jest`, `@swc/jest` ou Babel) |
| **`node:test`** | Exécuteur **intégré à Node.js**, sans dépendance |
| **Mocha** (+ Chai, Sinon) | Flexible, modulaire |
| **Playwright**, **Cypress** | Tests de bout en bout (E2E) dans un navigateur |

**Pyramide des tests** : beaucoup de tests **unitaires** (rapides, isolés), quelques tests d'**intégration** (plusieurs composants, vraie base de test), peu de tests **E2E** (parcours complets).

## 23.2 Vitest

```bash
npm install -D vitest
```

```typescript
// src/calculatrice.ts
export function diviser(a: number, b: number): number {
    if (b === 0) throw new RangeError('Division par zéro');
    return a / b;
}
```

```typescript
// src/calculatrice.test.ts
import { describe, it, expect } from 'vitest';
import { diviser } from './calculatrice.js';

describe('diviser', () => {
    it('divise deux nombres', () => {
        expect(diviser(10, 2)).toBe(5);
    });

    it('lève une erreur en cas de division par zéro', () => {
        expect(() => diviser(1, 0)).toThrow(RangeError);
    });

    it.each([[4, 2, 2], [9, 3, 3], [-6, 3, -2]])('diviser(%i, %i) = %i', (a, b, attendu) => {
        expect(diviser(a, b)).toBe(attendu);
    });
});
```

```json
{ "scripts": { "test": "vitest", "test:ci": "vitest run --coverage" } }
```

`toBe` compare avec `Object.is` (primitifs), `toEqual` compare **structurellement** (objets), `toStrictEqual` est plus strict (propriétés `undefined`, classes). `it.each` paramètre un test ; `beforeEach`/`afterEach` préparent et nettoient l'état.

## 23.3 Jest avec TypeScript

```bash
npm install -D jest @types/jest ts-jest
npx ts-jest config:init
```

```javascript
// jest.config.js
export default { preset: 'ts-jest', testEnvironment: 'node', testMatch: ['**/*.test.ts'] };
```

L'API (`describe`, `it`, `expect`, `jest.fn()`, `jest.mock()`) est quasi identique à Vitest ; avec TypeScript 6, ajoutez `"types": ["jest"]` dans le `tsconfig`. Note : `ts-jest` vérifie les types pendant les tests (plus lent) ; `@swc/jest` les efface seulement.

## 23.4 Mocha + Chai

```bash
npm install -D mocha chai tsx @types/mocha @types/chai
```

```typescript
import { expect } from 'chai';
import { diviser } from '../src/calculatrice.js';

describe('diviser', () => {
    it('divise', () => { expect(diviser(10, 2)).to.equal(5); });
    it('lève une erreur', () => { expect(() => diviser(1, 0)).to.throw(RangeError); });
});
```

```bash
mocha --import=tsx 'tests/**/*.test.ts'
```

## 23.5 Tester les types

Les **types** aussi se testent : on vérifie qu'un utilitaire produit le type attendu et qu'un mauvais usage est refusé.

```typescript
import { expectTypeOf, test } from 'vitest';
import { diviser } from './calculatrice.js';

type PartielProfond<T> = { [K in keyof T]?: T[K] extends object ? PartielProfond<T[K]> : T[K] };

test('types de l\'utilitaire', () => {
    expectTypeOf<PartielProfond<{ a: { b: number } }>>().toEqualTypeOf<{ a?: { b?: number } }>();
    expectTypeOf(diviser).parameters.toEqualTypeOf<[number, number]>();
    expectTypeOf(diviser).returns.toBeNumber();
});

// @ts-expect-error : vérifie qu'une erreur de compilation est bien levée
diviser('a', 1);
```

**`@ts-expect-error`** exige qu'il y ait une erreur sur la ligne suivante : si l'erreur disparaît, le test de compilation échoue. Il est préférable à `@ts-ignore`. Alternatives : **tsd**, ou `tsc --noEmit` sur des fichiers `*.test-d.ts`.

## 23.6 Doublures : mocks, stubs, espions

```typescript
import { vi, expect, it } from 'vitest';

interface Mailer { envoyer(destinataire: string, sujet: string): Promise<boolean> }

class Inscription {
    constructor(private readonly mailer: Mailer) {}
    async inscrire(email: string) { return this.mailer.envoyer(email, 'Bienvenue'); }
}

it('envoie un e-mail de bienvenue', async () => {
    const mailer: Mailer = { envoyer: vi.fn().mockResolvedValue(true) }; // doublure typée par l'interface
    const inscription = new Inscription(mailer);

    expect(await inscription.inscrire('alice@exemple.com')).toBe(true);
    expect(mailer.envoyer).toHaveBeenCalledWith('alice@exemple.com', 'Bienvenue');
    expect(mailer.envoyer).toHaveBeenCalledTimes(1);
});
```

| Doublure | Rôle |
| --- | --- |
| **Stub** | Renvoie des valeurs prédéfinies (`mockReturnValue`, `mockResolvedValue`) |
| **Mock** | Vérifie les appels (`toHaveBeenCalledWith`) |
| **Spy** (`vi.spyOn`) | Observe une méthode réelle sans la remplacer |
| **Fake** | Implémentation simplifiée (dépôt en mémoire) |

```typescript
vi.mock('./api.js', () => ({ charger: vi.fn().mockResolvedValue({ id: 1 }) })); // module entier
vi.useFakeTimers();                                                              // horloge simulée
```

Outils complémentaires : **MSW** (simuler l'API réseau), `sinon`, `ts-mockito`, `jest-mock-extended`. Réinitialisez les doublures entre les tests (`vi.restoreAllMocks`).

## 23.7 Sécurité des types dans les tests

- Programmez **vers des interfaces** et injectez les dépendances : les doublures restent **vérifiées** par le compilateur.
- Évitez `as any` ; préférez `Partial<T>` + une assertion limitée, ou une **fabrique de données** :

```typescript
interface Utilisateur { id: number; nom: string; email: string }

function faireUtilisateur(surcharges: Partial<Utilisateur> = {}): Utilisateur {
    return { id: 1, nom: 'Alice', email: 'alice@exemple.com', ...surcharges };
}
```

- Incluez les tests dans la vérification de types (`tsc --noEmit`) ; ajoutez `"types": ["vitest/globals"]` si vous utilisez les API globales.

## 23.8 Bonnes pratiques

- **Arrange – Act – Assert** : préparer, agir, vérifier ; **un comportement par test**, noms explicites.
- Testez les **cas limites** et les **erreurs**.
- Pas de réseau ni de base réelle dans les tests unitaires ; des **tests d'intégration** séparés (conteneurs de test).
- Tests **déterministes** : horloge, aléatoire et réseau contrôlés.
- Visez une couverture **utile** (pas 100 % à tout prix) et exécutez les tests en **CI**.

## Points clés du module 23

- Vitest : TypeScript natif ; Jest : transformateur ; `node:test` : sans dépendance.
- `expectTypeOf` et `@ts-expect-error` testent les types.
- Interfaces + injection = doublures sûres.

---

# 24. Nouveautés par version et bonnes pratiques

**Objectifs** : situer chaque fonctionnalité majeure dans la chronologie de TypeScript, découvrir `using`, et récapituler les bonnes pratiques de tout le cours.

## 24.1 Chronologie des fonctionnalités

| Version | À retenir |
| --- | --- |
| **4.1** | Types littéraux de gabarit, remappage de clés (`as`) dans les types mappés |
| **4.3–4.4** | `override`, signatures d'index pour symboles, analyse de flux contrôlée |
| **4.9** | **`satisfies`**, mot-clé `accessor` |
| **5.0** | **Décorateurs standard**, paramètres de type **`const`**, `verbatimModuleSyntax`, enums unifiés |
| **5.2** | Déclarations **`using`** / `await using` (gestion de ressources) |
| **5.4** | **`NoInfer`**, meilleure restriction dans les fermetures |
| **5.5** | **Prédicats de type inférés**, `isolatedDeclarations`, vérification des regex |
| **5.7–5.8** | `--rewriteRelativeImportExtensions`, **`--erasableSyntaxOnly`**, `require()` d'ESM |
| **6.0** (mars 2026) | **Version passerelle** : `strict` par défaut, `module: esnext`, `types: []`, `target` ES2025 ; nombreuses **dépréciations** ; types de **Temporal** et d'API ES récentes (`Promise.try`, méthodes de `Set`…) |
| **7.0** (juillet 2026) | **Compilateur natif (Go)** : vitesse, parallélisme ; options dépréciées supprimées |

**Stratégie de mise à jour** : passer par TS 6 (qui avertit des dépréciations), corriger la configuration, puis adopter TS 7. Garder les outils (typescript-eslint, frameworks) à jour de façon coordonnée.

## 24.2 Gestion de ressources : `using` (TS 5.2)

La déclaration **`using`** garantit qu'une ressource est **libérée automatiquement** à la sortie du bloc, même en cas d'exception (comme `try/finally`, mais déclaratif).

```typescript
class Connexion implements Disposable {
    [Symbol.dispose]() { console.log('Connexion fermée'); }
}

function travailler() {
    using connexion = new Connexion(); // libérée à la sortie du bloc
    // …
}

async function travaillerAsync() {
    await using ressource = obtenirRessource(); // libération asynchrone via [Symbol.asyncDispose]
}
```

Les ressources sont libérées dans l'**ordre inverse** de leur déclaration. Cela nécessite un runtime qui prend en charge `Symbol.dispose`, ou un *polyfill*. Cas d'usage : connexions, fichiers, verrous, transactions, abonnements.

## 24.3 Bonnes pratiques

| Pratique | Pourquoi |
| --- | --- |
| **`strict: true`** (désormais par défaut) + `noUncheckedIndexedAccess` + `noImplicitOverride` | Capture un maximum d'erreurs |
| **`unknown`** plutôt que `any` ; restreindre avant usage | Sécurité |
| **Unions discriminées** pour modéliser des états | Pas d'états impossibles |
| `interface` pour les formes d'objets, `type` pour le reste | Cohérence |
| **Unions de littéraux / `as const`** plutôt qu'`enum` | Moins de code généré, compatible mode effaçable |
| **`import type`** + `verbatimModuleSyntax` | Imports prévisibles |
| **Valider les données externes** (Zod, Valibot) | Les types disparaissent à l'exécution |
| Typer **entrées et sorties** des fonctions publiques | Contrats clairs |
| Éviter les assertions `as` et `!` | Elles contournent le compilateur |
| `tsc --noEmit` **en CI** | Vite, esbuild et `tsx` ne vérifient pas les types |
| Garder TypeScript et `@types/*` **à jour** | Corrections et nouvelles fonctionnalités |

## 24.4 Récapitulatif du cours en dix principes

1. Les types sont une **aide au raisonnement** et disparaissent à l'exécution.
2. Laissez l'**inférence** travailler ; annotez les frontières (paramètres, API publiques).
3. **Modélisez** les données pour que les états invalides soient inexprimables.
4. **Restreignez** plutôt que d'asserter.
5. Utilisez les **génériques** pour relier des types, pas pour décorer.
6. Préférez les **utilitaires standard** aux types maison.
7. **Validez** toute donnée externe ; dérivez les types des schémas.
8. Configurez `tsconfig` **strictement** et selon l'environnement (`nodenext` ou `bundler`).
9. **Automatisez** : `tsc --noEmit`, ESLint, Prettier, tests, CI.
10. Restez **simple** : le meilleur type est celui que l'équipe comprend.

## 24.5 Ressources

- **Documentation officielle** : https://www.typescriptlang.org/docs/
- **TypeScript Handbook** et **notes de version** : https://www.typescriptlang.org/docs/handbook/release-notes/overview.html
- **Playground** : https://www.typescriptlang.org/play
- **Type Challenges** (exercices de types) : https://github.com/type-challenges/type-challenges
- **DefinitelyTyped** : https://github.com/DefinitelyTyped/DefinitelyTyped
- **typescript-eslint** : https://typescript-eslint.io
- *Effective TypeScript* — Dan Vanderkam

---

*Bon code, et que vos types soient toujours justes !*
