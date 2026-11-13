# Laravel — Cours complet

*Cours magistral et module d'apprentissage exhaustif, fondé sur le plan « Cours complet Laravel » — Laravel 13 (mars 2026)*

## Avant de commencer : comment utiliser ce cours

Ce cours développe, chapitre par chapitre, l'intégralité du plan en **37 chapitres**, regroupés en neuf parties : **Fondations** (1 à 4), **Couche HTTP** (5 à 8), **Vues, Blade et validation** (9 et 10), **Base de données** (11 et 12), **Eloquent et relations** (13 et 14), **Authentification, autorisation et architecture interne** (15 à 20), **Événements, tâches asynchrones et services d'infrastructure** (21 à 27), **API, outillage, qualité et sécurité** (28 à 33) et **Frontend, écosystème, production et bonnes pratiques** (34 à 37).

Chaque chapitre suit la même trame : *objectifs d'apprentissage → notions et définitions → exemples de code commentés → pièges fréquents → synthèse*.

**Conventions de lecture**

- **(à jour)** : pratique moderne qui remplace une ancienne. **(héritage)** : ancienne approche, encore fréquente dans les projets existants. **(ajout)** : notion absente des anciens guides ou récente.
- Le code est écrit en **PHP 8.3+** avec typage explicite. Chaque extrait indique en première ligne le **chemin du fichier** concerné (`app/Http/Controllers/…`, `routes/web.php`, etc.). Les commandes de terminal sont dans des blocs `bash`.
- Chaque exemple est volontairement **autonome** : les `use` nécessaires sont indiqués lorsqu'ils ne sont pas évidents. Pour alléger, ils sont parfois omis quand la classe est une facade courante.
- Le cours enseigne le Laravel **actuel** (squelette allégé et configuration dans `bootstrap/app.php`, Form Requests, Resources, Pest, attributs PHP, Reverb, Pulse…) **et** explique l'ancien (`Http/Kernel.php`, `RouteServiceProvider`, Laravel Mix, `$casts` en propriété…) pour que vous sachiez lire du code existant.
- Les exemples ciblent **Laravel 11, 12 et 13**. Quand une fonction dépend d'une version, une *note de version* le précise. Vérifiez toujours la documentation officielle (`laravel.com/docs`) pour votre version exacte.

**Parcours conseillé** : lisez les chapitres 1 à 14 dans l'ordre (ils se construisent les uns sur les autres : cycle de vie, HTTP, vues, base de données, Eloquent), puis choisissez librement dans les parties suivantes selon vos besoins. Les chapitres 17 à 19 (conteneur, providers, facades) éclairent tout le reste et méritent une lecture attentive.

---

# Partie I — Les fondations de Laravel

## 1. Introduction

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : définir un framework et le distinguer d'une bibliothèque ; décrire ce qu'est Laravel et sa philosophie ; expliquer le patron MVC et sa déclinaison dans Laravel ; énumérer les prérequis techniques ; comprendre les principes qui sous-tendent le framework (PSR, injection de dépendances, interface fluide) ; connaître le calendrier de versions et la politique de support ; situer Laravel par rapport à d'autres frameworks ; identifier ses forces et ses limites.

### 1.1 Qu'est-ce qu'un framework ?

Un **framework** est un cadre logiciel qui fournit une **structure**, des **conventions** et des **composants réutilisables** pour développer des applications. Contrairement à une **bibliothèque** (que *votre* code appelle quand il en a besoin), un framework applique le principe d'**inversion de contrôle** : c'est **lui** qui appelle **votre** code (contrôleurs, listeners, jobs, commandes…) au bon moment du cycle d'exécution.

Sans framework, un développeur PHP doit réécrire pour chaque projet : le routage des URL, l'accès à la base de données, la gestion des sessions et des cookies, la protection contre les attaques courantes, l'envoi d'e-mails, la journalisation, les tests… Un framework fournit ces briques de manière **testée, cohérente et documentée**.

|  | **Bibliothèque** | **Framework** |
| --- | --- | --- |
| Qui appelle qui ? | Votre code appelle la bibliothèque | Le framework appelle votre code |
| Structure imposée | Aucune | Dossiers, conventions, cycle de vie |
| Portée | Un problème précis (dates, PDF, HTTP…) | Une application entière |
| Remplacement | Facile | Coûteux (choix structurant) |

### 1.2 Qu'est-ce que Laravel ?

**Laravel** est un framework web **PHP open source** (licence MIT), créé en **2011** par **Taylor Otwell**, conçu pour développer des applications web selon le patron **MVC**. Sa philosophie : rendre le développement **agréable et expressif** (*developer happiness*) sans sacrifier la puissance.

Il est « **tout inclus** » (*batteries included*) : il fournit en standard les briques dont une application professionnelle a besoin.

| Brique | Rôle | Chapitre |
| --- | --- | --- |
| **Routeur** | Associer URL et actions | 5 |
| **Middleware** | Filtrer les requêtes et réponses | 6 |
| **Contrôleurs, requêtes, réponses** | Orchestrer la couche HTTP | 7, 8 |
| **Blade** | Moteur de gabarits | 9 |
| **Validation** | Contrôler les entrées | 10 |
| **Query Builder, migrations, seeders** | Accès et évolution de la base | 11, 12 |
| **Eloquent ORM** | Modèles objets et relations | 13, 14 |
| **Authentification, autorisation** | Identité et droits | 15, 16 |
| **Conteneur, providers, facades, collections** | Architecture interne et utilitaires | 17 à 20 |
| **Événements, queues, scheduler, mails, cache, sessions, fichiers** | Services d'infrastructure | 21 à 27 |
| **API, Artisan, tests, logs, i18n, sécurité** | Outillage et qualité | 28 à 33 |

Principales caractéristiques :

- **Syntaxe expressive** : le code se lit presque comme une phrase (`User::where('active', true)->orderBy('name')->get()`).
- **Batteries incluses** : ORM, authentification, files d'attente, mails, cache, tâches planifiées, tests, WebSockets.
- **Fondé sur Symfony** : Laravel réutilise de nombreux composants Symfony (HttpFoundation, Console, Routing, Process, etc.).
- **Composer d'abord** : toutes les dépendances sont gérées par **Composer**.
- **Convention plutôt que configuration** : des choix par défaut raisonnables évitent la configuration inutile.

### 1.3 Les concepts fondateurs

Avant d'entrer dans le détail, voici le vocabulaire minimal. Chaque terme est approfondi dans un chapitre dédié.

- **Route** : association entre une méthode HTTP + un URI et une **action** (closure ou méthode de contrôleur).
- **Middleware** : couche qui intercepte la requête avant la route (et la réponse après).
- **Contrôleur** : classe qui regroupe la logique de traitement de requêtes liées.
- **Modèle (Eloquent)** : classe PHP liée à une **table** ; une instance représente une **ligne**.
- **Vue / Blade** : gabarit HTML enrichi de directives (`@if`, `@foreach`, `{{ }}`).
- **Migration** : « contrôle de version » du schéma de la base, écrit en PHP.
- **Service container** : conteneur d'**injection de dépendances** qui construit et fournit les objets.
- **Service provider** : classe d'amorçage qui enregistre services, écouteurs, routes, vues…
- **Facade** : interface **statique** d'apparence, qui délègue à un service du conteneur.
- **Contract** : **interface** qui définit un service fondamental du framework.
- **Artisan** : interface en ligne de commande (`php artisan …`).
- **Queue / Job** : mécanisme d'exécution différée en arrière-plan.
- **Event / Listener** : fait métier émis, et réactions à ce fait (patron Observateur).
- **Collection** : enveloppe fluide autour d'un tableau, avec des dizaines de méthodes de transformation.

### 1.4 Le patron MVC

| Couche | Rôle | Dans Laravel |
| --- | --- | --- |
| **Modèle** (*Model*) | Données et logique métier, accès à la base | Classes Eloquent dans `app/Models` |
| **Vue** (*View*) | Présentation (HTML) | Gabarits Blade dans `resources/views` |
| **Contrôleur** (*Controller*) | Reçoit la requête, orchestre modèle et vue | Classes dans `app/Http/Controllers` |

Flux simplifié : *Requête → Route → Contrôleur → Modèle (données) → Vue → Réponse*.

Laravel **ne force pas** MVC strictement : on peut ajouter des couches (**Services**, **Actions**, **Repositories**, **DTO**) pour mieux organiser une application complexe. Le chapitre 37 détaille cette organisation.

### 1.5 Prérequis techniques

- **PHP** : notions de **programmation orientée objet** (classes, interfaces, traits, espaces de noms, closures, typage) et **PHP 8+** (enums, attributs, propriétés promues, `match`, types union, arguments nommés, `readonly`).
- **Composer** : gestionnaire de dépendances PHP (`composer.json`, `composer.lock`, autoload PSR-4).
- **Bases de données relationnelles** : SQL, clés primaires et étrangères, jointures, index.
- **HTTP** : verbes (GET, POST, PUT, PATCH, DELETE), codes de statut (200, 201, 301, 302, 400, 401, 403, 404, 419, 422, 429, 500), en-têtes, cookies.
- **Ligne de commande** (terminal) et **Git**.
- Notions de **HTML, CSS et JavaScript** pour le frontend (chapitres 9 et 34).

### 1.6 Principes clés à comprendre dès le début

1. **PSR** : Laravel suit les standards de PHP-FIG : PSR-4 (autoload), PSR-12 (style de code), PSR-3 (journalisation), PSR-7 (messages HTTP), PSR-11 (conteneur), PSR-16 (cache simple).
2. **Injection de dépendances** : les classes **déclarent** ce dont elles ont besoin, le **conteneur** le leur fournit (chapitre 17).
3. **Interface fluide** (*fluent interface*) : chaînage de méthodes (`->where()->orderBy()->get()`).
4. **Magie contrôlée** : facades, méthodes dynamiques, macros. Très pratique, mais à comprendre pour déboguer.
5. **Convention avant configuration** : nommage prévisible (table `posts` pour le modèle `Post`, clé étrangère `user_id`…).
6. **Versionnage régulier** : une version majeure par an ; lire le guide de mise à jour (*Upgrade Guide*) à chaque montée de version.

### 1.7 Versions, cadence et support *(à jour)*

Laravel publie **une version majeure par an**, au premier trimestre. **Aucune version n'est « LTS » depuis Laravel 6** : toutes ont la même fenêtre de support.

- **Support** : chaque majeure reçoit des **correctifs de bogues pendant 18 mois** et des **correctifs de sécurité pendant 2 ans**.
- **Dépendances de la plateforme** : une nouvelle majeure peut **relever la version minimale de PHP** (Laravel 13 exige PHP 8.3 ; Laravel 14 doit exiger PHP 8.4).
- **Packages officiels** : seule la dernière majeure d'un package officiel reçoit des correctifs de bogues.

| Version | Sortie | PHP | Points marquants |
| --- | --- | --- | --- |
| **10** | févr. 2023 | 8.1–8.3 | Typage natif généralisé dans le squelette |
| **11** | mars 2024 | 8.2–8.4 | **Squelette allégé**, configuration dans `bootstrap/app.php`, SQLite par défaut, **Reverb**, route de santé `/up`, méthode `casts()`, planification à la seconde |
| **12** | févr. 2025 | 8.2–8.5 | Nouveaux **starter kits** (React, Vue, Livewire), mises à jour des dépendances, très peu de ruptures |
| **13** | 17 mars 2026 | 8.3–8.5 | PHP 8.3 minimum, **attributs PHP** étendus pour configurer les composants, **SDK d'IA** officiel, **ressources JSON:API**, recherche sémantique et vectorielle, routage de queues, protection contre la falsification de requête renforcée |

> **Note de version.** Laravel 12 a reçu des correctifs de bogues jusqu'en **août 2026** et reçoit des correctifs de sécurité jusqu'en **février 2027** ; Laravel 13 reçoit des correctifs de bogues jusqu'au **troisième trimestre 2027** et de sécurité jusqu'au **premier trimestre 2028**. Ces dates peuvent évoluer : consultez `laravel.com/docs/releases`.

**Quelle version utiliser ?** La plus récente que votre version de PHP permet. Si vous êtes encore en PHP 8.2, Laravel 12 reste une étape saine le temps de migrer.

### 1.8 Laravel et les autres frameworks

|  | **Laravel** | **Symfony** | **Django** (Python) | **Express** (Node.js) |
| --- | --- | --- | --- | --- |
| Nature | Framework complet, opinionné | Framework + composants découplés | Framework complet | Micro-framework |
| Langage | PHP | PHP | Python | JavaScript / TypeScript |
| Accès aux données | **Eloquent** (Active Record) | Doctrine (Data Mapper) | ORM Django (Active Record) | À choisir (Prisma, Sequelize…) |
| Gabarits | Blade | Twig | Gabarits Django | À choisir |
| Authentification, queues, mails | **Inclus** | Composants / bundles | Partiel + paquets | Paquets tiers |
| Philosophie | Productivité, expressivité | Flexibilité, rigueur | « Batteries incluses » | Minimalisme |

### 1.9 Quand choisir Laravel ? Forces et limites

**Forces**

- **Productivité** : un CRUD complet, avec authentification, se met en place en quelques heures.
- **Écosystème officiel intégré** : Sanctum, Horizon, Telescope, Scout, Cashier, Reverb, Forge, Cloud…
- **Documentation** de très grande qualité, et communauté très active (Laracasts, Laravel News, Laracon).
- **Testabilité** : outils de test, *fakes* et factories intégrés.
- **Adaptable** : du prototype (MVP) au projet d'envergure.

**Limites**

- **Performances brutes** inférieures à des frameworks plus minimalistes (atténuées par le cache, les queues et **Octane**).
- **Courbe d'apprentissage de la « magie »** : facades, méthodes dynamiques, macros demandent de comprendre ce qui se passe derrière.
- **Rythme annuel des majeures** : il faut planifier les mises à jour.
- Une partie du contenu en ligne est **obsolète** (cf. pièges ci-dessous).

### 1.10 Pièges fréquents

- **Suivre un tutoriel ancien** : un `app/Http/Kernel.php`, un `RouteServiceProvider` ou `Laravel Mix` indiquent un projet antérieur à Laravel 11 (ou 9 pour Mix) ; l'équivalent actuel se trouve dans `bootstrap/app.php` et Vite.
- **Confondre Laravel et PHP « à plat »** : ne mélangez pas du PHP procédural (`$_GET`, `mysqli_*`) avec le framework ; utilisez `Request`, `DB`, Eloquent.
- **Croire que la « magie » dispense de comprendre** : une facade n'est pas une méthode statique pure (chapitre 19).

### 1.11 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| Framework | Cadre qui impose structure et cycle de vie et appelle votre code |
| MVC | Modèle–Vue–Contrôleur : séparation données / présentation / orchestration |
| Eloquent | ORM de Laravel, selon le patron Active Record |
| Blade | Moteur de gabarits de Laravel, compilé en PHP |
| Composer | Gestionnaire de dépendances et d'autoload de PHP |
| Artisan | Interface en ligne de commande de Laravel |
| Service container | Conteneur d'injection de dépendances |
| Facade | Façade statique vers un service du conteneur |
| Starter kit | Squelette d'application avec authentification et interface prêts |
| PSR | Recommandation standard de PHP-FIG |

### Synthèse du chapitre 1

Laravel est un **framework PHP complet, expressif et opinionné**, bâti sur des composants Symfony et orchestré par un **conteneur de services**. Il suit **MVC** sans l'imposer strictement. Sa force est la **productivité** et un **écosystème officiel cohérent** ; ses points d'attention sont la « magie » à comprendre et la **cadence annuelle** de versions (Laravel 13, PHP 8.3 minimum).

---

## 2. Installation et configuration

**Objectifs d'apprentissage.** Préparer un environnement de développement (PHP, Composer, Node.js, base de données) ; choisir entre Herd, Sail et d'autres piles ; créer un projet et choisir un starter kit ; lancer l'application ; maîtriser le fichier `.env` et le dossier `config/` ; détecter l'environnement ; configurer une base de données ; connaître le mode maintenance ; utiliser Sail et les outils de confort ; diagnostiquer les problèmes d'installation.

### 2.1 Prérequis d'environnement

- **PHP** (version compatible avec votre Laravel) avec les extensions : `ctype`, `curl`, `dom`, `fileinfo`, `filter`, `hash`, `json`, `mbstring`, `openssl`, `pcre`, `pdo`, `session`, `tokenizer`, `xml`.
- **Composer**.
- **Node.js et npm** (compilation des assets avec **Vite**).
- Un **SGBD** : **SQLite** (par défaut dans les versions récentes), MySQL/MariaDB, PostgreSQL ou SQL Server.

**Options d'environnement**

| Option | Description |
| --- | --- |
| **Laravel Herd** | Environnement natif PHP pour macOS et Windows, très simple ; sites en `.test`, services intégrés |
| **Laravel Sail** | Environnement **Docker** officiel (PHP, MySQL, Redis, Mailpit…) |
| **Laragon / XAMPP / MAMP** | Piles locales classiques |
| **Docker « maison »** | Configuration personnalisée, proche de la production |
| **Valet / Homestead** *(héritage)* | Environnements historiques (macOS léger / machine virtuelle) |

### 2.2 Créer un projet

```bash
# Via Composer
composer create-project laravel/laravel mon-projet

# Via l'installateur Laravel (global)
composer global require laravel/installer
laravel new mon-projet
```

L'installateur interactif propose de choisir un **starter kit** (aucun, React, Vue, Livewire), un **framework de test** (Pest ou PHPUnit), la **base de données** et l'**initialisation Git**. Le choix du starter kit est détaillé aux chapitres 15 et 34.

### 2.3 Lancer l'application

```bash
cd mon-projet
php artisan serve              # serveur de développement : http://127.0.0.1:8000
npm install && npm run dev     # assets avec Vite (rechargement à chaud)
composer run dev               # raccourci des squelettes récents : serveur, queue, logs et Vite en parallèle
```

`php artisan serve` est un serveur **de développement** : ne l'utilisez jamais en production (chapitre 36).

### 2.4 Le fichier `.env`

Le fichier `.env` contient les **variables propres à l'environnement** (local, test, production). Il n'est **jamais versionné** (il figure dans `.gitignore`). Un fichier **`.env.example`** sert de modèle et, lui, est versionné.

| Variable | Rôle |
| --- | --- |
| `APP_NAME` | Nom de l'application |
| `APP_ENV` | Environnement : `local`, `staging`, `production`, `testing` |
| `APP_KEY` | Clé de chiffrement (générée par `php artisan key:generate`) |
| `APP_DEBUG` | Affiche les erreurs détaillées. **Toujours `false` en production** |
| `APP_URL` | URL de base de l'application |
| `APP_LOCALE`, `APP_FALLBACK_LOCALE` | Langue courante et de repli |
| `DB_*` | Connexion à la base de données |
| `CACHE_STORE`, `SESSION_DRIVER`, `QUEUE_CONNECTION` | Pilotes des sous-systèmes |
| `MAIL_*` | Configuration d'e-mail |
| `LOG_CHANNEL`, `LOG_LEVEL` | Journalisation |

```env
# .env
APP_NAME="Mon Application"      # les valeurs contenant des espaces sont entre guillemets
APP_ENV=local
APP_DEBUG=true
DB_CONNECTION=sqlite
```

> **Règle d'or.** On n'appelle `env()` **que** dans les fichiers de `config/`. Ailleurs, on utilise `config()`. Après `php artisan config:cache`, `env()` appelé hors de `config/` retourne **`null`**.

### 2.5 Le dossier `config/`

Chaque fichier retourne un **tableau** de configuration. Fichiers principaux :

- `app.php` : nom, environnement, fuseau horaire, locale, clé.
- `auth.php` : *guards*, *providers*, réinitialisation de mot de passe.
- `cache.php`, `database.php`, `filesystems.php`, `logging.php`, `mail.php`, `queue.php`, `session.php`.
- `services.php` : identifiants des services tiers (clés d'API).

```php
config('app.name');                          // lecture avec notation pointée
config('app.timezone', 'UTC');               // avec valeur par défaut
config(['app.timezone' => 'Indian/Antananarivo']);   // modification à l'exécution (non persistante)
```

```php
// config/services.php
return [
    'stripe' => ['key' => env('STRIPE_KEY'), 'secret' => env('STRIPE_SECRET')],   // env() autorisé ici
];
```

### 2.6 Détection de l'environnement

```php
app()->environment();                    // 'local'
app()->environment('local', 'staging');  // bool : l'un de ces environnements ?
app()->isProduction();
app()->isLocal();
```

### 2.7 Première connexion à une base de données

**SQLite** (le plus simple) :

```env
DB_CONNECTION=sqlite
```

Le fichier `database/database.sqlite` est créé automatiquement.

**MySQL** :

```env
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=ma_base
DB_USERNAME=root
DB_PASSWORD=secret
```

Puis exécutez `php artisan migrate` pour créer les tables initiales (chapitre 12).

### 2.8 Mode maintenance et optimisation

```bash
php artisan down      # mode maintenance : réponse 503 pour les visiteurs
php artisan down --secret="mot-secret"   # contournement par URL secrète
php artisan up
php artisan optimize  # met en cache config, routes, vues et événements (production)
```

### 2.9 Laravel Sail

```bash
./vendor/bin/sail up -d
./vendor/bin/sail artisan migrate
./vendor/bin/sail composer require vendor/package
./vendor/bin/sail test
```

Astuce : alias de confort `alias sail='[ -f sail ] && sh sail || sh vendor/bin/sail'`.

### 2.10 Outils de confort

- **IDE Helper** (`barryvdh/laravel-ide-helper`) : autocomplétion des facades et des modèles.
- **Laravel Pint** : formatage automatique du code (`./vendor/bin/pint`).
- **Larastan / PHPStan** : analyse statique.
- **Debugbar** et **Telescope** : débogage.
- **Tinker** : REPL (`php artisan tinker`, chapitre 29).
- **`php artisan about`** : résumé de la configuration (versions, pilotes, environnement).

### 2.11 Dépannage courant

| Symptôme | Cause probable et remède |
| --- | --- |
| « No application encryption key has been specified » | `APP_KEY` vide : `php artisan key:generate` |
| Erreur 500 sans détail | `APP_DEBUG=false` : consulter `storage/logs/laravel.log` |
| « Permission denied » sur `storage/` | Rendre `storage/` et `bootstrap/cache/` inscriptibles par l'utilisateur du serveur web |
| « could not find driver » | Extension PDO du SGBD manquante (`pdo_mysql`, `pdo_sqlite`…) |
| Modification de `.env` sans effet | Configuration en cache : `php artisan config:clear` |
| Assets non chargés | `npm run dev` non lancé, ou `npm run build` manquant en production |

### 2.12 Pièges fréquents

- **Versionner `.env`** : il contient des secrets ; seul `.env.example` doit l'être.
- **`env()` en dehors de `config/`** : fonctionne en local, casse en production après `config:cache`.
- **`APP_DEBUG=true` en production** : fuite de configuration et de traces d'erreur.
- **Oublier `key:generate`** après un `git clone` : sessions et chiffrement ne fonctionnent pas.

### Synthèse du chapitre 2

Un projet Laravel se crée avec `composer create-project` ou `laravel new`, s'exécute avec `php artisan serve` (ou Herd/Sail) et se configure par **`.env`** (valeurs d'environnement) lu uniquement dans **`config/`** (lu partout ailleurs par `config()`). `APP_DEBUG=false` en production, `optimize` à chaque déploiement.

---

## 3. Structure du projet

**Objectifs d'apprentissage.** Connaître le rôle de chaque dossier et fichier racine ; comprendre l'autoload PSR-4 et les espaces de noms ; identifier ce qui change depuis le squelette allégé de Laravel 11 ; savoir où placer le code métier ; adapter la structure à de grosses applications.

### 3.1 Vue d'ensemble

```text
mon-projet/
├── app/              ← code applicatif (namespace App\)
├── bootstrap/        ← démarrage du framework, caches générés
├── config/           ← fichiers de configuration
├── database/         ← migrations, factories, seeders
├── public/           ← seul dossier exposé au serveur web
├── resources/        ← vues Blade, CSS/JS sources, traductions
├── routes/           ← définition des routes
├── storage/          ← fichiers générés (logs, cache, uploads)
├── tests/            ← tests Feature et Unit
├── vendor/           ← dépendances Composer
├── .env / .env.example
├── artisan           ← point d'entrée CLI
├── composer.json / composer.lock
├── package.json
├── phpunit.xml
└── vite.config.js
```

### 3.2 `app/` : le cœur applicatif

Espace de noms racine `App\` (autoload **PSR-4** défini dans `composer.json`).

- `Models/` : modèles Eloquent.
- `Http/Controllers/` : contrôleurs.
- `Http/Middleware/` : middleware personnalisés.
- `Http/Requests/` : **Form Requests** (créé à la demande).
- `Providers/` : service providers (`AppServiceProvider`…).
- Dossiers **créés à la demande** par les commandes `make:*` : `Jobs/`, `Events/`, `Listeners/`, `Mail/`, `Notifications/`, `Policies/`, `Rules/`, `Observers/`, `Console/Commands/`, `Exceptions/`, `View/Components/`.

> **Note de version.** Depuis **Laravel 11**, le squelette est **allégé** : plus de `Http/Kernel.php`, de `Console/Kernel.php` ni de `Exceptions/Handler.php`. La configuration de l'application (routage, middleware, exceptions) est centralisée dans **`bootstrap/app.php`**. Les anciens `AuthServiceProvider`, `EventServiceProvider` et `RouteServiceProvider` ont disparu (découverte automatique). Un projet plus ancien conserve ces fichiers *(héritage)*.

Vous pouvez ajouter vos propres dossiers : `Services/`, `Actions/`, `DTOs/`, `Enums/`, `Repositories/`. Tant qu'ils sont sous `App\`, l'autoload fonctionne.

### 3.3 `bootstrap/`

- `app.php` : crée et configure l'application (routing, middleware, exceptions).
- `providers.php` : liste des **service providers** de l'application.
- `cache/` : fichiers de cache générés (packages, services). Doit être **inscriptible**.

### 3.4 `config/`

Voir le chapitre 2 (section 2.5).

### 3.5 `database/`

- `migrations/` : historique versionné du schéma.
- `factories/` : générateurs de données de test.
- `seeders/` : peuplement de la base.
- `database.sqlite` : base SQLite éventuelle.

### 3.6 `public/`

Seul dossier **exposé au serveur web**. Il contient :

- `index.php` : **point d'entrée unique** (*front controller*).
- les assets compilés (`build/`), images, `robots.txt`, `.htaccess`.
- le **lien symbolique** `storage` vers `storage/app/public` (créé par `php artisan storage:link`).

> **Attention.** Ne **jamais** pointer le serveur web vers la racine du projet : cela exposerait `.env` et le code source.

### 3.7 `resources/`

- `views/` : gabarits Blade.
- `css/`, `js/` : sources frontend compilées par Vite.
- `lang/` : fichiers de traduction (à publier par `php artisan lang:publish`).

### 3.8 `routes/`

- `web.php` : routes **web** (session, cookies, CSRF).
- `api.php` : routes **API** (sans état, préfixe `/api`), créé par `php artisan install:api`.
- `console.php` : commandes Artisan en closure et **tâches planifiées**.
- `channels.php` : autorisation des canaux de *broadcasting*.

### 3.9 `storage/`

- `app/` : fichiers de l'application (`app/private` pour le disque local, `app/public` pour les fichiers publics).
- `framework/` : cache, sessions, vues compilées.
- `logs/` : `laravel.log`.

Ce dossier doit être **inscriptible** par le serveur web.

### 3.10 `tests/`

- `Feature/` : tests d'intégration (HTTP, base de données).
- `Unit/` : tests unitaires isolés.
- `TestCase.php` : classe de base.

### 3.11 `vendor/`

Dépendances Composer. **Non versionné** ; reconstitué par `composer install`.

### 3.12 Fichiers racine

| Fichier | Rôle |
| --- | --- |
| `artisan` | Point d'entrée de la ligne de commande |
| `composer.json` | Dépendances PHP, autoload, scripts |
| `composer.lock` | Versions **exactes** installées (à versionner) |
| `package.json` | Dépendances JavaScript |
| `phpunit.xml` | Configuration des tests |
| `vite.config.js` | Configuration du bundler |
| `.gitignore`, `.editorconfig` | Outillage |

### 3.13 Autoload PSR-4 et espaces de noms

```json
// composer.json (extrait)
"autoload": {
    "psr-4": {
        "App\\": "app/",
        "Database\\Factories\\": "database/factories/",
        "Database\\Seeders\\": "database/seeders/"
    }
}
```

**Règle** : l'espace de noms d'une classe **reflète son chemin**. `App\Services\Billing\InvoiceService` → `app/Services/Billing/InvoiceService.php`. Après modification de l'autoload : `composer dump-autoload`.

### 3.14 Personnaliser la structure

Laravel n'impose pas de structure rigide. Pour de grosses applications :

- Organisation par **domaine** (`app/Domain/Billing/…`).
- **Modules** (package `nwidart/laravel-modules`).
- Architecture hexagonale ou DDD (chapitre 37).

### 3.15 Pièges fréquents

- **Namespace ≠ chemin** : la classe n'est pas trouvée (« Class not found »).
- **Créer un fichier hors `app/`** sans déclarer l'autoload correspondant.
- **Oublier `composer dump-autoload`** après ajout d'un fichier d'helpers dans `autoload.files`.
- **Placer des secrets dans `public/`** : tout fichier de ce dossier est téléchargeable.

### Synthèse du chapitre 3

`app/` contient votre code, `routes/` vos URL, `resources/` vos vues, `database/` votre schéma, `config/` et `.env` votre configuration. **Seul `public/` est exposé.** Depuis Laravel 11, `bootstrap/app.php` centralise routage, middleware et exceptions. L'autoload **PSR-4** relie espace de noms et chemin.

---

## 4. Cycle de vie d'une requête

**Objectifs d'apprentissage.** Décrire, étape par étape, le trajet d'une requête de `public/index.php` jusqu'à la réponse ; expliquer le rôle du noyau, des providers (`register` puis `boot`), du routeur et des middleware ; savoir où intervenir selon le besoin ; configurer l'application avec `bootstrap/app.php`.

### 4.1 Étape 1 : le point d'entrée

Toute requête est dirigée par le serveur web (Nginx, Apache) vers **`public/index.php`**. Ce fichier :

1. définit `LARAVEL_START` ;
2. vérifie le **mode maintenance** ;
3. charge l'autoloader de Composer (`vendor/autoload.php`) ;
4. charge `bootstrap/app.php` pour obtenir l'instance d'application ;
5. appelle `handleRequest()` avec la requête capturée.

```php
// public/index.php (extrait)
$app = require_once __DIR__.'/../bootstrap/app.php';
$app->handleRequest(Request::capture());
```

### 4.2 Étape 2 : création de l'application et du conteneur

`bootstrap/app.php` instancie `Illuminate\Foundation\Application`, qui **est** le **service container** (conteneur d'injection de dépendances). On y enregistre les composants de base et la configuration (routage, middleware, exceptions).

### 4.3 Étape 3 : le noyau HTTP

La requête est envoyée au **noyau** (*kernel*). Celui-ci :

1. **amorce** (*bootstrap*) le framework : charge les variables d'environnement et la configuration, configure la gestion d'erreurs, enregistre les **facades**, puis **enregistre et démarre les service providers** ;
2. fait passer la requête par la **pile de middleware globaux** (vérification du mode maintenance, taille de la requête POST, `TrimStrings`, `ConvertEmptyStringsToNull`, proxys de confiance, CORS…).

### 4.4 Étape 4 : les service providers

Deux phases, **dans cet ordre** :

1. **`register()`** de **tous** les providers : on y **lie** des services au conteneur. On n'y utilise **pas** d'autres services, car ils peuvent ne pas être encore enregistrés.
2. **`boot()`** de **tous** les providers : tout est enregistré, on peut utiliser n'importe quel service (routes, vues, événements, macros).

Les composants du framework (base de données, queue, validation, routage…) sont eux-mêmes démarrés par des providers.

### 4.5 Étape 5 : le routage

La requête est transmise au **routeur**, qui :

1. cherche la route correspondant à **méthode HTTP + URI** ;
2. résout les **paramètres** et le **route model binding** ;
3. applique les **middleware de route** (groupe `web` ou `api`, `auth`, `throttle`…).

Si aucune route ne correspond : `NotFoundHttpException` → **404**.

### 4.6 Étape 6 : exécution de la route

Le routeur exécute la closure ou la méthode du contrôleur :

- le conteneur **résout les dépendances** (injection dans le constructeur et dans la méthode) ;
- les **Form Requests** sont validées **avant** l'exécution de la méthode ;
- le contrôleur utilise modèles, services, etc., et **retourne une valeur**.

### 4.7 Étape 7 : fabrication de la réponse

La valeur de retour est convertie en objet `Response` :

| Valeur retournée | Réponse |
| --- | --- |
| `string` | HTML |
| `array`, `Arrayable`, modèle Eloquent | JSON |
| `View` | HTML rendu par Blade |
| `RedirectResponse`, `JsonResponse`, `StreamedResponse`… | Selon le type |

### 4.8 Étape 8 : retour à travers les middleware

La réponse **remonte** la pile de middleware **en sens inverse** (idéal pour ajouter des en-têtes, enregistrer des cookies, écrire la session…).

### 4.9 Étape 9 : envoi et terminaison

1. `send()` envoie la réponse au navigateur.
2. Les **middleware terminables** (méthode `terminate()`) et les jobs `dispatchAfterResponse` s'exécutent **après** l'envoi.

### 4.10 Gestion des exceptions

Toute exception non interceptée est traitée par le **gestionnaire d'exceptions** configuré dans `bootstrap/app.php` (`withExceptions`). Il **reporte** (journalise) puis **rend** (convertit en réponse HTTP : page d'erreur, JSON, redirection avec erreurs de validation).

### 4.11 Schéma récapitulatif

```text
Navigateur
   │
   ▼
public/index.php
   │
   ▼
bootstrap/app.php  → Application (Service Container)
   │
   ▼
Middleware globaux
   │
   ▼
Service Providers (register → boot)
   │
   ▼
Routeur → Middleware de route
   │
   ▼
Contrôleur / Closure
   │
   ▼
Réponse → Middleware (retour) → Navigateur
   │
   ▼
terminate()
```

### 4.12 Configurer l'application avec `bootstrap/app.php` *(à jour)*

```php
// bootstrap/app.php
use Illuminate\Foundation\Application;
use Illuminate\Foundation\Configuration\Exceptions;
use Illuminate\Foundation\Configuration\Middleware;

return Application::configure(basePath: dirname(__DIR__))
    ->withRouting(
        web: __DIR__.'/../routes/web.php',
        api: __DIR__.'/../routes/api.php',
        commands: __DIR__.'/../routes/console.php',
        health: '/up',                                   // route de santé pour les sondes
    )
    ->withMiddleware(function (Middleware $middleware) {
        $middleware->web(append: [\App\Http\Middleware\TrackVisits::class]);
        $middleware->alias(['admin' => \App\Http\Middleware\EnsureAdmin::class]);
    })
    ->withExceptions(function (Exceptions $exceptions) {
        //
    })
    ->create();
```

### 4.13 Points d'intervention : où mettre quoi ?

| Besoin | Lieu |
| --- | --- |
| Modifier toutes les requêtes ou réponses | Middleware **global** |
| Enregistrer un service dans le conteneur | `register()` d'un provider |
| Écouter un événement, définir une macro, un composeur de vue | `boot()` d'un provider |
| Contrôler l'accès à une route | Middleware de route / **Policy** |
| Gérer une erreur | `withExceptions` |
| Exécuter du code après la réponse | `terminate()` / `dispatchAfterResponse` |

### 4.14 Pièges fréquents

- **Utiliser un service dans `register()`** : il peut ne pas encore être enregistré ; déplacez le code dans `boot()`.
- **Chercher `Kernel.php`** dans un projet récent : la configuration est dans `bootstrap/app.php`.
- **Code lourd dans un middleware global** : il s'exécute à **chaque** requête, y compris les ressources statiques servies par PHP.
- **Oublier que la réponse repasse par les middleware** : une modification « après » ne s'applique qu'à la sortie de `$next($request)`.

### Synthèse du chapitre 4

Une requête entre par **`public/index.php`**, crée l'**application/conteneur**, traverse le **noyau** (amorçage + middleware globaux), les **providers** (`register` puis `boot`), le **routeur** (route, binding, middleware de route), atteint le **contrôleur**, produit une **réponse** qui remonte les middleware avant d'être **envoyée**, puis `terminate()` s'exécute. Les exceptions suivent le chemin `report` → `render`.

---

# Partie II — La couche HTTP

## 5. Routing

**Objectifs d'apprentissage.** Définir une route et ses fichiers de déclaration ; maîtriser les verbes HTTP et la méthode simulée ; utiliser paramètres, contraintes et routes nommées ; grouper des routes ; générer des routes de ressources ; comprendre le *route model binding* (implicite, explicite, clé personnalisée) ; connaître les routes spéciales (vue, redirection, *fallback*) ; limiter le débit ; signer des URL ; mettre les routes en cache.

### 5.1 Définition

Le **routing** associe une **méthode HTTP + un URI** à une **action** (closure ou méthode de contrôleur). Les routes sont déclarées dans :

- `routes/web.php` : interface **web** (session, cookies, protection CSRF) ;
- `routes/api.php` : **API** sans état, préfixe `/api` (créé par `php artisan install:api`).

### 5.2 Routes de base

```php
// routes/web.php
use Illuminate\Support\Facades\Route;

Route::get('/', fn () => view('welcome'));
Route::post('/articles', [ArticleController::class, 'store']);
Route::put('/articles/{id}', [ArticleController::class, 'update']);
Route::patch('/articles/{id}', [ArticleController::class, 'update']);
Route::delete('/articles/{id}', [ArticleController::class, 'destroy']);
Route::options('/ping', fn () => response('', 204));

Route::match(['get', 'post'], '/contact', ContactController::class);   // plusieurs verbes
Route::any('/webhook', WebhookController::class);                        // tous les verbes
```

**Verbes HTTP**

| Verbe | Sémantique | Idempotent |
| --- | --- | --- |
| GET | Lire | Oui |
| POST | Créer | Non |
| PUT | Remplacer | Oui |
| PATCH | Modifier partiellement | Non (en général) |
| DELETE | Supprimer | Oui |

**Méthode simulée.** Les formulaires HTML ne supportent que GET et POST. Pour PUT, PATCH ou DELETE, on envoie un POST avec un champ caché `_method` :

```blade
<form method="POST" action="/articles/1">
    @csrf
    @method('DELETE')
</form>
```

### 5.3 Paramètres de route

```php
Route::get('/users/{id}', function (string $id) {
    return "Utilisateur $id";
});

Route::get('/posts/{post}/comments/{comment}', function ($post, $comment) { /* … */ });
```

Les paramètres sont injectés **dans l'ordre**, indépendamment des noms de variables. Les dépendances du conteneur (comme `Request`) peuvent les précéder :

```php
Route::get('/users/{id}', function (Request $request, string $id) { /* … */ });
```

**Paramètres optionnels** (une valeur par défaut est obligatoire) :

```php
Route::get('/users/{name?}', fn (?string $name = 'Invité') => $name);
```

### 5.4 Contraintes de paramètres

```php
Route::get('/users/{id}', /* … */)->where('id', '[0-9]+');
Route::get('/users/{id}/{name}', /* … */)->where(['id' => '[0-9]+', 'name' => '[a-z]+']);

