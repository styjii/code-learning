# Next.js — Cours complet

*Cours magistral et module d'apprentissage exhaustif, fondé sur le plan « Cours complet Next.js — Du débutant à l'expert » — Next.js 16.4 (octobre 2026), React 19.3*

## Avant de commencer : comment utiliser ce cours

Ce cours développe, chapitre par chapitre, l'intégralité du plan en **25 chapitres**, regroupés en cinq parties : **Fondamentaux** (1 à 6), **Rendu, cache et mutations** (7 à 12), **Interface et optimisation** (13 à 15), **Applications de production** (16 à 20) et **Qualité et exploitation** (21 à 25).

Chaque chapitre suit la même trame : *objectifs d'apprentissage → notions et définitions → exemples de code commentés → pièges fréquents → glossaire → synthèse*. Le cours ne contient **aucun exercice** : il se concentre sur l'explication des concepts.

**Conventions de lecture**

- **(à jour)** : pratique moderne qui remplace une ancienne. **(héritage)** : ancienne approche, encore fréquente dans les projets existants. **(ajout)** : notion absente des anciens guides. **Version** : comportement qui a changé entre Next.js 13, 14, 15 et 16.
- Le code est écrit en **TypeScript**. Les exemples utilisent l'**App Router** (dossier `app/`) ; le Pages Router est traité au chapitre 23.
- Chaque exemple est volontairement **autonome** : les imports nécessaires sont toujours indiqués. Les fonctions comme `db`, `getPost` ou `verifySession` désignent des fonctions **fictives** de votre application.
- Le cours enseigne le Next.js **actuel** (App Router, Server Components, Cache Components avec `"use cache"`, Server Actions, `proxy.ts`, Turbopack) **et** explique l'ancien (Pages Router, `getServerSideProps`, `middleware.ts`, options de `fetch`) pour que vous sachiez lire du code existant.

**Parcours conseillé** : lisez les chapitres 1 à 6 dans l'ordre (ils se construisent les uns sur les autres), puis les chapitres 7 à 9 (cache, rendu, mutations), qui forment le cœur du modèle mental de Next.js. Choisissez ensuite librement dans le reste selon vos besoins.

**Prérequis** : JavaScript moderne (ES2020+ : modules, `async` / `await`, déstructuration), bases de **React** (composants, props, état, hooks `useState` / `useEffect`), HTML / CSS, notions de **HTTP** (méthodes, codes de statut, en-têtes, cookies). TypeScript est un plus.

> **À propos des versions.** Next.js évolue vite, surtout sur le cache et la navigation. Ce cours distingue le **modèle actuel** (Cache Components, recommandé depuis Next.js 16.4 et annoncé comme futur défaut de Next.js 17) du **modèle classique** (cache implicite des versions 13 et 14, options de `fetch`). En cas de doute sur un détail d'API, la documentation officielle (<https://nextjs.org/docs>) de votre version fait foi.

---

## 1. Introduction et installation

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : définir Next.js et expliquer ce qui le distingue de React seul ; décrire les limites d'une application monopage et ce que le rendu serveur y change ; distinguer les trois environnements d'exécution (build, serveur, client) ; décrire le cycle de vie d'une requête ; comprendre le calendrier des versions ; installer un projet, lancer les commandes essentielles et lire le résultat d'un build.

### 1.1 Qu'est-ce que Next.js ?

**Next.js** est un **framework full-stack** open source, développé par **Vercel** et une large communauté, construit sur **React**. Il permet de bâtir des sites et des applications web qui s'exécutent **à la fois sur le serveur et dans le navigateur**, avec un seul langage (JavaScript / TypeScript) et une seule base de code.

**Framework ou bibliothèque ?** **React** est une *bibliothèque* : elle sait décrire une interface (composants, état, rendu) et rien d'autre. Elle ne dit rien sur :

