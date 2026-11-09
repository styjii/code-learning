# Vue.js 3 et TypeScript — Cours complet

*Cours magistral et module d'apprentissage exhaustif, fondé sur le plan « Vue.js 3 + TypeScript » — Vue 3.5 (version stable) et Vue 3.6 (candidate à la sortie) — novembre 2026*

## Avant de commencer : comment utiliser ce cours

Ce cours développe, chapitre par chapitre, l'intégralité du plan en **26 chapitres**, regroupés en six parties : **Fondamentaux** (1 à 9), **Composants et réutilisation** (10 à 16), **Écosystème officiel** (17 à 19), **Avancé** (20 et 21), **Tests et performance** (22 et 23) et **Essentiels** (24 à 26). Deux annexes (glossaire et aide-mémoire) complètent l'ensemble.

Chaque chapitre suit la même trame : *objectifs d'apprentissage → notions et définitions → exemples de code commentés → pièges fréquents → synthèse*.

**Conventions de lecture**

- **(à jour)** : pratique moderne qui remplace une ancienne. **(héritage)** : ancienne approche, encore fréquente dans les projets existants. **(ajout)** : notion absente des anciens guides ou apparue récemment.
- Le code est écrit en **TypeScript strict**, avec la **Composition API** et la syntaxe **`<script setup lang="ts">`**. Les fichiers sont placés sous `src/` ; l'alias `@/` désigne `src/`.
- Chaque exemple est volontairement **autonome** : les imports nécessaires sont toujours indiqués. Le premier commentaire d'un bloc de code indique, quand c'est utile, le chemin du fichier.
- Le cours enseigne le Vue **actuel** (Composition API, `<script setup>`, `defineModel`, `useTemplateRef`, Pinia, Vue Router, Vite) **et** explique l'ancien (Options API, mixins, `Vue.set`, Vuex) pour que vous sachiez lire du code existant.
- **Prérequis** : HTML et CSS, JavaScript moderne (ES2015 et suivants : modules, `const` / `let`, fonctions fléchées, déstructuration, opérateur de décomposition, classes, `Promise` et `async` / `await`) et des notions de base de TypeScript (types, interfaces, génériques).

**État de l'écosystème à la date de rédaction.** La version stable de Vue est la branche **3.5** (correctifs fréquents). La branche **3.6** est en **candidate à la sortie** : elle réécrit le moteur de réactivité (sur la base de la bibliothèque *alien-signals*) et introduit le **mode Vapor** (optionnel, chapitre 23). Elle ne doit pas être utilisée en production tant que la version finale n'est pas publiée. **Vue Router 5** (routage par fichiers intégré au cœur), **Pinia 3**, **Nuxt 4** et **Vitest** sont les versions de référence de l'écosystème. Les détails de version sont à vérifier sur la documentation officielle avant tout projet.

**Parcours conseillé** : lisez les chapitres 1 à 10 dans l'ordre (ils se construisent les uns sur les autres), puis choisissez librement dans les parties suivantes selon vos besoins.

---

# Partie I — Fondamentaux

## 1. Introduction et installation

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : définir Vue et expliquer ce qui le distingue ; décrire les deux piliers du framework (rendu déclaratif et réactivité) ; expliquer le modèle de composants, le DOM virtuel et le compilateur ; distinguer Vue 2 et Vue 3, Options API et Composition API ; comparer Vue à Angular et à React ; situer les versions dans le temps ; créer un projet Vue + TypeScript avec `create-vue` ; comprendre le rôle de chaque fichier généré ; configurer TypeScript et les outils de vérification de types.

### 1.1 Qu'est-ce que Vue ?

**Vue** (prononcé « vioue », comme *view* en anglais) est un **framework JavaScript** open source pour construire des **interfaces utilisateur** et des **applications monopages** (*SPA*, *Single Page Applications*). Il a été créé en **2014** par **Evan You**, ancien ingénieur chez Google, et il est aujourd'hui maintenu par une équipe cœur et une large communauté. Il est entièrement écrit en **TypeScript**.

Vue est qualifié de **progressif** : on peut l'adopter **graduellement**, de la simple amélioration d'une page HTML existante jusqu'à l'application complète rendue côté serveur. Le framework n'impose pas de tout adopter d'un bloc.

| Niveau d'adoption | Usage |
| --- | --- |
| Balise `<script src>` | Améliorer une page HTML existante, sans étape de compilation |
| Composants web (*Web Components*) | Éléments natifs réutilisables partout (`defineCustomElement`) |
| Application monopage | Application complète avec routeur et gestion d'état |
| Rendu serveur / génération statique | SSR ou SSG, généralement avec **Nuxt** |
| Mobile et bureau | Capacitor, Ionic, Quasar, Electron, Tauri |

**Framework ou bibliothèque ?** Vue se situe entre les deux. Son **cœur** ne s'occupe que de la couche d'affichage (comme une bibliothèque), mais il est entouré d'un **écosystème officiel** cohérent : **Vue Router** (navigation), **Pinia** (état global), **Vite** (outil de build), **Vitest** (tests), **Nuxt** (méta-framework full-stack). Contrairement à Angular, ces briques sont **séparées** et optionnelles ; contrairement à React, elles sont **officielles** et maintenues par la même équipe.

#### Les deux piliers de Vue

1. **Le rendu déclaratif.** On décrit **ce que** l'interface doit afficher en fonction de l'état, et non **comment** manipuler le DOM étape par étape. On écrit un gabarit HTML étendu ; Vue se charge des mises à jour.
2. **La réactivité.** Vue **suit automatiquement** les changements de l'état JavaScript et met à jour le DOM de façon efficace, sans que vous ayez à signaler quoi que ce soit.

```vue
<!-- src/components/Compteur.vue -->
<script setup lang="ts">
import { ref } from 'vue'

const count = ref(0)               // état réactif
</script>

<template>
  <button @click="count++">Compteur : {{ count }}</button>
</template>
```

La comparaison suivante montre la différence entre l'approche **impérative** (JavaScript pur) et l'approche **déclarative** (Vue).

```ts
// Impératif : on gère le DOM à la main
let count = 0
const btn = document.querySelector('button')!
btn.addEventListener('click', () => {
  count++
  btn.textContent = `Compteur : ${count}`   // il faut penser à chaque mise à jour
})

// Déclaratif (Vue) : on modifie l'état, Vue met à jour le DOM
// count.value++  →  le gabarit est re-rendu automatiquement, aux seuls endroits concernés
```

Plus l'interface grandit, plus l'approche impérative devient difficile à maintenir : chaque modification de l'état exige de se souvenir de **tous** les endroits du DOM à mettre à jour. L'approche déclarative élimine cette catégorie d'erreurs.

### 1.2 Les concepts fondateurs

Voici le vocabulaire minimal. Chaque terme sera approfondi dans un chapitre dédié.

- **Composant** : brique d'interface qui encapsule un **gabarit** (HTML), une **logique** (TypeScript) et des **styles** (CSS). Une application est un **arbre de composants**.
- **Composant monofichier (SFC)** : fichier `.vue` qui regroupe le gabarit, le script et le style d'un composant (chapitre 2).
- **Gabarit (*template*)** : HTML enrichi de la syntaxe Vue (interpolation `{{ }}`, directives `v-…`), compilé en fonction de rendu (chapitre 3).
- **Directive** : attribut spécial préfixé par `v-` qui applique un comportement réactif au DOM (`v-if`, `v-for`, `v-model`…).
- **État réactif** : données dont la modification déclenche automatiquement des mises à jour (`ref`, `reactive`, chapitre 4).
- **Propriété calculée (`computed`)** : valeur **dérivée** d'autres données, mise en cache.
- **Observateur (`watch`)** : fonction exécutée en réaction à un changement, pour produire un **effet de bord**.
- **Prop** : donnée transmise d'un composant **parent** à un composant **enfant** (chapitre 10).
- **Événement émis (`emit`)** : notification envoyée d'un enfant vers son parent.
- **Slot** : emplacement dans un composant où le parent injecte du contenu (chapitre 11).
- **Composable** : fonction réutilisable qui encapsule une **logique à état** en s'appuyant sur la Composition API (chapitre 13).
- **Plugin** : extension qui ajoute des fonctionnalités à l'échelle de l'application (chapitre 15).
- **Routeur** et **store** : navigation entre pages et état global partagé (chapitres 17 et 18).

### 1.3 Architecture générale d'une application

Une application Vue est un **arbre de composants**. Le composant racine est monté dans un élément de la page HTML ; il contient des composants enfants, qui en contiennent d'autres.

```text
index.html
   └── <div id="app">                   ← élément hôte
          └── App.vue (composant racine)
                 ├── TheHeader
                 │     ├── Logo
                 │     └── NavMenu
                 └── <RouterView>       ← zone où le routeur affiche la page courante
                        └── Page (composant de vue)
                               ├── ArticleList
                               │     └── ArticleCard (× N)
                               └── Sidebar

Stores Pinia, plugins, provide/inject ←— état et services partagés, accessibles aux composants
```

**Le flux de données est unidirectionnel** : « **props vers le bas, événements vers le haut** ». Les données descendent du parent vers l'enfant par les *props* ; les enfants informent leur parent par des *événements*. Cette règle rend le flux de données **prévisible** et les bogues faciles à localiser.

**Cycle d'une interaction :**

1. L'utilisateur clique sur un bouton : le gestionnaire `@click` s'exécute.
2. Le gestionnaire **modifie l'état réactif** (`count.value++`).
3. Vue sait quels effets (rendu de composants, propriétés calculées, observateurs) **dépendent** de cette donnée et les **replanifie**.
4. Au prochain « tick », Vue re-génère l'arbre virtuel des composants concernés, le compare au précédent et applique au DOM **uniquement les différences**.

#### Le DOM virtuel et le compilateur

- Un **DOM virtuel** (*Virtual DOM*) est une représentation légère en mémoire de l'arbre DOM réel, faite d'objets JavaScript appelés **nœuds virtuels** (*VNodes*).
- À chaque changement d'état, Vue produit un nouvel arbre virtuel, le **compare** au précédent (*diffing*) et applique au DOM réel les seules différences (*patch*).
- Vue ajoute une **optimisation par le compilateur** : le gabarit est analysé **à la compilation**, ce qui permet d'isoler les parties **statiques** (créées une seule fois et jamais re-comparées) des parties **dynamiques** (marquées par des *patch flags* indiquant ce qui peut changer : texte, classe, props…). Le moteur d'exécution ne traite alors que le strict nécessaire. C'est une approche **hybride** : gabarits compilés + DOM virtuel optimisé.

#### Le système de réactivité

Vue 3 utilise les **`Proxy`** d'ES2015 pour intercepter la lecture (`get`) et l'écriture (`set`) des propriétés d'un objet.

- **Lecture** d'une propriété à l'intérieur d'un *effet* (rendu, `computed`, `watch`) : Vue **enregistre la dépendance** (*track*).
- **Écriture** : Vue **notifie** les effets dépendants (*trigger*), qui sont replanifiés.

Les mises à jour du DOM sont **groupées** (*batched*) et exécutées de façon asynchrone. Le chapitre 4 détaille ce mécanisme.

#### Composition API et Options API

| | **Options API** | **Composition API** |
| --- | --- | --- |
| Organisation | Par **type d'option** (`data`, `methods`, `computed`…) | Par **préoccupation logique** |
| Réutilisation | Mixins (limités) | **Composables** (fonctions) |
| TypeScript | Correct, inférence parfois lourde | **Excellent** |
| Syntaxe recommandée | Héritage de Vue 2, toujours supportée | **`<script setup>`** |

Ce cours privilégie la **Composition API avec `<script setup lang="ts">`**, voie recommandée pour les nouveaux projets. L'Options API est traitée au chapitre 20.

### 1.4 Les applications monopages (SPA)

Une **SPA** ne charge **qu'une seule page HTML**. Lors d'un clic sur un lien, le routeur intercepte la navigation, modifie l'URL grâce à l'**API History** du navigateur (`pushState`) et remplace le contenu affiché, **sans recharger la page**. Les données sont obtenues par des appels HTTP en arrière-plan (généralement du JSON).

| | **Application multipage (MPA)** | **Application monopage (SPA)** |
| --- | --- | --- |
| Navigation | Le serveur renvoie une page HTML complète à chaque clic | Le navigateur remplace des portions de la page |
| Fluidité | Rechargement visible | Transitions fluides, sensation d'application native |
| Premier affichage | Rapide (HTML prêt) | Plus lent si tout est rendu côté client |
| Référencement (SEO) | Naturel | Demande du **SSR** ou du **pré-rendu** |
| Logique | Principalement serveur | Répartie entre client et serveur |

**Limites et remèdes.** Le premier chargement d'une SPA pure peut être lent et mal indexé par certains robots. Vue répond par le **rendu côté serveur (SSR)**, la **génération statique (SSG)** et l'**hydratation** (chapitre 24), ainsi que par le **chargement paresseux** de routes et de composants (chapitres 10, 17 et 23).

### 1.5 Vue 2 et Vue 3 : histoire et confusion à éviter

- **2014** : première version de Vue, par Evan You.
- **2016** : **Vue 2**, fondée sur l'Options API et sur `Object.defineProperty` pour la réactivité.
- **2020** : **Vue 3**, réécriture en TypeScript avec réactivité par `Proxy`, Composition API, fragments, `Teleport`, `Suspense`.
- **2021** : la syntaxe `<script setup>` devient stable (3.2).
- **2023** : **Vue 2 atteint sa fin de vie le 31 décembre 2023** ; plus aucun correctif, même de sécurité, n'est publié (sauf offres commerciales de support étendu tierces).
- **2024** : Vue 3.5 (déstructuration réactive des props, `useTemplateRef`, `useId`, hydratation paresseuse).
- **2026** : Vue 3.6 en candidate à la sortie (nouveau noyau de réactivité, mode Vapor).

| Aspect | **Vue 2** | **Vue 3** |
| --- | --- | --- |
| Réactivité | `Object.defineProperty` | **`Proxy`** |
| API principale | Options API | **Composition API** (+ Options API) |
| TypeScript | Support limité | **Écrit en TypeScript**, support natif |
| Racines multiples (fragments) | Non | **Oui** |
| `Teleport`, `Suspense` | Non | **Oui** |
| `v-model` | Un seul par composant | **Plusieurs** `v-model` |
| Ajout de propriété réactive | `Vue.set` / `this.$set` nécessaire | **Inutile** |
| Gestion d'état officielle | Vuex | **Pinia** |
| Outil de build | Vue CLI (webpack) | **Vite** |
| Statut | **Fin de vie (31 décembre 2023)** | Version actuelle |

> **Attention.** Ne mélangez jamais les deux versions. Beaucoup de tutoriels anciens décrivent Vue 2. **Comment dater un exemple de code ?** `new Vue({ … })`, `Vue.use`, `Vue.set`, `this.$set`, `Vuex` → Vue 2 ; `createApp`, `defineComponent`, `export default { data() {…} }` → Vue 3 en Options API ; `<script setup>`, `ref()`, `defineProps` → Vue 3 moderne.

### 1.6 Pourquoi choisir Vue ? Forces et limites

**Forces**

- **Courbe d'apprentissage douce** : on peut être productif avec du HTML, du CSS et un peu de JavaScript. Le gabarit ressemble à du HTML ordinaire.
- **Adoption progressive** : du simple script dans une page jusqu'à une application en rendu serveur.
- **Réactivité automatique** : pas de liste de dépendances à écrire, pas d'appel manuel de mise à jour.
- **Composants monofichiers** : gabarit, logique et style colocalisés, avec isolation des styles native.
- **Écosystème officiel cohérent** : routeur, store, outils de build, tests, méta-framework.
- **Typage** : Vue 3 est écrit en TypeScript ; le support TypeScript est de premier ordre dans les composants et dans les gabarits.
- **Performance** : compilateur optimisant, DOM virtuel allégé, chargement paresseux, SSR et hydratation paresseuse.
- **Excellente documentation**, disponible en plusieurs langues.

**Limites**

- **Moins de conventions imposées** qu'Angular : deux projets Vue peuvent être organisés très différemment. Il faut définir des règles d'équipe (chapitre 26).
- **Plusieurs styles coexistent** (Options API, Composition API, `<script setup>`, JSX), ce qui peut dérouter dans une équipe non alignée.
- **Écosystème plus petit** que celui de React pour certaines bibliothèques spécialisées.
- Une partie du contenu en ligne est **obsolète** (Vue 2, Vuex, Vue CLI).

| | **Vue** | **React** | **Angular** |
| --- | --- | --- | --- |
| Nature | Framework progressif | Bibliothèque d'interface | Framework complet |
| Langage | JS / TS (gabarits ou JSX) | JS / TS (JSX) | TypeScript |
| Réactivité | `ref` / `reactive` (proxies) | État + hooks, re-rendu explicite | Signaux + RxJS |
| Routage, état | Officiels, séparés (**Router**, **Pinia**) | Bibliothèques tierces | **Inclus** |
| Courbe d'apprentissage | Douce | Moyenne | Plus raide |
| Idéal pour | Prise en main rapide, projets de toute taille | Flexibilité maximale | Grandes applications d'entreprise |

**Quand choisir Vue ?** Équipe mixte ou débutante, besoin de livrer vite, adoption progressive dans un site existant, applications de taille petite à grande avec des conventions d'équipe claires. **Quand hésiter ?** Très grande organisation qui exige des conventions strictes imposées par l'outil (Angular peut convenir mieux), ou besoin d'un écosystème de bibliothèques très spécialisé (React).

### 1.7 Versions, publications et support *(à jour)*

Vue suit le **versionnement sémantique** : les versions mineures ajoutent des fonctionnalités sans casser l'existant, les correctifs sont publiés fréquemment.

| Version | Date | Points marquants |
| --- | --- | --- |
| **3.0** | sept. 2020 | Composition API, `Proxy`, fragments, `Teleport`, `Suspense` |
| **3.2** | août 2021 | `<script setup>` stable, `v-memo`, `defineCustomElement`, `effectScope` |
| **3.3** | mai 2023 | Génériques dans `<script setup>`, `defineSlots`, `defineOptions`, `toValue`, types importés dans `defineProps` |
| **3.4** | déc. 2023 | Nouveau analyseur de gabarits plus rapide, `defineModel` stable, raccourci `:src` pour `:src="src"`, `computed` plus stable |
| **3.5** | sept. 2024 | Déstructuration réactive des props, `useTemplateRef`, `useId`, `onWatcherCleanup`, hydratation paresseuse, `defer` sur `Teleport` |
| **3.6** | en candidate à la sortie | Réécriture du noyau de réactivité (*alien-signals*), **mode Vapor** optionnel |

- **Support** : la branche stable la plus récente reçoit les correctifs ; les préversions (*alpha*, *beta*, *rc*) sont **instables** et **déconseillées en production**.
- **Mises à jour** : le passage d'une version mineure à l'autre est en général sans heurts. Consultez toujours les notes de version sur GitHub (`vuejs/core`) et le blog officiel.
- **Prochaines évolutions** : les propositions de changement passent par les **RFC** publiques (`github.com/vuejs/rfcs`).

### 1.8 Prérequis et environnement de travail

**Connaissances requises**

- **HTML** sémantique et **CSS** (sélecteurs, modèle de boîte, flexbox, grid).
- **JavaScript moderne (ES2015+)** : `let` / `const`, fonctions fléchées, déstructuration, opérateur de décomposition, modules `import` / `export`, classes, **promesses** et `async` / `await`, méthodes de tableaux (`map`, `filter`, `reduce`), chaînage optionnel `?.` et coalescence nulle `??`.
- Notions de **TypeScript** : types de base, `interface`, unions, génériques.

**Outils**

- **Node.js** (version LTS récente) et un gestionnaire de paquets : `npm`, `pnpm` ou `yarn`. **Git**.
- **VS Code** avec l'extension **Vue - Official** (anciennement *Volar*) : coloration, vérification de types et autocomplétion dans les `.vue`, y compris dans les gabarits.
- **Vue DevTools** : extension de navigateur (ou plugin Vite) pour inspecter composants, état, routeur, store et performances.
- Un navigateur moderne.

### 1.9 Création d'un projet avec `create-vue`

L'outil officiel de génération de projet est **`create-vue`**, fondé sur **Vite**.

```bash
npm create vue@latest
```

L'assistant propose des options à activer :

| Option | Rôle |
| --- | --- |
| TypeScript | Ajoute `tsconfig`, `vue-tsc` et les types |
| JSX Support | Plugin `@vitejs/plugin-vue-jsx` (chapitre 21) |
| Vue Router | Routage de l'application monopage |
| Pinia | Gestion d'état globale |
| Vitest | Tests unitaires et de composants |
| End-to-End Testing | Playwright ou Cypress |
| ESLint / Prettier | Qualité et formatage du code |
| Vue DevTools | Outils de débogage |

```bash
cd mon-projet
npm install
npm run dev        # serveur de développement (Vite, remplacement à chaud)
npm run build      # build de production (vérification de types + vite build)
npm run preview    # prévisualiser le build de production
```

#### Structure d'un projet généré

```text
mon-projet/
├── index.html            # point d'entrée HTML (Vite)
├── package.json
├── vite.config.ts        # configuration de Vite
├── tsconfig.json         # références vers les autres tsconfig
├── tsconfig.app.json     # TypeScript pour le code de l'application
├── tsconfig.node.json    # TypeScript pour les fichiers de configuration (Node)
├── env.d.ts              # déclarations de types globales
├── public/               # fichiers statiques servis tels quels
└── src/
    ├── main.ts           # point d'entrée de l'application
    ├── App.vue           # composant racine
    ├── assets/           # images, CSS (traités par Vite)
    ├── components/       # composants réutilisables
    ├── views/            # pages (avec Vue Router)
    ├── router/index.ts   # configuration du routeur
    ├── stores/           # stores Pinia
    └── composables/      # (convention) logique réutilisable
```

#### Le point d'entrée

```ts
// src/main.ts
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

const app = createApp(App)    // 1. crée l'instance d'application
app.use(createPinia())        // 2. installe des plugins
app.use(router)
app.mount('#app')             // 3. monte dans <div id="app"></div>
```

- `createApp(composantRacine, propsRacine?)` crée une **instance d'application**. Chaque application possède sa propre configuration (composants globaux, plugins, `provide`).
- `app.mount(sélecteur)` rend l'application dans l'élément ciblé et **retourne l'instance du composant racine**. Il doit être appelé **en dernier** (après `use`, `component`, `provide`…).
- **Plusieurs applications indépendantes** peuvent coexister sur la même page, chacune montée sur son propre élément.

#### Utilisation sans étape de build (CDN)

```html
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<div id="app">{{ message }}</div>
<script>
  const { createApp, ref } = Vue
  createApp({
    setup() {
      const message = ref('Bonjour Vue !')
      return { message }
    }
  }).mount('#app')
</script>
```

> **Limites de ce mode.** Pas de composants monofichiers, pas de TypeScript natif, et le gabarit est analysé **dans le navigateur** (compilateur embarqué, plus lourd). Réservé au prototypage et à l'amélioration progressive d'une page. Pour un vrai projet : `create-vue` + Vite.

### 1.10 Configuration de TypeScript

**Pourquoi TypeScript avec Vue ?** Détection des erreurs **à la compilation** (props, événements, store, routes), **autocomplétion** et refactorisation sûre, documentation vivante par les types.

| Outil | Rôle |
| --- | --- |
| **Vue - Official** (ex-Volar) | Support de l'éditeur : vérification de types dans les `.vue`, autocomplétion dans les gabarits |
| **`vue-tsc`** | Équivalent de `tsc` pour les `.vue` : `vue-tsc --noEmit` |
| **Vite** | Transpile le TypeScript (via esbuild) **sans vérifier les types** |

> **Attention.** **Vite ne vérifie pas les types** : il se contente de supprimer les annotations. Le contrôle de types est assuré par l'éditeur et par **`vue-tsc`**, à exécuter **en intégration continue et avant chaque build**.

#### `tsconfig` recommandé

```json
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "jsx": "preserve",
    "verbatimModuleSyntax": true,
    "isolatedModules": true,
    "skipLibCheck": true,
    "lib": ["ESNext", "DOM", "DOM.Iterable"],
    "types": ["vite/client"],
    "paths": { "@/*": ["./src/*"] }
  },
  "include": ["src/**/*", "src/**/*.vue", "env.d.ts"]
}
```

| Option | Importance |
| --- | --- |
| `strict: true` | Active toutes les vérifications strictes (fortement recommandé) |
| `moduleResolution: "bundler"` | Résolution adaptée à Vite et aux bundlers |
| `verbatimModuleSyntax` / `isolatedModules` | Imposent `import type` pour les types, indispensable car chaque fichier est transpilé isolément |
| `jsx: "preserve"` | Pour le TSX avec le plugin JSX de Vue |
| `paths` | Alias `@/` (à **dupliquer** dans `vite.config.ts` via `resolve.alias`) |

#### Alias dans Vite

```ts
// vite.config.ts
import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: { '@': fileURLToPath(new URL('./src', import.meta.url)) },
  },
})
```

#### Importer des types

```ts
import type { Ref } from 'vue'   // import de type uniquement : effacé à la compilation
```

Avec `verbatimModuleSyntax`, un import qui ne sert qu'aux types **doit** utiliser `import type` (ou la forme `import { type Ref }`), sinon l'import resterait dans le code JavaScript produit.

### 1.11 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| SPA | Application qui ne charge qu'une page HTML et met à jour la vue dynamiquement |
| SFC | *Single-File Component* : fichier `.vue` regroupant gabarit, script et style |
| Réactivité | Suivi automatique des dépendances et mise à jour des effets |
| DOM virtuel | Arbre d'objets légers comparé à l'arbre précédent pour minimiser les mutations du DOM |
| VNode | Nœud du DOM virtuel |
| Proxy | Objet ES2015 qui intercepte la lecture et l'écriture d'un autre objet |
| Composable | Fonction `useXxx` qui encapsule une logique à état |
| Vite | Outil de développement et de build (serveur ESM natif, remplacement à chaud) |
| `vue-tsc` | Vérificateur de types qui comprend les fichiers `.vue` |
| SSR / SSG | Rendu côté serveur / génération statique au build |
| Hydratation | Rattachement de l'application Vue au HTML produit par le serveur |
| Vapor | Mode de compilation optionnel de Vue 3.6, sans DOM virtuel |

### 1.12 Pièges fréquents

- Oublier `lang="ts"` sur `<script setup>` : le composant n'est alors plus typé.
- Croire que `npm run dev` détecte les erreurs de types : il faut lancer `vue-tsc`.
- Suivre un tutoriel Vue 2 (Vuex, `new Vue()`, Vue CLI) pour un projet Vue 3.
- Appeler `app.mount()` **avant** `app.use()` : les plugins ne sont alors pas disponibles au premier rendu.
- Utiliser une version en candidate à la sortie (Vue 3.6) dans un projet de production.
- Oublier de dupliquer l'alias `@/` dans `vite.config.ts` **et** dans `tsconfig`.

### Synthèse du chapitre 1

Vue est un **framework progressif, déclaratif et réactif**, fondé sur des **composants**. Vue 3 utilise des **`Proxy`**, un **compilateur optimisant** et un **DOM virtuel** allégé ; Vue 2 est en fin de vie. Le standard de création de projet est **`create-vue` + Vite**. **Vue - Official** et **`vue-tsc`** assurent le typage : **Vite ne vérifie pas les types**. La Composition API avec `<script setup lang="ts">` est la voie recommandée.

---

## 2. Structure d'un composant (SFC)

**Objectifs d'apprentissage.** Maîtriser l'anatomie d'un **composant monofichier** (`.vue`) ; distinguer `<script setup>` et `<script>` classique ; utiliser les **macros du compilateur** ; comprendre le bloc `<template>` ; maîtriser les styles : `scoped`, CSS Modules, `v-bind()` en CSS, sélecteurs spéciaux (`:deep`, `:slotted`, `:global`) ; connaître les blocs personnalisés et les imports de fichiers externes.

### 2.1 Définition et rôle

Un **composant monofichier** (*Single-File Component*, **SFC**) est un fichier `.vue` qui regroupe, dans un seul fichier, jusqu'à trois types de blocs de premier niveau : `<template>`, `<script>` et `<style>`. Ce n'est **pas** du JavaScript valide : le fichier est **compilé** par `@vitejs/plugin-vue` (qui s'appuie sur `@vue/compiler-sfc`) en un module JavaScript ordinaire.

```vue
<!-- src/components/Message.vue -->
<script setup lang="ts">
import { ref } from 'vue'

const message = ref('Bonjour')
</script>

<template>
  <p class="msg">{{ message }}</p>
</template>

<style scoped lang="scss">
.msg { color: teal; }
</style>
```

**Avantages du format SFC**

- **Colocalisation** : le gabarit, la logique et le style d'un même composant sont ensemble, ce qui facilite la lecture et la suppression.
- **Isolation du CSS** native (`scoped`, `module`).
- **Précompilation** des gabarits : meilleures performances et erreurs détectées tôt.
- **Remplacement à chaud (HMR)** précis, composant par composant, sans perdre l'état.
- Support de **préprocesseurs** : `lang="ts"`, `lang="scss"`, `lang="pug"`, etc.

**Séparation des préoccupations ?** Le principe n'est pas de séparer les **technologies** (HTML / JS / CSS) mais les **préoccupations** : le composant est l'unité de découpage. On peut malgré tout externaliser un bloc : `<script src="./logique.ts">`, `<style src="./style.css">`, `<template src="./vue.html">`.

### 2.2 Le bloc `<script setup>`

`<script setup>` est un **sucre syntaxique de compilation** de la Composition API dans un SFC. Deux règles le résument :

1. Le code de premier niveau est exécuté **à chaque création d'instance** du composant (c'est le corps de `setup()`).
2. **Toutes** les variables, fonctions et imports de premier niveau sont **automatiquement exposés au gabarit**.

```vue
<!-- src/components/Panier.vue -->
<script setup lang="ts">
import { ref } from 'vue'
import LigneProduit from './LigneProduit.vue'   // utilisable directement dans le gabarit

const count = ref(0)                              // exposé au gabarit
function incrementer() { count.value++ }          // exposée au gabarit
</script>

<template>
  <LigneProduit />
  <button @click="incrementer">{{ count }}</button>
</template>
```

**Équivalent sans `<script setup>`** (pour comprendre ce que le compilateur fait à votre place) :

```ts
import { defineComponent, ref } from 'vue'
import LigneProduit from './LigneProduit.vue'

export default defineComponent({
  components: { LigneProduit },                 // enregistrement manuel obligatoire
  setup() {
    const count = ref(0)
    function incrementer() { count.value++ }
    return { count, incrementer }               // retour manuel obligatoire
  },
})
```

**Avantages de `<script setup>`**

- **Moins de code** : pas de `return`, pas d'enregistrement de composants, pas de `export default`.
- **Meilleur typage** : `defineProps`, `defineEmits`, `defineModel` se typent par de simples types TypeScript.
- **Meilleures performances** : le gabarit est compilé dans la **même portée** que le script (accès direct aux variables, sans passer par un proxy de rendu).
- **Meilleure inférence** dans l'éditeur.

#### Utilisation de composants, directives et variables dans le gabarit

- Un composant **importé** est utilisable dans le gabarit sous son nom (PascalCase recommandé) : `<LigneProduit />`.
- Une variable nommée **`vNomDirective`** est utilisable comme directive `v-nom-directive` (chapitre 14).
- Les composants dynamiques s'écrivent `<component :is="monComposant" />`.
- Un composant récursif peut s'appeler **par le nom de son fichier** sans import (chapitre 10).
- Les composants à espace de noms sont possibles : `<Formulaire.Champ />` si `Formulaire` est un objet exportant des composants.

#### `await` de premier niveau

```vue
<script setup lang="ts">
const donnees = await fetch('/api/articles').then((r) => r.json())
</script>
```

Le composant devient **asynchrone** : il doit être utilisé dans un `<Suspense>` (chapitre 16). Après un `await`, Vue **restaure automatiquement** le contexte de l'instance, ce qui permet d'appeler encore des hooks et `provide` / `inject` dans `<script setup>`.

### 2.3 Le bloc `<script>` classique

Un SFC peut contenir **à la fois** un `<script>` classique et un `<script setup>`. Le bloc classique est exécuté **une seule fois**, à l'import du module (et non à chaque instance). Il sert à :

- **exporter** des valeurs ou des types nommés (`export`) ;
- déclarer des **options** qui n'existaient pas dans `<script setup>` avant `defineOptions` ;
- exécuter des **effets de bord** une seule fois.

```vue
<script lang="ts">
export interface Item { id: number; label: string }   // exportable depuis le module
let instancesCreees = 0                               // partagé entre toutes les instances
</script>

<script setup lang="ts">
instancesCreees++                                     // exécuté par chaque instance
</script>
```

> Les deux blocs doivent utiliser le **même attribut `lang`**.

### 2.4 Les macros du compilateur

Les **macros** sont des fonctions **résolues à la compilation** : elles ne sont **pas importées**, ne sont valides que dans `<script setup>` et sont transformées par le compilateur en code d'options.