// Aides prêtes à l'emploi
->whereNumber('id')
->whereAlpha('name')
->whereAlphaNumeric('slug')
->whereUuid('id')
->whereUlid('id')
->whereIn('type', ['a', 'b'])
```

**Contraintes globales** (dans le `boot()` d'un provider) :

```php
Route::pattern('id', '[0-9]+');
```

Pour autoriser un `/` dans un paramètre : `->where('search', '.*')`.

### 5.5 Routes nommées

```php
Route::get('/profil', [ProfileController::class, 'show'])->name('profile.show');

$url = route('profile.show');
$url = route('users.show', ['user' => 1, 'tab' => 'info']);   // /users/1?tab=info
return redirect()->route('profile.show');
$request->routeIs('profile.*');                                // test du nom de route
```

**Bonne pratique** : **toujours nommer** ses routes pour ne jamais coder les URL en dur.

### 5.6 Groupes de routes

```php
Route::middleware(['auth', 'verified'])
    ->prefix('admin')            // /admin/…
    ->name('admin.')             // admin.dashboard
    ->group(function () {
        Route::get('/dashboard', DashboardController::class)->name('dashboard');
    });

Route::controller(OrderController::class)->group(function () {
    Route::get('/orders/{id}', 'show');
    Route::post('/orders', 'store');
});

Route::domain('{account}.monsite.com')->group(function () {          // sous-domaines
    Route::get('/', fn (string $account) => $account);
});

Route::scopeBindings()->group(/* … */);                             // liaison enfant limitée au parent
Route::withoutMiddleware([/* … */])->group(/* … */);
```

### 5.7 Routes de ressources (CRUD)

```bash
php artisan make:controller PhotoController --resource
```

```php
Route::resource('photos', PhotoController::class);
Route::resources(['photos' => PhotoController::class, 'posts' => PostController::class]);
Route::apiResource('photos', PhotoController::class);        // sans create ni edit
Route::apiResources([/* … */]);

// Restrictions et personnalisation
Route::resource('photos', PhotoController::class)->only(['index', 'show']);
Route::resource('photos', PhotoController::class)->except(['destroy']);
Route::resource('photos', PhotoController::class)->names('gallery');
Route::resource('photos', PhotoController::class)->parameters(['photos' => 'image']);
Route::resource('photos', PhotoController::class)->shallow();               // imbrication « peu profonde »
Route::resource('photos.comments', CommentController::class);               // ressources imbriquées
Route::resource('photos', PhotoController::class)->missing(fn () => redirect('/'));
Route::resource('photos', PhotoController::class)->withTrashed();
Route::singleton('profile', ProfileController::class);                      // ressource singleton
```

**Routes générées par `resource`**

| Verbe | URI | Action | Nom |
| --- | --- | --- | --- |
| GET | `/photos` | index | photos.index |
| GET | `/photos/create` | create | photos.create |
| POST | `/photos` | store | photos.store |
| GET | `/photos/{photo}` | show | photos.show |
| GET | `/photos/{photo}/edit` | edit | photos.edit |
| PUT/PATCH | `/photos/{photo}` | update | photos.update |
| DELETE | `/photos/{photo}` | destroy | photos.destroy |

### 5.8 Route Model Binding

**Liaison implicite.** Si le nom du paramètre correspond à une variable typée avec un **modèle Eloquent**, Laravel récupère l'instance (et répond **404** automatiquement si elle est absente).

```php
Route::get('/articles/{article}', fn (Article $article) => $article);
```

**Clé personnalisée**

```php
Route::get('/articles/{article:slug}', fn (Article $article) => $article);

// ou, pour tout le modèle :
// app/Models/Article.php
public function getRouteKeyName(): string { return 'slug'; }
```

**Soft deletes** : `->withTrashed()` pour inclure les enregistrements supprimés logiquement.

**Liaison explicite** (dans le `boot()` d'un provider) :

```php
Route::model('article', Article::class);
Route::bind('article', fn (string $value) => Article::where('slug', $value)->firstOrFail());
```

**Résolution personnalisée** dans le modèle : méthode `resolveRouteBinding($value, $field)`.

**Enums** : un enum *backed* (string) typé dans la closure est résolu automatiquement ; une valeur invalide donne un 404.

```php
Route::get('/categories/{category}', fn (Category $category) => /* … */);   // Category est un enum
```

### 5.9 Autres types de routes

```php
Route::view('/about', 'about', ['team' => 'X']);                 // vue directe, sans contrôleur
Route::redirect('/ancien', '/nouveau', 301);
Route::permanentRedirect('/ancien', '/nouveau');
Route::fallback(fn () => response()->view('errors.404', [], 404));   // route « attrape-tout », à déclarer en dernier
```

### 5.10 Limitation de débit (*rate limiting*)

```php
// app/Providers/AppServiceProvider.php, dans boot()
RateLimiter::for('api', function (Request $request) {
    return Limit::perMinute(60)->by($request->user()?->id ?: $request->ip());
});

Route::middleware('throttle:api')->group(/* … */);
Route::middleware('throttle:10,1')->group(/* … */);           // 10 requêtes par minute
```

En cas de dépassement : réponse **429 Too Many Requests** avec l'en-tête `Retry-After`.

### 5.11 URLs signées

Une URL **signée** contient une signature qui détecte toute modification.

```php
URL::signedRoute('unsubscribe', ['user' => 1]);
URL::temporarySignedRoute('unsubscribe', now()->addMinutes(30), ['user' => 1]);

Route::get('/unsubscribe/{user}', /* … */)->name('unsubscribe')->middleware('signed');
$request->hasValidSignature();
```

### 5.12 Mise en cache des routes et inspection

```bash
php artisan route:list [--path=api] [--method=GET] [-v]
php artisan route:cache
php artisan route:clear
```

> **À retenir.** Historiquement, les routes en **closure** ne pouvaient pas être mises en cache. Les versions récentes savent les sérialiser, mais en production **préférez les contrôleurs** : plus lisibles, testables et compatibles avec la mise en cache.

### 5.13 Accès à la route courante et CORS

```php
Route::current();
Route::currentRouteName();
Route::currentRouteAction();
```

**CORS** (*Cross-Origin Resource Sharing*) : configurable dans `config/cors.php` (chapitre 28).

### 5.14 Pièges fréquents

- **Ordre des routes** : une route générique (`/users/{id}`) déclarée avant une route précise (`/users/create`) l'intercepte.
- **Oublier `@csrf`** ou `@method` dans un formulaire : réponse **419** ou **405**.
- **Fermeture de route non mise en cache** (anciennes versions) : `route:cache` échoue.
- **Lier `{article}` à un autre nom de variable** : l'implicite ne fonctionne que si le **nom du paramètre** et celui de la **variable typée** coïncident.
- **Coder les URL en dur** : cassées dès qu'une route change ; utilisez `route()`.

### Synthèse du chapitre 5

Une route associe **verbe + URI** à une action. Utilisez des **routes nommées**, des **groupes** (`prefix`, `name`, `middleware`, `controller`), des **routes de ressources** et le **route model binding**. Contraignez les paramètres, limitez le débit (`throttle`), signez les URL sensibles, et mettez les routes en cache en production.

---

## 6. Middleware

**Objectifs d'apprentissage.** Expliquer le patron « oignon » ; créer un middleware ; agir avant ou après la requête ; l'enregistrer (global, groupe, alias) selon Laravel 11+ ; l'assigner aux routes ; lui passer des paramètres ; écrire un middleware terminable ; connaître les middleware intégrés.

### 6.1 Définition et rôle

Un **middleware** est une couche qui intercepte la requête **avant** qu'elle atteigne la route (et/ou la réponse **après**). Il suit le patron « chaîne de responsabilité », dit aussi « oignon » :

```text
Requête → [MW1 → [MW2 → [Contrôleur] ← MW2] ← MW1] → Réponse
```

Usages : authentification, autorisation, journalisation, CORS, compression, localisation, limitation de débit, mode maintenance, modification de la requête ou de la réponse.

### 6.2 Créer un middleware

```bash
php artisan make:middleware EnsureTokenIsValid
```

```php
// app/Http/Middleware/EnsureTokenIsValid.php
namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;

class EnsureTokenIsValid
{
    public function handle(Request $request, Closure $next): Response
    {
        if ($request->input('token') !== 'mon-secret') {
            return redirect('home');            // court-circuite la chaîne
        }

        return $next($request);                 // passe au maillon suivant
    }
}
```

### 6.3 Avant et après

```php
// AVANT : la logique précède $next
public function handle($request, Closure $next)
{
    // logique avant
    return $next($request);
}

// APRÈS : la logique suit $next
public function handle($request, Closure $next)
{
    $response = $next($request);
    $response->headers->set('X-App', 'Laravel');     // ex. : ajout d'un en-tête
    return $response;
}
```

### 6.4 Enregistrement *(à jour : Laravel 11+)*

```php
// bootstrap/app.php
->withMiddleware(function (Middleware $middleware) {
    // Global (toutes les requêtes)
    $middleware->append(LogRequest::class);
    $middleware->prepend(FirstMiddleware::class);

    // Groupes web / api
    $middleware->web(append: [TrackVisits::class]);
    $middleware->api(prepend: [ForceJson::class]);

    // Alias
    $middleware->alias([
        'admin'      => EnsureUserIsAdmin::class,
        'subscribed' => EnsureUserIsSubscribed::class,
    ]);

    // Priorité d'exécution
    $middleware->priority([/* … */]);

    // Exclusions CSRF / chiffrement des cookies
    $middleware->validateCsrfTokens(except: ['stripe/*']);
    $middleware->encryptCookies(except: ['cookie_clair']);

    // Proxys de confiance
    $middleware->trustProxies(at: '*');
})
```

> **Héritage.** Avant Laravel 11, on déclarait les middleware dans `app/Http/Kernel.php` (`$middleware`, `$middlewareGroups`, `$middlewareAliases`/`$routeMiddleware`).

### 6.5 Assignation aux routes

```php
Route::get('/admin', /* … */)->middleware('admin');
Route::get('/x', /* … */)->middleware(['auth', 'verified']);
Route::get('/y', /* … */)->middleware(EnsureTokenIsValid::class);
Route::middleware('auth')->group(/* … */);
Route::get('/z', /* … */)->withoutMiddleware([EnsureTokenIsValid::class]);
```

### 6.6 Groupes de middleware

Laravel définit deux groupes par défaut :

- **`web`** : chiffrement des cookies, ajout des cookies à la réponse, démarrage de la session, partage des erreurs de validation, vérification CSRF, *bindings* de routes.
- **`api`** : *bindings* (+ `throttle` si configuré, Sanctum…), sans session ni CSRF.

Personnalisation :

```php
$middleware->appendToGroup('admin', [Authenticate::class, EnsureAdmin::class]);
```

### 6.7 Paramètres de middleware

```php
Route::put('/post/{id}', /* … */)->middleware('role:editor,admin');

// app/Http/Middleware/EnsureUserHasRole.php
public function handle(Request $request, Closure $next, string ...$roles): Response
{
    if (! in_array($request->user()->role, $roles)) {
        abort(403);
    }
    return $next($request);
}
```

### 6.8 Middleware terminable

```php
public function terminate(Request $request, Response $response): void
{
    // exécuté APRÈS l'envoi de la réponse au navigateur
}
```

> **Attention.** Un middleware terminable est **instancié une nouvelle fois** pour `terminate()`. Si l'instance doit être **partagée**, enregistrez-le en **singleton** dans un provider.

### 6.9 Middleware de contrôleur

```php
// app/Http/Controllers/UserController.php
use Illuminate\Routing\Controllers\HasMiddleware;
use Illuminate\Routing\Controllers\Middleware;

class UserController extends Controller implements HasMiddleware
{
    public static function middleware(): array
    {
        return [
            'auth',
            new Middleware('log', only: ['index']),
            new Middleware('subscribed', except: ['store']),
        ];
    }
}
```

### 6.10 Middleware intégrés importants

| Alias / classe | Rôle |
| --- | --- |
| `auth` | Utilisateur authentifié requis |
| `auth.basic` | HTTP Basic |
| `guest` | Réservé aux invités |
| `verified` | E-mail vérifié |
| `password.confirm` | Confirmation du mot de passe |
| `can:action,model` | Autorisation via Gate / Policy |
| `signed` | URL signée valide |
| `throttle` | Limitation de débit |
| `cache.headers` | En-têtes de cache HTTP |
| `ValidateCsrfToken` | Protection CSRF |
| `TrimStrings`, `ConvertEmptyStringsToNull` | Normalisation des entrées |
| `PreventRequestsDuringMaintenance` | Mode maintenance |
| `TrustProxies`, `TrustHosts` | Proxys et hôtes de confiance |

### 6.11 Exemple complet : middleware de langue

```php
// app/Http/Middleware/SetLocale.php
class SetLocale
{
    public function handle(Request $request, Closure $next): Response
    {
        $locale = $request->segment(1);
        if (in_array($locale, ['fr', 'en', 'mg'])) {
            app()->setLocale($locale);
        }
        return $next($request);
    }
}
```

### 6.12 Pièges fréquents

- **Oublier `return $next($request)`** : la requête n'atteint jamais la route (page blanche).
- **Ordre des middleware** : un middleware qui lit `$request->user()` doit passer **après** `auth`.
- **Modifier la réponse sans la récupérer** : appelez `$response = $next($request)` avant d'agir « après ».
- **Middleware global trop coûteux** : exécuté sur toutes les requêtes.
- **Confondre `abort(403)` et `redirect()`** : pour une API, retournez un code HTTP, pas une redirection.

### Synthèse du chapitre 6

Un **middleware** enveloppe la requête : il peut **agir avant**, **court-circuiter**, **agir après** (sur la réponse) ou **terminer** (`terminate`). Depuis Laravel 11, on les enregistre dans **`bootstrap/app.php`** (global, groupes `web`/`api`, alias). On les assigne aux routes, groupes ou contrôleurs, avec ou sans **paramètres**.

---

## 7. Contrôleurs

**Objectifs d'apprentissage.** Définir le rôle d'un contrôleur ; générer les différents types de contrôleurs ; utiliser l'injection de dépendances ; écrire un contrôleur de ressource et un contrôleur d'API ; appliquer des middleware ; organiser la logique métier (services, actions) ; reconnaître les bonnes pratiques.

### 7.1 Rôle

Un **contrôleur** regroupe la logique de traitement de requêtes liées. Il doit rester **mince** : *recevoir*, *valider*, *déléguer*, *répondre*. La logique métier vit ailleurs (services, actions, modèles).

### 7.2 Création

```bash
php artisan make:controller UserController
php artisan make:controller PhotoController --resource            # 7 actions CRUD
php artisan make:controller PhotoController --api                 # sans create/edit
php artisan make:controller PhotoController --resource --model=Photo
php artisan make:controller ShowProfile --invokable               # une seule action
php artisan make:controller Admin/UserController                  # sous-dossier
```

### 7.3 Contrôleur de base

```php
// app/Http/Controllers/UserController.php
namespace App\Http\Controllers;

use App\Models\User;

class UserController extends Controller
{
    public function show(string $id)
    {
        return view('user.profile', ['user' => User::findOrFail($id)]);
    }
}
```

```php
// routes/web.php
Route::get('/user/{id}', [UserController::class, 'show']);
```

### 7.4 Contrôleurs invocables

Une seule action, via la méthode magique `__invoke` :

```php
// app/Http/Controllers/ProvisionServer.php
class ProvisionServer extends Controller
{
    public function __invoke() { /* … */ }
}

Route::post('/server', ProvisionServer::class);
```

### 7.5 Injection de dépendances

**Dans le constructeur** (disponible pour toutes les méthodes) :

```php
public function __construct(protected UserRepository $users) {}
```

**Dans la méthode** (spécifique à l'action), mélangeable avec les paramètres de route :

```php
public function update(Request $request, string $id, Mailer $mailer) { /* … */ }
```

### 7.6 Contrôleurs de ressource

```php
class PhotoController extends Controller
{
    public function index()   { /* liste */ }
    public function create()  { /* formulaire de création */ }
    public function store(Request $request) { /* enregistrement */ }
    public function show(Photo $photo) { /* affichage */ }
    public function edit(Photo $photo) { /* formulaire d'édition */ }
    public function update(Request $request, Photo $photo) { /* mise à jour */ }
    public function destroy(Photo $photo) { /* suppression */ }
}
```

### 7.7 Exemple complet : CRUD

```php
// app/Http/Controllers/ArticleController.php
class ArticleController extends Controller
{
    public function index()
    {
        $articles = Article::with('author')->latest()->paginate(10);   // eager loading + pagination
        return view('articles.index', compact('articles'));
    }

    public function store(StoreArticleRequest $request)
    {
        $article = $request->user()->articles()->create($request->validated());

        return redirect()
            ->route('articles.show', $article)
            ->with('success', 'Article créé avec succès.');             // message flash
    }

    public function update(UpdateArticleRequest $request, Article $article)
    {
        $this->authorize('update', $article);
        $article->update($request->validated());
        return back()->with('success', 'Mis à jour.');
    }

    public function destroy(Article $article)
    {
        $this->authorize('delete', $article);
        $article->delete();
        return redirect()->route('articles.index');
    }
}
```

> **Note.** Depuis Laravel 11, le contrôleur de base `Controller` est **vide** : il n'inclut plus automatiquement les traits `AuthorizesRequests` et `ValidatesRequests`. Pour utiliser `$this->authorize()`, ajoutez le trait ou préférez `Gate::authorize()` / `Gate::allows()` (chapitre 16).

### 7.8 Contrôleurs d'API

Ils retournent du **JSON** avec des codes HTTP adaptés (200, 201, 204, 404, 422).

```php
public function store(StoreArticleRequest $request): JsonResponse
{
    $article = Article::create($request->validated());
    return (new ArticleResource($article))
        ->response()->setStatusCode(201);
}

public function destroy(Article $article): Response
{
    $article->delete();
    return response()->noContent();              // 204
}
```

### 7.9 Middleware dans le contrôleur

Voir le chapitre 6 (section 6.9) : interface `HasMiddleware` et méthode statique `middleware()`.

### 7.10 Organisation avancée

Pour garder des contrôleurs minces :

| Brique | Rôle | Exemple |
| --- | --- | --- |
| **Services** | Logique métier réutilisable | `OrderService::place($data)` |
| **Actions** | Classes à action unique | `CreateOrderAction::execute()` |
| **Form Requests** | Validation et autorisation | `StoreArticleRequest` |
| **Resources** | Formatage des réponses | `ArticleResource` |
| **Jobs / Events** | Traitements secondaires | `SendInvoice`, `OrderPlaced` |

### 7.11 Bonnes pratiques

- **Un contrôleur = une ressource**, avec les **7 actions standard** ; créez un nouveau contrôleur plutôt que d'ajouter des actions « exotiques ».
- **Pas de requêtes SQL complexes** dans le contrôleur.
- **Typer** les paramètres et les retours.
- Retourner des réponses **cohérentes** : *redirect + flash* pour le web, *JSON + code HTTP* pour l'API.
- Valider par **Form Request**, autoriser par **Policy**.

### 7.12 Pièges fréquents

- **Contrôleur « fourre-tout »** de centaines de lignes : extraire services et actions.
- **`$request->all()` passé à `create()`** : risque d'*assignation de masse* (chapitre 13) ; utiliser `validated()`.
- **Oublier l'autorisation** : l'accès à une route ne prouve pas que l'utilisateur possède la ressource (faille **IDOR**, chapitre 33).
- **Appeler `$this->authorize()`** sans le trait requis (Laravel 11+).

### Synthèse du chapitre 7

Un contrôleur **reçoit, valide, délègue et répond**. Générez-le avec `make:controller` (`--resource`, `--api`, `--invokable`). L'**injection** par constructeur ou par méthode fournit les dépendances. Gardez-le **mince** grâce aux Form Requests, Resources, services et actions.

---

## 8. Requêtes et réponses

**Objectifs d'apprentissage.** Lire les données d'entrée d'une requête (query, corps, JSON, fichiers) ; tester leur présence ; obtenir des informations sur la requête ; gérer les anciennes entrées ; téléverser des fichiers ; produire différentes réponses (texte, JSON, vue, redirection, fichier, flux) ; maîtriser les codes de statut, les cookies et la négociation de contenu ; créer des macros de réponse.

### 8.1 L'objet `Request`

`Illuminate\Http\Request` étend `Symfony\Component\HttpFoundation\Request`. On l'obtient par **injection de dépendances**, ou par le helper `request()`.

```php
public function store(Request $request) { /* … */ }
```

### 8.2 Lire les données d'entrée

```php
$request->all();                          // tout (query + corps + JSON)
$request->input('name');                  // une valeur (query ou corps)
$request->input('name', 'défaut');
$request->input('products.0.name');       // notation pointée (tableaux)
$request->input('products.*.name');       // joker
$request->query('page');                  // uniquement la query string
$request->post('name');                   // uniquement le corps
$request->only(['name', 'email']);
$request->except(['password']);
$request->string('name')->trim();         // objet Stringable
$request->integer('per_page', 15);
$request->boolean('archived');
$request->date('birthday');               // Carbon
$request->enum('status', Status::class);
$request->collect('tags');                // Collection
$request->safe()->only([/* … */]);        // données validées (Form Request)
```

**Tester la présence**

```php
$request->has('name');              // clé présente (même vide)
$request->hasAny(['a', 'b']);
$request->filled('name');           // présente ET non vide
$request->missing('name');
$request->whenHas('name', fn ($v) => /* … */, fn () => /* … */);
$request->whenFilled('name', fn ($v) => /* … */);
```

**Entrées JSON.** Si l'en-tête `Content-Type: application/json` est présent, `input()` lit directement le JSON.

**Fusionner / injecter des valeurs** : `$request->merge(['slug' => Str::slug($titre)])`, `$request->mergeIfMissing([/* … */])`.

**Anciennes entrées (*old input*)** — pour réafficher un formulaire après échec :

```php
return back()->withInput();
$request->old('username');
// dans Blade : old('username')
$request->flash();
```

### 8.3 Informations sur la requête

```php
$request->path();             // 'users/1'
$request->url();              // sans query string
$request->fullUrl();          // avec query string
$request->method();           // 'GET'
$request->isMethod('post');
$request->is('admin/*');
$request->routeIs('admin.*');
$request->ip();  $request->ips();
$request->userAgent();
$request->header('X-Header', 'défaut');
$request->hasHeader('X-Header');
$request->bearerToken();
$request->expectsJson();      // le client attend du JSON
$request->wantsJson();
$request->acceptsJson();
$request->secure();           // HTTPS ?
$request->host();
$request->user();             // utilisateur authentifié
$request->route('user');      // paramètre de la route
$request->cookie('name');
$request->session();
```

### 8.4 Fichiers téléversés

```php
$file = $request->file('photo');
$request->hasFile('photo');
$request->file('photo')->isValid();

$file->path();
$file->extension();
$file->getClientOriginalName();
$file->getClientOriginalExtension();
$file->getSize();
$file->getMimeType();

$path = $file->store('images');                         // nom généré automatiquement
$path = $file->store('images', 's3');
$path = $file->storeAs('images', 'moi.jpg', 'public');
$path = $file->storePublicly('avatars', 's3');
```

Le formulaire doit déclarer `enctype="multipart/form-data"`. Le stockage est détaillé au chapitre 27.

### 8.5 Normalisation automatique des entrées

Les middleware **`TrimStrings`** (suppression des espaces) et **`ConvertEmptyStringsToNull`** (chaîne vide → `null`) nettoient les entrées. On peut les désactiver sélectivement dans `withMiddleware`.

### 8.6 Les réponses

Tout retour de route est converti en réponse :

```php
return 'Bonjour';                       // text/html
return ['name' => 'Jean'];              // JSON automatiquement
return User::find(1);                   // JSON (Arrayable)
return view('home');
```

### 8.7 L'objet `Response`

```php
return response('Hello', 200)
    ->header('Content-Type', 'text/plain')
    ->withHeaders(['X-A' => '1', 'X-B' => '2'])
    ->cookie('name', 'value', $minutes)
    ->withoutCookie('name');
```

### 8.8 Réponses JSON

```php
return response()->json(['name' => 'Abigail'], 201);
return response()->json($data)->withCallback($request->input('callback'));   // JSONP
```

### 8.9 Redirections

```php
return redirect('/home');
return redirect()->route('login');
return redirect()->action([UserController::class, 'index']);
return redirect()->away('https://exemple.com');                  // domaine externe
return back();
return back()->withInput();
return redirect('/dashboard')->with('status', 'Profil mis à jour !');   // message flash (session)
return redirect()->route('x')->withErrors($validator);
return redirect()->intended('/dashboard');                       // destination d'origine après connexion
```

### 8.10 Autres types de réponses

```php
return response()->view('hello', $data, 200);
return response()->download($pathToFile, 'nom.pdf', $headers);
return response()->file($pathToFile);                            // affichage dans le navigateur
return response()->streamDownload(fn () => print('contenu'), 'fichier.txt');
return response()->stream(function () { /* … */ }, 200, $headers);   // flux continu
return response()->noContent();                                  // 204
return response()->json([/* … */], 422);
```

### 8.11 Macros de réponse

```php
// app/Providers/AppServiceProvider.php, dans boot()
Response::macro('caps', fn (string $value) => Response::make(strtoupper($value)));

return response()->caps('foo');
```

### 8.12 Codes de statut HTTP à connaître

| Code | Signification |
| --- | --- |
| 200 OK | Succès |
| 201 Created | Ressource créée |
| 204 No Content | Succès sans contenu |
| 301 / 302 | Redirection permanente / temporaire |
| 304 | Non modifié |
| 400 | Mauvaise requête |
| 401 | Non authentifié |
| 403 | Interdit (authentifié mais non autorisé) |
| 404 | Introuvable |
| 405 | Méthode non autorisée |
| 409 | Conflit |
| 419 | Jeton CSRF expiré (spécifique à Laravel) |
| 422 | Entité non traitable (échec de validation) |
| 429 | Trop de requêtes |
| 500 | Erreur serveur |
| 503 | Service indisponible (maintenance) |

### 8.13 Cookies

```php
Cookie::queue('name', 'value', $minutes);       // ajouté à la prochaine réponse
$request->cookie('name');
```

Les cookies Laravel sont **chiffrés et signés** par défaut.

### 8.14 Négociation de contenu

```php
if ($request->expectsJson()) {
    return response()->json($data);
}
return view('page', $data);
```

### 8.15 Pièges fréquents

- **`has()` vs `filled()`** : `has('name')` est vrai pour une chaîne vide ; utilisez `filled()` pour exiger une valeur.
- **`input()` mélange query et corps** : utilisez `query()` ou `post()` pour être précis.
- **Oublier `enctype="multipart/form-data"`** : le fichier n'arrive pas.
- **Faire confiance à `getClientOriginalName()`** : nom contrôlé par le client ; préférez le nom généré (chapitre 27).
- **Redirection sans `with()`** : le message flash n'existe pas pour la page suivante.
- **Retourner une redirection à une API** : renvoyez un code HTTP et du JSON.

### Synthèse du chapitre 8

L'objet **`Request`** donne accès aux entrées (`input`, `query`, `file`…), à leur présence (`has`, `filled`) et aux métadonnées. Les **réponses** peuvent être du texte, du **JSON**, une **vue**, une **redirection** (avec `with`, `withErrors`, `withInput`), un **fichier** ou un **flux**. Maîtrisez les **codes HTTP**, les **cookies** (chiffrés) et la **négociation de contenu** (`expectsJson`).

---

# Partie III — Vues, Blade et validation

## 9. Vues et Blade

**Objectifs d'apprentissage.** Créer et retourner des vues ; partager des données (`View::share`, composeurs) ; afficher des données en sécurité (échappement) ; maîtriser directives conditionnelles, boucles et `$loop` ; construire des layouts par héritage et par composants ; écrire des composants (classe, anonymes, slots, attributs) ; afficher erreurs de validation et jeton CSRF ; créer des directives personnalisées ; injecter des services ; connaître les approches frontend modernes.

### 9.1 Les vues

Les **vues** séparent la **présentation** de la logique. Elles sont stockées dans `resources/views` avec l'extension `.blade.php`.

```php
return view('greeting', ['name' => 'James']);       // resources/views/greeting.blade.php
return view('admin.profile', $data);                // resources/views/admin/profile.blade.php
return view('greeting')->with('name', 'Victoria')->with('age', 30);
view()->exists('admin.profile');
view()->first(['custom.admin', 'admin'], $data);    // la première qui existe
```

**Partage de données avec toutes les vues** (dans le `boot()` d'un provider) :

```php
View::share('appName', config('app.name'));
```

**View composers** : injectent des données **lorsqu'une vue est rendue**.

```php
View::composer('dashboard', function (View $view) {
    $view->with('count', User::count());
});
View::composer(['profile', 'dashboard'], ProfileComposer::class);
View::composer('*', /* … */);                       // toutes les vues
```

Les **creators** sont similaires, mais s'exécutent à l'**instanciation** de la vue.

**Optimisation.** Les vues Blade sont **compilées en PHP** dans `storage/framework/views` ; `php artisan view:cache` les pré-compile, `view:clear` les vide.

### 9.2 Blade : présentation

**Blade** est le moteur de gabarits de Laravel. Il **compile en PHP pur** (aucun surcoût à l'exécution) et autorise le PHP natif dans les gabarits.

### 9.3 Afficher des données

```blade
Bonjour, {{ $name }}.
{{ time() }}
{{ $user->name ?? 'Invité' }}
{{ isset($name) ? $name : 'Défaut' }}
```

| Syntaxe | Effet |
| --- | --- |
| `{{ $x }}` | **Échappe** automatiquement (`htmlspecialchars`) → protection **XSS** |
| `{!! $html !!}` | **N'échappe pas**. À réserver au contenu de confiance |
| `@{{ name }}` | Empêche l'interprétation (utile avec Vue/Alpine) |
| `@verbatim … @endverbatim` | Bloc non interprété |
| `{{-- commentaire --}}` | Commentaire Blade (absent du HTML final) |

**Rendu JSON pour JavaScript**

```blade
<script>
    const app = @json($array);
    const app2 = {{ Js::from($array) }};
</script>
```

Le double encodage des entités HTML est désactivable par `Blade::withoutDoubleEncoding()`.

### 9.4 Directives conditionnelles

```blade
@if (count($records) === 1)
    Un enregistrement
@elseif (count($records) > 1)
    Plusieurs
@else
    Aucun
@endif

@unless (Auth::check()) Vous n'êtes pas connecté @endunless

@isset($records) … @endisset
@empty($records) … @endempty

@auth … @endauth
@auth('admin') … @endauth
@guest … @endguest

@production … @endproduction
@env('staging') … @endenv

@hasSection('navigation') … @endif
@sectionMissing('navigation') … @endif

@switch($i)
    @case(1) Premier @break
    @case(2) Second @break
    @default Défaut
@endswitch
```

**Attributs conditionnels**

```blade
<input type="checkbox" @checked(old('active', $user->active)) />
<option @selected($value == $current)>…</option>
<button @disabled($errors->isNotEmpty())>Envoyer</button>
<input @readonly($user->isNotAdmin()) />
<input @required($user->isAdmin()) />
<div @class(['p-4', 'font-bold' => $isActive, 'bg-red' => $hasError])></div>
<div @style(['background-color: red', 'font-weight: bold' => $isActive])></div>
```

### 9.5 Boucles

```blade
@for ($i = 0; $i < 10; $i++) Valeur : {{ $i }} @endfor

@foreach ($users as $user)
    <p>{{ $user->name }}</p>
@endforeach

@forelse ($users as $user)
    <li>{{ $user->name }}</li>
@empty
    <p>Aucun utilisateur</p>
@endforelse

@while (true) … @endwhile

@continue
@break
@continue($user->type == 1)
@break($user->number == 5)
```

**Variable `$loop`** (dans `@foreach` et `@forelse`)

| Propriété | Description |
| --- | --- |
| `$loop->index` | Index (commence à 0) |
| `$loop->iteration` | Itération (commence à 1) |
| `$loop->remaining` | Itérations restantes |
| `$loop->count` | Nombre total d'éléments |
| `$loop->first` / `$loop->last` | Première / dernière itération |
| `$loop->even` / `$loop->odd` | Parité |
| `$loop->depth` | Niveau d'imbrication |
| `$loop->parent` | `$loop` de la boucle parente |

### 9.6 PHP brut et directives diverses

```blade
@php
    $counter = 1;
@endphp

@use('App\Models\Flight')
@include('shared.errors')
@include('view.name', ['status' => 'complete'])
@includeIf('view.name')
@includeWhen($boolean, 'view.name')
@includeUnless($boolean, 'view.name')
@includeFirst(['custom.admin', 'admin'])
@each('view.name', $jobs, 'job', 'view.empty')
@once … @endonce                                   {{-- n'est rendu qu'une fois --}}
```

### 9.7 Layouts : héritage de gabarits

**Layout parent**

```blade
{{-- resources/views/layouts/app.blade.php --}}
<html>
<head>
    <title>@yield('title', 'Mon site')</title>
    @stack('styles')
</head>
<body>
    @section('sidebar') Barre latérale principale @show
    <div class="container">
        @yield('content')
    </div>
    @stack('scripts')
</body>
</html>
```

**Vue enfant**

```blade
{{-- resources/views/home.blade.php --}}
@extends('layouts.app')

@section('title', 'Accueil')

@section('sidebar')
    @parent
    <p>Ajouté à la barre latérale.</p>
@endsection

@section('content')
    <p>Contenu</p>
@endsection

@push('scripts')
    <script src="/x.js"></script>
@endpush
```

| Directive | Rôle |
| --- | --- |
| `@yield` | Affiche le contenu d'une section |
| `@section … @show` | Définit **et** affiche immédiatement |
| `@parent` | Inclut le contenu de la section parente |
| `@push` / `@prepend` / `@stack` | Accumulation de contenu (scripts, styles) |

### 9.8 Formulaires, CSRF et méthodes

```blade
<form method="POST" action="/profile">
    @csrf
    @method('PUT')
    …
</form>
```

- `@csrf` génère `<input type="hidden" name="_token" value="…">`.
- Requêtes **AJAX** : en-tête `X-CSRF-TOKEN` (depuis `<meta name="csrf-token" content="{{ csrf_token() }}">`) ; Axios lit le cookie `XSRF-TOKEN` automatiquement.

### 9.9 Affichage des erreurs de validation

```blade
@if ($errors->any())
    <ul>
        @foreach ($errors->all() as $error) <li>{{ $error }}</li> @endforeach
    </ul>
@endif

<input name="title" class="@error('title') is-invalid @enderror" value="{{ old('title') }}">
@error('title')
    <div class="alert">{{ $message }}</div>
@enderror