- le **routage** (quelle page pour quelle URL ?) ;
- le **rendu côté serveur** (comment produire du HTML avant l'arrivée du JavaScript ?) ;
- la **récupération de données** (où et quand charger les données ?) ;
- le **découpage du code** (*code splitting*), le **bundling** et l'**optimisation** des images, polices et scripts ;
- le **back-end** (API, authentification, accès à une base de données) ;
- le **déploiement**.

Next.js apporte des réponses **cohérentes et éprouvées** à toutes ces questions. Il est dit **opinionné** (*opinionated*) : il impose des **conventions** (par exemple, l'organisation des fichiers détermine les URLs) qui réduisent le nombre de décisions à prendre et rendent deux projets Next.js semblables entre eux.

| Brique | Rôle | Chapitre |
| --- | --- | --- |
| **Routage par fichiers** | Une URL = un dossier | 3, 4 |
| **Server Components / Client Components** | Décider où s'exécute chaque composant | 5 |
| **Récupération de données** | Charger les données côté serveur | 6 |
| **Cache et revalidation** | Éviter le travail inutile | 7 |
| **Stratégies de rendu** | Statique, dynamique, partiel | 8 |
| **Server Actions** | Mutations depuis l'interface | 9 |
| **Route Handlers** | Endpoints HTTP, webhooks | 10 |
| **Proxy** | Interception des requêtes | 11 |
| **Navigation** | Liens, prefetching, historique | 12 |
| **Styles, images, polices, scripts** | Interface et optimisation | 13, 14 |
| **Métadonnées / SEO** | Référencement et partage | 15 |
| **Authentification, i18n, configuration** | Fonctions transverses | 16 à 19 |
| **Tests, déploiement** | Qualité et exploitation | 21, 22 |

### 1.2 Le problème des applications monopages (SPA)

Une **SPA** React « classique » (créée avec Vite ou l'ancien Create React App) envoie au navigateur un HTML presque vide :

```html
<body>
    <div id="root"></div>
    <script src="/bundle.js"></script>
</body>
```

Le navigateur doit alors **télécharger** le bundle JavaScript, l'**exécuter**, **appeler des API** pour récupérer les données, puis **afficher** l'interface. Conséquences :

| Problème | Explication |
| --- | --- |
| **Affichage tardif** | L'utilisateur voit une page blanche tant que le JavaScript n'est pas chargé et exécuté (mauvais *First Contentful Paint* et *Largest Contentful Paint*). |
| **SEO fragile** | Les robots doivent exécuter du JavaScript pour voir le contenu ; les réseaux sociaux (aperçus de liens) ne le font généralement pas. |
| **Cascades (*waterfalls*)** | Bundle → composant → requête de données → sous-composant → autre requête : chaque étape attend la précédente. |
| **Bundle volumineux** | Tout le code, y compris la logique qui pourrait rester sur le serveur, est envoyé au navigateur. |
| **Secrets impossibles** | Aucune clé d'API ne peut être utilisée dans le navigateur sans être exposée. |

Next.js résout ces problèmes en **rendant les composants React sur le serveur**, en envoyant du **HTML déjà complet** et en n'envoyant au navigateur **que le JavaScript nécessaire** à l'interactivité.

### 1.3 Fonctionnalités clés

1. **Routage par système de fichiers** (App Router et Pages Router).
2. **React Server Components (RSC)** : composants exécutés uniquement côté serveur.
3. **Rendu hybride** : chaque route (et, avec Cache Components, chaque composant) peut être statique, dynamique ou les deux.
4. **Streaming** : envoi progressif de l'interface avec `Suspense`.
5. **Server Actions / Server Functions** : fonctions serveur appelables depuis l'interface, pour les mutations.
6. **Route Handlers** : endpoints HTTP personnalisés.
7. **Optimisations intégrées** : `next/image`, `next/font`, `next/script`, préchargement des liens.
8. **Proxy** (anciennement Middleware) : interception des requêtes.
9. **Bundlers** : **Turbopack** (par défaut depuis Next.js 16) ou Webpack.
10. **TypeScript**, **ESLint**, variables d'environnement, **i18n**, **métadonnées / SEO**, images Open Graph.

### 1.4 Historique et versions *(à jour)*

Next.js suit le **versionnement sémantique**. Une version majeure paraît environ **une fois par an** (octobre), accompagnée de versions mineures plus fréquentes. Depuis l'été 2026, l'équipe applique aussi un **programme formel de versions de sécurité** : des correctifs de sécurité sont publiés régulièrement, annoncés à l'avance, pour les lignes de versions encore maintenues.

| Version | Date | Apports majeurs |
| --- | --- | --- |
| 1.0 | 2016 | Rendu serveur React, routage par fichiers (`pages/`) |
| 9 – 12 | 2019–2021 | API Routes, SSG / ISR, `next/image`, Middleware |
| **13** | 2022 | **App Router** (bêta) : layouts imbriqués, Server Components, streaming ; Turbopack (alpha) |
| **13.4** | 2023 | App Router déclaré stable |
| **14** | oct. 2023 | **Server Actions** stables, Partial Prerendering (aperçu) |
| **15** | oct. 2024 | React 19, API de requête **asynchrones**, `fetch` **non mis en cache par défaut**, `after()` |
| **16** | oct. 2025 | **Cache Components** (`"use cache"`), **Turbopack par défaut**, `proxy.ts`, React Compiler stable, `updateTag`, `refresh` |
| 16.1 | déc. 2025 | Cache disque de Turbopack en développement |
| 16.2 | mars 2026 | Adaptateurs de build, rendu plus rapide, meilleurs écrans d'erreur |
| **16.3** | juin–août 2026 | **Instant Navigations** (*Partial Prefetching*, Instant Insights, ISR amélioré), cache disque pour `next build`, `catchError`, *root params*, jusqu'à 90 % de mémoire en moins en développement |
| **16.4** | oct. 2026 | Cache Components **recommandé pour toute application** et activé par défaut dans `create-next-app` ; `ensureStatic`, `navigation()`, `prefetch()` ; React 19.3 |

> **Direction du projet.** L'équipe a annoncé que **Cache Components deviendra le modèle par défaut de Next.js 17**. Le cours enseigne donc ce modèle comme référence, et le modèle classique comme héritage à connaître.

**Quelle version utiliser ?** La plus récente (ici, **16.4**), en installant régulièrement les correctifs de sécurité de votre ligne de versions (chapitre 24).

### 1.5 Les trois environnements d'exécution

Comprendre **où** le code s'exécute est la clé de Next.js. Un même fichier peut s'exécuter dans plusieurs environnements.

| Environnement | Quand ? | Où ? | Exemples |
| --- | --- | --- | --- |
| **Build** (compilation) | Lors de `next build` | Machine de build / CI | Génération des pages statiques, `generateStaticParams` |
| **Serveur** (*runtime*) | À chaque requête (ou à la revalidation) | Serveur Node.js, serverless, edge | Server Components dynamiques, Route Handlers, Server Actions, Proxy |
| **Client** | Dans le navigateur | Navigateur de l'utilisateur | Client Components : `useState`, événements, `window` |

**Cycle de vie simplifié d'une requête (App Router) :**

1. Le navigateur demande `GET /blog/mon-article`.
2. *(Optionnel)* Le **Proxy** intercepte la requête : redirection, réécriture, en-têtes.
3. Next.js détermine la **route** correspondante dans `app/`.
4. Les **Server Components** s'exécutent, récupèrent leurs données et produisent un **payload RSC** : une description sérialisée de l'arbre React.
5. Next.js génère le **HTML** à partir de ce payload et l'envoie, éventuellement **par morceaux** (*streaming*).
6. Le navigateur **affiche** le HTML immédiatement : la page est visible.
7. Le JavaScript des **Client Components** est téléchargé, puis **hydraté** : React « attache » les gestionnaires d'événements au HTML existant, ce qui rend la page interactive.
8. Les navigations suivantes se font **côté client** : seul le payload RSC des segments modifiés est demandé au serveur.

> **Hydratation.** Processus par lequel React rend interactif un HTML déjà produit par le serveur, en associant l'arbre de composants au DOM existant. Si le HTML du serveur et le premier rendu du client diffèrent, on obtient une **erreur d'hydratation** (*hydration mismatch*, voir 5.10).

### 1.6 Rappel : les nouveautés de React utiles à Next.js

Next.js 15 et 16 s'appuient sur React 19.x ; Next.js 16.4 embarque **React 19.3**. À connaître :

- **Actions** : fonctions asynchrones passées à `<form action={...}>` ou déclenchées dans une transition.
- **`useActionState`**, **`useFormStatus`**, **`useOptimistic`** (chapitre 9).
- **`use(promise)`** / **`use(context)`** : lit une promesse ou un contexte ; peut être appelé de façon conditionnelle.
- **`ref` comme prop** dans les composants fonction (plus besoin de `forwardRef`).
- **Métadonnées natives** : `<title>`, `<meta>`, `<link>` rendus depuis n'importe quel composant.
- **React 19.2** : `<Activity>`, `useEffectEvent`, première version des **View Transitions**.
- **React 19.3** : **View Transitions** stables, *Fragment Refs*.
- **React Compiler** (1.0) : mémoïsation automatique, activable dans Next.js (chapitre 14).

### 1.7 Prérequis système *(à jour)*

- **Node.js** : version **20.9 ou plus récente** (Node 18 n'est plus supporté depuis Next.js 16).
- **TypeScript** (si utilisé) : version **5.1 ou plus** ; **TypeScript 7** (port natif, beaucoup plus rapide) peut servir à la vérification de types pendant `next build` depuis Next.js 16.3.
- **Navigateurs** : versions récentes de Chrome, Edge, Firefox et Safari.
- **Gestionnaire de paquets** : npm, pnpm, yarn ou bun.

### 1.8 Créer un projet

```bash
npx create-next-app@latest mon-app
```

L'assistant pose des questions (les valeurs par défaut suffisent pour débuter) :

| Question | Signification |
| --- | --- |
| TypeScript ? | Génère `tsconfig.json` et des fichiers `.tsx` |
| Linter ? | ESLint (ou Biome selon les options) |
| React Compiler ? | Active la mémoïsation automatique |
| Tailwind CSS ? | Installe et configure Tailwind |
| Dossier `src/` ? | Place le code dans `src/` |
| App Router ? | Recommandé : oui |
| Alias d'import (`@/*`) ? | Permet `import x from "@/lib/x"` |

> **Version 16.4.** Les nouveaux projets créés avec `create-next-app` ont **Cache Components activé par défaut** (`cacheComponents: true`). Si vous reprenez du code écrit pour un ancien modèle, certaines options de segment (`export const dynamic`, `revalidate`…) ne sont pas compatibles : voir chapitres 7 et 8.

Lancement :

```bash
cd mon-app
npm run dev      # serveur de développement sur http://localhost:3000
```

**Scripts de `package.json` :**

```json
{
    "scripts": {
        "dev": "next dev",
        "build": "next build",
        "start": "next start",
        "lint": "eslint"
    }
}
```

| Commande | Rôle |
| --- | --- |
| `next dev` | Serveur de développement avec **Fast Refresh** (rechargement à chaud qui conserve l'état React) |
| `next build` | Compilation de production : optimisation, génération statique, analyse des routes |
| `next start` | Démarre le serveur de production (après `build`) |
| `next info` | Affiche des informations de diagnostic (versions, système) |
| `next typegen` | Génère les types de routes (chapitre 20) |
| `next upgrade` | Met à niveau Next.js ; l'option `--agent` prépare une mise à niveau assistée par un agent de codage |

> **Version 16.** `next lint` a été **retiré** : on appelle ESLint directement. De plus, `next build` n'exécute plus le lint automatiquement.

### 1.9 Turbopack et Webpack *(à jour)*

- **Turbopack** est un bundler écrit en **Rust**, **par défaut** pour `next dev` et `next build` depuis Next.js 16.
- Pour utiliser Webpack : `next dev --webpack` et `next build --webpack`.
- Turbopack propose un **cache sur système de fichiers** : en développement depuis 16.1, il fonctionne aussi pour `next build` et est activé par défaut depuis **16.3**, ce qui accélère nettement les builds répétés (surtout en CI).
- Depuis 16.3, une **éviction mémoire** réduit fortement la consommation de RAM des longues sessions de développement.
- Certains loaders Webpack spécifiques peuvent être incompatibles : consultez la table de compatibilité de la documentation.

### 1.10 Ce que fait `next build`

À la fin d'un build, Next.js affiche un **tableau des routes** avec leur mode de rendu (symboles tels que ○ statique, ● SSG avec `generateStaticParams`, ƒ dynamique, ◐ partiellement pré-rendu selon la version). Lire ce tableau permet de **vérifier que vos routes sont statiques ou dynamiques comme prévu**, et de voir la taille du JavaScript chargé pour chaque route (« First Load JS »).

### 1.11 Pièges fréquents

- **Confondre développement et production.** Certains comportements (préchargement des liens, cache) diffèrent en développement. Testez toujours avec `build` + `start`.
- **Mauvaise version de Node.** Les erreurs de build sont alors obscures.
- **Oublier que code serveur et code client coexistent.** Une API du navigateur (`window`) appelée dans un composant serveur provoque une erreur.
- **Suivre un tutoriel ancien.** `getServerSideProps`, `pages/`, `middleware.ts`, `fetch` mis en cache par défaut : autant de signes d'un contenu antérieur à Next.js 15 (voir 23.6 pour dater un exemple).

### 1.12 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| Framework full-stack | Outil qui couvre l'interface **et** le serveur dans un même projet |
| SPA / MPA | Application monopage / multipage |
| RSC | *React Server Components* : composants exécutés uniquement sur le serveur |
| Payload RSC | Représentation sérialisée de l'arbre de composants envoyée au navigateur |
| Hydratation | Activation d'un HTML pré-rendu en y attachant React |
| Streaming | Envoi progressif du HTML et du payload RSC |
| Turbopack | Bundler écrit en Rust, par défaut depuis Next.js 16 |
| Fast Refresh | Rechargement à chaud conservant l'état React |
| Cache Components | Modèle de cache **explicite** fondé sur `"use cache"` |
| First Load JS | Quantité de JavaScript chargée pour afficher une route |

### Synthèse du chapitre 1

Next.js est un **framework full-stack opinionné** construit sur React : routage, rendu serveur, données, optimisations et déploiement dans un seul outil. Il combine **trois environnements** (build, serveur, client) et repose sur des **Server Components** qui n'envoient au navigateur que le nécessaire. L'actuel (16.4) s'appuie sur **Turbopack**, **Cache Components** et **React 19.3** ; installez avec `create-next-app`, développez avec `next dev`, et vérifiez toujours le résultat avec `next build` + `next start`.

---

## 2. Structure d'un projet

**Objectifs d'apprentissage.** Connaître le rôle de chaque dossier et fichier de la racine d'un projet ; appliquer les conventions de **colocation**, de **dossiers privés** et de **groupes de routes** ; choisir une stratégie d'organisation du code ; configurer les **alias d'import** ; connaître les fichiers de configuration courants.

### 2.1 Arborescence type

```text
mon-app/
├── app/                      # App Router : routes et interface
│   ├── layout.tsx            # Layout racine (obligatoire)
│   ├── page.tsx              # Route "/"
│   ├── globals.css
│   ├── favicon.ico
│   └── ...
├── public/                   # Fichiers statiques
├── components/               # (convention) composants partagés
├── lib/                      # (convention) utilitaires, accès aux données
├── next.config.ts            # Configuration de Next.js
├── proxy.ts                  # (optionnel) Proxy, ex-middleware.ts
├── instrumentation.ts        # (optionnel) observabilité
├── tsconfig.json
├── eslint.config.mjs
├── package.json
├── .env.local                # Variables d'environnement locales (non commité)
├── .gitignore
└── next-env.d.ts             # Types générés par Next.js (ne pas modifier)
```

**Fichiers et dossiers de la racine**

| Élément | Rôle |
| --- | --- |
| `app/` | Routes de l'**App Router** |
| `pages/` | Routes du **Pages Router** *(héritage)* |
| `public/` | Fichiers statiques servis à la racine du site : `public/logo.png` → `/logo.png` |
| `src/` | Dossier **optionnel** qui regroupe `app/`, `components/`, `lib/`… |
| `next.config.ts` (ou `.js` / `.mjs`) | Configuration (chapitre 18) |
| `proxy.ts` | Interception des requêtes ; **Version 16** : remplace `middleware.ts` |
| `instrumentation.ts` | Code exécuté au démarrage du serveur (monitoring, OpenTelemetry) |
| `.next/` | Sortie du build et du cache : **à ignorer dans Git** |
| `.env*` | Variables d'environnement (chapitre 19) |
| `next-env.d.ts` | Déclarations de types ; régénéré automatiquement |
| `AGENTS.md` | *(ajout, 16.3)* Fichier maintenu par `next dev` pour guider les agents de codage vers la documentation correspondant à votre version |

### 2.2 Le dossier `public/`

Tout fichier placé dans `public/` est servi **tel quel** à partir de la racine du site. Usages : favicon, images statiques, polices, fichiers de vérification de domaine, `robots.txt` (ou sa génération par `app/robots.ts`, chapitre 15).

```tsx
<img src="/logo.png" alt="Logo" />   {/* fichier public/logo.png */}
```

> **Attention.** Ne mettez **jamais** de données sensibles dans `public/` : tout y est accessible publiquement. Si un fichier change, **renommez-le ou versionnez-le** pour éviter qu'un cache (navigateur ou CDN) serve l'ancienne version.

### 2.3 Le dossier `src/`

Si vous choisissez `src/`, la structure devient `src/app/`, `src/components/`, `src/lib/`. Seuls les fichiers de configuration (`next.config.ts`, `package.json`, `tsconfig.json`, fichiers `.env`) restent à la **racine**. **`proxy.ts` se place dans `src/`** à côté de `app/`.

### 2.4 Conventions de nommage dans `app/`

Dans `app/`, certains **noms de fichiers sont réservés** (chapitre 4) : `page`, `layout`, `loading`, `error`, `not-found`, `route`, `template`, `default`, etc. Les extensions supportées sont `.js`, `.jsx`, `.ts` et `.tsx`. Les noms de dossiers déterminent les segments d'URL (chapitre 3).

### 2.5 La colocation

Dans l'App Router, **un dossier n'est accessible publiquement que s'il contient un fichier `page` ou `route`**. Vous pouvez donc placer côte à côte composants, styles, tests et utilitaires dans le dossier d'une route sans les exposer :

```text
app/blog/
├── page.tsx              # → /blog
├── BlogCard.tsx          # non routable
├── blog.module.css       # non routable
└── utils.ts              # non routable
```

**La colocation** garde ensemble ce qui change ensemble : en supprimant le dossier d'une fonctionnalité, vous supprimez aussi ses composants et ses styles.

**Dossiers privés.** Préfixer un dossier par `_` l'**exclut explicitement du routage** et signale son caractère privé :

```text
app/
├── _components/Header.tsx    # jamais une route
└── _lib/db.ts
```

Pour qu'une URL commence réellement par un underscore, on l'encode : `%5Ffichier`.

**Groupes de routes.** Un dossier `(nom)` regroupe des routes **sans modifier l'URL** (chapitre 3).

### 2.6 Organisation recommandée

Trois stratégies courantes :

1. **Tout en dehors de `app/`** : `app/` ne contient que le routage ; `components/`, `lib/`, etc. sont à la racine ou dans `src/`.
2. **Dossiers partagés dans `app/`** : `app/_components`, `app/_lib`.
3. **Découpage par fonctionnalité (*feature-based*)** : `features/auth/`, `features/billing/` avec leurs composants, actions et schémas ; `app/` se contente de les importer.

Choisissez **une** stratégie et appliquez-la de façon cohérente dans toute l'équipe.

| Dossier conventionnel | Contenu typique |
| --- | --- |
| `components/` | Composants d'interface réutilisables (boutons, cartes) |
| `lib/` | Fonctions utilitaires, client de base de données, schémas |
| `lib/dal.ts` | Couche d'accès aux données (chapitre 6) |
| `actions/` ou `actions.ts` | Server Actions (chapitre 9) |
| `hooks/` | Hooks personnalisés (Client Components) |
| `types/` | Types partagés |

### 2.7 Alias d'import

Dans `tsconfig.json` (ou `jsconfig.json`) :

```json
{
    "compilerOptions": {
        "baseUrl": ".",
        "paths": { "@/*": ["./src/*"] }
    }
}
```

Usage : `import { db } from "@/lib/db";` au lieu de `../../../lib/db`. Next.js lit automatiquement ces `paths`.

### 2.8 Fichiers de configuration courants

- **`next.config.ts`** : options de Next.js (chapitre 18).
- **`eslint.config.mjs`** : configuration ESLint au format « flat config ».
- **`postcss.config.mjs`** : utilisé notamment par Tailwind CSS.
- **`tsconfig.json`** : configuration TypeScript (chapitre 20).
- **`.gitignore`** : doit ignorer `.next/`, `node_modules/`, `.env*.local`.
- **`instrumentation.ts`** : branchement de l'observabilité (4.9).

### 2.9 Pièges fréquents

- **Placer un `page.tsx` dans un dossier utilitaire** : il devient une **route publique**.
- **Mélanger `app/` et `pages/`** avec des routes qui entrent en conflit : le build échoue (une URL ne peut exister que dans un seul routeur).
- **Commiter `.env.local`** : fuite de secrets.
- **Oublier de placer `proxy.ts` dans `src/`** quand ce dossier est utilisé : le proxy est ignoré.
- **Ne pas ignorer `.next/`** dans Git : dépôt alourdi de fichiers générés.

### 2.10 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| Colocation | Placer composants, styles et tests à côté de la route sans les exposer |
| Dossier privé (`_x`) | Dossier exclu du routage |
| Groupe de routes (`(x)`) | Dossier qui organise sans changer l'URL |
| Alias d'import | Raccourci de chemin défini dans `tsconfig.json` |
| `public/` | Dossier des fichiers servis tels quels |
| `.next/` | Dossier de sortie du build, généré |

### Synthèse du chapitre 2

`app/` contient les **routes**, `public/` les **fichiers statiques**, `src/` est facultatif. Seuls `page` et `route` rendent un dossier accessible : le reste est **colocalisé** sans risque. `_dossier` = privé ; `(groupe)` = organisation sans effet sur l'URL. Choisissez une stratégie d'organisation et tenez-vous-y.

---

## 3. Routing (App Router)

**Objectifs d'apprentissage.** Créer des routes statiques, dynamiques et *catch-all* ; utiliser **layouts**, **templates**, **groupes de routes**, **routes parallèles** et **routes interceptées** ; lire `params` et `searchParams` ; pré-générer des routes dynamiques avec `generateStaticParams` ; connaître les hooks de routage côté client et les helpers de types.

### 3.1 Principes

Le routeur de Next.js est **basé sur le système de fichiers** :

- Un **dossier** dans `app/` = un **segment d'URL**.
- Un fichier **`page.tsx`** dans ce dossier rend la route **accessible**.
- Les dossiers imbriqués forment des routes imbriquées.

```text
app/page.tsx                → /
app/about/page.tsx          → /about
app/blog/page.tsx           → /blog
app/blog/archive/page.tsx   → /blog/archive
```

**Anatomie d'une URL :**

```text
https://exemple.com/blog/mon-article?tri=date#commentaires
        └ domaine ┘└────── chemin ──────┘└ query ┘└ fragment ┘
                     segments : blog / mon-article
```

- Le **chemin** est mis en correspondance avec l'arbre de dossiers.
- La **query string** (`?tri=date`) est lue via `searchParams` (3.7).
- Le **fragment** (`#commentaires`) n'est **jamais envoyé au serveur**.

**Hiérarchie de composants.** Pour `/dashboard/settings`, Next.js assemble :

```tsx
<RootLayout>
    <DashboardLayout>
        <SettingsPage />
    </DashboardLayout>
</RootLayout>
```

Chaque layout enveloppe ses enfants ; chaque segment peut aussi avoir son `loading`, son `error`, son `not-found`, qui deviennent des **frontières** (`Suspense`, *error boundary*) autour du segment (chapitre 4).

### 3.2 Les pages

```tsx
// app/about/page.tsx
export default function AboutPage() {
    return <h1>À propos</h1>;
}
```

- Une page est un composant exporté **par défaut**.
- Par défaut, c'est un **Server Component** (chapitre 5).
- Une page peut être **`async`** et charger ses données directement (chapitre 6).

### 3.3 Les layouts

Un **layout** est une interface **partagée** entre plusieurs pages. Il reçoit `children` : la page ou le layout enfant.

```tsx
// app/layout.tsx — layout racine, obligatoire
export default function RootLayout({ children }: { children: React.ReactNode }) {
    return (
        <html lang="fr">
            <body>{children}</body>
        </html>
    );
}
```

**Règles :**

- Le **layout racine** doit contenir les balises `<html>` et `<body>`.
- Un layout **n'est pas remonté** lors d'une navigation entre ses pages enfants : son **état** (champ de recherche, défilement d'une barre latérale) est **conservé**.
- Un layout **ne reçoit pas `searchParams`** (il ne se re-rend pas quand la query change). Utilisez la page, ou un Client Component avec `useSearchParams`.
- Un layout ne peut pas lire directement le chemin de la page enfant ; utilisez `usePathname()` dans un Client Component.
- Les layouts peuvent charger des données ; Next.js **déduplique** les requêtes identiques (6.3).

**Layouts imbriqués :**

```text
app/
├── layout.tsx                    # racine
└── dashboard/
    ├── layout.tsx                # layout du tableau de bord
    ├── page.tsx                  # /dashboard
    └── settings/page.tsx         # /dashboard/settings
```

```tsx
// app/dashboard/layout.tsx
export default function DashboardLayout({ children }: { children: React.ReactNode }) {
    return (
        <div className="flex">
            <aside>Menu latéral</aside>
            <main>{children}</main>
        </div>
    );
}
```

### 3.4 Les templates

`template.tsx` fonctionne comme un layout, mais **un nouvel exemplaire est créé à chaque navigation**. L'état est **réinitialisé**, les effets sont **ré-exécutés**, le DOM est **recréé**.

Cas d'usage : animations d'entrée, journalisation de vues de page via `useEffect`, états qui doivent être remis à zéro à chaque page.

```tsx
// app/template.tsx
export default function Template({ children }: { children: React.ReactNode }) {
    return <div className="fade-in">{children}</div>;
}
```

**Ordre de rendu :** `layout` → `template` → `page`. Le template se situe **entre** le layout et ses enfants.

| | **Layout** | **Template** |
| --- | --- | --- |
| Entre deux pages enfants | **Conservé** (état préservé) | **Recréé** (état réinitialisé) |
| Effets (`useEffect`) | Exécutés une fois | Ré-exécutés à chaque navigation |
| Usage typique | Navigation, barre latérale | Animations, statistiques de vues |

### 3.5 Routes dynamiques

Un dossier entre crochets définit un **segment dynamique** : `[slug]`.

```text
app/blog/[slug]/page.tsx   →  /blog/hello, /blog/nextjs-16, ...
```

```tsx
// app/blog/[slug]/page.tsx
export default async function PostPage({
    params,
}: {
    params: Promise<{ slug: string }>;
}) {
    const { slug } = await params;
    return <h1>Article : {slug}</h1>;
}
```

> **Version.** Depuis Next.js 15, `params` est une **Promise** ; en Next.js 16, l'accès **synchrone est entièrement retiré** : il faut `await params`. Dans un Client Component, on utilise `use(params)` ou le hook `useParams()`.

**Plusieurs segments dynamiques :**

```text
app/[categorie]/[produit]/page.tsx   → /chaussures/air-max
```

```tsx
const { categorie, produit } = await params;
```

**Segment *catch-all* : `[...slug]`** — capture **un ou plusieurs** segments :

```text
app/docs/[...slug]/page.tsx
/docs/a            → { slug: ["a"] }
/docs/a/b/c        → { slug: ["a", "b", "c"] }
/docs              → ne correspond pas
```

**Segment *catch-all* optionnel : `[[...slug]]`** — capture **zéro, un ou plusieurs** segments :

```text
app/docs/[[...slug]]/page.tsx
/docs              → { slug: undefined }
/docs/a/b          → { slug: ["a", "b"] }
```

| Dossier | Exemple d'URL | `params` |
| --- | --- | --- |
| `[id]` | `/produit/42` | `{ id: "42" }` |
| `[...slug]` | `/a/b/c` | `{ slug: ["a", "b", "c"] }` |
| `[[...slug]]` | `/` ou `/a/b` | `{ slug: undefined }` ou `{ slug: [...] }` |

> **Important.** Les valeurs de `params` sont toujours des **chaînes** (ou des tableaux de chaînes) : convertissez-les (`Number(id)`) et **validez-les**. Un utilisateur peut taper n'importe quoi dans l'URL.

**Priorité de correspondance.** Quand plusieurs routes peuvent correspondre, Next.js privilégie la plus **spécifique** : segment statique > dynamique `[x]` > *catch-all* `[...x]` > *catch-all* optionnel `[[...x]]`.

### 3.6 Pré-génération : `generateStaticParams`

Cette fonction permet de **générer à l'avance** (au build) les pages d'une route dynamique.

```tsx
// app/blog/[slug]/page.tsx
export async function generateStaticParams() {
    const posts = await fetch("https://api.exemple.com/posts").then((r) => r.json());
    return posts.map((post: { slug: string }) => ({ slug: post.slug }));
}
```

- Elle retourne un tableau d'objets dont les **clés** correspondent aux noms de segments.
- Pour plusieurs segments : `[{ categorie: "a", produit: "x" }, ...]`.
- Pour un *catch-all* : `{ slug: ["a", "b"] }`.
- Les requêtes `fetch` de `generateStaticParams` sont **dédupliquées** avec celles de la page.
- Une route avec `generateStaticParams` est marquée ● (SSG) dans le tableau du build.

**Que se passe-t-il pour une valeur non listée ?** Cela dépend de `dynamicParams` (modèle classique) :

```tsx
export const dynamicParams = true;     // (défaut) génération à la demande, puis mise en cache
// export const dynamicParams = false; // toute valeur non listée → 404
```

> **Version (Cache Components).** Avec `cacheComponents: true`, la configuration de segment `dynamicParams` n'est **pas supportée** ; le comportement dépend de l'usage de `"use cache"` et de `Suspense` (chapitres 7 et 8). Avec Cache Components, `generateStaticParams` doit retourner **au moins un jeu de paramètres** pour permettre la validation au build. Depuis **16.3**, une page **non pré-rendue** au build sert à son premier visiteur une **coque de chargement instantanée** (nouvelle forme d'ISR, chapitre 8), puis est mise à niveau en arrière-plan.

### 3.7 Paramètres de requête (`searchParams`)

```tsx
// app/recherche/page.tsx — URL : /recherche?q=next&page=2
export default async function Recherche({
    searchParams,
}: {
    searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
}) {
    const { q, page } = await searchParams;
    return <p>Recherche : {q} (page {page ?? "1"})</p>;
}
```

Points essentiels :

- `searchParams` est une **Promise** (version 15+).
- Lire `searchParams` rend la page **dynamique** (rendue à chaque requête), car la valeur n'est connue qu'à la requête.
- Disponible dans les **pages**, **pas** dans les layouts.
- Une clé répétée (`?a=1&a=2`) donne un **tableau**.
- Côté client : `useSearchParams()`, à envelopper dans `<Suspense>` pour ne pas désactiver le pré-rendu statique de toute la page.

### 3.8 Groupes de routes : `(nom)`

Un dossier entre parenthèses **n'apparaît pas dans l'URL**. Utilités :

1. **Organiser** les routes par domaine fonctionnel.
2. **Attribuer des layouts différents** à des groupes de pages.
3. Créer **plusieurs layouts racines** (chacun avec `<html>` et `<body>`).

```text
app/
├── (marketing)/
│   ├── layout.tsx
│   ├── page.tsx              → /
│   └── about/page.tsx        → /about
└── (app)/
    ├── layout.tsx            # layout avec barre latérale
    └── dashboard/page.tsx    → /dashboard
```

> **Attention.** Deux groupes ne doivent pas définir **la même URL** (par exemple `(a)/about/page.tsx` et `(b)/about/page.tsx`) : erreur. Naviguer entre deux **layouts racines** différents provoque un **rechargement complet** de la page.

### 3.9 Routes parallèles : `@slot`

Les **routes parallèles** permettent de rendre **simultanément** plusieurs pages dans un même layout, ou de rendre conditionnellement. Un dossier `@nom` définit un **slot** ; il est passé en **prop** au layout parent (ce n'est **pas** un segment d'URL).

```text
app/
├── layout.tsx
├── page.tsx
├── @analytics/
│   ├── page.tsx
│   └── default.tsx
└── @equipe/
    ├── page.tsx
    └── default.tsx
```

```tsx
// app/layout.tsx
export default function Layout({
    children,
    analytics,
    equipe,
}: {
    children: React.ReactNode;
    analytics: React.ReactNode;
    equipe: React.ReactNode;
}) {
    return (
        <>
            {children}
            <section>{analytics}</section>
            <section>{equipe}</section>
        </>
    );
}
```

Chaque slot a ses propres `loading.tsx` et `error.tsx` : il se charge et échoue **indépendamment** (streaming, résilience).

**`default.tsx`.**

- Lors d'une **navigation côté client** (*soft navigation*), Next.js **conserve l'état** des slots non concernés.
- Lors d'un **chargement complet** (*hard navigation*, rafraîchissement), un slot dont le contenu ne correspond pas à l'URL affiche son **`default.tsx`** ; sans lui → 404.

> **Version 16.** Next.js 16 **exige** un fichier `default.tsx` explicite pour chaque slot de route parallèle ; sans lui, le build échoue.

**Cas d'usage :** tableaux de bord à panneaux indépendants ; **rendu conditionnel** selon le rôle (`@admin` / `@utilisateur`) en choisissant dans le layout ; modales (avec routes interceptées) ; onglets ayant leur propre état de navigation.

### 3.10 Routes interceptées

Elles permettent de **charger une route dans le contexte courant** (par exemple en **modale**) lors d'une navigation interne, tout en gardant une **URL partageable** qui, lors d'un accès direct, affiche la page complète.

Syntaxe (relative aux **segments de route**, pas aux dossiers du système de fichiers) :

| Convention | Intercepte |
| --- | --- |
| `(.)nom` | Le même niveau |
| `(..)nom` | Un niveau au-dessus |
| `(..)(..)nom` | Deux niveaux au-dessus |
| `(...)nom` | Depuis la racine `app/` |

**Exemple : galerie photo avec modale.**

```text
app/
├── layout.tsx                 # reçoit children + modal
├── page.tsx                   # galerie
├── @modal/
│   ├── default.tsx            # retourne null
│   └── (.)photo/[id]/page.tsx # photo affichée en modale
└── photo/[id]/page.tsx        # page complète (accès direct)
```

```tsx
// app/layout.tsx
export default function Layout({
    children,
    modal,
}: {
    children: React.ReactNode;
    modal: React.ReactNode;
}) {
    return (
        <html lang="fr">
            <body>
                {children}
                {modal}
            </body>
        </html>
    );
}
```

```tsx
// app/@modal/default.tsx
export default function Default() {
    return null;
}
```

Fermeture de la modale : `router.back()` dans un Client Component.

**Comportement :** un clic sur un lien `/photo/3` depuis la galerie ouvre la **modale** (interception) ; un rafraîchissement ou un lien partagé affiche la **page complète** `/photo/3`.

### 3.11 Hooks utiles liés au routage

| Hook (Client Component) | Rôle |
| --- | --- |
| `usePathname()` | Chemin courant (`/blog/a`) |
| `useParams()` | Paramètres dynamiques |
| `useSearchParams()` | Lecture des paramètres de requête |
| `useSelectedLayoutSegment()` | Segment actif juste sous le layout |
| `useSelectedLayoutSegments()` | Tous les segments actifs sous le layout |
| `useRouter()` | Navigation impérative (chapitre 12) |

**Exemple : lien actif.**

```tsx
"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";

export function NavLink({ href, children }: { href: string; children: React.ReactNode }) {
    const pathname = usePathname();
    const active = pathname === href;
    return (
        <Link href={href} aria-current={active ? "page" : undefined} className={active ? "active" : ""}>
            {children}
        </Link>
    );
}
```

### 3.12 Paramètres racine : `next/root-params` *(ajout, 16.3)*

Pour les paramètres situés **au-dessus du layout racine** (par exemple un segment `[lang]` en tête d'arborescence), il fallait jusqu'ici les **faire descendre en props** à travers tout l'arbre. Depuis **16.3**, ils s'obtiennent depuis **n'importe quel Server Component** :

```tsx
// app/[lang]/posts/[slug]/page.tsx
import { lang } from "next/root-params";

export default async function PostPage(props: PageProps<"/[lang]/posts/[slug]">) {
    const { slug } = await props.params;
    const language = await lang();            // lu sans prop drilling

    return (
        <article>
            <p>Langue : {language}</p>
            <p>Article : {slug}</p>
        </article>
    );
}
```

Les *root params* fonctionnent aussi dans un périmètre `"use cache"`. Ils sont pris en charge dans les Server Components ; le support des Route Handlers et des Server Actions est annoncé pour une version ultérieure. Cas typique : l'internationalisation (chapitre 17).

### 3.13 Redirections et réécritures au niveau du routage

- **Redirections** (`redirects` dans `next.config`) : statut **307 / 308** ; l'URL du navigateur **change**.
- **Réécritures** (`rewrites`) : servent un autre contenu **sans changer l'URL affichée** (proxy transparent).
- Voir chapitres 11 et 18.

### 3.14 Helpers de types pour `params` *(à jour)*

Next.js 15.5+ et 16 offrent des **helpers de types globaux**, générés par `next dev`, `next build` ou `next typegen` :

```tsx
export default async function Page(props: PageProps<"/blog/[slug]">) {
    const { slug } = await props.params;
    return <h1>{slug}</h1>;
}
```

Autres helpers : `LayoutProps<"/dashboard">`, `RouteContext<"/api/posts/[id]">`. Ils évitent de retaper les types des paramètres (chapitre 20).

### 3.15 Pièges fréquents

- **Oublier `await params`** (Next.js 15 / 16) : erreur ou avertissement.
- **Utiliser `searchParams` dans un layout** : non supporté ; passez par la page.
- **Lire `searchParams` sans le savoir** : la page devient **dynamique**.
- **Deux routes menant à la même URL** (via groupes) : erreur de build.
- **Oublier `default.tsx`** dans un slot parallèle : build en échec (Next.js 16).
- **Confondre `[...slug]` et `[[...slug]]`** : le premier **ne correspond pas** à la racine du segment.
- **Faire confiance à `params`** sans validation : ce sont des chaînes saisies par l'utilisateur.

### 3.16 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| Segment | Partie de l'URL entre deux `/`, associée à un dossier |
| Layout | Interface partagée persistante entre routes |
| Template | Layout recréé à chaque navigation |
| Segment dynamique | Dossier `[x]` capturant une valeur d'URL |
| *Catch-all* | Segment `[...x]` capturant plusieurs segments |
| Groupe de routes | Dossier `(x)` sans effet sur l'URL |
| Route parallèle | Slot `@x` rendu en même temps que la page |
| Route interceptée | Route chargée dans le contexte courant (modale) |
| `generateStaticParams` | Fonction listant les valeurs à pré-générer |
| *Root params* | Paramètres au-dessus du layout racine, lisibles partout |

### Synthèse du chapitre 3

Dossier = **segment** ; `page.tsx` = **route publique**. Le `layout` **persiste**, le `template` se **recrée**. `[x]`, `[...x]`, `[[...x]]` pour le dynamique ; `(x)` pour regrouper ; `@x` pour les slots (avec `default.tsx` obligatoire) ; `(.)x` pour intercepter. `params` et `searchParams` sont **asynchrones** ; `generateStaticParams` pré-génère les routes dynamiques ; `next/root-params` évite de faire descendre `[lang]` en props.

---

## 4. Fichiers spéciaux

**Objectifs d'apprentissage.** Connaître chaque fichier réservé de l'App Router et son rôle ; comprendre la **hiérarchie de frontières** qu'ils composent ; gérer les états de chargement, d'erreur et de page introuvable ; utiliser `redirect`, `notFound`, `forbidden` et `unauthorized` ; définir des frontières d'erreur personnalisées avec `catchError` ; brancher l'observabilité avec `instrumentation.ts` ; générer les fichiers de métadonnées (icônes, images Open Graph).

### 4.1 Vue d'ensemble

Next.js attribue un **sens particulier** à certains noms de fichiers. Ils se composent **dans un ordre hiérarchique précis** autour de la page :

```tsx
<Layout>
    <Template>
        <ErrorBoundary fallback={<Error />}>
            <Suspense fallback={<Loading />}>
                <ErrorBoundary fallback={<NotFound />}>
                    <Page />
                </ErrorBoundary>
            </Suspense>
        </ErrorBoundary>
    </Template>
</Layout>
```

Cette imbrication explique plusieurs comportements. Par exemple, le `error.tsx` d'un segment **n'intercepte pas** les erreurs du `layout.tsx` du **même** segment (il se trouve à l'intérieur) : on utilise alors le `error.tsx` du segment **parent**, ou `global-error.tsx`.

| Fichier | Rôle |
| --- | --- |
| `layout` | Interface partagée, persistante |
| `page` | Interface unique d'une route (la rend publique) |
| `template` | Layout recréé à chaque navigation |
| `loading` | État de chargement instantané (Suspense) |
| `error` | Frontière d'erreur du segment |
| `global-error` | Frontière d'erreur du layout racine |
| `not-found` | Interface « introuvable » (404) |
| `route` | Endpoint HTTP (Route Handler) |
| `default` | Repli d'un slot de route parallèle |
| `forbidden` / `unauthorized` | Pages 403 / 401 (expérimental) |
| `proxy` (ex-`middleware`) | Interception des requêtes (racine) |
| `instrumentation` | Hook de démarrage / observabilité |
| `opengraph-image`, `twitter-image`, `icon`, `apple-icon` | Images de métadonnées |
| `sitemap`, `robots`, `manifest` | Fichiers SEO / PWA |

### 4.2 `loading.tsx`

Il crée automatiquement une frontière `<Suspense>` autour de la page et de ses enfants. Pendant que la page (asynchrone) charge ses données, l'utilisateur voit immédiatement le **contenu de `loading.tsx`**, et la navigation reste **interruptible**.

```tsx
// app/dashboard/loading.tsx
export default function Loading() {
    return <div className="skeleton">Chargement du tableau de bord…</div>;
}
```

**Bonnes pratiques :**

- Afficher des **squelettes** (*skeletons*) fidèles à la mise en page finale pour limiter les décalages visuels.
- `loading.tsx` ne protège que ce qui est **sous** lui : un layout qui attend des données n'est pas couvert.
- Pour un contrôle plus fin, utilisez `<Suspense>` directement dans la page autour de composants individuels.
- Avec **Cache Components** (chapitre 7), `loading.tsx` reste valable, mais les `<Suspense>` explicites sont l'outil principal : ils définissent précisément la **coque statique** de la page.

> **Instant Navigations (16.3).** Oublier un `loading.tsx` ou un `<Suspense>` rendait certaines navigations lentes sans qu'on s'en aperçoive. Les DevTools de Next.js intègrent désormais **Instant Insights**, qui signale les navigations non instantanées (chapitre 12).

### 4.3 `error.tsx`

C'est une **frontière d'erreur React** pour le segment : elle capture les erreurs **de rendu** (et d'exécution dans les composants enfants) et affiche une interface de repli, sans casser le reste de l'application (les layouts parents restent affichés).

```tsx
// app/dashboard/error.tsx
"use client"; // obligatoire : les error boundaries sont des Client Components

import { useEffect } from "react";

export default function Error({
    error,
    reset,
}: {
    error: Error & { digest?: string };
    reset: () => void;
}) {
    useEffect(() => {
        console.error(error); // journaliser vers un service de monitoring
    }, [error]);

    return (
        <div role="alert">
            <h2>Quelque chose s'est mal passé</h2>
            <button onClick={() => reset()}>Réessayer</button>
        </div>
    );
}
```

**Points essentiels :**

- **`"use client"` obligatoire.**
- `reset()` tente de **re-rendre** le segment.
- **`error.digest`** : identifiant d'erreur. En **production**, les erreurs levées dans les Server Components sont **masquées** au client (le message réel pourrait contenir des informations sensibles) ; seul un `digest` générique est transmis, que l'on retrouve dans les **logs serveur**.
- **Ne capture pas** : les erreurs dans les **gestionnaires d'événements** (utilisez `try` / `catch` et `useState`), les erreurs asynchrones hors du rendu, les erreurs du layout du même segment.
- Pour les **erreurs attendues** dans les Server Actions (validation, conflit), **ne levez pas d'exception** : retournez un objet d'erreur (chapitre 9).

**`global-error.tsx`.** Il capture les erreurs du **layout racine** et **remplace complètement** ce layout : il doit donc définir `<html>` et `<body>`.

```tsx
// app/global-error.tsx
"use client";

export default function GlobalError({ reset }: { error: Error; reset: () => void }) {
    return (
        <html lang="fr">
            <body>
                <h2>Erreur critique</h2>
                <button onClick={() => reset()}>Réessayer</button>
            </body>
        </html>
    );
}
```

### 4.4 Frontières d'erreur personnalisées : `catchError` *(ajout, 16.3)*

Les frontières d'erreur de fichier (`error.tsx`) ont deux limites : elles interféraient avec le code qui appelle `notFound()` ou `redirect()`, et `reset()` ne réinitialisait que l'**état côté client**, sans permettre de **relancer les Server Components** qui avaient échoué.

Depuis **16.3**, `catchError` définit une frontière **imbriquée** de votre choix, n'importe où dans l'arbre, qui ne perturbe pas `notFound` ni `redirect` et reçoit une fonction **`retry()`** : elle **re-récupère** les enfants de la frontière, y compris en re-rendant des Server Components.

```tsx
// app/mon-error-boundary.tsx
"use client";
import { catchError, type ErrorInfo } from "next/error";

function ErrorFallback(props: { titre: string }, { error, retry }: ErrorInfo) {
    return (
        <div role="alert">
            <h2>{props.titre}</h2>
            <p>{error.message}</p>
            <button onClick={() => retry()}>Réessayer</button>
        </div>
    );
}

export default catchError(ErrorFallback);
```

Utilisation : on enveloppe la zone concernée avec le composant retourné (`<MonErrorBoundary titre="Statistiques">…</MonErrorBoundary>`). C'est la bonne approche pour isoler **un widget** plutôt qu'un segment entier.

### 4.5 `not-found.tsx` et `notFound()`

```tsx
// app/blog/[slug]/page.tsx
import { notFound } from "next/navigation";

export default async function Post({ params }: { params: Promise<{ slug: string }> }) {
    const { slug } = await params;
    const post = await getPost(slug);
    if (!post) notFound(); // lève une exception interne, interrompt le rendu
    return <article>{post.title}</article>;
}
```

```tsx
// app/blog/[slug]/not-found.tsx
export default function NotFound() {
    return <h2>Article introuvable</h2>;
}
```

- `notFound()` renvoie le statut **404** et affiche le `not-found.tsx` le plus proche.
- Un `app/not-found.tsx` à la racine gère **toutes les URLs non correspondantes** de l'application.
- En *streaming*, si les en-têtes ont déjà été envoyés, le statut peut rester 200 ; Next.js ajoute alors une balise `noindex` automatiquement.

### 4.6 Redirections : `redirect` et `permanentRedirect`

```tsx
import { redirect, permanentRedirect } from "next/navigation";

redirect("/login");                 // 307 (temporaire) ; 303 depuis une Server Action
permanentRedirect("/nouvelle-url"); // 308 (permanente)
```

- Utilisables dans les Server Components, Server Actions et Route Handlers.
- **Elles lèvent une exception interne** : ne les placez **pas** dans un `try` / `catch` (vous interceptez la redirection). Appelez-les en dehors du bloc, ou utilisez `unstable_rethrow(error)` dans le `catch`.
- Côté client (événement) : préférez `router.push` (chapitre 12).

### 4.7 `forbidden()` et `unauthorized()` *(expérimental)*

Pages dédiées aux statuts **403** et **401**, à activer :

```ts
// next.config.ts
import type { NextConfig } from "next";

const nextConfig: NextConfig = { experimental: { authInterrupts: true } };
export default nextConfig;
```

```tsx
import { forbidden, unauthorized } from "next/navigation";

const session = await verifySession();
if (!session) unauthorized();                 // affiche app/unauthorized.tsx (401)
if (session.role !== "admin") forbidden();    // affiche app/forbidden.tsx (403)
```

### 4.8 `route.ts` et `default.tsx`

- **`route.ts`** définit un **endpoint HTTP** (chapitre 10). Un dossier ne peut pas contenir **à la fois** `page.tsx` et `route.ts` pour la même URL : séparez-les.
- **`default.tsx`** est le repli d'un slot de route parallèle (chapitre 3) ; **obligatoire** dans Next.js 16.

### 4.9 `instrumentation.ts`

Ce fichier est exécuté **une fois au démarrage** du serveur. Il sert à brancher **OpenTelemetry**, Sentry, Datadog, etc.

```ts
// instrumentation.ts (racine ou src/)
export async function register() {
    if (process.env.NEXT_RUNTIME === "nodejs") {
        await import("./instrumentation-node");
    }
}

export async function onRequestError(
    err: unknown,
    request: { path: string; method: string; headers: Record<string, string | string[] | undefined> },
    context: { routerKind: string; routePath: string; routeType: string; renderSource?: string }
) {
    // envoyer l'erreur à votre outil de monitoring
}
```

`register()` s'exécute au démarrage ; `onRequestError()` est appelée à **chaque erreur** survenue lors du traitement d'une requête, avec le contexte (route, type de rendu) nécessaire à un diagnostic.

### 4.10 Fichiers de métadonnées

**Icônes** : `app/favicon.ico`, `app/icon.png|jpg|svg`, `app/apple-icon.png`. Génération dynamique : `app/icon.tsx` retournant une `ImageResponse`.

**Images Open Graph / Twitter :**

```tsx
// app/blog/[slug]/opengraph-image.tsx
import { ImageResponse } from "next/og";

export const size = { width: 1200, height: 630 };
export const contentType = "image/png";
export const alt = "Image de l'article";

export default async function Image({ params }: { params: Promise<{ slug: string }> }) {
    const { slug } = await params;
    return new ImageResponse(
        (
            <div style={{ fontSize: 64, display: "flex", width: "100%", height: "100%", alignItems: "center", justifyContent: "center" }}>
                {slug}
            </div>
        ),
        size
    );
}
```

**`sitemap.ts`, `robots.ts`, `manifest.ts`** : voir chapitre 15.

### 4.11 Pièges fréquents

- **Oublier `"use client"`** dans `error.tsx` : erreur de build.
- **Attendre que `error.tsx` capture une erreur de son propre `layout.tsx`** : placez-le dans le parent.
- **Mettre `redirect()` dans un `try` / `catch`** : la redirection est avalée.
- **Exposer des messages d'erreur serveur au client** : en production Next.js les masque ; ne les réinjectez pas manuellement.
- **Oublier `default.tsx`** dans un slot : build en échec.
- **Utiliser `loading.tsx` comme unique stratégie de chargement** : il couvre tout le segment, alors qu'un `<Suspense>` ciblé isole mieux les parties lentes.

### 4.12 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| Frontière (*boundary*) | Composant qui encadre une zone (Suspense, erreur, introuvable) |
| *Error boundary* | Composant React qui capture les erreurs de rendu de ses enfants |
| `digest` | Identifiant d'une erreur serveur, corrélé aux logs |
| `catchError` | API (16.3) pour créer une frontière d'erreur personnalisée avec `retry()` |
| Soft / hard navigation | Navigation côté client / rechargement complet |
| `instrumentation.ts` | Fichier de démarrage pour l'observabilité |
| `ImageResponse` | Générateur d'images (Open Graph, icônes) à partir de JSX |

### Synthèse du chapitre 4

Les fichiers spéciaux composent une **hiérarchie de frontières** : Layout > Template > Error > Suspense (`loading`) > NotFound > Page. `loading` = Suspense automatique ; `error` = *error boundary* **cliente** ; `not-found` = 404 ; `redirect` et `notFound` interrompent le rendu en **levant une exception**. `catchError` (16.3) ajoute des frontières locales avec `retry()`, et `instrumentation.ts` branche le monitoring.

---

## 5. Server Components et Client Components

**Objectifs d'apprentissage.** Comprendre le modèle des **React Server Components (RSC)** ; savoir quand choisir un Server ou un Client Component ; maîtriser la frontière **`"use client"`** et les règles de composition ; sérialiser correctement les props ; fournir des contextes ; intégrer des bibliothèques tierces ; protéger le code et les données sensibles ; comprendre et corriger les erreurs d'hydratation.

### 5.1 Le modèle mental

Dans l'App Router, **tout composant est un Server Component par défaut**. On bascule vers le client **seulement quand c'est nécessaire**.

**Server Components.** Exécutés **uniquement sur le serveur** (au build ou à la requête). Leur code n'est **jamais envoyé** au navigateur ; seul leur **résultat** l'est.

*Avantages :*

- **Accès direct aux ressources back-end** : base de données, système de fichiers, services internes.
- **Sécurité** : secrets et clés d'API ne quittent pas le serveur.
- **Moins de JavaScript** : les bibliothèques lourdes utilisées uniquement côté serveur (Markdown, formatage, ORM) n'alourdissent pas le bundle.
- **Performance** : données chargées près de leur source, sans cascade client → API.
- **Streaming** et **cache**.
- **SEO** : contenu présent dans le HTML initial.

*Limites :*

- Pas de `useState`, `useReducer`, `useEffect`, `useLayoutEffect`.
- Pas de **gestionnaires d'événements** (`onClick`…).
- Pas d'**API du navigateur** (`window`, `document`, `localStorage`, `navigator`).
- Pas de **Context** (`createContext` / `useContext`).
- Pas de hooks personnalisés dépendant des éléments ci-dessus.

**Client Components.** Marqués par la directive **`"use client"`**. Ils sont **pré-rendus** sur le serveur (HTML initial) **puis hydratés** dans le navigateur. Ils servent à tout ce qui est **interactif** : état local, événements, effets, API du navigateur, contextes, hooks personnalisés, bibliothèques purement clientes (cartes, graphiques interactifs, éditeurs riches).

```tsx
"use client";

import { useState } from "react";

export default function Compteur() {
    const [n, setN] = useState(0);
    return <button onClick={() => setN(n + 1)}>Clics : {n}</button>;
}
```

**Tableau de décision :**

| Besoin | Server | Client |
| --- | :-: | :-: |
| Lire une base de données / un secret | Oui | Non |
| `async` / `await` directement dans le composant | Oui | Non |
| `useState`, `useEffect`, `useReducer` | Non | Oui |
| `onClick`, `onChange`, `onSubmit` (gestionnaires) | Non | Oui |
| `window`, `localStorage`, `navigator` | Non | Oui |
| `useContext` / providers | Non | Oui |
| Réduire le JavaScript envoyé | Oui | Non |
| Bibliothèque dépendant du navigateur | Non | Oui |

### 5.2 La directive `"use client"`

- À placer **tout en haut du fichier**, avant les imports.
- Elle déclare une **frontière client–serveur** : **ce fichier et tous les modules qu'il importe** (directement ou indirectement) font partie du **bundle client**.
- Inutile de la répéter dans chaque composant enfant importé par un fichier déjà « client ».
- Elle s'applique au **module**, pas à un composant individuel.

```tsx
"use client";
import { Bouton } from "./Bouton";   // Bouton devient automatiquement client
```

**Composants « partagés ».** Un composant **sans** directive, sans API serveur ni client spécifique, peut être utilisé **des deux côtés** : il s'exécute selon l'endroit d'où il est importé (serveur s'il est importé par un Server Component, client s'il est importé par un Client Component).

### 5.3 Que se passe-t-il à l'exécution ?

**Au chargement initial (rendu serveur) :**

1. React rend les Server Components en un format spécial, le **payload RSC** (représentation compacte de l'arbre, avec des « trous » qui référencent les Client Components).
2. Next.js utilise ce payload et le code des Client Components pour générer le **HTML** pré-rendu, envoyé au navigateur.
3. Côté client, le payload RSC sert à **réconcilier** l'arbre de Server et de Client Components et à mettre à jour le DOM.
4. Les Client Components sont **hydratés**.

**Navigations suivantes :** le navigateur demande uniquement le **payload RSC** des segments qui changent ; les Client Components déjà chargés sont réutilisés ; **pas de rechargement complet**.

### 5.4 Règles de composition

**5.4.1 Un Server Component peut importer un Client Component**

```tsx
// Server Component
import Compteur from "./Compteur"; // "use client"

export default function Page() {
    return (
        <>
            <h1>Page serveur</h1>
            <Compteur />
        </>
    );
}
```

**5.4.2 Un Client Component ne peut pas *importer* un Server Component.** Si un fichier `"use client"` importe un composant serveur, ce dernier **devient client** et perd ses capacités serveur (`async`, `server-only`…).

**5.4.3 …mais il peut en *recevoir* un en `children` ou en prop.** C'est le **motif d'entrelacement** (*interleaving*) :

```tsx
// Modal.tsx
"use client";
import { useState } from "react";

export default function Modal({ children }: { children: React.ReactNode }) {
    const [ouvert, setOuvert] = useState(false);
    return (
        <>
            <button onClick={() => setOuvert(true)}>Ouvrir</button>
            {ouvert && <div role="dialog">{children}</div>}
        </>
    );
}
```

```tsx
// page.tsx (Server Component)
import Modal from "./Modal";
import Panier from "./Panier"; // Server Component asynchrone

export default function Page() {
    return (
        <Modal>
            <Panier />  {/* rendu côté serveur, passé comme children */}
        </Modal>
    );
}
```

Le Server Component est rendu **d'abord sur le serveur** ; le résultat sérialisé est passé au Client Component comme un « trou » à remplir. Le client n'a pas besoin de son code.

**5.4.4 Sérialisation des props.** Les props passées d'un Server Component à un Client Component doivent être **sérialisables par React** :

| Autorisé | Interdit |
| --- | --- |
| `string`, `number`, `boolean`, `null`, `undefined` | **Fonctions** (sauf Server Actions) |
| Tableaux, objets simples | Instances de classes |
| `Date`, `Map`, `Set`, `BigInt`, `Promise` | Symboles non globaux |
| `FormData`, `TypedArray`, éléments JSX | Objets avec méthodes |
| **Server Actions** (fonctions `"use server"`) | |

Astuce : pour passer une fonction, passez plutôt une **Server Action**, ou déclarez la fonction côté client.

**5.4.5 Promesses comme props et hook `use`.** Un Server Component peut passer une **promesse non attendue** à un Client Component, qui la lit avec `use()` (sous `Suspense`) : la requête démarre côté serveur, le rendu se fait côté client.

```tsx
// Server Component
import { Suspense } from "react";
import Posts from "./Posts";

export default function Page() {
    const posts = getPosts(); // pas de await
    return (
        <Suspense fallback={<p>Chargement…</p>}>
            <Posts posts={posts} />
        </Suspense>
    );
}
```

```tsx
// Posts.tsx
"use client";
import { use } from "react";

export default function Posts({ posts }: { posts: Promise<{ id: string; title: string }[]> }) {
    const liste = use(posts);
    return <ul>{liste.map((p) => <li key={p.id}>{p.title}</li>)}</ul>;
}
```

### 5.5 Placer la frontière le plus bas possible

Marquer un **grand** composant `"use client"` envoie tout son sous-arbre au navigateur. Préférez **isoler la partie interactive** dans un petit composant.

Mauvais :

```tsx
"use client";
export default function Page() {          // toute la page devient cliente
    const [open, setOpen] = useState(false);
    return (
        <>
            <HeavyArticle />              {/* dépend d'une grosse bibliothèque */}
            <button onClick={() => setOpen(!open)}>Menu</button>
        </>
    );
}
```

Bon :

```tsx
// Page serveur
import MenuToggle from "./MenuToggle"; // petit composant client
export default function Page() {
    return (
        <>
            <HeavyArticle />
            <MenuToggle />
        </>
    );
}
```

### 5.6 Fournisseurs de contexte (*Context Providers*)

`createContext` n'est pas disponible dans les Server Components. On crée un **Client Component Provider** et on l'insère **le plus bas possible** dans l'arbre.

```tsx
// theme-provider.tsx
"use client";
import { createContext, useContext, useState } from "react";

const ThemeContext = createContext<"light" | "dark">("light");
export const useTheme = () => useContext(ThemeContext);

export default function ThemeProvider({ children }: { children: React.ReactNode }) {
    const [theme] = useState<"light" | "dark">("light");
    return <ThemeContext.Provider value={theme}>{children}</ThemeContext.Provider>;
}
```

```tsx
// app/layout.tsx (serveur)
import ThemeProvider from "./theme-provider";

export default function RootLayout({ children }: { children: React.ReactNode }) {
    return (
        <html lang="fr">
            <body>
                <ThemeProvider>{children}</ThemeProvider>
            </body>
        </html>
    );
}
```

Les `children` (Server Components) restent rendus côté serveur grâce à l'entrelacement.

### 5.7 Bibliothèques tierces

Beaucoup de bibliothèques utilisent `useState` ou des effets **sans** déclarer `"use client"`. Les importer directement dans un Server Component provoque une erreur. Solution : un **wrapper** :

```tsx
// carousel.tsx
"use client";
import { Carousel } from "acme-carousel";
export default Carousel;
```

### 5.8 Protéger le code serveur : `server-only` et `client-only`

```bash
npm install server-only client-only
```

```ts
// lib/data.ts
import "server-only"; // erreur de build si importé par un Client Component
export async function getSecrets() { /* ... */ }
```

- **`server-only`** empêche un module (qui utilise des secrets, la base de données) d'être importé côté client.
- **`client-only`** empêche l'inverse (module dépendant de `window`).
- **Variables d'environnement** : seules celles préfixées **`NEXT_PUBLIC_`** sont inlinées dans le code client (chapitre 19).
- **API de *taint* (expérimentale)** : React propose `experimental_taintObjectReference` et `experimental_taintUniqueValue` pour **interdire** qu'un objet ou une valeur sensible (jeton, utilisateur complet) soit passé à un Client Component ; à activer via `experimental.taint`. Elle **complète**, sans le remplacer, une bonne **couche d'accès aux données (DAL)** qui ne renvoie que des **DTO** (objets minimaux, 6.11).

### 5.9 Chargement dynamique et `ssr: false`

```tsx
// Client Component
"use client";
import dynamic from "next/dynamic";

const Carte = dynamic(() => import("./Carte"), {
    ssr: false,              // ne pas pré-rendre côté serveur
    loading: () => <p>Chargement de la carte…</p>,
});
```

Attention : `ssr: false` n'est **autorisé que dans un Client Component** (version 15+).

### 5.10 Erreurs d'hydratation

Une **erreur d'hydratation** survient quand le HTML produit par le serveur diffère du premier rendu du client. Causes fréquentes :

- `Date.now()`, `Math.random()`, `window.innerWidth` dans le rendu (valeurs différentes côté serveur et client).
- HTML invalide imbriqué (`<p>` dans `<p>`, `<div>` dans `<p>`).
- Extensions de navigateur qui modifient le DOM.
- Formats de date ou de langue dépendant du **fuseau horaire**.

**Solutions :** déplacer le code dépendant du client dans `useEffect` ; utiliser un état « monté » ; ou `suppressHydrationWarning` (avec parcimonie, sur un seul niveau d'élément).

### 5.11 Pièges fréquents

- **Marquer toute la page `"use client"` « pour que ça marche »** : perte des bénéfices des RSC.
- **Importer un module serveur secret dans un composant client** sans `server-only`.
- **Passer une fonction en prop** d'un Server à un Client Component.
- **Oublier `Suspense`** autour d'un composant qui lit une promesse avec `use`.
- **Utiliser `useContext` dans un Server Component**.
- **Confondre « Client Component » et « rendu côté client uniquement »** : un Client Component est **aussi pré-rendu** sur le serveur.

### 5.12 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| Server Component | Composant exécuté uniquement sur le serveur (défaut) |
| Client Component | Composant hydraté dans le navigateur (`"use client"`) |
| Frontière client | Module marqué `"use client"` et tout ce qu'il importe |
| Entrelacement | Passer un Server Component en `children` d'un Client Component |
| Sérialisable | Que React sait transmettre du serveur au client |
| `server-only` | Paquet qui interdit l'import d'un module côté client |
| DTO | Objet de transfert de données, version minimale d'une entité |
| Erreur d'hydratation | Différence entre HTML serveur et premier rendu client |

### Synthèse du chapitre 5

Par défaut : **Server Component**. `"use client"` **seulement** pour l'interactivité. La frontière est définie au niveau du **module**. **Entrelacez** : un Server Component en `children` d'un Client Component. Props **sérialisables** ; secrets protégés (`server-only`, DAL, DTO) ; frontière **la plus basse possible**.

---

## 6. Récupération de données (*Data Fetching*)

**Objectifs d'apprentissage.** Charger des données dans les Server Components (`fetch`, ORM, fichiers) ; dédupliquer les requêtes ; organiser les requêtes **en parallèle ou en séquence** ; utiliser le **streaming** avec `Suspense` ; charger des données côté client lorsque c'est nécessaire ; connaître les **API de requête** dynamiques ; exécuter du code après la réponse ; gérer les erreurs ; sécuriser l'accès aux données avec une **DAL**.

### 6.1 Principe

Dans l'App Router, **un composant serveur peut être `async`** et attendre directement ses données :

```tsx
export default async function Page() {
    const res = await fetch("https://api.exemple.com/posts");
    if (!res.ok) throw new Error("Échec du chargement");
    const posts: { id: number; title: string }[] = await res.json();

    return (
        <ul>
            {posts.map((p) => (
                <li key={p.id}>{p.title}</li>
            ))}
        </ul>
    );
}
```

Pas de `useEffect`, pas d'état de chargement manuel : la requête s'exécute **sur le serveur**, avant l'envoi du HTML.

### 6.2 Sources de données

**6.2.1 `fetch` (API externes).**

- L'API Web standard `fetch` est **étendue** par Next.js (options `cache`, `next.revalidate`, `next.tags` dans le modèle classique).
- **Version 15+** : les requêtes `fetch` **ne sont plus mises en cache par défaut**. Avec Cache Components, on met en cache **la fonction ou le composant** qui encapsule le `fetch` avec `"use cache"` (chapitre 7).
- Gérez toujours les erreurs : `res.ok`, codes HTTP, expirations (`fetch` ne lève **pas** d'exception sur un 404 ou un 500).

**6.2.2 Base de données, ORM, SDK.** Le code s'exécutant sur le serveur, on appelle directement Prisma, Drizzle, un client SQL ou un SDK de CMS :

```tsx
import { db } from "@/lib/db";

export default async function Utilisateurs() {
    const users = await db.user.findMany({ select: { id: true, name: true } });
    return <ul>{users.map((u) => <li key={u.id}>{u.name}</li>)}</ul>;
}
```

**6.2.3 Système de fichiers.**

```tsx
import { readFile } from "node:fs/promises";
import path from "node:path";

export default async function Page() {
    const contenu = await readFile(path.join(process.cwd(), "content/a-propos.md"), "utf8");
    return <pre>{contenu}</pre>;
}
```

*(ajout, 16.3)* Pour charger **plusieurs fichiers locaux** (articles Markdown, par exemple), Turbopack prend en charge `import.meta.glob`, avec rechargement à chaud : `import.meta.glob("./posts/*.md", { eager: true })` (un loader doit être déclaré dans la configuration pour les fichiers `.md`).

### 6.3 Déduplication des requêtes

Dans **un même passage de rendu**, plusieurs composants peuvent demander les mêmes données sans surcoût : Next.js **mémoïse** les `fetch` GET identiques (*Request Memoization*). Pour les accès **sans `fetch`** (ORM, SDK), utilisez **`React.cache`** :

```ts
// lib/data.ts
import { cache } from "react";
import { db } from "./db";

export const getUser = cache(async (id: string) => {
    return db.user.findUnique({ where: { id } });
});
```

Le layout, la page et un composant enfant peuvent tous appeler `getUser("42")` : **une seule** requête est faite par rendu. Ce cache vit **le temps d'une requête serveur** ; il est distinct du cache persistant du chapitre 7.

> **Conseil.** Au lieu de « remonter » les données dans un parent pour les passer en props, **récupérez-les là où vous en avez besoin**, grâce à la déduplication.

### 6.4 Requêtes parallèles et séquentielles

**Séquentielles (cascade, *waterfall*) :**

```tsx
const artiste = await getArtiste(id);        // 1) attendre
const albums = await getAlbums(artiste.id);  // 2) dépend du résultat précédent
```

Acceptable **uniquement** si la 2ᵉ requête **dépend** de la 1ʳᵉ.

**Parallèles :**

```tsx
const [artiste, albums] = await Promise.all([getArtiste(id), getAlbums(id)]);
```

Si une requête peut échouer sans bloquer l'autre : `Promise.allSettled`.

**Motif « *preload* ».** Démarrer une requête tôt, l'attendre plus tard :

```tsx
const promesse = getAlbums(id);       // lancée
const artiste = await getArtiste(id); // on attend l'autre
const albums = await promesse;        // probablement déjà prête
```

**Cascades implicites par composants.** Si un parent `async` attend ses données avant de rendre un enfant `async`, les requêtes s'enchaînent. Atténuez avec **`Suspense`** (les deux composants rendent indépendamment) ou en remontant les requêtes avec `Promise.all`.

### 6.5 Streaming avec Suspense et `loading.tsx`

Le **streaming** envoie le HTML **par morceaux** : la coque de la page arrive tout de suite, puis chaque zone lente arrive quand elle est prête.

```tsx
import { Suspense } from "react";

export default function Dashboard() {
    return (
        <>
            <h1>Tableau de bord</h1>               {/* envoyé immédiatement */}
            <Suspense fallback={<Skeleton />}>
                <Statistiques />                   {/* lent */}
            </Suspense>
            <Suspense fallback={<Skeleton />}>
                <DernieresCommandes />             {/* lent, indépendant */}
            </Suspense>
        </>
    );
}
```

*Avantages :* meilleur **TTFB** perçu, interaction plus précoce (**hydratation sélective**), isolement des lenteurs.

### 6.6 Données dans les Client Components

Quand les données dépendent de l'interactivité (saisie, *polling*, temps réel), plusieurs options :

1. **Promesse passée depuis le serveur** + `use()` (voir 5.4.5).
2. **Bibliothèques** : **SWR** ou **TanStack Query** (cache, revalidation, déduplication, états de chargement).
3. **Route Handler** (`/api/...`) appelé depuis le client.

```tsx
"use client";
import useSWR from "swr";

const fetcher = (url: string) => fetch(url).then((r) => r.json());

export default function Profil() {
    const { data, error, isLoading } = useSWR("/api/profil", fetcher);
    if (isLoading) return <p>Chargement…</p>;
    if (error) return <p>Erreur</p>;
    return <p>{data.nom}</p>;
}
```

> **À éviter.** Appeler **depuis un Server Component** votre propre Route Handler (`fetch("/api/...")`) : cela ajoute un aller-retour réseau inutile. Appelez directement la fonction partagée.

### 6.7 API de requête dynamiques

Ces API lisent des informations **propres à la requête** : leur utilisation rend la portion concernée **dynamique**.

```tsx
import { cookies, headers, draftMode } from "next/headers";
import { connection } from "next/server";

const cookieStore = await cookies();
const theme = cookieStore.get("theme")?.value;

const headerList = await headers();
const ua = headerList.get("user-agent");

const { isEnabled } = await draftMode();

await connection(); // « attendre une vraie requête » avant de continuer (rend le rendu dynamique)
```

> **Version.** `cookies()`, `headers()`, `draftMode()`, `params`, `searchParams` sont **asynchrones** ; Next.js 16 supprime l'accès synchrone. Un **codemod** est fourni : `npx @next/codemod@canary upgrade latest`.

- `cookies()` : **lecture seule** dans les Server Components ; **écriture** (`set`, `delete`) uniquement dans les **Server Actions** et **Route Handlers** (les en-têtes sont déjà partis lors d'un rendu en *streaming*).
- `connection()` remplace l'ancien `unstable_noStore()` pour signaler « ne pas pré-rendre ceci ».
- Avec **Cache Components**, ces API ne sont **pas utilisables à l'intérieur** d'un périmètre `"use cache"` : lisez-les **à l'extérieur** et passez les valeurs en arguments (chapitre 7).

### 6.8 Exemple : pagination et filtre via l'URL

L'URL est une excellente source d'état **partageable**.

```tsx
// app/produits/page.tsx
export default async function Produits({
    searchParams,
}: {
    searchParams: Promise<{ page?: string; q?: string }>;
}) {
    const { page = "1", q = "" } = await searchParams;
    const numero = Math.max(1, Number(page) || 1);
    const produits = await db.produit.findMany({
        where: { nom: { contains: q } },
        skip: (numero - 1) * 20,
        take: 20,
    });

    return (
        <>
            <FormulaireRecherche valeur={q} />
            <ListeProduits produits={produits} />
            <Pagination page={numero} />
        </>
    );
}
```

### 6.9 Exécuter du code **après** la réponse : `after()`

Pour la journalisation, les statistiques ou les notifications **sans retarder** la réponse :

```tsx
import { after } from "next/server";

export default async function Page() {
    after(() => {
        enregistrerVisite(); // s'exécute après l'envoi de la réponse
    });
    return <h1>Bonjour</h1>;
}
```

Utilisable dans les Server Components, Server Actions, Route Handlers et Proxy (stable depuis Next.js 15.1).

### 6.10 Gestion des erreurs de données

| Situation | Stratégie |
| --- | --- |
| Ressource absente | `notFound()` |
| Erreur inattendue | Laisser remonter l'exception → `error.tsx` |
| Erreur attendue (Server Action) | Retourner `{ error: "..." }` |
| Échec partiel d'un composant | Isoler avec `Suspense` + frontière d'erreur (segment, slot ou `catchError`) |
| Réseau lent | Délai d'expiration (`AbortSignal.timeout(5000)`) |

```ts
const res = await fetch(url, { signal: AbortSignal.timeout(5000) });
```

### 6.11 Sécurité des données : la couche d'accès (DAL)

**Principes :**

- **Centraliser** l'accès aux données dans un module `server-only`.
- **Vérifier l'autorisation** dans chaque fonction d'accès, **pas seulement** dans la page ou le proxy.
- Retourner des **DTO** (objets minimaux) et non des enregistrements bruts : cela évite de fuiter un `passwordHash`.

```ts
// lib/dal.ts
import "server-only";
import { cache } from "react";
import { verifySession } from "./session";

export const getProfil = cache(async () => {
    const session = await verifySession();         // redirige si non connecté
    const user = await db.user.findUnique({ where: { id: session.userId } });
    return { id: user!.id, nom: user!.nom };       // DTO
});
```

### 6.12 Pièges fréquents

- **Cascades involontaires** : `await` en série de requêtes indépendantes.
- **Fetch côté client « par réflexe »** alors qu'un Server Component suffit.
- **Utiliser `cookies()` / `headers()` sans le savoir** : toute la route (ou toute la zone non protégée par `Suspense`) devient dynamique.
- **Oublier de gérer `res.ok`**.
- **Retourner des objets entiers de la base de données** au client.
- **Appeler son propre Route Handler** depuis un Server Component.

### 6.13 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| *Waterfall* | Enchaînement de requêtes qui s'attendent inutilement |
| Request Memoization | Déduplication des `fetch` identiques pendant un rendu |
| `React.cache` | Déduplication d'une fonction quelconque sur la durée d'une requête |
| Streaming | Envoi progressif de l'interface |
| `Suspense` | Mécanisme React d'attente avec interface de repli |
| API de requête | `cookies`, `headers`, `searchParams`, `connection`… (rendent dynamique) |
| `after()` | Exécute du code après l'envoi de la réponse |
| DAL | Couche centralisant l'accès aux données et l'autorisation |

### Synthèse du chapitre 6

Les Server Components chargent les données **directement**, en `async`. `React.cache` déduplique les accès sans `fetch` ; `Promise.all` parallélise. `Suspense` et le streaming réduisent le temps d'affichage perçu. Les API de requête (`cookies`, `headers`, `searchParams`) sont **asynchrones** et rendent le rendu **dynamique**. Sécurisez via une **DAL** et des **DTO**.

---

# Partie II — Rendu, cache et mutations

## 7. Mise en cache (*Caching*)

**Objectifs d'apprentissage.** Comprendre pourquoi et où Next.js met des choses en cache ; maîtriser le modèle **Cache Components** (`"use cache"`, `cacheLife`, `cacheTag`) ; distinguer contenu statique, mis en cache et dynamique ; utiliser les API de **revalidation** (`revalidateTag`, `updateTag`, `refresh`, `revalidatePath`) ; comprendre l'effet du cache sur la navigation côté client ; lire et maintenir du code du **modèle classique** (Next.js ≤ 15).

> **Version.** Le cache est **le sujet qui a le plus évolué**. Next.js 13 et 14 mettaient beaucoup de choses en cache **implicitement** ; Next.js 15 a supprimé la plupart des caches par défaut ; **Next.js 16 introduit un modèle explicite : Cache Components**, recommandé pour **toute** application depuis **16.4** et activé par défaut dans les nouveaux projets. Ce chapitre présente d'abord le modèle actuel, puis le modèle classique.

### 7.1 Pourquoi mettre en cache ?

Le cache évite de **refaire un travail coûteux** (requête de base de données, appel d'API, rendu d'un composant) quand le résultat n'a pas changé. Bénéfices : **rapidité**, **moindre charge**, **coût réduit**. Risque : **servir des données périmées** (*stale*). Toute stratégie de cache consiste donc à décider :

1. **Quoi** mettre en cache ?
2. **Pendant combien de temps** ?
3. **Comment invalider** quand les données changent ?

**Vocabulaire :**

| Terme | Définition |
| --- | --- |
| **Cache hit / miss** | La donnée est trouvée / absente dans le cache |
| **TTL** (*time to live*) | Durée de vie d'une entrée |
| **Stale** | Donnée périmée mais encore servable |
| **Stale-while-revalidate (SWR)** | Servir la donnée périmée immédiatement, la rafraîchir en arrière-plan |
| **Revalidation** | Mise à jour d'une entrée de cache |
| **Invalidation** | Marquer une entrée comme périmée |
| **Mémoïsation** | Réutiliser un résultat pendant un temps très court (ici : une requête de rendu) |

### 7.2 Le modèle Cache Components

**Principe.** Avec **Cache Components**, le comportement par défaut est : **le code s'exécute à la requête (dynamique)**. Vous **choisissez explicitement** ce qui est mis en cache avec la directive **`"use cache"`**. On peut la comprendre comme une version, au niveau d'un composant, de l'en-tête HTTP `Cache-Control`.

Le résultat : **dans une même route**, une **coque statique** (pré-rendue, servie instantanément depuis un CDN), des **îlots mis en cache** et des **zones dynamiques** diffusées en *streaming*. Ce modèle s'appuie sur le *Partial Prerendering (PPR)* et le remplace.

**Activation :**

```ts
// next.config.ts
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
    cacheComponents: true,
    partialPrefetching: true,   // (16.3+) préchargement partiel : fait partie du modèle depuis 16.4
};

export default nextConfig;
```

> **À savoir.** Depuis **16.4**, les projets créés avec `create-next-app` activent déjà ce modèle, et l'équipe annonce qu'il sera **le défaut de Next.js 17**. L'option `partialPrefetching` apporte le préchargement fin décrit au chapitre 12.

**Les trois catégories de contenu.** Avec Cache Components, chaque morceau de rendu relève de l'une d'elles :

| Catégorie | Exemple | Comportement |
| --- | --- | --- |
| **Statique** (déterministe) | JSX pur, calculs purs, imports de modules, lecture de fichier au build | **Inclus dans la coque statique** au build |
| **Mis en cache** (`"use cache"`) | Données d'API, requêtes de catalogue | Calculé, **stocké**, réutilisé ; inclus dans la coque si possible |
| **Dynamique** | `cookies()`, `headers()`, `searchParams`, `fetch` non mis en cache, `Math.random()` / `Date.now()` | **Calculé à chaque requête**, doit être **enveloppé dans `<Suspense>`** |

> **Règle de sécurité du framework.** Si Next.js détecte, au rendu, un accès à des données dynamiques **hors d'une frontière `<Suspense>`** et hors d'un `"use cache"`, il **signale une erreur** (message du type « *Uncached data was accessed outside of `<Suspense>`* »). Vous devez alors : (1) mettre la donnée en cache avec `"use cache"`, ou (2) envelopper le composant dans `<Suspense>` avec un *fallback*. Cela force à **décider explicitement** du comportement.

**Exemple complet :**

```tsx
// app/produits/page.tsx
import { Suspense } from "react";
import { cacheLife, cacheTag } from "next/cache";
import { cookies } from "next/headers";

async function Catalogue() {
    "use cache";
    cacheLife("hours");          // profil de durée
    cacheTag("catalogue");       // étiquette pour l'invalidation

    const produits = await db.produit.findMany();
    return (
        <ul>
            {produits.map((p) => <li key={p.id}>{p.nom}</li>)}
        </ul>
    );
}

async function Bienvenue() {
    const nom = (await cookies()).get("nom")?.value ?? "invité";  // dynamique
    return <p>Bonjour {nom}</p>;
}

export default function Page() {
    return (
        <>
            <h1>Produits</h1>                        {/* statique : dans la coque */}
            <Suspense fallback={<p>…</p>}>
                <Bienvenue />                        {/* dynamique : streaming */}
            </Suspense>
            <Catalogue />                            {/* mis en cache */}
        </>
    );
}
```

Next.js sert l'élément en cache (comme un fichier de `public/` ou un CDN) et rend l'élément dynamique **à la requête**, **dans la même réponse HTTP**.

### 7.3 La directive `"use cache"`

**Où la placer ?**

- **En haut d'un fichier** : tout ce que le module exporte (composants, fonctions asynchrones) est mis en cache.
- **Au début d'un composant asynchrone** ou **d'une fonction asynchrone**.

```ts
// Niveau fonction
export async function getArticles() {
    "use cache";
    return db.article.findMany();
}
```

```tsx
// Niveau fichier
"use cache";
export default async function Page() { /* ... */ }
```

**Comment la clé de cache est-elle calculée ?** La clé combine l'**identifiant de la fonction**, ses **arguments sérialisables**, les **valeurs capturées par fermeture** (*closures*) qui sont sérialisables, et le **build**. Deux appels avec les mêmes arguments partagent l'entrée ; des arguments différents produisent des entrées différentes.

```ts
async function getProduit(id: string) {
    "use cache";
    cacheTag(`produit-${id}`);
    return db.produit.findUnique({ where: { id } }); // une entrée par id
}
```

**Règles et limites :**

1. **Arguments et valeurs de retour sérialisables** (types primitifs, objets simples, tableaux, `Date`, `Map`, `Set`, éléments JSX…). Les fonctions et instances de classe ne le sont pas.
2. **Pas d'API de requête à l'intérieur** : `cookies()`, `headers()`, `searchParams` ne peuvent pas être lus **dans** un contexte `"use cache"` (le résultat dépendrait de la requête). **Lisez-les à l'extérieur** et passez les valeurs **en arguments** :

```tsx
export default async function Page() {
    const lang = (await cookies()).get("lang")?.value ?? "fr";   // dynamique, dehors
    return (
        <Suspense fallback={null}>
            <Contenu lang={lang} />
        </Suspense>
    );
}

async function Contenu({ lang }: { lang: string }) {
    "use cache";                                 // la clé inclut `lang`
    return <p>{await traduire(lang)}</p>;
}
```

3. Les **`children` et les props de type JSX** peuvent traverser un composant mis en cache **sans être lus** (*pass-through*) : un composant en cache peut envelopper du contenu dynamique placé par le parent.
4. Les **Server Actions** passées en props peuvent être transmises sans être exécutées dans le cache.
5. **`Date.now()`, `Math.random()`, `crypto.randomUUID()`** : dans un contexte de cache, la valeur est **figée** avec l'entrée. Hors cache et hors `connection()`, Next.js signale ces appels pour éviter des pages « statiques » aux valeurs surprenantes.
6. Les **paramètres racine** (`next/root-params`, 3.12) fonctionnent dans un périmètre `"use cache"`.

**Variantes avancées :**

| Directive | Usage |
| --- | --- |
| `"use cache"` | Cache par défaut, partagé côté serveur |
| `"use cache: private"` | Autorise la lecture de `cookies()` / `headers()` dans le périmètre ; mis en cache **uniquement dans la mémoire du navigateur** de l'utilisateur (données personnalisées) |
| `"use cache: remote"` | Utilise un **cache distant partagé** (gestionnaire de cache dédié) dans des contextes dynamiques ; utile en serverless |

Ces variantes sont plus récentes et spécialisées : consultez la documentation de votre version avant de les adopter.

### 7.4 `cacheLife` : la durée de vie

```ts
import { cacheLife } from "next/cache";
```

**Trois paramètres de temps :**

| Propriété | Signification |
| --- | --- |
| **`stale`** | Durée pendant laquelle le **client** peut utiliser la valeur sans demander au serveur |
| **`revalidate`** | Après ce délai, la valeur est périmée côté serveur : servie une dernière fois (SWR) **et régénérée en arrière-plan** |
| **`expire`** | Après ce délai sans trafic, l'entrée est **supprimée** : la prochaine requête est **bloquante** (régénération synchrone) |

Contrainte : `stale` ≤ `revalidate` ≤ `expire`.

**Profils prédéfinis :** `"seconds"`, `"minutes"`, `"hours"`, `"days"`, `"weeks"`, `"max"` (et un profil par défaut si l'on n'appelle pas `cacheLife`). Les durées exactes sont définies par le framework : vérifiez le tableau de la documentation de votre version.

```ts
async function getActualites() {
    "use cache";
    cacheLife("minutes");
    /* ... */
}
```

**Durées personnalisées**, en ligne :

```ts
cacheLife({ stale: 60, revalidate: 300, expire: 3600 }); // en secondes
```

ou par **profils nommés** dans la configuration :

```ts
// next.config.ts
const nextConfig = {
    cacheComponents: true,
    cacheLife: {
        editorial: { stale: 300, revalidate: 900, expire: 86400 },
    },
};
```

```ts
cacheLife("editorial");
```

### 7.5 `cacheTag` : étiqueter pour invalider

```ts
import { cacheTag } from "next/cache";

async function getPosts() {
    "use cache";
    cacheTag("posts");
    return db.post.findMany();
}
```

Plusieurs étiquettes sont possibles : `cacheTag("posts", "homepage")`. On invalide ensuite **toutes les entrées portant cette étiquette**, quel que soit l'endroit où elles sont utilisées.

### 7.6 Revalidation et invalidation

Toutes ces fonctions viennent de **`next/cache`**.

**`revalidateTag(tag, profil)` — *stale-while-revalidate*.**

```ts
import { revalidateTag } from "next/cache";

revalidateTag("posts", "max");
```

- Marque les entrées comme périmées ; **sert la valeur périmée immédiatement** puis régénère **en arrière-plan** (SWR).
- **Version 16** : le **second argument** (profil de cache, par exemple `"max"`, `"hours"` ou un objet `{ expire: ... }`) est **requis** ; la forme à un seul argument est dépréciée. `"max"` est généralement recommandé.
- Utilisable dans les **Server Actions** et **Route Handlers**.

**`updateTag(tag)` — « lire ses propres écritures ».**

```ts
"use server";
import { updateTag } from "next/cache";

export async function creerPost(formData: FormData) {
    await db.post.create({ data: { titre: String(formData.get("titre")) } });
    updateTag("posts");        // expire immédiatement ET rafraîchit dans la même requête
}
```

- **Uniquement dans les Server Actions.**
- Invalide **immédiatement** : l'utilisateur qui vient de muter voit **sa donnée à jour** dans la même navigation (*read-your-writes*), contrairement à `revalidateTag` (SWR).

**`refresh()` — rafraîchir ce qui n'est pas en cache.**

```ts
"use server";
import { refresh } from "next/cache";

export async function marquerLu(id: string) {
    await db.notification.update({ where: { id }, data: { lu: true } });
    refresh();   // re-rend la route courante (données non mises en cache, compteurs…)
}
```

- **Uniquement dans les Server Actions.** Ne touche **pas** au cache : il rafraîchit le routeur côté client et les données dynamiques.

**`revalidatePath(chemin, type?)` :**

```ts
import { revalidatePath } from "next/cache";

revalidatePath("/blog");                     // une page
revalidatePath("/blog/[slug]", "page");      // un motif de route dynamique
revalidatePath("/blog", "layout");           // un layout et ses enfants
revalidatePath("/", "layout");               // tout le site
```

Elle invalide le cache **associé à un chemin** (rendu de la route). Plus grossier que les étiquettes.

**Quel outil choisir ?**

| Besoin | Outil |
| --- | --- |
| L'auteur doit voir immédiatement son changement | `updateTag` |
| Contenu partagé, fraîcheur « raisonnable » | `revalidateTag(tag, "max")` |
| Rafraîchir de l'interface non mise en cache | `refresh()` |
| Invalider une page entière | `revalidatePath` |
| Depuis un webhook (CMS) | `revalidateTag` dans un Route Handler |

**Revalidation à la demande depuis un webhook :**

```ts
// app/api/revalidate/route.ts
import { revalidateTag } from "next/cache";
import { NextResponse } from "next/server";

export async function POST(request: Request) {
    const secret = request.headers.get("x-webhook-secret");
    if (secret !== process.env.REVALIDATE_SECRET) {
        return NextResponse.json({ ok: false }, { status: 401 });
    }
    const { tag } = await request.json();
    revalidateTag(tag, "max");
    return NextResponse.json({ ok: true });
}
```

### 7.7 Le cache côté client avec Cache Components *(ajout)*

Avec Cache Components, `"use cache"` ne gère plus seulement le **cache serveur** : Next.js peut aussi conserver l'interface mise en cache **dans le navigateur** pendant les navigations côté client. Ce cache client est ce qui permet de revenir instantanément sur une page déjà visitée. Il est piloté par les mêmes profils (`stale` notamment) et est déjà évoqué avec les préchargements partiels du chapitre 12. Retenez que **`stale`** dans `cacheLife` règle précisément **combien de temps le navigateur réutilise une valeur sans interroger le serveur**.

### 7.8 Ce que Cache Components change pour les anciennes options

Avec `cacheComponents: true` :

- `experimental.ppr` et `experimental.dynamicIO` sont **supprimés** (fusionnés dans Cache Components).
- Les **options de segment** `export const dynamic`, `export const revalidate`, `export const fetchCache`, `dynamicParams` (selon le cas) et `runtime = "edge"` ne sont **pas supportées** : on les remplace par `"use cache"`, `cacheLife`, `Suspense`, `connection()`.
- `unstable_cache` est remplacé par `"use cache"` ; `unstable_cacheLife` et `unstable_cacheTag` deviennent **`cacheLife`** et **`cacheTag`** (stables).
- `fetch(..., { cache: "force-cache" })` n'est plus le mécanisme recommandé : on met en cache **la fonction ou le composant** qui encapsule le `fetch`.

**Migrer un projet existant.** Next.js fournit un guide de migration vers Cache Components et, depuis 16.4, la commande `next upgrade --agent` ainsi que des *Skills* pour agents de codage qui guident cette migration. Procédez route par route : activez le modèle, corrigez les erreurs « accès dynamique hors `Suspense` », puis ajoutez `"use cache"` là où l'ancien code comptait sur le cache implicite.

### 7.9 Le modèle classique (Next.js ≤ 15, ou sans Cache Components) *(héritage)*

Utile pour comprendre et maintenir du code existant.

**Les quatre mécanismes historiques :**

| Mécanisme | Où | Contenu | Durée |
| --- | --- | --- | --- |
| **Request Memoization** | Serveur | Résultats des `fetch` GET identiques | Une requête de rendu |
| **Data Cache** | Serveur | Réponses de `fetch` | Persistant (jusqu'à revalidation) |
| **Full Route Cache** | Serveur | HTML + payload RSC des routes **statiques** | Persistant (jusqu'à revalidation ou redéploiement) |
| **Router Cache** | Client | Payload RSC des segments visités / préchargés | Session ou durée limitée |

**Options de `fetch` :**

```ts
fetch(url, { cache: "force-cache" });             // met en cache (Data Cache)
fetch(url, { cache: "no-store" });                // jamais en cache
fetch(url, { next: { revalidate: 3600 } });       // revalidation temporelle (ISR)
fetch(url, { next: { tags: ["posts"] } });        // étiquette pour revalidateTag
```

> **Version 15.** Sans option, `fetch` n'est **pas** mis en cache. Les Route Handlers `GET` ne sont plus mis en cache par défaut (`export const dynamic = "force-static"` pour l'activer). Le Router Cache ne conserve plus par défaut les segments **page** (`staleTime = 0`) ; layouts et états de chargement restent partagés.

**Options de segment (historique) :**

```ts
export const dynamic = "auto" | "force-dynamic" | "force-static" | "error";
export const revalidate = false | 0 | number;   // secondes
export const fetchCache = "auto" | "default-cache" | "only-cache" | "force-cache" | "force-no-cache" | "default-no-store" | "only-no-store";
export const dynamicParams = true | false;
export const runtime = "nodejs" | "edge";
export const preferredRegion = "auto" | "home" | "global" | "string" | "string[]";
export const maxDuration = 30;                  // plateformes supportées
```

**`unstable_cache` (pour ORM / SDK) :**

```ts
import { unstable_cache } from "next/cache";

const getUtilisateurs = unstable_cache(
    async () => db.user.findMany(),
    ["utilisateurs"],                       // clé
    { revalidate: 3600, tags: ["users"] }
);
```

**Router Cache : ajuster `staleTimes` (expérimental) :**

```ts
// next.config.ts
const nextConfig = {
    experimental: { staleTimes: { dynamic: 30, static: 180 } },
};
```

Le routeur côté client peut aussi être rafraîchi avec `router.refresh()`.

### 7.10 Cache du navigateur et en-têtes HTTP

En complément du cache de Next.js, les **en-têtes `Cache-Control`** pilotent les caches du navigateur et des CDN :

- Fichiers statiques de `_next/static/` : **immuables**, longue durée (noms hachés). Depuis 16.3, les ressources immuables peuvent même être **réutilisées d'un déploiement à l'autre**, puisqu'elles ne peuvent pas provoquer de décalage de version (*skew*).
- Images optimisées : `images.minimumCacheTTL` (défaut de 4 heures en Next.js 16).
- Pages : `s-maxage` et `stale-while-revalidate` sont ajoutés automatiquement pour l'ISR sur certaines plateformes ; personnalisables via `headers()` dans `next.config`.

### 7.11 Auto-hébergement et cache partagé

Par défaut, le cache est **local au processus / serveur** (mémoire + disque `.next/`). En **multi-instances** (plusieurs conteneurs, Kubernetes), chaque instance a **son propre cache** : la revalidation n'est pas partagée. Solutions : un **gestionnaire de cache personnalisé** (`cacheHandler`, `cacheHandlers` pour Cache Components) branché sur Redis ou S3, ou une plateforme qui fournit un cache partagé (chapitre 22).

### 7.12 Cache et sécurité

- **Ne mettez jamais en cache des données propres à un utilisateur** dans un cache **partagé** : la fuite entre utilisateurs est le risque principal. Avec `"use cache"`, **lisez les cookies / en-têtes à l'extérieur** et incluez l'identifiant dans les arguments, ou utilisez `"use cache: private"`.
- Un cache mal configuré derrière un CDN peut servir une page personnalisée à un autre visiteur : vérifiez les en-têtes `Vary` et `Cache-Control`.

### 7.13 Pièges fréquents

- **Oublier d'invalider** après une mutation : l'utilisateur voit des données obsolètes.
- **Mettre en cache une fonction qui lit des cookies** : erreur ou fuite entre utilisateurs.
- **Confondre `revalidateTag` (SWR) et `updateTag` (immédiat)**.
- **Appeler `updateTag` ou `refresh` hors d'une Server Action** : non autorisé.
- **Mélanger options de segment (`dynamic`, `revalidate`) et Cache Components** : incompatible.
- **Penser que le mode développement reflète la production** : testez avec `build` + `start`.
- **Appeler `revalidateTag("x")` sans second argument** (Next.js 16) : forme dépréciée.

### 7.14 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| Cache Components | Modèle de cache explicite fondé sur `"use cache"` |
| Coque statique | Partie de la page pré-rendue et servie instantanément |
| `"use cache"` | Directive qui met en cache une fonction, un composant ou un fichier |
| `cacheLife` | Règle `stale` / `revalidate` / `expire` |
| `cacheTag` | Étiquette servant à invalider des entrées |
| `updateTag` | Invalidation immédiate, réservée aux Server Actions |
| `revalidateTag` | Invalidation en SWR |
| `refresh` | Rafraîchit les données non mises en cache |
| SWR | *Stale-while-revalidate* |
| Data Cache / Router Cache | Caches du modèle classique (serveur / client) |

### Synthèse du chapitre 7

**Next.js 16 : dynamique par défaut, cache explicite avec `"use cache"`.** `cacheLife` règle `stale` / `revalidate` / `expire` ; `cacheTag` étiquette. `updateTag` (immédiat, Server Actions) ≠ `revalidateTag` (SWR) ≠ `refresh` (hors cache). Tout ce qui est dynamique doit être sous `Suspense`. Le modèle classique (options de `fetch`, ISR, `unstable_cache`) reste à connaître pour maintenir du code existant.

---

## 8. Stratégies de rendu : SSR, SSG, ISR, PPR, CSR

**Objectifs d'apprentissage.** Définir précisément chaque stratégie de rendu ; savoir comment Next.js décide qu'une route est statique ou dynamique ; comprendre la coque statique de Cache Components et l'ISR amélioré de 16.3 ; garantir qu'une page reste statique avec `ensureStatic` ; choisir la stratégie adaptée à un cas d'usage ; connaître les runtimes et l'export statique ; comprendre les **Core Web Vitals**.

### 8.1 Définitions

| Stratégie | Quand le HTML est-il produit ? | Où ? | Idéal pour |
| --- | --- | --- | --- |
| **SSG** — *Static Site Generation* | **Au build** | Machine de build | Blogs, documentation, pages marketing |
| **SSR** — *Server-Side Rendering* | **À chaque requête** | Serveur | Contenu personnalisé ou toujours frais |
| **ISR** — *Incremental Static Regeneration* | Au build **puis régénéré** (délai ou événement) | Serveur | Catalogues, actualités |
| **CSR** — *Client-Side Rendering* | **Dans le navigateur** | Client | Zones très interactives, tableaux de bord privés |
| **Streaming** | Progressivement, par morceaux | Serveur → client | Pages avec zones lentes |
| **PPR** — *Partial Prerendering* (aujourd'hui via Cache Components) | Coque au build + trous dynamiques à la requête | Mixte | La plupart des pages modernes |

**SSG.** Le HTML est **calculé une fois** puis servi comme un fichier (idéalement par un **CDN**). Très rapide, peu coûteux. Limite : les données sont figées jusqu'au prochain build (sauf ISR).

**SSR.** Le HTML est **généré à chaque requête** : données toujours fraîches et personnalisables (cookies, en-têtes). Coût : latence serveur, charge, TTFB plus élevé.

**ISR.** Page statique **régénérée en arrière-plan** :

- **Temporelle** : toutes les *n* secondes (modèle classique : `revalidate`) ; avec Cache Components : `cacheLife`.
- **À la demande** : `revalidateTag`, `revalidatePath`, `updateTag`.
- Comportement SWR : un visiteur reçoit la version existante ; la régénération se produit en arrière-plan ; les suivants reçoivent la nouvelle.

**CSR.** Le serveur envoie un squelette ; le navigateur charge les données (SWR, TanStack Query). Convient aux zones **derrière authentification** sans besoin de SEO, ou très interactives.

**PPR → Cache Components.** Une **même route** combine :

1. une **coque statique** (layout, titres, navigation, éléments en cache) servie instantanément depuis un CDN ;
2. des **trous dynamiques** (`Suspense`) remplis en streaming depuis le serveur.

C'est le modèle recommandé de Next.js 16.4 (chapitre 7).

### 8.2 Comment Next.js choisit : statique ou dynamique ?

**Modèle classique (sans Cache Components).** Une route est **statique par défaut** et devient **dynamique** quand elle utilise :

- `cookies()`, `headers()`, `draftMode()` (dans leurs formes asynchrones) ;
- `searchParams` (props de page) ;
- `connection()` ;
- un `fetch` avec `cache: "no-store"` ou `revalidate: 0` ;
- `export const dynamic = "force-dynamic"` ;
- un Route Handler avec méthode non-GET ou utilisant l'objet `Request` dynamiquement.

**Avec Cache Components.** Tout ce qui est **dynamique** doit être sous **`<Suspense>`** (ou mis en cache avec `"use cache"`). Ce qui est déterministe et mis en cache est inclus dans la **coque statique**. Le tableau des routes affiché par `next build` indique alors, par exemple, les routes **partiellement pré-rendues**.

### 8.3 Pré-génération de routes dynamiques

`generateStaticParams` (chapitre 3) génère au build les pages d'une route dynamique. Stratégie courante : **pré-générer les pages les plus visitées** (liste courte) et laisser les autres être générées **à la demande**, puis mises en cache.

**ISR amélioré avec Cache Components (16.3).** Quand vous ne pré-rendez qu'**une partie** des pages d'une route, les autres posaient un dilemme : afficher une coque de chargement sans jamais être pré-rendues, ou bloquer le premier visiteur. Désormais, **une page non pré-rendue sert une coque de chargement instantanée à sa première visite, puis est mise à niveau en arrière-plan** vers la page complète ; les visiteurs suivants reçoivent le contenu final depuis le cache.

### 8.4 Garantir qu'une page reste statique : `ensureStatic` *(ajout, 16.4)*

Avec Cache Components, un seul composant dynamique glissé par erreur dans une page peut dégrader ses performances et son coût. `ensureStatic` fait **échouer le build** si du contenu dynamique apparaît :

```tsx
// app/blog/[slug]/page.tsx
export const ensureStatic = "navigation";

export default function Page() {
    return (
        <>
            <UserAvatar />   {/* composant dynamique : le build échoue */}
            <Contenu />
        </>
    );
}
```

| Valeur | Garantie |
| --- | --- |
| `"shell"` | Seul du contenu **statique** est récupéré à la première découverte de la route |
| `"prefetch"` | Les liens à préchargement explicite ne récupèrent que du contenu statique |
| `"navigation"` | La plus stricte : les navigations vers cette route ne se rendent **jamais** à la requête |

On peut l'ajouter à un **layout** pour appliquer la garantie à toutes les pages qu'il enveloppe, puis la relâcher plus bas pour les pages qui ont besoin de dynamique. Utile pour les boutiques, pages marketing et blogs.

### 8.5 Runtimes d'exécution

| Runtime | Description | Remarques |
| --- | --- | --- |
| **Node.js** | Par défaut ; accès complet aux API Node | Recommandé |
| **Edge** | Environnement léger (API Web), démarrage très rapide, proche de l'utilisateur | API limitées ; attention : non supporté avec Cache Components ; le **Proxy** de Next.js 16 s'exécute sur **Node.js** |

```ts
export const runtime = "nodejs"; // (modèle classique) ou "edge" pour un Route Handler / une page concernée
```

### 8.6 Core Web Vitals : mesurer le résultat

| Métrique | Définition | Seuil « bon » |
| --- | --- | --- |
| **TTFB** (*Time To First Byte*) | Délai avant le premier octet reçu | < 0,8 s |
| **FCP** (*First Contentful Paint*) | Premier contenu affiché | < 1,8 s |
| **LCP** (*Largest Contentful Paint*) | Affichage du plus grand élément visible | < 2,5 s |
| **INP** (*Interaction to Next Paint*) | Réactivité aux interactions (remplace FID) | < 200 ms |
| **CLS** (*Cumulative Layout Shift*) | Stabilité visuelle (décalages) | < 0,1 |

Mesure dans Next.js :

```tsx
"use client";
import { useReportWebVitals } from "next/web-vitals";

export function WebVitals() {
    useReportWebVitals((metric) => {
        console.log(metric); // envoyer vers votre outil d'analyse
    });
    return null;
}
```

### 8.7 Guide de décision

| Contenu | Stratégie conseillée |
| --- | --- |
| Page statique (À propos, documentation) | SSG / coque statique |
| Articles de blog | SSG + `generateStaticParams`, revalidation via CMS |
| Catalogue produit | `"use cache"` + `cacheLife` + `cacheTag`, invalidation par webhook |
| Page produit + stock en temps réel | Coque en cache + stock en `Suspense` dynamique |
| Tableau de bord utilisateur | Dynamique (cookies) avec streaming ; éventuellement CSR pour les widgets |
| Recherche | Dynamique (`searchParams`) ou CSR avec SWR |
| Contenu très personnalisé | SSR / `Suspense` |

### 8.8 Export statique

```ts
// next.config.ts
const nextConfig = { output: "export" };
export default nextConfig;
```

Génère un dossier `out/` de fichiers HTML / CSS / JS à héberger sur n'importe quel serveur statique. **Limites** : pas de Server Actions, pas de Route Handlers dynamiques, pas de Proxy, pas de rendu dynamique, pas d'optimisation d'images par défaut (loader personnalisé nécessaire), pas d'ISR.

### 8.9 Pièges fréquents

- **Croire qu'une page est statique** alors qu'un composant lit `cookies()` ou `searchParams`.
- **Ne pas lire le tableau de build** pour vérifier le mode de rendu.
- **SSR partout « par défaut »** : coût inutile quand le cache suffit.
- **CSR partout** : perte de SEO et de performance perçue.
- **Utiliser `export const dynamic`** avec Cache Components : non supporté.
- **Oublier qu'un layout racine dynamique** (lecture de cookies hors `Suspense`) casse la coque statique de **toutes** les pages.

### 8.10 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| SSG / SSR / ISR / CSR | Génération statique / côté serveur / statique régénérée / côté client |
| PPR | Pré-rendu partiel : coque statique + trous dynamiques |
| Coque (*shell*) | Partie statique servie immédiatement |
| `ensureStatic` | Garde-fou qui fait échouer le build si du dynamique apparaît |
| Runtime | Environnement d'exécution (Node.js, Edge) |
| LCP / INP / CLS / TTFB | Métriques de performance perçue |
| Export statique | Sortie de fichiers sans serveur (`output: "export"`) |

### Synthèse du chapitre 8

SSG = au build ; SSR = à la requête ; ISR = statique régénéré ; CSR = navigateur ; **PPR / Cache Components = coque statique + trous dynamiques**. Le caractère statique ou dynamique découle de **ce que vos composants utilisent**. `ensureStatic` verrouille la nature statique d'une route. Mesurez avec les Core Web Vitals.

---

## 9. Server Actions et mutations

**Objectifs d'apprentissage.** Définir et appeler des **Server Actions** (formulaires et événements) ; gérer **validation**, **erreurs**, **états de chargement** et **mises à jour optimistes** ; revalider le cache et rediriger après une mutation ; téléverser des fichiers ; **sécuriser** les actions ; choisir entre Server Action et Route Handler.

### 9.1 Définition

Une **Server Action** (plus largement, une **Server Function**) est une **fonction asynchrone exécutée sur le serveur**, appelable depuis le client. Elle sert aux **mutations** (créer, modifier, supprimer) et à tout traitement qui ne doit pas s'exécuter dans le navigateur.

> **Terminologie.** *Server Function* : toute fonction serveur appelable par le client. *Server Action* : une Server Function utilisée comme **action** (passée à `<form action>` ou appelée dans une transition), généralement pour une mutation.

**Fonctionnement technique :**

- Next.js génère un **identifiant** pour chaque action et un **endpoint** interne ; l'appel est une requête **`POST`** envoyée au serveur.
- Les **arguments** et le **résultat** sont sérialisés.
- Les actions d'un même client sont traitées **l'une après l'autre** (file d'attente).
- Les variables capturées par fermeture sont **chiffrées** ; les actions **non utilisées** sont éliminées du build.

### 9.2 Créer une Server Action

**Option 1 : dans un fichier dédié (recommandé).**

```ts
// app/actions.ts
"use server";   // toutes les fonctions exportées sont des Server Actions

import { updateTag } from "next/cache";
import { redirect } from "next/navigation";

export async function creerPost(formData: FormData) {
    const titre = String(formData.get("titre") ?? "");
    await db.post.create({ data: { titre } });
    updateTag("posts");
    redirect("/blog");
}
```

**Option 2 : directive en ligne dans un Server Component.**

```tsx
export default function Page() {
    async function supprimer(formData: FormData) {
        "use server";
        await db.post.delete({ where: { id: String(formData.get("id")) } });
    }
    return (
        <form action={supprimer}>
            <input type="hidden" name="id" value="42" />
            <button>Supprimer</button>
        </form>
    );
}
```

> Dans un **Client Component**, on **ne peut pas** définir une action en ligne : il faut l'**importer** depuis un fichier `"use server"`.

### 9.3 Utilisation dans un formulaire

Passer l'action à l'attribut **`action`** de `<form>` :

```tsx
import { creerPost } from "./actions";

export default function Formulaire() {
    return (
        <form action={creerPost}>
            <input name="titre" required />
            <textarea name="contenu" />
            <button type="submit">Publier</button>
        </form>
    );
}
```

- L'action reçoit un objet **`FormData`** natif.
- **Amélioration progressive** : dans un Server Component, le formulaire **fonctionne même sans JavaScript** (soumission HTML classique) ; après hydratation, il est envoyé sans rechargement.
- Lire les champs : `formData.get("nom")`, `formData.getAll("tags")`, `Object.fromEntries(formData)`.

### 9.4 Passer des arguments supplémentaires : `bind`

```tsx
import { supprimerPost } from "./actions";

export function BoutonSupprimer({ id }: { id: string }) {
    const supprimerAvecId = supprimerPost.bind(null, id); // 1er argument lié
    return (
        <form action={supprimerAvecId}>
            <button>Supprimer</button>
        </form>
    );
}
```

```ts
export async function supprimerPost(id: string, formData: FormData) { /* ... */ }
```

### 9.5 Appels depuis des Client Components

**Depuis un gestionnaire d'événement :**

```tsx
"use client";
import { useTransition } from "react";
import { aimer } from "./actions";

export function Like({ id }: { id: string }) {
    const [pending, startTransition] = useTransition();
    return (
        <button
            disabled={pending}
            onClick={() => startTransition(async () => { await aimer(id); })}
        >
            {pending ? "…" : "J'aime"}
        </button>
    );
}
```

**Depuis `useEffect`** : possible, mais à réserver aux cas particuliers (par exemple un compteur de vues).

### 9.6 État du formulaire : `useActionState`

```tsx
"use client";
import { useActionState } from "react";
import { inscrire } from "./actions";

type Etat = { erreurs?: { email?: string[] }; message?: string } | null;

export default function Inscription() {
    const [etat, action, pending] = useActionState<Etat, FormData>(inscrire, null);

    return (
        <form action={action}>
            <input name="email" type="email" aria-invalid={!!etat?.erreurs?.email} />
            {etat?.erreurs?.email && <p role="alert">{etat.erreurs.email[0]}</p>}
            <button disabled={pending}>{pending ? "Envoi…" : "S'inscrire"}</button>
            {etat?.message && <p>{etat.message}</p>}
        </form>
    );
}
```

L'action reçoit **l'état précédent** en premier argument :

```ts
// actions.ts
"use server";
import { z } from "zod";

const schema = z.object({ email: z.string().email("Email invalide") });

export async function inscrire(prev: unknown, formData: FormData) {
    const resultat = schema.safeParse({ email: formData.get("email") });
    if (!resultat.success) {
        return { erreurs: resultat.error.flatten().fieldErrors };
    }
    await db.inscrit.create({ data: { email: resultat.data.email } });
    return { message: "Inscription réussie !" };
}
```

`useActionState` retourne `[état, actionEnveloppée, enCours]`.

### 9.7 Indicateur de chargement : `useFormStatus`

```tsx
"use client";
import { useFormStatus } from "react-dom";

export function BoutonEnvoyer() {
    const { pending } = useFormStatus();
    return <button disabled={pending}>{pending ? "Envoi…" : "Envoyer"}</button>;
}
```

Attention : `useFormStatus` doit être appelé dans un composant **enfant** du `<form>`, pas dans le composant qui rend le `<form>`.

### 9.8 Mises à jour optimistes : `useOptimistic`

Afficher **immédiatement** le résultat attendu, puis le réconcilier avec la réponse du serveur.

```tsx
"use client";
import { useOptimistic } from "react";
import { ajouterTache } from "./actions";

export function Taches({ taches }: { taches: { id: string; titre: string }[] }) {
    const [optimistes, ajouterOptimiste] = useOptimistic(
        taches,
        (etat, titre: string) => [...etat, { id: "temp", titre }]
    );

    async function action(formData: FormData) {
        const titre = String(formData.get("titre"));
        ajouterOptimiste(titre);          // mise à jour immédiate de l'interface
        await ajouterTache(titre);        // vraie mutation
    }

    return (
        <>
            <ul>{optimistes.map((t) => <li key={t.id}>{t.titre}</li>)}</ul>
            <form action={action}><input name="titre" /><button>Ajouter</button></form>
        </>
    );
}
```

En cas d'échec, l'état **revient automatiquement** à la valeur réelle.

### 9.9 Validation des données

**Ne faites jamais confiance au client.** Validez **toujours côté serveur** (schémas **Zod**, Valibot, ArkType…), même si le formulaire valide déjà côté client : la validation client n'est qu'un confort.

```ts
const Schema = z.object({
    titre: z.string().min(3).max(120),
    prix: z.coerce.number().positive(),     // coerce : FormData envoie des chaînes
    tags: z.array(z.string()).max(5).default([]),
});

const parsed = Schema.safeParse({
    titre: formData.get("titre"),
    prix: formData.get("prix"),
    tags: formData.getAll("tags"),
});
```

### 9.10 Gestion des erreurs

| Type | Traitement |
| --- | --- |
| **Erreurs attendues** (validation, email déjà pris, droits insuffisants) | **Retourner** un objet d'erreur (`{ erreur: "..." }`) |
| **Erreurs inattendues** (bug, base indisponible) | Laisser **l'exception** remonter : `error.tsx` ou `catchError` l'attrape |

Évitez `throw` pour les erreurs de validation : l'utilisateur perdrait la saisie du formulaire.

### 9.11 Revalider, rafraîchir, rediriger

```ts
"use server";
import { updateTag, revalidatePath, refresh } from "next/cache";
import { redirect } from "next/navigation";

export async function modifierPost(id: string, data: FormData) {
    await db.post.update({ where: { id }, data: { titre: String(data.get("titre")) } });

    updateTag("posts");            // lecture immédiate des données à jour (Next.js 16)
    // ou revalidateTag("posts", "max"); revalidatePath("/blog"); refresh();

    redirect(`/blog/${id}`);       // en dernier : lève une exception interne
}
```

Attention : **`redirect()` doit venir après** la revalidation et **hors `try` / `catch`**.

### 9.12 Cookies dans les actions

```ts
"use server";
import { cookies } from "next/headers";

export async function choisirTheme(theme: "clair" | "sombre") {
    const store = await cookies();
    store.set("theme", theme, { httpOnly: true, secure: true, sameSite: "lax", path: "/", maxAge: 60 * 60 * 24 * 365 });
}
```

Les Server Actions et Route Handlers sont les **seuls** endroits où l'on peut **écrire** des cookies côté serveur.

### 9.13 Téléversement de fichiers

```ts
"use server";
export async function televerser(formData: FormData) {
    const fichier = formData.get("fichier") as File;
    if (!fichier || fichier.size === 0) return { erreur: "Aucun fichier" };
    if (fichier.size > 2 * 1024 * 1024) return { erreur: "Fichier trop volumineux" };
    if (!["image/png", "image/jpeg"].includes(fichier.type)) return { erreur: "Type refusé" };
    const octets = Buffer.from(await fichier.arrayBuffer());
    // enregistrer dans un stockage objet (S3, etc.)
}
```

Formulaire : `<form action={televerser}><input type="file" name="fichier" /></form>`. La limite de taille du corps d'une action est de **1 Mo par défaut** ; ajustez :

```ts
// next.config.ts
const nextConfig = { experimental: { serverActions: { bodySizeLimit: "5mb" } } };
```

Pour de gros fichiers : **URL pré-signées** pour téléverser directement vers le stockage. Le type MIME déclaré par le client est falsifiable : contrôlez aussi le contenu réel (signature du fichier) pour les cas sensibles.

### 9.14 Le composant `<Form>` de `next/form`

```tsx
import Form from "next/form";

export default function Recherche() {
    return (
        <Form action="/recherche">
            <input name="q" />
            <button>Chercher</button>
        </Form>
    );
}
```

Pour les formulaires de **recherche (GET)** : navigation **côté client** avec préchargement de l'interface de chargement et conservation de l'état des layouts, avec **amélioration progressive**.

### 9.15 Sécurité des Server Actions

Les Server Actions sont des **endpoints HTTP publics**. Appliquez la même rigueur qu'à une API :

1. **Authentification et autorisation** dans **chaque** action (vérifier la session et les droits **à l'intérieur** de l'action).
2. **Validation** des entrées (types, tailles, formats).
3. **Protection CSRF** : Next.js n'accepte que `POST` et compare les en-têtes `Origin` et `Host` ; autorisez des domaines additionnels avec `serverActions.allowedOrigins` si nécessaire (reverse proxy).
4. **Chiffrement** des variables capturées par fermeture (clé configurable pour les déploiements multi-instances via `NEXT_SERVER_ACTIONS_ENCRYPTION_KEY`).
5. **Limitation de débit** (*rate limiting*) pour les actions sensibles (connexion, envoi d'e-mail).
6. **Ne jamais renvoyer** de données sensibles superflues.
7. Les identifiants d'actions non utilisées ne sont pas exposés, mais **les actions exportées restent appelables** : vérifiez toujours les droits.

> **Mises à jour de sécurité.** Les Server Functions ont déjà fait l'objet de correctifs importants dans l'écosystème React / Next.js. Appliquez systématiquement les versions de sécurité (programme formel depuis juillet 2026, chapitre 24).

### 9.16 Quand préférer un Route Handler ?

| Server Action | Route Handler |
| --- | --- |
| Mutation déclenchée par **votre** interface | **API publique**, consommée par des clients tiers (mobile, partenaires) |
| Formulaires, amélioration progressive | **Webhooks**, endpoints REST / GraphQL |
| Revalidation intégrée | Réponses non-JSON, streaming, formats personnalisés |

### 9.17 Pièges fréquents

- **Oublier l'autorisation** dans l'action (« la page est protégée, donc l'action aussi » : faux).
- **`redirect()` dans un `try` / `catch`**.
- **Utiliser une action pour *lire* des données** : privilégiez les Server Components (les actions sont mises en file et ne conviennent pas au chargement).
- **`useFormStatus` au mauvais niveau**.
- **Retourner des valeurs non sérialisables**.
- **Valider seulement côté client**.
- **Oublier d'invalider le cache** après la mutation.

### 9.18 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| Server Action | Fonction serveur utilisée comme action de formulaire ou de transition |
| Server Function | Toute fonction serveur appelable par le client |
| `FormData` | Objet natif contenant les champs d'un formulaire |
| Amélioration progressive | Fonctionnement sans JavaScript, enrichi après hydratation |
| `useActionState` | Hook gérant l'état renvoyé par une action |
| `useOptimistic` | Hook d'état optimiste |
| CSRF | Falsification de requête inter-sites |
| `bind` | Pré-remplissage d'arguments d'une fonction |

### Synthèse du chapitre 9

`"use server"` + `<form action>` = **mutation avec amélioration progressive**. `useActionState`, `useFormStatus`, `useOptimistic` soignent l'expérience. Après mutation : `updateTag` / `revalidateTag` / `revalidatePath`, **puis** `redirect`. **Toujours valider et autoriser côté serveur** : une action est un endpoint public.

---

## 10. Route Handlers (API)

**Objectifs d'apprentissage.** Créer des endpoints HTTP avec `route.ts` ; utiliser `Request`, `NextRequest` et `NextResponse` ; gérer paramètres dynamiques, cookies, en-têtes, codes de statut, cache, CORS, streaming et webhooks ; appeler un Route Handler ; appliquer les bonnes pratiques d'API.

### 10.1 Principe

Un **Route Handler** est défini dans un fichier **`route.ts`** (ou `.js`) à l'intérieur d'`app/`. Il exporte des **fonctions nommées d'après les méthodes HTTP** : `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`. Il s'appuie sur les API Web standard **`Request`** et **`Response`**.

```ts
// app/api/bonjour/route.ts  →  /api/bonjour
export async function GET() {
    return Response.json({ message: "Bonjour" });
}
```

- `OPTIONS` est implémentée automatiquement si vous ne la définissez pas.
- Une méthode non exportée renvoie **405 *Method Not Allowed***.
- Un dossier ne peut pas avoir à la fois un `page` et un `route` pour la **même URL**.

### 10.2 Lire la requête

```ts
import { NextRequest, NextResponse } from "next/server";

export async function GET(request: NextRequest) {
    const q = request.nextUrl.searchParams.get("q");        // paramètres de requête
    const jeton = request.headers.get("authorization");     // en-têtes
    const session = request.cookies.get("session")?.value;  // cookies
    return NextResponse.json({ q, aSession: !!session });
}

export async function POST(request: Request) {
    const donnees = await request.json();                   // corps JSON
    // autres : await request.formData(), await request.text(), await request.arrayBuffer()
    return NextResponse.json({ recu: donnees }, { status: 201 });
}
```

### 10.3 Segments dynamiques

```ts
// app/api/posts/[id]/route.ts
export async function GET(
    _request: Request,
    { params }: { params: Promise<{ id: string }> }
) {
    const { id } = await params;
    const post = await db.post.findUnique({ where: { id } });
    if (!post) return Response.json({ erreur: "Introuvable" }, { status: 404 });
    return Response.json(post);
}

export async function DELETE(_req: Request, ctx: RouteContext<"/api/posts/[id]">) {
    const { id } = await ctx.params;
    await db.post.delete({ where: { id } });
    return new Response(null, { status: 204 });
}
```

(`RouteContext<...>` est un helper de types généré par Next.js ; voir chapitre 20.)

### 10.4 Construire des réponses

```ts
// JSON
return NextResponse.json({ ok: true }, { status: 200, headers: { "X-Custom": "1" } });

// Texte / HTML / autre
return new Response("<h1>Salut</h1>", { headers: { "Content-Type": "text/html; charset=utf-8" } });

// Redirection
return NextResponse.redirect(new URL("/login", request.url));

// Cookies en réponse
const res = NextResponse.json({ ok: true });
res.cookies.set("visite", "1", { httpOnly: true, maxAge: 3600 });
return res;
```

Cookies et en-têtes via les API serveur :

```ts
import { cookies, headers } from "next/headers";
const store = await cookies();
store.set("a", "b");
```

### 10.5 Codes de statut courants

| Code | Sens | Usage |
| --- | --- | --- |
| 200 | OK | Lecture réussie |
| 201 | Created | Ressource créée |
| 204 | No Content | Suppression réussie |
| 301 / 308 | Redirection permanente | |
| 302 / 307 | Redirection temporaire | |
| 400 | Bad Request | Entrée invalide |
| 401 | Unauthorized | Non authentifié |
| 403 | Forbidden | Authentifié mais interdit |
| 404 | Not Found | Ressource absente |
| 409 | Conflict | Doublon, état incompatible |
| 422 | Unprocessable Entity | Validation échouée |
| 429 | Too Many Requests | Limitation de débit |
| 500 | Internal Server Error | Erreur serveur |

### 10.6 Mise en cache des Route Handlers

- **Version 15+** : les handlers `GET` **ne sont pas mis en cache par défaut**.
- **Modèle classique** : `export const dynamic = "force-static"` permet de les pré-rendre au build (flux RSS, `sitemap` personnalisé) ; `export const revalidate = 3600` pour une régénération temporelle.
- **Avec Cache Components** : le handler est **dynamique par défaut** ; pour mettre en cache, extrayez la logique dans une **fonction `"use cache"`** appelée par le handler (la directive ne se place pas dans le corps de la méthode du handler lui-même).

```ts
// avec Cache Components
import { cacheLife } from "next/cache";

async function getStats() {
    "use cache";
    cacheLife("minutes");
    return db.stats.compute();
}

export async function GET() {
    return Response.json(await getStats());
}
```

### 10.7 CORS

```ts
const entetesCors = {
    "Access-Control-Allow-Origin": "https://app.exemple.com",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Authorization",
};

export async function OPTIONS() {
    return new Response(null, { status: 204, headers: entetesCors });
}

export async function GET() {
    return Response.json({ ok: true }, { headers: entetesCors });
}
```

Évitez `Access-Control-Allow-Origin: *` pour les API qui exigent des identifiants.

### 10.8 Webhooks

Réception d'un webhook avec **vérification de signature** (le **corps brut** est nécessaire) :

```ts
import crypto from "node:crypto";

export async function POST(request: Request) {
    const brut = await request.text();                          // corps brut, pas .json()
    const signature = request.headers.get("x-signature") ?? "";
    const attendu = crypto.createHmac("sha256", process.env.WEBHOOK_SECRET!).update(brut).digest("hex");

    const ok =
        signature.length === attendu.length &&
        crypto.timingSafeEqual(Buffer.from(signature), Buffer.from(attendu));
    if (!ok) return new Response("Signature invalide", { status: 401 });

    const evenement = JSON.parse(brut);
    // traiter l'événement de façon idempotente ; répondre vite (2xx)
    return new Response(null, { status: 204 });
}
```

### 10.9 Streaming et Server-Sent Events

```ts
export async function GET() {
    const encodeur = new TextEncoder();
    const flux = new ReadableStream({
        async start(controller) {
            for (let i = 0; i < 5; i++) {
                controller.enqueue(encodeur.encode(`data: tick ${i}\n\n`));
                await new Promise((r) => setTimeout(r, 1000));
            }
            controller.close();
        },
    });
    return new Response(flux, {
        headers: { "Content-Type": "text/event-stream", "Cache-Control": "no-cache", Connection: "keep-alive" },
    });
}
```

### 10.10 Appeler un Route Handler

- Depuis un **Client Component** : `fetch("/api/...")`, SWR, TanStack Query.
- Depuis un **client externe** : `curl`, application mobile, service tiers.
- **Pas** depuis un Server Component : appelez directement la fonction partagée.

```bash
curl -X POST http://localhost:3000/api/posts \
    -H "Content-Type: application/json" \
    -d '{"titre":"Salut"}'
```

### 10.11 Bonnes pratiques d'API

- Valider les entrées (Zod) ; renvoyer des erreurs **cohérentes** (`{ erreur, details }`).
- Authentifier et autoriser **chaque** handler.
- Pagination, tri, limites par défaut.
- **Idempotence** pour les webhooks et paiements.
- Journalisation et identifiants de corrélation.
- Versionner si l'API est publique (`/api/v1/...`).

### 10.12 Pièges fréquents

- **Lire le corps deux fois** (`json()` puis `text()`) : le flux est consommé.
- **Oublier `await params`**.
- **Compter sur le cache par défaut** (supprimé en 15).
- **Définir un CORS ouvert partout**.
- **Écrire un Route Handler pour ce qu'une Server Action ferait mieux** (formulaires internes).
- **Placer `"use cache"` directement dans le handler** avec Cache Components : extrayez une fonction.

### 10.13 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| Route Handler | Endpoint HTTP défini dans `route.ts` |
| `NextRequest` / `NextResponse` | Extensions de `Request` / `Response` (cookies, `nextUrl`, redirections) |
| Webhook | Appel HTTP émis par un service tiers vers votre application |
| HMAC | Signature de message par clé secrète partagée |
| CORS | Règles d'accès inter-origines du navigateur |
| SSE | *Server-Sent Events* : flux serveur → navigateur |
| Idempotence | Répéter une opération produit le même résultat |

### Synthèse du chapitre 10

`route.ts` + fonctions `GET` / `POST` / … fondées sur `Request` / `Response`. `NextRequest` / `NextResponse` ajoutent `nextUrl`, `cookies` et les helpers de redirection. Idéal pour **API publiques, webhooks, flux, endpoints non-JSON** ; pour les mutations de votre propre interface, préférez les Server Actions.

---

## 11. Proxy (ex-Middleware)

**Objectifs d'apprentissage.** Comprendre le rôle et les **limites** du Proxy ; écrire des règles de redirection, réécriture, en-têtes et cookies ; configurer le `matcher` ; connaître l'ordre d'exécution ; mesurer les enjeux de sécurité ; migrer de `middleware.ts` vers `proxy.ts`.

### 11.1 Définition

Le **Proxy** est un code qui s'exécute **avant** qu'une requête n'atteigne une route (page, Route Handler, fichier statique). Il peut **lire** la requête et **modifier** la réponse : rediriger, réécrire l'URL, ajouter des en-têtes ou des cookies, ou répondre directement.

> **Version 16.** Le fichier **`middleware.ts`** est **renommé `proxy.ts`**, et la fonction exportée `middleware` devient `proxy`, pour clarifier qu'il agit comme une **frontière réseau** devant l'application. La logique reste identique. `proxy.ts` s'exécute sur le runtime **Node.js**. `middleware.ts` fonctionne encore (déprécié) et reste nécessaire si vous avez besoin du runtime **Edge**.

**Migration automatique :**

```bash
npx @next/codemod@canary middleware-to-proxy .
```

### 11.2 Emplacement et structure

Un seul fichier à la **racine du projet** (ou dans `src/` si utilisé), au même niveau que `app/`.

```ts
// proxy.ts
import { NextResponse, type NextRequest } from "next/server";

export function proxy(request: NextRequest) {
    const { pathname } = request.nextUrl;

    // 1) Redirection
    if (pathname.startsWith("/ancien-blog")) {
        return NextResponse.redirect(new URL(pathname.replace("/ancien-blog", "/blog"), request.url));
    }

    // 2) Protection optimiste
    const session = request.cookies.get("session")?.value;
    if (pathname.startsWith("/dashboard") && !session) {
        return NextResponse.redirect(new URL("/login", request.url));
    }

    // 3) En-têtes
    const reponse = NextResponse.next();
    reponse.headers.set("x-pathname", pathname);
    return reponse;
}

export const config = {
    matcher: ["/dashboard/:path*", "/ancien-blog/:path*"],
};
```

### 11.3 Opérations possibles

| Opération | Code |
| --- | --- |
| Continuer | `NextResponse.next()` |
| Rediriger | `NextResponse.redirect(url)` |
| Réécrire (URL inchangée côté navigateur) | `NextResponse.rewrite(url)` |
| Répondre directement | `NextResponse.json(...)` / `new NextResponse(body, { status })` |
| Modifier les en-têtes de **requête** transmis à l'application | `NextResponse.next({ request: { headers } })` |
| Poser des cookies | `reponse.cookies.set(...)` |
| Travail différé | `event.waitUntil(promesse)` |

```ts
// Passer des en-têtes de requête aux routes
const entetes = new Headers(request.headers);
entetes.set("x-user-id", "42");
return NextResponse.next({ request: { headers: entetes } });
```

```ts
// Réécriture : test A/B
const variante = request.cookies.get("ab")?.value ?? (Math.random() < 0.5 ? "a" : "b");
const reponse = NextResponse.rewrite(new URL(`/accueil-${variante}`, request.url));
reponse.cookies.set("ab", variante);
return reponse;
```

**Cas d'usage :**

- Redirections conditionnelles (langue, pays, ancienne URL).
- **Vérifications d'authentification optimistes** (présence d'un cookie).
- Tests A/B, *feature flags*.
- En-têtes de sécurité (CSP avec *nonce*), CORS simple.
- Détection d'appareil, de robot, géolocalisation (selon la plateforme).
- Réécriture multi-locataire (`client.exemple.com` → `/client`).

### 11.4 Le `matcher`

Sans `matcher`, le proxy s'exécute sur **toutes** les requêtes, y compris les fichiers statiques. Filtrez :

```ts
export const config = {
    matcher: [
        // toutes les routes sauf api, ressources Next et fichiers statiques
        "/((?!api|_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)",
    ],
};
```

**Syntaxe :**

| Motif | Signification |
| --- | --- |
| `/dashboard` | Chemin exact |
| `/dashboard/:path*` | Zéro ou plus de segments |
| `/dashboard/:path+` | Un ou plusieurs segments |
| `/blog/:slug?` | Segment optionnel |
| Expression régulière entre parenthèses | Motifs avancés |

**Conditions avancées :**

```ts
export const config = {
    matcher: [
        {
            source: "/api/:path*",
            has: [{ type: "header", key: "Authorization" }],
            missing: [{ type: "cookie", key: "bypass" }],
        },
    ],
};
```

Les valeurs du `matcher` doivent être des **constantes** analysables au build.

### 11.5 Ordre d'exécution

Pour une requête entrante :

1. `headers` (de `next.config`)
2. `redirects` (de `next.config`)
3. **Proxy** (`proxy.ts`)
4. `rewrites` `beforeFiles`
5. Fichiers du système de fichiers (`public/`, `_next/static`, pages)
6. `rewrites` `afterFiles`
7. Routes dynamiques
8. `rewrites` `fallback`

### 11.6 Limites et bonnes pratiques

- **Léger et rapide** : le Proxy s'exécute sur chaque requête concernée. Évitez les appels réseau lents et les requêtes de base de données.
- **Pas de source de vérité pour l'autorisation.** Utilisez le Proxy pour des **contrôles rapides** (cookie présent, redirection), puis **revérifiez** identité et droits **au plus près des données** (DAL, Server Actions, Route Handlers).
- **Rappel de sécurité.** En mars 2025, la faille **CVE-2025-29927** a montré qu'un en-tête interne spécifique permettait de **contourner** le middleware dans certaines versions ; des correctifs ont été publiés. Conséquence : ne faites **jamais** reposer toute la sécurité sur le proxy, et gardez Next.js à jour.
- **Pas de partage d'état** entre requêtes ; évitez les variables globales.
- Pas d'accès direct à vos composants React ni aux Server Actions.
- Utilisez `config.matcher` pour limiter l'exécution.

### 11.7 Proxy, Route Handlers ou `next.config` ?

| Besoin | Outil |
| --- | --- |
| Redirection simple, statique | `redirects` dans `next.config` |
| Réécriture simple | `rewrites` dans `next.config` |
| Logique conditionnelle sur la requête | **Proxy** |
| Logique métier, accès aux données | Route Handler / Server Action |

### 11.8 Pièges fréquents

- **Matcher trop large** : proxy exécuté sur des images et fichiers `_next`.
- **Boucles de redirection** (`/login` redirige vers `/login`).
- **Authentification uniquement dans le proxy**.
- **Oublier de renommer** `middleware` en `proxy` (Next.js 16).
- **Requêtes lourdes** dans le proxy.
- **Placer `proxy.ts` à la racine** alors que le projet utilise `src/`.

### 11.9 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| Proxy | Code interceptant les requêtes avant le routage (`proxy.ts`) |
| Middleware | Ancien nom du proxy (≤ Next.js 15) |
| `matcher` | Filtre des chemins sur lesquels le proxy s'exécute |
| Réécriture (*rewrite*) | Servir un autre contenu sans changer l'URL |
| Redirection | Changer l'URL du navigateur (307 / 308) |
| Nonce | Valeur aléatoire à usage unique pour une CSP |

### Synthèse du chapitre 11

Le Proxy intercepte **avant** les routes ; il s'exécute sur **Node.js** dans Next.js 16. Il redirige, réécrit, ajoute en-têtes et cookies. Le `matcher` cible les chemins ; le proxy n'est **jamais la seule barrière de sécurité**.

---

## 12. Navigation

**Objectifs d'apprentissage.** Naviguer avec `<Link>`, `useRouter` et `redirect` ; comprendre le **préchargement** (*prefetching*), les navigations douces et dures, la restauration du défilement ; utiliser les préchargements partiels et les **Instant Navigations** (16.3 / 16.4) ; connaître `next/form`, `useLinkStatus`, l'API History et `useOffline`.

### 12.1 Mécanisme de navigation

Next.js remplace le comportement par défaut du navigateur par une **navigation côté client** :

1. **Préchargement** : le contenu des routes visibles (liens `<Link>`) est **préchargé** en arrière-plan.
2. **Navigation douce (*soft*)** : au clic, seuls les **segments modifiés** sont récupérés ; les **layouts partagés sont conservés** (état inchangé) ; pas de rechargement.
3. **Streaming** : les parties lentes arrivent progressivement avec `loading.tsx` / `Suspense`.
4. **Historique** : les boutons précédent / suivant restaurent l'état et la position de défilement.

Une **navigation dure (*hard*)** (rechargement complet) a lieu pour un lien `<a>` classique, une URL tapée, un changement de layout racine, ou quand le préchargement n'est pas applicable.

> **Version 16.** Le routage a été optimisé : **déduplication des layouts** lors du préchargement (un layout partagé n'est téléchargé qu'une fois) et **préchargement incrémental** (seules les parties absentes du cache sont demandées, avec annulation des requêtes de liens qui sortent de la vue). Depuis **16.3**, les petits préchargements sont aussi **regroupés** pour réduire le nombre de requêtes.

### 12.2 Le composant `<Link>`

```tsx
import Link from "next/link";

export default function Menu({ slug }: { slug: string }) {
    return (
        <nav>
            <Link href="/">Accueil</Link>
            <Link href="/blog">Blog</Link>
            <Link href={`/blog/${slug}`}>Article</Link>
            <Link href={{ pathname: "/recherche", query: { q: "next" } }}>Recherche</Link>
        </nav>
    );
}
```

**Props principales :**

| Prop | Rôle |
| --- | --- |
| `href` | Destination (chaîne ou objet `{ pathname, query }`) — **obligatoire** |
| `replace` | Remplace l'entrée d'historique au lieu d'en ajouter une |
| `scroll` | `false` : ne remonte pas en haut de page après navigation |
| `prefetch` | `true` / `false` / (défaut : automatique) |
| `onNavigate` | Callback avant navigation ; `e.preventDefault()` l'annule |
| `className`, `target`, `rel`… | Comme `<a>` |

**Préchargement en détail :**

- Actif **en production** uniquement (désactivé en développement).
- Les liens sont préchargés **quand ils entrent dans le viewport**.
- Modèle classique : routes statiques préchargées en totalité ; routes dynamiques préchargées **jusqu'à la première frontière `loading.tsx`**.
- `prefetch={false}` : désactive (utile sur de très longues listes de liens).

**Liens externes.** Utilisez un `<a>` classique (avec `rel="noopener noreferrer"` pour `target="_blank"`) ; `<Link>` est destiné à la navigation **interne**.

**Ancres :** `<Link href="/doc#installation">Installation</Link>`.

### 12.3 Navigations instantanées et préchargement partiel *(ajout, 16.3–16.4)*

Les Server Components évitent les cascades réseau, mais rendaient certaines navigations **moins réactives** qu'une SPA : chaque clic pouvait attendre le serveur. Next.js 16.3 introduit **Instant Navigations**, un ensemble d'outils (activés avec `cacheComponents: true` et `partialPrefetching: true`) qui rend les navigations aussi vives qu'une SPA.

**Partial Prefetching.** Avant 16.3, on choisissait entre une coque réutilisable (`loading.tsx`) et un préchargement complet (`<Link prefetch={true}>`), trop coûteux. Désormais, Next.js extrait une **coque de chargement réutilisable** de n'importe quelle route (à partir de vos `Suspense` et de vos `"use cache"`), et `<Link prefetch>` peut précharger **autant ou aussi peu** de contenu que vous le décidez.

```tsx
async function Inbox() {
    const messages = await db.query.messages.findMany();
    return (
        <nav>
            {messages.map((m) => (
                <Link prefetch href={`/message/${m.id}`} key={m.id}>
                    {m.sujet}
                </Link>
            ))}
        </nav>
    );
}
```

**Exclure du contenu d'un préchargement : `navigation()` et `prefetch()` (16.4).** Précharger tout le fil d'une conversation pour *chaque* lien visible serait trop coûteux. `await navigation()` exclut un composant du préchargement : il ne sera rendu que lors d'une **vraie navigation** ; `await prefetch()` repousse un contenu de la coque jusqu'à un préchargement explicite.

```tsx
import { navigation } from "next/cache";

async function Fil({ id }: { id: string }) {
    await navigation();                 // exclu du préchargement
    const fil = await getFil(id);
    return fil.map((m) => <div key={m.id}>{m.corps}</div>);
}
```

**Outils associés :**

| Outil | Rôle |
| --- | --- |
| **Instant Insights** | Panneau des DevTools qui signale les navigations **non instantanées** et fournit une consigne de correction pour un agent |
| **Navigation Inspector** | Met en pause un chargement à l'état de coque pour **voir** ce que l'utilisateur verrait (le préchargement est désactivé en développement) |
| **Helper Playwright `instant()`** | Test E2E qui vérifie ce qui doit être visible **sans attendre le réseau** (chapitre 21) |

### 12.4 Navigation impérative : `useRouter`

```tsx
"use client";
import { useRouter } from "next/navigation";

export function Actions() {
    const router = useRouter();
    return (
        <>
            <button onClick={() => router.push("/dashboard")}>Aller</button>
            <button onClick={() => router.replace("/login")}>Remplacer</button>
            <button onClick={() => router.back()}>Retour</button>
            <button onClick={() => router.forward()}>Avancer</button>
            <button onClick={() => router.refresh()}>Rafraîchir</button>
            <button onClick={() => router.prefetch("/blog")}>Précharger</button>
        </>
    );
}
```

| Méthode | Effet |
| --- | --- |
| `push(href, { scroll })` | Navigue et ajoute à l'historique |
| `replace(href, { scroll })` | Navigue sans ajouter à l'historique |
| `back()` / `forward()` | Historique |
| `refresh()` | Re-demande les données du serveur pour la route courante (le cache client est invalidé ; l'état client est conservé) |
| `prefetch(href)` | Précharge manuellement |

Attention : `useRouter` de **`next/navigation`** (App Router) diffère de celui de `next/router` (Pages Router) : il n'expose pas `router.events`, ni `pathname` / `query` (utilisez `usePathname`, `useSearchParams`).

### 12.5 Redirection côté serveur

```tsx
import { redirect } from "next/navigation";

export default async function Page() {
    const session = await getSession();
    if (!session) redirect("/login");   // 307
    return <p>Bienvenue</p>;
}
```

Voir chapitre 4 pour `permanentRedirect`, `notFound`, `forbidden`, `unauthorized`.

### 12.6 Lire l'URL côté client

```tsx
"use client";
import { usePathname, useSearchParams, useParams } from "next/navigation";

export function Debug() {
    const pathname = usePathname();      // "/blog/mon-article"
    const search = useSearchParams();    // lecture seule (URLSearchParams)
    const params = useParams();          // { slug: "mon-article" }
    return <pre>{pathname} {search.get("q")} {JSON.stringify(params)}</pre>;
}
```

`useSearchParams` exige un `<Suspense>` autour du composant pour ne pas rendre toute la page dynamique au build.

**Mettre à jour la query string :**

```tsx
"use client";
import { useRouter, usePathname, useSearchParams } from "next/navigation";

export function Filtre() {
    const router = useRouter();
    const pathname = usePathname();
    const search = useSearchParams();

    function changer(valeur: string) {
        const params = new URLSearchParams(search.toString());
        params.set("tri", valeur);
        router.replace(`${pathname}?${params.toString()}`, { scroll: false });
    }
    return <select onChange={(e) => changer(e.target.value)}><option>date</option><option>prix</option></select>;
}
```

### 12.7 Indicateur de navigation : `useLinkStatus`

```tsx
"use client";
import Link, { useLinkStatus } from "next/link";

function Spinner() {
    const { pending } = useLinkStatus();
    return pending ? <span aria-hidden>…</span> : null;
}

export function LienAvecIndicateur({ href, children }: { href: string; children: React.ReactNode }) {
    return <Link href={href}>{children}<Spinner /></Link>;
}
```

`useLinkStatus` doit être utilisé **dans un enfant** de `<Link>` ; il indique si la navigation de ce lien est en cours (utile quand le préchargement n'a pas eu lieu).

### 12.8 API History native

`window.history.pushState` et `replaceState` sont **intégrés au routeur** : ils mettent à jour `usePathname` et `useSearchParams` **sans rechargement ni requête serveur**. Pratique pour trier ou filtrer instantanément côté client.

```tsx
"use client";
export function Tri() {
    return <button onClick={() => {
        const p = new URLSearchParams(window.location.search);
        p.set("tri", "prix");
        window.history.pushState(null, "", `?${p.toString()}`);
    }}>Trier</button>;
}
```

### 12.9 Défilement (*scroll*)

- Par défaut, après une navigation, Next.js **fait défiler jusqu'en haut** du nouveau segment (ou jusqu'à l'ancre), **sauf** s'il est déjà visible.
- Désactiver : `<Link scroll={false}>` ou `router.push(url, { scroll: false })`.
- Boutons précédent / suivant : restauration de la position.

### 12.10 Résilience réseau : `useOffline` *(expérimental, 16.3)*

Avec `experimental.useOffline: true`, une navigation douce, une récupération de données ou une Server Action n'échoue plus quand le réseau tombe : elle reste **en attente** et est **relancée au retour de la connexion**. Un préchargement partiel ayant déjà mis la coque d'une route en cache, cette coque s'affiche même hors ligne.

```tsx
"use client";
import { useOffline } from "next/offline";

export function BanniereHorsLigne() {
    const horsLigne = useOffline();
    if (!horsLigne) return null;
    return <div role="status">Vous êtes hors ligne. Nouvelle tentative à la reconnexion.</div>;
}
```

### 12.11 Transitions de vue

Avec React 19.3, les **View Transitions** (animations natives entre états) sont **stables** dans React. Next.js les expose via un réglage expérimental (`experimental.viewTransition`) : consultez la documentation de votre version.

### 12.12 Pièges fréquents

- **Utiliser `<a>` pour une navigation interne** : rechargement complet, perte d'état.
- **Appeler `router.push` dans le rendu** (au lieu d'un événement ou d'un effet).
- **Importer `useRouter` depuis `next/router`** dans l'App Router.
- **Utiliser `useSearchParams` sans `Suspense`**.
- **Tester le préchargement en développement** (il est désactivé) : utilisez le Navigation Inspector ou un build de production.
- **`prefetch` sur des centaines de liens** sans `navigation()` ni limites : charge serveur inutile.

### 12.13 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| Préchargement (*prefetch*) | Chargement anticipé d'une route liée |
| Navigation douce / dure | Côté client sans rechargement / rechargement complet |
| Partial Prefetching | Préchargement fin, de la coque jusqu'au contenu choisi |
| Instant Navigations | Ensemble d'outils (16.3) pour des navigations instantanées |
| `useLinkStatus` | Hook indiquant qu'un lien est en cours de navigation |
| `useOffline` | Hook (expérimental) signalant la perte de réseau |
| `router.refresh()` | Rafraîchit les données de la route courante |

### Synthèse du chapitre 12

`<Link>` pour la navigation déclarative ; `useRouter` pour l'impératif ; `redirect` côté serveur. **Préchargement + layouts persistants + streaming** donnent une navigation fluide ; avec Cache Components, le **préchargement partiel**, `navigation()` et Instant Insights permettent d'atteindre des navigations **instantanées**. L'URL reste un excellent conteneur d'état partageable (`searchParams`).

---

# Partie III — Interface et optimisation

## 13. Styles

**Objectifs d'apprentissage.** Utiliser le **CSS global**, les **CSS Modules**, **Tailwind CSS** et **Sass** ; comprendre la compatibilité du **CSS-in-JS** avec les Server Components ; mettre en place un **thème clair / sombre** sans flash ; comprendre l'ordre et le chargement du CSS.

### 13.1 Vue d'ensemble

| Approche | Portée | Quand l'utiliser |
| --- | --- | --- |
| **CSS global** | Toute l'application | Reset, variables, typographie |
| **CSS Modules** | Locale au composant | Styles scopés sans configuration |
| **Tailwind CSS** | Classes utilitaires | Prototypage rapide, design system |
| **Sass / SCSS** | Global ou module | Variables, imbrication, mixins |
| **CSS-in-JS** | Composant | Avec précautions (Client Components) |
| **Styles en ligne** | Élément | Valeurs dynamiques ponctuelles |

### 13.2 CSS global

```css
/* app/globals.css */
:root {
    --couleur-fond: #ffffff;
    --couleur-texte: #111111;
}
body {
    background: var(--couleur-fond);
    color: var(--couleur-texte);
    font-family: system-ui, sans-serif;
}
```

```tsx
// app/layout.tsx
import "./globals.css";
```

**Bonnes pratiques :** importez le CSS global **dans le layout racine** ; limitez-le aux styles réellement globaux (reset, variables, typographie de base).

### 13.3 CSS Modules

Un fichier **`nom.module.css`** génère des **noms de classes uniques** (hachés) : aucune collision.

```css
/* bouton.module.css */
.primaire {
    background: royalblue;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 6px;
}
.primaire:hover { filter: brightness(1.1); }
```

```tsx
import styles from "./bouton.module.css";

export default function Bouton({ children }: { children: React.ReactNode }) {
    return <button className={styles.primaire}>{children}</button>;
}
```

- Utilisable dans les Server **et** Client Components.
- Combinaison de classes : `` `${styles.a} ${styles.b}` `` ou la bibliothèque **`clsx`**.
- Sélecteurs globaux explicites : `:global(.nom)`.
- *(16.4)* En production, Turbopack génère des **noms de classes plus courts** pour alléger CSS et HTML ; le développement garde les noms longs pour faciliter le débogage.

### 13.4 Tailwind CSS

Framework de **classes utilitaires** (`flex`, `p-4`, `text-lg`). `create-next-app` peut le configurer. Principe avec Tailwind v4 :

```bash
npm install tailwindcss @tailwindcss/postcss postcss
```

```js
// postcss.config.mjs
export default { plugins: { "@tailwindcss/postcss": {} } };
```

```css
/* app/globals.css */
@import "tailwindcss";
```

```tsx
export default function Carte() {
    return (
        <article className="rounded-xl border p-4 shadow-sm hover:shadow-md dark:bg-zinc-900">
            <h2 className="text-xl font-semibold">Titre</h2>
        </article>
    );
}
```

**Points clés :**

- **Variantes** : `hover:`, `focus:`, `md:` (responsive), `dark:` (mode sombre).
- **Thème personnalisable** (v4 : directive `@theme` dans le CSS).
- Pour fusionner des classes conditionnelles : `clsx` + `tailwind-merge` (utilitaire `cn()`).
- Les classes doivent apparaître **en entier** dans le code (pas de concaténation dynamique `text-${couleur}-500`) pour être détectées.

### 13.5 Sass

```bash
npm install --save-dev sass
```

Renommez vos fichiers en `.scss` / `.module.scss`. Options dans `next.config.ts` :

```ts
const nextConfig = { sassOptions: { includePaths: ["./styles"] } };
```

Attention : **Turbopack** : l'import avec tilde (`@import "~bibliotheque/..."`) **n'est pas supporté** ; utilisez des chemins standards sans `~`.

### 13.6 CSS-in-JS

- Les bibliothèques **à l'exécution** (styled-components, Emotion) reposent sur le contexte React et les effets : elles ne fonctionnent que dans les **Client Components** et demandent un **registre de styles** pour le rendu serveur.
- **styled-jsx** (livré avec Next.js) ne fonctionne que dans les Client Components.
- Alternatives compatibles RSC : **CSS Modules**, **Tailwind**, et les solutions **« zero-runtime »** (vanilla-extract, Panda CSS, StyleX).
- **Recommandation :** préférez une approche qui génère du **CSS statique** pour tirer parti des Server Components.

### 13.7 Mode sombre (thème)

**Avec CSS et `prefers-color-scheme` :**

```css
:root { --fond: #fff; --texte: #111; }
@media (prefers-color-scheme: dark) {
    :root { --fond: #0b0b0b; --texte: #eee; }
}
```

**Avec bascule manuelle : `next-themes`.**

```tsx
// providers.tsx
"use client";
import { ThemeProvider } from "next-themes";

export function Providers({ children }: { children: React.ReactNode }) {
    return <ThemeProvider attribute="class" defaultTheme="system" enableSystem>{children}</ThemeProvider>;
}
```

```tsx
// app/layout.tsx
<html lang="fr" suppressHydrationWarning>  {/* la classe est ajoutée avant l'hydratation */}
    <body><Providers>{children}</Providers></body>
</html>
```

### 13.8 Ordre et chargement du CSS

- Le CSS est **découpé par route** et chargé uniquement quand nécessaire.
- L'**ordre d'import** détermine la priorité de cascade : gardez un ordre cohérent entre composants (évitez de dépendre de l'ordre pour la correction visuelle).
- Les feuilles externes peuvent être déclarées avec `<link rel="stylesheet" href="..." precedence="default" />` (React 19).

### 13.9 Pièges fréquents

- **Importer du CSS global dans plusieurs composants** : effets de bord imprévisibles.
- **Classes Tailwind construites dynamiquement** (non détectées).
- **Utiliser styled-components dans un Server Component** : erreur.
- **Flash de thème** (FOUC) mal géré lors du mode sombre.
- **Import Sass avec `~`** sous Turbopack.

### 13.10 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| CSS Module | Fichier `.module.css` aux classes locales hachées |
| Classe utilitaire | Classe à effet unique (Tailwind) |
| CSS-in-JS | Styles écrits en JavaScript |
| Zero-runtime | CSS généré à la compilation, sans coût d'exécution |
| FOUC | Flash de contenu non stylé (ou mal thémé) |
| `prefers-color-scheme` | Préférence claire / sombre du système |

### Synthèse du chapitre 13

**CSS Modules** et **Tailwind** conviennent bien aux Server Components. Le CSS-in-JS d'exécution est **réservé aux Client Components**. **Variables CSS + `next-themes`** pour le mode sombre sans flash.

---

## 14. Optimisations

**Objectifs d'apprentissage.** Optimiser **images**, **polices** et **scripts** avec les composants natifs ; réduire la taille des bundles (chargement dynamique, imports ciblés, analyse) ; utiliser le **React Compiler** ; éviter les décalages de mise en page ; mesurer les performances ; appliquer une liste de contrôle de production.

### 14.1 Images : `next/image`

**Problèmes résolus.** Les images sont la **première source de poids** et de **décalages visuels (CLS)**. `next/image` fournit : **redimensionnement** selon l'appareil (`srcset` généré), **formats modernes** (WebP, AVIF), **chargement paresseux** par défaut, **réservation d'espace** (évite le CLS), **optimisation à la demande** (mise en cache sur le serveur).

**Utilisation de base :**

```tsx
import Image from "next/image";
import photo from "./photo.jpg"; // import statique : largeur / hauteur / flou automatiques

export default function Exemple() {
    return (
        <>
            <Image src={photo} alt="Description de la photo" placeholder="blur" />
            <Image src="/logo.png" alt="Logo" width={200} height={60} />
            <Image src="https://images.exemple.com/p.jpg" alt="Distante" width={800} height={600} />
        </>
    );
}
```

**Props importantes :**

| Prop | Rôle |
| --- | --- |
| `src` | Chemin local, import statique ou URL distante |
| `alt` | **Obligatoire** : texte alternatif (accessibilité, SEO) ; `alt=""` pour une image décorative |
| `width`, `height` | **Obligatoires** pour les images non importées, sauf avec `fill` |
| `fill` | L'image remplit son parent (`position: relative` requis sur le parent) |
| `sizes` | Largeur occupée selon le viewport (ex. `(max-width: 768px) 100vw, 50vw`) : **essentiel** avec `fill` ou pour des images responsives |
| `quality` | 1–100 (par défaut 75 ; en Next.js 16, les valeurs autorisées se configurent via `images.qualities`) |
| `priority` / `preload` | Précharge l'image (élément **LCP**, au-dessus de la ligne de flottaison). Attention : Next.js 16 déprécie `priority` au profit de `preload` : vérifiez la documentation de votre version |
| `loading` | `"lazy"` (défaut) ou `"eager"` |
| `placeholder` | `"blur"` (avec `blurDataURL` si image distante) ou `"empty"` |
| `unoptimized` | Désactive l'optimisation pour cette image |
| `loader` | Fonction de génération d'URL (CDN d'images) |
| `onLoad`, `onError` | Événements (Client Components) |

**Image responsive avec `fill` :**

```tsx
<div style={{ position: "relative", aspectRatio: "16 / 9" }}>
    <Image
        src="/banniere.jpg"
        alt="Bannière"
        fill
        sizes="(max-width: 768px) 100vw, 50vw"
        style={{ objectFit: "cover" }}
    />
</div>
```

**Autoriser des images distantes :**

```ts
// next.config.ts
const nextConfig = {
    images: {
        remotePatterns: [
            { protocol: "https", hostname: "images.exemple.com", pathname: "/produits/**" },
        ],
    },
};
```

Toujours **restreindre** les domaines (sécurité, coûts d'optimisation).

**Autres réglages (`images` dans la configuration) :**

| Option | Rôle |
| --- | --- |
| `formats` | `["image/avif", "image/webp"]` |
| `deviceSizes` / `imageSizes` | Largeurs générées |
| `minimumCacheTTL` | Durée de cache minimale des images optimisées (défaut de 4 h en Next.js 16) |
| `localPatterns` | Chemins locaux autorisés (requis en Next.js 16 pour les images locales avec *query string*) |
| `qualities` | Liste des qualités autorisées |
| `loader` / `loaderFile` | Loader personnalisé (Cloudinary, Imgix…) |
| `dangerouslyAllowSVG` | Autorise l'optimisation des SVG (à manier avec prudence) |
| `unoptimized` | Désactive globalement (utile en export statique) |

**Bonnes pratiques :** fournissez **toujours** `alt` et des dimensions (ou `fill` + parent dimensionné) ; marquez l'image **LCP** avec `preload` / `priority` ; utilisez des `sizes` précis ; préférez les SVG pour logos et icônes.

### 14.2 Polices : `next/font`

Avantages : **auto-hébergement** (aucune requête vers Google à l'exécution, meilleure confidentialité), **zéro décalage de mise en page** (métriques de repli ajustées), chargement optimisé.

**Google Fonts :**

```tsx
// app/layout.tsx
import { Inter, Playfair_Display } from "next/font/google";

const inter = Inter({ subsets: ["latin"], display: "swap", variable: "--font-inter" });
const playfair = Playfair_Display({ subsets: ["latin"], weight: ["400", "700"], variable: "--font-playfair" });

export default function RootLayout({ children }: { children: React.ReactNode }) {
    return (
        <html lang="fr" className={`${inter.variable} ${playfair.variable}`}>
            <body className={inter.className}>{children}</body>
        </html>
    );
}
```

- Les **polices variables** n'exigent pas `weight`.
- `subsets` : jeux de caractères à inclure.
- `display` : stratégie d'affichage (`swap`, `optional`…).
- `variable` : expose la police via une **variable CSS** (pratique avec Tailwind).

**Polices locales :**

```tsx
import localFont from "next/font/local";

const maPolice = localFont({
    src: [
        { path: "./fonts/Marque-Regular.woff2", weight: "400", style: "normal" },
        { path: "./fonts/Marque-Bold.woff2", weight: "700", style: "normal" },
    ],
    variable: "--font-marque",
});
```

### 14.3 Scripts : `next/script`

```tsx
import Script from "next/script";

<Script src="https://exemple.com/widget.js" strategy="afterInteractive" />
```

| Stratégie | Moment de chargement |
| --- | --- |
| `beforeInteractive` | Avant l'hydratation (scripts critiques) ; **uniquement dans le layout racine** |
| `afterInteractive` (défaut) | Juste après l'hydratation (analytics, gestionnaires de balises) |
| `lazyOnload` | Pendant les temps d'inactivité (widgets de chat) |
| `worker` | Dans un Web Worker (expérimental, via Partytown) |

- Callbacks (Client Components) : `onLoad`, `onReady`, `onError`.
- Scripts **en ligne** : fournir un `id`.
- Paquet **`@next/third-parties`** : composants optimisés pour Google Analytics, Google Tag Manager, YouTube, Google Maps.

```tsx
import { GoogleAnalytics } from "@next/third-parties/google";
<GoogleAnalytics gaId="G-XXXXXXX" />
```

### 14.4 Réduire le JavaScript envoyé

1. **Server Components par défaut** : la logique reste côté serveur.
2. **Chargement dynamique** (`next/dynamic`, `React.lazy`) pour les composants lourds non critiques :

```tsx
"use client";
import dynamic from "next/dynamic";
const Editeur = dynamic(() => import("./Editeur"), { loading: () => <p>…</p> });
```

3. **Importer à la demande** les bibliothèques lourdes :

```ts
async function exporter() {
    const { default: jsPDF } = await import("jspdf");
    /* ... */
}
```

4. **Imports ciblés** : `import debounce from "lodash/debounce"` plutôt que `import _ from "lodash"` ; l'option `experimental.optimizePackageImports` optimise les paquets à nombreux exports (icônes, etc.).
5. **Analyse** : le **Turbopack Bundle Analyzer** (16.4) met en évidence les plus gros bundles côté client, propose une vue en tableau triable, conserve des instantanés pour **comparer** deux analyses et distingue les modules du **chemin critique**. Une *Skill* d'agent expérimentale (`next-bundle-optimizer`) aide à diagnostiquer et réduire le JavaScript livré. `@next/bundle-analyzer` reste disponible avec Webpack.
6. **Éviter les doublons** de dépendances (`npm ls`, `npm dedupe`).
7. **Paquets externes côté serveur** : `serverExternalPackages` exclut du bundling certains modules natifs.

*(16.4, expérimental)* `turbopackLazyDynamicImports` ne compile en développement les imports dynamiques côté client que lorsque le navigateur les demande ; `turbopackGc` nettoie du cache disque le travail devenu inutile.

### 14.5 React Compiler

Outil de build qui **mémoïse automatiquement** composants et valeurs (équivalent d'un `useMemo` / `useCallback` / `memo` posé partout où c'est utile), sans changer votre code.

```bash
npm install --save-dev babel-plugin-react-compiler
```

```ts
// next.config.ts
const nextConfig = { reactCompiler: true };
```

- Stable depuis Next.js 16 (compilateur 1.0).
- Allonge légèrement les temps de compilation.
- Exclusion locale : directive `"use no memo"`.
- Respectez les **règles de React** (composants purs, pas de mutation d'état).
- **Version Rust (expérimentale, 16.3 / 16.4).** `experimental.turbopackRustReactCompiler: true` exécute le compilateur **directement dans Turbopack**, sans passer par Babel : démarrage du développement nettement plus rapide sur de grosses applications, à condition de ne plus dépendre de Babel pour d'autres transformations.

### 14.6 Précharger et préconnecter

```tsx
import { preload, preconnect } from "react-dom";

preconnect("https://api.exemple.com");   // ouvre tôt la connexion
preload("/hero.jpg", { as: "image" });   // précharge une ressource critique
```

### 14.7 Éviter les décalages de mise en page (CLS)

- Dimensions explicites pour images, vidéos, iframes.
- `next/font` pour éviter les sauts de police.
- Réserver l'espace des contenus chargés tardivement (squelettes de même taille).
- Ne pas insérer de contenu au-dessus du contenu existant après chargement.

### 14.8 Mesurer

- **Lighthouse**, **PageSpeed Insights**, onglet *Performance* de Chrome DevTools.
- `useReportWebVitals` (chapitre 8), **Vercel Speed Insights** ou un outil RUM (*Real User Monitoring*).
- `next build` : taille de chaque route (« First Load JS »).
- Surveillez régulièrement : LCP, INP, CLS, TTFB, taille de bundle.

### 14.9 Liste de contrôle de production

- Images via `next/image`, `sizes` correctes, LCP préchargé.
- Polices via `next/font`.
- Scripts tiers via `next/script` ou `@next/third-parties`.
- Composants lourds chargés dynamiquement.
- Cache configuré (chapitre 7) ; routes dynamiques justifiées.
- `loading.tsx` / `Suspense` aux bons endroits.
- Métadonnées complètes (chapitre 15).
- En-têtes de sécurité (chapitre 18).
- Monitoring et suivi des erreurs.

### 14.10 Pièges fréquents

- **Oublier `sizes`** avec `fill` : l'image la plus grande est téléchargée.
- **Autoriser tous les hôtes distants** (`hostname: "**"`) : risque d'abus.
- **Précharger trop d'images** (`priority` partout) : annule le gain.
- **Charger Google Analytics en `beforeInteractive`** : bloque le rendu.
- **Activer le React Compiler sur du code qui mute son état** : comportements inattendus.

### 14.11 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| LCP | Plus grand élément affiché, souvent une image |
| `sizes` | Indication de largeur d'image selon le viewport |
| `remotePatterns` | Liste blanche des images distantes |
| Chargement dynamique | Import d'un module à la demande |
| *Tree shaking* | Élimination du code inutilisé |
| React Compiler | Compilateur de mémoïsation automatique |
| RUM | Mesure des performances sur de vrais utilisateurs |

### Synthèse du chapitre 14

`next/image`, `next/font` et `next/script` automatisent des optimisations majeures. **Moins de JavaScript** = Server Components + chargement dynamique + imports ciblés. Le **React Compiler** supprime la mémoïsation manuelle. **Mesurez avant et après** chaque optimisation.

---

## 15. Métadonnées et SEO

**Objectifs d'apprentissage.** Définir des métadonnées **statiques et dynamiques** ; comprendre fusion et héritage ; configurer `viewport` ; générer images Open Graph, `sitemap`, `robots`, `manifest` ; ajouter des **données structurées** JSON-LD ; appliquer les bonnes pratiques de SEO technique.

### 15.1 Pourquoi les métadonnées ?

Les **métadonnées** (`<title>`, `<meta name="description">`, Open Graph, Twitter Cards, `<link rel="canonical">`…) décrivent la page aux **moteurs de recherche**, aux **réseaux sociaux** et aux **navigateurs**. L'API Metadata de Next.js les gère de façon **typée** et **côté serveur**.

> Les métadonnées se définissent **uniquement dans les Server Components** (`layout.tsx` et `page.tsx`).

### 15.2 Métadonnées statiques

```tsx
import type { Metadata } from "next";

export const metadata: Metadata = {
    title: "Mon site",
    description: "Description de moins de 160 caractères.",
    keywords: ["next.js", "react"],
    authors: [{ name: "Alice" }],
    openGraph: {
        title: "Mon site",
        description: "Description pour les réseaux sociaux",
        url: "https://exemple.com",
        siteName: "Mon site",
        images: [{ url: "/og.png", width: 1200, height: 630, alt: "Aperçu" }],
        locale: "fr_FR",
        type: "website",
    },
    twitter: { card: "summary_large_image", title: "Mon site", images: ["/og.png"] },
    robots: { index: true, follow: true },
    alternates: { canonical: "https://exemple.com" },
};
```

### 15.3 Métadonnées dynamiques

```tsx
import type { Metadata, ResolvingMetadata } from "next";

export async function generateMetadata(
    { params }: { params: Promise<{ slug: string }> },
    parent: ResolvingMetadata
): Promise<Metadata> {
    const { slug } = await params;
    const post = await getPost(slug);                   // dédupliqué avec la page via React.cache / fetch
    const imagesParentes = (await parent).openGraph?.images ?? [];

    return {
        title: post.titre,
        description: post.extrait,
        openGraph: { images: [post.image, ...imagesParentes] },
    };
}
```

- Peut être `async` ; lit `params` et `searchParams`.
- Les requêtes de données sont **dédupliquées** avec celles de la page (via `fetch` ou `React.cache`).
- Le **streaming des métadonnées** est géré : la page peut commencer à s'envoyer pendant le calcul (les robots reçoivent les métadonnées dans le `<head>` ; pour les navigateurs, elles peuvent être injectées plus tard).

### 15.4 Fusion et héritage

- Les métadonnées se **fusionnent** du layout racine vers la page (la plus profonde l'emporte, **champ par champ au premier niveau**) : un `openGraph` défini dans une page **remplace entièrement** l'objet `openGraph` du layout parent (pas de fusion profonde).
- **Template de titre :**

```tsx
// app/layout.tsx
export const metadata: Metadata = {
    metadataBase: new URL("https://exemple.com"),   // base pour résoudre les URLs relatives
    title: { default: "Mon site", template: "%s | Mon site" },
};

// app/blog/page.tsx
export const metadata: Metadata = { title: "Blog" };   // → "Blog | Mon site"

// forcer un titre exact :
export const metadata: Metadata = { title: { absolute: "Titre exact" } };
```

- **`metadataBase`** : indispensable pour des URLs relatives dans `openGraph.images`, `alternates`, etc.

### 15.5 Viewport et couleur de thème

Depuis Next.js 14, `viewport` est séparé :

```tsx
import type { Viewport } from "next";

export const viewport: Viewport = {
    width: "device-width",
    initialScale: 1,
    themeColor: [
        { media: "(prefers-color-scheme: light)", color: "#ffffff" },
        { media: "(prefers-color-scheme: dark)", color: "#000000" },
    ],
};
// ou : export function generateViewport() { ... }
```

### 15.6 Autres champs utiles

| Champ | Rôle |
| --- | --- |
| `alternates.canonical` | URL canonique (évite le contenu dupliqué) |
| `alternates.languages` | Balises `hreflang` (versions linguistiques) |
| `icons` | Favicons, icônes Apple |
| `manifest` | Lien vers le manifeste PWA |
| `verification` | Vérification Search Console, etc. |
| `appleWebApp`, `formatDetection` | Options mobiles |
| `other` | Balises `<meta>` personnalisées |

### 15.7 Fichiers de métadonnées (conventions)

**Icônes.** `app/favicon.ico` ; `app/icon.(png|svg|jpg)` ; `app/apple-icon.png`. Génération dynamique : `app/icon.tsx` (retourne une `ImageResponse`).

**Images Open Graph / Twitter.** Statiques : `opengraph-image.png`, `twitter-image.png` (+ `.alt.txt`). Dynamiques : `opengraph-image.tsx` (voir 4.10) avec `ImageResponse` de `next/og`. Limites d'`ImageResponse` : sous-ensemble de CSS (flexbox, pas de grid), taille de bundle limitée (~500 Ko), polices à charger explicitement.

**`sitemap.ts` :**

```ts
import type { MetadataRoute } from "next";

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
    const posts = await getPosts();
    return [
        { url: "https://exemple.com", lastModified: new Date(), changeFrequency: "weekly", priority: 1 },
        ...posts.map((p) => ({ url: `https://exemple.com/blog/${p.slug}`, lastModified: p.updatedAt })),
    ];
}
```

Pour plus de 50 000 URLs : `generateSitemaps()` découpe en plusieurs fichiers.

**`robots.ts` :**

```ts
import type { MetadataRoute } from "next";

export default function robots(): MetadataRoute.Robots {
    return {
        rules: [{ userAgent: "*", allow: "/", disallow: ["/api/", "/dashboard/"] }],
        sitemap: "https://exemple.com/sitemap.xml",
    };
}
```

**`manifest.ts` (PWA) :**

```ts
import type { MetadataRoute } from "next";

export default function manifest(): MetadataRoute.Manifest {
    return {
        name: "Mon application",
        short_name: "App",
        start_url: "/",
        display: "standalone",
        background_color: "#ffffff",
        theme_color: "#000000",
        icons: [{ src: "/icon-192.png", sizes: "192x192", type: "image/png" }],
    };
}
```

### 15.8 Données structurées (JSON-LD)

```tsx
export default async function Page({ params }: { params: Promise<{ slug: string }> }) {
    const { slug } = await params;
    const post = await getPost(slug);

    const jsonLd = {
        "@context": "https://schema.org",
        "@type": "Article",
        headline: post.titre,
        datePublished: post.date,
        author: { "@type": "Person", name: post.auteur },
    };

    return (
        <article>
            <script
                type="application/ld+json"
                dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd).replace(/</g, "\\u003c") }}
            />
            {/* contenu */}
        </article>
    );
}
```

Le remplacement de `<` évite l'injection de balises (XSS) si des champs proviennent d'utilisateurs.

### 15.9 Bonnes pratiques de SEO technique

1. **Titres uniques** (≈ 50–60 caractères) et **descriptions** (≈ 150–160) par page.
2. **Structure HTML sémantique** : un seul `<h1>`, hiérarchie `h2` / `h3`, `<main>`, `<nav>`, `<article>`.
3. **URL propres et lisibles**, pas de paramètres inutiles ; **canonical** sur les variantes.
4. **Rendu côté serveur** (ou statique) du contenu important : visible sans JavaScript.
5. **Performances** (Core Web Vitals) : facteur de classement.
6. **Images** : `alt` pertinent, tailles optimisées.
7. **Maillage interne** avec `<Link>` et textes d'ancre explicites.
8. **Sitemap** et **robots** à jour ; `noindex` pour les pages privées (`robots: { index: false }`).
9. **`hreflang`** pour les sites multilingues.
10. **Codes HTTP** corrects : 404 réels (`notFound()`), redirections 301 / 308 pour les URLs migrées.
11. **Données structurées** pertinentes.
12. **Accessibilité** : bénéfique aussi au SEO.

### 15.10 Pièges fréquents

- **Oublier `metadataBase`** : URLs relatives incorrectes dans Open Graph.
- **Croire que `openGraph` fusionne en profondeur** (il remplace).
- **Exporter `metadata` depuis un Client Component** : non supporté.
- **Exporter `metadata` et `generateMetadata` dans le même segment** : conflit.
- **Pages privées indexées** par oubli de `noindex`.

### 15.11 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| Open Graph | Balises décrivant la page pour les aperçus de partage |
| Canonical | URL de référence d'une page |
| `hreflang` | Lien entre versions linguistiques d'une page |
| Sitemap | Liste des URLs offertes aux moteurs de recherche |
| JSON-LD | Données structurées au format JSON liées (schema.org) |
| `noindex` | Consigne de ne pas indexer une page |

### Synthèse du chapitre 15

`metadata` (statique) ou `generateMetadata` (dynamique), **côté serveur uniquement**. Fichiers conventionnels pour icônes, images OG, `sitemap`, `robots`, `manifest`. Le SEO repose autant sur le **contenu et les performances** que sur les balises.

---

# Partie IV — Applications de production

## 16. Authentification

**Objectifs d'apprentissage.** Distinguer **authentification**, **session** et **autorisation** ; implémenter une session sécurisée (cookies, JWT) ; écrire connexion et déconnexion avec des Server Actions ; appliquer l'autorisation **à plusieurs niveaux** (proxy, DAL, composants, actions) ; choisir une bibliothèque ou un service ; connaître les défenses complémentaires (CSRF, XSS, limitation de débit).

### 16.1 Concepts

| Notion | Définition |
| --- | --- |
| **Authentification** (AuthN) | Vérifier **qui** est l'utilisateur (connexion, mot de passe, OAuth, passkey) |
| **Session** | Maintenir l'identité entre les requêtes |
| **Autorisation** (AuthZ) | Vérifier **ce que** l'utilisateur peut faire (rôles, permissions) |

**Méthodes d'authentification :**

- **Identifiant + mot de passe** (stockage haché : **argon2** ou **bcrypt**, jamais en clair).
- **OAuth 2.0 / OpenID Connect** (« Se connecter avec Google / GitHub »).
- **Lien magique / code à usage unique** par e-mail.
- **Passkeys / WebAuthn** (sans mot de passe, résistant à l'hameçonnage).
- **Authentification multifacteur (MFA)** : TOTP, SMS (moins sûr), clé matérielle.
- **SSO d'entreprise** (SAML, OIDC).

**Types de session :**

| Type | Principe | Avantages | Inconvénients |
| --- | --- | --- | --- |
| **Sans état** (*stateless*) | Un **jeton signé / chiffré** (JWT) est stocké dans un cookie | Pas de base de sessions, rapide | Révocation difficile, taille limitée |
| **En base de données** | Un **identifiant de session opaque** dans le cookie ; données en base / Redis | Révocation immédiate, contrôle total | Une lecture par requête |

**Cookie de session sécurisé :**

| Attribut | Rôle |
| --- | --- |
| `HttpOnly` | Inaccessible au JavaScript (limite le vol via XSS) |
| `Secure` | Envoyé en HTTPS uniquement |
| `SameSite=Lax` (ou `Strict`) | Limite l'envoi inter-sites (défense CSRF) |
| `Path=/` | Portée |
| `Expires` / `Max-Age` | Durée de vie |

### 16.2 Session sans état avec `jose`

```bash
npm install jose
openssl rand -base64 32   # générer SESSION_SECRET
```

```ts
// lib/session.ts
import "server-only";
import { SignJWT, jwtVerify } from "jose";
import { cookies } from "next/headers";

const cle = new TextEncoder().encode(process.env.SESSION_SECRET);

type Payload = { userId: string; role: "user" | "admin"; expiresAt: number };

export async function chiffrer(payload: Payload) {
    return new SignJWT(payload)
        .setProtectedHeader({ alg: "HS256" })
        .setIssuedAt()
        .setExpirationTime("7d")
        .sign(cle);
}

export async function dechiffrer(jeton: string | undefined) {
    if (!jeton) return null;
    try {
        const { payload } = await jwtVerify(jeton, cle, { algorithms: ["HS256"] });
        return payload as unknown as Payload;
    } catch {
        return null;
    }
}

export async function creerSession(userId: string, role: "user" | "admin") {
    const expiresAt = Date.now() + 7 * 24 * 60 * 60 * 1000;
    const jeton = await chiffrer({ userId, role, expiresAt });
    (await cookies()).set("session", jeton, {
        httpOnly: true,
        secure: true,
        sameSite: "lax",
        path: "/",
        expires: new Date(expiresAt),
    });
}

export async function supprimerSession() {
    (await cookies()).delete("session");
}
```

> Un JWT **signé** (HS256) est **lisible** par le client (non chiffré). N'y placez aucune donnée sensible ; utilisez un chiffrement (JWE) si nécessaire.

### 16.3 Connexion et déconnexion (Server Actions)

```ts
// app/login/actions.ts
"use server";
import { z } from "zod";
import bcrypt from "bcryptjs";
import { redirect } from "next/navigation";
import { creerSession, supprimerSession } from "@/lib/session";

const Schema = z.object({ email: z.string().email(), motDePasse: z.string().min(8) });

export async function connexion(_prev: unknown, formData: FormData) {
    const parsed = Schema.safeParse({
        email: formData.get("email"),
        motDePasse: formData.get("motDePasse"),
    });
    if (!parsed.success) return { erreur: "Identifiants invalides" };

    const user = await db.user.findUnique({ where: { email: parsed.data.email } });
    const ok = user && (await bcrypt.compare(parsed.data.motDePasse, user.motDePasseHash));
    if (!ok) return { erreur: "Identifiants invalides" };   // message identique : pas d'énumération de comptes

    await creerSession(user.id, user.role);
    redirect("/dashboard");
}

export async function deconnexion() {
    await supprimerSession();
    redirect("/login");
}
```

**Bonnes pratiques de connexion :** message d'erreur **générique**, **limitation de débit**, **délai constant** de comparaison, verrouillage progressif, MFA pour les comptes sensibles.

### 16.4 Autoriser à plusieurs niveaux

**Niveau 1 — Proxy : vérification *optimiste*.**

```ts
// proxy.ts
import { NextResponse, type NextRequest } from "next/server";
import { dechiffrer } from "@/lib/session";

const protegees = ["/dashboard", "/admin"];

export async function proxy(request: NextRequest) {
    const estProtegee = protegees.some((p) => request.nextUrl.pathname.startsWith(p));
    const session = await dechiffrer(request.cookies.get("session")?.value);

    if (estProtegee && !session) return NextResponse.redirect(new URL("/login", request.url));
    return NextResponse.next();
}

export const config = { matcher: ["/((?!api|_next/static|_next/image|.*\\.png$).*)"] };
```

Attention : **Optimiste** = rapide mais **non suffisant** (pas d'accès à la base de données, contournable en cas de faille).

**Niveau 2 — Couche d'accès aux données (DAL) : vérification *sûre*.**

```ts
// lib/dal.ts
import "server-only";
import { cache } from "react";
import { cookies } from "next/headers";
import { redirect } from "next/navigation";
import { dechiffrer } from "./session";

export const verifierSession = cache(async () => {
    const jeton = (await cookies()).get("session")?.value;
    const session = await dechiffrer(jeton);
    if (!session?.userId) redirect("/login");
    return { userId: session.userId, role: session.role };
});

export const getUtilisateur = cache(async () => {
    const { userId } = await verifierSession();
    const user = await db.user.findUnique({ where: { id: userId } });
    return user ? { id: user.id, nom: user.nom, email: user.email } : null; // DTO
});
```

**Niveau 3 — Composants et actions.**

```tsx
// Server Component
import { verifierSession } from "@/lib/dal";
import { forbidden } from "next/navigation";

export default async function Admin() {
    const { role } = await verifierSession();
    if (role !== "admin") forbidden();   // nécessite experimental.authInterrupts
    return <AdminPanel />;
}
```

```ts
// Server Action
"use server";
export async function supprimerUtilisateur(id: string) {
    const { role } = await verifierSession();
    if (role !== "admin") throw new Error("Interdit");
    await db.user.delete({ where: { id } });
}
```

**Piège majeur : les layouts.** Un **layout ne se re-rend pas** à chaque navigation entre pages enfants (rendu partiel). **Ne placez pas votre contrôle d'accès uniquement dans un layout** : une page enfant pourrait être servie sans revérification. Vérifiez l'accès **dans la page** et/ou **au moment de l'accès aux données** (DAL).

**Avec Cache Components.** La session dépend de la requête (`cookies()`) : les composants qui la lisent sont **dynamiques** et doivent se trouver sous `<Suspense>`. Lisez la session **à l'extérieur** d'un périmètre `"use cache"` et passez-en l'identifiant en argument si vous mettez en cache des données propres à l'utilisateur (chapitre 7).

**Autorisation par rôles (RBAC) :**

```ts
const permissions = { user: ["lire"], editeur: ["lire", "ecrire"], admin: ["lire", "ecrire", "supprimer"] } as const;
export function peut(role: keyof typeof permissions, action: string) {
    return (permissions[role] as readonly string[]).includes(action);
}
```

Pour des règles plus fines : **ABAC** (basé sur attributs), **ReBAC** (relations), ou des bibliothèques dédiées (CASL, Oso, OpenFGA).

### 16.5 Bibliothèques et services

| Solution | Type | Notes |
| --- | --- | --- |
| **Auth.js (NextAuth)** | Bibliothèque open source | OAuth, e-mail, *credentials* ; adaptateurs de bases de données |
| **Better Auth** | Bibliothèque open source TypeScript | Plugins MFA, organisations, passkeys |
| **Clerk** | Service hébergé | Interface prête à l'emploi, gestion d'organisations |
| **Auth0**, **WorkOS**, **Kinde**, **Stytch**, **Descope** | Services | SSO / entreprise, MFA |
| **Supabase Auth**, **Firebase Auth** | BaaS | Intégré au backend associé |

**Critères de choix :** coût, hébergement des données, SSO, MFA, passkeys, personnalisation de l'interface, verrouillage fournisseur, maturité et maintenance.

### 16.6 Sécurité complémentaire

- **CSRF** : cookies `SameSite`, contrôle d'origine des Server Actions (intégré).
- **XSS** : échappement par défaut de React ; **ne jamais** utiliser `dangerouslySetInnerHTML` avec du contenu non nettoyé (utilisez DOMPurify) ; **CSP** avec *nonce* (via proxy).
- **Limitation de débit** : connexion, réinitialisation de mot de passe, API publiques.
- **Journalisation** des événements d'authentification.
- **Rotation et expiration** des sessions ; invalidation à la déconnexion et au changement de mot de passe.
- **Secrets** hors du dépôt ; rotation des clés.
- **Mots de passe** : longueur minimale, vérification contre les fuites connues, pas de règles de composition rigides.
- **Réinitialisation de mot de passe** : jetons à usage unique, courte durée, stockés hachés.

### 16.7 Pièges fréquents

- **Vérifier l'authentification seulement dans le proxy ou le layout.**
- **Stocker des données sensibles dans un JWT non chiffré.**
- **Message d'erreur distinguant « email inconnu » et « mauvais mot de passe »** (énumération de comptes).
- **Cookie sans `HttpOnly` / `Secure`.**
- **Renvoyer l'objet utilisateur complet** (avec hash) aux composants.
- **Mettre en cache, dans un cache partagé, des données propres à un utilisateur.**

### 16.8 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| AuthN / AuthZ | Authentification / autorisation |
| Session | Identité maintenue entre les requêtes |
| JWT | Jeton signé contenant des revendications |
| `HttpOnly` / `Secure` / `SameSite` | Attributs de sécurité d'un cookie |
| RBAC / ABAC | Contrôle d'accès par rôles / par attributs |
| Passkey | Identifiant sans mot de passe fondé sur WebAuthn |
| MFA | Authentification multifacteur |
| DAL | Couche d'accès aux données qui impose l'autorisation |

### Synthèse du chapitre 16

**Authentifier → créer une session → autoriser au plus près des données.** Proxy = optimiste ; **DAL = source de vérité**. Cookies `HttpOnly` + `Secure` + `SameSite`. Ne réinventez pas la cryptographie : envisagez une bibliothèque éprouvée.

---

## 17. Internationalisation (i18n)

**Objectifs d'apprentissage.** Distinguer i18n et l10n ; choisir une stratégie de routage par langue ; mettre en place un segment `[lang]` avec des **dictionnaires côté serveur** ; détecter la langue dans le proxy ; accéder à la langue partout avec les *root params* ; gérer le **SEO multilingue** ; formater dates, nombres et pluriels avec `Intl` ; choisir une bibliothèque.

### 17.1 Concepts

| Terme | Définition |
| --- | --- |
| **i18n** (internationalisation) | Préparer l'application à plusieurs langues et régions |
| **l10n** (localisation) | Adapter le contenu à une langue / région précise |
| **Locale** | Code langue-région : `fr`, `fr-FR`, `en-US`, `ar-MA` |
| **RTL** | Écriture de droite à gauche (arabe, hébreu) : `dir="rtl"` |
| **Pluriels / genre / ICU** | Règles linguistiques complexes (`{count, plural, one {# élément} other {# éléments}}`) |

### 17.2 Stratégies de routage

| Stratégie | Exemple | Remarques |
| --- | --- | --- |
| **Sous-chemin** | `/fr/blog`, `/en/blog` | Simple, bon pour le SEO, recommandé |
| **Sous-domaine** | `fr.exemple.com` | Séparation nette |
| **Domaine dédié** | `exemple.fr`, `exemple.com` | Marché par pays |
| **Cookie / en-tête** (sans URL) | `/blog` | Moins bon pour le SEO (une URL, plusieurs contenus) |

### 17.3 Mise en place avec un segment `[lang]`

> **App Router :** pas d'option `i18n` intégrée dans `next.config`. On utilise un **segment dynamique** et le **proxy**.

```text
app/
└── [lang]/
    ├── layout.tsx
    ├── page.tsx
    └── dictionaries/
        ├── fr.json
        └── en.json
```

**Dictionnaires :**

```json
// app/[lang]/dictionaries/fr.json
{ "accueil": { "titre": "Bienvenue", "cta": "Commencer" } }
```

```ts
// app/[lang]/dictionaries.ts
import "server-only";

const dictionnaires = {
    fr: () => import("./dictionaries/fr.json").then((m) => m.default),
    en: () => import("./dictionaries/en.json").then((m) => m.default),
};

export type Locale = keyof typeof dictionnaires;
export const hasLocale = (l: string): l is Locale => l in dictionnaires;
export const getDictionary = async (l: Locale) => dictionnaires[l]();
```

**Layout et page :**

```tsx
// app/[lang]/layout.tsx
import { notFound } from "next/navigation";
import { hasLocale } from "./dictionaries";

export async function generateStaticParams() {
    return [{ lang: "fr" }, { lang: "en" }];
}

export default async function Layout({
    children,
    params,
}: {
    children: React.ReactNode;
    params: Promise<{ lang: string }>;
}) {
    const { lang } = await params;
    if (!hasLocale(lang)) notFound();
    return (
        <html lang={lang} dir={lang === "ar" ? "rtl" : "ltr"}>
            <body>{children}</body>
        </html>
    );
}
```

```tsx
// app/[lang]/page.tsx
import { getDictionary, hasLocale } from "./dictionaries";
import { notFound } from "next/navigation";

export default async function Page({ params }: { params: Promise<{ lang: string }> }) {
    const { lang } = await params;
    if (!hasLocale(lang)) notFound();
    const t = await getDictionary(lang);
    return <h1>{t.accueil.titre}</h1>;
}
```

Les dictionnaires étant chargés **côté serveur**, ils **n'alourdissent pas** le bundle client.

**Accéder à la langue sans prop drilling *(ajout, 16.3).*** Le segment `[lang]` est situé **au-dessus** du layout racine : c'est un *root param*. Il se lit depuis n'importe quel Server Component, y compris dans un périmètre `"use cache"` :

```tsx
// components/Pied.tsx (Server Component)
import { lang } from "next/root-params";
import { getDictionary } from "@/app/[lang]/dictionaries";

export async function Pied() {
    const t = await getDictionary(await lang());
    return <footer>{t.accueil.cta}</footer>;
}
```

Le support des Route Handlers et des Server Actions est annoncé pour une version ultérieure.

### 17.4 Détection de la langue et redirection (Proxy)

```bash
npm install @formatjs/intl-localematcher negotiator
npm install --save-dev @types/negotiator
```

```ts
// proxy.ts
import { NextResponse, type NextRequest } from "next/server";
import { match } from "@formatjs/intl-localematcher";
import Negotiator from "negotiator";

const locales = ["fr", "en"];
const defaut = "fr";

function getLocale(request: NextRequest) {
    const entetes = { "accept-language": request.headers.get("accept-language") ?? "" };
    const langues = new Negotiator({ headers: entetes }).languages();
    return match(langues, locales, defaut);
}

export function proxy(request: NextRequest) {
    const { pathname } = request.nextUrl;
    const aLocale = locales.some((l) => pathname === `/${l}` || pathname.startsWith(`/${l}/`));
    if (aLocale) return;

    const locale = request.cookies.get("NEXT_LOCALE")?.value ?? getLocale(request);
    request.nextUrl.pathname = `/${locale}${pathname}`;
    return NextResponse.redirect(request.nextUrl);
}

export const config = {
    matcher: ["/((?!_next|api|favicon.ico|.*\\..*).*)"],
};
```

**Ordre de détection habituel :** **URL** > **cookie** (choix mémorisé) > **`Accept-Language`** > langue par défaut.

### 17.5 SEO multilingue

```tsx
export async function generateMetadata({ params }: { params: Promise<{ lang: string }> }) {
    const { lang } = await params;
    return {
        alternates: {
            canonical: `https://exemple.com/${lang}`,
            languages: { fr: "https://exemple.com/fr", en: "https://exemple.com/en", "x-default": "https://exemple.com/fr" },
        },
    };
}
```

- Balises **`hreflang`** (via `alternates.languages`) pour relier les versions.
- `<html lang="...">` correct.
- **Sitemap** listant toutes les versions linguistiques.
- Ne **pas** rediriger automatiquement les robots uniquement selon `Accept-Language` sans offrir d'URL stables par langue.

### 17.6 Formatage selon la locale

Utilisez l'API native **`Intl`** :

```ts
new Intl.DateTimeFormat("fr-FR", { dateStyle: "long" }).format(new Date());       // 14 novembre 2026
new Intl.NumberFormat("fr-FR", { style: "currency", currency: "EUR" }).format(1234.5); // 1 234,50 €
new Intl.RelativeTimeFormat("fr", { numeric: "auto" }).format(-1, "day");         // hier
new Intl.PluralRules("fr").select(2);                                             // "other"
new Intl.ListFormat("fr", { type: "conjunction" }).format(["a", "b", "c"]);       // a, b et c
```

**Pièges de formats :** séparateurs décimaux et de milliers, ordre jour-mois-année, **fuseaux horaires** (stocker en UTC, afficher dans le fuseau de l'utilisateur), devise **distincte** de la langue, premier jour de la semaine.

### 17.7 Bibliothèques

| Bibliothèque | Points forts |
| --- | --- |
| **next-intl** | Conçue pour l'App Router : routage, `useTranslations` / `getTranslations`, ICU, formatage, proxy de locale |
| **next-international** | Typage fort des clés |
| **react-i18next / i18next** | Écosystème large, fonctionne côté client et serveur |
| **Paraglide (inlang)** | Messages compilés, bundles réduits |
| **Lingui** | Extraction de messages, ICU |

Avec une bibliothèque, vous gagnez : pluriels ICU, interpolation sûre, typage des clés, outils d'extraction, gestion du routage.

### 17.8 Pages Router *(héritage)*

Le Pages Router propose une configuration **native** :

```ts
// next.config.ts
const nextConfig = {
    i18n: { locales: ["fr", "en"], defaultLocale: "fr", localeDetection: true },
};
```

Next.js gère alors le préfixe de locale et l'objet `locale` (`useRouter().locale`). Cette option **n'existe pas** dans l'App Router.

### 17.9 Pièges fréquents

- **Oublier `await params`** avant de lire `lang`.
- **Charger tous les dictionnaires côté client** : bundle gonflé.
- **Dupliquer le contenu** sans canonical ni `hreflang`.
- **Concaténer des chaînes** au lieu d'utiliser des messages ICU (pluriels, ordre des mots).
- **Oublier `dir="rtl"`** pour les langues RTL.

### 17.10 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| Locale | Identifiant langue-région |
| ICU | Syntaxe standard de pluriels et de sélections |
| RTL / LTR | Sens d'écriture |
| `Intl` | API native de formatage localisé |
| `Accept-Language` | En-tête HTTP des langues préférées du navigateur |
| `hreflang` | Lien entre versions linguistiques |
| *Root param* | Paramètre situé au-dessus du layout racine |

### Synthèse du chapitre 17

**Sous-chemin `[lang]`** + proxy de détection + **dictionnaires côté serveur**. `next/root-params` rend la langue accessible partout. SEO : `hreflang`, canonical, sitemap par langue. `Intl` pour formater dates, nombres et pluriels.

---

## 18. Configuration

**Objectifs d'apprentissage.** Maîtriser `next.config.ts` : redirections, réécritures, en-têtes, images, sortie ; configurer Turbopack et Webpack, les paquets externes et les options expérimentales ; appliquer des **en-têtes de sécurité** et une CSP ; connaître les adaptateurs de build.

### 18.1 Le fichier de configuration

Fichiers acceptés : `next.config.ts`, `next.config.js`, `next.config.mjs`, `next.config.cjs`.

```ts
// next.config.ts
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
    reactStrictMode: true,
    /* options */
};

export default nextConfig;
```

Forme **fonction** (accès à la phase de lancement) :

```ts
import { PHASE_DEVELOPMENT_SERVER } from "next/constants";
import type { NextConfig } from "next";

export default function (phase: string): NextConfig {
    if (phase === PHASE_DEVELOPMENT_SERVER) return { /* développement */ };
    return { /* production */ };
}
```

Le fichier est lu **au démarrage** de Next.js (pas à chaque requête, pas inclus dans le bundle client) : **redémarrez** le serveur après modification.

### 18.2 Options générales

| Option | Rôle |
| --- | --- |
| `reactStrictMode` | Active le Strict Mode de React (double rendu en développement pour détecter les effets de bord) — activé par défaut avec l'App Router |
| `basePath` | Préfixe de chemin si l'application est servie sous un sous-chemin (`/docs`) |
| `assetPrefix` | Préfixe d'URL des ressources statiques (CDN) |
| `trailingSlash` | `true` : `/about/` plutôt que `/about` |
| `output` | `"standalone"` (déploiement minimal Node), `"export"` (statique) |
| `distDir` | Dossier de build (défaut `.next`) |
| `generateBuildId` | Identifiant de build personnalisé (utile en multi-instances) |
| `compress` | Compression gzip des réponses (désactivez si un reverse proxy compresse) |
| `poweredByHeader` | `false` pour retirer l'en-tête `X-Powered-By` |
| `pageExtensions` | Extensions considérées comme pages |
| `typedRoutes` | Routes typées (chapitre 20) |
| `cacheComponents` | Active le modèle Cache Components |
| `partialPrefetching` | Préchargement partiel (modèle Cache Components, 16.3+) |
| `cacheLife` | Profils de durée de cache personnalisés |
| `reactCompiler` | Active le React Compiler |
| `serverExternalPackages` | Paquets non bundlés côté serveur (modules natifs, ORM) |
| `transpilePackages` | Paquets (monorepo) à transpiler |
| `allowedDevOrigins` | Origines autorisées à accéder au serveur de développement |
| `logging` | Journalisation (par exemple des `fetch`) |
| `env` | Variables inlinées au build (préférez les fichiers `.env`) |
| `experimental` | Fonctionnalités non stables |

### 18.3 Redirections

```ts
async redirects() {
    return [
        { source: "/ancien", destination: "/nouveau", permanent: true },            // 308
        { source: "/blog/:slug", destination: "/articles/:slug", permanent: false },// 307
        { source: "/:path((?!public).*)", destination: "/maintenance", permanent: false,
          has: [{ type: "cookie", key: "maintenance", value: "on" }] },
    ];
},
```

- `permanent: true` → **308** ; `false` → **307**.
- Paramètres de chemin (`:slug`, `:path*`), conditions `has` / `missing` (en-tête, cookie, query, host).
- Exécutées **avant** le proxy (chapitre 11).

### 18.4 Réécritures

```ts
async rewrites() {
    return {
        beforeFiles: [{ source: "/blog", destination: "/actualites" }],
        afterFiles: [{ source: "/api/:path*", destination: "https://api.exemple.com/:path*" }],
        fallback: [{ source: "/:path*", destination: "https://ancien-site.exemple.com/:path*" }],
    };
},
```

- **Sans changement d'URL** visible : c'est un **proxy transparent**.
- Usages : masquer un domaine d'API (évite le CORS), migration progressive d'un ancien site (`fallback`), multi-zones.
- Forme simple : retourner directement un tableau (équivalent à `afterFiles`).

### 18.5 En-têtes HTTP

```ts
async headers() {
    return [
        {
            source: "/(.*)",
            headers: [
                { key: "X-Content-Type-Options", value: "nosniff" },
                { key: "X-Frame-Options", value: "DENY" },
                { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
                { key: "Permissions-Policy", value: "camera=(), microphone=(), geolocation=()" },
                { key: "Strict-Transport-Security", value: "max-age=63072000; includeSubDomains; preload" },
            ],
        },
        {
            source: "/static/:path*",
            headers: [{ key: "Cache-Control", value: "public, max-age=31536000, immutable" }],
        },
    ];
},
```

**Politique de sécurité du contenu (CSP) :**

- **Statique** : `Content-Security-Policy` dans `headers()` (ne permet pas de *nonce* par requête).
- **Avec *nonce*** : générer un nonce par requête dans le proxy et l'injecter dans l'en-tête CSP ; cela rend les pages **dynamiques** (le nonce change à chaque requête). Exemple de directive : `script-src 'self' 'nonce-XXXX' 'strict-dynamic'`.
- En développement, `'unsafe-eval'` est parfois nécessaire (Fast Refresh) ; ne le laissez pas en production.
- Testez d'abord en mode **report-only**.

| En-tête | Protège contre |
| --- | --- |
| `Content-Security-Policy` | XSS, injection de ressources |
| `X-Frame-Options` / `frame-ancestors` | Clickjacking |
| `X-Content-Type-Options` | Interprétation MIME erronée |
| `Referrer-Policy` | Fuite d'URL via `Referer` |
| `Strict-Transport-Security` | Rétrogradation HTTP |
| `Permissions-Policy` | Accès non voulu aux API du navigateur |

### 18.6 Sortie de build : `output`

| Valeur | Effet |
| --- | --- |
| (absent) | Build standard ; nécessite `node_modules` à l'exécution |
| `"standalone"` | Produit `.next/standalone` : serveur minimal avec **uniquement** les dépendances utilisées (idéal pour Docker) |
| `"export"` | Site statique dans `out/` (voir chapitre 8) |

### 18.7 Turbopack et Webpack

```ts
const nextConfig: NextConfig = {
    turbopack: {
        resolveAlias: { "ancien-module": "nouveau-module" },
        rules: {
            "*.svg": { loaders: ["@svgr/webpack"], as: "*.js" },
        },
    },
};
```

- Turbopack est le bundler **par défaut** ; l'option `turbopack` est un champ **de premier niveau** (version 16 ; auparavant sous `experimental.turbopack`).
- Pour rester sur **Webpack** : `next build --webpack`, et personnalisation via :

```ts
webpack: (config, { isServer }) => {
    config.module.rules.push({ test: /\.svg$/, use: ["@svgr/webpack"] });
    return config;
},
```

> Si une fonction `webpack` personnalisée existe et que vous lancez Turbopack, le build échoue pour signaler l'incompatibilité : basculez vers `--webpack` ou migrez la configuration.

**Options Turbopack récentes :** cache disque (`turbopackFileSystemCache`, activé par défaut depuis 16.3 pour `next dev` et `next build`), éviction mémoire, et, en expérimental (16.4), `turbopackAdditionalRoots` (dépendances liées hors du dossier du projet, magasins virtuels globaux de pnpm / Bun), `turbopackPluginRuntimeStrategy` (outils exécutés dans des *worker threads*).

### 18.8 Adaptateurs de build

Next.js propose une **API d'adaptateurs de build** (apparue en 16.2) : des plateformes d'hébergement fournissent un adaptateur qui transforme la sortie de build selon leur infrastructure (fonctions, CDN, cache). Elle permet de prendre en charge l'ensemble des fonctionnalités (proxy, cache, ISR) hors de Vercel. Consultez la documentation de votre hébergeur pour savoir quel adaptateur utiliser (chapitre 22).

### 18.9 Autres notions de configuration

- **Alias de chemins** : `tsconfig.json` (`paths`) — Next.js les lit automatiquement.
- **Monorepo** : `transpilePackages`, `outputFileTracingRoot`.
- **Journaux des requêtes `fetch`** : `logging: { fetches: { fullUrl: true } }`.
- **Indicateurs de développement** : `devIndicators`.
- **Origines autorisées en développement** : `allowedDevOrigins: ["*.local"]` si accès depuis un autre appareil.
- **Taille du corps des actions** : `experimental.serverActions.bodySizeLimit`.
- **Vérification de types** : `useTypeScriptCli` permet d'utiliser le TypeScript installé (par exemple TypeScript 7) pour `next build`.
- **Rappels de mise à niveau** : `experimental.agentUpgrade` (`"security"` par défaut, `"latest"`, ou `false`).
- **TypeScript / ESLint au build** : `typescript: { ignoreBuildErrors: true }` (déconseillé).

### 18.10 Pièges fréquents

- **Modifier `next.config` sans redémarrer**.
- **`rewrites` vers une API sans contrôle d'accès**.
- **CSP trop stricte** qui bloque vos propres scripts.
- **Mélanger options Webpack et Turbopack**.
- **Laisser `ignoreBuildErrors` activé** : bugs de typage en production.

### 18.11 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| `redirects` / `rewrites` / `headers` | Règles déclaratives de réseau dans `next.config` |
| CSP | Politique de sécurité du contenu |
| Nonce | Valeur à usage unique autorisant un script en ligne |
| `standalone` | Sortie de build minimale pour conteneur |
| Adaptateur | Module qui adapte la sortie de build à une plateforme |
| `basePath` | Préfixe de chemin de l'application |

### Synthèse du chapitre 18

`next.config.ts` centralise **redirections, réécritures, en-têtes, images, sortie et bundler**. Appliquez systématiquement des **en-têtes de sécurité**. `output: "standalone"` pour Docker ; les **adaptateurs** étendent la prise en charge des plateformes.

---

## 19. Variables d'environnement

**Objectifs d'apprentissage.** Utiliser les fichiers `.env` et comprendre leur **ordre de priorité** ; distinguer variables **serveur** et **publiques** (`NEXT_PUBLIC_`) ; lire des valeurs à l'exécution ; valider et sécuriser la configuration.

### 19.1 Fichiers `.env`

| Fichier | Environnement | Commité ? |
| --- | --- | --- |
| `.env` | Toujours (valeurs par défaut) | Oui (sans secrets) |
| `.env.development` | `next dev` | Oui |
| `.env.production` | `next build` / `next start` | Oui |
| `.env.test` | Tests (`NODE_ENV=test`) | Oui |
| `.env.local` | Local, **prioritaire** (sauf test) | **Non** |
| `.env.development.local`, `.env.production.local`, `.env.test.local` | Surcharge locale par environnement | **Non** |

**Ordre de priorité (du plus au moins prioritaire) :**

1. `process.env` (variables réelles du système ou de la CI)
2. `.env.$(NODE_ENV).local`
3. `.env.local` (non chargé quand `NODE_ENV=test`)
4. `.env.$(NODE_ENV)`
5. `.env`

**Syntaxe et expansion :**

```bash
# .env
DATABASE_URL="postgres://user:pass@localhost:5432/app"
APP_URL=http://localhost:3000
CALLBACK=$APP_URL/auth/callback      # expansion de variable
```

(`\$` pour un dollar littéral.)

### 19.2 Variables côté serveur et côté client

```ts
process.env.DATABASE_URL                 // serveur uniquement
process.env.NEXT_PUBLIC_API_URL          // disponible aussi côté navigateur
```

- **Sans préfixe** : accessible **uniquement côté serveur** (Server Components, Server Actions, Route Handlers, Proxy). Dans le code client, la valeur est **absente**.
- **`NEXT_PUBLIC_`** : **inlinée dans le bundle JavaScript au moment du build** (remplacement textuel). Donc :
    - **visible par tout le monde** : jamais de secret ici ;
    - **figée au build** : changer la variable exige de **reconstruire** (une même image Docker ne peut pas servir plusieurs environnements avec des valeurs `NEXT_PUBLIC_` différentes sans rebuild).
- L'inlining ne fonctionne que pour un accès **statique** : `process.env.NEXT_PUBLIC_X` est remplacé, mais pas `process.env[nom]` ni une déstructuration dynamique.

**Lire des variables à l'*exécution* (*runtime*).** Pour des valeurs qui changent selon l'environnement de déploiement **sans rebuild** :

- Lire `process.env.MA_VARIABLE` dans un **Server Component dynamique** (après `await connection()` si besoin), puis la **passer en prop** au client ;
- ou exposer un Route Handler `/api/config`.

Attention : `serverRuntimeConfig` et `publicRuntimeConfig` ont été **supprimés** (Next.js 16).

### 19.3 Validation de la configuration

Échouez **tôt** si une variable manque ou est invalide :

```ts
// lib/env.ts
import "server-only";
import { z } from "zod";

const schema = z.object({
    DATABASE_URL: z.string().url(),
    SESSION_SECRET: z.string().min(32),
    STRIPE_SECRET_KEY: z.string().startsWith("sk_"),
});

export const env = schema.parse(process.env);
```

Pour un schéma client / serveur unifié : des bibliothèques comme `@t3-oss/env-nextjs`.

### 19.4 Variables hors de Next.js (scripts, tests)

Hors de Next.js (scripts, tests Jest / Vitest), chargez les fichiers `.env` avec `@next/env` :

```ts
import { loadEnvConfig } from "@next/env";
loadEnvConfig(process.cwd());
```

### 19.5 Bonnes pratiques

- **Jamais** de secrets dans le dépôt, ni dans `NEXT_PUBLIC_*`.
- Fournir un **`.env.example`** (sans valeurs sensibles) pour l'équipe.
- Utiliser le **gestionnaire de secrets** de la plateforme (Vercel, AWS Secrets Manager, Vault, Kubernetes Secrets).
- **Rotation** régulière des clés ; clés distinctes par environnement.
- Principe du **moindre privilège** (clé d'API restreinte).
- Valider les variables au démarrage.

### 19.6 Pièges fréquents

- **Préfixer par `NEXT_PUBLIC_` une clé secrète** : exposée publiquement.
- **Changer une variable `NEXT_PUBLIC_` sans rebuild**.
- **Commiter `.env.local`**.
- **Oublier de définir les variables dans l'environnement de production**.
- **Lire `process.env[nom]` dynamiquement côté client** : la valeur n'est pas inlinée.

### 19.7 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| `.env.local` | Fichier local, non commité, prioritaire |
| `NEXT_PUBLIC_` | Préfixe des variables exposées au navigateur |
| Inlining | Remplacement textuel d'une variable au build |
| `process.env` | Objet des variables d'environnement Node.js |
| `.env.example` | Modèle documentant les variables attendues |

### Synthèse du chapitre 19

**Sans préfixe = serveur ; `NEXT_PUBLIC_` = public et figé au build.** Priorité : `process.env` > `.env.*.local` > `.env.local` > `.env.*` > `.env`. **Validez** avec un schéma.

---

## 20. TypeScript

**Objectifs d'apprentissage.** Configurer TypeScript pour Next.js ; utiliser les types fournis (`Metadata`, `NextConfig`, props de pages) et les helpers générés (`PageProps`, `LayoutProps`, `RouteContext`) ; activer les **routes typées** ; typer Server Actions, `params` et données ; reconnaître les erreurs fréquentes.

### 20.1 Mise en place

- Créez un fichier `.ts` / `.tsx` : Next.js propose d'installer TypeScript et génère `tsconfig.json` et `next-env.d.ts`.
- Exigence : TypeScript ≥ 5.1 (version 16). **TypeScript 7** (port natif, jusqu'à dix fois plus rapide) peut vérifier les types pendant `next build` depuis 16.3 : `npm install -D typescript@^7` (voir l'option `useTypeScriptCli`).

```json
// tsconfig.json (extrait typique)
{
    "compilerOptions": {
        "target": "ES2017",
        "lib": ["dom", "dom.iterable", "esnext"],
        "strict": true,
        "noEmit": true,
        "module": "esnext",
        "moduleResolution": "bundler",
        "jsx": "react-jsx",
        "incremental": true,
        "plugins": [{ "name": "next" }],
        "paths": { "@/*": ["./src/*"] }
    },
    "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
    "exclude": ["node_modules"]
}
```

- Le **plugin `next`** de l'éditeur vérifie les directives, les options de segment et les types d'exports de pages / layouts.
- `next-env.d.ts` : ne pas modifier.
- `strict: true` : fortement recommandé.
- La vérification de types s'exécute pendant `next build` : une erreur de type fait échouer le build.

### 20.2 Types fournis par Next.js

```ts
import type { Metadata, Viewport, NextConfig } from "next";
import type { NextRequest, NextResponse } from "next/server";
import type { MetadataRoute } from "next";
```

**Pages, layouts, `params` (asynchrones) :**

```tsx
export default async function Page({
    params,
    searchParams,
}: {
    params: Promise<{ slug: string }>;
    searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
}) {
    const { slug } = await params;
    const sp = await searchParams;
    /* ... */
}
```

**Helpers de types générés : `PageProps`, `LayoutProps`, `RouteContext`.** Disponibles globalement après génération des types (au `next dev`, `next build` ou via **`npx next typegen`**) :

```tsx
export default async function Page(props: PageProps<"/blog/[slug]">) {
    const { slug } = await props.params;           // typé : string
    return <h1>{slug}</h1>;
}

export default function Layout(props: LayoutProps<"/dashboard">) {
    return <section>{props.children}</section>;   // les slots de routes parallèles sont aussi typés
}

export async function GET(_req: Request, ctx: RouteContext<"/api/posts/[id]">) {
    const { id } = await ctx.params;
    return Response.json({ id });
}
```

### 20.3 Routes typées (`typedRoutes`)

```ts
// next.config.ts
const nextConfig = { typedRoutes: true };
```

Next.js génère un type **`Route`** : un `href` inexistant provoque une **erreur de compilation**.

```tsx
import Link from "next/link";
<Link href="/blog/mon-article">OK</Link>
<Link href="/page-inexistante">Erreur de type</Link>
```

Pour un lien dynamique construit à l'exécution : `href={url as Route}` (avec prudence).

### 20.4 Bonnes pratiques de typage

- **Valider à la frontière** (Zod) puis **inférer** les types : `type Entree = z.infer<typeof Schema>`.
- Typer les **DTO** retournés par la couche d'accès aux données.
- Utiliser **`satisfies`** pour vérifier un objet sans élargir son type :

```ts
export const metadata = { title: "Accueil" } satisfies Metadata;
```

- **Props de composants** : interfaces explicites ; `React.ReactNode` pour `children`.
- **Server Actions :**

```ts
type Etat = { ok: true } | { ok: false; erreurs: Record<string, string[]> };
export async function sauver(_prev: Etat | null, fd: FormData): Promise<Etat> { /* ... */ }
```

- **Variables d'environnement** : déclarez-les (schéma Zod ou `declare namespace NodeJS { interface ProcessEnv { ... } }`).
- Éviter `any` ; préférer `unknown` + validation.

### 20.5 Erreurs fréquentes

| Erreur | Cause | Correctif |
| --- | --- | --- |
| « `params` is a Promise » | Types de Next.js 15 / 16 | `Promise<{...}>` + `await` |
| Type de page invalide | Export non autorisé dans `page.tsx` | N'exporter que les éléments permis (`default`, `metadata`, `generateMetadata`, options de segment…) |
| `Cannot find module '@/...'` | Alias non configuré | `paths` dans `tsconfig` |
| Build échoue sur un type | Vérification de types à la compilation | Corriger (éviter `ignoreBuildErrors`) |

### 20.6 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| `strict` | Ensemble de vérifications TypeScript rigoureuses |
| `PageProps` / `LayoutProps` / `RouteContext` | Helpers de types générés pour les routes |
| `typedRoutes` | Vérification statique des liens |
| `satisfies` | Opérateur qui vérifie un type sans l'élargir |
| `z.infer` | Déduction d'un type à partir d'un schéma Zod |
| `next-env.d.ts` | Déclarations de types générées |

### Synthèse du chapitre 20

`strict`, plugin `next`, `next-env.d.ts`. Helpers `PageProps` / `LayoutProps` / `RouteContext` + `typedRoutes`. **Validez puis inférez** ; typez les frontières (actions, handlers, DTO).

---

# Partie V — Qualité et exploitation

## 21. Tests

**Objectifs d'apprentissage.** Choisir le bon type de test pour chaque couche (pyramide de tests) ; configurer **Vitest** ou **Jest** avec React Testing Library ; mocker les modules de Next.js ; tester une Server Action ; écrire des tests **E2E** avec Playwright (dont le helper `instant()`) ; automatiser des contrôles d'accessibilité ; appliquer les bonnes pratiques.

### 21.1 Pyramide de tests

| Niveau | Outils | Cible | Quantité |
| --- | --- | --- | --- |
| **Unitaires** | Jest, Vitest | Fonctions pures, validations, DAL (avec mocks) | Beaucoup |
| **Composants** | React Testing Library | Client Components, comportements d'interface | Moyen |
| **Intégration** | Vitest / Jest + base de test | Server Actions, Route Handlers | Moyen |
| **Bout en bout (E2E)** | Playwright, Cypress | Parcours complets dans un vrai navigateur | Peu, critiques |
| **Visuels / accessibilité** | Storybook, axe | Régressions visuelles, accessibilité | Selon besoin |

> **Important.** Les **Server Components asynchrones** sont mal supportés par les outils de test unitaire (React Testing Library ne sait pas les rendre). **Testez-les en E2E**, ou extrayez leur logique dans des fonctions testables unitairement.

### 21.2 Vitest et React Testing Library

```bash
npm install -D vitest @vitejs/plugin-react jsdom @testing-library/react @testing-library/dom @testing-library/jest-dom vite-tsconfig-paths
```

```ts
// vitest.config.mts
import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react";
import tsconfigPaths from "vite-tsconfig-paths";

export default defineConfig({
    plugins: [tsconfigPaths(), react()],
    test: { environment: "jsdom", setupFiles: ["./vitest.setup.ts"] },
});
```

```ts
// vitest.setup.ts
import "@testing-library/jest-dom/vitest";
```

```tsx
// __tests__/compteur.test.tsx
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { expect, test } from "vitest";
import Compteur from "@/components/Compteur";

test("incrémente au clic", async () => {
    render(<Compteur />);
    await userEvent.click(screen.getByRole("button"));
    expect(screen.getByRole("button")).toHaveTextContent("1");
});
```

Script : `"test": "vitest"`.

### 21.3 Jest

```bash
npm install -D jest jest-environment-jsdom @testing-library/react @testing-library/jest-dom ts-node @types/jest
```

```ts
// jest.config.ts
import nextJest from "next/jest.js";

const createJestConfig = nextJest({ dir: "./" });   // charge next.config et .env, gère CSS / images / SWC

export default createJestConfig({
    testEnvironment: "jsdom",
    setupFilesAfterEnv: ["<rootDir>/jest.setup.ts"],
    moduleNameMapper: { "^@/(.*)$": "<rootDir>/src/$1" },
});
```

### 21.4 Mocker des modules Next.js

```tsx
import { vi } from "vitest";

vi.mock("next/navigation", () => ({
    useRouter: () => ({ push: vi.fn(), replace: vi.fn(), refresh: vi.fn() }),
    usePathname: () => "/",
    useSearchParams: () => new URLSearchParams(),
}));
```

- `next/image` : se comporte comme un `<img>` en test ; mock rarement nécessaire.
- `next/headers` (`cookies`, `headers`) : mockez pour tester la DAL et les actions.
- Réseau : **MSW** (*Mock Service Worker*) pour simuler les API.

### 21.5 Tester une Server Action ou la logique serveur

Une Server Action est une **fonction asynchrone** : testez-la comme telle en mockant ses dépendances.

```ts
import { vi, test, expect } from "vitest";
vi.mock("next/cache", () => ({ revalidatePath: vi.fn(), updateTag: vi.fn() }));
vi.mock("@/lib/dal", () => ({ verifierSession: vi.fn().mockResolvedValue({ userId: "1", role: "admin" }) }));

import { supprimerPost } from "@/app/actions";

test("refuse sans droits", async () => {
    /* configurer le mock role: "user" et vérifier l'erreur */
});
```

### 21.6 Playwright (E2E)

```bash
npm init playwright@latest
```

```ts
// playwright.config.ts
import { defineConfig } from "@playwright/test";

export default defineConfig({
    testDir: "./e2e",
    use: { baseURL: "http://localhost:3000", trace: "on-first-retry" },
    webServer: {
        command: "npm run build && npm run start",   // tester la version de production
        url: "http://localhost:3000",
        reuseExistingServer: !process.env.CI,
    },
});
```

```ts
// e2e/connexion.spec.ts
import { test, expect } from "@playwright/test";

test("un utilisateur peut se connecter", async ({ page }) => {
    await page.goto("/login");
    await page.getByLabel("Email").fill("alice@exemple.com");
    await page.getByLabel("Mot de passe").fill("motdepasse123");
    await page.getByRole("button", { name: "Se connecter" }).click();
    await expect(page).toHaveURL("/dashboard");
    await expect(page.getByRole("heading", { name: "Tableau de bord" })).toBeVisible();
});
```

**Conseils :** sélecteurs **sémantiques** (`getByRole`, `getByLabel`), tests **indépendants**, données de test dédiées, authentification réutilisée via `storageState`, exécution en CI avec rapports et traces.

**Tester les navigations instantanées : `instant()` *(ajout, 16.3).*** Une page qui navigue instantanément aujourd'hui peut devenir lente demain : un composant lisant `cookies()` ajouté à un en-tête partagé, un `<Suspense>` déplacé lors d'un refactoring. Le helper `instant()` du paquet `@next/playwright` vérifie **ce qui doit être visible sans attendre le réseau** :

```ts
import { expect, test } from "@playwright/test";
import { instant } from "@next/playwright";

test("le titre du produit est disponible immédiatement", async ({ page }) => {
    await page.goto("/produits/chaussures");

    await instant(page, async () => {
        await page.click('a[href="/produits/casquettes"]');
        await expect(page.locator("h1")).toContainText("Casquette");
        await expect(page.getByText("Vérification du stock…")).toBeVisible();
    });

    await expect(page.getByText("12 en stock")).toBeVisible();
});
```

Le test échoue dès que l'interface instantanée change, quelle qu'en soit la cause.

### 21.7 Cypress

Alternative à Playwright : tests E2E et **tests de composants** (`cypress run --component`). Le support des Server Components asynchrones est limité côté composant ; privilégiez l'E2E.

### 21.8 Accessibilité automatisée

`@axe-core/playwright` ou `jest-axe` détectent une partie des problèmes (contraste, libellés, rôles). Ils **ne remplacent pas** un audit manuel (clavier, lecteurs d'écran).

### 21.9 Bonnes pratiques

- Tester le **comportement** visible, pas l'implémentation.
- Extraire la logique métier hors des composants pour la tester simplement.
- **Base de données de test** isolée (conteneur, SQLite en mémoire, transactions annulées).
- Intégrer tests, lint, vérification de types et build dans la **CI**.
- Couverture : un indicateur, pas un objectif absolu.

### 21.10 Pièges fréquents

- **Essayer de rendre un Server Component `async` avec RTL**.
- **Tests E2E fragiles** (sélecteurs CSS, attentes fixes `waitForTimeout`).
- **Tester en mode développement** (comportement de cache et de préchargement différent).
- **Dépendre de services externes réels** dans les tests.

### 21.11 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| RTL | *React Testing Library* |
| Mock | Doublure d'un module ou d'une fonction |
| MSW | Outil de simulation d'API au niveau réseau |
| E2E | Test de bout en bout dans un vrai navigateur |
| `storageState` | État d'authentification réutilisé par Playwright |
| `instant()` | Helper Playwright des navigations instantanées |
| axe | Moteur de détection de problèmes d'accessibilité |

### Synthèse du chapitre 21

Unitaires et composants (Vitest / Jest + RTL), plus E2E (Playwright / Cypress). Les **Server Components asynchrones** se testent surtout en E2E. Mockez `next/navigation`, `next/headers` et `next/cache`. `instant()` protège contre les régressions de navigation.

---

## 22. Déploiement

**Objectifs d'apprentissage.** Connaître les modes de déploiement (Node.js, Docker, statique, plateformes) ; construire une **image Docker** optimisée ; gérer cache, variables, reverse proxy et streaming en production ; mettre en place observabilité et CI/CD ; appliquer une liste de contrôle avant mise en production.

### 22.1 Options de déploiement

| Option | Description | Fonctionnalités |
| --- | --- | --- |
| **Serveur Node.js** | `next build` puis `next start` | **Toutes** |
| **Docker** | Conteneur (souvent `output: "standalone"`) | **Toutes** |
| **Export statique** | HTML / CSS / JS dans `out/` | Limitées (pas de serveur) |
| **Vercel** | Plateforme du créateur de Next.js, zéro configuration | Toutes, intégrations natives |
| **Autres plateformes** (AWS Amplify, Netlify, Cloudflare, Google Cloud Run, Azure, Fly.io, Railway, Render…) | Adaptateurs ou Docker | Variable selon la plateforme |

> **Adaptateurs de build.** Next.js propose une **API d'adaptateurs** (16.2) pour que les plateformes tierces prennent en charge l'ensemble des fonctionnalités (proxy, cache, ISR). Consultez la documentation de votre hébergeur pour savoir ce qu'il supporte.

### 22.2 Serveur Node.js

```bash
npm ci
npm run build
npm run start      # écoute sur le port 3000 (variable PORT, option -p)
```

- Exécutez derrière un **reverse proxy** (Nginx, Caddy, Traefik) pour TLS, compression, limites.
- Gestionnaire de processus : **PM2**, systemd, Kubernetes.
- `HOSTNAME=0.0.0.0` pour écouter sur toutes les interfaces en conteneur.

### 22.3 Docker avec `standalone`

```ts
// next.config.ts
const nextConfig = { output: "standalone" };
```

```dockerfile
# syntax=docker/dockerfile:1
FROM node:22-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

FROM node:22-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
# Variables NEXT_PUBLIC_* : à fournir ici (figées au build)
ARG NEXT_PUBLIC_API_URL
ENV NEXT_PUBLIC_API_URL=$NEXT_PUBLIC_API_URL
RUN npm run build

FROM node:22-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
ENV HOSTNAME=0.0.0.0
ENV PORT=3000
RUN addgroup -S nodejs && adduser -S nextjs -G nodejs
COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static
USER nextjs
EXPOSE 3000
CMD ["node", "server.js"]
```

**Points essentiels :**

- Le dossier **`standalone`** ne contient **pas** `public/` ni `.next/static/` : copiez-les (ou servez-les via un CDN).
- Utilisez un utilisateur **non-root**.
- Les variables **secrètes** sont injectées à l'**exécution** (pas dans l'image).
- Le point d'entrée est `server.js`.
- L'optimisation d'images nécessite `sharp` (vérifiez son inclusion pour votre version).
- Le **cache disque de Turbopack** (`.next/cache`) accélère les builds répétés en CI : conservez-le entre deux exécutions (cache de la CI).

### 22.4 Export statique

`output: "export"` + `next build` → dossier `out/` à déposer sur un hébergeur statique (S3 + CloudFront, GitHub Pages, Netlify). Limites : voir chapitre 8. Pensez à `images.unoptimized` ou à un loader externe, et à `trailingSlash` selon l'hébergeur.

### 22.5 Cache, ISR et multi-instances

- Par défaut, le cache est **local à chaque instance** : avec plusieurs conteneurs, les revalidations ne se propagent pas.
- Solution : **gestionnaire de cache partagé** (`cacheHandler` / `cacheHandlers`) sur Redis, S3, etc. ; ou plateforme avec cache distribué.
- Un **CDN** devant l'application met en cache les ressources (`/_next/static/*` : immuables, 1 an) et, selon l'en-tête `Cache-Control`, certaines pages. Depuis 16.3, les ressources immuables peuvent être **réutilisées entre déploiements**.
- Cohérence de **build** : utilisez le même `buildId` (`generateBuildId`) sur toutes les instances d'un même déploiement pour éviter les incohérences d'actions et de ressources (*version skew*).

### 22.6 Streaming derrière un proxy

Le streaming nécessite que le proxy **ne mette pas les réponses en tampon**. Exemple Nginx :

```nginx
location / {
    proxy_pass http://app:3000;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_buffering off;
}
```

(Ou renvoyer l'en-tête `X-Accel-Buffering: no`.)

### 22.7 Variables d'environnement en production

- `NEXT_PUBLIC_*` : à fournir **au build**.
- Secrets : à l'**exécution**, depuis le gestionnaire de secrets de la plateforme.
- Distinguer `NODE_ENV=production` (défini par `next build` / `next start`) des environnements applicatifs (staging, prod) : utilisez une variable dédiée (`APP_ENV`).

### 22.8 Observabilité

- **Journaux** structurés (JSON), niveaux, identifiants de corrélation.
- **Erreurs** : `instrumentation.ts` + `onRequestError` vers Sentry, Datadog, etc.
- **Traces** : OpenTelemetry via `@vercel/otel` ou le SDK OpenTelemetry.
- **Métriques** : latence, taux d'erreur, mémoire, taux de réussite du cache.
- **Santé** : endpoint `/api/health` (vérifie base de données et dépendances) pour les sondes de *liveness* / *readiness*.

### 22.9 Intégration et livraison continues (CI/CD)

Pipeline type : `npm ci` → lint → vérification de types (`tsc --noEmit`) → tests unitaires → `next build` → tests E2E sur le build → image Docker → déploiement (*blue/green* ou *canary*) → vérifications post-déploiement.

### 22.10 Liste de contrôle avant la mise en production

- `next build` sans erreur ; tableau des routes conforme.
- Variables d'environnement définies ; `NEXT_PUBLIC_*` présentes au build.
- En-têtes de sécurité + HTTPS / HSTS.
- Domaines d'images (`remotePatterns`) restreints.
- `robots` / `sitemap` ; pages privées en `noindex`.
- Gestion des erreurs : `error.tsx`, `global-error.tsx`, `not-found.tsx`.
- Monitoring, journalisation, alertes.
- Stratégie de cache et d'invalidation validée (multi-instances).
- Sauvegardes et migrations de base de données automatisées.
- Tests E2E des parcours critiques passés.
- Plan de retour arrière (*rollback*).
- **Version de Next.js à jour** des derniers correctifs de sécurité.

### 22.11 Pièges fréquents

- **Oublier de copier `public/` et `.next/static`** dans l'image standalone.
- **Valeurs `NEXT_PUBLIC_` incorrectes** car absentes au build.
- **Cache non partagé** entre instances.
- **Proxy qui met le streaming en tampon**.
- **Exécuter le conteneur en root**.
- **Déployer sans suivre les correctifs de sécurité** (voir 24.3).

### 22.12 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| `standalone` | Sortie minimale incluant seulement les dépendances nécessaires |
| Reverse proxy | Serveur frontal (TLS, compression, répartition) |
| CDN | Réseau de diffusion de contenu |
| `buildId` | Identifiant d'un build |
| Version skew | Incohérence entre ressources de versions différentes |
| Rollback | Retour à la version précédente |
| Sonde de santé | Requête vérifiant qu'une instance fonctionne |

### Synthèse du chapitre 22

Node et Docker prennent en charge **toutes** les fonctionnalités ; l'export statique est limité. **`standalone` + Docker multi-étapes**. Pensez au **cache partagé**, à un `buildId` cohérent et à un streaming **non bufférisé** ; surveillez erreurs et performances, et gardez Next.js **à jour**.

---

## 23. Pages Router (historique et migration)

**Objectifs d'apprentissage.** Lire et maintenir une application **Pages Router** ; connaître ses fonctions de données (`getStaticProps`, `getServerSideProps`, `getStaticPaths`) et les API Routes ; savoir **dater** un exemple de code ; utiliser la table d'équivalences avec l'App Router ; planifier une **migration progressive**.

### 23.1 Structure

```text
pages/
├── _app.tsx            # composant racine (layout global, providers)
├── _document.tsx       # HTML personnalisé (<Html>, <Head>, <Main>, <NextScript>)
├── index.tsx           # /
├── about.tsx           # /about
├── blog/
│   ├── index.tsx       # /blog
│   └── [slug].tsx      # /blog/:slug
├── 404.tsx             # page 404 personnalisée
├── 500.tsx             # page 500 personnalisée
└── api/
    └── hello.ts        # API Route
```

- Le **chemin du fichier** détermine l'URL ; chaque fichier = une page.
- Tous les composants sont des composants « classiques » (pré-rendus puis hydratés) ; **pas de Server Components**.

### 23.2 `_app.tsx` et `_document.tsx`

```tsx
// pages/_app.tsx
import type { AppProps } from "next/app";
import "../styles/globals.css";

export default function App({ Component, pageProps }: AppProps) {
    return (
        <Layout>
            <Component {...pageProps} />
        </Layout>
    );
}
```

```tsx
// pages/_document.tsx
import { Html, Head, Main, NextScript } from "next/document";

export default function Document() {
    return (
        <Html lang="fr">
            <Head />
            <body>
                <Main />
                <NextScript />
            </body>
        </Html>
    );
}
```

### 23.3 Récupération de données

**`getStaticProps` (SSG / ISR) :**

```tsx
import type { GetStaticProps } from "next";

export const getStaticProps: GetStaticProps = async () => {
    const posts = await fetch("https://api.exemple.com/posts").then((r) => r.json());
    return {
        props: { posts },
        revalidate: 60,        // ISR : régénération au plus toutes les 60 s
        // notFound: true,     // → 404
        // redirect: { destination: "/", permanent: false },
    };
};

export default function Blog({ posts }: { posts: { id: number; title: string }[] }) {
    return <ul>{posts.map((p) => <li key={p.id}>{p.title}</li>)}</ul>;
}
```

**`getStaticPaths` (routes dynamiques statiques) :**

```tsx
import type { GetStaticPaths } from "next";

export const getStaticPaths: GetStaticPaths = async () => ({
    paths: [{ params: { slug: "a" } }, { params: { slug: "b" } }],
    fallback: "blocking",   // false → 404 ; true → page de repli puis données ; "blocking" → SSR bloquant puis cache
});
```

**`getServerSideProps` (SSR) :**

```tsx
import type { GetServerSideProps } from "next";

export const getServerSideProps: GetServerSideProps = async ({ req, res, params, query, locale }) => {
    const session = await getSession(req);
    if (!session) return { redirect: { destination: "/login", permanent: false } };
    return { props: { user: session.user } };
};
```

**Autres :** `getInitialProps` (hérité, déconseillé : désactive l'optimisation statique) ; récupération **côté client** : SWR / TanStack Query.

### 23.4 API Routes

```ts
// pages/api/posts/[id].ts
import type { NextApiRequest, NextApiResponse } from "next";

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
    const { id } = req.query;
    switch (req.method) {
        case "GET":
            return res.status(200).json({ id });
        case "DELETE":
            return res.status(204).end();
        default:
            res.setHeader("Allow", ["GET", "DELETE"]);
            return res.status(405).end(`Méthode ${req.method} non autorisée`);
    }
}
```

### 23.5 Métadonnées, navigation, styles

- **Métadonnées** : `<Head>` de `next/head`.
- **Navigation** : `useRouter` de **`next/router`** (expose `pathname`, `query`, `asPath`, `locale`, `events`).
- **i18n** : option `i18n` native dans `next.config`.
- **Styles** : CSS global **uniquement** dans `_app.tsx`.

```tsx
import Head from "next/head";
<Head><title>Mon titre</title><meta name="description" content="..." /></Head>
```

### 23.6 Dater un exemple de code

| Indice dans le code | Époque probable |
| --- | --- |
| `pages/`, `getServerSideProps`, `getStaticProps`, `next/head` | Pages Router (toutes versions) |
| `app/`, Server Components sans `await params` | App Router, Next.js 13–14 |
| `await params`, `await cookies()` | Next.js 15 et suivants |
| `middleware.ts`, `unstable_cache` | ≤ Next.js 15 |
| `proxy.ts`, `"use cache"`, `updateTag` | Next.js 16 |
| `partialPrefetching`, `ensureStatic`, `navigation()`, `catchError` | Next.js 16.3–16.4 |

### 23.7 Table d'équivalences

| Pages Router | App Router |
| --- | --- |
| `pages/index.tsx` | `app/page.tsx` |
| `_app.tsx` / `_document.tsx` | `app/layout.tsx` (layout racine) |
| `getStaticProps` | Server Component `async` + `"use cache"` |
| `getServerSideProps` | Server Component `async` dynamique (`cookies()`, `connection()`) sous `Suspense` |
| `getStaticPaths` | `generateStaticParams` |
| `revalidate` (dans `getStaticProps`) | `cacheLife` / options de cache |
| `res.revalidate("/path")` | `revalidatePath` / `revalidateTag` |
| `pages/api/*` | `app/api/*/route.ts` |
| `next/head` | `metadata` / `generateMetadata` |
| `next/router` | `next/navigation` (`useRouter`, `usePathname`, `useSearchParams`) |
| `router.query` | `params` (props), `useParams`, `useSearchParams` |
| `router.events` | Pas d'équivalent direct : effet sur `usePathname` / `useSearchParams` |
| `pages/404.tsx` | `app/not-found.tsx` |
| `pages/_error.tsx` | `error.tsx` / `global-error.tsx` |
| `next.config` `i18n` | Segment `[lang]` + proxy |
| `middleware.ts` | `proxy.ts` (identique entre routeurs) |

### 23.8 Stratégie de migration progressive

Les deux routeurs **coexistent** : on peut migrer **route par route**.

1. **Mettre à niveau** Next.js et React ; exécuter les **codemods** officiels (`npx @next/codemod@canary upgrade latest`). Depuis 16.4, `next upgrade --agent` prépare une mise à niveau guidée pour un agent de codage.
2. Créer **`app/layout.tsx`** (balises `<html>` / `<body>`, polices, providers, CSS global).
3. Migrer d'abord les **pages simples** (statiques) ; supprimer la page correspondante de `pages/` (**une URL ne peut exister que dans un routeur**).
4. Remplacer `next/head` par `metadata`.
5. Remplacer les fonctions de données par des **Server Components `async`**.
6. Extraire l'interactivité dans des **Client Components** (`"use client"`).
7. Remplacer `next/router` par `next/navigation`.
8. Migrer les **API Routes** vers des Route Handlers (ou des Server Actions pour les formulaires).
9. Migrer i18n, authentification, middleware.
10. Retirer `pages/` quand tout est migré.

**Points d'attention :** `getServerSideProps` + `req` / `res` → `cookies()` / `headers()` ; les bibliothèques sans `"use client"` ; l'ordre du CSS global ; les tests E2E comme **filet de sécurité** pendant toute la migration.

### 23.9 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| Pages Router | Routeur historique basé sur `pages/` |
| `getStaticProps` | Fonction de données exécutée au build (SSG / ISR) |
| `getServerSideProps` | Fonction de données exécutée à chaque requête (SSR) |
| API Route | Endpoint défini dans `pages/api/` |
| `_app` / `_document` | Composants racine et HTML du Pages Router |
| Codemod | Script qui réécrit automatiquement du code |

### Synthèse du chapitre 23

Pages Router = pages classiques + fonctions de données dédiées + API Routes ; il reste **supporté**. L'App Router apporte RSC, layouts imbriqués, streaming, Server Actions et le modèle Cache Components. La migration est possible **progressivement, route par route**.

---

## 24. Bonnes pratiques

**Objectifs d'apprentissage.** Structurer une application par fonctionnalité ; appliquer les bonnes pratiques de **données et de cache**, de **sécurité**, de **performance**, d'**accessibilité** et d'**observabilité** ; adopter une **stratégie de mise à jour** (y compris les versions de sécurité) ; repérer les anti-patrons ; utiliser une liste de contrôle de revue de code.

### 24.1 Architecture

- **Server Components par défaut** ; frontière `"use client"` la plus basse possible.
- **Colocation** logique ; organisation par fonctionnalité pour les gros projets.
- **Couche d'accès aux données (DAL)** `server-only` : requêtes, autorisations, DTO.
- **Validation** à chaque frontière (formulaires, API, variables d'environnement).
- Fonctions **pures** et testables, séparées de l'interface.
- Éviter les composants « dieux » ; composition plutôt qu'héritage.

### 24.2 Données et cache

- Charger les données **là où elles servent**, en **parallèle** ; éviter les cascades.
- **Streaming** (`Suspense`, `loading.tsx`) pour les zones lentes.
- Mettre en cache **explicitement** (`"use cache"`) avec `cacheLife` et `cacheTag` adaptés.
- Invalider avec `updateTag` / `revalidateTag` après mutation.
- **Ne jamais** mettre en cache des données personnelles dans un cache partagé.
- Dédupliquer avec `React.cache`.
- Garder les pages vitrines **statiques** avec `ensureStatic`.

### 24.3 Sécurité

- **Autorisation côté serveur** dans chaque action, handler et accès aux données.
- **Cookies** `HttpOnly`, `Secure`, `SameSite`.
- **Secrets** hors du code et hors de `NEXT_PUBLIC_*`.
- **En-têtes de sécurité** + CSP ; HTTPS / HSTS.
- Protection contre **XSS** (pas de `dangerouslySetInnerHTML` non nettoyé), **CSRF**, **injections SQL** (requêtes paramétrées / ORM), **SSRF** (valider les URLs côté serveur), **téléversements** (type, taille, stockage isolé).
- **Limitation de débit** sur les endpoints sensibles.
- **Dépendances** : audit régulier (`npm audit`), mises à jour de sécurité de Next.js et de React **rapides**.
- **Programme de versions de sécurité (depuis juillet 2026).** L'équipe Next.js publie des **correctifs de sécurité planifiés** (annoncés à l'avance, par exemple en juillet, août, septembre et novembre 2026), accompagnés si besoin de mises à jour hors calendrier pour des failles critiques en amont. Ces correctifs concernent les lignes de versions maintenues (par exemple 16.x et 15.5). Suivez le blog officiel, installez les versions corrigées de **votre ligne** et utilisez le rappel automatique `experimental.agentUpgrade: "security"` (valeur par défaut) pour être averti pendant `next dev` et `next build`.
- Ne pas exposer d'erreurs détaillées aux utilisateurs.

### 24.4 Performance

- Réduire le JavaScript client ; `next/dynamic` pour le non critique.
- `next/image`, `next/font`, `next/script`.
- Éviter les décalages de mise en page.
- **Navigations instantanées** : `Suspense` bien placés, préchargement partiel, test `instant()`.
- Mesurer : Core Web Vitals, Lighthouse, RUM.
- Surveiller la taille de bundle en CI (Turbopack Bundle Analyzer).

### 24.5 Accessibilité

- HTML sémantique, hiérarchie de titres, `alt`, libellés de formulaire (`<label>`).
- Navigation **au clavier**, focus visible, gestion du focus dans les modales.
- Contraste suffisant, `prefers-reduced-motion`.
- ARIA seulement si le HTML natif ne suffit pas.
- Annoncer les changements de route et les erreurs (`role="alert"`).

### 24.6 Gestion des erreurs et observabilité

- `error.tsx` par segment critique, `global-error.tsx`, `not-found.tsx`, `catchError` pour les widgets isolés.
- Erreurs **attendues** → valeurs retournées ; **inattendues** → exceptions.
- Journalisation structurée ; suivi des erreurs ; alertes.
- Identifiants de requête pour corréler logs, traces, erreurs.

### 24.7 Qualité de code et outillage

- TypeScript `strict`, ESLint, Prettier, hooks Git (Husky, lint-staged).
- Revues de code avec liste de contrôle (24.10).
- Tests : unitaires + E2E sur les parcours critiques.
- Conventions de nommage et de dossiers documentées.
- Mises à jour **régulières** et progressives (ne pas accumuler des versions de retard).
- **Agents de codage** : `next dev` maintient un bloc `AGENTS.md` pointant vers la documentation **de votre version** ; adoptez-le plutôt que de laisser un agent travailler avec une documentation périmée.

### 24.8 Stratégie de mise à jour

```bash
npx @next/codemod@canary upgrade latest             # met à niveau Next.js / React et applique les codemods
npx @next/codemod@canary next-async-request-api .   # (si besoin) accès asynchrones à params / cookies / headers
npx @next/codemod@canary middleware-to-proxy .      # middleware → proxy
npx next@canary upgrade --agent=latest              # (16.4) mise à niveau guidée pour un agent de codage
```

1. Lire les **notes de version** et le **guide de migration**.
2. Mettre à jour sur une **branche**, lancer lint, types, tests, build.
3. Tester en **staging**.
4. Déployer progressivement.

### 24.9 Anti-patrons fréquents

| Anti-patron | Pourquoi c'est un problème | Alternative |
| --- | --- | --- |
| `"use client"` en haut de chaque fichier | Perd les bénéfices des RSC | Frontière client minimale |
| `useEffect` + `fetch` pour tout | Cascades, SEO, JS | Server Component `async` |
| Appeler son propre Route Handler depuis un Server Component | Aller-retour inutile | Fonction partagée |
| Authentification uniquement dans le proxy ou le layout | Contournable | DAL + vérification au plus près des données |
| Tout en `force-dynamic` | Coût, lenteur | Cache explicite + `Suspense` |
| Secrets dans `NEXT_PUBLIC_*` | Fuite | Variables serveur |
| Retourner l'objet utilisateur complet | Fuite de champs sensibles | DTO |
| Ignorer les erreurs de type (`ignoreBuildErrors`) | Bugs en production | Corriger |
| `<img>` partout | Poids, CLS | `next/image` |
| Valider seulement côté client | Contournable | Validation serveur |
| Rester sur une version non corrigée | Failles connues exploitables | Suivre les versions de sécurité |

### 24.10 Liste de contrôle de revue de code

- Composant serveur ou client : choix justifié ?
- Requêtes en parallèle ? Pas de cascade inutile ?
- Données sensibles filtrées (DTO) ?
- Autorisation vérifiée côté serveur ?
- Entrées validées ?
- Cache et invalidations cohérents ?
- Éléments dynamiques sous `Suspense` ?
- États de chargement, d'erreur et de vide gérés ?
- Accessibilité de base respectée ?
- Métadonnées et SEO présents ?
- Tests ajoutés ou mis à jour ?
- Aucune variable d'environnement exposée par erreur ?

### 24.11 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| Anti-patron | Pratique courante mais problématique |
| DAL / DTO | Couche d'accès aux données / objet de transfert minimal |
| `agentUpgrade` | Rappels automatiques de mise à niveau |
| Codemod | Réécriture automatique de code lors d'une migration |
| `AGENTS.md` | Fichier orientant les agents vers la documentation de la version |

### Synthèse du chapitre 24

**Server Components par défaut, DAL pour les données, cache explicite, autorisation au plus près des données, mesure continue.** Gardez Next.js **à jour** (programme de versions de sécurité), relisez le code avec une liste de contrôle et évitez les anti-patrons.

---

## 25. Aide-mémoire et glossaire

**Objectifs d'apprentissage.** Retrouver rapidement les importations, directives, fichiers, segments de route et API de cache ; choisir entre Server Component, Server Action et Route Handler ; disposer d'un glossaire complet ; suivre un parcours d'apprentissage.

### 25.1 Importations fréquentes

```ts
import Link from "next/link";
import Image from "next/image";
import dynamic from "next/dynamic";
import Script from "next/script";
import Form from "next/form";
import { Inter } from "next/font/google";
import localFont from "next/font/local";
import { cookies, headers, draftMode } from "next/headers";
import {
    redirect, permanentRedirect, notFound, forbidden, unauthorized,
    useRouter, usePathname, useSearchParams, useParams,
    useSelectedLayoutSegment, useSelectedLayoutSegments,
} from "next/navigation";
import { NextRequest, NextResponse, after, connection, userAgent } from "next/server";
import {
    revalidatePath, revalidateTag, updateTag, refresh, cacheLife, cacheTag, navigation, prefetch,
} from "next/cache";
import { catchError } from "next/error";
import { useOffline } from "next/offline";
import { lang } from "next/root-params";        // exemple : paramètre racine [lang]
import { ImageResponse } from "next/og";
import type { Metadata, Viewport, NextConfig, MetadataRoute } from "next";
```

### 25.2 Directives

| Directive | Effet |
| --- | --- |
| `"use client"` | Frontière Client Component (module + imports) |
| `"use server"` | Server Actions (fichier ou fonction) |
| `"use cache"` | Met en cache le résultat (Cache Components) |
| `"use cache: private"` / `"use cache: remote"` | Variantes avancées |

### 25.3 Fichiers de l'App Router

| Fichier | Rôle |
| --- | --- |
| `layout` | Interface partagée persistante |
| `page` | Route publique |
| `template` | Layout recréé à chaque navigation |
| `loading` | Suspense / chargement |
| `error` / `global-error` | Gestion d'erreurs (client) |
| `not-found` | 404 |
| `route` | Route Handler |
| `default` | Repli de slot parallèle (obligatoire en 16) |
| `forbidden` / `unauthorized` | 403 / 401 |
| `proxy` (ex-`middleware`) | Interception de requêtes |
| `instrumentation` | Observabilité |
| `icon`, `apple-icon`, `opengraph-image`, `twitter-image` | Images de métadonnées |
| `sitemap`, `robots`, `manifest` | SEO / PWA |

### 25.4 Segments de route

| Dossier | Signification |
| --- | --- |
| `nom` | Segment statique |
| `[x]` | Dynamique |
| `[...x]` | *Catch-all* |
| `[[...x]]` | *Catch-all* optionnel |
| `(x)` | Groupe (sans effet sur l'URL) |
| `@x` | Slot de route parallèle |
| `(.)x`, `(..)x`, `(..)(..)x`, `(...)x` | Route interceptée |
| `_x` | Dossier privé |

### 25.5 API de cache

| API | Rôle | Où |
| --- | --- | --- |
| `"use cache"` | Met en cache | Fonctions, composants, fichiers |
| `cacheLife(profil)` | Durée (`stale` / `revalidate` / `expire`) | Dans un périmètre `"use cache"` |
| `cacheTag(tag)` | Étiquette | Dans un périmètre `"use cache"` |
| `revalidateTag(tag, profil)` | Invalide (SWR) | Actions, Route Handlers |
| `updateTag(tag)` | Invalide **immédiatement** | **Server Actions** seulement |
| `refresh()` | Rafraîchit les données non mises en cache | **Server Actions** seulement |
| `revalidatePath(chemin)` | Invalide une route | Actions, Route Handlers |
| `React.cache(fn)` | Déduplication sur la durée d'une requête | Serveur |
| `navigation()` / `prefetch()` | Exclut du contenu d'un préchargement | Composants sous Cache Components |

### 25.6 Hooks et API (client)

| Hook | Rôle |
| --- | --- |
| `useRouter` | Navigation impérative |
| `usePathname` | Chemin courant |
| `useSearchParams` | Paramètres de requête (lecture) |
| `useParams` | Paramètres dynamiques |
| `useSelectedLayoutSegment(s)` | Segment(s) actif(s) |
| `useLinkStatus` | État de navigation d'un lien |
| `useOffline` | Perte de réseau (expérimental) |
| `useActionState` | État d'une action |
| `useFormStatus` | État d'envoi du formulaire parent |
| `useOptimistic` | Interface optimiste |
| `useTransition` | Transition non bloquante |
| `use` | Lire une promesse ou un contexte |
| `useReportWebVitals` | Mesure des Web Vitals |

### 25.7 Options de `fetch` (modèle classique)

| Option | Effet |
| --- | --- |
| `cache: "force-cache"` | Met en cache |
| `cache: "no-store"` | Pas de cache |
| `next: { revalidate: n }` | Revalidation toutes les `n` s |
| `next: { tags: [...] }` | Étiquettes |
| `signal: AbortSignal.timeout(ms)` | Délai d'expiration |

### 25.8 Options de segment (modèle classique ; incompatibles avec `cacheComponents`)

`dynamic`, `dynamicParams`, `revalidate`, `fetchCache`, `runtime`, `preferredRegion`, `maxDuration`. À l'inverse, `ensureStatic` (16.4) est propre au modèle Cache Components.

### 25.9 Commandes CLI

| Commande | Rôle |
| --- | --- |
| `next dev` | Développement avec Fast Refresh |
| `next build` | Build de production |
| `next start` | Serveur de production |
| `next typegen` | Génère les types de routes |
| `next info` | Diagnostic |
| `next upgrade` | Mise à niveau (`--agent` : guidée pour un agent) |
| `--webpack` | Utiliser Webpack au lieu de Turbopack |
| `-p`, `--port` | Port |

### 25.10 Choisir : Server Action, Route Handler ou Server Component ?

| Besoin | Choix |
| --- | --- |
| Afficher des données | Server Component |
| Mutation depuis votre interface | Server Action |
| API publique / webhook / mobile | Route Handler |
| Interactivité (état, événements) | Client Component |
| Intercepter avant routage | Proxy |

### 25.11 Glossaire (A–Z)

| Terme | Définition |
| --- | --- |
| **App Router** | Routeur basé sur `app/`, avec layouts imbriqués, Server Components, streaming |
| **Cache Components** | Modèle de cache explicite (`"use cache"`), recommandé depuis 16.4, futur défaut de Next.js 17 |
| **Catch-all** | Segment dynamique capturant plusieurs segments d'URL |
| **Client Component** | Composant hydraté dans le navigateur (`"use client"`) |
| **Code splitting** | Découpage du JavaScript en morceaux chargés à la demande |
| **Colocation** | Placer composants, tests et styles à côté de la route sans les exposer |
| **Core Web Vitals** | LCP, INP, CLS : métriques d'expérience utilisateur |
| **CSR** | Rendu côté client |
| **DAL** | Couche centralisant l'accès aux données et l'autorisation |
| **`default.tsx`** | Repli d'un slot de route parallèle |
| **Draft Mode** | Mode d'aperçu de contenu non publié |
| **DTO** | Objet de transfert de données, version minimale d'une entité |
| **Dynamic rendering** | Rendu à chaque requête |
| **`ensureStatic`** | Garde-fou qui fait échouer le build si du contenu dynamique apparaît |
| **Edge runtime** | Environnement d'exécution léger fondé sur les API Web |
| **Fast Refresh** | Rechargement à chaud conservant l'état React |
| **Hydratation** | Activation d'un HTML pré-rendu en y attachant React |
| **Instant Navigations** | Outils (16.3) pour des navigations aussi vives que dans une SPA |
| **Intercepting routes** | Routes chargées dans le contexte courant (modale) avec URL partageable |
| **ISR** | Régénération statique incrémentale |
| **JSON-LD** | Données structurées pour moteurs de recherche |
| **Layout** | Interface partagée persistante entre routes |
| **Matcher** | Filtre des chemins sur lesquels le proxy s'exécute |
| **Middleware** | Ancien nom du proxy (≤ Next.js 15) |
| **Pages Router** | Routeur historique basé sur `pages/` |
| **Parallel routes** | Plusieurs pages rendues simultanément via des slots `@x` |
| **Partial Prefetching** | Préchargement fin, de la coque jusqu'au contenu choisi |
| **PPR** | Pré-rendu partiel (coque statique + trous dynamiques) |
| **Prefetching** | Préchargement des routes liées |
| **Proxy** | Interception des requêtes avant routage (`proxy.ts`) |
| **RSC** | *React Server Components* : composants exécutés uniquement côté serveur |
| **Request Memoization** | Déduplication des requêtes identiques pendant un rendu |
| **Root params** | Paramètres au-dessus du layout racine, lisibles depuis tout Server Component |
| **Route Group** | Dossier `(x)` qui organise sans changer l'URL |
| **Route Handler** | Endpoint HTTP défini dans `route.ts` |
| **SEO** | Optimisation pour les moteurs de recherche |
| **Server Action / Server Function** | Fonction serveur appelable depuis le client |
| **SSG** | Génération statique au build |
| **SSR** | Rendu côté serveur à chaque requête |
| **Stale-while-revalidate** | Servir une valeur périmée pendant sa régénération |
| **Standalone** | Sortie de build minimale pour Docker |
| **Streaming** | Envoi progressif du HTML et du payload RSC |
| **Suspense** | Mécanisme React d'attente avec interface de repli |
| **Tag (cache)** | Étiquette servant à invalider des entrées de cache |
| **Template** | Layout recréé à chaque navigation |
| **Turbopack** | Bundler Rust, par défaut depuis Next.js 16 |
| **TTFB** | Délai avant le premier octet |
| **Typed Routes** | Vérification statique des liens |

### 25.12 Parcours d'apprentissage suggéré

1. **Semaine 1** : chapitres 1 à 4 (bases, routing) → site statique multi-pages.
2. **Semaine 2** : chapitres 5 et 6 → blog avec données chargées côté serveur.
3. **Semaine 3** : chapitres 7 et 8 → cache, ISR, streaming, mesure de performance.
4. **Semaine 4** : chapitres 9 à 12 → formulaires, API, proxy, navigation fluide.
5. **Semaine 5** : chapitres 13 à 17 → design, SEO, authentification, i18n.
6. **Semaine 6** : chapitres 18 à 22 → configuration, tests, déploiement.
7. **Semaine 7** : chapitres 23 et 24 → migration, revue qualité, projet final.

**Projet fil rouge proposé : « Blog + espace membre ».**

- **Pages** : accueil, liste d'articles (pagination, recherche via `searchParams`), article (`generateStaticParams`, métadonnées dynamiques, image OG).
- **Espace membre** : inscription et connexion (session par cookie), tableau de bord protégé (DAL + rôles).
- **Contenu** : CRUD d'articles via Server Actions avec validation Zod, `updateTag` après mutation.
- **Commentaires** : mise à jour optimiste (`useOptimistic`).
- **API publique** : Route Handler `/api/articles` + webhook de revalidation.
- **Qualité** : i18n FR / EN, tests Vitest + Playwright, en-têtes de sécurité, Docker, CI/CD.

### 25.13 Ressources

- **Documentation officielle** : <https://nextjs.org/docs>
- **Tutoriel officiel « Learn Next.js »** : <https://nextjs.org/learn>
- **Blog et notes de version** : <https://nextjs.org/blog>
- **Guides de mise à niveau** : <https://nextjs.org/docs/app/guides/upgrading>
- **Dépôt GitHub** : <https://github.com/vercel/next.js>
- **Documentation React** : <https://react.dev>

> Les API de Next.js évoluent. En cas de divergence entre ce cours et votre version, **la documentation officielle de votre version fait foi.**

### Synthèse du chapitre 25

L'aide-mémoire rassemble **importations, directives, fichiers, segments, API de cache, hooks et commandes**. Choisissez : **Server Component** pour afficher, **Server Action** pour muter depuis votre interface, **Route Handler** pour une API publique, **Client Component** pour l'interactivité, **Proxy** pour intercepter avant le routage.

---

*Fin du cours. Bon développement avec Next.js !*