| Macro | Rôle |
| --- | --- |
| `defineProps` | Déclare les **props** du composant |
| `defineEmits` | Déclare les **événements émis** |
| `defineModel` | Déclare un **`v-model`** (prop + événement) |
| `defineExpose` | **Expose** des membres à un parent via une référence de gabarit |
| `defineOptions` | Définit des **options de composant** (`name`, `inheritAttrs`…) |
| `defineSlots` | **Type** les slots (aide de l'éditeur) |
| `withDefaults` | Valeurs par défaut pour un `defineProps` fondé sur les types |

Elles sont détaillées au chapitre 10 (sauf `defineModel`, chapitre 8). Une macro doit apparaître au **niveau supérieur** de `<script setup>` ; elle peut référencer des constantes importées mais **pas** des variables locales du script (car elle est « remontée » hors de `setup()`).

### 2.5 Le bloc `<template>`

- Contient le **HTML enrichi** de la syntaxe Vue (interpolations, directives).
- **Un seul** `<template>` de premier niveau par SFC.
- Depuis Vue 3, un gabarit peut avoir **plusieurs racines** (*fragments*) ; mais le **transfert d'attributs** (*fallthrough*, chapitre 10) exige alors un traitement explicite.
- Il est **compilé en fonction de rendu** : aucun gabarit n'est analysé dans le navigateur avec un projet à étape de build.
- L'attribut `lang="pug"` permet d'utiliser un autre langage de gabarit (nécessite le préprocesseur).

### 2.6 Le bloc `<style>`

#### `scoped` : styles limités au composant

L'attribut `scoped` ajoute un **attribut de données unique** (`data-v-xxxx`) aux éléments du composant et aux sélecteurs, de sorte que les règles ne s'appliquent **qu'à ce composant**.

```vue
<style scoped>
.titre { color: red; }
/* compilé : .titre[data-v-7ba5bd90] { color: red; } */
</style>
```

- Pour un composant **enfant**, seul son **élément racine** est affecté par le style `scoped` du parent (pour permettre au parent de le positionner). Les autres éléments internes de l'enfant ne sont pas atteints.
- **Performance** : en mode `scoped`, préférez des sélecteurs de **classe** (`.a`) plutôt que des sélecteurs d'élément (`p`), plus coûteux avec l'attribut ajouté.
- Trois sélecteurs spéciaux :

```vue
<style scoped>
:deep(.classe-enfant) { color: blue; }    /* atteint un descendant, y compris dans les enfants */
:slotted(div) { color: green; }           /* cible le contenu injecté dans un slot par le parent */
:global(.globale) { margin: 0; }          /* règle globale écrite dans un bloc scoped */
</style>
```

#### CSS Modules (`<style module>`)

```vue
<script setup lang="ts">
import { useCssModule } from 'vue'
const classes = useCssModule()              // ou useCssModule('nom') pour un module nommé
</script>

<template>
  <p :class="$style.rouge">Rouge</p>
  <p :class="classes.rouge">Rouge aussi</p>
</template>

<style module>
.rouge { color: red; }
</style>
```

- Les noms de classes sont **hachés** : aucune collision possible.
- Module **nommé** : `<style module="monModule">` expose `$monModule.classe`.
- Les classes sont **injectées comme propriété calculée** (`$style`) ; elles peuvent donc se combiner aux liaisons `:class` du chapitre 5.

#### `v-bind()` en CSS

`v-bind()` lie une **variable réactive** à une valeur CSS. Vue la transforme en variable CSS appliquée en ligne sur l'élément racine du composant.

```vue
<script setup lang="ts">
import { ref } from 'vue'

const couleur = ref('crimson')
const theme = { taille: '2rem' }
</script>

<template><p class="txt">Texte dynamique</p></template>

<style scoped>
.txt {
  color: v-bind(couleur);
  font-size: v-bind('theme.taille');       /* une expression JavaScript s'écrit entre guillemets */
}
</style>
```

#### Préprocesseurs et plusieurs blocs

- `<style lang="scss">`, `lang="less"`, `lang="stylus"` : installez le préprocesseur correspondant (`npm i -D sass`).
- Un SFC peut contenir **plusieurs blocs `<style>`** (par exemple un bloc `scoped` et un bloc global).

### 2.7 Blocs personnalisés et ordre des blocs

Les **blocs personnalisés** (`<i18n>`, `<docs>`…) nécessitent un **plugin de build** pour être traités ; sans plugin, ils sont **ignorés**. Ils servent à colocaliser des métadonnées (traductions, documentation, configuration de route).

**Ordre des blocs** : le style officiel recommande de garder un ordre **cohérent** dans tout le projet ; la convention actuelle est `<script setup>` → `<template>` → `<style>`.

### 2.8 Pièges fréquents

- Mélanger `<script>` et `<script setup>` avec des attributs `lang` **différents**.
- Compter sur `scoped` pour styler l'**intérieur** d'un composant enfant sans `:deep()`.
- Utiliser les macros (`defineProps`…) **en dehors** de `<script setup>`, dans une fonction ou après un `await`.
- **Importer** les macros : elles sont globales dans `<script setup>` et ne s'importent pas.
- Oublier que les variables du **`<script>` classique** sont partagées entre toutes les instances.
- Abuser de `:deep()` : cela rompt l'encapsulation ; préférez les variables CSS ou les slots.

### Synthèse du chapitre 2

Un **SFC** regroupe `<script>`, `<template>` et `<style>` et est **compilé en module JavaScript**. **`<script setup>`** est la syntaxe recommandée : tout ce qui est de premier niveau est **exposé au gabarit**. Les **macros** (`defineProps`, `defineEmits`, `defineModel`, `defineExpose`, `defineOptions`, `defineSlots`, `withDefaults`) sont des instructions du compilateur. **`scoped`**, **`module`** et **`v-bind()`** en CSS offrent l'isolation et le dynamisme des styles.

---

## 3. Syntaxe de template

**Objectifs d'apprentissage.** Maîtriser l'**interpolation** et les **expressions** autorisées ; connaître **toutes** les directives intégrées et leur syntaxe (arguments, modificateurs, arguments dynamiques) ; utiliser `v-bind` sous toutes ses formes ; mesurer les risques de `v-html` ; utiliser `v-once`, `v-pre`, `v-memo`, `v-cloak` ; comprendre l'accès aux globales, la gestion des espaces blancs et l'élément `<template>`.

### 3.1 Les gabarits Vue

Les gabarits Vue sont du **HTML syntaxiquement valide** (donc analysable par les navigateurs et les outils HTML), étendu par :

- l'**interpolation** de texte `{{ }}` ;
- les **directives** (attributs préfixés `v-`) ;
- deux **raccourcis** très utilisés : `:` pour `v-bind` et `@` pour `v-on` (et `#` pour `v-slot`).

Sous le capot, Vue **compile** le gabarit en fonctions de rendu optimisées qui produisent des nœuds virtuels. Le compilateur peut ainsi repérer les parties statiques et dynamiques (chapitre 23).

### 3.2 Interpolation de texte

La syntaxe « **moustache** » `{{ }}` évalue une **expression JavaScript** et affiche le résultat sous forme de **texte**.

```vue
<script setup lang="ts">
import { ref } from 'vue'

const message = ref('Bonjour')
const ok = ref(true)
const html = '<strong>gras</strong>'
</script>

<template>
  <p>{{ message }}</p>
  <p>{{ message.toUpperCase() }}</p>
  <p>{{ 1 + 1 }}</p>
  <p>{{ ok ? 'Oui' : 'Non' }}</p>
  <p>{{ html }}</p>             <!-- affiche la chaîne brute : le HTML est échappé -->
  <p v-html="html"></p>         <!-- interprète comme HTML : à utiliser avec précaution -->
</template>
```

- Le contenu est **échappé** : c'est une protection native contre les attaques XSS.
- L'interpolation se met à jour **automatiquement** quand ses dépendances changent.
- Les `ref` de premier niveau sont **déballés** dans le gabarit : on écrit `{{ message }}` et non `{{ message.value }}` (chapitre 4).

#### Qu'est-ce qu'une « expression » ?

Une expression est tout ce qui peut apparaître **après un `return`** : une valeur, une opération, un appel de fonction, un ternaire, un accès de propriété. Une expression ne peut **pas** être une **instruction**.

| Autorisé | Interdit |
| --- | --- |
| `{{ a + b }}` | `{{ let x = 1 }}` (déclaration) |
| `{{ fn(x) }}` | `{{ if (ok) { } }}` (instruction de contrôle) |
| `{{ ok ? 'a' : 'b' }}` | `{{ for (...) }}` (boucle) |
| `{{ obj?.prop }}` | `{{ a = 5 }}` dans une interpolation |
| `@click="a = 5"` (affectation autorisée dans un gestionnaire) | |

#### Accès aux variables globales

Les expressions ont accès à une **liste restreinte** de globales : `Math`, `Date`, `parseInt`, `parseFloat`, `JSON`, `Array`, `Number`, `String`, `Object`, `isNaN`, `Intl`, etc. Les autres (`window`, `document`, `localStorage`) ne sont **pas** accessibles : exposez-les depuis le script ou via `app.config.globalProperties` (chapitre 15).

#### Appel de fonctions dans le gabarit

```vue
<span :title="versTitre(date)">{{ formaterDate(date) }}</span>
```

Les fonctions appelées dans le gabarit sont **réexécutées à chaque rendu** du composant : elles doivent être **légères** et **sans effet de bord** (ne jamais modifier l'état, faire une requête ou toucher au DOM). Pour un calcul coûteux, utilisez une **propriété calculée** (`computed`, chapitre 4).

### 3.3 Les directives

Une **directive** est un attribut spécial préfixé par `v-` dont la valeur est **une expression JavaScript unique** (exceptions : `v-for`, `v-on` et `v-slot`, qui ont une syntaxe propre).

#### Anatomie complète

```text
v-on:click.prevent="envoyer"
│    │     │        └── valeur (expression)
│    │     └── modificateur
│    └── argument
└── nom de la directive
```

- **Argument** : suit le `:` et précise la cible (nom d'attribut, d'événement…).
- **Modificateurs** : suffixes précédés d'un point, qui indiquent un comportement particulier (`.prevent`, `.lazy`…).
- **Argument dynamique** : une expression entre crochets, évaluée à l'exécution.

```vue
<a v-bind:[nomAttribut]="url"></a>
<a v-on:[nomEvenement]="faire"></a>
<!-- avec les raccourcis : -->
<a :[nomAttribut]="url"></a>
<a @[nomEvenement]="faire"></a>
```

**Contraintes des arguments dynamiques.** L'expression doit s'évaluer en une **chaîne** (ou `null`, qui désactive la liaison). Évitez les espaces et les guillemets dans les crochets (utilisez une propriété calculée) et les majuscules si le gabarit est écrit **directement dans le HTML de la page** (le navigateur met alors les noms d'attributs en minuscules).

#### Liste complète des directives intégrées

| Directive | Rôle |
| --- | --- |
| `v-text` | Définit le `textContent` de l'élément |
| `v-html` | Définit le `innerHTML` de l'élément |
| `v-show` | Bascule la propriété CSS `display` |
| `v-if` / `v-else-if` / `v-else` | Rendu conditionnel (chapitre 6) |
| `v-for` | Rendu de listes (chapitre 6) |
| `v-on` (`@`) | Écoute d'événements (chapitre 7) |
| `v-bind` (`:`) | Liaison d'attributs et de props |
| `v-model` | Liaison bidirectionnelle (chapitre 8) |
| `v-slot` (`#`) | Slots nommés et à portée (chapitre 11) |
| `v-pre` | Saute la compilation de l'élément |
| `v-once` | Rend l'élément une seule fois |
| `v-memo` | Mémoïsation conditionnelle d'un sous-arbre |
| `v-cloak` | Masque l'élément jusqu'à la fin de la compilation |

### 3.4 `v-bind` en détail

`v-bind` lie dynamiquement un **attribut HTML** ou une **prop de composant** à une expression.

```vue
<img :src="urlImage" :alt="description" />
<button :disabled="enChargement">Valider</button>
```

#### Raccourci « même nom » *(ajout, 3.4)*

Quand le nom de l'attribut est identique à celui de la variable :

```vue
<img :src :alt />          <!-- équivaut à :src="src" :alt="alt" -->
```

#### Attributs booléens

Une valeur **vraie** (*truthy*) fait **apparaître** l'attribut ; une valeur **fausse** (*falsy*) le **supprime**. Exception : la chaîne vide `""` le fait apparaître (comme `<button disabled>`).

#### Lier plusieurs attributs à la fois

```vue
<script setup lang="ts">
const attrs = { id: 'conteneur', class: 'boite' }
</script>

<template>
  <div v-bind="attrs"></div>
</template>
```

#### Modificateurs de `v-bind`

| Modificateur | Effet |
| --- | --- |
| `.prop` | Force la liaison comme **propriété DOM** (raccourci : préfixe `.`, `.valeur="x"`) |
| `.attr` | Force la liaison comme **attribut** (raccourci : préfixe `^`) |
| `.camel` | Transforme un nom en kebab-case en camelCase (gabarits dans le DOM) |

#### Casse des props

En SFC, on peut écrire `:maProp` (camelCase) ou `:ma-prop` (kebab-case). La convention est **kebab-case dans le gabarit** et **camelCase dans le script**.

### 3.5 `v-text` et `v-html`

```vue
<span v-text="msg"></span>       <!-- équivaut à <span>{{ msg }}</span> -->
<div v-html="htmlBrut"></div>    <!-- remplace l'innerHTML -->
```

> **Sécurité.** `v-html` sur un contenu **non fiable** ouvre une faille **XSS** (injection de scripts). À réserver à du contenu **maîtrisé** ou **assaini** (bibliothèque **DOMPurify**). De plus, `v-html` **ne compile pas** de gabarit Vue : les directives et composants qu'il contiendrait ne fonctionnent pas. Les styles `scoped` ne s'appliquent pas non plus au HTML injecté (utilisez `:deep()`).

### 3.6 `v-once`, `v-pre`, `v-memo` et `v-cloak`

```vue
<span v-once>Ne change jamais : {{ msg }}</span>
<span v-pre>{{ ceci n'est pas compilé }}</span>
<div v-memo="[a, b]">…</div>
<div v-cloak>{{ message }}</div>
```

- **`v-once`** : rend l'élément et ses enfants **une seule fois** ; les rendus suivants les considèrent comme statiques.
- **`v-pre`** : ignore la compilation et affiche les moustaches **telles quelles** (utile pour documenter la syntaxe de Vue).
- **`v-memo="[dépendances]"`** : le sous-arbre n'est **re-rendu que si l'une des valeurs** du tableau change. Utile dans de **très grandes listes** (chapitre 23). `v-memo="[]"` équivaut à `v-once`.
- **`v-cloak`** : reste sur l'élément jusqu'à la fin de la compilation du gabarit ; avec la règle CSS `[v-cloak] { display: none }`, il évite l'affichage des moustaches brutes. Utile **uniquement sans étape de build**.

### 3.7 Modificateurs : vue d'ensemble

Les modificateurs sont détaillés dans les chapitres concernés : **événements** (`.stop`, `.prevent`, touches, souris, chapitre 7) et **`v-model`** (`.lazy`, `.number`, `.trim`, chapitre 8). Ceux de `v-bind` (`.prop`, `.attr`, `.camel`) ont été vus plus haut.

### 3.8 Commentaires, espaces blancs et élément `<template>`

- `<!-- commentaire -->` : conservé ou supprimé selon la configuration du compilateur (supprimé en production par défaut).
- Vue **condense** les espaces blancs par défaut (`whitespace: 'condense'`) : plusieurs espaces ou retours à la ligne consécutifs entre éléments sont réduits à un seul espace, et les espaces en début et fin sont supprimés. L'option `'preserve'` les conserve tels quels.
- La balise **`<template>` sans directive** est un **élément de groupement invisible** : elle n'apparaît pas dans le DOM. Utilisée avec `v-if`, `v-for` ou `v-slot`, elle permet d'appliquer une directive à **plusieurs éléments frères** sans ajouter d'élément parasite.

### 3.9 Pièges fréquents

- Mettre des **instructions** (`if`, `let`) dans un `{{ }}` : seules les expressions sont permises.
- Appeler des fonctions **coûteuses** dans le gabarit (réexécutées à chaque rendu).
- Utiliser `v-html` avec une entrée **utilisateur** non assainie.
- Utiliser des arguments dynamiques avec espaces ou majuscules dans un gabarit écrit dans le DOM.
- Oublier que `:disabled=""` **active** l'attribut (chaîne vide = présent).
- Attendre d'un `v-html` qu'il traite des composants ou directives Vue.

### Synthèse du chapitre 3

`{{ }}` accepte **une expression** et produit du **texte échappé**. Une directive s'écrit `v-nom:argument.modificateur="expression"`. Les raccourcis sont `:` pour `v-bind`, `@` pour `v-on` et `#` pour `v-slot`. **`v-html`** expose à des failles XSS ; **`v-once`** et **`v-memo`** servent à l'optimisation ; **`v-cloak`** ne sert que sans étape de build.

---

## 4. Réactivité

**Objectifs d'apprentissage.** Comprendre en profondeur le **système de réactivité** de Vue 3 (suivi et déclenchement, mises à jour groupées) ; maîtriser `ref`, `reactive`, `computed`, `watch` et `watchEffect` ; choisir entre `ref` et `reactive` ; utiliser les utilitaires avancés (`toRef`, `toRefs`, `toValue`, `shallowRef`, `readonly`, `markRaw`, `customRef`, `effectScope`) ; utiliser les **références de gabarit** (`useTemplateRef`), `nextTick` et `useId` ; connaître les cas où la réactivité se perd.

### 4.1 Principe de la réactivité

L'**état réactif** est un état JavaScript dont les modifications déclenchent **automatiquement** des mises à jour : du DOM, de valeurs dérivées, d'effets de bord. En JavaScript pur, modifier une variable ne prévient personne ; Vue doit donc **intercepter** les lectures et écritures.

#### Mécanisme interne (simplifié)

```ts
// Idée simplifiée (pseudo-code) : la réactivité par Proxy
function reactive<T extends object>(obj: T): T {
  return new Proxy(obj, {
    get(target, key, receiver) {
      track(target, key)                 // « l'effet courant dépend de target[key] »
      return Reflect.get(target, key, receiver)
    },
    set(target, key, value, receiver) {
      const ok = Reflect.set(target, key, value, receiver)
      trigger(target, key)               // relance les effets qui dépendent de target[key]
      return ok
    },
  })
}
```

- Un **effet** est une fonction dont les dépendances réactives sont suivies : le rendu d'un composant, un `computed`, un `watch`, un `watchEffect`.
- Quand un effet s'exécute, **toute propriété réactive lue** est enregistrée comme dépendance (*track*). Quand elle change, l'effet est **replanifié** (*trigger*). Le suivi est **dynamique** : à chaque exécution, les dépendances sont recalculées.
- Les **primitives** (`number`, `string`, `boolean`) ne peuvent pas être interceptées en JavaScript. Vue les enveloppe donc dans un objet `{ value }` doté d'un accesseur : c'est le **`ref`**.

#### Mises à jour asynchrones et groupées

Plusieurs modifications successives dans le même « tick » entraînent **un seul rendu**. Si vous écrivez `count.value++` trois fois de suite, le DOM n'est mis à jour qu'une fois, avec la valeur finale. Pour attendre que le DOM soit à jour, on utilise `nextTick()` (section 4.9).

> **Vue 3.6 (candidate à la sortie).** Le noyau de réactivité est réécrit sur la base de la bibliothèque *alien-signals* : l'API reste **identique**, seules les performances et la consommation mémoire s'améliorent. Aucune modification de code n'est nécessaire.

### 4.2 `ref()`

`ref()` crée une **référence réactive** qui contient une valeur (primitive ou objet) accessible par **`.value`**.

```ts
import { ref } from 'vue'

const count = ref(0)             // Ref<number>
console.log(count.value)         // 0
count.value++                    // déclenche les mises à jour

const utilisateur = ref({ nom: 'Alice', age: 30 })   // un objet devient profondément réactif
utilisateur.value.age++                               // réactif
```

#### Déballage automatique (*unwrapping*)

- **Dans le gabarit** : un `ref` de **premier niveau** est déballé automatiquement : `{{ count }}` (sans `.value`).
- **Dans un objet `reactive`** : un `ref` placé en propriété est déballé (`etat.count`).
- **Dans un tableau ou une `Map` réactifs** : **pas** de déballage ; il faut écrire `.value`.

```vue
<script setup lang="ts">
import { ref } from 'vue'

const count = ref(0)
const obj = { id: ref(1) }       // objet ordinaire (non réactif) contenant un ref
</script>

<template>
  {{ count + 1 }}               <!-- correct : count est de premier niveau -->
  {{ obj.id }}                  <!-- affiche l'objet ref, car obj.id n'est pas de premier niveau -->
  {{ obj.id.value }}            <!-- correct -->
</template>
```

**Astuce.** En déstructurant (`const { id } = obj`), `id` redevient une variable de premier niveau et sera déballée dans le gabarit.

#### Profondeur et typage

`ref` rend un objet **profondément réactif** : les propriétés imbriquées sont aussi proxifiées.

```ts
const n = ref(0)                       // Ref<number> (inféré)
const s = ref<string | null>(null)     // Ref<string | null>
const u = ref<Utilisateur>()           // Ref<Utilisateur | undefined>
```

### 4.3 `reactive()`

`reactive()` retourne un **proxy réactif profond** d'un objet.

```ts
import { reactive } from 'vue'

interface Etat { count: number; user: { nom: string }; items: string[] }

const etat = reactive<Etat>({ count: 0, user: { nom: 'Alice' }, items: [] })
etat.count++
etat.user.nom = 'Bob'
etat.items.push('x')
```

#### Limitations de `reactive`

1. **Types limités** : objets, tableaux, `Map`, `Set`. **Pas** de primitives.
2. **Impossible de remplacer l'objet entier** : la référence réactive de l'ancien proxy est perdue.
3. **Perte de réactivité** à la déstructuration et au passage d'une propriété primitive à une fonction.

```ts
let etat = reactive({ count: 0 })
etat = reactive({ count: 1 })      // la liaison avec l'ancien proxy est perdue

const { count } = etat             // `count` est un simple nombre (non réactif)

function f(n: number) { /* … */ }
f(etat.count)                      // on passe un nombre, pas une dépendance
```

**Solutions** : `toRefs(etat)`, `toRef(etat, 'count')`, ou utiliser **`ref`**, recommandé comme API principale.

#### Identité du proxy

```ts
const brut = { a: 1 }
const proxy = reactive(brut)
proxy === brut                  // false : le proxy n'est pas l'objet d'origine
reactive(brut) === proxy        // true : même proxy pour le même objet
reactive(proxy) === proxy       // true : un proxy n'est pas ré-enveloppé
```

Conséquence : **comparez toujours des proxies avec des proxies**, et modifiez l'état via le proxy (modifier l'objet brut ne déclenche rien).

### 4.4 `ref` ou `reactive` ?

| Critère | **`ref`** | **`reactive`** |
| --- | --- | --- |
| Valeurs primitives | Oui | **Non** |
| Remplacement complet | Oui (`x.value = nouveau`) | **Non** |
| Déstructuration sûre | Oui | Non (utiliser `toRefs`) |
| Syntaxe | `.value` dans le script | Directe |
| Recommandation | **Par défaut** | Usage ciblé (objet « structuré » local) |

> **Règle.** **`ref` par défaut** ; `reactive` pour un petit objet local dont on ne remplacera jamais la référence.

### 4.5 `computed()`

`computed()` crée une **propriété calculée** : une valeur **dérivée**, **mise en cache**, recalculée **uniquement** quand ses dépendances changent.

```ts
import { ref, computed } from 'vue'

const prenom = ref('Jean')
const nom = ref('Dupont')
const complet = computed(() => `${prenom.value} ${nom.value}`)   // ComputedRef<string>
```

#### Calculée ou méthode ?

| | **`computed`** | **Méthode / fonction** |
| --- | --- | --- |
| Cache | **Oui** (selon les dépendances) | Non (exécutée à chaque rendu) |
| Effets de bord | **Interdits** | Possibles |
| Paramètres | Non | Oui |
| Usage | Valeur dérivée | Action, calcul paramétré |

Dans le gabarit, `{{ complet }}` ne recalcule pas tant que `prenom` et `nom` ne changent pas, alors qu'`{{ fonctionComplet() }}` est réexécutée à **chaque rendu**.

#### Propriété calculée modifiable

```ts
const complet = computed({
  get: () => `${prenom.value} ${nom.value}`,
  set: (valeur: string) => {
    ;[prenom.value, nom.value] = valeur.split(' ')
  },
})
complet.value = 'Marie Curie'    // appelle le mutateur
```

#### Règles d'or

1. Le **getter ne doit pas avoir d'effets de bord** : pas de modification d'état, pas de requête, pas de manipulation du DOM.
2. **Ne modifiez pas** la valeur retournée : c'est un **instantané** de l'état dérivé ; modifiez l'état source.
3. **Valeur précédente** *(3.4)* : le getter reçoit `anciennesValeur` en paramètre.
4. Depuis la **3.4**, un `computed` ne notifie ses dépendants que si **sa valeur change réellement** (comparaison `Object.is`). Retourner des **primitives** évite des re-rendus superflus.

```ts
const compte = computed<number>((precedent) => (precedent ?? 0) + 1)
```

### 4.6 `watch()`

`watch()` exécute un **effet de bord** en réaction au changement d'une ou plusieurs **sources réactives**.

#### Types de sources

```ts
import { ref, reactive, watch } from 'vue'

const x = ref(0)
const etat = reactive({ count: 0, imbrique: { a: 1 } })

watch(x, (nouveau, ancien) => { /* … */ })                         // un ref
watch(() => etat.count, (n, a) => { /* … */ })                      // un getter
watch([x, () => etat.count], ([nx, nc], [ax, ac]) => { /* … */ })   // plusieurs sources
watch(etat, (n, a) => { /* … */ })                                  // un reactive : profond implicite
```

> **Erreur classique.** `watch(etat.count, …)` est **invalide** : on passe un nombre, pas une source. Il faut un **getter** : `watch(() => etat.count, …)`.

#### Options

| Option | Effet |
| --- | --- |
| `immediate: true` | Exécute le callback **immédiatement**, à la création |
| `deep: true` / `deep: n` | Observation **profonde** (ou jusqu'à la profondeur *n*, depuis la 3.5) |
| `flush: 'pre' \| 'post' \| 'sync'` | Moment d'exécution : avant le rendu (défaut), après le rendu, ou synchrone |
| `once: true` | Un **seul** déclenchement *(3.4)* |

```ts
watch(source, callback, { immediate: true, deep: true, flush: 'post', once: false })
```

#### Observation profonde

- Un `watch` sur un **getter** qui retourne un objet ne se déclenche **que si l'objet est remplacé**, sauf avec `deep: true`.
- `deep: true` sur de grosses structures est **coûteux** : préférez observer un getter précis.
- Lors d'une **mutation profonde**, `nouveau === ancien` (même objet) : clonez si vous devez comparer.

#### Effets asynchrones et nettoyage

```ts
import { watch, onWatcherCleanup } from 'vue'          // onWatcherCleanup : 3.5+

watch(id, async (nouvelId, ancienId, onCleanup) => {
  const controleur = new AbortController()
  onCleanup(() => controleur.abort())                  // appelé avant la prochaine exécution ou à l'arrêt
  const res = await fetch(`/api/${nouvelId}`, { signal: controleur.signal })
  donnees.value = await res.json()
})
```

La fonction **`onWatcherCleanup()`** *(3.5)* permet d'enregistrer le nettoyage depuis n'importe où dans l'exécution **synchrone** du callback (avant tout `await`).

#### Arrêt et pause *(3.5)*

```ts
const { stop, pause, resume } = watch(source, callback)
stop()      // arrêt définitif
pause()     // suspend
resume()    // reprend
```

- Un observateur créé **de façon synchrone dans `setup`** est **arrêté automatiquement** au démontage du composant.
- Un observateur créé **de façon asynchrone** (après un `await`) n'est **pas** lié au composant : arrêtez-le **manuellement** (`stop()`), sous peine de fuite mémoire.

#### `flush` et accès au DOM

Par défaut, les callbacks s'exécutent **avant** la mise à jour du DOM (`'pre'`). Pour lire le DOM **déjà mis à jour**, utilisez `flush: 'post'` ou `watchPostEffect`.

### 4.7 `watchEffect()`

`watchEffect()` exécute **immédiatement** une fonction et **suit automatiquement** toutes les dépendances réactives lues **de façon synchrone**.

```ts
import { watchEffect } from 'vue'

const stop = watchEffect(async (onCleanup) => {
  const controleur = new AbortController()
  onCleanup(() => controleur.abort())
  const res = await fetch(`/api/${id.value}`, { signal: controleur.signal })  // `id` suivi : lu avant l'await
  donnees.value = await res.json()                                             // lecture après await : non suivie
})
```

| | **`watch`** | **`watchEffect`** |
| --- | --- | --- |
| Dépendances | **Explicites** (sources) | **Automatiques** |
| Exécution initiale | Non (sauf `immediate`) | **Oui** |
| Ancienne valeur | Oui | Non |
| Usage | Contrôle précis | Simplicité |

Variantes : `watchPostEffect(fn)` équivaut à `watchEffect(fn, { flush: 'post' })` ; `watchSyncEffect(fn)` à `{ flush: 'sync' }`.

> **Seules les dépendances lues avant le premier `await`** sont suivies dans un `watchEffect` asynchrone. Lisez tous les états nécessaires au début de la fonction.

### 4.8 Utilitaires de réactivité

#### Conversions et lecture

| API | Description |
| --- | --- |
| `isRef(x)` | Vrai si `x` est un `ref` |
| `unref(x)` | `isRef(x) ? x.value : x` |
| `toValue(x)` *(3.3)* | Normalise un `ref`, un getter ou une valeur en valeur |
| `toRef(objet, 'cle')` | Crée un `ref` **lié** à une propriété d'un objet réactif |
| `toRef(() => objet.cle)` *(3.3)* | `ref` en **lecture seule** depuis un getter |
| `toRefs(objet)` | Convertit **toutes** les propriétés en `ref` liés |
| `isReactive`, `isReadonly`, `isProxy` | Prédicats |

```ts
const etat = reactive({ foo: 1, bar: 2 })
const { foo, bar } = toRefs(etat)    // refs liés : la réactivité est conservée
foo.value++                          // etat.foo vaut maintenant 2
```

#### Réactivité superficielle

```ts
import { shallowRef, shallowReactive, triggerRef } from 'vue'

const s = shallowRef({ n: 1 })
s.value.n++                // non réactif
s.value = { n: 2 }         // réactif : remplacement de .value
triggerRef(s)              // force la notification après une mutation interne

const sr = shallowReactive({ a: { b: 1 } })
sr.a = { b: 2 }            // réactif
sr.a.b++                   // non réactif
```

Usage : **gros objets ou listes** traités de façon immuable, instances de classes externes, optimisation de performance (chapitre 23).

#### Lecture seule

```ts
import { readonly, shallowReadonly } from 'vue'

const original = reactive({ count: 0 })
const copie = readonly(original)
copie.count++                  // avertissement en développement, ignoré
```

Utile pour **exposer** un état sans permettre sa modification (depuis un composable, un store, un `provide`).

#### Échapper à la réactivité

```ts
import { toRaw, markRaw } from 'vue'

const brut = toRaw(proxy)                  // l'objet d'origine
const obj = markRaw({ lourd: 1 })          // ne sera jamais proxifié
```

#### `customRef`

`customRef()` crée un `ref` avec un **contrôle total** de `get` et `set` (via `track` et `trigger`).

```ts
import { customRef } from 'vue'

export function useRefAntiRebond<T>(valeur: T, delai = 200) {
  let minuteur: ReturnType<typeof setTimeout>
  return customRef<T>((track, trigger) => ({
    get() { track(); return valeur },
    set(nouvelle) {
      clearTimeout(minuteur)
      minuteur = setTimeout(() => { valeur = nouvelle; trigger() }, delai)
    },
  }))
}
```

#### `effectScope`

`effectScope()` **regroupe** des effets (`computed`, `watch`…) pour les **arrêter ensemble**.

```ts
import { effectScope, onScopeDispose, getCurrentScope, computed, watch } from 'vue'

const scope = effectScope()
scope.run(() => {
  const double = computed(() => compteur.value * 2)
  watch(double, () => console.log(double.value))
  onScopeDispose(() => console.log('nettoyage'))
})
scope.stop()   // arrête tous les effets du scope et appelle onScopeDispose
```

Usage avancé : bibliothèques, composables partagés (par exemple `createSharedComposable` de VueUse).

### 4.9 `nextTick()`

`nextTick()` attend que Vue ait **appliqué les modifications au DOM**.

```ts
import { nextTick, ref } from 'vue'

const count = ref(0)

async function incrementer() {
  count.value++
  console.log(document.getElementById('c')!.textContent)   // ancienne valeur : le DOM n'est pas encore à jour
  await nextTick()
  console.log(document.getElementById('c')!.textContent)   // nouvelle valeur
}
```

### 4.10 Références de gabarit (*template refs*)

Elles donnent un accès **direct** à un élément DOM ou à une instance de composant enfant.

```vue
<script setup lang="ts">
import { ref, onMounted, useTemplateRef } from 'vue'

// Méthode classique : le nom de la variable = valeur de l'attribut `ref`
const input = ref<HTMLInputElement | null>(null)

// Vue 3.5+ : useTemplateRef, avec un identifiant de chaîne explicite
const input2 = useTemplateRef<HTMLInputElement>('champ2')

onMounted(() => {
  input.value?.focus()          // disponible APRÈS le montage
  input2.value?.focus()
})
</script>

<template>
  <input ref="input" />
  <input ref="champ2" />
</template>
```

- Avant le montage, après le démontage, ou si l'élément est masqué par `v-if`, la valeur est **`null`** : utilisez `?.`.
- **`ref` dans un `v-for`** : la référence est un **tableau** d'éléments (l'ordre n'est pas garanti identique à celui de la source).
- **Référence fonction** : `:ref="(el) => { … }"`, appelée au montage avec l'élément et au démontage avec `null`.
- **Référence sur un composant** : donne l'instance publique. Dans `<script setup>`, ses membres ne sont **pas exposés** sauf via `defineExpose` (chapitre 10).

```vue
<template>
  <li v-for="i in items" :key="i.id" :ref="(el) => el && lis.push(el as HTMLLIElement)">{{ i.nom }}</li>
</template>
```

> **Pourquoi `useTemplateRef` ?** Il découple le nom de la variable du nom de l'attribut, fonctionne avec les composables et permet un **typage** plus fiable que la convention d'homonymie.

### 4.11 `useId()` *(ajout, 3.5)*

`useId()` génère des **identifiants uniques et stables entre le serveur et le client** (utile pour `for` / `id` et `aria-*`).

```vue
<script setup lang="ts">
import { useId } from 'vue'

const id = useId()
</script>

<template>
  <label :for="id">Nom</label>
  <input :id="id" />
</template>
```

Chaque appel produit un identifiant distinct dans l'application, ce qui évite les collisions quand un composant est instancié plusieurs fois, et les **désaccords d'hydratation** en SSR (chapitre 24).

### 4.12 Cas particuliers

- **Ajout de propriétés** à un objet réactif : fonctionne en Vue 3 (plus besoin de `Vue.set`).
- **Tableaux** : toute modification par les méthodes (`push`, `splice`…) ou par **index** est réactive.
- **`Map`, `Set`, `WeakMap`** : supportés par `reactive`.
- **Classes** : une instance de classe stockée dans un `ref` ou un `reactive` est proxifiée ; ses méthodes appelées via le proxy ont `this` égal au **proxy**. Utilisez `markRaw` pour l'éviter.
- **Pertes de réactivité fréquentes** : déstructuration d'un `reactive`, remplacement d'un `reactive`, passage de valeurs primitives, lecture après `await` dans un `watchEffect`.

### 4.13 Pièges fréquents

- Oublier `.value` dans le **script** (mais pas dans le gabarit).
- Écrire `watch(etat.count, …)` au lieu de `watch(() => etat.count, …)`.
- Modifier l'état dans un `computed`.
- Remplacer un objet `reactive` entier.
- Utiliser `deep: true` sur de grosses structures.
- Lire une référence de gabarit **avant** `onMounted`.
- Muter un tableau ou un objet dans un `shallowRef` sans `triggerRef` ni remplacement.
- Utiliser un `watch` pour **calculer** une valeur : c'est le rôle de `computed`.

### Synthèse du chapitre 4

`ref` (valeur + `.value`) et `reactive` (proxy d'objet) sont les deux primitives de la réactivité ; **`ref` par défaut**. **`computed`** est une dérivée mise en cache **sans effet de bord** ; **`watch`** réagit avec des sources explicites ; **`watchEffect`** suit automatiquement ses dépendances (lues avant tout `await`). `shallowRef`, `markRaw`, `readonly`, `customRef` et `effectScope` servent aux cas avancés. **`nextTick`** attend le DOM ; **`useTemplateRef`** donne accès au DOM ; **`useId`** produit des identifiants stables.

---

## 5. Liaisons de classes et de styles

**Objectifs d'apprentissage.** Lier dynamiquement `class` et `style` avec les syntaxes **chaîne, objet et tableau** ; comprendre la **fusion** avec les classes statiques et celles du composant parent ; gérer les préfixes automatiques et les valeurs multiples ; utiliser les variables CSS ; typer `class` et `style` en TypeScript.

### 5.1 Pourquoi une liaison spéciale ?

`class` et `style` sont des attributs **manipulés très fréquemment**. Vue les traite de façon particulière avec `v-bind:class` et `v-bind:style` (raccourcis `:class` et `:style`) : en plus des chaînes, ils acceptent des **objets** et des **tableaux**, ce qui évite de concaténer des chaînes à la main.

### 5.2 Liaison de `class`

#### Syntaxe objet

Les **clés** sont les noms de classes, les **valeurs** sont des booléens (*truthy* ou *falsy*) qui activent la classe.

```vue
<script setup lang="ts">
import { ref, computed } from 'vue'

const actif = ref(true)
const erreur = ref(false)

const classes = computed(() => ({
  actif: actif.value,
  'text-danger': erreur.value,
}))
</script>

<template>
  <div class="statique" :class="{ actif, 'text-danger': erreur }"></div>
  <div :class="classes"></div>
</template>
```

Résultat (si `actif` est vrai et `erreur` faux) : `<div class="statique actif"></div>`.

- Un attribut `class` **statique** et un `:class` **dynamique** coexistent et sont **fusionnés**.
- L'objet peut être **en ligne**, un `ref` ou un `reactive`, ou une **propriété calculée** (recommandée dès que la logique se complexifie).
- Les clés contenant un tiret doivent être **entre guillemets** : `{ 'text-danger': x }`.

#### Syntaxe tableau

```vue
<div :class="[classeA, classeB]"></div>
<div :class="[actif ? 'actif' : '', classeB]"></div>
<div :class="[{ actif: estActif }, classeB]"></div>      <!-- un objet dans un tableau -->
```

#### Sur un composant

Quand `class` est appliquée à un composant, elle est **ajoutée à l'élément racine** du composant (transfert d'attributs).

```vue
<!-- Enfant.vue -->
<template><p class="enfant">Salut</p></template>

<!-- Parent -->
<Enfant class="ajoutee" :class="{ actif: true }" />
<!-- rendu : <p class="enfant ajoutee actif">Salut</p> -->
```

Si le composant possède **plusieurs racines**, il faut lier explicitement `$attrs` (chapitre 10).

### 5.3 Liaison de `style`

#### Syntaxe objet

Les propriétés CSS s'écrivent en **camelCase** ou en **kebab-case** (entre guillemets).

```vue
<script setup lang="ts">
import { ref, reactive } from 'vue'

const couleur = ref('red')
const taille = ref(30)
const styleObjet = reactive({ color: 'blue', fontSize: '20px' })
</script>

<template>
  <div :style="{ color: couleur, fontSize: taille + 'px' }"></div>
  <div :style="{ 'font-size': taille + 'px' }"></div>
  <div :style="styleObjet"></div>
</template>
```

#### Syntaxe tableau

Elle **fusionne** plusieurs objets de style ; les derniers l'emportent.

```vue
<div :style="[styleBase, styleSurcharge]"></div>
```

#### Préfixes automatiques

Vue ajoute **automatiquement** les préfixes de navigateur (`-webkit-`, etc.) quand cela est nécessaire.

#### Valeurs multiples

Un tableau permet de fournir plusieurs valeurs de repli ; seule **la dernière valeur supportée** par le navigateur est utilisée.

```vue
<div :style="{ display: ['-webkit-box', '-ms-flexbox', 'flex'] }"></div>
```

#### Propriétés CSS personnalisées (variables CSS)

```vue
<div :style="{ '--couleur-principale': couleur }" class="carte"></div>
```

```css
.carte { border: 2px solid var(--couleur-principale); }
```

C'est la technique recommandée pour thématiser un composant sans multiplier les classes.

### 5.4 Typage TypeScript

```ts
import type { StyleValue, CSSProperties } from 'vue'

const style: CSSProperties = { color: 'red', fontSize: '12px' }
const sv: StyleValue = [style, { margin: 0 }]

// Typage de props `class` et `style` pour un composant
defineProps<{ class?: any; style?: StyleValue }>()
```

### 5.5 Pièges fréquents

- Oublier les **guillemets** autour des clés avec tiret : `{ text-danger: x }` est invalide.
- Fournir une valeur numérique **sans unité** : `fontSize: 30` n'est **pas** converti en `px`.
- Utiliser des styles en ligne pour tout : préférez des **classes** et des variables CSS.
- Écraser par inadvertance : avec plusieurs `class` sur un composant, vérifiez que la racine reçoit bien les classes.

### Synthèse du chapitre 5

`:class` et `:style` acceptent une **chaîne, un objet ou un tableau**. Les classes dynamiques sont **fusionnées** avec les classes statiques et celles du parent. Préférez une **propriété calculée** pour les classes complexes et les **variables CSS** pour le thème.

---

## 6. Rendu conditionnel et listes

**Objectifs d'apprentissage.** Maîtriser `v-if`, `v-else-if`, `v-else` et `v-show` et savoir les choisir ; maîtriser `v-for` sur les tableaux, objets, plages, itérables, `<template>` et composants ; comprendre le rôle et les règles de **`key`** ; connaître la stratégie de mise à jour des listes ; détecter les changements de tableaux ; afficher des listes filtrées et triées sans muter l'état.

### 6.1 `v-if`, `v-else-if` et `v-else`

```vue
<script setup lang="ts">
import { ref } from 'vue'

const type = ref<'A' | 'B' | 'C'>('A')
</script>

<template>
  <p v-if="type === 'A'">A</p>
  <p v-else-if="type === 'B'">B</p>
  <p v-else>Autre</p>
</template>
```

- `v-else` et `v-else-if` doivent suivre **immédiatement** un élément portant `v-if` ou `v-else-if` (sans élément intermédiaire).
- Le bloc est **réellement ajouté ou retiré du DOM** ; les composants et écouteurs internes sont **détruits puis recréés** à chaque bascule.
- `v-if` est **paresseux** : si la condition est fausse au premier rendu, **rien n'est rendu**.

#### Groupe conditionnel avec `<template>`

```vue
<template v-if="connecte">
  <h1>Bienvenue</h1>
  <p>Contenu privé</p>
</template>
```

L'élément `<template>` n'apparaît pas dans le DOM final.

#### Forcer la réinitialisation avec `key`

Vue **réutilise** les éléments existants quand c'est possible. Dans l'exemple ci-dessous, passer de `email` à `mdp` conserverait le texte saisi. Pour forcer la **recréation**, donnez des `key` distinctes.

```vue
<input v-if="mode === 'email'" key="email" placeholder="Email" />
<input v-else key="mdp" placeholder="Mot de passe" />
```

### 6.2 `v-show`

```vue
<h1 v-show="ok">Bonjour</h1>
```

- Bascule la propriété CSS **`display`** : l'élément **reste dans le DOM**.
- **Ne supporte pas** `<template>` ni `v-else`.

#### Comparaison

| | **`v-if`** | **`v-show`** |
| --- | --- | --- |
| Mécanisme | Ajout / retrait dans le DOM | `display: none` |
| Coût initial | **Paresseux** (rien si faux au départ) | Toujours rendu |
| Coût de bascule | Plus élevé | Faible |
| Usage | Condition **rarement** modifiée | Bascule **fréquente** |
| `<template>` et `v-else` | Oui | Non |

### 6.3 `v-if` et `v-for` ensemble

En Vue 3, **`v-if` a une priorité plus haute que `v-for`** : le `v-if` n'a donc **pas accès** à la variable de la boucle sur le même élément. Il est **déconseillé** de les combiner.

```vue
<!-- Erreur : `todo` n'existe pas encore pour v-if -->
<li v-for="todo in todos" v-if="!todo.fait">{{ todo.nom }}</li>

<!-- Solution 1 : un <template> porte la boucle -->
<template v-for="todo in todos" :key="todo.id">
  <li v-if="!todo.fait">{{ todo.nom }}</li>
</template>

<!-- Solution 2 (préférée) : une propriété calculée filtre -->
<li v-for="todo in aFaire" :key="todo.id">{{ todo.nom }}</li>
```

> **Attention, changement par rapport à Vue 2.** Dans Vue 2, `v-for` avait la priorité sur `v-if`. Les anciens exemples qui combinent les deux sont à réécrire.

### 6.4 `v-for` : listes

#### Tableaux

```vue
<script setup lang="ts">
import { ref } from 'vue'

interface Item { id: number; message: string }
const items = ref<Item[]>([{ id: 1, message: 'A' }, { id: 2, message: 'B' }])
</script>

<template>
  <ul>
    <li v-for="(item, index) in items" :key="item.id">
      {{ index }} - {{ item.message }}
    </li>
  </ul>
  <!-- `of` est aussi accepté à la place de `in` -->
  <div v-for="item of items" :key="item.id"></div>
</template>
```

La portée de la boucle est la même que celle des fonctions JavaScript : les variables `item` et `index` sont accessibles à l'intérieur du bloc. La **déstructuration** est possible : `v-for="{ id, message } in items"`.

#### Objets

L'ordre d'itération suit `Object.keys()`.

```vue
<li v-for="(valeur, cle, index) in objet" :key="cle">
  {{ index }}. {{ cle }} : {{ valeur }}
</li>
```

#### Plage d'entiers

```vue
<span v-for="n in 10" :key="n">{{ n }}</span>     <!-- de 1 à 10 : la plage commence à 1 -->
```

#### Sur un `<template>`

```vue
<template v-for="item in items" :key="item.id">
  <dt>{{ item.titre }}</dt>
  <dd>{{ item.description }}</dd>
</template>
```

La `key` se place alors sur le `<template>`, et non sur ses enfants.

#### Itérables

`v-for` fonctionne avec tout **itérable** : `Map`, `Set`, générateurs, chaînes de caractères.

#### Sur un composant

Les données ne sont **pas** injectées automatiquement dans le composant : il faut les passer par des **props**.

```vue
<TodoItem
  v-for="(todo, index) in todos"
  :key="todo.id"
  :todo="todo"
  :index="index"
  @supprimer="todos.splice(index, 1)"
/>
```

### 6.5 La directive `key`

#### Rôle

L'attribut spécial `key` aide l'algorithme de **comparaison** (*diffing*) à **identifier chaque nœud** pour le **réutiliser, le réordonner ou le retirer**, au lieu de tout modifier « sur place ».

#### Règles

- **Toujours** fournir une `key` dans un `v-for` (sauf si le contenu est trivial et que la réutilisation en place est voulue).
- La clé doit être **unique parmi les frères**, **stable** dans le temps et de type **primitif** (`string`, `number` ou `symbol`).
- **N'utilisez pas l'index** comme clé si la liste peut être **réordonnée, filtrée ou modifiée** (l'état local des éléments se retrouverait sur le mauvais item).
- **N'utilisez pas un objet** comme clé.

#### Stratégie de mise à jour « en place » (sans `key`)

Sans `key`, si l'ordre des données change, Vue **modifie chaque élément en place** plutôt que de déplacer les éléments du DOM. C'est efficace tant que le rendu ne dépend que des données ; mais l'**état local** des éléments (valeur d'un `<input>`, état d'un composant enfant) peut se retrouver **sur le mauvais item**.

#### `key` hors `v-for`

`key` force aussi la **recréation** d'un composant (donc la réinitialisation de son état) quand sa valeur change :

```vue
<Formulaire :key="utilisateurId" />     <!-- recréé à chaque changement d'utilisateur -->
```

### 6.6 Détection des changements d'un tableau

**Méthodes mutantes** (la modification est détectée) : `push`, `pop`, `shift`, `unshift`, `splice`, `sort`, `reverse`.

**Méthodes non mutantes** (elles **renvoient** un nouveau tableau, à réaffecter) : `filter`, `concat`, `slice`, `map`, `toSorted`, `toReversed`, `toSpliced`, `with`.

```ts
items.value = items.value.filter((i) => i.message.match(/A/))
```

> Vue optimise le remplacement d'un tableau en **réutilisant au maximum** les éléments du DOM : remplacer un tableau entier est donc efficace. L'affectation par index (`items.value[0] = x`) est aussi réactive en Vue 3.

### 6.7 Afficher des résultats filtrés ou triés

Utilisez une **propriété calculée** (ou une méthode si elle est paramétrée). Attention : `sort()` et `reverse()` **mutent** le tableau d'origine ; travaillez sur une **copie**.

```ts
const pairs = computed(() => nombres.value.filter((n) => n % 2 === 0))
const tries = computed(() => [...nombres.value].sort((a, b) => a - b))    // copie : l'état source reste intact
const tries2 = computed(() => nombres.value.toSorted((a, b) => a - b))    // ES2023, ne mute pas
```

### 6.8 Pièges fréquents

- `v-for` **sans `key`** sur des listes ayant un état local.
- `key` égale à l'**index** sur une liste modifiable.
- Combiner `v-if` et `v-for` sur le même élément.
- Appeler `.sort()` ou `.reverse()` directement dans le gabarit ou un `computed` (mutation de l'état source).
- Penser que `v-for="n in 10"` démarre à 0 (il démarre à **1**).
- Utiliser `v-show` avec `<template>` ou `v-else` : non supporté.

### Synthèse du chapitre 6

**`v-if`** ajoute ou retire réellement les éléments du DOM ; **`v-show`** ne change que `display`. **`v-for`** avec une **`key` unique et stable** donne des listes correctes et performantes. Ne combinez pas `v-if` et `v-for` sur le même élément. Filtrez et triez par des **propriétés calculées**, sur des copies.

---

## 7. Gestion des événements

**Objectifs d'apprentissage.** Écouter des événements DOM avec `v-on` / `@` ; distinguer gestionnaires en ligne et gestionnaires de méthode ; maîtriser les **modificateurs** d'événements, de touches et de souris ; typer les événements en TypeScript ; connaître les bonnes pratiques de nettoyage d'écouteurs.

### 7.1 `v-on` et `@`

La directive `v-on` (raccourci `@`) écoute les événements DOM et exécute du JavaScript.

```vue
<script setup lang="ts">
import { ref } from 'vue'

const count = ref(0)
function saluer(event: MouseEvent) {
  console.log(event.target)
}
</script>

<template>
  <button @click="count++">En ligne : {{ count }}</button>     <!-- gestionnaire en ligne -->
  <button @click="saluer">Méthode</button>                      <!-- gestionnaire de méthode -->
</template>
```

#### Deux types de gestionnaires

| Type | Détection | Exemple |
| --- | --- | --- |
| **En ligne** | Une expression JavaScript | `@click="count++"` |
| **Méthode** | Un nom ou un chemin d'accès (`a`, `a.b`, `a['b']`) | `@click="saluer"` |

Un identifiant valide ou un chemin d'accès est traité comme une **méthode** (Vue lui passe l'événement natif) ; tout le reste est un gestionnaire **en ligne**.

#### Accéder à l'événement natif

```vue
<button @click="saluer('Bonjour', $event)">OK</button>
<button @click="(e) => saluer('Salut', e)">OK</button>
```

#### Plusieurs instructions

```vue
<button @click="a(), b()">Les deux</button>
```

#### Arguments dynamiques et écouteurs multiples

```vue
<button @[evenement]="gerer">…</button>
<button v-on="{ mousedown: onDown, mouseup: onUp }"></button>
```

### 7.2 Modificateurs d'événements

Les modificateurs évitent d'écrire `event.preventDefault()` et consorts dans les méthodes, qui restent ainsi **pures** (centrées sur la logique, sans détails DOM).

| Modificateur | Effet |
| --- | --- |
| `.stop` | Appelle `event.stopPropagation()` |
| `.prevent` | Appelle `event.preventDefault()` |
| `.self` | Ne déclenche que si `event.target` est l'élément lui-même |
| `.capture` | Écoute en phase de **capture** |
| `.once` | Écouteur déclenché **une seule fois** |
| `.passive` | Écouteur **passif** : ne bloque pas le défilement (incompatible avec `.prevent`) |

```vue
<form @submit.prevent="envoyer"></form>
<a @click.stop.prevent="faire"></a>             <!-- chaînage possible -->
<form @submit.prevent></form>                   <!-- sans gestionnaire -->
<div @scroll.passive="surDefilement"></div>
```

> **L'ordre compte.** `@click.prevent.self` empêche le comportement par défaut de **tous** les clics ; `@click.self.prevent` seulement de ceux qui ont lieu sur l'élément lui-même.

### 7.3 Modificateurs de touches

```vue
<input @keyup.enter="soumettre" />
<input @keyup.page-down="suivant" />
```

Alias fournis : `.enter`, `.tab`, `.delete` (couvre Suppr et Retour arrière), `.esc`, `.space`, `.up`, `.down`, `.left`, `.right`. Toute valeur de `KeyboardEvent.key` écrite en **kebab-case** peut servir de modificateur (`.page-down`, `.caps-lock`).

#### Touches système

`.ctrl`, `.alt`, `.shift`, `.meta` (Cmd sur Mac, Windows sur PC).

```vue
<input @keyup.alt.enter="effacer" />
<div @click.ctrl="faireQuelqueChose">Ctrl + clic</div>
```

#### `.exact`

`.exact` impose la combinaison **exacte** de touches système.

```vue
<button @click.ctrl.exact="seulementCtrl">Uniquement Ctrl</button>
<button @click.exact="aucuneTouche">Aucune touche système</button>
```

### 7.4 Modificateurs de souris

`.left`, `.right` et `.middle` restreignent le gestionnaire à un bouton précis de la souris.

### 7.5 Événements de composants (rappel)

```vue
<Enfant @changer="(valeur) => console.log(valeur)" />
```

Les événements **personnalisés** s'émettent avec `emit` (chapitre 10). Les modificateurs `.once` fonctionnent aussi sur eux ; `.native` n'existe plus en Vue 3 (les écouteurs natifs non déclarés tombent dans `$attrs`).

### 7.6 Typage TypeScript des événements

```ts
function onInput(event: Event) {
  const cible = event.target as HTMLInputElement
  console.log(cible.value)
}
function onKey(event: KeyboardEvent) { if (event.key === 'Enter') { /* … */ } }
function onClick(event: MouseEvent) { /* … */ }
function onSubmit(event: SubmitEvent) { /* … */ }
```

> Dans un gestionnaire **en ligne**, `$event` est typé automatiquement. Dans une **fonction externe**, il faut **annoter** le paramètre.

### 7.7 Bonnes pratiques

- Gardez la logique **hors du gabarit** (méthodes nommées).
- Préférez les **modificateurs** à `preventDefault()` manuel.
- **Nettoyez** les écouteurs ajoutés à la main (`addEventListener`) dans `onUnmounted`.
- Pour des événements sur `window` ou `document`, créez un **composable** (`useEventListener`) qui s'abonne et se désabonne automatiquement.

```ts
// src/composables/useEventListener.ts
import { onMounted, onUnmounted } from 'vue'

export function useEventListener<K extends keyof WindowEventMap>(
  cible: Window,
  evenement: K,
  gestionnaire: (e: WindowEventMap[K]) => void,
) {
  onMounted(() => cible.addEventListener(evenement, gestionnaire))
  onUnmounted(() => cible.removeEventListener(evenement, gestionnaire))
}
```

### 7.8 Pièges fréquents

- Oublier `.prevent` sur un `<form @submit>` : la page se recharge.
- Écouter un événement natif (`@keyup.enter`) sur un **composant** qui n'émet pas cet événement ni ne le transmet à sa racine.
- Combiner `.passive` et `.prevent` : conflit.
- Appeler la méthode au lieu de la **référencer** : `@click="faire()"` est un gestionnaire en ligne qui l'appelle au clic (correct), mais `:onClick="faire()"` l'exécute au **rendu**.

### Synthèse du chapitre 7

`@evenement="gestionnaire"` accepte du code **en ligne** ou une **méthode**. Les modificateurs `.stop .prevent .self .capture .once .passive`, les modificateurs de **touches**, de **souris** et `.exact` couvrent les besoins courants. `$event` donne accès à l'événement natif ; typez-le dans les fonctions externes.

---

## 8. Formulaires et `v-model`

**Objectifs d'apprentissage.** Maîtriser `v-model` sur tous les types de champs ; comprendre son fonctionnement interne ; utiliser ses modificateurs ; créer des **composants compatibles `v-model`** avec `defineModel` (un ou plusieurs modèles, modificateurs personnalisés) ; concevoir validation et soumission ; connaître les cas particuliers (fichiers, composition IME).

### 8.1 Principe de `v-model`

`v-model` crée une **liaison bidirectionnelle** entre un champ de formulaire (ou un composant) et une donnée. C'est un **sucre syntaxique** pour la combinaison d'une liaison de valeur et d'un écouteur d'événement.

```vue
<!-- Ces deux lignes sont équivalentes : -->
<input v-model="texte" />
<input :value="texte" @input="texte = ($event.target as HTMLInputElement).value" />
```

`v-model` **ignore** les attributs `value`, `checked` et `selected` du HTML : la **source de vérité** est l'état JavaScript. Initialisez donc la valeur dans le script.

| Élément | Propriété liée | Événement écouté |
| --- | --- | --- |
| `<input type="text">`, `<textarea>` | `value` | `input` |
| `<input type="checkbox">`, `<input type="radio">` | `checked` | `change` |
| `<select>` | `value` | `change` |

### 8.2 Types de champs

#### Texte

```vue
<input v-model="message" />
<textarea v-model="message"></textarea>        <!-- et non <textarea>{{ message }}</textarea> -->
```

> **Composition IME** (chinois, japonais, coréen). Pendant la composition d'un caractère, `v-model` **attend la fin** de celle-ci avant de mettre à jour la donnée. Pour réagir pendant la composition, utilisez `:value` avec `@input`.

#### Case à cocher

```vue
<input type="checkbox" v-model="coche" />                                      <!-- booléen -->
<input type="checkbox" v-model="coche" true-value="oui" false-value="non" />   <!-- valeurs personnalisées -->

<!-- Plusieurs cases liées au même tableau -->
<input type="checkbox" value="A" v-model="choix" />
<input type="checkbox" value="B" v-model="choix" />      <!-- choix : ref<string[]>([]) -->
```

#### Boutons radio

```vue
<input type="radio" value="Un" v-model="selection" />
<input type="radio" value="Deux" v-model="selection" />
```

#### Liste déroulante

```vue
<select v-model="option">
  <option disabled value="">Choisissez</option>
  <option value="a">A</option>
  <option v-for="o in options" :key="o.id" :value="o.id">{{ o.nom }}</option>
</select>

<select v-model="multiples" multiple>…</select>      <!-- tableau de valeurs -->
```

> Avec `v-model` sur un `<select>`, si la valeur initiale ne correspond à aucune option, le `<select>` est rendu dans un état « non sélectionné » : sur iOS, l'utilisateur ne peut alors pas choisir. Fournissez une **première option désactivée** avec une valeur vide.

#### Valeurs non textuelles avec `:value`

```vue
<input type="radio" v-model="choix" :value="{ id: 1 }" />
<select v-model="obj"><option :value="{ id: 1 }">A</option></select>
```

### 8.3 Modificateurs

| Modificateur | Effet |
| --- | --- |
| `.lazy` | Synchronise sur l'événement `change` au lieu de `input` |
| `.number` | Convertit en nombre (`parseFloat`) ; si c'est impossible, garde la chaîne |
| `.trim` | Supprime les espaces en début et fin |

```vue
<input v-model.lazy="msg" />
<input v-model.number="age" type="number" />       <!-- .number est appliqué automatiquement avec type="number" -->
<input v-model.trim="nom" />
```

### 8.4 `v-model` sur un composant

#### Avec `defineModel()` *(à jour, 3.4)*

```vue
<!-- src/components/ChampTexte.vue -->
<script setup lang="ts">
const modele = defineModel<string>()          // un ref bidirectionnel (prop + événement)
</script>

<template>
  <input v-model="modele" />
</template>
```

```vue
<!-- Parent -->
<script setup lang="ts">
import { ref } from 'vue'
import ChampTexte from './ChampTexte.vue'

const nom = ref('')
</script>

<template><ChampTexte v-model="nom" /></template>
```

`defineModel` :

- déclare une **prop** `modelValue` ;
- déclare l'**événement** `update:modelValue` ;
- retourne un **`ref`** : **lire** donne la valeur de la prop, **écrire** émet l'événement.

Si le parent n'utilise pas `v-model`, le `ref` retourné se comporte comme un état **local** (il garde sa propre valeur), ce qui rend le composant utilisable des deux manières.

#### Options

```ts
const modele = defineModel<string>({ required: true })
const modele2 = defineModel<number>({ default: 0 })

// Transformer la valeur avec get / set
const modele3 = defineModel<string>({
  set(v) { return v.trim() },                // appelé quand le composant écrit
})
```

#### Plusieurs `v-model` (avec argument)

```vue
<!-- Parent -->
<FormulaireUtilisateur v-model:prenom="p" v-model:nom="n" />

<!-- FormulaireUtilisateur.vue -->
<script setup lang="ts">
const prenom = defineModel<string>('prenom')
const nom = defineModel<string>('nom')
</script>
```

#### Modificateurs personnalisés

```vue
<ChampTexte v-model.capitalize="texte" />
```

```ts
// ChampTexte.vue : le deuxième élément du tuple contient les modificateurs
const [valeur, modificateurs] = defineModel<string, 'capitalize'>({
  set(v) {
    return modificateurs.capitalize ? v.charAt(0).toUpperCase() + v.slice(1) : v
  },
})
```

#### Approche manuelle (équivalente, héritage de Vue 3.0 à 3.3)

```vue
<script setup lang="ts">
const props = defineProps<{ modelValue: string }>()
const emit = defineEmits<{ 'update:modelValue': [valeur: string] }>()
</script>

<template>
  <input
    :value="props.modelValue"
    @input="emit('update:modelValue', ($event.target as HTMLInputElement).value)"
  />
</template>
```

#### Variante avec `computed`

```ts
const valeur = computed({
  get: () => props.modelValue,
  set: (v: string) => emit('update:modelValue', v),
})
```

### 8.5 Validation et soumission

```vue
<script setup lang="ts">
import { reactive, computed } from 'vue'

const form = reactive({ email: '', mdp: '' })

const erreurs = computed(() => ({
  email: /^\S+@\S+\.\S+$/.test(form.email) ? '' : 'Email invalide',
  mdp: form.mdp.length >= 8 ? '' : '8 caractères minimum',
}))
const valide = computed(() => !erreurs.value.email && !erreurs.value.mdp)

async function soumettre() {
  if (!valide.value) return
  await fetch('/api/login', { method: 'POST', body: JSON.stringify(form) })
}
</script>

<template>
  <form @submit.prevent="soumettre" novalidate>
    <input v-model.trim="form.email" type="email" />
    <small>{{ erreurs.email }}</small>
    <input v-model="form.mdp" type="password" />
    <small>{{ erreurs.mdp }}</small>
    <button :disabled="!valide">Connexion</button>
  </form>
</template>
```

**Principes de conception d'un formulaire**

- **Source unique de vérité** : un seul objet réactif pour les valeurs.
- Erreurs **dérivées** (`computed`), jamais stockées à part.
- N'afficher une erreur qu'après **interaction** (état « touché ») pour ne pas agresser l'utilisateur.
- **Accessibilité** : `label` associé (avec `useId`), `aria-invalid` et `aria-describedby` vers le message d'erreur.
- La validation **côté client** améliore l'expérience ; la validation **côté serveur** reste obligatoire pour la sécurité.

**Bibliothèques de validation** : **VeeValidate**, **FormKit**, **Vuelidate**, avec des schémas **Zod** ou **Valibot** pour un typage de bout en bout (le schéma produit à la fois la validation à l'exécution et le type TypeScript).

### 8.6 Cas particuliers

- **`<input type="file">`** : `v-model` n'est pas supporté ; utilisez `@change` et `event.target.files`.
- **`<input type="range">`, `date`, `color`** : fonctionnent avec `v-model` (valeur sous forme de chaîne).
- **Éléments personnalisés natifs** : `v-model` utilise par défaut `value` et `input`.
- **`v-model` sur un `ref` de tableau ou d'objet** : la mutation interne est détectée ; pour une valeur non primitive dans un composant, préférez remplacer la valeur entière.

### 8.7 Pièges fréquents

- `<textarea>{{ x }}</textarea>` ne crée aucune liaison : utilisez `v-model`.
- Oublier `.number` pour récupérer des nombres.
- **Modifier directement une prop** dans un composant au lieu d'utiliser `defineModel` ou `emit`.
- Utiliser `v-model` sur une valeur **non assignable** (par exemple `v-model="a + b"`).
- Initialiser un champ avec l'attribut HTML `value` : il est ignoré.
- Valider uniquement côté client.

### Synthèse du chapitre 8

`v-model` équivaut à une liaison de valeur plus un écouteur d'événement, adaptés à chaque élément. Modificateurs : **`.lazy`**, **`.number`**, **`.trim`**. Pour les composants : **`defineModel()`** (prop + événement), **plusieurs `v-model:argument`**, modificateurs personnalisés. Validez avec des propriétés calculées ou des schémas **Zod** / **Valibot**, et **toujours aussi côté serveur**.

---

## 9. Cycle de vie

**Objectifs d'apprentissage.** Connaître les phases de vie d'un composant et leurs **hooks** ; savoir où placer chaque type de logique (initialisation, accès au DOM, nettoyage) ; enregistrer correctement les hooks (y compris dans un composable) ; comprendre l'ordre parent / enfants ; gérer les erreurs avec `onErrorCaptured` ; utiliser `onActivated` et `onDeactivated` avec `KeepAlive`.

### 9.1 Vue d'ensemble

Chaque composant passe par quatre grandes étapes : **création → montage → mises à jour → démontage**. Vue offre des **hooks** (fonctions de rappel) pour exécuter du code à chacune de ces étapes.

```text
setup()  /  <script setup>
  │
  ├─► onBeforeMount     (avant le rendu initial)
  ├─► [rendu initial]
  ├─► onMounted         (DOM créé et inséré)
  │
  │   changement d'état réactif ─┐
  │                              ▼
  ├─► onBeforeUpdate    (avant la mise à jour du DOM)
  ├─► [nouveau rendu + modification du DOM]
  ├─► onUpdated         (après la mise à jour du DOM)
  │
  ├─► onBeforeUnmount   (avant le démontage)
  └─► onUnmounted       (après le démontage)
```

Dans `<script setup>`, le **code de premier niveau** remplace les hooks `beforeCreate` et `created` de l'Options API : il s'exécute à la création de l'instance.

### 9.2 Les hooks

| Hook | Moment | Usage typique |
| --- | --- | --- |
| `setup()` / `<script setup>` | Création de l'instance | État, propriétés calculées, observateurs, appels de composables |
| `onBeforeMount` | Avant le premier rendu (DOM pas encore créé) | Rare |
| `onMounted` | **Après** le montage ; DOM accessible | Accès au DOM, références de gabarit, initialisation de bibliothèques, écouteurs, requêtes côté client |
| `onBeforeUpdate` | Avant la mise à jour du DOM | Lire l'état du DOM avant sa modification |
| `onUpdated` | Après la mise à jour du DOM | Opérations postérieures au DOM (**évitez de modifier l'état ici**) |
| `onBeforeUnmount` | Avant le démontage (l'instance est encore fonctionnelle) | Dernières lectures |
| `onUnmounted` | Après le démontage | **Nettoyage** : minuteurs, écouteurs, WebSocket, observateurs |
| `onErrorCaptured` | Erreur d'un composant **descendant** | Gestion d'erreur, frontière d'erreur |
| `onRenderTracked` | Une dépendance est suivie (**développement uniquement**) | Débogage |
| `onRenderTriggered` | Un re-rendu est déclenché (**développement uniquement**) | Débogage |
| `onActivated` / `onDeactivated` | Composant mis en cache par `<KeepAlive>` | Reprendre ou suspendre une activité |
| `onServerPrefetch` | **SSR uniquement** | Précharger des données côté serveur |

> **En SSR**, `onBeforeMount`, `onMounted`, `onBeforeUpdate`, `onUpdated`, `onBeforeUnmount` et `onUnmounted` ne s'exécutent **pas** côté serveur. Tout code qui touche au navigateur doit donc se trouver dans `onMounted` (chapitre 24).

### 9.3 Utilisation

```vue
<script setup lang="ts">
import { onMounted, onUpdated, onUnmounted, ref } from 'vue'

const el = ref<HTMLElement | null>(null)

function onResize() { /* … */ }

onMounted(() => {
  console.log('monté', el.value)
  window.addEventListener('resize', onResize)
})

onUpdated(() => console.log('mis à jour'))

onUnmounted(() => {
  window.removeEventListener('resize', onResize)    // nettoyage : indispensable
})
</script>
```

#### Règles d'enregistrement

- Les hooks doivent être appelés **de façon synchrone** pendant l'exécution de `setup()` (ou d'un composable appelé depuis `setup()`).
- Ils sont **liés à l'instance courante**. Appelés après un `await` dans un `setup()` classique, ils **ne fonctionnent pas** ; dans `<script setup>`, le compilateur restaure le contexte après un `await` de premier niveau.
- On peut déclarer **plusieurs fois** le même hook : ils s'exécutent dans l'ordre de déclaration.

### 9.4 Ordre entre parent et enfants

**Montage** : le parent exécute `setup` et `onBeforeMount`, puis chaque enfant fait de même, puis les `onMounted` des enfants s'exécutent **avant** celui du parent.

```text
Parent setup → Parent beforeMount
  → Enfant setup → Enfant beforeMount → Enfant mounted
→ Parent mounted
```

Autrement dit, quand `onMounted` du parent s'exécute, **tout l'arbre est monté** et accessible.

**Démontage** : `beforeUnmount` du parent, puis `beforeUnmount` des enfants, puis `unmounted` des enfants, puis `unmounted` du parent.

### 9.5 `onErrorCaptured`

```ts
import { onErrorCaptured } from 'vue'

onErrorCaptured((err, instance, info) => {
  console.error(err, info)
  return false          // false : stoppe la propagation vers les ancêtres
})
```

Le hook capture les erreurs de **rendu**, de **hooks**, d'**observateurs** et de **gestionnaires d'événements** des composants **descendants**. Sans retour `false`, l'erreur continue de remonter jusqu'au gestionnaire global `app.config.errorHandler` (chapitre 15). Il permet de construire une **frontière d'erreur** qui affiche un message de repli.

### 9.6 `<KeepAlive>` : activation et désactivation

```ts
import { onActivated, onDeactivated } from 'vue'

onActivated(() => { /* composant réaffiché (aussi appelé au premier montage) */ })
onDeactivated(() => { /* composant mis en cache (aussi appelé au démontage) */ })
```

Dans un composant mis en cache, `onMounted` ne se déclenche **qu'une fois** ; utilisez `onActivated` pour actualiser les données à chaque retour sur la vue.

### 9.7 Où placer quoi ? Guide pratique

| Besoin | Où |
| --- | --- |
| Déclarer état, propriétés calculées, observateurs | `<script setup>` (premier niveau) |
| Requête de données côté client | `onMounted`, ou `watch` / `watchEffect` / composable |
| Accès à un élément du DOM | `onMounted` |
| Intégrer une bibliothèque tierce (graphique, carte) | `onMounted`, puis destruction dans `onUnmounted` |
| Écouteurs globaux | `onMounted` / `onUnmounted` |
| Minuteurs (`setInterval`) | Démarrage dans `onMounted`, `clearInterval` dans `onUnmounted` |

### 9.8 Pièges fréquents

- Accéder au DOM dans `<script setup>` (premier niveau) : le DOM n'existe pas encore.
- Oublier de **nettoyer** : fuites de mémoire et écouteurs en double.
- **Modifier l'état dans `onUpdated`** : boucle de rendu infinie.
- Appeler un hook dans un callback **asynchrone** ou après un `await` hors `<script setup>`.
- Supposer que `onMounted` s'exécute côté serveur.
- Attendre que `onMounted` s'exécute à chaque affichage d'un composant mis en cache par `KeepAlive`.

### Synthèse du chapitre 9

`setup` équivaut à `beforeCreate` plus `created`. **`onMounted`** signifie « DOM prêt » ; **`onUnmounted`** sert au **nettoyage**. Les hooks s'enregistrent **de façon synchrone** pendant `setup`. Les enfants sont montés **avant** le parent. `onErrorCaptured` capture les erreurs des descendants ; `onActivated` et `onDeactivated` gèrent le cache de `KeepAlive`.

---

# Partie II — Composants et réutilisation

## 10. Composants

**Objectifs d'apprentissage.** Définir, enregistrer et utiliser des composants ; maîtriser les **props** (déclaration par types, valeurs par défaut, déstructuration réactive, validation, flux unidirectionnel), les **événements** (`defineEmits`), `defineExpose`, `defineOptions` et `defineSlots` ; comprendre le **transfert d'attributs** (`$attrs`) ; utiliser les composants **dynamiques**, **asynchrones**, **génériques**, **fonctionnels**, **récursifs** et les éléments personnalisés ; choisir le bon mode de communication entre composants.

### 10.1 Définition et philosophie

Un **composant** est une unité d'interface **réutilisable** qui encapsule structure, comportement et style. Il reçoit des **entrées** (props, slots) et produit des **sorties** (événements, valeurs exposées).

```text
          props ↓             ↑ événements (emit)
   Parent ─────────► Composant ─────────► Parent
          slots ↓
```

**Principe fondamental : « props vers le bas, événements vers le haut ».** Les données descendent (parent vers enfant), les événements remontent (enfant vers parent). Un composant ne modifie **jamais** directement les données de son parent.

#### Conventions de nommage

- Fichiers : **PascalCase** (`CarteUtilisateur.vue`) ou kebab-case (`carte-utilisateur.vue`) ; restez **cohérent**.
- Composants **multi-mots** (`TodoItem`, pas `Item`) pour éviter les collisions avec les éléments HTML existants et futurs.
- Dans le gabarit : PascalCase (`<CarteUtilisateur />`) ou kebab-case (`<carte-utilisateur>`) ; **PascalCase recommandé** dans les SFC.
- Composants **de base** (présentation, sans état global) : préfixe `Base`, `App` ou `V` (`BaseButton`) ; composants **uniques** (une seule instance par page) : préfixe `The` (`TheHeader`) ; composants **étroitement couplés** : nom du parent en préfixe (`TodoListItem`).

### 10.2 Enregistrement des composants

#### Local *(recommandé)*

```vue
<script setup lang="ts">
import CarteUtilisateur from './CarteUtilisateur.vue'   // disponible dans le gabarit
</script>

<template><CarteUtilisateur /></template>
```

#### Global

```ts
// src/main.ts
import { createApp } from 'vue'
import BaseButton from './components/BaseButton.vue'
import App from './App.vue'

const app = createApp(App)
app.component('BaseButton', BaseButton)      // disponible dans tous les gabarits de l'application
```

| | **Local** | **Global** |
| --- | --- | --- |
| Élimination du code inutilisé (*tree-shaking*) | Oui | Non |
| Dépendances explicites | Oui | Non |
| Typage | Automatique | Nécessite `GlobalComponents` (chapitre 19) |
| Usage | Par défaut | Composants vraiment omniprésents |

### 10.3 Props

Une **prop** est un attribut personnalisé qu'un composant déclare pour **recevoir des données** de son parent.

#### Déclaration par types *(recommandée)*

```vue
<!-- src/components/CarteArticle.vue -->
<script setup lang="ts">
interface Props {
  titre: string
  compteur?: number
  statut: 'actif' | 'inactif'
  tags?: string[]
  onSelect?: (id: number) => void
}

const props = defineProps<Props>()
// props.titre (lecture seule) ; dans le gabarit : {{ titre }}
</script>
```

Le compilateur lit le type pour **générer la déclaration d'exécution** des props. Les types importés depuis un autre fichier sont supportés, tant qu'ils sont **analysables statiquement** (types simples, unions, intersections, `Pick`, `Omit`, `Partial`) ; certains types conditionnels complexes ne le sont pas.

#### Valeurs par défaut

**Avec `withDefaults`** :

```ts
const props = withDefaults(defineProps<Props>(), {
  compteur: 0,
  tags: () => [],            // objets et tableaux : fonction de fabrique obligatoire
  statut: 'actif',
})
```

**Déstructuration réactive des props** *(à jour, stable depuis la 3.5)* :

```ts
const { titre, compteur = 0, tags = [] } = defineProps<Props>()
// `titre` et `compteur` restent réactifs : le compilateur réécrit en props.titre, props.compteur
```

> **Dans un `watch` ou un composable**, une prop déstructurée doit être passée **dans un getter** : `watch(() => compteur, …)` ou `useTruc(() => compteur)`. Passer `compteur` directement transmettrait une valeur figée.

#### Déclaration à l'exécution (*runtime*)

```ts
import type { PropType } from 'vue'

const props = defineProps({
  titre: { type: String, required: true },
  compteur: { type: Number, default: 0 },
  items: { type: Array as PropType<string[]>, default: () => [] },
  niveau: {
    type: String as PropType<'a' | 'b'>,
    validator: (v: string) => ['a', 'b'].includes(v),
  },
})
```

Options : `type` (`String`, `Number`, `Boolean`, `Array`, `Object`, `Date`, `Function`, `Symbol`, une classe, ou un tableau de types), `required`, `default`, `validator`. Utilisez cette forme dans une bibliothèque qui doit contrôler finement les types à l'exécution ; pour une application, la déclaration par types est plus simple.

#### Casse

- **Déclaration** : camelCase (`titreArticle`).
- **Utilisation dans le gabarit** : kebab-case (`titre-article`) ou camelCase ; les deux fonctionnent en SFC.

#### Passage de valeurs

```vue
<Article titre="Bonjour" />                    <!-- chaîne statique -->
<Article :compteur="42" />                      <!-- expression : nombre -->
<Article :tags="['a', 'b']" :actif="true" />
<Article v-bind="objetDePropsComplet" />        <!-- plusieurs props depuis un objet -->
```

> **Piège.** `compteur="42"` (sans deux-points) passe la **chaîne** `"42"`, pas le nombre.

#### Cast des booléens

```vue
<Bouton disabled />              <!-- disabled vaut true -->
<Bouton :disabled="false" />
```

Si la prop est déclarée de type `Boolean`, un attribut sans valeur ou avec une chaîne vide vaut **`true`**, et son **absence** vaut **`false`** (même si elle est optionnelle).

#### Flux de données unidirectionnel

**Ne modifiez jamais une prop** : Vue affiche un avertissement en développement. Deux situations courantes et leur solution :

```ts
// 1. La prop sert de valeur initiale à un état local
const compteurLocal = ref(props.compteur)

// 2. La prop doit être transformée
const majuscules = computed(() => props.titre.toUpperCase())
```

> Les props **objets et tableaux** sont passées **par référence** : modifier `props.objet.x` ne déclenche **pas** d'avertissement, mais viole le flux de données et rend le code difficile à suivre. À éviter ; émettez un événement ou utilisez `defineModel`.

#### Validation

Les erreurs de validation des props (type incorrect, prop requise absente, `validator` négatif) produisent des **avertissements en développement uniquement**.

### 10.4 Événements (`defineEmits`)

```vue
<script setup lang="ts">
// Syntaxe courte avec tuples nommés (3.3+)
const emit = defineEmits<{
  changer: [valeur: number]
  supprimer: [id: number, raison?: string]
  fermer: []
}>()

// Syntaxe par signatures d'appel (équivalente)
// const emit = defineEmits<{ (e: 'changer', valeur: number): void }>()

function valider() { emit('changer', 42) }
</script>
```

```vue
<!-- Parent -->
<Enfant @changer="(v) => console.log(v)" @fermer="ouvert = false" />
```

#### Règles

- Les noms d'événements sont **sensibles à la casse**. Convention : **camelCase** à l'émission, **kebab-case** à l'écoute (`@ma-valeur`) ; les deux fonctionnent avec `@`.
- **Déclarez** les événements : cela documente le composant, active le typage et **exclut** ces écouteurs du transfert d'attributs (`$attrs`).
- Les événements de composants **ne remontent pas** (pas de propagation en bulle) : seul le parent **direct** les reçoit. Pour une communication à distance : `provide` / `inject`, store ou bus d'événements externe.
- Nommez les événements par un **verbe ou un fait** (`soumettre`, `selection-change`) ; la convention `update:xxx` est réservée à `v-model`.

#### Validation à l'exécution

```ts
const emit = defineEmits({
  soumettre: (payload: { email: string }) => !!payload.email,   // false : avertissement en développement
})
```

#### Dans un `<script>` classique (Options API)

```ts
this.$emit('changer', valeur)
```

### 10.5 `defineExpose`

Dans `<script setup>`, un composant est **fermé par défaut** : une référence de gabarit côté parent **ne voit rien** de ses variables. Pour exposer explicitement une API publique :

```vue
<!-- src/components/Compteur.vue -->
<script setup lang="ts">
import { ref } from 'vue'

const compteur = ref(0)
function reinitialiser() { compteur.value = 0 }

defineExpose({ compteur, reinitialiser })
</script>
```

```vue
<!-- Parent -->
<script setup lang="ts">
import { useTemplateRef } from 'vue'
import Compteur from './Compteur.vue'

const compteur = useTemplateRef<InstanceType<typeof Compteur>>('compteur')
function go() { compteur.value?.reinitialiser() }
</script>

<template><Compteur ref="compteur" /></template>
```

> À utiliser **avec parcimonie** : le modèle **props / événements** reste préférable ; l'exposition crée un couplage **impératif** (le parent « commande » l'enfant). Cas légitimes : `focus()` sur un champ, ouverture d'une modale, lecteur multimédia.

### 10.6 `defineOptions` et `defineSlots`

```vue
<script setup lang="ts">
defineOptions({
  name: 'MonComposant',      // utile pour les DevTools, include/exclude de KeepAlive, récursivité
  inheritAttrs: false,       // désactive le transfert automatique d'attributs
})

defineSlots<{
  default(props: { message: string }): any
  entete?(props: { titre: string }): any
}>()
</script>
```

`defineSlots` ne produit **aucun code d'exécution** : il sert uniquement au **typage** (autocomplétion et vérification des variables de slot côté parent).

### 10.7 Transfert d'attributs (`$attrs`)

Les **attributs** et **écouteurs** passés à un composant mais **non déclarés** comme `props` ou `emits` sont **automatiquement appliqués à l'élément racine** : c'est le *fallthrough*.

```vue
<!-- MonBouton.vue -->
<template><button class="btn">Cliquer</button></template>

<!-- Parent -->
<MonBouton class="large" id="b1" @click="go" />
<!-- rendu : <button class="btn large" id="b1" …> : classes fusionnées, écouteur attaché -->
```

#### Règles de fusion

- `class` et `style` sont **fusionnés**.
- Les autres attributs sont **écrasés** par la valeur du parent.
- Les écouteurs d'un même événement sont **chaînés** (les deux s'exécutent).

#### Désactiver et cibler manuellement

```vue
<script setup lang="ts">
defineOptions({ inheritAttrs: false })
</script>

<template>
  <div class="enveloppe">
    <input v-bind="$attrs" />       <!-- tous les attributs vont sur <input>, pas sur la racine -->
  </div>
</template>
```

#### Accès depuis le script

```ts
import { useAttrs } from 'vue'

const attrs = useAttrs()     // non réactif : valeurs à jour à chaque rendu, mais non observables par watch
```

#### Racines multiples

Un composant à **plusieurs racines** n'a **pas** de transfert automatique : Vue avertit tant que `$attrs` n'est pas lié explicitement (`<header v-bind="$attrs">`).

### 10.8 Composants dynamiques

```vue
<script setup lang="ts">
import { shallowRef } from 'vue'
import A from './A.vue'
import B from './B.vue'

const courant = shallowRef(A)      // shallowRef : évite de rendre le composant réactif
</script>

<template>
  <component :is="courant" />
  <component :is="'div'" class="x" />                   <!-- élément HTML natif -->
  <component :is="condition ? A : B" v-bind="props" />
</template>
```

- Associé à **`<KeepAlive>`**, il conserve l'état des vues désactivées (chapitre 16).
- Évitez de rendre un composant **réactif** (avec `ref`) : utilisez `shallowRef` ou `markRaw`.
- `:is` accepte aussi le **nom** d'un composant enregistré (`resolveComponent`) ou une chaîne désignant un élément HTML.

### 10.9 Composants asynchrones

```ts
import { defineAsyncComponent } from 'vue'

const Lourd = defineAsyncComponent(() => import('./Lourd.vue'))

const AvecEtats = defineAsyncComponent({
  loader: () => import('./Lourd.vue'),
  loadingComponent: Chargement,       // composant d'attente
  delay: 200,                         // délai avant d'afficher le chargement (ms)
  errorComponent: Erreur,
  timeout: 3000,                      // délai maximal avant l'erreur
  hydrate: hydrateOnVisible(),        // stratégie d'hydratation en SSR (3.5+)
})
```

Un composant asynchrone permet le **découpage du code** (*code splitting*) : son code n'est téléchargé qu'au moment de son premier affichage. Il s'associe à **`<Suspense>`** pour gérer les dépendances asynchrones (chapitre 16) et aux **stratégies d'hydratation paresseuse** (chapitre 24).

### 10.10 Composants génériques *(ajout, 3.3)*

```vue
<!-- src/components/ListeSelectionnable.vue -->
<script setup lang="ts" generic="T extends string | number, U extends { id: T }">
defineProps<{
  items: U[]
  selectionne: T
}>()

const emit = defineEmits<{ choisir: [item: U] }>()
</script>
```

Le type `T` est **inféré à l'utilisation**, avec autocomplétion et vérification :

```vue
<ListeSelectionnable :items="[{ id: 1 }, { id: 2 }]" :selectionne="1" />    <!-- T = number -->
```

L'attribut `generic` accepte plusieurs paramètres séparés par des virgules et les mêmes contraintes `extends` que TypeScript.

### 10.11 Composants fonctionnels

Un **composant fonctionnel** est une fonction pure qui reçoit `props` et un contexte (`attrs`, `slots`, `emit`) et retourne des nœuds virtuels. Il n'a **ni état propre ni cycle de vie**.

```ts
import { h, type FunctionalComponent } from 'vue'

interface Props { niveau: 1 | 2 | 3 }

const Titre: FunctionalComponent<Props, { clic: [e: MouseEvent] }> = (props, { slots, emit }) =>
  h(`h${props.niveau}`, { onClick: (e: MouseEvent) => emit('clic', e) }, slots.default?.())

Titre.props = ['niveau']
Titre.emits = ['clic']
```

Sans déclaration de `props`, **tous** les attributs sont transmis comme `props`. Les composants fonctionnels sont rarement utiles dans une application ; ils servent surtout dans des bibliothèques (chapitre 21).

### 10.12 Composants récursifs

Un SFC peut **s'appeler lui-même** par le nom de son fichier (ou son option `name`).

```vue
<!-- src/components/ElementArbre.vue -->
<script setup lang="ts">
interface Noeud { label: string; enfants?: Noeud[] }
defineProps<{ noeud: Noeud }>()
</script>

<template>
  <li>
    {{ noeud.label }}
    <ul v-if="noeud.enfants?.length">
      <ElementArbre v-for="e in noeud.enfants" :key="e.label" :noeud="e" />
    </ul>
  </li>
</template>
```

Prévoyez toujours une **condition d'arrêt** (ici `v-if`), sous peine de récursion infinie.

### 10.13 Éléments personnalisés (*Web Components*)

```ts
import { defineCustomElement } from 'vue'
import MonComposant from './MonComposant.ce.vue'

const MonElement = defineCustomElement(MonComposant)
customElements.define('mon-element', MonElement)
```

Un composant Vue peut être exporté comme **élément personnalisé natif**, utilisable dans n'importe quel framework ou page HTML. Les props deviennent des propriétés et attributs, les événements émis des `CustomEvent`, les styles sont encapsulés dans un *shadow DOM*. Le fichier se nomme conventionnellement `.ce.vue` pour que ses styles soient injectés dans le shadow DOM.

### 10.14 Communication entre composants : vue d'ensemble

| Direction / portée | Mécanisme |
| --- | --- |
| Parent vers enfant | **Props**, slots |
| Enfant vers parent | **Événements (`emit`)**, `v-model` |
| Parent vers enfant (impératif) | **Référence de gabarit + `defineExpose`** |
| Ancêtre vers descendants | **`provide` / `inject`** (chapitre 12) |
| Global ou sans lien | **Store (Pinia)**, composable partagé, bus d'événements (bibliothèque) |

### 10.15 Pièges fréquents

- **Modifier une prop**.
- Donner pour valeur par défaut un **objet ou tableau** sans fonction de fabrique (`default: () => ({})`).
- Utiliser une **référence de composant** sans `defineExpose`.
- Oublier de déclarer les `emits` : les écouteurs tombent dans `$attrs` et peuvent s'exécuter deux fois.
- Déstructurer des props **avant Vue 3.5** : la réactivité est perdue.
- Mettre `inheritAttrs: false` sans lier `$attrs`.
- Passer `:titre="'x'"` sans nécessité, ou oublier les deux-points pour un nombre.

### Synthèse du chapitre 10

**Props vers le bas, événements vers le haut.** `defineProps<T>()`, `defineEmits<T>()` et `defineModel<T>()` offrent une API **typée**. `$attrs` transmet attributs et écouteurs non déclarés à la racine. Les composants **génériques**, **asynchrones**, **dynamiques** et **fonctionnels** couvrent les cas avancés ; `defineExpose` reste une exception à utiliser avec parcimonie.

---

## 11. Slots

**Objectifs d'apprentissage.** Distribuer du contenu depuis le parent vers un composant enfant ; maîtriser les slots **par défaut**, **nommés**, **à portée** et **dynamiques** ; définir un **contenu de repli** ; tester l'existence d'un slot ; typer les slots avec `defineSlots` ; comprendre les composants sans rendu (*renderless*) et leurs usages.

### 11.1 Définition

Les **slots** (« emplacements ») permettent au **parent** de **passer du contenu de gabarit** (HTML, autres composants) à l'**enfant**, qui décide **où** l'afficher grâce à l'élément `<slot>`. Ils inversent le contrôle du rendu : le composant fournit la **structure**, le parent fournit le **contenu**.

Les props transmettent des **données** ; les slots transmettent du **balisage**. Quand un composant a besoin que son utilisateur décide de ce qu'il affiche à un endroit donné (titre d'une carte, corps d'une modale, contenu d'une cellule), c'est un slot qu'il faut.

```vue
<!-- src/components/Carte.vue -->
<template>
  <div class="carte">
    <slot>Contenu par défaut (repli)</slot>
  </div>
</template>
```

```vue
<!-- Parent -->
<Carte>Mon contenu <strong>riche</strong></Carte>
<Carte />        <!-- affiche le contenu de repli -->
```

#### Portée de compilation

Le contenu d'un slot est défini **dans le parent** : il a accès à la portée **du parent**, **pas** à celle de l'enfant (sauf par les *props de slot*, section 11.5). Règle simple : **tout ce qui est dans le gabarit du parent est compilé dans la portée du parent**.

### 11.2 Slot par défaut et contenu de repli

Le contenu placé entre `<slot>` et `</slot>` est affiché **si aucun contenu n'est fourni** (*fallback content*).

```vue
<button type="submit"><slot>Envoyer</slot></button>
```

Un slot avec contenu de repli rend le composant utilisable **sans configuration**, tout en restant personnalisable.

### 11.3 Slots nommés

Un composant peut offrir **plusieurs emplacements** distingués par un attribut `name`.

```vue
<!-- src/components/MiseEnPage.vue -->
<template>
  <header><slot name="entete" /></header>
  <main><slot /></main>                  <!-- slot nommé « default » -->
  <footer><slot name="pied" /></footer>
</template>
```

```vue
<!-- Parent : v-slot ou son raccourci # -->
<MiseEnPage>
  <template #entete><h1>Titre</h1></template>
  <template #default><p>Contenu principal</p></template>
  <template v-slot:pied><small>© 2026</small></template>
</MiseEnPage>
```

- Le contenu qui n'est dans aucun `<template v-slot>` constitue le **slot par défaut**.
- **Évitez d'ambiguïté** : si vous utilisez des slots nommés, écrivez aussi `<template #default>` explicitement plutôt que de mélanger contenu libre et `<template #…>`. Utiliser `v-slot` directement sur le composant **et** sur des `<template>` imbriqués provoque une erreur de compilation.
- Une même `<template #nom>` ne s'écrit **qu'une fois** par composant utilisé.

### 11.4 Slots dynamiques

Le nom d'un slot peut être calculé :

```vue
<template #[nomDuSlot]>…</template>
<template v-slot:[nomDuSlot]>…</template>
```

Même contrainte que pour les arguments dynamiques de directives (chaîne, sans espaces).

### 11.5 Slots à portée (*scoped slots*)

L'enfant peut **passer des données** au contenu fourni par le parent, au moyen de **props de slot** (attributs placés sur `<slot>`).

```vue
<!-- src/components/Liste.vue -->
<script setup lang="ts" generic="T">
defineProps<{ items: T[] }>()
</script>

<template>
  <ul>
    <li v-for="(item, index) in items" :key="index">
      <slot :item="item" :index="index">{{ item }}</slot>      <!-- props de slot + repli -->
    </li>
  </ul>
</template>
```

```vue
<!-- Parent -->
<Liste :items="utilisateurs">
  <template #default="{ item, index }">
    {{ index + 1 }}. {{ item.nom }}
  </template>
</Liste>

<!-- Slot par défaut seul : v-slot directement sur le composant -->
<Liste :items="utilisateurs" v-slot="{ item }">{{ item.nom }}</Liste>
```

On peut voir un slot à portée comme une **fonction** : l'enfant l'appelle avec des arguments (les props de slot) et le parent fournit le corps qui produit du balisage.

#### Slots nommés à portée

```vue
<Carte>
  <template #entete="{ titre }"><h2>{{ titre }}</h2></template>
</Carte>
```

> **`name` est un attribut réservé** de `<slot>` : ne l'utilisez pas comme nom de prop de slot.

#### Déstructuration et valeurs par défaut

```vue
<template #default="{ item = { nom: 'inconnu' } }">…</template>
```

#### Composants sans rendu (*renderless*)

Un composant *renderless* encapsule de la **logique** (état, comportement) et délègue **tout le rendu** au slot à portée.

```vue
<!-- src/components/SuiviSouris.vue -->
<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const x = ref(0)
const y = ref(0)
const maj = (e: MouseEvent) => { x.value = e.pageX; y.value = e.pageY }

onMounted(() => window.addEventListener('mousemove', maj))
onUnmounted(() => window.removeEventListener('mousemove', maj))
</script>

<template><slot :x="x" :y="y" /></template>
```

```vue
<SuiviSouris v-slot="{ x, y }">Souris : {{ x }}, {{ y }}</SuiviSouris>
```

Cette technique est aujourd'hui **largement remplacée par les composables** (chapitre 13), qui évitent le coût d'une instance de composant supplémentaire. Elle reste pertinente quand la logique est **étroitement liée** à un balisage (listes virtuelles, éléments de formulaire accessibles).

### 11.6 Tester l'existence d'un slot

```vue
<script setup lang="ts">
import { useSlots } from 'vue'

const slots = useSlots()
const aEntete = !!slots.entete        // lecture ponctuelle : non réactive
</script>

<template>
  <header v-if="$slots.entete"><slot name="entete" /></header>
</template>
```

Utilisez `$slots` directement dans le gabarit : la présence est **réévaluée à chaque rendu**, alors qu'une constante calculée dans le script est figée. Cela évite d'afficher un conteneur vide (`<header></header>`) quand le parent ne fournit rien.

### 11.7 Typage avec `defineSlots`

```vue
<script setup lang="ts" generic="T">
defineProps<{ items: T[] }>()

defineSlots<{
  default(props: { item: T; index: number }): any
  vide?(): any
  entete?(props: { total: number }): any
}>()
</script>
```

Le parent bénéficie alors de la **vérification** et de l'**autocomplétion** des variables de slot ; les slots optionnels sont marqués par `?`. Pour les composants génériques, c'est la manière de lier le type `T` des props au type des variables de slot.

### 11.8 Cas d'usage

| Cas | Exemple |
| --- | --- |
| Composants de mise en page | `MiseEnPage`, `Carte`, `Modale` |
| Contenu personnalisable | Tableaux avec cellules personnalisées |
| Inversion de contrôle du rendu | `TableauDonnees` : colonne `#cell-nom="{ ligne }"` |
| Composants de formulaire | Slots `label`, `erreur`, `aide` |
| Listes avec états | Slots `vide`, `chargement`, `erreur` |

### 11.9 Pièges fréquents

- Chercher à utiliser l'état de **l'enfant** dans un slot **sans** props de slot.
- Mélanger `v-slot` sur le composant et sur des `<template>` imbriqués.
- Utiliser `name` comme prop de slot.
- Calculer la présence d'un slot dans le script au lieu de `$slots` dans le gabarit.
- Passer des **données** par un slot alors qu'une simple prop suffirait.
- Oublier que les styles `scoped` du parent s'appliquent bien au contenu du slot (il est compilé dans la portée du parent) mais que ceux de l'enfant ne l'atteignent pas sans `:slotted()`.

### Synthèse du chapitre 11

`<slot>` définit un **emplacement**, avec un **repli** s'il est vide. Les slots **nommés** (`#nom`) et **à portée** (`#nom="{ props }"`) permettent de multiplier les emplacements et de transmettre des données à contre-sens. Le contenu d'un slot est compilé dans la **portée du parent**. `defineSlots` sert au **typage**.

---

## 12. Provide / Inject

**Objectifs d'apprentissage.** Comprendre et éviter le *prop drilling* ; partager des données **réactives** et **typées** entre un ancêtre et ses descendants ; utiliser `InjectionKey` ; fournir au niveau de l'application ; connaître les bonnes pratiques, les limites et les alternatives (props, store).

### 12.1 Le problème : le *prop drilling*

Transmettre une donnée à un descendant **profond** par des props **intermédiaires** qui n'en ont pas l'usage alourdit le code et le rend fragile.

```text
App → MiseEnPage → BarreLaterale → Menu → ElementMenu     (le thème n'est utile que dans ElementMenu)
```

Chaque composant entre `App` et `ElementMenu` doit déclarer la prop `theme` et la retransmettre, uniquement pour qu'elle arrive à destination.

### 12.2 `provide` et `inject`

Un **ancêtre** *fournit* une valeur ; **n'importe quel descendant**, quelle que soit sa profondeur, peut l'*injecter*.

```ts
// Ancêtre
import { provide, ref } from 'vue'

const theme = ref('sombre')
provide('theme', theme)                  // clé de type chaîne
```

```ts
// Descendant
import { inject } from 'vue'

const theme = inject('theme')                    // unknown : non typé
const theme2 = inject('theme', 'clair')          // valeur par défaut si rien n'est fourni
```

La recherche remonte l'**arbre des composants** jusqu'au premier ancêtre qui fournit la clé : un composant intermédiaire peut donc **redéfinir** la valeur pour son sous-arbre.

#### Fournir au niveau de l'application

```ts
// src/main.ts
app.provide('urlApi', 'https://api.exemple.com')       // disponible dans tous les composants
```

C'est la méthode utilisée par les **plugins** pour exposer leurs services (chapitre 15).

### 12.3 Réactivité

Si la valeur fournie est un **`ref`** ou un **`reactive`**, elle reste **réactive** chez le consommateur.

**Bonne pratique : gardez les modifications dans le fournisseur.** Fournissez la valeur en **lecture seule** et une **fonction** pour la modifier. Ainsi, l'origine de tout changement d'état est **traçable**.

```ts
// Fournisseur
import { provide, readonly, ref } from 'vue'

const theme = ref<'clair' | 'sombre'>('clair')
function basculer() { theme.value = theme.value === 'clair' ? 'sombre' : 'clair' }

provide('theme', { theme: readonly(theme), basculer })
```

```ts
// Consommateur
import { inject, type Ref } from 'vue'

const { theme, basculer } = inject('theme') as { theme: Readonly<Ref<string>>; basculer: () => void }
```

### 12.4 Typage avec `InjectionKey`

Une clé de type **`Symbol`** typée évite les collisions de noms et permet l'**inférence** automatique des types.

```ts
// src/keys.ts
import type { InjectionKey, Ref } from 'vue'

export interface ContexteTheme {
  theme: Readonly<Ref<'clair' | 'sombre'>>
  basculer: () => void
}

export const CleTheme: InjectionKey<ContexteTheme> = Symbol('theme')
```

```ts
provide(CleTheme, { theme: readonly(theme), basculer })     // type vérifié à la compilation

const ctx = inject(CleTheme)                  // ContexteTheme | undefined
const ctx2 = inject(CleTheme, contexteParDefaut)   // ContexteTheme
const ctx3 = inject(CleTheme)!                // assertion « non nul » : si la présence est garantie
```

#### Valeur par défaut « fabrique »

```ts
const x = inject('cle', () => new ObjetCouteux(), true)   // 3e argument true : le 2e est une fabrique
```

#### Injection obligatoire (schéma sûr)

```ts
// src/composables/useTheme.ts
import { inject } from 'vue'
import { CleTheme, type ContexteTheme } from '@/keys'

export function useTheme(): ContexteTheme {
  const ctx = inject(CleTheme)
  if (!ctx) throw new Error('useTheme doit être utilisé sous <FournisseurTheme>')
  return ctx
}
```

Encapsuler `inject` dans un composable `useXxx` donne un **message d'erreur explicite** et supprime le type `undefined` chez tous les consommateurs.

#### `hasInjectionContext()` *(3.3)*

Vérifie qu'un contexte d'injection existe. Utile aux **bibliothèques** dont les fonctions peuvent être appelées à l'intérieur ou à l'extérieur d'un composant.

### 12.5 Contraintes d'appel

`provide` et `inject` doivent être appelés **de façon synchrone** dans `setup()` (ou dans un composable appelé depuis `setup`). Hors composant, utilisez `app.runWithContext(() => inject(...))` (chapitre 15).

### 12.6 `provide` / `inject`, props ou store ?

| Critère | **Props** | **provide / inject** | **Pinia** |
| --- | --- | --- | --- |
| Source de la donnée | Parent direct | Ancêtre | Globale |
| Traçabilité | Élevée | Moyenne | Élevée (DevTools) |
| Couplage | Explicite | Implicite | Global |
| Usage | Cas par défaut | Contexte d'un **sous-arbre** (thème, formulaire, i18n, composants composés) | État **global ou partagé** |

#### Cas d'usage typiques

- **Composants composés** (*compound components*) : `Onglets` / `Onglet`, `Accordeon` / `ElementAccordeon`, `Formulaire` / `ChampFormulaire` coopèrent par un contexte partagé.
- Thème, langue, configuration régionale.
- Bibliothèques : le routeur, les stores et les outils d'internationalisation utilisent `inject` en interne.

### 12.7 Pièges fréquents

- **Modifier** la valeur injectée depuis un **descendant** : la modification est difficile à tracer.
- Utiliser des clés de type **chaîne** : risque de collision entre bibliothèques ; préférez `InjectionKey`.
- Utiliser `provide` / `inject` pour tout, au lieu de props explicites : le couplage devient invisible.
- Oublier la **valeur par défaut** : l'injection vaut `undefined` et provoque des erreurs tardives.
- Fournir une valeur **non réactive** (`provide('x', unRef.value)`) et s'étonner qu'elle ne change pas.

### Synthèse du chapitre 12

`provide(clé, valeur)` et `inject(clé, défaut?)` partagent une donnée dans un **sous-arbre**, sans *prop drilling*. La valeur est réactive si c'est un `ref` ou un `reactive` ; **les modifications restent côté fournisseur**. **`InjectionKey<T>`** (un `Symbol`) assure le **typage** et évite les collisions ; encapsulez l'injection dans un composable.

---

## 13. Composables

**Objectifs d'apprentissage.** Définir et écrire des **composables** (logique à état réutilisable) ; appliquer les conventions et bonnes pratiques ; gérer les **arguments réactifs** (`MaybeRefOrGetter`, `toValue`), les effets de bord et le nettoyage ; choisir la valeur de retour ; partager un état entre composants ; comparer aux mixins, aux composants *renderless* et aux fonctions utilitaires ; tester un composable ; connaître VueUse.

### 13.1 Définition

Un **composable** est une **fonction** qui encapsule et réutilise une **logique à état** (*stateful logic*) en s'appuyant sur la **Composition API** : refs, propriétés calculées, observateurs, hooks de cycle de vie.

| | **Fonction utilitaire** | **Composable** |
| --- | --- | --- |
| Nature | Logique **sans état**, entrée → sortie | Logique **avec état réactif** et cycle de vie |
| Exemple | `formaterDate(d)`, `slugify(s)` | `useSouris()`, `useRequete(url)` |
| Dépend de l'instance ? | Non | Souvent (hooks) |

#### Conventions

- Nom en **camelCase** préfixé par **`use`** : `useSouris`, `useRequete`.
- Fichier dans un dossier `composables/`, un composable par fichier.
- Appelé **de façon synchrone** dans `setup()` / `<script setup>` ou dans un autre composable : les hooks ont besoin de l'**instance courante**.
- Retourne un **objet de `ref`** (plutôt qu'un `reactive`) pour autoriser la **déstructuration sans perte de réactivité**.

### 13.2 Exemple fondamental : `useSouris`

```ts
// src/composables/useSouris.ts
import { ref, onMounted, onUnmounted } from 'vue'

export function useSouris() {
  const x = ref(0)
  const y = ref(0)

  function actualiser(event: MouseEvent) {
    x.value = event.pageX
    y.value = event.pageY
  }

  onMounted(() => window.addEventListener('mousemove', actualiser))
  onUnmounted(() => window.removeEventListener('mousemove', actualiser))

  return { x, y }
}
```

```vue
<script setup lang="ts">
import { useSouris } from '@/composables/useSouris'

const { x, y } = useSouris()
</script>

<template>Souris : {{ x }}, {{ y }}</template>
```

**Chaque appel crée un état indépendant** : deux composants qui appellent `useSouris()` ont chacun leurs propres `x` et `y` et leurs propres écouteurs. Le composable regroupe **toute** la logique d'une préoccupation (état, effet, nettoyage) au même endroit.

#### Composition de composables

Un composable peut en utiliser d'autres.

```ts
// src/composables/useSourisDansElement.ts
import { computed, type Ref } from 'vue'
import { useSouris } from './useSouris'

export function useSourisDansElement(el: Ref<HTMLElement | null>) {
  const { x, y } = useSouris()
  const dedans = computed(() => {
    const r = el.value?.getBoundingClientRect()
    return !!r && x.value >= r.left && x.value <= r.right && y.value >= r.top && y.value <= r.bottom
  })
  return { x, y, dedans }
}
```

### 13.3 Arguments réactifs : `toValue` et `MaybeRefOrGetter`

Un composable robuste accepte des **valeurs brutes, des refs ou des getters**, et **réagit** quand l'argument change.

```ts
// src/composables/useRequete.ts
import { ref, shallowRef, toValue, watchEffect, type MaybeRefOrGetter } from 'vue'

export function useRequete<T = unknown>(url: MaybeRefOrGetter<string>) {
  const data = shallowRef<T | null>(null)
  const erreur = ref<Error | null>(null)
  const chargement = ref(false)

  watchEffect(async (onCleanup) => {
    data.value = null
    erreur.value = null
    chargement.value = true

    const controleur = new AbortController()
    onCleanup(() => controleur.abort())

    try {
      const res = await fetch(toValue(url), { signal: controleur.signal })   // toValue AVANT l'await : dépendance suivie
      if (!res.ok) throw new Error(`HTTP ${res.status}`)
      data.value = await res.json()
    } catch (e) {
      if ((e as Error).name !== 'AbortError') erreur.value = e as Error
    } finally {
      chargement.value = false
    }
  })

  return { data, erreur, chargement }
}
```

```ts
const id = ref(1)
const { data } = useRequete<Utilisateur>(() => `/api/users/${id.value}`)    // se relance quand `id` change
```

#### Types utiles

```ts
import type { MaybeRef, MaybeRefOrGetter, Ref } from 'vue'

// MaybeRef<T>         = T | Ref<T>
// MaybeRefOrGetter<T> = T | Ref<T> | (() => T)
```

`toValue()` normalise ces trois formes ; `unref()` ne gère pas les getters. Une prop déstructurée (chapitre 10) se passe aussi sous forme de getter.

### 13.4 Effets de bord et nettoyage

- **Toujours nettoyer** : `onUnmounted`, `onScopeDispose` ou `onCleanup`.
- N'exécutez les effets qui touchent au **DOM** ou au navigateur que dans `onMounted`, afin que le composable soit utilisable en **SSR**.

```ts
import { onScopeDispose } from 'vue'

export function useIntervalle(fn: () => void, ms: number) {
  const id = setInterval(fn, ms)
  onScopeDispose(() => clearInterval(id))        // fonctionne dans un composant ET dans un effectScope
}
```

`onScopeDispose` est plus général que `onUnmounted` : il fonctionne aussi hors composant (tests, composables partagés).

### 13.5 Valeur de retour : `ref` ou `reactive` ?

```ts
// Retour d'un objet de refs : déstructurable
const { x, y } = useSouris()

// Si l'on préfère l'accès par propriété sans .value : envelopper dans reactive()
const souris = reactive(useSouris())
souris.x          // déballé automatiquement
```

Retournez des **`ref`** : l'appelant choisit librement entre déstructuration (avec renommage possible : `const { x: sourisX } = useSouris()`) et enveloppe `reactive`.

### 13.6 Composables à état partagé

Un état déclaré **en dehors** de la fonction est un **singleton** partagé entre tous les composants qui l'importent.

```ts
// src/composables/useCompteurGlobal.ts
import { ref } from 'vue'

const compteur = ref(0)          // niveau du module : partagé

export function useCompteurGlobal() {
  const incrementer = () => compteur.value++
  return { compteur, incrementer }
}
```

> Pour de l'état global structuré, utilisez **Pinia** (chapitre 18) : traçabilité dans les DevTools, SSR sûr, tests. **Attention au SSR** : un état de niveau module est **partagé entre toutes les requêtes** du serveur, donc entre utilisateurs (fuite de données).

### 13.7 Composables asynchrones et `Suspense`

Un composable ne doit pas faire d'`await` de premier niveau **avant** d'appeler des hooks : le contexte d'instance serait perdu. Préférez **retourner un état** (`chargement`, `data`, `erreur`) plutôt que de bloquer, comme dans `useRequete`.

### 13.8 Restrictions d'usage

- Appelés **uniquement** dans `<script setup>`, `setup()` ou un autre composable, et **de façon synchrone**.
- Pas dans des boucles ni des conditions non déterministes : l'ordre des appels doit rester stable.
- Un composable qui n'utilise **ni hook ni état** est probablement une simple fonction utilitaire.

### 13.9 Comparaison avec d'autres techniques de réutilisation

| Technique | Problèmes ou avantages |
| --- | --- |
| **Mixins** (Vue 2, Options API) | Origine des propriétés **floue**, collisions de noms, couplage implicite, typage faible |
| **Composants *renderless*** | Surcoût d'une instance de composant, logique cachée dans le gabarit |
| **Composables** | **Sources explicites**, pas de collision (renommage à la déstructuration), typage excellent, composables imbriquables |

### 13.10 La bibliothèque VueUse

**VueUse** est une collection de plus de 200 composables prêts à l'emploi : `useStorage`, `useDark`, `useDebounceFn`, `useIntersectionObserver`, `useFetch`, `useEventListener`, `useClipboard`, `useMagicKeys`, `useVModel`, `useTitle`, `useMediaQuery`… Elle est tree-shakable et compatible SSR. **Cherchez-y d'abord** avant de réécrire un composable courant.

### 13.11 Tester un composable

- **Sans hooks ni injection** : appelez directement la fonction.
- **Avec hooks ou injection** : montez-la dans un composant « hôte » éphémère.

```ts
// src/test/utils.ts
import { createApp } from 'vue'

export function avecSetup<T>(composable: () => T): [T, ReturnType<typeof createApp>] {
  let resultat!: T
  const app = createApp({
    setup() {
      resultat = composable()
      return () => null
    },
  })
  app.mount(document.createElement('div'))
  return [resultat, app]            // app.unmount() permet de tester le nettoyage
}
```

### 13.12 Pièges fréquents

- Retourner un `reactive` puis **le déstructurer**.
- Lire un argument réactif **après** un `await` dans un `watchEffect`.
- Oublier le **nettoyage** (écouteurs, minuteurs, requêtes).
- **Partager un état involontairement** (variable de module) ou le faire fuiter en SSR.
- Appeler un composable dans un callback ou après un `await`.
- Écrire un composable monolithique qui mélange plusieurs préoccupations.

### Synthèse du chapitre 13

Un composable est une fonction `useXxx` qui retourne un **état réactif et des actions**. Acceptez **`MaybeRefOrGetter`** et lisez avec **`toValue`** ; **nettoyez** les effets ; **retournez des refs**. C'est l'alternative moderne aux mixins et aux composants *renderless* ; consultez **VueUse** avant de réinventer.

---

## 14. Directives personnalisées

**Objectifs d'apprentissage.** Savoir quand recourir à une directive personnalisée plutôt qu'à un composant ou un composable ; maîtriser les **hooks** et leurs arguments (`el`, `binding`, `vnode`) ; utiliser la forme abrégée ; écrire des directives réelles (focus, clic extérieur) ; les enregistrer et les typer ; comprendre leur comportement avec le SSR et les fonctions de rendu.

### 14.1 Définition et cas d'usage

Une **directive personnalisée** est un moyen de **réutiliser une logique de manipulation bas niveau du DOM** sur des éléments simples. Les composants et composables sont l'abstraction par défaut ; la directive est l'outil **précis** quand il faut agir directement sur un élément du DOM.

- **Adaptée à** : focus automatique, clic extérieur, infobulle, observation d'intersection, chargement différé d'images, redimensionnement, glisser-déposer, permissions.
- **À éviter** si le besoin peut s'exprimer **de façon déclarative** (props, composants, composables).
- Les directives s'appliquent à des **éléments**. Sur un composant, elles s'appliquent à son **élément racine** ; sur un composant à racines multiples, Vue avertit et la directive est ignorée.

### 14.2 Définition dans `<script setup>`

Toute variable locale nommée **`vNomDirective`** est utilisable dans le gabarit sous la forme `v-nom-directive`.

```vue
<script setup lang="ts">
const vFocus = {
  mounted: (el: HTMLInputElement) => el.focus(),
}
</script>

<template>
  <input v-focus />
</template>
```

### 14.3 Hooks d'une directive

```ts
import type { Directive } from 'vue'

const maDirective: Directive<HTMLElement, string> = {
  created(el, binding, vnode, prevVnode) {},        // avant l'application des attributs et écouteurs de l'élément
  beforeMount(el, binding, vnode) {},               // avant l'insertion dans le DOM
  mounted(el, binding, vnode) {},                   // élément et enfants montés (inséré dans le DOM parent)
  beforeUpdate(el, binding, vnode, prevVnode) {},   // avant la mise à jour du composant contenant
  updated(el, binding, vnode, prevVnode) {},        // après la mise à jour du composant et de ses enfants
  beforeUnmount(el, binding, vnode) {},             // avant le démontage
  unmounted(el, binding, vnode) {},                 // après le démontage : nettoyage
}
```

#### Arguments des hooks

| Argument | Contenu |
| --- | --- |
| `el` | L'élément DOM auquel la directive est liée |
| `binding` | Objet de liaison : `value`, `oldValue`, `arg`, `modifiers`, `instance`, `dir` |
| `vnode` | Nœud virtuel sous-jacent |
| `prevVnode` | Nœud virtuel précédent (hooks `beforeUpdate` et `updated` uniquement) |

#### L'objet `binding`

```vue
<div v-exemple:argument.mod1.mod2="valeur + 1"></div>
```

```ts
binding.value        // résultat de l'expression : valeur + 1
binding.oldValue     // valeur précédente (beforeUpdate et updated)
binding.arg          // 'argument'
binding.modifiers    // { mod1: true, mod2: true }
binding.instance     // instance du composant où la directive est utilisée
binding.dir          // l'objet de définition de la directive
```

Les **arguments dynamiques** sont supportés : `v-exemple:[arg]="valeur"`.

> **Règle.** `el` est **à vous** pour lire et modifier le DOM ; en revanche, **ne modifiez pas** les propriétés de `binding` (en lecture seule) et gardez les informations propres à l'élément dans un `WeakMap` ou dans une propriété de `el` (ne supposez jamais qu'une directive n'est utilisée qu'une fois).

### 14.4 Forme abrégée

Si l'on ne veut que `mounted` et `updated` avec **le même comportement**, une simple fonction suffit.

```ts
const vCouleur: Directive<HTMLElement, string> = (el, binding) => {
  el.style.color = binding.value
}
```

### 14.5 Exemple : clic extérieur

```ts
// src/directives/clicExterieur.ts
import type { Directive } from 'vue'

type Gestionnaire = (e: MouseEvent) => void
const gestionnaires = new WeakMap<HTMLElement, Gestionnaire>()

export const vClicExterieur: Directive<HTMLElement, () => void> = {
  mounted(el, binding) {
    const gestionnaire: Gestionnaire = (e) => {
      if (!el.contains(e.target as Node)) binding.value()     // clic hors de l'élément
    }
    gestionnaires.set(el, gestionnaire)
    document.addEventListener('click', gestionnaire)
  },
  unmounted(el) {
    const g = gestionnaires.get(el)
    if (g) document.removeEventListener('click', g)            // nettoyage indispensable
    gestionnaires.delete(el)
  },
}
```

```vue
<script setup lang="ts">
import { vClicExterieur } from '@/directives/clicExterieur'

function fermer() { /* … */ }
</script>

<template><div v-clic-exterieur="fermer">Menu</div></template>
```

### 14.6 Enregistrement global et typage

```ts
// src/main.ts
app.directive('focus', { mounted: (el) => el.focus() })
```

Typage de l'autocomplétion pour une directive globale :

```ts
declare module 'vue' {
  interface GlobalDirectives {
    vFocus: typeof vFocus
  }
}
export {}
```

### 14.7 Directives et SSR

Les hooks de directive qui manipulent le DOM **ne s'exécutent pas côté serveur**. Pour fournir des **propriétés** au rendu serveur, définissez `getSSRProps(binding, vnode)` dans la directive :

```ts
const vMonAttribut: Directive = {
  getSSRProps(binding) { return { 'data-ok': binding.value } },
}
```

### 14.8 Directives et fonctions de rendu

```ts
import { h, withDirectives, resolveDirective } from 'vue'

const foo = resolveDirective('foo')            // directive enregistrée globalement
const bar = { mounted() {} }                   // directive locale

return withDirectives(h('div'), [
  [foo, valeur, 'arg', { mod: true }],         // [directive, valeur, argument, modificateurs]
  [bar],
])
```

### 14.9 Pièges fréquents

- Utiliser une directive pour de la logique **réalisable avec un composant ou un composable**.
- Appliquer une directive à un **composant à racines multiples**.
- Oublier le **nettoyage** dans `unmounted`.
- Mémoriser l'état dans une **variable de module** partagée entre éléments.
- Écrire dans l'état réactif Vue sans nécessité depuis une directive (elle doit travailler sur le DOM).
- Se reposer sur une directive pour de la **sécurité** (par exemple `v-can` seulement visuel : le contrôle réel reste côté serveur).

### Synthèse du chapitre 14

`vNom` dans `<script setup>` devient `v-nom` dans le gabarit. Les hooks suivent l'ordre `created` → `beforeMount` → `mounted` → `beforeUpdate` → `updated` → `beforeUnmount` → `unmounted`. `binding` donne `value`, `oldValue`, `arg` et `modifiers`. Réservez les directives à la **manipulation directe du DOM** et **nettoyez** dans `unmounted`.

---

## 15. Plugins

**Objectifs d'apprentissage.** Définir et écrire un plugin Vue ; comprendre `app.use`, `app.config`, `globalProperties` et `provide` ; typer les extensions globales ; accéder aux services depuis `<script setup>` ; connaître la configuration d'application et les autres méthodes de l'instance.

### 15.1 Définition

Un **plugin** est un code **autonome** qui ajoute des fonctionnalités **à l'échelle de l'application**. Il peut :

1. enregistrer des **composants** ou des **directives** globaux (`app.component`, `app.directive`) ;
2. **fournir** des ressources par `app.provide` ;
3. ajouter des **propriétés ou méthodes globales** (`app.config.globalProperties`) ;
4. installer des **comportements transversaux** (routeur, store, internationalisation, notifications).

Exemples officiels : **Vue Router**, **Pinia**, **Vue I18n**. Un plugin est ce qu'on installe avec `app.use(…)` dans `main.ts`.

### 15.2 Écriture d'un plugin

Un plugin est soit un **objet** doté d'une méthode `install(app, options)`, soit directement une **fonction** `(app, options) => void`.

```ts
// src/plugins/i18n.ts
import type { App, InjectionKey } from 'vue'

export interface OptionsI18n {
  messages: Record<string, Record<string, string>>
  locale: string
}
export interface I18n { t: (cle: string) => string }

export const cleI18n: InjectionKey<I18n> = Symbol('i18n')

export default {
  install(app: App, options: OptionsI18n) {
    const t = (cle: string) => options.messages[options.locale]?.[cle] ?? cle

    app.config.globalProperties.$t = t           // accessible dans le gabarit : {{ $t('bonjour') }}
    app.provide(cleI18n, { t })                  // accessible par inject(cleI18n)
  },
}
```

#### Version fonction

```ts
import type { Plugin } from 'vue'

export const monPlugin: Plugin<[options: { debug: boolean }]> = (app, options) => {
  /* … */
}
```

#### Installation

```ts
// src/main.ts
import i18n from './plugins/i18n'

app.use(i18n, { locale: 'fr', messages: { fr: { bonjour: 'Bonjour' } } })
```

`app.use()` **ignore les installations en double** d'un même plugin et **retourne l'application**, ce qui permet de chaîner les appels : `app.use(a).use(b)`.

### 15.3 Typage des extensions globales

```ts
// src/types/vue.d.ts
import 'vue'

declare module 'vue' {
  interface ComponentCustomProperties {
    $t: (cle: string) => string
  }
}
export {}
```

L'ajout à `ComponentCustomProperties` fait connaître `$t` aux gabarits et à l'Options API. Sans cette déclaration, `vue-tsc` signale une propriété inconnue.

### 15.4 Accès depuis `<script setup>`

`globalProperties` n'est **pas** accessible dans `<script setup>` (il n'y a pas de `this`). Utilisez **`provide` / `inject`** (recommandé) ; `getCurrentInstance()` existe mais est **déconseillé** (API interne).

```ts
import { inject } from 'vue'
import { cleI18n } from '@/plugins/i18n'

const i18n = inject(cleI18n)!
i18n.t('bonjour')
```

Une écriture encore plus propre consiste à fournir un composable `useI18n()` qui encapsule `inject` et vérifie sa présence (chapitre 12).

### 15.5 Configuration de l'application (`app.config`)

| Option | Rôle |
| --- | --- |
| `app.config.errorHandler` | Gestionnaire **global** d'erreurs |
| `app.config.warnHandler` | Gestionnaire d'avertissements (développement) |
| `app.config.globalProperties` | Propriétés globales |
| `app.config.performance` | Active le suivi des performances dans les DevTools |
| `app.config.compilerOptions` | Options du compilateur d'exécution (`isCustomElement`, `whitespace`, `delimiters`…) |
| `app.config.optionMergeStrategies` | Stratégies de fusion d'options personnalisées |

```ts
app.config.errorHandler = (err, instance, info) => {
  /* journaliser vers un service de suivi (Sentry, etc.) */
}

app.config.compilerOptions.isCustomElement = (tag) => tag.startsWith('ion-')
```

`errorHandler` est le **dernier filet** : il reçoit les erreurs de rendu, de hooks, d'observateurs et de gestionnaires d'événements qui n'ont été interceptées par aucun `onErrorCaptured`.

### 15.6 Autres méthodes de l'application

| Méthode | Rôle |
| --- | --- |
| `app.mount(cible)` | Monte l'application |
| `app.unmount()` | Démonte l'application |
| `app.provide(cle, valeur)` | Fournit une valeur à tous les composants |
| `app.component(nom, composant)` | Enregistre un composant global |
| `app.directive(nom, directive)` | Enregistre une directive globale |
| `app.mixin(...)` | Mixin global (**déconseillé**) |
| `app.runWithContext(fn)` *(3.3)* | Exécute `fn` dans le contexte de l'application : permet d'appeler `inject` hors composant |
| `app.onUnmount(fn)` *(3.5)* | Enregistre un nettoyage exécuté au démontage de l'application |

### 15.7 Un plugin de notifications (exemple complet)

```ts
// src/plugins/notifications.ts
import { reactive, readonly, type App, type InjectionKey } from 'vue'

export interface Notification { id: number; texte: string; type: 'info' | 'erreur' }
export interface ServiceNotifications {
  liste: readonly Notification[]
  notifier: (texte: string, type?: Notification['type']) => void
}

export const cleNotifications: InjectionKey<ServiceNotifications> = Symbol('notifications')

export default {
  install(app: App) {
    const etat = reactive<Notification[]>([])
    let prochainId = 1

    function notifier(texte: string, type: Notification['type'] = 'info') {
      const id = prochainId++
      etat.push({ id, texte, type })
      setTimeout(() => {
        const i = etat.findIndex((n) => n.id === id)
        if (i >= 0) etat.splice(i, 1)
      }, 4000)
    }

    app.provide(cleNotifications, { liste: readonly(etat), notifier })
  },
}
```

```ts
// src/composables/useNotifications.ts
import { inject } from 'vue'
import { cleNotifications } from '@/plugins/notifications'

export function useNotifications() {
  const service = inject(cleNotifications)
  if (!service) throw new Error("Le plugin de notifications n'est pas installé")
  return service
}
```

### 15.8 Pièges fréquents

- Utiliser `globalProperties` partout : perte de traçabilité, typage manuel. Préférez `provide` / `inject`.
- Oublier le **typage** des extensions globales.
- Appeler `app.use` **après** `mount`.
- Écrire un plugin qui dépend de l'ordre d'installation sans le documenter.
- Utiliser un **état de module** dans un plugin en SSR (partagé entre requêtes) : créez l'état **dans `install`**, à chaque application.

### Synthèse du chapitre 15

Un plugin est un objet avec **`install(app, options)`** (ou une fonction). Préférez **`provide` / `inject`** à `globalProperties` ; typez les extensions par `declare module 'vue'`. `app.config` centralise la configuration globale (erreurs, avertissements, compilateur).

---

## 16. Composants intégrés

**Objectifs d'apprentissage.** Maîtriser `Transition`, `TransitionGroup`, `KeepAlive`, `Teleport` et `Suspense` ; connaître leurs props, classes, hooks et limites ; les combiner (routeur, modales, listes) ; respecter l'accessibilité des animations.

Les composants intégrés sont **disponibles dans tous les gabarits sans enregistrement** et sont **tree-shakables** (absents du bundle s'ils ne sont pas utilisés).

### 16.1 `<Transition>`

`<Transition>` applique des **animations d'entrée et de sortie** à **un seul** élément ou composant lorsqu'il est inséré ou retiré du DOM, par :

- `v-if` ;
- `v-show` ;
- `<component :is>` ;
- un changement de `key`.

```vue
<script setup lang="ts">
import { ref } from 'vue'

const visible = ref(true)
</script>

<template>
  <button @click="visible = !visible">Basculer</button>
  <Transition name="fondu">
    <p v-if="visible">Bonjour</p>
  </Transition>
</template>

<style>
.fondu-enter-active, .fondu-leave-active { transition: opacity 0.5s ease; }
.fondu-enter-from, .fondu-leave-to { opacity: 0; }
</style>
```

#### Les six classes de transition

| Classe | Moment |
| --- | --- |
| `v-enter-from` | Début de l'entrée (retirée à l'image suivante) |
| `v-enter-active` | Pendant toute l'entrée (durée, courbe, délai) |
| `v-enter-to` | Fin de l'entrée (ajoutée à l'image suivante) |
| `v-leave-from` | Début de la sortie |
| `v-leave-active` | Pendant toute la sortie |
| `v-leave-to` | Fin de la sortie |

Le préfixe `v-` est remplacé par la valeur de `name` (`fondu-enter-from`). Sans `name`, le préfixe est `v-`. Des **classes personnalisées** sont possibles (`enter-active-class`, `leave-to-class`…) : pratique avec **Animate.css** ou **Tailwind**.

#### Propriétés

| Prop | Rôle |
| --- | --- |
| `name` | Préfixe des classes |
| `appear` | Applique la transition au **rendu initial** |
| `mode` | `'out-in'` (sortie puis entrée) ou `'in-out'` (entrée puis sortie) |
| `type` | `'transition'` ou `'animation'` : détermine la durée à suivre |
| `duration` | Durées explicites (`500` ou `{ enter: 500, leave: 800 }`) |
| `css` | `false` pour des animations **purement JavaScript** |
| `enter-*-class`, `leave-*-class` | Classes personnalisées |

#### Animations CSS `@keyframes`

```css
.rebond-enter-active { animation: rebond-entree 0.5s; }
.rebond-leave-active { animation: rebond-entree 0.5s reverse; }

@keyframes rebond-entree {
  0%   { transform: scale(0); }
  50%  { transform: scale(1.25); }
  100% { transform: scale(1); }
}
```

#### Hooks JavaScript

```vue
<Transition
  :css="false"
  @before-enter="avantEntree"
  @enter="entree"
  @after-enter="apresEntree"
  @enter-cancelled="entreeAnnulee"
  @before-leave="avantSortie"
  @leave="sortie"
  @after-leave="apresSortie"
  @leave-cancelled="sortieAnnulee"
/>
```

Le hook `@enter` reçoit `(el, done)` : avec `:css="false"`, appelez `done()` pour signaler la fin. Compatible avec **GSAP**, **Motion** et autres bibliothèques d'animation. Avec `:css="false"`, Vue ne cherche pas de classes CSS et ne détermine plus la fin de la transition : appelez `done()` vous-même.

#### Transition entre composants ou vues

```vue
<Transition name="glisse" mode="out-in">
  <component :is="vueActive" />
</Transition>

<RouterView v-slot="{ Component }">
  <Transition name="page" mode="out-in"><component :is="Component" /></Transition>
</RouterView>
```

#### Règles

- **Un seul enfant racine** (pas de liste ; pour une liste, voir `TransitionGroup`).
- Pour une transition **réutilisable**, créez un composant enveloppe avec un slot.
- Changer la **`key`** relance la transition sur un contenu qui reste du même type.
- Respectez **`prefers-reduced-motion`** : supprimez ou réduisez les animations pour les personnes qui le demandent.

```css
@media (prefers-reduced-motion: reduce) {
  .fondu-enter-active, .fondu-leave-active { transition: none; }
}
```

### 16.2 `<TransitionGroup>`

Anime l'**insertion, le retrait et le déplacement** des éléments d'une **liste** (`v-for`).

```vue
<TransitionGroup name="liste" tag="ul">
  <li v-for="item in items" :key="item.id">{{ item.nom }}</li>
</TransitionGroup>

<style>
.liste-move, .liste-enter-active, .liste-leave-active { transition: all 0.5s ease; }
.liste-enter-from, .liste-leave-to { opacity: 0; transform: translateX(30px); }
.liste-leave-active { position: absolute; }      /* permet aux voisins de se repositionner fluidement */
</style>
```

- Rend un **élément conteneur** si la prop `tag` est fournie (sinon, aucun enveloppe n'est ajoutée).
- **Pas de prop `mode`.**
- Chaque enfant **doit avoir une `key`** unique.
- La classe `-move` anime le **déplacement** (technique FLIP).
- Pour des animations **échelonnées**, utilisez des attributs de données et des hooks JavaScript.

### 16.3 `<KeepAlive>`

`<KeepAlive>` **met en cache** les instances de composants dynamiques lorsqu'elles sont désactivées, au lieu de les détruire : l'**état** (saisies, défilement, données chargées) est conservé.

```vue
<KeepAlive>
  <component :is="vueActive" />
</KeepAlive>
```

#### Props

| Prop | Rôle |
| --- | --- |
| `include` | Chaîne, expression régulière ou tableau : noms des composants **mis en cache** |
| `exclude` | Noms des composants **non** mis en cache |
| `max` | Nombre maximal d'instances en cache (stratégie **LRU** : la moins récemment utilisée est évincée) |

```vue
<KeepAlive :include="['VueA', 'VueB']" :max="10">
  <component :is="vue" />
</KeepAlive>
```

- Le nom provient de l'option `name` (`defineOptions({ name: 'VueA' })`) ou du nom de fichier inféré pour les SFC.
- Hooks : **`onActivated`** et **`onDeactivated`** (chapitre 9).
- `KeepAlive` n'accepte qu'**un seul composant enfant direct** (pas un élément DOM).

### 16.4 `<Teleport>`

`<Teleport>` rend une partie du gabarit **ailleurs dans le DOM**, tout en conservant la **hiérarchie logique** : props, événements et `provide` / `inject` continuent de fonctionner comme si le contenu était resté en place.

```vue
<button @click="ouvert = true">Ouvrir</button>

<Teleport to="body">
  <div v-if="ouvert" class="modale">
    <p>Contenu de la modale</p>
    <button @click="ouvert = false">Fermer</button>
  </div>
</Teleport>
```

#### Props

| Prop | Rôle |
| --- | --- |
| `to` | Sélecteur CSS ou élément DOM cible (doit **exister au montage**) |
| `disabled` | Désactive la téléportation (rendu à l'emplacement d'origine) |
| `defer` *(3.5)* | Résout `to` **après** le montage du reste de l'application (cible rendue plus tard) |

- Plusieurs `<Teleport>` peuvent viser la **même cible** : leur contenu s'ajoute dans l'ordre de montage.
- Usage : **modales, popovers, notifications, infobulles**. Cela évite les problèmes de `z-index`, d'`overflow` et de `transform` hérités des ancêtres.
- En **SSR**, la cible doit se trouver **hors** du conteneur de l'application, ou on utilise un marqueur spécifique (chapitre 24).

### 16.5 `<Suspense>` *(expérimental)*

`<Suspense>` orchestre les **dépendances asynchrones** dans l'arbre de composants et affiche un **état d'attente** (*fallback*) jusqu'à leur résolution.

**Dépendances asynchrones détectées :**

1. composants avec **`async setup()`** ou **`await` de premier niveau** dans `<script setup>` ;
2. **composants asynchrones** (`defineAsyncComponent`), sauf avec l'option `suspensible: false`.

```vue
<Suspense>
  <template #default>
    <ComposantAsynchrone />
  </template>
  <template #fallback>
    Chargement…
  </template>
</Suspense>
```

#### Événements et props

- Événements : `@pending` (entrée en attente), `@resolve` (contenu prêt), `@fallback` (affichage du repli).
- Props : `timeout` (délai avant d'afficher le repli après un changement de contenu) ; `suspensible` côté composants asynchrones.

#### Gestion d'erreurs

`<Suspense>` ne gère pas les rejets : combinez-le avec **`onErrorCaptured`** pour afficher un état d'erreur.

```vue
<RouterView v-slot="{ Component }">
  <Suspense><component :is="Component" /></Suspense>
</RouterView>
```

> **API expérimentale.** Son interface peut évoluer ; consultez la documentation avant de l'adopter. Nuxt l'utilise pour la navigation asynchrone.

### 16.6 Éléments spéciaux du gabarit

| Composant / élément | Usage |
| --- | --- |
| `<component :is>` | Composants dynamiques |
| `<slot>` | Emplacement |
| `<template>` | Groupement invisible |

### 16.7 Pièges fréquents

- `Transition` avec **plusieurs** éléments racines.
- Oublier `key` dans `TransitionGroup`.
- Utiliser `KeepAlive` sans `max` (fuite de mémoire) ou sans nom de composant exploitable.
- `Teleport` vers une cible **inexistante** au montage : utilisez `defer` ou créez la cible plus tôt.
- Oublier `done()` dans un hook `@enter` ou `@leave` avec `:css="false"`.
- Transitionner une propriété coûteuse (`height`, `top`) : privilégiez `transform` et `opacity`.

### Synthèse du chapitre 16

`Transition` (un élément), `TransitionGroup` (listes), `KeepAlive` (cache), `Teleport` (rendu ailleurs dans le DOM) et `Suspense` (asynchrone, **expérimental**). Six classes de transition et des hooks JavaScript offrent un contrôle fin ; respectez `prefers-reduced-motion`.

---

# Partie III — Écosystème officiel

## 17. Vue Router

**Objectifs d'apprentissage.** Installer et configurer **Vue Router** ; définir des routes (statiques, dynamiques, imbriquées, nommées, avec redirections et alias) ; naviguer par liens et par code ; lire paramètres, requêtes et métadonnées ; protéger la navigation avec des **gardes** ; charger paresseusement ; contrôler le défilement ; gérer dynamiquement les routes ; typer le routeur ; connaître le routage par fichiers et la récupération de données.

### 17.1 Qu'est-ce que Vue Router ?

**Vue Router** est le routeur **officiel** de Vue : il associe des **URL** à des **composants** dans une application monopage, **sans recharger la page**, grâce à l'API History du navigateur (ou au *hash*).

```bash
npm install vue-router
```

> **Version.** **Vue Router 5** est une version de transition : elle intègre dans le paquet principal le **routage par fichiers** (ancien `unplugin-vue-router`) et reste **sans changement incompatible** pour qui utilisait Vue Router 4 sans ce plugin (la mise à jour se limite à `npm update vue-router`). L'API présentée dans ce chapitre est valable pour les versions 4 et 5.

### 17.2 Configuration de base

```ts
// src/router/index.ts
import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import VueAccueil from '@/views/VueAccueil.vue'

const routes: RouteRecordRaw[] = [
  { path: '/', name: 'accueil', component: VueAccueil },
  { path: '/a-propos', name: 'apropos', component: () => import('@/views/VueAPropos.vue') },   // chargement paresseux
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
```

```ts
// src/main.ts
app.use(router)
```

```vue
<!-- src/App.vue -->
<template>
  <nav>
    <RouterLink to="/">Accueil</RouterLink>
    <RouterLink :to="{ name: 'apropos' }">À propos</RouterLink>
  </nav>
  <RouterView />
</template>
```

#### Modes d'historique

| Fonction | URL | Remarques |
| --- | --- | --- |
| `createWebHistory()` | `/utilisateurs/1` | URL propres ; le serveur doit **renvoyer `index.html`** pour toute URL inconnue (repli) |
| `createWebHashHistory()` | `/#/utilisateurs/1` | Aucune configuration serveur ; URL moins propres, moins bon pour le SEO |
| `createMemoryHistory()` | — | Rendu serveur (SSR) et tests |

> **Déploiement.** Avec `createWebHistory`, un rechargement sur `/utilisateurs/1` renvoie une erreur 404 si le serveur n'est pas configuré pour retourner `index.html`. Prévoyez la règle de repli sur votre hébergeur.

### 17.3 `RouterLink` et `RouterView`

#### `RouterLink`

Lien de navigation **sans rechargement de page** ; il ajoute automatiquement deux classes : **`router-link-active`** (correspondance partielle) et **`router-link-exact-active`** (correspondance exacte).

Props : `to`, `replace`, `active-class`, `exact-active-class`, `custom` avec un slot `v-slot` (`href`, `navigate`, `isActive`, `isExactActive`).

#### `RouterView`

Affiche le composant qui correspond à la route courante. Props : **`name`** (vues nommées) et **`route`**. Son slot `v-slot="{ Component, route }"` permet de l'envelopper dans `Transition`, `KeepAlive` ou `Suspense`.

### 17.4 Routes dynamiques et paramètres

```ts
{ path: '/users/:id', name: 'utilisateur', component: VueUtilisateur, props: true }
```

```vue
<script setup lang="ts">
import { useRoute } from 'vue-router'

const route = useRoute()
route.params.id           // string | string[]
</script>
```

#### Paramètres avancés

| Syntaxe | Signification |
| --- | --- |
| `/users/:id` | Paramètre obligatoire |
| `/users/:id?` | Optionnel |
| `/fichiers/:chemin*` | Zéro segment ou plus |
| `/fichiers/:chemin+` | Un segment ou plus |
| `/users/:id(\\d+)` | Avec **expression régulière** (ici un nombre) |
| `/:pathMatch(.*)*` | **Fourre-tout** (page 404) |

#### Réagir au changement de paramètre

Pour passer de `/users/1` à `/users/2`, le **même composant est réutilisé** (il n'est ni détruit ni recréé) : `onMounted` ne se redéclenche pas. Réagissez par `watch(() => route.params.id, …)` ou par le garde `onBeforeRouteUpdate`.

#### Props de route

```ts
{ path: '/users/:id', component: VueUtilisateur, props: true }                         // params vers props
{ path: '/recherche', component: Recherche, props: (route) => ({ q: route.query.q }) } // fonction
{ path: '/statique', component: Statique, props: { nom: 'x' } }                        // objet
```

Passer les paramètres en **props** découple le composant du routeur : il devient réutilisable et plus facile à tester.

### 17.5 Routes imbriquées

```ts
{
  path: '/utilisateur/:id',
  component: MiseEnPageUtilisateur,                    // contient un <RouterView />
  children: [
    { path: '', component: AccueilUtilisateur },       // /utilisateur/:id
    { path: 'profil', component: ProfilUtilisateur },  // /utilisateur/:id/profil
    { path: 'articles', component: ArticlesUtilisateur },
  ],
}
```

- Un chemin enfant **sans `/` initial** est relatif à celui du parent ; avec `/` initial, il est absolu.
- Un enfant avec `path: ''` constitue la route **par défaut** du parent.
- Chaque niveau d'imbrication correspond à un **`<RouterView>`** supplémentaire dans le composant parent.

### 17.6 Routes nommées, redirections et alias

```ts
{ path: '/accueil', redirect: '/' }
{ path: '/ancien', redirect: { name: 'accueil' } }
{ path: '/x', redirect: (to) => ({ path: '/y', query: { q: to.params.q as string } }) }
{ path: '/', component: Accueil, alias: ['/home', '/accueil'] }   // alias : URL différente, même rendu
```

Une **redirection** change l'URL affichée ; un **alias** conserve l'URL tapée tout en affichant la même vue. Préférez les **routes nommées** pour naviguer : changer un chemin n'oblige pas à modifier tous les liens.

### 17.7 Navigation programmatique

```ts
import { useRouter } from 'vue-router'

const router = useRouter()

router.push('/users/1')
router.push({ name: 'utilisateur', params: { id: 1 }, query: { onglet: 'articles' }, hash: '#haut' })
router.replace({ path: '/' })          // remplace l'entrée courante de l'historique
router.go(-1); router.back(); router.forward()
```

- `push` retourne une **promesse** : la navigation peut échouer (`NavigationFailure`).
- Les `params` ne se combinent **pas** avec `path` : utilisez `name`.

```ts
import { isNavigationFailure, NavigationFailureType } from 'vue-router'

const echec = await router.push('/x')
if (isNavigationFailure(echec, NavigationFailureType.duplicated)) { /* déjà sur cette route */ }
```

#### `useRoute`, `useRouter`, `useLink`

- **`useRoute()`** : la route courante **réactive** (`path`, `params`, `query`, `hash`, `name`, `meta`, `matched`, `fullPath`).
- **`useRouter()`** : l'instance du routeur (navigation, `addRoute`, `removeRoute`, `hasRoute`, `getRoutes`, gardes).
- **`useLink(props)`** : la logique de `RouterLink`, pour créer des liens personnalisés.

> **Ne déstructurez pas `useRoute()`** : la réactivité serait perdue. Utilisez `toRefs(route)` ou `computed(() => route.params.id)`.

### 17.8 Vues nommées

```ts
{ path: '/', components: { default: Principal, barre: BarreLaterale, entete: Entete } }
```

```vue
<RouterView name="entete" />
<RouterView />
<RouterView name="barre" />
```

### 17.9 Gardes de navigation

Les **gardes** contrôlent la navigation : authentification, permissions, confirmation, chargement de données.

#### Valeurs retournées par un garde

| Retour | Effet |
| --- | --- |
| `undefined` ou `true` | Autorise la navigation |
| `false` | **Annule** la navigation |
| `'/chemin'` ou `{ name: 'connexion' }` | **Redirige** |
| `Error` | Annule et déclenche `router.onError` |

> Les gardes utilisent le **retour de valeur** ; l'ancien paramètre `next()` n'est plus nécessaire (il reste possible, mais ne l'appelez pas deux fois).

#### Gardes globaux

```ts
router.beforeEach(async (to, from) => {
  const auth = useAuthStore()                                       // appelé DANS le garde, après app.use(pinia)
  if (to.meta.requiresAuth && !auth.estConnecte) {
    return { name: 'connexion', query: { redirect: to.fullPath } }
  }
})

router.beforeResolve(async (to) => { /* après les gardes de composants, avant la confirmation */ })
router.afterEach((to, from, echec) => { /* statistiques, titre de page… (pas de redirection possible) */ })
```

#### Garde par route

```ts
{ path: '/admin', component: Admin, beforeEnter: (to, from) => (estAdmin() ? true : '/') }
```

#### Gardes de composant (Composition API)

```ts
import { onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'

onBeforeRouteLeave((to, from) => {
  if (modifie.value && !confirm('Quitter sans enregistrer ?')) return false
})

onBeforeRouteUpdate(async (to, from) => { /* même composant, paramètres modifiés */ })
```

#### Ordre complet de résolution

1. La navigation est déclenchée.
2. `beforeRouteLeave` (composants désactivés).
3. `beforeEach` (globaux).
4. `beforeRouteUpdate` (composants réutilisés).
5. `beforeEnter` (dans les routes).
6. Résolution des composants asynchrones.
7. `beforeRouteEnter` (Options API).
8. `beforeResolve` (globaux).
9. La navigation est **confirmée**.
10. `afterEach`.
11. Mise à jour du DOM.

### 17.10 Métadonnées (`meta`) et typage

```ts
{ path: '/admin', component: Admin, meta: { requiresAuth: true, roles: ['admin'], titre: 'Administration' } }
```

```ts
// src/router/types.d.ts
import 'vue-router'

declare module 'vue-router' {
  interface RouteMeta {
    requiresAuth?: boolean
    roles?: string[]
    titre?: string
  }
}
export {}
```

`to.matched.some((r) => r.meta.requiresAuth)` vérifie aussi les routes **parentes** : `to.meta` ne fusionne que les métadonnées de la route finale (et des parents, qui sont **fusionnés** de façon superficielle), alors que `matched` expose chaque niveau.

### 17.11 Comportement de défilement

```ts
const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) return savedPosition                       // retour arrière du navigateur
    if (to.hash) return { el: to.hash, behavior: 'smooth' }       // ancre
    return { top: 0 }
  },
})
```

### 17.12 Chargement paresseux et découpage du code

```ts
component: () => import('@/views/VueAdmin.vue')
```

Chaque `import()` dynamique produit un **fragment** (*chunk*) chargé à la première visite de la route. Pour regrouper des routes dans un même fragment, utilisez les options `manualChunks` de Rollup dans la configuration Vite (chapitre 23).

### 17.13 Gestion dynamique des routes

```ts
router.addRoute({ path: '/nouvelle', name: 'nouvelle', component: X })
router.addRoute('parent', { path: 'enfant', component: Y })        // sous une route nommée
router.removeRoute('nouvelle')
router.hasRoute('nouvelle')
router.getRoutes()
```

Utile pour ajouter des routes **selon les permissions** de l'utilisateur ou pour des modules chargés à la demande.

### 17.14 Récupération de données

- **Après la navigation** : on affiche la vue immédiatement et on charge les données dans le composant (`watch` sur les paramètres, `Suspense`) ; l'utilisateur voit un état de chargement.
- **Avant la navigation** : on charge dans un garde (`beforeEnter`) ; l'utilisateur reste sur la page précédente jusqu'à la fin.
- **Chargeurs de données** : Vue Router 5 propose des **chargeurs expérimentaux** (`vue-router/experimental`), avec une variante fondée sur **Pinia Colada** pour la mise en cache ; leur API peut évoluer.
- Bibliothèques : **TanStack Query**, **Pinia Colada**, **Nuxt** (`useFetch` / `useAsyncData`).

### 17.15 Autres notions

- **Routage par fichiers** : les routes sont générées à partir de l'arborescence `src/pages/` et **typées** (intégré à Vue Router 5 ; auparavant `unplugin-vue-router`) ; c'est aussi le modèle de **Nuxt**.
- **Accessibilité** : après une navigation, déplacez le **focus** (ou annoncez le changement de page à un lecteur d'écran) ; mettez à jour le **titre** du document.
- **Transitions de page** : `Transition` autour de `RouterView` (chapitre 16).
- **Erreurs de navigation** : `router.onError`.
- **`router.isReady()`** : attend la résolution de la navigation initiale (SSR).
- **Base d'URL** : argument de `createWebHistory(base)`.

### 17.16 Pièges fréquents

- Oublier la **configuration du serveur** pour `createWebHistory` (erreur 404 au rechargement).
- **Déstructurer** `useRoute()`.
- Oublier que le composant est **réutilisé** quand seuls les paramètres changent.
- Boucles de redirection dans `beforeEach` (rediriger vers une route elle-même protégée).
- Utiliser `params` avec `path`.
- Appeler `useAuthStore()` au **niveau du module** du routeur, avant l'installation de Pinia.
- Croire que le contrôle d'accès du routeur est une **sécurité** : le serveur doit aussi autoriser.

### Synthèse du chapitre 17

`createRouter`, `RouterLink` et `RouterView` forment le socle. Les routes peuvent être **dynamiques, imbriquées et nommées** ; les **gardes**, les **métadonnées** et le **chargement paresseux** complètent le tout. `useRoute` lit la route (de façon réactive), `useRouter` navigue. Vue Router 5 intègre le **routage par fichiers** sans casser l'API existante.

---

## 18. Pinia (gestion d'état)

**Objectifs d'apprentissage.** Comprendre le rôle d'un **store** et savoir quand l'utiliser ; définir des stores (**Setup** et **Option**) ; consommer l'état, les getters et les actions avec `storeToRefs` ; modifier l'état (`$patch`, `$reset`) ; observer un store (`$subscribe`, `$onAction`) ; composer des stores ; typer ; écrire des plugins ; utiliser Pinia hors composants, en SSR et dans les tests.

### 18.1 Qu'est-ce que Pinia ?

**Pinia** est la bibliothèque **officielle** de gestion d'état de Vue (successeur de **Vuex**). Elle fournit un **état global réactif** partagé entre composants, avec un support **TypeScript** natif, l'intégration aux **DevTools**, le **remplacement à chaud** (HMR) et le **SSR**.

```bash
npm install pinia
```

```ts
// src/main.ts
import { createPinia } from 'pinia'

app.use(createPinia())
```

> **Version.** Pinia 3 est une version « tranquille » : elle supprime les API dépréciées et le support de Vue 2, sans nouvelle fonctionnalité majeure. Le code de ce chapitre fonctionne avec les versions 2 et 3 de Pinia sous Vue 3.

#### Quand utiliser un store ?

- État partagé par **plusieurs composants éloignés** dans l'arbre (utilisateur connecté, panier, préférences).
- État qui doit **survivre à la navigation**.
- **Logique métier** et communication avec l'API centralisées et testables.

> Un état **local** à un composant, ou à un sous-arbre, reste dans le composant ou dans `provide` / `inject`. Mettre tout l'état dans un store est un anti-modèle.

#### Pinia et Vuex

| | **Vuex 4** | **Pinia** |
| --- | --- | --- |
| Mutations | **Obligatoires** | **Supprimées** (les actions suffisent) |
| Modules | Imbriqués, avec espaces de noms | Un store = un module, **à plat** |
| TypeScript | Complexe | **Natif** |
| API | Options | Options **ou** Setup (Composition) |
| Statut | Mode maintenance | **Recommandé** |

### 18.2 Définir un store

`defineStore(id, définition)` crée un store ; l'**`id` doit être unique** dans l'application. Convention de nommage : **`useXxxStore`**.

#### Setup Store *(recommandé)*

```ts
// src/stores/compteur.ts
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCompteurStore = defineStore('compteur', () => {
  // état = ref / reactive
  const count = ref(0)
  const nom = ref('Compteur')

  // getters = computed
  const double = computed(() => count.value * 2)

  // actions = fonctions
  function incrementer() { count.value++ }
  async function chargerInitial() {
    count.value = await api.recupererCompteur()
  }

  return { count, nom, double, incrementer, chargerInitial }    // tout ce qui doit être public
})
```

> En Setup Store, **retournez toutes** les propriétés d'état pour que Pinia les reconnaisse (SSR, DevTools, plugins). N'utilisez pas de propriétés d'état **privées**.

#### Option Store

```ts
export const useUtilisateurStore = defineStore('utilisateur', {
  state: () => ({
    nom: '',
    age: 0,
    roles: [] as string[],
  }),
  getters: {
    majeur: (state) => state.age >= 18,
    nomMajuscule(): string { return this.nom.toUpperCase() },     // `this` : annotez le type de retour
  },
  actions: {
    async charger(id: number) {
      const u = await api.getUtilisateur(id)
      this.nom = u.nom
      this.age = u.age
    },
    reinitialiser() { this.$reset() },
  },
})
```

| Option Store | Setup Store |
| --- | --- |
| `state` | `ref` / `reactive` |
| `getters` | `computed` |
| `actions` | fonctions |

Le **Setup Store** est plus flexible (observateurs, composables, injection) et reprend les conventions de la Composition API ; l'**Option Store** est plus proche de Vuex et d'une lecture rapide.

### 18.3 Utiliser un store

```vue
<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { useCompteurStore } from '@/stores/compteur'

const store = useCompteurStore()                    // objet réactif

// État et getters : storeToRefs conserve la réactivité
const { count, double } = storeToRefs(store)

// Actions : déstructuration directe (fonctions déjà liées au store)
const { incrementer } = store

// const { count } = store   → perd la réactivité !
</script>

<template>
  <button @click="incrementer">{{ count }} (x2 = {{ double }})</button>
</template>
```

- Le store est **instancié à la première utilisation** (paresseux).
- Appelez `useXxxStore()` **après** `app.use(pinia)`, dans `setup`, un garde, une action…
- Hors composant (par exemple dans le routeur), appelez `useXxxStore()` **à l'intérieur** de la fonction (garde), jamais au niveau du module.

### 18.4 Modifier l'état

```ts
store.count++                                              // 1. modification directe
store.$patch({ count: store.count + 1, nom: 'x' })         // 2. $patch avec un objet (fusion)
store.$patch((state) => {                                  // 3. $patch avec une fonction (collections)
  state.items.push({ nom: 'A' })
})
store.$state = { count: 0, nom: '' }                       // 4. remplacement (Option Store)
store.$reset()                                             // 5. réinitialisation (Option Store)
```

`$patch` **regroupe** les modifications (une seule entrée dans les DevTools). Pour des tableaux et objets, la forme fonctionnelle évite de recréer l'ensemble de la collection.

#### Réinitialisation en Setup Store

```ts
function $reset() { count.value = 0 }      // à écrire manuellement
// ou utiliser un plugin qui l'implémente pour tous les stores
```

### 18.5 Observer un store

#### `$subscribe`

```ts
store.$subscribe((mutation, state) => {
  // mutation.type : 'direct' | 'patch object' | 'patch function'
  // mutation.storeId ; mutation.events (développement)
  localStorage.setItem('compteur', JSON.stringify(state))
}, { detached: true })            // detached : l'abonnement survit au démontage du composant
```

#### `$onAction`

```ts
const desabonner = store.$onAction(({ name, store, args, after, onError }) => {
  const debut = Date.now()
  after((resultat) => console.log(`${name} OK en ${Date.now() - debut} ms`))
  onError((erreur) => console.warn(`${name} en échec`, erreur))
})
```

`$onAction` intercepte **chaque action** (avant, après, en cas d'erreur) : idéal pour la journalisation et la mesure. Le `watch` classique fonctionne aussi : `watch(() => store.count, …)`.

### 18.6 Composer des stores

```ts
export const usePanierStore = defineStore('panier', () => {
  const utilisateur = useUtilisateurStore()                  // un store en utilise un autre
  const articles = ref<Article[]>([])
  const total = computed(() => articles.value.reduce((s, a) => s + a.prix, 0))
  const peutCommander = computed(() => utilisateur.estConnecte && articles.value.length > 0)
  return { articles, total, peutCommander }
})
```

**Évitez les dépendances circulaires** entre stores : ne lisez l'autre store que dans des actions ou des getters, jamais au niveau de la configuration lors de l'initialisation.

### 18.7 Actions asynchrones

```ts
actions: {
  async charger() {
    this.chargement = true
    try { this.items = await api.getItems() }
    catch (e) { this.erreur = e as Error }
    finally { this.chargement = false }
  },
}
```

Les actions peuvent `await`, appeler d'autres stores et retourner des valeurs. Modélisez explicitement l'état de chargement (`chargement`, `erreur`) pour que les composants affichent les cas « en cours » et « en échec ».

### 18.8 Typage

- **Setup Store** : les types sont **inférés** depuis `ref<T>()`, `computed` et les fonctions.
- **Option Store** : typez l'état (`state: () => ({ x: [] as string[] })`) et annotez le **type de retour** des getters qui utilisent `this`.
- Types utiles : `StoreDefinition`, `Store`, `_GettersTree`, `PiniaPluginContext`.

```ts
import type { Store } from 'pinia'

type CompteurStore = ReturnType<typeof useCompteurStore>
```

### 18.9 Plugins Pinia

```ts
import { createPinia, type PiniaPluginContext } from 'pinia'

function monPlugin({ store, options, app, pinia }: PiniaPluginContext) {
  store.$onAction(({ name }) => console.log('action', name))
  return { creeLe: new Date() }          // propriétés ajoutées à chaque store
}

const pinia = createPinia()
pinia.use(monPlugin)
```

Plugin répandu : **pinia-plugin-persistedstate** (persistance dans `localStorage`). Typage des ajouts :

```ts
declare module 'pinia' {
  export interface PiniaCustomProperties { creeLe: Date }
  export interface DefineStoreOptionsBase<S, Store> { persist?: boolean }
}
```

### 18.10 Pinia hors composants et en SSR

```ts
// Hors composant : fournissez l'instance de Pinia
const pinia = createPinia()
const store = useUtilisateurStore(pinia)

// Garde de routeur : appel à l'intérieur
router.beforeEach(() => {
  const auth = useAuthStore()
  /* … */
})
```

**SSR** : créez **une instance de Pinia par requête** ; l'état est **sérialisé** (`pinia.state.value`) côté serveur, puis **hydraté** côté client. Avec Nuxt, utilisez le module `@pinia/nuxt`.

### 18.11 Tests

```ts
import { setActivePinia, createPinia } from 'pinia'
import { describe, it, expect, beforeEach } from 'vitest'
import { useCompteurStore } from '@/stores/compteur'

beforeEach(() => setActivePinia(createPinia()))          // instance neuve pour chaque test

describe('compteur', () => {
  it('incrémente', () => {
    const s = useCompteurStore()
    s.incrementer()
    expect(s.count).toBe(1)
  })
})
```

Pour tester des **composants** : `createTestingPinia({ createSpy: vi.fn, initialState: {…}, stubActions: false })` du paquet `@pinia/testing` (chapitre 22).

### 18.12 DevTools

Les Vue DevTools permettent d'inspecter l'état des stores, de **voyager dans le temps** (*time travel*), de modifier l'état à chaud, de suivre les actions et de bénéficier du HMR des stores.

### 18.13 Pièges fréquents

- **Déstructurer** l'état sans `storeToRefs`.
- Appeler `useStore()` **avant** `app.use(pinia)`.
- Oublier de **retourner** une propriété d'état en Setup Store.
- Stocker **tout** l'état dans Pinia (état local inutilement global).
- Modifier l'état **depuis partout** (perte de traçabilité) : préférez des **actions**.
- En SSR, utiliser un état de **module** partagé entre requêtes.
- Stocker des données **non sérialisables** (instances de classe, fonctions) dans l'état, ce qui casse la sérialisation SSR et les DevTools.

### Synthèse du chapitre 18

Un store, c'est **état + getters + actions** ; le **Setup Store** est recommandé. Utilisez **`storeToRefs`** pour l'état et les getters, et déstructurez les actions directement. `$patch`, `$reset`, `$subscribe`, `$onAction` et les plugins complètent l'API. Pinia n'a **pas de mutations**, offre un typage natif et gère le SSR comme les tests.

---

## 19. TypeScript avancé avec Vue

**Objectifs d'apprentissage.** Typer **tous** les éléments d'un composant Vue (état, props, événements, `defineModel`, slots, `provide` / `inject`, références de gabarit, événements DOM) ; utiliser les **types utilitaires** de Vue ; écrire des **composants génériques** ; étendre les types globaux par **augmentation de modules** ; typer les variables d'environnement et les données d'API ; diagnostiquer les problèmes de typage courants.

### 19.1 Vue d'ensemble du support TypeScript

Vue 3 est **écrit en TypeScript** et fournit ses **définitions de types**. Deux niveaux de vérification coexistent :

| Niveau | Outil | Portée |
| --- | --- | --- |
| **Éditeur** | *Vue - Official* (Volar) | Temps réel dans les fichiers `.vue` |
| **Ligne de commande / CI** | `vue-tsc` | Vérifie les `.ts`, les `.vue` et leurs **gabarits** |

Les **gabarits sont eux aussi vérifiés** : prop inconnue, événement mal typé, variable inexistante sont détectés par `vue-tsc` et par l'éditeur.

**Options recommandées** : `"strict": true`, `"verbatimModuleSyntax": true` (imports de types par `import type`), et la version de TypeScript **du projet** dans l'éditeur (plus besoin de l'ancien mode « Take Over » de Volar).

### 19.2 Typer l'état réactif

```ts
import { ref, reactive, computed, shallowRef, type Ref, type ComputedRef } from 'vue'

// ref
const n = ref(0)                              // Ref<number>
const s = ref<string | null>(null)            // Ref<string | null>
const u = ref<Utilisateur>()                  // Ref<Utilisateur | undefined>
const liste = ref<Item[]>([])                 // Ref<Item[]>

// reactive : typer par une interface
interface Etat { compteur: number; utilisateur: Utilisateur | null }
const etat = reactive<Etat>({ compteur: 0, utilisateur: null })

// computed
const double = computed(() => n.value * 2)                    // type inféré
const label = computed<string>(() => `Total : ${n.value}`)    // type explicite

// Annoter des variables
const r: Ref<number> = ref(0)
const c: ComputedRef<number> = computed(() => r.value)
```

**Règle d'inférence.** Laissez TypeScript **inférer** quand l'initialisation est suffisante (`ref(0)`) ; ajoutez un **générique** quand elle ne l'est pas (`ref<'a' | 'b'>('a')`, `ref<Item[]>([])`, `ref<T | null>(null)`).

#### `UnwrapRef`

`ref<T>()` retourne `Ref<UnwrapRef<T>>` : les `ref` imbriqués sont **déballés au niveau du type**, comme à l'exécution.

```ts
const x = ref({ a: ref(1) })      // x.value.a est de type number (et non Ref<number>)
```

### 19.3 Typer les props

#### Approche par types *(recommandée)*

```vue
<script setup lang="ts">
interface Props {
  titre: string
  compteur?: number
  couleur: 'rouge' | 'vert'
  items: Array<{ id: number; nom: string }>
  onFermer?: () => void               // prop de type fonction (mais préférez emit)
}

const props = defineProps<Props>()
</script>
```

Valeurs par défaut :

```ts
const props = withDefaults(defineProps<Props>(), {
  compteur: 0,
  items: () => [],
})

// 3.5+ : déstructuration avec valeur par défaut
const { compteur = 0, items = [] } = defineProps<Props>()
```

#### Approche à l'exécution avec inférence

```ts
const props = defineProps({
  titre: { type: String, required: true },
  items: { type: Array as PropType<Item[]>, default: () => [] },
})
```

#### Types complexes

```ts
import type { PropType } from 'vue'

defineProps({
  utilisateur: { type: Object as PropType<Utilisateur>, required: true },
  rappel: Function as PropType<(id: number) => void>,
})
```

#### Props booléennes

Avec la syntaxe par types, `disabled?: boolean` est converti en `Boolean` à l'exécution : le **cast booléen** s'applique (`<Composant disabled />`).

#### Limites de l'analyse statique

Le compilateur doit pouvoir **résoudre** le type de `defineProps<T>()`. Les types **importés**, **intersections**, **unions simples**, `Pick`, `Omit` et `Partial` sont supportés ; certains **types conditionnels complexes** ne le sont pas.

### 19.4 Typer les événements (`defineEmits`)

```ts
const emit = defineEmits<{
  changer: [valeur: number]
  soumettre: [payload: { email: string; mdp: string }]
  fermer: []
}>()

emit('changer', 42)         // correct
emit('changer', 'x')        // erreur de type
emit('inconnu')             // erreur : événement non déclaré
```

Syntaxe par signatures :

```ts
const emit = defineEmits<{
  (e: 'changer', valeur: number): void
  (e: 'fermer'): void
}>()
```

Côté **parent**, le type du paramètre du gestionnaire est **inféré** :

```vue
<Enfant @changer="(v) => console.log(v.toFixed(2))" />      <!-- v : number -->
```

### 19.5 Typer `defineModel`

```ts
const modele = defineModel<string>()                          // Ref<string | undefined>
const requis = defineModel<string>({ required: true })        // Ref<string>
const nombre = defineModel<number>('compteur', { default: 0 })
const [valeur, modificateurs] = defineModel<string, 'trim' | 'capitalize'>()
```

### 19.6 Typer les slots

```vue
<script setup lang="ts" generic="T">
defineProps<{ items: T[] }>()

defineSlots<{
  default(props: { item: T; index: number }): any
  vide?(props: {}): any
}>()
</script>
```

### 19.7 Typer `provide` et `inject`

```ts
import type { InjectionKey } from 'vue'

export const CleConfig: InjectionKey<{ debug: boolean }> = Symbol('config')

provide(CleConfig, { debug: true })         // type vérifié
const cfg = inject(CleConfig)               // { debug: boolean } | undefined
```

### 19.8 Typer les références de gabarit

```ts
// Élément DOM
const input = ref<HTMLInputElement | null>(null)
const input2 = useTemplateRef<HTMLInputElement>('i')          // 3.5+

// Instance de composant
import MonComposant from './MonComposant.vue'
const comp = ref<InstanceType<typeof MonComposant> | null>(null)
comp.value?.methodeExposee()

// Composant générique
import type { ComponentExposed } from 'vue-component-type-helpers'
const gen = ref<ComponentExposed<typeof MonGenerique> | null>(null)
```

> L'instance n'expose que ce que déclare **`defineExpose`** : le type reflète cet objet. Le type utilitaire `ComponentInstance<typeof C>` est l'alias moderne d'`InstanceType<typeof C>` pour les composants.

### 19.9 Typer les événements du DOM

```ts
function onInput(e: Event) { const el = e.target as HTMLInputElement }
function onKey(e: KeyboardEvent) {}
function onClick(e: MouseEvent) {}
function onDrop(e: DragEvent) {}
function onSubmit(e: SubmitEvent) {}
function onChange(e: Event) {}
```

Dans le gabarit, `$event` est typé **automatiquement** dans un gestionnaire en ligne (`@input="(e) => …"`).

### 19.10 Types utilitaires de Vue

```ts
import type {
  Ref, ComputedRef, ShallowRef, WritableComputedRef,
  UnwrapRef, MaybeRef, MaybeRefOrGetter, ToRefs,
  Component, DefineComponent, PropType, ExtractPropTypes, ExtractPublicPropTypes,
  ComponentPublicInstance, ComponentInstance,
  InjectionKey, VNode, VNodeChild, Slot, Slots,
  Directive, DirectiveBinding, Plugin, App,
  StyleValue, CSSProperties, HTMLAttributes, ButtonHTMLAttributes, InputHTMLAttributes,
  FunctionalComponent, WatchSource, WatchCallback, WatchOptions,
} from 'vue'
```

| Type | Usage |
| --- | --- |
| `MaybeRef<T>` / `MaybeRefOrGetter<T>` | Paramètres de composables |
| `Component` | Prop qui accepte n'importe quel composant |
| `DefineComponent` | Type d'un composant défini |
| `ExtractPropTypes<typeof props>` | Type des props **internes** (valeurs par défaut appliquées) |
| `ExtractPublicPropTypes<…>` | Type des props **publiques** (côté parent) |
| `ComponentInstance<typeof C>` | Alias moderne de `InstanceType<typeof C>` |
| `StyleValue` | Type d'une prop `style` |

#### Hériter des attributs HTML natifs

```ts
import type { InputHTMLAttributes } from 'vue'

interface Props extends /* @vue-ignore */ InputHTMLAttributes { label: string }
```

Le commentaire `@vue-ignore` indique au compilateur de ne pas tenter de résoudre ce type pour la déclaration d'exécution des props, tout en gardant le typage dans l'éditeur.

### 19.11 Composants génériques

```vue
<script setup lang="ts" generic="T extends { id: string | number }, K extends keyof T">
const props = defineProps<{
  items: T[]
  cle: K
}>()

const emit = defineEmits<{ choisir: [item: T] }>()
const modele = defineModel<T | undefined>()
</script>
```

- Plusieurs paramètres génériques sont séparés par des **virgules** ; les contraintes `extends` sont supportées.
- L'inférence s'effectue **à partir des props passées** au composant.

### 19.12 Typage des composants fonctionnels

```ts
import { h, type FunctionalComponent } from 'vue'

const Icone: FunctionalComponent<{ nom: string }, { clic: [MouseEvent] }> = (props, { emit }) =>
  h('i', { class: props.nom, onClick: (e: MouseEvent) => emit('clic', e) })

Icone.props = ['nom']
Icone.emits = ['clic']
```

### 19.13 Augmentation de modules (types globaux)

```ts
// src/types/vue.d.ts
import 'vue'

declare module 'vue' {
  // Propriétés globales accessibles dans les gabarits (this.$maProp)
  interface ComponentCustomProperties {
    $http: typeof import('axios').default
    $t: (cle: string) => string
  }

  // Options personnalisées de composant
  interface ComponentCustomOptions {
    permission?: string
  }

  // Attributs globaux sur les éléments HTML
  interface HTMLAttributes {
    'data-testid'?: string
  }

  // Composants globaux (autocomplétion et typage des composants enregistrés globalement)
  interface GlobalComponents {
    BaseButton: typeof import('@/components/BaseButton.vue').default
  }

  // Directives globales
  interface GlobalDirectives {
    vFocus: typeof import('@/directives/focus').vFocus
  }
}

export {}        // transforme le fichier en module
```

#### Imports de ressources et variables d'environnement

```ts
// env.d.ts
/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_API_URL: string
  readonly VITE_TITRE_APP: string
}
interface ImportMeta { readonly env: ImportMetaEnv }
```

Les variables d'environnement exposées au client **doivent** être préfixées par `VITE_` ; elles sont **publiques** (chapitre 25).

### 19.14 Typage de Vue Router et de Pinia (rappel)

```ts
// Routeur
import 'vue-router'
declare module 'vue-router' {
  interface RouteMeta { requiresAuth?: boolean; roles?: string[] }
}

// Pinia
type UtilisateurStore = ReturnType<typeof useUtilisateurStore>
```

### 19.15 Typage de l'API et des données

```ts
// Types d'API partagés
export interface Utilisateur { id: number; nom: string; email: string }
export interface ReponseApi<T> { data: T; message: string }

async function get<T>(url: string): Promise<T> {
  const r = await fetch(url)
  if (!r.ok) throw new Error(r.statusText)
  return r.json() as Promise<T>
}

const utilisateurs = ref<Utilisateur[]>([])
utilisateurs.value = await get<Utilisateur[]>('/api/users')
```

> **Les types TypeScript sont effacés à l'exécution.** Un `as Promise<T>` n'est qu'une promesse faite au compilateur : si l'API renvoie autre chose, rien ne vous prévient. Pour les données **externes**, **validez à l'exécution** avec **Zod** ou **Valibot** : `z.infer<typeof Schema>` produit le type **et** vérifie les données reçues.

```ts
import { z } from 'zod'

const SchemaUtilisateur = z.object({ id: z.number(), nom: z.string(), email: z.string().email() })
type Utilisateur = z.infer<typeof SchemaUtilisateur>

const u: Utilisateur = SchemaUtilisateur.parse(await reponse.json())     // lève une erreur si la forme est incorrecte
```

### 19.16 Problèmes courants et solutions

| Problème | Cause / solution |
| --- | --- |
| `Property 'value' does not exist` | Oubli d'annotation ou `ref` mal typé ; vérifier `Ref<T>` |
| `Object is possibly 'null'` sur une référence de gabarit | Utiliser `?.` ou `!` après `onMounted` |
| `Cannot find module './X.vue'` | `env.d.ts` absent ou *Vue - Official* mal configuré |
| Props non typées dans le gabarit | Utiliser `defineProps<T>()` et exécuter `vue-tsc` |
| `ref` retourne un type trop large | Fournir un générique : `ref<'a' \| 'b'>('a')` |
| Inférence de `reactive` avec `ref` imbriqués | Garder à l'esprit `UnwrapRef` |
| `$refs` non typé (Options API) | Préférer les références de gabarit typées |

### 19.17 Pièges fréquents

- Croire que Vite **vérifie** les types.
- Typer des props par `any` ou `Object` générique.
- Oublier `export {}` dans un fichier d'augmentation de module (il n'est alors plus un module).
- Utiliser un type **non résolvable statiquement** dans `defineProps<T>()`.
- Employer des assertions `as` pour contourner le compilateur au lieu de corriger le type.
- Faire confiance au typage des réponses d'API sans validation.

### Synthèse du chapitre 19

Typez par **types** `defineProps`, `defineEmits`, `defineModel` et `defineSlots`. Utilisez **`InjectionKey<T>`**, `InstanceType<typeof C>` et les **composants génériques** (`generic="T"`). L'**augmentation de modules** (`ComponentCustomProperties`, `GlobalComponents`, `RouteMeta`) étend les types globaux. **`vue-tsc` en CI**, et **Zod** pour valider à l'exécution ce que TypeScript ne peut pas garantir.

---

# Partie IV — Vue avancé

## 20. Options API

**Objectifs d'apprentissage.** Lire, comprendre et maintenir du code en **Options API** (Vue 2 et Vue 3) ; connaître chaque option et l'instance `this` ; typer l'Options API avec TypeScript ; comprendre les mixins et leurs défauts ; mélanger Options et Composition ; migrer progressivement vers la Composition API.

### 20.1 Principe

L'**Options API** définit un composant par un **objet d'options** (`data`, `computed`, `methods`, `watch`, hooks…) qui accède à l'état par **`this`**. Elle reste **entièrement supportée** en Vue 3 et très répandue dans les projets existants (dont tous les projets Vue 2).

```vue
<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'Compteur',
  props: { depart: { type: Number, default: 0 } },
  emits: ['change'],
  data() {
    return { count: this.depart }
  },
  computed: {
    double(): number { return this.count * 2 },
  },
  watch: {
    count(nouveau: number, ancien: number) { console.log(nouveau, ancien) },
  },
  methods: {
    incrementer() {
      this.count++
      this.$emit('change', this.count)
    },
  },
  mounted() { console.log('monté') },
})
</script>

<template>
  <button @click="incrementer">{{ count }} (x2 = {{ double }})</button>
</template>
```

**Modèle mental.** Chaque option a un **rôle** : `data` contient l'état, `computed` les dérivées, `methods` les actions, `watch` les réactions, les hooks le cycle de vie. L'inconvénient : la logique d'une **même préoccupation** est **dispersée** entre plusieurs options, ce qui devient pénible dans les gros composants.

### 20.2 Les options

#### État

| Option | Rôle |
| --- | --- |
| `data()` | **Fonction** qui retourne l'état réactif (profond) |
| `props` | Déclaration des props |
| `computed` | Propriétés calculées (getter ou `{ get, set }`) |
| `methods` | Méthodes (**pas de fonctions fléchées** : `this` serait incorrect) |
| `watch` | Observateurs |
| `emits` | Événements émis |
| `expose` | Membres publics pour les références du parent |

#### Rendu

| Option | Rôle |
| --- | --- |
| `template` | Gabarit sous forme de chaîne (nécessite le compilateur d'exécution) |
| `render` | Fonction de rendu (chapitre 21) |
| `compilerOptions` | Options du compilateur d'exécution |
| `slots` | Aide au typage des slots avec fonction de rendu |

#### Cycle de vie

`beforeCreate`, `created`, `beforeMount`, `mounted`, `beforeUpdate`, `updated`, `beforeUnmount`, `unmounted`, `errorCaptured`, `renderTracked`, `renderTriggered`, `activated`, `deactivated`, `serverPrefetch`.

> **Équivalence.** `beforeCreate` et `created` correspondent au code de premier niveau de `setup`. En Vue 2, `beforeDestroy` et `destroyed` ont été **renommés** `beforeUnmount` et `unmounted`.

#### Composition

| Option | Rôle |
| --- | --- |
| `provide` / `inject` | Injection de dépendances |
| `mixins` | Fusion d'options (**déconseillé**) |
| `extends` | Héritage d'un composant |
| `components` | Composants locaux |
| `directives` | Directives locales |
| `setup()` | Pont vers la Composition API |

#### Divers

`name`, `inheritAttrs`, options personnalisées (`ComponentCustomOptions`).

### 20.3 L'instance `this`

| Propriété | Contenu |
| --- | --- |
| `this.$data` | Objet d'état |
| `this.$props` | Props |
| `this.$el` | Élément racine |
| `this.$refs` | Références de gabarit |
| `this.$slots` | Slots |
| `this.$attrs` | Attributs de transfert |
| `this.$emit()` | Émission d'événement |
| `this.$watch()` | Création impérative d'un observateur |
| `this.$nextTick()` | Attente du DOM |
| `this.$forceUpdate()` | Force un nouveau rendu |
| `this.$parent`, `this.$root` | Parent, racine (**à éviter** : couplage fort) |
| `this.$options` | Options du composant |

Tous les membres (`data`, `computed`, `methods`, props, `setup`) sont placés dans le **même espace de noms** sur `this` : un nom en collision est un bogue.

### 20.4 `watch` en Options API

```ts
watch: {
  count(n, o) {},                                                // simple
  'utilisateur.nom'(n) {},                                       // chemin d'accès
  utilisateur: { handler(n, o) {}, deep: true, immediate: true },
  tache: 'nomDeMethode',                                         // nom de méthode
},
```

### 20.5 Mixins

```ts
const mixinJournal = {
  created() { console.log('créé') },
  methods: { journaliser(m: string) { console.log(m) } },
}

export default { mixins: [mixinJournal] }
```

**Inconvénients** : **origine des propriétés obscure** (d'où vient `this.journaliser` ?), **collisions** de noms, couplage implicite entre mixin et composant, typage faible. **Remplacez-les par des composables** (chapitre 13).

#### Stratégies de fusion

- `data` : fusion récursive (le **composant** l'emporte).
- **Hooks** : tous sont appelés (ceux des mixins **d'abord**).
- `methods`, `components`, `computed` : le **composant** est prioritaire.

### 20.6 Typage de l'Options API

- Utilisez **`defineComponent()`** pour activer l'inférence.
- **Annotez le type de retour** des `computed` qui utilisent `this`.
- Typez `data` : `data() { return { items: [] as Item[] } }`.
- Typez les props : `type: Array as PropType<Item[]>`.
- Typez `$refs` : `(this.$refs.input as HTMLInputElement).focus()`.
- Typez `$emit` : option `emits` sous forme d'objet avec validateurs typés.

```ts
import { defineComponent, type PropType } from 'vue'

export default defineComponent({
  props: { items: { type: Array as PropType<Item[]>, required: true } },
  data() { return { selection: null as Item | null } },
  computed: { total(): number { return this.items.length } },
  methods: { choisir(i: Item) { this.selection = i } },
})
```

### 20.7 Mélanger Options et Composition

L'option `setup()` s'exécute **avant** les autres options ; ce qu'elle retourne est exposé à `this` et au gabarit.

```ts
import { defineComponent, ref } from 'vue'

export default defineComponent({
  props: { id: Number },
  setup(props, { emit, attrs, slots, expose }) {
    const donnees = ref<Item[]>([])
    return { donnees }                         // accessible par this.donnees
  },
  methods: { afficher() { console.log(this.donnees) } },
})
```

- `this` **n'est pas** disponible dans `setup()`.
- Les valeurs retournées par `setup` **ne sont pas** accessibles dans `data()`.
- Cette cohabitation sert surtout à **migrer progressivement** ou à utiliser un composable dans un composant existant.

### 20.8 Comparaison et choix

| Critère | **Options API** | **Composition API** |
| --- | --- | --- |
| Courbe d'apprentissage | Douce | Moyenne |
| Réutilisation | Mixins | Composables |
| TypeScript | Correct | Excellent |
| Grands composants | Logique **dispersée** | Logique **regroupée** |
| Taille du bundle | Légèrement supérieure | Meilleure élimination du code inutilisé |
| Recommandé pour | Projets existants, composants simples | **Nouveaux projets** |

### 20.9 Migration vers la Composition API

| Options API | Composition API |
| --- | --- |
| `data` | `ref` / `reactive` |
| `computed` | `computed()` |
| `methods` | Fonctions |
| `watch` | `watch()` / `watchEffect()` |
| `created` | Code de premier niveau |
| `mounted` / `unmounted` | `onMounted` / `onUnmounted` |
| `mixins` | Composables |
| `provide` / `inject` | `provide()` / `inject()` |
| `this.$refs.x` | Référence de gabarit (`useTemplateRef`) |
| `this.$emit` | `defineEmits` |
| `this.$props` | `defineProps` |

**Stratégie.** Migrez **composant par composant**, en commençant par les nouveaux composants et ceux que vous modifiez de toute façon ; les deux styles **cohabitent** sans problème dans la même application.

### 20.10 Pièges fréquents

- **Fonctions fléchées** dans `methods`, `computed` ou les hooks : `this` est incorrect.
- Déclarer `data` comme un **objet** : c'est obligatoirement une **fonction**.
- `this` indéfini dans les callbacks non fléchés (`setTimeout(function () { this.x })`).
- **Collisions** de noms entre mixins et composant.
- Mélanger des tutoriels Vue 2 et Vue 3 (`beforeDestroy`, `this.$set`, `.sync`).

### Synthèse du chapitre 20

L'Options API repose sur un **objet d'options** et sur **`this`**. Utilisez `defineComponent` et des annotations pour TypeScript. Remplacez les **mixins par des composables**. Les deux API **cohabitent** grâce à `setup()`, ce qui permet de migrer progressivement.

---

## 21. Fonctions de rendu et JSX

**Objectifs d'apprentissage.** Comprendre la **fonction de rendu** générée par le compilateur ; maîtriser `h()` et les nœuds virtuels ; écrire un composant en fonction de rendu ; utiliser **JSX / TSX** avec Vue ; traduire les directives de gabarit en fonction de rendu ; savoir quand privilégier chaque approche.

### 21.1 Gabarits et fonctions de rendu

Un **gabarit** est compilé en une **fonction de rendu** qui retourne un arbre de **nœuds virtuels**. On peut écrire **directement** cette fonction pour bénéficier de la **puissance complète de JavaScript** (boucles, composition dynamique).

**Cas d'usage :**

- composants **très dynamiques** (génération de balises selon une prop, rendu récursif complexe) ;
- **bibliothèques de composants** et abstractions de bas niveau ;
- préférence d'équipe pour **JSX / TSX**.

> Les gabarits sont **plus optimisables** par le compilateur (indicateurs de modification, remontée du statique) ; les fonctions de rendu écrites à la main sont plus flexibles mais **ne profitent pas de ces optimisations** (chapitre 23).

### 21.2 `h()` : créer des nœuds virtuels

Signature : `h(type, props?, enfants?)`.

```ts
import { h } from 'vue'

h('div')                                                       // <div></div>
h('div', { id: 'foo', class: 'bar' })                          // attributs
h('div', { class: ['a', { b: true }], style: { color: 'red' } })
h('div', { onClick: () => {} })                                // événements : préfixe `on` + PascalCase
h('p', 'texte')                                                // enfant texte
h('ul', [h('li', 'a'), h('li', 'b')])                          // enfants sous forme de tableau
h(MonComposant, { titre: 'x' }, {                              // slots = objet de fonctions
  default: () => 'contenu',
  entete: () => h('h1', 'Titre'),
})
```

#### Propriétés et attributs

`h('input', { value: 'x' })` : Vue choisit automatiquement entre **propriété DOM** et **attribut**. Forcez avec le préfixe `.` (propriété) ou `^` (attribut).

#### Événements et modificateurs

```ts
import { h, withModifiers } from 'vue'

h('input', { onInput: gestionnaire, onClickCapture: gestionnaire, onKeyupOnce: gestionnaire })
h('button', { onClick: withModifiers(gestionnaire, ['stop', 'prevent']) })
```

#### Constantes fournies

`Fragment` (racines multiples), `Text`, `Comment`, `Teleport`, `Suspense`, `KeepAlive`, `Transition`.

```ts
import { h, Fragment } from 'vue'

h(Fragment, [h('p', 'a'), h('p', 'b')])
```

### 21.3 Un composant en fonction de rendu

```ts
import { defineComponent, h, ref } from 'vue'

export default defineComponent({
  props: { niveau: { type: Number, required: true } },
  setup(props, { slots, emit, attrs, expose }) {
    const compteur = ref(0)
    return () => h(
      `h${props.niveau}`,
      { class: 'titre', onClick: () => compteur.value++ },
      [slots.default?.(), ` (${compteur.value})`],
    )
  },
})
```

- `setup` **retourne la fonction de rendu** (et non un objet d'état) : on ne peut alors pas utiliser en même temps un gabarit.
- Les **dépendances** lues dans la fonction de rendu sont suivies : le composant se re-rend quand elles changent.
- Pour **exposer** des méthodes : `expose({ methode })` dans `setup`.

#### Slots

```ts
slots.default?.()                          // slot par défaut : tableau de nœuds virtuels
slots.entete?.({ titre: 'x' })             // slot à portée
```

#### Directives intégrées en fonction de rendu

| Gabarit | Fonction de rendu |
| --- | --- |
| `v-if` | Opérateur ternaire ou `&&` |
| `v-for` | `tableau.map(...)` |
| `v-model` | `modelValue` + `'onUpdate:modelValue'` |
| `v-on:click.stop` | `withModifiers(fn, ['stop'])` |
| `v-slot` | Objet de fonctions en 3e argument |
| Directive personnalisée | `withDirectives(vnode, [[dir, valeur, arg, modificateurs]])` |

```ts
h(Champ, {
  modelValue: props.modelValue,
  'onUpdate:modelValue': (v: string) => emit('update:modelValue', v),
})
```

#### Résolution de composants et directives

```ts
import { resolveComponent, resolveDirective } from 'vue'

const Bouton = resolveComponent('MonBouton')      // composant enregistré globalement
```

### 21.4 Autres utilitaires

`createVNode` (version de bas niveau de `h`), `cloneVNode`, `isVNode`, `mergeProps` (fusion d'attributs), `render(vnode, conteneur)` (rendu impératif hors application).

### 21.5 JSX / TSX

Plugin : **`@vitejs/plugin-vue-jsx`**.

```bash
npm i -D @vitejs/plugin-vue-jsx
```

```ts
// vite.config.ts
import vueJsx from '@vitejs/plugin-vue-jsx'

export default defineConfig({ plugins: [vue(), vueJsx()] })
```

```json
// tsconfig.json
{ "compilerOptions": { "jsx": "preserve", "jsxImportSource": "vue" } }
```

```tsx
// src/components/Liste.tsx
import { defineComponent, ref, type PropType } from 'vue'

export default defineComponent({
  props: { items: { type: Array as PropType<string[]>, required: true } },
  setup(props, { slots }) {
    const n = ref(0)
    return () => (
      <div class="liste">
        <button onClick={() => n.value++}>{n.value}</button>
        <ul>
          {props.items.map((i) => <li key={i}>{i}</li>)}
        </ul>
        {slots.default?.()}
      </div>
    )
  },
})
```

#### Différences avec React

- L'attribut s'écrit **`class`** (et non `className`), `for`, et les événements `onClick`.
- Les `ref` doivent être lus avec **`.value`** dans le JSX.
- `v-model` : `<input v-model={ref.value} />` (supporté par le plugin) ; `v-show` supporté ; **`v-if` et `v-for` ne sont pas** des directives en JSX : utilisez des expressions JavaScript.
- Slots : `v-slots={{ default: () => 'x' }}` ou enfants sous forme de fonctions.
- Pas de « hooks » à ordre contraint : le composant n'est exécuté **qu'une fois** (`setup`), seule la fonction retournée est rappelée à chaque rendu.

#### Composant fonctionnel en JSX

```tsx
import type { FunctionalComponent } from 'vue'

const Item: FunctionalComponent<{ label: string }> = ({ label }) => <li>{label}</li>
```

### 21.6 Gabarit, JSX ou fonction de rendu ?

| | **Gabarit** | **JSX / TSX** | **`h()`** |
| --- | --- | --- | --- |
| Optimisations du compilateur | **Maximales** | Partielles | Aucune |
| Lisibilité (interface) | **Haute** | Bonne | Faible |
| Souplesse logique | Moyenne | **Haute** | **Haute** |
| Usage recommandé | **Par défaut** | Composants très dynamiques | Bibliothèques, bas niveau |

### 21.7 Pièges fréquents

- Oublier que `setup` doit **retourner une fonction** (et non un objet) pour produire le rendu.
- Réutiliser **le même nœud virtuel** à plusieurs endroits : chaque nœud doit être **unique**.
- Utiliser `v-if` ou `v-for` en JSX comme dans un gabarit.
- Mauvais format de slots dans `h()` : c'est un **objet de fonctions**, pas un tableau.
- Lire un `ref` sans `.value` dans la fonction de rendu.

### Synthèse du chapitre 21

Gabarit → **fonction de rendu** → **nœuds virtuels**. `h(type, props, enfants)`, `Fragment`, `withModifiers` et `withDirectives` constituent la boîte à outils ; le **JSX** (via `@vitejs/plugin-vue-jsx`) est proche de React, avec `class`. Le **gabarit reste le choix par défaut** pour ses optimisations.

---

# Partie V — Tests et performance

## 22. Tests

**Objectifs d'apprentissage.** Définir une stratégie de test ; mettre en place **Vitest** et **Vue Test Utils** ; tester composants, composables, stores Pinia et routes ; gérer l'asynchrone, les doublures (*mocks*) et les minuteries ; écrire des tests **de bout en bout** avec Playwright ou Cypress ; intégrer accessibilité et qualité ; connaître les bonnes pratiques.

### 22.1 Stratégie de test

| Niveau | Cible | Outils |
| --- | --- | --- |
| **Unitaire** | Fonctions, composables, stores | **Vitest** |
| **Composant** | Rendu et interactions d'un composant | Vitest + **Vue Test Utils** ou **Testing Library** |
| **De bout en bout (E2E)** | Parcours utilisateur réel dans un navigateur | **Playwright**, **Cypress** |

**Pyramide des tests** : beaucoup de tests unitaires et de composants (rapides, ciblés), quelques tests E2E sur les **parcours critiques** (connexion, achat).

**Principe directeur** : testez le **comportement observable** (ce que l'utilisateur voit et fait), **pas les détails d'implémentation** (état interne, noms de méthodes). Un bon test survit à une refonte interne du composant.

### 22.2 Installation

```bash
npm i -D vitest @vue/test-utils jsdom @vitest/coverage-v8
```

```ts
// vitest.config.ts
import { defineConfig, mergeConfig } from 'vitest/config'
import viteConfig from './vite.config'

export default mergeConfig(viteConfig, defineConfig({
  test: {
    environment: 'jsdom',            // ou 'happy-dom' : DOM simulé
    globals: true,
    coverage: { provider: 'v8', reporter: ['text', 'html'] },
  },
}))
```

Scripts : `"test": "vitest"` (mode veille) et `"coverage": "vitest run --coverage"`. `create-vue` génère cette configuration si l'option Vitest est cochée. **Vitest** réutilise la configuration de Vite : mêmes alias, mêmes plugins.

### 22.3 Tester un composant avec Vue Test Utils

```ts
// src/components/__tests__/Compteur.spec.ts
import { mount } from '@vue/test-utils'
import { describe, it, expect } from 'vitest'
import Compteur from '@/components/Compteur.vue'

describe('Compteur', () => {
  it('affiche la valeur initiale', () => {
    const wrapper = mount(Compteur, { props: { depart: 5 } })
    expect(wrapper.text()).toContain('5')
  })

  it('incrémente au clic', async () => {
    const wrapper = mount(Compteur)
    await wrapper.find('button').trigger('click')          // `await` : attend la mise à jour du DOM
    expect(wrapper.find('[data-test="valeur"]').text()).toBe('1')
  })

  it('émet un événement', async () => {
    const wrapper = mount(Compteur)
    await wrapper.find('button').trigger('click')
    expect(wrapper.emitted('change')).toHaveLength(1)
    expect(wrapper.emitted('change')![0]).toEqual([1])
  })
})
```

#### API principales

| API | Rôle |
| --- | --- |
| `mount(Comp, options)` | Monte le composant **et ses enfants** |
| `shallowMount` | Remplace les enfants par des **doublures** (*stubs*) |
| `wrapper.find` / `findAll` / `findComponent` | Sélection (CSS, `data-test`, composant) |
| `wrapper.text()` / `html()` / `classes()` / `attributes()` | Lecture |
| `wrapper.trigger('click')` | Déclenche un événement DOM |
| `wrapper.setValue('x')` | Saisie dans un champ |
| `wrapper.setProps({ … })` | Modifie les props |
| `wrapper.emitted()` | Événements émis |
| `wrapper.vm` | Instance (usage limité : détail d'implémentation) |
| `wrapper.unmount()` | Démonte |
| `flushPromises()` | Résout les promesses en attente |

#### Options de `mount`

```ts
mount(Comp, {
  props: { titre: 'x' },
  slots: { default: 'Contenu', entete: '<h1>Titre</h1>' },
  global: {
    plugins: [router, pinia, i18n],
    stubs: { RouterLink: RouterLinkStub, Enfant: true },
    mocks: { $t: (k: string) => k },
    provide: { [CleTheme as symbol]: contexte },
    directives: { focus: {} },
    components: { BaseButton },
  },
  attachTo: document.body,       // nécessaire pour tester focus et mise en page
})
```

#### Sélecteurs robustes

Utilisez des attributs dédiés **`data-test="…"`** ou, mieux, des **rôles ARIA et libellés** (Testing Library) plutôt que des classes de style : elles changent lors d'une refonte graphique.

### 22.4 Asynchronisme

```ts
await wrapper.setValue('abc')                         // met à jour et attend le prochain cycle
await flushPromises()                                 // après une requête simulée
vi.useFakeTimers(); vi.advanceTimersByTime(1000)      // minuteries simulées
```

Toute interaction qui modifie le DOM (`trigger`, `setValue`, `setProps`) retourne une promesse : **attendez-la** avant l'assertion.

### 22.5 Doublures (*mocks*)

```ts
import { vi } from 'vitest'

vi.mock('@/api/utilisateurs', () => ({
  getUtilisateurs: vi.fn().mockResolvedValue([{ id: 1, nom: 'A' }]),
}))

const fn = vi.fn()
fn.mockReturnValue(1)
expect(fn).toHaveBeenCalledWith('x')

vi.spyOn(window, 'fetch').mockResolvedValue(new Response(JSON.stringify({ ok: true })))
```

**MSW (Mock Service Worker)** intercepte les requêtes **au niveau réseau** : les mêmes définitions de réponses servent en développement, en test unitaire et en E2E, ce qui est plus réaliste que de substituer `fetch`.

> **Règle.** Remplacez par des doublures **aux frontières** du système (réseau, horloge, stockage), pas les modules internes que vous êtes censé tester.

### 22.6 Tester un composable

```ts
import { avecSetup } from '@/test/utils'
import { useCompteur } from '@/composables/useCompteur'

it('useCompteur', () => {
  const [{ count, inc }, app] = avecSetup(() => useCompteur())
  inc()
  expect(count.value).toBe(1)
  app.unmount()                  // permet de tester le nettoyage
})
```

- Sans hooks : appel direct de la fonction.
- Avec hooks ou injection : composant hôte (chapitre 13, section 13.11).

### 22.7 Tester Pinia

```ts
import { createTestingPinia } from '@pinia/testing'
import { vi } from 'vitest'

const wrapper = mount(Panier, {
  global: {
    plugins: [createTestingPinia({
      createSpy: vi.fn,
      initialState: { panier: { articles: [{ id: 1 }] } },
      stubActions: false,                  // true (défaut) : actions espionnées mais non exécutées
    })],
  },
})

const store = usePanierStore()
expect(store.ajouter).toHaveBeenCalled()
```

Pour tester un store **seul** : `setActivePinia(createPinia())` dans `beforeEach` (chapitre 18).

### 22.8 Tester avec Vue Router

```ts
import { createRouter, createMemoryHistory } from 'vue-router'

const router = createRouter({ history: createMemoryHistory(), routes })
router.push('/users/1')
await router.isReady()

const wrapper = mount(App, { global: { plugins: [router] } })
```

Ou **simulez** le routeur : `RouterLinkStub`, `mocks: { $route }`, `vi.mock('vue-router')` (utile pour un composant qui appelle seulement `useRoute`).

### 22.9 Tests d'instantané (*snapshots*)

`expect(wrapper.html()).toMatchSnapshot()` compare le HTML à une version enregistrée. À utiliser **avec parcimonie** : ces tests sont **fragiles** (tout changement de balisage les casse) et leurs échecs sont souvent validés sans lecture.

### 22.10 Tests de bout en bout

#### Playwright

```bash
npm init playwright@latest
```

```ts
import { test, expect } from '@playwright/test'

test('connexion', async ({ page }) => {
  await page.goto('/connexion')
  await page.getByLabel('Email').fill('a@b.fr')
  await page.getByLabel('Mot de passe').fill('secret')
  await page.getByRole('button', { name: 'Connexion' }).click()
  await expect(page).toHaveURL('/tableau-de-bord')
})
```

#### Cypress

```ts
describe('accueil', () => {
  it('affiche le titre', () => {
    cy.visit('/')
    cy.contains('h1', 'Bienvenue')
  })
})
```

Les deux outils supportent aussi les **tests de composants dans un vrai navigateur** (Playwright CT, Cypress Component Testing, mode navigateur de Vitest), utiles pour ce qui dépend du rendu réel (focus, mise en page, glisser-déposer).

### 22.11 Accessibilité et qualité

- **Testing Library** (`@testing-library/vue`) : requêtes par **rôle, libellé et texte** (`getByRole`, `getByLabelText`), qui reflètent l'expérience de l'utilisateur.
- **axe-core**, `vitest-axe` et `@axe-core/playwright` : audit **d'accessibilité** automatisé.
- **Couverture** : un indicateur, **pas un objectif** en soi.
- **Intégration continue** : exécutez `vue-tsc`, ESLint, tests unitaires et E2E à chaque modification.

### 22.12 Pièges fréquents

- Oublier `await` sur `trigger`, `setValue` ou `setProps` : l'assertion s'exécute trop tôt.
- Tester l'**implémentation** (`wrapper.vm.x`) plutôt que le rendu.
- Utiliser `shallowMount` partout : les tests ne sont plus représentatifs.
- Tests **dépendants les uns des autres** (état partagé, pas de nouvelle instance de Pinia).
- Sélecteurs **fragiles** fondés sur des classes CSS.
- Oublier `attachTo: document.body` pour tester le focus.
- Viser 100 % de couverture au détriment de la pertinence des tests.

### Synthèse du chapitre 22

**Vitest + Vue Test Utils** couvrent le niveau unitaire et composant ; **Playwright** et **Cypress** le niveau E2E. Testez le **comportement**, pas l'implémentation. Attendez (`await`) toute mise à jour du DOM, utilisez `flushPromises` pour l'asynchrone, `@pinia/testing` pour Pinia et `createMemoryHistory` pour le routeur.

---

## 23. Performance

**Objectifs d'apprentissage.** Comprendre ce qui détermine la performance d'une application Vue ; appliquer les techniques d'optimisation du **chargement** et des **mises à jour** ; connaître les optimisations automatiques du compilateur et le **mode Vapor** ; mesurer et diagnostiquer avec les bons outils ; maîtriser la mémoire.

### 23.1 Deux axes de performance

| Axe | Mesures | Leviers |
| --- | --- | --- |
| **Performance de chargement** | **LCP**, **FCP**, **TTI**, taille du bundle | Découpage du code, SSR / SSG, images, cache |
| **Performance de mise à jour** (exécution) | **INP**, fluidité, images par seconde | Éviter les re-rendus inutiles, listes virtuelles, réactivité superficielle |

> **Règle : mesurez d'abord** (Lighthouse, Chrome Performance, Vue DevTools), **optimisez ensuite**, puis **mesurez de nouveau**. Une optimisation sans mesure est un pari.

### 23.2 Optimisation du chargement

#### Choix d'architecture

- **SSG** (pré-rendu) pour le contenu statique ; **SSR** pour le contenu dynamique référencé ; **SPA** pour les applications internes (chapitre 24).
- **Hydratation paresseuse** *(3.5)* : `defineAsyncComponent({ hydrate: hydrateOnIdle() | hydrateOnVisible() | hydrateOnMediaQuery() | hydrateOnInteraction() })`.

#### Taille du bundle

- **Élimination du code inutilisé** (*tree-shaking*) : imports **nommés** (`import { debounce } from 'lodash-es'`).
- Préférez des **dépendances légères** (`date-fns` ou `dayjs` plutôt que `moment`).
- **Analysez** : `rollup-plugin-visualizer`, `vite-bundle-visualizer`.
- Évitez les plugins globaux et composants globaux inutiles.

#### Découpage du code et chargement à la demande

```ts
const routes = [{ path: '/admin', component: () => import('@/views/VueAdmin.vue') }]      // routes
const Graphique = defineAsyncComponent(() => import('./Graphique.vue'))                     // composants lourds
```

Préchargement : `<link rel="modulepreload">`, commentaires de préchargement, ou `import()` au survol d'un lien.

#### Ressources

- **Images** : formats modernes (WebP, AVIF), `loading="lazy"`, `srcset`, dimensions explicites.
- **Polices** : `font-display: swap`, préchargement, sous-ensembles de caractères.
- **Cache** : noms de fichiers à empreinte, en-têtes `Cache-Control`, **CDN**, compression **Brotli** ou gzip.
- **PWA et service workers** : `vite-plugin-pwa`.

### 23.3 Optimisation des mises à jour

#### 1. Stabilité des props

Un composant enfant ne se re-rend que si ses **props ont changé**. Passez des **valeurs primitives stables** plutôt que des objets recréés à chaque rendu.

```vue
<!-- Mauvais : chaque enfant reçoit une prop qui dépend de la liste entière -->
<ElementListe v-for="i in items" :key="i.id" :selection="selectionId" />

<!-- Meilleur : l'enfant reçoit un booléen ; seuls 2 enfants (l'ancien et le nouveau sélectionné) changent -->
<ElementListe v-for="i in items" :key="i.id" :actif="i.id === selectionId" />
```

#### 2. `v-once` et `v-memo`

```vue
<div v-once>{{ contenuStatique }}</div>

<div v-for="i in liste" :key="i.id" v-memo="[i.id === selectionId]">
  <!-- re-rendu seulement si la valeur du tableau change -->
</div>
```

`v-memo` : à réserver aux **très grandes listes** (plus d'un millier d'éléments) ; avec `v-for`, il se place **sur le même élément**.

#### 3. Propriétés calculées stables *(3.4)*

Un `computed` ne **notifie** ses dépendants que si sa valeur change réellement : retourner des **primitives** évite des déclenchements superflus.

#### 4. Réactivité superficielle

```ts
const grosseListe = shallowRef<Item[]>([])
grosseListe.value = nouvelleListe                  // remplacez pour déclencher

const instance = markRaw(new BibliothequeCarte())  // jamais proxifié
```

#### 5. Limiter l'abstraction en composants

Chaque **instance de composant** a un coût. Pour de très longues listes, ne créez pas un composant par ligne si un élément simple suffit, ou virtualisez la liste.

#### 6. Virtualisation des listes

Ne rendez que les éléments **visibles** à l'écran : `vue-virtual-scroller`, `@tanstack/vue-virtual`.

#### 7. Optimiser les observateurs

- Évitez `deep: true` sur de grosses structures : observez un **getter précis**.
- Ne créez pas d'observateurs dans des boucles.

#### 8. Fonctions dans le gabarit

Évitez les calculs coûteux dans le gabarit : utilisez une propriété calculée.

#### 9. `KeepAlive`

Évite de recréer des vues coûteuses ; limitez la mémoire par `max`.

#### 10. `key` pertinentes

Une `key` stable permet la **réutilisation** ; une `key` qui change provoque la **recréation** (outil de réinitialisation volontaire).

### 23.4 Optimisations de compilation (automatiques)

Le compilateur de gabarits applique :

- le **remontage statique** (*hoisting*) : les nœuds statiques sont créés **une seule fois** ;
- les **indicateurs de modification** (*patch flags*) : ils indiquent ce qui est dynamique (texte, classe, props) pour un **diff minimal** ;
- l'**aplatissement de l'arbre** (*tree flattening*) : seuls les **nœuds dynamiques** sont suivis (par blocs) ;
- la **mise en cache des gestionnaires** en ligne ;
- la **transformation en chaîne** des gros blocs statiques (insérés par `innerHTML`).

Ces optimisations s'appliquent **aux gabarits**, pas aux fonctions de rendu écrites à la main (chapitre 21).

### 23.5 Vue 3.6 et le mode Vapor

La branche **3.6**, en candidate à la sortie à la date de rédaction, apporte deux changements :

1. **Un nouveau noyau de réactivité**, réécrit sur la base de *alien-signals*, qui améliore les performances et la consommation mémoire **sans modifier l'API** : il suffit de mettre à jour.
2. **Le mode Vapor**, une **stratégie de compilation alternative sans DOM virtuel**, qui génère du code mettant à jour directement le DOM, pour réduire la taille de base et accélérer le rendu.

```vue
<script setup lang="ts" vapor>
import { ref } from 'vue'

const count = ref(0)
</script>

<template>
  <button @click="count++">{{ count }}</button>
</template>
```

- **Optionnel et par composant** : l'attribut `vapor` distingue un composant compilé en mode Vapor d'un composant classique ; les deux modes coexistent dans la même application (il est recommandé de regrouper les composants d'un même mode et d'éviter l'imbrication mixte).
- **Sous-ensemble d'API** : certaines fonctionnalités ne sont pas prises en charge dans un composant Vapor (consultez les notes de version).
- **Statut** : fonctionnellement complet mais **non stable** tant que la version 3.6 finale n'est pas publiée. À évaluer sur une page isolée où un goulot est déjà **mesuré** ; ne pas déployer en production avant la version stable.

### 23.6 Mesure et diagnostic

| Outil | Usage |
| --- | --- |
| **Vue DevTools** (onglets *Performance* et *Timeline*) | Temps de rendu des composants |
| `app.config.performance = true` | Marqueurs `performance.mark` (développement) |
| `onRenderTracked` / `onRenderTriggered` | Comprendre **pourquoi** un composant se re-rend |
| **Chrome DevTools** (Performance, Memory) | Profilage du processeur et de la mémoire |
| **Lighthouse / PageSpeed / WebPageTest** | Indicateurs Web Vitals |
| **Analyseurs de bundle** | Poids des dépendances |

```ts
import { onRenderTriggered } from 'vue'

onRenderTriggered((e) => console.log(e.key, e.target, e.type))      // quelle donnée a déclenché le rendu ?
```

### 23.7 Mémoire

- Nettoyez **minuteurs**, **écouteurs**, **observateurs** et **WebSocket** dans `onUnmounted`.
- Arrêtez les `watch` créés de façon **asynchrone**.
- Surveillez les **fermetures** (*closures*) qui capturent de grosses structures.
- Limitez le cache `KeepAlive` (`max`).
- Surveillez les **états de module** qui grossissent sans fin (caches, journaux).

### 23.8 Pièges fréquents

- Optimiser **sans mesurer**.
- `deep: true` sur de grosses données.
- Abuser de `v-memo` ou de `shallowRef` : la complexité dépasse le gain.
- Listes énormes **non virtualisées**.
- Bundle gonflé par des imports globaux (`import _ from 'lodash'`).
- Mettre en production une version candidate (3.6 RC) pour gagner quelques millisecondes.

### Synthèse du chapitre 23

**Mesurez → optimisez → mesurez.** Chargement : **découpage du code, SSR / SSG, images, cache**. Mises à jour : **props stables, `shallowRef`, virtualisation, `v-memo`, `computed` stables**. Le compilateur optimise automatiquement les **gabarits** ; Vue 3.6 prépare un nouveau noyau de réactivité et le **mode Vapor** (optionnel, à n'utiliser qu'en version stable).

---

# Partie VI — Essentiels

## 24. Rendu côté serveur (SSR), génération statique (SSG) et Nuxt

**Objectifs d'apprentissage.** Distinguer **CSR**, **SSR**, **SSG** et rendu **hybride** ; comprendre l'**hydratation** et les **désaccords d'hydratation** ; connaître les principes du code universel et de l'isolation par requête ; prendre en main **Nuxt** (routage par fichiers, récupération de données, serveur Nitro, rendu hybride) ; connaître VitePress et la génération statique ; choisir le bon mode.

### 24.1 Modes de rendu

| Mode | Où le HTML est produit | Avantages | Inconvénients |
| --- | --- | --- | --- |
| **CSR** (SPA) | Navigateur | Simple, très interactif | SEO limité, premier affichage lent, page blanche initiale |
| **SSR** | Serveur, **à chaque requête** | SEO, premier affichage rapide, contenu dynamique | Serveur requis, complexité |
| **SSG** | **À la compilation** (statique) | Très rapide, hébergeable sur CDN, sûr | Contenu figé jusqu'à la prochaine compilation |
| **ISR / SWR / hybride** | Statique **régénéré** | Équilibre entre fraîcheur et vitesse | Dépend du framework |
| **Îlots / hydratation partielle** | Statique + zones interactives | Très peu de JavaScript | Architecture spécifique |

Un même projet peut **mélanger** ces modes **par route** (les `routeRules` de Nuxt).

### 24.2 L'hydratation

Le serveur envoie du **HTML** ; le client **« hydrate »** l'application : il construit l'arbre de nœuds virtuels, **associe** les éléments DOM existants et **attache** les écouteurs, **sans recréer le DOM**. Résultat : l'utilisateur voit le contenu immédiatement, et la page devient interactive dès que le JavaScript est chargé.

#### Désaccord d'hydratation (*hydration mismatch*)

Quand le HTML produit par le serveur **diffère** du premier rendu côté client, Vue **avertit** et peut devoir corriger le DOM. **Causes fréquentes :**

- `Math.random()`, `Date.now()`, langue ou fuseau horaire différents entre serveur et client ;
- code qui dépend du **navigateur** exécuté pendant le rendu (`window`, `localStorage`) ;
- **HTML invalide** (imbrication de balises non autorisée, par exemple un `<div>` dans un `<p>`).

**Solutions :** déplacer le code dépendant du navigateur dans `onMounted`, utiliser `useId`, `<ClientOnly>` (Nuxt), initialiser avec des valeurs **identiques** côté serveur et client ; l'attribut `data-allow-mismatch` *(3.5)* tolère volontairement un écart connu (par exemple une date).

#### Stratégies d'hydratation paresseuse *(3.5)*

```ts
import {
  defineAsyncComponent, hydrateOnVisible, hydrateOnIdle,
  hydrateOnInteraction, hydrateOnMediaQuery,
} from 'vue'

const Carte = defineAsyncComponent({
  loader: () => import('./Carte.vue'),
  hydrate: hydrateOnVisible(),            // hydraté quand le composant devient visible
})
```

Les autres stratégies : `hydrateOnIdle()` (quand le navigateur est inactif), `hydrateOnInteraction()` (au premier clic ou survol), `hydrateOnMediaQuery('(max-width: 500px)')`. Elles retardent le coût du JavaScript pour les zones peu importantes.

### 24.3 SSR avec l'API Vue (bas niveau)

```ts
// serveur (Node)
import { createSSRApp } from 'vue'
import { renderToString } from 'vue/server-renderer'

const app = createSSRApp({ data: () => ({ count: 1 }), template: `<button>{{ count }}</button>` })
const html = await renderToString(app)
```

```ts
// client
import { createSSRApp } from 'vue'
import App from './App.vue'

createSSRApp(App).mount('#app')          // hydrate le HTML existant
```

#### Principes à respecter

- **Code universel** : le même code s'exécute côté serveur et côté navigateur ; **pas d'API du navigateur** directement au niveau racine.
- **Hooks** : seuls `setup` et `onServerPrefetch` s'exécutent côté serveur ; `onMounted` et les suivants **non**.
- **Isolation par requête** : créez une **nouvelle instance** d'application, de routeur et de store **pour chaque requête** ; un singleton partagé ferait **fuiter des données entre utilisateurs**.
- **Sérialisation de l'état** : transmettez l'état initial au client (`window.__INITIAL_STATE__`) pour **ne pas refaire** les requêtes au chargement.
- **Directives personnalisées** : `getSSRProps`.
- **`Teleport`** : cibles spécifiques côté SSR.

> En pratique, on utilise un **framework** (Nuxt) ou le mode SSR de Vite plutôt que d'assembler tout cela soi-même.

### 24.4 Nuxt

**Nuxt** est le **méta-framework full-stack** officiel de l'écosystème Vue : routage par fichiers, importations automatiques, SSR / SSG / hybride, serveur intégré (**Nitro**), modules.

```bash
npm create nuxt@latest mon-app
cd mon-app && npm run dev
```

> **Version.** **Nuxt 4** (publié en 2025) est la version de référence ; elle place le code de l'application dans un dossier **`app/`** et garde `server/`, `public/` et la configuration à la racine. Les projets **Nuxt 3** utilisent la même organisation mais avec les dossiers directement à la racine ; la plupart des concepts ci-dessous s'appliquent aux deux.

#### Structure (Nuxt 4)

```text
mon-app/
├── app/
│   ├── app.vue                 # composant racine
│   ├── pages/                  # routage par fichiers
│   │   ├── index.vue           # /
│   │   ├── a-propos.vue        # /a-propos
│   │   └── users/[id].vue      # /users/:id
│   ├── layouts/                # mises en page
│   ├── components/             # importés automatiquement
│   ├── composables/            # importés automatiquement
│   ├── middleware/             # gardes de route
│   ├── plugins/                # plugins Vue / Nuxt
│   ├── stores/                 # (avec @pinia/nuxt)
│   └── utils/                  # importés automatiquement
├── server/
│   ├── api/                    # points d'accès /api/*
│   ├── routes/                 # routes serveur
│   └── middleware/
├── public/                     # fichiers statiques
├── shared/                     # code partagé client / serveur
└── nuxt.config.ts              # configuration
```

#### Fonctionnalités clés

| Fonctionnalité | Description |
| --- | --- |
| **Routage par fichiers** | `pages/users/[id].vue`, `[...slug].vue`, routes imbriquées avec `<NuxtPage />` |
| **Importations automatiques** | `ref`, `computed`, composants et composables **sans `import`** |
| **Récupération de données** | `useFetch`, `useAsyncData`, `$fetch` (isomorphes, dédupliqués, sérialisés) |
| **État partagé** | `useState('cle', () => init)` (sûr en SSR) |
| **Mises en page** | `layouts/default.vue`, `definePageMeta({ layout: 'admin' })` |
| **Middleware** | `middleware/auth.ts` (nommé ou global avec `.global.ts`) |
| **Serveur** | `server/api/bonjour.get.ts` → `GET /api/bonjour` |
| **Rendu hybride** | `routeRules` par route (`prerender`, `ssr: false`, `swr`, `isr`) |
| **Modules** | `@nuxt/image`, `@nuxt/content`, `@nuxtjs/i18n`, `@pinia/nuxt`, `@nuxt/ui`… |
| **SEO** | `useHead`, `useSeoMeta` |
| **Composants clients** | `<ClientOnly>`, suffixes `.client.vue` et `.server.vue` |
| **Déploiement** | Préréglages Nitro (Node, Vercel, Netlify, Cloudflare, statique…) |

```vue
<!-- app/pages/users/[id].vue -->
<script setup lang="ts">
const route = useRoute()
const { data: user, status, error } = await useFetch<Utilisateur>(`/api/users/${route.params.id}`)

useSeoMeta({ title: () => user.value?.nom ?? 'Utilisateur' })
definePageMeta({ middleware: 'auth' })
</script>

<template>
  <div v-if="status === 'pending'">Chargement…</div>
  <div v-else-if="error">Erreur</div>
  <h1 v-else>{{ user?.nom }}</h1>
</template>
```

```ts
// server/api/users/[id].get.ts
export default defineEventHandler(async (event) => {
  const id = getRouterParam(event, 'id')
  return { id, nom: 'Alice' }
})
```

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  modules: ['@pinia/nuxt', '@nuxt/image'],
  routeRules: {
    '/': { prerender: true },
    '/blog/**': { swr: 3600 },
    '/admin/**': { ssr: false },
  },
  runtimeConfig: { apiSecret: '', public: { apiBase: '/api' } },
})
```

- `runtimeConfig` : les clés **à la racine** restent **côté serveur** (secrets) ; seules celles sous `public` sont exposées au client.
- **`useFetch` / `useAsyncData`** évitent la double requête (serveur puis client) en **transférant** le résultat au client ; la clé d'identification permet la mise en cache et la déduplication. Dans Nuxt 4, les données retournées sont dans un **`shallowRef`** par défaut.

#### TypeScript dans Nuxt

Les types sont **générés automatiquement** (dossier `.nuxt/` : routes, composants, importations automatiques). Vérification : `npx nuxi typecheck`.

### 24.5 Génération statique et sites de contenu

- **Nuxt** : `nuxt generate` (pré-rendu de toutes les routes) et **Nuxt Content** (Markdown et composants dans le contenu).
- **VitePress** : générateur de sites statiques (documentation) fondé sur **Vite + Vue**, avec du contenu en **Markdown** pouvant intégrer des composants Vue.
- **vite-ssg** : génération statique pour des applications Vite + Vue Router.

### 24.6 Choisir le mode

| Besoin | Choix |
| --- | --- |
| Application interne, derrière une authentification | **SPA** |
| Site vitrine, blog, documentation | **SSG** (Nuxt Content, VitePress) |
| Commerce en ligne, contenu dynamique référencé | **SSR / hybride** (Nuxt) |
| Grosse application avec zones statiques et dynamiques | **Hybride** (`routeRules`) |

### 24.7 Pièges fréquents

- Utiliser `window` ou `document` **à la racine** de `<script setup>` en SSR.
- **État global partagé** entre requêtes serveur (variable de module).
- **Désaccord d'hydratation** (valeurs aléatoires, dates, langue).
- Provoquer des **requêtes en double** serveur + client (utilisez `useFetch` / `useAsyncData`).
- Exposer des secrets dans `runtimeConfig.public`.
- Oublier que `onMounted` ne s'exécute pas sur le serveur.

### Synthèse du chapitre 24

**CSR / SSR / SSG / hybride** : choisissez selon le référencement, le dynamisme et l'infrastructure. **Hydratation** : le HTML du serveur doit correspondre au premier rendu du client. **Nuxt** apporte routage par fichiers, importations automatiques, récupération de données isomorphe et serveur Nitro. Respectez le **code universel** et l'**isolation par requête**.

---

## 25. Outils et écosystème

**Objectifs d'apprentissage.** Connaître les outils officiels et incontournables ; choisir bibliothèques d'interface, utilitaires, formulaires, internationalisation, requêtes serveur ; gérer les variables d'environnement ; mettre en place la chaîne de qualité (lint, formatage, types, intégration continue) ; savoir où trouver l'information officielle.

### 25.1 Construction et outillage

| Outil | Rôle |
| --- | --- |
| **Vite** | Serveur de développement très rapide (modules ES natifs), construction (Rollup, ou Rolldown dans les versions récentes), HMR |
| **`@vitejs/plugin-vue`** | Compilation des SFC |
| **`create-vue`** | Génération officielle de projet |
| **Vue CLI** | **Héritage** (mode maintenance) |
| **Webpack / Rspack** | Alternatives (projets existants) |
| **`unplugin-*`** | `unplugin-auto-import`, `unplugin-vue-components`, `unplugin-icons` (le routage par fichiers est désormais dans Vue Router 5) |

#### Variables d'environnement (Vite)

```text
.env                # toutes les configurations
.env.local          # local (ignoré par Git)
.env.development
.env.production
```

```ts
import.meta.env.VITE_API_URL          // exposé au client (préfixe VITE_ obligatoire)
import.meta.env.MODE / DEV / PROD
```

> **Tout ce qui est exposé au client est public** : ne mettez **jamais de secrets** dans une variable `VITE_*`, ils seraient lisibles dans le bundle.

### 25.2 Outils de développement

| Outil | Description |
| --- | --- |
| **Vue DevTools** (extension, plugin Vite ou application autonome) | Inspecter composants, props, état, Pinia, routeur, chronologie, performances |
| **Vue - Official (Volar)** | Extension VS Code : coloration, types, autocomplétion de gabarit |
| **`vue-tsc`** | Vérification de types en ligne de commande |
| **ESLint** + **`eslint-plugin-vue`** + `typescript-eslint` | Analyse statique (règles `vue/…` : `essential`, `strongly-recommended`, `recommended`) |
| **Prettier**, **Oxlint**, **Biome** | Formatage et analyse rapide |
| **Husky + lint-staged** | Hooks Git avant commit |

### 25.3 Bibliothèques d'interface

| Bibliothèque | Caractéristiques |
| --- | --- |
| **Vuetify** | Material Design, très complète |
| **PrimeVue** | Large catalogue, thèmes, accessibilité |
| **Element Plus** | Interfaces d'entreprise |
| **Naive UI** | Pensée pour TypeScript, thèmes |
| **Quasar** | Framework complet (web, SSR, PWA, mobile, bureau) |
| **Nuxt UI** | Fondée sur Tailwind et Reka UI |
| **Ant Design Vue** | Design Ant |
| **Reka UI (ex-Radix Vue)**, **Headless UI** | Composants **sans style**, accessibles |
| **shadcn-vue** | Composants copiables, fondés sur Reka UI et Tailwind |

**Styles** : **Tailwind CSS**, **UnoCSS** (CSS atomique), **Sass / SCSS**, **CSS Modules**, **PostCSS**. **Icônes** : **Iconify** et `unplugin-icons`.

### 25.4 Utilitaires et composables

| Domaine | Outils |
| --- | --- |
| **Composables** | **VueUse** (`@vueuse/core`, `@vueuse/integrations`) |
| **Validation** | **Zod**, **Valibot**, **VeeValidate**, **FormKit**, **Vuelidate** |
| **Requêtes serveur** | **TanStack Query (Vue Query)**, **Pinia Colada**, `ofetch`, **Axios** |
| **Internationalisation** | **Vue I18n** (Nuxt : `@nuxtjs/i18n`) |
| **Dates** | **date-fns**, **Day.js**, `Intl`, `Temporal` |
| **Graphiques** | **Chart.js** (`vue-chartjs`), **ECharts** (`vue-echarts`), **D3** |
| **Tableaux** | **TanStack Table**, composants d'interface |
| **Éditeurs** | **TipTap**, **Quill** |
| **Cartes** | **Leaflet**, **MapLibre** |
| **Animations** | **GSAP**, **Motion**, **AutoAnimate**, `@vueuse/motion` |
| **Glisser-déposer** | **VueDraggable (SortableJS)** |
| **Temps réel** | WebSocket natif, **Socket.IO** |
| **GraphQL** | **Apollo (vue-apollo)**, **urql**, **Villus** |
| **Authentification** | **Auth.js / sidebase**, **Supabase**, **Firebase** |

**Requêtes serveur.** Pour le **cache**, la déduplication, le rafraîchissement et les états de chargement des requêtes, une bibliothèque dédiée (TanStack Query, Pinia Colada) est préférable à des requêtes écrites à la main dans un store.

### 25.5 Pinia, Router et extensions

- **Pinia** : `pinia-plugin-persistedstate`, `@pinia/colada`, `@pinia/testing`.
- **Vue Router** : routage par fichiers intégré (v5), `vue-router-mock` pour les tests.

### 25.6 Tests

**Vitest**, **Vue Test Utils**, **Testing Library**, **Playwright**, **Cypress**, **MSW**, **Storybook** (documentation et tests de composants).

### 25.7 Documentation et système de conception

- **Storybook** : catalogue interactif de composants.
- **Histoire** : alternative native à Vue.
- **VitePress** : documentation.
- **VueUse** : exemple de bibliothèque de composables bien documentée.

### 25.8 Mobile et bureau

| Cible | Solutions |
| --- | --- |
| **Mobile hybride** | **Capacitor**, **Ionic Vue**, **Quasar** |
| **Mobile natif** | **NativeScript-Vue**, **Vue Native** (communautaire) |
| **Bureau** | **Tauri**, **Electron** |
| **PWA** | `vite-plugin-pwa` |
| **Extensions de navigateur** | `vite-plugin-web-extension` |

### 25.9 Chaîne de qualité (intégration et déploiement continus)

```yaml
# Exemple GitHub Actions (extrait)
steps:
  - uses: actions/checkout@v4
  - uses: actions/setup-node@v4
    with: { node-version: 'lts/*', cache: npm }
  - run: npm ci
  - run: npm run lint
  - run: npx vue-tsc --noEmit
  - run: npm run test -- --run --coverage
  - run: npm run build
```

Autres pratiques : **Conventional Commits**, **Renovate** ou **Dependabot** (mises à jour de dépendances), analyse de sécurité (`npm audit`), **budgets de performance**, **Lighthouse CI**.

### 25.10 Ressources officielles

- Documentation : <https://vuejs.org> (guide, API, exemples, tutoriel interactif)
- **Terrain de jeu des SFC** : <https://play.vuejs.org>
- Routeur : <https://router.vuejs.org> · Pinia : <https://pinia.vuejs.org> · Vite : <https://vite.dev> · Nuxt : <https://nuxt.com>
- VueUse : <https://vueuse.org> · Vue Test Utils : <https://test-utils.vuejs.org> · VitePress : <https://vitepress.dev>
- Communauté : Discord Vue Land, GitHub Discussions, **RFC** (`github.com/vuejs/rfcs`), Vue.js Newsletter, conférences (VueConf, Vue.js Amsterdam, VueDay).

### 25.11 Pièges fréquents

- Choisir une bibliothèque **sans vérifier** sa compatibilité avec Vue 3, TypeScript et SSR.
- Exposer des secrets dans les variables `VITE_*`.
- Multiplier les dépendances pour des besoins couverts par **VueUse** ou le navigateur.
- Négliger les **mises à jour de sécurité** des dépendances.
- Utiliser des outils **abandonnés** (Vue CLI, Vuex, Vetur) dans un nouveau projet.

### Synthèse du chapitre 25

**Vite + Vue DevTools + Vue - Official + ESLint + `vue-tsc`** forment le socle de développement. **Pinia, Vue Router, VueUse et Vitest** sont les briques officielles ou quasi officielles ; **Nuxt** couvre le full-stack et le SSR. Choisissez vos bibliothèques selon **accessibilité, typage, maintenance et taille**.

---

## 26. Bonnes pratiques et architecture

**Objectifs d'apprentissage.** Structurer un projet Vue de façon évolutive ; appliquer le **guide de style officiel** ; adopter des conventions de nommage et de typage ; concevoir des composants cohérents ; choisir où placer l'état ; gérer erreurs, accessibilité, sécurité et internationalisation ; migrer de Vue 2 vers Vue 3 ; disposer de listes de contrôle de revue de code et de mise en production.

### 26.1 Organiser le projet

#### Par type technique (petits projets)

```text
src/
├── assets/          ├── components/      ├── composables/
├── router/          ├── stores/          ├── views/
├── services/ (API)  ├── types/           └── utils/
```

#### Par fonctionnalité (*feature-based*, projets moyens et grands) *(recommandé)*

```text
src/
├── app/                     # initialisation : main.ts, router, providers, styles globaux
├── shared/                  # briques transverses
│   ├── ui/                  # composants de base (BaseButton, BaseModal…)
│   ├── composables/         # useDebounce, useEventListener…
│   ├── lib/                 # client HTTP, utilitaires purs
│   └── types/
└── features/
    ├── auth/
    │   ├── components/      # LoginForm.vue
    │   ├── composables/     # useAuth.ts
    │   ├── stores/          # auth.store.ts
    │   ├── api.ts           # appels réseau de la fonctionnalité
    │   ├── routes.ts        # routes de la fonctionnalité
    │   ├── types.ts
    │   └── index.ts         # API publique de la fonctionnalité
    └── panier/ …
```

**Principes**

- **Colocalisation** : ce qui change ensemble vit ensemble.
- **Dépendances à sens unique** : `features` → `shared`, **jamais** l'inverse ; une fonctionnalité n'importe pas les éléments **internes** d'une autre (seulement son `index.ts`).
- **Vues (`views` ou `pages`)** : assemblent des composants et branchent les données ; peu de logique.
- **Composants de présentation** (props → rendu, événements) et **composants conteneurs** (accès au store, requêtes).
- Une **couche d'accès à l'API** (`api.ts`, `services/`) : les composants n'appellent pas `fetch` directement.

### 26.2 Le guide de style officiel (résumé par priorités)

#### Priorité A — Essentielles (évitent les erreurs)

- Noms de composants **multi-mots** (sauf `App` et les composants intégrés).
- Définition **détaillée** des props (types, `required`, valeurs par défaut).
- **`key`** dans les `v-for`.
- **Pas de `v-if` avec `v-for`** sur le même élément.
- **Styles `scoped`** (ou modules) pour les composants.
- **Éviter l'état partagé implicite** et les noms de propriétés privées conflictuels.

#### Priorité B — Fortement recommandées (lisibilité)

- **Un composant par fichier**.
- Noms de fichiers **cohérents** (PascalCase ou kebab-case).
- Préfixe des composants **de base** (`Base`, `App`, `V`), des composants **uniques** (`The`), des composants **étroitement couplés** (`TodoList` → `TodoListItem`).
- Ordre des mots dans les noms : **du général au particulier** (`SearchButtonClear`).
- Composants **auto-fermants** dans les SFC (`<MonComposant />`).
- Casse dans les gabarits : **PascalCase** pour les composants, **kebab-case** pour les props et événements.
- Expressions de gabarit **simples** (déplacer la logique dans des propriétés calculées).
- Propriétés calculées **simples**, attributs **entre guillemets**, raccourcis de directives **systématiques** (`:`, `@`, `#`).

#### Priorité C — Recommandées (cohérence)

- **Ordre des options** et des attributs sur les éléments (`v-if`, `v-for`, `key`, `ref`, `v-model`, `:props`, `@événements`…).
- **Ordre des blocs** de SFC (`script`, `template`, `style`).

#### Priorité D — À utiliser avec précaution (modèles risqués)

- `v-if` avec `v-else` sans `key` ; sélecteurs d'élément dans `scoped` ; communication implicite parent-enfant ; accès à `$parent` ; état global hors Pinia.

### 26.3 Conception des composants

- **Responsabilité unique** : un composant fait **une chose**. Si le nom contient « et » ou si le fichier dépasse quelques centaines de lignes, découpez.
- **Props descendantes, événements montants** ; **aucune mutation** de props.
- **Préférez la composition à la configuration** : slots plutôt qu'une quarantaine de props pour décrire le contenu.
- **Contrats clairs** : props typées, événements déclarés, slots documentés.
- **Composants de base accessibles** : un `BaseButton`, `BaseInput`, `BaseModal` bien conçus évitent de répéter les mêmes attributs ARIA.
- **Logique extraite** en composables ; **accès aux données** dans une couche dédiée.
- **Limitez la profondeur** de l'arbre et le nombre de props (au-delà de 6 à 8, repensez le découpage).

### 26.4 Où placer l'état ?

| Portée | Emplacement |
| --- | --- |
| **Local** à un composant | `ref` / `reactive` |
| **Parent → enfants proches** | Props + événements, `v-model` |
| **Sous-arbre** | `provide` / `inject`, composable partagé |
| **Global ou partagé** | **Pinia** |
| **Dans l'URL** | Paramètres et requêtes de route (filtres, pagination, onglet) |
| **Données serveur** | Bibliothèque de requêtes (cache, déduplication) |
| **Persistant** | `localStorage` (`useStorage`), cookies |

**Mettez dans l'URL ce qui doit pouvoir être partagé ou restauré** (filtres, page courante) ; **dérivez** plutôt que de dupliquer : un état dérivé est un `computed`, jamais un second état synchronisé à la main.

### 26.5 TypeScript au quotidien

- `strict: true` ; **pas de `any`** (préférez `unknown` et le rétrécissement de type).
- **Types d'API** dans un module partagé ; **validation à l'exécution** (Zod, Valibot) aux frontières.
- Types **nominaux** (types de marque) pour les identifiants si nécessaire (`type UserId = number & { __brand: 'UserId' }`).
- **Unions discriminées** pour modéliser les états : `{ status: 'chargement' } | { status: 'ok'; data: T } | { status: 'erreur'; erreur: Error }`.
- Typer les **props, événements, slots et injections** (chapitre 19).
- `vue-tsc` en **intégration continue**.

```ts
type EtatRequete<T> =
  | { statut: 'inactif' }
  | { statut: 'chargement' }
  | { statut: 'succes'; donnees: T }
  | { statut: 'erreur'; erreur: Error }
```

Cette modélisation rend **impossibles** les états incohérents (par exemple `chargement` et `erreur` simultanés).

### 26.6 Conventions de code

| Élément | Convention |
| --- | --- |
| Composants | `PascalCase.vue`, multi-mots |
| Composables | `useXxx.ts` |
| Stores | `useXxxStore` (fichier `xxx.store.ts` ou `xxx.ts`) |
| Props dans le gabarit | `kebab-case` |
| Événements | verbes ou faits (`soumettre`, `selection-change`) |
| Constantes | `MAJUSCULES_SOULIGNEES` |
| Types et interfaces | `PascalCase` (sans préfixe `I`) |
| Directives | `vNomDirective` |
| Booléens | `estXxx`, `aXxx`, `peutXxx` |

Tout ce qui est **mécanisable** (formatage, imports, règles) doit l'être (Prettier, ESLint) : les revues de code se concentrent sur la conception.

### 26.7 Gestion des erreurs

- **Frontière d'erreur** : composant qui utilise `onErrorCaptured` et affiche un repli.
- **Gestionnaire global** : `app.config.errorHandler` pour la journalisation (Sentry, etc.).
- **Requêtes** : modélisez `chargement` / `erreur` / `succès`, annulez avec `AbortController`, affichez des messages **compréhensibles**.
- **Erreurs de navigation** : `router.onError`, route 404 (`/:pathMatch(.*)*`).
- **Ne masquez pas** les erreurs : journalisez avec du contexte (identifiant utilisateur anonymisé, route).

```vue
<!-- src/components/FrontiereErreur.vue -->
<script setup lang="ts">
import { onErrorCaptured, ref } from 'vue'

const erreur = ref<Error | null>(null)

onErrorCaptured((e) => {
  erreur.value = e as Error
  return false                    // stoppe la propagation
})
</script>

<template>
  <slot v-if="!erreur" />
  <div v-else role="alert">
    <p>Une erreur est survenue.</p>
    <button @click="erreur = null">Réessayer</button>
  </div>
</template>
```

### 26.8 Accessibilité (a11y)

- **HTML sémantique** (`<button>`, `<nav>`, `<main>`) avant les `role` et attributs ARIA.
- **Libellés** associés aux champs (`<label for>` + `useId`).
- **Navigation au clavier** : ordre de tabulation logique, focus visible, **gestion du focus** dans les modales (piège à focus, retour du focus à l'élément déclencheur) et après les navigations de route.
- **Messages dynamiques** annoncés (`aria-live`, `role="alert"`).
- **Contrastes** suffisants, texte alternatif des images, respect de `prefers-reduced-motion`.
- **Tests** : `eslint-plugin-vuejs-accessibility`, axe, Lighthouse, tests manuels au clavier et avec un lecteur d'écran.

### 26.9 Sécurité

- **XSS** : n'utilisez `v-html` qu'avec un contenu **assaini** (DOMPurify) ; ne construisez jamais de gabarits à partir d'une entrée utilisateur ; évitez d'injecter des valeurs non maîtrisées dans `href` (`javascript:`), `style` ou `srcdoc`.
- **Secrets** : jamais dans le code client (`VITE_*` est **public**).
- **Authentification** : préférez des **cookies `HttpOnly`** et `SameSite` aux jetons dans `localStorage` ; protection **CSRF** selon le mécanisme choisi.
- **Autorisations** : les gardes de routeur et directives type `v-can` ne sont que de **l'ergonomie** ; le serveur **applique** les droits.
- **Politique de sécurité du contenu (CSP)**, dépendances à jour (`npm audit`), intégrité des paquets (fichier de verrouillage).
- **SSR** : isolation par requête, échappement du JSON sérialisé dans la page.

### 26.10 Internationalisation et formats

- **Vue I18n** (`useI18n()`, `t('cle')`, pluriel, formats de nombres et de dates) ; **ne concaténez jamais** de phrases traduites.
- Utilisez `Intl.DateTimeFormat`, `Intl.NumberFormat` et `Intl.RelativeTimeFormat` pour les formats régionaux.
- Prévoyez les **langues écrites de droite à gauche** (propriétés logiques CSS : `margin-inline-start`) et l'**extensibilité du texte** (les traductions sont plus longues).

### 26.11 Migration de Vue 2 vers Vue 3

**Stratégie recommandée**

1. **Inventaire** : bibliothèques tierces, plugins, mixins, filtres, `Vuex`, `Vue CLI`.
2. **Mettre à jour** les dépendances compatibles Vue 3 ; remplacer les bibliothèques abandonnées.
3. Passer de **Vue CLI** à **Vite** (`create-vue`) ; de **Vuex** à **Pinia** ; de **Vetur** à **Vue - Official**.
4. **Corriger** les changements incompatibles (liste ci-dessous).
5. Migrer **progressivement** vers la Composition API et `<script setup>`, composant par composant.
6. Ajouter **TypeScript** par étapes (`allowJs`), en commençant par les nouveaux fichiers.

**Principaux changements incompatibles**

| Vue 2 | Vue 3 |
| --- | --- |
| `new Vue({…})` | `createApp(…)` |
| `Vue.use`, `Vue.component`, `Vue.prototype` | `app.use`, `app.component`, `app.config.globalProperties` |
| `Vue.set` / `this.$set`, `Vue.delete` | Inutiles (affectation directe) |
| `.sync` | `v-model:argument` |
| `v-model` (`value` / `input`) | `modelValue` / `update:modelValue` |
| Filtres (`{{ x \| f }}`) | **Supprimés** (fonctions ou propriétés calculées) |
| `$listeners` | Fusionné dans `$attrs` |
| `.native` | Supprimé (déclarez `emits`) |
| `beforeDestroy` / `destroyed` | `beforeUnmount` / `unmounted` |
| `v-for` prioritaire sur `v-if` | **`v-if` prioritaire** |
| `$on`, `$off`, `$once` (bus d'événements) | **Supprimés** (utiliser une bibliothèque ou un store) |
| Un seul élément racine | **Racines multiples** possibles |
| `Vue.config.productionTip`, `ignoredElements` | Supprimés ou renommés |
| Vuex | **Pinia** |

Les **outils** : le **build de compatibilité** `@vue/compat` (Vue 3 avec un mode de comportement Vue 2 et des avertissements ciblés) facilite une migration progressive pour de **grands** projets ; l'outil d'audit de migration officiel recense les points à traiter. Vue 2 n'étant **plus maintenu**, la migration est aussi une question de **sécurité**.

### 26.12 Liste de contrôle de revue de code

**Conception**

- [ ] Responsabilités claires ; composants ni trop gros ni trop nombreux.
- [ ] Pas de **duplication d'état** ; dérivations en `computed`.
- [ ] Flux de données : props descendantes, événements montants ; aucune mutation de prop.
- [ ] État au bon niveau (local, sous-arbre, global, URL).

**Qualité technique**

- [ ] `key` stables dans les `v-for` ; pas de `v-if` avec `v-for`.
- [ ] Écouteurs, minuteurs et requêtes **nettoyés**.
- [ ] Pas de `any` ; props, événements et slots typés ; données externes validées.
- [ ] Pas de fonction coûteuse dans le gabarit.
- [ ] Gestion des états de chargement, vide et erreur.

**Transversal**

- [ ] Accessibilité (clavier, libellés, ARIA, contrastes).
- [ ] Sécurité (`v-html`, secrets, autorisations côté serveur).
- [ ] Tests pertinents (comportement) ; textes **traduits**.
- [ ] Performance : chargement paresseux des routes et gros composants.

### 26.13 Liste de contrôle de mise en production

- [ ] `vue-tsc`, ESLint et tests **réussissent** en intégration continue.
- [ ] Build de production : taille du bundle analysée, découpage du code, sourcemaps conservés **hors** du public.
- [ ] Variables d'environnement vérifiées (aucun secret côté client).
- [ ] Repli serveur vers `index.html` (mode `createWebHistory`) ou rendu serveur configuré.
- [ ] **Suivi des erreurs** (Sentry…) et des performances (Web Vitals).
- [ ] En-têtes de sécurité (CSP, HSTS), cache (empreintes de fichiers, CDN), compression.
- [ ] Accessibilité et Lighthouse vérifiés ; balises `meta` et SEO (SSR / pré-rendu si nécessaire).
- [ ] Plan de **retour arrière** et surveillance après le déploiement.

### 26.14 Pièges fréquents

- **Sur-ingénierie** : introduire Pinia, des abstractions et des couches avant d'en avoir le besoin.
- **Sous-ingénierie** : composants de 1 000 lignes, état dupliqué, appels réseau dans les composants.
- Ignorer l'**accessibilité** jusqu'à la fin du projet.
- Dépendre de la **configuration du développeur** : sans lint, formatage et CI, les conventions ne tiennent pas.
- **Réinventer** ce que fournissent VueUse, Vue Router, Pinia ou la plateforme.
- Mélanger **plusieurs styles** (Options API, Composition API, mixins) sans règle d'équipe.

### Synthèse du chapitre 26

Organisez **par fonctionnalité**, appliquez le **guide de style officiel**, gardez des composants **petits, typés et accessibles**, placez l'état au **bon niveau**, **validez** aux frontières, **testez** le comportement et **automatisez** la qualité. Migrer de Vue 2 est une affaire de **dépendances et de conventions**, pas seulement de syntaxe.

---

# Annexes

## Annexe A — Glossaire

| Terme | Définition |
| --- | --- |
| **Action (Pinia)** | Fonction d'un store qui modifie l'état ou exécute une logique asynchrone |
| **Alias (routeur)** | URL alternative qui affiche la même route sans redirection |
| **Application (`createApp`)** | Instance racine qui porte la configuration, les plugins et le composant racine |
| **Argument (directive)** | Partie après `:` qui précise la cible (`v-bind:href`) |
| **`$attrs`** | Attributs et écouteurs non déclarés comme props ou `emits` |
| **Binding (liaison)** | Association entre une donnée et un attribut, un événement ou un texte |
| **Bundle** | Fichier(s) JavaScript produit(s) par la construction |
| **Cache (`computed`)** | Mémorisation d'une valeur dérivée tant que ses dépendances ne changent pas |
| **Chargement paresseux** | Téléchargement d'un code uniquement lorsqu'il est nécessaire |
| **Composable** | Fonction `useXxx` encapsulant une logique à état réactif |
| **Composant** | Unité d'interface réutilisable (gabarit + logique + style) |
| **Composition API** | API fondée sur des fonctions (`ref`, `computed`, `watch`, hooks) |
| **CSR / SSR / SSG** | Rendu côté client / serveur / statique à la compilation |
| **Dépendance (réactivité)** | Donnée lue par un effet, dont le changement le relance |
| **Directive** | Attribut `v-…` appliquant un comportement au DOM |
| **DOM virtuel** | Représentation en mémoire de l'arbre du DOM |
| **Effet** | Fonction dont les dépendances réactives sont suivies (rendu, `computed`, `watch`) |
| **`emit`** | Émission d'un événement vers le parent |
| **Fallthrough** | Transfert automatique des attributs non déclarés à l'élément racine |
| **Fragment** | Gabarit à plusieurs racines |
| **Garde de navigation** | Fonction qui autorise, annule ou redirige une navigation |
| **Getter** | Valeur dérivée d'un store (`computed`) ou fonction de lecture d'une source |
| **Hook** | Fonction de rappel liée à une étape du cycle de vie |
| **HMR** | Remplacement à chaud de modules, sans rechargement ni perte d'état |
| **Hydratation** | Rattachement de l'application au HTML produit par le serveur |
| **`InjectionKey`** | Clé typée (`Symbol`) pour `provide` / `inject` |
| **Interpolation** | Affichage d'une expression avec `{{ }}` |
| **Macro (compilateur)** | Instruction résolue à la compilation (`defineProps`…) |
| **`markRaw`** | Marque un objet comme jamais réactif |
| **Méta-framework** | Framework bâti sur un autre (Nuxt sur Vue) |
| **Mixin** | Objet d'options fusionné dans un composant (héritage, déconseillé) |
| **Modificateur** | Suffixe `.xxx` modifiant le comportement d'une directive |
| **Nitro** | Moteur de serveur de Nuxt |
| **Nœud virtuel (VNode)** | Objet décrivant un élément du DOM virtuel |
| **Options API** | API fondée sur un objet d'options (`data`, `methods`…) |
| **Patch flag** | Indicateur du compilateur précisant ce qui est dynamique dans un nœud |
| **Pinia** | Bibliothèque officielle de gestion d'état |
| **Plugin** | Extension installée avec `app.use` |
| **Prop** | Donnée transmise d'un parent à un enfant |
| **Prop drilling** | Transmission d'une prop à travers des composants intermédiaires inutiles |
| **Proxy** | Objet qui intercepte lecture et écriture d'un autre objet |
| **`provide` / `inject`** | Partage de données entre un ancêtre et ses descendants |
| **Réactivité** | Suivi automatique des dépendances et mise à jour des effets |
| **`ref`** | Référence réactive à une valeur (`.value`) |
| **Référence de gabarit** | Accès direct à un élément DOM ou à un composant |
| **Render function** | Fonction qui retourne des nœuds virtuels |
| **Renderless** | Composant sans rendu propre, qui délègue au slot |
| **SFC** | Composant monofichier `.vue` |
| **Slot** | Emplacement où le parent injecte du contenu |
| **Slot à portée** | Slot qui reçoit des données de l'enfant |
| **Store** | Conteneur d'état global (Pinia) |
| **Suspense** | Composant gérant les dépendances asynchrones |
| **Teleport** | Rendu d'un contenu à un autre endroit du DOM |
| **Tree-shaking** | Élimination du code inutilisé à la construction |
| **Vapor** | Mode de compilation sans DOM virtuel (Vue 3.6, optionnel) |
| **Vite** | Outil de développement et de construction |
| **`vue-tsc`** | Vérificateur de types pour les fichiers Vue |
| **VueUse** | Collection de composables utilitaires |

---

## Annexe B — Aide-mémoire

### B.1 Directives

| Directive | Exemple |
| --- | --- |
| Texte | `{{ x }}`, `v-text="x"`, `v-html="x"` |
| Liaison | `:src="x"`, `:class="{ a: ok }"`, `:style="{ color: c }"`, `v-bind="obj"`, `:src` (même nom) |
| Événement | `@click="f"`, `@click.stop.prevent`, `@keyup.enter`, `@click.ctrl.exact` |
| Condition | `v-if`, `v-else-if`, `v-else`, `v-show` |
| Liste | `v-for="(x, i) in xs" :key="x.id"` |
| Formulaire | `v-model`, `.lazy`, `.number`, `.trim` |
| Slot | `<slot name="a" :x="x">`, `#a="{ x }"` |
| Divers | `v-once`, `v-pre`, `v-memo="[a]"`, `v-cloak` |

### B.2 Réactivité

| API | Rôle |
| --- | --- |
| `ref(x)` / `reactive(o)` | État réactif |
| `computed(() => …)` | Valeur dérivée mise en cache |
| `watch(src, cb, opts)` | Réaction explicite |
| `watchEffect(fn)` | Réaction à suivi automatique |
| `toRef`, `toRefs`, `toValue`, `unref` | Conversions et lecture |
| `shallowRef`, `shallowReactive`, `triggerRef` | Réactivité superficielle |
| `readonly`, `toRaw`, `markRaw` | Protection et échappement |
| `customRef`, `effectScope` | Cas avancés |
| `nextTick`, `useTemplateRef`, `useId` | DOM et identifiants |

### B.3 Macros de `<script setup>`

```ts
const props = defineProps<{ a: string; b?: number }>()
const { a, b = 0 } = defineProps<{ a: string; b?: number }>()          // 3.5+
const emit = defineEmits<{ change: [v: number]; close: [] }>()
const modele = defineModel<string>()
defineExpose({ methode })
defineOptions({ name: 'X', inheritAttrs: false })
defineSlots<{ default(p: { x: number }): any }>()
```

### B.4 Hooks de cycle de vie

`onBeforeMount` · `onMounted` · `onBeforeUpdate` · `onUpdated` · `onBeforeUnmount` · `onUnmounted` · `onErrorCaptured` · `onActivated` · `onDeactivated` · `onServerPrefetch` · `onRenderTracked` · `onRenderTriggered` · `onWatcherCleanup` · `onScopeDispose`

### B.5 Vue Router

```ts
const route = useRoute()      // params, query, hash, name, meta, fullPath, matched
const router = useRouter()    // push, replace, go, back, addRoute, removeRoute, beforeEach…
onBeforeRouteLeave(() => {})
onBeforeRouteUpdate(() => {})
```

### B.6 Pinia

```ts
const s = useStore()
const { etat, getter } = storeToRefs(s)
const { action } = s
s.$patch({ x: 1 }); s.$reset(); s.$subscribe(cb); s.$onAction(cb)
```

### B.7 Commandes usuelles

| Commande | Rôle |
| --- | --- |
| `npm create vue@latest` | Nouveau projet |
| `npm run dev` / `build` / `preview` | Développement, production, prévisualisation |
| `npx vue-tsc --noEmit` | Vérification de types |
| `npx vitest` / `npx vitest run --coverage` | Tests |
| `npm create nuxt@latest` | Nouveau projet Nuxt |
| `npx playwright test` | Tests de bout en bout |

---

*Fin du cours.*