@error('email', 'login') … @enderror                 {{-- sac d'erreurs nommé --}}
```

### 9.10 Composants Blade

Deux types : **basés sur une classe** et **anonymes**.

**Composant à classe**

```bash
php artisan make:component Alert
php artisan make:component Forms/Input
```

```php
// app/View/Components/Alert.php
class Alert extends Component
{
    public function __construct(public string $type = 'info', public string $message = '') {}

    public function render(): View
    {
        return view('components.alert');
    }

    public function isError(): bool { return $this->type === 'error'; }
}
```

```blade
{{-- resources/views/components/alert.blade.php --}}
<div {{ $attributes->merge(['class' => 'alert alert-'.$type]) }}>
    {{ $message }}
    {{ $slot }}
</div>
```

Utilisation :

```blade
<x-alert type="error" :message="$msg" class="mt-4" />
<x-forms.input name="email" />          {{-- sous-dossier : point --}}
```

**Composants anonymes** (un simple fichier Blade dans `resources/views/components`) :

```blade
{{-- resources/views/components/button.blade.php --}}
@props(['type' => 'button', 'color' => 'blue'])
<button type="{{ $type }}" {{ $attributes->class(["bg-$color-500"]) }}>
    {{ $slot }}
</button>
```

**Passage de données**

- Chaînes : `type="error"`.
- Expressions PHP : `:message="$msg"`.
- Raccourci : `:$message`.
- Les attributs **non déclarés** dans le constructeur ou `@props` vont dans `$attributes`.

**Slots**

```blade
<x-card>
    <x-slot:title>Mon titre</x-slot>
    Contenu principal (slot par défaut).
    <x-slot:footer class="x">Pied</x-slot>
</x-card>
```

```blade
{{-- card.blade.php --}}
<h2>{{ $title }}</h2>
{{ $slot }}
@if ($footer->isNotEmpty()) {{ $footer }} @endif
{{ $slot->isEmpty() ? 'Vide' : $slot }}
```

**Manipulation des attributs**

```php
$attributes->merge([/* … */]);
$attributes->class([/* … */]);
$attributes->only(['class']);
$attributes->except(['class']);
$attributes->has('x');
$attributes->whereStartsWith('wire:model');
$attributes->prepends('…');
```

**Autres notions**

- **Composants dynamiques** : `<x-dynamic-component :component="$name" />`.
- **Layouts par composants** (alternative moderne à `@extends`) :

```blade
{{-- components/layout.blade.php --}}
<html><body>{{ $slot }}</body></html>

{{-- page --}}
<x-layout><h1>Hello</h1></x-layout>
```

- **Composants d'index** (`components/card/index.blade.php` → `<x-card>`), composants récursifs.
- **Fournir des données aux composants enfants** : `@aware(['color'])`.

### 9.11 Directives personnalisées

```php
// app/Providers/AppServiceProvider.php, dans boot()
Blade::directive('datetime', function (string $expression) {
    return "<?php echo ($expression)->format('d/m/Y H:i'); ?>";
});
Blade::if('disk', fn (string $value) => config('filesystems.default') === $value);
```

```blade
@datetime($user->created_at)
@disk('local') … @enddisk
```

Après modification d'une directive : `php artisan view:clear`.

### 9.12 Injection de services

```blade
@inject('metrics', 'App\Services\MetricsService')
<div>{{ $metrics->monthlyRevenue() }}</div>
```

### 9.13 Rendu de chaînes Blade

```php
use Illuminate\Support\Facades\Blade;

Blade::render('Hello, {{ $name }}', ['name' => 'Julian']);
```

### 9.14 Frontend moderne avec Blade

- **Vite** : `@vite(['resources/css/app.css', 'resources/js/app.js'])`.
- **Alpine.js** : interactivité légère.
- **Livewire** : composants réactifs en PHP.
- **Inertia** : SPA React / Vue / Svelte.

Voir le chapitre 34.

### 9.15 Bonnes pratiques

- **Pas de logique métier ni de requêtes** dans les vues.
- Préférer les **composants** aux `@include` répétitifs.
- **Toujours échapper** (`{{ }}`) sauf contenu purifié.
- Utiliser `@props` pour **documenter** les composants anonymes.

### 9.16 Pièges fréquents

- **`{!! !!}` sur une donnée utilisateur** : faille XSS.
- **Requêtes Eloquent dans la vue** : provoque du N+1 ; chargez les relations dans le contrôleur.
- **Oublier `view:clear`** après un changement de directive personnalisée : l'ancien rendu est servi.
- **`@section` sans `@endsection`/`@show`** : le contenu n'est pas rendu.
- **Confondre `$attributes->merge()` et `->class()`** : `class()` fusionne conditionnellement les classes CSS.

### Synthèse du chapitre 9

**Blade** compile en PHP : `{{ }}` **échappe**, `{!! !!}` non. Il offre des **directives** de contrôle, la variable **`$loop`**, des **layouts** (`@extends`/`@section` ou composants `<x-layout>`), des **composants** (classe ou anonymes, `@props`, slots, `$attributes`), des **directives personnalisées** et l'**injection** de services. `@csrf`, `@method` et `@error` couvrent formulaires et validation.

---

## 10. Validation

**Objectifs d'apprentissage.** Expliquer pourquoi valider côté serveur ; valider dans un contrôleur, avec `Validator` ou avec un **Form Request** ; personnaliser messages et noms d'attributs ; connaître le catalogue des règles ; valider conditionnellement, des tableaux, des fichiers, des mots de passe ; écrire des règles personnalisées ; gérer la validation pour les API.

### 10.1 Pourquoi valider ?

**Ne jamais faire confiance aux données utilisateur.** La validation garantit l'**intégrité**, la **sécurité** et une bonne **expérience utilisateur** (messages clairs). Laravel valide côté serveur de manière **déclarative**.

### 10.2 Validation dans un contrôleur

```php
public function store(Request $request)
{
    $validated = $request->validate([
        'title' => 'required|unique:posts|max:255',
        'body'  => 'required',
        'email' => ['required', 'email'],
    ]);

    // $validated ne contient que les champs validés
    Post::create($validated);
}
```

**En cas d'échec**

- **Requête web** : redirection vers la page précédente avec les erreurs (`$errors`) et les anciennes valeurs (`old()`), en session.
- **Requête JSON/AJAX** : réponse **422** avec la structure `{ message, errors: { champ: [messages] } }`.

**Arrêt à la première erreur** : règle `bail`.

```php
'title' => 'bail|required|unique:posts|max:255'
```

**Champs imbriqués et tableaux**

```php
'author.name' => 'required',
'tags.*'      => 'string|distinct',
'items.*.qty' => 'integer|min:1',
```

**Sacs d'erreurs nommés** : `$request->validateWithBag('post', [/* … */])`.

### 10.3 Validation manuelle (`Validator`)

```php
$validator = Validator::make($request->all(), $rules, $messages, $attributes);

if ($validator->fails()) {
    return redirect('post/create')->withErrors($validator)->withInput();
}

$validated = $validator->validated();
$validator->safe()->only(['name']);
$validator->after(function ($validator) {
    if ($this->somethingElseIsInvalid()) {
        $validator->errors()->add('field', 'Erreur');
    }
});
$validator->validate();        // lève ValidationException automatiquement
```

### 10.4 Form Requests

Classes dédiées qui encapsulent **autorisation + validation + messages**.

```bash
php artisan make:request StorePostRequest
```

```php
// app/Http/Requests/StorePostRequest.php
class StorePostRequest extends FormRequest
{
    public function authorize(): bool
    {
        return $this->user()->can('create', Post::class);
    }

    public function rules(): array
    {
        return [
            'title' => ['required', 'string', 'max:255'],
            'slug'  => ['required', Rule::unique('posts')->ignore($this->post)],
            'tags'  => ['array', 'max:5'],
        ];
    }

    public function messages(): array
    {
        return ['title.required' => 'Le titre est obligatoire.'];
    }

    public function attributes(): array
    {
        return ['title' => 'titre'];
    }

    protected function prepareForValidation(): void            // avant la validation
    {
        $this->merge(['slug' => Str::slug($this->title)]);
    }

    protected function passedValidation(): void { /* après un succès */ }

    public function after(): array                              // validations supplémentaires
    {
        return [fn (Validator $v) => /* … */];
    }
}
```

```php
public function store(StorePostRequest $request)
{
    $validated = $request->validated();                // toutes les données validées
    $partial   = $request->safe()->only(['title']);
}
```

Si `authorize()` retourne `false` → **403**.

**Propriétés utiles** : `$stopOnFirstFailure`, `$redirect`, `$redirectRoute`, et `failedValidation()` (pour personnaliser la réponse d'échec).

### 10.5 Messages d'erreur

Fichier `lang/fr/validation.php` (à publier avec `php artisan lang:publish`). Personnalisation à la volée :

```php
$messages = [
    'required'       => 'Le champ :attribute est requis.',
    'between'        => 'Le :attribute doit être entre :min et :max.',
    'email.required' => 'Une adresse e-mail est nécessaire.',
];
```

**Substituts** : `:attribute`, `:other`, `:size`, `:min`, `:max`, `:values`, `:date`.

Dans `validation.php`, la section `custom` définit des messages **par champ et par règle**, et `attributes` des **noms lisibles**.

### 10.6 Travailler avec les erreurs

```php
$errors = $validator->errors();
$errors->first('email');
$errors->get('email');
$errors->all();
$errors->has('email');
```

Dans Blade, la variable **`$errors`** est toujours disponible.

### 10.7 Catalogue des règles principales

| Famille | Règles |
| --- | --- |
| **Présence** | `required`, `nullable`, `sometimes`, `filled`, `present`, `missing`, `prohibited`, `required_if:autre,valeur`, `required_unless`, `required_with`, `required_with_all`, `required_without`, `required_without_all`, `required_array_keys`, `exclude_if`, `exclude_unless`, `accepted`, `accepted_if`, `declined` |
| **Types** | `string`, `integer`, `numeric`, `boolean`, `array`, `list`, `json`, `file`, `image`, `date`, `decimal:2`, `alpha`, `alpha_dash`, `alpha_num`, `ascii`, `hex_color`, `lowercase`, `uppercase`, `timezone` |
| **Format** | `email` (`email:rfc,dns`), `url`, `active_url`, `ip`, `ipv4`, `ipv6`, `mac_address`, `uuid`, `ulid`, `regex:/motif/`, `not_regex`, `starts_with`, `ends_with`, `doesnt_start_with`, `date_format:Y-m-d`, `confirmed` |
| **Taille / valeur** | `min`, `max`, `between`, `size`, `digits`, `digits_between`, `min_digits`, `max_digits`, `gt`, `gte`, `lt`, `lte`, `multiple_of` |
| **Comparaison** | `same:champ`, `different:champ`, `confirmed` (champ `xxx_confirmation`), `in:a,b`, `not_in`, `in_array`, `distinct`, `contains` |
| **Dates** | `date`, `date_equals`, `after:today`, `after_or_equal`, `before`, `before_or_equal` |

**Base de données**

```php
'email' => 'unique:users,email_address'
'email' => Rule::unique('users')->ignore($user->id)->where(fn ($q) => $q->where('account_id', 1))
'state' => 'exists:states,abbreviation'
'state' => Rule::exists('states')->where(/* … */)
```

**Fichiers**

```php
'photo'  => 'required|image|mimes:jpg,png|max:2048'            // 2048 Ko
'doc'    => 'file|mimetypes:application/pdf|extensions:pdf'
'avatar' => File::image()->min(10)->max(2048)->dimensions(Rule::dimensions()->maxWidth(1000))
```

**Mots de passe**

```php
Password::min(8)->letters()->mixedCase()->numbers()->symbols()->uncompromised()
```

**Enums et autres** : `Rule::enum(Status::class)`, `Rule::in`, `Rule::notIn`, `Rule::requiredIf(fn)`, `Rule::when($cond, [...])`, `Rule::forEach`, `Rule::anyOf` *(ajout)*, `Rule::dimensions`.

### 10.8 Validation conditionnelle

```php
$validator->sometimes('reason', 'required|max:500', fn ($input) => $input->games >= 100);

'reason' => Rule::when($this->games >= 100, ['required', 'max:500'], ['nullable']),
```

### 10.9 Tableaux et données imbriquées

```php
'photos.profile'      => 'required|image',
'users.*.email'       => 'email|unique:users',
'person.*.first_name' => 'required_with:person.*.last_name',
```

Messages personnalisés : `'users.*.email.unique' => '…'`.

### 10.10 Règles personnalisées

**Objet règle**

```bash
php artisan make:rule Uppercase
```

```php
// app/Rules/Uppercase.php
class Uppercase implements ValidationRule
{
    public function validate(string $attribute, mixed $value, Closure $fail): void
    {
        if (strtoupper($value) !== $value) {
            $fail('Le champ :attribute doit être en majuscules.');
        }
    }
}

'name' => ['required', new Uppercase]
```

**Closure**

```php
'title' => [function (string $attribute, mixed $value, Closure $fail) {
    if ($value === 'foo') $fail("$attribute est invalide.");
}]
```

**Autres variantes**

- **Règle avec accès aux données** : interfaces `DataAwareRule` et `ValidatorAwareRule`.
- **Règles implicites** (exécutées même si le champ est vide) : `make:rule --implicit`.
- **`Validator::extend`** *(héritage)* : ancienne méthode d'extension.

### 10.11 Validation côté client

Laravel valide **côté serveur**. On peut ajouter une validation HTML5/JavaScript pour le confort, **jamais en remplacement**. **Precognition** permet de valider « en direct » en réutilisant les **mêmes règles serveur**.

### 10.12 Validation et API

Les échecs renvoient automatiquement du **JSON 422** si l'en-tête `Accept: application/json` est présent :

```json
{
  "message": "The title field is required.",
  "errors": { "title": ["The title field is required."] }
}
```

### 10.13 Pièges fréquents

- **Utiliser `$request->all()`** après validation : préférez `validated()` ou `safe()`.
- **`unique` à la mise à jour sans `ignore()`** : l'enregistrement se bloque lui-même.
- **Oublier `nullable`** : un champ optionnel vide devient `null` (middleware `ConvertEmptyStringsToNull`) et échoue sur `string`.
- **Valider seulement côté client** : contournable.
- **Règle `max` sur un fichier** : exprimée en **kilo-octets**.
- **Confondre `required_with` et `required_if`**.

### Synthèse du chapitre 10

Validez **toute** entrée côté serveur : `$request->validate()` pour les cas simples, **Form Request** (autorisation + règles + messages) pour le reste, `Validator::make` pour le manuel. Utilisez le **catalogue de règles**, les règles conditionnelles, les tableaux (`items.*`), les **règles personnalisées** et récupérez les données avec **`validated()`**. En API, l'échec donne un **422** structuré.

---

# Partie IV — Base de données, migrations et seeders

## 11. Base de données

**Objectifs d'apprentissage.** Situer les trois niveaux d'accès aux données (SQL brut, Query Builder, Eloquent) ; configurer une ou plusieurs connexions, y compris lecture/écriture séparées ; exécuter du SQL brut en sécurité ; utiliser les transactions et les verrous ; maîtriser le Query Builder (sélection, `where`, tri, jointures, agrégats, écriture) ; paginer ; inspecter le schéma ; appliquer les bonnes pratiques de performance.

### 11.1 Vue d'ensemble

Laravel supporte nativement **MySQL/MariaDB, PostgreSQL, SQLite et SQL Server**. Trois niveaux d'accès :

| Niveau | Outil | Particularité |
| --- | --- | --- |
| 1 | **SQL brut** (`DB::select`, `DB::statement`) | Contrôle total |
| 2 | **Query Builder** | Interface fluide, protégée contre l'injection SQL (requêtes préparées PDO) |
| 3 | **Eloquent ORM** | Modèles objets (chapitres 13 et 14) |

### 11.2 Configuration

Dans `config/database.php` et `.env`. Plusieurs connexions sont possibles :

```php
// config/database.php (extrait)
'default' => env('DB_CONNECTION', 'sqlite'),
'connections' => [
    'mysql' => [/* … */],
    'pgsql' => [/* … */],
    'reporting' => ['driver' => 'mysql', 'host' => env('REPORT_DB_HOST'), /* … */],
],
```

Utiliser une autre connexion : `DB::connection('reporting')->table('…')`.

**Lecture/écriture séparées** (réplication) :

```php
'mysql' => [
    'read'   => ['host' => ['192.168.1.1', '192.168.1.2']],
    'write'  => ['host' => ['196.168.1.3']],
    'sticky' => true,
    // …
],
```

L'option **`sticky`** relit sur la connexion d'**écriture** après une écriture dans la même requête (évite de lire des données périmées sur un réplica en retard).

**URL de connexion** : `DB_URL=mysql://user:pass@host/db`.

### 11.3 SQL brut

```php
use Illuminate\Support\Facades\DB;

$users = DB::select('select * from users where active = ?', [1]);
$users = DB::select('select * from users where id = :id', ['id' => 1]);
DB::insert('insert into users (id, name) values (?, ?)', [1, 'Marc']);
$affected = DB::update('update users set votes = 100 where name = ?', ['Anita']);
$deleted  = DB::delete('delete from users');
DB::statement('drop table users');
DB::unprepared('…');                       // sans préparation (dangereux)
DB::scalar('select count(*) from users');
```

> **Règle absolue.** Utilisez **toujours des liaisons** (`?` ou `:nom`), **jamais** de concaténation de variables dans le SQL : c'est la défense contre l'**injection SQL**.

**Écouter les requêtes** (débogage) :

```php
DB::listen(function ($query) {
    // $query->sql, $query->bindings, $query->time
});
DB::enableQueryLog();
DB::getQueryLog();
```

### 11.4 Transactions

Une **transaction** garantit l'**atomicité** : tout réussit ou rien n'est appliqué.

```php
DB::transaction(function () {
    DB::update('update users set votes = 1');
    DB::delete('delete from posts');
}, attempts: 5);                           // retente en cas d'interblocage (deadlock)

DB::beginTransaction();
DB::rollBack();
DB::commit();
```

- Les transactions **imbriquées** sont gérées par des *savepoints*.
- **Verrous pessimistes** : `->lockForUpdate()` (écriture) et `->sharedLock()` (lecture partagée), à l'**intérieur** d'une transaction.
- Lorsque vous dispatchez des **jobs ou événements** dans une transaction, utilisez `afterCommit()` ou `ShouldDispatchAfterCommit` pour qu'ils ne s'exécutent qu'**après** le `commit`.

### 11.5 Query Builder : récupération

```php
$users  = DB::table('users')->get();                    // Collection d'objets stdClass
$user   = DB::table('users')->where('name', 'John')->first();
$email  = DB::table('users')->where('name', 'John')->value('email');
$user   = DB::table('users')->find(3);
$titles = DB::table('users')->pluck('title');
$titles = DB::table('users')->pluck('title', 'name');   // clé => valeur
```

**Gros volumes**

```php
DB::table('users')->orderBy('id')->chunk(100, function ($users) {
    foreach ($users as $user) { /* … */ }
    // return false pour arrêter
});
DB::table('users')->chunkById(100, fn ($users) => /* … */);   // sûr si l'on modifie les lignes
DB::table('users')->lazy()->each(/* … */);                    // LazyCollection
DB::table('users')->lazyById()->each(/* … */);
DB::table('users')->cursor();                                  // curseur (peu de mémoire)
```

**Agrégats** : `count`, `max`, `min`, `avg`, `sum`, `exists`, `doesntExist`.

### 11.6 Sélection

```php
->select('name', 'email as user_email')
->addSelect('age')
->distinct()
->selectRaw('price * ? as price_with_tax', [1.0825])
```

### 11.7 Clauses `where`

```php
->where('votes', '=', 100)
->where('votes', 100)                       // « = » implicite
->where('votes', '>=', 100)
->where('name', 'like', 'T%')
->where([['status', '1'], ['subscribed', '<>', '1']])
->orWhere('name', 'John')
->whereNot(/* … */)
->whereBetween('votes', [1, 100])
->whereNotBetween(/* … */)
->whereIn('id', [1, 2, 3])
->whereNotIn(/* … */)
->whereNull('updated_at')
->whereNotNull('updated_at')
->whereDate('created_at', '2024-01-01')
->whereMonth('created_at', '12')
->whereDay(/* … */)->whereYear(/* … */)->whereTime(/* … */)
->whereColumn('first_name', 'last_name')
->whereColumn('updated_at', '>', 'created_at')
->whereLike('name', '%john%')
->whereAny(['name', 'email'], 'like', '%x%')
->whereAll([/* … */], /* … */)
->whereNone([/* … */], /* … */)
->whereRaw('price > IF(state = "TX", ?, 100)', [200])
->whereExists(fn ($q) => $q->select(DB::raw(1))->from('orders')->whereColumn('orders.user_id', 'users.id'))
->whereJsonContains('options->languages', 'en')
->whereJsonLength('options->languages', '>', 1)
```

**Regroupement logique** (parenthèses) :

```php
->where('name', '=', 'John')
->where(function ($query) {
    $query->where('votes', '>', 100)->orWhere('title', '=', 'Admin');
})
// WHERE name = 'John' AND (votes > 100 OR title = 'Admin')
```

**Conditions dynamiques** :

```php
->when($role, fn ($query, $role) => $query->where('role_id', $role))
->unless(/* … */)
```

### 11.8 Tri, regroupement, limites

```php
->orderBy('name', 'desc')
->orderByDesc('name')
->latest('created_at')->oldest()
->inRandomOrder()
->reorder()
->groupBy('account_id')
->having('account_id', '>', 100)
->havingRaw(/* … */)
->skip(10)->take(5)                 // décalage / limite
->offset(10)->limit(5)
->forPage($page, $perPage)
```

### 11.9 Jointures, unions, sous-requêtes

```php
DB::table('users')
    ->join('contacts', 'users.id', '=', 'contacts.user_id')
    ->leftJoin('posts', 'users.id', '=', 'posts.user_id')
    ->rightJoin(/* … */)
    ->crossJoin('colors')
    ->select('users.*', 'contacts.phone')
    ->get();

->join('contacts', function (JoinClause $join) {
    $join->on('users.id', '=', 'contacts.user_id')->where('contacts.user_id', '>', 5);
})

->joinSub($latestPosts, 'latest_posts', fn ($join) => $join->on(/* … */))
```

- **Unions** : `$first->union($second)`, `unionAll`.
- **Sous-requêtes** : `->where('id', 'in', fn ($q) => /* … */)`, `->selectSub(/* … */)`, `->fromSub(/* … */)`.

**Expressions brutes** : `DB::raw('count(*) as total')`, `selectRaw`, `whereRaw`, `orderByRaw`, `groupByRaw`, `havingRaw`.

> **Attention.** Une expression brute est insérée **telle quelle** : risque d'injection. Utilisez des **liaisons**.

### 11.10 Insertion, mise à jour, suppression

```php
DB::table('users')->insert(['email' => 'a@b.c', 'votes' => 0]);
DB::table('users')->insert([[/* … */], [/* … */]]);                 // plusieurs lignes
DB::table('users')->insertOrIgnore([/* … */]);
$id = DB::table('users')->insertGetId(['email' => 'a@b.c']);
DB::table('users')->upsert(
    [['name' => 'A', 'dept' => 'X', 'salary' => 100]],
    ['name'],                      // colonnes d'unicité
    ['salary']                     // colonnes à mettre à jour si la ligne existe
);

$n = DB::table('users')->where('id', 1)->update(['votes' => 1]);
DB::table('users')->updateOrInsert(['email' => 'x'], ['name' => 'John']);
DB::table('users')->where('id', 1)->increment('votes');
DB::table('users')->increment('votes', 5, ['name' => 'X']);
DB::table('users')->decrement('votes');
DB::table('users')->where('votes', '>', 100)->delete();
DB::table('users')->truncate();
```

### 11.11 Pagination

```php
$users = DB::table('users')->paginate(15);          // total + liens (requête COUNT en plus)
$users = DB::table('users')->simplePaginate(15);    // Précédent / Suivant (plus rapide)
$users = DB::table('users')->orderBy('id')->cursorPaginate(15);   // par curseur (très gros jeux de données)
```

Dans Blade : `{{ $users->links() }}`. Personnalisation des vues : `php artisan vendor:publish --tag=laravel-pagination`. `->withQueryString()` conserve les paramètres d'URL ; `->appends([/* … */])` en ajoute ; `Paginator::useBootstrapFive()` change le style (Tailwind par défaut).

**Méthodes de l'instance** : `count()`, `currentPage()`, `lastPage()`, `total()`, `perPage()`, `nextPageUrl()`, `items()`, `hasMorePages()`.

### 11.12 Inspection du schéma et de la base

```bash
php artisan db                # ouvre le client en ligne de commande
php artisan db:show           # informations sur la base
php artisan db:table users    # informations sur une table
php artisan db:monitor        # surveille le nombre de connexions
```

```php
Schema::hasTable('users');
Schema::hasColumn('users', 'email');
Schema::getTables();
Schema::getColumns('users');
```

### 11.13 Performances et bonnes pratiques SQL

- Poser des **index** sur les colonnes de `WHERE`, `JOIN` et `ORDER BY`.
- Éviter `select *` : **sélectionner** les colonnes nécessaires.
- Utiliser `chunk` / `lazy` / `cursor` pour les gros volumes.
- Surveiller les requêtes lentes (`DB::listen`, Telescope, Debugbar).
- **Paginer** plutôt que d'appeler `get()` massivement.
- Utiliser des **transactions** pour les opérations multi-tables.

### 11.14 Pièges fréquents

- **Concaténer des variables dans du SQL** : injection ; toujours lier.
- **`chunk()` + modification de la colonne de filtre** : des lignes sont sautées ; utilisez `chunkById`.
- **`get()` sur une grande table** : épuise la mémoire.
- **`whereRaw` avec `orderBy` dynamique non filtré** : faille ; utiliser une liste blanche (chapitre 33).
- **Transaction trop longue** : verrous prolongés, interblocages.
- **Dispatcher un job avant le `commit`** : le job peut ne pas voir les données.

### Synthèse du chapitre 11

Trois niveaux d'accès : **SQL brut**, **Query Builder**, **Eloquent**. Les requêtes sont **préparées** (liaisons). Les **transactions** (`DB::transaction`) garantissent l'atomicité ; les **verrous** protègent les accès concurrents. Le Query Builder couvre sélection, `where`, jointures, agrégats, écriture et **pagination** (`paginate`, `simplePaginate`, `cursorPaginate`). **Indexez**, **paginez**, **traitez par lots**.

---

## 12. Migrations et Seeders

**Objectifs d'apprentissage.** Définir une migration et son cycle (`up`/`down`) ; générer et exécuter des migrations ; créer et modifier des tables, colonnes, index, clés étrangères ; connaître les types et modificateurs de colonnes ; écrire des factories (états, séquences, relations) ; écrire des seeders idempotents.

### 12.1 Migrations : concept

Les **migrations** sont du « contrôle de version » pour le **schéma** de la base : des classes PHP décrivant des changements (création ou modification de tables), **exécutables et réversibles**, partagées par toute l'équipe via Git.

### 12.2 Générer une migration

```bash
php artisan make:migration create_flights_table
php artisan make:migration add_votes_to_users_table --table=users
php artisan make:migration create_posts_table --create=posts
php artisan make:model Flight -m                       # modèle + migration
```

Fichier **horodaté** : `2026_01_15_103000_create_flights_table.php`. Le **nom** sert à deviner l'intention (`create_*`, `add_*_to_*`).

### 12.3 Structure d'une migration

```php
// database/migrations/2026_01_15_103000_create_flights_table.php
return new class extends Migration
{
    public function up(): void
    {
        Schema::create('flights', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('airline');
            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('flights');
    }
};
```

- `up()` **applique** ; `down()` **annule**.
- Connexion spécifique : `protected $connection = 'pgsql';`.
- Migration conditionnelle : méthode `shouldRun()`.

### 12.4 Exécuter les migrations

```bash
php artisan migrate                     # applique les migrations en attente
php artisan migrate --pretend           # affiche le SQL sans l'exécuter
php artisan migrate --force             # production (sans confirmation)
php artisan migrate --isolated          # verrou pour déploiements multi-serveurs
php artisan migrate:status
php artisan migrate:rollback            # annule le dernier lot (batch)
php artisan migrate:rollback --step=3
php artisan migrate:reset               # annule tout
php artisan migrate:refresh             # reset + migrate
php artisan migrate:refresh --seed
php artisan migrate:fresh               # supprime TOUTES les tables puis migre
php artisan migrate:fresh --seed
php artisan schema:dump                 # remplace les anciennes migrations par un dump SQL
php artisan schema:dump --prune
```

La table **`migrations`** enregistre les migrations exécutées et leur **batch** (lot).

### 12.5 Créer et modifier des tables

```php
Schema::create('users', function (Blueprint $table) { /* … */ });
Schema::table('users', function (Blueprint $table) { /* … */ });
Schema::rename('from', 'to');
Schema::drop('users');
Schema::dropIfExists('users');
Schema::connection('sqlite')->create(/* … */);

$table->engine('InnoDB');
$table->charset('utf8mb4');
$table->collation('utf8mb4_unicode_ci');
$table->temporary();
$table->comment('Table des utilisateurs');
```

### 12.6 Types de colonnes (principaux)

| Catégorie | Méthodes |
| --- | --- |
| **Clés** | `id()`, `bigIncrements`, `increments`, `uuid`, `ulid`, `foreignId`, `foreignUuid`, `foreignUlid` |
| **Chaînes** | `string($c, 100)`, `char`, `text`, `mediumText`, `longText`, `tinyText` |
| **Entiers** | `tinyInteger`, `smallInteger`, `mediumInteger`, `integer`, `bigInteger`, `unsigned*` |
| **Décimaux** | `decimal($c, 8, 2)`, `float`, `double` |
| **Booléen** | `boolean` |
| **Dates / heures** | `date`, `dateTime`, `time`, `timestamp`, `year`, `timestamps()`, `timestampsTz`, `softDeletes()`, `softDeletesTz` |
| **Binaires** | `binary`, `blob` |
| **JSON** | `json`, `jsonb` |
| **Énumérations** | `enum('status', ['a', 'b'])`, `set` |
| **Polymorphes** | `morphs('taggable')`, `nullableMorphs`, `uuidMorphs`, `ulidMorphs` |
| **Spéciaux** | `rememberToken()`, `ipAddress`, `macAddress`, `geometry`, `point`, `vector` (pgsql), colonnes calculées (`virtualAs`, `storedAs`) |

### 12.7 Modificateurs de colonnes

```php
$table->string('email')->nullable();
->default('valeur')      ->default(DB::raw('CURRENT_TIMESTAMP'))
->unique()               ->index()               ->primary()
->unsigned()             ->autoIncrement()
->after('colonne')       ->first()
->comment('…')           ->useCurrent()          ->useCurrentOnUpdate()
->charset('utf8mb4')     ->collation('…')
->invisible()            ->storedAs('…')         ->virtualAs('…')
->generatedAs()          ->always()
```

### 12.8 Modifier des colonnes existantes

Depuis Laravel 11, `change()` **redéfinit complètement** la colonne : il faut **répéter tous les modificateurs** à conserver.

```php
Schema::table('users', function (Blueprint $table) {
    $table->string('name', 50)->nullable()->change();
    $table->renameColumn('from', 'to');
    $table->dropColumn('votes');
    $table->dropColumn(['votes', 'avatar']);
    $table->dropSoftDeletes();
    $table->dropTimestamps();
    $table->dropRememberToken();
});
```

### 12.9 Index et clés étrangères

```php
$table->unique('email');
$table->index(['account_id', 'created_at']);
$table->primary(['id', 'parent_id']);
$table->fullText('body');
$table->spatialIndex('location');
$table->index('x', 'nom_index_custom');

$table->dropUnique('users_email_unique');
$table->dropIndex(['state']);
$table->dropPrimary();
$table->dropForeign(['user_id']);
```

**Clés étrangères**

```php
$table->unsignedBigInteger('user_id');
$table->foreign('user_id')->references('id')->on('users');

// Syntaxe concise
$table->foreignId('user_id')->constrained();                  // table « users » déduite
$table->foreignId('user_id')->constrained('utilisateurs');
$table->foreignId('user_id')->nullable()->constrained()->nullOnDelete();
$table->foreignId('user_id')->constrained()->cascadeOnDelete()->cascadeOnUpdate();
->restrictOnDelete()   ->noActionOnDelete()   ->onDelete('cascade')
```

Activer / désactiver les contraintes :

```php
Schema::enableForeignKeyConstraints();
Schema::disableForeignKeyConstraints();
Schema::withoutForeignKeyConstraints(fn () => /* … */);
```

### 12.10 Bonnes pratiques de migrations

- **Ne jamais modifier** une migration déjà déployée ; en créer une nouvelle.
- Toujours écrire un **`down()` cohérent**.
- Séparer migrations de **schéma** et migrations de **données**.
- Sur de **grosses tables en production** : attention au verrouillage ; procédez en plusieurs étapes (ajout nullable → remplissage → contrainte).
- Utiliser le **dump de schéma** (`schema:dump`) pour accélérer les installations.

### 12.11 Model Factories

Les **factories** génèrent des données **factices réalistes** (tests, seeders) grâce à **Faker**.

```bash
php artisan make:factory PostFactory --model=Post
```

```php
// database/factories/PostFactory.php
class PostFactory extends Factory
{
    public function definition(): array
    {
        return [
            'title'   => fake()->sentence(),
            'body'    => fake()->paragraphs(3, true),
            'user_id' => User::factory(),            // crée l'utilisateur associé
            'status'  => 'draft',
        ];
    }

    public function published(): static                // « état » nommé
    {
        return $this->state(fn (array $attributes) => [
            'status' => 'published', 'published_at' => now(),
        ]);
    }

    public function configure(): static
    {
        return $this->afterCreating(fn (Post $post) => /* … */);
    }
}
```

**Utilisation**

```php
Post::factory()->create();
Post::factory()->count(50)->create();
Post::factory(50)->published()->create(['user_id' => 1]);
Post::factory()->make();                                   // sans enregistrer
Post::factory()->raw();                                    // tableau d'attributs
Post::factory()->state(['status' => 'x'])->create();
Post::factory()->sequence(['status' => 'a'], ['status' => 'b'])->count(10)->create();

// Relations
User::factory()->has(Post::factory()->count(3))->create();
User::factory()->hasPosts(3)->create();                    // méthode magique
Post::factory()->for(User::factory()->state(['name' => 'X']))->create();
Post::factory()->forUser(['name' => 'X'])->create();
User::factory()->hasAttached(Role::factory()->count(3), ['active' => true])->create();
Comment::factory()->for($post, 'commentable')->create();   // polymorphe

// Autres
Post::factory()->recycle($users)->create();                // réutilise des modèles existants
```

**Liaison modèle ↔ factory** : trait `HasFactory`, attribut `#[UseFactory(PostFactory::class)]` *(ajout)* ou convention de nommage.

### 12.12 Seeders

Les **seeders** peuplent la base avec des données initiales (rôles, pays, comptes de démonstration).

```bash
php artisan make:seeder UserSeeder
php artisan db:seed
php artisan db:seed --class=UserSeeder
php artisan migrate:fresh --seed
php artisan db:seed --force                # production
```

```php
// database/seeders/DatabaseSeeder.php
class DatabaseSeeder extends Seeder
{
    use WithoutModelEvents;                  // désactive les événements de modèle

    public function run(): void
    {
        $this->call([
            RoleSeeder::class,
            UserSeeder::class,
        ]);

        User::factory(10)->has(Post::factory(5))->create();
    }
}

class RoleSeeder extends Seeder
{
    public function run(): void
    {
        DB::table('roles')->insert([['name' => 'admin'], ['name' => 'user']]);
    }
}
```

- `$this->callOnce()` : exécute une seule fois.
- `$this->callWith(Seeder::class, ['param' => 1])` : passe des paramètres.
- Rendez les seeders **idempotents** (`updateOrCreate`, `upsert`) pour la production : relancés, ils ne dupliquent rien.

### 12.13 Pièges fréquents

- **Modifier une migration déjà appliquée** : les environnements divergent.
- **`change()` sans répéter les modificateurs** : `nullable`, `default`… sont perdus.
- **`migrate:fresh` en production** : **supprime toutes les tables** ; interdisez-le (`DB::prohibitDestructiveCommands`).
- **Clé étrangère avant la table parente** : ordre des migrations (l'horodatage fait foi).
- **Seeder non idempotent** : doublons à chaque exécution.
- **Factory qui crée des relations en cascade** sans le vouloir : utilisez `recycle` ou passez les modèles.

### Synthèse du chapitre 12

Une **migration** (`up`/`down`) décrit un changement de schéma, versionné et réversible (`migrate`, `rollback`, `fresh`, `status`). Maîtrisez types, modificateurs, index et **clés étrangères** (`foreignId()->constrained()`). Les **factories** (états, séquences, relations) fabriquent des données de test ; les **seeders** peuplent la base de façon **idempotente**.

---

# Partie V — Eloquent ORM et relations

## 13. Eloquent ORM

**Objectifs d'apprentissage.** Définir un ORM et le patron Active Record ; créer des modèles et connaître leurs conventions ; lire, créer, modifier et supprimer des données ; maîtriser l'assignation de masse ; suivre l'état d'un modèle ; utiliser casts, accessors et mutators ; contrôler la sérialisation ; écrire des scopes ; appliquer soft deletes, élagage, événements et observers ; activer les protections contre les erreurs de développement.

### 13.1 Concept : l'ORM et le patron Active Record

Un **ORM** (*Object-Relational Mapping*) fait correspondre des **tables** à des **classes** et des **lignes** à des **objets**. **Eloquent** implémente le patron **Active Record** : chaque modèle est lié à une table, et l'objet **sait se lire, s'écrire et se supprimer lui-même**.

|  | **Active Record** (Eloquent) | **Data Mapper** (Doctrine) |
| --- | --- | --- |
| Persistance | Dans l'objet (`$post->save()`) | Dans un gestionnaire séparé |
| Simplicité | Élevée | Plus de cérémonie |
| Pureté du domaine | Couplé à la base | Domaine indépendant |

### 13.2 Créer un modèle

```bash
php artisan make:model Flight
php artisan make:model Flight -m          # + migration
php artisan make:model Flight -f          # + factory
php artisan make:model Flight -s          # + seeder
php artisan make:model Flight -c          # + contrôleur
php artisan make:model Flight -r          # + contrôleur de ressource
php artisan make:model Flight -p          # + policy
php artisan make:model Flight --all       # tout
php artisan make:model Flight -mfsc
php artisan model:show Flight             # inspecte colonnes et relations
```

### 13.3 Conventions

| Aspect | Convention par défaut | Personnalisation |
| --- | --- | --- |
| Nom de table | Pluriel *snake_case* du nom de classe (`Flight` → `flights`, `AirTrafficController` → `air_traffic_controllers`) | `protected $table = 'my_flights';` |
| Clé primaire | `id`, auto-incrémentée, entière | `protected $primaryKey = 'flight_id';` `public $incrementing = false;` `protected $keyType = 'string';` |
| Horodatage | `created_at`, `updated_at` | `public $timestamps = false;` `const CREATED_AT = 'creation_date';` `protected $dateFormat = 'U';` |
| Connexion | Par défaut | `protected $connection = 'sqlite';` |
| Valeurs par défaut | — | `protected $attributes = ['delayed' => false];` |

**UUID / ULID**

```php
use Illuminate\Database\Eloquent\Concerns\HasUuids;
use Illuminate\Database\Eloquent\Concerns\HasUlids;

class Article extends Model { use HasUuids; }     // clé primaire UUID (v7 par défaut depuis Laravel 12)
```

> **Note de version.** Laravel 13 permet de configurer un modèle par des **attributs PHP** (par exemple `#[Table('users', key: 'user_id', keyType: 'string', incrementing: false)]`, `#[Hidden(['password'])]`), en **alternative** aux propriétés de classe. C'est **facultatif et rétrocompatible** : les propriétés (`$table`, `$hidden`…) continuent de fonctionner. Consultez la documentation de votre version pour la liste exacte des attributs.

### 13.4 Lire des données

```php
$flights = Flight::all();
foreach (Flight::where('active', 1)->orderBy('name')->take(10)->get() as $f) { /* … */ }

$flight  = Flight::find(1);
$flights = Flight::find([1, 2, 3]);
$flight  = Flight::first();
$flight  = Flight::where('active', 1)->first();
$flight  = Flight::firstWhere('active', 1);
$flight  = Flight::findOr(1, fn () => /* … */);

Flight::findOrFail(1);                              // ModelNotFoundException → 404
Flight::where('legs', '>', 3)->firstOrFail();

Flight::firstOrCreate(['name' => 'X'], ['delayed' => 1]);    // cherche, sinon crée
Flight::firstOrNew(['name' => 'X']);                          // cherche, sinon instancie sans enregistrer
Flight::updateOrCreate(['departure' => 'Oakland'], ['price' => 99]);
```

Un résultat de `get()` / `all()` est une **`Eloquent\Collection`** (extension de `Collection`) avec des méthodes propres (`modelKeys()`, `load()`, `fresh()`, `contains($model)`, `find($id)`…).

**Gros volumes** : `chunk`, `chunkById`, `lazy`, `lazyById`, `cursor`.

```php
Flight::chunk(200, function (Collection $flights) { /* … */ });
Flight::lazy()->each(fn ($f) => /* … */);
Flight::cursor()->filter(/* … */);
```

**Sous-requêtes**

```php
Destination::addSelect(['last_flight' => Flight::select('name')
    ->whereColumn('destination_id', 'destinations.id')
    ->orderByDesc('arrived_at')->limit(1)
])->get();
```

**Agrégats** : `Flight::count()`, `max`, `sum`, `avg`, `exists()`.

### 13.5 Créer, modifier, supprimer

**Insertion**

```php
$flight = new Flight;
$flight->name = $request->name;
$flight->save();                                      // INSERT

$flight = Flight::create(['name' => 'London to Paris']);    // nécessite $fillable
Flight::insert([/* … */]);                            // sans événements ni horodatage automatique
Flight::upsert([/* … */], ['uniqueBy'], ['updateColumns']);
```

**Mise à jour**

```php
$flight = Flight::find(1);
$flight->name = 'Paris to London';
$flight->save();                                      // UPDATE (si le modèle existe)

$flight->update(['name' => 'X']);
Flight::where('active', 1)->update(['delayed' => 1]);       // en masse (pas d'événements)
$flight->increment('votes');
$flight->decrement('votes', 5);
$flight->touch();                                     // met à jour updated_at
```

**Suppression**

```php
$flight->delete();
Flight::destroy(1);
Flight::destroy([1, 2, 3]);
Flight::where('active', 0)->delete();
Flight::truncate();
```

**Assignation de masse (*mass assignment*).** Elle protège contre l'injection de champs non prévus (`is_admin`, etc.).

```php
protected $fillable = ['name', 'email'];     // liste blanche
protected $guarded  = ['id'];                // liste noire (ou [] pour tout permettre)
Model::unguard();                            // à éviter
```

**Autres opérations**

```php
$flight->replicate()->fill([/* … */])->save();    // cloner
$flight->fresh();                                  // recharge depuis la base (NOUVELLE instance)
$flight->refresh();                                // recharge l'instance courante
$flight->fill([/* … */]);
$flight->push();                                   // enregistre le modèle ET ses relations chargées
```

### 13.6 État du modèle (*dirty* / *changed*)

```php
$user->isDirty();                  // modifié depuis le chargement ?
$user->isDirty('title');
$user->isClean();
$user->wasChanged();               // modifié lors du dernier save() ?
$user->getOriginal('name');
$user->getChanges();
$user->getAttributes();
$user->only([/* … */]);
$user->exists;                     // bool : existe en base
$user->wasRecentlyCreated;
```

### 13.7 Casts d'attributs

Un **cast** convertit automatiquement un attribut entre sa forme stockée et sa forme PHP.

```php
// app/Models/User.php
protected function casts(): array
{
    return [
        'is_admin'     => 'boolean',
        'options'      => 'array',            // JSON ⇄ array
        'meta'         => AsCollection::class,
        'settings'     => AsArrayObject::class,
        'published_at' => 'datetime',
        'birthday'     => 'date:Y-m-d',
        'price'        => 'decimal:2',
        'status'       => StatusEnum::class,  // enum PHP
        'secret'       => 'encrypted',
        'password'     => 'hashed',
    ];
}
```

> **Héritage.** Avant Laravel 11, les casts se déclaraient dans la propriété `protected $casts = [...]`. La propriété reste valide ; la **méthode `casts()`** est la forme actuelle.

**Types** : `array`, `boolean`, `collection`, `date`, `datetime`, `immutable_date`, `immutable_datetime`, `decimal:n`, `double`, `encrypted`, `encrypted:array`, `float`, `hashed`, `integer`, `object`, `real`, `string`, `timestamp`, classes d'enum.

**Cast personnalisé**

```php
// app/Casts/Json.php
class Json implements CastsAttributes
{
    public function get(Model $model, string $key, mixed $value, array $attributes): array
    {
        return json_decode($value, true);
    }

    public function set(Model $model, string $key, mixed $value, array $attributes): string
    {
        return json_encode($value);
    }
}
```

Il existe aussi les **casts d'objets-valeurs** (par exemple un objet `Address` composé de plusieurs colonnes), `CastsInboundAttributes` (écriture seule) et `Castable`.

### 13.8 Accessors et mutators

```php
use Illuminate\Database\Eloquent\Casts\Attribute;

protected function firstName(): Attribute
{
    return Attribute::make(
        get: fn (string $value) => ucfirst($value),        // accessor : à la lecture
        set: fn (string $value) => strtolower($value),     // mutator : à l'écriture
    );
}

// Accessor calculé à partir de plusieurs attributs
protected function fullName(): Attribute
{
    return Attribute::make(
        get: fn (mixed $value, array $attributes) => $attributes['first_name'].' '.$attributes['last_name'],
    )->shouldCache();
}
```

Utilisation : `$user->first_name`, `$user->full_name`. Pour **inclure** un accessor dans le JSON ou le tableau : `protected $appends = ['full_name'];`.

### 13.9 Sérialisation

```php
$user->toArray();
$user->toJson(JSON_PRETTY_PRINT);
return $user;                                // JSON automatique

protected $hidden  = ['password', 'remember_token'];     // jamais sérialisés
protected $visible = ['first_name'];                      // seuls ceux-là le sont
$user->makeVisible('password')->toArray();
$user->makeHidden('x');
$user->append('full_name');
$user->setVisible([/* … */]);
// format de date : méthode serializeDate()
```

### 13.10 Scopes

**Scope global** (appliqué à **toutes** les requêtes du modèle) :

```php
// app/Models/Scopes/AncientScope.php
class AncientScope implements Scope
{
    public function apply(Builder $builder, Model $model): void
    {
        $builder->where('created_at', '<', now()->subYears(2000));
    }
}

// Dans le modèle
#[ScopedBy([AncientScope::class])]                  // attribut
class User extends Model { }

// ou dans booted()
protected static function booted(): void
{
    static::addGlobalScope(new AncientScope);
    static::addGlobalScope('ancient', fn (Builder $b) => $b->where(/* … */));
}

User::withoutGlobalScope(AncientScope::class)->get();
User::withoutGlobalScopes()->get();
```

**Scope local** (réutilisable **à la demande**) :

```php
#[Scope]                                              // attribut (Laravel 12+)
protected function popular(Builder $query): void { $query->where('votes', '>', 100); }

// Ancienne syntaxe (toujours valable)
public function scopePopular(Builder $query): void { /* … */ }
public function scopeOfType(Builder $query, string $type): void { $query->where('type', $type); }

User::popular()->ofType('admin')->orderBy('created_at')->get();
User::popular()->orWhere->active()->get();            // regroupement logique
```

### 13.11 Comparer des modèles

```php
if ($post->is($anotherPost)) { /* même clé, même table, même connexion */ }
if ($post->isNot($anotherPost)) { /* … */ }
```

### 13.12 Soft Deletes (suppression douce)

La ligne n'est **pas supprimée** : la colonne `deleted_at` est renseignée.

```php
// Migration : $table->softDeletes();
use Illuminate\Database\Eloquent\SoftDeletes;

class Flight extends Model { use SoftDeletes; }

$flight->delete();                 // suppression douce
$flight->trashed();                // bool
$flight->restore();
$flight->forceDelete();            // suppression réelle
Flight::withTrashed()->get();
Flight::onlyTrashed()->get();
Flight::onlyTrashed()->restore();
Flight::withoutTrashed();
$flight->history()->withTrashed()->get();     // relation incluant les supprimés
```

### 13.13 Élagage de modèles (*pruning*)

```php
use Illuminate\Database\Eloquent\Prunable;      // ou MassPrunable

public function prunable(): Builder
{
    return static::where('created_at', '<=', now()->subMonth());
}

protected function pruning(): void { /* nettoyage avant suppression */ }
```

```bash
php artisan model:prune
```

À **planifier** avec le scheduler (chapitre 23).

### 13.14 Événements de modèle

Cycle de vie : `retrieved`, `creating`, `created`, `updating`, `updated`, `saving`, `saved`, `deleting`, `deleted`, `trashed`, `forceDeleting`, `forceDeleted`, `restoring`, `restored`, `replicating`.

```php
// Mapper vers des classes d'événements
protected $dispatchesEvents = ['saved' => UserSaved::class, 'deleted' => UserDeleted::class];

// Closures
protected static function booted(): void
{
    static::creating(function (User $user) { $user->uuid = Str::uuid(); });
}
```

**Observers**

```bash
php artisan make:observer UserObserver --model=User
```

```php
// app/Models/User.php
#[ObservedBy([UserObserver::class])]
class User extends Model { }

// app/Observers/UserObserver.php
class UserObserver
{
    public function created(User $user): void { /* … */ }
    public function updated(User $user): void { /* … */ }
    public function deleted(User $user): void { /* … */ }
}
```

Pour dispatcher **après commit** : l'observer implémente `ShouldHandleEventsAfterCommit`.

**Mise en sourdine**

```php
User::withoutEvents(fn () => /* … */);
$user->saveQuietly();
```

> **Rappel.** Les opérations **en masse** (`update`, `delete` via le builder) ne déclenchent **pas** les événements de modèle.

### 13.15 JSON et attributs spéciaux

```php
User::where('preferences->dining->meal', 'salad')->get();
User::whereJsonContains('options->languages', 'en')->get();
$user->update(['options->enabled' => true]);
```

### 13.16 Agrégats sur relations

Voir le chapitre 14 (`withCount`, `withSum`, `whereHas`…).

### 13.17 Protection contre les erreurs de développement

À placer dans `AppServiceProvider::boot()` :

```php
Model::shouldBeStrict(! app()->isProduction());
// = preventLazyLoading + preventSilentlyDiscardingAttributes + preventAccessingMissingAttributes

Model::preventLazyLoading(! app()->isProduction());       // exception en cas de N+1
Model::preventSilentlyDiscardingAttributes();             // exception si champ non « fillable »
Model::preventAccessingMissingAttributes();               // exception si attribut absent
Relation::enforceMorphMap([/* … */]);
```

### 13.18 Collections Eloquent

Méthodes **en plus** de `Collection` : `contains($model)`, `diff`, `except`, `find`, `fresh`, `intersect`, `load`, `loadMissing`, `modelKeys`, `makeVisible`, `makeHidden`, `only`, `setVisible`, `append`, `unique`, `toQuery`.

```php
$users->each->delete();
$users->load('posts');
```

### 13.19 Bonnes pratiques

- Définir **`$fillable`** explicitement.
- **Typer** avec `casts`.
- Activer **`shouldBeStrict`** hors production pour détecter le N+1.
- Mettre les requêtes réutilisables dans des **scopes**.
- Éviter la logique lourde dans les observers (préférer événements et jobs explicites).
- **Sélectionner** uniquement les colonnes nécessaires pour les gros volumes.

### 13.20 Pièges fréquents

- **`$guarded = []` + `$request->all()`** : n'importe quel champ peut être écrit (`is_admin`).
- **`update()` en masse et événements** : observers et événements ne se déclenchent pas.
- **`fresh()` vs `refresh()`** : `fresh()` renvoie une **nouvelle** instance, `refresh()` modifie l'**actuelle**.
- **Accessor non listé dans `$appends`** : absent du JSON.
- **`find()` renvoie `null`** : utilisez `findOrFail()` pour obtenir un 404.
- **Soft deletes et `unique`** : une ligne « supprimée » bloque encore la contrainte d'unicité en base.

### Synthèse du chapitre 13

**Eloquent** (Active Record) lie **modèle ↔ table** par convention. Lisez (`find`, `first`, `chunk`…), écrivez (`create`, `update`, `delete`) en maîtrisant l'**assignation de masse** (`$fillable`). Utilisez **casts**, **accessors/mutators**, **scopes**, **soft deletes**, **événements/observers**, et activez **`shouldBeStrict`** hors production.

---

## 14. Relations Eloquent

**Objectifs d'apprentissage.** Définir les relations comme méthodes de modèle ; distinguer propriété dynamique et méthode ; implémenter les relations un-à-un, un-à-plusieurs, plusieurs-à-plusieurs, « through » et polymorphes ; manipuler les tables pivot ; interroger les relations (existence, agrégats) ; **éliminer le problème N+1** par l'eager loading ; insérer et modifier via les relations.

### 14.1 Principe

Les relations traduisent les liens entre tables en **méthodes de modèle**. Chaque méthode retourne un objet relation (qui est aussi un Query Builder). On y accède :

- **comme propriété dynamique** : `$user->posts` → exécute la requête et retourne le résultat (*lazy loading*, mis en cache sur l'instance) ;
- **comme méthode** : `$user->posts()` → renvoie la relation pour **ajouter des contraintes**.

### 14.2 Un-à-un : `hasOne` / `belongsTo`

Un utilisateur a un téléphone.

```php
// app/Models/User.php
public function phone(): HasOne
{
    return $this->hasOne(Phone::class);       // clés personnalisées : hasOne(Phone::class, 'foreign_key', 'local_key')
}

// app/Models/Phone.php
public function user(): BelongsTo
{
    return $this->belongsTo(User::class);
}

$phone = User::find(1)->phone;
```

La clé étrangère déduite est `user_id` dans la table `phones`.

**`ofMany`** : un-à-un dérivé d'un `hasMany`

```php
public function latestOrder(): HasOne  { return $this->hasOne(Order::class)->latestOfMany(); }
public function oldestOrder(): HasOne  { return $this->hasOne(Order::class)->oldestOfMany(); }
public function largestOrder(): HasOne { return $this->hasOne(Order::class)->ofMany('price', 'max'); }
```

### 14.3 Un-à-plusieurs : `hasMany` / `belongsTo`

```php
// app/Models/Post.php
public function comments(): HasMany { return $this->hasMany(Comment::class); }

// app/Models/Comment.php
public function post(): BelongsTo { return $this->belongsTo(Post::class); }

foreach ($post->comments as $comment) { /* … */ }
$comment = $post->comments()->where('title', 'x')->first();
```

**`belongsTo` avec modèle par défaut** (évite les `null`) :

```php
return $this->belongsTo(User::class)->withDefault(['name' => 'Invité']);
```

**`hasOneThrough` / `hasManyThrough`** : via un modèle **intermédiaire** (`Country → User → Post`).

```php
public function posts(): HasManyThrough
{
    return $this->hasManyThrough(Post::class, User::class);
}
```

Syntaxe fluide : `$country->through('users')->has('posts')`.

### 14.4 Plusieurs-à-plusieurs : `belongsToMany`

Tables : `users`, `roles` et **`role_user`** (table **pivot** : noms au singulier, ordre alphabétique).

```php
// app/Models/User.php
public function roles(): BelongsToMany
{
    return $this->belongsToMany(Role::class)
        ->withPivot('assigned_at', 'note')      // colonnes supplémentaires du pivot
        ->withTimestamps()
        ->as('subscription')                    // renomme la propriété « pivot »
        ->using(RoleUser::class);               // modèle pivot personnalisé
}

// app/Models/Role.php
public function users(): BelongsToMany { return $this->belongsToMany(User::class); }

foreach ($user->roles as $role) { echo $role->pivot->created_at; }
```

**Filtrer via le pivot** : `wherePivot('active', 1)`, `wherePivotIn`, `wherePivotNull`, `orderByPivot`.

**Manipuler l'association**

```php
$user->roles()->attach($roleId);
$user->roles()->attach($roleId, ['expires_at' => $date]);
$user->roles()->attach([1 => ['expires' => $a], 2 => ['expires' => $b]]);
$user->roles()->detach($roleId);
$user->roles()->detach();                           // tout
$user->roles()->sync([1, 2, 3]);                    // fait correspondre EXACTEMENT
$user->roles()->sync([1 => ['expires' => true], 2]);
$user->roles()->syncWithoutDetaching([1, 2]);       // ajoute sans retirer
$user->roles()->syncWithPivotValues([1, 2], ['active' => true]);
$user->roles()->toggle([1, 2, 3]);
$user->roles()->updateExistingPivot($roleId, ['active' => false]);
```

**Modèle pivot personnalisé** : étend `Pivot` (ou `MorphPivot`), avec `$incrementing = true` si l'identifiant est auto-incrémenté.

### 14.5 Relations polymorphes

Un modèle appartient à **plusieurs types** de modèles via **une seule** association.

**Un-à-un / un-à-plusieurs polymorphe** — exemple : `Comment` sur `Post` **ou** `Video`.

```php
// Migration : $table->morphs('commentable');    // commentable_id + commentable_type

// app/Models/Comment.php
public function commentable(): MorphTo { return $this->morphTo(); }

// app/Models/Post.php  et  app/Models/Video.php
public function comments(): MorphMany { return $this->morphMany(Comment::class, 'commentable'); }

$comment->commentable;           // retourne un Post ou une Video
```

Variantes : `morphOne`, `morphOne … ofMany` (`latestOfMany`).

**Plusieurs-à-plusieurs polymorphe** — exemple : `Tag` pour `Post` et `Video`.

```php
// Tables : posts, videos, tags, taggables (tag_id, taggable_id, taggable_type)

// app/Models/Post.php
public function tags(): MorphToMany { return $this->morphToMany(Tag::class, 'taggable'); }

// app/Models/Tag.php
public function posts(): MorphToMany  { return $this->morphedByMany(Post::class, 'taggable'); }
public function videos(): MorphToMany { return $this->morphedByMany(Video::class, 'taggable'); }
```

**Morph map** (évite de stocker le nom complet des classes en base) :

```php
Relation::enforceMorphMap(['post' => Post::class, 'video' => Video::class]);
```

**Types dynamiques** : `morphTo` avec `morphWith`, `morphWithCount`, `whereHasMorph`.

**Relations dynamiques** :

```php
Order::resolveRelationUsing('customer', fn ($order) => $order->belongsTo(Customer::class));
```

### 14.6 Interroger les relations

**Contraintes**

```php
$user->posts()->where('active', 1)->get();
$user->posts()->where('active', 1)->orWhere('votes', '>=', 100)->get();    // attention aux OR
$user->posts()->where(fn ($q) => $q->where(/* … */)->orWhere(/* … */))->get();   // groupé
```

**Existence**

```php
Post::has('comments')->get();                           // au moins un commentaire
Post::has('comments', '>=', 3)->get();
Post::has('comments.votes')->get();                     // imbriqué
Post::doesntHave('comments')->get();
Post::whereHas('comments', fn ($q) => $q->where('content', 'like', 'code%'))->get();
Post::whereHas('comments', fn ($q) => /* … */, '>=', 10)->get();
Post::whereDoesntHave('comments', fn ($q) => /* … */)->get();
Post::withWhereHas('comments', fn ($q) => /* … */)->get();      // filtre + eager load
Post::whereRelation('comments', 'is_approved', false)->get();
Post::whereBelongsTo($user)->get();
Post::orWhereHas(/* … */);
Comment::whereMorphRelation('commentable', [Post::class, Video::class], 'title', 'like', 'code%');
```

**Agrégats**

```php
Post::withCount('comments')->get();                     // propriété comments_count
Post::withCount(['votes', 'comments as pending' => fn ($q) => $q->where('approved', false)])->get();
Post::withSum('comments', 'votes')->get();              // comments_sum_votes
Post::withMin(/* … */); Post::withMax(/* … */); Post::withAvg(/* … */); Post::withExists('comments');
$post->loadCount('comments');
```

### 14.7 Eager loading : le problème N+1

**Problème.** `Book::all()` puis `$book->author` dans une boucle = **1 + N requêtes**.

**Solution : charger les relations à l'avance**

```php
$books = Book::with('author')->get();                   // 2 requêtes au total
Book::with(['author', 'publisher'])->get();
Book::with('author.contacts')->get();                   // imbriqué
Book::with(['author:id,name', 'publisher:id,name'])->get();    // colonnes précises (inclure la clé !)
Book::with(['comments' => fn ($q) => $q->where('approved', 1)->orderBy('created_at')])->get();
```

**Chargement par défaut** : `protected $with = ['author'];` ; désactivé par `->without('author')` / `->withOnly('genre')`.

**Chargement tardif ciblé**

```php
$books->load('author');
$book->loadMissing('author');
$book->loadMorph('commentable', [Post::class => ['author']]);
```

**Prévention globale**

```php
Model::preventLazyLoading(! app()->isProduction());       // exception en cas de lazy loading
Model::automaticallyEagerLoadRelationships();             // eager loading automatique (Laravel 12+)
```

### 14.8 Insérer et modifier via les relations

```php
// hasOne / hasMany
$comment = new Comment(['message' => 'Super']);
$post->comments()->save($comment);
$post->comments()->saveMany([/* … */]);
$post->comments()->create(['message' => 'Texte']);
$post->comments()->createMany([/* … */]);

// belongsTo
$comment->post()->associate($post);        // puis save()
$comment->post()->dissociate();

// Mise à jour en cascade des horodatages du parent
class Comment extends Model { protected $touches = ['post']; }
```

### 14.9 Sérialisation et relations

Les relations **chargées** sont incluses dans `toArray()` / `toJson()` ; masquez-les par `$hidden` ou `makeHidden`.

### 14.10 Relations « has many » avancées

```php
public function latestPost(): HasOne { return $this->hasOne(Post::class)->latestOfMany(); }
$this->hasMany(Post::class)->chaperone();         // relation inverse automatique (Laravel 11.x et suivantes)
```

### 14.11 Tableau récapitulatif

| Besoin | Relation | Exemple |
| --- | --- | --- |
| 1–1 | `hasOne` / `belongsTo` | Utilisateur–Profil |
| 1–N | `hasMany` / `belongsTo` | Article–Commentaires |
| N–N | `belongsToMany` | Utilisateurs–Rôles |
| 1–1 indirect | `hasOneThrough` | Mécanicien–Propriétaire via Voiture |
| 1–N indirect | `hasManyThrough` | Pays–Articles via Utilisateurs |
| 1–1 / 1–N polymorphe | `morphOne` / `morphMany` / `morphTo` | Commentaires sur Posts ou Vidéos |
| N–N polymorphe | `morphToMany` / `morphedByMany` | Tags sur Posts ou Vidéos |

### 14.12 Bonnes pratiques

- **Typer les retours** des méthodes de relation.
- **Eager load systématiquement** dans les listes.
- Contraindre les relations dans la méthode (`->orderBy('created_at')`) pour définir des **sous-vues nommées** (`recentComments()`).
- Définir `onDelete` en base (cascade / null) **cohérent** avec la logique applicative.
- **Indexer** les clés étrangères.

### 14.13 Pièges fréquents

- **Boucle sur `$post->comments` sans `with()`** : N+1.
- **`orWhere` dans une relation** : sans regroupement, il sort du périmètre de la relation.
- **`with('author:name')`** sans la clé : la relation ne se rattache plus (incluez `id`).
- **`sync()` au lieu de `syncWithoutDetaching()`** : supprime les associations absentes de la liste.
- **Stocker le nom complet de classe** dans une colonne polymorphe : fragile au renommage ; utilisez un *morph map*.
- **Confondre `has()` et `whereHas()`** : le second permet de filtrer sur la relation.

### Synthèse du chapitre 14

Les relations (`hasOne`, `hasMany`, `belongsTo`, `belongsToMany`, `…Through`, `morph…`) sont des **méthodes de modèle**. Interrogez-les (`has`, `whereHas`, `withCount`…), manipulez-les (`attach`, `sync`, `associate`, `create`) et surtout **chargez-les à l'avance** (`with`) pour éviter le **N+1**, en activant `preventLazyLoading` hors production.

---

# Partie VI — Authentification, autorisation et architecture interne

## 15. Authentification

**Objectifs d'apprentissage.** Distinguer authentification et autorisation ; comprendre *guards* et *user providers* ; choisir une solution (starter kits, Fortify, Sanctum, Passport, Socialite) ; authentifier manuellement ; protéger les routes ; gérer « se souvenir de moi », confirmation de mot de passe, vérification d'e-mail, réinitialisation ; hasher les mots de passe ; configurer plusieurs guards ; utiliser Sanctum (jetons et SPA) ; sécuriser le dispositif.

### 15.1 Concepts fondamentaux

- **Authentification** : prouver **qui** on est (identifiant/mot de passe, jeton, OAuth…).
- **Autorisation** : déterminer **ce qu'on a le droit de faire** (chapitre 16).

Laravel repose sur deux notions :

| Notion | Rôle |
| --- | --- |
| **Guard** | *Comment* l'utilisateur est authentifié à chaque requête (`session` : via cookie de session ; `sanctum` / jeton : via un jeton) |
| **User Provider** | *Comment* l'utilisateur est récupéré depuis le stockage (`eloquent`, `database`) |

```php
// config/auth.php (extrait)
'defaults'  => ['guard' => 'web', 'passwords' => 'users'],
'guards'    => ['web' => ['driver' => 'session', 'provider' => 'users']],
'providers' => ['users' => ['driver' => 'eloquent', 'model' => App\Models\User::class]],
'passwords' => [
    'users' => ['provider' => 'users', 'table' => 'password_reset_tokens', 'expire' => 60, 'throttle' => 60],
],
'password_timeout' => 10800,
```

### 15.2 Choisir une solution

| Besoin | Solution |
| --- | --- |
| Application web classique, démarrage rapide | **Starter kits** officiels (React, Vue, Livewire) *(à jour)* |
| Kits historiques | **Breeze**, **Jetstream** *(héritage)* : Jetstream apporte 2FA, équipes, jetons d'API |
| Backend d'authentification **sans interface** | **Fortify** |
| SPA / mobile / jetons d'API simples | **Sanctum** |
| Serveur **OAuth2** complet | **Passport** |
| Connexion Google / GitHub / Facebook… | **Socialite** (consommer OAuth) |

### 15.3 Le modèle `User`

```php
// app/Models/User.php
class User extends Authenticatable          // implémente Illuminate\Contracts\Auth\Authenticatable
{
    use HasFactory, Notifiable;

    protected $fillable = ['name', 'email', 'password'];
    protected $hidden   = ['password', 'remember_token'];

    protected function casts(): array
    {
        return ['email_verified_at' => 'datetime', 'password' => 'hashed'];
    }
}
```

Le cast **`hashed`** hashe automatiquement le mot de passe à l'affectation.

### 15.4 Authentification manuelle

```php
// app/Http/Controllers/LoginController.php
use Illuminate\Support\Facades\Auth;

public function authenticate(Request $request): RedirectResponse
{
    $credentials = $request->validate([
        'email'    => ['required', 'email'],
        'password' => ['required'],
    ]);

    if (Auth::attempt($credentials, $request->boolean('remember'))) {
        $request->session()->regenerate();            // protège contre la fixation de session
        return redirect()->intended('dashboard');
    }

    return back()->withErrors(['email' => 'Identifiants invalides.'])->onlyInput('email');
}

public function logout(Request $request): RedirectResponse
{
    Auth::logout();
    $request->session()->invalidate();
    $request->session()->regenerateToken();
    return redirect('/');
}
```

**Variantes**

```php
Auth::attempt(['email' => $e, 'password' => $p, 'active' => 1]);               // conditions supplémentaires
Auth::attempt(['email' => $e, 'password' => $p, fn ($q) => $q->has('activeSubscription')]);
Auth::guard('admin')->attempt($credentials);
Auth::login($user, $remember = true);
Auth::loginUsingId(1);
Auth::once($credentials);                  // pour une requête, sans session
Auth::onceUsingId(1);
Auth::logoutOtherDevices($password);
Auth::viaRemember();
Auth::validate($credentials);              // vérifie sans connecter
```

### 15.5 Récupérer l'utilisateur

```php
$user = Auth::user();                       // ou auth()->user() ou $request->user()
$id   = Auth::id();
Auth::check();                              // connecté ?
Auth::guest();
```

### 15.6 Protéger les routes

```php
Route::get('/dashboard', /* … */)->middleware('auth');
Route::get('/admin', /* … */)->middleware('auth:admin');      // guard spécifique
Route::get('/login', /* … */)->middleware('guest');
```

**Redirections** à personnaliser dans `bootstrap/app.php` :

```php
$middleware->redirectGuestsTo('/login');
$middleware->redirectUsersTo('/dashboard');
```

### 15.7 « Se souvenir de moi » (*remember me*)

Colonne `remember_token` ; `Auth::attempt($credentials, true)`. Un cookie de longue durée est alors émis.

### 15.8 Confirmation de mot de passe

Le middleware **`password.confirm`** protège les zones sensibles ; la durée de validité est réglée par `password_timeout`.

### 15.9 Vérification d'e-mail

```php
class User extends Authenticatable implements MustVerifyEmail { /* … */ }

Route::get('/profile', /* … */)->middleware(['auth', 'verified']);
```

Routes requises : avis de vérification, traitement du **lien signé** (`EmailVerificationRequest`), renvoi du mail. Les starter kits les fournissent. L'événement `Registered` déclenche l'envoi.

### 15.10 Réinitialisation de mot de passe

Flux : formulaire « mot de passe oublié » → `Password::sendResetLink()` → e-mail avec jeton → formulaire → `Password::reset()`.

```php
$status = Password::sendResetLink($request->only('email'));

$status = Password::reset(
    $request->only('email', 'password', 'password_confirmation', 'token'),
    function (User $user, string $password) {
        $user->forceFill(['password' => $password])->setRememberToken(Str::random(60));
        $user->save();
        event(new PasswordReset($user));
    }
);
```

Table : `password_reset_tokens`. Nettoyage : `php artisan auth:clear-resets`.

### 15.11 Hashage des mots de passe

```php
use Illuminate\Support\Facades\Hash;

$hashed = Hash::make('mot-de-passe');          // Bcrypt par défaut (coût réglable)
Hash::check('mot-de-passe', $hashed);
Hash::needsRehash($hashed);
```

Algorithmes : **Bcrypt** (défaut), **Argon2i / Argon2id**. Configuration : `config/hashing.php` (`BCRYPT_ROUNDS`). **Ne jamais** stocker un mot de passe en clair ; ne pas utiliser MD5 ou SHA1.

### 15.12 Multi-guards et multi-providers

Exemple : un guard `admin` avec un modèle `Admin` distinct.

```php
// config/auth.php
'guards' => [
    'web'   => ['driver' => 'session', 'provider' => 'users'],
    'admin' => ['driver' => 'session', 'provider' => 'admins'],
],
'providers' => [
    'users'  => ['driver' => 'eloquent', 'model' => User::class],
    'admins' => ['driver' => 'eloquent', 'model' => Admin::class],
],
```

**Guards personnalisés** : `Auth::extend('jwt', fn ($app, $name, $config) => new JwtGuard(/* … */))`. **Request guard** : `Auth::viaRequest('custom', fn (Request $r) => /* … */)`.

### 15.13 HTTP Basic Auth

`->middleware('auth.basic')` ; version sans état : `Auth::onceBasic()`.

### 15.14 Événements d'authentification

`Registered`, `Attempting`, `Authenticated`, `Login`, `Failed`, `Validated`, `Logout`, `CurrentDeviceLogout`, `OtherDeviceLogout`, `Lockout`, `PasswordReset`, `Verified`. Ils permettent de journaliser, notifier, etc.

### 15.15 Laravel Sanctum

Deux usages :

**1. Jetons d'API personnels**

```php
// Modèle : use Laravel\Sanctum\HasApiTokens;
$token = $user->createToken('mobile', ['read', 'write'])->plainTextToken;
// Le client envoie : Authorization: Bearer <jeton>

Route::middleware('auth:sanctum')->get('/user', fn (Request $r) => $r->user());

$request->user()->tokenCan('write');
$user->tokens()->delete();
$request->user()->currentAccessToken()->delete();
```

Middleware `abilities:read,write` / `ability:…`. Expiration configurable (`config/sanctum.php`).

**2. Authentification de SPA** (cookie/session + protection CSRF) : le front et l'API partagent un **domaine de premier niveau** ; appelez `/sanctum/csrf-cookie` avant la connexion.

### 15.16 Laravel Passport et Socialite

- **Passport** : serveur **OAuth2** (Authorization Code + PKCE, Client Credentials, etc.), jetons JWT.
- **Socialite** :

```php
Route::get('/auth/redirect', fn () => Socialite::driver('github')->redirect());

Route::get('/auth/callback', function () {
    $githubUser = Socialite::driver('github')->user();
    $user = User::updateOrCreate(['github_id' => $githubUser->id], [
        'name' => $githubUser->name, 'email' => $githubUser->email,
    ]);
    Auth::login($user);
    return redirect('/dashboard');
});
```

### 15.17 Double facteur (2FA) et passkeys

Jetstream et Fortify proposent la **2FA TOTP** (avec codes de récupération). Les **passkeys** (WebAuthn) sont gérées par des packages ou des kits récents.

### 15.18 Sécurité de l'authentification

- **Limiter** les tentatives de connexion (`RateLimiter`, événement `Lockout`).
- **Régénérer** la session à la connexion et à la déconnexion.
- **HTTPS** et cookies `Secure` / `HttpOnly` / `SameSite`.
- Valider la **force** des mots de passe (`Password::defaults()`), vérifier les fuites (`uncompromised`).

### 15.19 Pièges fréquents

- **Oublier `session()->regenerate()`** après `attempt()` : fixation de session.
- **Stocker le mot de passe en clair** ou le hasher deux fois (cast `hashed` + `Hash::make`).
- **`Auth::user()` sans vérifier `null`** hors des routes protégées.
- **Mélanger guards** : `auth:sanctum` ≠ `auth` (session) ; vérifier lequel protège la route.
- **Jetons Sanctum sans capacités** : un jeton sans restriction peut tout faire.
- **Pas de limitation de débit** sur la connexion : force brute.

### Synthèse du chapitre 15

Un **guard** décide *comment* on authentifie, un **provider** *où* l'on retrouve l'utilisateur. Utilisez un **starter kit** pour démarrer, **Sanctum** pour SPA et jetons d'API, **Passport** pour OAuth2, **Socialite** pour la connexion sociale. Hashez (`Hash`, cast `hashed`), régénérez la session, limitez les tentatives, vérifiez l'e-mail et activez la 2FA.

---

## 16. Autorisation

**Objectifs d'apprentissage.** Distinguer Gates et Policies ; définir et utiliser une Gate ; écrire une Policy complète ; autoriser dans contrôleurs, middleware, Blade et Form Requests ; gérer les réponses personnalisées et les hooks `before`/`after` ; modéliser rôles et permissions ; autoriser côté API ; tester les autorisations.

### 16.1 Principe

L'**autorisation** décide si un utilisateur **authentifié** peut effectuer une action. Deux mécanismes :

| Mécanisme | Nature | Usage |
| --- | --- | --- |
| **Gate** | Closure, globale | Actions non liées à un modèle précis |
| **Policy** | Classe liée à un modèle | CRUD d'une ressource |

### 16.2 Gates

Définies dans `AppServiceProvider::boot()` :

```php
use Illuminate\Support\Facades\Gate;

Gate::define('update-post', function (User $user, Post $post) {
    return $user->id === $post->user_id;
});
Gate::define('update-post', [PostPolicy::class, 'update']);     // via une méthode de classe
```

**Utilisation**

```php
if (Gate::allows('update-post', $post)) { /* … */ }
if (Gate::denies('update-post', $post)) { abort(403); }
Gate::allows('create-post');                      // sans argument
Gate::any(['update-post', 'delete-post'], $post);
Gate::none([/* … */], $post);
Gate::authorize('update-post', $post);            // lève AuthorizationException → 403
Gate::forUser($user)->allows('update-post', $post);
Gate::inspect('update-post', $post);              // réponse détaillée
```

**Réponses personnalisées**

```php
Gate::define('edit-settings', fn (User $user) => $user->isAdmin
    ? Response::allow()
    : Response::deny('Réservé aux administrateurs.'));
// ou Response::denyWithStatus(404) / Response::denyAsNotFound()
```

**Utilisateurs invités** : typez le paramètre `?User $user` pour autoriser les non-connectés.

**Hooks**

```php
Gate::before(fn (User $user, string $ability) => $user->isSuperAdmin() ? true : null);
Gate::after(fn ($user, $ability, $result, $arguments) => /* … */);
```

`null` laisse le contrôle normal se poursuivre ; `true` / `false` court-circuitent.

### 16.3 Policies

```bash
php artisan make:policy PostPolicy --model=Post
```

```php
// app/Policies/PostPolicy.php
class PostPolicy
{
    public function viewAny(User $user): bool { return true; }

    public function view(?User $user, Post $post): bool
    {
        return $post->published || $user?->id === $post->user_id;
    }

    public function create(User $user): bool { return $user->can_write; }

    public function update(User $user, Post $post): Response
    {
        return $user->id === $post->user_id
            ? Response::allow()
            : Response::deny('Vous n\'êtes pas l\'auteur.');
    }

    public function delete(User $user, Post $post): bool { return $user->id === $post->user_id; }
    public function restore(User $user, Post $post): bool { /* … */ }
    public function forceDelete(User $user, Post $post): bool { /* … */ }

    public function before(User $user, string $ability): ?bool    // exécutée avant les autres méthodes
    {
        if ($user->isAdmin()) return true;
        return null;
    }
}
```

**Découverte** : Laravel associe automatiquement `App\Models\Post` ↔ `App\Policies\PostPolicy`. Sinon : `Gate::policy(Post::class, PostPolicy::class)` ou l'attribut `#[UsePolicy(PostPolicy::class)]`.

### 16.4 Utiliser les autorisations

**Via le modèle utilisateur**

```php
$request->user()->can('update', $post);
$request->user()->cannot('update', $post);
$request->user()->can('create', Post::class);        // sans instance
```

**Dans un contrôleur**

```php
$this->authorize('update', $post);                   // trait AuthorizesRequests (à inclure)
Gate::authorize('update', $post);
$this->authorizeResource(Post::class, 'post');       // associe automatiquement les actions du CRUD
```

| Méthode de contrôleur | Méthode de policy |
| --- | --- |
| `index` | `viewAny` |
| `show` | `view` |
| `create`, `store` | `create` |
| `edit`, `update` | `update` |
| `destroy` | `delete` |

**Via middleware**

```php
Route::put('/post/{post}', /* … */)->middleware('can:update,post');
Route::post('/post', /* … */)->middleware('can:create,App\Models\Post');
Route::put('/post/{post}', /* … */)->can('update', 'post');
```

**Via Blade**

```blade
@can('update', $post) … @elsecan('create', App\Models\Post::class) … @endcan
@cannot('update', $post) … @endcannot
@canany(['update', 'delete'], $post) … @endcanany
```

**Via Form Request** : méthode `authorize()`. **Contexte supplémentaire** : `Gate::authorize('create', [Post::class, $category])`.

### 16.5 Modèle « rôles et permissions »

Laravel ne fournit pas de rôles prêts à l'emploi. Approches :

1. Colonne `role` simple + Gates / Policies.
2. Tables `roles` et `permissions` + pivots, avec `Gate::before`.
3. Package **`spatie/laravel-permission`** : `$user->assignRole('admin')`, `$user->givePermissionTo('edit articles')`, directive `@role('admin')`, middleware `role:admin|writer`.

### 16.6 Autorisation côté API

Retourne **403 Forbidden** (authentifié mais interdit) et non **401** (non authentifié). Pour **masquer l'existence** d'une ressource, utilisez `denyAsNotFound()` (404).

### 16.7 Tester les autorisations

```php
$this->actingAs($otherUser)->put("/posts/{$post->id}", [/* … */])->assertForbidden();
$this->assertTrue(Gate::forUser($author)->allows('update', $post));
```

### 16.8 Pièges fréquents

- **Masquer un bouton sans protéger la route** : l'autorisation doit se faire **côté serveur**.
- **Faille IDOR** : charger une ressource par identifiant sans vérifier qu'elle appartient à l'utilisateur.
- **`before()` qui retourne `false`** à tort : bloque tout, même l'admin ; retournez `null` pour poursuivre.
- **`authorizeResource` et noms de paramètres** : le nom de route doit correspondre.
- **Policy non découverte** : modèle ou policy hors des chemins conventionnels sans enregistrement.

### Synthèse du chapitre 16

Les **Gates** (closures) et les **Policies** (classes par modèle) décident des droits. Appelez-les depuis le modèle utilisateur (`can`), les contrôleurs (`authorize`), les middleware (`can:`), Blade (`@can`) et les Form Requests. Utilisez `before` pour les super-administrateurs, `spatie/laravel-permission` pour des rôles, et **toujours** autorisez côté serveur.

---

## 17. Conteneur de services et injection de dépendances

**Objectifs d'apprentissage.** Définir dépendance, injection de dépendances, inversion de contrôle et conteneur ; comprendre la résolution automatique par réflexion ; maîtriser les liaisons (`bind`, `singleton`, `scoped`, `instance`), les liaisons contextuelles, le tagging et l'extension ; utiliser les attributs de contexte ; résoudre manuellement ; réagir aux événements du conteneur ; découpler et tester grâce au conteneur.

### 17.1 Définitions

- **Dépendance** : un objet dont une classe a besoin.
- **Injection de dépendances (DI)** : fournir les dépendances **de l'extérieur** (constructeur ou méthode) plutôt que de les créer en interne (`new`).
- **Inversion de contrôle (IoC)** : le conteneur décide de la création des objets.
- **Service container** : l'outil de Laravel qui gère la **résolution** et l'**injection** des classes.

| Avantage | Détail |
| --- | --- |
| **Découplage** | Une classe dépend d'une abstraction, pas d'une implémentation |
| **Testabilité** | On substitue un *mock* ou un *fake* |
| **Flexibilité** | On change l'implémentation sans toucher aux consommateurs |

### 17.2 Résolution automatique (zéro configuration)

Si une classe n'a **pas de dépendances**, ou seulement des classes concrètes résolubles, le conteneur la construit par **réflexion**.

```php
// app/Http/Controllers/PodcastController.php
class PodcastController extends Controller
{
    public function __construct(protected AppleMusic $apple) {}        // injecté automatiquement
}

Route::get('/', function (Service $service) { /* … */ });             // injection dans une closure
public function show(Request $request, Mailer $mailer, string $id)    // injection de méthode
```

L'injection automatique fonctionne dans : contrôleurs, middleware, listeners, jobs (`handle`), policies, composants Blade, commandes…

### 17.3 Liaisons (*bindings*)

Nécessaires pour les **interfaces** ou une construction particulière. Elles se déclarent dans le **`register()`** d'un provider :

```php
// bind : nouvelle instance à chaque résolution
$this->app->bind(Transistor::class, function (Application $app) {
    return new Transistor($app->make(PodcastParser::class));
});

// Interface → implémentation
$this->app->bind(PaymentGateway::class, StripeGateway::class);

// singleton : une seule instance pour toute l'application
$this->app->singleton(Transistor::class, fn ($app) => new Transistor(/* … */));
$this->app->singletonIf(/* … */);
$this->app->bindIf(/* … */);

// scoped : une instance par cycle de requête / de job (utile avec Octane et les queues)
$this->app->scoped(Transistor::class, fn () => /* … */);

// instance existante
$this->app->instance(Transistor::class, new Transistor($service));

// Valeurs primitives
$this->app->when(UserController::class)->needs('$variableName')->give($value);
$this->app->when(Report::class)->needs('$apiKey')->giveConfig('services.report.key');
```

| Méthode | Durée de vie |
| --- | --- |
| `bind` | Nouvelle instance **à chaque** résolution |
| `singleton` | **Une** instance pour toute l'application |
| `scoped` | Une instance **par cycle** (requête, job) |
| `instance` | Instance **déjà construite** |

**Liaison contextuelle** (même interface, implémentations différentes selon la classe) :

```php
$this->app->when(PhotoController::class)
          ->needs(Filesystem::class)
          ->give(fn () => Storage::disk('local'));

$this->app->when([VideoController::class, UploadController::class])
          ->needs(Filesystem::class)
          ->give(fn () => Storage::disk('s3'));
```

**Tagging**

```php
$this->app->tag([CpuReport::class, MemoryReport::class], 'reports');

$this->app->bind(ReportAnalyzer::class, fn ($app) => new ReportAnalyzer($app->tagged('reports')));
```

**Extension** (décorer un service) :

```php
$this->app->extend(Service::class, fn ($service, $app) => new DecoratedService($service));
```

Existent aussi : injection **variadique**, `giveTagged`, `giveConfig`.

**Attributs de contexte** *(ajout, Laravel 11+)*

```php
public function __construct(
    #[Config('app.timezone')] protected string $timezone,
    #[Storage('s3')] protected Filesystem $disk,
    #[CurrentUser] protected User $user,
    #[Log('daily')] protected LoggerInterface $log,
    #[Auth('admin')] protected Guard $guard,
    #[Cache('redis')] protected Repository $cache,
    #[DB('mysql')] protected Connection $connection,
    #[RouteParameter('photo')] protected Photo $photo,
    #[Tag('reports')] protected iterable $reports,
) {}
```

D'autres attributs (`#[Singleton]`, `#[Scoped]`, `#[Bind(...)]`) existent selon la version : vérifiez la documentation.

### 17.4 Résoudre manuellement

```php
$api = $this->app->make(HelpSpot\API::class);
$api = app(HelpSpot\API::class);
$api = resolve(HelpSpot\API::class);
$api = app()->makeWith(HelpSpot\API::class, ['id' => 1]);
app()->bound(Foo::class);
```

Préférez **l'injection par le constructeur** ; la résolution manuelle est un **dernier recours**.

### 17.5 Événements du conteneur

```php
$this->app->resolving(Transistor::class, function (Transistor $t, Application $app) { /* … */ });
$this->app->afterResolving(/* … */);
```

### 17.6 Conteneur et PSR-11

Le conteneur implémente `Psr\Container\ContainerInterface` : `$container->get(Foo::class)`, `has()`.

### 17.7 Fonctionnement interne

Réflexion PHP (`ReflectionClass`) → inspection des types du constructeur → résolution **récursive** de chaque type → instanciation. Si un paramètre est un type **scalaire** sans valeur par défaut ni liaison → `BindingResolutionException`.

### 17.8 Exemple pratique : découplage

```php
interface SmsSender { public function send(string $to, string $msg): void; }
class TwilioSender implements SmsSender { /* … */ }
class FakeSender implements SmsSender { /* … */ }

// Provider
$this->app->bind(SmsSender::class, fn () => app()->isLocal() ? new FakeSender : new TwilioSender(config('services.twilio')));

// Consommateur
class WelcomeService { public function __construct(private SmsSender $sms) {} }
```

En test : `$this->app->instance(SmsSender::class, new FakeSender);`.

### 17.9 Pièges fréquents

- **`singleton` avec un état utilisateur** : fuite de données entre requêtes sous **Octane** ; préférez `scoped`.
- **Type scalaire sans liaison** : `BindingResolutionException`.
- **Utiliser `app()` partout** : dépendances cachées (*service locator*) ; injectez.
- **Dépendance circulaire** : A requiert B qui requiert A ; extraire un troisième service.
- **Lier dans `boot()`** ce qui doit l'être dans `register()`.

### Synthèse du chapitre 17

Le **conteneur** construit les objets par **réflexion** et injecte leurs dépendances. On **lie** interfaces et cas spéciaux dans `register()` (`bind`, `singleton`, `scoped`, `instance`, contextuel, tags, `extend`). Les **attributs de contexte** simplifient l'injection de configuration. **Injectez** plutôt que de résoudre à la main : c'est la clé du découplage et des tests.

---

## 18. Service Providers

**Objectifs d'apprentissage.** Définir un service provider ; distinguer `register()` et `boot()` ; enregistrer un provider (Laravel 11+) et connaître l'auto-découverte ; créer un provider différé ; connaître les providers par défaut et leurs usages typiques ; écrire un provider de package.

### 18.1 Définition

Un **service provider** est le **lieu central d'amorçage** : il enregistre des liaisons dans le conteneur, des écouteurs d'événements, des middleware, des routes, des vues… **Tous** les composants du framework sont chargés par des providers.

### 18.2 Structure

```bash
php artisan make:provider RiakServiceProvider
```

```php
// app/Providers/RiakServiceProvider.php
namespace App\Providers;

class RiakServiceProvider extends ServiceProvider
{
    // Phase 1 : uniquement des liaisons au conteneur
    public function register(): void
    {
        $this->app->singleton(Connection::class, fn ($app) => new Connection(config('riak')));
    }

    // Phase 2 : tout est enregistré
    public function boot(): void
    {
        View::composer('view', function () { /* … */ });
        Event::listen(/* … */);
        Gate::define(/* … */);
        Route::model(/* … */);
        Blade::directive(/* … */);
    }
}
```

**Règle d'or** : dans `register()`, on **ne** résout **pas** d'autres services (ils ne sont pas tous enregistrés). `boot()` peut tout utiliser, avec **injection de dépendances sur la méthode** :

```php
public function boot(ResponseFactory $response): void
{
    $response->macro('serialized', fn ($value) => /* … */);
}
```

### 18.3 Raccourcis `bindings` et `singletons`

```php
public array $bindings   = [ServerProvider::class => DigitalOceanServerProvider::class];
public array $singletons = [DowntimeNotifier::class => PingdomDowntimeNotifier::class];
```

### 18.4 Enregistrement

Laravel 11+ : `bootstrap/providers.php`.

```php
// bootstrap/providers.php
return [
    App\Providers\AppServiceProvider::class,
    App\Providers\RiakServiceProvider::class,
];
```

`php artisan make:provider` l'y ajoute automatiquement. Les providers de **packages** sont découverts par **auto-discovery** (clé `extra.laravel.providers` du `composer.json` du package).

> **Héritage.** Avant Laravel 11, les providers se listaient dans `config/app.php`, clé `providers`.

### 18.5 Providers différés (*deferred*)

Chargés **seulement si** l'un de leurs services est requis :

```php
class RiakServiceProvider extends ServiceProvider implements DeferrableProvider
{
    public function register(): void { /* … */ }
    public function provides(): array { return [Connection::class]; }
}
```

### 18.6 Providers par défaut

- **`AppServiceProvider`** : enregistrement et amorçage généraux (macros, `Model::shouldBeStrict`, `Paginator`, `JsonResource::withoutWrapping`, `Password::defaults`…).
- Les anciens `AuthServiceProvider`, `EventServiceProvider` et `RouteServiceProvider` sont **inutiles par défaut** depuis Laravel 11 (découverte automatique des policies et listeners ; routes dans `bootstrap/app.php`).

### 18.7 Utilisations typiques de `boot()`

```php
Model::shouldBeStrict(! $this->app->isProduction());
Paginator::useBootstrapFive();
Password::defaults(fn () => Password::min(12)->mixedCase()->numbers()->uncompromised());
URL::forceScheme('https');
Date::use(CarbonImmutable::class);
DB::prohibitDestructiveCommands($this->app->isProduction());
Vite::prefetch(concurrency: 3);
JsonResource::withoutWrapping();
RateLimiter::for('api', /* … */);
Relation::enforceMorphMap([/* … */]);
Schema::defaultStringLength(191);
```

### 18.8 Créer un package avec un provider

```php
// src/MyPackageServiceProvider.php
public function boot(): void
{
    $this->loadRoutesFrom(__DIR__.'/../routes/web.php');
    $this->loadViewsFrom(__DIR__.'/../resources/views', 'mypackage');
    $this->loadMigrationsFrom(__DIR__.'/../database/migrations');
    $this->loadTranslationsFrom(__DIR__.'/../lang', 'mypackage');
    $this->mergeConfigFrom(__DIR__.'/../config/mypackage.php', 'mypackage');
    $this->publishes([__DIR__.'/../config/mypackage.php' => config_path('mypackage.php')], 'config');
    $this->commands([MyCommand::class]);
}
```

Publication : `php artisan vendor:publish --tag=config`.

### 18.9 Pièges fréquents

- **Résoudre un service dans `register()`** : peut ne pas exister encore.
- **Code lourd dans `boot()`** : exécuté à chaque requête ; utilisez un provider **différé** ou du cache.
- **Provider non listé** dans `bootstrap/providers.php` (ou non découvert) : ses liaisons n'existent pas.
- **Oublier `provides()`** dans un provider différé : le service n'est jamais résolu.

### Synthèse du chapitre 18

Un **provider** amorce l'application en deux temps : **`register()`** (liaisons seulement) puis **`boot()`** (usage libre des services). On l'enregistre dans **`bootstrap/providers.php`**, ou il est **auto-découvert** pour un package. Les providers **différés** économisent l'amorçage ; `AppServiceProvider` accueille les réglages globaux.

---

## 19. Facades et Contracts

**Objectifs d'apprentissage.** Expliquer le fonctionnement d'une facade ; connaître les facades principales et leurs helpers ; utiliser les *real-time facades* ; tester avec les facades ; créer sa facade ; définir les contracts et comparer facades et contracts ; étendre le framework par macros et mixins.

### 19.1 Facades

Une **facade** offre une **interface statique** vers un service du conteneur. Elle étend `Illuminate\Support\Facades\Facade` et implémente `getFacadeAccessor()`.

```php
use Illuminate\Support\Facades\Cache;

Route::get('/cache', fn () => Cache::get('key'));
```

**Fonctionnement.** L'appel `Cache::get('key')` est intercepté par `__callStatic`, qui **résout l'objet sous-jacent dans le conteneur** et appelle `->get('key')` dessus. Ce n'est **pas** une vraie méthode statique : le code reste **testable**.

```php
class Cache extends Facade
{
    protected static function getFacadeAccessor(): string { return 'cache'; }
}
```

**Facades principales**

| Facade | Service |
| --- | --- |
| `App` | Application |
| `Artisan` | Console |
| `Auth` | Authentification |
| `Blade` | Compilateur Blade |
| `Bus`, `Queue` | Files d'attente |
| `Cache` | Cache |
| `Config` | Configuration |
| `Cookie`, `Session` | Cookies, session |
| `Crypt`, `Hash` | Chiffrement, hashage |
| `DB`, `Schema` | Base de données |
| `Event` | Événements |
| `File`, `Storage` | Fichiers |
| `Gate` | Autorisation |
| `Http` | Client HTTP |
| `Lang` | Traductions |
| `Log` | Journalisation |
| `Mail`, `Notification` | Envoi |
| `Process` | Exécution de processus |
| `RateLimiter` | Limitation de débit |
| `Redirect`, `Request`, `Response`, `Route`, `URL`, `View` | HTTP |
| `Validator` | Validation |
| `Vite` | Assets |
| `Schedule` | Planification |

**Facades et helpers.** De nombreuses facades ont un helper équivalent : `cache()`, `config()`, `session()`, `view()`, `response()`, `redirect()`, `route()`, `url()`, `auth()`, `logger()`, `event()`, `dispatch()`, `now()`, `collect()`, `app()`…

### 19.2 Real-Time Facades

Transformer **n'importe quelle classe** en facade en préfixant son espace de noms par `Facades\` :

```php
use Facades\App\Services\Publisher;

Publisher::publish($podcast);
```

### 19.3 Tester avec les facades

```php
Cache::shouldReceive('get')->once()->with('key')->andReturn('value');
Mail::fake();  Mail::assertSent(Welcome::class);
Queue::fake(); Event::fake(); Notification::fake(); Storage::fake('s3'); Http::fake();
Bus::fake();   Log::spy();   Date::setTestNow(/* … */);
```

### 19.4 Créer sa propre facade

```php
// app/Facades/Greeter.php
class Greeter extends Facade
{
    protected static function getFacadeAccessor(): string { return 'greeter'; }
}

// Provider : $this->app->singleton('greeter', fn () => new GreeterService);
```

### 19.5 Avantages et inconvénients

| Avantages | Inconvénients |
| --- | --- |
| Syntaxe **concise** | Dépendances **cachées** (absentes du constructeur) |
| **Testable** (`shouldReceive`, `fake`) | Risque de classes trop couplées (*class creep*) |
| Accès rapide | Pour un code très découplé, préférer l'**injection** |

### 19.6 Contracts

Les **contracts** (`Illuminate\Contracts\*`) sont des **interfaces** définissant les services fondamentaux : `Illuminate\Contracts\Cache\Repository`, `Queue\Queue`, `Mail\Mailer`, `Auth\Guard`, `Filesystem\Filesystem`, `Events\Dispatcher`, etc.

```php
use Illuminate\Contracts\Cache\Repository as Cache;

class OrderService
{
    public function __construct(protected Cache $cache) {}
}
```

**Avantages** : couplage faible, remplacement possible de l'implémentation, documentation claire de l'API, utile pour des packages indépendants du framework.

### 19.7 Facade ou contract ?

Les deux sont **techniquement équivalents** (même objet résolu). Les facades privilégient la **brièveté**, les contracts le **découplage explicite**. L'équipe doit choisir une **convention** et s'y tenir.

### 19.8 Macros

Étendre à l'exécution des classes « *macroable* » (Collection, Str, Response, Request, Builder…) :

```php
Collection::macro('toUpper', fn () => $this->map(fn ($v) => Str::upper($v)));
Str::macro('initials', fn (string $s) => /* … */);
Response::macro('success', fn ($data) => response()->json(['ok' => true, 'data' => $data]));
```

À déclarer dans `boot()`. Les **mixins** enregistrent plusieurs macros via une classe : `Collection::mixin(new MyMixin)`.

### 19.9 Pièges fréquents

- **Croire qu'une facade est statique** : l'appel est résolu dynamiquement ; on peut la simuler en test.
- **Facades partout dans le domaine** : dépendances invisibles ; injecter un contract pour la logique critique.
- **Macro déclarée trop tard** (hors `boot()`) : introuvable au moment de l'appel.
- **Alias de facade en conflit** avec un nom de classe applicative.

### Synthèse du chapitre 19

Une **facade** est un **proxy statique** vers un service du conteneur (via `__callStatic` et `getFacadeAccessor`) ; un **contract** est l'**interface** de ce service. Les deux sont équivalents ; choisissez selon le besoin de **concision** ou de **découplage**. Les **fakes** et `shouldReceive` rendent les facades testables ; les **macros** étendent les classes du framework.

---

## 20. Collections

**Objectifs d'apprentissage.** Créer et chaîner des collections ; connaître les grandes familles de méthodes (transformation, filtrage, tri, regroupement, agrégation, test, mutation, itération, conversion) ; utiliser les *higher order messages* ; traiter de gros volumes avec les `LazyCollection` ; utiliser `Arr`, `Str`, `Number` et Carbon.

### 20.1 Principe

`Illuminate\Support\Collection` est un **wrapper fluide** autour d'un tableau. La plupart des méthodes retournent une **nouvelle** collection (immuabilité par convention), ce qui permet de **chaîner**.

```php
$collection = collect(['Taylor', 'Abigail', null])
    ->map(fn ($name) => strtoupper($name))
    ->reject(fn ($name) => empty($name));
```

Création : `collect([...])`, `Collection::make([...])`, `Collection::times(10, fn ($n) => $n * 2)`, `Collection::range(1, 5)`, `Collection::wrap($x)`.

### 20.2 Catégories de méthodes

**Transformation**

```php
->map(fn)            ->mapWithKeys(fn)      ->mapInto(Class)
->mapToGroups(fn)    ->mapSpread(fn)        ->flatMap(fn)
->transform(fn)      // modifie en place
->pluck('name')      ->pluck('name', 'id')
->flatten()          ->flatten(1)           ->collapse()
->flip()             ->pad(5, 0)
->pipe(fn)           ->pipeInto(Class)      ->pipeThrough([/* … */])
->undot()            ->dot()
```

**Filtrage**

```php
->filter(fn)         ->reject(fn)           ->where('a', 1)
->where('a', '>', 1) ->whereIn('a', [/* … */])  ->whereNotIn
->whereBetween       ->whereNull            ->whereNotNull
->whereInstanceOf    ->unique()             ->unique('key')
->duplicates()       ->only([/* … */])      ->except([/* … */])
->take(3)            ->takeUntil(fn)        ->takeWhile(fn)
->skip(3)            ->skipUntil(fn)        ->skipWhile(fn)
->slice(2, 3)        ->nth(4)               ->forget('key')
->pull('key')        ->diff([/* … */])      ->diffKeys     ->diffAssoc
->intersect([/* … */]) ->intersectByKeys    ->before / after
```

**Tri**

```php
->sort()             ->sort(fn)             ->sortDesc()
->sortBy('a')        ->sortBy([['a', 'asc'], ['b', 'desc']])
->sortByDesc('a')    ->sortKeys()           ->sortKeysDesc()
->reverse()          ->shuffle()
```

**Regroupement et découpage**

```php
->groupBy('category')  ->groupBy(fn)        ->keyBy('id')
->chunk(4)             ->chunkWhile(fn)     ->split(3)
->splitIn(3)           ->partition(fn)      ->sliding(2)
->zip([/* … */])       ->combine([/* … */]) ->crossJoin
->countBy()            ->countBy(fn)
```

**Agrégation et réduction**

```php
->count()              ->sum()              ->sum('price')
->avg()                ->average('price')   ->median()
->mode()               ->min()              ->max()
->reduce(fn ($carry, $item) => $carry + $item, 0)
->reduceSpread(fn)     ->implode(', ')      ->join(', ', ' et ')
->first()              ->first(fn)          ->firstWhere('a', 1)
->last()               ->sole()             ->firstOrFail()
->get('key', 'default')  ->random()         ->random(3)
```

**Test et existence**

```php
->contains(fn)         ->contains('key', 'value')   ->doesntContain
->containsOneItem()    ->has('key')                 ->hasAny
->isEmpty()            ->isNotEmpty()               ->every(fn)
->some(fn)             ->search($value)
```

**Mutation de contenu**

```php
->push($x)       ->prepend($x)       ->put('k', 'v')
->pop()          ->shift()           ->add($x)
->merge([/* … */])  ->mergeRecursive    ->concat([/* … */])
->replace([/* … */]) ->replaceRecursive  ->union([/* … */])
->splice(2, 1, [/* … */])
```

**Itération et effets de bord**

```php
->each(fn)       ->eachSpread(fn)     ->tap(fn)
->dump()         ->dd()
->when($cond, fn)  ->unless($cond, fn)  ->whenEmpty / whenNotEmpty
```

**Conversion** : `all()`, `toArray()`, `toJson()`, `toPrettyJson()`, `toBase()`, `lazy()`.

**Autres** : `macro`, `ensure(Type::class)`, `percentage()`, `value()`, `forPage($page, $perPage)`, `unwrap`.

### 20.3 Exemples pratiques

```php
// Totaux par catégorie
$orders->groupBy('category')->map(fn ($group) => $group->sum('total'));

// Top 3 clients
$orders->groupBy('customer_id')
       ->map(fn ($g) => ['customer' => $g->first()->customer, 'total' => $g->sum('total')])
       ->sortByDesc('total')->take(3)->values();

// Transformer un tableau associatif
collect($users)->mapWithKeys(fn ($u) => [$u['id'] => $u['name']]);

// Pagination manuelle
$page = collect($items)->forPage(2, 10);
```

### 20.4 Higher Order Messages

Raccourcis pour les actions courantes :

```php
$users->each->markAsVip();
$users->map->name;
$users->sum->votes;
$users->filter->isActive();
$users->sortBy->age;
$users->groupBy->country;
$users->reject->isBanned();
```

### 20.5 Lazy Collections

Basées sur les **générateurs PHP** : elles traitent de gros fichiers ou jeux de données avec une **consommation mémoire minimale**.

```php
use Illuminate\Support\LazyCollection;

LazyCollection::make(function () {
    $handle = fopen('log.txt', 'r');
    while (($line = fgets($handle)) !== false) yield $line;
})->chunk(4)->map(fn ($lines) => /* … */)->each(/* … */);

User::cursor()->filter(fn ($u) => /* … */)->each(/* … */);
$collection->lazy();
$lazy->eager();
$lazy->remember();                          // mémoïse les valeurs déjà énumérées
$lazy->takeUntilTimeout(now()->addMinute());
$lazy->tapEach(fn ($v) => /* … */);
```

### 20.6 Autres utilitaires : `Arr`, `Str`, `Number`

```php
Arr::get($array, 'a.b.c', 'défaut');  Arr::set(/* … */);  Arr::has;  Arr::pluck;  Arr::flatten;
Arr::dot;  Arr::undot;  Arr::only;  Arr::except;  Arr::first;  Arr::last;  Arr::where;  Arr::wrap;
Arr::random;  Arr::shuffle;  Arr::sort;  Arr::sortRecursive;  Arr::query;  Arr::forget;  Arr::pull;

Str::slug('Titre exemple');  Str::camel;  Str::snake;  Str::kebab;  Str::studly;  Str::title;
Str::limit($t, 100);  Str::words;  Str::contains;  Str::startsWith;  Str::endsWith;
Str::before;  Str::after;  Str::between;  Str::replace;  Str::random(16);  Str::uuid;
Str::ulid;  Str::plural;  Str::singular;  Str::mask;  Str::markdown;  Str::isUuid;
Str::of('Hello')->append(' World')->upper()->slug();        // interface fluide Stringable

Number::format(1234567.891, 2);  Number::currency(500, 'EUR');  Number::percentage(10);
Number::abbreviate(1000000);  Number::fileSize(1024 * 1024);  Number::forHumans(/* … */);  Number::ordinal(3);
```

### 20.7 Dates avec Carbon

```php
now(); today(); Carbon::parse('2026-01-01');
now()->addDays(3)->startOfDay()->format('d/m/Y');
$date->diffForHumans();                     // « il y a 3 jours » (avec la locale)
$date->isPast(); $date->between($a, $b);
Date::use(CarbonImmutable::class);          // dates immuables
Carbon::setTestNow('2026-01-01');           // figer le temps (tests)
```

### 20.8 Pièges fréquents

- **Oublier que les clés sont conservées** après `filter` : utilisez `->values()` pour réindexer.
- **Charger 1 million de lignes dans une `Collection`** : préférez `LazyCollection` / `cursor()`.
- **Confondre `Eloquent\Collection` et `Support\Collection`** : certaines méthodes ne portent que sur les modèles.
- **`pluck` vs `map`** : `pluck` extrait une clé ; `map` transforme chaque élément.
- **Calcul côté PHP** de ce qu'SQL fait mieux : agrégez dans la requête.

### Synthèse du chapitre 20

Les **collections** offrent une API **fluide et chaînable** (transformation, filtrage, tri, regroupement, agrégation…), simplifiée par les **higher order messages**. Les **LazyCollections** traitent de gros volumes à mémoire constante. `Arr`, `Str`, `Number` et **Carbon** complètent la boîte à outils.

---

# Partie VII — Événements, tâches asynchrones et services d'infrastructure

## 21. Events et Listeners

**Objectifs d'apprentissage.** Expliquer le patron Observateur ; créer et enregistrer événements et listeners (découverte automatique) ; émettre des événements ; mettre un listener en file d'attente ; écrire un subscriber ; tester ; diffuser en temps réel (*broadcasting*) avec Reverb, Echo et les canaux public, privé et de présence.

### 21.1 Principe

Les **événements** implémentent le patron **Observateur** (publication/abonnement) : un **fait métier** se produit (`OrderShipped`), et zéro, un ou plusieurs **écouteurs** (*listeners*) y réagissent, **sans que l'émetteur les connaisse**. Cela **découple** les effets secondaires (envoyer un mail, mettre à jour des statistiques, notifier Slack…) de l'action principale.

### 21.2 Créer un événement et un listener

```bash
php artisan make:event OrderShipped
php artisan make:listener SendShipmentNotification --event=OrderShipped
php artisan event:list
```

```php
// app/Events/OrderShipped.php
class OrderShipped
{
    use Dispatchable, InteractsWithSockets, SerializesModels;

    public function __construct(public Order $order) {}
}

// app/Listeners/SendShipmentNotification.php
class SendShipmentNotification
{
    public function handle(OrderShipped $event): void
    {
        // $event->order
    }
}
```

`SerializesModels` : les modèles Eloquent sont sérialisés par leur **identifiant** (utile pour la file d'attente).

### 21.3 Enregistrement

**Découverte automatique** *(à jour : Laravel 11+)* : tout listener dans `app/Listeners` dont la méthode `handle*` / `__invoke` est typée avec un événement est enregistré automatiquement.

**Enregistrement manuel** (dans le `boot()` d'un provider) :

```php
Event::listen(OrderShipped::class, SendShipmentNotification::class);
Event::listen(function (PodcastProcessed $event) { /* … */ });                  // closure
Event::listen('event.*', function (string $eventName, array $data) { /* … */ });   // joker
```

En production : `php artisan event:cache` / `event:clear`.

### 21.4 Émettre un événement

```php
OrderShipped::dispatch($order);
OrderShipped::dispatchIf($condition, $order);
OrderShipped::dispatchUnless($condition, $order);
event(new OrderShipped($order));
Event::dispatch(new OrderShipped($order));
```

### 21.5 Listeners en file d'attente

Pour les traitements lents (mail, API tierce), ajoutez **`ShouldQueue`** :

```php
class SendShipmentNotification implements ShouldQueue
{
    use InteractsWithQueue;

    public $connection = 'redis';
    public $queue      = 'listeners';
    public $delay      = 60;
    public $tries      = 3;
    public $backoff    = [10, 60];

    public function handle(OrderShipped $event): void { /* … */ }

    public function shouldQueue(OrderShipped $event): bool { return $event->order->total > 100; }

    public function failed(OrderShipped $event, Throwable $exception): void { /* … */ }
}
```

Dans un listener, `$this->release(30)` remet le job en file, `$this->delete()` le supprime.

**Après commit.** Pour éviter qu'un listener s'exécute **avant** la validation de la transaction : `ShouldQueueAfterCommit` (ou `$afterCommit = true`) côté listener, `ShouldDispatchAfterCommit` côté événement.

### 21.6 Subscribers

Une classe qui écoute **plusieurs** événements :

```php
class UserEventSubscriber
{
    public function handleLogin(Login $event): void { /* … */ }
    public function handleLogout(Logout $event): void { /* … */ }

    public function subscribe(Dispatcher $events): array
    {
        return [
            Login::class  => 'handleLogin',
            Logout::class => 'handleLogout',
        ];
    }
}

Event::subscribe(UserEventSubscriber::class);
```

### 21.7 Arrêter la propagation

Un listener qui retourne **`false`** empêche les listeners suivants de s'exécuter.

### 21.8 Tester les événements

```php
Event::fake();                         // ou Event::fake([OrderShipped::class]);
// … action …
Event::assertDispatched(OrderShipped::class, fn ($e) => $e->order->id === $order->id);
Event::assertNotDispatched(/* … */);
Event::assertDispatchedTimes(OrderShipped::class, 2);
Event::assertNothingDispatched();
Event::assertListening(OrderShipped::class, SendShipmentNotification::class);
```

### 21.9 Broadcasting (diffusion en temps réel)

Le *broadcasting* **pousse** des événements du serveur vers les clients (WebSockets).

**Composants**

- **Serveur WebSocket** : **Laravel Reverb** (officiel), Pusher Channels, Ably, Soketi.
- **Laravel Echo** : bibliothèque JavaScript cliente.
- **Canaux** : *public* (`Channel`), *privé* (`PrivateChannel`, autorisation requise), *présence* (`PresenceChannel`, liste des membres).

```bash
php artisan install:broadcasting
```

```php
// app/Events/OrderShipmentStatusUpdated.php
class OrderShipmentStatusUpdated implements ShouldBroadcast        // ou ShouldBroadcastNow
{
    public function __construct(public Order $order) {}

    public function broadcastOn(): array
    {
        return [new PrivateChannel('orders.'.$this->order->id)];
    }

    public function broadcastAs(): string { return 'order.updated'; }
    public function broadcastWith(): array { return ['id' => $this->order->id, 'status' => $this->order->status]; }
    public function broadcastWhen(): bool { return $this->order->value > 100; }
}
```

**Autorisation des canaux**

```php
// routes/channels.php
Broadcast::channel('orders.{orderId}', fn (User $user, int $orderId) => $user->id === Order::find($orderId)->user_id);
Broadcast::channel('chat.{room}', fn ($user, $room) => ['id' => $user->id, 'name' => $user->name]);   // présence
```

**Côté client**

```js
Echo.private(`orders.${orderId}`)
    .listen('.order.updated', (e) => console.log(e));
Echo.join(`chat.${room}`).here(users => /* … */).joining(user => /* … */).leaving(user => /* … */);
Echo.channel('news').listen('NewsPublished', /* … */);
```

**Autres notions** : *client events* (`whisper`), `toOthers()` (exclure l'émetteur), **Model Broadcasting** (`BroadcastsEvents`), **notifications broadcast**.

### 21.10 Pièges fréquents

- **Listener qui lit la base avant le `commit`** : utilisez les variantes `AfterCommit`.
- **Passer un gros objet** à l'événement : sérialisez des identifiants (`SerializesModels`).
- **Listener en queue sans worker** : rien ne s'exécute.
- **Logique métier critique dans un listener asynchrone** : une panne silencieuse est possible ; surveillez les jobs échoués.
- **Canal privé sans règle d'autorisation** : abonnement refusé (403).

### Synthèse du chapitre 21

Un **événement** annonce un fait ; des **listeners** y réagissent, éventuellement **en file** (`ShouldQueue`, après commit). La **découverte automatique** les enregistre ; les **subscribers** en regroupent plusieurs ; `Event::fake` les teste. Le **broadcasting** (Reverb + Echo, canaux public/privé/présence) diffuse en **temps réel**.

---

## 22. Queues (files d'attente)

**Objectifs d'apprentissage.** Expliquer l'intérêt des queues ; choisir un pilote ; créer et dispatcher des jobs ; chaîner et grouper des jobs ; utiliser les middleware de jobs et les jobs uniques ; exécuter et superviser des workers ; gérer les jobs échoués ; connaître Horizon ; tester.

### 22.1 Pourquoi ?

Certaines tâches sont lentes (envoi d'e-mails, traitement d'images, appels d'API, exports). Les exécuter **pendant la requête** dégrade l'expérience. Les **queues** les déportent en arrière-plan, exécutées par des **workers**.

### 22.2 Pilotes et configuration

`config/queue.php` et `.env` (`QUEUE_CONNECTION`).

| Pilote | Usage |
| --- | --- |
| `sync` | Exécution immédiate (développement, tests) |
| `database` | Simple, aucune infrastructure |
| `redis` | Performant, **recommandé en production** (Horizon) |
| `sqs` | Amazon SQS |
| `beanstalkd` | Beanstalkd |
| `null` | Ignore les jobs |
| `failover` | Basculement entre pilotes |

**Préparer le pilote `database`**

```bash
php artisan make:queue-table
php artisan migrate
```

Notions : **connexion** (le service) → **file nommée** (`default`, `emails`, `high`), qui permet de **prioriser**.

### 22.3 Créer un job

```bash
php artisan make:job ProcessPodcast
```

```php
// app/Jobs/ProcessPodcast.php
class ProcessPodcast implements ShouldQueue
{
    use Queueable;                                // Dispatchable, InteractsWithQueue, SerializesModels…

    public $tries = 3;                            // nombre de tentatives
    public $maxExceptions = 2;
    public $timeout = 120;                        // secondes
    public $backoff = [10, 60, 300];              // délais entre tentatives
    public $failOnTimeout = true;
    public $deleteWhenMissingModels = true;

    public function __construct(public Podcast $podcast) {}

    public function handle(AudioProcessor $processor): void       // dépendances injectées
    {
        $processor->process($this->podcast);
    }

    public function failed(?Throwable $exception): void { /* notifier */ }

    public function retryUntil(): DateTime { return now()->addMinutes(10); }
}
```

> **Note de version.** Des attributs PHP (`#[Tries(3)]`, `#[Timeout(120)]`, `#[Backoff(...)]`) sont disponibles selon la version (Laravel 13 étend l'usage des attributs) ; les propriétés restent valides.

### 22.4 Dispatcher un job

```php
ProcessPodcast::dispatch($podcast);
ProcessPodcast::dispatchIf($cond, $podcast);
ProcessPodcast::dispatch($podcast)->delay(now()->addMinutes(10));
ProcessPodcast::dispatch($podcast)->onQueue('processing')->onConnection('redis');
ProcessPodcast::dispatch($podcast)->afterCommit();         // après la transaction
ProcessPodcast::dispatch($podcast)->beforeCommit();
ProcessPodcast::dispatchSync($podcast);                    // immédiat, synchrone
ProcessPodcast::dispatchAfterResponse($podcast);           // après l'envoi de la réponse HTTP
dispatch(function () { /* … */ })->catch(fn (Throwable $e) => /* … */);   // closure
```

### 22.5 Chaînage et lots

**Chaînes (séquentielles)**

```php
Bus::chain([
    new OptimizePodcast,
    new ReleasePodcast,
    function () { /* closure */ },
])->onQueue('podcasts')->catch(fn (Throwable $e) => /* … */)->dispatch();
```

Si un job échoue, **les suivants ne s'exécutent pas**.

**Lots (parallèles)**

```php
$batch = Bus::batch([new ImportCsv(1, 100), new ImportCsv(101, 200)])
    ->then(fn (Batch $b) => /* tous réussis */)
    ->catch(fn (Batch $b, Throwable $e) => /* premier échec */)
    ->finally(fn (Batch $b) => /* terminé */)
    ->progress(fn (Batch $b) => /* … */)
    ->allowFailures()
    ->name('Import CSV')
    ->onQueue('imports')
    ->dispatch();

$batch->id; Bus::findBatch($id)->progress();       // pourcentage de progression
```

Les jobs d'un lot utilisent `Batchable` puis `$this->batch()->cancelled()`, `$this->batch()->add([...])`. Table : `php artisan make:queue-batches-table`.

### 22.6 Middleware de jobs

```php
public function middleware(): array
{
    return [
        new RateLimited('backups'),
        new WithoutOverlapping($this->user->id),             // évite l'exécution concurrente
        (new ThrottlesExceptions(10, 5 * 60))->backoff(5),
        new SkipIfBatchCancelled,
    ];
}
```

### 22.7 Jobs uniques

```php
class UpdateSearchIndex implements ShouldQueue, ShouldBeUnique
{
    public $uniqueFor = 3600;
    public function uniqueId(): string { return $this->product->id; }
}
// ShouldBeUniqueUntilProcessing : le verrou est levé au démarrage du traitement
```

Nécessite un cache supportant les **verrous** (Redis, database, memcached…).

### 22.8 Exécuter les workers

```bash
php artisan queue:work                                # démon : garde le framework en mémoire (rapide)
php artisan queue:work redis --queue=high,default     # priorités
php artisan queue:work --tries=3 --timeout=90 --sleep=3 --max-jobs=1000 --max-time=3600 --memory=128
php artisan queue:work --once
php artisan queue:work --stop-when-empty
php artisan queue:listen                              # recharge le code à chaque job (dev, lent)
php artisan queue:restart                             # redémarrage gracieux après déploiement
php artisan queue:monitor redis:default --max=100
php artisan queue:clear
```

> **Important.** Le worker garde le code **en mémoire** : relancez-le (`queue:restart`) après **chaque déploiement**.

**Supervisor** (Linux) maintient les workers actifs :

```ini
; /etc/supervisor/conf.d/laravel-worker.conf
[program:laravel-worker]
command=php /var/www/artisan queue:work --sleep=3 --tries=3 --max-time=3600
autostart=true
autorestart=true
numprocs=4
stopwaitsecs=3600
```

### 22.9 Jobs échoués

Table `failed_jobs` :

```bash
php artisan make:queue-failed-table && php artisan migrate
php artisan queue:failed
php artisan queue:retry 5            # un job
php artisan queue:retry all
php artisan queue:forget 5
php artisan queue:flush
php artisan queue:prune-failed --hours=48
```

Événements : `JobFailed`, `JobProcessed`, `JobProcessing`, `JobQueued`. La méthode `failed()` permet de réagir.

### 22.10 Gestion d'un job en cours

```php
$this->release(60);        // remet en file avec un délai
$this->fail($exception);   // marque comme échoué
$this->delete();
$this->attempts();
```

### 22.11 Laravel Horizon

Tableau de bord et supervision pour **Redis** : métriques de débit, temps d'attente, jobs échoués, **équilibrage automatique** des workers, étiquettes (*tags*).

```bash
composer require laravel/horizon
php artisan horizon:install
php artisan horizon            # remplace queue:work
php artisan horizon:terminate
```

### 22.12 Bonnes pratiques

- Jobs **idempotents** (réexécutables sans double effet).
- Passer des **identifiants/modèles**, pas de gros objets.
- Définir `tries`, `timeout`, `backoff`.
- **Séparer** les files par priorité.
- **Surveiller** (Horizon, `queue:monitor`, alertes).
- `afterCommit` quand on dispatche dans une transaction.

### 22.13 Tester

```php
Queue::fake();
// action
Queue::assertPushed(ProcessPodcast::class);
Queue::assertPushedOn('processing', ProcessPodcast::class);
Queue::assertNotPushed(/* … */);
Queue::assertNothingPushed();
Queue::assertPushedWithChain(/* … */);
Bus::fake(); Bus::assertBatched(/* … */); Bus::assertChained([/* … */]);
```

### 22.14 Pièges fréquents

- **Worker non redémarré** après déploiement : il exécute l'ancien code.
- **`QUEUE_CONNECTION=sync` en production** : tout reste synchrone.
- **Job non idempotent** retenté : double facturation, double mail.
- **Timeout du job supérieur à `retry_after`** de la connexion : le job est repris pendant qu'il tourne.
- **Modèle supprimé avant exécution** : `ModelNotFoundException` ; `deleteWhenMissingModels`.
- **Dispatcher avant le `commit`** : le job ne retrouve pas les données.

### Synthèse du chapitre 22

Les **queues** déportent les tâches lentes vers des **workers**. Créez des **jobs** (`ShouldQueue`, `tries`, `timeout`, `backoff`), dispatchez-les (délai, file, après commit), **chaînez** ou **groupez** (`Bus::chain`, `Bus::batch`), protégez-les (middleware, unicité). Supervisez les workers (Supervisor, **Horizon**), traitez les **jobs échoués**, et rendez tout **idempotent**.

---

## 23. Jobs planifiés (Scheduler)

**Objectifs d'apprentissage.** Comprendre le principe d'une seule entrée cron ; définir des tâches planifiées (closures, commandes, jobs) ; choisir fréquences et contraintes ; éviter les chevauchements et les doublons multi-serveurs ; gérer sorties et notifications ; inspecter et tester.

### 23.1 Principe

Au lieu de gérer plusieurs entrées `cron`, Laravel n'en requiert **qu'une seule** (exécutée chaque minute) ; la planification est définie **en PHP**, versionnée avec le code.

```cron
* * * * * cd /chemin/projet && php artisan schedule:run >> /dev/null 2>&1
```

### 23.2 Définir les tâches

Dans `routes/console.php` *(à jour : Laravel 11+)* :

```php
// routes/console.php
use Illuminate\Support\Facades\Schedule;

Schedule::call(fn () => DB::table('recent_users')->delete())->daily();
Schedule::command('emails:send Taylor --force')->daily();
Schedule::command(SendEmailsCommand::class, ['Taylor', '--force'])->daily();
Schedule::job(new Heartbeat)->everyFiveMinutes();
Schedule::job(new Heartbeat, 'heartbeats', 'sqs')->everyFiveMinutes();      // file spécifique
Schedule::exec('node /home/forge/script.js')->daily();
Schedule::call(new DeleteRecentUsers)->daily();
```

> **Héritage.** Avant Laravel 11, la planification se définissait dans la méthode `schedule()` de `app/Console/Kernel.php`.

### 23.3 Fréquences

```text
->everySecond() (limité)    ->everyMinute()         ->everyTwoMinutes()
->everyFiveMinutes()        ->everyTenMinutes()     ->everyFifteenMinutes()
->everyThirtyMinutes()      ->hourly()              ->hourlyAt(17)
->everyTwoHours()           ->daily()               ->dailyAt('13:00')
->twiceDaily(1, 13)         ->weekly()              ->weeklyOn(1, '8:00')
->monthly()                 ->monthlyOn(4, '15:00') ->twiceMonthly(1, 16, '13:00')
->lastDayOfMonth('15:00')   ->quarterly()           ->yearly()
->cron('* * * * *')         ->timezone('Indian/Antananarivo')
```

**Contraintes de jour et d'horaire**

```php
->weekdays()  ->weekends()  ->mondays() … ->sundays()
->days([0, 3])  ->between('8:00', '17:00')  ->unlessBetween('23:00', '4:00')
->when(fn () => true)  ->skip(fn () => false)  ->environments(['staging', 'production'])
```

### 23.4 Options d'exécution

```php
->withoutOverlapping()          // évite les exécutions concurrentes (verrou, expire après 24 h par défaut)
->withoutOverlapping(10)        // expire après 10 min
->onOneServer()                 // un seul serveur parmi plusieurs (cache partagé requis)
->runInBackground()             // commandes en parallèle
->evenInMaintenanceMode()
->name('rapport')               // nom explicite (nécessaire pour closures et onOneServer)
->description('…')
```

### 23.5 Sorties et notifications

```php
->sendOutputTo($path)  ->appendOutputTo($path)
->emailOutputTo('a@b.com')  ->emailOutputOnFailure('a@b.com')
->pingBefore($url)  ->thenPing($url)  ->pingOnSuccess($url)  ->pingOnFailure($url)
->before(fn () => /* … */)  ->after(fn () => /* … */)
->onSuccess(fn () => /* … */)  ->onFailure(fn () => /* … */)
```

### 23.6 Exécution locale et inspection

```bash
php artisan schedule:list         # liste les tâches et prochaines exécutions
php artisan schedule:run          # exécute les tâches dues
php artisan schedule:work         # boucle en développement (sans cron)
php artisan schedule:test         # exécute une tâche choisie
php artisan schedule:interrupt    # arrête proprement lors d'un déploiement
```

### 23.7 Tâches fréquentes typiques

- Purge d'anciens enregistrements (`model:prune`).
- Sauvegardes (`spatie/laravel-backup`).
- Rapports et e-mails récapitulatifs.
- Nettoyage de caches et jetons expirés (`auth:clear-resets`, `sanctum:prune-expired`).
- Synchronisation avec des API externes.
- `queue:work --stop-when-empty` planifié chaque minute (hébergement **sans** Supervisor).
- `horizon:snapshot` toutes les 5 minutes.

### 23.8 Pièges fréquents

- **Oublier l'entrée cron** : aucune tâche ne s'exécute.
- **Plusieurs serveurs sans `onOneServer`** : tâche exécutée en double.
- **Tâche longue sans `withoutOverlapping`** : empilement d'exécutions.
- **Fuseau horaire implicite** : définissez `timezone` (heure serveur ≠ heure locale).
- **Closure sans `name()`** avec `onOneServer` : impossible d'identifier la tâche.

### Synthèse du chapitre 23

**Une seule** entrée cron (`schedule:run` chaque minute) suffit : la planification s'écrit en PHP dans `routes/console.php` (closures, commandes, jobs, `exec`), avec fréquences et contraintes lisibles. Protégez-la avec **`withoutOverlapping`** et **`onOneServer`**, surveillez-la (`schedule:list`, pings) et testez-la (`schedule:test`).

---

## 24. Notifications et Mails

**Objectifs d'apprentissage.** Configurer l'envoi d'e-mails ; créer et envoyer un Mailable (enveloppe, contenu, pièces jointes) ; écrire des mails Markdown ; prévisualiser et tester ; créer des notifications multicanaux (mail, base de données, broadcast, SMS, Slack) ; router, mettre en file et localiser ; appliquer les bonnes pratiques de délivrabilité.

### 24.1 Mails : configuration

`config/mail.php` et `.env` : `MAIL_MAILER` (`smtp`, `ses`, `postmark`, `resend`, `mailgun`, `sendmail`, `log`, `array`, `failover`, `roundrobin`), `MAIL_FROM_ADDRESS`, `MAIL_FROM_NAME`.

En développement : **Mailpit**, **Mailtrap** ou le pilote **`log`** (le mail s'écrit dans les journaux).

### 24.2 Créer un Mailable

```bash
php artisan make:mail OrderShipped
php artisan make:mail OrderShipped --markdown=mail.orders.shipped
```

```php
// app/Mail/OrderShipped.php
class OrderShipped extends Mailable implements ShouldQueue
{
    use Queueable, SerializesModels;

    public function __construct(public Order $order) {}

    public function envelope(): Envelope
    {
        return new Envelope(
            from: new Address('jeffrey@example.com', 'Jeffrey Way'),
            replyTo: [new Address('taylor@example.com')],
            subject: 'Votre commande a été expédiée',
            tags: ['shipment'], metadata: ['order_id' => $this->order->id],
        );
    }

    public function content(): Content
    {
        return new Content(
            view: 'mail.orders.shipped',               // ou markdown: / text: / html:
            with: ['orderName' => $this->order->name],
        );
    }

    public function attachments(): array
    {
        return [
            Attachment::fromPath('/path/to/file.pdf')->as('facture.pdf')->withMime('application/pdf'),
            Attachment::fromStorage('/path/to/file'),
            Attachment::fromData(fn () => $pdf, 'rapport.pdf'),
        ];
    }

    public function headers(): Headers { return new Headers(text: ['X-Custom' => 'valeur']); }
}
```

Les propriétés **publiques** sont disponibles dans la vue.

### 24.3 Envoyer

```php
Mail::to($user)->send(new OrderShipped($order));
Mail::to($request->user())->cc($moreUsers)->bcc($evenMoreUsers)->send(new OrderShipped($order));
Mail::to($user)->queue(new OrderShipped($order));
Mail::to($user)->later(now()->addMinutes(10), new OrderShipped($order));
Mail::mailer('postmark')->to($user)->send(/* … */);
Mail::to('a@b.com')->locale('fr')->send(/* … */);
Mail::raw('Texte brut', fn ($m) => $m->to('a@b.com')->subject('Test'));
```

### 24.4 Mailables Markdown

```blade
<x-mail::message>
# Commande expédiée

Votre commande a été expédiée.

<x-mail::button :url="$url" color="success">Voir la commande</x-mail::button>

<x-mail::panel>Texte encadré</x-mail::panel>

<x-mail::table>
| Laravel | Table | Exemple |
|:--|:-:|--:|
| A | B | C |
</x-mail::table>

Merci,<br>{{ config('app.name') }}
</x-mail::message>
```

Personnalisation du thème : `php artisan vendor:publish --tag=laravel-mail`.

### 24.5 Prévisualiser et tester

```php
Route::get('/mailable', fn () => new OrderShipped(Order::find(1)));     // rendu dans le navigateur

Mail::fake();
Mail::assertSent(OrderShipped::class, fn ($mail) => $mail->hasTo($user->email));
Mail::assertQueued(/* … */); Mail::assertNothingSent(); Mail::assertSentCount(2);
(new OrderShipped($order))->assertSeeInHtml('texte');
```

### 24.6 Notifications

Les **notifications** sont des messages **multicanaux** envoyés à un « *notifiable* » : `mail`, `database`, `broadcast`, `vonage` (SMS), `slack`, plus des canaux communautaires (Telegram, WhatsApp, Firebase…).

```bash
php artisan make:notification InvoicePaid
php artisan make:notifications-table && php artisan migrate        # canal « database »
```

```php
// app/Notifications/InvoicePaid.php
class InvoicePaid extends Notification implements ShouldQueue
{
    use Queueable;

    public function __construct(public Invoice $invoice) {}

    public function via(object $notifiable): array
    {
        return ['mail', 'database'];
        // dynamique : $notifiable->prefers_sms ? ['vonage'] : ['mail']
    }

    public function toMail(object $notifiable): MailMessage
    {
        return (new MailMessage)
            ->subject('Facture payée')
            ->greeting('Bonjour '.$notifiable->name)
            ->line('Votre facture a été payée.')
            ->action('Voir la facture', url('/invoices/'.$this->invoice->id))
            ->line('Merci !');
            // ->success() / ->error() / ->attach($file) / ->markdown('mail.x')
    }

    public function toArray(object $notifiable): array         // database / broadcast
    {
        return ['invoice_id' => $this->invoice->id, 'amount' => $this->invoice->amount];
    }

    public function toVonage(object $notifiable): VonageMessage { /* … */ }
    public function toSlack(object $notifiable): SlackMessage { /* … */ }
}
```

### 24.7 Envoi

```php
$user->notify(new InvoicePaid($invoice));                  // trait Notifiable sur le modèle
Notification::send($users, new InvoicePaid($invoice));
Notification::sendNow($users, new InvoicePaid($invoice));
Notification::route('mail', 'a@b.com')->route('slack', $webhook)->notify(new InvoicePaid($invoice));   // à la volée
$notification->delay(now()->addMinutes(10))->onQueue('x');
$notification->afterCommit();
```

**Routage** : le modèle définit `routeNotificationForMail()`, `routeNotificationForVonage()`, `routeNotificationForSlack()`.

**Localisation** : `->locale('fr')`, interface `HasLocalePreference`.

### 24.8 Notifications en base de données

```php
$user->notifications;                    // toutes
$user->unreadNotifications;
$user->readNotifications;
foreach ($user->unreadNotifications as $n) { $n->data['invoice_id']; $n->markAsRead(); }
$user->unreadNotifications->markAsRead();
$user->notifications()->delete();
```

### 24.9 Événements et tests

Événements : `NotificationSending`, `NotificationSent`, `NotificationFailed`.

```php
Notification::fake();
Notification::assertSentTo($user, InvoicePaid::class, fn ($n) => /* … */);
Notification::assertNothingSent();
Notification::assertCount(3);
```

### 24.10 Bonnes pratiques

- **Toujours mettre en queue** les envois.
- Utiliser un **service transactionnel** (SES, Postmark, Resend, Mailgun) en production.
- Configurer **SPF, DKIM, DMARC**.
- **Prévisualiser** les mailables dans le navigateur.
- Gérer le **désabonnement** (URL signée).

### 24.11 Pièges fréquents

- **Envoi synchrone** dans la requête : lenteur et échec visible pour l'utilisateur.
- **Mailable sans `SerializesModels`** en queue : modèle périmé ou volumineux.
- **Pilote `log` oublié en production** : aucun mail ne part.
- **Expéditeur non vérifié** chez le fournisseur : rejet.
- **Lien d'action en `localhost`** : `APP_URL` mal configuré.

### Synthèse du chapitre 24

Un **Mailable** (`envelope`, `content`, `attachments`) s'envoie avec `Mail::to()->send()` ou en queue ; le format **Markdown** accélère les gabarits. Une **Notification** envoie le même message sur plusieurs **canaux** (`via`, `toMail`, `toArray`…), se met en file et se localise. **Prévisualisez**, **testez avec `fake`**, et soignez la délivrabilité.

---

## 25. Cache

**Objectifs d'apprentissage.** Définir le cache ; choisir un pilote ; utiliser `put`, `get`, `remember`, `flexible` ; utiliser les tags et les verrous atomiques ; appliquer des motifs d'invalidation ; connaître les caches du framework et le cache HTTP ; tester.

### 25.1 Concept

Le **cache** stocke temporairement des résultats **coûteux** (requêtes, appels API, calculs) pour accélérer l'application.

### 25.2 Pilotes

`CACHE_STORE` : `database`, `file`, `redis`, `memcached`, `dynamodb`, `array` (tests), `null`, `octane`, `failover`.

```bash
php artisan make:cache-table && php artisan migrate        # pilote « database »
```

### 25.3 Utilisation de base

```php
use Illuminate\Support\Facades\Cache;

Cache::put('key', 'value', $seconds = 600);
Cache::put('key', 'value', now()->addMinutes(10));
Cache::put('key', 'value');                              // indéfiniment
Cache::forever('key', 'value');
Cache::add('key', 'value', 600);                         // seulement si absente
Cache::get('key');
Cache::get('key', 'défaut');
Cache::get('key', fn () => DB::table('…')->get());
Cache::has('key');  Cache::missing('key');
Cache::increment('key');  Cache::increment('key', 5);  Cache::decrement('key');
Cache::pull('key');                                      // récupère et supprime
Cache::forget('key');
Cache::flush();                                          // vide TOUT (attention aux préfixes partagés)
Cache::many(['a', 'b']);  Cache::putMany([/* … */], 600);
```

### 25.4 `remember` : le motif principal

```php
$users = Cache::remember('users', 3600, fn () => DB::table('users')->get());
$users = Cache::rememberForever('users', fn () => /* … */);
$value = Cache::flexible('stats', [5, 10], fn () => /* … */);     // « stale-while-revalidate » : frais 5 s, périmé acceptable jusqu'à 10 s
$value = Cache::sear('key', fn () => /* … */);
```

### 25.5 Choisir le magasin

```php
Cache::store('file')->get('foo');
Cache::store('redis')->put('bar', 'baz', 600);
cache('key'); cache(['key' => 'value'], 600); cache()->remember(/* … */);
```

### 25.6 Tags (Redis, Memcached, Array)

```php
Cache::tags(['people', 'artists'])->put('John', $john, 600);
Cache::tags('people')->get('John');
Cache::tags(['people'])->flush();          // vide uniquement ce groupe
```

### 25.7 Verrous atomiques

Ils évitent les **conditions de course** (cron concurrent, double clic) :

```php
$lock = Cache::lock('foo', 10);
if ($lock->get()) { try { /* … */ } finally { $lock->release(); } }

Cache::lock('foo', 10)->get(function () { /* verrou libéré automatiquement */ });
Cache::lock('foo', 10)->block(5, fn () => /* … */);           // attend jusqu'à 5 s
$owner = $lock->owner();  Cache::restoreLock('foo', $owner)->release();   // entre processus
```

### 25.8 Cache de modèles et de requêtes : motifs

```php
// Cache de lecture
Cache::remember("user:{$id}", 600, fn () => User::with('profile')->find($id));

// Invalidation à l'écriture (Observer)
public function saved(User $user) { Cache::forget("user:{$user->id}"); }

// Cache aside + tags
Cache::tags(['products'])->remember("product:$id", 3600, fn () => Product::find($id));
// Product::saved → Cache::tags(['products'])->flush();
```

**Principes** : clés explicites et **versionnées**, TTL raisonnables, invalidation **explicite**, attention au *cache stampede* (utiliser `flexible` ou des verrous).

### 25.9 Caches du framework

```bash
php artisan config:cache   config:clear
php artisan route:cache    route:clear
php artisan view:cache     view:clear
php artisan event:cache    event:clear
php artisan optimize       optimize:clear
php artisan cache:clear    cache:forget key
php artisan cache:prune-stale-tags
```

### 25.10 Cache HTTP

Le middleware `cache.headers:public;max_age=2628000;etag` contrôle `Cache-Control` et l'ETag.

### 25.11 Événements et tests

Événements : `CacheHit`, `CacheMissed`, `KeyWritten`, `KeyForgotten`. Tests : `Cache::shouldReceive('get')->andReturn(...)`, ou pilote `array`.

### 25.12 Pièges fréquents

- **`Cache::flush()` en production** : vide le cache de toutes les applications partageant le même préfixe.
- **Pas d'invalidation** : données périmées servies longtemps.
- **Clés non uniques** (`"users"` pour des contextes différents) : collisions.
- **Tags avec `file` ou `database`** : non supportés.
- **Mettre en cache des données propres à l'utilisateur** sous une clé globale : fuite de données.
- **Oublier `config:clear`** après modification du `.env` quand la config est en cache.

### Synthèse du chapitre 25

Le **cache** (`Cache::remember`, `flexible`) évite de recalculer ; **Redis** est le pilote de choix. Utilisez les **tags** pour invalider par groupe et les **verrous atomiques** contre les courses. **Nommez** vos clés, fixez des **TTL**, **invalidez** explicitement, et mettez en cache la configuration, les routes, les vues et les événements en production.

---

## 26. Sessions

**Objectifs d'apprentissage.** Expliquer le rôle de la session dans un protocole sans état ; configurer pilote, durée et cookie ; lire, écrire et supprimer des données ; utiliser les données éclair (*flash*) ; régénérer et invalider ; gérer le verrouillage de session.

### 26.1 Concept

HTTP est **sans état**. La **session** conserve des données entre les requêtes d'un même visiteur : un **identifiant** est stocké dans un **cookie chiffré**, et les données vivent côté serveur (selon le pilote).

### 26.2 Configuration

`config/session.php` et `.env` :

| Option | Rôle |
| --- | --- |
| `SESSION_DRIVER` | `file`, `cookie`, `database`, `redis`, `memcached`, `dynamodb`, `array` |
| `SESSION_LIFETIME` | Durée d'inactivité (minutes) |
| `SESSION_EXPIRE_ON_CLOSE` | Expire à la fermeture du navigateur |
| `SESSION_ENCRYPT` | Chiffre les données |
| `SESSION_SECURE_COOKIE` | Cookie uniquement en HTTPS |
| `SESSION_HTTP_ONLY` | Inaccessible au JavaScript (défaut `true`) |
| `SESSION_SAME_SITE` | `lax` (défaut), `strict`, `none` |
| `SESSION_DOMAIN`, `SESSION_PATH`, `SESSION_COOKIE` | Portée du cookie |

Pilote **`database`** : `php artisan make:session-table && php artisan migrate`. En production sur **plusieurs serveurs** : `database` ou `redis`.

### 26.3 Utilisation

```php
// Via la requête
$value = $request->session()->get('key');
$value = $request->session()->get('key', 'défaut');
$request->session()->put('key', 'value');
$request->session()->push('user.teams', 'developers');         // ajoute à un tableau
$request->session()->all();
$request->session()->only(['a', 'b']);   $request->session()->except([/* … */]);
$request->session()->has('users');       // présent ET non null
$request->session()->exists('users');    // présent (même null)
$request->session()->missing('users');
$value = $request->session()->pull('key');                     // récupère et supprime
$request->session()->increment('count'); $request->session()->decrement('count');
$request->session()->forget('name');     $request->session()->forget(['a', 'b']);
$request->session()->flush();

// Via les helpers et la facade
session('key'); session(['key' => 'value']);
Session::get('key');
```

### 26.4 Données éclair (*flash*)

Disponibles **uniquement pour la requête suivante** :

```php
$request->session()->flash('status', 'Tâche réussie !');
$request->session()->reflash();                   // conserver pour une requête de plus
$request->session()->keep(['username']);
$request->session()->now('status', 'x');          // pour la requête courante seulement
return redirect('/dashboard')->with('status', 'Profil mis à jour !');
```

```blade
@if (session('status')) <div class="alert">{{ session('status') }}</div> @endif
```

### 26.5 Régénération et invalidation

```php
$request->session()->regenerate();          // nouvel identifiant (anti-fixation) à la connexion
$request->session()->invalidate();          // supprime les données + nouvel identifiant (déconnexion)
$request->session()->regenerateToken();     // jeton CSRF
```

### 26.6 Verrouillage de session

Des requêtes **concurrentes** avec le même identifiant peuvent écraser des données. Les pilotes `redis`, `memcached`, `dynamodb` et `database` supportent le **verrou** :

```php
Route::post(/* … */)->block($lockSeconds = 10, $waitSeconds = 10);
```

### 26.7 Session personnalisée

```php
Session::extend('mongo', fn (Application $app) => new MongoSessionHandler);
```

### 26.8 Sessions et API

Les API **sans état** (jetons) n'utilisent pas la session. Les SPA avec Sanctum utilisent la session côté serveur via un cookie.

### 26.9 Pièges fréquents

- **Pilote `file` derrière plusieurs serveurs** : la session « disparaît » d'un serveur à l'autre.
- **Pas de `regenerate()`** à la connexion : fixation de session.
- **Données volumineuses en session** : alourdit chaque requête ; stockez un identifiant.
- **`flash` perdu après une redirection supplémentaire** : utilisez `reflash()` / `keep()`.
- **Cookie `SameSite=none` sans HTTPS** : refusé par les navigateurs.

### Synthèse du chapitre 26

La **session** (identifiant en cookie chiffré, données côté serveur) maintient l'état entre requêtes. Choisissez un pilote partagé (`redis`, `database`) en production, utilisez `put/get/pull/forget`, les **données flash** pour les messages, **régénérez** à la connexion et **invalidez** à la déconnexion.

---

## 27. Stockage de fichiers

**Objectifs d'apprentissage.** Utiliser le système de fichiers abstrait (Flysystem) ; distinguer les disques `local`, `public`, `s3` ; manipuler fichiers et dossiers ; gérer la visibilité ; téléverser en sécurité ; configurer des disques personnalisés ; générer des URL temporaires ; tester.

### 27.1 Le système de fichiers

Laravel utilise **Flysystem** : une API unique pour le disque local, **S3**, SFTP, FTP, Azure, etc. Configuration : `config/filesystems.php`.

| Disque | Racine | Usage |
| --- | --- | --- |
| `local` | `storage/app/private` | Fichiers **privés** (non accessibles par URL) |
| `public` | `storage/app/public` | Fichiers publics (via lien symbolique) |
| `s3` | Bucket Amazon S3 | Cloud (`league/flysystem-aws-s3-v3`) |

```bash
php artisan storage:link        # public/storage → storage/app/public
```

```php
asset('storage/file.txt');
Storage::url('file.txt');
```

### 27.2 Opérations de base

```php
use Illuminate\Support\Facades\Storage;

Storage::put('file.jpg', $contents);
Storage::put('file.jpg', $resource);
Storage::disk('s3')->put('avatars/1', $content);
Storage::get('file.jpg');
Storage::json('data.json');
Storage::exists('file.jpg');  Storage::missing('file.jpg');
Storage::download('file.jpg', $name, $headers);
Storage::response('file.jpg');                          // affichage « inline »
Storage::delete('file.jpg');  Storage::delete(['a', 'b']);
Storage::copy('old/file.jpg', 'new/file.jpg');
Storage::move('old/file.jpg', 'new/file.jpg');
Storage::append('file.log', 'Contenu');  Storage::prepend('file.log', '…');
Storage::size('file.jpg');
Storage::lastModified('file.jpg');
Storage::mimeType('file.jpg');
Storage::path('file.jpg');                               // chemin absolu (local)
Storage::url('file.jpg');
Storage::temporaryUrl('file.jpg', now()->addMinutes(5));          // S3 : URL signée
Storage::temporaryUploadUrl('file.jpg', now()->addMinutes(5));    // téléversement direct vers S3
```

### 27.3 Dossiers

```php
Storage::files('dossier');           Storage::allFiles('dossier');
Storage::directories('dossier');     Storage::allDirectories('dossier');
Storage::makeDirectory('dossier');   Storage::deleteDirectory('dossier');
```

### 27.4 Visibilité

```php
Storage::put('file.jpg', $contents, 'public');
Storage::getVisibility('file.jpg');
Storage::setVisibility('file.jpg', 'public');            // ou 'private'
```

### 27.5 Téléversements (*uploads*)

```php
public function store(Request $request)
{
    $request->validate(['avatar' => ['required', 'image', 'max:2048']]);

    $path = $request->file('avatar')->store('avatars');                  // nom unique généré
    $path = $request->file('avatar')->store('avatars', 's3');
    $path = $request->file('avatar')->storeAs('avatars', $request->user()->id.'.jpg', 'public');
    $path = Storage::putFile('avatars', $request->file('avatar'));
    $path = Storage::putFileAs('avatars', $request->file('avatar'), 'nom.jpg');
    $request->file('avatar')->storePublicly('avatars', 's3');

    $request->user()->update(['avatar_path' => $path]);
}
```

**Sécurité des uploads**

- **Valider** type MIME, extension, taille et dimensions.
- **Ne jamais faire confiance** au nom fourni (`getClientOriginalName`) : utiliser le nom généré.
- Stocker **hors du dossier public** ou sur un disque dédié ; servir via un contrôleur ou une URL signée si privé.
- Limites serveur : `upload_max_filesize` et `post_max_size` (php.ini), `client_max_body_size` (Nginx).

### 27.6 Disques personnalisés et SFTP

```php
// config/filesystems.php
'disks' => [
    'photos' => ['driver' => 'local', 'root' => storage_path('app/photos'), 'visibility' => 'public', 'url' => env('APP_URL').'/photos'],
    'sftp'   => ['driver' => 'sftp', 'host' => env('SFTP_HOST'), 'username' => env('SFTP_USERNAME'), 'privateKey' => env('SFTP_PRIVATE_KEY')],
    's3'     => ['driver' => 's3', 'key' => env('AWS_ACCESS_KEY_ID'), 'secret' => env('AWS_SECRET_ACCESS_KEY'), 'region' => env('AWS_DEFAULT_REGION'), 'bucket' => env('AWS_BUCKET'), 'endpoint' => env('AWS_ENDPOINT'), 'use_path_style_endpoint' => true],   // compatible MinIO, R2, DigitalOcean Spaces
],
'links' => [public_path('storage') => storage_path('app/public')],
```

**Disques *scoped*, en lecture seule, pilotes personnalisés** : `Storage::extend(...)`.

### 27.7 Images

Laravel ne traite pas les images nativement : utilisez `intervention/image`, `spatie/image` ou `spatie/laravel-medialibrary` (conversions, collections, images adaptatives).

### 27.8 Streaming et gros fichiers

```php
return Storage::download('big.zip');
return response()->streamDownload(function () { /* … */ }, 'export.csv');
Storage::readStream('file');
Storage::writeStream('file', $stream);
```

### 27.9 Tests

```php
Storage::fake('avatars');
$file = UploadedFile::fake()->image('avatar.jpg', 600, 600)->size(100);
$this->post('/avatar', ['avatar' => $file]);
Storage::disk('avatars')->assertExists($file->hashName());
Storage::disk('avatars')->assertMissing('missing.jpg');
UploadedFile::fake()->create('document.pdf', 500, 'application/pdf');
```

### 27.10 Pièges fréquents

- **Oublier `storage:link`** : les URL publiques donnent 404.
- **Stocker un fichier privé sur le disque `public`** : accessible à tous.
- **Croire le MIME du client** : valider côté serveur (`mimes`, `mimetypes`).
- **Fichier remplacé sans suppression de l'ancien** : le disque se remplit.
- **Chemin construit avec une entrée utilisateur** : *path traversal* (`../`).
- **Limites PHP/Nginx trop basses** : l'upload échoue avant même d'atteindre Laravel.

### Synthèse du chapitre 27

L'API **`Storage`** (Flysystem) unifie disques `local`, `public` et cloud (`s3`). Pour les **uploads** : validez, laissez Laravel générer le nom, stockez hors du public si privé, servez via **URL temporaire**. Pensez à `storage:link`, à la **visibilité** et à `Storage::fake()` en test.

---

# Partie VIII — API, outillage, qualité et sécurité

## 28. API et ressources

**Objectifs d'apprentissage.** Rappeler les principes REST ; activer les routes API ; formater les réponses avec les API Resources ; produire des erreurs cohérentes ; authentifier une API ; limiter le débit ; paginer, filtrer, trier ; versionner ; configurer CORS ; consommer des API externes avec le client HTTP ; documenter.

### 28.1 Principes d'une API REST

**REST** (*Representational State Transfer*) est un style d'architecture où les **ressources** sont identifiées par des URL, manipulées par les verbes HTTP, de façon **sans état** (chaque requête contient tout le nécessaire, typiquement un jeton).

| Action | Requête | Code de succès |
| --- | --- | --- |
| Lister | `GET /api/articles` | 200 |
| Lire | `GET /api/articles/1` | 200 |
| Créer | `POST /api/articles` | 201 (+ `Location`) |
| Remplacer | `PUT /api/articles/1` | 200 |
| Modifier | `PATCH /api/articles/1` | 200 |
| Supprimer | `DELETE /api/articles/1` | 204 |

Format de données : **JSON**. Négociation par `Accept: application/json`.

### 28.2 Activer les routes API

```bash
php artisan install:api      # crée routes/api.php, installe Sanctum, ajoute la migration des jetons
```

Les routes de `routes/api.php` reçoivent le préfixe `/api` et le groupe de middleware `api` (sans session ni CSRF).

```php
// routes/api.php
Route::apiResource('articles', ArticleController::class);
Route::prefix('v1')->group(function () { /* … */ });
Route::middleware('auth:sanctum')->group(function () { /* … */ });
```

### 28.3 API Resources : couche de transformation

Une **Resource** convertit un modèle en tableau JSON et **découple** le schéma de la base de la réponse publique.

```bash
php artisan make:resource UserResource
php artisan make:resource UserCollection          # ou UserResource::collection()
```

```php
// app/Http/Resources/UserResource.php
class UserResource extends JsonResource
{
    public function toArray(Request $request): array
    {
        return [
            'id'          => $this->id,
            'name'        => $this->name,
            'email'       => $this->email,
            'posts'       => PostResource::collection($this->whenLoaded('posts')),
            'posts_count' => $this->whenCounted('posts'),
            'secret'      => $this->when($request->user()?->isAdmin(), $this->secret),
            'meta'        => $this->mergeWhen($this->isPremium(), ['plan' => $this->plan]),
            'role'        => new RoleResource($this->whenLoaded('role')),
            'pivot'       => $this->whenPivotLoaded('role_user', fn () => $this->pivot->expires_at),
            'created_at'  => $this->created_at->toIso8601String(),
        ];
    }

    public function with(Request $request): array { return ['meta' => ['version' => 'v1']]; }
    public function withResponse(Request $request, JsonResponse $response): void { $response->header('X-Value', 'True'); }
}
```

**Utilisation**

```php
return new UserResource(User::findOrFail($id));
return UserResource::collection(User::paginate(15));            // inclut liens et méta de pagination
return (new UserResource($user))->response()->setStatusCode(201);
return (new UserCollection(User::all()))->additional(['status' => 'ok']);
```

**Enveloppe `data`.** Par défaut, la réponse est enveloppée dans `{"data": …}`. Pour la supprimer : `JsonResource::withoutWrapping();` (dans `AppServiceProvider::boot()`).

**Conditions utiles** : `when`, `whenLoaded`, `whenCounted`, `whenAggregated`, `whenHas`, `whenNotNull`, `mergeWhen`, `whenPivotLoaded`.

> **Note de version.** Laravel 13 ajoute des **ressources conformes à la spécification JSON:API**. Consultez la documentation de votre version pour leur usage exact.

### 28.4 Réponses d'erreur et codes cohérents

```php
// bootstrap/app.php, dans withExceptions
$exceptions->render(function (ModelNotFoundException $e, Request $request) {
    if ($request->expectsJson()) {
        return response()->json(['message' => 'Ressource introuvable.'], 404);
    }
});
$exceptions->shouldRenderJsonWhen(fn (Request $request, Throwable $e) => $request->is('api/*') || $request->expectsJson());
```

Format d'erreur recommandé (ou **RFC 7807 / Problem Details**) : `{ "message": "…", "errors": {…}, "code": "…" }`.

| Situation | Code |
| --- | --- |
| Validation | **422** |
| Non authentifié | **401** |
| Non autorisé | **403** |
| Limite de débit | **429** |

### 28.5 Authentification d'API

- **Sanctum** (jetons personnels et SPA) : chapitre 15, section 15.15.
- **Passport** (OAuth2).
- **JWT** via un package (`tymon/jwt-auth`, `php-open-source-saver/jwt-auth`).

### 28.6 Limitation de débit

```php
// AppServiceProvider::boot()
RateLimiter::for('api', fn (Request $request) =>
    $request->user()
        ? Limit::perMinute(120)->by($request->user()->id)
        : Limit::perMinute(30)->by($request->ip()));
```

`->middleware('throttle:api')`. En-têtes de réponse : `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `Retry-After`.

### 28.7 Pagination, filtrage, tri, inclusions

```php
public function index(Request $request)
{
    $articles = Article::query()
        ->when($request->search, fn ($q, $s) => $q->where('title', 'like', "%{$s}%"))
        ->when($request->status, fn ($q, $s) => $q->where('status', $s))
        ->orderBy($request->input('sort', 'created_at'), $request->input('dir', 'desc'))
        ->with($request->boolean('include_author') ? ['author'] : [])
        ->paginate($request->integer('per_page', 15))
        ->withQueryString();

    return ArticleResource::collection($articles);
}
```

> **Attention.** Le tri dynamique par `$request->sort` doit passer par une **liste blanche** de colonnes (chapitre 33).

Package utile : **`spatie/laravel-query-builder`** (`?filter[name]=x&sort=-created_at&include=posts`).

### 28.8 Versionnement

- **Par URL** (`/api/v1/…`, recommandé pour sa simplicité).
- **Par en-tête** (`Accept: application/vnd.app.v2+json`).
- **Par paramètre**.

Gardez des Resources et contrôleurs **séparés par version** : `App\Http\Controllers\Api\V1`.

### 28.9 CORS

`config/cors.php` : `paths`, `allowed_origins`, `allowed_methods`, `allowed_headers`, `supports_credentials`. Nécessaire quand le front est sur un **autre domaine**.

### 28.10 Client HTTP (consommer des API)

```php
use Illuminate\Support\Facades\Http;

$response = Http::get('https://api.example.com/users', ['page' => 1]);
$response = Http::withHeaders(['X-First' => 'foo'])
    ->withToken($token)
    ->acceptJson()
    ->timeout(10)
    ->connectTimeout(3)
    ->retry(3, 100, throw: false)
    ->baseUrl('https://api.example.com')
    ->post('/users', ['name' => 'Taylor']);

$response->body(); $response->json(); $response->json('data.0.name'); $response->object(); $response->collect();
$response->status(); $response->ok(); $response->successful(); $response->failed();
$response->clientError(); $response->serverError(); $response->header('X-X');
$response->throw();                          // lève RequestException en cas d'échec
$response->onError(fn ($r) => /* … */);

// Données multipart / fichiers
Http::attach('attachment', file_get_contents('photo.jpg'), 'photo.jpg')->post(/* … */);
Http::asForm()->post(/* … */);   Http::asMultipart();   Http::withBody($xml, 'text/xml');

// Requêtes concurrentes
$responses = Http::pool(fn (Pool $pool) => [
    $pool->as('first')->get('https://a'),
    $pool->as('second')->get('https://b'),
]);

// Macros / clients nommés
Http::macro('github', fn () => Http::withToken(config('services.github.token'))->baseUrl('https://api.github.com'));
Http::github()->get('/repos/laravel/framework');

// Tests
Http::fake(['github.com/*' => Http::response(['foo' => 'bar'], 200), '*' => Http::response('…', 500)]);
Http::assertSent(fn (Request $r) => $r->url() === '…');
Http::preventStrayRequests();
```

### 28.11 Documentation d'API

**OpenAPI / Swagger** : `dedoc/scramble`, `l5-swagger`, `knuckleswtf/scribe` génèrent la documentation à partir du code.

### 28.12 Bonnes pratiques

- **Resources** pour toute réponse.
- **Codes HTTP exacts**.
- **Pagination** systématique des listes.
- `Idempotency-Key` pour les créations sensibles (paiement).
- **Versionner** dès le début.
- Ne pas exposer d'identifiants séquentiels s'ils sont sensibles (UUID / ULID).
- **Documenter** et **tester**.

### 28.13 Pièges fréquents

- **Retourner directement un modèle** : expose des champs non voulus ; passez par une Resource.
- **N+1 dans une Resource** : utilisez `whenLoaded` et chargez les relations dans le contrôleur.
- **Oublier `Accept: application/json`** : les erreurs de validation redirigent au lieu de répondre en 422.
- **Pas de timeout sur le client HTTP** : un service tiers lent bloque votre requête.
- **Erreurs en HTML** pour une API : configurez `shouldRenderJsonWhen`.

### Synthèse du chapitre 28

Une API Laravel combine routes `api.php`, **Resources** (format stable et découplé), **Form Requests** (422), authentification **Sanctum**, **throttling**, **pagination/filtrage/tri**, **versionnement**, **CORS** et erreurs JSON cohérentes. Le **client `Http`** (timeouts, `retry`, `pool`, `fake`) sert à consommer d'autres API.

---

## 29. Artisan et commandes console

**Objectifs d'apprentissage.** Utiliser Artisan et connaître ses commandes essentielles ; explorer avec Tinker ; créer des commandes personnalisées (signature, arguments, options) ; gérer entrées et sorties, Laravel Prompts ; appeler des commandes ; gérer l'isolation et les signaux ; tester les commandes.

### 29.1 Présentation

**Artisan** est l'interface en ligne de commande de Laravel (`php artisan`), fondée sur **Symfony Console**. Elle sert à **générer du code**, exécuter migrations, queues, tâches planifiées, et vos propres scripts.

```bash
php artisan list
php artisan help migrate
php artisan --version
php artisan about
php artisan env
```

### 29.2 Commandes essentielles

| Domaine | Commandes |
| --- | --- |
| **Génération** | `make:model`, `make:controller`, `make:migration`, `make:request`, `make:resource`, `make:middleware`, `make:policy`, `make:event`, `make:listener`, `make:job`, `make:mail`, `make:notification`, `make:observer`, `make:rule`, `make:seeder`, `make:factory`, `make:command`, `make:component`, `make:provider`, `make:test`, `make:enum`, `make:class`, `make:interface`, `make:trait`, `make:scope`, `make:view`, `make:cast`, `make:channel`, `make:exception`, `make:lang` |
| **Base de données** | `migrate`, `migrate:rollback`, `migrate:fresh`, `migrate:status`, `db:seed`, `db:show`, `db:table`, `db:wipe`, `model:show`, `model:prune`, `schema:dump` |
| **Cache et optimisation** | `optimize`, `optimize:clear`, `config:cache`, `route:cache`, `view:cache`, `event:cache`, `cache:clear` |
| **Queue** | `queue:work`, `queue:listen`, `queue:retry`, `queue:failed`, `queue:restart`, `queue:monitor` |
| **Scheduler** | `schedule:run`, `schedule:work`, `schedule:list` |
| **Divers** | `serve`, `tinker`, `route:list`, `storage:link`, `key:generate`, `down`, `up`, `vendor:publish`, `lang:publish`, `install:api`, `install:broadcasting`, `config:publish`, `stub:publish`, `event:list`, `pail`, `test` |

**Options des commandes `make:*`** : `--force` (écrase), `--help`, et des drapeaux spécifiques (`-m`, `-f`, `-r`, `--api`, `--invokable`, `--pest`, `--unit`…).

**Stubs personnalisables** : `php artisan stub:publish` copie les gabarits dans `stubs/` pour adapter le code généré.

### 29.3 Tinker (REPL)

```bash
php artisan tinker
>>> User::count()
>>> $u = User::factory()->create()
>>> $u->posts()->create(['title' => 'X'])
>>> Cache::get('key')
>>> app(Service::class)->handle()
```

Idéal pour tester rapidement requêtes, relations et services.

### 29.4 Créer une commande personnalisée

```bash
php artisan make:command SendEmails
```

```php
// app/Console/Commands/SendEmails.php
use Illuminate\Console\Command;
use Symfony\Component\Console\Attribute\AsCommand;

#[AsCommand(name: 'mail:send', description: 'Envoie les e-mails programmés')]
class SendEmails extends Command
{
    protected $signature = 'mail:send {user : ID de l\'utilisateur} {--queue= : Nom de la file} {--force}';

    public function handle(DripEmailer $drip): int
    {
        $user  = User::findOrFail($this->argument('user'));
        $queue = $this->option('queue');

        $drip->send($user);

        $this->info('Terminé !');
        return Command::SUCCESS;                   // 0 ; Command::FAILURE = 1
    }
}
```

**Syntaxe de la signature**

| Forme | Signification |
| --- | --- |
| `{user}` | Argument obligatoire |
| `{user?}` | Argument optionnel |
| `{user=foo}` | Argument avec valeur par défaut |
| `{user*}` | Argument tableau (plusieurs valeurs) |
| `{--queue}` | Option booléenne (drapeau) |
| `{--queue=}` | Option avec valeur |
| `{--queue=default}` | Option avec défaut |
| `{--Q\|queue}` | Option avec raccourci |
| `{--id=*}` | Option tableau |
| `{user : description}` | Avec description |

**Commande en closure** (dans `routes/console.php`) :

```php
Artisan::command('mail:send {user}', function (string $user) {
    $this->info("Envoi à {$user}");
})->purpose('Envoie un mail');
```

### 29.5 Entrées et sorties

```php
$this->argument('user');   $this->arguments();
$this->option('queue');    $this->options();
$this->hasArgument('x');   $this->hasOption('x');

// Interactions
$name = $this->ask('Quel est votre nom ?');
$pw   = $this->secret('Mot de passe ?');
$ok   = $this->confirm('Continuer ?', true);
$c    = $this->choice('Couleur ?', ['rouge', 'bleu'], 0);
$n    = $this->anticipate('Nom ?', ['Taylor', 'Dayle']);

// Sorties
$this->line('Ligne');   $this->info('Info');   $this->comment('Commentaire');
$this->question('Question');   $this->warn('Attention');   $this->error('Erreur');
$this->newLine(2);      $this->alert('Alerte');
$this->table(['Nom', 'Email'], User::all(['name', 'email'])->toArray());

// Barre de progression
$this->withProgressBar($users, fn ($user) => $this->process($user));
$bar = $this->output->createProgressBar(count($users));
$bar->start(); foreach ($users as $u) { /* … */ $bar->advance(); } $bar->finish();
```

**Verbosité** : `-v`, `-vv`, `-vvv` ; `$this->line($msg, null, 'v')`.

### 29.6 Laravel Prompts *(ajout)*

Interfaces CLI modernes avec validation, texte indicatif et autocomplétion :

```php
use function Laravel\Prompts\{text, password, confirm, select, multiselect, suggest, search, multisearch, pause, spin, progress, info, warning, error, table, note, alert};

$name   = text(label: 'Nom ?', placeholder: 'Jean', required: true, validate: fn ($v) => strlen($v) < 3 ? 'Trop court' : null);
$role   = select('Rôle ?', ['admin', 'user'], default: 'user');
$perms  = multiselect('Permissions', ['read', 'write', 'delete']);
$result = spin(fn () => $this->longTask(), 'Traitement…');
```

### 29.7 Appel de commandes

```php
$this->call('mail:send', ['user' => 1, '--queue' => 'default']);
$this->callSilently(/* … */);

Artisan::call('mail:send', ['user' => 1]);       // depuis du code (déconseillé : préférer un service)
Artisan::queue('mail:send', ['user' => 1])->onQueue('commands');
```

### 29.8 Enregistrement et isolation

Les commandes de `app/Console/Commands` sont **auto-découvertes**. **Isolation** (une seule instance à la fois) : `implements Isolatable` + option `--isolated`. **Interdiction** de commandes destructrices en production : `DB::prohibitDestructiveCommands(app()->isProduction())`.

### 29.9 Signaux et gestion de fin

`$this->trap([SIGTERM, SIGINT], fn () => /* … */)` permet de terminer proprement.

### 29.10 Tester les commandes

```php
$this->artisan('mail:send 1')
     ->expectsQuestion('Quel est votre nom ?', 'Taylor')
     ->expectsConfirmation('Continuer ?', 'yes')
     ->expectsOutput('Terminé !')
     ->assertExitCode(0);
```

### 29.11 Pièges fréquents

- **Logique métier dans la commande** : extraire un service/action réutilisable aussi par HTTP.
- **Oublier le code de retour** : les scripts et le CI se fient à `0` / `1`.
- **Commande longue sans `Isolatable`** : exécutions concurrentes.
- **`Artisan::call` depuis un contrôleur** : lent et peu testable.
- **`migrate:fresh` accidentel en production** : verrouiller avec `prohibitDestructiveCommands`.

### Synthèse du chapitre 29

**Artisan** génère (`make:*`), migre, planifie et diagnostique. **Tinker** explore l'application. Une commande personnalisée se définit par sa **signature** (`{arg}`, `{--option}`), sa méthode `handle()` et un **code de retour** ; **Laravel Prompts** soigne l'interactivité ; `artisan()` en test vérifie questions, sorties et code.

---

## 30. Tests

**Objectifs d'apprentissage.** Justifier les tests ; distinguer tests unitaires, Feature et navigateur ; exécuter la suite ; écrire des tests avec PHPUnit et Pest ; envoyer des requêtes de test et utiliser les assertions HTTP ; gérer la base de données de test ; isoler les effets de bord avec les fakes et les mocks ; tester commandes, vues ; connaître Dusk ; intégrer en CI.

### 30.1 Pourquoi tester ?

Les tests garantissent la **non-régression**, **documentent** le comportement et permettent de **refactorer en confiance**. Laravel intègre **PHPUnit** et propose **Pest** (syntaxe expressive, choix par défaut des nouveaux projets).

### 30.2 Types de tests

| Type | Portée | Dossier |
| --- | --- | --- |
| **Unitaire** | Une classe/fonction isolée, sans framework lourd | `tests/Unit` |
| **Feature (fonctionnel)** | Plusieurs composants : requête HTTP, base de données | `tests/Feature` |
| **Navigateur** (Dusk) | Parcours utilisateur réel dans un navigateur | `tests/Browser` |

### 30.3 Exécution

```bash
php artisan test
php artisan test --parallel
php artisan test --filter=UserTest
php artisan test --testsuite=Feature
php artisan test --stop-on-failure
php artisan test --coverage --min=80
php artisan test --profile
php artisan make:test UserTest              # Feature
php artisan make:test UserTest --unit
php artisan make:test UserTest --pest
```

**`phpunit.xml`** définit les variables d'environnement de test : `APP_ENV=testing`, `DB_DATABASE=:memory:` (SQLite en mémoire), `CACHE_STORE=array`, `QUEUE_CONNECTION=sync`, `MAIL_MAILER=array`, `SESSION_DRIVER=array`.

### 30.4 Test Feature (PHPUnit)

```php
// tests/Feature/PostTest.php
use Illuminate\Foundation\Testing\RefreshDatabase;

class PostTest extends TestCase
{
    use RefreshDatabase;

    public function test_authenticated_user_can_create_post(): void
    {
        $user = User::factory()->create();

        $response = $this->actingAs($user)->post('/posts', ['title' => 'Salut', 'body' => 'Contenu']);

        $response->assertRedirect('/posts');
        $this->assertDatabaseHas('posts', ['title' => 'Salut', 'user_id' => $user->id]);
    }

    public function test_guest_cannot_create_post(): void
    {
        $this->post('/posts', [])->assertRedirect('/login');
    }
}
```

### 30.5 Pest

```php
// tests/Feature/PostTest.php
use function Pest\Laravel\{actingAs, get, post, assertDatabaseHas};

it('creates a post', function () {
    $user = User::factory()->create();

    actingAs($user)->post('/posts', ['title' => 'Salut', 'body' => 'x'])
        ->assertRedirect('/posts');

    assertDatabaseHas('posts', ['title' => 'Salut']);
});

test('guest is redirected', fn () => get('/dashboard')->assertRedirect('/login'));

it('validates', function (array $data, string $field) {
    actingAs(User::factory()->create())->post('/posts', $data)->assertInvalid($field);
})->with([
    'sans titre' => [['body' => 'x'], 'title'],
    'sans corps' => [['title' => 'x'], 'body'],
]);

beforeEach(fn () => $this->user = User::factory()->create());
expect($value)->toBe(1)->toBeInt()->toBeGreaterThan(0);
uses(RefreshDatabase::class)->in('Feature');
arch()->expect('App\Models')->toExtend(Model::class);        // tests d'architecture
```

### 30.6 Requêtes HTTP de test

```php
$this->get('/'); $this->post('/x', $data); $this->put(/* … */); $this->patch(/* … */); $this->delete(/* … */);
$this->getJson('/api/x'); $this->postJson('/api/x', $data); $this->putJson(/* … */); $this->patchJson(/* … */); $this->deleteJson(/* … */);
$this->withHeaders(['X-Header' => 'v'])->post(/* … */);
$this->withCookie('c', 'v')->get(/* … */);
$this->withSession(['k' => 'v'])->get(/* … */);
$this->followingRedirects()->get(/* … */);
$this->withoutMiddleware(); $this->withoutExceptionHandling();
$this->from('/previous')->post(/* … */);
$this->actingAs($user, 'web');
Sanctum::actingAs($user, ['*']);
```

### 30.7 Assertions HTTP

```php
->assertOk() ->assertCreated() ->assertAccepted() ->assertNoContent()
->assertNotFound() ->assertForbidden() ->assertUnauthorized() ->assertUnprocessable()
->assertStatus(200) ->assertSuccessful() ->assertRedirect($uri) ->assertRedirectToRoute('x')
->assertSee('texte') ->assertSeeText ->assertDontSee ->assertSeeInOrder([/* … */])
->assertHeader('X', 'v') ->assertCookie('n', 'v') ->assertSessionHas('k', 'v')
->assertSessionHasErrors(['email']) ->assertSessionHasNoErrors()
->assertViewIs('home') ->assertViewHas('key', 'value') ->assertViewHasAll([/* … */])
->assertJson(['created' => true]) ->assertExactJson([/* … */]) ->assertJsonPath('data.0.id', 1)
->assertJsonStructure(['data' => ['*' => ['id', 'name']]]) ->assertJsonCount(3, 'data')
->assertJsonFragment([/* … */]) ->assertJsonMissing([/* … */]) ->assertJsonValidationErrors(['name'])
->assertInvalid(['email']) ->assertValid() ->assertDownload('file.pdf')
->assertStreamed()
->assertJson(fn (AssertableJson $json) => $json->has('data', 3)->has('data.0', fn ($j) => $j->where('id', 1)->etc()));
```

### 30.8 Base de données

| Trait | Effet |
| --- | --- |
| `RefreshDatabase` | Migre une fois, puis enveloppe chaque test dans une transaction annulée (**recommandé**) |
| `DatabaseMigrations` | Migre / annule à chaque test (lent) |
| `DatabaseTransactions` | Transaction par test, sans migrer |
| `LazilyRefreshDatabase` | Comme `RefreshDatabase` mais seulement si la base est utilisée |

**Assertions**

```php
$this->assertDatabaseHas('users', ['email' => 'x']);
$this->assertDatabaseMissing('users', [/* … */]);
$this->assertDatabaseCount('users', 5);
$this->assertDatabaseEmpty('users');
$this->assertSoftDeleted($user);   $this->assertNotSoftDeleted($user);
$this->assertModelExists($user);   $this->assertModelMissing($user);
```

### 30.9 Fakes (isoler les effets de bord)

```php
Mail::fake();            Mail::assertSent(Welcome::class, 1);   Mail::assertQueued(/* … */);
Notification::fake();    Notification::assertSentTo($user, X::class);
Queue::fake();           Queue::assertPushed(X::class);
Bus::fake();             Bus::assertDispatched(X::class);
Event::fake();           Event::assertDispatched(X::class);
Storage::fake('local');  Storage::disk('local')->assertExists('f');
Http::fake();            Http::assertSent(fn ($r) => /* … */);
Process::fake();         Process::assertRan('ls');
Cache::spy();            Log::spy();
Sleep::fake();           Sleep::assertSlept(/* … */);
Exceptions::fake();      Exceptions::assertReported(X::class);

// Temps
$this->travel(5)->days(); $this->travelTo(now()->addWeek()); $this->freezeTime(); $this->travelBack();
Carbon::setTestNow('2026-01-01');
```

### 30.10 Mocking

```php
$this->mock(PaymentGateway::class, function (MockInterface $mock) {
    $mock->shouldReceive('charge')->once()->with(100)->andReturn(true);
});
$this->partialMock(Service::class, fn ($m) => $m->shouldReceive('x')->andReturn(1));
$this->spy(Service::class);
$this->instance(Service::class, Mockery::mock(Service::class, /* … */));
```

### 30.11 Tests unitaires

```php
class PriceCalculatorTest extends PHPUnit\Framework\TestCase     // sans amorçage de Laravel (rapide)
{
    public function test_applies_discount(): void
    {
        $this->assertSame(90.0, (new PriceCalculator)->apply(100, 10));
    }
}
```

Utilisez `Tests\TestCase` si vous avez besoin du conteneur ou des facades.

### 30.12 Tests de commandes, de vues et de composants

```php
$this->artisan('inspire')->assertExitCode(0);
$view = $this->view('welcome', ['name' => 'X']); $view->assertSee('X');
$this->blade('<x-alert/>')->assertSee('…');
$this->component(Alert::class, ['type' => 'x'])->assertSee('…');
```

### 30.13 Laravel Dusk (navigateur)

```bash
composer require laravel/dusk --dev
php artisan dusk:install
php artisan dusk
```

```php
$this->browse(function (Browser $browser) {
    $browser->visit('/login')->type('email', 'a@b.c')->type('password', 'secret')
            ->press('Login')->assertPathIs('/home')->assertSee('Tableau de bord');
});
```

Alternatives : **Playwright**, **Cypress**, **Pest Browser Testing**.

### 30.14 Couverture, parallélisme, intégration continue

- **Couverture** : Xdebug ou PCOV, option `--coverage`.
- **Parallèle** : `--parallel` (une base par processus).
- **CI** : GitHub Actions / GitLab CI exécutant `composer install`, `php artisan test`, Pint, Larastan.

### 30.15 Bonnes pratiques

- **AAA** : *Arrange, Act, Assert*.
- **Un test = un comportement.**
- **Nommer explicitement** (`test_user_cannot_delete_foreign_post`).
- Utiliser des **factories**, pas de fixtures statiques.
- Tester les **cas d'erreur** et les **limites**.
- Tests **rapides** et **indépendants** (aucun ordre requis).
- **TDD** : écrire le test avant le code quand c'est possible.

### 30.16 Pièges fréquents

- **Tests dépendants de l'ordre** ou d'un état partagé.
- **Oublier `RefreshDatabase`** : données qui fuient d'un test à l'autre.
- **Appels réseau réels** : `Http::preventStrayRequests()` les interdit.
- **Tester l'implémentation** (méthodes privées) plutôt que le comportement.
- **Heure réelle** dans un test : utiliser `freezeTime` / `travel`.
- **Mock excessif** : un test qui mocke tout ne prouve plus rien.

### Synthèse du chapitre 30

Testez au niveau **Feature** (HTTP + base) et **Unit**, avec **Pest** ou PHPUnit. `RefreshDatabase`, factories, `actingAs`, assertions HTTP/JSON/base, **fakes** (`Mail`, `Queue`, `Event`, `Http`, `Storage`…) et mocks isolent les effets de bord. Exécutez en **parallèle** et en **CI**, nommez par comportement, suivez **AAA**.

---

## 31. Logging et gestion des erreurs

**Objectifs d'apprentissage.** Configurer la journalisation (canaux, niveaux, contexte, `stack`) ; écrire des logs structurés ; comprendre le gestionnaire d'exceptions (`report`, `render`) configuré dans `bootstrap/app.php` ; créer des exceptions personnalisées ; personnaliser les pages d'erreur ; déboguer (dd, Telescope, Debugbar, Pulse) ; configurer le mode production.

### 31.1 Logging

Fondé sur **Monolog**, avec la notion de **canaux** (*channels*) définis dans `config/logging.php`. Variables : `LOG_CHANNEL`, `LOG_LEVEL`, `LOG_STACK`.

**Canaux** : `single` (un fichier), `daily` (rotation quotidienne, option `days`), `stack` (agrège plusieurs canaux), `slack`, `papertrail`, `syslog`, `errorlog`, `stderr`, `stdout`, `monolog` (personnalisé), `custom`, `null`, `emergency`.

**Niveaux (RFC 5424)**, du plus grave au moins grave :

| Niveau | Usage typique |
| --- | --- |
| `emergency` | Système inutilisable |
| `alert` | Action immédiate requise |
| `critical` | Condition critique |
| `error` | Erreur d'exécution |
| `warning` | Situation anormale non bloquante |
| `notice` | Événement normal mais significatif |
| `info` | Information |
| `debug` | Détail de débogage |

```php
use Illuminate\Support\Facades\Log;

Log::emergency($message); Log::alert($message); Log::critical($message); Log::error($message);
Log::warning($message);   Log::notice($message); Log::info($message);     Log::debug($message);

Log::info('Utilisateur connecté', ['id' => $user->id]);           // contexte
Log::withContext(['request_id' => $id]);                           // contexte persistant
Log::shareContext([/* … */]);                                      // partagé entre canaux
Log::channel('slack')->critical('Paiement KO');
Log::stack(['single', 'slack'])->info('…');
Log::build(['driver' => 'single', 'path' => storage_path('logs/custom.log')])->info('…');
logger('Message');  logger()->error('…');  info('…');
```

**Personnaliser le format** (*tap*) :

```php
// config/logging.php
'single' => ['driver' => 'single', 'tap' => [App\Logging\CustomizeFormatter::class], /* … */]
```

**Journal en temps réel** : `php artisan pail` (options `--filter`, `--level`, `--user`).

**Bonnes pratiques** : journaliser avec un **contexte structuré** (JSON), **ne jamais** consigner mots de passe, jetons ou données personnelles sensibles, **centraliser** (ELK, Datadog, Papertrail, Sentry), prévoir la **rotation** (`daily`).

### 31.2 Gestion des erreurs et exceptions

Toute exception passe par le **gestionnaire d'exceptions** configuré dans `bootstrap/app.php` :

```php
// bootstrap/app.php
->withExceptions(function (Exceptions $exceptions) {
    // Reporter (journaliser / notifier)
    $exceptions->report(function (InvalidOrderException $e) { /* envoyer à Sentry */ });
    $exceptions->report(function (Throwable $e) { /* … */ })->stop();     // empêche le report par défaut
    $exceptions->dontReport([InvalidOrderException::class]);
    $exceptions->dontReportDuplicates();
    $exceptions->throttle(fn (Throwable $e) => Limit::perMinute(10));       // limiter le report
    $exceptions->context(fn () => ['app' => 'x']);
    $exceptions->level(PDOException::class, LogLevel::CRITICAL);

    // Rendre (convertir en réponse)
    $exceptions->render(function (InvalidOrderException $e, Request $request) {
        return response()->view('errors.invalid-order', status: 500);
    });
    $exceptions->render(function (NotFoundHttpException $e, Request $request) {
        if ($request->is('api/*')) return response()->json(['message' => 'Introuvable.'], 404);
    });
    $exceptions->shouldRenderJsonWhen(fn (Request $request, Throwable $e) => $request->is('api/*'));
    $exceptions->respond(fn (Response $response) => $response->getStatusCode() === 419
        ? back()->with('message', 'Page expirée.')
        : $response);
})
```

> **Héritage.** Avant Laravel 11, ces réglages se faisaient dans `app/Exceptions/Handler.php` (propriétés `$dontReport`, méthodes `register`, `report`, `render`).

**Exceptions personnalisées**

```php
// app/Exceptions/InvalidOrderException.php
class InvalidOrderException extends Exception
{
    public function report(): void { /* rapport personnalisé */ }
    public function render(Request $request): Response { return response(/* … */); }
    public function context(): array { return ['order_id' => $this->orderId]; }
}
```

**Helpers**

```php
report($e);                          // reporter sans interrompre
rescue(fn () => risky(), fn ($e) => 'repli');
throw_if($cond, Exception::class, 'msg');  throw_unless(/* … */);
abort(404);  abort(403, 'Interdit');  abort_if($cond, 403);  abort_unless($cond, 403);
```

**Pages d'erreur HTTP.** Créez `resources/views/errors/404.blade.php`, `500.blade.php`, `503.blade.php`, `419.blade.php`, `429.blade.php`. `$exception` et `$exception->getMessage()` sont disponibles. `php artisan vendor:publish --tag=laravel-errors` publie les modèles.

**Exceptions courantes**

| Exception | Cause | Code |
| --- | --- | --- |
| `ModelNotFoundException` | `findOrFail`, route binding | 404 |
| `NotFoundHttpException` | Route inconnue | 404 |
| `ValidationException` | Validation échouée | 422 / redirection |
| `AuthenticationException` | Non connecté | 401 / redirection vers login |
| `AuthorizationException` | Autorisation refusée | 403 |
| `TokenMismatchException` | Jeton CSRF invalide | 419 |
| `ThrottleRequestsException` | Trop de requêtes | 429 |
| `MethodNotAllowedHttpException` | Mauvais verbe | 405 |
| `QueryException` | Erreur SQL | 500 |

### 31.3 Débogage

- `APP_DEBUG=true` (développement) → page d'erreur détaillée (Ignition / Spatie).
- `dd($x)` (*dump & die*), `dump($x)`, `ddd`, `Log::debug`.
- `$request->dd()`, `$collection->dd()`.
- **Telescope** : requêtes, jobs, mails, exceptions, requêtes SQL, cache.
- **Debugbar** : barre de débogage (requêtes, chronologie).
- **Xdebug** : débogage pas à pas.
- **Laravel Pulse** : surveillance en production.
- **Sentry / Flare / Bugsnag** : suivi d'erreurs en production.

### 31.4 Mode production

`APP_DEBUG=false`, `APP_ENV=production`, `LOG_LEVEL=warning` ou `error`.

### 31.5 Pièges fréquents

- **`APP_DEBUG=true` en production** : stack traces et variables d'environnement visibles.
- **Avaler une exception** (`catch` vide) : l'erreur disparaît ; au minimum `report($e)`.
- **Logger des données sensibles** : mots de passe, jetons, numéros de carte.
- **`dd()` oublié** dans le code livré : la page s'interrompt.
- **Logs sans rotation** (`single`) : le fichier grossit indéfiniment ; préférez `daily`.
- **Reporter la même exception en boucle** : `dontReportDuplicates`, `throttle`.

### Synthèse du chapitre 31

Les **logs** (Monolog : canaux, niveaux, contexte, `stack`) racontent l'application ; le **gestionnaire d'exceptions** (`withExceptions` : `report` puis `render`) transforme les erreurs en réponses. Créez des exceptions métier avec `report/render`, personnalisez les pages d'erreur, déboguez avec **Telescope/Debugbar/Pulse**, et passez en **`APP_DEBUG=false`** en production.

---

## 32. Localisation

**Objectifs d'apprentissage.** Distinguer i18n et l10n ; organiser les fichiers de traduction (PHP et JSON) ; récupérer et paramétrer les traductions ; gérer le pluriel ; définir et détecter la locale ; traduire les messages du framework ; localiser dates et nombres ; concevoir un site multilingue.

### 32.1 Concepts

La localisation permet de proposer l'application en **plusieurs langues** (i18n, internationalisation) et de formater selon les régions (l10n). Configuration : `APP_LOCALE`, `APP_FALLBACK_LOCALE`, `APP_FAKER_LOCALE`. Publier les fichiers : `php artisan lang:publish`.

### 32.2 Fichiers de traduction

**Fichiers PHP** (`lang/fr/messages.php`) pour des **clés courtes** :

```php
// lang/fr/messages.php
return [
    'welcome'  => 'Bienvenue sur notre site !',
    'greeting' => 'Bonjour, :name !',
];
```

**Fichiers JSON** (`lang/fr.json`) pour des **chaînes complètes** (la clé est le texte source) :

```json
{ "I love programming.": "J'adore programmer." }
```

### 32.3 Récupérer des traductions

```php
echo __('messages.welcome');
echo __('I love programming.');
echo trans('messages.welcome');
Lang::get('messages.welcome');
Lang::has('messages.welcome');
Lang::get('messages.welcome', [], 'fr');        // locale précise
```

```blade
{{ __('messages.welcome') }}
@lang('messages.welcome')
```

**Remplacements**

```php
__('messages.greeting', ['name' => 'Dayle']);
// ':name' → 'Dayle' ; ':NAME' → 'DAYLE' ; ':Name' → 'Dayle' (capitalisation automatique)
```

### 32.4 Pluralisation

```php
'apples' => '{0} Aucune pomme|{1} Une pomme|[2,*] :count pommes',

trans_choice('messages.apples', 10);
trans_choice('messages.apples', 1);
```

Pour les langues à plusieurs formes de pluriel, on exprime les intervalles : `'minutes_ago' => '{1} il y a :value minute|[2,*] il y a :value minutes'`.

### 32.5 Définir et détecter la locale

```php
App::setLocale('fr');
App::getLocale();
App::isLocale('fr');
App::currentLocale();
App::setFallbackLocale('en');
```

**Middleware de détection**

```php
// app/Http/Middleware/SetLocale.php
class SetLocale
{
    public function handle(Request $request, Closure $next)
    {
        $locale = $request->segment(1);                          // /fr/articles
        if (! in_array($locale, config('app.supported_locales'))) {
            $locale = $request->getPreferredLanguage(config('app.supported_locales')) ?? config('app.locale');
        }
        app()->setLocale($locale);
        URL::defaults(['locale' => $locale]);
        return $next($request);
    }
}

Route::prefix('{locale}')->where(['locale' => 'fr|en|mg'])->middleware(SetLocale::class)->group(/* … */);
```

Autres sources : en-tête `Accept-Language`, session, **préférence utilisateur** en base (`HasLocalePreference`).

### 32.6 Traduction des messages du framework

- **Validation** : `lang/fr/validation.php` (messages, `attributes`).
- **Auth** : `lang/fr/auth.php` ; **Pagination** : `lang/fr/pagination.php` ; **Mots de passe** : `lang/fr/passwords.php`.
- Package **`laravel-lang/lang`** : traductions de tout le framework pour de nombreuses langues (`php artisan lang:add fr`).

### 32.7 Dates, nombres, devises

```php
Carbon::setLocale('fr');
now()->translatedFormat('l j F Y');           // « vendredi 13 novembre 2026 »
now()->isoFormat('LLLL');
$date->diffForHumans();                       // « il y a 2 heures »
Number::currency(1500.5, 'EUR', 'fr');
Number::format(1234567.89, locale: 'fr');
Number::percentage(45.5);
```

### 32.8 Localisation dans les mails, notifications, jobs

- `Mail::to($u)->locale('fr')->send(...)`, `->locale()` sur les notifications.
- Interface `Illuminate\Contracts\Translation\HasLocalePreference` sur le modèle.
- `Number::useLocale('fr')`, `Number::withLocale('fr', fn () => ...)`.

### 32.9 Stratégies pour sites multilingues

- **URL** : `/fr/…` (recommandé pour le SEO) ou sous-domaine `fr.site.com`.
- **Contenu en base** : `spatie/laravel-translatable` (colonnes JSON), `astrotomic/laravel-translatable` (tables de traductions).
- `hreflang`, attribut `lang` sur `<html>`, plan de site multilingue.

### 32.10 Pièges fréquents

- **Clé manquante** : l'interface affiche la clé brute (`messages.welcome`) ; définissez une locale de repli.
- **Concaténer des phrases** au lieu d'utiliser des substituts : impossible à traduire correctement.
- **Locale non remise à zéro** dans un job ou une queue : utilisez `->locale()` / `withLocale`.
- **Pluriel codé en dur** (`s`) : utilisez `trans_choice`.
- **Oublier `lang:publish`** : le dossier `lang/` n'existe pas dans le squelette récent.

### Synthèse du chapitre 32

Traduisez avec `lang/xx/*.php` (clés) ou `lang/xx.json` (phrases), via `__()` / `trans_choice()` et des **substituts** `:name`. Définissez la locale par **middleware** (préfixe d'URL, en-tête, préférence), traduisez aussi **validation/auth**, localisez **dates et nombres** (Carbon, `Number`), et soignez le **SEO** (`hreflang`).

---

## 33. Sécurité

**Objectifs d'apprentissage.** Connaître les protections intégrées de Laravel contre les failles courantes (OWASP) ; maîtriser CSRF, XSS, injection SQL, assignation de masse, IDOR ; appliquer chiffrement, gestion des secrets, sécurité des uploads, en-têtes HTTP, HTTPS ; protéger contre l'abus ; appliquer la checklist avant production.

### 33.1 Principes

Laravel intègre des protections contre les failles courantes (**OWASP Top 10**). Les comprendre permet de **ne pas les contourner par erreur**.

### 33.2 Protection CSRF

**Cross-Site Request Forgery** : un site malveillant déclenche une action à l'insu d'un utilisateur connecté.

**Défense** : un **jeton aléatoire par session**, exigé pour POST/PUT/PATCH/DELETE (middleware `ValidateCsrfToken` du groupe `web`).

```blade
<form method="POST">@csrf …</form>
<meta name="csrf-token" content="{{ csrf_token() }}">
```

```js
// fetch / AJAX
fetch('/x', { method: 'POST', headers: { 'X-CSRF-TOKEN': token } });
// Axios lit automatiquement le cookie XSRF-TOKEN et envoie X-XSRF-TOKEN
```

**Exceptions** (webhooks externes) : `$middleware->validateCsrfTokens(except: ['stripe/*']);`. Jeton invalide → **419**. Les cookies `SameSite=lax` ajoutent une défense.

> **Note de version.** Laravel 13 renforce la protection contre la falsification de requête. Les noms de classes et options exacts peuvent différer de ceux de Laravel 11/12 : consultez le guide de mise à jour avant de migrer.

### 33.3 Protection XSS

**Cross-Site Scripting** : injection de JavaScript dans une page.

- `{{ $var }}` **échappe** automatiquement le HTML.
- `{!! $var !!}` n'échappe pas → **dangereux** ; **purifiez** (HTMLPurifier, par exemple via le package `mews/purifier`) avant affichage.
- Ne pas injecter de données dans `href="javascript:…"` ou `<script>` sans `@json` / `Js::from`.
- Configurer une **Content-Security-Policy** (middleware ou package `spatie/laravel-csp`).

### 33.4 Injection SQL

- Eloquent et le Query Builder utilisent des **requêtes préparées** (PDO).
- **À éviter** : concaténer des entrées dans `DB::raw`, `whereRaw`, `orderByRaw`, `selectRaw` sans liaison.

```php
// Mauvais
User::whereRaw("name = '$name'")->get();
// Bon
User::whereRaw('name = ?', [$name])->get();
// Noms de colonnes dynamiques (tri) : liste blanche
$col = in_array($request->sort, ['name', 'created_at']) ? $request->sort : 'created_at';
```

### 33.5 Assignation de masse

Définir **`$fillable`** (liste blanche). Utiliser `$request->validated()` plutôt que `$request->all()`.

### 33.6 Authentification et mots de passe

- **Hash** Bcrypt / Argon2 (`Hash::make`, cast `hashed`).
- Règles de mots de passe (`Password::defaults`), vérification de fuite (`uncompromised()`).
- **Limitation des tentatives** (*rate limiting*), verrouillage progressif.
- **2FA**, vérification d'e-mail, confirmation de mot de passe.
- Régénérer la session à la connexion (`session()->regenerate()`), l'invalider à la déconnexion.

### 33.7 Autorisation

- **Toujours** vérifier les droits **côté serveur** (Policies / Gates), pas seulement masquer des boutons.
- Prévenir l'**IDOR** (*Insecure Direct Object Reference*) : vérifier que l'objet demandé appartient à l'utilisateur (`$request->user()->posts()->findOrFail($id)`, ou policy).
- Principe du **moindre privilège**.

### 33.8 Chiffrement

```php
use Illuminate\Support\Facades\Crypt;

$encrypted = Crypt::encryptString('secret');
$decrypted = Crypt::decryptString($encrypted);          // DecryptException si invalide
// Cast Eloquent
'api_token' => 'encrypted',
```

Algorithme **AES-256** (CBC ou GCM), clé = `APP_KEY`. **Rotation** : `APP_PREVIOUS_KEYS=old1,old2`. Ne jamais perdre la clé ni la versionner.

### 33.9 Gestion des secrets et de la configuration

- `.env` **hors dépôt** ; variables d'environnement du serveur ou coffre-fort (Vault, secrets manager) en production.
- **`APP_DEBUG=false`** en production (sinon fuite de configuration et de traces).
- Fichiers sensibles **hors de `public/`** ; serveur pointant sur `public/`.
- `composer audit` pour détecter les vulnérabilités des dépendances ; mises à jour régulières (Dependabot / Renovate).

### 33.10 Fichiers et uploads

- Valider MIME, extension et taille ; générer des **noms aléatoires** ; stocker **hors du webroot** ; **ne jamais exécuter** de fichiers téléversés ; désactiver l'exécution PHP dans les dossiers d'upload.
- Éviter le **path traversal** (`../`) : n'utilisez pas une entrée utilisateur dans un chemin sans nettoyage (`basename`).

### 33.11 En-têtes HTTP de sécurité

| En-tête | Rôle |
| --- | --- |
| `Strict-Transport-Security` | Force HTTPS (HSTS) |
| `Content-Security-Policy` | Limite les sources de scripts et de styles |
| `X-Content-Type-Options: nosniff` | Empêche le *MIME sniffing* |
| `X-Frame-Options` / `frame-ancestors` | Anti-clickjacking |
| `Referrer-Policy` | Contrôle de l'en-tête Referer |
| `Permissions-Policy` | Restreint les API du navigateur |

À ajouter par **middleware** ou par la configuration du serveur web.

### 33.12 HTTPS, cookies et sessions

- Forcer HTTPS : `URL::forceScheme('https')`, redirection au niveau serveur, `SESSION_SECURE_COOKIE=true`.
- Cookies `HttpOnly`, `Secure`, `SameSite`.
- **Proxys de confiance** correctement configurés derrière un répartiteur de charge.
- **Hôtes de confiance** : `$middleware->trustHosts(at: ['monsite.com'])` (contre l'injection d'en-tête `Host`).

### 33.13 Limitation de débit et protection contre l'abus

- `throttle` sur la connexion, la réinitialisation de mot de passe et l'API.
- **CAPTCHA** (reCAPTCHA, hCaptcha, Turnstile) sur les formulaires publics.
- **Honeypot** (`spatie/laravel-honeypot`).

### 33.14 URL signées et redirections

- URL signées pour les liens sensibles (désabonnement, vérification) : `URL::signedRoute`.
- **Open redirect** : validez la destination avant `redirect($request->input('next'))` (utilisez `redirect()->intended()` ou une liste blanche de domaines).

### 33.15 Sécurité des dépendances et de la chaîne d'approvisionnement

- Verrouiller par `composer.lock` ; **revue** des packages ajoutés ; limiter les scripts Composer ; versions épinglées en CI.
- Analyse statique et sécurité : Larastan, Enlightn, PHPStan, `composer audit`.

### 33.16 Checklist de sécurité avant mise en production

1. `APP_ENV=production`, `APP_DEBUG=false`, `APP_KEY` définie.
2. HTTPS partout, HSTS activé, cookies sécurisés.
3. Serveur web pointant vers `public/`, permissions correctes (`storage`, `bootstrap/cache`).
4. Base de données accessible **seulement** depuis l'application, utilisateur SQL aux droits minimaux.
5. Limitation de débit et protection contre la force brute.
6. Validation de **toutes** les entrées ; policies sur toutes les ressources.
7. Dépendances à jour, `composer audit` propre.
8. Sauvegardes testées ; journalisation et alertes.
9. En-têtes de sécurité configurés.
10. Secrets hors dépôt.

### 33.17 Pièges fréquents

- **`{!! !!}` sur du contenu utilisateur** : XSS.
- **`whereRaw` avec une variable** : injection SQL.
- **Exclure trop largement le CSRF** (`except: ['*']`) : protection annulée.
- **Se fier à un `id` fourni par le client** sans vérifier l'appartenance : IDOR.
- **`APP_KEY` régénérée sans rotation** : données chiffrées illisibles, sessions invalidées.
- **Dossier d'upload exécutable** : exécution de code arbitraire.

### Synthèse du chapitre 33

Laravel protège **par défaut** (CSRF, échappement Blade, requêtes préparées, hashage, chiffrement) : ne contournez pas ces mécanismes. Validez tout, **autorisez côté serveur** (anti-IDOR), sécurisez uploads, secrets, cookies et **en-têtes**, limitez le débit, tenez les dépendances à jour (`composer audit`) et appliquez la **checklist** avant la mise en production.

---

# Partie IX — Frontend, écosystème, production et bonnes pratiques

## 34. Frontend

**Objectifs d'apprentissage.** Comparer les approches frontend de Laravel (Blade, Alpine, Livewire, Inertia, front découplé) ; configurer et utiliser Vite ; gérer AJAX et CSRF avec Axios ; écrire des composants Alpine et Livewire ; comprendre Inertia ; choisir un starter kit ; connecter une SPA ou une application mobile ; soigner assets, accessibilité et SEO ; tester le frontend ; choisir sa pile.

### 34.1 Panorama des approches

Laravel est **agnostique** : on choisit le niveau d'interactivité nécessaire.

| Approche | Principe | Quand l'utiliser |
| --- | --- | --- |
| **Blade seul** | Rendu serveur classique, pages complètes | Sites de contenu, back-offices simples |
| **Blade + Alpine.js** | Petites interactions côté client (menus, modales, onglets) | Interactivité légère sans build complexe |
| **Livewire** | Composants dynamiques écrits en **PHP**, sans écrire d'API | Applications interactives, équipes PHP |
| **Inertia.js** | SPA (Vue / React / Svelte) pilotée par les routes et contrôleurs Laravel, **sans API REST séparée** | Équipes à l'aise avec le JavaScript moderne |
| **API + SPA / mobile séparés** | Front indépendant (Next.js, Nuxt, React Native…) qui consomme une API | Multi-clients, équipes séparées |

### 34.2 Vite : le bundler

**Vite** compile et sert les assets (JS, CSS, TypeScript, Sass, JSX/Vue) avec **rechargement à chaud** (HMR). Il est intégré par le plugin `laravel-vite-plugin`.

```js
// vite.config.js
import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';

export default defineConfig({
    plugins: [
        laravel({
            input: ['resources/css/app.css', 'resources/js/app.js'],
            refresh: true,                 // recharge la page si une vue Blade change
        }),
    ],
});
```

**Commandes**

```bash
npm install
npm run dev       # serveur de développement + HMR (génère public/hot)
npm run build     # build de production (hachage des noms, manifest.json)
```

**Dans Blade**

```blade
<head>
    @vite(['resources/css/app.css', 'resources/js/app.js'])
</head>
```

En développement, `@vite` pointe vers le serveur Vite ; en production, vers les fichiers versionnés de `public/build`.

**Fonctions utiles**

- `Vite::asset('resources/images/logo.png')` : URL d'un asset traité.
- `import.meta.glob` pour importer des dossiers d'images ou de composants.
- Préchargement : `Vite::prefetch(concurrency: 3)`.
- Content Security Policy : `Vite::useCspNonce()`.
- Alias `@` configurables pour les imports.

> **Héritage.** **Laravel Mix** (webpack) a été remplacé par Vite ; la migration est documentée.

**Tailwind CSS** : framework utilitaire installé par défaut dans les starter kits (`@import "tailwindcss"` en v4).

### 34.3 Axios, CSRF et requêtes AJAX

`resources/js/bootstrap.js` configure Axios (en-tête `X-Requested-With`, gestion automatique du cookie `XSRF-TOKEN`).

```js
axios.post('/comments', { body: 'Salut' })
     .then(res => /* … */)
     .catch(err => err.response.status === 422 && console.log(err.response.data.errors));
```

Côté serveur : retourner du JSON (`expectsJson()`), avec les codes 200 / 201 / 422.

### 34.4 Alpine.js

Framework JavaScript **minimaliste** qui utilise des attributs HTML :

```blade
<div x-data="{ open: false }">
    <button @click="open = !open">Menu</button>
    <ul x-show="open" x-transition @click.outside="open = false">…</ul>
</div>
```

Directives clés : `x-data`, `x-show`, `x-if`, `x-for`, `x-model`, `x-on` (`@`), `x-bind` (`:`), `x-text`, `x-html`, `x-ref`, `x-init`, `x-transition`, stores (`Alpine.store`), `$dispatch`, `$watch`. Alpine est embarqué avec Livewire.

### 34.5 Livewire

Livewire permet de construire des interfaces **réactives en PHP**. Un composant = une classe PHP + une vue Blade ; les interactions déclenchent des requêtes AJAX et mettent à jour le DOM par différentiel (*morphing*).

```bash
composer require livewire/livewire
php artisan make:livewire counter
```

```php
// app/Livewire/Counter.php
class Counter extends Component
{
    public int $count = 0;

    public function increment(): void { $this->count++; }

    public function render() { return view('livewire.counter'); }
}
```

```blade
{{-- resources/views/livewire/counter.blade.php --}}
<div>
    <h1>{{ $count }}</h1>
    <button wire:click="increment">+</button>
</div>
```

Utilisation : `<livewire:counter />` ou `@livewire('counter')`.

**Notions clés**

| Notion | Détail |
| --- | --- |
| **Propriétés publiques** | État synchronisé client ↔ serveur (types simples, modèles, collections) |
| **`wire:model`** | Liaison bidirectionnelle (`.live`, `.blur`, `.debounce.500ms`) |
| **`wire:click`, `wire:submit`, `wire:keydown`** | Actions |
| **`wire:loading`** | États de chargement |
| **`wire:poll`** | Rafraîchissement périodique |
| **`wire:key`** | Identité des éléments d'une boucle |
| **Validation** | Attribut `#[Validate('required\|min:3')]` ou `$this->validate()` |
| **Événements** | `$this->dispatch('post-created')`, `#[On('post-created')]` |
| **Cycle de vie** | `mount`, `hydrate`, `updated`, `updatedFoo`, `render`, `dehydrate` |
| **Propriétés calculées** | `#[Computed]` |
| **Verrouillage** | `#[Locked]` sur une propriété (empêche la modification côté client) |
| **Pagination** | Trait `WithPagination` |
| **Uploads** | Trait `WithFileUploads` |
| **Navigation SPA** | `wire:navigate` |
| **Chargement différé** | `#[Lazy]` |
| **Composants imbriqués** | Parents / enfants, props |
| **Alpine intégré** | `$wire`, `@entangle` |

**Volt** : syntaxe monofichier fonctionnelle de Livewire. **Flux** : bibliothèque de composants d'interface officielle.

> **Sécurité.** Toute propriété publique est **modifiable par le client** : **validez et autorisez dans chaque action**.

### 34.6 Inertia.js

« Le meilleur des deux mondes » : le serveur retourne un **composant de page + des props** au lieu d'une vue Blade.

```php
// app/Http/Controllers/UserController.php
return Inertia::render('Users/Index', [
    'users'   => User::paginate(10)->through(fn ($u) => ['id' => $u->id, 'name' => $u->name]),
    'filters' => $request->only('search'),
]);
```

```vue
<!-- resources/js/Pages/Users/Index.vue -->
<script setup>
import { Link, useForm, router } from '@inertiajs/vue3';
defineProps({ users: Object, filters: Object });
</script>
<template>
  <ul><li v-for="u in users.data" :key="u.id"><Link :href="`/users/${u.id}`">{{ u.name }}</Link></li></ul>
</template>
```

**Notions** : `<Link>` (navigation sans rechargement), `useForm` (soumission et erreurs), partage de données globales (`HandleInertiaRequests::share`), rendu côté serveur (**SSR**), *deferred props*, *lazy props*, *merging props*, *layouts* persistants, `router.visit`, gestion de l'historique.

### 34.7 Starter kits

| Kit | Pile |
| --- | --- |
| **Starter kits officiels récents** *(à jour)* | React, Vue ou Livewire, avec **WorkOS AuthKit** en option |
| **Breeze** *(héritage)* | Blade, Livewire, React, Vue (Inertia), API |
| **Jetstream** *(héritage)* | Livewire ou Inertia + équipes, 2FA, jetons d'API |
| **Fortify** | Backend d'authentification **sans** interface |

Installation : `laravel new app`, puis choix du kit.

### 34.8 Frontend découplé (SPA / mobile)

- Laravel expose une **API** ; authentification **Sanctum** (cookie SPA ou jetons).
- **CORS** et **CSRF** à configurer (`SESSION_DOMAIN`, `SANCTUM_STATEFUL_DOMAINS`).
- Frameworks : Next.js, Nuxt, SvelteKit, Angular, React Native, Flutter.

### 34.9 Assets et médias

- **Images** : optimiser (WebP / AVIF), `loading="lazy"`, `srcset`.
- **Polices** : auto-hébergées ou préchargées.
- **Cache-busting** : versionnage automatique via le manifeste de Vite.

### 34.10 Accessibilité et SEO

- HTML **sémantique**, attributs `alt`, `aria-*`, contraste, navigation au clavier.
- Balises `<title>`, `<meta description>`, Open Graph, URL propres (slugs), plan de site (`spatie/laravel-sitemap`), `hreflang`, **rendu serveur** (SSR) pour le SEO des SPA.

### 34.11 Tester le frontend

```php
Livewire::test(Counter::class)->call('increment')->assertSet('count', 1);

// Inertia
->assertInertia(fn (Assert $page) => $page->component('Users/Index')->has('users.data', 10));
```

- E2E : **Dusk**, **Playwright**, **Pest Browser**.
- Tests unitaires JavaScript : **Vitest**.

### 34.12 Choisir sa pile : arbre de décision

1. Site surtout de **contenu** ? → **Blade (+ Alpine)**.
2. Application **interactive**, équipe **PHP** ? → **Livewire**.
3. Équipe **JavaScript**, expérience de **SPA**, un seul dépôt ? → **Inertia**.
4. **Plusieurs clients** (web + mobile), équipes distinctes ? → **API + front découplé**.

### 34.13 Pièges fréquents

- **Oublier `npm run build`** en production : `@vite` ne trouve pas le manifeste (erreur 500).
- **Laisser `public/hot`** présent : le site pointe vers un serveur Vite inexistant.
- **Faire confiance aux propriétés Livewire** : modifiables par le client.
- **Multiplier les approches** dans un même projet sans règle : dette technique.
- **SPA sans SSR** quand le référencement est crucial.
- **CSRF oublié** dans les requêtes `fetch` : réponse 419.

### Synthèse du chapitre 34

Cinq voies : **Blade** (+ **Alpine**), **Livewire** (réactivité en PHP), **Inertia** (SPA sans API), ou **API + front séparé**. **Vite** compile les assets (`@vite`, `npm run dev/build`). Les **starter kits** officiels accélèrent le départ. Choisissez selon l'**équipe**, l'**interactivité** et les **clients** à servir, et testez avec Livewire/Inertia/Dusk.

---

## 35. Écosystème Laravel

**Objectifs d'apprentissage.** Connaître les outils officiels (développement, authentification, données et recherche, temps réel et performance, déploiement, administration) ; utiliser les utilitaires récents (Process, Concurrency, Benchmark, Lottery…) ; repérer les packages communautaires incontournables et savoir en évaluer la qualité ; connaître les ressources d'apprentissage.

### 35.1 Outils de développement

| Outil | Description |
| --- | --- |
| **Laravel Herd** | Environnement PHP natif ultra-rapide (macOS / Windows), sites `.test`, services intégrés |
| **Laravel Sail** | Docker prêt à l'emploi (MySQL, Redis, Meilisearch, Mailpit, Selenium) |
| **Valet** *(héritage)* | Environnement léger macOS |
| **Homestead** *(héritage)* | Machine virtuelle Vagrant |
| **Tinker** | REPL |
| **Pint** | Formatage PSR-12 (`./vendor/bin/pint`) |
| **Pail** | Logs en direct dans le terminal |
| **Telescope** | Observatoire de débogage en développement (requêtes, jobs, mails, exceptions, cache, événements) |
| **Debugbar** | Barre de débogage (`barryvdh/laravel-debugbar`) |
| **IDE Helper** | Autocomplétion modèles et facades |
| **Larastan** | Analyse statique PHPStan pour Laravel |
| **Boost / Laravel MCP** *(ajout)* | Outils d'assistance IA et serveurs MCP |

### 35.2 Authentification et autorisation

| Outil | Usage |
| --- | --- |
| **Starter kits, Breeze, Jetstream, Fortify** | Échafaudage d'authentification |
| **Sanctum** | Jetons d'API et SPA |
| **Passport** | Serveur OAuth2 |
| **Socialite** | OAuth social (Google, GitHub, Facebook, X, LinkedIn, GitLab, Bitbucket, Slack…) |
| **`spatie/laravel-permission`** | Rôles et permissions |
| **Laravel Pennant** | *Feature flags* (activation progressive de fonctionnalités) |

### 35.3 Données et recherche

| Outil | Usage |
| --- | --- |
| **Eloquent** | ORM |
| **Scout** | Recherche plein texte (Meilisearch, Algolia, Typesense, database) |
| **Cashier** (Stripe / Paddle) | Abonnements, facturation, coupons, factures PDF, essais |
| **Spark** | Squelette de facturation SaaS |
| **Pulse** | Surveillance applicative en production (requêtes lentes, jobs, utilisateurs actifs) |
| **Nightwatch** | Observabilité officielle |
| **Horizon** | Tableau de bord des queues Redis |
| **Telescope** | Débogage |

### 35.4 Temps réel et performance

| Outil | Usage |
| --- | --- |
| **Reverb** | Serveur WebSocket officiel, scalable (Redis), compatible protocole Pusher |
| **Echo** | Client JS pour le broadcasting |
| **Octane** | Serveur d'application haute performance (**FrankenPHP**, Swoole, RoadRunner) : l'application reste en mémoire |
| **Precognition** | Validation en direct côté client avec les règles du serveur |

### 35.5 Utilitaires et nouveautés de syntaxe

- **Folio** : routage fondé sur les pages Blade (`resources/views/pages`).
- **Volt** : composants Livewire monofichiers.
- **Prompts** : interfaces CLI interactives.
- **Context** : contexte propagé aux logs et aux jobs.
- **Concurrency** (`Concurrency::run([...])`) : exécution parallèle.
- **Process** : enveloppe de `Symfony\Process` (`Process::run('ls')`, `Process::pool`).
- **Pipeline**, **Sleep**, **Benchmark**, **Number**, **Uri**, **Lottery**.
- **SDK d'IA** officiel (Laravel 13) : API unifiée pour la génération de texte, les agents à outils, les *embeddings*, l'audio, l'image et les bases vectorielles.

```php
Benchmark::dd([fn () => User::count(), fn () => User::all()->count()]);
Lottery::odds(1, 20)->winner(fn () => /* … */)->choose();
Process::path(base_path())->run('npm run build')->throw();
```

### 35.6 Déploiement et hébergement

| Service | Description |
| --- | --- |
| **Laravel Forge** | Provisionne et gère des serveurs (DigitalOcean, AWS, Hetzner, Linode…), déploiements, SSL, workers, cron |
| **Laravel Vapor** | *Serverless* sur AWS Lambda (autoscaling, S3, SQS, RDS) |
| **Laravel Cloud** | Plateforme d'hébergement gérée officielle |
| **Envoyer** | Déploiements sans interruption (*zero-downtime*) |
| **Envoy** | Exécution de tâches distantes avec syntaxe Blade |
| **Ploi, Ray, Coolify, Deployer** | Alternatives communautaires |

### 35.7 Interface d'administration

- **Laravel Nova** (payant, officiel) : back-office généré à partir des modèles (ressources, filtres, actions, métriques, *lenses*).
- **Filament** (open source) : panneaux d'administration, formulaires, tables, widgets ; très populaire.
- **Backpack**, **Orchid**, **Voyager**, **Statamic** (CMS).

### 35.8 Packages communautaires incontournables

| Domaine | Package(s) |
| --- | --- |
| **Rôles et permissions** | `spatie/laravel-permission` |
| **Médias** | `spatie/laravel-medialibrary`, `intervention/image` |
| **Audit** | `spatie/laravel-activitylog`, `owen-it/laravel-auditing` |
| **Sauvegarde** | `spatie/laravel-backup` |
| **Filtrage d'API** | `spatie/laravel-query-builder` |
| **Données / DTO** | `spatie/laravel-data` |
| **Traductions de modèle** | `spatie/laravel-translatable` |
| **Slug** | `spatie/laravel-sluggable` |
| **Import / export Excel** | `maatwebsite/excel` |
| **PDF** | `barryvdh/laravel-dompdf`, `spatie/laravel-pdf`, `snappy` |
| **Débogage** | `barryvdh/laravel-debugbar` |
| **Documentation d'API** | `dedoc/scramble`, `knuckleswtf/scribe`, `darkaonline/l5-swagger` |
| **Multi-tenance** | `stancl/tenancy`, `spatie/laravel-multitenancy` |
| **Arborescences** | `kalnoy/nestedset` |
| **Santé et supervision de tâches** | `spatie/laravel-health`, `spatie/laravel-schedule-monitor` |
| **Sécurité** | `spatie/laravel-csp`, `enlightn/enlightn` |
| **Webhooks entrants** | `spatie/laravel-webhook-client` |
| **Tests** | Pest, Mockery, Faker, `pestphp/pest-plugin-laravel` |

**Choisir un package** : activité de maintenance, compatibilité avec votre version de Laravel, nombre d'installations, qualité de la documentation, couverture de tests, licence.

### 35.9 Ressources d'apprentissage

- Documentation officielle : `laravel.com/docs`
- **Laracasts** (vidéos), **Laravel News**, **Laravel Daily**, **Laravel Podcast**
- **Laracon** (conférences), **Laravel.io** (forum), GitHub Discussions, Discord officiel
- Livres : *Laravel Up & Running*, *Laravel Beyond CRUD*, *Domain-Driven Design with Laravel*

### 35.10 Pièges fréquents

- **Ajouter un package pour tout** : chaque dépendance est une surface d'attaque et de maintenance.
- **Package abandonné** : incompatible avec la prochaine majeure.
- **Telescope actif en production** sans restriction : surcoût et fuite de données.
- **Confondre outils historiques et actuels** (Breeze/Jetstream vs nouveaux starter kits, Mix vs Vite).
- **Octane sans revue de l'état global** : fuites entre requêtes.

### Synthèse du chapitre 35

L'écosystème couvre le **développement** (Herd, Sail, Pint, Telescope), l'**identité** (Sanctum, Passport, Socialite), les **données** (Scout, Cashier, Pulse, Horizon), le **temps réel et la performance** (Reverb, Octane), le **déploiement** (Forge, Vapor, Cloud) et l'**administration** (Nova, Filament). **Évaluez** chaque package avant de l'adopter.

---

## 36. Performance et déploiement

**Objectifs d'apprentissage.** Mesurer avant d'optimiser ; éliminer les goulots d'étranglement de la base de données ; utiliser cache et caches du framework ; connaître les leviers (OPcache, queues, Octane, Redis, CDN) ; concevoir une architecture de production ; configurer Nginx et PHP-FPM ; déployer (manuel, zero-downtime, CI/CD, conteneurs) ; surveiller, sauvegarder, mettre à l'échelle ; appliquer la checklist de production.

### 36.1 Mesurer avant d'optimiser

**Règle** : *on n'optimise pas ce qu'on n'a pas mesuré.*

Outils : **Telescope**, **Debugbar**, **Pulse**, **Nightwatch**, `DB::listen`, **Blackfire**, **Xdebug** (profilage), **Clockwork**, `Benchmark::measure(...)`, **New Relic / Datadog**, tests de charge (**k6**, **wrk**, **Apache Bench**, **JMeter**).

Indicateurs : **TTFB**, temps de réponse p50 / p95 / p99, requêtes par seconde, nombre de requêtes SQL par page, mémoire, taux d'erreur.

### 36.2 Optimiser la base de données (première source de lenteur)

1. **Éliminer le N+1** : `with()`, `load()`, `withCount()`, `Model::preventLazyLoading()`.
2. **Indexer** les colonnes de filtre, de tri et de jointure (`EXPLAIN` pour vérifier).
3. **Sélectionner** seulement les colonnes utiles (`select('id', 'name')`).
4. **Paginer** (`simplePaginate` / `cursorPaginate` pour grands volumes).
5. **`chunk` / `lazy` / `cursor`** pour les traitements massifs.
6. **Agréger en SQL** plutôt qu'en PHP (`withSum`, `groupBy`).
7. **Éviter les `count()` coûteux** sur grandes tables (cache ou compteurs dénormalisés).
8. **Requêtes lentes** : *slow query log*, `DB::whenQueryingForLongerThan(500, fn ($c, $q) => Log::warning(...))`.
9. **Transactions courtes**, pool de connexions, réplicas en lecture.
10. **Eager loading automatique** (`Model::automaticallyEagerLoadRelationships()`) en dernier recours.

### 36.3 Cache applicatif

- `Cache::remember` pour les requêtes ou API lentes ; **Redis** comme pilote.
- `Cache::flexible` (*stale-while-revalidate*), verrous pour éviter le *stampede*.
- Cache HTTP / CDN : en-têtes `Cache-Control`, ETag.
- Cache de **pages entières** (package `spatie/laravel-responsecache`).

### 36.4 Caches du framework en production

```bash
php artisan optimize          # config + routes + événements + vues
# équivalent à :
php artisan config:cache
php artisan route:cache
php artisan event:cache
php artisan view:cache
php artisan icons:cache       # si Blade Icons
composer install --no-dev --optimize-autoloader      # (--classmap-authoritative en option)
```

À relancer à **chaque déploiement**. **Attention** : après `config:cache`, `env()` hors de `config/` renvoie `null`.

### 36.5 Autres leviers

| Levier | Détail |
| --- | --- |
| **OPcache** | Activer en production (`opcache.enable=1`, `validate_timestamps=0`, JIT optionnel) |
| **Queues** | Déporter e-mails, exports, images, appels tiers |
| **Octane** | Application chargée **une fois** en mémoire (gain très variable selon la charge) — attention à l'état global, aux fuites mémoire, aux singletons |
| **Redis** | Cache + sessions + queues |
| **CDN** | Assets statiques, images |
| **Compression** | gzip / brotli au niveau du serveur |
| **HTTP/2, HTTP/3** | Multiplexage |
| **Images** | WebP / AVIF, chargement paresseux, redimensionnement |
| **Build Vite** | Minification, découpage du code, préchargement |
| **Limiter les providers et packages inutiles** | Moins d'amorçage |
| **Lazy collections / streaming** | Réduire la mémoire |
| **Éviter `Model::all()`** | Toujours borner |

### 36.6 Architecture de production type

```text
Utilisateur → CDN → Répartiteur de charge (HTTPS)
                      ├── Serveur web (Nginx) + PHP-FPM / Octane   (×N)
                      ├── Workers de queue (Supervisor / Horizon)
                      ├── Scheduler (cron, onOneServer)
                      ├── Redis (cache, sessions, queues)
                      ├── Base de données (primaire + réplicas)
                      └── Stockage objet (S3)
```

**Application sans état** : sessions, cache et fichiers **hors du disque local** pour permettre la mise à l'échelle horizontale.

### 36.7 Configuration serveur

**Nginx (extrait)**

```nginx
server {
    listen 80;
    server_name example.com;
    root /var/www/app/public;
    index index.php;

    add_header X-Frame-Options "SAMEORIGIN";
    add_header X-Content-Type-Options "nosniff";

    location / { try_files $uri $uri/ /index.php?$query_string; }
    location ~ \.php$ {
        fastcgi_pass unix:/var/run/php/php8.3-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
        include fastcgi_params;
    }
    location ~ /\.(?!well-known).* { deny all; }
}
```

**PHP-FPM** : régler `pm.max_children`, `memory_limit`, `max_execution_time`, `upload_max_filesize`, `post_max_size`.

**Permissions** : `storage/` et `bootstrap/cache/` inscriptibles par l'utilisateur du serveur web.

### 36.8 Procédure de déploiement

**Manuelle (exemple)**

```bash
git pull origin main
composer install --no-dev --optimize-autoloader
npm ci && npm run build
php artisan down --retry=60          # optionnel
php artisan migrate --force
php artisan optimize
php artisan queue:restart            # redémarre les workers
php artisan schedule:interrupt       # optionnel
php artisan up
```

**Zero-downtime** : dossiers de *releases* + lien symbolique `current` (Envoyer, Deployer, Forge zero-downtime, mise à jour progressive Kubernetes). Les **migrations** doivent être **rétrocompatibles** (l'ancienne et la nouvelle version du code coexistent brièvement) : ajout nullable → déploiement → remplissage → contrainte.

### 36.9 CI/CD (exemple GitHub Actions)

```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: shivammathur/setup-php@v2
        with: { php-version: '8.3', coverage: none }
      - run: composer install --no-interaction --prefer-dist
      - run: cp .env.example .env && php artisan key:generate
      - run: ./vendor/bin/pint --test
      - run: ./vendor/bin/phpstan analyse
      - run: php artisan test --parallel
```

Étapes de déploiement : tests → build → déploiement (SSH, Forge, Envoyer, registre Docker) → migrations → vérification de santé → **retour arrière** si échec.

### 36.10 Conteneurs (Docker / Kubernetes)

- Image **multi-étapes** (build Composer/Node → image d'exécution avec PHP-FPM ou FrankenPHP).
- **Un processus par conteneur** : *web*, *worker*, *scheduler*.
- Configuration par **variables d'environnement** ; secrets via le gestionnaire de l'orchestrateur.
- Logs vers `stderr` / `stdout` (`LOG_CHANNEL=stderr`).
- Sondes de santé : route **`/up`** (Laravel 11+).

### 36.11 Surveillance, sauvegardes, reprise

- **Santé** : `/up`, `spatie/laravel-health` (disque, base, queue, cache, certificats…).
- **Monitoring** : Pulse / Nightwatch, Sentry / Flare, Datadog / New Relic, UptimeRobot / BetterStack.
- **Alertes** sur : taux d'erreur, jobs échoués, files qui s'accumulent, disque, latence.
- **Sauvegardes** : base + fichiers (`spatie/laravel-backup`), stockage externe chiffré, **tests de restauration réguliers**, plan de reprise (RPO / RTO).
- **Journaux** centralisés et rotation.

### 36.12 Mise à l'échelle

1. **Verticale** : plus de CPU / RAM.
2. **Horizontale** : plusieurs serveurs web derrière un répartiteur (application *stateless*), Redis partagé, base répliquée.
3. **Séparer** : web / workers / scheduler / base / cache.
4. **Asynchronisme** : queues, événements, traitements par lots.
5. **Partitionnement / sharding** (cas extrêmes), CQRS, lecture sur réplicas.
6. **Multi-région**, CDN, cache en périphérie.

### 36.13 Checklist de production

- [ ] `APP_ENV=production`, `APP_DEBUG=false`
- [ ] `php artisan optimize` exécuté
- [ ] OPcache activé
- [ ] HTTPS + HSTS
- [ ] Workers de queue supervisés (Supervisor / Horizon) + `queue:restart` au déploiement
- [ ] Cron `schedule:run` actif (`onOneServer` si multi-serveurs)
- [ ] Sauvegardes automatiques testées
- [ ] Monitoring et alertes
- [ ] Journaux centralisés
- [ ] `composer audit` propre

### 36.14 Pièges fréquents

- **Optimiser sans mesurer** : effort perdu, complexité ajoutée.
- **`config:cache` avec des `env()` hors `config/`** : valeurs `null` en production.
- **Workers non redémarrés** après déploiement : ancien code en mémoire.
- **Migration bloquante** sur une grosse table pendant le trafic.
- **Octane et état global** : données d'un utilisateur visibles par le suivant.
- **Sessions et fichiers sur le disque local** avec plusieurs serveurs : comportement incohérent.
- **Sauvegardes jamais restaurées** : on ignore si elles fonctionnent.

### Synthèse du chapitre 36

**Mesurez d'abord.** Les gains viennent en premier de la **base de données** (N+1, index, pagination), puis du **cache**, des **queues**, d'**OPcache** et d'**`optimize`**. En production : application **stateless**, Nginx + PHP-FPM (ou Octane), Redis, workers supervisés, **déploiement** scripté (idéalement *zero-downtime*, migrations rétrocompatibles), **CI/CD**, **monitoring**, **sauvegardes testées**.

---

## 37. Bonnes pratiques

**Objectifs d'apprentissage.** Organiser le code en couches (contrôleur, Form Request, service/action, modèle, resource, policy, job) ; appliquer les principes de conception (SOLID, DRY, KISS, YAGNI) ; respecter les conventions de nommage ; écrire du PHP moderne ; appliquer les bonnes pratiques Eloquent, sécurité, API, configuration, tests ; gérer les dépendances et les mises à jour ; travailler en équipe ; mettre en œuvre un projet de synthèse.

### 37.1 Architecture et organisation du code

**Principe : contrôleurs minces, modèles pertinents, logique métier isolée.**

| Couche | Responsabilité |
| --- | --- |
| **Route** | Associer URL → action, middleware |
| **Contrôleur** | Recevoir la requête, déléguer, retourner la réponse |
| **Form Request** | Valider et autoriser |
| **Service / Action** | Logique métier réutilisable |
| **Modèle** | Relations, scopes, casts, accessors, règles propres à l'entité |
| **Resource** | Format des réponses d'API |
| **Policy** | Autorisations |
| **Job / Event / Listener** | Traitements asynchrones et effets secondaires |
| **Repository** *(optionnel)* | Abstraction d'accès aux données (utile seulement si justifié) |
| **DTO / Value Object / Enum** | Structures de données typées |

**Pattern Action (classe à action unique)**

```php
// app/Actions/CreateOrderAction.php
class CreateOrderAction
{
    public function __construct(private PaymentGateway $payments, private Dispatcher $events) {}

    public function execute(User $user, OrderData $data): Order
    {
        return DB::transaction(function () use ($user, $data) {
            $order = $user->orders()->create($data->toArray());
            $this->payments->charge($order);
            $this->events->dispatch(new OrderPlaced($order));
            return $order;
        });
    }
}

// app/Http/Controllers/OrderController.php
public function store(StoreOrderRequest $request, CreateOrderAction $create)
{
    $order = $create->execute($request->user(), OrderData::fromRequest($request));
    return new OrderResource($order);
}
```

**À éviter** : *fat controllers*, *fat models*, logique dans les vues, dépendances cachées, singletons globaux mutables.

### 37.2 Principes de conception

- **SOLID** : responsabilité unique, ouvert/fermé, substitution de Liskov, ségrégation des interfaces, inversion des dépendances.
- **DRY** (ne pas se répéter), mais pas au prix d'abstractions prématurées (**règle des trois**).
- **KISS** / **YAGNI** : simplicité, pas de sur-ingénierie.
- **Loi de Déméter** : limiter la connaissance de la structure interne des autres objets.
- **Composition plutôt qu'héritage** ; traits avec parcimonie.
- **Domain-Driven Design** pour les domaines complexes (organisation par domaine, agrégats, événements de domaine).

### 37.3 Conventions de nommage

| Élément | Convention | Exemple |
| --- | --- | --- |
| Classe | PascalCase | `OrderController` |
| Modèle | Singulier | `Article` |
| Table | Pluriel *snake_case* | `articles` |
| Pivot | Singuliers, ordre alphabétique | `article_tag` |
| Clé primaire | `id` | `id` |
| Clé étrangère | `singulier_id` | `user_id` |
| Méthode / variable | camelCase | `getFullName()` |
| Relation | camelCase (pluriel pour `hasMany`) | `comments()` |
| Route nommée | notation pointée | `articles.show` |
| Contrôleur | Singulier + `Controller` | `ArticleController` |
| Resource | `XResource` | `ArticleResource` |
| Form Request | `StoreXRequest`, `UpdateXRequest` | `StoreArticleRequest` |
| Job | Verbe + objet | `ProcessPodcast` |
| Event | Passé | `OrderShipped` |
| Listener | Action | `SendShipmentNotification` |
| Migration | Descriptif | `create_articles_table`, `add_slug_to_articles_table` |
| Constantes / enums | `UPPER_SNAKE` / cases PascalCase | `Status::Published` |
| Vue | kebab-case / notation pointée | `articles.show`, `user-profile.blade.php` |
| Config / env | snake_case / UPPER_SNAKE | `app.name`, `APP_NAME` |

### 37.4 Code PHP moderne

```php
<?php

declare(strict_types=1);

enum OrderStatus: string
{
    case Pending = 'pending';
    case Paid    = 'paid';
    case Shipped = 'shipped';

    public function label(): string
    {
        return match ($this) {
            self::Pending => 'En attente',
            self::Paid    => 'Payée',
            self::Shipped => 'Expédiée',
        };
    }
}

final class OrderData
{
    public function __construct(
        public readonly string $reference,
        public readonly int $amount,
        public readonly OrderStatus $status = OrderStatus::Pending,
    ) {}
}
```

Utilisez : **types stricts** et types de retour, **propriétés promues**, `readonly`, **enums**, `match`, **arguments nommés**, `?->` (nullsafe), **attributs**, syntaxe *first-class callable*.

**Style** : PSR-12 via **Pint** ; analyse statique **Larastan** (niveau ≥ 5 puis montée progressive) ; **Rector** pour les migrations de code.

### 37.5 Eloquent et base de données

- Définir `$fillable`, `casts`, **relations typées**.
- Éviter le N+1 : `with()`, et `Model::shouldBeStrict()` hors production.
- **Scopes** pour les requêtes réutilisables.
- **Indexer** et poser des **contraintes** (clés étrangères, unicité) **au niveau de la base**, pas seulement dans l'application.
- Migrations **atomiques**, jamais modifiées après déploiement.
- **Transactions** pour les opérations multi-tables.
- Pas de logique métier lourde dans les observers (préférer événements et jobs explicites).
- Préférer les **enums** aux chaînes magiques ; les caster dans le modèle.
- Utiliser **UUID / ULID** quand les identifiants ne doivent pas être devinables.

### 37.6 Validation, sécurité, API

- Valider via **Form Requests** ; ne jamais passer `$request->all()` à `create()`.
- Autoriser via **Policies** sur chaque ressource.
- Utiliser des **API Resources** pour toutes les sorties JSON.
- **Versionner** l'API ; la documenter (OpenAPI).
- Retourner des **codes HTTP justes** et des erreurs structurées.
- **Limitation de débit** sur les routes sensibles.
- Appliquer la **checklist de sécurité** (chapitre 33).

### 37.7 Configuration et environnements

- `.env` non versionné ; `.env.example` à jour.
- `env()` **uniquement** dans `config/`.
- Une variable = une configuration ; pas de logique conditionnelle sur `APP_ENV` dispersée ; centraliser dans `config/`.
- **Parité** dev / staging / prod (mêmes versions de PHP, base, Redis, idéalement via Sail / Docker).
- Fuseaux horaires : stocker en **UTC**, convertir à l'affichage.

### 37.8 Tests et qualité continue

- **Pyramide** : beaucoup de tests unitaires et Feature, peu de tests E2E.
- Nommer les tests par **comportement**.
- **Factories** et **fakes** ; aucune dépendance à l'ordre.
- **CI obligatoire** : Pint + Larastan + tests + audit Composer.
- Couverture raisonnable sur le code **critique** (paiement, authentification, droits).
- Revue de code, conventions d'équipe documentées, **ADR** (*Architecture Decision Records*) pour les décisions importantes.

### 37.9 Performance (rappel)

- Mesurer d'abord.
- Éviter le N+1, indexer, paginer, mettre en cache.
- Déporter en queue tout traitement de plus de 200–300 ms non indispensable à la réponse.
- Utiliser `optimize`, OPcache, Redis, CDN.

### 37.10 Gestion des dépendances et des mises à jour

- Mettre à jour **régulièrement** (petites étapes plutôt que gros sauts).
- Lire le **Upgrade Guide** à chaque version majeure ; utiliser **Laravel Shift** ou **Rector** pour automatiser.
- Verrouiller par `composer.lock` ; `composer outdated` / `composer audit`.
- Évaluer chaque package ajouté (maintenance, licence, sécurité).
- Éviter de « forker » le framework ; l'étendre par **macros, providers, événements**.

### 37.11 Journalisation, observabilité, maintenance

- Logs **structurés** avec contexte (identifiant de requête, d'utilisateur).
- **Aucune donnée sensible** dans les logs.
- Remontée d'erreurs (Sentry / Flare), métriques (Pulse), alertes.
- Documentation : README clair (installation, commandes, architecture), collection Postman / OpenAPI, diagrammes (Mermaid).
- Gestion de la **dette technique** : refactorings planifiés.

### 37.12 Travail en équipe

- **Git** : branches courtes, PR relues, commits atomiques (*Conventional Commits*).
- **Linters / formateurs** dans les hooks *pre-commit* (`husky`, `captainhook`).
- **Revue de code** : lisibilité, sécurité, tests, performance.
- **Définition de « terminé »** : code, tests, documentation, migration, revue, déploiement.
- Revues régulières de sécurité et de performance.

### 37.13 Les 25 règles d'or (récapitulatif)

1. Valider toute entrée via Form Request.
2. Autoriser toute action via Policy.
3. Ne jamais utiliser `{!! !!}` sur des données non fiables.
4. Utiliser `$fillable`, jamais `Model::unguard()` globalement.
5. `env()` uniquement dans `config/`.
6. Nommer toutes les routes ; utiliser `route()`.
7. Contrôleurs minces ; logique dans Services / Actions.
8. Eager loading systématique pour les listes.
9. Paginer toutes les listes.
10. Indexer les colonnes de recherche et les clés étrangères.
11. Transactions pour les opérations multi-étapes.
12. Queues pour les tâches lentes ; jobs idempotents.
13. `afterCommit` pour dispatcher depuis une transaction.
14. Cache avec invalidation claire.
15. Enums et types stricts.
16. Resources pour les API ; versionner.
17. Tests pour tout code critique ; CI obligatoire.
18. Pint + Larastan systématiques.
19. `APP_DEBUG=false` en production.
20. HTTPS partout, cookies sécurisés.
21. Secrets hors du dépôt ; rotation des clés.
22. Logs structurés, sans données sensibles.
23. Sauvegardes testées.
24. Mises à jour régulières des dépendances.
25. Documenter les décisions et garder le code simple.

**Anti-patterns à repérer en revue de code**

- `$request->all()` passé à `create()` ou `update()`.
- Requêtes Eloquent dans les vues Blade ; boucles sans `with()`.
- `env()` dans le code applicatif ; routes en dur au lieu de `route()`.
- Contrôleurs de plusieurs centaines de lignes ; logique métier dans les observers.
- `catch (Exception $e) {}` vide ; `dd()` ou `dump()` oubliés.
- Jobs non idempotents ; dispatch dans une transaction sans `afterCommit`.
- Autorisation seulement dans l'interface (boutons masqués).
- Migrations modifiées après déploiement ; `migrate:fresh` possible en production.

**Liste de contrôle d'une revue de pull request** : validation par Form Request ; policy appliquée ; pas de N+1 (relations chargées) ; transactions et `afterCommit` corrects ; jobs idempotents avec `tries/backoff` ; tests ajoutés ou mis à jour ; Pint et Larastan au vert ; aucune donnée sensible dans les logs ni les réponses ; migration rétrocompatible ; documentation ou changelog mis à jour.

### 37.14 Projet de synthèse (*capstone*)

Pour consolider l'ensemble du cours, voici le **cahier des charges** d'une application « **Gestionnaire de tâches collaboratif** », qui mobilise chaque partie :

1. **Modélisation** : `User`, `Team`, `Project`, `Task`, `Comment` (polymorphe), `Tag` (N–N), pièces jointes (chapitres 12 à 14).
2. **Authentification** : starter kit + vérification d'e-mail + 2FA ; **Sanctum** pour l'API mobile (chapitre 15).
3. **Autorisation** : rôles d'équipe (propriétaire / membre) via **Policies** (chapitre 16).
4. **CRUD complet** : contrôleurs de ressource, Form Requests, Resources d'API versionnée (chapitres 7, 10, 28).
5. **Asynchrone** : notifications (mail + base + broadcast Reverb), rappels planifiés (scheduler), export CSV en queue (chapitres 21 à 24).
6. **Temps réel** : mise à jour en direct du tableau de tâches (Livewire ou Echo) (chapitres 21 et 34).
7. **Stockage** : pièces jointes sur S3 avec URL temporaires (chapitre 27).
8. **Localisation** : français / anglais (chapitre 32).
9. **Qualité** : tests Feature et Unit (Pest), Pint, Larastan, CI GitHub Actions (chapitres 30 et 36).
10. **Production** : Docker / Sail → déploiement Forge ou Cloud, monitoring Pulse, sauvegardes (chapitre 36).

### Synthèse du chapitre 37

Un code Laravel durable repose sur des **couches claires** (contrôleurs minces, Form Requests, services/actions, policies, resources, jobs), des **conventions de nommage** respectées, du **PHP moderne et typé**, une **sécurité** systématique, des **tests** et une **CI**, des **mises à jour régulières** et un **travail d'équipe** outillé. Les **25 règles d'or** et la liste de contrôle de revue en sont le résumé opérationnel.

---

## Conclusion du cours

Vous avez parcouru l'ensemble du framework : les **fondations** (structure, cycle de vie), la **couche HTTP** (routing, middleware, contrôleurs, requêtes et réponses), les **vues** et la **validation**, la **donnée** (migrations, Eloquent, relations), l'**architecture interne** (conteneur, providers, facades, collections), les **services d'infrastructure** (événements, queues, scheduler, mails, cache, sessions, fichiers), la **qualité** (API, tests, erreurs, localisation, sécurité) et la **mise en production**.

**Pour progresser** : construisez des projets réels, lisez le code source du framework, suivez les notes de version de chaque release (une majeure par an, PHP minimal relevé régulièrement), lisez le guide de mise à jour à chaque montée de version, et contribuez à l'écosystème.

---

*Fin du cours. Bon développement avec Laravel !*
