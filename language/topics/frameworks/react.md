# React — Cours complet

*Cours magistral et module d'apprentissage exhaustif, fondé sur le plan « Cours complet de React : du premier composant aux Server Components » — React 19.x*

## Avant de commencer : comment utiliser ce cours

Ce cours développe, chapitre par chapitre, l'intégralité du plan en **34 chapitres**, regroupés en cinq parties : **Fondamentaux** (1 à 10), **Hooks et architecture des composants** (11 à 15), **Performance, rendu avancé et serveur** (16 à 24), **Données, navigation, état et styles** (25 à 28) et **Qualité et essentiels** (29 à 34).

Chaque chapitre suit la même trame : *objectifs d'apprentissage → notions et définitions → exemples de code commentés → pièges fréquents → synthèse*.

**Conventions de lecture**

- Les exemples sont écrits en **JavaScript moderne (JSX)** ; le chapitre 31 présente **TypeScript avec React**. Chaque exemple est volontairement **autonome** et les imports nécessaires sont indiqués.
- Le cours enseigne le React **actuel** (composants fonctions, Hooks, Actions, `use`, Server Components, React Compiler) **et** explique l'ancien (composants classes, cycle de vie, API historiques) pour que vous sachiez lire du code existant.
- Le contenu couvre React jusqu'à la série **19.x** (dont `useEffectEvent` et `<Activity>`). L'API évolue : en cas de doute, la référence reste <https://react.dev>.
- Les **mises en garde** sont signalées par le terme « piège » ; les notions les plus importantes sont en **gras**.

**Plan du cours**

| Partie | Chapitres |
| --- | --- |
| **I. Fondamentaux** | 1 Introduction · 2 Mise en place · 3 JSX · 4 Composants · 5 Props · 6 State · 7 Gestion des événements · 8 Rendu conditionnel · 9 Listes et clés · 10 Formulaires |
| **II. Hooks et architecture des composants** | 11 Hooks · 12 Hooks personnalisés · 13 Context API · 14 Refs et accès au DOM · 15 Composition et patterns |
| **III. Performance, rendu avancé et serveur** | 16 Performance et optimisation · 17 Suspense et chargement différé · 18 Error Boundaries · 19 Portals · 20 Fragments · 21 Strict Mode · 22 Concurrent Rendering · 23 Server Components et Actions · 24 Composants classes (héritage) |
| **IV. Données, navigation, état et styles** | 25 Récupération de données · 26 Routage · 27 Gestion d'état global · 28 Styles |
| **V. Qualité et essentiels** | 29 Tests · 30 Accessibilité · 31 TypeScript avec React · 32 Bonnes pratiques · 33 Écosystème et frameworks · 34 Glossaire et ressources |

**Parcours conseillé** : lisez les chapitres 1 à 10 dans l'ordre (ils se construisent les uns sur les autres), puis les chapitres 11 à 15 ; choisissez librement dans les parties suivantes selon vos besoins.

---

## 1. Introduction

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : définir précisément ce qu'est React et ce qu'il n'est pas ; comprendre le problème que React résout par rapport à la manipulation directe du DOM ; maîtriser le modèle mental central : **UI = f(state)**, rendu, commit, réconciliation ; connaître l'histoire, les packages et les versions majeures.

### 1.1 Qu'est-ce que React ?

**React** est une **bibliothèque JavaScript open source** destinée à construire des **interfaces utilisateur** (UI). Elle a été créée chez Facebook (aujourd'hui Meta) par Jordan Walke, utilisée en production dès 2011 pour le fil d'actualité, puis ouverte au public en 2013.

#### Bibliothèque ou framework ?

| Critère | Bibliothèque (React) | Framework (Angular, par exemple) |
|---|---|---|
| Périmètre | La **couche vue** : composants, état, rendu | Solution complète : routage, HTTP, formulaires, DI, build… |
| Contrôle | Vous choisissez les autres briques | Le framework impose une structure |
| Courbe d'apprentissage | Cœur petit, mais choix d'écosystème à faire | Beaucoup de concepts d'emblée |
| Inversion de contrôle | Vous appelez React | Le framework vous appelle |

React seul **ne fournit pas** : de routeur, de client HTTP, de gestion d'état global, de système de styles, d'outil de build. C'est pourquoi des **méta-frameworks** (Next.js, React Router v7 en mode framework, Expo…) existent : ils assemblent React avec ces briques. Depuis la documentation officielle actuelle, React recommande d'ailleurs de démarrer un nouveau projet avec un framework ou un outil de build comme Vite.

#### Ce que React fait

1. Décrit l'UI sous forme d'un **arbre de composants**.
2. **Calcule** la différence entre deux états de l'UI.
3. **Met à jour** efficacement la cible de rendu (DOM navigateur, mobile natif, HTML serveur, PDF, terminal…).

React est **agnostique de la cible** : le cœur (`react`) décrit les éléments et composants ; un **renderer** (`react-dom`, `react-native`, `react-pdf`, `ink`…) les traduit en sortie concrète.

### 1.2 Le problème résolu : DOM impératif vs UI déclarative

#### Approche impérative (JavaScript « vanilla »)

On décrit **comment** modifier l'interface, étape par étape :

```js
const bouton = document.querySelector('#like');
const compteur = document.querySelector('#compteur');
let likes = 0;

bouton.addEventListener('click', () => {
  likes++;
  compteur.textContent = likes;                       // 1. mettre à jour le texte
  bouton.classList.toggle('actif', likes > 0);        // 2. mettre à jour la classe
  if (likes >= 10) {
    document.querySelector('#badge').hidden = false;  // 3. afficher le badge
  }
});
```

Dès que l'application grossit, il faut synchroniser **à la main** l'état et le DOM. Chaque nouvelle fonctionnalité multiplie les cas : on oublie une mise à jour, l'interface devient incohérente (bugs d'état « fantômes »).

#### Approche déclarative (React)

On décrit **à quoi** doit ressembler l'UI pour un état donné ; React se charge des transitions :

```jsx
function Like() {
  const [likes, setLikes] = useState(0);

  return (
    <>
      <button className={likes > 0 ? 'actif' : ''} onClick={() => setLikes(likes + 1)}>
        👍 {likes}
      </button>
      {likes >= 10 && <span>Badge 🏅</span>}
    </>
  );
}
```

Il n'y a plus de « mise à jour du DOM » dans votre code : seulement une **fonction** qui, pour un nombre de likes donné, retourne la description de l'interface.

### 1.3 Les principes fondamentaux

#### 1.3.1 Déclaratif

Vous décrivez l'**état cible**, pas le chemin pour y arriver. Penser en React = lister les **états visuels** possibles d'un composant (vide, chargement, erreur, succès…) et décrire l'UI de chacun.

#### 1.3.2 Composants

Un **composant** est une unité d'UI **isolée, réutilisable et composable**. Une application est un **arbre** de composants : `App` contient `Header`, `Main`, `Footer`, etc., qui contiennent eux-mêmes d'autres composants.

#### 1.3.3 Flux de données unidirectionnel (« one-way data flow »)

Les données descendent **du parent vers l'enfant** via les **props**. Un enfant ne modifie jamais directement les données du parent ; il appelle une **fonction** reçue en prop (callback), et c'est le parent qui change son état. Conséquence : le cheminement des données est **prévisible** et le débogage plus simple.

```
        App (state: utilisateur)
         │ props ↓          ↑ callbacks (onChange…)
     ┌───┴────┐
  Header    Profil
```

#### 1.3.4 UI = f(state)

L'interface est une **fonction pure** de l'état (et des props / du contexte). Même entrée → même sortie. C'est la formule centrale de React.

#### 1.3.5 Pureté du rendu

Pendant le rendu, un composant ne doit **ni modifier** des variables externes **ni produire d'effets de bord** (requêtes, écriture DOM, timers). Cette contrainte permet à React d'appeler un composant plusieurs fois, de l'interrompre, de le rejouer ou de l'ignorer (rendu concurrent).

#### 1.3.6 Immutabilité

On ne **mute** pas les données du state ; on crée de **nouvelles valeurs**. React compare les références (`Object.is`) pour savoir si quelque chose a changé.

#### 1.3.7 « Learn once, write anywhere »

Les concepts (composants, props, state, hooks) sont identiques sur le web, le mobile (React Native), le serveur, etc.

### 1.4 Virtual DOM, réconciliation et Fiber

#### Le coût du DOM

Manipuler le DOM réel est relativement coûteux (recalcul de styles, layout, peinture). Les opérations isolées sont rapides, mais en faire beaucoup de façon non coordonnée dégrade les performances.

#### Le Virtual DOM

Le **Virtual DOM** est un **arbre d'objets JavaScript légers** (les « React elements ») décrivant l'UI désirée :

```js
// <h1 className="titre">Salut</h1> produit approximativement :
{
  type: 'h1',
  props: { className: 'titre', children: 'Salut' },
  key: null
}
```

#### La réconciliation (« diffing »)

À chaque rendu, React obtient un **nouvel arbre** et le compare à l'**ancien** pour déterminer le **minimum de changements** à appliquer au DOM. Un algorithme général de comparaison d'arbres serait en O(n³) ; React utilise deux **heuristiques** pour obtenir du O(n) :

1. **Deux éléments de types différents produisent des arbres différents.** Si `<div>` devient `<span>` (ou `<A />` devient `<B />`), React **détruit** l'ancien sous-arbre (état inclus) et **reconstruit** le nouveau.
2. **Les `key` identifient les éléments stables** parmi des frères. Elles permettent de détecter les déplacements dans une liste.

Si le type est identique, React **réutilise le nœud existant** et ne met à jour que les attributs qui ont changé.

#### React Fiber

**Fiber** est la réécriture du moteur de réconciliation (React 16). Chaque composant correspond à une **unité de travail** (un « fiber »). Le travail peut être **découpé, mis en pause, repris ou abandonné**, et chaque mise à jour reçoit une **priorité** (une saisie clavier est plus urgente qu'un graphique). C'est le socle du **rendu concurrent** (React 18+).

### 1.5 Le cycle : déclencher, rendre, valider (commit)

React met à jour l'écran en **trois étapes**, que l'on compare souvent à un restaurant : le client **passe commande** (déclenchement), la cuisine **prépare** (rendu), le serveur **apporte le plat** (commit).

#### Étape 1 : Déclenchement (trigger)

Deux causes :
1. Le **rendu initial** (`root.render(<App />)`).
2. Une **mise à jour d'état** (un `setState`, `dispatch`, etc.) du composant ou d'un de ses ancêtres.

#### Étape 2 : Rendu (render)

React **appelle vos composants** pour obtenir leur JSX.
- Au rendu initial : appel du composant racine, puis récursivement de tous les enfants.
- Aux rendus suivants : appel des composants dont l'état a changé, **et de leurs descendants** (sauf optimisation avec `memo`).

Cette phase doit être **pure** : aucun effet de bord. Elle ne touche pas le DOM.

#### Étape 3 : Commit

- Au rendu initial : React crée les nœuds DOM (`appendChild`).
- Aux rendus suivants : React applique le **minimum d'opérations** pour que le DOM corresponde à la sortie du rendu.
- React **ne modifie le DOM que si la sortie du rendu a changé** entre deux rendus.

#### Étape 4 (après le commit) : Effets et peinture

Après le commit, le navigateur **peint** l'écran. Les **effets** (`useEffect`) s'exécutent généralement **après** la peinture ; `useLayoutEffect` s'exécute **avant** la peinture, juste après la mise à jour du DOM.

#### Le state comme « instantané » (snapshot)

Chaque rendu est une **photo figée** : les valeurs de props, state et variables locales y sont **constantes**. Appeler `setCount(count + 1)` ne change pas `count` dans le rendu en cours ; cela **planifie** un nouveau rendu avec une nouvelle valeur.

```jsx
function Exemple() {
  const [n, setN] = useState(0);
  function clic() {
    setN(n + 1);
    console.log(n); // affiche encore l'ANCIENNE valeur (0 au premier clic)
  }
  return <button onClick={clic}>{n}</button>;
}
```

### 1.6 Les packages et l'architecture

| Package | Rôle |
|---|---|
| `react` | Cœur : `createElement`, hooks, `memo`, `lazy`, `Suspense`, `Fragment`, `createContext`… Indépendant de la plateforme. |
| `react-dom` | Renderer pour le **navigateur** : `createPortal`, `flushSync`, API de préchargement, `useFormStatus`. |
| `react-dom/client` | `createRoot`, `hydrateRoot`. |
| `react-dom/server` | Rendu serveur : `renderToString`, `renderToPipeableStream`, `renderToReadableStream`. |
| `react-dom/static` | Pré-rendu statique : `prerender`, `prerenderToNodeStream`. |
| `react-native` | Renderer pour iOS/Android. |
| `scheduler` | Planificateur interne des tâches (priorités). |
| `react-reconciler` | Pour écrire son **propre renderer**. |

### 1.7 Historique et versions majeures

| Version | Date (approx.) | Apport principal |
|---|---|---|
| 0.3 | 2013 | Ouverture en open source |
| 15 | 2016 | Rendu amélioré, SVG |
| **16** | 2017 | **Fiber**, Error Boundaries, Portals, Fragments |
| **16.8** | 2019 | **Hooks** |
| 17 | 2020 | « Version sans nouvelle fonctionnalité » : mise à jour progressive, délégation d'événements à la racine |
| **18** | 2022 | **Rendu concurrent**, batching automatique, Transitions, Suspense côté serveur, `createRoot`, `useId`… |
| **19** | 2024 | **Actions**, `use`, `useActionState`, `useOptimistic`, `ref` comme prop, métadonnées de document, Server Components stables |
| **19.2** | 2025 | `<Activity>`, `useEffectEvent`, pistes de performance dans les DevTools |

> **Mise en garde** : Create React App est officiellement **déprécié** (2025). Les projets neufs utilisent Vite ou un framework.

### 1.8 Pièges fréquents

- Croire que React est un framework complet (le routage, le fetch, etc. ne sont pas inclus).
- Croire que le Virtual DOM est « toujours plus rapide » que le DOM : il apporte surtout un **modèle de programmation** déclaratif avec des performances suffisantes.
- Penser que `setState` modifie immédiatement la variable.
- Confondre **rendu** (appeler le composant) et **mise à jour du DOM** (commit) : un composant peut être rendu sans que le DOM change.

### Synthèse du chapitre 1

React = bibliothèque d'UI **déclarative**, basée sur des **composants**, avec un flux **unidirectionnel** ; **UI = f(state)** ; le rendu doit être **pur** ; Cycle : **déclenchement → rendu → commit**, puis effets ; Le **state est un instantané** par rendu ; La réconciliation s'appuie sur le **type** des éléments et les **clés**.

---

## 2. Mise en place

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : disposer des **prérequis JavaScript** indispensables ; créer, lancer et comprendre la structure d'un projet React moderne ; savoir initialiser React (`createRoot`, `hydrateRoot`) et configurer l'outillage de base.

### 2.1 Prérequis JavaScript

React demande une solide maîtrise du JavaScript moderne (ES2015+). Rappel des notions utilisées en permanence.

#### Variables et portée

```js
const PI = 3.14;        // constante (référence non réassignable)
let compteur = 0;       // variable réassignable, portée de bloc
// var : à éviter (portée de fonction, hoisting)
```

#### Fonctions fléchées et closures

```js
const double = (x) => x * 2;
const creerCompteur = () => {
  let n = 0;
  return () => ++n;       // closure : la fonction retournée "se souvient" de n
};
```

> Les **closures** sont au cœur du fonctionnement des hooks et de la notion de snapshot.

#### Destructuration

```js
const { nom, age = 18, ...reste } = utilisateur;   // objets
const [premier, , troisieme] = liste;              // tableaux
function Carte({ titre, children }) {}             // dans les paramètres
```

#### Spread et rest

```js
const copie = { ...utilisateur, nom: 'Bob' };       // copie d'objet avec modification
const fusion = [...tableauA, ...tableauB];          // copie / concaténation de tableaux
function somme(...nombres) {}                       // rest : collecte les arguments
```

#### Méthodes de tableaux (essentielles)

```js
[1, 2, 3].map(x => x * 2);            // transforme : [2, 4, 6]
[1, 2, 3].filter(x => x > 1);         // filtre : [2, 3]
[1, 2, 3].reduce((a, x) => a + x, 0); // agrège : 6
[1, 2, 3].find(x => x > 1);           // premier élément : 2
[1, 2, 3].some(x => x > 2);           // au moins un : true
[1, 2, 3].every(x => x > 0);          // tous : true
[3, 1, 2].toSorted();                 // copie triée (ES2023) — sort() MUTE le tableau
```

#### Modules ES

```js
// math.js
export const PI = 3.14;
export default function aire(r) { return PI * r * r; }

// app.js
import aire, { PI } from './math.js';
import * as math from './math.js';
```

#### Opérateurs modernes

```js
utilisateur?.adresse?.ville     // optional chaining
valeur ?? 'défaut'              // nullish coalescing (seulement null/undefined)
valeur || 'défaut'              // fallback sur toute valeur falsy (0, '' inclus)
a ||= b;  a &&= b;  a ??= b;    // assignations logiques
`Bonjour ${nom}`                // template literals
```

#### Asynchronisme

```js
async function charger() {
  try {
    const reponse = await fetch('/api/users');
    if (!reponse.ok) throw new Error(`HTTP ${reponse.status}`);
    return await reponse.json();
  } catch (e) {
    console.error(e);
  }
}
Promise.all([charger(), autreAppel()]);  // en parallèle
```

#### Égalité et références

```js
Object.is(a, b)      // utilisé par React pour comparer
{} === {}            // false : deux objets distincts
const o = {}; o === o // true : même référence
```

> **Valeurs primitives** (nombre, chaîne, booléen, `null`, `undefined`, `bigint`, `symbol`) sont comparées par valeur ; **objets, tableaux, fonctions** par **référence**. C'est fondamental pour comprendre `useEffect`, `useMemo` et `memo`.

#### Valeurs « falsy »

`false`, `0`, `-0`, `0n`, `''`, `null`, `undefined`, `NaN`. Tout le reste est « truthy » (y compris `[]`, `{}`, `'0'`).

### 2.2 Environnement de développement

1. **Node.js** (version LTS) + gestionnaire de paquets : `npm` (inclus), `pnpm`, `yarn` ou `bun`.
2. Un **éditeur** (VS Code recommandé) avec les extensions ESLint, Prettier, ES7+ React snippets.
3. **Navigateur** + extension **React Developer Tools** (onglets *Components* et *Profiler*).
4. **Git** pour le versionnage.

### 2.3 Créer un projet

#### Option A : Vite (SPA)

```bash
npm create vite@latest mon-app -- --template react        # JavaScript
npm create vite@latest mon-app -- --template react-ts     # TypeScript
cd mon-app
npm install
npm run dev        # serveur de développement (HMR)
npm run build      # build de production dans dist/
npm run preview    # prévisualiser le build
```

**Vite** utilise des modules ES natifs en développement (démarrage quasi instantané) et Rollup (ou Rolldown selon les versions) pour la production. Le **HMR** (Hot Module Replacement) met à jour le module modifié sans recharger la page, en préservant l'état quand c'est possible (*React Fast Refresh*).

#### Option B : Framework

```bash
npx create-next-app@latest          # Next.js
npx create-react-router@latest      # React Router en mode framework
npx create-expo-app@latest          # Mobile (React Native / Expo)
```

À choisir si vous avez besoin de **SSR/SSG**, de **routage par fichiers**, de **Server Components**, de SEO.

#### Option C : Sans outil de build (démonstration seulement)

```html
<script type="importmap">
  { "imports": { "react": "https://esm.sh/react@19", "react-dom/client": "https://esm.sh/react-dom@19/client" } }
</script>
```

Utile pour apprendre, **inadapté** à la production.

### 2.4 Anatomie d'un projet Vite

```
mon-app/
├── index.html           # point d'entrée HTML (contient <div id="root">)
├── package.json         # dépendances et scripts
├── vite.config.js       # configuration Vite (plugins, alias, proxy)
├── eslint.config.js     # règles de lint
├── public/              # fichiers servis tels quels (favicon, robots.txt)
└── src/
    ├── main.jsx         # point d'entrée JS : monte React dans #root
    ├── App.jsx          # composant racine
    ├── App.css
    ├── index.css
    └── assets/          # images importées par le code (hashées au build)
```

**`index.html`** :

```html
<!doctype html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Mon app</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
```

**`src/main.jsx`** :

```jsx
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import App from './App.jsx';
import './index.css';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
```

### 2.5 Initialiser React : les « roots »

#### `createRoot` : rendu côté client

```jsx
import { createRoot } from 'react-dom/client';

const root = createRoot(document.getElementById('root'), {
  // options facultatives (React 19) :
  onCaughtError(error, info) { /* erreur capturée par un Error Boundary */ },
  onUncaughtError(error, info) { /* erreur non capturée */ },
  onRecoverableError(error, info) { /* erreur dont React s'est remis */ },
  identifierPrefix: 'app1-',   // préfixe des useId (utile avec plusieurs roots)
});

root.render(<App />);
// root.render(<AutreApp />);  // un nouvel appel remplace l'arbre
// root.unmount();             // démonte tout l'arbre
```

#### `hydrateRoot` : « hydrater » du HTML généré par le serveur

```jsx
import { hydrateRoot } from 'react-dom/client';
hydrateRoot(document.getElementById('root'), <App />);
```

L'**hydratation** attache les gestionnaires d'événements et l'état React à un HTML **déjà présent**. Le rendu client doit produire **exactement le même HTML** que le serveur, sinon : erreur d'hydratation (*hydration mismatch*).

#### Plusieurs roots

On peut monter plusieurs applications React indépendantes dans une même page (intégration progressive dans un site existant). Chaque root a son propre arbre et son propre état.

#### Migration depuis les API historiques

| Ancienne API (supprimée en 19) | Remplacement |
|---|---|
| `ReactDOM.render` | `createRoot(...).render` |
| `ReactDOM.hydrate` | `hydrateRoot` |
| `ReactDOM.unmountComponentAtNode` | `root.unmount()` |
| `ReactDOM.findDOMNode` | `ref` |
| `propTypes` / `defaultProps` (fonctions) | TypeScript / paramètres par défaut |
| refs en chaîne de caractères | refs d'objet / callback |

### 2.6 Configuration utile

#### Variables d'environnement (Vite)

```bash
# .env
VITE_API_URL=https://api.exemple.com
SECRET=non_expose_au_client      # PAS de préfixe VITE_ = non exposée
```

```js
const url = import.meta.env.VITE_API_URL;
```

> Tout ce qui est préfixé `VITE_` est **embarqué dans le bundle** et donc **public**. Ne mettez jamais de secret côté client.

#### Alias d'import

```js
// vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'node:path';

export default defineConfig({
  plugins: [react()],
  resolve: { alias: { '@': path.resolve(__dirname, 'src') } },
  server: { proxy: { '/api': 'http://localhost:3000' } },   // évite les problèmes CORS en dev
});
```

```jsx
import Header from '@/components/Header';
```

#### Outils de qualité

- **ESLint** + `eslint-plugin-react-hooks` : détecte les violations des règles des hooks et les dépendances manquantes.
- **Prettier** : formatage automatique.
- **TypeScript** : typage statique (chapitre 31).
- **Husky + lint-staged** : vérifications avant commit.

#### Les React DevTools

- **Components** : arbre des composants, inspection/modification des props, du state et des hooks.
- **Profiler** : enregistrement des rendus, durée, cause de chaque rendu (« why did this render? »).

### 2.7 Fil rouge du cours

Pour fixer les notions, imaginez une application de **gestion de tâches** (*Todo*) que l'on enrichit module après module : liste (chapitre 9), formulaire (10), persistance via hook personnalisé (12), thème via Context (13), chargement via API (25), routage (26), tests (29).

### 2.8 Pièges fréquents

- Importer React inutilement : depuis la **transformation JSX automatique** (React 17+), `import React from 'react'` n'est plus nécessaire pour écrire du JSX.
- Oublier `type="module"` sur le script d'entrée.
- Exposer des secrets via `VITE_…`.
- Mélanger **extension `.js`** et JSX : avec Vite, utilisez `.jsx` / `.tsx` pour les fichiers contenant du JSX.

### Synthèse du chapitre 2

Utilisez **Vite** pour une SPA, un **framework** pour du SSR/SEO ; `createRoot` (client), `hydrateRoot` (HTML serveur) ; `StrictMode` à la racine en développement ; Variables d'environnement côté client = **publiques**.

---

## 3. JSX

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : comprendre ce qu'est JSX et comment il est compilé ; maîtriser toutes les règles de syntaxe (attributs, enfants, expressions, fragments) ; savoir ce que React affiche (ou non) pour chaque type de valeur ; connaître les mécanismes de sécurité et les différences avec HTML.

### 3.1 Définition

**JSX** (*JavaScript XML*) est une **extension de syntaxe de JavaScript** qui permet d'écrire des structures ressemblant à du HTML directement dans le code. Ce n'est **ni du HTML, ni une chaîne de caractères, ni un langage de template** : c'est du **sucre syntaxique** qui est **compilé** (par Babel, SWC, esbuild/Oxc, TypeScript) en appels de fonctions JavaScript.

Pourquoi JSX ? Parce que la **logique de rendu** et le **balisage** sont intrinsèquement liés (un clic modifie ce qui s'affiche). React les regroupe par **composant** plutôt que de séparer artificiellement « HTML d'un côté, JS de l'autre ».

### 3.2 Compilation : ce que devient JSX

```jsx
const element = <h1 className="titre">Bonjour, {nom} !</h1>;
```

#### Ancienne transformation (« classic runtime »)

```js
const element = React.createElement('h1', { className: 'titre' }, 'Bonjour, ', nom, ' !');
```

#### Transformation actuelle (« automatic runtime », React 17+)

```js
import { jsx as _jsx, jsxs as _jsxs } from 'react/jsx-runtime';
const element = _jsxs('h1', { className: 'titre', children: ['Bonjour, ', nom, ' !'] });
```

L'import est **injecté automatiquement** : plus besoin d'écrire `import React from 'react'`.

#### Ce que retourne ce code : un « React element »

Un **élément React** est un **objet JavaScript simple, immuable**, qui **décrit** ce que l'on veut voir à l'écran :

```js
{
  $$typeof: Symbol(react.transitional.element),
  type: 'h1',
  key: null,
  props: { className: 'titre', children: ['Bonjour, ', 'Alice', ' !'] }
}
```

> **Élément ≠ composant ≠ instance** :
> - **Composant** : une fonction (ou classe) qui **retourne** des éléments.
> - **Élément** : l'objet de **description** (léger, jetable).
> - **Instance** : l'entité interne que React gère pour conserver l'état d'un composant monté (invisible pour le développeur).

### 3.3 Règles de syntaxe

#### Règle 1 : un seul nœud racine

Une expression JSX ne peut retourner **qu'un seul élément parent**. Pour regrouper sans ajouter de nœud DOM : **Fragment**.

```jsx
// ❌ Erreur : deux éléments adjacents
return (
  <h1>Titre</h1>
  <p>Texte</p>
);

// ✅ Fragment (syntaxe courte)
return (
  <>
    <h1>Titre</h1>
    <p>Texte</p>
  </>
);
```

> Pourquoi ? Une fonction ne retourne qu'**une seule valeur** ; JSX est compilé en un appel de fonction unique.

#### Règle 2 : fermer toutes les balises

```jsx
<img src="a.png" alt="" />   // auto-fermante obligatoire
<input type="text" />
<br />
<MonComposant />
```

#### Règle 3 : attributs en camelCase

JSX est plus proche de JavaScript que de HTML ; les attributs deviennent des **propriétés d'objet**, et certains noms sont des mots réservés JS.

| HTML | JSX |
|---|---|
| `class` | `className` |
| `for` | `htmlFor` |
| `tabindex` | `tabIndex` |
| `onclick` | `onClick` |
| `maxlength` | `maxLength` |
| `readonly` | `readOnly` |
| `autofocus` | `autoFocus` |
| `contenteditable` | `contentEditable` |
| `stroke-width` (SVG) | `strokeWidth` |
| `fill-rule` (SVG) | `fillRule` |
| `xlink:href` (SVG) | `xlinkHref` (ou `href`) |

**Exceptions** : les attributs `data-*` et `aria-*` restent **en minuscules avec tirets**.

```jsx
<div data-testid="carte" aria-label="Fermer" role="dialog" />
```

#### Règle 4 : les expressions JavaScript entre accolades

Les **accolades** `{}` ouvrent une « fenêtre » vers JavaScript. On peut y mettre **toute expression** (qui produit une valeur), **pas** des instructions (`if`, `for`, `const`…).

Deux endroits possibles :

```jsx
// 1. Comme CONTENU d'une balise
<h1>{titre.toUpperCase()}</h1>
<p>Total : {prix * quantite} €</p>
<p>{utilisateur.estConnecte ? 'Connecté' : 'Déconnecté'}</p>

// 2. Comme VALEUR d'un attribut (à la place des guillemets)
<img src={utilisateur.avatar} alt={`Photo de ${utilisateur.nom}`} />
<button disabled={chargement} onClick={supprimer}>Supprimer</button>
```

```jsx
// ❌ Une instruction n'est pas une expression
<p>{if (ok) 'oui'}</p>
// ✅ Utiliser un ternaire ou &&
<p>{ok ? 'oui' : 'non'}</p>
```

#### Règle 5 : « double accolades » = objet dans des accolades

```jsx
<div style={{ backgroundColor: 'tomato', fontSize: 16, marginTop: '1rem' }} />
//          ↑ accolade JSX  ↑ objet JavaScript
```

- Les propriétés de `style` sont en **camelCase** (`backgroundColor`).
- Les nombres sont convertis en `px` (sauf propriétés sans unité comme `opacity`, `zIndex`, `flex`, `lineHeight`).

#### Règle 6 : commentaires

```jsx
<div>
  {/* commentaire JSX */}
  <p
    // commentaire dans les attributs
    id="a"
  />
</div>
```

#### Règle 7 : parenthèses pour le multi-ligne

```jsx
function Carte() {
  return (          // sans parenthèses, `return` suivi d'un saut de ligne retourne undefined (ASI) !
    <div>...</div>
  );
}
```

### 3.4 Attributs en détail

#### Valeurs d'attributs

```jsx
<input value="texte" />           {/* chaîne littérale */}
<input value={variable} />        {/* expression */}
<input disabled />                {/* équivaut à disabled={true} */}
<input disabled={false} />        {/* attribut absent */}
```

#### Attributs booléens

`disabled`, `checked`, `readOnly`, `required`, `hidden`, `autoFocus`, `multiple`, `selected`… : `true` ajoute l'attribut, `false`/`null`/`undefined` le retire.

#### `className` dynamique

```jsx
<div className={`carte ${actif ? 'carte--actif' : ''}`} />
<div className={['carte', actif && 'carte--actif'].filter(Boolean).join(' ')} />
// avec la bibliothèque clsx :
<div className={clsx('carte', { 'carte--actif': actif }, taille && `carte--${taille}`)} />
```

#### Spread d'attributs

```jsx
const props = { id: 'btn', type: 'button', disabled: false };
<button {...props} className="primaire">Valider</button>
```

> L'**ordre** compte : `<Comp {...a} x="1" />` → `x` écrase `a.x` ; `<Comp x="1" {...a} />` → `a.x` écrase `x`.

#### Valeurs par défaut des champs de formulaire

`defaultValue` / `defaultChecked` : valeur **initiale** (champ non contrôlé) ; `value` / `checked` : champ **contrôlé** (chapitre 10).

#### Attributs spéciaux de React

| Attribut | Rôle |
|---|---|
| `key` | Identité stable dans une liste (chapitre 9). Non transmis au composant. |
| `ref` | Référence vers un nœud DOM ou une instance (chapitre 14). Prop normale depuis React 19. |
| `dangerouslySetInnerHTML` | Injection de HTML brut (`{{ __html: '...' }}`). |
| `suppressHydrationWarning` | Désactive l'avertissement pour une différence volontaire serveur/client (dates, par exemple). |
| `children` | Contenu entre les balises. |

### 3.5 Les enfants (children)

Entre balises ouvrante et fermante, on peut placer :

1. du **texte** ;
2. des **éléments** JSX (hôtes `<div>` ou composants `<Carte>`) ;
3. des **expressions** `{...}` ;
4. des **tableaux** d'éléments (chaque élément doit avoir une `key`) ;
5. des **fonctions** (si le composant les attend : *render props*, chapitre 15).

```jsx
<ul>
  <li>Texte</li>
  {valeur}
  {liste.map(el => <li key={el.id}>{el.nom}</li>)}
</ul>
```

#### Ce que React affiche, selon la valeur

| Valeur | Rendu |
|---|---|
| `string` | Texte (échappé) |
| `number` | Texte (`0` s'affiche !) |
| `bigint` | Texte |
| `true` / `false` | **Rien** |
| `null` / `undefined` | **Rien** |
| `[]` (tableau vide) | Rien |
| Tableau d'éléments | Chacun est rendu (clés requises) |
| Élément React | Rendu |
| Objet simple `{}` | ❌ **Erreur** « Objects are not valid as a React child » |
| Fonction | Avertissement, rien affiché |
| `Promise` | Uniquement dans un composant serveur/avec `use` (sinon erreur) |

```jsx
<p>{true}</p>   {/* rien */}
<p>{0}</p>      {/* affiche 0 */}
<p>{'0'}</p>    {/* affiche 0 */}
<p>{String(true)}</p> {/* affiche "true" */}
```

#### Gestion des espaces et sauts de ligne

JSX **supprime** les espaces en début/fin de ligne et les lignes vides ; plusieurs espaces/sauts de ligne **entre deux mots** sont condensés en un seul espace. Pour forcer un espace : `{' '}`.

```jsx
<p>
  Bonjour
  <strong>{nom}</strong>   {/* PAS d'espace entre "Bonjour" et <strong> */}
</p>

<p>
  Bonjour{' '}
  <strong>{nom}</strong>   {/* espace conservé */}
</p>
```

### 3.6 Composants dans JSX : majuscule obligatoire

JSX distingue **balises natives** (minuscule) et **composants** (majuscule ou notation pointée) :

```jsx
<div />          // → React.createElement('div')  (élément DOM)
<Carte />        // → createElement(Carte)        (composant)
<carte />        // → élément DOM inconnu "carte" (probable erreur !)
<Menu.Item />    // → propriété d'objet : composant Menu.Item (composants « composés »)
```

#### Type d'élément choisi dynamiquement

```jsx
const composants = { photo: PhotoStory, video: VideoStory };

function Story({ type, ...props }) {
  // ❌ <composants[type] {...props} />   (syntaxe invalide)
  const Composant = composants[type];     // ✅ variable en MAJUSCULE
  return <Composant {...props} />;
}

function Titre({ niveau, children }) {
  const Balise = `h${niveau}`;            // une chaîne : balise native
  return <Balise>{children}</Balise>;
}
```

### 3.7 JSX est une expression

Comme JSX produit un objet, on peut l'**affecter**, le **passer**, le **retourner**, le **stocker** :

```jsx
const entete = <h1>Titre</h1>;

function Page({ avecEntete }) {
  let contenu = <p>Contenu</p>;
  if (avecEntete) {
    contenu = <>{entete}{contenu}</>;
  }
  return <main>{contenu}</main>;
}

<Carte titre={<strong>Important</strong>} />   // JSX comme prop
```

### 3.8 Sécurité : échappement automatique et XSS

React **échappe** toute valeur insérée via `{}` avant de la placer dans le DOM : `<`, `>`, `&`, `"`, `'` sont neutralisés.

```jsx
const saisie = '<img src=x onerror="alert(1)">';
<p>{saisie}</p>   // affiche le TEXTE littéral ; aucun script exécuté
```

#### `dangerouslySetInnerHTML`

Nom volontairement alarmant : il **contourne la protection**.

```jsx
<div dangerouslySetInnerHTML={{ __html: htmlNettoye }} />
```

> N'injectez **jamais** du HTML provenant d'une source non fiable sans **assainissement** (par exemple avec **DOMPurify**). Notez aussi que des URLs `javascript:` dans `href` restent un vecteur : validez les URLs provenant des utilisateurs.

### 3.9 Différences JSX / HTML (synthèse)

| Sujet | HTML | JSX |
|---|---|---|
| Classe CSS | `class` | `className` |
| Style inline | `style="color:red"` | `style={{ color: 'red' }}` |
| Événements | `onclick="fn()"` | `onClick={fn}` |
| Balises | Certaines non fermées | **Toutes fermées** |
| Booléens | `disabled="disabled"` | `disabled` ou `disabled={true}` |
| Racine | Plusieurs nœuds frères possibles | Un seul parent (ou Fragment) |
| Commentaires | `<!-- -->` | `{/* */}` |
| Entités | `&nbsp;` `&copy;` | Fonctionnent aussi, ou caractères Unicode/`{'\u00A0'}` |
| Casse | Insensible | **Sensible** |

### 3.10 API associées (cas avancés)

```jsx
import { createElement, cloneElement, isValidElement, Children } from 'react';

createElement('button', { onClick: fn }, 'Clic');           // équivalent bas niveau de JSX
isValidElement(valeur);                                      // true si élément React
cloneElement(element, { extra: 1 });                         // ⚠ patterns fragiles, déconseillé
Children.map(children, enfant => ...);                       // ⚠ utilitaires hérités, peu recommandés
```

> L'API `Children` et `cloneElement` rendent le code fragile (dépendance à la forme exacte des enfants). Préférez la **composition explicite**, les **props** ou le **Context** (chapitre 15).

### 3.11 Pièges fréquents

- `return` suivi d'un saut de ligne sans parenthèses → `undefined`.
- Afficher un **objet** directement : `{utilisateur}` → erreur. Affichez ses champs.
- `{liste.length && <Liste />}` affiche **`0`** si la liste est vide. Utilisez `liste.length > 0 &&`.
- Mettre `class` au lieu de `className` (avertissement) ou `for` au lieu de `htmlFor`.
- Oublier la majuscule d'un composant.
- Écrire `onClick={fonction()}` qui **appelle** la fonction pendant le rendu, au lieu de `onClick={fonction}`.

### Synthèse du chapitre 3

JSX est compilé en **appels de fonctions** qui produisent des **objets** (éléments) ; `{}` = expression JavaScript ; `{{}}` = objet dans une expression ; Un seul parent, balises fermées, attributs en camelCase ; `true/false/null/undefined` ne rendent **rien**, `0` rend « 0 » ; Le contenu inséré est **échappé** : protection XSS par défaut.

---

## 4. Composants

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : définir un composant, ses règles de nommage, d'export et de structuration ; comprendre la **pureté**, l'**identité** d'un composant et la préservation de son état ; savoir découper une interface en composants.

### 4.1 Définition

Un **composant** est une **fonction JavaScript** (ou, historiquement, une classe) qui :
1. reçoit un unique argument : l'objet **`props`** ;
2. **retourne** ce que React doit afficher (le plus souvent du JSX).

```jsx
function Salutation({ nom }) {
  return <h1>Bonjour {nom} !</h1>;
}

const Salutation2 = ({ nom }) => <h1>Bonjour {nom} !</h1>;   // flèche
```

#### Valeurs de retour possibles

JSX, `null` (rien), chaînes, nombres, **tableaux** (avec clés), `undefined` (autorisé depuis React 18), **Promesses** (composants serveur), éléments `<Fragment>`.

### 4.2 Règles de nommage et de définition

1. **Nom en PascalCase** (`MaCarte`), sinon JSX le traite comme une balise native.
2. **Définir au niveau supérieur du module**, **jamais à l'intérieur d'un autre composant**.
3. Un composant par responsabilité ; généralement **un composant principal par fichier**.
4. Utiliser le **même nom** pour le fichier et le composant (`Carte.jsx` → `Carte`).

#### Piège : composant défini dans un composant

```jsx
function Parent() {
  const [n, setN] = useState(0);

  // ❌ Nouvelle fonction (donc nouveau « type ») à CHAQUE rendu de Parent :
  //    React détruit et recrée Enfant (perte d'état, lenteur, perte de focus)
  function Enfant() { return <input />; }

  return <Enfant />;
}

// ✅ Défini en dehors
function Enfant() { return <input />; }
function Parent() { return <Enfant />; }
```

### 4.3 Exports et imports

```jsx
// Export par défaut : un seul par fichier ; nom libre à l'import
export default function Carte() {}
import MaCarte from './Carte';

// Exports nommés : plusieurs par fichier ; nom imposé (ou renommé avec `as`)
export function Bouton() {}
export function Lien() {}
import { Bouton, Lien as LienUI } from './UI';
```

> Conseil : les **exports nommés** facilitent la refactorisation, l'autocomplétion et évitent les noms incohérents ; les **exports par défaut** sont requis par certains outils (`React.lazy`, routage par fichiers de frameworks).

#### Fichier « barrel »

```js
// components/index.js
export { default as Carte } from './Carte';
export { default as Bouton } from './Bouton';
```

⚠ Les barrels peuvent nuire au *tree-shaking* et aux temps de build dans de grandes bases de code.

### 4.4 Composer des composants : l'arbre

Les composants s'**imbriquent**. Un composant parent peut en utiliser d'autres :

```jsx
function Profil({ utilisateur }) {
  return (
    <section>
      <Avatar url={utilisateur.avatar} />
      <Nom valeur={utilisateur.nom} />
      <ListeCompetences competences={utilisateur.competences} />
    </section>
  );
}
```

#### Les arbres de React

- **Arbre de rendu** : qui rend qui, à un instant donné (varie selon les conditions).
- **Arbre de dépendances de modules** : qui importe qui (statique), utile pour le *bundle splitting*.

### 4.5 La pureté, en profondeur

Un composant **pur** respecte :

1. **Il ne s'occupe que de ses affaires** : il ne modifie aucun objet ou variable existant avant son appel.
2. **Mêmes entrées, même sortie** : mêmes props/state/context → même JSX.

```jsx
// ❌ Impur : dépend d'une variable externe modifiée à chaque appel
let tasse = 0;
function Tasse() {
  tasse = tasse + 1;
  return <h2>Tasse n° {tasse}</h2>;
}
// <Tasse /><Tasse /> → résultat dépend de l'ordre/nombre d'appels

// ✅ Pur : tout passe par les props
function Tasse({ numero }) {
  return <h2>Tasse n° {numero}</h2>;
}
```

#### Mutation locale : autorisée

On peut créer et modifier des variables **créées pendant le rendu** :

```jsx
function ListeTasses({ nombre }) {
  const tasses = [];                       // créé ici : mutation locale OK
  for (let i = 0; i < nombre; i++) tasses.push(<Tasse key={i} numero={i + 1} />);
  return <>{tasses}</>;
}
```

#### Entrées interdites à la mutation

`props`, `state`, valeurs de `context` : **lecture seule**, même pour les objets imbriqués.

#### Où placer les effets de bord ?

| Besoin | Endroit |
|---|---|
| Réagir à une action utilisateur (clic, saisie) | **Gestionnaire d'événement** |
| Se synchroniser avec un système externe (API, abonnement, DOM non React, timer) | **`useEffect`** |
| Lire/mesurer le DOM avant la peinture | `useLayoutEffect` |
| Mutation locale pendant le rendu | Autorisé (variables créées dans le rendu) |

#### Pourquoi la pureté ?

- Permet le **rendu concurrent** (React peut interrompre/rejouer).
- Permet de **sauter** des rendus (mémoïsation sûre).
- Permet le **rendu serveur** (mêmes résultats).
- Facilite les tests.
- **StrictMode** (chapitre 21) appelle vos composants **deux fois** en développement pour révéler les impuretés.

### 4.6 Identité et état des composants

React identifie un composant par son **type** et sa **position** dans l'arbre.

```jsx
// Même type, même position → l'ÉTAT est conservé entre les rendus
{estPremier ? <Compteur nom="A" /> : <Compteur nom="B" />}
// Passer de A à B ne réinitialise pas le compteur (même type, même position)

// Types différents ou clé différente → l'état est RÉINITIALISÉ
{estPremier ? <Compteur key="a" /> : <Compteur key="b" />}
{estPremier ? <div><Compteur /></div> : <section><Compteur /></section>}
```

#### Cycle de vie conceptuel d'un composant (fonction)

1. **Montage** : première apparition dans l'arbre ; l'état initial est créé, les effets s'exécutent.
2. **Mise à jour** : nouveaux rendus suite à des changements de state/props/context.
3. **Démontage** : disparition de l'arbre ; les fonctions de nettoyage d'effets s'exécutent, l'état est détruit.

### 4.7 Découper une interface en composants (« Penser en React »)

Méthode en 5 étapes recommandée par la documentation :

1. **Découper l'UI en hiérarchie de composants** (principe de **responsabilité unique** ; une boîte de maquette = souvent un composant).
2. **Construire une version statique** : props uniquement, **sans state**.
3. **Identifier la représentation minimale de l'état** (principe **DRY** : ne pas stocker ce qui se déduit).
4. **Déterminer où doit vivre l'état** : le **plus proche ancêtre commun** des composants qui l'utilisent.
5. **Ajouter le flux de données inverse** : fonctions de rappel transmises vers le bas.

Critères pour créer un composant : réutilisation, lisibilité, taille (≈ une page), isolation des responsabilités, besoins de performance (frontière de `memo`).

### 4.8 Typologie des composants

| Type | Description | Remarque |
|---|---|---|
| **Fonction** | Fonction + hooks | Standard actuel |
| **Classe** | `extends React.Component` | Legacy ; indispensable pour les *Error Boundaries* (chapitre 24) |
| **Présentation** | Reçoit des props, affiche | Facile à tester/réutiliser |
| **Conteneur** | Gère données et logique | Largement remplacé par les hooks |
| **Contrôlé / non contrôlé** | Piloté par le parent ou autonome | Chapitre 10 |
| **Layout / Page** | Squelette, route | Chapitre 26 |
| **HOC** | Fonction `(Comp) => Comp` | Chapitre 15 |
| **Serveur** | Rendu uniquement côté serveur | Chapitre 23 |
| **Client** | Interactif, directive `'use client'` | Chapitre 23 |

### 4.9 Exemple fil rouge

```jsx
// TodoItem.jsx
export function TodoItem({ tache, onBasculer, onSupprimer }) {
  return (
    <li className={tache.faite ? 'faite' : ''}>
      <label>
        <input type="checkbox" checked={tache.faite} onChange={() => onBasculer(tache.id)} />
        {tache.titre}
      </label>
      <button onClick={() => onSupprimer(tache.id)} aria-label={`Supprimer ${tache.titre}`}>✕</button>
    </li>
  );
}

// TodoList.jsx
import { TodoItem } from './TodoItem';
export function TodoList({ taches, onBasculer, onSupprimer }) {
  if (taches.length === 0) return <p>Aucune tâche 🎉</p>;
  return (
    <ul>
      {taches.map(t => (
        <TodoItem key={t.id} tache={t} onBasculer={onBasculer} onSupprimer={onSupprimer} />
      ))}
    </ul>
  );
}
```

### 4.10 Quand un composant est-il rendu à nouveau ?

Un composant fonction est **rappelé** (« re-rendu ») dans quatre cas :

1. **Premier rendu** : montage initial de l'arbre ou apparition du composant.
2. **Son propre state change** (`setState`, `dispatch`) : React rappelle **ce composant** et, par défaut, **tous ses descendants**.
3. **Le composant parent se re-rend** : les enfants sont rappelés **même si leurs props n'ont pas changé**. C'est le comportement par défaut ; `memo` (chapitre 16) permet de l'éviter quand les props sont identiques.
4. **Un contexte qu'il lit change** (chapitre 13).

**Idées fausses courantes**

- *« Un composant ne se re-rend que si ses props changent »* : faux. Le re-rendu d'un parent suffit.
- *« Re-rendre, c'est modifier le DOM »* : faux. Le **rendu** (appeler la fonction) est distinct du **commit** (appliquer les différences au DOM) ; un re-rendu qui produit le même JSX ne change rien dans le DOM.
- *« Il faut éviter tous les re-rendus »* : faux. Un rendu **rapide et pur** est bon marché ; n'optimisez qu'après **mesure** (chapitre 16).

Pour comprendre pourquoi un composant s'est rendu, utilisez l'onglet **Profiler** de React DevTools, qui indique la cause (state, props, parent, contexte) pour chaque rendu.

### 4.11 Organiser les fichiers d'un composant

- **Un composant principal par fichier**, nommé comme lui : `BoutonAchat.jsx` exporte `BoutonAchat`. Des petits composants **privés** (non exportés) peuvent cohabiter dans le même fichier s'ils ne servent que là.
- **Extensions** : `.jsx` (ou `.tsx`) pour les fichiers contenant du JSX, `.js` / `.ts` pour la logique pure. Les outils modernes acceptent JSX dans `.js`, mais l'extension explicite aide l'éditeur et les linters.
- **Colocation** : gardez à côté du composant ce qui lui est propre.

```text
BoutonAchat/
├── BoutonAchat.jsx          ← le composant
├── BoutonAchat.module.css   ← ses styles
├── BoutonAchat.test.jsx     ← ses tests
├── useAchat.js              ← son hook spécifique
└── index.js                 ← export public : export { BoutonAchat } from './BoutonAchat';
```

- **Nommage** : composants en **PascalCase** ; hooks en `useXxx` ; fichiers de composants dans la même casse que le composant (convention répandue) ; dossiers en `kebab-case` ou PascalCase, mais **de façon cohérente**.
- **Export nommé** de préférence : il facilite le renommage automatique, la recherche et les imports explicites ; réservez l'export par défaut aux cas où l'outil l'exige (`lazy`, routes de certains frameworks).

### 4.12 Un composant est d'abord du HTML sémantique

Un composant ne doit pas faire oublier le HTML qu'il produit. Avant d'écrire un `<div onClick>`, demandez-vous quel **élément natif** convient.

| Intention | Élément à utiliser | Ce que vous obtenez gratuitement |
| --- | --- | --- |
| Action | `<button type="button">` | Focus au clavier, Entrée et Espace, rôle annoncé |
| Navigation | `<a href>` (ou `<Link>` du routeur) | Ouverture dans un nouvel onglet, clic milieu, URL partageable |
| Liste | `<ul>` / `<ol>` + `<li>` | Nombre d'éléments annoncé |
| Titre | `<h1>`…`<h6>` dans l'ordre | Navigation par titres |
| Région de page | `<header>`, `<nav>`, `<main>`, `<footer>` | Points de repère pour les lecteurs d'écran |
| Champ de saisie | `<input>` + `<label>` | Association, zone de clic élargie |

Un composant générique (`Bouton`, `Carte`) doit **laisser passer** les attributs natifs (`type`, `disabled`, `aria-*`, `className`) via les rest props (chapitre 5) pour ne pas bloquer l'accessibilité.

### 4.13 Outils pour travailler avec les composants

- **React DevTools**, onglet *Components* : arbre des composants, props, state, hooks ; recherche par nom ; sélection d'un élément du DOM pour retrouver son composant.
- **Noms lisibles** : une fonction anonyme (`export default () => …`) apparaît comme `Anonymous` dans les outils. Nommez toujours la fonction du composant.
- **ESLint** : `eslint-plugin-react-hooks` (règles des Hooks), `react/no-unstable-nested-components` (composant défini dans un composant), `react/jsx-key` (clés manquantes).
- **Storybook** : documentation et développement de composants **isolés**, avec leurs états (chargement, erreur, vide).
- **TypeScript** : types des props vérifiés à la compilation (chapitre 31).

### 4.14 Pièges fréquents

- Définir un composant dans un autre composant (perte d'état, performances).
- Muter les props ou une variable globale pendant le rendu.
- Composants géants « fourre-tout » (> 300 lignes, plusieurs responsabilités).
- Noms en minuscule.
- Mélanger logique métier, appels API et affichage dans un même composant sans extraire de hook.

### Synthèse du chapitre 4

Composant = **fonction pure** `props → JSX`, nom en **PascalCase**, défini au **niveau module** ; L'**identité** (type + position + clé) détermine la préservation de l'état ; Effets de bord : **événements** ou **`useEffect`**, jamais dans le corps du rendu ; « Penser en React » : hiérarchie → version statique → état minimal → emplacement de l'état → flux inverse.

---

## 5. Props

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : définir les props et comprendre leur nature (lecture seule, instantané) ; maîtriser toutes les formes de transmission : valeurs, fonctions, JSX, `children`, `ref`, spread ; éviter le prop drilling et l'anti-pattern « copier une prop dans le state » ; savoir valider et typer les props.

### 5.1 Définition

Les **props** (abréviation de *properties*) sont les **paramètres d'un composant** : un **objet unique** passé comme premier argument de la fonction. Elles permettent à un **parent de configurer un enfant**.

```jsx
function Avatar({ personne, taille }) {   // destructuration du paramètre `props`
  return <img src={personne.url} alt={personne.nom} width={taille} height={taille} />;
}

<Avatar personne={{ nom: 'Ada', url: '/ada.jpg' }} taille={80} />
```

Équivalent sans destructuration :

```jsx
function Avatar(props) {
  return <img src={props.personne.url} width={props.taille} />;
}
```

> Les props sont l'**unique canal** par lequel les données descendent explicitement dans l'arbre (hors Context). Ce sont les « arguments » de votre fonction de rendu.

### 5.2 Passer des props

#### Selon le type de valeur

```jsx
<Composant
  texte="chaîne littérale"          // chaîne : guillemets
  nombre={42}                       // tout le reste : accolades
  actif={true}
  actif                             // raccourci pour actif={true}
  tableau={[1, 2, 3]}
  objet={{ a: 1 }}                  // double accolades : objet littéral
  fonction={() => alert('salut')}
  element={<Icone />}               // JSX comme prop
  composant={Icone}                 // le composant lui-même (pas d'appel)
/>
```

#### Props de fonction (callbacks) : remonter l'information

Un enfant **ne modifie pas** l'état du parent ; il **notifie** le parent via une fonction reçue en prop.

```jsx
function Bouton({ onClick, children }) {
  return <button onClick={onClick}>{children}</button>;
}

function Parent() {
  const [n, setN] = useState(0);
  return <Bouton onClick={() => setN(n + 1)}>Cliqué {n} fois</Bouton>;
}
```

**Convention de nommage** :
- côté **prop** : `onXxx` (`onSelect`, `onChange`, `onSubmit`) ;
- côté **gestionnaire** défini dans le composant : `handleXxx` (`handleSelect`).

#### Passer des props avec le spread

```jsx
function Profil(props) {
  return <Avatar {...props} />;      // transmet tout
}
```

⚠ À utiliser avec modération : cela masque ce que le composant utilise réellement et peut propager des props inutiles.

#### Rest props : séparer « mes » props des props transmises

```jsx
function Bouton({ variante = 'primaire', className = '', ...reste }) {
  return <button className={`btn btn--${variante} ${className}`} {...reste} />;
}
<Bouton variante="danger" onClick={fn} disabled aria-label="Supprimer" />
```

### 5.3 Valeurs par défaut

```jsx
// ✅ Paramètre par défaut JavaScript (standard)
function Bouton({ taille = 'moyenne', type = 'button' }) {}
```

- Le défaut s'applique **uniquement** quand la prop vaut **`undefined`** (absente ou `undefined` explicite) — **pas** pour `null`, `0`, `''`, `false`.
- `Composant.defaultProps` est **supprimé pour les composants fonctions en React 19** ; utilisez les paramètres par défaut.

### 5.4 La prop spéciale `children`

Le contenu placé **entre les balises** devient la prop `children`.

```jsx
function Carte({ titre, children }) {
  return (
    <section className="carte">
      <h2>{titre}</h2>
      <div className="carte__corps">{children}</div>
    </section>
  );
}

<Carte titre="Bienvenue">
  <p>Un paragraphe.</p>
  <Bouton>OK</Bouton>
</Carte>
```

- `children` peut être : texte, élément, tableau, fonction (render prop), `undefined`.
- C'est le fondement de la **composition** (chapitre 15) : le parent « ne sait pas » ce que contiendra l'enfant.
- **Plusieurs « emplacements »** (*slots*) : utilisez des props nommées contenant du JSX.

```jsx
<Layout entete={<Navbar />} barreLaterale={<Menu />} pied={<Footer />}>
  <Contenu />
</Layout>
```

### 5.5 Les props sont en lecture seule

```jsx
function Mauvais(props) {
  props.titre = 'modifié';   // ❌ mutation interdite (l'objet est figé en développement)
}
```

Un composant **ne modifie jamais** ses props (ni les objets/tableaux imbriqués). S'il a besoin d'une valeur différente :
- il **dérive** une nouvelle valeur localement (calcul pendant le rendu) ;
- ou il demande au **parent**, via un callback, de changer ce qui est passé ;
- ou il possède son **propre state** (initialisé à partir d'une prop, voir 5.8).

#### Les props changent dans le temps

Un composant peut recevoir **différentes props à chaque rendu**. Chaque rendu voit **ses** props comme un **instantané**. Si un parent passe de nouvelles props, React rappelle le composant avec elles ; l'ancien objet n'est pas modifié.

### 5.6 `ref` comme prop (React 19)

```jsx
// React 19 : `ref` est une prop ordinaire pour les composants fonctions
function Champ({ ref, ...props }) {
  return <input ref={ref} {...props} />;
}

// Avant React 19
const Champ = forwardRef((props, ref) => <input ref={ref} {...props} />);
```

`forwardRef` reste fonctionnel mais sera déprécié. `key` n'est, lui, **jamais** transmis comme prop.

### 5.7 Le prop drilling

**Prop drilling** : transmettre une donnée à travers de nombreux **niveaux intermédiaires** qui ne l'utilisent pas, juste pour atteindre un descendant profond.

```jsx
<App utilisateur={u}>
  <Layout utilisateur={u}>
    <Sidebar utilisateur={u}>
      <Avatar utilisateur={u} />   {/* seul consommateur réel */}
```

#### Solutions, par ordre de préférence

1. **Extraire des composants et passer du JSX en `children`** (inversion) : souvent suffisant et sous-estimé.

```jsx
// Au lieu de passer `utilisateur` à Layout puis Sidebar :
<Layout>
  <Sidebar>
    <Avatar utilisateur={utilisateur} />   {/* le JSX est créé là où la donnée existe */}
  </Sidebar>
</Layout>
```

2. **Context** pour les données « globales » (thème, langue, utilisateur courant) — chapitre 13.
3. **Bibliothèque d'état** (Zustand, Redux, Jotai) pour un état partagé complexe — chapitre 27.
4. **Composition par slots** (props contenant du JSX).

> Le drilling sur 2-3 niveaux est normal et **explicite** (traçabilité). Ne recourez à Context que lorsque cela devient réellement lourd.

### 5.8 Props et state : différences et relations

| | **Props** | **State** |
|---|---|---|
| Propriétaire | Le **parent** | Le **composant lui-même** |
| Modifiable par le composant ? | ❌ Non | ✅ Oui (via le setter) |
| Déclenche un rendu | Quand le parent re-rend avec d'autres valeurs | Quand on appelle le setter |
| Analogie | Arguments d'une fonction | Variables locales **persistantes** |

#### Anti-pattern : copier une prop dans le state

```jsx
// ❌ Le state est initialisé UNE fois ; il ignorera les changements ultérieurs de la prop
function Message({ messageInitial }) {
  const [message, setMessage] = useState(messageInitial);
}
```

Corrections selon l'intention :

- **Vraiment une valeur initiale** (puis le composant en est maître) → renommer en `initialXxx` / `defaultXxx` pour l'expliciter.
- **Valeur dérivée** → calculer pendant le rendu, sans state.
- **Réinitialiser le state quand la prop change** → utiliser une **`key`** :

```jsx
<Formulaire key={utilisateur.id} utilisateur={utilisateur} />
```

### 5.9 Validation et typage

#### TypeScript (recommandé)

```tsx
type BoutonProps = {
  variante?: 'primaire' | 'secondaire';
  onClick: () => void;
  children: React.ReactNode;
};
function Bouton({ variante = 'primaire', onClick, children }: BoutonProps) {}
```

#### `PropTypes` (JavaScript)

Le package `prop-types` reste utilisable, mais **React 19 n'exécute plus la vérification des `propTypes`** (la propriété est ignorée). Pour du JavaScript pur, utilisez JSDoc + TypeScript en mode `checkJs`, ou une validation à l'exécution (**Zod**) aux frontières du système (API, formulaires).

### 5.10 Bonnes pratiques de conception d'API de composant

- Garder une **API petite** : peu de props, noms explicites.
- Préférer des **props sémantiques** (`variante="danger"`) aux props de style (`couleur="red"`).
- Éviter l'**explosion de props booléennes** (`primaire`, `secondaire`, `danger`…) → un enum `variante`.
- Préférer **`children` / slots** à des props de configuration de contenu (`texteBouton`, `iconeGauche`…).
- Transmettre `...rest` à l'élément racine pour permettre `className`, `aria-*`, `data-*`.
- Ne **pas** passer des objets/fonctions inline si l'enfant est mémoïsé (nouvelle référence à chaque rendu → `memo` inefficace, chapitre 16).
- Nommer les callbacks `onXxx`, les booléens `estXxx` / `aXxx` / adjectifs (`disabled`, `actif`).

### 5.11 Pièges fréquents

- Muter une prop.
- `useState(prop)` en attendant la synchronisation automatique.
- Oublier que `0`, `''`, `null` ne déclenchent **pas** la valeur par défaut.
- Passer `onClick={fn(arg)}` (appel immédiat) au lieu de `onClick={() => fn(arg)}`.
- Écrire `<Comp prop="{variable}" />` (chaîne littérale `"{variable}"` !) au lieu de `prop={variable}`.
- S'attendre à ce que `key` soit disponible dans `props.key`.

### Synthèse du chapitre 5

Props = **arguments** d'un composant, **immuables** du point de vue de l'enfant ; Les données descendent (props), les événements remontent (callbacks) ; `children` + slots = base de la composition ; N'initialisez pas du state avec une prop en espérant la synchronisation ; dérivez ou utilisez `key` ; Typage avec TypeScript ; `propTypes` est ignoré en React 19.

---

## 6. State

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : comprendre pourquoi les variables locales ne suffisent pas et ce qu'apporte le state ; maîtriser le fonctionnement interne : snapshot, file d'attente de mises à jour, batching ; mettre à jour objets et tableaux **sans mutation** ; structurer correctement l'état et savoir où le faire vivre.

### 6.1 Pourquoi le state ?

Un composant a souvent besoin de **se souvenir** d'informations (saisie, compteur, onglet actif). Les variables locales ne conviennent pas :

```jsx
function Galerie() {
  let index = 0;                               // ❌
  function suivant() { index = index + 1; }    // 1. la variable change mais…
  return <button onClick={suivant}>{index}</button>;
  // 1. Les variables locales sont RÉINITIALISÉES à chaque rendu (la fonction est ré-appelée)
  // 2. Modifier une variable locale NE DÉCLENCHE PAS de nouveau rendu
}
```

Le **state** (`useState`) apporte deux choses :
1. **Persistance** : la valeur est **conservée par React** entre les rendus.
2. **Déclenchement** : appeler le **setter** **planifie un nouveau rendu**.

### 6.2 `useState` : syntaxe

```jsx
import { useState } from 'react';

const [valeur, setValeur] = useState(valeurInitiale);
```

- Retourne un **tableau de deux éléments** (destructuré) : la valeur courante et la **fonction de mise à jour**.
- La valeur initiale n'est utilisée **qu'au premier rendu** ; ensuite elle est **ignorée**.
- Les noms sont libres, convention : `[xxx, setXxx]`.
- Un composant peut avoir **plusieurs** appels à `useState`. React les associe **par ordre d'appel** (d'où la règle « pas de hooks conditionnels », chapitre 11).

```jsx
function Galerie() {
  const [index, setIndex] = useState(0);
  const [afficherDetails, setAfficherDetails] = useState(false);
  const oeuvre = oeuvres[index];

  return (
    <>
      <button onClick={() => setIndex((i) => (i + 1) % oeuvres.length)}>Suivant</button>
      <h2>{oeuvre.titre}</h2>
      <button onClick={() => setAfficherDetails(!afficherDetails)}>
        {afficherDetails ? 'Masquer' : 'Afficher'} les détails
      </button>
      {afficherDetails && <p>{oeuvre.description}</p>}
    </>
  );
}
```

#### Ce qui se passe quand on appelle le setter

1. React **enregistre** la nouvelle valeur dans une **file d'attente**.
2. React **planifie** un nouveau rendu du composant.
3. Au rendu suivant, `useState` **retourne la nouvelle valeur**.
4. React compare le JSX obtenu à l'ancien et **met à jour le DOM** si nécessaire.

#### Sortie anticipée (« bail out »)

Si la nouvelle valeur est identique à l'actuelle selon **`Object.is`**, React **ne re-rend pas** (ou re-rend le composant une fois sans toucher aux enfants).

### 6.3 Le state est un instantané (snapshot)

Dans un rendu, la valeur du state est **fixée**. Les gestionnaires d'événements « capturent » les valeurs de **leur** rendu (closures).

```jsx
function Compteur() {
  const [n, setN] = useState(0);
  return (
    <button onClick={() => {
      setN(n + 1);   // planifie 1
      setN(n + 1);   // planifie 1 (n vaut toujours 0 dans ce snapshot)
      setN(n + 1);   // planifie 1
      // Résultat après le clic : n = 1 (et non 3)
    }}>+3 ?</button>
  );
}
```

```jsx
<button onClick={() => {
  setN(n + 5);
  setTimeout(() => alert(n), 3000);   // affiche 0 : la valeur du rendu où le clic a eu lieu
}} />
```

### 6.4 Mises à jour fonctionnelles (« updater functions »)

Pour calculer le nouvel état **à partir de l'état précédent**, passez une **fonction** :

```jsx
setN(n => n + 1);
setN(n => n + 1);
setN(n => n + 1);   // résultat : +3
```

React place ces fonctions dans la **file d'attente** et les applique **en séquence** au rendu suivant, chacune recevant le résultat de la précédente.

#### Règles de la file d'attente

Pour `setN(5); setN(n => n + 1); setN(42);` à partir de `n = 0` :

| Action | `n` résultant |
|---|---|
| `setN(5)` | 5 |
| `setN(n => n + 1)` | 6 |
| `setN(42)` | 42 |

Les fonctions « updater » doivent être **pures** (StrictMode les exécute deux fois en dev) et **ne pas déclencher d'effets**.

#### Convention

On nomme souvent l'argument par la première lettre : `setPanier(p => ...)`, ou `précédent`/`prev`.

#### Quand utiliser quelle forme ?

| Situation | Forme |
|---|---|
| Nouvelle valeur indépendante de l'ancienne | `setX(valeur)` |
| Nouvelle valeur calculée depuis l'ancienne (compteur, ajout dans une liste) | `setX(prev => …)` |
| Plusieurs mises à jour successives dans le même événement | Forme fonctionnelle |
| Dans un `setTimeout` / intervalle / promesse | Forme fonctionnelle (évite les valeurs obsolètes) |

### 6.5 Le batching (regroupement automatique)

React **regroupe** plusieurs mises à jour d'état dans **un seul rendu** (pour les performances et la cohérence).

```jsx
function handleClick() {
  setNom('Alice');
  setAge(30);
  setConnecte(true);
  // → un SEUL re-rendu après la fin du gestionnaire
}
```

- **React 17** : batching seulement dans les gestionnaires d'événements React.
- **React 18+** : **batching automatique partout** (timeouts, promesses, événements natifs, `fetch().then`).
- Chaque événement est traité **séparément** : deux clics = deux rendus, jamais fusionnés.
- Pour forcer un rendu synchrone (cas rarissime, ex. mesurer le DOM juste après) : `flushSync` de `react-dom`.

```jsx
import { flushSync } from 'react-dom';
flushSync(() => setN(1));   // rendu immédiat ; usage exceptionnel
```

### 6.6 Mettre à jour des objets

#### Règle : traiter le state comme **immuable** (lecture seule)

Un objet dans le state **ne doit jamais être muté** : on crée une **copie** avec les changements.

```jsx
const [position, setPosition] = useState({ x: 0, y: 0 });

position.x = 5;                              // ❌ mutation : pas de rendu, bugs
setPosition({ x: 5, y: position.y });        // ✅ nouvel objet
setPosition({ ...position, x: 5 });          // ✅ avec spread (copie superficielle)
```

> **Mutation vs. variable locale** : muter un objet **que l'on vient de créer** pendant le rendu est correct ; muter un objet **du state** ne l'est pas.

#### Objets imbriqués

La copie par spread est **superficielle** (*shallow*). Il faut copier **chaque niveau** modifié :

```jsx
setPersonne({
  ...personne,
  adresse: { ...personne.adresse, ville: 'Lyon' },
});
```

#### Propriétés calculées (clés dynamiques)

```jsx
function handleChange(e) {
  setPersonne({ ...personne, [e.target.name]: e.target.value });
}
```

#### Immer (mises à jour « mutantes » sans mutation)

```jsx
import { useImmer } from 'use-immer';

const [personne, mettreAJour] = useImmer({ adresse: { ville: 'Paris' } });
mettreAJour(brouillon => { brouillon.adresse.ville = 'Lyon'; });   // le brouillon est un proxy
```

Immer produit un nouvel objet immuable derrière la scène. Utile pour des structures très imbriquées.

#### Pourquoi ne pas muter ?

1. **Détection du changement** : React compare les références ; une mutation conserve la même référence.
2. **Optimisations** (`memo`, `useMemo`, dépendances d'effets) reposent sur cette comparaison.
3. **Fonctionnalités** : rendu concurrent, annulation, historique d'états (undo/redo), débogage.
4. **Prévisibilité** : les snapshots passés ne sont pas altérés.

### 6.7 Mettre à jour des tableaux

Les méthodes qui **mutent** (`push`, `pop`, `shift`, `unshift`, `splice`, `sort`, `reverse`, affectation par index) sont **interdites** sur le state. Utilisez des méthodes **non mutantes** ou **copiez d'abord**.

| Opération | ❌ À éviter (mute) | ✅ À préférer (nouveau tableau) |
|---|---|---|
| Ajouter | `push`, `unshift` | `[...liste, x]`, `[x, ...liste]` |
| Supprimer | `pop`, `shift`, `splice` | `filter(el => el.id !== id)`, `slice` |
| Remplacer | `liste[i] = x` | `map((el, idx) => idx === i ? x : el)` |
| Trier / inverser | `sort`, `reverse` | `[...liste].sort(…)`, `toSorted()`, `toReversed()` |
| Insérer à une position | `splice` | `[...liste.slice(0, i), x, ...liste.slice(i)]` |
| Remplacer un élément (ES2023) | | `liste.with(i, x)` |
| Retirer à l'index (ES2023) | | `liste.toSpliced(i, 1)` |

```jsx
// Ajouter
setTaches(prev => [...prev, { id: crypto.randomUUID(), titre, faite: false }]);

// Supprimer
setTaches(prev => prev.filter(t => t.id !== id));

// Modifier un champ d'un élément
setTaches(prev => prev.map(t => (t.id === id ? { ...t, faite: !t.faite } : t)));

// Trier (copie !)
const triees = [...taches].sort((a, b) => a.titre.localeCompare(b.titre));
```

#### Tableaux d'objets : le piège de la copie superficielle

```jsx
const copie = [...taches];
copie[0].faite = true;   // ❌ MUTE l'objet partagé avec le state d'origine !
```

Les éléments restent **les mêmes objets** ; modifiez-les en créant un nouvel objet (`{...t, faite: true}`).

### 6.8 Structurer l'état : 5 principes

1. **Regrouper les états liés** : si deux variables changent toujours ensemble, fusionnez-les en un objet (ou utilisez `useReducer`).
2. **Éviter les contradictions** : `estEnvoi` + `estEnvoye` peuvent être simultanément `true` ; préférez `statut: 'saisie' | 'envoi' | 'envoye'`.
3. **Éviter les redondances** : ne stockez pas ce qui se calcule. Exemple : `prenom` + `nom` → calculez `nomComplet` pendant le rendu.
4. **Éviter les doublons** : ne dupliquez pas le même objet à deux endroits (ex. `elementSelectionne` en objet) ; stockez un **ID** (`idSelectionne`) et retrouvez l'objet.
5. **Éviter les structures profondément imbriquées** : **normalisez** (par ID) ou aplatissez.

```jsx
// ❌ Redondant
const [prenom, setPrenom] = useState('');
const [nom, setNom] = useState('');
const [nomComplet, setNomComplet] = useState('');   // à synchroniser à la main !

// ✅ Dérivé pendant le rendu
const nomComplet = `${prenom} ${nom}`;
```

```jsx
// ❌ Copie de l'objet : devient obsolète quand la liste change
const [selection, setSelection] = useState(articles[0]);
// ✅ Identifiant
const [selectionId, setSelectionId] = useState(articles[0].id);
const selection = articles.find(a => a.id === selectionId);
```

### 6.9 Remonter l'état (« lifting state up »)

Quand **deux composants** doivent refléter les mêmes données, **déplacez l'état dans leur plus proche ancêtre commun** et passez-le en props (+ callbacks).

```jsx
function Accordeon() {
  const [actifIndex, setActifIndex] = useState(0);     // état dans le parent
  return (
    <>
      <Panneau titre="À propos" estActif={actifIndex === 0} onAfficher={() => setActifIndex(0)}>…</Panneau>
      <Panneau titre="Étymologie" estActif={actifIndex === 1} onAfficher={() => setActifIndex(1)}>…</Panneau>
    </>
  );
}
```

#### Composant contrôlé vs non contrôlé

- **Contrôlé** : l'information importante est portée par les **props** (le parent décide).
- **Non contrôlé** : l'information est dans le **state local**.
Un bon composant réutilisable supporte souvent les deux (ex. `value`/`onChange` **ou** `defaultValue`).

#### « Source unique de vérité »

Chaque donnée doit avoir **un seul propriétaire**. Les autres composants la reçoivent en props.

### 6.10 Préserver et réinitialiser l'état

#### L'état est lié à la position dans l'arbre

L'état n'est pas stocké **dans** le composant mais **par React**, associé à la **position** du composant dans l'arbre de rendu.

```jsx
// Même composant, même position → état conservé même si la prop change
{estJoueurA ? <Compteur personne="Alice" /> : <Compteur personne="Bob" />}
```

#### Réinitialiser

Deux méthodes :
1. **Rendre à des positions différentes** (éléments distincts dans le JSX).
2. **Donner une `key` différente** : changer la `key` **détruit et recrée** le composant.

```jsx
<Compteur key={personne} personne={personne} />
```

#### Les composants imbriqués dans un composant perdent leur état à chaque rendu (rappel chapitre 4).

#### Conserver l'état d'un composant « masqué »

- Le rendre toujours, mais le masquer par **CSS** (`display: none`) ;
- ou **remonter** l'état dans le parent ;
- ou utiliser un stockage (localStorage via hook personnalisé) ;
- ou **`<Activity mode="hidden">`** (React 19.2) : cache le sous-arbre en **préservant son état** et en suspendant ses effets (chapitre 22).

### 6.11 Cas particuliers

#### Stocker une fonction dans le state

```jsx
const [rappel, setRappel] = useState(() => maFonction);   // ✅ fonction de init qui retourne la fonction
setRappel(() => autreFonction);                             // ✅ updater qui retourne la fonction
setRappel(autreFonction);                                   // ❌ React l'appelle comme un updater !
```

#### Initialisation « paresseuse »

```jsx
const [donnees, setDonnees] = useState(creerGrandeListe());     // ❌ appelée à CHAQUE rendu (résultat ignoré après le 1er)
const [donnees, setDonnees] = useState(() => creerGrandeListe()); // ✅ appelée une seule fois
```

#### Ajuster l'état en réaction à une prop (pendant le rendu)

Cas rare (ex. réinitialiser une sélection quand la liste change). Mieux vaut **`key`** ou un **calcul dérivé**. À défaut, on peut appeler un `setState` **pendant le rendu** du **même composant** avec une condition de garde ; React relance immédiatement le rendu sans afficher le résultat intermédiaire :

```jsx
const [precedente, setPrecedente] = useState(articles);
if (articles !== precedente) {
  setPrecedente(articles);
  setSelection(null);
}
```

#### État d'un composant non monté

Appeler un setter après le démontage n'a aucun effet (l'ancien avertissement a été supprimé).

#### Autres outils d'état

- **`useReducer`** : logique de transition centralisée (chapitre 11).
- **`useRef`** : valeur mutable qui **ne déclenche pas** de rendu.
- **Context** : état partagé dans un sous-arbre (chapitre 13).
- **Stores externes** : Zustand, Redux, Jotai (chapitre 27).

### 6.12 Pièges fréquents

- **Muter** le state (objet/tableau) → pas de rendu ou rendu incohérent.
- Lire la valeur juste après le setter en pensant qu'elle a changé.
- `setN(n + 1)` répété (au lieu de `setN(n => n + 1)`).
- **Dupliquer** ou **dériver** de l'état via un second `useState` + `useEffect` (cascades de rendus).
- Utiliser un `index` comme identifiant pour des éléments qui peuvent changer d'ordre.
- Oublier que `sort()` / `reverse()` **mutent**.
- Copie superficielle d'objets imbriqués.
- Utiliser `useState(valeurCouteuse())` sans fonction d'initialisation.

### Synthèse du chapitre 6

**State = mémoire** d'un composant ; le setter **planifie** un rendu ; Le state est un **instantané** ; le setter ne le modifie pas dans le rendu courant ; **Forme fonctionnelle** quand le nouvel état dépend de l'ancien ; **Immuabilité** : copiez, ne mutez pas ; État **minimal**, sans redondance ; on stocke un **ID** plutôt qu'un objet dupliqué ; **Remontez l'état** dans l'ancêtre commun ; **`key`** pour réinitialiser.

---

## 7. Gestion des événements

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : attacher et écrire correctement des gestionnaires d'événements ; comprendre `SyntheticEvent`, la propagation (bubbling / capture) et la délégation ; connaître les familles d'événements et leurs spécificités React ; distinguer gestionnaires d'événements et effets.

### 7.1 Principe

Un **gestionnaire d'événement** (*event handler*) est une **fonction** que React appelle en réponse à une interaction (clic, saisie, soumission…). On le passe via une prop en **camelCase** sur un élément **natif** (`onClick`, `onChange`…).

```jsx
function Bouton() {
  function handleClick() {
    alert('Cliqué !');
  }
  return <button onClick={handleClick}>Cliquer</button>;
}
```

#### Trois façons de définir un gestionnaire

```jsx
// 1. Fonction nommée définie dans le composant (conseillée si >1 ligne)
<button onClick={handleClick} />

// 2. Fonction fléchée inline (pratique pour passer un argument)
<button onClick={() => supprimer(id)} />

// 3. Fonction définie ailleurs (module) ou reçue en prop
<button onClick={props.onClick} />
```

#### Passer, ne pas appeler

```jsx
<button onClick={handleClick} />       // ✅ passe la fonction
<button onClick={handleClick()} />     // ❌ l'APPELLE pendant le rendu (et passe son résultat)
<button onClick={() => handleClick()} />// ✅ fonction fléchée qui appelle au clic
```

#### Les composants personnalisés n'ont pas d'événements « magiques »

`<MonBouton onClick={…} />` ne fait que **passer une prop** nommée `onClick`. C'est au composant `MonBouton` de la brancher sur un élément natif :

```jsx
function MonBouton({ onClick, children }) {
  return <button onClick={onClick}>{children}</button>;
}
```

Pour vos propres événements, nommez les props `onXxx` (`onSelect`, `onDelete`) et appelez-les avec les **données utiles** :

```jsx
function Recherche({ onRecherche }) {
  return <input onChange={(e) => onRecherche(e.target.value)} />;
}
```

### 7.2 L'objet événement : `SyntheticEvent`

React fournit à chaque gestionnaire un **objet événement synthétique** (*SyntheticEvent*) : un **wrapper cross-navigateur** autour de l'événement natif, avec la même interface que les événements DOM standard.

| Propriété / méthode | Description |
|---|---|
| `e.target` | Élément **à l'origine** de l'événement (le plus profond) |
| `e.currentTarget` | Élément **sur lequel le gestionnaire est attaché** |
| `e.type` | Nom de l'événement (`'click'`) |
| `e.nativeEvent` | Événement DOM natif sous-jacent |
| `e.preventDefault()` | Empêche le comportement par défaut du navigateur |
| `e.stopPropagation()` | Arrête la propagation |
| `e.isDefaultPrevented()` / `e.isPropagationStopped()` | État des deux actions précédentes |
| `e.timeStamp` | Horodatage |
| `e.bubbles`, `e.cancelable`, `e.defaultPrevented` | Informations de propagation |

> Depuis **React 17**, l'ancien mécanisme de « pooling » d'événements a été supprimé : on peut lire `e` dans du code asynchrone sans `e.persist()`.

#### Propriétés selon la famille

- **Souris** : `clientX/Y`, `pageX/Y`, `screenX/Y`, `button`, `buttons`, `ctrlKey`, `shiftKey`, `altKey`, `metaKey`.
- **Clavier** : `key` (valeur lisible : `'Enter'`, `'Escape'`, `'a'`), `code` (touche physique : `'KeyA'`), `repeat`, modificateurs.
- **Saisie** : `e.target.value`, `e.target.checked`, `e.target.files`, `e.target.name`, `e.target.type`.
- **Focus** : `relatedTarget`.
- **Pointeur** : `pointerId`, `pointerType`, `pressure`.

### 7.3 Catalogue des événements courants

| Famille | Événements |
|---|---|
| **Souris** | `onClick`, `onDoubleClick`, `onContextMenu`, `onMouseDown`, `onMouseUp`, `onMouseEnter`, `onMouseLeave`, `onMouseMove`, `onMouseOver`, `onMouseOut` |
| **Pointeur** (unifie souris/tactile/stylet) | `onPointerDown`, `onPointerUp`, `onPointerMove`, `onPointerEnter`, `onPointerLeave`, `onPointerCancel`, `onGotPointerCapture` |
| **Tactile** | `onTouchStart`, `onTouchMove`, `onTouchEnd`, `onTouchCancel` |
| **Clavier** | `onKeyDown`, `onKeyUp` (`onKeyPress` est déprécié) |
| **Focus** | `onFocus`, `onBlur` (propagent en React, contrairement au DOM natif) |
| **Formulaire** | `onChange`, `onInput`, `onSubmit`, `onReset`, `onInvalid`, `onSelect` |
| **Presse-papier** | `onCopy`, `onCut`, `onPaste` |
| **Glisser-déposer** | `onDrag`, `onDragStart`, `onDragEnd`, `onDragEnter`, `onDragOver`, `onDragLeave`, `onDrop` |
| **Défilement / molette** | `onScroll`, `onWheel` |
| **Média** | `onPlay`, `onPause`, `onEnded`, `onTimeUpdate`, `onLoadedData`, `onVolumeChange`… |
| **Images / ressources** | `onLoad`, `onError` |
| **Animation / transition CSS** | `onAnimationStart`, `onAnimationEnd`, `onAnimationIteration`, `onTransitionEnd` |
| **Composition (IME)** | `onCompositionStart`, `onCompositionUpdate`, `onCompositionEnd` |
| **Dialogue / détails** | `onToggle`, `onClose`, `onCancel` |

#### Particularités de React

- **`onChange` sur `<input>` / `<textarea>`** : se déclenche à **chaque modification** (comportement de l'événement DOM `input`), pas seulement au blur comme l'événement `change` natif.
- **`onFocus` / `onBlur`** utilisent `focusin` / `focusout` : ils **se propagent**, ce qui facilite la détection de focus dans un conteneur.
- **`onScroll`** ne se propage **pas** (depuis React 17).
- **`onMouseEnter` / `onMouseLeave`** ne se propagent pas ; **`onMouseOver` / `onMouseOut`** si.
- Certains événements « bloquants » (`touchstart`, `wheel`) sont enregistrés comme **passifs** : `preventDefault()` y est **sans effet** ; pour cela, utilisez `addEventListener` avec `{ passive: false }` dans un effet.

### 7.4 Propagation des événements

#### Bubbling (remontée)

Par défaut, un événement **remonte** de l'élément ciblé vers ses **ancêtres** : tous les gestionnaires du même type rencontrés sont appelés (hors `onScroll`).

```jsx
<div onClick={() => alert('div')}>
  <button onClick={() => alert('bouton')}>Clic</button>
</div>
// Clic sur le bouton : alerte "bouton", PUIS "div"
```

#### Arrêter la propagation

```jsx
function Bouton({ onClick, children }) {
  return (
    <button onClick={(e) => {
      e.stopPropagation();     // les ancêtres ne seront pas notifiés
      onClick();
    }}>{children}</button>
  );
}
```

> Préférez, quand c'est possible, une **conception** qui évite `stopPropagation` (qui casse d'autres écouteurs, comme les analytics). Si un parent doit réagir à tous les clics, laissez-les remonter.

#### Capture (descente)

Ajoutez le suffixe **`Capture`** pour intercepter **avant** que l'événement n'atteigne la cible :

```jsx
<div onClickCapture={() => console.log('1. capture (descente)')}>
  <button onClick={() => console.log('2. cible/bubbling')}>OK</button>
</div>
```

Ordre : capture (racine → cible), puis bubbling (cible → racine).

#### Délégation d'événements

React n'attache pas un écouteur DOM par élément : il attache **quelques écouteurs sur le conteneur racine** (celui passé à `createRoot`) et **dispatche** lui-même. Cela réduit la mémoire et simplifie la gestion des éléments dynamiques. (Avant React 17, c'était sur `document`.) Conséquence : un `addEventListener` natif sur `document` s'exécute **après** les gestionnaires React, et `e.stopPropagation()` natif n'arrête pas les gestionnaires React situés plus haut dans la même racine, d'où la prudence lors de mélanges.

#### Comportement par défaut

```jsx
function Formulaire() {
  function handleSubmit(e) {
    e.preventDefault();            // évite le rechargement de page
    /* traitement */
  }
  return <form onSubmit={handleSubmit}>…</form>;
}

<a href="/x" onClick={(e) => { e.preventDefault(); naviguer('/x'); }}>Lien</a>
```

> `preventDefault` ≠ `stopPropagation` : l'un arrête l'**action du navigateur**, l'autre arrête la **remontée**. Ils sont indépendants.

### 7.5 Gestionnaires d'événements et effets de bord

Contrairement au **rendu**, un gestionnaire **n'a pas besoin d'être pur** : c'est **l'endroit naturel** pour les effets de bord déclenchés par l'utilisateur (changer le state, envoyer une requête, naviguer, écrire dans `localStorage`, appeler `focus()`).

```jsx
function handleEnvoyer() {
  setEnvoi(true);
  await api.envoyer(donnees);   // effet de bord
  navigate('/merci');
}
```

> Règle : si le code doit s'exécuter **parce que l'utilisateur a fait quelque chose**, il va dans un **gestionnaire**. S'il doit s'exécuter **parce que le composant est affiché / une valeur a changé**, c'est un **effet** (chapitre 11).

### 7.6 Gestionnaires et state : snapshots et closures

Un gestionnaire voit les **valeurs du rendu où il a été créé** :

```jsx
function Message() {
  const [texte, setTexte] = useState('');
  function envoyer() {
    setTimeout(() => alert(`Envoyé : ${texte}`), 3000);
    // `texte` = valeur au moment du clic, même si l'utilisateur continue à taper
  }
}
```

Pour toujours lire la **dernière** valeur, utilisez une **ref** ou `useEffectEvent` (chapitre 11).

### 7.7 Événements dans les listes : transmettre des arguments

```jsx
{taches.map(t => (
  <li key={t.id}>
    {t.titre}
    <button onClick={() => supprimer(t.id)}>✕</button>      {/* closure : t.id capturé */}
  </li>
))}
```

Alternative avec attributs `data-*` et un seul gestionnaire (**délégation manuelle**) :

```jsx
<ul onClick={(e) => {
  const id = e.target.closest('[data-id]')?.dataset.id;
  if (id) supprimer(id);
}}>
  {taches.map(t => <li key={t.id} data-id={t.id}>{t.titre}</li>)}
</ul>
```

### 7.8 Clavier et accessibilité

```jsx
function Champ({ onValider, onAnnuler }) {
  return (
    <input
      onKeyDown={(e) => {
        if (e.key === 'Enter') onValider(e.currentTarget.value);
        if (e.key === 'Escape') onAnnuler();
      }}
    />
  );
}
```

- Utilisez `e.key` (valeur sémantique) plutôt que `keyCode` (déprécié).
- Pendant une saisie avec **IME** (japonais, chinois…), vérifiez `e.nativeEvent.isComposing` avant de traiter `Enter`.
- **Éléments interactifs** : utilisez de vrais `<button>` / `<a>` plutôt que `<div onClick>`. Si c'est inévitable, ajoutez `role="button"`, `tabIndex={0}` et la gestion de `Enter`/`Space`.

### 7.9 Écouteurs natifs dans des effets

Pour `window`, `document`, `ResizeObserver`, ou des événements non gérés par React (ex. `resize`, `beforeunload`, écouteur non passif) :

```jsx
useEffect(() => {
  function onResize() { setLargeur(window.innerWidth); }
  window.addEventListener('resize', onResize);
  return () => window.removeEventListener('resize', onResize);   // nettoyage obligatoire
}, []);
```

### 7.10 Techniques usuelles

#### Debounce et throttle

```jsx
// Debounce d'une recherche : attendre 300 ms après la dernière frappe
const [terme, setTerme] = useState('');
const [recherche, setRecherche] = useState('');
useEffect(() => {
  const id = setTimeout(() => setRecherche(terme), 300);
  return () => clearTimeout(id);
}, [terme]);
```

Ou `useDeferredValue` (chapitre 11) quand il s'agit d'alléger un rendu coûteux.

#### Éviter le double envoi

```jsx
async function handleSubmit(e) {
  e.preventDefault();
  if (envoi) return;
  setEnvoi(true);
  try { await envoyer(); } finally { setEnvoi(false); }
}
<button disabled={envoi}>Envoyer</button>
```

### 7.11 Pièges fréquents

- `onClick={fn()}` : appel immédiat.
- Oublier `e.preventDefault()` dans un `onSubmit` (rechargement de la page).
- Penser que `e.target` est toujours l'élément portant le gestionnaire (utilisez `e.currentTarget`).
- `stopPropagation` abusif qui casse d'autres comportements.
- Ajouter un écouteur natif sans le **retirer**.
- Utiliser `onKeyPress` (déprécié) ou `keyCode`.
- Rendre cliquable un `<div>` sans clavier/ARIA.

### Synthèse du chapitre 7

Passez **une fonction**, ne l'appelez pas ; L'événement est un **SyntheticEvent** ; `target` ≠ `currentTarget` ; Les événements **remontent** ; `Capture` pour intercepter en descente ; `preventDefault` ≠ `stopPropagation` ; Les gestionnaires peuvent avoir des **effets de bord** ; `onChange` se déclenche **à chaque frappe** en React.

---

## 8. Rendu conditionnel

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : maîtriser toutes les techniques de rendu conditionnel et savoir laquelle choisir ; éviter les pièges (`&&` et `0`, ternaires imbriqués) ; comprendre l'impact sur l'état et le DOM (monter/démonter vs masquer).

### 8.1 Principe

Le rendu conditionnel utilise **le JavaScript ordinaire** (`if`, `?:`, `&&`, `switch`) pour décider **quel JSX** retourner. Il n'existe pas de directive spéciale (`v-if`, `*ngIf`) en React.

### 8.2 Techniques

#### 8.2.1 `if` avec retour anticipé (« early return »)

```jsx
function Element({ nom, emballe }) {
  if (emballe) {
    return <li>{nom} ✔</li>;
  }
  return <li>{nom}</li>;
}

function Page({ chargement, erreur, donnees }) {
  if (chargement) return <Spinner />;
  if (erreur) return <MessageErreur erreur={erreur} />;
  if (!donnees) return null;                 // ne rien afficher
  return <Contenu donnees={donnees} />;
}
```

Excellent pour les **cas limites** (chargement, erreur, vide) : le « cas heureux » reste lisible.

#### 8.2.2 Opérateur ternaire `condition ? A : B`

```jsx
<li>{emballe ? <del>{nom} ✔</del> : nom}</li>
<p className={actif ? 'actif' : 'inactif'}>…</p>
```

À éviter quand **imbriqué** (illisible) : extraire un composant ou utiliser `if`.

#### 8.2.3 Opérateur logique ET `&&`

```jsx
<li>{nom} {emballe && '✔'}</li>
{utilisateur && <Profil utilisateur={utilisateur} />}
```

- Si la condition est `false`/`null`/`undefined`, rien n'est rendu.
- **Piège du `0`** : `{nombre && <X />}` rend **`0`** quand `nombre === 0`.

```jsx
{messages.length && <Liste />}        // ❌ affiche "0"
{messages.length > 0 && <Liste />}    // ✅ condition booléenne
{!!messages.length && <Liste />}      // ✅
{messages.length ? <Liste /> : null}  // ✅
```

#### 8.2.4 `null` : ne rien afficher

```jsx
function Notification({ message }) {
  if (!message) return null;
  return <div role="alert">{message}</div>;
}
```

#### 8.2.5 Affecter du JSX à une variable

```jsx
function Element({ nom, emballe }) {
  let contenu = nom;
  if (emballe) contenu = <del>{nom} ✔</del>;
  return <li>{contenu}</li>;
}
```

#### 8.2.6 Fallback avec `||` et `??`

```jsx
<p>{utilisateur.surnom || utilisateur.nom}</p>   // falsy → fallback (attention à 0 et '')
<p>{compteur ?? 'N/A'}</p>                       // seulement null/undefined → fallback
```

#### 8.2.7 `switch` / tables de correspondance (lookup)

```jsx
function Statut({ etat }) {
  switch (etat) {
    case 'chargement': return <Spinner />;
    case 'erreur':     return <Erreur />;
    case 'succes':     return <Succes />;
    default:           return null;
  }
}

// Lookup object : plus compact et extensible
const vues = { chargement: Spinner, erreur: Erreur, succes: Succes };
function Statut({ etat }) {
  const Vue = vues[etat];
  return Vue ? <Vue /> : null;
}
```

#### 8.2.8 Attributs, classes et styles conditionnels

```jsx
<button disabled={!valide} className={`btn ${valide ? 'btn--ok' : ''}`} style={{ opacity: valide ? 1 : 0.5 }} />
<input aria-invalid={erreur ? 'true' : undefined} />      {/* undefined → attribut absent */}
```

#### 8.2.9 Enveloppe conditionnelle

```jsx
function Lien({ href, children }) {
  return href ? <a href={href}>{children}</a> : <span>{children}</span>;
}
// ou
const contenu = <Texte />;
return href ? <a href={href}>{contenu}</a> : contenu;
```

### 8.3 Monter/démonter ou simplement masquer ?

| Approche | Effet | À utiliser quand |
|---|---|---|
| **Rendu conditionnel** `{ok && <X/>}` | Le composant est **monté/démonté** : **état perdu**, effets relancés | L'élément n'a pas besoin de persister ; économie de ressources |
| **Masquage CSS** (`hidden`, `display:none`) | Le composant reste monté : **état conservé**, effets actifs | Basculements fréquents ; préserver une saisie ; éviter de recharger |
| **`<Activity mode="hidden">`** (React 19.2) | Masqué, **état conservé**, **effets suspendus**, mises à jour différées | Onglets, panneaux, navigation retour en préservant l'état sans coût d'effets |

```jsx
<div hidden={!ouvert}><Formulaire /></div>              // état conservé
{ouvert && <Formulaire />}                              // état perdu à la fermeture
```

> Un composant démonté perd son **état** : placez l'état dans le **parent** si vous voulez le garder.

### 8.4 Le pattern « chargement / erreur / vide / succès »

Toute interface qui dépend de données asynchrones a **quatre états** à gérer :

```jsx
function ListeUtilisateurs() {
  const { data, isLoading, error } = useUtilisateurs();
  if (isLoading) return <Squelette />;
  if (error)     return <Erreur message={error.message} reessayer={…} />;
  if (data.length === 0) return <EtatVide message="Aucun utilisateur" />;
  return <ul>{data.map(u => <li key={u.id}>{u.nom}</li>)}</ul>;
}
```

Préférez un **état énuméré** (`'idle' | 'loading' | 'success' | 'error'`) à plusieurs booléens susceptibles de se contredire.

### 8.5 Évaluer la condition : valeurs vraies et fausses

En JavaScript, toute valeur est évaluée comme **vraie** (*truthy*) ou **fausse** (*falsy*) dans un contexte booléen. Les valeurs fausses sont : `false`, `0`, `-0`, `0n`, `""`, `null`, `undefined` et `NaN`. **Tout le reste est vrai**, y compris `"0"`, `"false"`, `[]` et `{}`.

React ajoute une seconde règle, **indépendante** : certaines valeurs sont **ignorées au rendu** (rien n'est inséré dans le DOM) alors que d'autres sont **affichées**.

| Valeur placée dans le JSX | Rendu |
| --- | --- |
| `true`, `false`, `null`, `undefined` | **Rien** |
| `""` (chaîne vide) | Rien (nœud texte vide) |
| `0`, `NaN`, `0n` | **Affichés** (`0`, `NaN`, `0`) |
| `"texte"`, `42` | Affichés |
| Tableau (`[<li/>, <li/>]`) | Chaque élément est rendu (clés requises) |
| Objet quelconque (hors élément React) | **Erreur** (*Objects are not valid as a React child*) |

C'est la combinaison de ces deux règles qui explique le piège le plus célèbre du rendu conditionnel :

```jsx
// ❌ Si messages.length vaut 0, le nombre 0 est affiché à l'écran
{messages.length && <Liste messages={messages} />}

// ✅ Condition explicitement booléenne
{messages.length > 0 && <Liste messages={messages} />}
{Boolean(messages.length) && <Liste messages={messages} />}

// ✅ Ou un ternaire avec null
{messages.length ? <Liste messages={messages} /> : null}
```

**Règle pratique.** À gauche d'un `&&`, mettez toujours une expression dont le résultat est un **booléen** (`> 0`, `!== null`, `Boolean(...)`, `!!`), jamais un nombre ou une chaîne brute. En React Native, la règle est encore plus stricte : une chaîne vide ou un texte hors composant `<Text>` provoque une **erreur**, pas seulement un affichage indésirable.

### 8.6 Rendu conditionnel et identité : ce que devient l'état

React identifie un composant par son **type** et sa **position** dans l'arbre (chapitre 9 pour le rôle des clés). Le rendu conditionnel agit donc directement sur la **conservation de l'état** local.

**Cas 1 : même type, même position → l'état est conservé.**

```jsx
function Page({ estAdmin }) {
  return estAdmin
    ? <Formulaire titre="Administration" />
    : <Formulaire titre="Profil" />;   // même composant, même position
}
// Le texte saisi dans le formulaire survit au changement de estAdmin.
```

**Cas 2 : type différent à la même position → l'état est détruit.**

```jsx
return estAdmin
  ? <section><Formulaire /></section>
  : <div><Formulaire /></div>;          // <section> ≠ <div> : tout est remonté
```

**Cas 3 : composant rendu ou non → monté / démonté.** Quand `{cond && <Panneau />}` passe de vrai à faux, `Panneau` est **démonté** : son état est perdu et ses effets sont nettoyés. Quand la condition redevient vraie, il est **remonté à neuf**.

**Réinitialiser volontairement** : donnez une `key` différente, ce qui force React à considérer qu'il s'agit d'un autre composant.

```jsx
<Formulaire key={utilisateur.id} utilisateur={utilisateur} />
```

**Conserver volontairement** un état malgré l'absence d'affichage : (a) **remontez l'état** dans un parent qui reste monté ; (b) **masquez** avec du CSS ou l'attribut `hidden` ; (c) utilisez `<Activity mode="hidden">` (chapitre 22), qui garde l'état tout en suspendant les effets.

> **Ne définissez jamais un composant à l'intérieur d'un autre composant.** À chaque rendu du parent, la fonction interne est une **nouvelle fonction**, donc un **nouveau type** : React démonte et remonte l'enfant à chaque fois, et son état est perdu.

### 8.7 Rendu conditionnel et Hooks

Les Hooks doivent être appelés **à chaque rendu, dans le même ordre** (chapitre 11). Un `return` anticipé placé **avant** un Hook viole cette règle.

```jsx
// ❌ useState n'est pas appelé quand chargement est vrai
function Profil({ chargement, utilisateur }) {
  if (chargement) return <Spinner />;
  const [edition, setEdition] = useState(false);   // erreur : nombre de Hooks variable
  return <Fiche utilisateur={utilisateur} edition={edition} />;
}

// ✅ Tous les Hooks d'abord, les retours anticipés ensuite
function Profil({ chargement, utilisateur }) {
  const [edition, setEdition] = useState(false);
  if (chargement) return <Spinner />;
  return <Fiche utilisateur={utilisateur} edition={edition} />;
}

// ✅✅ Ou : extraire la partie conditionnelle dans un composant dédié
function Profil({ chargement, utilisateur }) {
  if (chargement) return <Spinner />;
  return <FicheEditable utilisateur={utilisateur} />;  // porte son propre useState
}
```

Le message d'erreur typique est *Rendered fewer hooks than expected* (ou *more*). La règle de lint `react-hooks/rules-of-hooks` la détecte à l'écriture.

### 8.8 Masquer, démonter ou suspendre : récapitulatif

| Technique | État local | Effets | DOM | Accessibilité | Usage typique |
| --- | --- | --- | --- | --- | --- |
| `{cond && <X />}` (démontage) | Perdu | Nettoyés | Absent | Absent | Cas général, contenu léger ou sans état à garder |
| CSS `display: none` / attribut `hidden` | Conservé | **Toujours actifs** | Présent | Masqué aux lecteurs d'écran | Onglets, menus : bascule fréquente et état à préserver |
| CSS `visibility: hidden` | Conservé | Actifs | Présent (occupe l'espace) | Masqué | Réserver la place pour éviter un décalage de mise en page |
| `<Activity mode="hidden">` | **Conservé** | **Suspendus** (nettoyés) | Présent mais masqué | Masqué | Pages/onglets « en veille » dont on veut garder l'état sans coût d'effets |
| Remontée de l'état dans un parent | Conservé (dans le parent) | Selon l'enfant | Absent | Absent | État à conserver sans garder le DOM |

Le critère de choix est double : **faut-il conserver l'état ?** et **le composant doit-il continuer à travailler en arrière-plan ?** (abonnements, minuteurs, requêtes). Avec `display: none`, un `setInterval` continue de tourner ; avec `<Activity mode="hidden">`, les effets sont nettoyés et recréés à l'affichage.

### 8.9 Composants de garde et conditions d'accès

Quand la même condition se répète (utilisateur connecté, droit particulier, fonctionnalité activée), encapsulez-la dans un **composant de garde** (*guard*) plutôt que de dupliquer des `&&` partout.

```jsx
function Garde({ autorise, secours = null, children }) {
  return autorise ? children : secours;
}

function PageAdmin() {
  const { utilisateur } = useSession();
  return (
    <Garde autorise={utilisateur?.role === 'admin'} secours={<AccesRefuse />}>
      <TableauDeBord />
    </Garde>
  );
}
```

Pour les **fonctionnalités activées par drapeau** (*feature flags*), le même principe s'applique :

```jsx
function Fonctionnalite({ nom, children, repli = null }) {
  const drapeaux = useDrapeaux();
  return drapeaux[nom] ? children : repli;
}
```

> Une garde **côté interface** ne protège **pas** les données : l'autorisation doit toujours être **revérifiée côté serveur**. Elle sert l'expérience utilisateur, pas la sécurité.

### 8.10 Accessibilité du contenu qui apparaît et disparaît

Afficher ou masquer du contenu n'est pas qu'un sujet visuel.

- **Annoncer les changements** : un message d'erreur ou de confirmation inséré dynamiquement n'est lu que s'il est dans une **région vivante** (*live region*) présente **dès le départ** dans le DOM : `<div role="status" aria-live="polite">{message}</div>` pour une information, `role="alert"` pour une erreur urgente.
- **Gérer le focus** : si un clic ouvre un panneau ou une modale, déplacez le focus dedans ; à la fermeture, **restituez** le focus à l'élément déclencheur. Si l'élément qui a le focus disparaît, le focus retombe sur `<body>`, et l'utilisateur au clavier est perdu.
- **Exposer l'état** : `aria-expanded` sur le bouton d'un panneau dépliable, `aria-controls` vers son identifiant, `aria-busy="true"` pendant un chargement.
- **Masquer correctement** : `display: none` et l'attribut `hidden` retirent l'élément de l'arbre d'accessibilité **et** de l'ordre de tabulation ; `aria-hidden="true"` ne masque qu'aux technologies d'assistance mais laisse l'élément **focalisable** (à éviter sur du contenu interactif). L'attribut `inert` désactive à la fois le focus, les clics et l'exposition aux lecteurs d'écran.
- **Squelettes de chargement** : indiquez l'état de chargement par un texte alternatif ou `aria-busy`, pas seulement par une animation.

### 8.11 Lisibilité : choisir la bonne écriture

| Situation | Écriture recommandée |
| --- | --- |
| Deux branches, rendu court | Ternaire `cond ? <A /> : <B />` |
| Afficher ou ne rien afficher | `cond && <A />` (condition **booléenne**) |
| Cas d'erreur, de chargement ou de vide avant le rendu principal | **Retour anticipé** |
| Trois cas ou plus, mutuellement exclusifs | **Table de correspondance** ou `switch` dans une fonction |
| Branche longue ou logique complexe | **Extraire un composant** (`<Resultat />`, `<Erreur />`) |
| Même condition répétée | **Composant de garde** ou variable nommée (`const peutEditer = …`) |

Évitez les **ternaires imbriqués** : au-delà d'un niveau, ils deviennent illisibles. Remplacez-les par une table :

```jsx
const vues = {
  chargement: <Spinner />,
  erreur: <Erreur />,
  vide: <EtatVide />,
  succes: <Liste elements={elements} />,
};
return vues[statut] ?? null;
```

Nommer les conditions améliore la lecture : `const afficherBanniere = !abonne && essaiTermine;` est plus clair que la même expression écrite dans le JSX.

### 8.12 Pièges fréquents

- `{nombre && <X />}` affichant `0`.
- **Ternaires imbriqués** illisibles.
- Hooks placés **après** un `return` anticipé → viole la règle des hooks (les appels doivent être dans le même ordre à chaque rendu).
- Démonter un formulaire pour le « masquer » et perdre la saisie.
- Rendre `undefined` dans un composant hérité d'une ancienne version (erreur avant React 18).

### Synthèse du chapitre 8

C'est du **JavaScript pur** : `if`, `?:`, `&&`, `switch` ; **Early return** pour les cas limites ; **ternaire** pour deux branches ; **`&&`** pour « afficher ou rien » (avec condition booléenne) ; Monter/démonter **détruit l'état** ; masquer le **conserve** ; Gérez toujours **chargement, erreur, vide**.

---

## 9. Listes et clés

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : afficher des collections avec `map`, `filter` et leurs dérivés ; comprendre le rôle exact des `key` dans la réconciliation ; choisir des clés correctes et éviter les bugs liés à l'index.

### 9.1 Afficher une liste

On **transforme un tableau de données en tableau d'éléments JSX** avec `map`, que React sait rendre :

```jsx
const personnes = [
  { id: 0, nom: 'Ada Lovelace', metier: 'mathématicienne' },
  { id: 1, nom: 'Grace Hopper', metier: 'informaticienne' },
  { id: 2, nom: 'Margaret Hamilton', metier: 'ingénieure logiciel' },
];

function ListePersonnes() {
  const items = personnes.map(p => (
    <li key={p.id}>
      <b>{p.nom}</b> : {p.metier}
    </li>
  ));
  return <ul>{items}</ul>;
}
```

#### Filtrer puis afficher

```jsx
const mathematiciennes = personnes.filter(p => p.metier === 'mathématicienne');
return <ul>{mathematiciennes.map(p => <li key={p.id}>{p.nom}</li>)}</ul>;
```

> Le tri, le filtre et les regroupements sont des **valeurs dérivées** : calculez-les **pendant le rendu** (éventuellement avec `useMemo`), ne les stockez **pas** dans un state.

#### Fonction fléchée avec corps

```jsx
{personnes.map(p => {
  const age = calculerAge(p);          // instructions → accolades + return
  return <Fiche key={p.id} personne={p} age={age} />;
})}
```

#### Objets : `Object.entries`

```jsx
{Object.entries(stocks).map(([produit, quantite]) => (
  <li key={produit}>{produit} : {quantite}</li>
))}
```

#### Aplatir : `flatMap`

```jsx
{groupes.flatMap(g => g.membres).map(m => <Membre key={m.id} membre={m} />)}
```

#### Listes imbriquées

```jsx
{categories.map(cat => (
  <section key={cat.id}>
    <h2>{cat.nom}</h2>
    <ul>{cat.produits.map(p => <li key={p.id}>{p.nom}</li>)}</ul>
  </section>
))}
```

Chaque niveau a ses propres `key` (unicité requise **parmi les frères uniquement**).

#### Liste vide

```jsx
{items.length === 0 ? <p>Aucun résultat</p> : <ul>{items.map(…)}</ul>}
```

### 9.2 Les clés (`key`) : définition

La **`key`** est un **identifiant spécial** que React utilise pour **reconnaître chaque élément d'une liste** d'un rendu à l'autre. Elle permet à React de :

- savoir **quel élément correspond à quel élément** lors d'un ajout, d'une suppression ou d'un déplacement ;
- **réutiliser** les nœuds DOM et **conserver l'état** des composants associés au bon élément ;
- **minimiser** les opérations DOM.

Sans `key`, React avertit (« Each child in a list should have a unique key prop ») et se rabat sur l'**index** (position).

### 9.3 Règles des clés

1. **Uniques parmi les frères** (même tableau) ; pas besoin d'être globalement uniques.
2. **Stables** : une clé ne doit **pas changer** entre les rendus pour un même élément (pas de `Math.random()` ou `crypto.randomUUID()` **pendant le rendu**).
3. **Placées sur l'élément retourné par `map`** (le plus externe), pas sur un enfant.
4. **Pas de `key` transmise** : `props.key` est `undefined` ; si le composant a besoin de l'ID, passez-le sous un autre nom (`id`).
5. **Type** : chaîne ou nombre.

```jsx
// ❌ La clé doit être sur l'élément externe du map
{items.map(i => <Fragment><dt key={i.id}>…</dt></Fragment>)}
// ✅
{items.map(i => <Fragment key={i.id}><dt>{i.terme}</dt><dd>{i.def}</dd></Fragment>)}
```

> La syntaxe courte `<>…</>` **n'accepte pas de `key`** : utilisez `<Fragment key={…}>`.

### 9.4 D'où viennent les clés ?

| Source | Exemple | Remarque |
|---|---|---|
| **Base de données / API** | `id`, `uuid`, `slug` | Idéal |
| **Données locales** | Identifiant créé **à la création de l'élément** (`crypto.randomUUID()`, compteur incrémental) | Générer **une fois** (dans le gestionnaire d'ajout) |
| **Valeur unique naturelle** | e-mail, SKU, nom de fichier | Si garantie unique et stable |
| **Index** | `index` | Acceptable **uniquement** si la liste est **statique** (jamais réordonnée, filtrée, insérée) |

```jsx
function ajouter(titre) {
  setTaches(prev => [...prev, { id: crypto.randomUUID(), titre }]);   // ID créé UNE fois
}
```

### 9.5 Pourquoi l'index est dangereux

Si l'on **insère, supprime ou réordonne**, les index se **décalent** : React associe l'état/DOM à la mauvaise donnée.

```jsx
// Liste d'inputs avec index comme clé
{lignes.map((l, i) => <li key={i}><input defaultValue={l.texte} /></li>)}
// Supprimer la ligne 0 : le texte saisi dans l'input n°0 reste affiché alors que la donnée n°0 a disparu
```

Symptômes : champs non contrôlés qui gardent la mauvaise valeur, **focus** déplacé, animations erronées, état local (checkbox, expansion) attaché au mauvais élément, rendus inutiles.

> Utiliser l'index **supprime l'avertissement**, mais **ne corrige pas** le problème d'identité.

### 9.6 Clés et réconciliation (fonctionnement)

Lorsqu'une liste change, React compare les anciens et nouveaux enfants :

- **Même clé + même type** → l'élément est **mis à jour** (réutilisé), son **état conservé**.
- **Nouvelle clé** → élément **créé** (monté).
- **Clé disparue** → élément **détruit** (démonté).
- **Clé déplacée** → nœud **déplacé** dans le DOM, sans recréation.

### 9.7 Utiliser `key` en dehors des listes : réinitialiser un composant

Changer la `key` d'un composant force React à le **recréer** (état remis à zéro) :

```jsx
<ProfilEditeur key={utilisateurId} utilisateurId={utilisateurId} />
```

Plus propre et plus fiable que de synchroniser manuellement l'état avec des effets.

### 9.8 Séparer les responsabilités : extraire l'élément de liste

```jsx
function Tache({ tache, onBasculer }) {          // pas de `key` ici : elle est posée par le parent
  return <li>…</li>;
}
{taches.map(t => <Tache key={t.id} tache={t} onBasculer={onBasculer} />)}
```

### 9.9 Performance sur de grandes listes

- Éviter de recalculer `filter/sort` à chaque rendu si la liste est volumineuse : `useMemo`.
- Mémoïser l'élément enfant (`memo`) et stabiliser les callbacks (`useCallback`) — **après mesure**.
- **Pagination** / **« charger plus »**.
- **Virtualisation** (windowing) : ne rendre que les éléments visibles : `react-window`, `react-virtuoso`, `@tanstack/react-virtual`. Indispensable à partir de plusieurs centaines/milliers de lignes.
- `useDeferredValue` / `useTransition` pour garder la saisie fluide lors du filtrage.

### 9.10 Exemple complet : liste de tâches avec filtre

```jsx
function TodoApp() {
  const [taches, setTaches] = useState([]);
  const [filtre, setFiltre] = useState('toutes');       // 'toutes' | 'actives' | 'faites'

  const visibles = taches.filter(t =>
    filtre === 'toutes' ? true : filtre === 'faites' ? t.faite : !t.faite
  );                                                      // dérivé, pas de state

  return (
    <>
      <Ajout onAjouter={titre => setTaches(p => [...p, { id: crypto.randomUUID(), titre, faite: false }])} />
      <Filtres valeur={filtre} onChange={setFiltre} />
      {visibles.length === 0 ? <p>Rien à afficher</p> : (
        <ul>
          {visibles.map(t => (
            <TodoItem
              key={t.id}
              tache={t}
              onBasculer={id => setTaches(p => p.map(x => x.id === id ? { ...x, faite: !x.faite } : x))}
              onSupprimer={id => setTaches(p => p.filter(x => x.id !== id))}
            />
          ))}
        </ul>
      )}
    </>
  );
}
```

### 9.11 Trier, filtrer, paginer sans muter

`Array.prototype.sort`, `reverse` et `splice` **modifient** le tableau d'origine : si ce tableau est un état ou une prop, c'est une mutation interdite (chapitres 4 et 6). Travaillez sur une **copie**.

```jsx
// ✅ Copie puis tri
const tries = [...produits].sort((a, b) => a.prix - b.prix);

// ✅ Méthodes non mutantes (ES2023)
const tries2 = produits.toSorted((a, b) => a.prix - b.prix);
const inverses = produits.toReversed();
const sans = produits.toSpliced(2, 1);        // retire l'élément d'indice 2
const modifie = produits.with(0, nouveau);    // remplace l'élément d'indice 0
```

**Tri, filtre, pagination : valeurs dérivées.** Ne stockez pas la liste affichée dans un état ; stockez les **critères** (tri, filtre, page) et **calculez** la liste pendant le rendu :

```jsx
function Catalogue({ produits }) {
  const [filtre, setFiltre] = useState('');
  const [tri, setTri] = useState('nom');
  const [page, setPage] = useState(0);
  const TAILLE = 20;

  const affiches = produits
    .filter(p => p.nom.toLowerCase().includes(filtre.toLowerCase()))
    .toSorted((a, b) => (a[tri] > b[tri] ? 1 : -1))
    .slice(page * TAILLE, (page + 1) * TAILLE);

  return <ul>{affiches.map(p => <li key={p.id}>{p.nom}</li>)}</ul>;
}
```

Si le calcul devient **mesurablement** coûteux, mémoïsez-le avec `useMemo` (chapitre 16). Pour le tri **textuel** en français, utilisez `localeCompare('fr')` (ou `Intl.Collator`) afin de respecter accents et casse.

### 9.12 Cas particuliers des clés

- **Clé composite** : quand l'unicité vient de plusieurs champs, concaténez-les : `key={`${commande.id}-${ligne.produitId}`}`.
- **Clé sur un fragment** : `<Fragment key={id}>…</Fragment>` (chapitre 20), jamais sur les éléments internes seuls.
- **Unicité parmi les frères** : une clé doit être unique **dans sa liste**, pas globalement. Deux listes différentes peuvent réutiliser les mêmes valeurs.
- **`key` n'est pas une prop** : le composant enfant ne la reçoit pas (`props.key` est `undefined`). Si l'enfant a besoin de l'identifiant, passez-le **aussi** sous un autre nom (`id`).
- **Données sans identifiant** : générez l'identifiant **à la création** de l'élément (dans le gestionnaire d'ajout, avec `crypto.randomUUID()`), pas pendant le rendu. Un identifiant produit à chaque rendu change à chaque fois et fait **remonter** tous les éléments.
- **Clé stable ≠ clé significative pour l'utilisateur** : ne réutilisez pas un libellé modifiable (nom saisi par l'utilisateur) comme clé, car la modification changerait l'identité de l'élément.
- **Liste statique** (jamais réordonnée, jamais filtrée, jamais modifiée) : l'index est acceptable, mais un identifiant reste préférable.

### 9.13 Sélection, drapeaux et état dérivé dans une liste

Pour mémoriser **l'élément sélectionné**, stockez son **identifiant**, pas l'objet :

```jsx
const [idSelectionne, setIdSelectionne] = useState(null);
const selectionne = taches.find(t => t.id === idSelectionne);   // toujours à jour
```

Stocker l'objet lui-même crée une **copie obsolète** dès que la liste est mise à jour (immutabilité : l'objet de la liste est remplacé). Pour une **sélection multiple**, utilisez un `Set` d'identifiants (copié à chaque modification) ou un tableau d'identifiants.

Pour des modifications **ciblées** dans une liste, utilisez `map` :

```jsx
setTaches(taches.map(t => (t.id === id ? { ...t, faite: !t.faite } : t)));
```

### 9.14 Accessibilité des listes interactives

- Utilisez `<ul>` / `<ol>` et `<li>` : les lecteurs d'écran annoncent « liste de N éléments ». Si une règle CSS retire les puces (`list-style: none`), certains navigateurs ne l'annoncent plus comme liste : ajoutez `role="list"`.
- **Suppression d'un élément** : déplacez le focus vers l'élément suivant (ou précédent, ou le titre de la liste) ; sinon le focus retombe sur `<body>` et l'utilisateur au clavier perd sa position.
- **Annoncer les changements** (ajout, suppression, tri) dans une région `role="status"` : « Tâche supprimée. 4 tâches restantes. »
- **Boutons explicites** : `aria-label={`Supprimer ${tache.titre}`}` plutôt qu'une série de boutons « Supprimer » indistincts.
- **Listes virtualisées** (seul un sous-ensemble est dans le DOM) : exposez la position avec `aria-setsize` et `aria-posinset`.
- **Réordonnancement par glisser-déposer** : prévoyez une **alternative clavier** (boutons « Monter » / « Descendre ») ; des bibliothèques comme dnd-kit fournissent le comportement accessible.

### 9.15 Pagination, « charger plus » et défilement infini

| Approche | Avantages | Inconvénients |
| --- | --- | --- |
| **Pagination** numérotée | Position repérable, URL par page, accessible | Clic supplémentaire |
| **Bouton « Charger plus »** | Contrôle de l'utilisateur, simple, accessible | Liste qui s'allonge |
| **Défilement infini** | Fluidité d'exploration | Pied de page inatteignable, focus et retour arrière difficiles, accessibilité délicate |
| **Virtualisation** | Peu de nœuds DOM, très grandes listes | Complexité, recherche native du navigateur limitée |

Un défilement infini s'implémente avec un **élément sentinelle** observé par un `IntersectionObserver` (chapitre 14) : quand il devient visible, on charge la page suivante. Les bibliothèques de données (TanStack Query : `useInfiniteQuery`) gèrent la pagination, le cache et les doublons. Conservez l'état (page, filtres) dans l'**URL** pour permettre le retour arrière et le partage.

### 9.16 Animer l'entrée, la sortie et le déplacement

Les **clés stables** sont indispensables aux animations de liste, car elles permettent de suivre un élément d'un rendu à l'autre. Un élément **supprimé** disparaît du DOM immédiatement : pour l'animer en sortie, utilisez une bibliothèque qui retarde le démontage (**Motion** / Framer Motion avec `AnimatePresence`, **React Transition Group**) ou une animation CSS avec un état de sortie intermédiaire. Pour animer un **déplacement** (réordonnancement), les techniques FLIP (mesurer avant et après, puis animer la différence) ou la propriété `layout` de Motion s'appuient toutes sur l'identité par clé. Respectez **`prefers-reduced-motion`**.

### 9.17 Typer un composant de liste générique

```tsx
import type { ReactNode } from 'react';

type ListeProps<T> = {
  elements: readonly T[];
  getCle: (element: T) => string | number;
  rendu: (element: T, index: number) => ReactNode;
  vide?: ReactNode;
};

export function Liste<T>({ elements, getCle, rendu, vide = <p>Aucun élément.</p> }: ListeProps<T>) {
  if (elements.length === 0) return vide;
  return <ul>{elements.map((e, i) => <li key={getCle(e)}>{rendu(e, i)}</li>)}</ul>;
}

// <Liste elements={produits} getCle={p => p.id} rendu={p => <Produit {...p} />} />
```

Le **générique** `T` est inféré à partir de `elements` : `rendu` reçoit un `Produit` correctement typé, sans conversion. La **clé** est demandée à l'appelant, ce qui oblige à y penser.

### 9.18 Pièges fréquents

- Oublier la `key` (avertissement + comportements imprévisibles).
- `key={Math.random()}` : recrée tous les éléments à chaque rendu.
- `key={index}` dans une liste dynamique.
- Placer la `key` sur un mauvais niveau ou sur `<>…</>`.
- Attendre `props.key` dans l'enfant.
- Stocker la liste filtrée dans le state au lieu de la dériver.
- Muter le tableau (`sort()`) en le triant avant l'affichage.

### Synthèse du chapitre 9

`map` transforme **données → éléments** ; la **`key`** donne l'**identité** ; Clés **uniques entre frères, stables, issues des données** ; L'**index** n'est valable que pour des listes **statiques** ; Changer la `key` d'un composant = le **réinitialiser** ; Filtrer/trier = **calculs dérivés**, pas du state ; **virtualisez** les très grandes listes.

---

## 10. Formulaires

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : distinguer composants **contrôlés** et **non contrôlés** et savoir choisir ; gérer chaque type de champ (texte, case, radio, liste, fichier…) ; implémenter validation, messages d'erreur et accessibilité ; utiliser les **Actions de formulaire** de React 19 (`action`, `useActionState`, `useFormStatus`, `useOptimistic`) ; connaître les bibliothèques de formulaires et leurs compromis.

### 10.1 Deux modèles : contrôlé et non contrôlé

#### Composant **contrôlé**

La **valeur affichée** est **pilotée par le state React** ; chaque modification passe par un gestionnaire. React est la **source unique de vérité**.

```jsx
function Recherche() {
  const [texte, setTexte] = useState('');
  return (
    <input
      value={texte}                              // la valeur vient du state
      onChange={(e) => setTexte(e.target.value)} // chaque frappe met à jour le state
    />
  );
}
```

#### Composant **non contrôlé**

Le **DOM** garde la valeur ; React la lit **à la demande** (via `ref` ou `FormData`). On fournit une valeur **initiale** avec `defaultValue` / `defaultChecked`.

```jsx
function Recherche() {
  function handleSubmit(e) {
    e.preventDefault();
    const donnees = new FormData(e.currentTarget);
    console.log(donnees.get('q'));
  }
  return (
    <form onSubmit={handleSubmit}>
      <input name="q" defaultValue="react" />
      <button>Chercher</button>
    </form>
  );
}
```

#### Comparatif

| Critère | Contrôlé | Non contrôlé |
|---|---|---|
| Source de vérité | State React | DOM |
| Valeur disponible à chaque frappe | ✅ | ❌ (à la demande) |
| Validation en direct / formatage / désactivation du bouton | ✅ facile | ⚠ plus laborieux |
| Re-rendu à chaque frappe | Oui | Non |
| Code | Plus verbeux | Plus concis |
| `<input type="file">` | ❌ impossible (lecture seule) | ✅ obligatoire |
| Intégration de bibliothèques non React | Plus difficile | Plus simple |

> Règle pratique : **non contrôlé + `FormData` + Actions** pour les formulaires simples ; **contrôlé** quand l'UI réagit à la saisie (validation en direct, champs dépendants, masques, aperçu).

#### Avertissements fréquents

- **« You provided a `value` prop to a form field without an `onChange` handler »** : champ en lecture seule involontaire. Ajoutez `onChange`, ou `readOnly`, ou `defaultValue`.
- **« A component is changing an uncontrolled input to be controlled »** : `value` est passé de `undefined`/`null` à une chaîne. Initialisez le state avec `''`, jamais `undefined`/`null`.
- Ne **jamais** donner à la fois `value` et `defaultValue`.

### 10.2 Chaque type de champ

#### Texte, e-mail, mot de passe, nombre, date, couleur, recherche, URL, tel

```jsx
<input type="text" value={nom} onChange={e => setNom(e.target.value)} />
<input type="email" value={email} onChange={e => setEmail(e.target.value)} autoComplete="email" />
<input type="number" value={age} onChange={e => setAge(e.target.value)} />   {/* e.target.value est une CHAÎNE */}
<input type="date" value={date} onChange={e => setDate(e.target.value)} />   {/* 'AAAA-MM-JJ' */}
<input type="color" value={couleur} onChange={e => setCouleur(e.target.value)} />
```

> Pour un `type="number"`, convertissez : `e.target.valueAsNumber` (NaN si vide) ou `Number(e.target.value)`. Conservez la **chaîne** dans le state tant que la saisie n'est pas terminée (sinon `''`, `-`, `1.` posent problème).

#### `<textarea>`

En React, `<textarea>` utilise `value` (et non son contenu enfant) :

```jsx
<textarea value={message} onChange={e => setMessage(e.target.value)} rows={4} />
```

#### `<select>`

La valeur est placée sur le **`<select>`**, pas sur `<option selected>` :

```jsx
<select value={pays} onChange={e => setPays(e.target.value)}>
  <option value="">— Choisir —</option>
  <option value="fr">France</option>
  <option value="be">Belgique</option>
</select>
```

Sélection **multiple** : `value` est un **tableau**.

```jsx
<select multiple value={choix} onChange={e =>
  setChoix(Array.from(e.target.selectedOptions, o => o.value))
}>…</select>
```

#### Case à cocher (`checkbox`) : on utilise `checked`

```jsx
<input type="checkbox" checked={accepte} onChange={e => setAccepte(e.target.checked)} />
```

Groupe de cases (tableau de valeurs) :

```jsx
function toggle(valeur) {
  setSelection(prev => prev.includes(valeur) ? prev.filter(v => v !== valeur) : [...prev, valeur]);
}
{options.map(o => (
  <label key={o}>
    <input type="checkbox" checked={selection.includes(o)} onChange={() => toggle(o)} /> {o}
  </label>
))}
```

#### Boutons radio

```jsx
{['S', 'M', 'L'].map(t => (
  <label key={t}>
    <input type="radio" name="taille" value={t} checked={taille === t} onChange={e => setTaille(e.target.value)} />
    {t}
  </label>
))}
```

#### Curseur (`range`)

```jsx
<input type="range" min="0" max="100" value={volume} onChange={e => setVolume(Number(e.target.value))} />
```

#### Fichiers : toujours non contrôlé

```jsx
function Upload() {
  const [fichier, setFichier] = useState(null);
  return (
    <>
      <input type="file" accept="image/*" onChange={e => setFichier(e.target.files[0] ?? null)} />
      {fichier && <img src={URL.createObjectURL(fichier)} alt="aperçu" />}
      {/* Libérer avec URL.revokeObjectURL dans un effet de nettoyage pour éviter les fuites */}
    </>
  );
}
// Envoi : const fd = new FormData(); fd.append('fichier', fichier); fetch('/upload', { method: 'POST', body: fd });
```

### 10.3 Gérer plusieurs champs

#### Un seul gestionnaire avec `name`

```jsx
const [form, setForm] = useState({ nom: '', email: '', newsletter: false });

function handleChange(e) {
  const { name, type, value, checked } = e.target;
  setForm(prev => ({ ...prev, [name]: type === 'checkbox' ? checked : value }));
}

<input name="nom" value={form.nom} onChange={handleChange} />
<input name="email" value={form.email} onChange={handleChange} />
<input name="newsletter" type="checkbox" checked={form.newsletter} onChange={handleChange} />
```

#### Avec `useReducer` pour des formulaires complexes

```jsx
function reducer(state, action) {
  switch (action.type) {
    case 'champ':   return { ...state, valeurs: { ...state.valeurs, [action.nom]: action.valeur } };
    case 'touche':  return { ...state, touches: { ...state.touches, [action.nom]: true } };
    case 'erreurs': return { ...state, erreurs: action.erreurs };
    case 'reset':   return initial;
    default: throw new Error('Action inconnue');
  }
}
```

### 10.4 Soumission

```jsx
function Formulaire() {
  const [statut, setStatut] = useState('saisie');   // 'saisie' | 'envoi' | 'succes' | 'erreur'

  async function handleSubmit(e) {
    e.preventDefault();                               // empêche le rechargement
    setStatut('envoi');
    try {
      await api.inscrire(form);
      setStatut('succes');
    } catch {
      setStatut('erreur');
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      …
      <button type="submit" disabled={statut === 'envoi'}>
        {statut === 'envoi' ? 'Envoi…' : "S'inscrire"}
      </button>
    </form>
  );
}
```

- Utiliser `onSubmit` du **`<form>`** (et non `onClick` du bouton) : prend en charge la touche **Entrée** et l'accessibilité.
- Un `<button>` dans un formulaire est `type="submit"` **par défaut** ; indiquez `type="button"` pour les boutons qui ne soumettent pas.
- **Réinitialiser** : `e.currentTarget.reset()` (non contrôlé) ou remettre le state initial (contrôlé) ; ou changer la `key` du formulaire.
- **FormData** → objet : `Object.fromEntries(new FormData(form))` (attention aux champs multiples : utilisez `getAll`).

### 10.5 Validation

#### Niveaux de validation

1. **Natif HTML** : `required`, `minLength`, `maxLength`, `min`, `max`, `pattern`, `type="email"`. Le navigateur bloque la soumission et affiche un message. `noValidate` sur `<form>` pour désactiver et gérer soi-même.
2. **Côté client personnalisé** : fonctions de validation.
3. **Côté serveur** : **indispensable** (la validation client est contournable) et source de vérité.

#### Validation personnalisée

```jsx
function valider({ email, mdp }) {
  const erreurs = {};
  if (!/^\S+@\S+\.\S+$/.test(email)) erreurs.email = 'E-mail invalide';
  if (mdp.length < 8) erreurs.mdp = 'Au moins 8 caractères';
  return erreurs;
}

const erreurs = valider(form);                        // dérivé pendant le rendu
const estValide = Object.keys(erreurs).length === 0;
```

#### Quand afficher les erreurs ?

| Stratégie | Description |
|---|---|
| À la **soumission** | Simple, peu intrusif |
| Au **blur** (`onBlur`) | Après que l'utilisateur quitte le champ (suivi d'un état « touché ») |
| À la **frappe** | Réactif, mais agressif au début ; combiner avec « touché » |
| **Hybride** (recommandé) | Premier affichage au blur, puis mise à jour en direct |

```jsx
const [touches, setTouches] = useState({});
<input name="email" value={form.email} onChange={handleChange}
       onBlur={() => setTouches(t => ({ ...t, email: true }))}
       aria-invalid={touches.email && !!erreurs.email}
       aria-describedby="err-email" />
{touches.email && erreurs.email && <p id="err-email" role="alert">{erreurs.email}</p>}
```

#### Accessibilité des formulaires

- Chaque champ a un **`<label>`** associé : `htmlFor` + `id` (utiliser `useId`) ou champ **imbriqué** dans le `<label>`.
- Signaler les erreurs avec `aria-invalid`, `aria-describedby`, et un message avec `role="alert"` ou une région `aria-live`.
- Marquer les champs requis (`required`, `aria-required`) **et** visuellement.
- Gérer le **focus** : placer le focus sur le premier champ en erreur après soumission (via `ref`).
- Attributs `autoComplete`, `inputMode`, `type` adaptés (clavier mobile, gestionnaires de mots de passe).
- Groupes : `<fieldset>` + `<legend>` pour radios/cases.

```jsx
function ChampTexte({ label, erreur, ...props }) {
  const id = useId();
  return (
    <div>
      <label htmlFor={id}>{label}</label>
      <input id={id} aria-invalid={!!erreur} aria-describedby={erreur ? `${id}-err` : undefined} {...props} />
      {erreur && <p id={`${id}-err`} role="alert">{erreur}</p>}
    </div>
  );
}
```

### 10.6 Formatage et masques

```jsx
function ChampTelephone({ valeur, onChange }) {
  function format(brut) {
    const chiffres = brut.replace(/\D/g, '').slice(0, 10);
    return chiffres.replace(/(\d{2})(?=\d)/g, '$1 ').trim();
  }
  return <input value={valeur} onChange={e => onChange(format(e.target.value))} inputMode="tel" />;
}
```

> Les champs formatés peuvent déplacer le **curseur** : pour des masques complexes, utilisez une bibliothèque dédiée (`react-imask`, `react-number-format`).

### 10.7 Actions de formulaire (React 19)

React 19 permet de passer **une fonction (éventuellement asynchrone)** à la prop **`action`** d'un `<form>`. React :

1. appelle la fonction avec un objet **`FormData`** ;
2. gère automatiquement l'état **« en attente »** (pending) via une **transition** ;
3. **réinitialise** les champs non contrôlés du formulaire **après** une action réussie ;
4. s'intègre avec les **Server Functions** (`'use server'`) et l'**amélioration progressive** (le formulaire fonctionne avant que JavaScript ne soit chargé dans un framework compatible).

```jsx
function Inscription() {
  async function inscrire(formData) {
    const email = formData.get('email');
    await api.inscrire({ email });
  }
  return (
    <form action={inscrire}>
      <input name="email" type="email" required />
      <button>S'inscrire</button>
    </form>
  );
}
```

#### `useFormStatus` (de `react-dom`) : lire l'état du formulaire parent

À appeler depuis un composant **enfant** d'un `<form>` (pas dans le composant qui rend le `<form>`).

```jsx
import { useFormStatus } from 'react-dom';

function BoutonEnvoi() {
  const { pending, data, method, action } = useFormStatus();
  return <button type="submit" disabled={pending}>{pending ? 'Envoi…' : 'Envoyer'}</button>;
}
```

#### `useActionState` : état de l'action (résultat, erreur, pending)

```jsx
import { useActionState } from 'react';

async function connexion(etatPrecedent, formData) {
  try {
    await api.connexion(formData.get('email'), formData.get('mdp'));
    return { ok: true, erreur: null };
  } catch (e) {
    return { ok: false, erreur: e.message };
  }
}

function Connexion() {
  const [etat, action, enAttente] = useActionState(connexion, { ok: false, erreur: null });
  return (
    <form action={action}>
      <input name="email" type="email" />
      <input name="mdp" type="password" />
      <button disabled={enAttente}>Connexion</button>
      {etat.erreur && <p role="alert">{etat.erreur}</p>}
    </form>
  );
}
```

- Signature : `useActionState(actionFn, etatInitial, permalink?)` → `[etat, action, isPending]`.
- `actionFn(etatPrecedent, formData)` retourne le **nouvel état**.
- Les actions d'un même `useActionState` sont **mises en file** et exécutées **séquentiellement**.
- (Anciennement `ReactDOM.useFormState`.)

#### `useOptimistic` : mise à jour optimiste

Afficher **immédiatement** le résultat attendu pendant que l'action asynchrone s'exécute ; revient à l'état réel quand l'action se termine (ou échoue).

```jsx
import { useOptimistic } from 'react';

function Messages({ messages, envoyerMessage }) {
  const [messagesOptimistes, ajouterOptimiste] = useOptimistic(
    messages,
    (etat, nouveau) => [...etat, { texte: nouveau, envoi: true }]
  );

  async function action(formData) {
    const texte = formData.get('texte');
    ajouterOptimiste(texte);               // affichage immédiat
    await envoyerMessage(texte);           // le parent met à jour `messages` à la fin
  }

  return (
    <>
      {messagesOptimistes.map((m, i) => <p key={i}>{m.texte}{m.envoi && ' (envoi…)'}</p>)}
      <form action={action}><input name="texte" /><button>Envoyer</button></form>
    </>
  );
}
```

#### Boutons avec `formAction`

```jsx
<form action={enregistrer}>
  <input name="titre" />
  <button>Enregistrer</button>
  <button formAction={supprimer}>Supprimer</button>   {/* action différente pour ce bouton */}
</form>
```

#### Transitions asynchrones (`useTransition` avec fonctions async)

Depuis React 19, `startTransition` accepte une **fonction asynchrone** : c'est la base des « Actions » (pending, erreurs, mises à jour optimistes).

```jsx
const [enAttente, startTransition] = useTransition();
function enregistrer() {
  startTransition(async () => {
    const erreur = await mettreAJourNom(nom);
    if (erreur) { setErreur(erreur); return; }
    navigate('/profil');
  });
}
```

#### Réinitialisation automatique

Après une action `<form action={fn}>` **réussie**, React réinitialise les **champs non contrôlés** (équivalent de `form.reset()`). Pour conserver les valeurs, utilisez des champs **contrôlés** ou renvoyez les valeurs dans l'état (`defaultValue={etat.valeurs.email}`). Vous pouvez aussi utiliser `requestFormReset`.

### 10.8 Bibliothèques de formulaires

| Bibliothèque | Approche | Points forts |
|---|---|---|
| **React Hook Form** | Majoritairement **non contrôlé** (refs, `register`) | Très peu de re-rendus, léger, intégration avec Zod/Yup, `Controller` pour composants UI |
| **Formik** | Contrôlé, contexte | API simple, mais plus de re-rendus ; moins actif |
| **TanStack Form** | Typé, headless | Typage fort, validation fine, framework-agnostic |
| **Conform / Remix / Next** | Basé sur les Actions & FormData | Amélioration progressive, validation côté serveur partagée |
| **Zod / Valibot / Yup** | Schémas de validation | Un schéma = validation + types TypeScript |

```jsx
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';

const schema = z.object({
  email: z.string().email('E-mail invalide'),
  mdp: z.string().min(8, '8 caractères minimum'),
});

function Connexion() {
  const { register, handleSubmit, formState: { errors, isSubmitting } } = useForm({
    resolver: zodResolver(schema),
  });
  return (
    <form onSubmit={handleSubmit(async (data) => { await api.connexion(data); })}>
      <input {...register('email')} />
      {errors.email && <p role="alert">{errors.email.message}</p>}
      <input type="password" {...register('mdp')} />
      {errors.mdp && <p role="alert">{errors.mdp.message}</p>}
      <button disabled={isSubmitting}>Connexion</button>
    </form>
  );
}
```

> Réutilisez le **même schéma** côté serveur pour valider les données reçues.

### 10.9 Patterns avancés

#### Formulaire multi-étapes (« wizard »)

Un state `etape` + un state `donnees` **remonté** dans le parent ; chaque étape reçoit ses valeurs et un `onSuivant`. Conservez les données entre étapes (ne démontez pas l'état), validez à chaque étape.

#### Champs dépendants / conditionnels

```jsx
{form.pays === 'fr' && <ChampCodePostal valeur={form.cp} onChange={…} />}
// Réinitialiser les champs dépendants dans le gestionnaire de changement (pas dans un effet) :
function changerPays(pays) { setForm(f => ({ ...f, pays, region: '' })); }
```

#### Enregistrement automatique (autosave)

Combiner un état local, un `useEffect` avec **debounce**, et un nettoyage pour annuler les requêtes obsolètes (`AbortController`).

#### Performance

Un champ **contrôlé** re-rend le composant à chaque frappe. Si le formulaire est volumineux :
- isoler chaque champ dans un **composant** avec son propre state ;
- utiliser un **formulaire non contrôlé** / React Hook Form ;
- `memo` pour les sections coûteuses ; `useDeferredValue` pour les aperçus.

#### Réinitialiser par `key`

```jsx
<Formulaire key={versionFormulaire} />    {/* incrémenter versionFormulaire pour tout remettre à zéro */}
```

### 10.10 Pièges fréquents

- `value` sans `onChange` (champ figé).
- Valeur initiale `undefined`/`null` → passage non contrôlé → contrôlé.
- Utiliser `onClick` sur le bouton au lieu de `onSubmit` sur le formulaire.
- Oublier `preventDefault()` (rechargement de page) quand on n'utilise pas `action`.
- Stocker un nombre depuis `<input type="number">` sans convertir (chaînes !).
- Muter l'objet de state du formulaire.
- Ne valider que côté client.
- Oublier `name` (nécessaire pour `FormData` et le gestionnaire unique).
- `useFormStatus` appelé dans le même composant que le `<form>` (retourne toujours `pending: false`).
- `<label>` non associé au champ.

### Synthèse du chapitre 10

**Contrôlé** (state) vs **non contrôlé** (DOM + `FormData`) : choisissez selon le besoin d'interaction avec la saisie ; `checked` pour cases/radios, `value` pour le reste ; `select` et `textarea` utilisent `value` ; Valeurs de `input` = **chaînes** ; fichiers = non contrôlé ; Validation **client ET serveur**, erreurs accessibles (`aria-*`, `role="alert"`) ; React 19 : `<form action>`, **`useActionState`**, **`useFormStatus`**, **`useOptimistic`**, transitions async ; Pour les formulaires complexes : **React Hook Form** (+ **Zod**).

---

# Partie II — Hooks et architecture des composants

## 11. Hooks

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : comprendre ce qu'est un Hook, pourquoi ils existent et comment ils fonctionnent en interne ; appliquer sans erreur les **règles des Hooks** ; maîtriser **tous** les hooks intégrés de React : `useState`, `useEffect`, `useEffectEvent`, `useContext`, `useReducer`, `useRef`, `useMemo`, `useCallback`, `useLayoutEffect`, `useImperativeHandle`, `useId`, `useTransition`, `useDeferredValue`, `useSyncExternalStore`, `useInsertionEffect`, `useDebugValue`, `use`, `useActionState`, `useFormStatus`, `useOptimistic` ; savoir choisir le bon hook et éviter les erreurs classiques (dépendances, boucles infinies, valeurs obsolètes). > Ce module est découpé en deux parties : **11.A** (règles, `useState`, `useEffect`, `useEffectEvent`, `useContext`, `useReducer`) puis **11.B** (les autres hooks).

### 11.1 Qu'est-ce qu'un Hook ?

Un **Hook** est une **fonction spéciale**, dont le nom commence par `use`, qui permet à un **composant fonction** de **se « brancher »** sur des fonctionnalités de React : état, cycle de vie, contexte, références, optimisations, etc.

#### Pourquoi les Hooks ont été introduits (React 16.8, 2019)

Avant, partager de la logique avec état entre composants imposait des **HOC** et des **render props** (« wrapper hell »), et les **classes** posaient des problèmes :
- logique **éclatée** entre `componentDidMount`, `componentDidUpdate`, `componentWillUnmount` ;
- logique **non liée** regroupée dans les mêmes méthodes ;
- confusion autour de `this` ;
- difficulté d'optimisation et de compilation.

Les Hooks permettent de **regrouper la logique par préoccupation** (et non par moment du cycle de vie) et de la **réutiliser** via des **hooks personnalisés**.

#### Catégories

| Catégorie | Hooks |
|---|---|
| **État** | `useState`, `useReducer` |
| **Contexte** | `useContext` |
| **Refs** | `useRef`, `useImperativeHandle` |
| **Effets** | `useEffect`, `useLayoutEffect`, `useInsertionEffect`, `useEffectEvent` |
| **Performance** | `useMemo`, `useCallback`, `useTransition`, `useDeferredValue` |
| **Autres** | `useId`, `useDebugValue`, `useSyncExternalStore` |
| **Ressources / Actions (React 19)** | `use`, `useActionState`, `useOptimistic`, `useFormStatus` (de `react-dom`) |

### 11.2 Comment les Hooks fonctionnent (modèle mental)

React conserve, **pour chaque composant monté**, une **liste ordonnée** (liste chaînée) de « cases mémoire » : une par appel de Hook. À chaque rendu, React **rejoue** les appels **dans le même ordre** et associe chaque appel à sa case **par sa position**.

```jsx
function Exemple() {
  const [a, setA] = useState(0);      // case 1
  const [b, setB] = useState('x');    // case 2
  const ref = useRef(null);           // case 3
  useEffect(() => {}, [a]);           // case 4
}
```

Cela explique les règles ci-dessous : si l'ordre ou le nombre d'appels varie, **les cases sont décalées** et l'état est attribué au mauvais hook.

### 11.3 Règles des Hooks

1. **Appelez les Hooks uniquement au niveau supérieur** d'un composant ou d'un hook personnalisé : **jamais** dans des conditions, des boucles, des fonctions imbriquées, des `try/catch/finally`, après un `return` anticipé, ni dans des gestionnaires d'événements.
2. **Appelez les Hooks uniquement depuis** des **composants fonctions React** ou des **hooks personnalisés** (pas depuis des fonctions JavaScript ordinaires ni des classes).
3. **Les hooks personnalisés** doivent commencer par **`use`** (convention que le linter exploite).

```jsx
// ❌ Conditionnel
if (connecte) { const [x, setX] = useState(0); }

// ❌ Après un return anticipé
if (chargement) return <Spinner />;
const [x, setX] = useState(0);

// ❌ Dans une boucle / callback
liste.forEach(() => useState(0));
onClick={() => { const v = useContext(Ctx); }}

// ✅ Toujours au niveau supérieur ; mettre la condition DANS le hook ou après
const [x, setX] = useState(0);
if (chargement) return <Spinner />;
```

> Exception notable : **`use`** (React 19) **peut** être appelé conditionnellement et dans des boucles (voir 11.B).

**Linter** : `eslint-plugin-react-hooks` applique `rules-of-hooks` (erreur) et `exhaustive-deps` (avertissement). Activez-les systématiquement.

---

**Partie 11.A — Les hooks d'état, d'effet et de contexte**

### 11.4 `useState`

Détaillé au chapitre 6. Rappel de la signature :

```jsx
const [etat, setEtat] = useState(initial);          // valeur
const [etat, setEtat] = useState(() => initial());  // initialisation paresseuse
setEtat(valeur);                                     // remplacement
setEtat(prev => nouveau);                            // mise à jour fonctionnelle
```

Points clés : instantané, batching, immutabilité, bail-out via `Object.is`.

### 11.5 `useEffect`

#### 11.5.1 Définition et philosophie

`useEffect` permet de **synchroniser un composant avec un système externe** : serveur, API du navigateur (`document.title`, `localStorage`, `IntersectionObserver`), bibliothèque non-React (carte, graphique), WebSocket, minuteur, etc.

> Un **effet** n'est **pas** un « événement de cycle de vie ». Pensez **synchronisation** : *« à chaque fois que ces valeurs changent, mets le système externe en accord avec elles, et sais comment le défaire »*.

```jsx
useEffect(() => {
  // 1. SETUP : démarre la synchronisation
  const connexion = creerConnexion(serveur, salon);
  connexion.connecter();

  return () => {
    // 2. CLEANUP : arrête proprement la synchronisation
    connexion.deconnecter();
  };
}, [serveur, salon]);   // 3. DÉPENDANCES : quand re-synchroniser
```

#### 11.5.2 Cycle de vie d'un effet

Chaque effet décrit **un cycle** « démarrer → arrêter ». React :

1. **Monte** le composant → exécute le **setup**.
2. À chaque **nouveau rendu où une dépendance a changé** → exécute le **cleanup** de l'effet précédent (avec **les anciennes valeurs**), puis le **setup** avec les **nouvelles valeurs**.
3. Au **démontage** → exécute le **cleanup** final.

Chronologie pour `salon` passant de `"général"` à `"voyage"` :

```
rendu(general) → commit → setup(general)
rendu(voyage)  → commit → cleanup(general) → setup(voyage)
démontage      →          cleanup(voyage)
```

#### 11.5.3 Le tableau de dépendances

| Forme | Quand l'effet s'exécute |
|---|---|
| `useEffect(fn)` | Après **chaque** rendu |
| `useEffect(fn, [])` | **Au montage** seulement (cleanup au démontage) |
| `useEffect(fn, [a, b])` | Au montage, puis à chaque fois que `a` ou `b` change (comparaison `Object.is`) |

##### Valeurs réactives

Sont **réactives** : les **props**, le **state**, et toute variable/fonction **déclarée dans le corps du composant** (elles sont recréées à chaque rendu). **Toute valeur réactive lue dans l'effet doit figurer dans les dépendances** (le linter le vérifie). Ne sont **pas** réactives : les variables **hors composant** (module), les **refs** (`ref.current` n'est pas réactif), les setters d'état et `dispatch` (stables).

> Vous **ne choisissez pas** les dépendances : elles sont **déterminées par le code** de l'effet. Si une dépendance ne vous convient pas, modifiez **le code** (déplacer la valeur hors du composant, la dériver autrement, ou utiliser `useEffectEvent`), jamais le linter.

##### Dépendances de type objet/fonction : le piège de la référence

```jsx
function Salon({ id }) {
  const options = { serveur: 'x', id };        // NOUVEL objet à chaque rendu !
  useEffect(() => { connecter(options); }, [options]);   // ❌ se relance à CHAQUE rendu
}

// ✅ Déplacer la création DANS l'effet et dépendre des primitives
useEffect(() => {
  const options = { serveur: 'x', id };
  const c = connecter(options);
  return () => c.fermer();
}, [id]);
```

Solutions : primitives en dépendances ; créer l'objet/la fonction **dans** l'effet ; la déplacer **hors** du composant si elle est constante ; `useMemo`/`useCallback` en dernier recours.

#### 11.5.4 Quand l'effet s'exécute-t-il ?

- **Après** que React a mis à jour le DOM **et** que le navigateur a **peint** l'écran (généralement).
- Si l'effet est la conséquence d'une **interaction discrète** (clic), React peut l'exécuter **avant la peinture**.
- Pour mesurer/modifier le layout **avant la peinture** (éviter un scintillement) : `useLayoutEffect` (11.B).
- Les effets **ne s'exécutent pas** pendant le rendu **côté serveur**.

#### 11.5.5 Le cleanup en détail

Le nettoyage doit **annuler** ce que le setup a fait : se désabonner, `clearTimeout`, `removeEventListener`, fermer connexion, annuler requête.

```jsx
// Abonnement DOM
useEffect(() => {
  function onKey(e) { if (e.key === 'Escape') fermer(); }
  window.addEventListener('keydown', onKey);
  return () => window.removeEventListener('keydown', onKey);
}, [fermer]);

// Minuteur
useEffect(() => {
  const id = setInterval(() => setSecondes(s => s + 1), 1000);   // forme fonctionnelle : pas de dépendance à `secondes`
  return () => clearInterval(id);
}, []);

// Animation / librairie externe
useEffect(() => {
  const carte = new Carte(ref.current);
  carte.setZoom(zoom);
  return () => carte.detruire();
}, [zoom]);
```

#### 11.5.6 Récupération de données et conditions de course

Cas classique : une requête qui dépend d'une prop. Si la prop change rapidement, les **réponses peuvent arriver dans le désordre** (*race condition*). Solutions : **drapeau « ignorer »** ou **`AbortController`**.

```jsx
useEffect(() => {
  let ignorer = false;
  const controleur = new AbortController();

  async function charger() {
    try {
      const rep = await fetch(`/api/users/${id}`, { signal: controleur.signal });
      const json = await rep.json();
      if (!ignorer) setUtilisateur(json);
    } catch (e) {
      if (e.name !== 'AbortError' && !ignorer) setErreur(e);
    }
  }
  charger();

  return () => { ignorer = true; controleur.abort(); };
}, [id]);
```

> En pratique, préférez **TanStack Query / SWR** ou les mécanismes du **framework** (loaders, Server Components, `use` + Suspense) : cache, déduplication, retries, revalidation (chapitre 25).

#### 11.5.7 StrictMode : le « double montage » en développement

En développement, `StrictMode` exécute **setup → cleanup → setup** au montage initial pour vérifier que votre cleanup est correct. Si l'effet se comporte mal (double requête, double abonnement), **c'est un bug** à corriger par un **cleanup symétrique**, pas à contourner avec un drapeau « déjà exécuté ».

#### 11.5.8 « Vous n'avez peut-être pas besoin d'un effet »

Les effets sont une **échappatoire** pour sortir de React. Les cas où **il ne faut pas** en utiliser :

| Besoin | Mauvaise approche | Bonne approche |
|---|---|---|
| **Transformer des données** pour l'affichage | `useEffect` + `setState` | **Calculer pendant le rendu** (éventuellement `useMemo`) |
| **Réagir à une action utilisateur** | Effet qui observe un state | **Gestionnaire d'événement** |
| **Réinitialiser un état** quand une prop change | Effet qui appelle `setState` | **`key`** sur le composant |
| **Ajuster un état** partiel en fonction d'une prop | Effet | Calcul dérivé, ou ajustement **pendant le rendu** |
| **Chaîner** des mises à jour d'état | Effets en cascade | Calculer dans **un seul gestionnaire** |
| **Notifier le parent** d'un changement | Effet qui appelle `onChange` | Appeler `onChange` **dans le gestionnaire** (ou remonter l'état) |
| **Envoyer une requête POST** suite à un clic | Effet | **Gestionnaire** |
| **Initialiser l'application** (une fois) | Effet `[]` | Code au niveau module ou garde de module |
| **S'abonner à un store externe** | Effet + state | **`useSyncExternalStore`** |
| **Récupérer des données** | Effet nu | Bibliothèque de requêtes / framework |

```jsx
// ❌ État redondant + effet
const [nomComplet, setNomComplet] = useState('');
useEffect(() => { setNomComplet(`${prenom} ${nom}`); }, [prenom, nom]);

// ✅ Calcul pendant le rendu
const nomComplet = `${prenom} ${nom}`;
```

```jsx
// ❌ Effet pour réagir à un clic
useEffect(() => { if (achete) { api.acheter(); } }, [achete]);

// ✅ Gestionnaire
function handleAcheter() { api.acheter(); }
```

#### 11.5.9 Erreurs fréquentes

- **Boucle infinie** : l'effet modifie un état qui figure dans ses dépendances (ou une dépendance est recréée à chaque rendu).
- **Valeur obsolète (« stale closure »)** : dépendance omise → l'effet lit d'anciennes valeurs.
- **Cleanup oublié** : fuites (écouteurs, intervalles, connexions).
- **Effet `async`** : `useEffect(async () => …)` est invalide (la fonction retourne une promesse, pas un cleanup). Définir une fonction `async` **à l'intérieur** et l'appeler.
- **Supprimer des dépendances pour « faire taire » le linter** (`// eslint-disable-line`).

#### 11.5.10 Exemple : synchroniser `document.title` et `localStorage`

```jsx
useEffect(() => { document.title = `(${nonLus}) Messagerie`; }, [nonLus]);

useEffect(() => { localStorage.setItem('theme', theme); }, [theme]);
```

### 11.6 `useEffectEvent` (React 19.2)

#### Le problème

Certains effets doivent **lire la dernière valeur** d'une variable **sans** que cette variable **relance** l'effet.

```jsx
function Salon({ id, theme }) {
  useEffect(() => {
    const c = creerConnexion(id);
    c.on('connecte', () => afficherNotification('Connecté !', theme));   // utilise `theme`
    c.connecter();
    return () => c.deconnecter();
  }, [id, theme]);   // ❌ changer le thème RECONNECTE le salon : indésirable
}
```

#### La solution : extraire une « fonction d'événement d'effet »

```jsx
import { useEffect, useEffectEvent } from 'react';

function Salon({ id, theme }) {
  const onConnecte = useEffectEvent(() => {
    afficherNotification('Connecté !', theme);   // voit TOUJOURS le dernier `theme`
  });

  useEffect(() => {
    const c = creerConnexion(id);
    c.on('connecte', () => onConnecte());
    c.connecter();
    return () => c.deconnecter();
  }, [id]);   // `onConnecte` n'est PAS une dépendance
}
```

#### Règles

- Une *Effect Event* **ne doit être appelée que depuis l'intérieur d'un effet** (ou d'une autre Effect Event), **jamais** pendant le rendu ni transmise à d'autres composants/hooks.
- Elle **n'est pas déclarée** dans les dépendances de l'effet (le plugin ESLint à jour le sait).
- Elle exprime : *« cette partie du code est un **événement** (non réactif), même si elle vit dans un **effet** »*.
- À réserver aux cas où la logique est **conceptuellement un événement** ; ne l'utilisez pas pour masquer une vraie dépendance.

### 11.7 `useContext`

Lit la valeur du **contexte** le plus proche au-dessus dans l'arbre.

```jsx
const theme = useContext(ThemeContext);
```

- Le composant est **re-rendu** chaque fois que la valeur du contexte change (comparaison `Object.is`).
- Si aucun fournisseur n'existe au-dessus, la **valeur par défaut** de `createContext(defaut)` est utilisée.
- Peut se lire **après** un `return` conditionnel via **`use(Contexte)`** (React 19).
- Voir le **chapitre 13** pour la création, les fournisseurs, les optimisations et les patterns.

### 11.8 `useReducer`

#### Définition

`useReducer` gère un **état complexe** via une **fonction de réduction** (*reducer*) qui calcule **le nouvel état à partir de l'état courant et d'une action**. C'est `useState` + une **logique de transition centralisée**.

```jsx
const [etat, dispatch] = useReducer(reducer, etatInitial, init?);
```

- `reducer(etat, action) → nouvelEtat` : **pure**, **sans effet de bord**, ne **mute pas** `etat`.
- `dispatch(action)` : **envoie** une action (convention : objet `{ type, ...donnees }`).
- `init(etatInitial)` (facultatif) : calcul **paresseux** de l'état initial.
- `dispatch` est **stable** (même identité entre les rendus) : on peut l'omettre des dépendances.

#### Exemple complet : liste de tâches

```jsx
const initial = { taches: [], filtre: 'toutes' };

function reducer(etat, action) {
  switch (action.type) {
    case 'ajouter':
      return { ...etat, taches: [...etat.taches, { id: action.id, titre: action.titre, faite: false }] };
    case 'basculer':
      return { ...etat, taches: etat.taches.map(t => t.id === action.id ? { ...t, faite: !t.faite } : t) };
    case 'supprimer':
      return { ...etat, taches: etat.taches.filter(t => t.id !== action.id) };
    case 'filtrer':
      return { ...etat, filtre: action.filtre };
    default:
      throw new Error(`Action inconnue : ${action.type}`);   // détecter les fautes de frappe
  }
}

function TodoApp() {
  const [etat, dispatch] = useReducer(reducer, initial);
  return (
    <>
      <button onClick={() => dispatch({ type: 'ajouter', id: crypto.randomUUID(), titre: 'Nouvelle' })}>
        Ajouter
      </button>
      {etat.taches.map(t => (
        <li key={t.id} onClick={() => dispatch({ type: 'basculer', id: t.id })}>{t.titre}</li>
      ))}
    </>
  );
}
```

#### Initialisation paresseuse

```jsx
function init(utilisateurId) { return { taches: chargerTaches(utilisateurId), filtre: 'toutes' }; }
const [etat, dispatch] = useReducer(reducer, utilisateurId, init);
```

#### `useState` ou `useReducer` ?

| Critère | `useState` | `useReducer` |
|---|---|---|
| Quantité de code | Moindre pour cas simples | Plus verbeux au départ |
| Mises à jour **dispersées** dans plusieurs gestionnaires | Répétitif et risqué | **Centralisé** |
| Logique de transition complexe (plusieurs champs liés) | Difficile | **Adapté** |
| Valeur suivante dépend de la précédente de manière non triviale | Possible | **Naturel** |
| Testabilité de la logique | Liée au composant | Reducer **pur**, testable isolément |
| Débogage (journalisation des actions) | Moins direct | **Facile** (voir toutes les actions) |
| Partage via Context (dispatch stable) | Moyen | **Excellent** |

#### Règles de reducers

1. **Purs** : mêmes entrées → même sortie ; pas de requêtes, pas de timers.
2. **Immuables** : retourner un **nouvel objet** ; ne jamais muter `etat` (ou utiliser **`useImmerReducer`**).
3. **Une action = une interaction** utilisateur décrite (`'formulaire_reinitialise'`) plutôt qu'une série de mises à jour techniques.
4. En StrictMode, le reducer est exécuté **deux fois** : une impureté se verra.

#### Pattern Context + Reducer (état partagé sans bibliothèque)

```jsx
const TachesContext = createContext(null);
const TachesDispatchContext = createContext(null);

function TachesProvider({ children }) {
  const [taches, dispatch] = useReducer(reducer, []);
  return (
    <TachesContext value={taches}>
      <TachesDispatchContext value={dispatch}>{children}</TachesDispatchContext>
    </TachesContext>
  );
}
const useTaches = () => useContext(TachesContext);
const useTachesDispatch = () => useContext(TachesDispatchContext);
```

Séparer l'**état** du **dispatch** évite des rendus inutiles pour les composants qui ne font qu'envoyer des actions.

### 11.9 Comparaison synthétique des hooks d'état et d'effet

| Besoin | Hook |
|---|---|
| Mémoriser une valeur qui déclenche un rendu | `useState` |
| Logique d'état complexe/centralisée | `useReducer` |
| Se synchroniser avec un système externe | `useEffect` |
| Lire la dernière valeur dans un effet sans le relancer | `useEffectEvent` |
| Lire des données partagées de l'arbre | `useContext` |
| Mesurer/modifier le DOM **avant** la peinture | `useLayoutEffect` |
| S'abonner à une source externe lisible de façon synchrone | `useSyncExternalStore` |

### 11.10 `useRef`

#### Définition

`useRef(valeurInitiale)` retourne un **objet mutable unique** `{ current: valeurInitiale }` dont l'**identité est stable** pendant toute la vie du composant. **Modifier `ref.current` ne déclenche pas de nouveau rendu.**

```jsx
const ref = useRef(0);
ref.current = ref.current + 1;    // pas de rendu
```

#### Deux usages

**1. Référencer un nœud DOM**

```jsx
function Champ() {
  const inputRef = useRef(null);
  useEffect(() => { inputRef.current.focus(); }, []);   // `current` est renseigné après le commit
  return <input ref={inputRef} />;
}
```

**2. Stocker une valeur mutable « hors rendu »** (identifiant de minuteur, instance d'une librairie, valeur précédente, drapeau)

```jsx
function Chrono() {
  const [t, setT] = useState(0);
  const idRef = useRef(null);
  const demarrer = () => { idRef.current = setInterval(() => setT(x => x + 1), 1000); };
  const arreter  = () => clearInterval(idRef.current);
}

// Valeur précédente
function usePrecedent(valeur) {
  const ref = useRef();
  useEffect(() => { ref.current = valeur; });
  return ref.current;       // valeur du rendu précédent
}
```

#### `useRef` vs `useState`

| | `useRef` | `useState` |
|---|---|---|
| Retourne | `{ current }` | `[valeur, setter]` |
| Modifier déclenche un rendu | ❌ | ✅ |
| Mutable | ✅ (`ref.current = …`) | ❌ (immuable) |
| Lisible pendant le rendu | ❌ (déconseillé) | ✅ |
| Usage | Infos **non affichées**, accès DOM | Données qui **influencent l'affichage** |

#### Règles

- **Ne lisez ni n'écrivez `ref.current` pendant le rendu** (sauf initialisation paresseuse) : cela rend le composant impur et imprévisible.
- Lisez/écrivez dans des **gestionnaires d'événements** ou des **effets**.
- **Initialisation paresseuse** d'un objet coûteux :

```jsx
const ref = useRef(null);
if (ref.current === null) ref.current = new ObjetCouteux();   // seule exception admise
```

#### Refs de callback

Une fonction peut servir de `ref`. Elle est appelée avec le nœud au montage ; en **React 19**, elle peut **retourner une fonction de nettoyage** (appelée au démontage). Utile pour des listes de refs ou un observateur.

```jsx
<li ref={(noeud) => {
  const observateur = new IntersectionObserver(…);
  observateur.observe(noeud);
  return () => observateur.disconnect();       // React 19
}} />
```

> Les refs de callback **inline** sont recréées à chaque rendu (cleanup + setup à chaque fois) : mémoïsez-les (`useCallback`) si c'est coûteux.

Détails complets au **chapitre 14**.

### 11.11 `useMemo`

#### Définition

`useMemo(calcul, dependances)` **mémorise le résultat** d'un calcul entre les rendus ; il n'est **recalculé** que si une dépendance change.

```jsx
const visibles = useMemo(() => filtrer(taches, filtre), [taches, filtre]);
```

#### Usages légitimes

1. **Éviter un calcul réellement coûteux** (le mesurer : console.time > ~1 ms de façon notable).
2. **Stabiliser la référence** d'un objet/tableau passé à un composant **mémoïsé** (`memo`) ou utilisé comme **dépendance** d'un hook.
3. Éviter de recréer une valeur qui **relancerait un effet**.

```jsx
const options = useMemo(() => ({ langue, devise }), [langue, devise]);
<Tableau options={options} />       // Tableau est enveloppé par memo
```

#### Règles et limites

- Le calcul doit être **pur** ; en StrictMode il est exécuté **deux fois** en dev.
- `useMemo` est une **optimisation de performance**, **pas une garantie sémantique** : React peut **jeter le cache** (ex. hors écran, remontage, évolutions futures). Votre code doit fonctionner **sans** lui.
- Le coût de la comparaison des dépendances + mémoire n'est pas nul : **ne mémoïsez pas par défaut**.
- Ne **pas** mémoïser quand le calcul est trivial.
- Peut être **sauté** par le **React Compiler** qui mémoïse automatiquement.

### 11.12 `useCallback`

#### Définition

`useCallback(fn, dependances)` **mémorise la fonction elle-même** (même référence tant que les dépendances sont identiques). Équivalent à `useMemo(() => fn, deps)`.

```jsx
const supprimer = useCallback((id) => {
  setTaches(prev => prev.filter(t => t.id !== id));     // forme fonctionnelle : pas de dépendance à `taches`
}, []);

<TodoItem onSupprimer={supprimer} />     // TodoItem est enveloppé par memo
```

#### Quand l'utiliser

- Passer une fonction à un composant **`memo`** pour ne pas casser sa mémoïsation.
- Fonction utilisée comme **dépendance** d'un `useEffect` / `useMemo` pour éviter de relancer l'effet.
- Fonction passée à un hook personnalisé qui en dépend.

#### Quand ne pas l'utiliser

- Fonctions passées à des éléments natifs ou à des composants non mémoïsés : **aucun gain**.
- Partout « par précaution » : cela alourdit le code sans bénéfice mesuré.

> Astuce : réduisez les dépendances avec la **forme fonctionnelle** de `setState` ou un **reducer** ; sinon l'identité change et `useCallback` perd tout intérêt.

### 11.13 `useLayoutEffect`

Identique à `useEffect` dans sa forme, mais s'exécute **de façon synchrone après les mutations du DOM et avant la peinture** du navigateur. React **attend** la fin de l'effet (et de ses éventuelles mises à jour d'état) avant de laisser le navigateur peindre.

#### Quand l'utiliser

- **Mesurer** un élément (`getBoundingClientRect`, `offsetHeight`) puis **ajuster** l'affichage (position d'un tooltip, hauteur) **sans scintillement**.
- Restaurer une position de défilement.

```jsx
function Tooltip({ ancre, children }) {
  const ref = useRef(null);
  const [haut, setHaut] = useState(0);
  useLayoutEffect(() => {
    const { height } = ref.current.getBoundingClientRect();
    setHaut(height);                                    // recalcul AVANT la peinture
  }, [children]);
  return <div ref={ref} style={{ top: -haut }}>{children}</div>;
}
```

#### Précautions

- **Bloque la peinture** : à utiliser **uniquement** si nécessaire (sinon `useEffect`).
- N'a **aucun effet côté serveur** (le code ne s'exécute pas) : prévoir un rendu initial cohérent.
- Évitez les mises à jour d'état coûteuses à l'intérieur.

### 11.14 `useImperativeHandle`

#### Définition

Personnalise la **valeur exposée** à un parent via une `ref` : au lieu d'exposer le nœud DOM complet, on expose une **API restreinte** (`focus`, `scrollIntoView`, `reset`…).

```jsx
function ChampRiche({ ref }) {                         // React 19 : `ref` est une prop
  const inputRef = useRef(null);
  useImperativeHandle(ref, () => ({
    focus()  { inputRef.current.focus(); },
    vider()  { inputRef.current.value = ''; },
  }), []);
  return <input ref={inputRef} />;
}

function Parent() {
  const ref = useRef(null);
  return (
    <>
      <ChampRiche ref={ref} />
      <button onClick={() => ref.current.focus()}>Focus</button>
    </>
  );
}
```

> Avant React 19, il fallait envelopper le composant dans `forwardRef`. N'utilisez `useImperativeHandle` que pour des **actions impératives** (focus, défilement, lecture/pause) ; pour tout le reste, utilisez des **props**.

### 11.15 `useId`

Génère un **identifiant unique et stable**, **identique côté serveur et client** (évite les erreurs d'hydratation). Idéal pour relier `label` ↔ `input`, ou les attributs `aria-*`.

```jsx
function Champ({ label }) {
  const id = useId();
  return (
    <>
      <label htmlFor={id}>{label}</label>
      <input id={id} aria-describedby={`${id}-aide`} />
      <p id={`${id}-aide`}>…</p>
    </>
  );
}
```

- **Ne l'utilisez pas pour les `key`** d'une liste (utilisez des identifiants issus des données).
- Ne l'utilisez pas comme sélecteur CSS (le format contient des caractères spéciaux et peut changer d'une version à l'autre).
- Un appel par **élément racine** ; dérivez des suffixes pour les sous-éléments.
- `identifierPrefix` de `createRoot`/`hydrateRoot` évite les collisions entre plusieurs roots.

### 11.16 `useTransition`

#### Définition

Permet de marquer une mise à jour d'état comme **transition** (**non urgente**, interruptible), pour que l'interface reste **réactive** pendant que le rendu lourd se prépare.

```jsx
const [enAttente, startTransition] = useTransition();

function choisirOnglet(nom) {
  startTransition(() => {
    setOnglet(nom);                 // rendu potentiellement lent, interruptible
  });
}

return (
  <>
    <button onClick={() => choisirOnglet('posts')}>Posts</button>
    {enAttente && <Spinner />}
    <Contenu onglet={onglet} />
  </>
);
```

#### Fonctionnement

- Les mises à jour **à l'intérieur** de `startTransition` ont une **priorité basse** : si l'utilisateur déclenche une action **urgente** (frappe, clic), React **abandonne** le rendu en cours et traite l'urgent d'abord.
- Une transition **n'affiche pas** de fallback Suspense **déjà visible** : l'ancienne interface reste à l'écran (avec `enAttente = true`) jusqu'à ce que la nouvelle soit prête.
- Depuis React 19, la fonction passée peut être **asynchrone** (Actions) : `enAttente` reste `true` pendant toute l'exécution. ⚠ Les mises à jour d'état effectuées **après un `await`** doivent être à nouveau enveloppées dans `startTransition`.

#### Limites

- **Ne pas** l'utiliser pour **contrôler la valeur d'un `<input>`** (la saisie doit rester urgente).
- Elle ne s'applique qu'aux **mises à jour d'état**, pas au code synchrone de la fonction passée.
- `startTransition` (importé de `react`) existe aussi **sans** `isPending`, pour les bibliothèques.

### 11.17 `useDeferredValue`

#### Définition

Retourne une **version « retardée »** d'une valeur. Pendant une mise à jour urgente, React réutilise l'**ancienne valeur** ; ensuite, **en arrière-plan**, il re-rend avec la nouvelle (interruptible).

```jsx
function Recherche() {
  const [requete, setRequete] = useState('');
  const requeteDifferee = useDeferredValue(requete);
  const obsolete = requete !== requeteDifferee;

  return (
    <>
      <input value={requete} onChange={e => setRequete(e.target.value)} />   {/* reste fluide */}
      <div style={{ opacity: obsolete ? 0.5 : 1 }}>
        <ResultatsLourds requete={requeteDifferee} />   {/* memo requis pour éviter des rendus inutiles */}
      </div>
    </>
  );
}
```

- `useDeferredValue(valeur, valeurInitiale?)` : le second argument (React 19) sert de valeur au **premier rendu** avant de basculer vers `valeur`.
- Pour que ce soit utile, le composant coûteux doit être **`memo`** (afin qu'il ne se re-rende pas avec l'ancienne valeur identique).
- **Différence avec le debounce** : pas de délai fixe, pas de temps mort inutile ; React s'adapte aux performances de l'appareil et le rendu est **interruptible**. Le debounce reste utile pour **limiter les requêtes réseau**.

#### `useTransition` ou `useDeferredValue` ?

| | `useTransition` | `useDeferredValue` |
|---|---|---|
| Vous contrôlez | Le **code qui met à jour** l'état | Une **valeur reçue** (prop, state) |
| Fournit `isPending` | ✅ | ❌ (comparer valeur et valeur différée) |
| Cas typique | Navigation, changement d'onglet | Filtrage/recherche, valeur venant d'un parent ou d'une bibliothèque |

### 11.18 `useSyncExternalStore`

#### Définition

Permet de **s'abonner à une source de données externe** (store, API navigateur) de façon **sûre avec le rendu concurrent** (pas de « tearing » : incohérence visuelle entre composants).

```jsx
const valeur = useSyncExternalStore(subscribe, getSnapshot, getServerSnapshot?);
```

- `subscribe(callback)` : s'abonne, retourne une fonction de désabonnement.
- `getSnapshot()` : retourne la valeur courante ; **doit retourner la même référence** tant que les données n'ont pas changé (sinon boucle infinie).
- `getServerSnapshot()` : valeur pour le **rendu serveur et l'hydratation**.

```jsx
function useEnLigne() {
  return useSyncExternalStore(
    (cb) => {
      window.addEventListener('online', cb);
      window.addEventListener('offline', cb);
      return () => { window.removeEventListener('online', cb); window.removeEventListener('offline', cb); };
    },
    () => navigator.onLine,
    () => true                                   // valeur côté serveur
  );
}
```

> À réserver aux **auteurs de bibliothèques** (Redux, Zustand… l'utilisent en interne) et aux sources externes mutables (`matchMedia`, `navigator.onLine`, `localStorage` avec événement `storage`).

### 11.19 `useInsertionEffect`

S'exécute **avant** toute mutation du DOM par React (donc **avant** `useLayoutEffect`). Réservé aux **bibliothèques CSS-in-JS** qui doivent **injecter des règles `<style>`** avant le calcul du layout.

- Ne peut **pas** mettre à jour l'état.
- Les **refs** ne sont pas encore attachées.
- Sans usage de votre part dans une application classique.

### 11.20 `useDebugValue`

Ajoute une **étiquette** visible dans les **React DevTools** pour un **hook personnalisé**.

```jsx
function useEnLigne() {
  const enLigne = useSyncExternalStore(…);
  useDebugValue(enLigne ? 'En ligne' : 'Hors ligne');
  return enLigne;
}
// Avec formatage différé : useDebugValue(date, d => d.toISOString());
```

À réserver aux hooks **partagés** (bibliothèques).

### 11.21 Hooks et API de React 19

#### 11.21.1 `use`

`use(ressource)` **lit** la valeur d'une **ressource** : une **Promise** ou un **Context**. Particularités :

- **Peut être appelé dans des conditions et des boucles** (contrairement aux autres hooks), mais **toujours dans un composant ou un hook** et **pas dans un bloc `try/catch`**.
- **Avec une Promise** : suspend le composant (affiche le fallback `<Suspense>` le plus proche) jusqu'à résolution ; une promesse **rejetée** remonte au plus proche **Error Boundary**.
- **Avec un Context** : équivaut à `useContext`, mais utilisable après un retour anticipé.

```jsx
import { use, Suspense } from 'react';

function Commentaires({ promesseCommentaires }) {
  const commentaires = use(promesseCommentaires);              // suspend tant que non résolue
  return commentaires.map(c => <p key={c.id}>{c.texte}</p>);
}

function Page({ id }) {
  const promesse = chargerCommentaires(id);     // ⚠ idéalement créée côté serveur ou mise en cache
  return (
    <Suspense fallback={<Squelette />}>
      <Commentaires promesseCommentaires={promesse} />
    </Suspense>
  );
}

function Panneau({ afficher }) {
  if (!afficher) return null;
  const theme = use(ThemeContext);              // ✅ lecture conditionnelle de contexte
  return <div className={theme} />;
}
```

> **Attention** : ne créez pas une **nouvelle** promesse à chaque rendu d'un composant client (elle serait recréée à l'infini). Passez-la depuis un **Server Component**, ou utilisez un **cache** (TanStack Query, `cache`, bibliothèque compatible Suspense).

#### 11.21.2 `useActionState`

Gère l'**état retourné par une action** (souvent d'un formulaire) : `const [etat, action, enAttente] = useActionState(fn, etatInitial)`. Voir le **chapitre 10**.

#### 11.21.3 `useFormStatus` (`react-dom`)

Lit l'état du `<form>` **parent** : `{ pending, data, method, action }`. Voir le **chapitre 10**.

#### 11.21.4 `useOptimistic`

Affiche un **état optimiste** temporaire pendant une action asynchrone, puis **revient** à l'état réel. Voir le **chapitre 10**.

#### 11.21.5 Autres nouveautés utiles liées aux hooks

- `ref` comme prop ; cleanup des **refs de callback**.
- `<Context value>` à la place de `<Context.Provider>`.
- `useDeferredValue` avec valeur initiale.
- `useEffectEvent` (19.2), composant `<Activity>` (19.2).
- **`cache`** (Server Components) : mémoïse une fonction asynchrone **le temps d'une requête serveur**.
- **React Compiler** : mémoïsation automatique (chapitre 16).

### 11.22 Tableau de décision : quel hook choisir ?

| Question | Réponse |
|---|---|
| Une donnée change et l'affichage doit suivre ? | `useState` / `useReducer` |
| Une valeur se calcule à partir d'autres ? | **Rien** : calcul pendant le rendu |
| Calcul réellement lourd ou référence à stabiliser ? | `useMemo` |
| Fonction stable à passer à un enfant `memo` / dépendance ? | `useCallback` |
| Besoin de communiquer avec le DOM / une lib externe ? | `useRef` + `useEffect` |
| Mesurer le DOM avant peinture ? | `useLayoutEffect` |
| S'abonner à un store/navigateur ? | `useSyncExternalStore` |
| Réagir à un clic ? | **Gestionnaire d'événement** |
| Garder l'interface fluide pendant un rendu lourd ? | `useTransition` / `useDeferredValue` |
| Identifiant d'accessibilité ? | `useId` |
| Partager une valeur dans un sous-arbre ? | `useContext` / `use(Context)` |
| Lire une promesse dans le rendu ? | `use(promesse)` + `Suspense` |
| État d'un formulaire/action ? | `useActionState`, `useFormStatus`, `useOptimistic` |
| Exposer une API impérative à un parent ? | `useImperativeHandle` |

### 11.23 Récapitulatif : ordre d'exécution lors d'un rendu avec mise à jour

1. **Rendu** : appel du composant (et de ses hooks dans l'ordre) → `useMemo`, `useCallback`, `useReducer` (calcul) sont évalués.
2. **Commit** : React met à jour le DOM ; les **refs** sont attachées.
3. **`useInsertionEffect`** (cleanup puis setup).
4. **`useLayoutEffect`** : cleanup des anciens effets, puis setup des nouveaux (synchrone, avant peinture).
5. **Peinture** par le navigateur.
6. **`useEffect`** : cleanup des anciens, puis setup des nouveaux.

### 11.24 Pièges fréquents

- `useRef` pour une donnée affichée → l'écran ne se met pas à jour.
- Lire/écrire `ref.current` pendant le rendu.
- `useMemo`/`useCallback` partout, sans mesure, ou avec des dépendances instables.
- `useLayoutEffect` à tort (blocage de la peinture, avertissements en SSR).
- `getSnapshot` de `useSyncExternalStore` qui retourne un **nouvel objet** à chaque appel.
- `use(promesseCrééeDansLeRendu)` dans un composant client.
- Utiliser `useId` pour des `key`.
- `startTransition` autour de la valeur d'un `<input>` contrôlé.

### Synthèse du chapitre 11

`useRef` : **valeur mutable hors rendu** ou **accès DOM** ; `useMemo` / `useCallback` : **optimisations**, jamais une obligation fonctionnelle ; `useLayoutEffect` : mesures avant peinture ; `useInsertionEffect` : CSS-in-JS ; `useTransition` / `useDeferredValue` : **prioriser** les mises à jour ; `useSyncExternalStore` : sources externes sans « tearing » ; `use` : lire **promesses et contextes**, même conditionnellement.

---

## 12. Hooks personnalisés

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : comprendre ce qu'est un hook personnalisé et ce qu'il partage (la logique, pas l'état) ; savoir en extraire, nommer, typer et tester ; connaître une bibliothèque de hooks courants et les bonnes pratiques de conception.

### 12.1 Définition

Un **hook personnalisé** (*custom hook*) est une **fonction JavaScript dont le nom commence par `use`** et qui **appelle d'autres hooks**. Il permet d'**extraire et de réutiliser de la logique avec état** (état + effets + refs…) entre plusieurs composants.

```jsx
function useEnLigne() {
  const [enLigne, setEnLigne] = useState(true);
  useEffect(() => {
    const on = () => setEnLigne(true);
    const off = () => setEnLigne(false);
    window.addEventListener('online', on);
    window.addEventListener('offline', off);
    return () => { window.removeEventListener('online', on); window.removeEventListener('offline', off); };
  }, []);
  return enLigne;
}

function BarreStatut()  { return <h1>{useEnLigne() ? '✅ En ligne' : '❌ Hors ligne'}</h1>; }
function BoutonEnvoyer() { const enLigne = useEnLigne(); return <button disabled={!enLigne}>Envoyer</button>; }
```

#### Ce qui est partagé, et ce qui ne l'est pas

- La **logique** est partagée (le code du hook).
- L'**état n'est pas partagé** : **chaque appel** du hook crée **son propre état** isolé. Deux composants qui appellent `useEnLigne()` ont chacun leur `useState`.
- Pour **partager l'état lui-même** : Context, store externe, ou remontée d'état.

### 12.2 Règles et conventions

1. Nom **`useXxx`** (le linter applique les règles de hooks aux fonctions ainsi nommées).
2. Respecte les **règles des hooks** : niveau supérieur, même ordre.
3. Une fonction qui **n'appelle aucun hook** ne doit **pas** s'appeler `useXxx` : c'est une fonction normale.
4. Un hook peut **accepter des arguments** et **retourner n'importe quoi** (valeur, tableau, objet, fonction).
5. Chaque hook doit avoir **un but précis** (principe de responsabilité unique) : `useDebounce`, pas `useTout`.
6. Un hook **re-rend** le composant qui l'appelle quand **son état interne** change.

#### Valeur de retour : tableau ou objet ?

| Forme | Avantage | Cas |
|---|---|---|
| **Tableau** `[valeur, setValeur]` | Renommage facile à l'appel (`const [a, setA] = …`) | 2-3 valeurs, à l'image de `useState` |
| **Objet** `{ data, erreur, chargement }` | Valeurs **nommées**, ordre indifférent, extensible | Plus de 3 valeurs |

### 12.3 Quand extraire un hook ?

- **Duplication** : la même combinaison `useState` + `useEffect` apparaît dans plusieurs composants.
- **Complexité** : un composant mélange affichage et logique technique (abonnements, requêtes).
- **Intention** : le nom du hook **documente** ce que fait le code (`useRaccourciClavier('Escape', fermer)`).
- **Testabilité** : isoler la logique.

> Ne créez pas de hook pour **chaque** `useEffect` : seulement pour réduire la duplication ou clarifier une **préoccupation** réelle. Évitez les hooks de « cycle de vie » génériques (`useMount`, `useEffectOnce`) qui masquent la logique de synchronisation.

### 12.4 Recueil de hooks courants

#### `useLocalStorage`

```jsx
function useLocalStorage(cle, valeurInitiale) {
  const [valeur, setValeur] = useState(() => {
    try {
      const brut = localStorage.getItem(cle);
      return brut !== null ? JSON.parse(brut) : valeurInitiale;
    } catch { return valeurInitiale; }
  });

  useEffect(() => {
    try { localStorage.setItem(cle, JSON.stringify(valeur)); } catch { /* quota, mode privé */ }
  }, [cle, valeur]);

  return [valeur, setValeur];
}
```

> En **SSR**, `localStorage` n'existe pas : la valeur initiale diffère entre serveur et client → risque d'erreur d'hydratation. Utilisez `useSyncExternalStore` ou lisez après le montage.

#### `useDebounce`

```jsx
function useDebounce(valeur, delai = 300) {
  const [debounced, setDebounced] = useState(valeur);
  useEffect(() => {
    const id = setTimeout(() => setDebounced(valeur), delai);
    return () => clearTimeout(id);
  }, [valeur, delai]);
  return debounced;
}
```

#### `useFetch` (version pédagogique)

```jsx
function useFetch(url) {
  const [etat, setEtat] = useState({ data: null, erreur: null, chargement: true });

  useEffect(() => {
    const controleur = new AbortController();
    setEtat(e => ({ ...e, chargement: true, erreur: null }));
    fetch(url, { signal: controleur.signal })
      .then(r => { if (!r.ok) throw new Error(`HTTP ${r.status}`); return r.json(); })
      .then(data => setEtat({ data, erreur: null, chargement: false }))
      .catch(e => { if (e.name !== 'AbortError') setEtat({ data: null, erreur: e, chargement: false }); });
    return () => controleur.abort();
  }, [url]);

  return etat;
}
```

> En production, préférez **TanStack Query** / **SWR** (cache, déduplication, revalidation).

#### `useToggle`

```jsx
function useToggle(initial = false) {
  const [valeur, setValeur] = useState(initial);
  const basculer = useCallback(() => setValeur(v => !v), []);
  return [valeur, basculer, setValeur];
}
```

#### `useEventListener`

```jsx
function useEventListener(cible, type, gestionnaire) {
  const dernier = useRef(gestionnaire);
  useEffect(() => { dernier.current = gestionnaire; });            // ou useEffectEvent (19.2)
  useEffect(() => {
    const el = cible?.current ?? cible ?? window;
    const ecouteur = (e) => dernier.current(e);
    el.addEventListener(type, ecouteur);
    return () => el.removeEventListener(type, ecouteur);
  }, [cible, type]);
}
```

#### `useClickOutside`

```jsx
function useClickOutside(ref, onOutside) {
  useEffect(() => {
    function handler(e) { if (ref.current && !ref.current.contains(e.target)) onOutside(e); }
    document.addEventListener('pointerdown', handler);
    return () => document.removeEventListener('pointerdown', handler);
  }, [ref, onOutside]);
}
```

#### `useMediaQuery`

```jsx
function useMediaQuery(requete) {
  return useSyncExternalStore(
    (cb) => { const m = window.matchMedia(requete); m.addEventListener('change', cb); return () => m.removeEventListener('change', cb); },
    () => window.matchMedia(requete).matches,
    () => false
  );
}
```

#### `useInterval` (Dan Abramov)

```jsx
function useInterval(rappel, delai) {
  const dernier = useRef(rappel);
  useEffect(() => { dernier.current = rappel; }, [rappel]);
  useEffect(() => {
    if (delai === null) return;
    const id = setInterval(() => dernier.current(), delai);
    return () => clearInterval(id);
  }, [delai]);
}
```

#### `usePrevious`, `useWindowSize`, `useOnScreen` (IntersectionObserver), `useCopyToClipboard`, `useAsync`, `useForm`, `useUndoRedo`… sont d'autres exemples courants ; des bibliothèques comme **usehooks-ts**, **react-use**, **ahooks** ou **@uidotdev/usehooks** en fournissent des versions éprouvées.

### 12.5 Composition de hooks

Un hook peut appeler **d'autres hooks personnalisés** :

```jsx
function useRecherche(url) {
  const [terme, setTerme] = useState('');
  const termeDebounce = useDebounce(terme, 300);
  const { data, chargement } = useFetch(`${url}?q=${encodeURIComponent(termeDebounce)}`);
  return { terme, setTerme, resultats: data ?? [], chargement };
}
```

### 12.6 Passer des gestionnaires à un hook

Si le hook appelle un **callback fourni par le composant**, ce callback change à chaque rendu. Options : **ref du dernier callback** (comme dans `useInterval`), **`useEffectEvent`**, ou exiger que l'appelant le mémoïse. N'incluez pas un callback instable dans les dépendances d'un effet.

### 12.7 Hooks et TypeScript

```tsx
function useLocalStorage<T>(cle: string, initial: T): readonly [T, React.Dispatch<React.SetStateAction<T>>] {
  const [valeur, setValeur] = useState<T>(() => {
    const brut = localStorage.getItem(cle);
    return brut ? (JSON.parse(brut) as T) : initial;
  });
  useEffect(() => { localStorage.setItem(cle, JSON.stringify(valeur)); }, [cle, valeur]);
  return [valeur, setValeur] as const;       // `as const` conserve le type tuple
}
```

### 12.8 Tester un hook

```jsx
import { renderHook, act } from '@testing-library/react';

test('useToggle bascule', () => {
  const { result } = renderHook(() => useToggle(false));
  expect(result.current[0]).toBe(false);
  act(() => result.current[1]());
  expect(result.current[0]).toBe(true);
});
```

Pour les hooks dépendant d'un contexte : option `wrapper` de `renderHook`.

### 12.9 Pièges fréquents

- Croire que deux composants partagent l'état d'un même hook.
- Nommer `useXxx` une fonction qui n'utilise aucun hook (ou l'inverse : appeler des hooks dans `fetchXxx`).
- Hook « fourre-tout » à responsabilités multiples.
- Dépendances instables (objets, fonctions inline) dans les effets internes.
- Oublier de nettoyer (abonnements, minuteurs).
- Retourner de nouveaux objets à chaque rendu quand le consommateur les utilise en dépendances.

### Synthèse du chapitre 12

Hook personnalisé = **fonction `useXxx`** qui compose des hooks ; **logique partagée, état isolé** ; Extrayez pour **clarté** et **réutilisation**, pas par principe ; Tableau pour 2-3 valeurs, **objet** au-delà ; Testez avec **`renderHook`**.

---

## 13. Context API

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : comprendre le problème résolu (prop drilling) et le fonctionnement du Context ; créer, fournir et consommer un contexte, avec les patterns recommandés ; maîtriser les implications de performance et les alternatives.

### 13.1 Le problème et la solution

Le **prop drilling** (chapitre 5) consiste à transmettre une donnée à travers de nombreux composants intermédiaires. Le **Context** permet à un composant parent de **« diffuser »** une valeur à **tous ses descendants**, **quelle que soit la profondeur**, sans la passer explicitement via les props.

Cas d'usage typiques : **thème** (clair/sombre), **langue** (i18n), **utilisateur authentifié**, **configuration**, **état de routage**, **état d'un composant composé** (Tabs, Accordion).

### 13.2 Les trois étapes

```jsx
import { createContext, useContext, useState } from 'react';

// 1. CRÉER le contexte (valeur par défaut = utilisée en l'absence de fournisseur)
const ThemeContext = createContext('clair');

// 2. FOURNIR la valeur à un sous-arbre
function App() {
  const [theme, setTheme] = useState('clair');
  return (
    <ThemeContext value={{ theme, setTheme }}>      {/* React 19 : <Context value> */}
      <Page />
    </ThemeContext>
  );
}
// Avant React 19 : <ThemeContext.Provider value={…}>…</ThemeContext.Provider>

// 3. CONSOMMER la valeur n'importe où en dessous
function Bouton() {
  const { theme, setTheme } = useContext(ThemeContext);
  return (
    <button className={`btn btn--${theme}`} onClick={() => setTheme(theme === 'clair' ? 'sombre' : 'clair')}>
      Thème : {theme}
    </button>
  );
}
```

#### Fonctionnement

- `useContext(Ctx)` lit la valeur du **fournisseur le plus proche** au-dessus de l'appelant.
- Sans fournisseur : valeur par défaut passée à `createContext`.
- Les **fournisseurs peuvent être imbriqués** : le plus proche l'emporte (utile pour **surcharger** localement, ex. thème sombre pour un panneau).
- `use(Ctx)` (React 19) lit aussi un contexte, **y compris conditionnellement**.
- Le consommateur est **re-rendu** chaque fois que la valeur change (`Object.is`), **même s'il passe par un `memo`** intermédiaire.
- `Ctx.Consumer` (ancienne API) existe mais n'est plus utilisé.
- `displayName` : `Ctx.displayName = 'Theme'` aide dans les DevTools.

### 13.3 Pattern recommandé : fournisseur + hook de consommation

```jsx
const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [utilisateur, setUtilisateur] = useState(null);

  const valeur = useMemo(() => ({
    utilisateur,
    connexion: async (email, mdp) => setUtilisateur(await api.connexion(email, mdp)),
    deconnexion: () => setUtilisateur(null),
  }), [utilisateur]);

  return <AuthContext value={valeur}>{children}</AuthContext>;
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (ctx === null) throw new Error('useAuth doit être utilisé dans <AuthProvider>');   // garde-fou
  return ctx;
}
```

Avantages : **encapsulation** (les consommateurs n'importent pas le contexte brut), **erreur explicite** si le fournisseur manque, **API** cohérente.

### 13.4 Performance : le point clé

**Tous les consommateurs** d'un contexte se **re-rendent** quand sa valeur change. Pièges et remèdes :

#### 1. Valeur objet recréée à chaque rendu du fournisseur

```jsx
<Ctx value={{ a, b }}>…</Ctx>        // ❌ nouvel objet à chaque rendu du parent → tous les consommateurs re-rendent
const valeur = useMemo(() => ({ a, b }), [a, b]);    // ✅
```

> Si le fournisseur ne se re-rend que quand l'état change réellement, ce problème est moindre ; il apparaît surtout quand le parent du fournisseur se re-rend souvent.

#### 2. Un seul contexte « fourre-tout »

Un contexte qui regroupe des données qui changent à des fréquences différentes force des rendus inutiles. **Découpez** :

```jsx
<UtilisateurContext value={utilisateur}>
  <ThemeContext value={theme}>
    <PanierContext value={panier}>…</PanierContext>
  </ThemeContext>
</UtilisateurContext>
```

#### 3. Séparer **état** et **actions**

```jsx
<EtatContext value={etat}>
  <DispatchContext value={dispatch}>{children}</DispatchContext>   {/* dispatch est stable */}
</EtatContext>
```

Les composants qui ne font que **déclencher** des actions ne se re-rendent pas quand l'état change.

#### 4. Éviter qu'un fournisseur re-rende ses enfants

Passez les enfants via **`children`** : si l'état du fournisseur change, les `children` (même référence créée plus haut) ne sont pas re-rendus (sauf consommateurs).

#### 5. Pas de sélecteur natif

`useContext` ne permet pas de s'abonner à **une partie** de la valeur. Pour des **mises à jour fines et fréquentes**, préférez **Zustand**, **Jotai**, **Redux Toolkit** ou la bibliothèque `use-context-selector`.

### 13.5 Context et mise à jour : où met-on l'état ?

Le Context **ne gère pas l'état** : il **transporte** une valeur. L'état vit dans un `useState`/`useReducer` du fournisseur (ou ailleurs).

```jsx
function ThemeProvider({ children }) {
  const [theme, setTheme] = useState(() => localStorage.getItem('theme') ?? 'clair');
  useEffect(() => { localStorage.setItem('theme', theme); document.documentElement.dataset.theme = theme; }, [theme]);
  return <ThemeContext value={useMemo(() => ({ theme, setTheme }), [theme])}>{children}</ThemeContext>;
}
```

### 13.6 Alternatives et compléments

| Besoin | Alternative |
|---|---|
| Éviter le drilling sur 2-3 niveaux | **Composition** (`children`, slots) |
| Données serveur | **TanStack Query / SWR** (pas de Context) |
| État global très dynamique | **Zustand / Jotai / Redux Toolkit** |
| Valeur lue rarement et statique (config) | Context ✅ (idéal) |
| Valeur changeant souvent, nombreux consommateurs | Store externe avec sélecteurs |

### 13.7 Contexte et composants composés

Les composants **composés** partagent un état implicite via un contexte privé :

```jsx
const OngletsContext = createContext(null);

function Onglets({ defaut, children }) {
  const [actif, setActif] = useState(defaut);
  return <OngletsContext value={{ actif, setActif }}>{children}</OngletsContext>;
}
Onglets.Bouton = function Bouton({ id, children }) {
  const { actif, setActif } = useContext(OngletsContext);
  return <button role="tab" aria-selected={actif === id} onClick={() => setActif(id)}>{children}</button>;
};
Onglets.Panneau = function Panneau({ id, children }) {
  const { actif } = useContext(OngletsContext);
  return actif === id ? <div role="tabpanel">{children}</div> : null;
};
// <Onglets defaut="a"><Onglets.Bouton id="a">A</Onglets.Bouton>…</Onglets>
```

### 13.8 Contexte et Server Components

Les contextes **ne fonctionnent pas dans les Server Components** (pas de `useContext`). Le fournisseur doit être un **composant client** (`'use client'`) qui reçoit `children` (pouvant être des Server Components). Placez-le **le plus bas possible** pour limiter le JavaScript envoyé au client.

### 13.9 Tester

```jsx
render(<ThemeContext value={{ theme: 'sombre', setTheme: vi.fn() }}><Bouton /></ThemeContext>);
```

### 13.10 Comment le Context fonctionne réellement

- **Lecture pendant le rendu.** `useContext(Ctx)` (ou `use(Ctx)`) retourne la valeur du **fournisseur le plus proche au-dessus** de l'appelant dans l'arbre **React** (pas dans le DOM : un portail conserve ses contextes, chapitre 19). Aucun abonnement manuel n'est nécessaire : React enregistre, lors du rendu, que ce composant **dépend** de ce contexte.
- **Mise à jour.** Quand la `value` d'un fournisseur change (comparaison par `Object.is`), React **parcourt le sous-arbre**, repère les composants qui lisent ce contexte et **planifie leur re-rendu**, même si un parent intermédiaire est protégé par `memo` ou `shouldComponentUpdate`. Les composants qui **ne lisent pas** le contexte ne sont pas touchés (sauf s'ils re-rendent pour une autre raison).
- **Valeur par défaut.** L'argument de `createContext(valeurParDefaut)` n'est utilisé **que lorsqu'aucun fournisseur** n'entoure le consommateur. Ce n'est **pas** un état initial. Elle sert aux **tests isolés** et aux composants autonomes ; pour imposer la présence d'un fournisseur, passez `null` et levez une erreur dans le hook de consommation (13.3).
- **Identité de la valeur.** Seule la **référence** compte : un objet reconstruit à chaque rendu est une « nouvelle valeur », même à contenu identique (13.4).
- **Contexte et `children`.** Un fournisseur qui reçoit ses enfants en `children` ne les re-rend pas quand son propre état change : seuls les **consommateurs** sont mis à jour.

> Le Context est un mécanisme de **transport**, pas un moteur de gestion d'état : il ne sait ni stocker, ni calculer, ni sélectionner une partie de la valeur.

### 13.11 Exemple complet : `useReducer` + Context

Pour un état partagé qui évolue selon des actions (liste de tâches, panier), combinez `useReducer` et **deux contextes** : un pour l'**état**, un pour le **`dispatch`** (stable, donc sans re-rendu inutile).

```jsx
import { createContext, useContext, useReducer } from 'react';

function reducteur(taches, action) {
  switch (action.type) {
    case 'ajouter':   return [...taches, { id: action.id, texte: action.texte, faite: false }];
    case 'basculer':  return taches.map(t => (t.id === action.id ? { ...t, faite: !t.faite } : t));
    case 'supprimer': return taches.filter(t => t.id !== action.id);
    default: throw new Error(`Action inconnue : ${action.type}`);
  }
}

const TachesContext = createContext(null);
const TachesDispatchContext = createContext(null);

export function TachesProvider({ children }) {
  const [taches, dispatch] = useReducer(reducteur, []);
  return (
    <TachesContext value={taches}>
      <TachesDispatchContext value={dispatch}>{children}</TachesDispatchContext>
    </TachesContext>
  );
}

export function useTaches() {
  const v = useContext(TachesContext);
  if (v === null) throw new Error('useTaches doit être utilisé dans <TachesProvider>');
  return v;
}
export function useTachesDispatch() {
  const v = useContext(TachesDispatchContext);
  if (v === null) throw new Error('useTachesDispatch doit être utilisé dans <TachesProvider>');
  return v;
}
```

Un bouton « Supprimer » qui n'appelle que `useTachesDispatch()` **ne re-rend pas** quand la liste change. Le **reducer est pur** : il retourne un nouvel état sans muter l'ancien (chapitre 6).

### 13.12 Composer plusieurs fournisseurs

Une application réelle empile souvent de nombreux fournisseurs (thème, session, i18n, notifications, données). Regroupez-les dans **un seul composant** pour garder la racine lisible :

```jsx
export function Fournisseurs({ children }) {
  return (
    <ThemeProvider>
      <I18nProvider>
        <AuthProvider>
          <NotificationsProvider>{children}</NotificationsProvider>
        </AuthProvider>
      </I18nProvider>
    </ThemeProvider>
  );
}
```

**Ordre des fournisseurs.** Un fournisseur ne peut lire que les contextes situés **au-dessus** de lui : si `NotificationsProvider` a besoin de la session, il doit être **à l'intérieur** de `AuthProvider`. Placez les contextes **les plus généraux** (thème, langue) vers l'extérieur.

**Portée.** Un fournisseur n'a pas à être à la racine : limitez-le au **sous-arbre qui en a besoin**. Cela réduit les rendus et permet de **surcharger** localement (un panneau en thème sombre dans une page claire).

### 13.13 Le Context comme injection de dépendances et pour les tests

Le Context sert aussi à **injecter des services** (client HTTP, horloge, journalisation) sans les importer en dur dans les composants.

```jsx
const ApiContext = createContext(apiReelle);

// En production : valeur par défaut. Dans un test ou une démonstration : remplacement.
render(
  <ApiContext value={{ chargerProduits: async () => [{ id: 1, nom: 'Test' }] }}>
    <Catalogue />
  </ApiContext>
);
```

Pour les tests, créez une fonction `renderAvecFournisseurs(ui, options)` qui entoure automatiquement les composants des fournisseurs nécessaires : tous les tests partagent alors la même configuration, et chacun peut surcharger une valeur.

### 13.14 Un store dans le Context : abonnements ciblés

Pour obtenir des **mises à jour fines** tout en gardant la diffusion par Context, placez dans le contexte un **objet store stable** (jamais recréé) et abonnez chaque composant **uniquement à la partie qui l'intéresse** avec `useSyncExternalStore` (chapitre 22).

```jsx
function creerStore(etatInitial) {
  let etat = etatInitial;
  const ecouteurs = new Set();
  return {
    lire: () => etat,
    modifier(partiel) { etat = { ...etat, ...partiel }; ecouteurs.forEach(l => l()); },
    abonner(l) { ecouteurs.add(l); return () => ecouteurs.delete(l); },
  };
}

const StoreContext = createContext(null);

function useSelecteur(selecteur) {
  const store = useContext(StoreContext);
  return useSyncExternalStore(store.abonner, () => selecteur(store.lire()));
}
// useSelecteur(e => e.theme) ne re-rend que si le thème change.
```

Le sélecteur doit retourner une valeur **primitive ou stable** ; un sélecteur qui crée un nouvel objet à chaque appel provoque une boucle de rendus. Dans la pratique, **Zustand**, **Jotai** et **Redux Toolkit** font exactement cela, avec les protections nécessaires : préférez-les à une version maison.

### 13.15 Context, props, composition ou store : que choisir ?

| Situation | Solution |
| --- | --- |
| Donnée utilisée par **un ou deux niveaux** de composants | **Props** |
| Les composants intermédiaires ne font que **relayer** | **Composition** (`children`, slots) : passez le JSX déjà construit |
| Donnée **globale à un sous-arbre**, qui change **rarement** (thème, langue, utilisateur) | **Context** |
| État **partagé**, modifié **souvent** par des composants **éloignés** | **Store externe** (Zustand, Jotai, Redux Toolkit) |
| Données **venant du serveur** (listes, détails, cache) | **Bibliothèque de données** (TanStack Query, SWR) ou framework |
| État **reflété dans l'URL** (filtre, page, onglet) | **Paramètres de l'URL** (routeur) |

Le premier réflexe n'est pas le Context mais la **composition** : souvent, le prop drilling disparaît en remontant la construction du JSX au niveau où se trouve la donnée.

### 13.16 Lire un contexte conditionnellement avec `use`

Contrairement à `useContext`, **`use(Ctx)`** peut être appelé **après un `return` anticipé** ou à l'intérieur d'une condition ou d'une boucle :

```jsx
function Message({ afficher }) {
  if (!afficher) return null;
  const theme = use(ThemeContext);     // autorisé ici
  return <p className={theme}>Bonjour</p>;
}
```

Les deux lectures créent la même dépendance ; `use` offre simplement plus de souplesse. Pour tout le reste (règles de Hooks, performance), le comportement est identique.

### 13.17 Déboguer un contexte

- Dans **React DevTools**, un fournisseur apparaît sous le nom `Context.Provider` (ou le `displayName` que vous lui avez donné) ; sélectionnez un consommateur pour voir la **valeur lue**.
- Donnez un `displayName` : `ThemeContext.displayName = 'Theme'`.
- Activez dans le Profiler l'option « **Pourquoi ce composant a-t-il été rendu ?** » : elle indique « Le contexte a changé » le cas échéant.
- Si **trop** de composants se re-rendent, vérifiez dans l'ordre : l'identité de la valeur (13.4-1), le découpage du contexte (13.4-2), la séparation état / actions (13.4-3).

### 13.18 Pièges fréquents

- Valeur objet recréée à chaque rendu sans `useMemo`.
- Contexte unique géant pour tout l'état de l'application.
- Utiliser Context pour des données **très fréquemment mises à jour** (position souris, saisie).
- Oublier le fournisseur → valeur par défaut `undefined`/`null` → erreurs obscures (prévoir une garde dans le hook).
- Croire que `memo` bloque la propagation d'un changement de contexte (non : le consommateur est re-rendu).
- Utiliser Context pour remplacer des props ordinaires dans tous les cas (perte de traçabilité).

### Synthèse du chapitre 13

**createContext → Provider (`<Ctx value>`) → `useContext` / `use`** ; Le consommateur se re-rend à **tout changement** de valeur ; **mémoïsez** la valeur et **découpez** les contextes ; Pattern : **Provider + hook `useXxx`** avec garde d'erreur ; Pour des états globaux dynamiques et fins → **stores externes**.

---

## 14. Refs et accès au DOM

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : comprendre quand et pourquoi sortir du modèle déclaratif avec les refs ; maîtriser `useRef`, les refs de callback, le transfert de refs et `useImperativeHandle` ; manipuler le DOM de façon sûre (focus, scroll, mesure) et intégrer des bibliothèques externes.

### 14.1 Définition et rôle

Une **ref** est une **« échappatoire »** (*escape hatch*) qui permet à un composant de :
1. **accéder à un nœud DOM** (ou à une instance de composant classe) ;
2. **mémoriser une valeur** qui **n'influence pas** le rendu.

React gère le DOM pour vous ; n'utilisez les refs que pour des actions que React **ne peut pas exprimer de façon déclarative** : **focus**, **sélection de texte**, **défilement**, **mesure**, **lecture/pause** de média, **intégration** de bibliothèques tierces (cartes, graphiques, éditeurs), **animations impératives**, **APIs navigateur** (Canvas, Web Audio, Fullscreen).

### 14.2 Obtenir une ref sur un nœud DOM

```jsx
import { useRef } from 'react';

function Formulaire() {
  const inputRef = useRef(null);                 // 1. créer

  function handleClick() {
    inputRef.current.focus();                    // 3. utiliser (dans un gestionnaire ou un effet)
  }

  return (
    <>
      <input ref={inputRef} />                   {/* 2. attacher */}
      <button onClick={handleClick}>Focus</button>
    </>
  );
}
```

- `ref.current` vaut **`null`** au premier rendu ; React y place le **nœud DOM** **pendant le commit** et le remet à **`null`** au démontage.
- En TypeScript : `useRef<HTMLInputElement>(null)`.

### 14.3 Valeurs mutables sans rendu

Voir le chapitre 11 (`useRef`). Cas : identifiants de minuteurs, instances d'objets externes, compteurs de rendus, état « mémoïsé » non affiché, valeur précédente, « dernier callback ».

### 14.4 Règles d'utilisation

1. **Pas de lecture/écriture de `ref.current` pendant le rendu** (sauf initialisation paresseuse).
2. **Ne modifiez pas, par une ref, un nœud DOM géré par React** (ajouter/supprimer des enfants, changer le texte) : cela désynchronise React. Autorisé : `focus()`, `scrollIntoView()`, mesures, lecture.
3. Si vous devez modifier le DOM géré par React, vous le faites **sur des propriétés que React n'utilise pas** (par exemple la classe d'un élément dont `className` n'est pas contrôlé), ou vous recourez à une **clé** pour recréer l'élément.
4. Utilisez les refs avec **parcimonie** : privilégiez props et state.

### 14.5 Refs vers plusieurs éléments (listes)

#### Ref de callback + `Map`

```jsx
function Galerie({ images }) {
  const refs = useRef(new Map());

  function defiler(id) { refs.current.get(id)?.scrollIntoView({ behavior: 'smooth', inline: 'center' }); }

  return (
    <ul>
      {images.map(img => (
        <li key={img.id}
            ref={(noeud) => {
              refs.current.set(img.id, noeud);
              return () => refs.current.delete(img.id);       // nettoyage (React 19)
            }}>
          <img src={img.url} alt={img.alt} />
        </li>
      ))}
    </ul>
  );
}
```

> On ne peut pas appeler `useRef` dans une boucle ni dans un `map` (règles des hooks). D'où la **ref de callback** ou une **`Map`** dans une seule ref.

### 14.6 Refs de callback

Au lieu d'un objet, on passe **une fonction** à `ref` :

- appelée avec le **nœud** quand il est **monté** (et avec `null` au démontage, **avant React 19**) ;
- en **React 19**, elle peut **retourner une fonction de nettoyage** ; dans ce cas React n'appelle plus avec `null`.

```jsx
<div ref={(el) => {
  if (!el) return;
  const obs = new ResizeObserver(([e]) => setLargeur(e.contentRect.width));
  obs.observe(el);
  return () => obs.disconnect();
}} />
```

Une ref de callback **inline** est recréée à chaque rendu → React l'appelle à nouveau (cleanup puis setup). Stabilisez-la avec `useCallback` si nécessaire.

### 14.7 Transmettre une ref à un composant

Par défaut, une ref sur un composant personnalisé ne donne **pas** accès à son DOM interne.

```jsx
// React 19 : `ref` est une simple prop
function Champ({ ref, ...props }) {
  return <input ref={ref} {...props} />;
}
<Champ ref={monRef} />

// React 18 et avant : forwardRef
const Champ = forwardRef(function Champ(props, ref) {
  return <input ref={ref} {...props} />;
});
```

#### Exposer une API limitée : `useImperativeHandle`

Pour **ne pas** exposer tout le DOM, exposez seulement certaines méthodes (chapitre 11) :

```jsx
function Champ({ ref }) {
  const interne = useRef(null);
  useImperativeHandle(ref, () => ({
    focus: () => interne.current.focus(),
  }), []);
  return <input ref={interne} />;
}
```

### 14.8 Quand React attache les refs : synchronisation et `flushSync`

React met à jour `ref.current` **pendant le commit**, avant les effets. Lorsque vous devez accéder au **DOM mis à jour immédiatement après un `setState`** (ex. défiler jusqu'à l'élément qui vient d'être ajouté), le DOM n'est pas encore à jour dans le gestionnaire. Solutions :

```jsx
import { flushSync } from 'react-dom';

function ajouter() {
  flushSync(() => { setTodos([...todos, nouveau]); });   // force le commit synchrone
  dernierRef.current.scrollIntoView();                   // le DOM contient désormais le nouvel élément
}
```

⚠ `flushSync` nuit aux performances : alternative = effet réagissant au changement, ou ref de callback.

### 14.9 Exemples d'usage

```jsx
// Focus automatique au montage
useEffect(() => { ref.current?.focus(); }, []);          // ou autoFocus

// Défilement vers un élément
ref.current.scrollIntoView({ behavior: 'smooth', block: 'center' });

// Mesure
const { width, height } = ref.current.getBoundingClientRect();

// Média
videoRef.current.play();  videoRef.current.pause();

// Canvas
useEffect(() => { const ctx = canvasRef.current.getContext('2d'); ctx.fillRect(0, 0, 50, 50); }, []);

// Sélection de texte
inputRef.current.select();

// Bibliothèque externe
useEffect(() => {
  const carte = new Carte(conteneurRef.current, { zoom });
  return () => carte.destroy();
}, []);
```

### 14.10 Refs vs state, récapitulatif

| | Ref | State |
|---|---|---|
| Donnée affichée | ❌ | ✅ |
| Déclenche un rendu | ❌ | ✅ |
| Mutable directement | ✅ | ❌ |
| Persiste entre rendus | ✅ | ✅ |
| Accès au DOM | ✅ | ❌ |
| Prévisibilité / testabilité | Moindre | Meilleure |

### 14.11 Quand lire et écrire `ref.current`

`ref.current` est une **valeur mutable hors du cycle de rendu** : React ne la surveille pas. D'où une règle essentielle : **ne lisez ni n'écrivez `ref.current` pendant le rendu**, sauf pour une **initialisation paresseuse**. Lisez et écrivez dans :

- les **gestionnaires d'événements** ;
- les **effets** (`useEffect`, `useLayoutEffect`) ;
- les **callbacks de ref**.

```jsx
// ❌ Lecture pendant le rendu : le résultat dépend d'une valeur que React ne suit pas
function Compteur() {
  const rendus = useRef(0);
  rendus.current += 1;                     // mutation pendant le rendu (impure)
  return <p>{rendus.current}</p>;
}
```

**Initialisation paresseuse** : l'écriture est tolérée **une seule fois**, pour éviter de recréer un objet coûteux à chaque rendu.

```jsx
function Lecteur() {
  const moteur = useRef(null);
  if (moteur.current === null) moteur.current = new MoteurAudio();   // créé une seule fois
  // ...
}
```

`useRef(new MoteurAudio())` appellerait le constructeur à **chaque rendu** (le résultat serait simplement ignoré après le premier).

### 14.12 Manipuler le DOM : cas d'usage courants

Les refs servent aux opérations qui n'ont **pas d'équivalent déclaratif** :

| Besoin | API du DOM | Où l'appeler |
| --- | --- | --- |
| Donner le **focus** | `ref.current.focus()` | Gestionnaire ou effet |
| **Faire défiler** vers un élément | `ref.current.scrollIntoView({ behavior: 'smooth', block: 'nearest' })` | Gestionnaire ou effet |
| **Mesurer** une taille ou une position | `getBoundingClientRect()`, `offsetHeight` | `useLayoutEffect` (avant la peinture) |
| Contrôler un **média** | `video.play()`, `video.pause()` | Gestionnaire d'événement |
| Sélectionner du **texte** | `input.select()`, `setSelectionRange()` | Gestionnaire |
| Déclencher une **animation** impérative | `element.animate(...)` (Web Animations) | Effet, avec nettoyage |
| Intégrer une bibliothèque tierce | Constructeur de la bibliothèque sur le nœud | Effet, avec nettoyage |

```jsx
function Video({ src }) {
  const ref = useRef(null);
  const [lecture, setLecture] = useState(false);

  function basculer() {
    const v = ref.current;
    if (lecture) v.pause(); else v.play();
    setLecture(!lecture);
  }

  return (
    <>
      <video ref={ref} src={src} onPlay={() => setLecture(true)} onPause={() => setLecture(false)} />
      <button onClick={basculer}>{lecture ? 'Pause' : 'Lecture'}</button>
    </>
  );
}
```

> Ne modifiez pas par ref un nœud **géré par React** (`textContent`, ajout ou suppression d'enfants) : vous créeriez un désaccord entre l'arbre React et le DOM, et la prochaine mise à jour pourrait échouer. Limitez-vous à des opérations **non destructrices** (focus, défilement, mesure, lecture/écriture de propriétés impératives).

### 14.13 Fonction de nettoyage des refs de callback (React 19)

Depuis React 19, un **callback de ref peut retourner une fonction de nettoyage**, appelée quand l'élément est détaché. Cela remplace l'ancien motif « appelé avec `null` » :

```jsx
<div
  ref={noeud => {
    const observateur = new ResizeObserver(([entree]) => setLargeur(entree.contentRect.width));
    observateur.observe(noeud);
    return () => observateur.disconnect();      // nettoyage à la fin de la vie du nœud
  }}
/>
```

Conséquences :

- Quand une fonction de nettoyage est retournée, React **n'appelle plus** le callback avec `null`.
- Un callback écrit en **flèche à expression** (`ref={n => (this.x = n)}`) **retourne** la valeur assignée, ce qui est interprété comme un nettoyage : écrivez-le avec des **accolades** (`ref={n => { this.x = n; }}`). TypeScript signale cette erreur.
- Le callback est **recréé à chaque rendu** s'il est défini en ligne : React l'appelle alors en nettoyage puis en configuration. Stabilisez-le avec `useCallback` si le coût est notable.

### 14.14 Observer le DOM : `ResizeObserver` et `IntersectionObserver`

Mesurer la taille d'un élément ou savoir s'il est visible nécessite des **observateurs** du navigateur. Encapsulez-les dans un **Hook personnalisé** (chapitre 12) :

```jsx
function useTaille() {
  const [taille, setTaille] = useState({ largeur: 0, hauteur: 0 });
  const ref = useCallback(noeud => {
    if (!noeud) return;
    const obs = new ResizeObserver(([e]) =>
      setTaille({ largeur: e.contentRect.width, hauteur: e.contentRect.height })
    );
    obs.observe(noeud);
    return () => obs.disconnect();
  }, []);
  return [ref, taille];
}

function Panneau() {
  const [ref, { largeur }] = useTaille();
  return <section ref={ref}>{largeur > 600 ? <Large /> : <Etroit />}</section>;
}
```

```jsx
function useVisible(options) {
  const [visible, setVisible] = useState(false);
  const ref = useCallback(noeud => {
    if (!noeud) return;
    const obs = new IntersectionObserver(([e]) => setVisible(e.isIntersecting), options);
    obs.observe(noeud);
    return () => obs.disconnect();
  }, []);
  return [ref, visible];
}
// Usages : chargement paresseux d'images, défilement infini, animations à l'apparition.
```

Pour des besoins de **mise en page**, privilégiez d'abord le CSS (**requêtes de conteneur** `@container`, `clamp()`, grid) : un observateur n'est justifié que si la logique JavaScript dépend de la taille.

### 14.15 Intégrer une bibliothèque non React

Pour une carte, un graphique ou un éditeur riche, le schéma est toujours le même :

1. un **conteneur** rendu par React, repéré par une ref ;
2. **création** de l'instance dans un effet (`setup`) ;
3. **mise à jour** de l'instance quand les props changent (effet distinct) ;
4. **destruction** dans le nettoyage.

```jsx
function Graphique({ donnees, type }) {
  const conteneur = useRef(null);
  const instance = useRef(null);

  useEffect(() => {                                   // création et destruction
    instance.current = new Chart(conteneur.current, { type, data: donnees });
    return () => { instance.current.destroy(); instance.current = null; };
  }, [type]);

  useEffect(() => {                                   // synchronisation des données
    instance.current.data = donnees;
    instance.current.update();
  }, [donnees]);

  return <canvas ref={conteneur} />;
}
```

Strict Mode (chapitre 21) vérifie que ce couple création/destruction est **symétrique** : si deux graphiques apparaissent en développement, le nettoyage est incomplet. Le conteneur ne doit **pas** recevoir d'enfants React que la bibliothèque modifierait.

### 14.16 Refs, rendu serveur et Strict Mode

- **Avant le montage**, `ref.current` vaut `null` (ou la valeur initiale) : testez-le (`ref.current?.focus()`).
- **Rendu serveur** : il n'y a pas de DOM, donc aucun `ref.current` ; toute logique qui l'utilise doit se situer dans des **effets** ou des **gestionnaires**, jamais dans le corps du composant.
- **Strict Mode** appelle les callbacks de ref **deux fois** au montage (*setup → cleanup → setup*) pour vérifier le nettoyage.
- Une ref ne **déclenche pas** de rendu : si l'interface doit réagir à la valeur, utilisez le **state**.

### 14.17 Accessibilité et refs

- Pour **déplacer le focus** vers un élément non interactif (titre de page, message d'erreur), donnez-lui `tabIndex={-1}` : il devient focalisable par programme sans entrer dans l'ordre de tabulation.
- Après une **navigation** ou l'ouverture d'un panneau, déplacez le focus vers le **nouveau contenu** ; à la fermeture, **restituez-le** au déclencheur (mémorisez-le avec une ref).
- Associez `<label>` et champ avec **`useId`** et `htmlFor`, **pas** avec des refs.
- `aria-live`, `aria-expanded` et les autres attributs ARIA se pilotent par **props et state**, pas par `ref.current.setAttribute(...)`.

### 14.18 Tester le DOM sans refs

Les tests doivent interroger l'interface **comme un utilisateur** : `getByRole`, `getByLabelText`, `getByText`. Vérifiez l'effet d'une ref par son **résultat observable** :

```jsx
await userEvent.click(screen.getByRole('button', { name: /modifier/i }));
expect(screen.getByRole('textbox', { name: /nom/i })).toHaveFocus();
```

N'inspectez pas directement `ref.current` depuis le test : cela lierait le test à l'implémentation.

### 14.19 Pièges fréquents

- Lire `ref.current` pendant le rendu (valeur `null` au 1ᵉʳ rendu).
- Afficher une donnée stockée dans une ref (l'écran ne se met pas à jour).
- Modifier le DOM géré par React (`innerHTML`, `removeChild`) → erreurs « removeChild on Node ».
- `useRef` dans une boucle.
- Oublier le **nettoyage** (observateurs, bibliothèques externes).
- Utiliser `document.getElementById` au lieu d'une ref.
- Utiliser `forwardRef` en React 19 sans nécessité (la prop `ref` suffit).

### Synthèse du chapitre 14

Ref = **conteneur mutable** `{ current }` **hors rendu** ; moyen d'accéder au **DOM** ; Utilisez-les **seulement** pour focus, scroll, mesures, médias, bibliothèques externes ; **Ne touchez pas** à `ref.current` pendant le rendu ; **ne modifiez pas** le DOM géré par React ; React 19 : **`ref` est une prop** ; cleanup dans les refs de callback ; Listes : **callback ref** + `Map`.

---

## 15. Composition et patterns

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : comprendre pourquoi React favorise la **composition** plutôt que l'**héritage** ; maîtriser les patterns de conception : children/slots, render props, HOC, composants composés, headless, polymorphes, contrôlé/non contrôlé, state reducer ; savoir choisir le pattern adapté et connaître ses compromis.

### 15.1 Composition plutôt qu'héritage

Dans la POO classique, on réutilise du code par **héritage** (`class B extends A`). React recommande l'inverse : **composer** des composants, c'est-à-dire en **assembler** de petits pour en construire de plus grands, en leur passant des **props** (y compris du JSX). L'équipe React n'a trouvé **aucun cas** où l'héritage entre composants soit nécessaire : props + composition offrent toute la flexibilité voulue, de manière **explicite et sûre**.

### 15.2 Confinement (*containment*) : `children` et slots

Quand un composant **ne connaît pas à l'avance** son contenu (boîtes, panneaux, modales, mises en page), il reçoit des **enfants**.

```jsx
function Carte({ children }) {
  return <section className="carte">{children}</section>;
}
<Carte><h2>Titre</h2><p>Contenu</p></Carte>
```

#### Plusieurs emplacements (*slots*) via des props nommées

```jsx
function Layout({ entete, barreLaterale, children, pied }) {
  return (
    <div className="layout">
      <header>{entete}</header>
      <aside>{barreLaterale}</aside>
      <main>{children}</main>
      <footer>{pied}</footer>
    </div>
  );
}
<Layout entete={<Navbar />} barreLaterale={<Menu />} pied={<Pied />}>
  <Contenu />
</Layout>
```

#### Inversion de contrôle et prop drilling

Au lieu de faire descendre des données à travers des composants intermédiaires, **créez le JSX là où la donnée existe** et passez-le comme `children`/prop. Les intermédiaires deviennent **génériques et réutilisables**.

### 15.3 Spécialisation

Un composant « spécifique » est une version **configurée** d'un composant « générique » :

```jsx
function Dialogue({ titre, message, children }) {
  return <Fenetre couleur="bleu"><h1>{titre}</h1><p>{message}</p>{children}</Fenetre>;
}
function DialogueBienvenue() {
  return <Dialogue titre="Bienvenue" message="Merci de votre visite !" />;
}
```

### 15.4 Render props

Un composant reçoit une **fonction** qui **retourne du JSX** et l'appelle en lui donnant ses données internes. Le composant **gère la logique** ; l'appelant **décide de l'affichage**.

```jsx
function Souris({ children }) {
  const [pos, setPos] = useState({ x: 0, y: 0 });
  return <div onMouseMove={e => setPos({ x: e.clientX, y: e.clientY })}>{children(pos)}</div>;
}

<Souris>{({ x, y }) => <p>Souris en {x}, {y}</p>}</Souris>
// ou prop nommée : <Liste render={item => <Ligne item={item} />} />
```

- Très utilisé pour les **listes virtualisées**, **formulaires**, **bibliothèques de composants** (cellules de tableau, rendu d'option).
- Aujourd'hui, la **réutilisation de logique** se fait plutôt via des **hooks personnalisés** ; les render props restent pertinentes pour **déléguer le rendu**.
- Évitez d'imbriquer plusieurs render props (« callback hell ») ; si besoin, préférez des hooks.
- Si le composant parent est `memo`, une fonction inline casse la mémoïsation.

### 15.5 Composants d'ordre supérieur (HOC)

Un **HOC** est une **fonction qui prend un composant et retourne un nouveau composant** enrichi.

```jsx
function avecChargement(Composant) {
  function AvecChargement({ chargement, ...props }) {
    return chargement ? <Spinner /> : <Composant {...props} />;
  }
  AvecChargement.displayName = `avecChargement(${Composant.displayName || Composant.name})`;
  return AvecChargement;
}

const ListeAvecChargement = avecChargement(Liste);
```

#### Règles et pièges

- **Ne jamais appeler un HOC dans le rendu** : cela crée un **nouveau type de composant** à chaque rendu (démontage/remontage et perte d'état). Créez la version enrichie **au niveau module**.
- **Copier les statiques** (`hoist-non-react-statics`) si besoin.
- **Transmettre les refs** (`forwardRef` / prop `ref` en 19).
- **Collision de noms de props** possible ; HOC **opaques** (on ignore l'origine des props) ; imbrication difficile à lire dans les DevTools.
- Usages restants : bibliothèques (Redux `connect`, React Router `withRouter` historiques), **intégrations legacy**, ajout de comportements transversaux (erreurs, analytics). Pour du code neuf : **hooks**.

### 15.6 Composants composés (*compound components*)

Un **ensemble de composants qui coopèrent** en partageant un **état implicite** (souvent via **Context**), offrant une API déclarative et flexible (`<Select><Select.Option /></Select>`).

```jsx
const MenuCtx = createContext(null);

function Menu({ children }) {
  const [ouvert, setOuvert] = useState(false);
  return <MenuCtx value={{ ouvert, setOuvert }}><div className="menu">{children}</div></MenuCtx>;
}
Menu.Bouton = function ({ children }) {
  const { ouvert, setOuvert } = useContext(MenuCtx);
  return <button aria-expanded={ouvert} onClick={() => setOuvert(!ouvert)}>{children}</button>;
};
Menu.Liste = function ({ children }) {
  const { ouvert } = useContext(MenuCtx);
  return ouvert ? <ul role="menu">{children}</ul> : null;
};
Menu.Element = function ({ onSelect, children }) {
  const { setOuvert } = useContext(MenuCtx);
  return <li role="menuitem" onClick={() => { onSelect(); setOuvert(false); }}>{children}</li>;
};
```

Avantages : **flexibilité de la structure**, **peu de props**, état encapsulé. C'est le modèle de **Radix UI**, **Headless UI**, **Reach UI**, **shadcn/ui**.

### 15.7 Composants contrôlés et non contrôlés (réutilisables)

Un bon composant de bibliothèque supporte **les deux modes** :

```jsx
function useControlled({ value, defaultValue, onChange }) {
  const estControle = value !== undefined;
  const [interne, setInterne] = useState(defaultValue);
  const courant = estControle ? value : interne;
  const changer = (v) => { if (!estControle) setInterne(v); onChange?.(v); };
  return [courant, changer];
}

function Interrupteur({ checked, defaultChecked = false, onChange }) {
  const [actif, setActif] = useControlled({ value: checked, defaultValue: defaultChecked, onChange });
  return <button role="switch" aria-checked={actif} onClick={() => setActif(!actif)} />;
}
```

### 15.8 Pattern « State reducer » (inversion du contrôle de l'état)

Le composant expose son **reducer interne** : le consommateur peut **intercepter** ou **modifier** les transitions.

```jsx
function useCompteur({ initial = 0, reducer = compteurReducer } = {}) {
  const [{ compte }, dispatch] = useReducer(reducer, { compte: initial });
  return { compte, inc: () => dispatch({ type: 'inc' }), dec: () => dispatch({ type: 'dec' }) };
}
// Consommateur : plafonner à 10
const reducerPlafonne = (etat, action) => {
  const suivant = compteurReducer(etat, action);
  return suivant.compte > 10 ? etat : suivant;
};
const c = useCompteur({ reducer: reducerPlafonne });
```

### 15.9 Composants « headless » et props getters

**Headless** : logique et accessibilité **sans style** ; vous apportez le rendu. Souvent fournis sous forme de **hooks** retournant des **props getters** (objets de props à étaler sur vos éléments).

```jsx
function useDisclosure() {
  const [ouvert, setOuvert] = useState(false);
  const id = useId();
  return {
    ouvert,
    getBoutonProps: () => ({ 'aria-expanded': ouvert, 'aria-controls': id, onClick: () => setOuvert(o => !o) }),
    getPanneauProps: () => ({ id, hidden: !ouvert }),
  };
}
const d = useDisclosure();
<button {...d.getBoutonProps()}>Détails</button>
<div {...d.getPanneauProps()}>…</div>
```

Exemples : **TanStack Table / Form / Virtual**, **Downshift**, **React Aria**, **Radix Primitives**.

### 15.10 Composants polymorphes (`as` / `asChild`)

Permettre à l'appelant de **choisir l'élément rendu** tout en gardant le style/comportement.

```jsx
function Texte({ as: Balise = 'span', ...props }) { return <Balise {...props} />; }
<Texte as="h1">Titre</Texte>
<Texte as="a" href="/accueil">Lien</Texte>
```

Variante `asChild` (Radix) : le composant **fusionne** ses props sur son **unique enfant** (via `Slot`).

### 15.11 Container / présentation

Découpage historique : **conteneur** (récupère données, état) → **présentation** (affiche des props). Les **hooks** remplacent aujourd'hui le conteneur : le composant appelle un hook (`useUtilisateurs`) et délègue l'affichage à des composants simples.

### 15.12 Autres techniques

- **`cloneElement` et `Children.map`** pour injecter des props dans des enfants : **fragile** (dépend de la structure exacte). Préférez Context ou la prop render.
- **Composition de fournisseurs** : un composant `AppProviders` regroupe `ThemeProvider`, `AuthProvider`, `QueryClientProvider`…
- **Layouts imbriqués** : composants de mise en page enveloppant les pages.
- **Slots nommés avec des composants** : `<Carte.Entete />`, `<Carte.Corps />`.
- **Composition avec des hooks** : combiner `useAuth`, `usePermissions` → `useCanEdit`.

### 15.13 Tableau comparatif

| Pattern | Réutilise | Avantage | Inconvénient |
|---|---|---|---|
| `children` / slots | Structure | Simple, flexible | — |
| Hook personnalisé | Logique avec état | Lisible, composable | Ne gère pas le rendu |
| Render props | Logique + délégation du rendu | Contrôle total du rendu | Imbrication, performance si inline |
| HOC | Comportement transversal | Applicable à tout composant | Opaque, pièges de création |
| Composés (Context) | Structure + état | API déclarative | Contexte à gérer |
| Headless | Logique + a11y | Style libre | Plus de code d'intégration |
| Polymorphe | Style/comportement | Souplesse sémantique | Typage TypeScript complexe |
| State reducer | Logique extensible | Contrôle fin | Complexité |

### 15.14 Pièges fréquents

- Créer un HOC dans le corps d'un composant.
- Dépendre de la forme exacte de `children` (Children.map / cloneElement).
- Multiplier les props booléennes au lieu de composer.
- Surcharger l'API d'un composant (30 props) plutôt que le découper.
- Passer des fonctions inline à des composants `memo` sans `useCallback`.

### Synthèse du chapitre 15

**Composition > héritage**. `children` + slots + hooks couvrent la majorité des besoins ; **Hooks** pour réutiliser de la **logique** ; **composition/render props** pour déléguer le **rendu** ; **Composés + Context** pour des API riches ; **headless** pour des bibliothèques UI ; HOC : héritage de l'ère des classes, à éviter dans le code neuf.

---

# Partie III — Performance, rendu avancé et serveur

## 16. Performance et optimisation

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : comprendre **quand et pourquoi** React re-rend, et ce qui est (ou non) un vrai problème ; mesurer avec les bons outils avant d'optimiser ; maîtriser les techniques : colocation d'état, `memo`, `useMemo`, `useCallback`, virtualisation, code splitting, transitions, React Compiler.

### 16.1 Principe directeur

> **Mesurez d'abord, optimisez ensuite.** La plupart des applications React sont suffisamment rapides sans optimisation manuelle. Les problèmes se concentrent sur : **listes longues**, **calculs lourds**, **rendus en cascade**, **gros bundles**, **animations**, **réseau**.

Trois types de coûts : **rendu** (CPU), **chargement** (réseau/bundle), **interaction** (latence perçue).

### 16.2 Quand React re-rend-il un composant ?

Un composant est re-rendu quand :
1. **Son state** change (`useState` / `useReducer`).
2. **Son parent** est re-rendu (**même si ses props sont identiques**).
3. Un **contexte** qu'il consomme change.
4. Une **source externe** à laquelle il est abonné change (`useSyncExternalStore`, store).

> Re-rendre un composant **n'implique pas** de mettre à jour le DOM : React compare d'abord le résultat. Un rendu « inutile » est souvent **peu coûteux** ; il ne devient problématique que s'il est **lent** (calcul lourd, grand arbre) ou **fréquent**.

La **mise à jour est récursive** : re-rendre un parent re-rend **tout son sous-arbre** par défaut.

### 16.3 Mesurer

#### React DevTools Profiler

1. Onglet **Profiler** → **Record** → interagir → **Stop**.
2. Vues **Flamegraph** / **Ranked** : durée de rendu par composant.
3. **« Why did this render? »** (option à activer dans les paramètres du Profiler) : indique la cause (props, state, hooks, parent).
4. Option **« Highlight updates when components render »** dans les DevTools.
5. Les DevTools récents affichent des **pistes de performance** dans le panneau Performance de Chrome (React 19.2).

#### Autres outils

- `<Profiler id="x" onRender={callback}>` : mesures programmatiques.
- **Chrome Performance** / **Lighthouse** / **Web Vitals** (LCP, INP, CLS).
- **`console.time`** pour un calcul précis.
- **Bundle analyzer** (`rollup-plugin-visualizer`, `@next/bundle-analyzer`, `source-map-explorer`).
- Toujours profiler en **build de production** (le mode développement et StrictMode sont plus lents).

### 16.4 Technique n°1 : colocaliser l'état

Placer l'état **le plus bas possible** limite la portée des rendus.

```jsx
// ❌ La saisie re-rend ToUTE la page à chaque frappe
function Page() {
  const [texte, setTexte] = useState('');
  return <><input value={texte} onChange={e => setTexte(e.target.value)} /><GrosTableau /></>;
}

// ✅ L'état est isolé dans son composant
function Champ() { const [texte, setTexte] = useState(''); return <input value={texte} onChange={e => setTexte(e.target.value)} />; }
function Page() { return <><Champ /><GrosTableau /></>; }
```

### 16.5 Technique n°2 : « remonter le contenu » (children)

Passer le sous-arbre en **`children`** : sa référence est créée **au-dessus**, donc **inchangée** quand l'état du composant enveloppant change.

```jsx
function ConteneurSouris({ children }) {
  const [pos, setPos] = useState({ x: 0, y: 0 });
  return <div onMouseMove={e => setPos({ x: e.clientX, y: e.clientY })}>{children}</div>;
}
<ConteneurSouris><ComposantLourd /></ConteneurSouris>   // ne se re-rend pas quand pos change
```

### 16.6 Technique n°3 : `React.memo`

`memo(Composant)` **saute le rendu** si **les props sont identiques** au rendu précédent (comparaison **superficielle** `Object.is` de chaque prop).

```jsx
const Ligne = memo(function Ligne({ item, onSelect }) {
  return <li onClick={() => onSelect(item.id)}>{item.nom}</li>;
});

// Comparateur personnalisé (rare)
const Graphique = memo(Composant, (anciennes, nouvelles) => anciennes.donnees.version === nouvelles.donnees.version);
```

#### Quand `memo` est utile

- Composant **coûteux** à rendre **et** qui reçoit souvent les **mêmes props** alors que son parent se re-rend.
- Éléments d'une **longue liste**.

#### Quand `memo` est inefficace

- **Props instables** : objets/tableaux/fonctions **créés à chaque rendu** (`style={{…}}`, `onClick={() => …}`, `options={[…]}`) → nouvelle référence → `memo` ne protège plus.
- **`children`** JSX (nouvel élément à chaque rendu).
- Le composant **consomme un contexte** qui change (`memo` n'empêche pas ce rendu).
- Composants **légers** : le coût de comparaison dépasse le gain.

```jsx
<Ligne item={item} onSelect={(id) => selectionner(id)} />       // ❌ nouvelle fonction à chaque rendu
const onSelect = useCallback((id) => selectionner(id), []);     // ✅ + memo sur Ligne
```

### 16.7 Technique n°4 : `useMemo` et `useCallback`

Voir chapitre 11. Règle d'or : les employer **là où ils servent** (valeurs/fonctions passées à des composants `memo`, dépendances d'effets, calculs lourds **mesurés**). Réduire d'abord les dépendances (forme fonctionnelle de `setState`, reducers).

```jsx
const resultats = useMemo(() => rechercher(index, requete), [index, requete]);   // calcul lourd
```

### 16.8 Technique n°5 : listes — virtualisation et pagination

- **Virtualisation** (*windowing*) : ne monter dans le DOM que les lignes **visibles** : `@tanstack/react-virtual`, `react-window`, `react-virtuoso`. Passe de dizaines de milliers de nœuds DOM à quelques dizaines.
- **Pagination** ou **défilement infini** (chargement progressif).
- **Clés stables** (chapitre 9) ; éviter de recréer les éléments.
- `content-visibility: auto` (CSS) pour différer le rendu hors écran.

### 16.9 Technique n°6 : prioriser avec la concurrence

- **`useTransition`** pour marquer un changement lourd comme non urgent ;
- **`useDeferredValue`** pour retarder une valeur coûteuse à afficher ;
- **`<Suspense>`** pour ne pas bloquer l'interface en attendant du code/des données ;
- **`<Activity>`** (19.2) pour préparer en arrière-plan des vues masquées.

(Détails : chapitre 11, 17, 22.)

### 16.10 Technique n°7 : réduire le coût du chargement

| Levier | Description |
|---|---|
| **Code splitting** | `lazy` + `Suspense`, import dynamique par **route** et par **composant lourd** (éditeur, graphiques) |
| **Tree shaking** | Imports ES nommés, éviter les barrels volumineux, dépendances « side-effect free » |
| **Analyse du bundle** | Repérer les dépendances volumineuses ; remplacer (`date-fns` au lieu de `moment`, `dayjs`) |
| **Prefetch / preload** | Précharger les routes probables (au survol, à l'idle) ; API `preload` / `preinit` de `react-dom` |
| **Images** | Formats modernes (WebP/AVIF), `loading="lazy"`, `srcset`/`sizes`, dimensions explicites (évite le CLS) |
| **Polices** | `font-display: swap`, préchargement, sous-ensembles |
| **SSR / SSG / streaming** | Contenu affiché avant l'exécution du JS ; hydratation sélective |
| **Server Components** | Moins de JavaScript envoyé au client |
| **Cache & CDN** | Hash dans les noms de fichiers, `Cache-Control`, compression Brotli |

### 16.11 Technique n°8 : bonnes pratiques de rendu

- **Calculs dérivés** pendant le rendu plutôt que state + effet (évite des rendus en cascade).
- **Éviter les effets qui mettent à jour l'état** en chaîne.
- **Débouncer/throttler** les entrées fréquentes (scroll, resize, saisie) ; écouteurs **passifs**.
- **Animations** : privilégier **CSS** (`transform`, `opacity`) ou Web Animations, plutôt que des mises à jour d'état à 60 fps.
- **Gros calculs** : **Web Workers** (Comlink).
- **Structures de données** adaptées (`Map`/`Set`, index par ID) pour des recherches fréquentes.
- **État externe avec sélecteurs** (Zustand, Redux) pour éviter les rendus liés à un contexte large.
- **Éviter de définir des composants dans des composants.**

### 16.12 React Compiler

Le **React Compiler** (stable depuis fin 2025, plugin Babel/SWC/Vite) **analyse votre code à la compilation** et **ajoute automatiquement la mémoïsation** (composants, valeurs, fonctions) à une granularité plus fine que `memo`/`useMemo`/`useCallback` manuels.

```bash
npm install -D babel-plugin-react-compiler
# + eslint-plugin-react-hooks (inclut les règles du compilateur)
```

```js
// vite.config.js
react({ babel: { plugins: [['babel-plugin-react-compiler', {}]] } })
```

- Exige que le code **suive les « Rules of React »** (pureté, immutabilité, règles des hooks). Les composants qui les violent sont **ignorés** (pas compilés) ou signalés par le linter.
- **Directives** : `"use no memo"` (exclure un composant/hook), mode **`annotation`** avec `"use memo"` (adoption progressive).
- **Résultat** : moins de `useMemo`/`useCallback`/`memo` à écrire ; vous gardez ces API pour des **cas précis** (contrôle d'identité dans les dépendances d'effets).
- Compatible React 17+ (avec `react-compiler-runtime`), optimal en 19.
- Vérifiez dans les **DevTools** (badge « Memo ✨ ») et **mesurez** avant/après.

### 16.13 Performance du rendu serveur et de l'hydratation

- **Streaming SSR** avec `Suspense` : le shell s'affiche tôt, le reste suit.
- **Hydratation sélective** : les parties interactives s'hydratent par priorité (celles cliquées en premier).
- Réduire la taille du **JS client** (Server Components, îlots).
- Éviter les **différences serveur/client** (dates, `Math.random`, `window`).

### 16.14 Checklist d'optimisation

1. **Mesurer** (Profiler, Lighthouse) en production.
2. **Colocaliser** l'état / remonter le contenu en `children`.
3. **Corriger les rendus en cascade** (effets inutiles, état dérivé stocké).
4. **Virtualiser/paginer** les longues listes.
5. **Code splitting** par route ; analyser le bundle.
6. `memo` + props stables **là où le Profiler le justifie** (ou activer le **Compiler**).
7. **Transitions / valeurs différées** pour les interactions lourdes.
8. **Images, polices, cache** et **SSR/streaming**.
9. **Re-mesurer** pour confirmer le gain.

### 16.15 Pièges fréquents

- Optimiser **sans mesurer** ; `memo` partout.
- `memo` neutralisé par des **props inline**.
- Profiler en **développement** (StrictMode double les rendus).
- Utiliser l'**index** comme clé dans des listes dynamiques (rendus et bugs).
- Un **contexte unique** recréé à chaque rendu.
- Stocker en state des données **dérivées** (double rendu).
- Importer des bibliothèques entières (`import _ from 'lodash'`) au lieu d'imports ciblés.

### Synthèse du chapitre 16

Un rendu ≠ une mise à jour du DOM ; la plupart des rendus sont peu coûteux ; **Mesurer → corriger la structure (état local, children) → mémoïser → virtualiser → charger moins.** ; `memo` ne marche qu'avec des **props stables** ; **React Compiler** automatise la mémoïsation pour du code conforme aux règles de React ; Pensez **chargement** (bundle, réseau) autant que **rendu**.

---

## 17. Suspense et chargement différé

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : comprendre ce que « suspendre » signifie et comment `<Suspense>` orchestre les états d'attente ; utiliser `lazy` pour le **code splitting** et `use` / sources compatibles pour les **données** ; combiner Suspense avec les **transitions**, les **Error Boundaries** et le **streaming SSR**.

### 17.1 Définition

**`<Suspense>`** permet d'**afficher une interface de repli (`fallback`)** pendant que ses enfants **ne sont pas encore prêts** (code en cours de chargement, données en cours de récupération). Un composant **« suspend »** quand, pendant son rendu, il signale à React qu'il **attend une ressource** (une promesse).

```jsx
import { Suspense } from 'react';

<Suspense fallback={<Squelette />}>
  <Profil />          {/* peut suspendre */}
</Suspense>
```

Mécanisme :
1. Un enfant suspend (via `lazy`, `use(promesse)` ou une source compatible).
2. React **remonte** jusqu'au **`<Suspense>` le plus proche** et affiche son **`fallback`** à la place du sous-arbre.
3. Quand la ressource est prête, React **re-rend** le sous-arbre et **remplace** le fallback.

> Suspense **ne détecte pas** les requêtes lancées dans un `useEffect` ou un gestionnaire d'événement : seules les sources **intégrées à Suspense** fonctionnent.

### 17.2 `lazy` : chargement différé de composants (code splitting)

```jsx
import { lazy, Suspense } from 'react';

const Editeur = lazy(() => import('./Editeur'));         // le module doit avoir un export PAR DÉFAUT

function Page() {
  const [ouvert, setOuvert] = useState(false);
  return (
    <>
      <button onClick={() => setOuvert(true)}>Ouvrir l'éditeur</button>
      {ouvert && (
        <Suspense fallback={<p>Chargement de l'éditeur…</p>}>
          <Editeur />
        </Suspense>
      )}
    </>
  );
}
```

- **Appelez `lazy` au niveau module**, jamais dans un composant (sinon le chargement est réinitialisé à chaque rendu).
- **Export nommé** : `lazy(() => import('./UI').then(m => ({ default: m.Editeur })))`.
- **Préchargement** : lancer `import('./Editeur')` à l'avance (au survol d'un bouton, à l'idle) ; le composant `lazy` aura alors déjà son module en cache.
- **Découper par route** est le meilleur gain initial ; ensuite par composants lourds (éditeur, graphiques, cartes, PDF).
- Le chargement échoué (réseau) lève une **erreur** : associez un **Error Boundary** avec option « réessayer ».

### 17.3 Suspense pour les données

Sources compatibles :
- **Frameworks** (Next.js App Router, React Router, Remix) : loaders, Server Components `async`.
- **`use(promesse)`** (React 19).
- **Bibliothèques** : TanStack Query (`useSuspenseQuery`), Relay, SWR (`suspense: true`), Apollo (`useSuspenseQuery`).

```jsx
// Composant serveur : peut être async et « attend » directement
async function Articles() {
  const articles = await db.articles.findMany();
  return articles.map(a => <Article key={a.id} {...a} />);
}
<Suspense fallback={<ListeSquelette />}><Articles /></Suspense>
```

```jsx
// Composant client : promesse créée ailleurs (serveur / cache) + use
function Commentaires({ promesse }) {
  const commentaires = use(promesse);
  return commentaires.map(c => <p key={c.id}>{c.texte}</p>);
}
```

> Ne créez **pas** de promesse dans le corps d'un composant client à chaque rendu : elle serait recréée sans fin. Utilisez un **cache** ou passez-la depuis un **Server Component** / une bibliothèque.

### 17.4 Granularité et imbrication

On place **plusieurs frontières Suspense** pour contrôler **ce qui s'affiche** pendant l'attente :

```jsx
<Suspense fallback={<SqueletteGlobal />}>
  <Entete />
  <Suspense fallback={<SqueletteFil />}>
    <Fil />
  </Suspense>
  <Suspense fallback={<SqueletteBarre />}>
    <BarreLaterale />
  </Suspense>
</Suspense>
```

- Le fallback le **plus proche** de l'enfant suspendu s'affiche.
- Frontière **trop haute** : tout disparaît derrière un spinner ; **trop basse** : « effet pop-corn » (nombreux spinners). Alignez les frontières sur des **zones fonctionnelles** de l'interface.
- Les enfants **déjà visibles** ne sont **pas** masqués quand un frère suspend plus bas, sauf nouvelle frontière franchie.

### 17.5 Transitions : éviter de réafficher le fallback

Quand une mise à jour **déclenche** une suspension **dans une zone déjà affichée**, React remplace par le fallback (clignotement). Si la mise à jour est enveloppée dans une **transition**, React **conserve l'ancienne interface** jusqu'à ce que la nouvelle soit prête :

```jsx
const [enAttente, startTransition] = useTransition();
function aller(url) {
  startTransition(() => setPage(url));     // l'ancienne page reste affichée ; `enAttente` indique le chargement
}
<div style={{ opacity: enAttente ? 0.6 : 1 }}><Page url={page} /></div>
```

Le **routage** des frameworks utilise des transitions par défaut. **`useDeferredValue`** offre un effet comparable pour une **valeur** (affiche l'ancienne valeur pendant que la nouvelle charge).

### 17.6 Réinitialiser une frontière : `key`

```jsx
<Suspense key={idArticle} fallback={<Squelette />}>
  <Article id={idArticle} />
</Suspense>
```

Changer la `key` force le **retour au fallback** pour chaque nouvel article (au lieu de conserver l'ancien contenu).

### 17.7 Éviter les cascades (« waterfalls »)

Si un composant enfant ne démarre sa requête **qu'après** que le parent a fini la sienne, les attentes **s'additionnent**. Remèdes : **lancer les requêtes en parallèle** le plus tôt possible (au niveau de la route / du loader), **précharger**, regrouper côté serveur, **`Promise.all`**.

### 17.8 Suspense et rendu serveur

- **Streaming** : le serveur envoie d'abord le **shell** (HTML avec les fallbacks), puis **diffuse** chaque portion au fur et à mesure qu'elle est prête (`renderToPipeableStream` / `renderToReadableStream`).
- **Hydratation sélective** : chaque frontière Suspense s'hydrate **indépendamment** ; si l'utilisateur interagit avec une partie non encore hydratée, React **la priorise**.
- Les **erreurs** serveur dans une frontière peuvent **basculer** cette partie en rendu client sans casser la page.

### 17.9 Effets et Suspense

- Les **effets** d'un sous-arbre suspendu **ne s'exécutent pas** tant qu'il n'est pas révélé.
- Si un sous-arbre déjà affiché est de nouveau masqué par un fallback, ses **effets de layout** sont nettoyés puis relancés à la réapparition (l'état est conservé).

### 17.10 Concevoir de bons fallbacks

- Préférer des **squelettes** (même gabarit que le contenu) à des spinners génériques (réduit le **CLS**).
- Éviter les **flashs** : pour des attentes brèves, laisser les transitions masquer le fallback.
- **Accessibilité** : annoncer l'état de chargement (`aria-busy`, région `aria-live="polite"`).

### 17.11 Comment une source « suspend » : le mécanisme

React ne sait rien des requêtes réseau : il comprend seulement une **promesse** (plus exactement un *thenable*) lancée ou lue pendant le rendu.

1. Pendant le rendu, `use(promesse)` examine l'état de la promesse.
2. **En attente** : React **interrompt** le rendu du composant (c'est la « suspension ») et cherche le `<Suspense>` le plus proche pour afficher son `fallback`.
3. **Résolue** : `use` retourne la valeur, le rendu continue.
4. **Rejetée** : `use` **lève l'erreur**, interceptée par le **Error Boundary** le plus proche (chapitre 18).
5. Quand la promesse se résout, React **retente** le rendu de la frontière.

**Condition essentielle** : React identifie la ressource par l'**identité de la promesse**. Si le composant crée une **nouvelle** promesse à chaque tentative, il ne verra jamais de résultat stable et recommencera sans fin. D'où la règle : **la promesse vient d'un cache** (bibliothèque de données, framework) ou d'un **parent** (notamment un Server Component) ; elle n'est jamais créée dans le rendu d'un composant client.

### 17.12 Mettre en cache les promesses

Un cache minimal, pour comprendre le principe (en production, utilisez TanStack Query, SWR, Relay ou les chargeurs de votre routeur) :

```jsx
const cache = new Map();

export function chargerUtilisateur(id) {
  if (!cache.has(id)) {
    cache.set(id, fetch(`/api/utilisateurs/${id}`).then(r => r.json()));
  }
  return cache.get(id);                    // même promesse tant que la clé est connue
}

function Profil({ id }) {
  const utilisateur = use(chargerUtilisateur(id));
  return <h2>{utilisateur.nom}</h2>;
}
```

Un tel cache pose des questions que les bibliothèques résolvent : **invalidation** (quand rafraîchir ?), **expiration**, **déduplication** des requêtes simultanées, **gestion des erreurs** (ne pas garder une promesse rejetée), **mémoire** (suppression des entrées inutilisées).

Côté serveur, la fonction **`cache`** de React (réservée aux Server Components) **mémoïse un appel pendant la durée d'une requête** : plusieurs composants appelant `getUtilisateur(id)` partagent un seul résultat.

```jsx
import { cache } from 'react';
export const getUtilisateur = cache(async id => db.utilisateurs.trouver(id));
```

### 17.13 Précharger : code, données et ressources

Plus on **anticipe**, moins l'utilisateur voit de fallback.

- **Code** : lancer `import('./Editeur')` au **survol** ou à la **prise de focus** d'un lien/bouton ; le module est alors en cache quand `lazy` en a besoin.
- **Données** : démarrer la requête **avant** le rendu qui en a besoin (au clic, dans le chargeur de la route, au survol d'un lien) et **passer la promesse** au composant.
- **Ressources** : React 19 expose, dans `react-dom`, des fonctions d'indication au navigateur : **`preload`** (télécharger une ressource tôt : police, image, script), **`preinit`** (la charger et l'exécuter), **`preconnect`** et **`prefetchDNS`** (préparer la connexion).

```jsx
import { preload, preconnect } from 'react-dom';

function Galerie() {
  preconnect('https://cdn.exemple.org');
  preload('https://cdn.exemple.org/hero.avif', { as: 'image' });
  return <Hero />;
}
```

Les **routeurs** et méta-frameworks proposent un préchargement automatique des routes visibles ou survolées (`prefetch`) : exploitez-le avant d'écrire votre propre logique.

### 17.14 Streaming du rendu serveur et hydratation sélective

Avec le rendu serveur en **flux** (`renderToPipeableStream`, `renderToReadableStream`), les frontières Suspense deviennent des **points de livraison** progressive :

1. le serveur envoie d'abord la **coquille** (*shell*) : tout ce qui n'est pas suspendu, avec les `fallback` à la place des zones en attente ;
2. quand les données d'une zone sont prêtes, le serveur envoie **ce bloc HTML** et un petit script qui le **substitue** au fallback ;
3. côté client, React **hydrate** les frontières **indépendamment** (hydratation sélective) : une zone déjà prête peut devenir interactive pendant qu'une autre charge encore.

Si l'utilisateur interagit avec une zone **pas encore hydratée**, React **hydrate cette zone en priorité**.

Côté serveur, deux callbacks pilotent le moment d'envoi : `onShellReady` (coquille prête, flux de lecture **progressive**, idéal pour les utilisateurs) et `onAllReady` (tout est prêt, adapté aux **robots d'indexation** ou à la génération statique). Une erreur survenue **après** l'envoi de la coquille ne peut plus changer le **code de statut HTTP** : prévoyez un repli côté client.

### 17.15 Ordre d'apparition et stabilité visuelle

- **Séquence de révélation.** Quand plusieurs frontières sœurs se résolvent à des moments différents, elles apparaissent **dans l'ordre d'arrivée**, ce qui peut produire un affichage désordonné. Pour réduire cet effet, **regroupez** dans une même frontière les zones qui doivent apparaître ensemble.
- **Limitation des fallbacks.** React **espace** légèrement l'apparition de fallbacks successifs pour éviter le scintillement : vous n'avez pas à ajouter vous-même de délais artificiels.
- **Décalages de mise en page** (*layout shift*). Donnez au squelette les **dimensions** du contenu final (hauteur minimale, ratio d'image) pour que l'arrivée des données ne déplace rien : l'indicateur Core Web Vitals **CLS** s'en trouve amélioré.
- **Liste ordonnée de frontières** : une API de coordination (`SuspenseList`) a été explorée mais reste **expérimentale** ; ne l'utilisez pas en production sans vérifier la documentation de votre version.

### 17.16 Accessibilité et expérience de chargement

- Signalez le chargement par un texte ou **`aria-busy="true"`** sur la zone concernée, pas seulement par une animation.
- Pour un chargement long, placez un **message textuel** (« Chargement des résultats… ») dans une **région vivante** (`role="status"`) présente dès le départ.
- Respectez **`prefers-reduced-motion`** : désactivez ou atténuez les animations de squelette.
- Quand le contenu remplace le fallback, **ne déplacez pas le focus** sans raison ; si l'élément ayant le focus disparaît, replacez-le sur un élément pertinent.

### 17.17 Récupérer d'un échec de chargement de code

Un `lazy` peut échouer (réseau coupé, **nouvelle version** déployée dont les fichiers de l'ancienne ont disparu). Une enveloppe de **nouvelle tentative**, associée à un Error Boundary, améliore la robustesse :

```jsx
function lazyAvecReprise(importer, tentatives = 3) {
  return lazy(async () => {
    for (let i = 0; ; i++) {
      try { return await importer(); }
      catch (e) {
        if (i + 1 >= tentatives) throw e;
        await new Promise(r => setTimeout(r, 500 * (i + 1)));   // attente croissante
      }
    }
  });
}

const Editeur = lazyAvecReprise(() => import('./Editeur'));
```

Après plusieurs échecs, proposez à l'utilisateur de **recharger la page** : c'est la réponse habituelle à un décalage de version.

### 17.18 Tester Suspense

```jsx
render(
  <Suspense fallback={<p>Chargement…</p>}>
    <Profil id={1} />
  </Suspense>
);
expect(screen.getByText('Chargement…')).toBeInTheDocument();
expect(await screen.findByRole('heading', { name: 'Alice' })).toBeInTheDocument();
```

- Utilisez les requêtes **asynchrones** (`findBy…`, `waitFor`) : le contenu final arrive après la résolution.
- Fournissez des **promesses contrôlées** (résolues ou rejetées à la demande) pour tester chacun des trois états.
- Entourez le composant d'un **Error Boundary** de test pour vérifier le chemin d'erreur.
- Un composant `lazy` demande un `await` avant d'apparaître : pas de `getBy…` immédiat.

### 17.19 Pièges fréquents

- Attendre que `Suspense` détecte une requête faite dans `useEffect`.
- Définir `lazy` à l'intérieur d'un composant.
- `lazy` sur un module sans export par défaut.
- Frontière unique trop haute (page blanche avec spinner) ou trop nombreuse (effet pop-corn).
- Promesse recréée à chaque rendu avec `use`.
- Oublier l'**Error Boundary** autour de `lazy`/`use` (une promesse rejetée remonte en erreur).

### Synthèse du chapitre 17

**Suspense = fallback pendant l'attente** de code ou de données **compatibles** ; **`lazy`** pour le code, **`use` / frameworks / bibliothèques** pour les données ; **Transitions** : conserver l'ancienne UI ; **`key`** : réinitialiser ; Placer les frontières selon l'**expérience** ; **paralléliser** les requêtes ; **streaming** + **hydratation sélective** côté serveur.

---

## 18. Error Boundaries

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : comprendre comment React propage les erreurs de rendu et comment les contenir ; écrire (ou utiliser) des Error Boundaries et savoir ce qu'ils capturent ou non ; mettre en place une stratégie : granularité, réinitialisation, journalisation.

### 18.1 Problème

Par défaut, **une erreur levée pendant le rendu** (dans le corps d'un composant, un hook, un reducer, un constructeur) **fait planter l'application entière** : React **démonte tout l'arbre** (écran blanc).

### 18.2 Définition

Un **Error Boundary** (« frontière d'erreur ») est un **composant** qui **intercepte les erreurs** survenant **dans ses descendants** pendant le rendu, les cycles de vie et les constructeurs, **journalise** l'erreur et affiche une **interface de secours** (*fallback*), au lieu de laisser tout l'arbre se démonter.

> Il **doit être un composant classe** (aucun équivalent en hook n'existe), mais il est possible d'utiliser une **bibliothèque** pour éviter d'écrire la classe.

### 18.3 Écriture d'une frontière

```jsx
import { Component } from 'react';

class ErrorBoundary extends Component {
  state = { erreur: null };

  // Phase de rendu : mettre à jour l'état pour afficher le fallback au prochain rendu
  static getDerivedStateFromError(erreur) {
    return { erreur };
  }

  // Phase de commit : effets de bord (journalisation)
  componentDidCatch(erreur, info) {
    console.error(erreur, info.componentStack);
    envoyerAuService(erreur, info);          // Sentry, Datadog, etc.
  }

  reinitialiser = () => this.setState({ erreur: null });

  render() {
    if (this.state.erreur) {
      return this.props.fallback ?? (
        <div role="alert">
          <p>Une erreur est survenue.</p>
          <button onClick={this.reinitialiser}>Réessayer</button>
        </div>
      );
    }
    return this.props.children;
  }
}

<ErrorBoundary fallback={<p>Impossible d'afficher ce widget.</p>}>
  <Widget />
</ErrorBoundary>
```

| Méthode | Rôle |
|---|---|
| `static getDerivedStateFromError(error)` | Appelée pendant le **rendu** ; retourne le **nouvel état** pour afficher le fallback. Doit être **pure**. |
| `componentDidCatch(error, info)` | Appelée au **commit** ; pour **journaliser** (`info.componentStack`). |

### 18.4 La bibliothèque `react-error-boundary`

```jsx
import { ErrorBoundary, useErrorBoundary } from 'react-error-boundary';

function Fallback({ error, resetErrorBoundary }) {
  return (
    <div role="alert">
      <p>Erreur : {error.message}</p>
      <button onClick={resetErrorBoundary}>Réessayer</button>
    </div>
  );
}

<ErrorBoundary
  FallbackComponent={Fallback}
  onError={(erreur, info) => journaliser(erreur, info)}
  onReset={() => invalidateQueries()}
  resetKeys={[idUtilisateur]}              // réinitialise automatiquement si ces valeurs changent
>
  <Profil id={idUtilisateur} />
</ErrorBoundary>

// Remonter une erreur asynchrone ou d'événement vers la frontière
function Bouton() {
  const { showBoundary } = useErrorBoundary();
  return <button onClick={async () => { try { await action(); } catch (e) { showBoundary(e); } }}>Go</button>;
}
```

### 18.5 Ce qu'une frontière capture… et ne capture pas

#### Capturé

- Erreurs **pendant le rendu** des descendants.
- Erreurs dans les **méthodes de cycle de vie** et **constructeurs** des composants classes enfants.
- Erreurs dans les **hooks** (y compris `useMemo`, reducers).
- Promesses **rejetées lues par `use`** (renvoyées comme erreurs de rendu).
- Erreurs d'un composant `lazy` dont le chargement échoue.

#### Non capturé

| Cas | Traitement recommandé |
|---|---|
| **Gestionnaires d'événements** (`onClick`) | `try/catch` + mettre l'erreur dans le **state**, ou `showBoundary` |
| **Code asynchrone** (`setTimeout`, `fetch().then`) | `try/catch` / `.catch` + état d'erreur |
| **Effets** (`useEffect`) : le code asynchrone | `try/catch` |
| **Rendu côté serveur** (SSR) | Gestion par les API serveur (`onError`, `onShellError`) |
| **Erreurs dans la frontière elle-même** | Une frontière **parente** doit les capturer |

> Un « truc » : lancer l'erreur depuis un **setState** pour la faire remonter comme erreur de rendu :
> `setEtat(() => { throw erreur; })`.

### 18.6 Stratégie de placement (granularité)

| Niveau | Rôle |
|---|---|
| **Racine** | Dernier rempart : page d'erreur générique avec recharger/contact |
| **Par route / page** | Une erreur dans une page n'empêche pas la navigation |
| **Par zone fonctionnelle** (widget, panneau) | Le reste de la page continue de fonctionner |
| **Autour de contenus tiers ou instables** | Isoler les risques |

Évitez la frontière unique à la racine seulement : l'expérience utilisateur sera brutale.

### 18.7 Réinitialisation (*reset*)

Après une erreur, la frontière garde son état d'erreur. Pour réessayer :
- **bouton** « Réessayer » appelant `reset` ;
- **`resetKeys`** (react-error-boundary) ou **`key`** sur la frontière lorsque les entrées changent (navigation) ;
- combiner avec la **réinitialisation du cache** de requêtes (`QueryErrorResetBoundary` de TanStack Query).

### 18.8 Journalisation et observabilité

- Envoyez `error`, `componentStack`, l'**utilisateur**, la **version** et la **route** à un service (**Sentry**, **Datadog**, **LogRocket**…).
- Activez les **source maps** en production.
- React 19 expose `onCaughtError` (erreur capturée par une frontière), `onUncaughtError` (non capturée) et `onRecoverableError` sur `createRoot` / `hydrateRoot` : **un seul** endroit centralisé pour journaliser.

```jsx
createRoot(racine, {
  onCaughtError:   (erreur, info) => journaliser('caught', erreur, info.componentStack),
  onUncaughtError: (erreur, info) => journaliser('uncaught', erreur, info.componentStack),
  onRecoverableError: (erreur) => journaliser('recoverable', erreur),
});
```

> React 19 **ne journalise plus deux fois** la même erreur (suppression des doublons).

### 18.9 Interaction avec Suspense

- Une **promesse rejetée** (`lazy`, `use`) devient une **erreur de rendu** : elle est interceptée par la **frontière d'erreur la plus proche**.
- Schéma courant : `<ErrorBoundary><Suspense fallback={…}><Composant /></Suspense></ErrorBoundary>` (erreur **autour** de l'attente).

### 18.10 Les options d'erreur de la racine (React 19)

`createRoot` et `hydrateRoot` acceptent trois **callbacks globaux** qui centralisent le signalement des erreurs :

```jsx
import { createRoot } from 'react-dom/client';

createRoot(document.getElementById('root'), {
  onCaughtError(erreur, infos) {
    // Capturée par un Error Boundary
    journaliser('capturée', erreur, infos.componentStack);
  },
  onUncaughtError(erreur, infos) {
    // Aucune frontière : l'arbre entier est démonté
    journaliser('non capturée', erreur, infos.componentStack);
  },
  onRecoverableError(erreur, infos) {
    // Erreur dont React s'est remis seul (ex. incohérence d'hydratation)
    journaliser('récupérable', erreur, infos.componentStack);
  },
}).render(<App />);
```

Depuis React 19, une erreur de rendu n'est **plus relancée en double** : elle est signalée **une fois**, par l'un de ces callbacks. Cela simplifie la connexion à un service de supervision.

### 18.11 Faire remonter ce que les frontières ne voient pas

Les frontières ne capturent que les erreurs levées **pendant le rendu** (et dans les méthodes de cycle de vie). Pour les erreurs survenant dans un **gestionnaire d'événement** ou du code **asynchrone**, deux stratégies existent.

**1. Gérer localement** : `try/catch` et état d'erreur affiché dans l'interface (adapté à un envoi de formulaire, par exemple).

**2. Déléguer à la frontière la plus proche** : relancer l'erreur pendant un rendu.

```jsx
function useLancerErreur() {
  const [, setEtat] = useState();
  return erreur => setEtat(() => { throw erreur; });   // l'erreur est levée pendant le rendu
}

function Bouton() {
  const lancer = useLancerErreur();
  return <button onClick={() => charger().catch(lancer)}>Charger</button>;
}
```

La bibliothèque `react-error-boundary` fournit ce mécanisme prêt à l'emploi : `const { showBoundary } = useErrorBoundary();`.

**Filets globaux** (en complément, pas en remplacement) : `window.addEventListener('error', …)` et `window.addEventListener('unhandledrejection', …)` pour journaliser ce qui échappe à tout le reste.

### 18.12 Concevoir un bon écran d'erreur

Un repli utile répond à trois questions de l'utilisateur : **que s'est-il passé ? est-ce grave ? que puis-je faire ?**

- **Message clair, sans jargon**, sans trace technique ni détail sensible.
- **Action de reprise** : « Réessayer » (réinitialise la frontière), « Retour à l'accueil », « Recharger la page ».
- **Identifiant d'incident** affichable pour le support (le même que celui envoyé au service de supervision).
- **Différencier** les cas : réseau indisponible (réessayer plus tard), accès refusé (se reconnecter), ressource introuvable (lien de retour), erreur inattendue (signalement).
- **Accessibilité** : donnez au conteneur `role="alert"` pour que l'erreur soit annoncée, et déplacez le focus sur le message ou sur le bouton de reprise.

```jsx
function RepliErreur({ error, resetErrorBoundary }) {
  return (
    <div role="alert">
      <h2>Un problème est survenu</h2>
      <p>Cette section n'a pas pu s'afficher. Vos autres données ne sont pas affectées.</p>
      <button onClick={resetErrorBoundary}>Réessayer</button>
    </div>
  );
}
```

### 18.13 Stratégies de reprise

| Situation | Reprise recommandée |
| --- | --- |
| Erreur transitoire (réseau, délai dépassé) | Bouton « Réessayer » qui appelle `resetErrorBoundary`, éventuellement avec **attente croissante** |
| Erreur liée à des données précises | `resetKeys={[id]}` : la frontière se réinitialise quand l'identifiant change |
| Erreur dans une page de routeur | Placer la frontière **par route** : la navigation vers une autre route la remet à zéro |
| Chargement de code échoué (nouvelle version déployée) | **Recharger la page** |
| Erreur de rendu permanente (bug) | Afficher le repli, **journaliser**, ne pas boucler sur les tentatives |

Une réinitialisation **remonte** le sous-arbre : l'état local de ses composants est **perdu**. Remontez dans un parent l'état qui doit survivre.

### 18.14 Frontières dans les frameworks

Les méta-frameworks intègrent la notion de frontière **par route**, ce qui évite d'écrire la classe à la main :

- **Next.js (App Router)** : un fichier `error.js` définit le repli d'un segment (composant client recevant `error` et `reset`) ; `global-error.js` gère les erreurs de la racine ; `not-found.js` traite les ressources absentes. Les erreurs levées dans un Server Component reçoivent un **identifiant (`digest`)** : le détail reste dans les journaux serveur et n'est pas envoyé au navigateur.
- **React Router (mode framework / data router)** : chaque route peut exporter un composant `ErrorBoundary` ; les erreurs des chargeurs et des actions y sont acheminées.

Dans tous les cas, ces mécanismes **s'ajoutent** aux frontières que vous placez autour de **zones fonctionnelles** (widget, panneau, éditeur).

### 18.15 Supervision et confidentialité

- Envoyez à un service de supervision (Sentry, Datadog, Rollbar…) : le **message**, la **pile**, la **pile de composants** (`componentStack`), la **version** de l'application, la **route** et un identifiant de session **anonymisé**.
- **Filtrez les données personnelles** (identifiants, jetons, contenu de formulaires) avant l'envoi.
- Utilisez les **cartes de sources** (*source maps*) pour lire des piles lisibles, en les **réservant** à l'outil de supervision plutôt qu'en les exposant publiquement.
- Évitez le **bruit** : regroupez les erreurs identiques, ignorez celles des extensions de navigateur, échantillonnez si nécessaire.

### 18.16 Tester une frontière

```jsx
function Bombe() { throw new Error('boum'); }

test('affiche le repli quand un enfant lève une erreur', () => {
  const espion = vi.spyOn(console, 'error').mockImplementation(() => {});   // masque le bruit attendu
  render(
    <ErrorBoundary fallback={<p role="alert">Erreur</p>}>
      <Bombe />
    </ErrorBoundary>
  );
  expect(screen.getByRole('alert')).toHaveTextContent('Erreur');
  espion.mockRestore();
});
```

Testez aussi : la **réinitialisation** (le bouton « Réessayer » restitue le contenu après correction), l'**appel du journal** (le callback `onError` reçoit l'erreur) et le fait qu'un composant **hors** de la frontière n'est pas affecté.

### 18.17 Pièges fréquents

- Compter sur une frontière pour les erreurs dans `onClick` ou `fetch`.
- Une seule frontière à la racine.
- Frontière **sans** possibilité de réessayer.
- Journaliser dans `getDerivedStateFromError` (effets de bord interdits) au lieu de `componentDidCatch`.
- Afficher `error.message` brut à l'utilisateur final (fuite d'informations) : l'afficher en développement seulement.
- Oublier de **réinitialiser** après navigation (la page suivante reste en erreur).

### Synthèse du chapitre 18

Erreur de rendu non capturée = **écran blanc** ; **Error Boundary** = confinement + fallback ; **Classe** requise → utilisez **`react-error-boundary`** ; Ne capture **pas** événements, async, SSR → `try/catch` + état ; Frontières **granulaires**, **réinitialisables**, **journalisées**.

---

## 19. Portals

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : comprendre pourquoi et comment rendre du contenu **hors** de la hiérarchie DOM du parent ; maîtriser la propagation des événements et du contexte à travers un portail ; implémenter modales et popovers accessibles.

### 19.1 Définition

Un **Portal** permet de rendre des enfants dans **un nœud DOM situé ailleurs** dans le document (typiquement `document.body`), tout en conservant leur **place logique** dans l'arbre React.

```jsx
import { createPortal } from 'react-dom';

createPortal(enfants, noeudDom, cle?)
```

```jsx
function Modale({ ouvert, onFermer, children }) {
  if (!ouvert) return null;
  return createPortal(
    <div className="surcouche" onClick={onFermer}>
      <div role="dialog" aria-modal="true" className="modale" onClick={e => e.stopPropagation()}>
        {children}
        <button onClick={onFermer}>Fermer</button>
      </div>
    </div>,
    document.body
  );
}
```

### 19.2 Pourquoi un portail ?

Les éléments qui doivent **sortir visuellement** de leur conteneur sont gênés par le CSS des ancêtres : `overflow: hidden`, `transform`, `z-index`/contexte d'empilement, `position`. Cas d'usage :

- **Modales** / boîtes de dialogue ;
- **Info-bulles** (tooltips), **popovers**, **menus déroulants** ;
- **Notifications** (toasts) ;
- **Menus contextuels**, **lightbox** ;
- Rendu dans un **autre document/iframe** ou un nœud géré hors React.

### 19.3 Comportement : le DOM sort, l'arbre React reste

Même si le nœud est ailleurs dans le DOM :

- **Le contexte** React traverse le portail (les consommateurs voient les mêmes valeurs).
- **Les événements se propagent** (*bubbling*) selon l'**arbre React**, pas selon l'arbre DOM : un clic dans un portail **remonte** aux ancêtres React, y compris ceux qui ne contiennent pas le nœud dans le DOM. Utile (un `onClick` du parent capte les clics de la modale) mais parfois surprenant : utilisez `e.stopPropagation()` si nécessaire.
- **L'état** et les **effets** suivent le cycle normal du composant.
- Le CSS **hérité** du parent **ne s'applique pas** (le DOM est ailleurs) : style via classes globales/variables CSS.

### 19.4 Cible du portail

- `document.body` (le plus simple) ;
- un conteneur **dédié** `<div id="modales">` dans `index.html` ;
- **SSR** : `document` n'existe pas côté serveur → ne créer le portail qu'**après le montage** :

```jsx
function PortailClient({ children }) {
  const [monte, setMonte] = useState(false);
  useEffect(() => setMonte(true), []);
  return monte ? createPortal(children, document.body) : null;
}
```

> Ne pas utiliser comme cible un nœud **rendu par React** que React pourrait mettre à jour/supprimer.

### 19.5 Accessibilité d'une modale (indispensable)

1. **Rôle** : `role="dialog"` (ou `alertdialog`), `aria-modal="true"`, `aria-labelledby` (titre), `aria-describedby`.
2. **Gestion du focus** : déplacer le focus **dans** la modale à l'ouverture ; **piéger** le focus (Tab/Shift+Tab bouclent) ; **restaurer** le focus sur l'élément déclencheur à la fermeture.
3. **Fermeture au clavier** : touche **Échap**.
4. **Contenu d'arrière-plan** inerte : attribut **`inert`** sur le reste de la page, ou `aria-hidden`.
5. **Bloquer le défilement** du `body` pendant l'ouverture.
6. Cliquer sur la **surcouche** ferme (si approprié).

#### Alternatives natives

- **`<dialog>`** avec `showModal()` : focus piégé, Échap, couche supérieure (*top layer*), arrière-plan inerte **fournis par le navigateur** — souvent **sans portail** nécessaire.
- **Popover API** (`popover`, `popovertarget`) pour tooltips/menus.
- **Bibliothèques accessibles** : Radix UI (`Dialog`, `Popover`), React Aria, Headless UI, Floating UI (positionnement).

```jsx
function Dialogue({ ouvert, onFermer, children }) {
  const ref = useRef(null);
  useEffect(() => {
    const d = ref.current;
    if (ouvert && !d.open) d.showModal();
    if (!ouvert && d.open) d.close();
  }, [ouvert]);
  return <dialog ref={ref} onClose={onFermer}>{children}</dialog>;
}
```

### 19.6 Signature complète et règles de l'API

```jsx
import { createPortal } from 'react-dom';

createPortal(children, domNode, key?)
```

- **`children`** : tout ce que React sait rendre (élément JSX, fragment, chaîne, tableau, composant instancié).
- **`domNode`** : un **nœud DOM existant** (`document.body`, un conteneur, un élément d'un autre document). Il doit exister **au moment du rendu** ; pour un nœud qui dépend d'une `ref`, attendez le montage.
- **`key`** (facultatif) : identifiant de la clé du portail, utile quand on en rend plusieurs au même niveau.
- Valeur de retour : un **nœud React** à placer dans le JSX comme n'importe quel élément.

`createPortal` n'est **pas** un Hook ni un composant : on l'appelle pendant le rendu. Il vit dans **`react-dom`** (et non dans `react`) parce qu'il dépend du DOM du navigateur ; React Native possède son propre équivalent de rendu hors hiérarchie.

> **Ne ciblez pas un nœud géré par React.** Si `domNode` est un élément que React rend lui-même et peut supprimer ou mettre à jour, vous obtiendrez des erreurs de réconciliation. Ciblez `document.body` ou un conteneur **statique** défini dans `index.html`.

### 19.7 Les événements à travers un portail, en détail

React 17 et suivants attachent leurs écouteurs d'événements à la **racine** (le conteneur passé à `createRoot`) et rejouent la propagation selon l'**arbre de composants React**. Pour un portail, cela produit deux comportements qu'il faut distinguer.

| Mécanisme | Suit quel arbre ? | Conséquence |
| --- | --- | --- |
| Événements **React** (`onClick`, `onKeyDown`…) | Arbre **React** | Un clic dans la modale remonte au `onClick` du composant parent, même si le DOM est ailleurs |
| Événements **natifs** (`addEventListener` sur un ancêtre DOM) | Arbre **DOM** | Un écouteur posé sur le conteneur du parent **ne reçoit pas** les événements de la modale |
| **Contexte** | Arbre React | Les valeurs de contexte du parent sont visibles dans le portail |
| **CSS hérité** (`color`, `font-family`) | Arbre DOM | Le portail n'hérite **pas** des styles du parent |

**Application : détecter un clic « à l'extérieur ».** Le motif courant `ref.current.contains(event.target)` échoue avec un portail : le contenu du portail n'est **pas** dans le sous-arbre DOM de `ref.current`.

```jsx
function useClicExterieur(refs, rappel) {
  useEffect(() => {
    function gerer(e) {
      const dedans = refs.some(r => r.current?.contains(e.target));
      if (!dedans) rappel(e);
    }
    document.addEventListener('pointerdown', gerer);
    return () => document.removeEventListener('pointerdown', gerer);
  }, [refs, rappel]);
}
// On passe la ref du déclencheur ET celle du contenu du portail.
```

**Arrêter la propagation à bon escient.** `e.stopPropagation()` dans le portail empêche le clic de remonter aux ancêtres React (par exemple un parent cliquable). Réservez-le aux cas où le comportement est réellement indésirable : il peut gêner d'autres écouteurs (analytique, fermeture de menus).

### 19.8 Positionner une info-bulle ou un menu

Un tooltip rendu dans `document.body` doit être **positionné manuellement** par rapport à son déclencheur, puisque le CSS du parent ne s'applique plus. La démarche :

1. mesurer le déclencheur avec `getBoundingClientRect()` ;
2. calculer les coordonnées (`top`, `left`) de la bulle, en tenant compte du défilement de la page (`window.scrollX` / `scrollY` si position `absolute`) ;
3. mesurer **avant la peinture** pour éviter un « saut » visuel : `useLayoutEffect` ;
4. recalculer au redimensionnement et au défilement.

```jsx
function InfoBulle({ cible, children }) {
  const ref = useRef(null);
  const [pos, setPos] = useState({ top: 0, left: 0 });

  useLayoutEffect(() => {
    const r = cible.current.getBoundingClientRect();
    setPos({ top: r.bottom + window.scrollY + 8, left: r.left + window.scrollX });
  }, [cible]);

  return createPortal(
    <div ref={ref} role="tooltip" style={{ position: 'absolute', ...pos }}>
      {children}
    </div>,
    document.body
  );
}
```

Dans un projet réel, **ne réécrivez pas** la logique de positionnement : collisions avec le bord de l'écran, retournement automatique, flèche, défilement dans des conteneurs imbriqués sont délicats. Utilisez **Floating UI** (ou les composants Radix UI / React Aria / Headless UI qui l'emploient).

### 19.9 Conteneurs dédiés, empilement et notifications

- **Conteneur dédié.** Ajoutez dans `index.html` un nœud `<div id="portails"></div>` et ciblez-le avec `document.getElementById('portails')`. Cela isole les couches flottantes, facilite le style et évite de polluer `body`.
- **Empilement** (*stacking*). Plusieurs modales ouvertes simultanément doivent s'empiler dans le bon ordre. Maintenez une **pile** (dans un contexte ou un store) et n'appliquez le piégeage du focus et l'inertie qu'à la **modale du dessus**. Les éléments en **couche supérieure** (`<dialog>` modal, API Popover) s'empilent d'eux-mêmes sans `z-index`.
- **Notifications** (*toasts*). Rendez-les dans une **région vivante** persistante (`role="status"` ou `aria-live="polite"`), présente dès le chargement de la page, afin que les lecteurs d'écran annoncent chaque nouveau message. Prévoyez une durée suffisante et un moyen de les fermer au clavier.
- **Défilement.** Pendant qu'une modale est ouverte, bloquez le défilement de l'arrière-plan (`overflow: hidden` sur `body`, en compensant la disparition de la barre de défilement) et **rétablissez-le** dans le nettoyage de l'effet.

### 19.10 Portails, rendu serveur et hydratation

Le serveur n'a pas de `document` : les portails ne sont **pas pris en charge** par le rendu serveur (`renderToString`, `renderToPipeableStream`). Rendez-les **uniquement côté client**, après le montage. Outre le motif `useState` + `useEffect` vu en 19.4, le Hook `useSyncExternalStore` fournit une détection **sûre pour l'hydratation** :

```jsx
const vide = () => () => {};
function useEstClient() {
  return useSyncExternalStore(vide, () => true, () => false);  // client, client, serveur
}

function PortailClient({ children }) {
  return useEstClient() ? createPortal(children, document.body) : null;
}
```

Une modale **fermée** n'a de toute façon rien à rendre : le problème ne se pose que pour un portail **ouvert dès le premier rendu**.

### 19.11 Rendre dans une iframe ou un autre document

Un portail peut cibler le `body` du document d'une **iframe** (`iframe.contentDocument.body`). Cela sert à l'**aperçu isolé** (éditeur de gabarits, prévisualisation responsive, widgets embarqués). Précautions :

- les **feuilles de style** de la page parente ne sont pas disponibles dans l'iframe : copiez-les ou injectez les vôtres ;
- l'iframe doit être **chargée** avant de lire son `contentDocument` ;
- les événements restent gérés par React, mais le `window` et le `document` de référence changent : utilisez `e.target.ownerDocument` plutôt que le `document` global.

### 19.12 Tester un portail

React Testing Library interroge par défaut `document.body` : le contenu d'un portail est donc **trouvable** comme le reste.

```jsx
render(<Page />);
await userEvent.click(screen.getByRole('button', { name: /ouvrir/i }));
expect(screen.getByRole('dialog', { name: /confirmation/i })).toBeInTheDocument();

await userEvent.keyboard('{Escape}');
expect(screen.queryByRole('dialog')).not.toBeInTheDocument();
```

Vérifiez aussi le **focus** (`expect(document.activeElement)`), la **restitution du focus** après fermeture et l'absence de fuite : après le démontage, le nœud du portail ne doit plus être dans le document.

### 19.13 Portail, `<dialog>`, Popover : que choisir ?

| Besoin | Meilleur choix | Raison |
| --- | --- | --- |
| Modale bloquante | `<dialog>` + `showModal()` | Focus piégé, Échap, arrière-plan inerte, couche supérieure, natifs |
| Menu ou info-bulle ancré à un élément | **Popover API** + positionnement (CSS Anchor Positioning ou Floating UI) | Fermeture par clic extérieur et Échap natives |
| Contenu qui doit échapper à `overflow` / `transform` d'un ancêtre | **`createPortal`** | Sort du contexte d'empilement et de rognage |
| Toasts globaux | Portail vers une **région vivante** dédiée | Ordre et annonces maîtrisés |
| Composant accessible complet sans effort | Radix UI, React Aria, Headless UI | Focus, clavier et ARIA déjà gérés |

Règle de décision : **commencez par l'élément natif** ; recourez à un portail quand la hiérarchie DOM du parent pose un problème de rognage ou d'empilement que le natif ne résout pas.

### 19.14 Pièges fréquents

- Portail sans gestion du **focus** et du clavier.
- Oublier que les événements remontent selon l'**arbre React**.
- Utiliser `document` pendant le rendu serveur.
- Problèmes d'**empilement** (`z-index`) → préférer la **couche supérieure** (`<dialog>`, popover).
- Style qui dépend de sélecteurs d'ancêtres (ne s'applique plus).
- Cible de portail supprimée avant le démontage du composant.

### Synthèse du chapitre 19

`createPortal(enfants, noeud)` : DOM **ailleurs**, arbre React **inchangé** (contexte, événements, état) ; Cas d'usage : **modales, tooltips, menus, toasts** ; **Accessibilité** : rôle, focus, Échap, inert ; envisagez **`<dialog>`** ou une **bibliothèque**.

---

## 20. Fragments

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : savoir grouper des éléments sans nœud DOM supplémentaire ; utiliser les `key` avec des fragments, et comprendre l'impact sur le DOM et le CSS.

### 20.1 Définition

Un **Fragment** (`<Fragment>`) permet de **retourner plusieurs éléments frères** depuis un composant **sans ajouter de nœud** au DOM.

```jsx
import { Fragment } from 'react';

function Colonnes() {
  return (
    <>                         {/* syntaxe courte = <Fragment> */}
      <td>Nom</td>
      <td>Prénom</td>
    </>
  );
}
```

### 20.2 Pourquoi pas une `<div>` ?

Un `<div>` supplémentaire peut **casser** :

- la **structure HTML valide** : `<tr>` → `<td>`, `<ul>` → `<li>`, `<dl>` → `<dt>/<dd>`, `<table>` ;
- une mise en page **flexbox / grid** (les éléments ne sont plus enfants directs du conteneur) ;
- les **sélecteurs CSS** (`>`), la sémantique/accessibilité, le **poids du DOM**.

### 20.3 Deux syntaxes

| Syntaxe | Accepte `key` ? | Usage |
|---|---|---|
| `<>…</>` | ❌ | Cas général |
| `<Fragment>…</Fragment>` | ✅ | **Listes** d'éléments multiples par item |

```jsx
{glossaire.map(el => (
  <Fragment key={el.id}>
    <dt>{el.terme}</dt>
    <dd>{el.definition}</dd>
  </Fragment>
))}
```

### 20.4 Autres équivalents

- **Retourner un tableau** (avec clés) : `return [<li key="a" />, <li key="b" />]`.
- **`null`** pour ne rien rendre.

### 20.5 Détails

- Un fragment **n'accepte pas d'autres props** que `key` (et, dans certaines versions expérimentales, des refs de fragment).
- Il **n'affecte pas** l'état : placer un composant dans un fragment ou le rendre directement dans la même position ne change pas son identité, mais **ajouter/retirer un niveau d'imbrication** (`<><A/></>` vs `<A/>` au même endroit) **peut** modifier la position structurelle dans certains cas de listes de frères (l'état est associé à la **position**).

### 20.6 Un peu d'histoire et de compatibilité

- **React 16.0** a permis de **retourner des tableaux et des chaînes** depuis un composant (avec clés pour les tableaux).
- **React 16.2** a introduit `<Fragment>` et la **syntaxe courte** `<>…</>`.
- La syntaxe courte nécessite un compilateur qui la comprend : **Babel 7+**, **TypeScript 2.6.2+**, **esbuild**, **SWC** ; elle est donc disponible dans tous les outils actuels. Avec l'**ancien** runtime JSX (`React.createElement`), elle est transformée en `React.Fragment` ; avec le **nouveau** runtime (`react/jsx-runtime`), l'import explicite de `React` n'est plus nécessaire.
- En TypeScript, les options `jsxFragmentFactory` (ancien runtime, pour Preact par exemple) et `jsx: "react-jsx"` (nouveau runtime) pilotent cette transformation.

### 20.7 Fragments, clés et listes

Un `Fragment` est le **seul** moyen d'attribuer une `key` à un **groupe** d'éléments retourné par un `map`. Sans clé, React avertit (*Each child in a list should have a unique key*) et ne peut pas réconcilier correctement les groupes lors des insertions, suppressions ou réordonnancements.

```jsx
function Tableau({ lignes }) {
  return (
    <table>
      <tbody>
        {lignes.map(l => (
          <Fragment key={l.id}>
            <tr><th scope="row">{l.nom}</th><td>{l.valeur}</td></tr>
            {l.detail && <tr className="detail"><td colSpan={2}>{l.detail}</td></tr>}
          </Fragment>
        ))}
      </tbody>
    </table>
  );
}
```

La clé appartient au **Fragment**, pas aux éléments intérieurs : les enfants du fragment n'ont pas besoin de clé tant qu'ils sont en nombre fixe.

### 20.8 Fragments et structure HTML valide

Le HTML impose des **relations parent-enfant strictes**. Un fragment permet de **découper** un tableau, une liste ou une liste de définitions en composants sans casser la structure.

| Parent | Enfants autorisés | Composant qui retourne un fragment |
| --- | --- | --- |
| `<table>` / `<tbody>` | `<tr>` | `<LigneAvecDetail />` → `<><tr/><tr/></>` |
| `<tr>` | `<td>`, `<th>` | `<Colonnes />` → `<><td/><td/></>` |
| `<ul>` / `<ol>` | `<li>` | `<Elements />` → `<><li/><li/></>` |
| `<dl>` | `<dt>`, `<dd>` | `<Terme />` → `<><dt/><dd/></>` |
| `<select>` | `<option>`, `<optgroup>` | `<Options />` → `<><option/><option/></>` |

Si un composant enveloppait ces éléments dans une `<div>`, le navigateur corrigerait le DOM de façon inattendue, et React signalerait un avertissement d'**imbrication invalide** (*validateDOMNesting*).

### 20.9 Fragments, CSS et mise en page

- **Flexbox et Grid.** Les propriétés `display: flex` ou `grid` s'appliquent aux **enfants directs** du conteneur. Un wrapper `<div>` inutile devient l'unique enfant et casse la disposition ; un fragment laisse les éléments **enfants directs**.
- **Sélecteurs enfants** (`ul > li`, `.liste > .carte`) cessent de fonctionner si un wrapper s'intercale.
- **`display: contents`** fait « disparaître » visuellement une boîte pour ses enfants, mais l'élément **reste dans le DOM** (et dans l'arbre d'accessibilité selon les navigateurs). Ce n'est pas un équivalent d'un fragment : préférez le fragment quand aucun élément n'est nécessaire.
- **Quand une vraie balise est préférable** : dès que vous devez appliquer un **style**, un **identifiant**, un attribut ARIA, un gestionnaire d'événement ou une **`ref`** à l'ensemble du groupe, un fragment ne convient pas (il n'a pas de nœud DOM).

### 20.10 Fragments et position dans l'arbre

React rattache l'état d'un composant à sa **position** dans l'arbre. Le fragment intervient dans cette règle de deux façons.

- **Fragment sans clé retourné directement par un composant** (au sommet du `return`) : React le traite comme s'il s'agissait de la **liste de ses enfants**. Passer de `return <A />` à `return <><A /></>` ne crée donc pas, en pratique, un niveau supplémentaire.
- **Fragment imbriqué dans un élément parent** : il constitue un **niveau supplémentaire** dans l'arbre. Passer de `<div><A /></div>` à `<div><><A /></></div>` change la position de `A` (il devient l'enfant d'un fragment) et **réinitialise** son état.

```jsx
// L'état de <Compteur /> est perdu quand on bascule entre ces deux formes
<div>{enveloppe ? <><Compteur /></> : <Compteur />}</div>
```

Règle pratique : **ne faites pas apparaître ou disparaître un fragment autour d'un composant dont l'état doit survivre**. Les fragments à clé (`<Fragment key>`) suivent la règle des clés : changer la clé réinitialise le sous-arbre.

### 20.11 Fragments, `children` et composition

Le fragment est aussi un outil de **composition** : il permet de retourner `children` accompagnés d'éléments supplémentaires sans wrapper.

```jsx
function AvecAide({ children, aide }) {
  return (
    <>
      {children}
      <p className="aide" role="note">{aide}</p>
    </>
  );
}
```

Combiné avec `React.Children` ou `Children.toArray`, il faut savoir que **les fragments ne sont pas aplatis** : `Children.toArray(<><A/><B/></>)` retourne **un seul** enfant (le fragment). Si vous parcourez les enfants pour les transformer, un fragment passé par l'appelant sera traité comme un bloc unique.

### 20.12 Fragments et TypeScript

- Le type de retour d'un composant est `ReactNode` (ou, implicitement, `JSX.Element | null`). Un fragment est un `JSX.Element` valide.
- Les **chaînes**, **nombres** et **tableaux** de nœuds sont aussi des `ReactNode` valides, ce qui autorise `return "texte"` ou `return items.map(...)`.
- Pour typer la prop `children` : `children: ReactNode`.

```tsx
import { Fragment, type ReactNode } from 'react';

type Props = { elements: { id: number; titre: string; texte: string }[]; pied?: ReactNode };

export function Liste({ elements, pied }: Props) {
  return (
    <dl>
      {elements.map(e => (
        <Fragment key={e.id}>
          <dt>{e.titre}</dt>
          <dd>{e.texte}</dd>
        </Fragment>
      ))}
      {pied}
    </dl>
  );
}
```

### 20.13 Fragments et refs (fonctionnalité récente)

Un fragment n'a **pas de nœud DOM** : on ne peut donc pas lui attacher une `ref` classique. React expérimente des **refs de fragment** (une instance de fragment qui représente le groupe d'éléments : focus, observation, écouteurs sur l'ensemble). Cette API évolue ; consultez la documentation de votre version avant de l'utiliser. En attendant, enveloppez le groupe dans un élément réel ou utilisez une **ref de callback** sur chaque élément.

### 20.14 Choisir entre fragment, tableau et wrapper

| Besoin | Solution |
| --- | --- |
| Retourner plusieurs frères sans nœud supplémentaire | **`<>…</>`** |
| Même chose, avec une clé (dans un `map`) | **`<Fragment key>`** |
| Appliquer style, id, ARIA, `ref` ou événement au groupe | **Un élément réel** (`div`, `section`, `ul`…) |
| Ne rien rendre | **`null`** |
| Retourner une liste d'éléments déjà keyés | Un **tableau** (équivalent), le fragment étant plus lisible |

Règle de lecture : si un wrapper n'a **ni style, ni sémantique, ni comportement**, remplacez-le par un fragment.

### 20.15 Pièges fréquents

- Oublier la `key` sur un fragment dans un `map` (syntaxe courte invalide).
- Ajouter une `div` par réflexe, cassant tableaux/listes/flex.

### Synthèse du chapitre 20

`<>…</>` pour regrouper sans DOM ; `<Fragment key>` dans les listes.

---

## 21. Strict Mode

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : comprendre ce que `<StrictMode>` vérifie et pourquoi il double les appels ; corriger les problèmes qu'il révèle plutôt que de le désactiver.

### 21.1 Définition

**`<StrictMode>`** est un composant d'aide au développement : il active des **vérifications supplémentaires** et des **avertissements** pour son sous-arbre. **Aucun effet en production** (pas de double rendu, pas d'interface visible).

```jsx
<StrictMode>
  <App />
</StrictMode>
```

Peut être appliqué à **toute l'application** (recommandé) ou à **une partie**.

### 21.2 Ce qu'il fait (en développement)

1. **Double rendu** : appelle **deux fois** les corps de composants, **initialiseurs** de `useState`, fonctions de mise à jour d'état, **`useMemo`**, **`useReducer`** (reducers), constructeurs/`render` des classes → révèle les **impuretés**. (Une des deux exécutions est ignorée.) Depuis React 19, les résultats mémoïsés du premier rendu sont **réutilisés** pendant le second.
2. **Double exécution des effets** : au **montage initial**, simule *montage → démontage → remontage* : **setup → cleanup → setup** de chaque `useEffect`/`useLayoutEffect` → révèle les **cleanups manquants**.
3. **Double invocation des refs de callback** (React 19) : **setup → cleanup → setup** pour vérifier le nettoyage des refs.
4. **Avertissements sur les API dépréciées** (méthodes de cycle de vie `UNSAFE_`, `findDOMNode`, refs en chaîne, contexte hérité…).

### 21.3 Pourquoi ces doubles appels ?

- **Pureté** : un composant pur donne le **même résultat** s'il est appelé plusieurs fois.
- **Résilience** : React doit pouvoir **détruire et recréer** l'état d'un composant (Suspense, `<Activity>`, navigation avec préservation d'état, fast refresh, futures fonctionnalités). Un effet qui ne supporte pas « démontage/remontage » est **fragile**.

### 21.4 Problèmes typiques révélés et corrections

| Symptôme | Cause | Correction |
|---|---|---|
| Deux requêtes réseau au chargement | Effet sans annulation | `AbortController` / drapeau `ignorer` / bibliothèque de données |
| Deux connexions WebSocket ouvertes | Cleanup absent | Fermer la connexion dans le cleanup |
| Compteur incrémenté de 2 | Mutation d'une variable externe pendant le rendu | Rendre le composant **pur** |
| Liste dupliquée | `push` dans un tableau partagé pendant le rendu | Copier, ne pas muter |
| `console.log` doublé | Normal : 2ᵉ appel en gris dans les DevTools | Ne pas s'en soucier |
| Analytics comptés deux fois au montage | Effet d'envoi | Déplacer dans un **gestionnaire** ou dédoublonner côté analytique (en prod un seul appel) |
| Animation redémarrée | Setup non idempotent | Cleanup qui **réinitialise** l'état de l'animation |

> **Ne contournez pas** le double montage avec un `useRef` « déjà exécuté » : cela masque le bug et casse le comportement attendu avec Suspense/Activity.

### 21.5 Désactivation

Il n'y a **pas** d'option pour désactiver StrictMode par composant : il suffit de **ne pas l'envelopper**. Désactiver globalement est possible mais **déconseillé**.

### 21.6 Ce qui est exactement doublé

Les doubles invocations ne concernent que le **développement** et que le sous-arbre enveloppé par `<StrictMode>`.

| Élément | Comportement en développement | Ce que cela révèle |
| --- | --- | --- |
| Corps d'un composant (fonction) | Appelé **deux fois** par rendu | Mutations de variables externes, valeurs aléatoires ou dates dans le rendu |
| Initialiseur de `useState` / `useReducer` | Appelé **deux fois** | Initialiseurs impurs ou coûteux |
| Fonction passée à `setState` (mise à jour fonctionnelle) | Appelée **deux fois** | Mutation de l'état précédent |
| Fonction de `useMemo`, reducer | Appelés **deux fois** | Calculs non purs |
| Effets (`useEffect`, `useLayoutEffect`) | **Setup → cleanup → setup** au montage initial | Nettoyage absent ou asymétrique |
| Refs de callback | **Setup → cleanup → setup** au montage initial (React 19) | Nettoyage de ref manquant |
| Méthodes de classe (`render`, constructeur, `getDerivedStateFromProps`, `shouldComponentUpdate`) | Appelées deux fois | Idem pour les composants classes |

La double exécution d'un **effet** n'a lieu qu'**au montage initial** d'un composant, pas à chaque mise à jour. Les résultats de `useMemo` et `useCallback` du **premier** rendu sont réutilisés au second appel (React 19), pour limiter l'écart avec le comportement de production.

### 21.7 Écrire des effets symétriques

Un effet correct est **réversible** : exécuter *setup → cleanup → setup* doit laisser l'application dans le **même état** qu'un seul *setup*. Voici les motifs courants.

**Connexion (WebSocket, SSE, abonnement externe).**

```jsx
useEffect(() => {
  const connexion = creerConnexion(salon);
  connexion.ouvrir();
  return () => connexion.fermer();        // symétrique de ouvrir()
}, [salon]);
```

**Requête réseau.** Annulez ou ignorez la réponse obsolète.

```jsx
useEffect(() => {
  const ctrl = new AbortController();
  fetch(`/api/produits/${id}`, { signal: ctrl.signal })
    .then(r => r.json())
    .then(setProduit)
    .catch(e => { if (e.name !== 'AbortError') setErreur(e); });
  return () => ctrl.abort();
}, [id]);
```

**Écouteur d'événement.**

```jsx
useEffect(() => {
  const gerer = e => { if (e.key === 'Escape') onFermer(); };
  window.addEventListener('keydown', gerer);
  return () => window.removeEventListener('keydown', gerer);
}, [onFermer]);
```

**Bibliothèque non React** (carte, graphique, éditeur). Créez l'instance dans l'effet, détruisez-la dans le nettoyage ; sinon deux cartes se superposent au double montage.

```jsx
useEffect(() => {
  const carte = L.map(ref.current).setView(centre, 13);
  return () => carte.remove();
}, []);
```

**Animation ou minuteur.** Le nettoyage **annule** (`clearTimeout`, `cancelAnimationFrame`) et ramène l'élément à son état initial.

**Analytique.** Un « envoi de page vue » placé dans un effet est exécuté deux fois en développement seulement. Ne le contournez pas avec un drapeau : placez-le dans un **gestionnaire** (action de l'utilisateur) ou acceptez le doublon de développement, la production n'envoyant qu'un appel.

> Si votre effet ne peut **pas** être rendu symétrique, c'est souvent le signe qu'il n'aurait pas dû être un effet : une action déclenchée par l'utilisateur (achat, envoi de message) doit vivre dans un **gestionnaire d'événement**.

### 21.8 La pureté du rendu en pratique

Un composant est **pur** s'il retourne le **même JSX pour les mêmes props, état et contexte**, et s'il ne modifie rien d'extérieur pendant le rendu. Ce que le double rendu détecte :

```jsx
// ❌ Mutation d'une variable externe : le compteur augmente de 2 par rendu
let nbAffichages = 0;
function Entete() {
  nbAffichages++;
  return <h1>Affichage n°{nbAffichages}</h1>;
}

// ❌ Valeur instable dans le rendu : deux appels, deux résultats différents
function Carte() {
  return <div id={Math.random()}>{new Date().toLocaleTimeString()}</div>;
}

// ❌ Mutation d'une prop ou de l'état
function Liste({ elements }) {
  elements.sort();                // modifie le tableau du parent
  return <ul>{elements.map(...)}</ul>;
}

// ✅ Copie avant tri, valeur aléatoire créée une seule fois
function Liste({ elements }) {
  const tries = [...elements].sort();
  const [id] = useState(() => crypto.randomUUID());
  return <ul id={id}>{tries.map(...)}</ul>;
}
```

**Mutation locale acceptée** : créer un objet ou un tableau **pendant** le rendu puis le modifier est parfaitement pur, tant qu'il ne survit pas au rendu (`const lignes = []; for (...) lignes.push(<li/>)`).

### 21.9 Strict Mode, Fast Refresh et mode développement

- **Fast Refresh** (rechargement à chaud) réexécute les **effets** d'un composant modifié pour refléter votre édition : c'est un comportement distinct, mais il produit des effets visuellement similaires (un effet joué à nouveau). Un effet symétrique résiste aux deux.
- Les **DevTools** affichent les logs du **second** appel en **grisé** ; une option permet de masquer les logs du second rendu.
- Dans les méta-frameworks, Strict Mode est **souvent activé par défaut** (par exemple l'option `reactStrictMode` de Next.js, active par défaut avec le routeur d'applications).
- Il ne change **pas** le résultat final affiché : si l'interface diffère entre développement et production, la cause est une **impureté** ou un effet asymétrique.

### 21.10 Application partielle et bibliothèques tierces

Vous pouvez envelopper **seulement une partie** de l'application dans `<StrictMode>` pour migrer progressivement : activez-le sur un sous-arbre, corrigez, puis étendez.

```jsx
<Layout>
  <StrictMode>
    <NouvelleFonctionnalite />
  </StrictMode>
  <ModuleHeritage />      {/* pas encore vérifié */}
</Layout>
```

Une bibliothèque tierce qui échoue sous Strict Mode a généralement une **initialisation non réversible** (singleton, état global, abonnement sans désabonnement). Mettez-la à jour, signalez le problème, ou isolez son initialisation dans un composant qui la crée et la détruit proprement.

### 21.11 Méthode de diagnostic

1. **Reproduire** : l'anomalie n'apparaît qu'en développement ? Soupçonnez Strict Mode.
2. **Identifier** quel doublon est en cause : rendu (log dans le corps du composant) ou effet (log dans `setup` et dans `cleanup`).
3. **Lire le cycle** : en cas d'effet, vérifiez que le *cleanup* annule **tout** ce que le *setup* a créé.
4. **Corriger à la source** : rendre le calcul pur, symétriser l'effet, ou déplacer l'opération dans un gestionnaire.
5. **Vérifier en production** : un seul appel doit se produire, et le comportement doit être identique.
6. **Ne jamais** masquer le doublon avec une ref « déjà fait » ni retirer `<StrictMode>`.

### 21.12 Pièges fréquents

- Désactiver StrictMode au lieu de corriger le bug.
- Croire que la production double aussi les rendus (faux).
- Placer des **effets de bord** (requêtes, écriture de `localStorage`) dans le corps du composant ou dans un initialiseur de `useState`.

### Synthèse du chapitre 21

StrictMode = **filet de sécurité** en développement : double rendu + double effets + double refs ; Un composant **pur** et des effets **symétriques (setup/cleanup)** passent le test sans modification.

---

## 22. Concurrent Rendering

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : comprendre le **rendu concurrent** : interruptible, priorisé, non bloquant ; connaître les fonctionnalités qui s'y appuient et les contraintes pour votre code.

### 22.1 Définition

Le **rendu concurrent** est un **mode de fonctionnement interne** de React (activé par `createRoot`, React 18+) dans lequel **le rendu peut être préparé en arrière-plan, mis en pause, repris ou abandonné**, **sans bloquer le thread principal**. Il ne s'agit pas de multithreading : c'est de la **planification coopérative** (*time slicing*) : React **cède régulièrement la main** au navigateur (≈ toutes les 5 ms) pour traiter les entrées utilisateur et peindre.

Avant React 18, un rendu était **synchrone et ininterruptible** : un rendu lourd gelait l'interface (saisie bloquée, animations saccadées).

### 22.2 Modèle mental

- React maintient **deux arbres** : l'arbre **courant** (affiché) et l'arbre **« work in progress »** (en préparation).
- Les mises à jour sont **classées par priorité** (*lanes*) : **discrète/urgente** (clic, frappe) > **continue** (survol, défilement) > **transition** (non urgente) > **inactif/différé**.
- Si une mise à jour urgente arrive pendant le rendu d'une transition, React **abandonne** le travail en cours, traite l'urgent, puis **reprend** la transition avec l'état le plus récent.
- Rien n'est **commis** au DOM tant que le rendu n'est pas **terminé et cohérent** : l'utilisateur ne voit **jamais d'état intermédiaire**.

### 22.3 Fonctionnalités reposant sur la concurrence

| Fonctionnalité | Description |
|---|---|
| **Batching automatique** (18) | Regroupement des `setState` partout (promesses, timeouts, événements natifs) |
| **Transitions** : `startTransition` / `useTransition` | Mises à jour non urgentes interruptibles |
| **`useDeferredValue`** | Valeur retardée pour garder la saisie fluide |
| **Suspense** (côté client et serveur) | Attente sans bloquer ; streaming SSR |
| **Hydratation sélective** | Hydrater par priorité (clic de l'utilisateur) |
| **Actions** (19) | Transitions asynchrones avec état d'attente (`isPending`) |
| **`<Activity>`** (19.2) | Masquer un sous-arbre en **préservant son état**, effets suspendus, rendu à basse priorité |
| **`useSyncExternalStore`** | Lecture sûre de stores externes (évite le tearing) |

#### `<Activity>` (React 19.2)

```jsx
import { Activity } from 'react';

<Activity mode={onglet === 'messages' ? 'visible' : 'hidden'}>
  <Messages />          {/* état conservé quand masqué ; effets nettoyés ; mises à jour différées */}
</Activity>
```

- `mode="hidden"` : le sous-arbre est **masqué** (`display: none`), ses **effets sont démontés** (cleanup), son **état est préservé**, et il **continue** à se re-rendre à **basse priorité**.
- `mode="visible"` : affichage normal, effets recréés.
- Cas d'usage : onglets/pages qui conservent saisies et scroll, **pré-rendu** de la vue suivante probable.

### 22.4 Conséquences pour votre code

Comme React peut **appeler un rendu plusieurs fois, l'interrompre ou l'abandonner**, il faut :

1. **Pureté du rendu** : aucun effet de bord, aucune mutation externe pendant le rendu.
2. **Idempotence** : mêmes entrées → mêmes sorties.
3. **Lire les sources externes** avec `useSyncExternalStore` (pas de lecture directe d'une variable mutable pendant le rendu → *tearing*).
4. **Ne pas supposer** qu'un rendu mène à un commit.
5. **Effets symétriques** (setup/cleanup) — vérifiés par StrictMode.
6. **Éviter `flushSync`** sauf nécessité (il force un rendu synchrone urgent).

### 22.5 Mise en pratique

```jsx
function Recherche() {
  const [requete, setRequete] = useState('');
  const [liste, setListe] = useState(tous);
  const [enAttente, startTransition] = useTransition();

  function handleChange(e) {
    setRequete(e.target.value);                       // URGENT : saisie fluide
    startTransition(() => {
      setListe(filtrerLourd(tous, e.target.value));   // NON URGENT : interruptible
    });
  }

  return (
    <>
      <input value={requete} onChange={handleChange} />
      {enAttente && <small>Mise à jour…</small>}
      <Resultats liste={liste} />
    </>
  );
}
```

### 22.6 Ce que la concurrence ne fait pas

- Elle **ne rend pas** un calcul lent plus rapide : elle le **rend interruptible**. Un calcul synchrone de 500 ms **à l'intérieur d'un seul composant** reste bloquant (déplacez-le dans un Worker, découpez-le, ou mémoïsez-le).
- Elle n'est **pas du parallélisme** (un seul thread JS).
- Elle ne dispense pas de réduire la **taille de l'arbre** ou le **coût des rendus**.

### 22.7 Priorités et planification

Le rendu concurrent repose sur des **niveaux de priorité** : toutes les mises à jour ne se valent pas.

| Priorité | Exemples | Comportement |
| --- | --- | --- |
| **Urgente** (discrète) | Clic, frappe clavier, appui sur une touche | Traitée **immédiatement**, jamais interrompue |
| **Continue** | Défilement, survol, glissement | Traitée rapidement, après les événements discrets |
| **Transition** | Mise à jour marquée par `startTransition` / `useTransition` | **Interruptible** et reprise ; cède le pas aux mises à jour urgentes |
| **Différée** | Valeur lue via `useDeferredValue` | Calculée après la valeur urgente |
| **Inactive** (*idle*) | Contenu masqué par `<Activity>`, préchargements | Traitée quand le navigateur est libre |

Principe : si une mise à jour **urgente** arrive pendant qu'un rendu de transition est en cours, React **abandonne** (ou met en pause) ce rendu, traite l'urgence, puis **reprend** la transition avec l'état à jour. Résultat : la saisie reste fluide pendant qu'un gros rendu se prépare en arrière-plan.

### 22.8 Le traitement par lots automatique (*automatic batching*)

Depuis React 18, plusieurs mises à jour d'état déclenchées **dans la même tâche** sont regroupées en **un seul rendu**, quelle que soit leur origine (gestionnaire d'événement, `setTimeout`, promesse, callback natif).

```jsx
setTimeout(() => {
  setCompteur(c => c + 1);
  setDrapeau(f => !f);
  // Un seul rendu (avant React 18 : deux)
}, 1000);
```

Pour **forcer** un rendu synchrone immédiat (cas rare : lire le DOM juste après une mise à jour), on utilise `flushSync` de `react-dom` :

```jsx
import { flushSync } from 'react-dom';
flushSync(() => setOuvert(true));
// Le DOM est à jour à cet endroit
```

`flushSync` annule les bénéfices de la concurrence pour cette mise à jour : réservez-le aux synchronisations avec du code non React (focus, mesure, défilement).

### 22.9 Les transitions en détail

Une **transition** déclare qu'une mise à jour est **non urgente**.

```jsx
function Recherche() {
  const [saisie, setSaisie] = useState('');
  const [requete, setRequete] = useState('');
  const [enAttente, demarrerTransition] = useTransition();

  function surChangement(e) {
    setSaisie(e.target.value);                         // urgent : le champ répond tout de suite
    demarrerTransition(() => setRequete(e.target.value)); // non urgent : filtrage lourd
  }

  return (
    <>
      <input value={saisie} onChange={surChangement} />
      {enAttente && <Indicateur />}
      <Resultats requete={requete} />
    </>
  );
}
```

Points à connaître :

- `isPending` (ici `enAttente`) vaut `true` tant que la transition n'est pas validée : utile pour un indicateur discret.
- Les mises à jour d'une transition sont **interruptibles** et ne provoquent **pas** de retour au `fallback` d'un `Suspense` déjà affiché : l'ancien contenu reste visible pendant le chargement du nouveau.
- Une transition ne peut **pas** contrôler la valeur d'un `<input>` : la saisie doit rester une mise à jour **urgente**.
- Depuis React 19, la fonction passée à une transition peut être **asynchrone** : c'est la base des **Actions** (chapitres 10 et 23), avec gestion automatique de l'état en attente.
- `startTransition` (importé de `react`) existe aussi hors Hook, sans `isPending`.

### 22.10 `useDeferredValue` : différer plutôt que planifier

`useDeferredValue(valeur)` retourne une version **retardée** de `valeur` : au rendu urgent, elle conserve l'**ancienne** valeur ; React prépare ensuite en arrière-plan un rendu avec la **nouvelle**.

```jsx
function Page() {
  const [texte, setTexte] = useState('');
  const differe = useDeferredValue(texte);          // React 19 : useDeferredValue(texte, '') valeur initiale
  return (
    <>
      <input value={texte} onChange={e => setTexte(e.target.value)} />
      <ListeLourde filtre={differe} />               {/* enveloppée dans memo */}
    </>
  );
}
```

Condition d'efficacité : l'enfant coûteux doit être **mémoïsé** (`memo`) ; sinon il re-rend à chaque frappe avec l'ancienne valeur et l'on ne gagne rien. Contrairement au *debounce* (attente d'un délai fixe), le report est **adaptatif** : sur une machine rapide il est quasi instantané, sur une machine lente il laisse respirer l'interface, et il est **interruptible**.

### 22.11 Quel outil choisir ?

| Situation | Outil | Pourquoi |
| --- | --- | --- |
| Vous contrôlez le `setState` qui déclenche le rendu coûteux | **`useTransition`** | Marque la mise à jour comme non urgente ; fournit `isPending` |
| Vous recevez la valeur en **prop** ou d'un Hook tiers | **`useDeferredValue`** | Pas d'accès au `setState` à marquer |
| Données ou code en cours de chargement | **`Suspense`** (+ transition) | Fallback précis, ancien contenu conservé |
| Limiter les **appels réseau** pendant la frappe | **Debounce** (ou annulation de requête) | La concurrence n'évite pas les requêtes inutiles |
| Rendu très long de milliers de lignes | **Virtualisation** | La concurrence rend interruptible, mais ne réduit pas le travail |
| Écran ou onglet « en veille » | **`<Activity>`** | Conserve l'état, suspend les effets |

### 22.12 Concurrence et magasins externes : le *tearing*

Comme le rendu peut être **interrompu puis repris**, une lecture d'une donnée **externe** modifiable (variable globale, store maison) peut donner, au sein d'un même rendu, des valeurs **incohérentes** entre composants : on parle de **déchirure** (*tearing*).

Le Hook **`useSyncExternalStore(subscribe, getSnapshot, getServerSnapshot?)`** garantit une lecture **cohérente** : il force un rendu **synchrone** quand le store change.

```jsx
function useStore(store) {
  return useSyncExternalStore(store.subscribe, store.getSnapshot);
}
```

`getSnapshot` doit retourner une valeur **stable** (la même référence tant que rien n'a changé), sinon React boucle. Les bibliothèques d'état modernes (Redux Toolkit, Zustand, Jotai) l'utilisent déjà : vous n'avez à l'écrire vous-même que pour intégrer une source externe (API du navigateur, store maison).

### 22.13 Observer et diagnostiquer

- **React DevTools, onglet Profiler** : identifie les composants lents et la cause de chaque rendu.
- **Panneau Performance de Chrome** : les pistes **React Performance Tracks** (React 19.2) montrent les phases de planification (*Scheduler*) et le temps par composant, ce qui permet de voir quand un rendu est interrompu, repris ou abandonné.
- **Journalisation** : un `console.log` dans le corps d'un composant peut s'afficher **plus souvent** que le nombre de mises à jour validées (rendus abandonnés, Strict Mode) : n'en déduisez pas de fuite.
- **Indicateur `isPending`** : vérifiez que l'état d'attente s'affiche bien et que l'ancien contenu reste visible.

### 22.14 Adoption et compatibilité

- La concurrence est **activée par `createRoot`**. L'ancien `ReactDOM.render` utilise le mode **historique** (synchrone) et ne bénéficie ni du traitement par lots automatique ni des transitions.
- Elle est **opt-in par fonctionnalité** : tant que vous n'utilisez ni transitions, ni `useDeferredValue`, ni Suspense avancé, le comportement perçu ressemble à l'ancien, hormis le traitement par lots.
- Points de vigilance lors de la migration : effets exécutés **deux fois** en Strict Mode, rendus **abandonnés**, bibliothèques qui lisent un état externe pendant le rendu (voir *tearing*), code qui supposait un rendu **synchrone** après un `setState`.

### 22.15 Pièges fréquents

- Mutations/effets de bord dans le rendu → comportements non déterministes.
- Lire un store externe sans `useSyncExternalStore`.
- Envelopper la **valeur d'un input** dans une transition.
- Attendre qu'une transition s'exécute **immédiatement**.
- Utiliser abusivement `flushSync`.

### Synthèse du chapitre 22

Rendu **interruptible**, **priorisé** et **non bloquant** ; commit **atomique** ; Fonctionnalités : **transitions, valeurs différées, Suspense, hydratation sélective, Activity** ; Exigences : **pureté, idempotence, effets symétriques, stores externes via `useSyncExternalStore`**.

---

## 23. Server Components et Actions

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : situer les stratégies de rendu (CSR, SSR, SSG, ISR, streaming) et l'hydratation ; comprendre les **React Server Components** (RSC), la frontière **`'use client'`** et les règles de composition ; maîtriser les **Server Functions / Actions** (`'use server'`), leurs usages et leurs risques de sécurité ; connaître les API de document de React 19 (métadonnées, feuilles de style, préchargement). > Les RSC nécessitent un **framework ou un bundler compatible** (Next.js App Router, React Router en mode RSC, Waku, Parcel…). React fournit la spécification et les primitives ; l'intégration (routage, bundling, mise en cache) est assurée par le framework. Les détails de configuration varient selon l'outil et évoluent : consultez sa documentation.

### 23.1 Les stratégies de rendu

| Stratégie | Où et quand le HTML est produit | Forces | Limites |
|---|---|---|---|
| **CSR** (*Client-Side Rendering*) | Navigateur, après chargement du JS | Simple, interactions riches, hébergement statique | 1ᵉʳ affichage lent, SEO plus délicat, JS volumineux |
| **SSR** (*Server-Side Rendering*) | Serveur, **à chaque requête** | 1ᵉʳ affichage rapide, SEO, données fraîches | Coût serveur, TTFB, hydratation nécessaire |
| **SSG** (*Static Site Generation*) | **Au build** | Très rapide, CDN, économique | Contenu figé jusqu'au prochain build |
| **ISR** (*Incremental Static Regeneration*) | Statique **régénéré** périodiquement/à la demande | Compromis statique/dynamique | Dépend du framework |
| **Streaming SSR** | Serveur, **par morceaux** (Suspense) | Shell rapide, contenu lent différé | Complexité |
| **RSC** | Serveur/build, **sans JS client** pour ces composants | Moins de JS, accès direct aux données | Modèle mental à apprendre, framework requis |

#### Hydratation

Après un rendu serveur, le navigateur reçoit du **HTML** puis le **JS**. **`hydrateRoot`** « hydrate » ce HTML : React reconstruit l'arbre en mémoire, **attache les gestionnaires** et l'état, sans recréer le DOM. Le rendu **client initial** doit produire **le même HTML** que le serveur.

**Erreurs d'hydratation** (*mismatch*) typiques : `Date.now()`, `Math.random()`, `window`/`localStorage` dans le rendu, locale/fuseau différents, HTML invalide (`<div>` dans `<p>`), extensions de navigateur. Correctifs : lire ces valeurs **après montage** (`useEffect`), utiliser `useSyncExternalStore` avec `getServerSnapshot`, `suppressHydrationWarning` (pour une différence **assumée**, un seul niveau), générer les ID avec `useId`.

#### API serveur de `react-dom`

| API | Usage |
|---|---|
| `renderToString` | HTML complet synchrone (ancien, sans streaming/Suspense complet) |
| `renderToPipeableStream` | Streaming Node.js avec Suspense (`onShellReady`, `onAllReady`, `onError`) |
| `renderToReadableStream` | Streaming Web Streams (Edge, Deno, Bun) |
| `prerender` / `prerenderToNodeStream` (`react-dom/static`) | Pré-rendu statique en **attendant** toutes les données (SSG) |
| `resume` / `resumeAndPrerender` | Reprendre un pré-rendu partiel (base du **Partial Prerendering** des frameworks) |

### 23.2 React Server Components (RSC)

#### Définition

Un **Server Component** est un composant qui **s'exécute uniquement dans un environnement serveur** (au **build** ou à **chaque requête**), **avant** que le résultat ne soit envoyé au navigateur. Son **code n'est jamais envoyé au client** : seul son **résultat rendu** (une description sérialisée de l'UI, le **payload RSC**) l'est.

> **Ne pas confondre** avec le **SSR** : le SSR rend **tous** les composants (qui seront ensuite hydratés côté client) en HTML ; les RSC sont une **catégorie de composants** qui **ne s'hydratent pas** et ne sont **jamais** inclus dans le bundle client. Les deux se combinent.

#### Ce qu'un Server Component peut faire

- Être **`async`** et utiliser **`await`** directement dans le rendu.
- Accéder **directement** aux **bases de données**, au **système de fichiers**, aux **secrets/variables d'environnement**, à des **services internes**.
- Utiliser de **grosses dépendances** (Markdown, coloration syntaxique) **sans impact** sur le bundle client.
- Rendre des **Client Components** et leur passer des **props sérialisables**.

```jsx
// app/articles/page.jsx : Server Component (par défaut dans l'App Router de Next.js)
import { db } from '@/lib/db';

export default async function Articles() {
  const articles = await db.article.findMany({ orderBy: { date: 'desc' } });
  return (
    <ul>
      {articles.map(a => <li key={a.id}>{a.titre}</li>)}
    </ul>
  );
}
```

#### Ce qu'il ne peut pas faire

- **State et effets** : `useState`, `useReducer`, `useEffect`, `useLayoutEffect`, `useRef` pour des effets, etc.
- **Gestionnaires d'événements** (`onClick`…).
- **API du navigateur** (`window`, `localStorage`, `document`).
- **Context** (`createContext`/`useContext`) : un contexte se **fournit et consomme côté client**.
- Les hooks dépendant de ces fonctionnalités.

#### Client Components : la directive `'use client'`

```jsx
'use client';                     // en TOUT PREMIER du fichier (avant les imports)

import { useState } from 'react';

export function BoutonLike({ initial }) {
  const [likes, setLikes] = useState(initial);
  return <button onClick={() => setLikes(l => l + 1)}>👍 {likes}</button>;
}
```

- `'use client'` marque une **frontière** « serveur → client » : ce **module et tout ce qu'il importe** font partie du **bundle client** (inutile de répéter la directive dans les fichiers importés).
- Les Client Components sont **aussi pré-rendus en HTML sur le serveur** (SSR) puis hydratés.
- Les Server Components sont **le défaut** ; on ajoute `'use client'` **seulement** pour l'**interactivité** (état, effets, événements, API navigateur).

| | **Server Component** | **Client Component** |
|---|---|---|
| Directive | (aucune par défaut) | `'use client'` |
| S'exécute | Serveur/build uniquement | Serveur (SSR) **et** navigateur |
| Dans le bundle client | ❌ | ✅ |
| `async/await` dans le composant | ✅ | ❌ (utiliser `use`/bibliothèques) |
| State / effets / événements | ❌ | ✅ |
| API navigateur | ❌ | ✅ |
| Accès direct DB/secrets | ✅ | ❌ |

#### Règles de composition

1. **Un Server Component peut importer et rendre des Client Components.**
2. **Un Client Component ne peut pas importer un Server Component**… mais il peut **recevoir un Server Component en `children`/props** (déjà rendu côté serveur) :

```jsx
// Serveur
<PanneauClient>
  <ListeServeur />      {/* rendu serveur, passé comme children */}
</PanneauClient>
```

3. Les **props** passées d'un Server à un Client Component doivent être **sérialisables** : primitifs, tableaux, objets simples, `Date`, `Map`, `Set`, `BigInt`, `Promise`, éléments JSX, **Server Functions**. **Pas** de fonctions ordinaires, ni de classes/instances, ni de `Symbol` locaux.
4. **Placez `'use client'` le plus bas possible** (feuilles interactives) pour limiter le JavaScript client.
5. Les **bibliothèques tierces** utilisant état/effets doivent être enveloppées dans un petit **composant client** (`'use client'`).
6. Paquet **`server-only`** : `import 'server-only'` fait **échouer le build** si du code serveur (secrets) est importé côté client ; **`client-only`** pour l'inverse.

#### Récupération de données avec RSC

```jsx
// Requêtes parallèles (évite les cascades)
export default async function Page({ params }) {
  const [utilisateur, commandes] = await Promise.all([
    getUtilisateur(params.id),
    getCommandes(params.id),
  ]);
  return <Tableau utilisateur={utilisateur} commandes={commandes} />;
}

// Streaming : ne pas bloquer la page pour une partie lente
export default function Page() {
  return (
    <>
      <Entete />
      <Suspense fallback={<Squelette />}>
        <RecommandationsLentes />     {/* async, streamées quand prêtes */}
      </Suspense>
    </>
  );
}
```

- **`cache(fn)`** (de `react`, **serveur**) : mémoïse une fonction asynchrone **pendant la durée d'une requête serveur** (même appel appelé à plusieurs endroits → **une seule exécution**).
- Le **cache HTTP/données** et la **revalidation** dépendent du **framework**.
- Un Client Component peut recevoir une **`Promise`** en prop (créée côté serveur) et la lire avec **`use`** (Suspense) : les données **streament** jusqu'au client.

```jsx
// Serveur
export default function Page() {
  const promesse = getCommentaires();          // non attendue
  return <Suspense fallback={…}><Commentaires promesse={promesse} /></Suspense>;
}
// Client
'use client';
export function Commentaires({ promesse }) { const data = use(promesse); … }
```

#### Avantages

- **Moins de JavaScript client** (temps de chargement, INP).
- **Proximité des données** (moins d'allers-retours réseau).
- **Sécurité** : secrets et logique sensibles restent côté serveur.
- **Streaming** et **SEO** naturels.
- **Composition** flexible avec des composants interactifs ciblés.

#### Limites et points d'attention

- Modèle mental **plus complexe** (frontière, sérialisation, deux environnements).
- **Framework requis** ; écosystème de bibliothèques en adaptation (`'use client'` nécessaire).
- **Débogage** réparti serveur/client ; **coûts serveur**.
- **Contexte** non utilisable dans les Server Components (fournisseurs côté client).

### 23.3 Server Functions et Actions

#### Définition

Une **Server Function** est une **fonction asynchrone exécutée sur le serveur**, mais **appelable depuis le client**, comme une fonction ordinaire (React gère l'appel réseau et la sérialisation). Elles sont marquées par la directive **`'use server'`**. Quand elles sont passées à une prop **`action`** (formulaire) ou appelées dans une **transition**, on parle de **Server Actions**.

> **Ne confondez pas** : `'use server'` désigne les **Server Functions** (et non les Server Components, qui n'ont pas de directive).

```jsx
// actions.js
'use server';                                    // niveau FICHIER : toutes les exports sont des Server Functions
import { db } from '@/lib/db';
import { z } from 'zod';

const schema = z.object({ titre: z.string().min(3).max(100) });

export async function creerArticle(etatPrecedent, formData) {
  const session = await getSession();
  if (!session) throw new Error('Non autorisé');                 // 1. AUTHENTIFICATION / AUTORISATION

  const resultat = schema.safeParse({ titre: formData.get('titre') });  // 2. VALIDATION côté serveur
  if (!resultat.success) return { erreur: resultat.error.flatten().fieldErrors };

  await db.article.create({ data: { titre: resultat.data.titre, auteurId: session.userId } });
  revalidatePath('/articles');                                   // spécifique au framework
  return { erreur: null };
}
```

```jsx
// Client Component
'use client';
import { useActionState } from 'react';
import { creerArticle } from './actions';

export function FormulaireArticle() {
  const [etat, action, enAttente] = useActionState(creerArticle, { erreur: null });
  return (
    <form action={action}>
      <input name="titre" />
      {etat.erreur?.titre && <p role="alert">{etat.erreur.titre[0]}</p>}
      <button disabled={enAttente}>Créer</button>
    </form>
  );
}
```

#### Deux façons de déclarer

```jsx
// Niveau fonction (dans un Server Component)
async function enregistrer(formData) {
  'use server';
  await db.save(formData.get('nom'));
}

// Niveau fichier : 'use server' en tête d'un module d'actions
```

#### Appels possibles

1. **`<form action={serverFunction}>`** (avec **amélioration progressive** : fonctionne avant l'hydratation dans les frameworks compatibles).
2. **`formAction`** sur un bouton.
3. Depuis un gestionnaire d'événement, dans **`startTransition`** (mutation avec `isPending`).
4. Depuis `useActionState`, `useOptimistic` (chapitre 10 et 11).

#### Sécurité : **règles impératives**

> Une Server Function est un **point d'accès HTTP public** : n'importe qui peut l'appeler avec **n'importe quelles données**, même sans passer par votre interface.

1. **Authentifier et autoriser** à **l'intérieur de chaque** fonction (ne comptez pas sur « le bouton n'est visible que pour l'admin »).
2. **Valider et assainir** **toutes** les entrées (**Zod**/Valibot) : ne faites jamais confiance au client.
3. Ne **renvoyez** que les **données nécessaires** (pas d'objets complets de base de données).
4. Protection **CSRF** : gérée par le framework dans les cas standards (vérification d'origine) ; vérifiez la configuration.
5. **Limitation de débit** et **journalisation** pour les actions sensibles.
6. Éviter de **capturer par closure** des secrets/valeurs sensibles dans une fonction inline (ils seraient sérialisés dans le payload, chiffrés par le framework mais à manipuler avec prudence).
7. Les fonctions de fichiers `'use server'` **exportées** sont **toutes** exposées : ne placez pas d'utilitaires internes dans ces modules.

#### Comportement

- Les appels à des Server Functions depuis un même client sont **mis en file** et exécutés **séquentiellement** (pas de parallélisme garanti) ; pour de la **lecture de données**, privilégiez RSC/loaders.
- Les erreurs non gérées remontent à l'**Error Boundary** ; pour des erreurs **attendues** (validation), **retournez** un résultat plutôt que de lever.

### 23.4 API de document de React 19

React 19 permet de déclarer **dans les composants** des éléments qui appartiennent au **document**.

#### Métadonnées

```jsx
function Article({ article }) {
  return (
    <article>
      <title>{article.titre}</title>
      <meta name="description" content={article.resume} />
      <link rel="canonical" href={article.url} />
      <h1>{article.titre}</h1>
    </article>
  );
}
// React hisse automatiquement <title>, <meta>, <link> dans <head>
```

#### Feuilles de style avec précédence

```jsx
<link rel="stylesheet" href="/theme.css" precedence="default" />
// React gère l'ordre, la déduplication et attend le chargement avant de révéler le contenu (Suspense).
```

#### Scripts asynchrones dédupliqués

```jsx
<script async src="https://exemple.com/widget.js" />   // inséré une seule fois même s'il apparaît dans plusieurs composants
```

#### Préchargement de ressources (`react-dom`)

```jsx
import { prefetchDNS, preconnect, preload, preinit } from 'react-dom';

preconnect('https://api.exemple.com');
preload('/police.woff2', { as: 'font', type: 'font/woff2', crossOrigin: 'anonymous' });
preinit('/script.js', { as: 'script' });
```

#### Éléments personnalisés (Web Components)

React 19 supporte pleinement les **custom elements** : les props non primitives sont transmises comme **propriétés**, les événements personnalisés sont écoutables.

### 23.5 Choisir son architecture

| Besoin | Option |
|---|---|
| Application interne / tableau de bord, pas de SEO | **SPA Vite** (CSR) + TanStack Query/Router |
| Site vitrine / blog / documentation | **SSG** (Next.js, Astro avec îlots React, Gatsby) |
| Application publique, SEO, données dynamiques | **SSR + RSC + streaming** (Next.js, React Router v7) |
| Mobile | **React Native / Expo** |
| Intégrer du React dans un site existant | **Plusieurs roots** / îlots |

### 23.6 Pièges fréquents

- Confondre **SSR** et **RSC**, ou `'use client'` (frontière de bundle) et « rendu uniquement côté client ».
- Mettre `'use client'` **trop haut** (tout l'arbre devient client).
- Passer une **fonction** ordinaire ou une **instance de classe** en prop d'un Server vers un Client Component.
- Utiliser `useState`/`useEffect`/`onClick` dans un Server Component.
- Oublier **l'autorisation** dans une Server Function.
- Valider uniquement côté client.
- Provoquer des **cascades** `await` successifs au lieu de `Promise.all`.
- Erreurs d'hydratation causées par des valeurs non déterministes.
- Importer du code serveur (secrets) dans un module client (utiliser `server-only`).

### Synthèse du chapitre 23

**RSC** = composants **exécutés sur le serveur**, **0 JS client** ; **`'use client'`** = frontière vers l'interactivité ; Composition : **Server → Client** par import, **Client → Server** par `children`/props ; **Server Functions (`'use server'`)** = **endpoints publics** : **authentifiez, autorisez, validez** ; **Streaming + Suspense**, **`cache`**, **`use`** pour des données progressives ; React 19 : **métadonnées**, **feuilles de style**, **préchargement** déclaratifs.

---

## 24. Composants classes (legacy)

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : savoir lire, maintenir et migrer du code à base de **classes** ; connaître le cycle de vie et les équivalences avec les Hooks ; identifier les cas où une classe reste nécessaire (Error Boundaries).

### 24.1 Contexte

Les **composants classes** sont l'API d'origine de React. Ils sont **toujours supportés** et **non dépréciés**, mais **les Hooks sont recommandés** pour le code neuf. Vous les rencontrerez dans des bases de code existantes, des bibliothèques, et **obligatoirement** pour les **Error Boundaries**.

> Limites : pas de Hooks ni de `use`, logique réutilisable via HOC/render props, `this` à gérer, API moins propice à la compilation/optimisation.

### 24.2 Structure d'une classe

```jsx
import { Component } from 'react';

class Compteur extends Component {
  // 1. État initial (class field ; ou dans constructor)
  state = { compte: 0 };

  // 2. Méthodes : fonctions fléchées pour lier `this` automatiquement
  incrementer = () => {
    this.setState(prev => ({ compte: prev.compte + 1 }));
  };

  // 3. Méthode render obligatoire : retourne du JSX
  render() {
    return (
      <button onClick={this.incrementer}>
        {this.props.libelle} : {this.state.compte}
      </button>
    );
  }
}
```

#### Le constructeur (rarement nécessaire)

```jsx
constructor(props) {
  super(props);                           // OBLIGATOIRE en premier
  this.state = { compte: props.initial };
  this.incrementer = this.incrementer.bind(this);   // liaison de `this` si méthode classique
}
```

#### La liaison de `this`

Les méthodes passées comme callbacks **perdent leur `this`**. Solutions : **fonction fléchée en class field** (recommandé), `bind` dans le constructeur, ou fonction fléchée inline (nouvelle fonction à chaque rendu).

### 24.3 Props et state dans une classe

- Props : `this.props` (lecture seule).
- État : `this.state` ; **ne jamais l'assigner** directement hors constructeur/field initial ; **toujours `setState`**.

#### `setState`

```jsx
this.setState({ nom: 'Alice' });                     // FUSION superficielle avec l'état existant
this.setState(prev => ({ compte: prev.compte + 1 })); // forme fonctionnelle
this.setState({ x: 1 }, () => { /* callback après mise à jour du DOM */ });
```

- **Fusionne** les clés (différence avec `useState`, qui **remplace** la valeur).
- Les mises à jour sont **groupées (batching)** et **asynchrones** : `this.state` n'est pas à jour juste après l'appel.
- `forceUpdate()` force un rendu (à éviter).

### 24.4 Le cycle de vie

#### Montage

1. `constructor(props)`
2. `static getDerivedStateFromProps(props, state)`
3. `render()`
4. **`componentDidMount()`** : après insertion dans le DOM → requêtes, abonnements, timers, mesures.

#### Mise à jour (nouvelles props, `setState`, `forceUpdate`)

1. `static getDerivedStateFromProps(props, state)`
2. `shouldComponentUpdate(nextProps, nextState)` → `false` évite le rendu
3. `render()`
4. `getSnapshotBeforeUpdate(prevProps, prevState)` : lire le DOM **avant** mise à jour (ex. position de scroll) ; la valeur retournée est transmise à `componentDidUpdate`
5. **`componentDidUpdate(prevProps, prevState, snapshot)`** : après mise à jour du DOM ; **comparer** les props/état avant d'agir (sinon boucle infinie)

#### Démontage

- **`componentWillUnmount()`** : **nettoyage** (désabonnements, timers, annulation de requêtes).

#### Gestion d'erreurs

- `static getDerivedStateFromError(error)` et `componentDidCatch(error, info)` (voir chapitre 18).

#### Méthodes dépréciées (préfixe `UNSAFE_`)

`componentWillMount`, `componentWillReceiveProps`, `componentWillUpdate` : **à ne plus utiliser** (peu sûres avec le rendu concurrent). Les remplacer par `componentDidMount`, `componentDidUpdate`, `getDerivedStateFromProps`.

#### Exemple complet

```jsx
class Profil extends Component {
  state = { utilisateur: null, erreur: null };
  controleur = new AbortController();

  componentDidMount() { this.charger(); }

  componentDidUpdate(prevProps) {
    if (prevProps.id !== this.props.id) this.charger();    // garde indispensable
  }

  componentWillUnmount() { this.controleur.abort(); }

  async charger() {
    try {
      const rep = await fetch(`/api/users/${this.props.id}`, { signal: this.controleur.signal });
      this.setState({ utilisateur: await rep.json(), erreur: null });
    } catch (e) {
      if (e.name !== 'AbortError') this.setState({ erreur: e });
    }
  }

  render() {
    const { utilisateur, erreur } = this.state;
    if (erreur) return <p>Erreur</p>;
    if (!utilisateur) return <p>Chargement…</p>;
    return <h1>{utilisateur.nom}</h1>;
  }
}
```

### 24.5 Optimisation : `PureComponent` et `shouldComponentUpdate`

- **`PureComponent`** : implémente `shouldComponentUpdate` avec une **comparaison superficielle** des props et du state (équivalent de `memo`).
- **`shouldComponentUpdate`** : contrôle manuel (rarement nécessaire).

```jsx
class Ligne extends PureComponent { render() { return <li>{this.props.texte}</li>; } }
```

### 24.6 Refs et contexte dans les classes

```jsx
class Formulaire extends Component {
  inputRef = createRef();
  componentDidMount() { this.inputRef.current.focus(); }
  render() { return <input ref={this.inputRef} />; }
}

class Bouton extends Component {
  static contextType = ThemeContext;                  // un seul contexte via this.context
  render() { return <button className={this.context}>{this.props.children}</button>; }
}
// Plusieurs contextes : <Ctx.Consumer>{valeur => …}</Ctx.Consumer>
```

### 24.7 Valeurs par défaut et validation (classes)

```jsx
class Bouton extends Component {
  static defaultProps = { taille: 'moyenne' };         // toujours supporté pour les CLASSES
}
```

> En React 19, `defaultProps` n'est supporté que pour les classes ; les composants fonctions utilisent les paramètres par défaut. La vérification `propTypes` n'est plus exécutée.

### 24.8 Équivalences Classes ↔ Hooks

| Classe | Composant fonction + Hooks |
|---|---|
| `this.state` / `this.setState` | `useState` / `useReducer` |
| `setState` fusionne | `useState` **remplace** (fusion manuelle avec spread) |
| `constructor` (état initial) | Valeur initiale de `useState` |
| `componentDidMount` | `useEffect(fn, [])` |
| `componentDidUpdate` | `useEffect(fn, [deps])` |
| `componentWillUnmount` | **Cleanup** retourné par `useEffect` |
| `shouldComponentUpdate` / `PureComponent` | `React.memo` (+ `useMemo`/`useCallback`) |
| `getDerivedStateFromProps` | Calcul pendant le rendu / ajustement d'état pendant le rendu |
| `getSnapshotBeforeUpdate` | `useLayoutEffect` (+ ref) |
| `createRef` | `useRef` |
| `static contextType` / `Consumer` | `useContext` / `use` |
| `forceUpdate` | État factice / `useReducer` (à éviter) |
| `getDerivedStateFromError`, `componentDidCatch` | **Aucun équivalent** (classe requise) |
| `this.props` | Argument `props` |
| Méthode d'instance | Fonction dans le corps (ou `useCallback`) |
| Instance (`this.xxx` mutable) | `useRef` |

### 24.9 Migrer une classe vers une fonction

1. Transformer la classe en **fonction** ; `render` → corps de la fonction.
2. `state` → un ou plusieurs **`useState`** (ou `useReducer`).
3. Méthodes → **fonctions internes** ; supprimer `this`.
4. Cycle de vie → **`useEffect`** (un effet **par préoccupation**, avec cleanup).
5. `this.props.x` → **props destructurées**.
6. Refs → `useRef` ; contexte → `useContext`.
7. Conserver les **Error Boundaries** en classe (ou `react-error-boundary`).
8. Tester **avant/après** ; migrer **progressivement** (classes et fonctions cohabitent).

### 24.10 Statut des classes aujourd'hui

- Les composants classes **ne sont pas dépréciés** : l'équipe React indique ne pas prévoir de les retirer, et ils restent **pleinement fonctionnels**.
- Toutes les **nouvelles fonctionnalités** (Hooks, `use`, Actions, `useOptimistic`, `useEffectEvent`, React Compiler) ciblent les **composants fonctions**.
- Une classe **ne peut pas** être un **Server Component** (chapitre 23) ; elle ne peut exister que côté client.
- La seule raison technique d'écrire une classe aujourd'hui est l'**Error Boundary** (chapitre 18), pour laquelle il n'existe pas encore d'équivalent en Hook. Même là, la bibliothèque `react-error-boundary` vous évite de l'écrire.

Conclusion : **écrivez des fonctions**, **sachez lire des classes**, et **migrez au rythme** de vos modifications.

### 24.11 Lire du code existant : motifs fréquents

| Motif | Signification | Équivalent moderne |
| --- | --- | --- |
| `this.setState(prev => ({ n: prev.n + 1 }))` | Mise à jour fonctionnelle | `setN(n => n + 1)` |
| `this.setState({ a: 1 }, () => …)` | Callback exécuté **après** la mise à jour | `useEffect` dépendant de la valeur |
| `componentDidUpdate(prevProps) { if (prevProps.id !== this.props.id) … }` | Réagir à un changement de prop | `useEffect(..., [id])` ou calcul pendant le rendu |
| `static getDerivedStateFromProps` | Dériver l'état des props | Calculer pendant le rendu, ou `key` pour réinitialiser |
| `getSnapshotBeforeUpdate` | Lire le DOM avant le commit | `useLayoutEffect` (cas rare) |
| `static contextType = Ctx` | Lire **un** contexte | `useContext(Ctx)` |
| `defaultProps` | Valeurs par défaut | Paramètres par défaut dans la signature |
| `connect(mapState)(Composant)` (Redux), `withRouter(Composant)` | **Composant d'ordre supérieur** (HOC) | `useSelector`, `useNavigate`, `useParams` |
| `React.createRef()` / `this.ref = React.createRef()` | Ref d'instance | `useRef` |
| `this.interval = setInterval(...)` | Valeur d'instance hors état | `useRef` ou variable d'effet, avec nettoyage |

### 24.12 Migrer progressivement, sans tout réécrire

1. **Sécurisez** d'abord : écrivez ou complétez des **tests** de comportement (chapitre 29) qui passeront avant et après la migration.
2. **Migrez les feuilles** de l'arbre en premier (composants sans enfants complexes), puis remontez.
3. **Migrez à l'occasion** : un composant modifié pour une évolution est converti ; les autres restent en l'état.
4. **Faites coexister** les deux styles : une classe peut rendre une fonction, et une fonction peut rendre une classe. Pour utiliser un Hook dans un composant classe, **enveloppez-le** dans un composant fonction qui lit le Hook et passe le résultat en props :

```jsx
function AvecTheme(Composant) {
  return function Enveloppe(props) {
    const theme = useContext(ThemeContext);      // Hook dans une fonction
    return <Composant {...props} theme={theme} />;
  };
}
export default AvecTheme(ClasseExistante);
```

5. **Outillez-vous** : les *codemods* du dépôt `react-codemod` automatisent certaines transformations (renommage de cycles de vie dépréciés, par exemple) ; ils ne convertissent pas une classe en fonction à votre place, la logique des effets demandant un jugement humain.
6. **Vérifiez** chaque étape : comportement identique, pas de double effet révélé par Strict Mode, pas de régression de performance.

### 24.13 Ce qui ne se traduit pas mot à mot

- **`this.setState` fusionne** l'objet passé avec l'état existant ; **`useState` remplace** la valeur : si l'état est un objet, recopiez les champs (`{ ...ancien, a: 1 }`) ou séparez en plusieurs `useState`.
- **`componentDidMount` + `componentDidUpdate` + `componentWillUnmount`** correspondent à **un seul** `useEffect` avec **dépendances** et **nettoyage** : ne traduisez pas chaque méthode en un effet distinct, regroupez par **responsabilité** (une synchronisation = un effet).
- **Un `useEffect` s'exécute après la peinture** ; `componentDidMount` s'exécutait avant. Pour les mesures qui doivent précéder la peinture, utilisez `useLayoutEffect`.
- **Variables d'instance** (`this.timer`) deviennent des **refs** ; elles ne déclenchent pas de rendu.
- **`shouldComponentUpdate` / `PureComponent`** deviennent `memo` (avec comparateur si nécessaire) ; la comparaison par défaut est **superficielle** dans les deux cas.
- **Fermetures** : dans une fonction, un gestionnaire voit les valeurs **du rendu qui l'a créé** (*instantané*), alors que `this.state` dans une classe est **toujours la dernière valeur**. Un code asynchrone qui dépendait de `this.state` doit être adapté (mise à jour fonctionnelle, ref vers la dernière valeur, `useEffectEvent`).
- **`forceUpdate`** n'a pas d'équivalent recommandé : cherchez quel **état** manque plutôt que de forcer un rendu.

### 24.14 Exemple de conversion commentée

```jsx
// AVANT : classe
class Horloge extends React.Component {
  state = { heure: new Date() };
  componentDidMount()  { this.id = setInterval(() => this.setState({ heure: new Date() }), 1000); }
  componentWillUnmount() { clearInterval(this.id); }
  render() { return <time>{this.state.heure.toLocaleTimeString()}</time>; }
}

// APRÈS : fonction
function Horloge() {
  const [heure, setHeure] = useState(() => new Date());
  useEffect(() => {
    const id = setInterval(() => setHeure(new Date()), 1000);
    return () => clearInterval(id);               // remplace componentWillUnmount
  }, []);                                         // [] : une seule synchronisation au montage
  return <time>{heure.toLocaleTimeString()}</time>;
}
```

Observez : l'état initial est une **fonction d'initialisation paresseuse** ; la variable d'instance `this.id` devient une **constante locale à l'effet** (inutile de la conserver puisque le nettoyage est dans le même scope) ; les trois méthodes de cycle de vie tiennent dans **un effet**.

### 24.15 Pièges fréquents

- Oublier `super(props)` ou lier `this`.
- Modifier `this.state` directement.
- `componentDidUpdate` sans condition → boucle infinie.
- S'attendre à ce que `setState` mette à jour `this.state` immédiatement.
- Oublier de nettoyer dans `componentWillUnmount`.
- Utiliser des méthodes `UNSAFE_`.

### Synthèse du chapitre 24

Les classes fonctionnent toujours, mais on écrit du **neuf avec des fonctions + Hooks** ; `setState` **fusionne** ; `useState` **remplace** ; **Error Boundaries** = seul cas où la **classe est requise** ; Connaître le **cycle de vie** et ses équivalents facilite la **migration**.

---

# Partie IV — Données, navigation, état et styles

## 25. Récupération de données

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : comprendre les approches de récupération de données en React et leurs compromis ; distinguer **état serveur** et **état client** ; maîtriser `fetch`, la gestion d'erreurs, les conditions de course, TanStack Query, SWR, Suspense, les mutations et les mises à jour optimistes.

### 25.1 État serveur vs état client

| | **État client** | **État serveur** |
|---|---|---|
| Origine | Navigateur (UI) | Base de données distante |
| Exemples | Onglet actif, modale ouverte, saisie | Utilisateurs, articles, commandes |
| Propriété | Votre application | **Le serveur** (vous n'avez qu'une **copie**) |
| Particularités | Synchrone, fiable | **Asynchrone**, peut être **obsolète**, **partagé**, **échouer** |
| Outils | `useState`, Context, Zustand | **TanStack Query**, SWR, RTK Query, loaders |

> L'état serveur exige : **cache**, **déduplication**, **revalidation**, **gestion des échecs**, **pagination**, **mutations**, **synchronisation**. Les traiter avec `useState` + `useEffect` est source de bugs.

### 25.2 `fetch` : les bases (et ses pièges)

```js
async function getUtilisateur(id, signal) {
  const reponse = await fetch(`/api/users/${id}`, { signal });
  if (!reponse.ok) {                                       // fetch NE REJETTE PAS sur 404/500 !
    throw new Error(`Erreur HTTP ${reponse.status}`);
  }
  return reponse.json();
}

// POST JSON
await fetch('/api/users', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ nom: 'Ada' }),
});
```

- `fetch` ne rejette **que** sur erreur réseau ; **vérifiez `response.ok`**.
- **Annulation** : `AbortController` (levée `AbortError`).
- **Délai** : `AbortSignal.timeout(5000)`.
- **Cookies** : `credentials: 'include'` pour l'envoi inter-origine.
- **CORS** : configuration côté serveur ; en développement, **proxy** Vite.
- **Axios / ky / ofetch** : clients HTTP avec intercepteurs, erreurs automatiques sur 4xx/5xx, annulation.
- **Typage / validation des réponses** : **Zod** (`schema.parse(json)`) pour ne pas faire confiance aux données externes.

### 25.3 Approche 1 : `useEffect` + `useState`

```jsx
function Utilisateur({ id }) {
  const [etat, setEtat] = useState({ statut: 'chargement', data: null, erreur: null });

  useEffect(() => {
    const controleur = new AbortController();
    setEtat({ statut: 'chargement', data: null, erreur: null });

    getUtilisateur(id, controleur.signal)
      .then(data => setEtat({ statut: 'succes', data, erreur: null }))
      .catch(erreur => {
        if (erreur.name !== 'AbortError') setEtat({ statut: 'erreur', data: null, erreur });
      });

    return () => controleur.abort();                      // évite les conditions de course
  }, [id]);

  if (etat.statut === 'chargement') return <Spinner />;
  if (etat.statut === 'erreur') return <Erreur erreur={etat.erreur} />;
  return <h1>{etat.data.nom}</h1>;
}
```

#### Limites

- Pas de **cache** (rechargement à chaque montage), pas de **déduplication** (deux composants = deux requêtes).
- **Cascades** (*waterfalls*) : l'enfant ne commence qu'après le parent.
- Pas de **revalidation** (focus, reconnexion), **retries**, **pagination**.
- **Rien côté serveur** (les effets ne s'exécutent pas en SSR) : pas de HTML initial utile.
- Beaucoup de code répétitif à maintenir.

### 25.4 Approche 2 : TanStack Query (React Query)

Bibliothèque de référence pour l'état serveur.

```jsx
import { QueryClient, QueryClientProvider, useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const queryClient = new QueryClient({
  defaultOptions: { queries: { staleTime: 60_000, retry: 2 } },
});

<QueryClientProvider client={queryClient}><App /></QueryClientProvider>
```

#### Lecture : `useQuery`

```jsx
function Utilisateurs() {
  const { data, isPending, isError, error, isFetching, refetch } = useQuery({
    queryKey: ['utilisateurs', { page }],          // clé de cache : tableau sérialisable
    queryFn: ({ signal }) => getUtilisateurs({ page }, signal),
    staleTime: 30_000,                              // frais pendant 30 s (pas de refetch)
    placeholderData: keepPreviousData,              // garder l'ancienne page pendant le chargement de la suivante
  });

  if (isPending) return <Spinner />;
  if (isError) return <Erreur message={error.message} onRetry={refetch} />;
  return <Liste items={data.items} />;
}
```

#### Concepts clés

| Concept | Description |
|---|---|
| **`queryKey`** | Identifie la requête dans le cache ; inclure **toutes les variables** dont dépend la requête. |
| **`queryFn`** | Fonction **async** qui retourne les données (doit **lever** en cas d'erreur). |
| **`staleTime`** | Durée pendant laquelle les données sont considérées **fraîches** (défaut 0). |
| **`gcTime`** | Durée de conservation en mémoire d'une requête **inutilisée** (défaut 5 min). |
| **États** | `status` : `pending` / `error` / `success` ; `fetchStatus` : `fetching` / `paused` / `idle`. `isPending` = pas encore de données ; `isFetching` = requête en cours (y compris en arrière-plan). |
| **Revalidation** | Automatique : au **montage**, au **focus** de la fenêtre, à la **reconnexion**, par **intervalle** (`refetchInterval`). |
| **Déduplication** | Plusieurs composants avec la même clé = **une** requête. |
| **Retries** | Rejeu automatique avec backoff exponentiel. |
| **`enabled`** | Requêtes **dépendantes/conditionnelles** (`enabled: !!userId`). |
| **`select`** | Transformer/filtrer les données **sans** re-requête. |
| **Préchargement** | `queryClient.prefetchQuery(...)` (au survol, dans un loader). |
| **DevTools** | `@tanstack/react-query-devtools`. |

#### Écriture : `useMutation`

```jsx
function AjouterTache() {
  const client = useQueryClient();
  const mutation = useMutation({
    mutationFn: (titre) => api.creerTache({ titre }),
    onSuccess: () => client.invalidateQueries({ queryKey: ['taches'] }),   // refetch des listes concernées
  });

  return (
    <button disabled={mutation.isPending} onClick={() => mutation.mutate('Nouvelle tâche')}>
      {mutation.isPending ? 'Ajout…' : 'Ajouter'}
    </button>
  );
}
```

#### Mise à jour optimiste

```jsx
const mutation = useMutation({
  mutationFn: api.basculerTache,
  onMutate: async (id) => {
    await client.cancelQueries({ queryKey: ['taches'] });          // éviter qu'un refetch n'écrase
    const precedent = client.getQueryData(['taches']);             // sauvegarde pour rollback
    client.setQueryData(['taches'], (anciennes) =>
      anciennes.map(t => t.id === id ? { ...t, faite: !t.faite } : t));
    return { precedent };
  },
  onError: (_err, _id, ctx) => client.setQueryData(['taches'], ctx.precedent),   // rollback
  onSettled: () => client.invalidateQueries({ queryKey: ['taches'] }),           // resynchroniser
});
```

#### Pagination et défilement infini

```jsx
// Pagination par pages (offset/curseur) : placeholderData: keepPreviousData
// Défilement infini :
const { data, fetchNextPage, hasNextPage, isFetchingNextPage } = useInfiniteQuery({
  queryKey: ['messages'],
  queryFn: ({ pageParam }) => api.messages({ curseur: pageParam }),
  initialPageParam: null,
  getNextPageParam: (derniere) => derniere.curseurSuivant ?? undefined,
});
```

#### Suspense et SSR

- `useSuspenseQuery` : `data` toujours défini ; l'attente est gérée par `<Suspense>`, les erreurs par un **Error Boundary**.
- **Hydratation/préchargement** serveur : `dehydrate` / `HydrationBoundary`, ou intégration native des frameworks.

### 25.5 Approche 3 : SWR

```jsx
import useSWR from 'swr';

const fetcher = (url) => fetch(url).then(r => { if (!r.ok) throw new Error(r.status); return r.json(); });

function Profil() {
  const { data, error, isLoading, mutate } = useSWR('/api/me', fetcher, { revalidateOnFocus: true });
  if (isLoading) return <Spinner />;
  if (error) return <Erreur />;
  return <p>{data.nom}</p>;
}
```

Philosophie **stale-while-revalidate** : afficher le cache, revalider en arrière-plan. Plus léger et minimaliste que TanStack Query.

### 25.6 Approche 4 : Suspense, `use` et Server Components

- **Server Components** : `await` directement dans le composant (chapitre 23) ; **meilleure** option quand le framework le permet.
- **`use(promesse)`** + `<Suspense>` côté client avec une promesse **mise en cache/créée côté serveur**.
- **Loaders** des routeurs (React Router, TanStack Router) : récupération **avant** le rendu de la route, en **parallèle**.

```jsx
// React Router : loader + composant
export async function loader({ params }) {
  return { utilisateur: await getUtilisateur(params.id) };
}
function Profil() {
  const { utilisateur } = useLoaderData();
  return <h1>{utilisateur.nom}</h1>;
}
```

### 25.7 Autres sources et protocoles

| Besoin | Solution |
|---|---|
| **GraphQL** | Apollo Client, urql, Relay (+ `useSuspenseQuery`) ; TanStack Query avec un client GraphQL |
| **RPC typé de bout en bout** | **tRPC** (+ TanStack Query) |
| **Redux Toolkit** | **RTK Query** (cache + endpoints générés) |
| **Temps réel** | **WebSocket**, **SSE** (`EventSource`), bibliothèques (Socket.IO) → mettre à jour le **cache** de TanStack Query (`setQueryData`) |
| **Sondage (polling)** | `refetchInterval` |
| **Hors ligne / PWA** | Service workers, persistance du cache (`persistQueryClient`), `networkMode` |
| **Fichiers** | `FormData`, uploads avec progression (`XMLHttpRequest`/`axios`), URLs signées |

### 25.8 Authentification des requêtes

- **Cookies `HttpOnly`** + `SameSite` (recommandé, résistants au XSS) ; protéger du **CSRF**.
- **Jetons Bearer** : à éviter dans `localStorage` (vulnérables au XSS) ; préférer mémoire + rafraîchissement via cookie.
- **Intercepteur** (axios/ky) pour ajouter l'en-tête, **rafraîchir** le jeton et **rejouer** la requête sur 401.
- Redirection vers la connexion en cas de 401/403 (via la couche de requêtes, pas dans chaque composant).

### 25.9 Gestion des erreurs et états d'interface

Toujours gérer les **quatre états** : **chargement**, **erreur**, **vide**, **succès** (chapitre 8). Pour les erreurs :
- **Locales** (message + « Réessayer ») ;
- **Globales** (Error Boundary, toasts) ;
- **Typage des erreurs** (statut HTTP, code métier) ;
- **Rapports** (Sentry) sans exposer de détails internes.

### 25.10 Pièges et bonnes pratiques

- **Cascades** : démarrer les requêtes **le plus tôt** et **en parallèle** (loaders, `Promise.all`, préchargement).
- **Conditions de course** : annulation / `ignore` / bibliothèque.
- **Clés de cache** : incluez **tout** paramètre (filtre, page, utilisateur).
- **Ne copiez pas** les données serveur dans un `useState` (double source de vérité) ; utilisez **`select`** ou dérivez.
- **Invalidation après mutation** (ou mise à jour du cache) pour garder la cohérence.
- **Normalisation** : une entité = une source ; éviter des copies divergentes.
- **Pagination côté serveur** pour de grands volumes ; **curseurs** plutôt qu'offset pour les flux mouvants.
- **Mocks de tests** : **MSW** (Mock Service Worker) intercepte au niveau réseau.
- **Ne stockez pas de secrets** dans le code client.

### 25.11 Pièges fréquents

- `fetch` sans vérification de `response.ok`.
- `useEffect(async () => …)` invalide.
- Oublier l'annulation → mises à jour d'un composant obsolète, données d'une ancienne requête.
- `queryKey` incomplète → données mélangées entre paramètres.
- Refetch intempestifs faute de `staleTime`.
- Confondre `isPending` et `isFetching`.
- Cascades de requêtes.

### Synthèse du chapitre 25

**État serveur ≠ état client** : utilisez un outil dédié (**TanStack Query**, SWR, loaders, RSC) ; `fetch` ne rejette pas sur 4xx/5xx ; **annulez** les requêtes obsolètes ; **Cache + revalidation + déduplication + mutations optimistes** = ce que vous n'avez pas à réécrire ; **Parallélisez**, **préchargez**, **gérez les 4 états**.

---

## 26. Routage

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : comprendre le routage côté client et ses mécanismes (History API) ; maîtriser React Router : routes, imbrication, paramètres, navigation, loaders/actions, routes protégées ; connaître les alternatives (TanStack Router, routage par fichiers).

### 26.1 Pourquoi un routeur ?

Dans une **SPA** (*Single Page Application*), le serveur renvoie **une seule page HTML**. Le **routeur côté client** :
1. **Associe l'URL** à une **arborescence de composants** ;
2. **Navigue sans recharger** la page (via la **History API** : `pushState`, `replaceState`, `popstate`) ;
3. Gère **historique**, **liens**, **paramètres**, **requêtes**, **défilement**, **erreurs 404**.

> React **n'inclut pas** de routeur. Solutions : **React Router**, **TanStack Router**, ou un **framework** (Next.js, Remix/React Router v7 framework mode, Expo Router).

### 26.2 React Router : installation et modes

```bash
npm install react-router-dom        # (v7 : les API sont aussi exportées par `react-router`)
```

- **Mode déclaratif** : `<BrowserRouter>` + `<Routes>` / `<Route>`.
- **Mode données (« data router »)** : `createBrowserRouter` + `<RouterProvider>` — **loaders**, **actions**, `errorElement`, transitions, `lazy`.
- **Mode framework** (v7) : routage par configuration, SSR, RSC expérimental.

> Les noms d'import peuvent varier selon la version (v6 : `react-router-dom` ; v7 : `react-router`, avec `react-router-dom` conservé en réexportation). Référez-vous à la documentation de votre version.

#### Types de routeurs

| Routeur | URL | Usage |
|---|---|---|
| `createBrowserRouter` / `BrowserRouter` | `/utilisateurs/42` | Standard (nécessite la **redirection serveur** vers `index.html`) |
| `createHashRouter` / `HashRouter` | `/#/utilisateurs/42` | Hébergement statique sans réécriture |
| `createMemoryRouter` / `MemoryRouter` | (en mémoire) | **Tests**, Storybook, React Native |
| `StaticRouter` | — | SSR (anciennes versions) |

> **Déploiement SPA** : configurez le serveur/CDN pour renvoyer **`index.html`** pour toute route inconnue (sinon 404 au rechargement d'une URL profonde).

### 26.3 Routes de base

```jsx
import { BrowserRouter, Routes, Route, Link, NavLink, Navigate } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <nav>
        <NavLink to="/" end>Accueil</NavLink>
        <NavLink to="/articles" className={({ isActive }) => (isActive ? 'actif' : '')}>Articles</NavLink>
      </nav>

      <Routes>
        <Route path="/" element={<Accueil />} />
        <Route path="/articles" element={<Articles />} />
        <Route path="/articles/:id" element={<Article />} />      {/* paramètre dynamique */}
        <Route path="/ancienne-page" element={<Navigate to="/articles" replace />} />
        <Route path="*" element={<NonTrouvee />} />               {/* attrape-tout (404) */}
      </Routes>
    </BrowserRouter>
  );
}
```

- **`<Link to>`** : navigation sans rechargement (génère un vrai `<a href>`).
- **`<NavLink>`** : ajoute l'état **actif** (`aria-current="page"`, classe `active`, fonction de style).
- **`<Navigate>`** : redirection déclarative (`replace` évite d'empiler l'historique).
- **Correspondance** : classement par spécificité (pas besoin d'`exact`).
- **Segments** : statiques (`/a`), dynamiques (`:id`), optionnels (`:lang?`), **splat** (`files/*`).

### 26.4 Routes imbriquées et layouts

```jsx
<Routes>
  <Route element={<Layout />}>                     {/* route de mise en page (sans path) */}
    <Route index element={<Accueil />} />          {/* route par défaut du parent */}
    <Route path="tableau-de-bord" element={<Tableau />}>
      <Route index element={<Resume />} />
      <Route path="parametres" element={<Parametres />} />
    </Route>
  </Route>
</Routes>

function Layout() {
  return (
    <>
      <Entete />
      <main><Outlet /></main>                      {/* emplacement du rendu de la route enfant */}
      <Pied />
    </>
  );
}
```

### 26.5 Hooks de navigation et d'URL

```jsx
import { useParams, useNavigate, useLocation, useSearchParams, useMatch } from 'react-router-dom';

function Article() {
  const { id } = useParams();                         // paramètres de chemin (chaînes)
  const navigate = useNavigate();
  const location = useLocation();                     // { pathname, search, hash, state }
  const [params, setParams] = useSearchParams();      // ?page=2&tri=date
  const page = Number(params.get('page') ?? 1);

  return (
    <>
      <button onClick={() => navigate(-1)}>Retour</button>
      <button onClick={() => navigate('/articles', { replace: true, state: { depuis: id } })}>Liste</button>
      <button onClick={() => setParams({ page: page + 1 })}>Page suivante</button>
    </>
  );
}
```

> **L'URL comme état** : filtres, tri, pagination, onglet actif → **paramètres de recherche** (partageables, rechargeables, historique du navigateur).

### 26.6 Mode données : loaders, actions, erreurs, `lazy`

```jsx
import { createBrowserRouter, RouterProvider, redirect, useLoaderData, Form, useNavigation } from 'react-router-dom';

const router = createBrowserRouter([
  {
    path: '/',
    element: <Layout />,
    errorElement: <PageErreur />,                       // erreurs de loader/rendu pour ce segment
    children: [
      { index: true, element: <Accueil /> },
      {
        path: 'articles/:id',
        loader: async ({ params, request }) => {        // exécuté AVANT le rendu, en parallèle pour les routes imbriquées
          const rep = await fetch(`/api/articles/${params.id}`, { signal: request.signal });
          if (!rep.ok) throw new Response('Introuvable', { status: 404 });
          return rep.json();
        },
        action: async ({ request, params }) => {        // reçoit les soumissions de <Form method="post">
          const donnees = await request.formData();
          await api.commenter(params.id, donnees.get('texte'));
          return redirect(`/articles/${params.id}`);
        },
        element: <Article />,
      },
      { path: 'admin', lazy: () => import('./routes/admin') },   // code splitting par route
    ],
  },
]);

function Article() {
  const article = useLoaderData();
  const navigation = useNavigation();                   // 'idle' | 'loading' | 'submitting'
  return (
    <>
      <h1>{article.titre}</h1>
      <Form method="post"><textarea name="texte" /><button>Commenter</button></Form>
      {navigation.state !== 'idle' && <Barre />}
    </>
  );
}

<RouterProvider router={router} />
```

Avantages : **chargement en parallèle** (pas de cascade), **revalidation automatique** après actions, **gestion d'erreurs/404** par route, **états de navigation**, **préchargement** (`<Link prefetch>` en mode framework).

### 26.7 Routes protégées (authentification / autorisation)

```jsx
function RouteProtegee({ role }) {
  const { utilisateur, chargement } = useAuth();
  const location = useLocation();
  if (chargement) return <Spinner />;
  if (!utilisateur) return <Navigate to="/connexion" replace state={{ depuis: location }} />;
  if (role && utilisateur.role !== role) return <Navigate to="/interdit" replace />;
  return <Outlet />;
}

<Route element={<RouteProtegee />}>
  <Route path="/compte" element={<Compte />} />
</Route>
<Route element={<RouteProtegee role="admin" />}>
  <Route path="/admin" element={<Admin />} />
</Route>
```

> La protection côté client est une **commodité d'interface** : **l'autorisation réelle doit toujours être vérifiée côté serveur**.

### 26.8 Autres fonctionnalités importantes

- **Restauration du défilement** (`<ScrollRestoration />`) et défilement vers le haut à chaque navigation.
- **Titre de page** par route (métadonnées React 19 `<title>`, `handle`, ou `react-helmet-async`).
- **Transitions de navigation** : combiner avec `startTransition`/View Transitions (`viewTransition` sur `Link`).
- **Blocage de navigation** (formulaire non enregistré) : `useBlocker`.
- **Accessibilité** : après navigation, **déplacer le focus**/annoncer le changement de page (région `aria-live`), titre de document mis à jour.
- **Liens externes** : `<a href target="_blank" rel="noopener noreferrer">`.

### 26.9 Alternatives

| Outil | Particularité |
|---|---|
| **TanStack Router** | Routage **entièrement typé** (chemins, paramètres, search params), loaders, code splitting, génération de routes |
| **Next.js (App Router)** | Routage **par système de fichiers**, layouts, RSC, loaders implicites, `loading.js` / `error.js` |
| **React Router (framework mode) / Remix** | Routage + SSR + actions/loaders |
| **Expo Router** | Routage par fichiers pour React Native |
| **Wouter / Reach Router (obsolète)** | Routeurs minimalistes |

### 26.10 Pièges fréquents

- Oublier la **réécriture serveur** (404 au rafraîchissement).
- `<a href>` au lieu de `<Link>` (rechargement complet).
- Paramètres d'URL toujours des **chaînes** (convertir).
- Chemins relatifs mal compris dans des routes imbriquées.
- Protéger **uniquement côté client**.
- Cascades de requêtes dans des composants imbriqués au lieu de **loaders**.
- Oublier `end` sur `NavLink` de la racine (toujours actif).

### Synthèse du chapitre 26

Le routeur **synchronise URL ↔ UI** via la History API ; **Imbrication + `Outlet`** pour les layouts ; **`useParams` / `useSearchParams`** pour l'URL ; **loaders/actions** pour les données ; **L'URL est un état** : filtres, pagination, onglets ; **Sécurité côté serveur**, **accessibilité** de la navigation.

---

## 27. Gestion d'état global

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : savoir **quand** un état global est nécessaire et **quel type d'état** on gère ; connaître Redux Toolkit, Zustand, Jotai, MobX, XState et leurs philosophies ; choisir et structurer un état global (sélecteurs, normalisation, persistance).

### 27.1 Un état global est-il nécessaire ?

Avant d'ajouter une bibliothèque, vérifiez :

1. **État local** (`useState`) suffit-il ?
2. **Remonter l'état** dans l'ancêtre commun ?
3. **Composition** (`children`) ou **Context** (données stables) ?
4. **État serveur** → **TanStack Query/SWR** (pas un store).
5. **État d'URL** → paramètres de recherche.
6. **État de formulaire** → React Hook Form.

Un store global se justifie pour un état **client** partagé par **de nombreux composants éloignés**, **fréquemment mis à jour**, avec une **logique** non triviale (panier, préférences, brouillon d'éditeur, sélection, notifications, état d'une session de jeu).

#### Typologie

| Type d'état | Outil recommandé |
|---|---|
| UI locale | `useState` / `useReducer` |
| Partagé par un sous-arbre, rarement modifié | Context |
| Client global, fréquent | **Zustand / Redux Toolkit / Jotai** |
| Serveur | **TanStack Query / SWR / RTK Query** |
| URL | Router (`useSearchParams`) |
| Formulaire | **React Hook Form** |
| Machines à états / flux complexes | **XState** |

### 27.2 Principes communs (architecture Flux)

- **Source unique de vérité** : un store (ou des atomes) par domaine.
- **Flux unidirectionnel** : **action → mise à jour → état → vue**.
- **Immutabilité** des mises à jour (ou Immer).
- **Sélecteurs** : les composants s'abonnent à **la portion minimale** d'état qu'ils utilisent → moins de rendus.
- **Dérivation** : calculer (sélecteurs mémoïsés) plutôt que stocker des données redondantes.
- **Normalisation** : `{ byId: {…}, allIds: […] }` pour les collections.
- **Séparation** logique métier / composants.

### 27.3 Redux Toolkit (RTK)

L'approche **officielle** moderne de Redux : moins de code répétitif, Immer intégré, bonnes pratiques par défaut.

```jsx
// store.js
import { configureStore, createSlice, createAsyncThunk } from '@reduxjs/toolkit';

const panierSlice = createSlice({
  name: 'panier',
  initialState: { articles: [] },
  reducers: {
    ajouter(state, action) {                   // Immer : écriture « mutante » sûre
      const existant = state.articles.find(a => a.id === action.payload.id);
      if (existant) existant.quantite += 1;
      else state.articles.push({ ...action.payload, quantite: 1 });
    },
    retirer(state, action) {
      state.articles = state.articles.filter(a => a.id !== action.payload);
    },
    vider: (state) => { state.articles = []; },
  },
});
export const { ajouter, retirer, vider } = panierSlice.actions;

export const store = configureStore({ reducer: { panier: panierSlice.reducer } });

// Types (TypeScript)
export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
```

```jsx
// main.jsx
import { Provider } from 'react-redux';
<Provider store={store}><App /></Provider>

// Composant
import { useSelector, useDispatch } from 'react-redux';

function Panier() {
  const articles = useSelector(s => s.panier.articles);                       // abonnement ciblé
  const total = useSelector(s => s.panier.articles.reduce((t, a) => t + a.prix * a.quantite, 0));
  const dispatch = useDispatch();
  return articles.map(a => <Ligne key={a.id} article={a} onRetirer={() => dispatch(retirer(a.id))} />);
}
```

#### Éléments clés

| Notion | Description |
|---|---|
| **Slice** | Reducer + actions d'un domaine (`createSlice`) |
| **Action** | Objet `{ type, payload }` décrivant ce qui s'est passé |
| **Reducer** | Fonction pure `(état, action) → nouvel état` |
| **Store** | Conteneur unique de l'état (`configureStore`) |
| **Selector** | Fonction qui lit/dérive l'état ; **`createSelector`** (Reselect) pour la mémoïsation |
| **Thunk** | Logique **asynchrone** (`createAsyncThunk`) |
| **Middleware** | Interception des actions (logs, async, analytics) |
| **RTK Query** | Récupération/cache des données serveur intégrée |
| **DevTools** | Time travel, historique d'actions |
| **Listener middleware** | Réactions à des actions (effets) |

**Quand l'utiliser** : grandes équipes, logique complexe, besoin de **traçabilité** (DevTools), conventions strictes. **Coût** : plus de cérémonie que Zustand.

### 27.4 Zustand

Store **minimaliste** basé sur des hooks, sans Provider.

```jsx
import { create } from 'zustand';
import { persist, devtools } from 'zustand/middleware';
import { useShallow } from 'zustand/react/shallow';

const usePanier = create(
  devtools(
    persist(
      (set, get) => ({
        articles: [],
        ajouter: (article) => set((s) => ({ articles: [...s.articles, article] })),
        vider: () => set({ articles: [] }),
        total: () => get().articles.reduce((t, a) => t + a.prix, 0),
      }),
      { name: 'panier' }                                   // persistance dans localStorage
    )
  )
);

function Compteur() {
  const nombre = usePanier((s) => s.articles.length);       // sélecteur : ne re-rend que si ce nombre change
  return <span>{nombre}</span>;
}
function Actions() {
  const { ajouter, vider } = usePanier(useShallow((s) => ({ ajouter: s.ajouter, vider: s.vider })));
}
```

Points forts : API **très simple**, **peu de code**, **sélecteurs** par défaut, **middleware** (persist, devtools, immer), utilisable **hors React** (`usePanier.getState()`).

### 27.5 Jotai (état atomique)

L'état est constitué de petits **atomes** ; les composants s'abonnent à **ceux qu'ils lisent** (rendus minimaux).

```jsx
import { atom, useAtom, useAtomValue, useSetAtom } from 'jotai';

const compteAtom = atom(0);
const doubleAtom = atom((get) => get(compteAtom) * 2);                 // atome dérivé (lecture seule)
const incAtom = atom(null, (get, set) => set(compteAtom, get(compteAtom) + 1));   // atome d'écriture

function C() {
  const [compte, setCompte] = useAtom(compteAtom);
  const double = useAtomValue(doubleAtom);
  const inc = useSetAtom(incAtom);
}
```

Idéal pour un état **fin**, **dérivé**, **localisé** (formulaires riches, éditeurs, canevas). Voisin : **Recoil** (dépôt archivé en 2025, à éviter pour un nouveau projet).

### 27.6 Autres approches

| Outil | Philosophie |
|---|---|
| **MobX** | Observables et réactions **automatiques** (état mutable observable) ; `observer(Composant)` |
| **Valtio** | État **proxy** : on le mute, React se met à jour |
| **XState** | **Machines à états** finis et statecharts : transitions explicites, états impossibles évités (workflows, wizards, médias) |
| **Context + useReducer** | Sans dépendance ; adapté aux petits états globaux peu fréquents |
| **`use-context-selector`** | Sélecteurs sur Context |
| **Nanostores / Legend-State / Effector** | Alternatives spécialisées |

### 27.7 Comparatif

| | **Context + Reducer** | **Redux Toolkit** | **Zustand** | **Jotai** | **MobX** | **XState** |
|---|---|---|---|---|---|---|
| Courbe d'apprentissage | Faible | Moyenne | **Faible** | Faible | Moyenne | Élevée |
| Code répétitif | Moyen | Moyen | **Faible** | Faible | Faible | Élevé |
| Rendus ciblés (sélecteurs) | ❌ | ✅ | ✅ | ✅ (atomes) | ✅ (auto) | ✅ |
| DevTools / traçabilité | Limitée | **Excellente** | Bonne | Bonne | Bonne | **Excellente** (visualiseur) |
| Hors React | ❌ | ✅ | ✅ | ⚠ | ✅ | ✅ |
| Idéal pour | Thème, utilisateur | Grandes applis, équipes | Applis moyennes, simplicité | État fin et dérivé | Modèles objet réactifs | Workflows complexes |

### 27.8 Bonnes pratiques

1. **Ne mettez pas tout** dans le store : seulement l'état **réellement partagé**.
2. **Gardez l'état serveur hors du store** (TanStack Query/RTK Query).
3. **Sélecteurs étroits** : `useStore(s => s.compte)` plutôt que `useStore()` entier.
4. **Données sérialisables** dans Redux (pas de classes, fonctions, `Map`).
5. **Actions décrivant des événements** métier (`commandeValidee`) plutôt que des setters techniques.
6. **Normalisez** les collections ; **dérivez** les calculs.
7. **Découpez** par domaine (slices / stores multiples).
8. **Testez** reducers/stores indépendamment des composants.
9. **Persistance** : whitelist des clés, versionnage/migration (`persist` `version`/`migrate`).
10. **SSR** : instanciez un store **par requête** (pas de singleton partagé entre utilisateurs).

### 27.9 Pièges fréquents

- Mettre **tout** l'état dans Redux par défaut.
- Dupliquer l'état serveur dans le store.
- Sélecteurs qui retournent un **nouvel objet** à chaque appel (rendus infinis/inutiles) → `useShallow`, `createSelector`.
- Muter l'état hors Immer.
- Store singleton partagé entre requêtes en SSR (fuite de données entre utilisateurs).
- Abonner un composant au store entier.

### Synthèse du chapitre 27

**Trouvez d'abord la nature de l'état**, puis l'outil ; **Zustand** pour la simplicité, **Redux Toolkit** pour la structure et la traçabilité, **Jotai** pour l'état atomique, **XState** pour les machines à états ; **Sélecteurs**, **immutabilité**, **normalisation**, **état serveur séparé**.

---

## 28. Styles

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : connaître toutes les approches de style dans React et leurs compromis ; mettre en œuvre thématisation (clair/sombre), variants, responsive et animations ; choisir une stratégie adaptée au contexte (SSR/RSC, équipe, performance, accessibilité).

### 28.1 Panorama

React **ne prescrit pas** de solution de style. Les options :

| Approche | Exemple | Points forts | Points faibles |
|---|---|---|---|
| **CSS global** | `import './App.css'` | Simple, standard | Collisions de noms, portée globale |
| **CSS Modules** | `Bouton.module.css` | **Portée locale** automatique, CSS standard, zéro runtime | Composition dynamique moins fluide |
| **Style inline** | `style={{…}}` | Valeurs **dynamiques** | Pas de pseudo-classes/media queries, pas de cascade, performances si abusif |
| **Préprocesseurs** | Sass/SCSS | Variables, imbrication, mixins | Étape de build (moins utile avec CSS moderne) |
| **Utilitaires** | **Tailwind CSS**, UnoCSS | Rapide, cohérent, pas de nommage, bundle réduit | Classes verbeuses, courbe d'apprentissage |
| **CSS-in-JS (runtime)** | styled-components, Emotion | Styles liés au composant, dynamiques via props | **Coût runtime**, complexité avec **RSC/streaming** |
| **CSS-in-JS (zero-runtime)** | vanilla-extract, Panda CSS, StyleX, Linaria | Typage + **CSS statique** à la compilation | Configuration, contraintes de dynamisme |
| **Bibliothèques UI** | MUI, Chakra, Mantine, Ant Design, shadcn/ui, Radix Themes | Composants prêts, accessibilité | Poids, personnalisation, dépendance |

### 28.2 CSS global et classes

```jsx
import './Bouton.css';
<button className="bouton bouton--primaire">OK</button>
```

Mitiger les collisions : **BEM** (`bloc__element--modificateur`), préfixes, `@layer`, `:where()` pour réduire la spécificité.

#### Classes conditionnelles

```jsx
import clsx from 'clsx';
<button className={clsx('bouton', { 'bouton--actif': actif }, taille && `bouton--${taille}`)} />
```

### 28.3 CSS Modules

```css
/* Bouton.module.css */
.bouton { padding: 0.5rem 1rem; border-radius: 6px; }
.primaire { background: var(--couleur-primaire); color: white; }
```

```jsx
import styles from './Bouton.module.css';
<button className={`${styles.bouton} ${styles.primaire}`} />
```

Les noms (`bouton`) sont **hachés** à la compilation (`Bouton_bouton__x7Ab`) → **pas de collision**. Support natif dans Vite et Next.js.

### 28.4 Style inline

```jsx
<div style={{ width: `${progression}%`, transform: `translateX(${x}px)` }} />
// Variables CSS dynamiques (bonne pratique) :
<div style={{ '--couleur': couleur }} className={styles.carte} />
```

Réservez-le aux **valeurs dynamiques**. Utilisez les **variables CSS** pour passer des valeurs au CSS statique.

### 28.5 Tailwind CSS

```jsx
<button className="rounded-lg bg-blue-600 px-4 py-2 font-medium text-white hover:bg-blue-700 focus-visible:outline focus-visible:outline-2 disabled:opacity-50">
  Valider
</button>
```

- **Utilitaires atomiques**, états `hover:`, `focus:`, `dark:`, **responsive** `md:`, `lg:`.
- Tailwind **v4** : configuration **CSS-first** (`@import "tailwindcss";`, `@theme { … }`), moteur plus rapide.
- Écrire des **composants** (pas de duplication de classes) ; **`cva`** (class-variance-authority) pour les **variants** ; **`tailwind-merge`** pour résoudre les conflits de classes ; helper `cn = (...a) => twMerge(clsx(a))`.
- **shadcn/ui** : composants copiés dans votre code (Radix + Tailwind), très répandu.

```jsx
import { cva } from 'class-variance-authority';
const bouton = cva('rounded font-medium', {
  variants: {
    variante: { primaire: 'bg-blue-600 text-white', secondaire: 'bg-gray-200 text-gray-900' },
    taille:   { sm: 'px-2 py-1 text-sm', md: 'px-4 py-2' },
  },
  defaultVariants: { variante: 'primaire', taille: 'md' },
});
<button className={bouton({ variante: 'secondaire', taille: 'sm' })} />
```

### 28.6 CSS-in-JS

```jsx
import styled from 'styled-components';

const Bouton = styled.button`
  padding: 0.5rem 1rem;
  background: ${({ $primaire }) => ($primaire ? 'royalblue' : 'lightgray')};
  &:hover { filter: brightness(0.95); }
`;
<Bouton $primaire>OK</Bouton>
```

- **Runtime** (styled-components, Emotion) : génèrent des styles **à l'exécution** → coût CPU, nécessitent une **gestion SSR** dédiée, **incompatibles avec les Server Components** (hooks/contexte) sans adaptation. styled-components est annoncé en **mode maintenance** : privilégiez des alternatives pour les nouveaux projets.
- **Zero-runtime** (vanilla-extract, Panda CSS, StyleX, Linaria) : **CSS extrait au build**, compatible RSC.
- `useInsertionEffect` est le hook conçu pour les auteurs de ces bibliothèques.

### 28.7 Thématisation et mode sombre

#### Variables CSS (recommandé)

```css
:root {
  color-scheme: light dark;
  --fond: #fff; --texte: #111; --primaire: #2563eb;
}
@media (prefers-color-scheme: dark) { :root { --fond: #0b0b0f; --texte: #eee; } }
:root[data-theme='dark']  { --fond: #0b0b0f; --texte: #eee; }
:root[data-theme='light'] { --fond: #fff;    --texte: #111; }
body { background: var(--fond); color: var(--texte); }
```

```jsx
function useTheme() {
  const [theme, setTheme] = useLocalStorage('theme', 'system');
  useEffect(() => {
    const racine = document.documentElement;
    if (theme === 'system') racine.removeAttribute('data-theme');
    else racine.dataset.theme = theme;
  }, [theme]);
  return [theme, setTheme];
}
```

- Évitez le **flash** (FOUC) : appliquer le thème par un **script inline** dans `<head>` avant le premier rendu.
- Jetons de conception (**design tokens**) : couleurs, espacements, rayons, typographies, ombres → variables CSS ou fichier de configuration.

### 28.8 Responsive et CSS moderne

- **Mobile-first**, unités relatives (`rem`, `%`, `clamp()`, `vw`).
- **Flexbox**, **Grid**, **gap**, `aspect-ratio`.
- **Container queries** (`@container`) : le composant s'adapte à **son conteneur** (idéal pour la composition).
- **`:has()`**, `:is()`, `:where()`, **CSS nesting**, `@layer`, **`@scope`** selon le support navigateur.
- Hook **`useMediaQuery`** uniquement quand le **JS** doit réagir (sinon CSS pur).
- **Images** responsives : `srcset`, `sizes`, `<picture>`.

### 28.9 Animations

| Besoin | Outil |
|---|---|
| Transitions simples | **CSS** `transition`, `@keyframes`, `animation` |
| Animations d'entrée/sortie, layout, gestes, orchestrations | **Motion** (ex-Framer Motion), **React Spring** |
| Timelines complexes | **GSAP** |
| Transitions entre vues/pages | **View Transitions API** (+ support des frameworks) |
| Animations pilotées par le scroll | CSS `animation-timeline` (si supporté), IntersectionObserver |
| Lottie | `lottie-react` |

Bonnes pratiques :
- Animer **`transform`** et **`opacity`** (composités par le GPU) plutôt que `width`/`top`.
- Respecter **`prefers-reduced-motion`** :

```css
@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
```

- Ne **pas** piloter une animation 60 fps via `setState` ; utiliser CSS ou une bibliothèque dédiée.

### 28.10 Accessibilité des styles

- **Contraste** suffisant (WCAG : 4,5:1 pour le texte normal).
- **Indicateur de focus visible** (`:focus-visible`) : ne jamais supprimer `outline` sans équivalent.
- Ne pas communiquer une information **uniquement par la couleur**.
- Tailles de cibles tactiles suffisantes (≈ 44×44 px).
- Texte **redimensionnable** (unités relatives), `prefers-reduced-motion`, `prefers-contrast`, `forced-colors`.

### 28.11 Choix d'une stratégie

| Contexte | Recommandation |
|---|---|
| Petite app / prototype | CSS Modules ou Tailwind |
| Équipe habituée à l'écriture de CSS | **CSS Modules** + variables CSS |
| Productivité + cohérence design | **Tailwind** (+ `cva`, shadcn/ui) |
| Design system typé multi-plateformes | **vanilla-extract / Panda / StyleX** |
| App existante avec styled-components | Maintenir, migrer progressivement |
| **Server Components** / Next.js App Router | CSS Modules, Tailwind, zero-runtime ; **éviter** CSS-in-JS runtime |
| Délais courts, UI standard | **Bibliothèque UI** (MUI, Mantine, shadcn/ui) |

### 28.12 Pièges fréquents

- CSS global sans convention (collisions, spécificité).
- Abuser de `style={{…}}` pour du statique.
- `className` généré par concaténation hasardeuse (`undefined` dans la chaîne).
- Conflits de classes Tailwind non résolus (utiliser `tailwind-merge`).
- CSS-in-JS runtime avec RSC.
- Flash du thème au chargement.
- Supprimer l'outline de focus.
- Animer des propriétés qui déclenchent le layout.

### Synthèse du chapitre 28

**CSS Modules / Tailwind / zero-runtime** : bon équilibre aujourd'hui ; **variables CSS** pour thèmes ; **Style inline** : valeurs dynamiques uniquement ; **variables CSS** pour passer des valeurs au CSS ; **Accessibilité** : contraste, focus visible, mouvement réduit ; Adaptez votre choix à **RSC/SSR**, à l'**équipe**, à la **performance**.

---

# Partie V — Qualité et essentiels

## 29. Tests

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : définir une stratégie de tests adaptée à une application React (pyramide, outils) ; écrire des tests de composants centrés sur le **comportement utilisateur** avec React Testing Library ; tester hooks, formulaires, asynchronisme, contexte, routage, erreurs et appels réseau ; éviter les tests fragiles.

### 29.1 Stratégie : la pyramide (ou le « trophée ») de tests

| Niveau | Cible | Outils | Vitesse | Quantité |
|---|---|---|---|---|
| **Statique** | Fautes de frappe, types, règles | **TypeScript**, **ESLint**, Prettier | Instantanée | Toujours |
| **Unitaire** | Fonctions pures, reducers, hooks, utilitaires | **Vitest / Jest**, `renderHook` | Très rapide | Beaucoup |
| **Composant / intégration** | Composant(s) + interactions + contexte | **Vitest/Jest + React Testing Library** | Rapide | **La majorité** |
| **E2E** | Parcours complets dans un vrai navigateur | **Playwright**, Cypress | Lent | Peu, parcours critiques |
| **Visuel** | Rendu pixel-perfect | Storybook + Chromatic, Playwright snapshots | Moyen | Composants UI clés |
| **Accessibilité** | Règles WCAG automatisables | `jest-axe`, axe-core, Storybook a11y | Rapide | Systématique |

> **Principe directeur** (Testing Library) : *« Plus vos tests ressemblent à la manière dont votre logiciel est utilisé, plus ils vous donnent confiance. »* Testez ce que **voit et fait l'utilisateur**, pas l'implémentation interne (state, noms de méthodes).

### 29.2 Mise en place (Vitest + Testing Library)

```bash
npm i -D vitest jsdom @testing-library/react @testing-library/user-event @testing-library/jest-dom
```

```js
// vite.config.js
export default defineConfig({
  plugins: [react()],
  test: { environment: 'jsdom', globals: true, setupFiles: './src/test/setup.js' },
});
```

```js
// src/test/setup.js
import '@testing-library/jest-dom/vitest';          // matchers : toBeInTheDocument, toBeDisabled…
import { afterEach } from 'vitest';
import { cleanup } from '@testing-library/react';
afterEach(cleanup);
```

(Avec **Jest** : `jest-environment-jsdom`, `babel-jest` ou `ts-jest`/SWC.)

### 29.3 Premier test de composant

```jsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import Compteur from './Compteur';

test('incrémente le compteur au clic', async () => {
  const user = userEvent.setup();
  render(<Compteur />);

  const bouton = screen.getByRole('button', { name: /cliqué 0 fois/i });
  await user.click(bouton);

  expect(screen.getByRole('button', { name: /cliqué 1 fois/i })).toBeInTheDocument();
});
```

Structure **Arrange – Act – Assert** : préparer (`render`), agir (`user.click`), vérifier (`expect`).

### 29.4 Les requêtes (queries)

#### Priorité recommandée (de la plus à la moins souhaitable)

1. **`getByRole`** (avec `name`) : reflète l'arbre d'accessibilité → **à privilégier**.
2. **`getByLabelText`** (champs de formulaire).
3. `getByPlaceholderText`, **`getByText`**, `getByDisplayValue`.
4. `getByAltText`, `getByTitle`.
5. **`getByTestId`** (`data-testid`) : **en dernier recours** (ce que l'utilisateur ne perçoit pas).

#### Variantes selon le besoin

| Préfixe | 0 résultat | 1 résultat | >1 | Asynchrone |
|---|---|---|---|---|
| `getBy…` | ❌ erreur | ✅ | ❌ erreur | Non |
| `queryBy…` | `null` | ✅ | ❌ erreur | Non |
| `findBy…` | ❌ erreur (après timeout) | ✅ | ❌ erreur | **Oui** (attend) |
| `getAllBy…` / `queryAllBy…` / `findAllBy…` | — | tableaux | — | `findAll` asynchrone |

- **Vérifier l'absence** : `expect(screen.queryByText('x')).not.toBeInTheDocument()`.
- **Attendre l'apparition** : `await screen.findByText('Chargé')`.
- **`within(element)`** : requêtes limitées à une zone.
- **`screen.debug()`**, **`logRoles`**, **Testing Playground** pour trouver la bonne requête.

### 29.5 Interactions : `user-event`

```jsx
const user = userEvent.setup();
await user.click(bouton);
await user.type(screen.getByLabelText('E-mail'), 'ada@exemple.fr');
await user.selectOptions(screen.getByRole('combobox'), 'fr');
await user.keyboard('{Enter}');
await user.tab();
await user.upload(input, fichier);
await user.hover(el);
```

`user-event` simule le **comportement réel** (focus, frappe touche par touche, événements enchaînés) bien mieux que `fireEvent`.

### 29.6 Asynchronisme et `act`

- Les interactions de `user-event` et `findBy`/`waitFor` **enveloppent déjà** les mises à jour dans `act`.
- **`waitFor(() => expect(…))`** : réessaie jusqu'à réussite (assertions seulement, pas d'effets de bord).
- **`waitForElementToBeRemoved`** : attendre la disparition d'un spinner.
- Si vous voyez « *not wrapped in act(…)* » : une mise à jour d'état s'est produite **après** la fin du test → **attendre** l'élément final, ou nettoyer les effets.
- `act` est exporté par `react` (React 19) ; rarement utilisé à la main.
- **Minuteurs** : `vi.useFakeTimers()` / `vi.advanceTimersByTime()` (avec `userEvent.setup({ advanceTimers: vi.advanceTimersByTime })`).

### 29.7 Tester un formulaire

```jsx
test('soumet le formulaire avec les valeurs saisies', async () => {
  const user = userEvent.setup();
  const onSubmit = vi.fn();
  render(<Connexion onSubmit={onSubmit} />);

  await user.type(screen.getByLabelText(/e-mail/i), 'ada@exemple.fr');
  await user.type(screen.getByLabelText(/mot de passe/i), 'secret123');
  await user.click(screen.getByRole('button', { name: /connexion/i }));

  expect(onSubmit).toHaveBeenCalledWith({ email: 'ada@exemple.fr', mdp: 'secret123' });
});

test('affiche une erreur si l’e-mail est invalide', async () => {
  const user = userEvent.setup();
  render(<Connexion onSubmit={vi.fn()} />);
  await user.type(screen.getByLabelText(/e-mail/i), 'pasunemail');
  await user.click(screen.getByRole('button', { name: /connexion/i }));
  expect(await screen.findByRole('alert')).toHaveTextContent(/e-mail invalide/i);
});
```

### 29.8 Tester les hooks

```jsx
import { renderHook, act } from '@testing-library/react';

test('useToggle', () => {
  const { result, rerender } = renderHook(({ init }) => useToggle(init), { initialProps: { init: false } });
  expect(result.current[0]).toBe(false);
  act(() => result.current[1]());
  expect(result.current[0]).toBe(true);
});
```

- Option `wrapper` pour fournir contexte/Providers.
- Préférez tester le hook **à travers un composant** si son comportement dépend fortement du rendu.

### 29.9 Contexte, fournisseurs et routeur : `render` personnalisé

```jsx
// test-utils.jsx
import { render } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

export function renderAvecProviders(ui, { route = '/', ...options } = {}) {
  const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });   // pas de retries en test
  return render(
    <QueryClientProvider client={client}>
      <ThemeProvider>
        <MemoryRouter initialEntries={[route]}>{ui}</MemoryRouter>
      </ThemeProvider>
    </QueryClientProvider>,
    options
  );
}
```

### 29.10 Simuler le réseau : MSW (Mock Service Worker)

Intercepte les requêtes **au niveau réseau** : le code testé fait de vrais `fetch`, sans mock de module.

```js
// mocks/handlers.js
import { http, HttpResponse } from 'msw';
export const handlers = [
  http.get('/api/users/:id', ({ params }) => HttpResponse.json({ id: params.id, nom: 'Ada' })),
  http.post('/api/login', async ({ request }) => {
    const { email } = await request.json();
    return email ? HttpResponse.json({ ok: true }) : new HttpResponse(null, { status: 400 });
  }),
];

// setup : server = setupServer(...handlers) ; beforeAll(server.listen) ; afterEach(server.resetHandlers) ; afterAll(server.close)
// Cas d'erreur dans un test : server.use(http.get('/api/users/1', () => new HttpResponse(null, { status: 500 })))
```

Réutilisable dans le navigateur (développement, Storybook).

### 29.11 Mocks, espions, modules

```js
const fn = vi.fn();                       // fonction espion
vi.spyOn(console, 'error').mockImplementation(() => {});     // erreurs attendues (Error Boundary)
vi.mock('./api', () => ({ getUser: vi.fn().mockResolvedValue({ nom: 'Ada' }) }));
```

> Évitez de **trop mocker** : plus vous mockez de l'implémentation, moins le test est fiable. Préférez MSW pour le réseau, de vrais composants enfants, de vrais Providers.

### 29.12 Cas particuliers

| Cas | Technique |
|---|---|
| **Error Boundary** | Rendre un composant qui lève ; `vi.spyOn(console, 'error')` pour couper le bruit ; vérifier le fallback |
| **Suspense / `lazy`** | `await screen.findBy…` après le fallback |
| **Portals / modales** | `screen` interroge **tout** `document.body` ; vérifier `getByRole('dialog')` |
| **`localStorage`** | `localStorage.clear()` dans `beforeEach` |
| **IntersectionObserver / matchMedia** | Mocks dans le fichier de setup |
| **Composants dépendant du layout** (tailles) | Non fiable en jsdom → tests E2E/navigateur (Vitest Browser Mode, Playwright CT) |
| **Server Components** | Tester la **logique** (fonctions, actions) en unitaire ; l'ensemble en **E2E** |
| **Server Actions** | Tester la fonction comme une fonction async ; validation/permissions ; E2E pour l'intégration |
| **Instantanés (snapshots)** | À utiliser **avec parcimonie** (fragiles, peu significatifs) |

### 29.13 E2E avec Playwright

```js
import { test, expect } from '@playwright/test';

test('un utilisateur peut ajouter une tâche', async ({ page }) => {
  await page.goto('/');
  await page.getByLabel('Nouvelle tâche').fill('Apprendre React');
  await page.getByRole('button', { name: 'Ajouter' }).click();
  await expect(page.getByText('Apprendre React')).toBeVisible();
});
```

- Auto-attente, traces, vidéos, multi-navigateurs, **tests de composants**, captures visuelles, **accessibilité** (`@axe-core/playwright`).
- Limiter les E2E aux **parcours critiques** (connexion, paiement, création de contenu) ; données de test isolées.

### 29.14 Accessibilité automatisée

```jsx
import { axe, toHaveNoViolations } from 'jest-axe';
expect.extend(toHaveNoViolations);

test('pas de violation a11y', async () => {
  const { container } = render(<Formulaire />);
  expect(await axe(container)).toHaveNoViolations();
});
```

Ne détecte qu'une **partie** des problèmes (~30-40 %) : complétez avec la navigation clavier et lecteurs d'écran.

### 29.15 Bonnes pratiques

1. **Tester le comportement**, pas l'implémentation (pas d'accès à `state`, pas de `instance()`).
2. **Requêtes accessibles** (`getByRole`) ; `data-testid` en dernier recours.
3. **Un test = un comportement** ; noms de tests lisibles (« affiche une erreur quand… »).
4. **Isolation** : pas d'ordre d'exécution implicite ; réinitialiser mocks, stockage, serveur.
5. **Pas de dépendances au temps réel** : minuteurs simulés, `findBy`/`waitFor` plutôt que `setTimeout`.
6. **Réseau mocké au niveau réseau** (MSW).
7. Couverture **utile** (chemins critiques) plutôt que 100 % cosmétique.
8. **Intégration continue** : lint + types + tests + build à chaque PR.
9. **ESLint** : `eslint-plugin-testing-library`, `eslint-plugin-jest-dom`.

### 29.16 Pièges fréquents

- Tester l'état interne ou les noms de fonctions → tests cassés au moindre refactoring.
- `getByTestId` partout.
- `fireEvent` à la place de `userEvent`.
- Oublier `await` sur `user.*` ou `findBy`.
- `waitFor` contenant des effets de bord ou plusieurs assertions non liées.
- Snapshots énormes jamais relus.
- Retries de requêtes actifs en test (lenteur et fausses attentes).

### Synthèse du chapitre 29

**Testez comme l'utilisateur** : `render` → `user.*` → `expect(screen.getByRole…)` ; **Vitest/Jest + RTL + MSW** pour 90 % des cas ; **Playwright** pour les parcours critiques ; **Types + lint** détectent beaucoup avant l'exécution ; Évitez snapshots et mocks excessifs.

---

## 30. Accessibilité

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : comprendre les principes d'accessibilité (WCAG, POUR) et leur mise en œuvre en React ; utiliser le HTML sémantique, ARIA, la gestion du focus et les régions live à bon escient ; savoir tester et auditer l'accessibilité.

### 30.1 Pourquoi ?

L'accessibilité (**a11y**) garantit que l'application est utilisable par **tous** : handicaps visuels, auditifs, moteurs, cognitifs, situations temporaires (bras cassé, soleil, bruit) ou contextes (clavier seul, lecteur d'écran, zoom, mobile). C'est aussi une **obligation légale** dans de nombreux pays (en Europe : **Directive européenne sur l'accessibilité**, RGAA en France) et un **plus pour le SEO et l'UX**.

#### Les principes **POUR** (WCAG)

1. **Perceptible** : alternatives textuelles, contrastes, sous-titres.
2. **Utilisable** : clavier, temps suffisant, pas de contenu clignotant, navigation claire.
3. **Compréhensible** : langage clair, comportement prévisible, aide à la saisie.
4. **Robuste** : compatible avec les technologies d'assistance.

Niveaux de conformité : **A**, **AA** (cible courante), **AAA**.

### 30.2 HTML sémantique d'abord

> **Première règle d'ARIA** : si un élément HTML natif fournit déjà la sémantique et le comportement, **utilisez-le** plutôt que d'ajouter des rôles ARIA.

| Au lieu de… | Utilisez |
|---|---|
| `<div onClick>` | **`<button>`** (focus, Entrée/Espace, rôle gratuits) |
| `<div class="lien">` | **`<a href>`** |
| `<div class="titre">` | `<h1>`…`<h6>` hiérarchisés |
| `<div class="nav">` | `<nav>`, `<main>`, `<header>`, `<footer>`, `<aside>`, `<section aria-label>` |
| `<span class="liste">` | `<ul>/<ol>/<li>` |
| Tableaux de mise en page | `<table>` avec `<th scope>` pour les **données** uniquement |
| Groupe de champs | `<fieldset>` + `<legend>` |
| Boîte modale maison | `<dialog>` |

```jsx
// ❌
<div className="bouton" onClick={ouvrir}>Ouvrir</div>
// ✅
<button type="button" onClick={ouvrir}>Ouvrir</button>
```

### 30.3 Structure du document

- **Un seul `<h1>`** par page/vue ; hiérarchie sans saut (`h2` → `h3`).
- **Repères** (*landmarks*) : `<header>`, `<nav>`, `<main>`, `<footer>` ; libellés distincts si plusieurs `<nav>` (`aria-label="Principale"`).
- **Lien d'évitement** (« Aller au contenu ») en début de page.
- **Langue** : `<html lang="fr">` ; `lang` sur les passages dans une autre langue.
- **Titre de page** unique et descriptif, **mis à jour à chaque navigation** (`<title>`).

```jsx
<a href="#contenu" className="lien-evitement">Aller au contenu principal</a>
<main id="contenu" tabIndex={-1}>…</main>
```

### 30.4 ARIA : quand et comment

ARIA (*Accessible Rich Internet Applications*) **complète** la sémantique ; il **ne change ni le comportement ni le focus**.

#### Les trois familles

- **Rôles** : `role="dialog"`, `tablist`, `tab`, `tabpanel`, `alert`, `status`, `menu`, `switch`…
- **États/propriétés** : `aria-expanded`, `aria-selected`, `aria-checked`, `aria-pressed`, `aria-current`, `aria-disabled`, `aria-invalid`, `aria-required`, `aria-busy`, `aria-controls`, `aria-hidden`.
- **Relations/étiquettes** : `aria-label`, `aria-labelledby`, `aria-describedby`.

#### Syntaxe en JSX

Les attributs ARIA gardent leur **forme kebab-case** : `aria-label`, `aria-expanded={ouvert}`, `role="alert"`.

```jsx
<button aria-expanded={ouvert} aria-controls="menu-1" onClick={() => setOuvert(o => !o)}>Menu</button>
<ul id="menu-1" hidden={!ouvert}>…</ul>

<button aria-label="Fermer la fenêtre"><IconeX aria-hidden="true" /></button>   {/* bouton-icône nommé */}
<nav aria-label="Fil d'Ariane"><ol>…<li aria-current="page">Article</li></ol></nav>
```

#### Règles d'or

1. **Natif d'abord**, ARIA ensuite.
2. **Ne changez pas la sémantique native** sans nécessité (`<h2 role="button">` ✗).
3. **Tous les contrôles ARIA** doivent être **utilisables au clavier** (vous implémentez le comportement !).
4. **Pas de `role="presentation"`/`aria-hidden="true"` sur un élément focalisable**.
5. Tout élément interactif a un **nom accessible**.
6. Respectez les **patterns de conception** du **WAI-ARIA Authoring Practices Guide (APG)** pour les widgets complexes (onglets, menus, combobox, dialogues, arbres).

### 30.5 Noms accessibles et étiquettes

Ordre de calcul simplifié : `aria-labelledby` > `aria-label` > contenu/étiquette native (`<label>`, `alt`, `<legend>`) > `title`.

```jsx
<label htmlFor={id}>Nom</label><input id={id} />            // formulaire
<img src={p.url} alt="Portrait d'Ada Lovelace" />            // image informative
<img src="deco.svg" alt="" />                                // image DÉCORATIVE : alt vide
<svg role="img" aria-labelledby={titreId}><title id={titreId}>Ventes 2025</title>…</svg>
```

- Texte du lien **explicite hors contexte** (« Lire l'article sur React » plutôt que « Cliquez ici »).
- Boutons-icônes : `aria-label` ou texte masqué visuellement (`.sr-only`).

```css
.sr-only { position:absolute; width:1px; height:1px; margin:-1px; padding:0; overflow:hidden; clip:rect(0,0,0,0); white-space:nowrap; border:0; }
```

### 30.6 Navigation au clavier et focus

#### Exigences

- **Tout** ce qui est interactif est atteignable **au clavier** (`Tab`/`Shift+Tab`) et activable (**Entrée** pour liens/boutons, **Espace** pour boutons/cases).
- **Ordre de tabulation logique** = ordre du DOM (évitez `tabIndex > 0`).
- **Focus visible** : ne supprimez jamais `outline` sans équivalent (`:focus-visible`).
- `tabIndex={0}` : rend focalisable dans l'ordre ; `tabIndex={-1}` : focalisable **par programme** seulement (cible de `focus()`).
- **Pas de piège clavier**.
- **Raccourcis** : permettre de les désactiver/remapper ; ne pas entrer en conflit avec les lecteurs d'écran.

#### Gestion du focus en React

```jsx
// 1. Dialogue : focus au titre/premier champ à l'ouverture, restauration à la fermeture
const declencheur = useRef(null);
useEffect(() => {
  if (ouvert) { titreRef.current.focus(); }
  else { declencheur.current?.focus(); }
}, [ouvert]);

// 2. Navigation SPA : déplacer le focus vers le titre / main après changement de route
useEffect(() => { document.getElementById('titre-page')?.focus(); }, [location.pathname]);

// 3. Erreur de formulaire : focus sur le premier champ invalide
premierChampInvalideRef.current?.focus();
```

- **Pattern « roving tabindex »** (listes, barres d'outils, onglets) : un seul élément a `tabIndex={0}`, les autres `-1` ; les **flèches** déplacent le focus.
- **`inert`** sur le contenu d'arrière-plan d'une modale (ou `<dialog>.showModal()`).

### 30.7 Annonces dynamiques : régions *live*

Les changements de contenu non liés au focus doivent être **annoncés** :

```jsx
<div role="status" aria-live="polite">{message}</div>        {/* informations non urgentes */}
<div role="alert">{erreur}</div>                             {/* urgent (assertive) */}
```

- La **région doit exister dans le DOM avant** que son contenu change.
- `aria-busy="true"` pendant un chargement ; annoncez « Chargement » / « Résultats : 12 trouvés ».
- Changement de route : annoncer le nouveau titre (région live ou déplacement du focus).
- Évitez de sur-annoncer (frappes, mises à jour fréquentes).

### 30.8 Formulaires accessibles (rappel chapitre 10)

- Champ ↔ `<label>` ; consignes via `aria-describedby`.
- Champs requis : `required` / `aria-required` + indication visuelle **non uniquement colorée**.
- Erreurs : `aria-invalid="true"`, message lié par `aria-describedby`, `role="alert"` ou résumé d'erreurs focalisé.
- `autoComplete` approprié (WCAG 1.3.5), `type`/`inputMode` adaptés.
- Pas de **placeholder** comme unique étiquette.

### 30.9 Couleurs, contrastes, mouvement

- **Contraste** : **4,5:1** (texte normal), **3:1** (grand texte, composants UI, focus).
- Information **jamais transmise uniquement par la couleur**.
- **Zoom** jusqu'à 200 % sans perte ; mise en page **responsive** ; unités relatives.
- **`prefers-reduced-motion`**, `prefers-contrast`, `prefers-color-scheme`, `forced-colors` (mode contraste élevé).
- Évitez le contenu clignotant (> 3 fois/s), les médias lus automatiquement ; fournissez **sous-titres/transcriptions**.

### 30.10 Patterns de composants courants

#### Onglets (tabs)

```jsx
<div role="tablist" aria-label="Sections">
  {onglets.map((o, i) => (
    <button key={o.id} role="tab" id={`tab-${o.id}`} aria-selected={actif === o.id}
            aria-controls={`panel-${o.id}`} tabIndex={actif === o.id ? 0 : -1}
            onClick={() => setActif(o.id)} onKeyDown={gererFleches}>{o.titre}</button>
  ))}
</div>
{onglets.map(o => (
  <div key={o.id} role="tabpanel" id={`panel-${o.id}`} aria-labelledby={`tab-${o.id}`} hidden={actif !== o.id}>{o.contenu}</div>
))}
```

#### Accordéon, menu, combobox, tooltip, dialogue

Suivre les patterns **APG** ou **utiliser des primitives accessibles** : **Radix UI**, **React Aria / React Aria Components**, **Headless UI**, **Ariakit**, **Reach UI**. Elles gèrent clavier, focus, rôles et lecteurs d'écran, que l'on réimplémente difficilement à la main.

### 30.11 Spécificités React

- `htmlFor` (et non `for`), `tabIndex`, `readOnly`, `autoFocus` (à utiliser avec discernement).
- **`useId`** pour relier `label`/`aria-describedby` sans collisions (SSR).
- **Fragments** pour ne pas casser la sémantique (`<tr>`, `<ul>`, `<dl>`).
- **Titre du document** par route ; **focus** après navigation.
- **Listes virtualisées** : fournir `aria-rowcount`/`aria-setsize`/`aria-posinset` si nécessaire.
- **Rendu conditionnel** : retirer un contenu **retire** aussi son sémantique (OK) ; masquer visuellement uniquement avec `display:none`/`hidden` (retire de l'arbre d'accessibilité) vs `.sr-only` (reste lu).
- **Animations d'entrée/sortie** : conserver le focus et la logique clavier.

### 30.12 Tester et auditer

| Outil | Rôle |
|---|---|
| **eslint-plugin-jsx-a11y** | Règles statiques (alt manquant, `div` cliquable, `label` non associé…) |
| **axe DevTools / Lighthouse / WAVE** | Audit automatique dans le navigateur |
| **jest-axe / @axe-core/playwright / Storybook a11y** | Tests automatisés |
| **Navigation clavier** | Parcourir **toute** l'interface sans souris |
| **Lecteurs d'écran** | **NVDA/JAWS** (Windows), **VoiceOver** (macOS/iOS), **TalkBack** (Android) |
| **Zoom, mode sombre, contraste élevé, mouvements réduits** | Vérifications visuelles |
| **Accessibility Tree** (DevTools Chrome/Firefox) | Voir ce que perçoivent les technologies d'assistance |

> L'automatisation détecte seulement une **fraction** des problèmes : le **test manuel** reste indispensable. Idéalement, **impliquez des utilisateurs en situation de handicap**.

### 30.13 Pièges fréquents

- `<div onClick>` sans rôle, focus ni clavier.
- Supprimer l'outline de focus (`outline: none`).
- `alt` manquant, ou `alt` non vide sur image décorative.
- ARIA mal utilisé (pire que pas d'ARIA).
- Modale sans piégeage/restauration du focus ni Échap.
- Changement de page SPA silencieux pour les lecteurs d'écran.
- Message d'erreur affiché mais **non annoncé**.
- Placeholder utilisé comme label.
- Dépendre de la **couleur seule**.

### Synthèse du chapitre 30

**HTML sémantique d'abord**, **ARIA en complément**, **clavier partout**, **focus géré** ; **Noms accessibles** pour tout contrôle ; **alt** adapté ; **contrastes** ; **Annoncer** les changements dynamiques (`role="status"`/`alert`) ; **Bibliothèques headless accessibles** pour les widgets complexes ; **Linter + axe + test clavier + lecteur d'écran**.

---

## 31. TypeScript avec React

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : configurer TypeScript pour React et typer composants, props, hooks, événements, contextes ; utiliser génériques, unions discriminées et types utilitaires pour des API de composants robustes ; connaître les changements de typage de React 19.

### 31.1 Mise en place

```bash
npm create vite@latest mon-app -- --template react-ts
```

```json
// tsconfig.json (extraits)
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["ES2023", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "moduleResolution": "bundler",
    "jsx": "react-jsx",            // transformation automatique (pas d'import React)
    "strict": true,                // indispensable
    "noUncheckedIndexedAccess": true,
    "noUnusedLocals": true,
    "skipLibCheck": true,
    "isolatedModules": true
  }
}
```

Paquets de types : `@types/react`, `@types/react-dom` (versionnés comme React).

### 31.2 Typer les props

```tsx
// `type` ou `interface` : les deux conviennent ; type pour unions/intersections, interface pour extension d'objets
type BoutonProps = {
  variante?: 'primaire' | 'secondaire' | 'danger';
  taille?: 'sm' | 'md';
  onClick: (e: React.MouseEvent<HTMLButtonElement>) => void;
  children: React.ReactNode;
};

function Bouton({ variante = 'primaire', taille = 'md', onClick, children }: BoutonProps) {
  return <button className={`btn btn--${variante} btn--${taille}`} onClick={onClick}>{children}</button>;
}
```

#### Étendre les props natives

```tsx
type BoutonProps = React.ComponentPropsWithoutRef<'button'> & { variante?: 'primaire' | 'danger' };
function Bouton({ variante = 'primaire', className, ...reste }: BoutonProps) {
  return <button className={`btn btn--${variante} ${className ?? ''}`} {...reste} />;
}
// ComponentProps<typeof MonComposant> pour réutiliser les props d'un composant existant
```

#### `ReactNode`, `ReactElement`, `JSX.Element`

| Type | Contient |
|---|---|
| **`React.ReactNode`** | **Tout** ce qui est rendable : élément, string, number, `null`, `undefined`, booléen, tableau, fragment → **à utiliser pour `children`** |
| `React.ReactElement` | Un **élément React** uniquement |
| `React.JSX.Element` | Résultat typique d'une expression JSX (alias d'élément) |
| `React.ComponentType<P>` | Un composant (fonction ou classe) acceptant les props `P` |
| `React.ElementType` | Nom de balise ou composant (pour un `as` polymorphe) |

> **`React.FC`** n'est **plus recommandé** : typez les **props en paramètre** et laissez l'inférence gérer le retour.

#### Unions discriminées (props mutuellement exclusives)

```tsx
type Props =
  | { variante: 'lien'; href: string; onClick?: never }
  | { variante: 'bouton'; onClick: () => void; href?: never };

function Action(props: Props) {
  return props.variante === 'lien' ? <a href={props.href}>…</a> : <button onClick={props.onClick}>…</button>;
}
```

### 31.3 Typer les hooks

```tsx
// useState : inférence, ou générique pour null / unions
const [compte, setCompte] = useState(0);                       // number
const [utilisateur, setUtilisateur] = useState<Utilisateur | null>(null);
const [statut, setStatut] = useState<'idle' | 'chargement' | 'erreur'>('idle');

// useRef : DOM (null initial) vs valeur mutable
const inputRef = useRef<HTMLInputElement>(null);                // RefObject<HTMLInputElement | null> (React 19)
const idRef = useRef<number | undefined>(undefined);           // React 19 : argument OBLIGATOIRE
inputRef.current?.focus();

// useReducer : union discriminée d'actions
type Action = { type: 'ajouter'; titre: string } | { type: 'basculer'; id: string } | { type: 'vider' };
function reducer(etat: Etat, action: Action): Etat {
  switch (action.type) {
    case 'ajouter': return { ...etat, taches: [...etat.taches, { id: crypto.randomUUID(), titre: action.titre, faite: false }] };
    case 'basculer': return { ...etat, taches: etat.taches.map(t => t.id === action.id ? { ...t, faite: !t.faite } : t) };
    case 'vider': return { ...etat, taches: [] };
    default: { const _exhaustif: never = action; return etat; }   // vérification d'exhaustivité
  }
}

// useMemo / useCallback : types inférés ; on peut annoter
const total = useMemo<number>(() => calculer(items), [items]);
const onChange = useCallback((e: React.ChangeEvent<HTMLInputElement>) => setTexte(e.target.value), []);
```

### 31.4 Typer les événements

| Événement | Type |
|---|---|
| Clic | `React.MouseEvent<HTMLButtonElement>` |
| Changement d'input | `React.ChangeEvent<HTMLInputElement>` (`HTMLSelectElement`, `HTMLTextAreaElement`) |
| Soumission | `React.FormEvent<HTMLFormElement>` (ou `SubmitEvent` natif selon version de types) |
| Clavier | `React.KeyboardEvent<HTMLInputElement>` |
| Focus | `React.FocusEvent<HTMLInputElement>` |
| Pointeur / glisser | `React.PointerEvent`, `React.DragEvent` |
| Gestionnaire générique | `React.EventHandler<…>`, `React.MouseEventHandler<HTMLButtonElement>` |

```tsx
function handleChange(e: React.ChangeEvent<HTMLInputElement>) { setNom(e.target.value); }
function handleSubmit(e: React.FormEvent<HTMLFormElement>) { e.preventDefault(); }
const donnees = new FormData(e.currentTarget);
```

### 31.5 Typer Context et hooks personnalisés

```tsx
type AuthContextType = { utilisateur: Utilisateur | null; connexion: (e: string, m: string) => Promise<void>; deconnexion: () => void };
const AuthContext = createContext<AuthContextType | null>(null);

export function useAuth(): AuthContextType {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth doit être utilisé dans <AuthProvider>');   // restreint le type (plus de null)
  return ctx;
}

// Hook générique
function useLocalStorage<T>(cle: string, initial: T) {
  const [valeur, setValeur] = useState<T>(() => { const b = localStorage.getItem(cle); return b ? (JSON.parse(b) as T) : initial; });
  useEffect(() => localStorage.setItem(cle, JSON.stringify(valeur)), [cle, valeur]);
  return [valeur, setValeur] as const;           // tuple readonly [T, Dispatch<…>]
}
```

### 31.6 Composants génériques

```tsx
type ListeProps<T> = {
  items: readonly T[];
  getCle: (item: T) => string | number;
  rendu: (item: T) => React.ReactNode;
};
function Liste<T>({ items, getCle, rendu }: ListeProps<T>) {
  return <ul>{items.map(i => <li key={getCle(i)}>{rendu(i)}</li>)}</ul>;
}
<Liste items={utilisateurs} getCle={u => u.id} rendu={u => u.nom} />     // T inféré = Utilisateur
```

### 31.7 Composants polymorphes (`as`)

```tsx
type TexteProps<E extends React.ElementType> = { as?: E; children: React.ReactNode } &
  Omit<React.ComponentPropsWithoutRef<E>, 'as' | 'children'>;

function Texte<E extends React.ElementType = 'span'>({ as, children, ...reste }: TexteProps<E>) {
  const Balise = as ?? 'span';
  return <Balise {...reste}>{children}</Balise>;
}
<Texte as="a" href="/x">Lien</Texte>        // `href` accepté car E = 'a'
```

### 31.8 Types utilitaires utiles

```ts
Partial<T>   Required<T>   Readonly<T>   Pick<T, K>   Omit<T, K>   Record<K, V>
ReturnType<typeof fn>   Parameters<typeof fn>   Awaited<Promise<X>>   NonNullable<T>
React.ComponentProps<typeof Comp>   React.PropsWithChildren<P>   React.CSSProperties
```

- **`as const`** et **`satisfies`** pour des objets de configuration/variants **typés précisément** :

```ts
const couleurs = { primaire: '#2563eb', danger: '#dc2626' } as const;
type Couleur = keyof typeof couleurs;           // 'primaire' | 'danger'
const routes = { accueil: '/', profil: '/profil' } satisfies Record<string, string>;
```

### 31.9 Types, API et validation à l'exécution

- TypeScript **n'existe plus à l'exécution** : les données **externes** (API, formulaires, `localStorage`) ne sont **pas** garanties.
- **Zod / Valibot** : **un schéma = validation + type inféré**.

```ts
import { z } from 'zod';
const UtilisateurSchema = z.object({ id: z.string(), nom: z.string(), age: z.number().int().optional() });
type Utilisateur = z.infer<typeof UtilisateurSchema>;
const utilisateur = UtilisateurSchema.parse(await rep.json());      // lève si invalide
```

- **tRPC**, **OpenAPI → client typé** (`openapi-typescript`, `orval`) pour des types partagés client/serveur.

### 31.10 Server Components et Actions

```tsx
// Composant serveur asynchrone
export default async function Page({ params }: { params: Promise<{ id: string }> }) {   // forme selon le framework/version
  const { id } = await params;
  const article = await getArticle(id);
  return <h1>{article.titre}</h1>;
}

// Server Function typée
'use server';
export async function creer(etat: Etat, formData: FormData): Promise<Etat> { … }
```

### 31.11 Changements de types avec React 19

- **`useRef`** exige désormais un **argument** (`useRef<T>(undefined)`).
- Les **refs** : `RefObject<T | null>` ; les refs de callback **ne doivent pas retourner autre chose** qu'une fonction de cleanup/`void` (attention aux arrow implicites retournant une valeur).
- Le namespace global **`JSX`** est remplacé par **`React.JSX`**.
- **`ref` comme prop** : typer avec `React.Ref<T>` / `ref?: React.Ref<HTMLInputElement>` (plus de `forwardRef` nécessaire).
- Suppression des types de **fonctionnalités retirées** (`propTypes`, `defaultProps` pour fonctions, `ReactDOM.render`…).
- Codemods : `npx types-react-codemod@latest preset-19 ./src`.

### 31.12 Bonnes pratiques

1. **`strict: true`** toujours ; éviter `any` (préférer `unknown` + affinage).
2. **Ne pas sur-annoter** : laisser l'inférence faire son travail.
3. **Unions discriminées** plutôt que props booléennes contradictoires.
4. **Types dérivés** des schémas/données (`z.infer`, `typeof`, `keyof`) plutôt que dupliqués.
5. Éviter les assertions `as` (surtout `as unknown as X`) ; préférer des **gardes de type** (`function estX(v): v is X`).
6. **Exporter** les types de props des composants publics.
7. **ESLint** (`typescript-eslint`) pour détecter promesses non gérées, `any` implicite, etc.
8. Typer les **frontières** (API, props publiques) rigoureusement ; l'intérieur de l'implémentation peut être plus léger.

### 31.13 Pièges fréquents

- `React.FC` avec `children` implicite (obsolète).
- Typer `children` en `JSX.Element` (refuse les chaînes, `null`…) au lieu de `ReactNode`.
- `useState([])` → `never[]` : préciser `useState<Element[]>([])`.
- `as` pour « faire passer » les erreurs de type.
- Oublier de valider les données externes (le type est un mensonge si l'API change).
- Événements typés trop génériques (`any`).

### Synthèse du chapitre 31

Props typées en paramètre, **`ReactNode`** pour `children`, **`ComponentProps`** pour étendre ; **Génériques** pour hooks/composants réutilisables ; **unions discriminées** pour props exclusives ; Types d'événements précis ; **Context** avec garde de `null` ; **Validation à l'exécution (Zod)** aux frontières ; React 19 : `useRef(undefined)`, `React.JSX`, `ref` comme prop.

---

## 32. Bonnes pratiques

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : synthétiser les règles de conception, de code, de sécurité et d'organisation ; disposer d'une checklist de revue de code et d'une liste d'anti-patterns.

### 32.1 Conception des composants

1. **Responsabilité unique** : un composant fait **une** chose bien (afficher, orchestrer, ou fournir un contexte).
2. **Composition** plutôt que configuration par props nombreuses.
3. **API minimale et explicite** : peu de props, noms clairs, valeurs par défaut sensées.
4. **État le plus bas possible**, remonté seulement si nécessaire.
5. **Données dérivées calculées**, jamais dupliquées dans le state.
6. **Composants purs** : mêmes entrées → même sortie.
7. **Séparer logique et présentation** : hooks pour la logique, composants pour l'affichage.
8. **Composants contrôlés** pour les entrées partagées ; non contrôlés pour la simplicité.
9. **Accessibilité** dès la conception (sémantique, clavier, labels).
10. Penser **les 4 états** d'une vue : chargement, erreur, vide, succès.

### 32.2 Code

- **Nommage** : composants en `PascalCase`, hooks `useXxx`, handlers `handleXxx`, props de callback `onXxx`, booléens `est/a/peut…` (`isOpen`, `hasError`).
- **Immuabilité** : jamais de mutation du state/props.
- **Clés stables** dans les listes (jamais `Math.random()`, index seulement pour listes statiques).
- **Hooks** : règles respectées ; dépendances complètes ; cleanup systématique.
- **Effets** : seulement pour la **synchronisation externe** (« You Might Not Need an Effect »).
- **Mémoïsation** : après mesure ; sinon laisser le **React Compiler** faire.
- **Pas de composants définis dans des composants.**
- **Gestion d'erreurs** explicite (Error Boundaries, `try/catch` dans événements/async).
- **Pas de magie** : éviter `cloneElement`, `Children.map` complexes, HOC imbriqués.
- **Imports** : chemins alias, pas de barrels géants, imports ciblés de bibliothèques.
- **Constantes** et chaînes de caractères externalisées (i18n).
- **Commentaires** : expliquer le **pourquoi**, pas le **quoi**.

### 32.3 Organisation du projet

#### Par fonctionnalité (*feature-based*) : recommandé pour les projets moyens/grands

```
src/
├── app/                      # initialisation : providers, routeur, styles globaux
├── features/
│   ├── panier/
│   │   ├── components/       # composants spécifiques
│   │   ├── hooks/
│   │   ├── api.ts            # appels réseau
│   │   ├── store.ts          # état (si nécessaire)
│   │   ├── types.ts
│   │   ├── index.ts          # API publique de la feature
│   │   └── panier.test.tsx
│   └── auth/
├── components/               # composants UI génériques (Button, Modal, Input…)
├── hooks/                    # hooks transverses (useDebounce…)
├── lib/                      # utilitaires, clients (axios, queryClient)
├── pages/ ou routes/
└── types/
```

- **Colocation** : garder ensemble code, styles, tests, types qui changent ensemble.
- **Frontières** : une feature n'importe pas les **internes** d'une autre (seulement son `index.ts`) ; règle appliquée par ESLint (`import/no-restricted-paths`, `eslint-plugin-boundaries`).
- **Flux de dépendances** : `app → pages → features → components/lib` (jamais l'inverse).
- Éviter les dossiers **fourre-tout** (`utils/` de 80 fichiers).

### 32.4 Sécurité front-end

| Risque | Mesures |
|---|---|
| **XSS** | React échappe par défaut ; **évitez `dangerouslySetInnerHTML`** ou **assainissez** avec DOMPurify ; validez les URLs (`href`/`src`) pour éviter `javascript:` ; **CSP** stricte (`script-src` sans `unsafe-inline`) |
| **Secrets** | Aucune clé secrète dans le bundle (tout ce qui est `VITE_*`/`NEXT_PUBLIC_*` est **public**) ; secrets côté serveur |
| **Stockage de jetons** | Préférer cookies **`HttpOnly` + `Secure` + `SameSite`** ; éviter `localStorage` pour les jetons sensibles |
| **CSRF** | `SameSite`, jetons anti-CSRF, vérification d'origine (Server Actions : géré par le framework) |
| **Dépendances** | `npm audit`, Dependabot/Renovate, **lockfile** commité, `npm ci` en CI, vigilance sur les paquets typosquattés et les nouvelles versions |
| **Autorisation** | **Toujours côté serveur** ; l'UI masque, le serveur **décide** |
| **Données utilisateur** | Valider (Zod) **côté serveur** ; limiter les champs renvoyés |
| **Redirections ouvertes** | Valider les URLs de retour (`?next=`) |
| **Iframes / liens externes** | `rel="noopener noreferrer"`, `sandbox`, `X-Frame-Options`/`frame-ancestors` |
| **Server Functions** | Authentifier, autoriser, valider, limiter le débit |

### 32.5 Performance (rappel)

Mesurer d'abord ; **colocaliser l'état** ; **virtualiser** ; **code splitting** ; **images optimisées** ; **transitions** ; **Compiler** ; **cache de données** ; **SSR/streaming** (chapitre 16).

### 32.6 Internationalisation (i18n) et localisation

- Bibliothèques : **react-i18next**, **FormatJS/react-intl**, **Lingui**, **next-intl**.
- **Pas de chaînes en dur** ; clés de traduction ; **pluriels** et **genres** gérés par la bibliothèque (ICU MessageFormat).
- **`Intl`** natif : `Intl.NumberFormat`, `Intl.DateTimeFormat`, `Intl.RelativeTimeFormat`, `Intl.PluralRules`.
- Prévoir l'**expansion du texte** (allemand), le **RTL** (`dir="rtl"`, propriétés logiques CSS).
- **`lang`** du document à jour.

### 32.7 Qualité, outillage et processus

- **TypeScript strict**, **ESLint** (`react-hooks`, `jsx-a11y`, `typescript-eslint`), **Prettier**.
- **Husky + lint-staged** : vérifier avant commit.
- **CI** : lint → types → tests → build → (E2E) ; **déploiements de prévisualisation**.
- **Conventional Commits**, **revues de code**, **Storybook** pour le design system, **Changesets** pour le versionnage de bibliothèques.
- **Observabilité** : erreurs (Sentry), performances (Web Vitals), journaux, analytics respectueux de la vie privée.
- **Documentation** : README, décisions d'architecture (**ADR**), commentaires de composants (TSDoc).
- **Feature flags** pour des déploiements progressifs.

### 32.8 Anti-patterns : tableau récapitulatif

| Anti-pattern | Conséquence | Correction |
|---|---|---|
| Muter le state | Pas de rendu / bugs | Copies immuables |
| Dériver des données dans un `useEffect` + `setState` | Rendus en cascade | Calculer pendant le rendu |
| `useState(prop)` en attendant la synchro | Valeurs obsolètes | `key`, dérivation, ou `initialXxx` |
| Composant défini dans un composant | Perte d'état, lenteur | Définir au niveau module |
| `key={index}` (liste dynamique) | Mauvais état/DOM | ID stable |
| Dépendances d'effet omises/trichées | Valeurs obsolètes, boucles | Respecter `exhaustive-deps`, `useEffectEvent` |
| `useEffect` pour réagir à un clic | Flux difficile | Gestionnaire d'événement |
| Context pour des valeurs rapides/globales | Rendus massifs | Store avec sélecteurs |
| `memo/useMemo/useCallback` partout | Complexité sans gain | Mesurer / Compiler |
| Prop drilling profond | Rigidité | Composition, Context |
| Composant « Dieu » | Illisible, intestable | Découper, extraire des hooks |
| Données serveur dans un store global | Cache désynchronisé | TanStack Query/SWR |
| Validation seulement côté client | Faille de sécurité | Validation serveur |
| `any`/`as` partout | Faux sentiment de sécurité | Types précis, Zod |
| `<div onClick>` | Inaccessible | `<button>` |
| `dangerouslySetInnerHTML` non assaini | XSS | DOMPurify ou éviter |
| Aucun Error Boundary | Écran blanc | Frontières par zone |
| Requêtes en cascade | Lenteur | Parallélisme, loaders, RSC |

### 32.9 Checklist de revue de code

**Fonctionnel**
- [ ] Les 4 états (chargement/erreur/vide/succès) sont gérés.
- [ ] Les cas limites (listes vides, valeurs nulles, très longs textes) sont couverts.

**React**
- [ ] Composants purs, état minimal et bien placé.
- [ ] Pas de mutation ; clés stables ; pas de composants imbriqués.
- [ ] Effets justifiés, dépendances complètes, cleanup présent.
- [ ] Pas de memoïsation prématurée ; props stables pour les enfants `memo`.

**Accessibilité**
- [ ] Éléments sémantiques, labels, navigation clavier, focus visible.
- [ ] Contrastes, alternatives textuelles, annonces dynamiques.

**Sécurité**
- [ ] Pas de secret client ; entrées validées côté serveur ; autorisations côté serveur.
- [ ] Pas de HTML injecté non assaini.

**Qualité**
- [ ] Types stricts ; pas de `any` injustifié ; lint OK.
- [ ] Tests du comportement ; pas de snapshot superflu.
- [ ] Nommage clair, fichiers colocalisés, documentation utile.

**Performance**
- [ ] Pas de rendus/requêtes inutiles évidents ; code splitting ; images optimisées.

### Synthèse du chapitre 32

**Simplicité** : composants petits, purs, composables ; état local et minimal ; **Rigueur** : effets symétriques, immuabilité, types, tests ; **Responsabilité** : accessibilité, sécurité et performance sont des exigences de base ; **Mesurez** avant d'optimiser ; **automatisez** la qualité (lint, CI).

---

## 33. Écosystème et frameworks

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : cartographier l'écosystème React par besoin ; savoir choisir un framework/outil selon le contexte ; se donner une feuille de route d'apprentissage.

### 33.1 Frameworks et méta-frameworks

| Outil | Description | Quand le choisir |
|---|---|---|
| **Next.js** | Framework full-stack de Vercel : App Router, **RSC**, Server Actions, SSR/SSG/ISR, streaming, routes API, optimisation d'images/polices | Applications publiques, SEO, full-stack React ; très large communauté |
| **React Router v7** (mode framework) / **Remix** | Routage, loaders/actions, SSR, standards web, déploiement flexible | Applications orientées **formulaires et données**, standards du Web |
| **TanStack Start** | Framework full-stack basé sur **TanStack Router**, typage de bout en bout | Typage fort, contrôle |
| **Astro** (îlots React) | Sites orientés contenu, **JS minimal**, composants React en îlots | Blogs, docs, sites marketing |
| **Gatsby** | SSG basé sur GraphQL | Projets existants (moins actif) |
| **Vite (SPA)** | Outil de build rapide, pas de SSR intégré | Tableaux de bord, outils internes, apps derrière authentification |
| **Waku / Parcel (RSC)** | RSC minimalistes | Expérimentation, apps ciblées |
| **Expo / React Native** | Applications **mobiles natives** (iOS/Android) avec React | Mobile ; Expo Router pour le routage |
| **Electron / Tauri** | Applications **desktop** avec React en interface | Desktop multiplateforme |

### 33.2 Outils de build

| Outil | Remarques |
|---|---|
| **Vite** | Standard actuel pour les SPA et bibliothèques |
| **Turbopack / Rspack / Webpack** | Bundlers de gros projets (Next.js utilise Turbopack/Webpack) |
| **esbuild / SWC / Oxc / Rolldown** | Compilateurs/transpileurs rapides (Rust/Go) |
| **Babel** | Transformations et plugins (React Compiler) |
| **tsup / unbuild / Rollup** | Packaging de **bibliothèques** |

### 33.3 Par catégorie

| Catégorie | Outils |
|---|---|
| **Routage** | React Router, TanStack Router, Next.js, Expo Router |
| **Données serveur** | **TanStack Query**, SWR, RTK Query, Apollo/urql/Relay (GraphQL), tRPC |
| **État client** | Zustand, Redux Toolkit, Jotai, MobX, Valtio, XState |
| **Formulaires / validation** | React Hook Form, TanStack Form, Formik, **Zod**, Valibot, Yup |
| **UI / design systems** | shadcn/ui (Radix + Tailwind), MUI, Mantine, Chakra UI, Ant Design, HeroUI, Park UI |
| **Primitives accessibles (headless)** | Radix UI, React Aria, Headless UI, Ariakit |
| **Styles** | CSS Modules, Tailwind, vanilla-extract, Panda CSS, StyleX, styled-components, Emotion |
| **Animation** | Motion (ex-Framer Motion), React Spring, GSAP, Lottie, Auto-Animate |
| **Tableaux / listes** | TanStack Table, TanStack Virtual, AG Grid, react-window, react-virtuoso |
| **Graphiques** | Recharts, Nivo, Visx, Victory, ECharts, D3, Chart.js (`react-chartjs-2`) |
| **Cartes** | react-leaflet, MapLibre GL / react-map-gl, Google Maps (`@vis.gl/react-google-maps`) |
| **Éditeurs de texte** | Tiptap, Lexical, Slate, Plate, CodeMirror, Monaco |
| **Drag & drop** | dnd-kit, react-beautiful-dnd (archivé), Pragmatic drag and drop |
| **Dates** | date-fns, Day.js, Luxon, Temporal (polyfill) ; sélecteurs React Day Picker |
| **i18n** | react-i18next, FormatJS, Lingui, next-intl |
| **3D / jeux** | **React Three Fiber** (Three.js), Drei |
| **Tests** | Vitest, Jest, Testing Library, Playwright, Cypress, MSW, Storybook |
| **Qualité** | ESLint, Prettier, TypeScript, Biome, Husky, lint-staged |
| **Monorepo** | pnpm workspaces, Turborepo, Nx |
| **Documentation UI** | Storybook, Ladle, Histoire |
| **Observabilité** | Sentry, Datadog RUM, LogRocket, Web Vitals |
| **Authentification** | Auth.js (NextAuth), Clerk, Auth0, Supabase Auth, Lucia/Better Auth, Keycloak |
| **Backend-as-a-service** | Supabase, Firebase, Appwrite, Convex |
| **ORM / BD (côté serveur)** | Prisma, Drizzle, Kysely |
| **Outils de développement** | React DevTools, React Scan, why-did-you-render, React Compiler Playground |

### 33.4 Choisir une stack : arbres de décision

```
Besoin de SEO / contenu public dynamique ?
 ├─ Oui → Framework SSR/RSC (Next.js, React Router framework) 
 │        └─ Contenu surtout statique ? → Astro / SSG
 └─ Non (app derrière login) → SPA Vite + TanStack Router/React Router + TanStack Query

Mobile ? → Expo / React Native (+ Expo Router)
Desktop ? → Tauri / Electron

État :
 données serveur → TanStack Query
 état UI simple → useState / Context
 état global fréquent → Zustand (simple) | Redux Toolkit (grandes équipes)
 workflows complexes → XState

UI :
 rapide et accessible → shadcn/ui ou Mantine/MUI
 design system sur mesure → Radix/React Aria + Tailwind/CSS Modules
```

> **Principe** : choisissez des outils **mainstream**, **maintenus**, adaptés à **votre équipe** ; évitez d'ajouter une dépendance sans besoin avéré. Vérifiez : maintenance, taille du bundle, compatibilité React 19 / RSC, TypeScript, accessibilité, licence.

### 33.5 Feuille de route d'apprentissage

1. **Prérequis** : HTML/CSS, **JavaScript moderne**, Git, terminal.
2. **Fondamentaux React** : JSX, composants, props, state, événements, listes/clés, formulaires.
3. **Hooks** : `useState`, `useEffect`, `useRef`, `useContext`, `useReducer`, hooks personnalisés.
4. **Écosystème de base** : routage, requêtes (TanStack Query), formulaires (RHF + Zod), styles (Tailwind/CSS Modules).
5. **TypeScript** + **tests** (Vitest, Testing Library, Playwright).
6. **Performance & concurrence** : `memo`, `useTransition`, Suspense, Profiler, Compiler.
7. **Full-stack** : Next.js / React Router framework : **RSC**, **Server Actions**, authentification, base de données.
8. **Qualité & production** : accessibilité, sécurité, CI/CD, observabilité, i18n.
9. **Approfondissement** : architecture, design system, micro-frontends, monorepos, lecture du code source de React.
10. **Pratique** : projets réels (to-do → blog → e-commerce → tableau de bord → application collaborative).

#### Projets suggérés

| Niveau | Projet | Notions travaillées |
|---|---|---|
| Débutant | Todo list, compteur, quiz | Composants, state, listes, formulaires |
| Intermédiaire | Météo, catalogue de films, blog | Fetch, routage, Context, hooks personnalisés |
| Intermédiaire+ | Tableau de bord avec graphiques | TanStack Query, tableaux, virtualisation |
| Avancé | E-commerce (panier, paiement, admin) | État global, auth, SSR/RSC, tests, a11y |
| Expert | Éditeur collaboratif temps réel / design system | WebSocket, CRDT, headless, Storybook, performance |

---

### 33.6 Comparer les méta-frameworks

| Critère | Next.js | React Router (mode framework) | TanStack Start | Astro + React | Expo (React Native) |
| --- | --- | --- | --- | --- | --- |
| **Cible** | Sites et applications web | Applications web | Applications web | Sites orientés contenu | Applications **mobiles** (iOS, Android) et web |
| **Rendu** | SSR, SSG, ISR, rendu partiel | SSR, SPA, pré-rendu | SSR, SPA | HTML statique, **îlots** React hydratés | Natif |
| **Server Components** | Oui (App Router) | Évolution en cours : consultez la documentation | À vérifier | Non (îlots client) | Selon la version |
| **Routage** | Fichiers (dossiers) | Fichiers ou configuration | Fichiers, typé de bout en bout | Fichiers (pages) | Fichiers (Expo Router) |
| **Points forts** | Écosystème, intégrations, déploiement | Standards du web, formulaires, chargeurs et actions | Typage, intégration TanStack | Peu de JavaScript envoyé | Un seul code pour plusieurs plateformes |
| **À surveiller** | Complexité et rythme des évolutions | Maturité du support RSC | Jeunesse du projet | Interactivité complexe entre îlots | Limites par rapport au natif pur |

> Ce tableau est **volontairement qualitatif** : l'écosystème évolue vite. Avant de décider, relisez la documentation et les notes de version de chaque outil.

### 33.7 Évaluer une dépendance avant de l'adopter

Chaque bibliothèque ajoutée est un **engagement** (maintenance, sécurité, taille). Vérifiez :

| Critère | Question à se poser |
| --- | --- |
| **Maintenance** | Dernière version, fréquence des publications, tickets ouverts, nombre de mainteneurs |
| **Compatibilité** | Fonctionne avec **votre version** de React (19, rendu concurrent, Strict Mode, RSC) ? |
| **Taille** | Poids dans le *bundle* (analyseur de bundle), arborescence (*tree-shaking*) possible ? |
| **TypeScript** | Types fournis et à jour ? |
| **Accessibilité** | Composants conformes aux modèles WAI-ARIA, clavier géré ? |
| **Licence** | Compatible avec votre usage commercial ? |
| **Sécurité** | Historique de vulnérabilités, dépendances transitives, audit (`npm audit`) |
| **Sortie de secours** | Si le projet s'arrête, quel est le coût de remplacement (API standard, abstraction locale) ? |
| **Alternative native** | Le navigateur ou React fait-il déjà l'essentiel (`<dialog>`, CSS, `useReducer`) ? |

Une **couche d'abstraction locale** (un module de votre code qui encapsule la bibliothèque) limite le coût d'un remplacement futur.

### 33.8 React au-delà du navigateur

Le modèle de React (composants, state, rendu déclaratif) se retrouve sur de nombreuses **cibles**, grâce à des *renderers* distincts :

- **React Native** et **Expo** : interfaces mobiles natives.
- **React Email** : messages électroniques générés en HTML compatible clients de messagerie.
- **react-pdf** : documents PDF.
- **react-three-fiber** : scènes 3D (Three.js).
- **Ink** : interfaces en ligne de commande.
- **Remotion** : vidéos programmatiques.

Ce que l'on **réutilise** d'une cible à l'autre : le modèle mental, les Hooks, la logique métier. Ce qui **change** : les éléments de base (pas de `div` en natif), le style, la navigation, l'accessibilité propre à chaque plateforme.

### 33.9 Se tenir à jour

- **Sources officielles** : le blog de React (<https://react.dev/blog>), les notes de version du dépôt, la page des versions de la documentation.
- **Canaux de publication** : *Stable* (production), *Canary* (fonctionnalités validées par l'équipe, destinées aux frameworks), *Experimental* (à ne pas utiliser en production).
- **Mises à jour** : lisez les **guides de migration**, exécutez les **codemods** proposés, mettez à jour par **versions majeures** plutôt que par grands sauts, et vérifiez la compatibilité de vos dépendances avant.
- **Automatisation** : un outil de mise à jour automatique (Renovate, Dependabot) ouvre des demandes de modification régulières, relues et testées par votre intégration continue.
- **Veille raisonnée** : suivez peu de sources fiables ; une nouveauté n'est adoptable qu'après **stabilité** et **bénéfice démontré** pour votre contexte.

### 33.10 Documenter ses choix techniques

Un choix de stack se justifie par des **critères explicites** et se retrouve dans un **document d'architecture** (*Architecture Decision Record*, ADR) court : contexte, options étudiées, décision, conséquences, date. Quand le contexte change (équipe, charge, nouveautés), l'ADR permet de **réviser** la décision en connaissance de cause plutôt que par effet de mode.

### Synthèse du chapitre 33

L'écosystème React est **modulaire** : React fournit le **rendu**, tout le reste se choisit. Pour un **nouveau projet**, partez d'un **méta-framework** (Next.js, React Router en mode framework) ou d'une **SPA Vite** ; ajoutez une bibliothèque de **données serveur** (TanStack Query), un **routeur**, un état global **seulement si nécessaire**, puis des outils de **test**, de **style** et d'**accessibilité**. Choisissez selon vos **contraintes** (SEO, rendu serveur, équipe, durée de vie du projet) et vérifiez la **maintenance** de chaque dépendance avant de l'adopter.

---

## 34. Glossaire et ressources

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : .

### 34.1 Glossaire

| Terme | Définition |
|---|---|
| **Action** | Fonction (souvent async) passée à `<form action>` ou exécutée dans une transition ; gère pending/erreur/optimisme. |
| **Activity** | Composant (19.2) pour masquer un sous-arbre en préservant son état et en suspendant ses effets. |
| **Batching** | Regroupement de plusieurs mises à jour d'état en un seul rendu. |
| **Bail-out** | Absence de re-rendu quand la nouvelle valeur d'état est identique (`Object.is`). |
| **Children** | Prop spéciale contenant le JSX placé entre les balises d'un composant. |
| **Client Component** | Composant exécuté dans le navigateur (et pré-rendu en SSR), marqué par `'use client'`. |
| **Commit** | Phase où React applique les changements au DOM. |
| **Composant** | Fonction (ou classe) retournant du JSX, nom en PascalCase. |
| **Composant contrôlé** | Champ dont la valeur est pilotée par le state React. |
| **Composant non contrôlé** | Champ dont la valeur est conservée par le DOM. |
| **Composant pur** | Même entrée → même sortie, sans effet de bord pendant le rendu. |
| **Concurrent rendering** | Rendu interruptible et priorisé. |
| **Context** | Mécanisme de diffusion d'une valeur à un sous-arbre sans props. |
| **Custom hook** | Fonction `useXxx` composant d'autres hooks. |
| **Délégation d'événements** | Écouteurs attachés à la racine, dispatch par React. |
| **Dépendances (effet)** | Valeurs réactives qui déterminent quand un effet se re-synchronise. |
| **Diffing** | Comparaison de deux arbres pour calculer les changements. |
| **Effect (effet)** | Code de synchronisation avec un système externe (`useEffect`). |
| **Effect Event** | Fonction non réactive utilisée dans un effet (`useEffectEvent`). |
| **Element (élément)** | Objet immuable décrivant l'UI (résultat de JSX). |
| **Error Boundary** | Composant classe interceptant les erreurs de rendu des descendants. |
| **Fiber** | Architecture interne de React : unités de travail interruptibles. |
| **Fragment** | Regroupe des éléments sans nœud DOM (`<>…</>`). |
| **Hook** | Fonction `useXxx` permettant d'utiliser état/effets/etc. dans un composant fonction. |
| **HOC** | Fonction qui prend un composant et retourne un composant enrichi. |
| **Hydratation** | Attachement de l'interactivité à du HTML produit par le serveur. |
| **Immutabilité** | Ne pas modifier une donnée existante ; en créer une nouvelle. |
| **JSX** | Extension de syntaxe JavaScript pour décrire l'UI. |
| **Key** | Identifiant stable d'un élément parmi ses frères, utilisé par la réconciliation. |
| **Lazy loading** | Chargement différé de code (`lazy`) ou de ressources. |
| **Memoization** | Mise en cache d'un résultat pour éviter un recalcul (`useMemo`, `memo`). |
| **Mount / Unmount** | Apparition / disparition d'un composant dans l'arbre. |
| **Portal** | Rendu d'enfants dans un autre nœud DOM. |
| **Prop drilling** | Passage de props à travers des niveaux intermédiaires inutiles. |
| **Props** | Arguments d'un composant, en lecture seule. |
| **Reconciliation** | Processus de mise à jour du DOM à partir de deux arbres d'éléments. |
| **Ref** | Objet `{ current }` mutable hors rendu ; accès au DOM. |
| **Render** | Appel d'un composant pour calculer son JSX. |
| **RSC** | React Server Components : composants exécutés uniquement côté serveur/build. |
| **Selector** | Fonction qui lit/dérive une portion de l'état d'un store. |
| **Server Function** | Fonction `'use server'` appelable depuis le client. |
| **Snapshot (état)** | Valeur figée du state pour un rendu donné. |
| **SSR / SSG / ISR / CSR** | Rendu serveur / statique / statique régénéré / client. |
| **State** | Mémoire d'un composant dont la modification déclenche un rendu. |
| **StrictMode** | Vérifications supplémentaires en développement. |
| **Suspense** | Mécanisme d'attente avec interface de repli. |
| **Transition** | Mise à jour non urgente, interruptible. |
| **Virtual DOM** | Représentation légère en mémoire de l'UI désirée. |
| **Virtualisation** | Rendu des seuls éléments visibles d'une longue liste. |

### 34.2 Aide-mémoire des Hooks

| Hook | Rôle en une ligne |
|---|---|
| `useState` | État local déclenchant un rendu |
| `useReducer` | État complexe via reducer pur |
| `useContext` | Lire un contexte |
| `useRef` | Valeur mutable hors rendu / nœud DOM |
| `useImperativeHandle` | Exposer une API impérative via ref |
| `useEffect` | Synchroniser avec l'extérieur (après peinture) |
| `useLayoutEffect` | Effet synchrone avant peinture |
| `useInsertionEffect` | Injection de styles (CSS-in-JS) |
| `useEffectEvent` | Logique d'événement non réactive dans un effet |
| `useMemo` | Mémoriser une valeur |
| `useCallback` | Mémoriser une fonction |
| `useTransition` | Marquer une mise à jour non urgente + `isPending` |
| `useDeferredValue` | Valeur retardée |
| `useSyncExternalStore` | S'abonner à un store externe |
| `useId` | Identifiant unique SSR-safe |
| `useDebugValue` | Étiquette DevTools |
| `use` | Lire promesse/contexte (même conditionnel) |
| `useActionState` | État d'une action de formulaire |
| `useFormStatus` | Statut du formulaire parent |
| `useOptimistic` | État optimiste temporaire |

### 34.3 Ressources officielles et recommandées

- **Documentation React** : <https://react.dev> (Learn, Reference, Blog, « You Might Not Need an Effect », « Thinking in React »).
- **Référence des API** : <https://react.dev/reference/react>
- **Blog React** (annonces de versions) : <https://react.dev/blog>
- **React Compiler** : <https://react.dev/learn/react-compiler>
- **TypeScript + React** : React TypeScript Cheatsheets.
- **WAI-ARIA Authoring Practices (APG)** : <https://www.w3.org/WAI/ARIA/apg/>
- **TanStack** (Query, Router, Table, Form, Virtual) : <https://tanstack.com>
- **Testing Library** : <https://testing-library.com> ; **Playwright** : <https://playwright.dev>
- **MDN Web Docs** : JavaScript, HTML, CSS, accessibilité.
- **Next.js** : <https://nextjs.org/docs> ; **React Router** : <https://reactrouter.com>
- **Patterns.dev** : patterns de conception et de rendu.
- **web.dev** : performance, Core Web Vitals, accessibilité.

> L'écosystème évolue vite : vérifiez toujours la **version** de la documentation correspondant à votre projet.

### 34.4 Carte mentale : l'essentiel en 15 phrases

1. **UI = f(state)** : l'interface est une fonction de l'état.
2. Un **composant** est une **fonction pure** qui retourne du **JSX**.
3. Les **props** descendent, les **événements/callbacks** remontent.
4. Le **state** est un **instantané** ; on le met à jour par **copie immuable**.
5. Le rendu = **render → commit → effets** ; seul le **minimum** du DOM change.
6. Les **clés** donnent l'**identité** ; changer la `key` **réinitialise**.
7. Les **Hooks** s'appellent **au niveau supérieur**, **dans le même ordre**.
8. **`useEffect` synchronise** avec l'extérieur ; **calculez** le reste pendant le rendu.
9. **Refs** pour le DOM et les valeurs hors rendu ; **Context** pour diffuser.
10. **Composition** (`children`, slots, hooks) plutôt qu'héritage.
11. **Mesurez** avant d'optimiser ; **colocalisez** l'état ; **virtualisez** ; **découpez** le code.
12. **Suspense + transitions + concurrence** gardent l'UI fluide.
13. **RSC** réduisent le JS client ; **Server Functions** = endpoints à **sécuriser**.
14. **TypeScript, tests, accessibilité, sécurité** font partie du code « terminé ».
15. **Simple d'abord** : état local → remonter → Context → store ; données serveur → bibliothèque dédiée.

---

*Fin du cours.*

### 34.5 Index des API par chapitre

| API | Rôle en une phrase | Chapitre(s) |
| --- | --- | --- |
| `createRoot`, `hydrateRoot` | Démarrer React dans le navigateur / hydrater du HTML serveur | 2, 22 |
| JSX, `createElement` | Décrire l'interface | 3 |
| `useState`, `useReducer` | État local | 6, 11 |
| `useEffect`, `useLayoutEffect`, `useEffectEvent` | Synchroniser avec l'extérieur | 11, 21 |
| `useContext`, `createContext`, `use(Context)` | Diffuser une valeur dans un sous-arbre | 13 |
| `useRef`, `useImperativeHandle`, `ref` en prop | Valeurs hors rendu, accès au DOM | 14 |
| `Children`, `cloneElement`, composants composés | Composition avancée | 15 |
| `memo`, `useMemo`, `useCallback`, React Compiler | Éviter le travail inutile | 16 |
| `lazy`, `Suspense`, `use(promesse)` | Chargement différé, données asynchrones | 17 |
| Error Boundary (classe), `react-error-boundary` | Contenir les erreurs de rendu | 18 |
| `createPortal` | Rendre hors de la hiérarchie DOM | 19 |
| `Fragment`, `<>…</>` | Regrouper sans nœud DOM | 20 |
| `StrictMode` | Vérifications en développement | 21 |
| `useTransition`, `startTransition`, `useDeferredValue`, `Activity`, `useSyncExternalStore` | Rendu concurrent | 11, 22 |
| `'use client'`, `'use server'`, Actions, `useActionState`, `useFormStatus`, `useOptimistic` | Serveur, formulaires, mutations | 10, 23 |
| `Component`, `PureComponent` | Composants classes | 24 |
| `useId`, `useDebugValue`, `useInsertionEffect` | Utilitaires et bibliothèques | 11 |

Cet index renvoie au chapitre où chaque API est **principalement** expliquée ; plusieurs sont **reprises** dans d'autres chapitres (par exemple les transitions en 17, 22 et 23).

### 34.6 Parcours de relecture par objectif

| Objectif | Chapitres à relire |
| --- | --- |
| Écrire un premier composant fiable | 1 à 6 |
| Comprendre pourquoi « ça se re-rend » | 4, 6, 11, 13, 16, 22 |
| Gérer des formulaires et des données | 10, 23, 25, 27 |
| Rendre une application rapide | 16, 17, 22, 28 |
| Fiabiliser (erreurs, tests, accessibilité) | 18, 21, 29, 30 |
| Travailler sur un projet existant | 24, 31, 32 |
| Choisir une stack | 26, 27, 33 |

---

*Fin du cours. Bon développement avec React !*
