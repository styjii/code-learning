# 🔷 Exercices TypeScript

> Un parcours de **27 exercices et 3 mini-projets guidés**, des types de base jusqu'aux bases de données et aux tests. Les deux séries d'origine (« Exercises » et « basics ») ont été fusionnées, dédoublonnées et classées par difficulté croissante.

## 📑 Sommaire

0. [Mise en place et contexte d'exécution](#0-mise-en-place-et-contexte-dexécution)
1. [Partie 1 : fondamentaux](#partie-1--fondamentaux)
2. [Partie 2 : programmation orientée objet et génériques](#partie-2--programmation-orientée-objet-et-génériques)
3. [Partie 3 : types avancés](#partie-3--types-avancés)
4. [Partie 4 : trois mini-projets guidés](#partie-4--trois-mini-projets-guidés)
5. [Partie 5 : asynchrone](#partie-5--asynchrone)
6. [Partie 6 : modules, déclarations et configuration](#partie-6--modules-déclarations-et-configuration)
7. [Partie 7 : décorateurs](#partie-7--décorateurs)
8. [Partie 8 : web et frameworks](#partie-8--web-et-frameworks)
9. [Partie 9 : bases de données et tests](#partie-9--bases-de-données-et-tests)
10. [Récapitulatif des notions](#récapitulatif-des-notions)

**Légende** : 🟢 débutant · 🟡 intermédiaire · 🔴 avancé · ➕ ajouté dans cette version (notion absente de l'original)

---

## 0. Mise en place et contexte d'exécution

Le même code TypeScript se comporte différemment selon **l'endroit où il s'exécute** (Node.js, navigateur, framework, tests) et selon la **configuration** du projet. Cette section est commune à tous les exercices.

### Installation

Prérequis : **Node.js 20 ou plus récent** (version LTS) et **TypeScript 5.x**.

```bash
mkdir ts-exercices && cd ts-exercices
npm init -y
npm install --save-dev typescript tsx @types/node
npx tsc --init
```

### Configuration recommandée : `tsconfig.json`

```json
{
    "compilerOptions": {
        "target": "ES2022",
        "lib": ["ES2023"],
        "module": "NodeNext",
        "moduleResolution": "NodeNext",
        "rootDir": "src",
        "outDir": "build",

        "strict": true,
        "noUncheckedIndexedAccess": true,
        "noImplicitOverride": true,
        "verbatimModuleSyntax": true,
        "skipLibCheck": true
    },
    "include": ["src"]
}
```

> 💡 **`strict: true` est indispensable** : sans lui, TypeScript laisse passer beaucoup d'erreurs (`null`, `any` implicite…). Ajoutez `"type": "module"` dans `package.json` pour utiliser les modules ES.

### Exécuter et vérifier

| Commande | Rôle |
| --- | --- |
| `npx tsx src/index.ts` | Exécute directement un fichier TypeScript (sans compilation préalable) |
| `npx tsc --noEmit` | **Vérifie uniquement les types**, sans produire de JavaScript |
| `npx tsc` | Compile `src/` vers `build/` |
| `node build/index.js` | Exécute le JavaScript compilé |

> ℹ️ Les versions récentes de Node.js peuvent exécuter des fichiers `.ts` simples en supprimant les types (selon la version, vérifiez la documentation). Ce mode ne gère **pas** les syntaxes qui produisent du code (`enum`, `namespace`, décorateurs, propriétés de paramètre). TypeScript 5.8 propose l'option `erasableSyntaxOnly` pour les interdire, ce qui explique les alternatives proposées dans les exercices 4 et 19.

### Selon le contexte d'exécution

| Contexte | À configurer | Exercices concernés |
| --- | --- | --- |
| 🟢 **Node.js** | `lib: ["ES2023"]`, paquet `@types/node` | La plupart |
| 🌐 **Navigateur** | Ajouter `"DOM"` et `"DOM.Iterable"` à `lib` ; utiliser un bundler (Vite) | 23 |
| ⚛️ **Frameworks** (React, Angular, Vue) | Fournis par le générateur de projet (`npm create vite`, `ng new`…) | 24 |
| 🧪 **Tests** | Jest, Vitest ou `node:test` + types associés | 27 |

> ⚠️ Avec `"module": "NodeNext"`, les imports **relatifs** doivent inclure l'extension `.js`, même si le fichier source est en `.ts` : `import { add } from "./math.js";`.

---

# Partie 1 : fondamentaux

### Exercice 1 : Variables typées 🟢

Déclarez ces variables avec le bon type :

1. `userName`, une chaîne valant `"Alice"`
2. `userAge`, un nombre valant `30`
3. `isAdmin`, un booléen valant `false`
4. `hobbies`, un tableau de chaînes : `["lecture", "code", "échecs"]`
5. `locat`, un **tuple** contenant une chaîne (ville) et un nombre (code postal)

> 💡 Avec une valeur initiale, TypeScript **infère** le type : n'ajoutez une annotation que lorsqu'elle apporte quelque chose (tuple, tableau vide, etc.). Préférez `const` à `let`.

---

### Exercice 2 : Fonctions typées 🟢

1. Écrivez `sum(a, b)` qui renvoie la somme de deux nombres.
2. Écrivez `multiply(a: number, b: number): number`.
3. Écrivez `greetUser(name: string): string`.
   ```ts
   console.log(greetUser("Alice")); // "Bonjour, Alice !"
   ```
4. Écrivez `sayHello(name: string, age?: number): string` : le paramètre `age` est **optionnel**.
5. Créez un **alias de type de fonction** `CalcFn` pour `(a: number, b: number) => number`, puis utilisez-le pour typer deux fonctions `add` et `multiply`.
6. ➕ Écrivez `total(...nombres: number[])` avec un **paramètre rest**, puis `puissance(base: number, exposant = 2)` avec une **valeur par défaut**.

---

### Exercice 3 : Tableaux et tuples 🟢

1. Déclarez un `string[]` de couleurs préférées.
2. Ajoutez une couleur avec `push()`.
3. Créez un `readonly number[]` de nombres premiers, puis essayez d'y faire un `push()` : lisez l'erreur du compilateur.
4. Définissez un type tuple `Person` de la forme `[string, number]`.
5. Créez et affichez une valeur de type `Person`.
6. ➕ Rendez le tuple plus lisible avec des **étiquettes** : `[name: string, age: number]`.

---

### Exercice 4 : Énumérations 🟡

1. Créez un `enum Status` avec `Active`, `Inactive` et `Blocked`, puis une fonction `logStatus(status: Status): void` qui affiche la valeur.
2. Créez un `enum Direction` (`North`, `South`, `East`, `West`) et une fonction `move(dir: Direction): string` qui renvoie un message.
3. Créez un `const enum LogLevel` (`Debug`, `Info`, `Error`).
4. ➕ **Comparez** quatre façons de modéliser un ensemble de valeurs, puis choisissez-en une pour `Direction` :

   | Approche | Exemple |
   | --- | --- |
   | `enum` numérique | `enum Dir { North, South }` |
   | `enum` de chaînes | `enum Dir { North = "N" }` |
   | Union de littéraux | `type Dir = "N" \| "S" \| "E" \| "W"` |
   | Objet `as const` | voir ci-dessous |

   ```ts
   const Direction = { North: "N", South: "S", East: "E", West: "W" } as const;
   type Direction = (typeof Direction)[keyof typeof Direction]; // "N" | "S" | "E" | "W"
   ```

> ⚠️ Les `enum` et surtout les `const enum` posent problème avec les bundlers (`isolatedModules`) et avec l'exécution directe par Node.js. Dans un projet récent, l'**union de littéraux** ou l'objet `as const` est souvent préféré.

---

### Exercice 5 : Interfaces et objets 🟢

1. Créez une interface `User` avec `name: string`, `age: number` et `isAdmin: boolean`.
2. Créez un objet `user` puis une fonction `printUserInfo(user: User): void`.
   ```ts
   printUserInfo(user); // Nom : Alice, Âge : 30, Admin : oui
   ```
   Utilisez un **opérateur ternaire** pour afficher « oui » ou « non ».
3. **Bonus** : ajoutez `hobbies: string[]` à `User`, et affichez les loisirs s'il y en a.

---

### Exercice 6 : Héritage d'interfaces et classes 🟡

1. Définissez une interface `Book` avec `title`, `author` et `year` (optionnel).
2. Créez `printBook(book: Book): void`.
3. Étendez `Book` avec une interface `EBook` qui ajoute `fileSize` (en Mo).
4. Écrivez une classe `EBookReader` qui affiche les détails d'un `EBook`.

---

### Exercice 7 : Alias de types, unions et littéraux 🟢

1. Créez un alias `ID` valant `number | string`, une variable `userId` de ce type, puis une fonction `displayId(id: ID)` qui affiche `"ID numérique : 42"` ou `"ID texte : user_abc"`. Utilisez `typeof` pour distinguer les deux cas.
2. Créez un alias `UserRole` valant `"admin" | "user" | "guest"`.
3. Créez un alias `User` avec `id: number`, `name: string` et `role: UserRole`.
4. Écrivez `describeUser(user: User): string`.

---

### Exercice 8 : Unions discriminées 🟡

1. Définissez deux interfaces :
   - `Admin` : `role: "admin"`, `name: string`, `permissions: string[]`
   - `Guest` : `role: "guest"`, `name: string`, `expiration: Date`
2. Créez `type UserType = Admin | Guest`.
3. Écrivez `handleUser(user: UserType)` qui affiche :
   - `"L'administrateur <nom> a les permissions : ..."` si `role === "admin"` ;
   - `"L'invité <nom> expire le : ..."` si `role === "guest"`.
4. ➕ Ajoutez un troisième rôle et utilisez une **vérification d'exhaustivité** : une fonction `assertNever(x: never): never` appelée dans le `default` du `switch`. Le compilateur doit signaler l'oubli d'un cas.

> `role` est le **discriminant** : TypeScript réduit le type dans chaque branche.

---

### Exercice 9 : Surcharge de fonctions 🟡

Créez une fonction `combine` avec ces surcharges :

- deux `number` → leur somme ;
- deux `string` → leur concaténation ;
- un `number` et une `string` → une chaîne combinant les deux.

```ts
console.log(combine(2, 3));       // 5
console.log(combine("foo", "bar")); // "foobar"
console.log(combine(10, "px"));   // "10px"
```

---

# Partie 2 : programmation orientée objet et génériques

### Exercice 10 : Classes, héritage et interfaces 🟡

1. Créez une classe de base `Employee` avec `name` et `salary`.
2. Ajoutez une méthode `describe()`.
3. Créez une sous-classe `Manager` avec `department`, qui **redéfinit** `describe()` (utilisez le mot-clé `override`).
4. Créez une interface `Payable` avec `getPay(): number`.
5. Faites implémenter `Payable` par les deux classes.
6. ➕ **Bonus** : rendez `Employee` **abstraite** (`abstract`), passez `salary` en `protected`, et utilisez une **propriété de paramètre** dans le constructeur (`constructor(private readonly name: string)`).

---

### Exercice 11 : Génériques 🟡

1. Écrivez `reverseArray<T>(items: T[]): T[]`.
2. Créez une interface générique `ApiResponse<T>` (par exemple `{ data: T; error?: string }`).
3. Créez une classe `DataStore<T>` avec `add(item: T)` et `getAll(): T[]`.
4. ➕ **Bonus** : ajoutez une **contrainte** `T extends { id: number }` et une méthode `findById(id: number): T | undefined`.

---

### Exercice 12 : Accès typé aux clés (`keyof`) 🔴

Créez un objet de configuration typé :

1. Définissez `interface Config` avec les clés `theme`, `lang` et `debug`.
2. Écrivez :
   ```ts
   function getConfigValue<K extends keyof Config>(key: K): Config[K];
   ```
   qui renvoie la valeur associée à une clé. Le type de retour doit **dépendre de la clé** : `getConfigValue("debug")` est un `boolean`.

---

### Exercice 13 : Mixins et composition 🔴

Construisez une classe `Robot` qui :

- affiche son état grâce à un mixin `Logger` ;
- possède un numéro de série ajouté par un mixin ;
- peut être allumée et éteinte, par **composition** (un objet `Power` détenu par le robot).

> 💡 Discutez ensuite : quand préférer la composition à l'héritage ?

---

# Partie 3 : types avancés

### Exercice 14 : Types utilitaires 🟡

1. Utilisez `Partial<T>` pour définir la charge utile d'une mise à jour de `Product`.
2. Utilisez `Pick<T, K>` pour créer `UserPreview` avec seulement `id` et `name`.
3. ➕ Utilisez `Omit<T, K>`, `Required<T>` et `Readonly<T>` sur l'un de vos types.
4. Créez un `Record<Day, string[]>` où `Day` est une union de noms de jours.
5. Écrivez un type `DeepReadonly<T>` qui rend un objet immuable **récursivement**.
6. ➕ Utilisez `ReturnType<typeof f>` et `Awaited<Promise<string>>`.

> ⚠️ `Pick` prend **deux** paramètres : le type et les clés (`Pick<User, "id" | "name">`).

---

### Exercice 15 : Types mappés et conditionnels 🔴

1. Créez un type `Car` avec `make`, `model` et `year`.
2. Créez un type mappé `CarWithOptionalYear` où seule `year` est optionnelle (sans utiliser `Partial`).
3. Utilisez `Pick` pour créer `CarInfo` avec seulement `make` et `model`.
4. Écrivez un type conditionnel `IsCar<T>` qui vaut `true` si `T` est un `Car`, sinon `false`.
5. ➕ Écrivez `Nullable<T>`, un type mappé qui autorise `null` pour chaque propriété.

---

### Exercice 16 : `unknown`, `any`, `never` et gardes de type ➕ 🟡

1. Écrivez `parseJson(texte: string): unknown`, qui appelle `JSON.parse`.
2. Écrivez une **garde de type** `isUser(valeur: unknown): valeur is User` qui vérifie la forme de l'objet à l'exécution.
3. Utilisez cette garde pour afficher le nom d'un utilisateur lu depuis du JSON.
4. Dans un bloc `catch (e)`, traitez `e` comme `unknown` : affichez `e.message` uniquement si `e instanceof Error`.
5. Comparez `any` et `unknown` : que peut-on faire avec chacun ?

> 💡 Préférez `unknown` à `any` : il oblige à **vérifier** avant d'utiliser la valeur.

---

### Exercice 17 : `as const`, `satisfies` et types gabarits ➕ 🔴

1. Définissez un objet `routes` avec `as const`, et déduisez-en le type `Route` (union des chemins).
2. Utilisez `satisfies` pour vérifier qu'un objet respecte un type **sans élargir** son type inféré :
   ```ts
   const couleurs = {
       rouge: [255, 0, 0],
       vert: "#00ff00",
   } satisfies Record<string, string | number[]>;
   ```
   Pourquoi `couleurs.rouge.map(...)` fonctionne-t-il ici, mais pas avec une annotation `: Record<...>` ?
3. Créez un **type gabarit** (*template literal type*) :
   ```ts
   type EventName = "click" | "focus";
   type Handler = `on${Capitalize<EventName>}`; // "onClick" | "onFocus"
   ```

---

# Partie 4 : trois mini-projets guidés

Chaque projet se construit petit à petit, en réutilisant le code de l'étape précédente : réalisez les étapes **dans l'ordre**.

## Projet A : journal d'événements

### A1 : tuples d'événements 🟢

Voici le type d'un événement sous forme de tuple :

```ts
type EventTuple = [eventName: string, payload: Record<string, unknown>];
```

Déclarez un tableau `eventLog` contenant :

- `["login", { user: "alice", time: "12:00" }]`
- `["purchase", { user: "bob", item: "livre", price: 25 }]`
- `["logout", { user: "alice", time: "12:30" }]`

> 💡 L'original utilisait `payload: any`. `Record<string, unknown>` est plus sûr, mais il vous obligera à vérifier les valeurs à l'étape A3.

### A2 : union discriminée 🟡

```ts
interface LoginEvent    { type: "login";    user: string; time: string }
interface LogoutEvent   { type: "logout";   user: string; time: string }
interface PurchaseEvent { type: "purchase"; user: string; item: string; price: number }

type AppEvent = LoginEvent | LogoutEvent | PurchaseEvent;
```

Écrivez `handleEvent(event: AppEvent): void` qui affiche (en vous appuyant sur `event.type`) :

- `Utilisateur alice connecté à 12:00`
- `bob a acheté livre pour 25 $`
- `Utilisateur alice déconnecté à 12:30`

### A3 : convertir un tuple en événement typé 🔴

Écrivez `convertToAppEvent(tuple: EventTuple): AppEvent` qui ajoute le champ `type` selon le nom de l'événement. Elle doit **valider** le contenu de `payload` et lever une erreur pour un événement inconnu. Parcourez ensuite `eventLog` :

```ts
for (const event of eventLog) {
    handleEvent(convertToAppEvent(event));
}
```

### A4 : propriété optionnelle 🟢

Ajoutez `metadata?: Record<string, unknown>` à chaque interface d'événement. Si `metadata` existe, terminez le message par `📎 Métadonnées : ...`.

---

## Projet B : gestionnaire de paramètres

```ts
interface UserSettings {
    theme: "light" | "dark";
    notifications: boolean;
    fontSize: "small" | "medium" | "large";
}
```

### B1 : valeurs par défaut 🟢

Créez une constante `defaultSettings` de type `UserSettings`.

### B2 : fusionner des paramètres 🟡

Écrivez `mergeSettings(userSettings: Partial<UserSettings>): UserSettings` qui complète les champs manquants avec `defaultSettings`.

> 💡 Utilisez l'opérateur de **décomposition** (`...`). Attention : `{ theme: undefined }` écrase la valeur par défaut. Comment l'éviter ?

### B3 : valider des paramètres 🟡

Écrivez `validateSettings(settings: Partial<UserSettings>): string[]` qui renvoie la liste des messages d'erreur (par exemple `"Thème invalide : blue"`). Vérifiez chaque clé à la main : c'est un exercice de **rétrécissement de types**.

### B4 : accès dynamique 🔴

```ts
function getSetting<K extends keyof UserSettings>(
    key: K,
    settings: UserSettings
): UserSettings[K];
```

Utilisez-la : `getSetting("theme", mergedSettings)`.

### B5 : type mappé de métadonnées 🔴

```ts
type SettingsMeta = {
    [K in keyof UserSettings]: { label: string; description: string };
};
```

Construisez un objet `settingsInfo: SettingsMeta` décrivant chaque paramètre.

---

## Projet C : calculatrice typée

### C1 : définir les types 🟢

1. Créez `type Operator` valant `"add" | "subtract" | "multiply" | "divide"`.
2. Créez `type Expression = [Operator, number, number]`.

### C2 : l'évaluateur 🟡

```ts
function evaluate(expr: Expression): number;
```

Par exemple, `evaluate(["add", 4, 2])` renvoie `6`.

**Bonus** : pour `"divide"` avec un diviseur nul, levez une erreur d'une **classe personnalisée** (`class DivisionParZeroError extends Error`).

### C3 : historique 🟢

1. Créez `history: Expression[]` et ajoutez-y plusieurs expressions.
2. Écrivez `printHistory` qui parcourt l'historique et affiche `add(4, 2) = 6`.

> Utilisez la **déstructuration** `[op, a, b]`.

### C4 : type utilitaire personnalisé 🔴

```ts
type Result<T extends Expression> = {
    expression: T;
    result: number;
};

function evaluateWithResult<T extends Expression>(expr: T): Result<T>;
```

---

# Partie 5 : asynchrone

### Exercice 18 : promesses et `async` / `await` 🟡

1. Écrivez `fetchData(): Promise<string>` qui se résout avec des données au bout de 2 secondes.
2. Écrivez une fonction `async getData` qui appelle `fetchData` et affiche le résultat.
3. Modifiez `getData` pour gérer le cas où `fetchData` **rejette** la promesse (`try` / `catch`, avec `e` de type `unknown`).
4. Utilisez `Promise.all` pour récupérer plusieurs données **en parallèle** et affichez les résultats (mesurez la durée totale).
5. ➕ Comparez `Promise.all`, `Promise.allSettled` et `Promise.race`.
6. ➕ Ajoutez un **délai maximal** avec `AbortSignal.timeout(1000)` ou `Promise.race`.

---

# Partie 6 : modules, déclarations et configuration

### Exercice 19 : modules et espaces de noms 🟡

1. Créez un module `math.ts` qui exporte `add`, `subtract` et `multiply`.
2. Créez un `namespace Geometry` contenant `circleArea` et `rectangleArea`.
3. Dans `app.ts`, importez les fonctions du module et utilisez l'espace de noms.
4. ➕ Réécrivez `Geometry` **sans** `namespace`, sous forme de module ES (`geometry.ts`) importé avec `import * as Geometry from "./geometry.js"`.

> ⚠️ Les `namespace` sont un héritage d'avant les modules ES. Ils produisent du code à l'exécution, donc ils sont refusés avec `erasableSyntaxOnly`. Vous les rencontrerez dans de vieux projets et dans les fichiers `.d.ts`, mais **préférez les modules ES** dans le code neuf.

---

### Exercice 20 : fichiers de déclaration (`.d.ts`) 🔴

1. **Paquet `@types`** : installez les types d'une bibliothèque courante (par exemple `npm i -D @types/lodash`) et utilisez-la dans votre code.
   > ℹ️ De nombreuses bibliothèques modernes (comme `axios`) **fournissent déjà leurs propres types** : aucun paquet `@types` n'est alors nécessaire. Vérifiez la clé `types` du `package.json` de la bibliothèque.
2. **Fichier `.d.ts` personnalisé** : écrivez les déclarations d'une bibliothèque inventée, puis importez-la dans un fichier TypeScript.
3. **Déclarations ambiantes** : déclarez une constante globale, par exemple `declare const APP_VERSION: string;`.
4. **Bibliothèque JavaScript sans types** : utilisez-la en écrivant votre propre `declare module "nom-de-la-lib"`.

---

### Exercice 21 : configurer la structure du projet 🔴

Configurez un projet où :

- le code source est dans `src/` ;
- le code compilé va dans `build/` ;
- les imports utilisent `@services/` au lieu de chemins relatifs (`@services/utilisateurs.js`).

> ⚠️ **Piège** : l'option `paths` de `tsconfig.json` n'aide que le **compilateur** ; `tsc` ne réécrit pas ces alias dans le JavaScript produit. Il faut en plus un bundler, un outil comme `tsc-alias`, ou l'alternative native de Node.js : les **imports de sous-chemins** (`"imports": { "#services/*": "./build/services/*" }` dans `package.json`).

---

# Partie 7 : décorateurs

### Exercice 22 : décorateurs de méthode, de propriété et de paramètre 🔴

> ℹ️ **Deux systèmes coexistent.** Depuis TypeScript 5.0, les décorateurs **standard** (ECMAScript) sont activés par défaut. L'ancien système (`"experimentalDecorators": true`), utilisé par NestJS, Angular et TypeORM, a une syntaxe différente, et seul lui supporte les décorateurs de **paramètre**.

**Partie A : décorateurs standard**

1. Créez une classe `Book` avec `title` et `author`.
2. Appliquez à une méthode `getBookInfo` un **décorateur de méthode** `logExecutionTime` qui affiche sa durée d'exécution.
3. Appliquez un **décorateur de champ** `capitalize` qui met en majuscule la première lettre de la propriété.

> 💡 Un décorateur standard reçoit `(valeur, context)`. Un décorateur de champ renvoie une fonction qui transforme la valeur initiale.

**Partie B : décorateurs historiques (`experimentalDecorators`)**

4. Activez `experimentalDecorators` dans une copie du projet.
5. Écrivez un **décorateur de paramètre** qui affiche l'indice du paramètre décoré dans une méthode.

---

# Partie 8 : web et frameworks

### Exercice 23 : manipuler le DOM 🟡

> 🌐 Contexte : le navigateur. Ajoutez `"DOM"` à `lib` et servez la page avec Vite (`npm create vite@latest -- --template vanilla-ts`).

1. Ajoutez un formulaire avec un `<input type="text">` et un bouton d'envoi.
2. Gérez l'événement `submit` en TypeScript et affichez la valeur saisie.
3. Typez correctement les éléments du DOM (`HTMLFormElement`, `HTMLInputElement`) et empêchez le rechargement de la page (`event.preventDefault()`).
4. Récupérez un élément avec `getElementById`, **vérifiez qu'il n'est pas `null`** et affichez une erreur s'il est introuvable.
5. Ajoutez un écouteur `input` qui affiche un **aperçu en temps réel** du texte sous le champ.

---

### Exercice 24 : TypeScript avec React, Angular et Vue 🟡

> ℹ️ L'original demandait un fichier `app.ts` dans chaque framework. En réalité, chaque framework a ses propres conventions de fichiers : utilisez les noms ci-dessous.

1. **⚛️ React** (`App.tsx`) :
   - Créez un composant fonction avec une prop `name` de type `string` et un état `greeting` de type `string`.
   - Utilisez `useState<string>` pour modifier `greeting`.
2. **🅰️ Angular** (`message.component.ts` et `message.service.ts`) :
   - Créez un composant **autonome** (`standalone`) qui reçoit une entrée `message` de type `string`. Utilisez la fonction `input<string>()` (entrées à base de *signals*).
   - Créez un service (`@Injectable({ providedIn: "root" })`) qui contient un tableau de `string` et fournit des méthodes pour ajouter et récupérer des messages.
3. **💚 Vue.js** (`Compteur.vue`) :
   - Créez un composant avec `<script setup lang="ts">` qui affiche un `message` de type `string` et incrémente un `count` de type `number` (`ref<number>`) à chaque clic.

---

### Exercice 25 : TypeScript côté serveur (Express et NestJS) 🔴

1. **Express** (`src/app.ts`, avec `@types/express`) :
   - Créez une application avec une route `/hello` qui renvoie `"Bonjour, TypeScript avec Express !"`.
   - Ajoutez un **middleware de gestion d'erreurs** (il prend quatre paramètres : `err, req, res, next`) qui renvoie une réponse JSON contenant un message d'erreur.
   > ℹ️ Express 5 transmet automatiquement au gestionnaire d'erreurs les rejets de promesses des routes `async`.
2. **NestJS** :
   - Créez un DTO `CreateUserDto` avec `name` et `email`. Validez-les avec `class-validator` (`@IsString()`, `@IsEmail()`) et activez le `ValidationPipe`.
   - Créez un contrôleur avec une route `POST /users` qui accepte le DTO (`@Body()`) et renvoie un message de succès.

---

# Partie 9 : bases de données et tests

### Exercice 26 : accès aux données 🔴

> 🔐 Stockez les URL de connexion dans des **variables d'environnement** (fichier `.env`, jamais versionné). Pour lancer les bases en local, utilisez Docker Compose.

1. **MongoDB** :
   - Créez une connexion (pilote officiel ou Mongoose) et définissez un schéma `Product` avec `name`, `price` et `category`.
   - Réalisez un cycle **CRUD** : ajouter un produit, le lire, le modifier, le supprimer.
2. **PostgreSQL** :
   - Configurez une connexion (paquet `pg` et `@types/pg`) et créez une table `Book` avec `title`, `author` et `year_published`.
   - Réalisez le CRUD avec des **requêtes paramétrées** (`$1`, `$2`) pour éviter les injections SQL.
3. **TypeORM** :
   - Créez une entité `Customer` avec `name`, `email` et `phone`, puis réalisez le CRUD.
4. ➕ **Bonus** : refaites l'exercice avec un ORM plus récent, **Prisma** ou **Drizzle**, et comparez la sécurité de typage des requêtes.

---

### Exercice 27 : tests automatisés 🟡

1. **Jest** :
   - Créez `multiply(a: number, b: number): number`.
   - Écrivez des tests pour des valeurs positives, négatives et nulles.
2. **Mocha et Chai** :
   - Créez une classe `BankAccount` avec `deposit(amount)` et `withdraw(amount)`.
   - Écrivez des tests vérifiant que le solde est correctement mis à jour, et qu'un retrait supérieur au solde est refusé.
3. **Simulation (*mocking*)** :
   - Simulez la lecture d'un fichier (`readFileSync` depuis `node:fs`) dans Jest et dans Mocha (avec Sinon), puis testez une fonction qui lit et traite ce fichier.
4. ➕ Refaites l'exercice 1 avec **Vitest** ou le lanceur intégré à Node.js (`node:test` et `node:assert`) : quels avantages par rapport à Jest ?

> 💡 Pour exécuter des tests TypeScript, il faut un transformateur (`ts-jest`, `@swc/jest`, `tsx`…) ou un lanceur qui le gère nativement (Vitest).

---

## Récapitulatif des notions

| Notion | Exercices |
| --- | --- |
| Types de base, inférence, tuples, tableaux | 1, 3 |
| Fonctions (optionnels, rest, surcharge) | 2, 9 |
| `enum`, unions de littéraux, `as const` | 4, 7, 17 |
| Interfaces, alias, héritage de types | 5, 6, 7 |
| Unions discriminées, exhaustivité (`never`) | 8, A2 |
| Classes, `abstract`, `override`, mixins | 10, 13 |
| Génériques et contraintes, `keyof` | 11, 12, B4 |
| Types utilitaires, mappés, conditionnels | 14, 15, B5, C4 |
| `unknown`, gardes de type, `satisfies` | 16, 17, A3 |
| Asynchrone | 18 |
| Modules, déclarations, configuration | 19, 20, 21 |
| Décorateurs | 22 |
| DOM, frameworks, serveur | 23, 24, 25 |
| Bases de données, tests | 26, 27 |
