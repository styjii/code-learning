# Cours complet de PHP

*Du débutant à l'avancé : langage, bases de données, sécurité, API, frameworks et qualité — mis à jour pour PHP 8.5*

---

## Avant de commencer : mode d'emploi du cours

**Public visé.** Ce cours s'adresse à toute personne sachant utiliser un ordinateur et un éditeur de texte. Aucune connaissance préalable de PHP n'est exigée ; la connaissance de HTML (balises, formulaires) est un plus pour les sections 9 à 15. Les sections 14 à 21 supposent que les sections 1 à 13 sont acquises.

**Organisation.** Chaque section suit la même structure :

1. **Objectifs** : ce que vous saurez faire à la fin.
2. **Notions et définitions** : le vocabulaire exact, expliqué.
3. **Exemples commentés** : du code que l'on peut exécuter tel quel.
4. **Pièges et bonnes pratiques** : les erreurs classiques et les réflexes professionnels.
5. **À retenir** **: l'essentiel de la section en quelques lignes**.

**Convention.** Les exemples utilisent `echo` pour afficher les résultats et `PHP_EOL` pour le saut de ligne. Les commentaires `// →` indiquent la sortie obtenue. Les mentions *(8.x)* indiquent la version de PHP qui introduit une fonctionnalité.

**Méthode de travail conseillée.** Lisez les sections dans l'ordre : chacune s'appuie sur les notions des précédentes.

---

## 1. Introduction et installation

### Objectifs

- Définir ce qu'est PHP et situer son rôle dans l'architecture du web.
- Expliquer le cycle de vie d'une requête PHP.
- Installer PHP, vérifier l'installation et lancer un premier script.
- Choisir une structure de projet saine.

### 1.1 Qu'est-ce que PHP ?

**PHP** (acronyme récursif : *PHP: Hypertext Preprocessor*) est un **langage de programmation de script**, **interprété**, **open source**, conçu à l'origine pour produire des pages web dynamiques. Détaillons chaque terme :

- **Langage de script** : on écrit des fichiers texte (`.php`) exécutés directement par un programme appelé **interpréteur**, sans étape de compilation manuelle par le développeur. En interne, le moteur (le **Zend Engine**) compile le code en *bytecode* à la volée, et l'extension **OPcache** peut conserver ce bytecode en mémoire pour accélérer les requêtes suivantes.
- **Côté serveur** : le code s'exécute sur le serveur, jamais dans le navigateur. Le visiteur reçoit uniquement le **résultat** (HTML, JSON, image, PDF…) et ne voit jamais le code source PHP. Cela permet de manipuler en sécurité des secrets (mots de passe de base de données, clés d'API).
- **Open source** : le code de PHP est public, gratuit, et développé par une communauté via un processus de propositions appelées **RFC**.
- **Typage dynamique avec types facultatifs** : une variable peut changer de type au cours de l'exécution, mais on peut (et on doit, dans le code moderne) déclarer des types pour les paramètres, retours et propriétés.
- **Multi-paradigme** : on peut écrire du code **procédural** (suite de fonctions), **orienté objet** (classes, objets) ou **fonctionnel** (fonctions anonymes, `array_map`).

| Caractéristique | Détail |
| --- | --- |
| Exécution | Côté serveur ; aussi en ligne de commande (CLI) |
| Typage | Dynamique + déclarations de types facultatives |
| Paradigmes | Procédural, orienté objet, fonctionnel |
| Extension de fichier | `.php` |
| Gestionnaire de dépendances | Composer, dépôt Packagist |
| Écosystème | Laravel, Symfony, WordPress, Drupal… |

### 1.2 Brève histoire

| Année | Événement |
| --- | --- |
| 1994 | Rasmus Lerdorf écrit en C des outils CGI pour suivre les visites de son CV en ligne |
| 1995 | Publication de *Personal Home Page Tools* (PHP/FI) |
| 1998 | **PHP 3** : réécriture par Zeev Suraski et Andi Gutmans ; le nom devient *PHP: Hypertext Preprocessor* |
| 2000 | PHP 4 : moteur Zend |
| 2004 | PHP 5 : modèle objet complet (visibilité, interfaces, exceptions) |
| 2015 | **PHP 7** (la version 6 n'a jamais été publiée) : performances environ doublées, types scalaires |
| 2020 | **PHP 8.0** : arguments nommés, `match`, attributs, types union, JIT |
| 2021–2024 | 8.1 (énumérations, `readonly`, *fibers*), 8.2, 8.3, **8.4** (hooks de propriétés) |
| 2025 | **PHP 8.5** : opérateur pipe \` |
| 2026 | PHP 8.6 en phase de test |

### 1.3 Versions et cycle de support

Chaque branche mineure de PHP (8.3, 8.4, 8.5…) est publiée en novembre. Elle bénéficie de **2 ans de support actif** (correctifs de bugs et de sécurité) puis de **2 ans de support de sécurité seul**. Une version sortie du support ne reçoit **plus aucun correctif de sécurité** : l'utiliser en production est une faute professionnelle.

| Branche | Sortie | Fin du support actif | Fin du support de sécurité |
| --- | --- | --- | --- |
| 8.2 | déc. 2022 | terminé | 31 déc. 2026 |
| 8.3 | nov. 2023 | terminé | 31 déc. 2027 |
| 8.4 | nov. 2024 | 31 déc. 2026 | 31 déc. 2028 |
| 8.5 | nov. 2025 | 31 déc. 2027 | 31 déc. 2029 |

**Règle :** pour un nouveau projet, choisissez PHP 8.4 ou 8.5. PHP 8.1 et les versions antérieures ne sont plus supportées. Consultez toujours la page officielle des versions supportées (php.net/supported-versions.php).

### 1.4 Ce que PHP sait faire

- Générer du **HTML dynamique** et traiter des **formulaires**.
- Gérer l'état d'un visiteur avec des **sessions** et des **cookies**.
- Dialoguer avec des **bases de données** (MySQL/MariaDB, PostgreSQL, SQLite).
- Lire/écrire des **fichiers**, envoyer des **e-mails**, appeler d'autres services web.
- Construire des **API REST** consommées par des applications mobiles ou JavaScript.
- Écrire des **scripts en ligne de commande** (tâches planifiées, outils).
- Faire tourner de grands frameworks (Laravel, Symfony) et des CMS (WordPress, Drupal).

### 1.5 Comment PHP fonctionne : le cycle de vie d'une requête

Le web repose sur le protocole **HTTP**, de type **requête/réponse** : un **client** (le navigateur) envoie une requête, un **serveur** renvoie une réponse. Pour une page PHP :

1. Le navigateur envoie une requête HTTP (par exemple `GET /produits.php?page=2`).
2. Le **serveur web** (Apache, Nginx, Caddy/FrankenPHP…) reconnaît un fichier `.php` et le confie à l'interpréteur PHP. Avec Nginx, la liaison se fait via **PHP-FPM** (*FastCGI Process Manager*), un gestionnaire de processus PHP.
3. PHP exécute le script de haut en bas, peut interroger une base de données, et produit une **sortie**.
4. Le serveur web renvoie cette sortie, accompagnée d'**en-têtes HTTP** (type de contenu, code de statut), au navigateur.
5. **La requête se termine : toute la mémoire utilisée est libérée.**

Ce dernier point est fondamental : PHP suit traditionnellement le modèle **« shared nothing »** (rien n'est partagé entre deux requêtes). Les variables d'une requête disparaissent à sa fin. Pour conserver une information d'une requête à l'autre, il faut la stocker dans une **session**, un **cookie**, une **base de données**, un **fichier** ou un **cache**. Cette architecture rend PHP simple et robuste : un plantage dans une requête n'affecte pas les autres.

> **SAPI** (*Server API*) : c'est l'interface par laquelle PHP est appelé. Les principales sont `cli` (terminal), `fpm-fcgi` (PHP-FPM), `apache2handler` (module Apache) et `cli-server` (serveur intégré). La constante `PHP_SAPI` indique laquelle est active.

### 1.6 Installer PHP

**Option 1 : paquets du système (recommandé).**

```bash
# macOS (Homebrew)
brew install php

# Ubuntu / Debian
sudo apt update && sudo apt install php php-cli php-mysql php-mbstring php-xml php-curl

# Windows
winget install PHP.PHP
```

**Option 2 : environnement tout-en-un.** XAMPP, Laragon (Windows), MAMP (macOS) ou Laravel Herd installent d'un coup PHP, un serveur web et une base MySQL. Pratique pour débuter.

**Option 3 : Docker.** L'image officielle isole PHP de votre système :

```bash
docker run --rm -it -v "$PWD":/app -w /app -p 8000:8000 php:8.5-cli php -S 0.0.0.0:8000
```

**Vérifier l'installation :**

```bash
php -v        # version installée
php -m        # extensions chargées (mbstring, pdo_mysql, curl, intl…)
php --ini     # fichiers de configuration lus (php.ini)
```

### 1.7 Le fichier de configuration `php.ini`

Le comportement de PHP se règle dans **`php.ini`** (dont l'emplacement est donné par `php --ini`). Les directives que vous rencontrerez le plus souvent :

| Directive | Rôle |
| --- | --- |
| `display_errors` | Afficher ou non les erreurs à l'écran (`On` en dev, `Off` en production) |
| `error_reporting` | Niveaux d'erreurs signalés (`E_ALL` recommandé) |
| `memory_limit` | Mémoire maximale par script |
| `max_execution_time` | Durée maximale d'exécution (secondes) |
| `upload_max_filesize`, `post_max_size` | Limites des envois de fichiers et de formulaires |
| `date.timezone` | Fuseau horaire par défaut |
| `opcache.enable` | Active le cache de bytecode (production) |

On peut aussi modifier certains réglages à l'exécution avec `ini_set('clé', 'valeur')` et les lire avec `ini_get('clé')`.

### 1.8 Le serveur de développement intégré

PHP embarque un petit serveur web, très pratique pour apprendre :

```bash
php -S localhost:8000                 # sert le dossier courant
php -S localhost:8000 -t public       # définit public/ comme racine web
```

Ouvrez ensuite `http://localhost:8000` dans le navigateur. **Ce serveur est réservé au développement** : il n'est ni sécurisé ni conçu pour supporter une charge réelle.

### 1.9 Premier script

Créez un fichier `index.php` :

```php
<?php
echo 'Bonjour le monde !';
```

Exécution en terminal :

```bash
php index.php
```

PHP peut être **mêlé à du HTML**. Tout ce qui est hors des balises `<?php … ?>` est envoyé tel quel :

```php
<!DOCTYPE html>
<html lang='fr'>
<head><meta charset='UTF-8'><title>Ma première page PHP</title></head>
<body>
    <h1><?= htmlspecialchars($titre ?? 'Bienvenue') ?></h1>
    <p>Nous sommes le <?= date('d/m/Y') ?></p>
</body>
</html>
```

Ici, `<?= … ?>` est la forme abrégée de `<?php echo … ; ?>`, et `htmlspecialchars()` protège l'affichage (voir section 7.5).

### 1.10 Structure de projet recommandée

Même pour un petit projet, adoptez dès le départ une organisation propre :

```text
mon-projet/
├── public/          ← SEULE racine web : index.php, CSS, JS, images
│   └── index.php
├── src/             ← votre code PHP (classes)
├── templates/       ← gabarits HTML
├── tests/           ← tests automatisés
├── vendor/          ← dépendances Composer (non versionné)
├── .env             ← secrets (non versionné)
├── .gitignore
└── composer.json
```

Seul le dossier `public/` est exposé au web : ainsi, vos fichiers de configuration et votre code ne peuvent pas être téléchargés par un visiteur.

### 1.11 Outils du développeur

- **Éditeur / IDE** : PhpStorm (payant, très complet), VS Code avec l'extension *PHP Intelephense*.
- **Débogueur** : **Xdebug** (points d'arrêt, profilage).
- **Git** pour versionner, **Composer** pour les dépendances (section 17).
- **Outils en ligne** : 3v4l.org exécute un code sur toutes les versions de PHP.

### À retenir

- PHP s'exécute sur le serveur et renvoie du HTML/JSON ; le visiteur ne voit jamais le code.
- Chaque requête repart de zéro (*shared nothing*).
- Utilisez une version supportée (8.4 ou 8.5) et exposez uniquement `public/`.
- `php -S` sert au développement uniquement.

---

## 2. Syntaxe et bases

### Objectifs

- Écrire un script PHP syntaxiquement correct.
- Manipuler variables, types et constantes ; maîtriser les conversions.
- Comprendre la portée des variables et les superglobales.
- Activer le typage strict.

### 2.1 Balises PHP

```php
<?php
$variable = 'Bonjour';
?>
<p>HTML ici</p>
<p><?= $variable ?></p>
<p><?php echo $variable; ?></p>
```

Le code PHP doit être entouré de `<?php … ?>`. La forme `<?= $x ?>` équivaut à `<?php echo $x; ?>`. **Bonne pratique :** dans un fichier contenant **uniquement du PHP**, **omettez la balise fermante `?>`**. Un espace ou un saut de ligne oublié après `?>` serait envoyé au navigateur avant les en-têtes HTTP et provoquerait l'erreur *« headers already sent »* (section 15.1).

### 2.2 Instructions et commentaires

Chaque **instruction** se termine par un point-virgule `;`. PHP est **insensible à la casse** pour les mots-clés (`echo`, `ECHO`, `Echo`) et les noms de fonctions, mais **sensible à la casse pour les variables et constantes** : `$nom` et `$Nom` sont deux variables différentes.

```php
<?php
// Commentaire sur une ligne
# Autre forme de commentaire sur une ligne
/* Commentaire
   sur plusieurs lignes */
/** Commentaire de documentation (PHPDoc), lu par les IDE et outils d'analyse */

$nom = 'Alice';
$Nom = 'Bob';                       // variable différente
echo "$nom et $Nom" . PHP_EOL;       // → Alice et Bob
ECHO 'Mots-clés insensibles à la casse' . PHP_EOL;
```

### 2.3 Le typage strict

Placez **en toute première instruction** du fichier :

```php
<?php
declare(strict_types=1);
```

Par défaut, PHP applique le **mode coercitif** : il convertit silencieusement les valeurs vers le type attendu (`'5'` devient `5`). Le mode **strict** refuse toute conversion implicite et lève une `TypeError`.

```php
<?php
declare(strict_types=1);

function addition(int $a, int $b): int
{
    return $a + $b;
}

echo addition(2, 3), PHP_EOL;       // → 5

try {
    echo addition('5', 3);          // chaîne passée à un paramètre int
} catch (TypeError $e) {
    echo 'Erreur : ' . $e->getMessage() . PHP_EOL;
}
```

Le mode strict est propre **au fichier où il est déclaré** et concerne les appels effectués depuis ce fichier. Adoptez-le systématiquement : il transforme des bugs silencieux en erreurs immédiates et explicites.

### 2.4 Afficher des données

| Construction | Rôle |
| --- | --- |
| `echo` | Affiche une ou plusieurs chaînes (construction du langage, pas une fonction) |
| `print` | Comme `echo` mais renvoie toujours `1` (rarement utile) |
| `print_r($x)` | Affichage lisible d'un tableau ou objet |
| `var_dump($x)` | Affiche **type et valeur** : l'outil de débogage de référence |
| `var_export($x)` | Représentation sous forme de code PHP valide |
| `printf` / `sprintf` | Affichage / construction de texte formaté |

```php
<?php
$tableau = ['a' => 1, 'b' => [2, 3]];
$nom = 'Alice';
$age = 30;

echo 'A', 'B', 'C', PHP_EOL;                 // → ABC (plusieurs arguments)
print_r($tableau);
var_dump(42);                                // → int(42)
var_dump('texte');                           // → string(5) 'texte'
printf('%s a %d ans' . PHP_EOL, $nom, $age); // → Alice a 30 ans
$ligne = sprintf('%s a %d ans', $nom, $age); // retourne la chaîne sans l'afficher
```

Spécificateurs de format courants : `%s` chaîne, `%d` entier, `%f` flottant, `%05.2f` flottant sur 5 caractères avec 2 décimales complétés par des zéros, `%x` hexadécimal, `%b` binaire, `%%` pour un `%` littéral.

### 2.5 Variables

Une **variable** est un nom associé à une valeur en mémoire. Elle commence par **`$`**, ne nécessite **aucune déclaration préalable**, et son type est déduit de la valeur.

**Règles de nommage :** lettres, chiffres et `_` ; ne commence pas par un chiffre ; sensible à la casse. Convention PSR-12 : `$camelCase` pour les variables, `snake_case` toléré s'il est cohérent. Choisissez des **noms parlants** (`$prixTotal`, pas `$p`).

```php
<?php
$nom = 'Alice';        // string
$age = 30;             // int
$taille = 1.68;        // float
$actif = true;         // bool

echo "$nom, $age ans, $taille m" . PHP_EOL;
```

**Références.** Le symbole `&` crée un second nom pour la **même** valeur :

```php
<?php
$a = 1;
$b = &$a;      // $b est un alias de $a
$b = 2;
echo "a = $a, b = $b" . PHP_EOL;   // → a = 2, b = 2
```

**Variables variables** (`$$nom`) : le nom d'une variable est lui-même contenu dans une variable. Cette pratique rend le code illisible : **à éviter**.

```php
<?php
$nomVariable = 'x';
$$nomVariable = 5;       // crée $x
echo $x . PHP_EOL;       // → 5
```

**Tester une variable :**

- `isset($v)` : vrai si la variable existe **et n'est pas `null`**.
- `empty($v)` : vrai si la valeur est « vide » (voir *falsy* ci-dessous) ou n'existe pas.
- `unset($v)` : détruit la variable.

### 2.6 Types de données

PHP distingue trois familles de types.

**Types scalaires :**

| Type | Description | Exemples |
| --- | --- | --- |
| `int` | Entier signé (64 bits sur les systèmes 64 bits ; `PHP_INT_MAX` = 9 223 372 036 854 775 807) | `42`, `0x1A` (hexa), `0b101` (binaire), `0755` ou `0o755` (octal), `1_000_000` (séparateur) |
| `float` | Nombre à virgule flottante (double précision) | `3.14`, `1.5e3`, `NAN`, `INF` |
| `string` | Suite d'octets (texte) | `'texte'`, `"texte"` |
| `bool` | Booléen | `true`, `false` |

**Types composés :** `array` (tableau), `object` (instance de classe), `callable` (fonction appelable), `iterable` (tableau ou objet parcourable avec `foreach`).

**Types spéciaux :** `null` (absence de valeur), `resource` (ressource externe : fichier ouvert, connexion).

> **Piège des flottants.** Les `float` sont binaires et donc approximatifs : `0.1 + 0.2 === 0.3` vaut `false`. Pour comparer, utilisez une tolérance : `abs($a - $b) < 1e-9`. Pour l'argent, travaillez en **centimes entiers** ou avec une bibliothèque décimale (extension BCMath ou GMP).

```php
<?php
$x = 'texte';
$y = 42;

echo gettype($x) . ' / ' . gettype($y) . PHP_EOL;            // → string / integer
echo get_debug_type($x) . ' / ' . get_debug_type($y) . PHP_EOL; // → string / int (8.0)

var_dump(is_int($y), is_string($y), is_array($y), is_null($y), is_numeric('12.5'));
var_dump(0.1 + 0.2 === 0.3);                                    // → bool(false)
var_dump(PHP_INT_MAX + 1);                                      // → float(9.2233720368547758E+18) : dépassement
```

**Valeurs « fausses » (*falsy*)** : converties en `false` dans un contexte booléen : `false`, `0`, `0.0`, `''` (chaîne vide), `'0'`, `[]` (tableau vide), `null`. **Tout le reste est « vrai »**, y compris `'0.0'`, `' '` et `'false'`.

### 2.7 Conversion de types (*casting*)

PHP convertit parfois automatiquement (**jonglage de types**), mais vous pouvez forcer la conversion :

```php
<?php
var_dump((int) '42abc');    // → int(42)   : lit les chiffres de début
var_dump((int) 'abc');      // → int(0)
var_dump((float) '3.14');   // → float(3.14)
var_dump((string) 123);     // → string(3) '123'
var_dump((bool) '0');       // → bool(false)
var_dump((array) 'a');      // → array(1) { [0]=> 'a' }
var_dump(intval('12'), floatval('1.5'), strval(5), boolval(1));
var_dump((int) 3.99);       // → int(3) : troncature, pas d'arrondi
```

Pour arrondir, utilisez `round()`, `floor()` (inférieur), `ceil()` (supérieur). Pour tester qu'une chaîne représente bien un nombre : `is_numeric()` ou `filter_var($s, FILTER_VALIDATE_INT)`.

### 2.8 Constantes

Une **constante** est une valeur nommée qui ne peut plus changer. Convention : `MAJUSCULES_AVEC_TIRETS_BAS`, **sans `$`**.

```php
<?php
define('TVA', 0.2);              // définie à l'exécution (peut être conditionnelle)
const NOM_SITE = 'MonSite';      // définie à la compilation (forme préférée)

echo TVA . ' ' . NOM_SITE . PHP_EOL;   // → 0.2 MonSite

class Config { const VERSION = '1.0'; }
echo Config::VERSION . PHP_EOL;         // → 1.0
```

**Constantes magiques** (leur valeur dépend de l'endroit où elles sont écrites) : `__FILE__` (chemin du fichier), `__DIR__` (son dossier), `__LINE__`, `__FUNCTION__`, `__CLASS__`, `__METHOD__`, `__NAMESPACE__`. **Constantes prédéfinies** utiles : `PHP_EOL` (saut de ligne), `PHP_VERSION`, `PHP_INT_MAX`, `M_PI`, `DIRECTORY_SEPARATOR`.

### 2.9 Chaînes : guillemets simples et doubles

```php
<?php
$nom = 'Alice';
$utilisateur = ['age' => 30];

echo "Bonjour $nom !" . PHP_EOL;                 // variables interprétées
echo "Âge : {$utilisateur['age']}" . PHP_EOL;    // expressions complexes entre accolades
echo 'Bonjour $nom' . PHP_EOL;                   // → Bonjour $nom (texte brut)
```

Entre **guillemets doubles**, PHP interprète les variables et les séquences d'échappement (`\n`, `\t`, `\\`, `\"`, `\$`). Entre **guillemets simples**, seuls `\\` et `\'` sont interprétés : c'est plus rapide à lire et à écrire quand aucune interpolation n'est nécessaire. Voir la section 7 pour les détails.

### 2.10 Portée des variables et superglobales

La **portée** (*scope*) est la zone du code où une variable est visible. Une variable définie hors d'une fonction (**globale**) n'est **pas** visible à l'intérieur ; une variable définie dans une fonction (**locale**) disparaît à la fin de l'appel (section 5.5).

Les **superglobales** font exception : elles sont accessibles partout, sans `global`.

| Superglobale | Contenu |
| --- | --- |
| `$_GET` | Paramètres de l'URL (`?page=2`) |
| `$_POST` | Données envoyées dans le corps d'une requête (formulaires) |
| `$_REQUEST` | GET + POST + COOKIE mélangés (**à éviter**) |
| `$_SERVER` | Informations sur le serveur et la requête (méthode, URI, en-têtes `HTTP_*`) |
| `$_FILES` | Fichiers téléversés |
| `$_COOKIE` | Cookies reçus |
| `$_SESSION` | Données de session |
| `$_ENV` | Variables d'environnement |
| `$GLOBALS` | Toutes les variables globales |

> **Règle de sécurité :** `$_GET`, `$_POST`, `$_COOKIE`, `$_FILES` et une grande partie de `$_SERVER` sont **contrôlés par l'utilisateur** : ne leur faites jamais confiance (section 16).

### 2.11 Exemple complet

```php
<?php
declare(strict_types=1);

const TVA = 0.2;

$prixHT = 100.0;
$prixTTC = $prixHT * (1 + TVA);
echo 'Prix TTC : ' . number_format($prixTTC, 2, ',', ' ') . ' €' . PHP_EOL;   // → Prix TTC : 120,00 €
```

### Pièges fréquents

- Oublier le `;` ou un `$` devant une variable : erreur d'analyse (*Parse error*).
- Confondre `=` (affectation) et `==` / `===` (comparaison).
- Utiliser une variable non définie : *Warning: Undefined variable*. Initialisez toujours vos variables.
- Comparer des flottants avec `===`.

### À retenir

- `declare(strict_types=1);` en tête de chaque fichier.
- Les variables commencent par `$` et sont sensibles à la casse ; les constantes non.
- `var_dump()` est l'outil de débogage de base.
- Falsy : `false, 0, 0.0, '', '0', [], null`.
- Les superglobales viennent du client : à valider.

---

## 3. Opérateurs

### Objectifs

- Utiliser correctement tous les opérateurs courants.
- Distinguer `==` et `===` et connaître les règles de comparaison de PHP 8.
- Maîtriser les opérateurs modernes (`??`, `?->`, `match`, `...`, `|>`).
- Raisonner sur la priorité des opérateurs.

### 3.1 Opérateurs arithmétiques

| Opérateur | Rôle | Exemple |
| --- | --- | --- |
| `+` `-` `*` | Addition, soustraction, multiplication | `4 * 3` → `12` |
| `/` | Division | `7 / 2` → `3.5` |
| `%` | **Modulo** (reste de la division entière) | `7 % 3` → `1` |
| `**` | Puissance | `2 ** 3` → `8` |
| `intdiv(a, b)` | Division entière | `intdiv(7, 2)` → `3` |
| `-$x` | Négation unaire |  |

`/` renvoie un `int` seulement si le résultat est exact (`6 / 3` → `2`), sinon un `float`. Depuis PHP 8, une **division par zéro** lève une `DivisionByZeroError` ; le modulo par zéro aussi. Le modulo prend le signe du **dividende** : `-7 % 3` → `-1`. Pour un modulo mathématique sur flottants : `fmod()`.

### 3.2 Opérateurs d'affectation

```php
<?php
$x = 5;
$x += 2;  echo $x . PHP_EOL;    // → 7
$x -= 1;  echo $x . PHP_EOL;    // → 6
$x *= 3;  echo $x . PHP_EOL;    // → 18
$x /= 2;  echo $x . PHP_EOL;    // → 9
$x %= 4;  echo $x . PHP_EOL;    // → 1
$x **= 2; echo $x . PHP_EOL;    // → 1

$s = 'début';
$s .= ' fin';                   // concaténation
echo $s . PHP_EOL;              // → début fin

$y ??= 'défaut';                // affecte seulement si $y est null ou non défini (7.4)
echo $y . PHP_EOL;              // → défaut
```

L'affectation est elle-même une **expression** qui vaut la valeur affectée : `$a = $b = 3;` est valide. L'affectation de tableaux se fait **par valeur** (copie), celle des objets par **poignée** (section 14.10).

### 3.3 Opérateurs de comparaison

| Opérateur | Signification |
| --- | --- |
| `==` | Égal après conversion de types (**comparaison souple**) |
| `===` | **Identique** : même valeur **et** même type (**comparaison stricte**) |
| `!=` ou `<>` | Différent (souple) |
| `!==` | Non identique (strict) |
| `<` `>` `<=` `>=` | Ordre |
| `<=>` | **Opérateur « vaisseau spatial »** : renvoie `-1`, `0` ou `1` |

```php
<?php
var_dump(0 == 'a');       // → false en PHP 8 (true avant PHP 8 !)
var_dump('1' == '01');    // → true : deux chaînes numériques comparées comme nombres
var_dump('10' == '1e1');  // → true : idem
var_dump('abc' == 0);     // → false en PHP 8
var_dump(null == false);  // → true
var_dump(null === false); // → false
var_dump(0 === '0');      // → false : types différents
var_dump(1 <=> 2);        // → int(-1)
var_dump('b' <=> 'a');    // → int(1)
```

**Règle PHP 8 :** pour comparer un nombre à une chaîne, PHP convertit le nombre en chaîne **si la chaîne n'est pas numérique**. D'où `0 == 'a'` → `false`. Mais `==` reste source de surprises : **utilisez `===` par défaut**, et réservez `==` aux cas où vous voulez explicitement la conversion.

L'opérateur `<=>` est précieux pour les tris personnalisés (section 6.6) : `usort($t, fn($a, $b) => $a['age'] <=> $b['age'])`.

### 3.4 Opérateurs logiques

| Opérateur | Rôle |
| --- | --- |
| `&&` | ET |
| \` |  |
| `!` | NON |
| `xor` | OU exclusif |
| `and`, `or` | Variantes à **priorité très basse** |

**Évaluation en court-circuit** : dans `A && B`, `B` n'est évalué que si `A` est vrai ; dans `A || B`, `B` n'est évalué que si `A` est faux. On s'en sert pour protéger un accès :

```php
<?php
$utilisateur = null;
if ($utilisateur !== null && $utilisateur->estAdmin()) { /* jamais d'erreur ici */ }
```

> **Piège :** `$ok = true and false;` affecte `true` à `$ok`, car `=` est prioritaire sur `and`. Utilisez toujours `&&` et `||`.

### 3.5 Concaténation, incrément et opérateurs de tableaux

```php
<?php
$s = 'Bonjour' . ' ' . 'monde';       // concaténation avec .

$i = 5;
$j = $i++;    // post-incrémentation : $j vaut 5, puis $i devient 6
$k = ++$i;    // pré-incrémentation  : $i devient 7, puis $k vaut 7

$a = [1, 2] + [3, 4, 5];              // union : [1, 2, 5]
print_r($a);                          // les clés de gauche l'emportent

var_dump([0 => 'a', 1 => 'b'] == [1 => 'b', 0 => 'a']);    // → true : mêmes paires clé/valeur
var_dump([0 => 'a', 1 => 'b'] === [1 => 'b', 0 => 'a']);   // → false : ordre différent
```

Il ne faut pas confondre `+` entre tableaux (union par clés) avec `array_merge()` (qui renumérote les clés numériques).

### 3.6 Opérateurs sur les bits

Ils travaillent sur la représentation binaire des entiers : `&` (ET), `|` (OU), `^` (OU exclusif), `~` (NON), `<<` et `>>` (décalages). Usage typique : les **drapeaux** (*flags*) combinés avec `|`, comme `FILE_APPEND | LOCK_EX` ou `ENT_QUOTES | ENT_SUBSTITUTE`.

```php
<?php
const LIRE = 1;      // 0b001
const ECRIRE = 2;    // 0b010
const EXECUTER = 4;  // 0b100

$droits = LIRE | ECRIRE;                  // combiner
var_dump(($droits & ECRIRE) !== 0);       // → true : tester un drapeau
$droits &= ~ECRIRE;                       // retirer un drapeau
var_dump(($droits & ECRIRE) !== 0);       // → false
```

### 3.7 Opérateurs modernes

**Fusion null `??`** : renvoie l'opérande de gauche s'il existe et n'est pas `null`, sinon celui de droite. Il ne produit **aucun avertissement** si la variable ou la clé n'existe pas.

```php
<?php
$nom = $_GET['nom'] ?? 'Invité';
$ville = $utilisateur['adresse']['ville'] ?? 'Inconnue';   // chaînable, tolère les clés absentes
```

**Appel null-safe `?->` (8.0)** : arrête la chaîne et renvoie `null` si un maillon est `null`.

```php
<?php
$ville = $utilisateur?->adresse?->ville;   // null si $utilisateur ou adresse est null
```

**Ternaire et ternaire court :**

```php
<?php
$age = 20;
$statut = $age >= 18 ? 'majeur' : 'mineur';
$valeur = $entree ?: 'défaut';      // « Elvis » : $entree si elle est « vraie », sinon 'défaut'
```

PHP 8 interdit d'imbriquer des ternaires sans parenthèses.

**`match` (8.0)** : expression qui compare en **strict** (`===`), **renvoie une valeur**, n'a pas besoin de `break`, et lève `UnhandledMatchError` si aucun cas ne correspond et qu'il n'y a pas de `default`.

```php
<?php
$code = 404;
$libelle = match (true) {          // match (true) permet des conditions
    $code >= 500 => 'Erreur serveur',
    $code >= 400 => 'Erreur client',
    default      => 'Autre',
};
echo $libelle . PHP_EOL;           // → Erreur client

$texte = match ($code) {
    200, 201 => 'Succès',
    404      => 'Introuvable',
    default  => 'Erreur',
};
```

**Décomposition / *spread* `...`** : déballe un tableau dans une liste d'éléments ou d'arguments (les clés chaînes sont acceptées depuis 8.1).

```php
<?php
$a = [1, 2]; $b = [3, 4];
$tous = [...$a, ...$b];                      // [1, 2, 3, 4]
function somme(int ...$nombres): int { return array_sum($nombres); }
echo somme(...$tous) . PHP_EOL;              // → 10
```

**Opérateur pipe `|>` (8.5)** : passe le résultat de gauche en **argument unique** de l'appelable de droite, ce qui évite les appels imbriqués illisibles.

```php
<?php
$slug = '  Bonjour Le Monde  '
    |> trim(...)
    |> strtolower(...)
    |> (fn(string $s) => str_replace(' ', '-', $s));
echo $slug . PHP_EOL;                        // → bonjour-le-monde
```

Autres opérateurs : `instanceof` (test d'appartenance à une classe), `new`, `clone`, `@` (suppression d'erreur, **à proscrire**), les opérateurs d'exécution (backticks, dangereux : jamais avec une saisie utilisateur).

### 3.8 Priorité et associativité

Quand plusieurs opérateurs apparaissent, la **priorité** détermine l'ordre d'évaluation. Du plus prioritaire au moins prioritaire (extrait) :

`**` → `++ --` → `!` → `* / %` → `+ -` → `<< >>` → `.` (depuis PHP 8, `+` et `-` priment sur `.`) → `< <= > >=` → `== != === !== <=>` → `&` → `^` → `|` → `&&` → `||` → `??` → `? :` → `= += …` → `and` → `xor` → `or`.

**Associativité :** `**`, `??` et l'affectation s'associent **de droite à gauche** (`2 ** 3 ** 2` vaut `512`), la plupart des autres de gauche à droite. **En cas de doute, mettez des parenthèses** : la lisibilité prime sur la concision.

```php
<?php
echo 'Somme : ' . 1 + 2 . PHP_EOL;     // PHP 8 : (1 + 2) évalué d'abord → Somme : 3
echo -3 ** 2 . PHP_EOL;                 // → -9 : ** prioritaire sur le signe moins
```

### À retenir

- `===` par défaut ; `==` fait des conversions surprenantes.
- `&&` / `||` plutôt que `and` / `or`.
- `??` pour les valeurs par défaut, `?->` pour les chaînes pouvant contenir `null`.
- `match` est plus sûr et plus expressif que `switch`.
- Parenthèses dès qu'un doute existe sur la priorité.

---

## 4. Structures de contrôle

### Objectifs

- Orienter l'exécution avec des conditions (`if`, `switch`, `match`).
- Répéter des traitements avec les boucles (`for`, `while`, `do…while`, `foreach`).
- Maîtriser `break`, `continue`, les générateurs et l'inclusion de fichiers.

### 4.1 Les conditions

Une **structure de contrôle** modifie l'ordre d'exécution linéaire d'un script. Une **condition** s'évalue en booléen : PHP convertit toute expression selon la règle *falsy/truthy* (section 2.6).

```php
<?php
$note = 14;

if ($note >= 16) {
    echo 'Très bien';
} elseif ($note >= 10) {
    echo 'Passable';
} else {
    echo 'Insuffisant';
}
echo PHP_EOL;                      // → Passable
```

Points importants :

- `elseif` (un mot) et `else if` (deux mots) sont équivalents avec accolades.
- Les accolades sont facultatives pour une instruction unique, mais **toujours recommandées** (PSR-12) : elles évitent des bugs lors d'ajouts de lignes.
- Évitez la **condition d'affectation** accidentelle : `if ($a = 5)` affecte puis teste ; c'est presque toujours une faute de frappe pour `===`.
- Utilisez les **clauses de garde** (*early return*) pour limiter l'imbrication : testez d'abord les cas d'erreur et sortez immédiatement.

```php
<?php
function remise(?array $client): float
{
    if ($client === null) {
        return 0.0;                  // garde : cas particulier traité d'emblée
    }
    return $client['fidele'] ? 0.1 : 0.0;
}
```

### 4.2 `switch` (comparaison souple)

```php
<?php
$jour = 'samedi';

switch ($jour) {
    case 'samedi':
    case 'dimanche':               // plusieurs cas partagent le même traitement
        echo 'Week-end';
        break;                     // sans break : exécution « en cascade » (fall-through)
    default:
        echo 'Semaine';
}
echo PHP_EOL;                      // → Week-end
```

`switch` compare en **souple** (`==`), ce qui peut surprendre (`switch ('1e1')` correspond à `case 10`). L'oubli de `break` est une erreur classique. **Préférez `match`** : comparaison stricte, pas de `break`, valeur retournée, `UnhandledMatchError` si aucun cas n'est prévu (ce qui révèle les oublis).

### 4.3 Syntaxe alternative pour les gabarits HTML

Dans les fichiers mêlant HTML et PHP, la syntaxe à deux-points (`if: … endif;`, `foreach: … endforeach;`) évite les accolades difficiles à repérer au milieu du HTML :

```php
<?php
$connecte = true;
$articles = [['titre' => 'Premier article'], ['titre' => 'Deuxième article']];
?>
<?php if ($connecte): ?>
    <p>Bienvenue !</p>
<?php else: ?>
    <p>Veuillez vous connecter.</p>
<?php endif; ?>

<?php foreach ($articles as $article): ?>
    <h2><?= htmlspecialchars($article['titre']) ?></h2>
<?php endforeach; ?>
```

Existent aussi `endfor;`, `endwhile;`, `endswitch;`. Les moteurs de gabarits (Twig, Blade) offrent des syntaxes encore plus lisibles.

### 4.4 Les boucles

Une **boucle** répète un bloc tant qu'une condition est remplie ou pour chaque élément d'une collection.

| Boucle | Quand l'utiliser |
| --- | --- |
| `for` | Nombre d'itérations connu à l'avance (compteur) |
| `while` | Répéter tant qu'une condition est vraie (test **avant** chaque tour) |
| `do … while` | Même chose, mais le bloc s'exécute **au moins une fois** (test après) |
| `foreach` | Parcourir un tableau ou un objet itérable |

```php
<?php
for ($i = 0; $i < 5; $i++) { echo $i; }     // initialisation ; condition ; incrément
echo PHP_EOL;                               // → 01234

$n = 0;
while ($n < 3) { $n++; }
echo $n . PHP_EOL;                          // → 3

do { $n--; } while ($n > 0);                // s'exécute une fois même si la condition est fausse d'emblée
echo $n . PHP_EOL;                          // → 0

foreach ([10, 20, 30] as $valeur) { echo $valeur . ' '; }
echo PHP_EOL;                               // → 10 20 30

foreach (['a' => 1, 'b' => 2] as $cle => $valeur) { echo "$cle=$valeur "; }
echo PHP_EOL;                               // → a=1 b=2
```

**`foreach` par référence.** Pour modifier les éléments en place, on précède la variable de `&` — mais la référence **persiste après la boucle** et peut corrompre le tableau si on réutilise la variable. **Détruisez-la toujours avec `unset()`** :

```php
<?php
$tableau = [1, 2, 3];
foreach ($tableau as &$element) { $element *= 2; }
unset($element);                            // indispensable
echo implode(', ', $tableau) . PHP_EOL;     // → 2, 4, 6
```

Alternative plus sûre : `array_map()` ou `foreach ($t as $k => $v) { $t[$k] = $v * 2; }`.

**Boucles infinies.** `while (true) { … }` est volontaire pour les services de longue durée, accompagnée d'un `break`. Une boucle infinie accidentelle (condition jamais modifiée) est arrêtée par `max_execution_time` en contexte web.

### 4.5 `break` et `continue`

- **`break`** quitte immédiatement la boucle (ou le `switch`).
- **`continue`** passe directement à l'itération suivante.
- Les deux acceptent un **niveau numérique** (`break 2`, `continue 2`) pour agir sur une boucle englobante.

```php
<?php
for ($i = 0; $i < 10; $i++) {
    if ($i === 3) continue;      // saute 3
    if ($i === 7) break;         // arrête à 7
    echo $i . ' ';
}
echo PHP_EOL;                    // → 0 1 2 4 5 6

$lignes = [[1, 2], [3, null, 5], [6, 7]];
foreach ($lignes as $numero => $ligne) {
    foreach ($ligne as $cellule) {
        if ($cellule === null) {
            echo "Ligne $numero ignorée" . PHP_EOL;
            continue 2;          // reprend à la ligne suivante de la boucle EXTÉRIEURE
        }
    }
    echo "Ligne $numero complète" . PHP_EOL;
}
```

### 4.6 Les générateurs

Un **générateur** est une fonction qui contient `yield`. Au lieu de calculer et retourner toute une collection d'un coup, elle **produit les valeurs une à une, à la demande**, en gardant son état entre deux valeurs. Résultat : une consommation mémoire quasi constante, même pour des millions d'éléments.

```php
<?php
function lireLignes(string $chemin): Generator
{
    $f = fopen($chemin, 'r');
    while (($ligne = fgets($f)) !== false) {
        yield rtrim($ligne);          // suspend la fonction et renvoie la valeur
    }
    fclose($f);
}

$chemin = tempnam(sys_get_temp_dir(), 'demo');
file_put_contents($chemin, "ligne 1\nligne 2\nligne 3\n");

foreach (lireLignes($chemin) as $ligne) {
    echo $ligne . PHP_EOL;            // une seule ligne en mémoire à la fois
}
unlink($chemin);
```

Fonctionnalités complémentaires : `yield $cle => $valeur` (clé explicite), `yield from autreGenerateur()` (déléguer), et `$generateur->send($valeur)` (communication bidirectionnelle). Un générateur ne peut être **parcouru qu'une seule fois**.

### 4.7 Inclusion de fichiers

Pour découper un programme en fichiers, PHP propose quatre instructions :

| Instruction | Fichier absent | Inclusions multiples |
| --- | --- | --- |
| `include` | Avertissement, le script continue | Oui |
| `include_once` | Avertissement | Une seule fois |
| `require` | **Erreur fatale** | Oui |
| `require_once` | **Erreur fatale** | Une seule fois |

```php
<?php
$dossier = sys_get_temp_dir();
file_put_contents($dossier . '/config.php', "<?php\nreturn ['site' => 'MonSite'];\n");
file_put_contents($dossier . '/outils.php', "<?php\nfunction bonjour(): string { return 'Bonjour'; }\n");

$config = require $dossier . '/config.php';       // un fichier peut RETOURNER une valeur (ex. un tableau de configuration)
require_once $dossier . '/outils.php';
require_once $dossier . '/outils.php';            // ignoré : déjà inclus (sinon : fonction redéclarée)
echo bonjour() . ' sur ' . $config['site'] . PHP_EOL;   // → Bonjour sur MonSite

unlink($dossier . '/config.php');
unlink($dossier . '/outils.php');
```

**Règles de sécurité et de robustesse :**

- Construisez les chemins avec `__DIR__` (indépendant du dossier courant).
- **Ne passez jamais une saisie utilisateur à `include`/`require`** : cela permet d'exécuter du code arbitraire (*inclusion de fichier locale ou distante*).
- Dans les projets modernes, on n'écrit presque plus de `require` : l'**autoloader de Composer** charge les classes automatiquement (sections 14.12 et 17).

### À retenir

- `match` plutôt que `switch` ; accolades toujours ; clauses de garde.
- `foreach` par référence : `unset()` de la variable ensuite.
- Les générateurs économisent la mémoire sur les gros volumes.
- `require_once` pour les dépendances indispensables ; jamais de chemin issu de l'utilisateur.

---

## 5. Fonctions

### Objectifs

- Définir, appeler et typer des fonctions.
- Maîtriser paramètres (par défaut, nommés, variadiques, par référence) et valeurs de retour.
- Comprendre la portée, les fonctions anonymes, fléchées et les *callables* de première classe.
- Écrire des fonctions récursives et propres.

### 5.1 Définir et appeler

Une **fonction** est un bloc de code nommé, réutilisable, qui reçoit des **paramètres** (variables déclarées dans sa définition) et peut renvoyer une **valeur**. Les valeurs fournies à l'appel sont des **arguments**. Intérêts : éviter la duplication (principe **DRY**), nommer les intentions, tester isolément.

```php
<?php
function saluer(string $nom): string
{
    return 'Bonjour ' . $nom . ' !';
}

echo saluer('Alice') . PHP_EOL;       // → Bonjour Alice !
```

Une fonction peut être appelée **avant** sa définition si elle est définie au niveau racine du fichier (PHP les « remonte » à la compilation). Une fonction définie conditionnellement ou dans une autre fonction n'existe qu'après l'exécution de ce code.

### 5.2 Les paramètres

**Valeurs par défaut.** Un paramètre avec défaut devient facultatif. Convention : les paramètres facultatifs viennent **en dernier**.

**Arguments nommés (8.0).** On désigne le paramètre par son nom : l'ordre n'importe plus et on peut « sauter » des paramètres facultatifs. Cela améliore la lisibilité des appels à nombreux paramètres booléens.

**Fonctions variadiques.** `...$nombres` capture un nombre quelconque d'arguments dans un tableau. L'opérateur `...` à l'appel déballe un tableau en arguments.

**Passage par référence.** `&$param` donne accès à la variable de l'appelant, que la fonction peut modifier.

```php
<?php
function presenter(string $nom, int $age = 18, ?string $ville = null): string
{
    return "$nom, $age ans" . ($ville !== null ? " à $ville" : '');
}

echo presenter('Alice') . PHP_EOL;                      // → Alice, 18 ans
echo presenter('Bob', 25, 'Paris') . PHP_EOL;           // → Bob, 25 ans à Paris
echo presenter(nom: 'Chloé', ville: 'Lyon') . PHP_EOL;  // arguments nommés → Chloé, 18 ans à Lyon

function total(int ...$nombres): int { return array_sum($nombres); }
echo total(1, 2, 3) . PHP_EOL;          // → 6
echo total(...[4, 5, 6]) . PHP_EOL;     // → 15

function ajouter(array &$liste, mixed $x): void { $liste[] = $x; }
$liste = [1, 2];
ajouter($liste, 3);
echo implode(', ', $liste) . PHP_EOL;   // → 1, 2, 3
```

**Valeur ou référence ?** Par défaut, les arguments sont passés **par valeur** : la fonction travaille sur une copie. Pour les **objets**, on copie la *poignée* (identifiant) : la fonction peut modifier l'objet partagé (section 14.10). Privilégiez le retour de valeurs plutôt que la modification par référence, qui rend le flux de données opaque.

**Paramètres nullables et implicites.** `?string $x = null` déclare explicitement un type nullable ; l'écriture `string $x = null` (nullable implicite) est dépréciée depuis 8.4.

### 5.3 Valeurs de retour

`return` termine la fonction et renvoie une valeur. Sans `return`, la fonction renvoie `null` (ou doit déclarer `void`). Pour renvoyer plusieurs valeurs, retournez un **tableau** (avec destructuration) ou, mieux, un **objet** dédié.

```php
<?php
function minMax(array $t): array { return [min($t), max($t)]; }
[$mini, $maxi] = minMax([3, 1, 4]);               // destructuration
echo "min = $mini, max = $maxi" . PHP_EOL;        // → min = 1, max = 4

function nePasRetourner(): void { echo 'rien' . PHP_EOL; }   // void : aucun return de valeur

function arreter(): never { exit('Fin' . PHP_EOL); }          // never (8.1) : ne rend jamais la main
```

### 5.4 Les déclarations de types

Typer une fonction documente son contrat et déclenche des erreurs précoces (avec `strict_types`).

| Type | Signification |
| --- | --- |
| `int`, `float`, `string`, `bool`, `array`, `object`, `callable`, `iterable` | Types de base |
| `?string` | `string` **ou** `null` |
| `int\|string` | **Union** (8.0) : l'un ou l'autre |
| `Countable&Traversable` | **Intersection** (8.1) : les deux à la fois |
| `mixed` | Toute valeur (y compris `null`) |
| `void` | N'a pas de valeur de retour |
| `never` | Ne retourne jamais (exit, exception) |
| `self`, `static` | La classe courante / la classe appelée |
| `null`, `false`, `true` | Types autonomes (8.2) |

**Coercition.** Sans `strict_types`, PHP convertit certaines valeurs (`'5'` → `5`) ; en mode strict, il lève `TypeError`. L'exception : un `int` est accepté là où un `float` est attendu.

```php
<?php
function trouver(array $liste, int|string $cle): mixed
{
    return $liste[$cle] ?? null;
}

var_dump(trouver(['a' => 1, 5 => 'cinq'], 'a'));   // → int(1)
var_dump(trouver(['a' => 1, 5 => 'cinq'], 5));     // → string(4) 'cinq'
var_dump(trouver(['a' => 1], 'z'));                 // → NULL
```

### 5.5 La portée des variables

À l'intérieur d'une fonction, **seules** les variables locales (paramètres compris) sont visibles. Pour accéder à une variable globale : mot-clé `global` ou tableau `$GLOBALS` — **à éviter**, car cela crée des dépendances cachées. Pour mémoriser une valeur entre les appels : variable **`static`**.

```php
<?php
$global = 'G';

function sansPortee(): void
{
    echo $global;                   // variable locale jamais définie : avertissement « Undefined variable »
}

function compteur(): int
{
    static $n = 0;                  // initialisée une seule fois, conservée entre les appels
    return ++$n;
}

echo compteur() . compteur() . compteur() . PHP_EOL;     // → 123
```

> **Bonne pratique :** passez les valeurs nécessaires **en paramètres**. Une fonction qui dépend uniquement de ses arguments (fonction « pure ») est prévisible et facile à tester.

### 5.6 Fonctions anonymes, fléchées, *callables*

Une **fonction anonyme** (ou *closure*, de classe `Closure`) n'a pas de nom ; on la stocke dans une variable, on la passe en argument ou on la renvoie.

```php
<?php
$carre = function (int $x): int { return $x * $x; };
echo $carre(4) . PHP_EOL;                                    // → 16

$facteur = 3;
$multiplier = function ($x) use ($facteur) { return $x * $facteur; };   // use : capture explicite, par valeur
echo $multiplier(5) . PHP_EOL;                               // → 15

$compteurRef = 0;
$incrementer = function () use (&$compteurRef) { $compteurRef++; };     // use (&$x) : capture par référence
$incrementer(); $incrementer();
echo $compteurRef . PHP_EOL;                                 // → 2

$triple = fn($x) => $x * 3;      // fonction fléchée (7.4) : une seule expression, capture AUTOMATIQUE par valeur
echo $triple(7) . PHP_EOL;                                   // → 21

echo implode(', ', array_map(fn($n) => $n * 2, [1, 2, 3])) . PHP_EOL;   // → 2, 4, 6
```

Un **callable** est toute valeur appelable : nom de fonction (`'strlen'`), closure, tableau `[$objet, 'methode']`, chaîne `'Classe::methode'`, objet avec `__invoke()`. `is_callable($v)` le vérifie ; `call_user_func()` et `call_user_func_array()` l'invoquent dynamiquement.

**Syntaxe de callable de première classe (8.1).** `f(...)` crée une `Closure` à partir d'une fonction ou méthode existante, sans chaîne de caractères ni tableau :

```php
<?php
class Outils
{
    public function majuscules(string $s): string { return strtoupper($s); }
    public static function fabrique(): string { return 'fabriqué'; }
}

$longueur = strlen(...);                    // fonction native
echo $longueur('bonjour') . PHP_EOL;        // → 7

$objet = new Outils();
$methode = $objet->majuscules(...);         // méthode d'instance
echo $methode('php') . PHP_EOL;             // → PHP

$statique = Outils::fabrique(...);          // méthode statique
echo $statique() . PHP_EOL;                 // → fabriqué
```

### 5.7 Récursivité

Une fonction **récursive** s'appelle elle-même. Elle exige un **cas de base** (arrêt) et un appel qui se rapproche de ce cas.

```php
<?php
function factorielle(int $n): int
{
    return $n <= 1 ? 1 : $n * factorielle($n - 1);   // cas de base : n <= 1
}

echo factorielle(5) . PHP_EOL;        // → 120
```

PHP n'optimise pas la récursion terminale et limite la profondeur par la mémoire : pour de très grandes profondeurs, préférez une **boucle**. La récursivité est naturelle pour les structures arborescentes (dossiers, menus imbriqués).

### 5.8 Fonctions utiles et introspection

`function_exists('nom')`, `is_callable($v)`, `func_get_args()` (arguments reçus), `get_defined_functions()`. Les **fonctions natives** (plus de mille) couvrent chaînes, tableaux, maths, dates, fichiers ; consultez le manuel officiel avant de réécrire un outil.

### 5.9 Bonnes pratiques

- Fonctions **courtes**, à **responsabilité unique**, nommées par un **verbe** (`calculerTotal`, `envoyerEmail`).
- **Typez** paramètres et retours ; activez `strict_types`.
- Documentez avec **PHPDoc** ce que les types ne disent pas (`@param list<int> $nombres`, `@throws`).
- Évitez les effets de bord, les globales et les paramètres booléens ambigus (préférez les arguments nommés).
- Limitez le nombre de paramètres (au-delà de 3 ou 4, regroupez-les dans un objet).

### À retenir

- Une fonction = un contrat typé ; l'entrée passe par les paramètres, la sortie par `return`.
- Arguments nommés, variadiques, valeurs par défaut rendent les API lisibles.
- Closures : `use` (explicite) ou `fn` (capture automatique).
- `static` conserve un état entre appels ; `global` est à proscrire.

---

## 6. Tableaux

### Objectifs

- Comprendre la nature du tableau PHP (liste, dictionnaire, pile, file).
- Créer, lire, modifier, parcourir et supprimer des éléments.
- Utiliser les fonctions natives essentielles, les fonctions d'ordre supérieur et les tris.
- Comprendre la copie, les références et les structures SPL.

### 6.1 Qu'est-ce qu'un tableau PHP ?

Un **tableau** (*array*) est une structure de données qui associe des **clés** à des **valeurs**, en conservant l'**ordre d'insertion**. En interne, c'est une table de hachage ordonnée : un seul type sert donc de **liste**, de **dictionnaire**, de **pile**, de **file** et d'**ensemble**.

- Les **clés** sont des entiers ou des chaînes. Une clé chaîne qui ressemble à un entier décimal (`'5'`) est convertie en entier (`5`) ; un flottant est tronqué ; un booléen devient 0 ou 1 ; `null` devient `''`.
- Les **valeurs** peuvent être de n'importe quel type, y compris d'autres tableaux.

```php
<?php
// Indexé : clés 0, 1, 2… attribuées automatiquement
$fruits = ['pomme', 'banane', 'cerise'];

// Associatif : clés choisies
$personne = ['nom' => 'Alice', 'age' => 30];

// Multidimensionnel : tableaux imbriqués
$utilisateurs = [
    ['nom' => 'Alice', 'age' => 30],
    ['nom' => 'Bob',   'age' => 25],
];

echo $fruits[0] . PHP_EOL;                    // → pomme
echo $personne['nom'] . PHP_EOL;              // → Alice
echo $utilisateurs[1]['nom'] . PHP_EOL;       // → Bob
```

Utilisez la syntaxe courte `[]` plutôt que l'ancienne `array()`. Accéder à une clé absente produit un avertissement : on la protège avec `??` ou `isset()`.

### 6.2 Ajouter, modifier, supprimer

```php
<?php
$fruits = ['pomme', 'banane', 'cerise'];
$personne = ['nom' => 'Alice', 'age' => 30];

$fruits[] = 'fraise';             // ajout à la fin (clé = plus grand entier + 1)
$fruits[1] = 'kiwi';              // modification
$personne['ville'] = 'Paris';     // ajout d'une clé
unset($personne['age']);          // suppression (n'a PAS d'effet de renumérotation sur une liste)
echo implode(', ', $fruits) . PHP_EOL;     // → pomme, kiwi, cerise, fraise
echo json_encode($personne) . PHP_EOL;     // → {'nom':'Alice','ville':'Paris'}

array_push($fruits, 'a', 'b');       // ajoute à la fin
echo array_pop($fruits) . PHP_EOL;   // retire et renvoie le dernier → b
array_unshift($fruits, 'début');     // ajoute au début (renumérote)
echo array_shift($fruits) . PHP_EOL; // retire et renvoie le premier → début
```

`array_push/array_pop` (fin) et `array_unshift/array_shift` (début) transforment un tableau en **pile** (LIFO) ou en **file** (FIFO). Attention : `array_shift`/`array_unshift` renumérotent toutes les clés ; sur de gros volumes, préférez `SplQueue`.

### 6.3 Parcourir

```php
<?php
$fruits = ['pomme', 'banane'];
$personne = ['nom' => 'Alice', 'age' => 30];
$utilisateurs = [['nom' => 'Alice', 'age' => 30], ['nom' => 'Bob', 'age' => 25]];

foreach ($fruits as $indice => $fruit) { echo "$indice : $fruit" . PHP_EOL; }
foreach ($personne as $cle => $valeur) { echo "$cle = $valeur" . PHP_EOL; }

// Destructuration (liste ou clés)
[$premier, $second] = $fruits;
['nom' => $nom, 'age' => $age] = $personne;
echo "$nom a $age ans" . PHP_EOL;
foreach ($utilisateurs as ['nom' => $n, 'age' => $a]) { echo "$n ($a)" . PHP_EOL; }
```

### 6.4 Fonctions essentielles

| Besoin | Fonctions |
| --- | --- |
| **Taille** | `count($t)` |
| **Existence d'une clé** | `isset($t['k'])` (faux si valeur `null`), `array_key_exists('k', $t)` (vrai même si `null`) |
| **Existence d'une valeur** | `in_array($v, $t, true)` |
| **Clés / valeurs** | `array_keys()`, `array_values()` |
| **Recherche** | `array_search($v, $t, true)` (renvoie la clé ou `false`) |
| **Extraction** | `array_slice($t, $debut, $longueur)`, `array_splice()` (modifie le tableau) |
| **Fusion** | `array_merge($a, $b)`, `[...$a, ...$b]`, `array_combine($cles, $valeurs)`, `array_replace()` |
| **Unicité** | `array_unique($t)` |
| **Colonne** | `array_column($lignes, 'nom', 'id')` |
| **Découpage** | `array_chunk($t, 3)` |
| **Remplissage** | `range(1, 10)`, `array_fill(0, 5, 'x')`, `array_pad()` |
| **Opérations ensemblistes** | `array_diff`, `array_intersect` (valeurs), `array_diff_key`, `array_intersect_key` (clés) |
| **Somme / produit** | `array_sum()`, `array_product()` |
| **Inverser / échanger** | `array_reverse()`, `array_flip()` |
| **Compter les occurrences** | `array_count_values()` |
| **Aléatoire** | `shuffle()`, `array_rand()` |
| **Tester une liste** | `array_is_list($t)` (8.1) |
| **Premier / dernier** | `array_key_first()`, `array_key_last()` ; `array_first()`, `array_last()` *(8.5)* |
| **Recherche fonctionnelle** | `array_find()`, `array_find_key()`, `array_any()`, `array_all()` *(8.4)* |

```php
<?php
$lignes = [['id' => 7, 'nom' => 'Alice'], ['id' => 9, 'nom' => 'Bob']];

print_r(array_column($lignes, 'nom', 'id'));        // [7 => 'Alice', 9 => 'Bob']
print_r(array_chunk([1, 2, 3, 4, 5], 2));           // [[1,2],[3,4],[5]]
print_r(array_count_values(['a', 'b', 'a']));       // ['a' => 2, 'b' => 1]
print_r(array_merge(['a' => 1, 5 => 'x'], ['a' => 2, 5 => 'y']));   // ['a' => 2, 0 => 'x', 1 => 'y']
var_dump(array_is_list([1, 2, 3]));                  // → true
```

> **Piège de `in_array` / `array_search` :** sans le 3ᵉ argument `true`, la comparaison est souple : `in_array('abc', [0])` pouvait être vrai avant PHP 8, et `in_array('1e1', ['10'])` l'est encore. Passez **toujours `true`**.

**`array_merge` ou `+` ?** `array_merge` renumérote les clés entières et, pour les clés chaînes, la valeur de droite écrase celle de gauche. L'opérateur `+` conserve les clés de gauche et ignore celles de droite déjà présentes.

### 6.5 Fonctions d'ordre supérieur

Une fonction d'**ordre supérieur** reçoit une autre fonction en argument. Elles permettent un style **fonctionnel**, déclaratif.

```php
<?php
$nombres = [1, 2, 3, 4, 5];

// map : transforme chaque élément
echo json_encode(array_map(fn($n) => $n * 2, $nombres)) . PHP_EOL;           // → [2,4,6,8,10]

// filter : conserve ceux qui satisfont la condition (les CLÉS sont conservées !)
echo json_encode(array_filter($nombres, fn($n) => $n % 2 === 0)) . PHP_EOL;  // → {'1':2,'3':4}
echo json_encode(array_values(array_filter($nombres, fn($n) => $n % 2 === 0))) . PHP_EOL; // → [2,4]

// reduce : réduit à une seule valeur
echo array_reduce($nombres, fn($somme, $n) => $somme + $n, 0) . PHP_EOL;     // → 15

// walk : parcourt en place (valeur par référence)
array_walk($nombres, function (&$n) { $n *= 2; });
echo json_encode($nombres) . PHP_EOL;                                        // → [2,4,6,8,10]
```

`array_filter` peut aussi filtrer sur la clé (`ARRAY_FILTER_USE_KEY`) ou sur clé et valeur (`ARRAY_FILTER_USE_BOTH`). Sans callback, il retire toutes les valeurs *falsy*. `array_map` accepte plusieurs tableaux en parallèle.

### 6.6 Trier

| Fonction | Tri |
| --- | --- |
| `sort()` / `rsort()` | Valeurs croissantes / décroissantes ; **renumérote** les clés |
| `asort()` / `arsort()` | Valeurs, **conserve les clés** |
| `ksort()` / `krsort()` | Par **clés** |
| `usort($t, fn)` | Tri **personnalisé** par valeur (renumérote) |
| `uasort()` / `uksort()` | Tri personnalisé en conservant les clés / par clé |
| `array_multisort()` | Tri de plusieurs tableaux liés |

Ces fonctions **modifient le tableau passé** (par référence) et renvoient un booléen. Depuis PHP 8.0, le tri est **stable** : deux éléments égaux conservent leur ordre relatif. Les drapeaux (`SORT_STRING`, `SORT_NATURAL | SORT_FLAG_CASE`, `SORT_NUMERIC`) contrôlent la comparaison ; `natsort()` donne l'ordre « naturel » (`img2` avant `img10`).

```php
<?php
$utilisateurs = [
    ['nom' => 'Chloé', 'age' => 30],
    ['nom' => 'Bob',   'age' => 25],
    ['nom' => 'Alice', 'age' => 30],
];

usort($utilisateurs, fn($a, $b) => $a['age'] <=> $b['age']);            // par âge
echo implode(', ', array_column($utilisateurs, 'nom')) . PHP_EOL;       // → Bob, Chloé, Alice

usort($utilisateurs, fn($a, $b) => [$a['age'], $a['nom']] <=> [$b['age'], $b['nom']]);   // critères multiples
echo implode(', ', array_column($utilisateurs, 'nom')) . PHP_EOL;       // → Bob, Alice, Chloé
```

La fonction de comparaison doit renvoyer un entier négatif, nul ou positif : `<=>` est l'outil idéal. Ne renvoyez jamais un booléen.

### 6.7 Copie et références

Les tableaux sont copiés **par valeur**, avec une optimisation (*copy-on-write*) : la copie réelle n'a lieu qu'à la première modification. À l'inverse, les **objets** sont manipulés par poignée.

```php
<?php
$a = [1, 2];
$b = $a;
$b[] = 3;                         // $a reste inchangé
echo implode(', ', $a) . PHP_EOL;   // → 1, 2
echo implode(', ', $b) . PHP_EOL;   // → 1, 2, 3
```

### 6.8 Tableaux multidimensionnels

```php
<?php
$utilisateurs = [['nom' => 'Alice', 'age' => 30], ['nom' => 'Bob', 'age' => 25]];

foreach ($utilisateurs as $u) {
    echo "{$u['nom']} a {$u['age']} ans" . PHP_EOL;
}

// Regrouper : tableau associatif de listes
$parAge = [];
foreach ($utilisateurs as $u) { $parAge[$u['age']][] = $u['nom']; }
print_r($parAge);                       // [30 => ['Alice'], 25 => ['Bob']]
```

### 6.9 Interfaces et structures SPL

Pour qu'un objet se comporte comme un tableau, il implémente `ArrayAccess` (`$o['k']`), `Countable` (`count($o)`) et `IteratorAggregate`/`Iterator` (`foreach`). La **SPL** (*Standard PHP Library*) fournit des structures prêtes à l'emploi : `ArrayObject`, `SplStack`, `SplQueue`, `SplObjectStorage` (ensemble d'objets), `SplPriorityQueue`, `SplFixedArray` (tableau de taille fixe, plus économe). Les frameworks ajoutent des **collections** riches (`Illuminate\Support\Collection`).

### À retenir

- Un seul type pour listes, dictionnaires, piles et files ; ordre d'insertion conservé.
- `isset`/`??` pour les clés absentes ; `in_array(..., true)` en strict.
- `array_filter` conserve les clés (ajoutez `array_values` si besoin) ; les tris modifient en place et sont stables.
- Copie par valeur pour les tableaux, par poignée pour les objets.

---

## 7. Chaînes de caractères

### Objectifs

- Créer des chaînes avec les quatre syntaxes (simple, double, heredoc, nowdoc).
- Distinguer octets et caractères, et manipuler l'Unicode correctement.
- Utiliser les fonctions courantes de recherche, extraction, remplacement et formatage.
- Échapper une chaîne selon son contexte de sortie (HTML, URL, JSON, SQL).

### 7.1 Créer des chaînes

En PHP, une **chaîne** est une suite d'**octets** (pas de caractères). PHP ne connaît pas l'encodage : c'est à vous de travailler en UTF-8 de bout en bout.

```php
<?php
$nom = 'Alice';

$simple = 'Texte $brut\n';               // aucune interprétation (sauf \\ et \')
$double = "Bonjour $nom\n";              // variables et séquences d'échappement interprétées

$heredoc = <<<TEXTE
    Bonjour {$nom},
    Texte sur plusieurs lignes avec "guillemets".
    TEXTE;                                // l'indentation de la fermeture est retirée (7.3)

$nowdoc = <<<'TEXTE'
    Aucune $interpolation ici.
    TEXTE;

echo $heredoc . PHP_EOL . $nowdoc . PHP_EOL;
```

| Syntaxe | Interpolation | Échappements | Usage |
| --- | --- | --- | --- |
| `'...'` | Non | `\\` et `\'` seulement | Texte fixe |
| `"..."` | Oui | `\n \t \\ \" \$ \u{1F600}` | Texte avec variables |
| `<<<ID … ID` (heredoc) | Oui | Oui | Longs textes, SQL, HTML |
| `<<<'ID' … ID` (nowdoc) | Non | Non | Longs textes bruts |

**Concaténation :** `.` et `.=`. **Accès à un caractère :** `$s[0]` (octet), `$s[-1]` (dernier octet). Pour de l'UTF-8, utilisez `mb_substr($s, $i, 1)`.

### 7.2 Octets, caractères et Unicode

Un caractère accentué ou un emoji occupe **plusieurs octets** en UTF-8 : `strlen('é')` vaut **2**. Les fonctions classiques (`strlen`, `substr`, `strtoupper`, `strrev`, `str_pad`…) travaillent sur les octets et **cassent** les caractères multi-octets. Utilisez les équivalents de l'extension **mbstring** préfixés `mb_` :

| Besoin | Octets (ASCII) | Caractères (UTF-8) |
| --- | --- | --- |
| Longueur | `strlen` | `mb_strlen` |
| Extraire | `substr` | `mb_substr` |
| Majuscules / minuscules | `strtoupper`, `strtolower` | `mb_strtoupper`, `mb_strtolower` |
| Position | `strpos` | `mb_strpos` |
| Découper en caractères | `str_split` | `mb_str_split` |
| Compléter | `str_pad` | `mb_str_pad` (8.3+) |
| Nettoyer | `trim` | `mb_trim`, `mb_ltrim`, `mb_rtrim` (8.4) |
| Première lettre | `ucfirst` | `mb_ucfirst`, `mb_lcfirst` (8.4) |

Pour les **graphèmes** (emoji composés, lettres + accents combinés) : fonctions `grapheme_*` de l'extension `intl`.

```php
<?php
echo strlen('é') . ' octets, ' . mb_strlen('é') . ' caractère' . PHP_EOL;   // → 2 octets, 1 caractère
echo mb_strtoupper('élève') . PHP_EOL;                                       // → ÉLÈVE
echo strtoupper('élève') . PHP_EOL;                                           // les accents ne sont pas transformés
print_r(mb_str_split('été'));                                                // ['é', 't', 'é']
```

### 7.3 Fonctions courantes

| Besoin | Fonctions |
| --- | --- |
| **Recherche** | `str_contains`, `str_starts_with`, `str_ends_with` *(8.0)*, `strpos`, `strrpos`, `stripos`, `strstr`, `substr_count` |
| **Extraction** | `substr($s, $debut, $longueur)`, `strstr`, `strrchr` |
| **Remplacement** | `str_replace`, `str_ireplace`, `substr_replace`, `strtr` |
| **Nettoyage** | `trim`, `ltrim`, `rtrim` (avec liste de caractères en 2ᵉ argument) |
| **Découpe / assemblage** | `explode(',', $s)`, `implode(', ', $t)`, `str_split`, `chunk_split` |
| **Casse** | `strtolower`, `strtoupper`, `ucfirst`, `ucwords`, `lcfirst` |
| **Formatage** | `sprintf`, `printf`, `number_format`, `str_pad`, `wordwrap`, `nl2br` |
| **Comparaison** | `strcmp`, `strcasecmp`, `strncmp`, `strnatcmp`, `similar_text`, `levenshtein`, `soundex`, `metaphone` |
| **Répétition / inversion** | `str_repeat`, `strrev` |
| **HTML** | `htmlspecialchars`, `htmlspecialchars_decode`, `html_entity_decode`, `strip_tags` |
| **Encodage** | `base64_encode`, `bin2hex`, `urlencode`, `rawurlencode`, `json_encode` |

**`strpos` renvoie `false` en cas d'absence mais `0` si la position est le début :** testez toujours avec `!== false`.

```php
<?php
var_dump(strpos('Bonjour', 'B'));                 // → int(0)  : trouvé en position 0 !
var_dump(strpos('Bonjour', 'B') !== false);       // → true
var_dump(str_contains('Bonjour', 'jour'));        // → true (plus lisible)

echo substr('Bonjour', 0, 3) . PHP_EOL;                    // → Bon
echo substr('Bonjour', -3) . PHP_EOL;                       // → our (3 derniers octets)
echo str_replace('a', 'o', 'banane') . PHP_EOL;            // → bonone
echo implode(', ', explode(',', 'a,b,c')) . PHP_EOL;       // → a, b, c
echo sprintf('%05.2f', 3.14159) . PHP_EOL;                 // → 03.14
echo number_format(1234567.891, 2, ',', ' ') . PHP_EOL;    // → 1 234 567,89
echo str_pad('7', 3, '0', STR_PAD_LEFT) . PHP_EOL;         // → 007
echo ucwords('jean de la fontaine') . PHP_EOL;             // → Jean De La Fontaine
echo wordwrap('Un long texte à couper', 10, PHP_EOL, true) . PHP_EOL;
```

**Heredoc indenté (7.3).** L'indentation de la ligne de fermeture est retirée de toutes les lignes du bloc. La fermeture doit être suivie d'un caractère non alphanumérique (`;`, `,`, `)`…).

### 7.4 Traiter la saisie utilisateur

```php
<?php
$_POST = ['nom' => '  Alice Dupont  '];      // simulation d'un formulaire
$phrase = 'un deux  trois';

$nom = trim($_POST['nom'] ?? '');              // retirer les espaces superflus
$nom = mb_substr($nom, 0, 50);                  // limiter la longueur
$mots = preg_split('/\s+/', $phrase, -1, PREG_SPLIT_NO_EMPTY);

echo '[' . $nom . ']' . PHP_EOL;                // → [Alice Dupont]
echo implode('|', $mots) . PHP_EOL;             // → un|deux|trois
```

### 7.5 Échapper pour la sortie

Le **principe cardinal** de la sécurité des chaînes : *échapper au moment de la sortie, en fonction du contexte de destination.* Un même texte s'échappe différemment pour HTML, URL, JSON, SQL ou shell.

| Contexte de sortie | Technique |
| --- | --- |
| Texte HTML ou attribut HTML | \`htmlspecialchars($s, ENT\_QUOTES |
| Composant d'URL | `rawurlencode($s)`, `http_build_query($tableau)` |
| JSON | `json_encode()` (avec `JSON_THROW_ON_ERROR`) |
| SQL | **Requêtes préparées** (jamais d'échappement manuel) |
| Commande shell | Éviter ; sinon `escapeshellarg()` |
| Expression régulière | `preg_quote($s, '/')` |

```php
<?php
$saisie = '<script>alert(1)</script>';

echo htmlspecialchars($saisie, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') . PHP_EOL;
// → &lt;script&gt;alert(1)&lt;/script&gt;

function e(string $s): string      // raccourci utilisé dans les gabarits
{
    return htmlspecialchars($s, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}
```

`htmlspecialchars` convertit `&`, `<`, `>`, `"` et (avec `ENT_QUOTES`) `'` en entités HTML ; elle neutralise ainsi les attaques **XSS** (section 16). `strip_tags()` n'est **pas** une protection suffisante.

### 7.6 Comparer des chaînes

```php
<?php
var_dump('abc' === 'abc');              // → true
echo strcmp('a', 'b') . PHP_EOL;        // → -1 (négatif : 'a' < 'b')
echo strcasecmp('A', 'a') . PHP_EOL;    // → 0 (insensible à la casse)
echo strnatcmp('img2', 'img10') . PHP_EOL;   // → -1 (ordre naturel)

$connu = hash('sha256', 'secret');
$saisi = hash('sha256', 'secret');
var_dump(hash_equals($connu, $saisi));       // comparaison à TEMPS CONSTANT
```

**`hash_equals()`** doit être utilisée pour comparer des secrets (jetons, signatures) : une comparaison ordinaire s'arrête au premier caractère différent, ce qui peut révéler des informations par mesure du temps de réponse (*attaque par canal temporel*).

### 7.7 Encodage

Enregistrez vos fichiers en **UTF-8 sans BOM**, déclarez `Content-Type: text/html; charset=UTF-8` et `<meta charset='UTF-8'>`, configurez `default_charset = 'UTF-8'`, et utilisez `utf8mb4` pour MySQL. Pour convertir : `mb_convert_encoding($s, 'UTF-8', 'ISO-8859-1')` ; pour vérifier : `mb_check_encoding($s, 'UTF-8')`. La translittération (`é` → `e`) s'obtient avec `Transliterator` (intl) pour fabriquer des *slugs*.

### À retenir

- Chaîne = octets ; avec l'UTF-8, utilisez `mb_*`.
- `strpos(...) !== false`, ou mieux `str_contains`.
- Validez à l'entrée, **échappez à la sortie selon le contexte**.
- `hash_equals` pour comparer des secrets.

---

## 8. Dates, heures et expressions régulières

### Objectifs

- Manipuler dates, durées et fuseaux horaires sans erreur.
- Formater une date localisée.
- Écrire et utiliser des expressions régulières (PCRE).

### 8.1 Les bons réflexes sur les dates

Les dates sont une source majeure de bugs (fuseaux, heure d'été, années bissextiles). Règles d'or :

1. Utilisez les classes **`DateTimeImmutable`** (jamais modifiée en place : chaque opération renvoie un **nouvel** objet) et `DateTimeZone` plutôt que `date()` / `strtotime()`.
2. **Stockez en UTC** (ou dans un type `DATETIME`/`TIMESTAMP` cohérent) et **convertissez à l'affichage** dans le fuseau de l'utilisateur.
3. Définissez `date.timezone` ou appelez `date_default_timezone_set('Europe/Paris')`.

```php
<?php
$tz = new DateTimeZone('Europe/Paris');
$maintenant = new DateTimeImmutable('2026-10-11 14:30', $tz);   // date figée ; utilisez 'now' pour l'heure réelle
echo $maintenant->format('d/m/Y H:i') . PHP_EOL;                // → 11/10/2026 14:30

$dans30Jours = $maintenant->modify('+30 days');
echo $dans30Jours->format('d/m/Y') . PHP_EOL;                   // → 10/11/2026

$date = DateTimeImmutable::createFromFormat('!d/m/Y', '25/12/2026', $tz);
$difference = $maintenant->diff($date);                         // objet DateInterval
echo $difference->days . ' jours' . PHP_EOL;                    // → 74 jours

$autreFuseau = $maintenant->setTimezone(new DateTimeZone('Indian/Antananarivo'));
echo $autreFuseau->format('d/m/Y H:i') . PHP_EOL;               // → 11/10/2026 15:30
```

**Formats courants :** `d` jour (01–31), `m` mois (01–12), `Y` année sur 4 chiffres, `H` heure 24 h, `i` minutes, `s` secondes, `D`/`l` jour de la semaine abrégé/complet (anglais), `N` jour ISO (1 = lundi), `W` semaine ISO, `c` format ISO 8601, `U` timestamp Unix, `e` identifiant du fuseau.

**Concepts :**

- **Timestamp Unix** : nombre de secondes depuis le 1er janvier 1970 UTC (`time()`, `$d->getTimestamp()`).
- **`DateInterval`** : durée (`new DateInterval('P1M2DT3H')` = 1 mois, 2 jours, 3 heures) ; `add()` / `sub()` l'appliquent à une date.
- **`DatePeriod`** : itère sur une série de dates.
- **`createFromFormat`** : analyse une date saisie selon un format précis ; le `!` initial remet à zéro les champs non précisés. Vérifiez les erreurs avec `DateTimeImmutable::getLastErrors()`.

```php
<?php
$debut = new DateTimeImmutable('2026-01-30');
echo $debut->add(new DateInterval('P1M'))->format('Y-m-d') . PHP_EOL;   // → 2026-03-02 : piège de fin de mois !
echo $debut->modify('last day of next month')->format('Y-m-d') . PHP_EOL;   // → 2026-02-28

foreach (new DatePeriod($debut, new DateInterval('P1D'), 3) as $jour) {
    echo $jour->format('D d/m') . PHP_EOL;       // 3 récurrences après le début
}
```

**Affichage localisé** avec `IntlDateFormatter` (extension `intl`) :

```php
<?php
$maintenant = new DateTimeImmutable('2026-10-11 14:30', new DateTimeZone('Europe/Paris'));
$fmt = new IntlDateFormatter('fr_FR', IntlDateFormatter::FULL, IntlDateFormatter::SHORT, 'Europe/Paris');
echo $fmt->format($maintenant) . PHP_EOL;      // → dimanche 11 octobre 2026 à 14:30
```

La bibliothèque **Carbon** (surcouche très utilisée) ajoute une API fluide et la localisation. Pour mesurer une durée d'exécution précisément, utilisez `hrtime(true)` ou `microtime(true)`.

### 8.2 Expressions régulières (PCRE)

Une **expression régulière** (*regex*) est un motif décrivant un ensemble de chaînes. PHP utilise la bibliothèque **PCRE** via les fonctions `preg_*`. Le motif est écrit entre **délimiteurs** (ici `/`), suivis éventuellement de **modificateurs**.

**Éléments de syntaxe :**

| Élément | Signification |
| --- | --- |
| `.` | N'importe quel caractère (sauf saut de ligne) |
| `\d` `\w` `\s` | Chiffre, caractère de mot, espace (majuscule = négation) |
| `[abc]` `[a-z]` `[^0-9]` | Classe de caractères, intervalle, négation |
| `^` `$` | Début / fin de chaîne (ou de ligne avec `m`) |
| `*` `+` `?` | 0 ou plus, 1 ou plus, 0 ou 1 |
| `{3}` `{2,5}` | Répétition exacte, bornée |
| `(…)` `(?<nom>…)` | Groupe capturant, groupe nommé |
| `(?:…)` | Groupe non capturant |
| \`a | b\` |
| `\b` | Limite de mot |
| `(?=…)` `(?!…)` | Anticipation positive / négative |
| `*?` `+?` | Quantificateurs **paresseux** (plus court possible) |

**Modificateurs :** `i` (insensible à la casse), `m` (multiligne), `s` (le point inclut le saut de ligne), `u` (**UTF-8 / Unicode**, indispensable avec du texte accentué), `x` (espaces et commentaires autorisés).

```php
<?php
var_dump(preg_match('/^\d{4}-\d{2}-\d{2}$/', '2026-10-11'));   // → int(1) : correspondance

preg_match('/(?<annee>\d{4})-(?<mois>\d{2})/', '2026-10', $m);
echo $m['annee'] . ' / ' . $m['mois'] . PHP_EOL;                // → 2026 / 10

preg_match_all('/\d+/', 'a1b22c333', $tous);
echo implode(', ', $tous[0]) . PHP_EOL;                         // → 1, 22, 333

echo preg_replace('/\s+/', ' ', 'a   b    c') . PHP_EOL;        // → a b c
echo preg_replace_callback('/\d+/', fn($m) => $m[0] * 2, 'a1 b2') . PHP_EOL;   // → a2 b4
echo implode('|', preg_split('/[\s,]+/', 'a, b  c')) . PHP_EOL; // → a|b|c

echo preg_quote('a.b*c', '/') . PHP_EOL;                         // → a\.b\*c : échappe une saisie utilisée dans un motif
```

| Fonction | Rôle |
| --- | --- |
| `preg_match` | Teste et capture la **première** correspondance (renvoie 1, 0 ou `false`) |
| `preg_match_all` | Toutes les correspondances |
| `preg_replace` / `preg_replace_callback` | Remplace (avec valeur / avec fonction) |
| `preg_split` | Découpe selon un motif |
| `preg_quote` | Échappe un texte pour l'insérer dans un motif |
| `preg_last_error_msg()` | Message de la dernière erreur PCRE |

**Bonnes pratiques :** ajoutez `u` pour l'UTF-8 ; ne validez pas un e-mail ou une URL à la regex (utilisez `filter_var`) ; méfiez-vous des motifs à **retour arrière catastrophique** (*ReDoS*), qui peuvent bloquer le serveur sur des entrées hostiles ; commentez les motifs complexes avec le modificateur `x`.

### À retenir

- `DateTimeImmutable` + fuseaux explicites + stockage en UTC.
- Attention aux additions de mois en fin de mois.
- `preg_*` avec le modificateur `u` ; `preg_quote` sur toute saisie insérée dans un motif.

---

## 9. Formulaires et saisies utilisateur

### Objectifs

- Construire un formulaire HTML et traiter sa soumission côté serveur.
- Choisir entre GET et POST.
- Valider rigoureusement les données, afficher les erreurs et pré-remplir les champs.
- Appliquer le motif Post/Redirect/Get et connaître la protection CSRF.

### 9.1 Le principe : requête, formulaire, traitement

Un **formulaire HTML** (`<form>`) regroupe des champs (`<input>`, `<select>`, `<textarea>`) et les envoie au serveur lors du clic sur le bouton d'envoi. Deux attributs de `<form>` sont essentiels :

- **`action`** : l'URL du script PHP qui traite les données (vide = la page courante).
- **`method`** : `get` ou `post`, la méthode HTTP utilisée.

Chaque champ envoie une paire **nom=valeur** ; le nom vient de l'attribut `name` (un champ sans `name` n'est **pas envoyé**). PHP rend ces paires disponibles dans `$_GET` ou `$_POST`.

```html
<form action='traiter.php' method='post'>
    <label>Nom : <input type='text' name='nom' required></label>
    <label>E-mail : <input type='email' name='email' required></label>
    <button type='submit'>Envoyer</button>
</form>
```

```php
<?php
// traiter.php : à lancer avec « php -S localhost:8000 », puis envoyer le formulaire
if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    http_response_code(405);                       // 405 : méthode non autorisée
    exit('Cette page attend une requête POST.');
}

$nom = trim($_POST['nom'] ?? '');
echo 'Bonjour ' . htmlspecialchars($nom, ENT_QUOTES, 'UTF-8');
```

**Cas particuliers de champs :** cases à cocher non cochées et boutons radio non choisis **ne sont pas envoyés** (testez avec `isset`) ; un nom de champ de la forme `options[]` produit un **tableau** côté PHP ; `<select multiple name='choix[]'>` aussi.

### 9.2 `$_GET` ou `$_POST` ?

|  | `$_GET` | `$_POST` |
| --- | --- | --- |
| Transmission | Dans l'**URL** (`?q=php&page=2`) | Dans le **corps** de la requête |
| Visible, mise en favori, partageable | Oui | Non |
| Taille | Limitée (quelques Ko) | Grande (`post_max_size`) |
| Usage | **Lecture** : recherche, filtres, pagination — opérations **idempotentes** sans effet de bord | **Modification** : création, connexion, suppression, envoi de fichiers |
| Sécurité | Ne **jamais** y mettre de secrets (historique, journaux, en-tête *Referer*) | Pas plus « sûr » par nature : il faut valider et protéger contre le CSRF |

Une requête **idempotente** produit le même effet qu'on la répète une ou plusieurs fois (une recherche). Une action qui modifie des données ne doit **jamais** passer par `GET` : les robots d'indexation et les préchargements de navigateur pourraient la déclencher.

`$_REQUEST` mélange GET, POST et cookies : **évitez-le**, on ne sait plus d'où vient une donnée.

### 9.3 Valider les données

**Règle absolue :** toute donnée reçue est **suspecte** (tout client peut forger une requête). Validez le **type**, la **longueur**, le **format** et le **domaine de valeurs** (liste autorisée). Rassemblez les erreurs champ par champ plutôt que de s'arrêter à la première.

```php
<?php
$_POST = ['nom' => '', 'email' => 'pas-un-email', 'age' => '200'];   // simulation

$erreurs = [];

$nom = trim($_POST['nom'] ?? '');
if ($nom === '' || mb_strlen($nom) > 50) {
    $erreurs['nom'] = 'Le nom est obligatoire (50 caractères max).';
}

$email = filter_var($_POST['email'] ?? '', FILTER_VALIDATE_EMAIL);
if ($email === false) {
    $erreurs['email'] = 'Adresse e-mail invalide.';
}

$age = filter_var($_POST['age'] ?? null, FILTER_VALIDATE_INT, ['options' => ['min_range' => 0, 'max_range' => 120]]);
if ($age === false || $age === null) {
    $erreurs['age'] = 'Âge invalide.';
}

if (!$erreurs) {
    echo 'Formulaire valide' . PHP_EOL;
} else {
    foreach ($erreurs as $champ => $message) { fwrite(STDERR, "$champ : $message" . PHP_EOL); }
}
```

**Filtres utiles de `filter_var` :** `FILTER_VALIDATE_EMAIL`, `_INT`, `_FLOAT`, `_BOOLEAN` (avec `FILTER_NULL_ON_FAILURE`), `_URL`, `_IP`, `_DOMAIN`, `_REGEXP`. `filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL)` lit et valide directement.

**Liste blanche** pour les choix : `in_array($_POST['pays'] ?? '', ['FR', 'BE', 'CH'], true)`.

> **Obsolète :** `FILTER_SANITIZE_STRING` est **déprécié depuis PHP 8.1** : ne l'utilisez plus. Le principe actuel est : **valider à l'entrée, échapper à la sortie** (`htmlspecialchars` pour HTML, requêtes préparées pour SQL).

### 9.4 Validation côté client et côté serveur

Les attributs HTML5 (`required`, `type='email'`, `pattern`, `min`, `max`, `maxlength`) et JavaScript améliorent l'**expérience** (retour immédiat) mais **ne protègent rien** : un attaquant peut envoyer une requête sans passer par votre page (avec `curl`, par exemple). **La validation serveur est obligatoire.**

### 9.5 Le motif Post/Redirect/Get (PRG)

Si une page répond directement à un `POST`, recharger la page (F5) **renvoie le formulaire** et peut dupliquer une commande. Le motif **PRG** l'évite : après un traitement réussi, le serveur répond par une **redirection `303`** vers une page `GET` ; un message de confirmation temporaire (*message flash*) est conservé en session.

```php
<?php
// traiter.php
declare(strict_types=1);
session_start();

function enregistrer(string $nom, string $email): void
{
    file_put_contents(__DIR__ . '/inscrits.csv', $nom . ';' . $email . PHP_EOL, FILE_APPEND | LOCK_EX);
}

if ($_SERVER['REQUEST_METHOD'] === 'GET') {          // affichage du message flash
    echo $_SESSION['flash'] ?? 'Aucun message.';
    unset($_SESSION['flash']);                        // il ne s'affiche qu'une fois
    exit;
}

$erreurs = [];
$nom = trim($_POST['nom'] ?? '');
$email = filter_var($_POST['email'] ?? '', FILTER_VALIDATE_EMAIL);
if ($nom === '') { $erreurs['nom'] = 'Le nom est obligatoire.'; }
if ($email === false) { $erreurs['email'] = 'Adresse e-mail invalide.'; }

if (!$erreurs) {
    enregistrer($nom, $email);
    $_SESSION['flash'] = 'Enregistré !';
    header('Location: /traiter.php', true, 303);      // Post/Redirect/Get
    exit;
}

http_response_code(422);                              // 422 : entité non traitable (erreurs de validation)
foreach ($erreurs as $champ => $message) { echo $champ . ' : ' . $message . PHP_EOL; }
```

### 9.6 Pré-remplir après une erreur

Quand la validation échoue, **réaffichez le formulaire avec les valeurs saisies** (échappées) et les messages d'erreur, pour que l'utilisateur ne ressaisisse pas tout. Ne pré-remplissez jamais un champ mot de passe.

```php
<?php
$nom = 'Alice <b>';
$erreurs = ['nom' => 'Le nom est obligatoire.'];
?>
<input type='text' name='nom' value='<?= htmlspecialchars($nom ?? '', ENT_QUOTES, 'UTF-8') ?>'>
<?php if (isset($erreurs['nom'])): ?>
    <span class='erreur'><?= htmlspecialchars($erreurs['nom']) ?></span>
<?php endif; ?>
```

### 9.7 Protection CSRF

Tout formulaire qui **modifie des données** doit contenir un **jeton secret** lié à la session (section 16.3), sans quoi un site tiers pourrait déclencher l'action à l'insu d'un utilisateur connecté.

### À retenir

- `name` obligatoire ; cases non cochées absentes de `$_POST`.
- GET = lecture, POST = modification ; jamais de secret dans l'URL.
- Validation **serveur** systématique ; collecte de toutes les erreurs ; liste blanche pour les choix.
- PRG après un POST réussi ; jeton CSRF sur les formulaires d'action.

---

## 10. Système de fichiers

### Objectifs

- Lire et écrire des fichiers de manière sûre et économe en mémoire.
- Manipuler chemins, dossiers, CSV et JSON.
- Implémenter un téléversement sécurisé.
- Se prémunir contre la traversée de répertoires.

### 10.1 Lecture et écriture rapides

```php
<?php
$fichier = sys_get_temp_dir() . '/notes.txt';

file_put_contents($fichier, 'Ligne' . PHP_EOL);                              // crée ou écrase
file_put_contents($fichier, 'Suite' . PHP_EOL, FILE_APPEND | LOCK_EX);      // ajoute, avec verrou exclusif

$contenu = file_get_contents($fichier);                                     // false en cas d'échec
echo $contenu;

$lignes = file($fichier, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);    // tableau de lignes
print_r($lignes);

unlink($fichier);
```

`file_get_contents` et `file()` **chargent tout en mémoire** : adaptés aux petits fichiers. Pour les gros fichiers, lisez progressivement (10.2). Le drapeau **`LOCK_EX`** demande un **verrou exclusif** pour éviter que deux requêtes simultanées écrivent en même temps et corrompent le fichier.

### 10.2 Ouverture avec `fopen`

`fopen` renvoie une **ressource** (un *flux*) ; il faut tester l'échec, lire/écrire, puis `fclose`.

```php
<?php
$chemin = tempnam(sys_get_temp_dir(), 'donnees');
file_put_contents($chemin, 'première ligne' . PHP_EOL . 'seconde ligne' . PHP_EOL);

$f = fopen($chemin, 'r');
if ($f === false) { throw new RuntimeException('Ouverture impossible'); }

while (($ligne = fgets($f)) !== false) {        // ligne par ligne : mémoire constante
    echo htmlspecialchars($ligne);
}
fclose($f);
unlink($chemin);
```

| Mode | Signification |
| --- | --- |
| `r` | Lecture seule, curseur au début |
| `w` | Écriture, **vide** le fichier (crée s'il n'existe pas) |
| `a` | Ajout à la fin (crée si absent) |
| `x` | Création **exclusive** (échoue si le fichier existe) |
| `r+` `w+` `a+` | Lecture **et** écriture |
| `b` | Mode binaire (`rb`, `wb`) : indispensable sous Windows pour les images |

Fonctions de flux : `fgets` (une ligne), `fread($f, $n)` (n octets), `fwrite`, `feof`, `fseek`/`ftell`/`rewind` (position), `flock($f, LOCK_EX)` (verrou), `fflush`. Les **flux spéciaux** : `php://stdin`, `php://stdout`, `php://stderr` (constantes `STDIN`, `STDOUT`, `STDERR`), `php://input` (corps brut d'une requête), `php://memory`, `php://temp`.

### 10.3 Fonctions utiles

| Fonction | Rôle |
| --- | --- |
| `file_exists()`, `is_file()`, `is_dir()` | Existence / type |
| `is_readable()`, `is_writable()` | Droits |
| `filesize()`, `filemtime()` | Taille, date de modification |
| `unlink()` | Supprimer un fichier |
| `rename()`, `copy()` | Renommer / déplacer, copier |
| `mkdir($d, 0755, true)`, `rmdir()` | Créer (récursif) / supprimer un dossier **vide** |
| `scandir()`, `glob('*.txt')` | Lister |
| `basename()`, `dirname()`, `pathinfo()` | Analyser un chemin |
| `realpath()` | Chemin absolu canonique (résout `..` et liens) ; `false` si inexistant |
| `tempnam()`, `sys_get_temp_dir()` | Fichiers temporaires |
| `chmod()`, `fileperms()` | Droits Unix |

```php
<?php
print_r(pathinfo('/var/www/photo.jpg'));
// ['dirname' => '/var/www', 'basename' => 'photo.jpg', 'extension' => 'jpg', 'filename' => 'photo']
```

**Droits Unix :** `0644` (fichiers : lecture/écriture propriétaire, lecture autres), `0755` (dossiers : traversée autorisée). **N'utilisez jamais `0777`**, qui donne tous les droits à tout le monde.

### 10.4 CSV et JSON

```php
<?php
$dossier = sys_get_temp_dir();

// CSV : écrire (les 3 derniers arguments sont explicites car leur valeur par défaut évolue)
$f = fopen($dossier . '/sortie.csv', 'w');
fputcsv($f, ['nom', 'age'], ',', '"', '\\');
fputcsv($f, ['Alice', 30], ',', '"', '\\');
fclose($f);

// CSV : lire
if (($f = fopen($dossier . '/sortie.csv', 'r')) !== false) {
    $entete = fgetcsv($f, 0, ',', '"', '\\');
    while (($ligne = fgetcsv($f, 0, ',', '"', '\\')) !== false) {
        print_r(array_combine($entete, $ligne));      // ['nom' => 'Alice', 'age' => '30']
    }
    fclose($f);
}

// JSON : écrire puis relire
$donnees = ['nom' => 'Alice', 'villes' => ['Paris', 'Lyon']];
file_put_contents($dossier . '/data.json', json_encode($donnees, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR));
$relu = json_decode(file_get_contents($dossier . '/data.json'), true, 512, JSON_THROW_ON_ERROR);
echo $relu['villes'][1] . PHP_EOL;                    // → Lyon

try {
    json_decode('{invalide', true, 512, JSON_THROW_ON_ERROR);
} catch (JsonException $e) {
    fwrite(STDERR, 'Erreur JSON : ' . $e->getMessage() . PHP_EOL);
}

unlink($dossier . '/sortie.csv');
unlink($dossier . '/data.json');
```

CSV : `fputcsv`/`fgetcsv` gèrent correctement guillemets, séparateurs et sauts de ligne dans les cellules — **n'utilisez pas `explode(',')`** pour lire un CSV. Les cellules lues sont toujours des chaînes : convertissez-les.

**Autres formats :** INI (`parse_ini_file`), XML (`SimpleXMLElement`, `DOMDocument`), YAML (bibliothèque `symfony/yaml`), Excel (PhpSpreadsheet).

### 10.5 Classes SPL pour les fichiers

```php
<?php
$chemin = tempnam(sys_get_temp_dir(), 'gros');
file_put_contents($chemin, 'un' . PHP_EOL . 'deux' . PHP_EOL . 'trois' . PHP_EOL);

$fichier = new SplFileObject($chemin);
foreach ($fichier as $numero => $ligne) {
    if ($ligne === '') { continue; }                       // dernière ligne vide
    echo ($numero + 1) . ' : ' . rtrim($ligne) . PHP_EOL;
}
unlink($chemin);
```

`SplFileObject` offre une interface objet, itérable ligne par ligne. `DirectoryIterator` et `RecursiveDirectoryIterator` parcourent les dossiers ; `Symfony\Component\Finder` et `League\Flysystem` abstraient le stockage (disque local, S3…).

### 10.6 Téléversement sécurisé de fichiers

Le formulaire doit utiliser **`method='post'`** et **`enctype='multipart/form-data'`**. PHP place alors le fichier dans un dossier temporaire et décrit chaque envoi dans `$_FILES['champ']` : `name` (nom d'origine, **falsifiable**), `type` (type MIME déclaré, **falsifiable**), `tmp_name`, `error` (code `UPLOAD_ERR_*`), `size`.

```html
<form action='upload.php' method='post' enctype='multipart/form-data'>
    <input type='file' name='photo' accept='image/*'>
    <button>Envoyer</button>
</form>
```

```php
<?php
declare(strict_types=1);

const DOSSIER = __DIR__ . '/../uploads';          // idéalement HORS de la racine web
const TAILLE_MAX = 2 * 1024 * 1024;               // 2 Mo
const TYPES_AUTORISES = ['image/jpeg' => 'jpg', 'image/png' => 'png', 'image/webp' => 'webp'];

function refuser(string $message, int $statut = 400): never
{
    http_response_code($statut);
    exit($message);
}

if (!is_dir(DOSSIER)) { mkdir(DOSSIER, 0755, true); }

$fichier = $_FILES['photo'] ?? null;

if (!$fichier || $fichier['error'] !== UPLOAD_ERR_OK) {
    refuser('Erreur de téléversement (code ' . ($fichier['error'] ?? '?') . ').');
}
if ($fichier['size'] > TAILLE_MAX) { refuser('Fichier trop volumineux.', 413); }
if (!is_uploaded_file($fichier['tmp_name'])) { refuser('Fichier invalide.'); }

// Type RÉEL détecté par le CONTENU (jamais par $_FILES['type'] ni par l'extension)
$mime = (new finfo(FILEINFO_MIME_TYPE))->file($fichier['tmp_name']);
if (!isset(TYPES_AUTORISES[$mime])) { refuser('Type de fichier non autorisé.', 415); }

// Nouveau nom ALÉATOIRE : on ne réutilise jamais le nom d'origine
$nom = bin2hex(random_bytes(16)) . '.' . TYPES_AUTORISES[$mime];

if (!move_uploaded_file($fichier['tmp_name'], DOSSIER . '/' . $nom)) {
    refuser("Impossible d'enregistrer le fichier.", 500);
}
echo 'Fichier enregistré : ' . $nom;
```

**Réglages `php.ini` :** `file_uploads`, `upload_max_filesize`, `post_max_size` (doit être supérieur ou égal à la taille du fichier), `max_file_uploads`. Pour les images, vous pouvez en plus les **ré-encoder** avec GD ou Imagick, ce qui détruit d'éventuelles charges cachées.

### 10.7 Précautions

**Traversée de répertoires (*path traversal*).** Si un script construit un chemin à partir d'une saisie (`?fichier=../../etc/passwd`), l'attaquant peut lire des fichiers hors du dossier prévu. Défenses : `basename()` pour ne garder que le nom, **liste blanche** de noms autorisés, et vérification que `realpath()` reste dans le dossier racine.

```php
<?php
$racine = sys_get_temp_dir() . '/uploads_demo';
if (!is_dir($racine)) { mkdir($racine, 0755, true); }
file_put_contents($racine . '/photo.jpg', 'contenu');

function cheminSur(string $racine, string $demande): ?string
{
    $chemin = realpath($racine . '/' . basename($demande));
    if ($chemin === false || !str_starts_with($chemin, realpath($racine) . DIRECTORY_SEPARATOR)) {
        return null;
    }
    return $chemin;
}

foreach (['photo.jpg', '../../etc/passwd', 'absent.png'] as $demande) {
    echo (cheminSur($racine, $demande) === null ? 'Refusé : ' : 'Accepté : ') . $demande . PHP_EOL;
}

unlink($racine . '/photo.jpg');
rmdir($racine);
```

Autres précautions : n'**exécutez jamais** un fichier téléversé et interdisez l'exécution de PHP dans le dossier d'envoi ; utilisez `LOCK_EX` pour les écritures concurrentes ; vérifiez les droits du système ; ne servez pas directement des fichiers privés (passez par un script PHP qui contrôle l'autorisation).

### À retenir

- Petits fichiers : `file_get_contents` ; gros fichiers : `fopen` + `fgets` ou générateurs.
- CSV via `fgetcsv`/`fputcsv` ; JSON avec `JSON_THROW_ON_ERROR`.
- Téléversement : taille, type réel (`finfo`), nom aléatoire, dossier hors web.
- Jamais de chemin construit à partir d'une saisie brute.

---

## 11. Sessions et cookies

### Objectifs

- Expliquer l'absence d'état de HTTP et le rôle des cookies et sessions.
- Utiliser `$_SESSION` et `setcookie()` correctement.
- Sécuriser les sessions contre la fixation, le vol et le CSRF.

### 11.1 Le problème : HTTP est sans état

Chaque requête HTTP est **indépendante** : le serveur n'a aucun souvenir de la précédente. Pour reconnaître un visiteur (connexion, panier), on utilise :

- un **cookie** : petite donnée stockée par le **navigateur**, renvoyée automatiquement à chaque requête vers le même site ;
- une **session** : données stockées sur le **serveur**, retrouvées grâce à un **identifiant de session** (`PHPSESSID`) conservé dans un cookie.

|  | `$_SESSION` | `$_COOKIE` |
| --- | --- | --- |
| Stockage | **Serveur** (le navigateur n'a qu'un identifiant) | **Navigateur** |
| Sécurité | Plus sûr | Lisible et **modifiable** par l'utilisateur |
| Taille | Grande | \~4 Ko par cookie |
| Durée | Par défaut jusqu'à la fermeture du navigateur ; expiration serveur | Choisie (`expires`) |
| Usage | Connexion, panier, messages flash, jeton CSRF | Préférences (thème, langue), « se souvenir de moi » (jeton aléatoire) |

### 11.2 Utiliser les sessions

```php
<?php
session_start();                                // AVANT toute sortie ; charge ou crée la session

$_SESSION['utilisateur'] = 'Alice';            // écrit dans la session
echo $_SESSION['utilisateur'] ?? 'Invité', PHP_EOL;     // → Alice

unset($_SESSION['utilisateur']);               // retire une variable
echo $_SESSION['utilisateur'] ?? 'Invité', PHP_EOL;     // → Invité
```

Par défaut, les données sont stockées dans des fichiers du serveur (`session.save_path`). Pour plusieurs serveurs, on les place dans **Redis** ou en base (`session.save_handler`). `session_id()` renvoie l'identifiant ; `session_write_close()` libère le verrou de session (une session verrouille les requêtes concurrentes du même utilisateur).

**Déconnexion complète :** vider le tableau, supprimer le cookie, détruire la session.

```php
<?php
session_start();
$_SESSION = [];
if (ini_get('session.use_cookies')) {
    $p = session_get_cookie_params();
    setcookie(session_name(), '', ['expires' => time() - 42000, 'path' => $p['path'], 'domain' => $p['domain'],
                                   'secure' => $p['secure'], 'httponly' => $p['httponly'], 'samesite' => $p['samesite'] ?: 'Lax']);
}
session_destroy();
```

### 11.3 Les cookies

```php
<?php
// cookie.php : à lancer avec « php -S localhost:8000 » ; rechargez la page pour lire le cookie
if (isset($_COOKIE['theme'])) {
    echo 'Thème : ' . htmlspecialchars($_COOKIE['theme']) . PHP_EOL;   // lisible dès la REQUÊTE SUIVANTE
    setcookie('theme', '', ['expires' => time() - 3600, 'path' => '/']);   // supprimer = expiration dans le passé
    exit;
}

setcookie('theme', 'sombre', [
    'expires'  => time() + 30 * 24 * 3600,     // 30 jours
    'path'     => '/',
    'secure'   => true,                         // envoyé en HTTPS uniquement
    'httponly' => true,                         // invisible pour JavaScript
    'samesite' => 'Lax',                        // limite l'envoi inter-sites (CSRF)
]);
echo 'Cookie envoyé : rechargez la page.' . PHP_EOL;
```

**Attributs d'un cookie :** `expires`/`max-age` (durée ; absent = cookie de session), `path` et `domain` (portée), `Secure`, `HttpOnly`, `SameSite` (`Lax`, `Strict` ou `None`).

> **Attention :** `setcookie()` modifie les **en-têtes HTTP** : il doit être appelé **avant toute sortie**, sinon *« headers already sent »*. Un cookie envoyé n'apparaît dans `$_COOKIE` qu'à la requête suivante. **Sécurité :** ne stockez jamais d'information sensible (mot de passe, droits) dans un cookie : tout son contenu est **modifiable par l'utilisateur**. Si vous devez y mettre une valeur, signez-la ou stockez un jeton aléatoire dont le sens est côté serveur.

**RGPD / ePrivacy :** les cookies non strictement nécessaires (statistiques, publicité) exigent le **consentement** de l'utilisateur dans l'Union européenne.

### 11.4 Sécuriser les sessions

```php
<?php
ini_set('session.use_strict_mode', '1');       // refuse les identifiants inconnus fournis par le client
ini_set('session.use_only_cookies', '1');      // pas d'identifiant dans l'URL
session_set_cookie_params(['lifetime' => 0, 'path' => '/', 'secure' => true, 'httponly' => true, 'samesite' => 'Lax']);
session_start();

// À la connexion réussie : NOUVEL identifiant (anti-fixation de session)
session_regenerate_id(true);
$_SESSION['user_id'] = 42;
$_SESSION['derniere_activite'] = time();

// Expiration par inactivité (30 minutes)
if (time() - ($_SESSION['derniere_activite'] ?? time()) > 1800) {
    session_unset();
    session_destroy();
}
```

**Menaces :**

- **Fixation de session** : l'attaquant impose un identifiant connu à la victime, puis le réutilise après sa connexion. Parade : `session_regenerate_id(true)` à la connexion et à toute élévation de droits, plus `use_strict_mode`.
- **Vol de session** (XSS, réseau) : `HttpOnly`, HTTPS + `Secure`, durée de vie limitée.
- **CSRF** : `SameSite` + jeton (section 16.3).

| Bonne pratique | Pourquoi |
| --- | --- |
| HTTPS partout, cookies `Secure` | Empêche l'interception |
| `HttpOnly` | Protège du vol par un script injecté |
| `SameSite=Lax` ou `Strict` | Réduit le CSRF |
| `session_regenerate_id(true)` après connexion | Anti-fixation |
| Jamais d'identifiant de session dans l'URL | Fuite par *Referer*, historique, journaux |
| Expiration et déconnexion explicite | Limite les sessions volées |
| Stocker l'**identifiant** de l'utilisateur, jamais son mot de passe | Minimiser la donnée sensible |

### 11.5 Aller plus loin

Pour des API, on remplace la session serveur par des **jetons** (JWT, OAuth) : section 20.5. Pour un « se souvenir de moi », stockez en base un **jeton aléatoire haché** associé à l'utilisateur et envoyez-le dans un cookie `HttpOnly` et `Secure`, avec rotation à chaque usage.

### À retenir

- Session = données côté serveur, cookie = identifiant côté client.
- `session_start()` avant toute sortie ; `session_regenerate_id(true)` à la connexion.
- Cookies : `Secure`, `HttpOnly`, `SameSite` ; rien de sensible dedans.

---

## 12. Bases de données avec PDO

### Objectifs

- Comprendre le rôle d'une base de données relationnelle et du SQL dans une application PHP.
- Se connecter avec PDO de façon sûre.
- Écrire des requêtes préparées (protection contre l'injection SQL) et réaliser des opérations CRUD.
- Utiliser les transactions et appliquer les bonnes pratiques.

### 12.1 Notions de base

Une **base de données relationnelle** (MySQL/MariaDB, PostgreSQL, SQLite…) stocke des données dans des **tables** (lignes = enregistrements, colonnes = champs) reliées par des **clés** (clé primaire, clé étrangère). On l'interroge en **SQL** (`SELECT`, `INSERT`, `UPDATE`, `DELETE`). PHP dialogue avec elle par une **extension** : PDO ou MySQLi.

|  | **PDO** (recommandé) | **MySQLi** |
| --- | --- | --- |
| Bases supportées | MySQL, MariaDB, PostgreSQL, SQLite, SQL Server… | MySQL / MariaDB uniquement |
| API | Orientée objet | Objet et procédural |
| Paramètres nommés (`:nom`) | Oui | Non (uniquement `?`) |
| Recommandation | **Standard actuel** | Acceptable pour du 100 % MySQL |

> Les anciennes fonctions `mysql_*` ont été **supprimées en PHP 7** : ne les utilisez jamais.

### 12.2 Connexion avec PDO

La connexion s'établit avec un **DSN** (*Data Source Name* : type de base, hôte, nom, encodage), un utilisateur, un mot de passe et des **options**.

```php
<?php
declare(strict_types=1);

// SQLite en mémoire par défaut (exemple autonome). Pour MySQL :
// DB_DSN='mysql:host=localhost;dbname=boutique;charset=utf8mb4' DB_USER=... DB_PASS=...
$dsn = getenv('DB_DSN') ?: 'sqlite::memory:';

try {
    $pdo = new PDO($dsn, getenv('DB_USER') ?: null, getenv('DB_PASS') ?: null, [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,   // erreurs SQL → exceptions PDOException
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,         // lignes sous forme de tableaux associatifs
        PDO::ATTR_EMULATE_PREPARES   => false,                    // vraies requêtes préparées côté serveur
    ]);
    echo 'Connexion réussie' . PHP_EOL;
} catch (PDOException $e) {
    error_log($e->getMessage());                                  // journaliser, ne JAMAIS afficher
    exit('Service momentanément indisponible.');
}
```

**Pourquoi ces options ?** Sans `ERRMODE_EXCEPTION`, PDO se tait en cas d'erreur ; sans `EMULATE_PREPARES => false`, PDO (pilote MySQL) simule les requêtes préparées côté PHP.

> **Sécurité :** chargez les identifiants depuis des **variables d'environnement** (`getenv()`, fichier `.env` non versionné), jamais en dur dans le code. Une exception de connexion peut contenir le mot de passe dans sa trace : ne l'affichez jamais.

Une connexion est généralement créée **une fois par requête** et partagée (injection de dépendances).

### 12.3 Requêtes préparées et injection SQL

**L'injection SQL** consiste à glisser du SQL dans une saisie qui est concaténée à une requête : l'attaquant modifie la logique, lit ou détruit des données. C'est l'une des vulnérabilités les plus graves et les plus répandues.

**Règle absolue : n'insérez jamais une variable directement dans une requête SQL.** Une **requête préparée** envoie d'abord le **modèle** de requête (avec des **marqueurs**), puis les **valeurs** séparément : la base les traite uniquement comme des données, jamais comme du code.

```php
<?php
$pdo = new PDO('sqlite::memory:', null, null, [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
]);
$pdo->exec('CREATE TABLE users (id INTEGER PRIMARY KEY, nom TEXT, email TEXT, actif INTEGER DEFAULT 1)');
$pdo->exec("INSERT INTO users (nom, email) VALUES ('Alice', 'alice@exemple.com'), ('Bob', 'bob@exemple.com')");

$email = "' OR '1'='1";          // saisie malveillante

// VULNÉRABLE : la condition devient toujours vraie
$lignes = $pdo->query("SELECT * FROM users WHERE email = '$email'")->fetchAll();
echo count($lignes) . ' ligne(s) : l\'injection a réussi' . PHP_EOL;       // → 2

// SÛR : paramètres nommés
$stmt = $pdo->prepare('SELECT id, nom, email FROM users WHERE email = :email AND actif = :actif');
$stmt->execute([':email' => $email, ':actif' => 1]);
var_dump($stmt->fetch());                                    // → bool(false) : aucune ligne

$stmt->execute([':email' => 'alice@exemple.com', ':actif' => 1]);   // la requête préparée se réutilise
print_r($stmt->fetch());

// SÛR : paramètres positionnels
$stmt = $pdo->prepare('INSERT INTO users (nom, email) VALUES (?, ?)');
$stmt->execute(['Chloé', 'chloe@exemple.com']);
echo 'Identifiant créé : ' . $pdo->lastInsertId() . PHP_EOL;         // → 3
```

Pour imposer un type : `$stmt->bindValue(':id', $id, PDO::PARAM_INT);` (ou `bindParam` pour lier une variable par référence). Les marqueurs remplacent des **valeurs** uniquement, pas des identifiants (noms de tables ou de colonnes) ni des mots-clés SQL.

**Clause `IN` dynamique :** générez autant de `?` que de valeurs.

```php
<?php
$pdo = new PDO('sqlite::memory:', null, null, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC]);
$pdo->exec('CREATE TABLE produits (id INTEGER PRIMARY KEY, nom TEXT)');
$pdo->exec("INSERT INTO produits (nom) VALUES ('Stylo'), ('Cahier'), ('Règle')");

$ids = [1, 3];
$marqueurs = implode(',', array_fill(0, count($ids), '?'));
$stmt = $pdo->prepare("SELECT * FROM produits WHERE id IN ($marqueurs)");
$stmt->execute($ids);
foreach ($stmt->fetchAll() as $produit) { echo $produit['id'] . ' : ' . $produit['nom'] . PHP_EOL; }
```

**Noms de tables / colonnes dynamiques :** ils ne se paramètrent pas ; utilisez une **liste blanche**.

```php
<?php
$pdo = new PDO('sqlite::memory:', null, null, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC]);
$pdo->exec('CREATE TABLE produits (id INTEGER PRIMARY KEY, nom TEXT, prix REAL, date TEXT)');
$pdo->exec("INSERT INTO produits (nom, prix, date) VALUES ('Stylo', 1.5, '2026-01-02'), ('Cahier', 3.2, '2026-01-01')");

$_GET['tri'] = 'prix; DROP TABLE produits';          // saisie malveillante simulée

$colonnesTriables = ['nom', 'prix', 'date'];
$tri = in_array($_GET['tri'] ?? '', $colonnesTriables, true) ? $_GET['tri'] : 'nom';
echo 'Tri appliqué : ' . $tri . PHP_EOL;                // → nom
foreach ($pdo->query("SELECT * FROM produits ORDER BY $tri") as $produit) { echo $produit['nom'] . PHP_EOL; }
```

**`LIKE` :** le motif (`%`) fait partie de la **valeur** : `$stmt->execute(['%' . $terme . '%'])`. Échappez `%` et `_` dans `$terme` si nécessaire.

### 12.4 Opérations CRUD

**CRUD** = *Create, Read, Update, Delete* (créer, lire, modifier, supprimer).

```php
<?php
$pdo = new PDO('sqlite::memory:', null, null, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC]);
$pdo->exec('CREATE TABLE users (id INTEGER PRIMARY KEY, nom TEXT, email TEXT, actif INTEGER DEFAULT 1)');
$pdo->exec("INSERT INTO users (nom, email) VALUES ('Alice', 'alice@exemple.com'), ('Bob', 'bob@exemple.com')");

// CREATE
$stmt = $pdo->prepare('INSERT INTO users (nom, email) VALUES (:nom, :email)');
$stmt->execute([':nom' => 'Chloé', ':email' => 'chloe@exemple.com']);
$id = (int) $pdo->lastInsertId();

// READ : plusieurs lignes, puis une seule
foreach ($pdo->query('SELECT id, nom FROM users ORDER BY nom')->fetchAll() as $u) {
    echo htmlspecialchars($u['nom']) . '<br>' . PHP_EOL;       // échapper avant affichage HTML
}
$stmt = $pdo->prepare('SELECT * FROM users WHERE id = ?');
$stmt->execute([$id]);
$user = $stmt->fetch();                                          // false si aucune ligne
echo $user['nom'] . PHP_EOL;                                     // → Chloé

// UPDATE
$stmt = $pdo->prepare('UPDATE users SET nom = :nom WHERE id = :id');
$stmt->execute([':nom' => 'Chloé Martin', ':id' => $id]);
echo $stmt->rowCount() . ' ligne(s) modifiée(s)' . PHP_EOL;     // → 1

// DELETE
$stmt = $pdo->prepare('DELETE FROM users WHERE id = ?');
$stmt->execute([$id]);
echo $stmt->rowCount() . ' ligne(s) supprimée(s)' . PHP_EOL;    // → 1
```

**Modes de récupération :** `FETCH_ASSOC` (tableau associatif), `FETCH_NUM`, `FETCH_OBJ` (objet anonyme), `FETCH_CLASS` (hydrate une de vos classes), `fetchColumn()` (une valeur), `FETCH_KEY_PAIR` (tableau clé => valeur), `FETCH_GROUP`. Pour les gros résultats, itérez avec `foreach ($stmt as $ligne)` au lieu de `fetchAll()` afin de ne pas tout charger en mémoire.

**`UPSERT`** (insérer ou mettre à jour) : `INSERT … ON DUPLICATE KEY UPDATE` (MySQL) ou `ON CONFLICT … DO UPDATE` (PostgreSQL, SQLite).

### 12.5 Transactions

Une **transaction** regroupe plusieurs opérations en un bloc **atomique** : toutes réussissent (`commit`) ou toutes sont annulées (`rollBack`). C'est la garantie **ACID** : Atomicité, Cohérence, Isolation, Durabilité. Exemple classique : un virement bancaire (débit + crédit).

```php
<?php
$pdo = new PDO('sqlite::memory:', null, null, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
$pdo->exec('CREATE TABLE comptes (id INTEGER PRIMARY KEY, solde REAL CHECK (solde >= 0))');
$pdo->exec('INSERT INTO comptes (id, solde) VALUES (1, 50), (2, 10)');

function virement(PDO $pdo, int $de, int $vers, float $montant): void
{
    try {
        $pdo->beginTransaction();
        $pdo->prepare('UPDATE comptes SET solde = solde - ? WHERE id = ?')->execute([$montant, $de]);
        $pdo->prepare('UPDATE comptes SET solde = solde + ? WHERE id = ?')->execute([$montant, $vers]);
        $pdo->commit();
    } catch (Throwable $e) {
        if ($pdo->inTransaction()) { $pdo->rollBack(); }
        throw $e;
    }
}

virement($pdo, 1, 2, 20);                                  // réussit : 30 et 30
try {
    virement($pdo, 1, 2, 100);                             // échoue (solde négatif) : tout est annulé
} catch (PDOException $e) {
    fwrite(STDERR, 'Virement annulé : ' . $e->getMessage() . PHP_EOL);
}
```

**Verrous et concurrence :** `SELECT … FOR UPDATE` verrouille les lignes lues jusqu'à la fin de la transaction ; les **niveaux d'isolation** (`READ COMMITTED`, `REPEATABLE READ`, `SERIALIZABLE`) arbitrent entre cohérence et performance. Sous MySQL, les instructions DDL (`CREATE TABLE`…) valident implicitement la transaction.

### 12.6 Concevoir le schéma

- **Normalisation** : éviter la duplication (1FN, 2FN, 3FN) ; relations 1-N (clé étrangère) et N-N (table d'association).
- **Types adaptés** : `INT`, `DECIMAL(10,2)` pour l'argent (jamais `FLOAT`), `DATETIME`/`TIMESTAMP`, `VARCHAR`, `TEXT`, `JSON`.
- **Contraintes** : `PRIMARY KEY`, `UNIQUE`, `NOT NULL`, `FOREIGN KEY`, `CHECK` : la base est la dernière ligne de défense de l'intégrité des données.
- **Index** : accélèrent les recherches sur les colonnes filtrées/triées/jointes, mais ralentissent légèrement les écritures. `EXPLAIN` montre le plan d'exécution.
- **Le problème N+1** : exécuter 1 requête pour la liste puis 1 requête **par ligne** pour des données liées ; remplacez par une **jointure** (`JOIN`) ou un chargement groupé (`WHERE id IN (…)`).

### 12.7 MySQLi (rappel)

```php
<?php
// Nécessite l'extension mysqli et un serveur MySQL / MariaDB
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);          // erreurs → exceptions

try {
    $conn = new mysqli('localhost', 'user', 'mdp', 'boutique');
    $conn->set_charset('utf8mb4');

    $email = 'alice@exemple.com';
    $stmt = $conn->prepare('SELECT id, nom FROM users WHERE email = ?');
    $stmt->bind_param('s', $email);          // s = string, i = int, d = double, b = blob
    $stmt->execute();
    $resultat = $stmt->get_result();
    while ($ligne = $resultat->fetch_assoc()) { echo $ligne['id'] . ' : ' . $ligne['nom'] . PHP_EOL; }
} catch (mysqli_sql_exception $e) {
    fwrite(STDERR, 'Erreur MySQL : ' . $e->getMessage() . PHP_EOL);
}
```

### 12.8 Bonnes pratiques

- **Requêtes préparées partout**, sans exception.
- Encodage **`utf8mb4`** (Unicode complet, emojis compris).
- Compte de base de données aux **privilèges minimaux** (jamais `root` ; un compte en lecture seule quand c'est possible).
- N'affichez **jamais** une erreur SQL à l'utilisateur : journalisez.
- Créez des **index** adaptés ; évitez `SELECT *` ; **paginez** (`LIMIT`/`OFFSET`, ou pagination par curseur plus performante sur de gros volumes).
- Versionnez le schéma avec des **migrations** (Phinx, Doctrine Migrations, migrations Laravel).
- Pour réduire le code répétitif : constructeur de requêtes ou **ORM** (Eloquent, Doctrine) — qui appliquent eux aussi les requêtes préparées.
- Sauvegardez régulièrement et **testez la restauration**.

### À retenir

- PDO + `ERRMODE_EXCEPTION` + `EMULATE_PREPARES => false`.
- Requêtes préparées pour les **valeurs** ; liste blanche pour les **identifiants**.
- Transactions pour les opérations multiples ; index, pagination, migrations.

---

## 13. Gestion des erreurs et exceptions

### Objectifs

- Distinguer erreurs, avertissements et exceptions ; connaître la hiérarchie `Throwable`.
- Utiliser `try / catch / finally`, lancer et créer ses propres exceptions.
- Configurer l'affichage et la journalisation selon l'environnement.
- Mettre en place des gestionnaires globaux.

### 13.1 Niveaux d'erreurs

Un programme rencontre des situations anormales de gravités diverses. PHP les classe par **niveau** :

| Niveau | Constante | Description |
| --- | --- | --- |
| Avis | `E_NOTICE` | Problème mineur |
| Avertissement | `E_WARNING` | Problème non bloquant (fichier introuvable, variable non définie, clé absente) |
| Fatal | `E_ERROR` | Arrêt immédiat du script |
| Analyse | `E_PARSE` | Erreur de syntaxe |
| Dépréciation | `E_DEPRECATED` | Fonctionnalité à ne plus utiliser (disparaîtra) |
| Utilisateur | `E_USER_ERROR`, `E_USER_WARNING`, `E_USER_NOTICE`, `E_USER_DEPRECATED` | Générés par `trigger_error()` |
| Tous | `E_ALL` | Masque combinant tous les niveaux |

Depuis PHP 7, la plupart des erreurs graves ne sont plus des « erreurs fatales » opaques mais des **exceptions de type `Error`**, que l'on peut attraper. De nombreux avertissements de PHP 7 sont devenus des exceptions (`TypeError`, `ValueError`, `DivisionByZeroError`) en PHP 8.

### 13.2 La hiérarchie `Throwable`

Tout ce qui peut être « lancé » (`throw`) implémente l'interface **`Throwable`**. Deux branches :

```text
Throwable
 ├── Error                        ← erreurs du moteur / de programmation
 │    ├── TypeError (ArgumentCountError)
 │    ├── ValueError
 │    ├── ArithmeticError (DivisionByZeroError)
 │    ├── UnhandledMatchError
 │    └── …
 └── Exception                    ← situations prévisibles, à gérer
      ├── LogicException (InvalidArgumentException, DomainException, …)
      ├── RuntimeException (OutOfBoundsException, UnexpectedValueException, …)
      ├── JsonException, PDOException
      └── vos exceptions personnalisées
```

Convention : `LogicException` = erreur du **programmeur** (appel invalide, à corriger) ; `RuntimeException` = problème qui ne se détecte qu'à l'**exécution** (fichier absent, réseau en panne).

### 13.3 `try` / `catch` / `finally`

```php
<?php
try {
    $resultat = intdiv(10, 0);
    echo $resultat;
} catch (DivisionByZeroError $e) {
    fwrite(STDERR, 'Division par zéro : ' . $e->getMessage() . PHP_EOL);
} catch (InvalidArgumentException | TypeError $e) {    // plusieurs types dans un même catch
    fwrite(STDERR, 'Erreur d\'argument : ' . $e->getMessage() . PHP_EOL);
} catch (Throwable $e) {                                // filet de sécurité : attrape tout
    error_log((string) $e);
} finally {
    echo 'Toujours exécuté (nettoyage)' . PHP_EOL;
}
```

- Les blocs `catch` sont examinés **dans l'ordre** : placez les types les plus **spécifiques** avant les plus généraux.
- **`finally`** s'exécute **toujours**, qu'il y ait eu exception ou non (même après un `return`) : idéal pour fermer un fichier, libérer un verrou.
- Depuis PHP 8, on peut omettre la variable : `catch (JsonException)`.

### 13.4 Lancer et créer des exceptions

```php
<?php
function diviser(float $a, float $b): float
{
    if ($b === 0.0) {
        throw new InvalidArgumentException('Le diviseur ne peut pas être nul.');
    }
    return $a / $b;
}

class SoldeInsuffisantException extends RuntimeException
{
    public function __construct(private float $manque, ?Throwable $precedente = null)
    {
        parent::__construct("Il manque $manque €.", 0, $precedente);
    }
    public function getManque(): float { return $this->manque; }
}

function retirer(float $solde, float $montant): float
{
    if ($montant > $solde) { throw new SoldeInsuffisantException($montant - $solde); }
    return $solde - $montant;
}

try {
    echo diviser(10, 4) . PHP_EOL;                       // → 2.5
    echo diviser(1, 0) . PHP_EOL;
} catch (InvalidArgumentException $e) {
    fwrite(STDERR, 'Erreur : ' . $e->getMessage() . PHP_EOL);
}

try {
    retirer(50, 80);
} catch (SoldeInsuffisantException $e) {
    fwrite(STDERR, $e->getMessage() . ' (manque : ' . $e->getManque() . ')' . PHP_EOL);
}

// Chaînage d'exceptions : conserver la cause d'origine
try {
    try {
        json_decode('{invalide', true, 512, JSON_THROW_ON_ERROR);
    } catch (JsonException $e) {
        throw new RuntimeException('Impossible de lire la configuration.', 0, $e);
    }
} catch (RuntimeException $e) {
    fwrite(STDERR, $e->getMessage() . ' Cause : ' . $e->getPrevious()->getMessage() . PHP_EOL);
}

// throw est une EXPRESSION (8.0)
$x = null;
try {
    $valeur = $x ?? throw new InvalidArgumentException('x manquant');
} catch (InvalidArgumentException $e) {
    fwrite(STDERR, 'Erreur : ' . $e->getMessage() . PHP_EOL);
}
```

**Méthodes de `Throwable` :** `getMessage()`, `getCode()`, `getFile()`, `getLine()`, `getTrace()`, `getTraceAsString()`, `getPrevious()`.

**Quand créer sa propre exception ?** Lorsque l'appelant doit pouvoir **réagir différemment** à ce cas précis (`SoldeInsuffisantException`, `UtilisateurIntrouvableException`). Une exception exprime un **échec** ; elle ne doit pas servir de flux de contrôle normal.

**Codes de retour ou exceptions ?** Préférez les exceptions : un code de retour peut être ignoré silencieusement, une exception ne peut pas l'être.

### 13.5 Configuration et journalisation

La règle d'or : **en développement, on affiche tout ; en production, on n'affiche rien à l'utilisateur et on journalise tout.** Afficher une erreur à un visiteur révèle des chemins, des requêtes et des versions exploitables par un attaquant.

```php
<?php
// Développement
error_reporting(E_ALL);
ini_set('display_errors', '1');

// Production
ini_set('display_errors', '0');
ini_set('log_errors', '1');
$journal = sys_get_temp_dir() . '/app.log';       // en production : /var/log/php/app.log
ini_set('error_log', $journal);

error_log('Message à journaliser');
echo file_get_contents($journal);
unlink($journal);
```

Dans `php.ini` : `error_reporting = E_ALL`, `display_errors = Off` (production), `log_errors = On`.

### 13.6 Gestionnaires globaux

`set_error_handler()` intercepte les erreurs « classiques » (avis, avertissements) ; un usage courant les **convertit en exceptions** pour un traitement uniforme. `set_exception_handler()` reçoit toute exception non attrapée ; `register_shutdown_function()` s'exécute à la fin du script (utile pour intercepter une erreur fatale).

```php
<?php
set_error_handler(function (int $niveau, string $message, string $fichier, int $ligne): bool {
    throw new ErrorException($message, 0, $niveau, $fichier, $ligne);     // erreur → exception
});

set_exception_handler(function (Throwable $e): void {
    error_log((string) $e);                         // détails complets dans le journal
    http_response_code(500);
    echo 'Une erreur est survenue.' . PHP_EOL;       // message GÉNÉRIQUE pour l'utilisateur
});

echo $variableInconnue;                             // avertissement → ErrorException → gestionnaire
```

Pour une journalisation professionnelle : **Monolog** (compatible **PSR-3**, avec niveaux `debug`, `info`, `warning`, `error`, `critical`) et un service de suivi d'erreurs (**Sentry**, **Bugsnag**…) qui regroupe les erreurs et alerte l'équipe.

### 13.7 Déboguer

- `var_dump()`, `print_r()`, `error_log()` pour l'exploration rapide.
- **Xdebug** : points d'arrêt, pas-à-pas, inspection des variables dans l'IDE.
- `debug_backtrace()` / `debug_print_backtrace()` : pile d'appels.
- Frameworks : Symfony Profiler, Laravel Telescope/Debugbar, pages d'erreur détaillées (uniquement en développement).
- **`assert()`** : vérifie des hypothèses en développement (désactivé en production avec `zend.assertions = -1`).

### 13.8 Bonnes pratiques

- Attrapez une exception **là où vous savez réellement la traiter** ; sinon laissez-la remonter.
- Ne **taisez** jamais une erreur : pas d'opérateur `@`, pas de `catch` vide.
- Messages **génériques** pour l'utilisateur, **détails** dans les journaux (sans données sensibles : mots de passe, cartes bancaires).
- Utilisez des exceptions **spécifiques** et `JSON_THROW_ON_ERROR`.
- Libérez les ressources dans `finally`.
- Chaînez la cause d'origine (`$previous`) en relançant une exception.
- Pour l'utilisateur, distinguez les erreurs **attendues** (validation : message clair) des erreurs **internes** (page d'erreur générique, code 500).

### À retenir

- `Throwable` → `Error` (moteur) et `Exception` (applicatif).
- `catch` du plus spécifique au plus général ; `finally` pour le nettoyage.
- Production : `display_errors=Off`, `log_errors=On`.
- Convertissez les avertissements en exceptions pour un code plus sûr.

---

## 14. Programmation orientée objet

### Objectifs

- Comprendre les concepts fondamentaux : classe, objet, encapsulation, héritage, polymorphisme, abstraction.
- Écrire des classes modernes (promotion de propriétés, `readonly`, énumérations, hooks).
- Utiliser interfaces, traits, classes abstraites, méthodes magiques, attributs.
- Organiser le code avec espaces de noms et autochargement PSR-4.

### 14.1 Pourquoi la programmation orientée objet ?

La **programmation orientée objet** (POO) organise un programme en **objets** qui combinent des **données** (propriétés) et des **comportements** (méthodes). Elle répond à un problème de taille : au-delà de quelques centaines de lignes, un code fait de fonctions et de variables globales devient difficile à comprendre, à tester et à faire évoluer.

**Vocabulaire :**

- **Classe** : le plan (le moule) décrivant les propriétés et méthodes d'un type d'objets.
- **Objet / instance** : une réalisation concrète d'une classe, créée avec `new`.
- **Propriété** : variable appartenant à l'objet. **Méthode** : fonction appartenant à l'objet.
- **Constructeur** : méthode spéciale `__construct()` appelée à la création.
- **Encapsulation** : cacher l'état interne et n'exposer qu'une interface contrôlée.
- **Héritage** : une classe fille réutilise et spécialise une classe mère.
- **Polymorphisme** : des objets de classes différentes répondent au même message (même méthode) de façon propre à chacun.
- **Abstraction** : on programme contre un contrat (interface) plutôt qu'une implémentation.

### 14.2 Classes et objets

```php
<?php
declare(strict_types=1);

class Voiture
{
    public string $marque;
    private int $kilometrage = 0;

    public function __construct(string $marque)
    {
        $this->marque = $marque;
    }

    public function rouler(int $km): void
    {
        if ($km < 0) {
            throw new InvalidArgumentException('Distance négative.');
        }
        $this->kilometrage += $km;
    }

    public function getKilometrage(): int
    {
        return $this->kilometrage;
    }
}

$v = new Voiture('Renault');
$v->rouler(120);
echo $v->marque . ' : ' . $v->getKilometrage() . ' km' . PHP_EOL;     // → Renault : 120 km
```

- **`$this`** désigne l'objet courant. **`->`** accède à un membre d'instance ; **`::`** à un membre statique ou à une constante de classe.
- L'état `kilometrage` est **privé** : seul le code de la classe peut le modifier, ce qui permet de garantir ses règles (ici, jamais de distance négative). C'est l'**encapsulation**.
- Une classe par fichier, nom en `PascalCase`, nom de fichier = nom de classe.

### 14.3 Promotion de propriétés du constructeur (8.0) et `readonly` (8.1, 8.2)

Écrire propriétés, paramètres et affectations est répétitif. La **promotion** les fusionne : un paramètre précédé d'un modificateur de visibilité **devient** une propriété.

```php
<?php
class Utilisateur
{
    public function __construct(
        public readonly int $id,            // readonly (8.1) : assignée une seule fois
        public string $nom,
        private ?string $email = null,
    ) {}
}

$u = new Utilisateur(1, 'Alice');
echo $u->id . ' ' . $u->nom . PHP_EOL;       // → 1 Alice

try {
    $u->id = 2;                              // interdit : propriété readonly
} catch (Error $e) {
    fwrite(STDERR, 'Erreur : ' . $e->getMessage() . PHP_EOL);
}

readonly class Point                         // classe readonly (8.2) : toutes ses propriétés le sont
{
    public function __construct(public int $x, public int $y) {}
}
$p = new Point(1, 2);
echo $p->x . ',' . $p->y . PHP_EOL;          // → 1,2
```

Une propriété **`readonly`** doit être typée et ne peut être initialisée qu'**une fois**, depuis l'intérieur de la classe. Elle sert à construire des **objets de valeur immuables** (*value objects*) : plus prévisibles, sans effets de bord.

### 14.4 Visibilité

| Mot-clé | Accessible depuis |
| --- | --- |
| `public` | Partout |
| `protected` | La classe et ses **sous-classes** |
| `private` | La **classe seule** (pas les sous-classes) |

**Règle :** exposez le **minimum** nécessaire (privé par défaut). Modifier un membre public casse tous les appelants ; un membre privé peut évoluer librement.

**Visibilité asymétrique (8.4) :** lecture publique, écriture restreinte, sans getter :

```php
<?php
class Compte
{
    public private(set) float $solde = 0.0;      // lisible partout, modifiable seulement dans la classe
    public function deposer(float $m): void { $this->solde += $m; }
}

$c = new Compte();
$c->deposer(50);
echo $c->solde . PHP_EOL;                         // → 50
try {
    $c->solde = 1000;                             // écriture extérieure : refusée
} catch (Error $e) {
    fwrite(STDERR, 'Erreur : ' . $e->getMessage() . PHP_EOL);
}
```

### 14.5 Hooks de propriétés (8.4)

Un **hook** attache du code au **moment où une propriété est lue (`get`) ou écrite (`set`)**, ce qui remplace la plupart des getters/setters écrits à la main tout en gardant l'écriture `$objet->propriete`.

```php
<?php
class Personne
{
    public string $nomComplet {
        get => $this->prenom . ' ' . $this->nom;            // propriété calculée (virtuelle)
    }

    public string $email {
        set (string $valeur) {                                // validation à l'écriture
            if (!filter_var($valeur, FILTER_VALIDATE_EMAIL)) {
                throw new InvalidArgumentException('E-mail invalide');
            }
            $this->email = strtolower($valeur);
        }
    }

    public function __construct(public string $prenom, public string $nom) {}
}

$p = new Personne('Alice', 'Martin');
echo $p->nomComplet . PHP_EOL;                // → Alice Martin
$p->email = 'ALICE@Exemple.COM';
echo $p->email . PHP_EOL;                     // → alice@exemple.com
```

Les hooks fonctionnent aussi dans les **interfaces** (on peut exiger une propriété lisible) et sont compatibles avec la promotion de propriétés.

### 14.6 Héritage

Le mot-clé **`extends`** crée une classe **fille** qui hérite des propriétés et méthodes **non privées** de la classe **mère**. La fille peut **redéfinir** (*override*) une méthode et appeler celle du parent avec `parent::`.

```php
<?php
class Animal
{
    public function __construct(protected string $nom) {}
    public function parler(): string { return '...'; }
}

class Chien extends Animal
{
    public function parler(): string { return "{$this->nom} dit : Ouaf !"; }
    public function presenter(): string { return parent::parler() . ' (parent)'; }
}

$rex = new Chien('Rex');
echo $rex->parler() . PHP_EOL;        // → Rex dit : Ouaf !
echo $rex->presenter() . PHP_EOL;     // → ... (parent)
```

- **`final class`** ne peut pas être étendue ; **`final function`** ne peut pas être redéfinie. Par défaut, déclarez vos classes `final` et ouvrez-les seulement si nécessaire.
- **`#[\Override]` (8.3)** : vérifie qu'une méthode redéfinit bien une méthode parente (détecte les fautes de frappe).
- La **substitution de Liskov** : une classe fille doit pouvoir remplacer sa mère sans casser le programme (mêmes types acceptés, retours compatibles).
- **Composition plutôt qu'héritage** : l'héritage crée un couplage fort. Souvent, il vaut mieux qu'un objet **contienne** d'autres objets (`Voiture` *a un* `Moteur`) plutôt qu'il en **hérite** (*est un*).

### 14.7 Membres statiques, constantes et liaison statique tardive

Un membre **`static`** appartient à la **classe**, pas à une instance. Une **constante de classe** (`const`) est une valeur fixe associée à la classe.

```php
<?php
class Compteur
{
    public const MAX = 100;                       // constante de classe
    public const string NOM = 'Compteur';         // constante TYPÉE (8.3)
    private static int $total = 0;

    public static function incrementer(): int { return ++self::$total; }
}

Compteur::incrementer();
echo Compteur::incrementer() . PHP_EOL;            // → 2
echo Compteur::MAX . ' ' . Compteur::NOM . PHP_EOL;

// Liaison statique tardive : static:: désigne la classe APPELÉE, self:: la classe où le code est écrit
class Modele { public static function creer(): static { return new static(); } }
class Article extends Modele {}
echo get_class(Article::creer()) . PHP_EOL;        // → Article (avec self, on obtiendrait Modele)
```

Dans le code de la classe : `self::` (cette classe), `static::` (classe appelée, liaison tardive), `parent::` (classe mère). Les membres statiques créent un état global caché : à utiliser avec parcimonie (constantes, fabriques).

### 14.8 Classes abstraites, interfaces et traits

- **Classe abstraite** (`abstract`) : non instanciable, impose des méthodes abstraites que les filles doivent implémenter, et peut fournir du code commun.
- **Interface** (`interface`) : un **contrat** (signatures de méthodes publiques). Une classe peut en implémenter **plusieurs** (`implements`). Elle garantit à l'appelant ce que l'objet sait faire, indépendamment de son implémentation.
- **Trait** (`trait`) : un paquet de propriétés et méthodes **réutilisable horizontalement** dans plusieurs classes (`use`), pour contourner l'héritage simple.

```php
<?php
abstract class Forme
{
    abstract public function aire(): float;
    public function decrire(): string { return sprintf('Aire : %.2f', $this->aire()); }
}

interface Exportable { public function exporter(): string; }

trait Horodatage
{
    private ?DateTimeImmutable $creeLe = null;
    public function marquerCreation(): void { $this->creeLe = new DateTimeImmutable(); }
    public function creeLe(): ?DateTimeImmutable { return $this->creeLe; }
}

class Cercle extends Forme implements Exportable
{
    use Horodatage;

    public function __construct(private float $rayon) {}
    public function aire(): float { return M_PI * $this->rayon ** 2; }
    public function exporter(): string { return json_encode(['rayon' => $this->rayon]); }
}

$c = new Cercle(2);
$c->marquerCreation();
echo $c->decrire() . PHP_EOL;                  // → Aire : 12.57
echo $c->exporter() . PHP_EOL;                 // → {'rayon':2}

try {
    $f = new Forme();                          // une classe abstraite ne s'instancie pas
} catch (Error $e) {
    fwrite(STDERR, 'Erreur : ' . $e->getMessage() . PHP_EOL);
}
```

|  | Classe abstraite | Interface | Trait |
| --- | --- | --- | --- |
| Instanciable | Non | Non | Non |
| Héritage / implémentation | Un seul parent | **Plusieurs** | Plusieurs traits |
| Contient du code | Oui | Non (signatures) | Oui |
| Propriétés | Oui | Non (constantes ; hooks depuis 8.4) | Oui |
| Rôle | Base commune | **Contrat** | **Réutilisation** de code |

**Polymorphisme en pratique :** une fonction typée `Exportable $x` accepte n'importe quel objet respectant le contrat. C'est le fondement de l'injection de dépendances (14.14).

### 14.9 Énumérations (8.1)

Une **énumération** (`enum`) définit un type dont les valeurs possibles sont **un ensemble fini et nommé** (statut, rôle, jour…). Elle remplace avantageusement les constantes éparpillées et les « chaînes magiques ».

```php
<?php
enum Statut: string                   // enum « adossée » : chaque cas a une valeur scalaire
{
    case Brouillon = 'brouillon';
    case Publie = 'publie';

    public function libelle(): string
    {
        return match ($this) {
            self::Brouillon => 'Brouillon',
            self::Publie    => 'Publié',
        };
    }
}

$s = Statut::from('publie');          // lève ValueError si la valeur est inconnue
$t = Statut::tryFrom('inconnu');      // renvoie null
echo $s->value . ' ' . $s->name . ' ' . $s->libelle() . PHP_EOL;    // → publie Publie Publié
echo count(Statut::cases()) . ' cas' . PHP_EOL;                    // → 2 cas
```

Les cas sont des **objets uniques** comparables avec `===`. Une enum peut avoir des méthodes, des constantes et implémenter des interfaces, mais pas de propriétés d'état ni d'héritage. Une enum non adossée (`enum Couleur { case Rouge; … }`) n'a pas de `value`. Les enums s'utilisent directement comme types de paramètres et de propriétés, et les ORM les convertissent.

### 14.10 Méthodes magiques

Ce sont des méthodes dont le nom commence par `__`, appelées automatiquement par PHP dans des situations précises.

| Méthode | Déclenchement |
| --- | --- |
| `__construct()` / `__destruct()` | Création / destruction de l'objet |
| `__toString()` | Conversion en chaîne (`echo $objet`) |
| `__get($n)` / `__set($n, $v)` / `__isset()` / `__unset()` | Accès à une propriété **inaccessible ou inexistante** |
| `__call()` / `__callStatic()` | Appel d'une méthode inexistante |
| `__invoke()` | Utilisation de l'objet comme une fonction |
| `__clone()` | Juste après un `clone` |
| `__serialize()` / `__unserialize()` | Sérialisation personnalisée |
| `__set_state()`, `__debugInfo()` | Export (`var_export`) et affichage (`var_dump`) |

```php
<?php
class Prix implements Stringable
{
    public function __construct(private float $montant) {}
    public function __toString(): string { return number_format($this->montant, 2, ',', ' ') . ' €'; }
}
echo new Prix(12.5) . PHP_EOL;       // → 12,50 €
```

Usez de `__get`/`__set`/`__call` avec modération : ils masquent l'API réelle et gênent les outils d'analyse. Les **propriétés dynamiques** (créer `$obj->nouvelle` sans la déclarer) sont dépréciées depuis 8.2.

### 14.11 Objets : copie et comparaison

Une variable d'objet contient une **poignée** (identifiant) vers l'objet, pas l'objet lui-même. Affecter ou passer un objet **copie la poignée** : les deux variables désignent le **même** objet.

```php
<?php
class Voiture { public function __construct(public string $marque) {} }

$a = new Voiture('A');
$b = $a;              // même objet
$c = clone $a;        // copie SUPERFICIELLE (les objets imbriqués restent partagés ; __clone() permet une copie profonde)

$b->marque = 'B';
echo $a->marque . PHP_EOL;                // → B : $a et $b désignent le même objet
echo $c->marque . PHP_EOL;                // → A : $c est indépendant

$d = clone $a;
var_dump($a == $d);                       // → true  : même classe, propriétés égales
var_dump($a === $d);                      // → false : instances différentes
var_dump($a === $b);                      // → true  : même instance
var_dump($a instanceof Voiture);          // → true

// (8.5) clone avec modification : pratique pour les objets readonly (« with-er »)
final class Coordonnees
{
    public function __construct(public readonly int $x, public readonly int $y) {}
    public function avecX(int $x): static { return clone($this, ['x' => $x]); }
}
$decale = (new Coordonnees(0, 0))->avecX(5);
echo $decale->x . ',' . $decale->y . PHP_EOL;     // → 5,0
```

### 14.12 Attributs (8.0)

Les **attributs** `#[…]` attachent des **métadonnées structurées** à des classes, méthodes, propriétés ou paramètres. Ils sont lus par **réflexion** et servent aux frameworks (routes, validation, mapping ORM, sécurité).

```php
<?php
#[Attribute]
class Route
{
    public function __construct(public string $chemin, public array $methods = ['GET']) {}
}

class Controleur
{
    #[Route('/produits', methods: ['GET'])]
    #[\Deprecated('Utiliser nouvelleMethode()')]            // 8.4
    public function liste(): string { return 'liste des produits'; }
}

$methode = new ReflectionMethod(Controleur::class, 'liste');
foreach ($methode->getAttributes(Route::class) as $attribut) {
    $route = $attribut->newInstance();
    echo $route->chemin . ' ' . implode(',', $route->methods) . PHP_EOL;      // → /produits GET
}
```

Attributs natifs utiles : `#[\Override]` (8.3), `#[\Deprecated]` (8.4), `#[\SensitiveParameter]` (8.2, masque un paramètre dans les traces d'erreur), `#[\NoDiscard]` (8.5, avertit si le retour est ignoré), `#[\AllowDynamicProperties]`.

### 14.13 Espaces de noms et chargement automatique

Un **espace de noms** (*namespace*) regroupe des classes sous un préfixe pour **éviter les collisions de noms** entre votre code et les bibliothèques (`App\Model\Utilisateur` ≠ `Lib\Utilisateur`). `use` importe un nom pour l'écrire court ; les classes globales natives (`DateTime`, `Exception`) s'écrivent avec un `\` initial ou s'importent.

```php
<?php
declare(strict_types=1);

namespace App\Model {
    final class Utilisateur
    {
        public function __construct(public int $id, public string $nom) {}
    }
}

namespace App\Service {
    use App\Model\Utilisateur;
    use InvalidArgumentException;                  // classe globale à importer

    final class UtilisateurService
    {
        public function creer(string $nom): Utilisateur
        {
            if ($nom === '') { throw new InvalidArgumentException('Nom vide'); }
            return new Utilisateur(1, $nom);
        }
    }
}

namespace {
    use App\Service\UtilisateurService;
    $u = (new UtilisateurService())->creer('Alice');
    echo $u::class . ' : ' . $u->nom . PHP_EOL;     // → App\Model\Utilisateur : Alice
}
```

(En pratique, on écrit **un `namespace` par fichier**.) **PSR-4** est la norme de correspondance : le nom complet de la classe détermine le chemin du fichier (`App\Service\UtilisateurService` → `src/Service/UtilisateurService.php`). **Composer** génère l'**autoloader** qui charge un fichier au moment où une classe est utilisée pour la première fois (section 17). Mécanisme sous-jacent :

```php
<?php
// Autoloader PSR-4 minimal (Composer génère l'équivalent dans vendor/autoload.php)
$racine = sys_get_temp_dir() . '/psr4_demo';
if (!is_dir($racine . '/src/Service')) { mkdir($racine . '/src/Service', 0755, true); }
file_put_contents($racine . '/src/Service/Mailer.php', <<<'CLASSE'
    <?php
    namespace App\Service;

    final class Mailer
    {
        public function envoyer(string $nom): string { return "Message pour $nom"; }
    }
    CLASSE);

spl_autoload_register(function (string $classe) use ($racine): void {
    $prefixe = 'App\\';
    if (!str_starts_with($classe, $prefixe)) { return; }
    $fichier = $racine . '/src/' . str_replace('\\', '/', substr($classe, strlen($prefixe))) . '.php';
    if (is_file($fichier)) { require $fichier; }
});

echo (new App\Service\Mailer())->envoyer('Alice') . PHP_EOL;     // → Message pour Alice
```

### 14.14 Concevoir proprement

- **Injection de dépendances** : une classe reçoit ses collaborateurs (via le constructeur) au lieu de les créer elle-même. Le code devient testable (on injecte un faux) et modulable.

```php
<?php
interface Mailer { public function envoyer(string $a, string $m): void; }

final class Inscription
{
    public function __construct(private Mailer $mailer) {}      // dépend d'une INTERFACE
    public function inscrire(string $email): void { $this->mailer->envoyer($email, 'Bienvenue'); }
}
```

- **Principes SOLID** : **S**ingle responsibility (une seule raison de changer), **O**pen/closed (ouvert à l'extension, fermé à la modification), **L**iskov substitution, **I**nterface segregation (interfaces petites et ciblées), **D**ependency inversion (dépendre d'abstractions).
- **DRY** (ne pas se répéter), **KISS** (rester simple), **YAGNI** (ne pas anticiper des besoins hypothétiques).
- **Objets de valeur** immuables (`Email`, `Money`, `Point`) qui valident leurs données à la construction : l'objet existant est **toujours valide**.
- Autres nouveautés : `new` dans les initialiseurs (8.1, `private Logger $log = new NullLogger()`), instanciation sans parenthèses englobantes (8.4, `new Voiture('A')->rouler(10)`), **objets paresseux** (8.4, initialisation différée pour les ORM), fermetures liées (`Closure::bind`, `Closure::fromCallable`).
- **Itération d'objets** : implémentez `IteratorAggregate` (avec un générateur) pour rendre un objet parcourable par `foreach`.

### Pièges fréquents

- Croire qu'affecter un objet le copie (il faut `clone`).
- Hériter par commodité de réutilisation (préférez composition ou trait).
- Tout rendre `public` (casse l'encapsulation).
- Classes « fourre-tout » (`Utils`, `Helper`) qui cumulent des responsabilités.

### À retenir

- Encapsulez : état privé, interface publique réduite ; objets immuables dès que possible.
- Interfaces pour découpler, traits pour réutiliser, `final` par défaut.
- Énumérations pour les ensembles finis ; hooks (8.4) pour valider/calculer des propriétés.
- Namespaces + PSR-4 + Composer ; injection de dépendances.

---

## 15. PHP et le web

### Objectifs

- Maîtriser les en-têtes HTTP, codes de statut, redirections et téléchargements.
- Envoyer des e-mails correctement.
- Appeler des services externes avec cURL ou un client HTTP.
- Manipuler les URL.

### 15.1 Rappels sur HTTP

Une **requête** HTTP comprend : une **méthode** (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `OPTIONS`, `HEAD`), une **URL**, des **en-têtes** et éventuellement un **corps**. Une **réponse** comprend un **code de statut**, des **en-têtes** et un **corps**.

| Famille | Signification | Exemples |
| --- | --- | --- |
| `1xx` | Information | `101` (changement de protocole) |
| `2xx` | Succès | `200` OK, `201` Créé, `204` Pas de contenu |
| `3xx` | Redirection | `301` permanente, `302`/`307` temporaire, `303` voir ailleurs, `304` non modifié |
| `4xx` | Erreur du **client** | `400` requête invalide, `401` non authentifié, `403` interdit, `404` introuvable, `405` méthode non autorisée, `409` conflit, `413` trop volumineux, `415` type non supporté, `422` non traitable, `429` trop de requêtes |
| `5xx` | Erreur du **serveur** | `500` erreur interne, `502`/`503`/`504` passerelle ou service indisponible |

### 15.2 Envoyer des en-têtes

```php
<?php
// api.php : à lancer avec « php -S localhost:8000 » puis « curl -i http://localhost:8000/api.php »
header('Content-Type: application/json; charset=utf-8');   // type et encodage du corps
header('Cache-Control: no-store');                          // directive de cache
http_response_code(201);                                    // code de statut
header_remove('X-Powered-By');                              // retirer une information inutile

if (headers_sent($fichier, $ligne)) {
    exit("En-têtes déjà envoyés ($fichier:$ligne)");
}
echo json_encode(['cree' => true]);
```

> **Attention :** `header()`, `setcookie()` et `session_start()` modifient les en-têtes : ils doivent être appelés **avant toute sortie** (HTML, espace, retour à la ligne, **BOM** d'un fichier mal encodé). Sinon : *« Cannot modify header information – headers already sent »*. `headers_sent($fichier, $ligne)` indique l'endroit fautif. La **temporisation de sortie** (`ob_start()`) peut retarder l'envoi, mais corriger la cause reste préférable.

**Lire les en-têtes de la requête :**

```php
<?php
$methode      = $_SERVER['REQUEST_METHOD'] ?? 'CLI';
$agent        = $_SERVER['HTTP_USER_AGENT'] ?? '';
$autorisation = $_SERVER['HTTP_AUTHORIZATION'] ?? '';
$tous         = function_exists('getallheaders') ? getallheaders() : [];   // selon l'environnement

echo 'Méthode : ' . $methode . PHP_EOL;
echo "Nombre d'en-têtes reçus : " . count($tous) . PHP_EOL;
```

Les en-têtes `HTTP_*` de `$_SERVER` sont **fournis par le client** : n'en faites pas confiance (adresse IP derrière un proxy : `X-Forwarded-For` falsifiable sauf proxy de confiance configuré).

**Négociation de contenu et cache HTTP :** `Accept`/`Content-Type` (format), `ETag` + `If-None-Match` ou `Last-Modified` + `If-Modified-Since` (réponse `304` sans corps si la ressource est inchangée), `Cache-Control: public, max-age=3600`.

### 15.3 Redirections

```php
<?php
header('Location: /tableau-de-bord.php', true, 302);
exit;                          // TOUJOURS arrêter le script après une redirection
```

Sans `exit`, le reste du script **continue de s'exécuter** (et peut afficher ou modifier des données) même si le navigateur est redirigé.

| Code | Usage |
| --- | --- |
| `301` | Redirection **permanente** (SEO : déplacement d'une URL) |
| `302` / `307` | Temporaire (`307` conserve la méthode et le corps) |
| `303` | « Voir ailleurs » : après un POST (motif PRG, section 9.5) |

> **Sécurité : *open redirect*.** Ne redirigez jamais vers une URL fournie directement par l'utilisateur (`?retour=http://site-pirate`) : cela sert au hameçonnage. N'acceptez que des chemins internes ou une **liste blanche**.

### 15.4 Télécharger un fichier

```php
<?php
// telecharger.php?f=rapport.txt
$dossier = __DIR__ . '/fichiers';
if (!is_dir($dossier)) {
    mkdir($dossier);
    file_put_contents($dossier . '/rapport.txt', 'Contenu du rapport' . PHP_EOL);
}
$dossier = realpath($dossier);
$chemin  = realpath($dossier . '/' . basename($_GET['f'] ?? ''));

if ($chemin === false || !str_starts_with($chemin, $dossier . DIRECTORY_SEPARATOR)) {
    http_response_code(404);
    exit('Fichier introuvable.');
}

header('Content-Type: application/octet-stream');
header('Content-Disposition: attachment; filename="' . rawurlencode(basename($chemin)) . '"');
header('Content-Length: ' . filesize($chemin));
header('X-Content-Type-Options: nosniff');
readfile($chemin);                // envoie le fichier en flux, sans le charger en mémoire
exit;
```

`Content-Disposition: attachment` force le téléchargement (au lieu de l'affichage). Pour de gros fichiers ou un fort trafic, déléguez l'envoi au serveur web : `X-Accel-Redirect` (Nginx) ou `X-Sendfile` (Apache), après avoir vérifié l'autorisation en PHP.

### 15.5 Envoyer des e-mails

**La fonction `mail()`** transmet le message au programme de messagerie local (sendmail, msmtp…), qui doit être configuré.

```php
<?php
$ok = mail('dest@exemple.com', 'Sujet', 'Corps du message', [
    'From' => 'noreply@monsite.fr',
    'Content-Type' => 'text/plain; charset=UTF-8',
]);

if ($ok) { echo 'Message remis au serveur de messagerie' . PHP_EOL; }
else     { fwrite(STDERR, "Échec de l'envoi" . PHP_EOL); }
```

Limites : pas d'authentification SMTP, forte probabilité d'être classé en **spam**, aucun suivi. **Risque d'injection d'en-têtes :** si une saisie utilisateur contenant des retours à la ligne est insérée dans `From`, `To` ou `Subject`, l'attaquant peut ajouter des destinataires (envoi massif de spam). Nettoyez-la strictement (`filter_var(..., FILTER_VALIDATE_EMAIL)`, retrait de `\r` et `\n`).

**Bibliothèques (recommandé) : PHPMailer, Symfony Mailer.**

```bash
composer require phpmailer/phpmailer
```

```php
<?php
require __DIR__ . '/vendor/autoload.php';

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

$mail = new PHPMailer(true);                       // true : active les exceptions
try {
    $mail->isSMTP();
    $mail->Host       = getenv('SMTP_HOST');
    $mail->SMTPAuth   = true;
    $mail->Username   = getenv('SMTP_USER');
    $mail->Password   = getenv('SMTP_PASS');
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
    $mail->Port       = 587;
    $mail->CharSet    = 'UTF-8';

    $mail->setFrom('noreply@monsite.fr', 'Mon Site');
    $mail->addAddress('dest@exemple.com');
    $mail->isHTML(true);
    $mail->Subject = 'Bienvenue';
    $mail->Body    = '<p>Bonjour !</p>';
    $mail->AltBody = 'Bonjour !';                   // version texte brut
    $mail->send();
} catch (Exception $e) {
    fwrite(STDERR, "Erreur d'envoi : " . $mail->ErrorInfo . PHP_EOL);
}
```

**Délivrabilité :** configurez pour votre domaine **SPF** (serveurs autorisés), **DKIM** (signature) et **DMARC** (politique), ou utilisez un service transactionnel (Mailgun, Postmark, Amazon SES, Brevo…). Envoyez les e-mails via une **file d'attente** afin de ne pas ralentir la requête de l'utilisateur. Ne mettez jamais de secrets (mots de passe, jetons réutilisables) en clair dans un e-mail : préférez des liens à **usage unique et durée limitée**.

### 15.6 Requêtes HTTP sortantes

Votre serveur PHP peut lui-même **appeler** d'autres API : cURL (extension) ou un client HTTP moderne.

```php
<?php
$jeton = getenv('API_JETON') ?: 'jeton-de-demonstration';

$ch = curl_init('https://api.github.com/zen');
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,           // renvoyer la réponse au lieu de l'afficher
    CURLOPT_TIMEOUT        => 10,             // TOUJOURS définir un délai maximal
    CURLOPT_FOLLOWLOCATION => false,
    CURLOPT_HTTPHEADER     => ['Accept: application/json', 'Authorization: Bearer ' . $jeton, 'User-Agent: guide-php'],
]);
$reponse = curl_exec($ch);

if ($reponse === false) {
    fwrite(STDERR, 'Erreur cURL : ' . curl_error($ch) . PHP_EOL);
} else {
    echo 'Code HTTP : ' . curl_getinfo($ch, CURLINFO_HTTP_CODE) . PHP_EOL;
    echo $reponse . PHP_EOL;
}
curl_close($ch);
```

Plus confortables : **Guzzle** (`composer require guzzlehttp/guzzle`), **Symfony HttpClient** (interface **PSR-18**). Bonnes pratiques : délai d'attente, **nouvelles tentatives** avec attente croissante, vérification du **certificat TLS** (jamais `CURLOPT_SSL_VERIFYPEER => false`), traitement des codes `4xx`/`5xx`, et **protection SSRF** (*Server-Side Request Forgery*) : si l'URL appelée vient d'un utilisateur, validez le domaine, refusez les adresses internes (`127.0.0.1`, `169.254.169.254`, réseaux privés).

### 15.7 Manipuler les URL

```php
<?php
$url = parse_url('https://exemple.com:8080/chemin?x=1#haut');
print_r($url);                         // scheme, host, port, path, query, fragment

parse_str($url['query'], $parametres);
print_r($parametres);                  // ['x' => '1']

echo http_build_query(['q' => 'café', 'page' => 2]) . PHP_EOL;   // → q=caf%C3%A9&page=2

$texte = 'a b&c';
echo urlencode($texte) . PHP_EOL;      // → a+b%26c    (formulaires : espace = +)
echo rawurlencode($texte) . PHP_EOL;   // → a%20b%26c  (RFC 3986 : chemins et paramètres)
```

*(8.5)* L'extension **URI** (`Uri\Rfc3986\Uri`, `Uri\WhatWg\Url`) analyse les URL selon les standards, avec plus de rigueur que `parse_url()`.

### 15.8 Bonnes pratiques

- En-têtes **avant** toute sortie ; `exit` après chaque redirection.
- Toujours préciser `Content-Type` et l'encodage.
- Valider tout ce que vous redirigez, téléchargez ou appelez côté serveur.
- E-mails : SMTP authentifié, SPF/DKIM/DMARC, file d'attente.
- Appels sortants : délai d'attente, gestion d'erreurs, vérification TLS.

### À retenir

- `header()` avant toute sortie ; `Location` + `exit`.
- Un code de statut précis communique le résultat (`201`, `404`, `422`, `429`…).
- `mail()` est limité : PHPMailer ou Symfony Mailer.
- Un appel HTTP sortant exige délai, vérification TLS et prudence (SSRF).

---

## 16. Sécurité

### Objectifs

- Adopter l'état d'esprit « ne jamais faire confiance à l'utilisateur ».
- Connaître et contrer les principales vulnérabilités web : injection SQL, XSS, CSRF, session, fichiers, injections de commandes, désérialisation…
- Gérer correctement mots de passe, aléatoire, HTTPS, configuration et secrets.

### 16.1 Principe général

> **Ne faites jamais confiance aux données venant de l'extérieur** : formulaires, URL, cookies, en-têtes, fichiers téléversés, réponses d'API tierces, contenu de la base. **Validez à l'entrée, échappez à la sortie.**

La sécurité est une **défense en profondeur** : plusieurs couches, de sorte que la défaillance d'une seule ne suffise pas à une compromission. Appliquez aussi le **principe de moindre privilège** : chaque composant (compte de base de données, utilisateur système, jeton d'API) ne reçoit que les droits indispensables.

| Menace | Protection |
| --- | --- |
| **Injection SQL** | Requêtes préparées (PDO) |
| **XSS** (injection de scripts) | `htmlspecialchars()` à l'affichage, CSP |
| **CSRF** | Jeton anti-CSRF, cookies `SameSite` |
| **Fixation / vol de session** | `session_regenerate_id`, `HttpOnly`, HTTPS |
| **Mots de passe faibles / fuites** | `password_hash`, limitation des tentatives, 2FA |
| **Téléversements dangereux** | Type réel, renommage, dossier hors web |
| **Traversée de chemin** | `basename`, `realpath`, liste blanche |
| **Injection de commandes** | Éviter `exec`/`shell_exec` ; `escapeshellarg` |
| **Désérialisation non fiable** | Pas de `unserialize()` sur des données externes → JSON |
| **Inclusion de fichiers** | Jamais de chemin issu de l'utilisateur dans `include` |
| **SSRF** | Valider / filtrer les URL appelées côté serveur |
| **Contrôle d'accès défaillant** | Vérifier l'autorisation **à chaque requête**, côté serveur |

### 16.2 Validation, échappement et XSS

**XSS** (*Cross-Site Scripting*) : un attaquant fait afficher du JavaScript par le navigateur d'autres utilisateurs (commentaire contenant `<script>`), pour voler des sessions, usurper des actions ou défigurer la page. Trois types : **stocké** (enregistré en base), **réfléchi** (renvoyé depuis l'URL), **DOM** (côté JavaScript).

La parade est d'**échapper selon le contexte de sortie** :

```php
<?php
$_POST = ['email' => 'alice@exemple.com'];
$saisie = '<img src=x onerror=alert(1)>';
$donnees = ['titre' => '</script><script>alert(1)</script>'];

// Validation (entrée)
$email = filter_var($_POST['email'] ?? '', FILTER_VALIDATE_EMAIL);
var_dump($email);

// Échappement (sortie), selon le contexte
echo htmlspecialchars($saisie, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') . PHP_EOL;                    // HTML
echo json_encode($donnees, JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT) . PHP_EOL;   // JSON dans un <script>
echo urlencode($saisie) . PHP_EOL;                                                                  // paramètre d'URL
// SQL : requêtes préparées (jamais d'échappement manuel)
```

Si vous devez autoriser du HTML riche (éditeur de texte), passez par une bibliothèque de **liste blanche** comme **HTMLPurifier** ; `strip_tags()` n'est pas une protection. Les moteurs de gabarits modernes (**Twig**, **Blade**) **échappent par défaut** : ne désactivez cette protection qu'en connaissance de cause.

**Content Security Policy (CSP)** : un en-tête qui restreint les sources de scripts, styles, images, etc. Elle limite l'impact d'un XSS résiduel.

```php
<?php
header("Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'self'");
echo 'Page protégée par une politique CSP';
```

### 16.3 CSRF : falsification de requête inter-sites

**CSRF** (*Cross-Site Request Forgery*) : un site malveillant incite le navigateur d'un utilisateur **connecté** à envoyer une requête à votre site (virement, suppression), le navigateur joignant automatiquement ses cookies. Défense : un **jeton aléatoire** secret, placé dans la session et dans un champ caché de chaque formulaire, vérifié à la réception.

```php
<?php
session_start();
if (empty($_SESSION['csrf'])) {
    $_SESSION['csrf'] = bin2hex(random_bytes(32));
}
?>
<form method='post' action='supprimer.php'>
    <input type='hidden' name='csrf' value='<?= htmlspecialchars($_SESSION['csrf']) ?>'>
    <button>Supprimer</button>
</form>
```

```php
<?php
// supprimer.php
session_start();

if (!hash_equals($_SESSION['csrf'] ?? '', $_POST['csrf'] ?? '')) {      // comparaison à temps constant
    http_response_code(403);
    exit('Requête refusée (jeton CSRF invalide).');
}
echo 'Suppression effectuée';
```

Complément : cookies **`SameSite=Lax/Strict`**, contrôle de l'en-tête `Origin`/`Referer`, et **méthodes HTTP appropriées** (jamais d'action destructive sur `GET`). Les frameworks intègrent cette protection : ne la désactivez pas.

### 16.4 Mots de passe

Ne stockez **jamais** un mot de passe en clair, ni haché par `md5()`/`sha1()`/`hash('sha256')` seuls (calculés trop vite : des milliards d'essais par seconde), ni avec un sel « maison ». Utilisez une fonction de hachage **lente et salée** conçue pour cela : `password_hash()`.

```php
<?php
$motDePasse = 'correct horse battery staple';
$hash = password_hash($motDePasse, PASSWORD_DEFAULT);       // algorithme sûr du moment + sel aléatoire intégré
// Option plus robuste : PASSWORD_ARGON2ID

if (password_verify('correct horse battery staple', $hash)) {
    if (password_needs_rehash($hash, PASSWORD_DEFAULT)) {    // migrer vers un meilleur algorithme/coût au fil des connexions
        $nouveau = password_hash('correct horse battery staple', PASSWORD_DEFAULT);
        // … mise à jour en base
    }
    echo 'Connecté' . PHP_EOL;
}

if (!password_verify('mauvais mot de passe', $hash)) {
    fwrite(STDERR, 'Identifiants invalides' . PHP_EOL);     // même message que l'e-mail ou le mot de passe soit faux
}
```

- La colonne de base doit accepter **255 caractères** (`VARCHAR(255)`) : la longueur des hachés peut évoluer.
- Exigez une longueur minimale (12 caractères conseillés plutôt que des règles de complexité), vérifiez les mots de passe **compromis** (API *Have I Been Pwned* en k-anonymat), **limitez les tentatives** (*rate limiting*, verrouillage temporaire), proposez l'**authentification à deux facteurs** et les **passkeys** (WebAuthn).
- Message de connexion **identique** que l'e-mail ou le mot de passe soit faux (évite l'**énumération de comptes**) ; le temps de réponse doit être comparable.
- Réinitialisation : jeton aléatoire **à usage unique**, durée courte, stocké **haché** en base.

### 16.5 Aléatoire et jetons

```php
<?php
echo strlen(random_bytes(32)) . ' octets' . PHP_EOL;       // octets cryptographiquement sûrs
echo bin2hex(random_bytes(16)) . PHP_EOL;                  // jeton hexadécimal (32 caractères)
echo random_int(100000, 999999) . PHP_EOL;                 // entier sûr (codes à usage unique)
// À éviter pour la sécurité : rand(), mt_rand(), uniqid() sont prévisibles
```

**Chiffrement :** pour chiffrer des données, utilisez **libsodium** (`sodium_crypto_secretbox`, intégrée à PHP) plutôt que d'inventer un schéma avec `openssl_*` ; ne créez jamais votre propre algorithme de chiffrement.

### 16.6 Autres vulnérabilités

- **Injection de commandes** : évitez `exec`, `shell_exec`, `system`, `passthru`, `proc_open` avec des données externes ; sinon `escapeshellarg()` et une liste blanche d'options. Préférez les bibliothèques PHP aux commandes externes.
- **Désérialisation non fiable** : `unserialize()` sur une donnée contrôlée par l'utilisateur permet d'instancier des objets arbitraires (*injection d'objets*) et d'exécuter du code. Utilisez **JSON** ; si indispensable, `unserialize($d, ['allowed_classes' => false])`.
- **Inclusion de fichiers** (LFI/RFI) : jamais de chemin issu de l'utilisateur dans `include`/`require` ; `allow_url_include=Off`.
- **XXE** (entités externes XML) : désactivez le chargement d'entités externes lors de l'analyse XML (comportement par défaut sûr dans les versions récentes de libxml).
- **Contrôle d'accès** (*IDOR*) : si `?facture=1042` retourne la facture sans vérifier qu'elle appartient à l'utilisateur, n'importe qui lit les autres. Vérifiez **l'autorisation sur chaque ressource**, côté serveur.
- **Redirection ouverte, SSRF, détournement de clic** (*clickjacking* : `X-Frame-Options` / `frame-ancestors`).
- **Divulgation d'informations** : messages d'erreur détaillés, `phpinfo()` accessible, fichiers `.git`, `.env`, sauvegardes (`.sql`, `.bak`) sous la racine web.
- **Race conditions** : des requêtes simultanées contournent une vérification (solde, stock) : transactions et verrous.

### 16.7 Téléversements (rappel)

Taille limitée · type **réel** (`finfo`) · nom **aléatoire** · dossier **hors racine web** ou exécution PHP interdite · aucune confiance dans l'extension ni dans le type MIME envoyés par le navigateur (section 10.6).

### 16.8 HTTPS et en-têtes de sécurité

HTTPS chiffre les échanges et authentifie le serveur (certificats gratuits via **Let's Encrypt**). Redirigez tout le trafic HTTP vers HTTPS **au niveau du serveur web**, et ajoutez des en-têtes :

```php
<?php
const DOMAINE = 'exemple.com';                // nom de domaine fixe issu de la configuration

if (empty($_SERVER['HTTPS']) || $_SERVER['HTTPS'] === 'off') {
    header('Location: https://' . DOMAINE . $_SERVER['REQUEST_URI'], true, 301);
    exit;
}

header('Strict-Transport-Security: max-age=31536000; includeSubDomains');   // HSTS : le navigateur exigera HTTPS
header('X-Content-Type-Options: nosniff');                                  // empêche le « reniflage » de type MIME
header('X-Frame-Options: DENY');                                            // anti-clickjacking (ou CSP frame-ancestors)
header('Referrer-Policy: strict-origin-when-cross-origin');
header('Permissions-Policy: camera=(), microphone=(), geolocation=()');
```

> `$_SERVER['HTTP_HOST']` provient du client : n'en dépendez pas pour construire des URL ; utilisez un **nom de domaine fixe** issu de la configuration.

### 16.9 Configuration et déploiement sûrs

| Réglage | Valeur recommandée en production |
| --- | --- |
| `display_errors` | `Off` |
| `expose_php` | `Off` |
| `allow_url_include` | `Off` |
| `session.cookie_httponly`, `session.cookie_secure`, `session.use_strict_mode` | `1` |
| `disable_functions` | `exec, shell_exec, system, passthru, proc_open` si non nécessaires |
| `open_basedir` | Restreindre les dossiers accessibles |

- **Secrets** (clés d'API, mots de passe) dans des **variables d'environnement** ou un coffre-fort ; jamais dans Git. Si un secret a été publié par erreur, **révoquez-le** (le supprimer de l'historique ne suffit pas). Le fichier `.env` reste hors de la racine web (bibliothèque `vlucas/phpdotenv`).
- Racine web = dossier **`public/`** uniquement.
- **Mises à jour** régulières de PHP, du serveur et des dépendances ; `composer audit` détecte les vulnérabilités connues.
- **Journalisez** les événements de sécurité (échecs de connexion, accès refusés) ; **sauvegardez** et testez la restauration ; sécurisez l'accès administrateur (2FA, IP limitées).
- **Dépendances** : n'installez que des paquets maintenus ; verrouillez les versions (`composer.lock`).

### 16.10 Liste de contrôle

- [ ] Requêtes préparées partout
- [ ] Sortie HTML échappée (ou moteur de gabarits à échappement automatique)
- [ ] Jeton CSRF sur chaque formulaire d'action
- [ ] `password_hash` / `password_verify`, limitation des tentatives
- [ ] Sessions durcies et HTTPS partout
- [ ] Autorisation vérifiée sur chaque ressource
- [ ] Téléversements contrôlés
- [ ] Erreurs masquées, journaux actifs
- [ ] Secrets hors du dépôt
- [ ] Dépendances à jour (`composer audit`)

Référence : **OWASP Top 10** (owasp.org/www-project-top-ten) et les *Cheat Sheets* OWASP.

### À retenir

- Valider en entrée, échapper en sortie selon le contexte, requêtes préparées, jeton CSRF.
- `password_hash`, `random_bytes`, HTTPS, cookies durcis.
- Moindre privilège, défense en profondeur, mises à jour, secrets hors du code.

---

## 17. Composer et gestion des dépendances

### Objectifs

- Comprendre le rôle d'un gestionnaire de dépendances et de l'autochargement.
- Maîtriser `composer.json`, `composer.lock`, les contraintes de version et les commandes courantes.
- Créer et publier son propre paquet.

### 17.1 Qu'est-ce que Composer ?

Une **dépendance** est une bibliothèque externe dont votre projet a besoin (envoi d'e-mails, journalisation, client HTTP…). **Composer** est le **gestionnaire de dépendances** de PHP : il lit la liste des bibliothèques requises dans **`composer.json`**, télécharge celles-ci **et leurs propres dépendances** (résolution récursive des versions compatibles), les place dans **`vendor/`** et génère un **autoloader**. Les paquets sont référencés sur **Packagist** (packagist.org), le dépôt public principal.

```bash
# Installation : voir getcomposer.org/download (script d'installation vérifié) ou :
brew install composer              # macOS
winget install Composer.Composer   # Windows
composer --version
```

### 17.2 Le fichier `composer.json`

```json
{
    "name": "monorg/mon-projet",
    "description": "Application d'exemple",
    "type": "project",
    "require": {
        "php": "^8.3",
        "monolog/monolog": "^3.0",
        "vlucas/phpdotenv": "^5.6"
    },
    "require-dev": {
        "phpunit/phpunit": "^12.0"
    },
    "autoload": {
        "psr-4": { "App\\": "src/" }
    },
    "autoload-dev": {
        "psr-4": { "Tests\\": "tests/" }
    },
    "scripts": {
        "test": "phpunit",
        "stan": "phpstan analyse src"
    },
    "config": { "sort-packages": true }
}
```

- **`require`** : dépendances nécessaires en production (et version de PHP/extensions : `"ext-mbstring": "*"`).
- **`require-dev`** : dépendances de développement (tests, outils d'analyse), absentes en production.
- **`autoload`** : règles de chargement automatique (PSR-4 : le préfixe d'espace de noms `App\` correspond au dossier `src/`).
- **`scripts`** : raccourcis de commandes (`composer test`).
- **`composer.lock`** : fichier **généré** qui fige les versions **exactes** installées (et leurs empreintes) pour que chaque machine obtienne les mêmes versions.

### 17.3 Commandes courantes

```bash
composer init                                # créer composer.json interactivement
composer require monolog/monolog             # ajouter une dépendance (met à jour json + lock + vendor)
composer require --dev phpunit/phpunit       # dépendance de développement
composer install                             # installer EXACTEMENT les versions de composer.lock (reproductible)
composer update                              # mettre à jour dans les contraintes → réécrit composer.lock
composer update monolog/monolog              # un seul paquet
composer remove monolog/monolog
composer outdated                            # paquets ayant des versions plus récentes
composer audit                               # vulnérabilités connues dans vos dépendances
composer show                                # liste des paquets installés
composer why monolog/monolog                 # qui exige ce paquet ?
composer why-not php 8.5                     # qui bloque cette version ?
composer validate                            # vérifie composer.json
composer run test                            # exécuter un script
composer install --no-dev --optimize-autoloader    # production
```

**`install` ou `update` ?** `install` lit le lock (version exacte, **à utiliser en déploiement et en CI**) ; `update` recalcule les versions autorisées par les contraintes et **réécrit** le lock (à faire consciemment, puis tester).

### 17.4 Contraintes de version (SemVer)

Le **versionnement sémantique** (*SemVer*) : `MAJEUR.MINEUR.CORRECTIF`. Un **correctif** corrige des bugs sans changer l'API ; une version **mineure** ajoute des fonctionnalités de façon rétrocompatible ; une version **majeure** peut casser la compatibilité.

| Écriture | Signification |
| --- | --- |
| `^1.2` | `>= 1.2.0` et `< 2.0.0` (le plus courant : tout sauf la prochaine majeure) |
| `^0.3` | `>= 0.3.0` et `< 0.4.0` (en `0.x`, la mineure se comporte comme une majeure) |
| `~1.2` | `>= 1.2.0` et `< 2.0.0` ; `~1.2.3` : `>= 1.2.3` et `< 1.3.0` |
| `1.2.*` | N'importe quel correctif de 1.2 |
| `>=1.2 <2.0` | Intervalle explicite |
| `dev-main` | Branche de développement (instable) |

> **Bonne pratique :** **versionnez `composer.lock`** pour les **applications** (reproductibilité) ; pour une **bibliothèque** destinée à être installée par d'autres, ne le versionnez pas toujours (ses utilisateurs ont leur propre lock). **Ne versionnez jamais `vendor/`.**

### 17.5 Chargement automatique

Sans autoloader, chaque classe exigerait un `require`. Composer génère `vendor/autoload.php` ; une seule inclusion suffit.

```php
<?php
// Prérequis : "autoload": {"psr-4": {"App\\": "src/"}} et une classe App\Service\Mailer dans src/Service/Mailer.php
require __DIR__ . '/vendor/autoload.php';       // une seule inclusion pour tout le projet

use App\Service\Mailer;

$mailer = new Mailer();
echo $mailer::class . PHP_EOL;                  // → App\Service\Mailer
```

Après avoir modifié la section `autoload` : `composer dump-autoload` (avec `-o` pour produire une **carte de classes** optimisée en production). Autres types : `classmap` (analyse de dossiers), `files` (fichiers de fonctions toujours chargés).

### 17.6 Créer et publier son propre paquet

1. Structure : `src/`, `tests/`, `composer.json`, `README.md`, `LICENSE`.
2. `composer.json` : `"name": "vendeur/paquet"`, `"autoload"` PSR-4, `"require": {"php": "^8.2"}`, licence.
3. Dépôt Git public avec des **tags SemVer** (`v1.0.0`) : Packagist déduit les versions des tags.
4. Soumission sur Packagist, avec *webhook* pour la mise à jour automatique.
5. Vérification : `composer validate`.

Travailler sur un paquet local sans le publier :

```json
"repositories": [{ "type": "path", "url": "../mon-paquet" }]
```

### 17.7 Sécurité de la chaîne d'approvisionnement

Chaque dépendance est du code exécuté chez vous : une faille ou un paquet malveillant se propage (*supply chain*). Mesures : lancer `composer audit` régulièrement (et en intégration continue), préférer des paquets **maintenus** et largement utilisés, relire les mises à jour importantes, verrouiller via `composer.lock`, limiter les dépendances, et vérifier l'orthographe d'un nom de paquet (attaques par **typosquatting**).

### 17.8 Bonnes pratiques

- Exiger une **version de PHP** (`"php": "^8.3"`) dans `require`.
- Respecter les **PSR** (normes du PHP-FIG) : **PSR-1/PSR-12** (style de code), **PSR-3** (journaux), **PSR-4** (autochargement), **PSR-7/PSR-17/PSR-18** (HTTP), **PSR-11** (conteneur d'injection), **PSR-6/PSR-16** (cache).
- Séparer `require` et `require-dev` ; en production, `--no-dev`.
- Mettre à jour souvent, par petits pas.

### À retenir

- `composer.json` = intention ; `composer.lock` = versions exactes ; `vendor/` jamais versionné.
- `^` autorise tout sauf la prochaine majeure ; `install` en production et CI.
- `composer audit` : une habitude de sécurité.

---

## 18. Frameworks PHP

### Objectifs

- Expliquer pourquoi et quand utiliser un framework.
- Comprendre l'architecture MVC et le cycle requête-réponse d'un framework.
- Connaître les principaux frameworks et choisir le bon.

### 18.1 Pourquoi un framework ?

Un **framework** est un ensemble structuré de composants et de conventions qui résout les problèmes communs : routage, accès aux données, gabarits, sécurité (CSRF, XSS, authentification), validation, mail, files d'attente, tests, ligne de commande. Il impose une **architecture** et inverse le contrôle : c'est le framework qui appelle votre code (*principe d'Hollywood*).

| Avantage | Inconvénient |
| --- | --- |
| Productivité, conventions partagées | Courbe d'apprentissage |
| Sécurité intégrée et mises à jour | Dépendance au framework et à ses versions |
| Architecture claire, tests facilités | Surcoût pour de très petits scripts |
| Écosystème et recrutement | Risque de « magie » opaque |

**MVC** (*Modèle – Vue – Contrôleur*) est l'architecture la plus courante :

- **Modèle** : données et règles métier (accès à la base).
- **Vue** : présentation (gabarits HTML).
- **Contrôleur** : reçoit la requête, appelle le modèle, choisit la vue.

Cycle d'une requête : le serveur envoie tout à un **point d'entrée unique** (`public/index.php`) → le **routeur** associe l'URL à un contrôleur → des **middlewares** (authentification, CSRF…) filtrent → le contrôleur utilise des **services** (injectés par le **conteneur d'injection de dépendances**) → une **réponse** est renvoyée.

### 18.2 Laravel

Le framework **le plus populaire** : syntaxe expressive, écosystème complet, très bonne documentation.

```bash
composer create-project laravel/laravel mon-app
cd mon-app
php artisan serve
```

```php
<?php
// routes/web.php
use App\Http\Controllers\ArticleController;
use Illuminate\Support\Facades\Route;

Route::get('/articles/{id}', [ArticleController::class, 'show']);
```

```php
<?php
// app/Http/Controllers/ArticleController.php
namespace App\Http\Controllers;

use App\Models\Article;

class ArticleController extends Controller
{
    public function show(int $id)
    {
        return view('articles.show', ['article' => Article::findOrFail($id)]);   // 404 automatique si absent
    }
}
```

| Fonctionnalité | Description |
| --- | --- |
| **Artisan** | CLI (`make:model`, `migrate`, `queue:work`…) |
| **Eloquent** | ORM de type *Active Record* (un modèle = une table) |
| **Blade** | Moteur de gabarits à échappement automatique |
| **Migrations / seeders** | Versionnement du schéma et jeux de données |
| **Files d'attente, planificateur, événements** | Tâches asynchrones et planifiées |
| **Auth** | Kits de démarrage (Breeze, Jetstream), **Sanctum** (API/SPA), **Passport** (OAuth2) |
| **Front** | Livewire, Inertia, Vite |
| **Performance** | Octane (FrankenPHP / Swoole / RoadRunner) |
| **Outils** | Sail (Docker), Pint (style), Forge / Cloud (déploiement) |

### 18.3 Symfony

Framework **modulaire** de niveau entreprise ; ses **composants** indépendants (HttpFoundation, Console, Routing, Mailer…) sont utilisés par Laravel, Drupal et bien d'autres.

```bash
composer create-project symfony/skeleton:'7.*' mon-app    # ou la dernière version stable
# Symfony CLI : symfony new mon-app --webapp
```

| Élément | Rôle |
| --- | --- |
| **Twig** | Moteur de gabarits |
| **Doctrine** | ORM de type *Data Mapper* (les objets métier ignorent la base) |
| **Flex / Maker** | Recettes d'installation, génération de code |
| **Messenger, Mailer, HttpClient, Security, Console, Validator** | Composants indépendants |
| **Versions LTS** | Support long terme, adapté aux grands projets |

### 18.4 CodeIgniter 4

Framework **léger** et rapide à prendre en main, à faible empreinte ; adapté aux petits projets et aux hébergements simples.

```bash
composer create-project codeigniter4/appstarter mon-app
php spark serve
```

### 18.5 Slim (micro-framework)

Idéal pour des **API** et services : routage, middlewares PSR-7/PSR-15, rien de plus.

```php
<?php
// index.php : après « composer require slim/slim slim/psr7 », « php -S localhost:8000 index.php »
use Slim\Factory\AppFactory;

require __DIR__ . '/vendor/autoload.php';

$app = AppFactory::create();
$app->addErrorMiddleware(true, true, true);

$app->get('/bonjour/{nom}', function ($request, $response, array $args) {
    $response->getBody()->write('Bonjour ' . htmlspecialchars($args['nom']));
    return $response;
});
$app->run();
```

### 18.6 Comparaison et choix

| Framework | Idéal pour | Courbe d'apprentissage | Points forts |
| --- | --- | --- | --- |
| **Laravel** | Applications web complètes, startups | Moyenne | Écosystème, productivité |
| **Symfony** | Grands projets, entreprise | Élevée | Modularité, stabilité, LTS |
| **CodeIgniter** | Petits projets, hébergement simple | Faible | Légèreté |
| **Slim** | API, microservices | Faible | Minimaliste, PSR-7 |
| **API Platform** | API REST/GraphQL | Moyenne | Génération d'API depuis le modèle (Symfony) |

Autres : **CakePHP**, **Yii**, **Laminas** ; CMS : **WordPress**, **Drupal**.

**Comment choisir ?** Selon la taille et la durée de vie du projet, les compétences de l'équipe, l'écosystème (paquets, hébergement, communauté), le besoin de support long terme et les performances attendues. Vérifiez toujours la **version actuelle** et la **version minimale de PHP** requise sur le site officiel avant de démarrer.

### À retenir

- Un framework apporte structure, sécurité et productivité ; il se paie en apprentissage.
- MVC, point d'entrée unique, routeur, middlewares, conteneur d'injection de dépendances.
- Laravel (productivité), Symfony (modularité, LTS), Slim (API légères).

---

## 19. Tests et qualité du code

### Objectifs

- Comprendre pourquoi tester et la pyramide des tests.
- Écrire des tests unitaires avec PHPUnit, utiliser fournisseurs de données et doublures.
- Pratiquer le TDD ; connaître les outils d'analyse statique, de style et d'intégration continue.

### 19.1 Pourquoi tester ?

Un **test automatisé** est un programme qui vérifie qu'un autre programme se comporte comme prévu. Il détecte les **régressions** (un changement casse une fonctionnalité existante), documente le comportement attendu et permet de **refactoriser** sans peur.

**Pyramide des tests :** beaucoup de **tests unitaires** (une classe/fonction isolée, rapides), moins de tests d'**intégration** (plusieurs composants, base de données), très peu de tests **de bout en bout** (navigateur, lents et fragiles).

### 19.2 Tests unitaires avec PHPUnit

```bash
composer require --dev phpunit/phpunit
vendor/bin/phpunit --version
```

`phpunit.xml` minimal :

```xml
<?xml version='1.0' encoding='UTF-8'?>
<phpunit bootstrap='vendor/autoload.php' colors='true'>
    <testsuites>
        <testsuite name='Unit'><directory>tests</directory></testsuite>
    </testsuites>
</phpunit>
```

Classe à tester :

```php
<?php
// src/Calculatrice.php
namespace App;

class Calculatrice
{
    public function additionner(int $a, int $b): int { return $a + $b; }

    public function diviser(float $a, float $b): float
    {
        if ($b === 0.0) { throw new \InvalidArgumentException('Division par zéro'); }
        return $a / $b;
    }
}
```

Test :

```php
<?php
// tests/CalculatriceTest.php
namespace Tests;

use App\Calculatrice;
use PHPUnit\Framework\Attributes\DataProvider;
use PHPUnit\Framework\TestCase;

final class CalculatriceTest extends TestCase
{
    public function testAdditionner(): void
    {
        $this->assertSame(5, (new Calculatrice())->additionner(2, 3));
    }

    public function testDivisionParZero(): void
    {
        $this->expectException(\InvalidArgumentException::class);
        (new Calculatrice())->diviser(1, 0);
    }

    #[DataProvider('cas')]
    public function testAdditionnerAvecJeuxDeDonnees(int $a, int $b, int $attendu): void
    {
        $this->assertSame($attendu, (new Calculatrice())->additionner($a, $b));
    }

    public static function cas(): array
    {
        return [[1, 1, 2], [0, 0, 0], [-1, 1, 0]];
    }
}
```

```bash
vendor/bin/phpunit
vendor/bin/phpunit --filter testAdditionner
vendor/bin/phpunit --coverage-text      # nécessite Xdebug ou PCOV
```

Les méthodes de test commencent par `test` (ou portent l'attribut `#[Test]`). Dans les versions récentes de PHPUnit, les **attributs** (`#[Test]`, `#[DataProvider]`) remplacent les annotations de commentaires (`@dataProvider`), dépréciées puis supprimées.

**Assertions courantes :** `assertSame` (strict `===`, à préférer), `assertEquals` (souple), `assertTrue`, `assertFalse`, `assertNull`, `assertCount`, `assertContains`, `assertInstanceOf`, `assertStringContainsString`, `expectException`. Cycle de vie : `setUp()` avant chaque test, `tearDown()` après.

### 19.3 Doublures de test (*mocks*)

Pour **isoler** la classe testée de ses dépendances (réseau, base, e-mail), on les remplace par des **doublures**. Cela suppose un code qui dépend d'**interfaces** et reçoit ses dépendances par **injection**.

```php
<?php
namespace App;

interface MailerInterface { public function envoyer(string $destinataire): bool; }

final class InscriptionService
{
    public function __construct(private MailerInterface $mailer) {}
    public function inscrire(string $email): bool { return $this->mailer->envoyer($email); }
}

// tests/InscriptionServiceTest.php
namespace Tests;

use App\InscriptionService;
use App\MailerInterface;
use PHPUnit\Framework\TestCase;

final class InscriptionServiceTest extends TestCase
{
    public function testEnvoiEmailInscription(): void
    {
        $mailer = $this->createMock(MailerInterface::class);
        $mailer->expects($this->once())
               ->method('envoyer')
               ->with('alice@exemple.com')
               ->willReturn(true);

        $service = new InscriptionService($mailer);
        $this->assertTrue($service->inscrire('alice@exemple.com'));
    }
}
```

| Type | Rôle |
| --- | --- |
| **Dummy** | Objet de remplissage jamais utilisé |
| **Stub** | Renvoie des valeurs prédéfinies |
| **Mock** | Vérifie les **appels** reçus (nombre, arguments) |
| **Spy** | Enregistre les appels pour vérification a posteriori |
| **Fake** | Implémentation simplifiée fonctionnelle (base en mémoire) |

Outils : **Mockery**, **Prophecy**. Ne sur-spécifiez pas : un test lié aux détails internes se casse à chaque refactorisation.

### 19.4 TDD (*Test-Driven Development*)

1. **Rouge** : écrire un test qui échoue (il exprime le comportement voulu).
2. **Vert** : écrire le code **minimal** qui le fait passer.
3. **Refactoriser** : améliorer le code, tests toujours verts.

Avantages : conception pilotée par l'usage, couverture naturelle, confiance.

### 19.5 Autres outils de qualité

| Besoin | Outils |
| --- | --- |
| Tests expressifs | **Pest** (au-dessus de PHPUnit) |
| **Analyse statique** | **PHPStan**, **Psalm** (détectent des bugs sans exécuter le code, niveaux de rigueur croissants) |
| Style de code | **PHP-CS-Fixer**, **Laravel Pint**, PHP\_CodeSniffer (PSR-12) |
| Modernisation automatique | **Rector** |
| Tests de bout en bout | Playwright, Laravel Dusk, Codeception |
| Tests d'API | Pest / PHPUnit + client HTTP, Postman, Bruno |
| Tests de mutation | **Infection** (vérifie que les tests détectent réellement des changements du code) |
| Couverture | Xdebug, PCOV |
| Intégration continue | GitHub Actions, GitLab CI |

```yaml
# .github/workflows/tests.yml
name: Tests
on: [push, pull_request]
jobs:
  phpunit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: shivammathur/setup-php@v2
        with:
          php-version: '8.4'
      - run: composer install --prefer-dist --no-progress
      - run: vendor/bin/phpunit
```

### 19.6 Bonnes pratiques

- Un test = **un comportement**, au nom explicite, **indépendant** des autres (aucun ordre imposé).
- Schéma **Arrange – Act – Assert** (préparer, agir, vérifier).
- Tester les **cas limites** (vide, zéro, négatif, très grand) et les **erreurs**.
- Pas de vraie base de données, de réseau ni d'horloge réelle dans les tests unitaires (injectez une horloge, PSR-20).
- Lancer les tests **automatiquement** (CI) à chaque modification.
- Une couverture élevée n'est pas un objectif en soi : visez les **comportements critiques**.

### À retenir

- Beaucoup de tests unitaires rapides, peu de tests de bout en bout.
- `assertSame`, fournisseurs de données, `expectException`, doublures pour isoler.
- TDD : rouge → vert → refactoriser ; PHPStan, Pint/CS-Fixer et CI complètent la chaîne qualité.

---

## 20. Créer des API avec PHP

### Objectifs

- Comprendre les principes REST et concevoir des URL, verbes et codes de statut cohérents.
- Manipuler JSON en entrée et en sortie.
- Construire une API en PHP pur puis avec un framework.
- Sécuriser, documenter et tester une API.

### 20.1 Qu'est-ce qu'une API ?

Une **API** (*Application Programming Interface*) est une interface par laquelle des programmes dialoguent. Une **API web** expose des **ressources** via HTTP ; l'échange se fait le plus souvent en **JSON**. Elle sert aux applications mobiles, aux front-ends JavaScript (React, Vue…), aux partenaires et aux services entre eux. **REST** (*Representational State Transfer*) est un style d'architecture, non un protocole.

| Principe | Application |
| --- | --- |
| **Ressources** identifiées par des URL | `/api/utilisateurs/42` (noms **au pluriel**, pas de verbes dans l'URL) |
| **Verbes HTTP** pour les actions | `GET`, `POST`, `PUT`, `PATCH`, `DELETE` |
| **Sans état** | Chaque requête contient tout le nécessaire (jeton d'authentification) |
| **Codes de statut** significatifs | `200`, `201`, `204`, `400`, `401`, `403`, `404`, `409`, `422`, `429`, `500` |
| **Format** | JSON, avec `Content-Type: application/json` |
| **Cacheable, interface uniforme** | `ETag`, `Cache-Control` ; mêmes conventions partout |

| Action | Méthode + URL | Succès |
| --- | --- | --- |
| Lister | `GET /api/utilisateurs` | `200` |
| Lire | `GET /api/utilisateurs/42` | `200` |
| Créer | `POST /api/utilisateurs` | `201` + en-tête `Location` |
| Remplacer | `PUT /api/utilisateurs/42` | `200` / `204` |
| Modifier partiellement | `PATCH /api/utilisateurs/42` | `200` |
| Supprimer | `DELETE /api/utilisateurs/42` | `204` |

**Propriétés des méthodes :** `GET` est **sûr** (ne modifie rien) et **idempotent** ; `PUT` et `DELETE` sont idempotents (répéter l'appel produit le même état) ; `POST` ne l'est pas. Sous-ressources : `/api/utilisateurs/42/commandes`.

### 20.2 JSON en PHP

```php
<?php
// Encoder
echo json_encode(['id' => 1, 'nom' => 'Alice'], JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR) . PHP_EOL;

// Décoder (true : tableau associatif, sinon objets stdClass)
$texte = '{"id":1,"nom":"Alice"}';
$data = json_decode($texte, true, 512, JSON_THROW_ON_ERROR);
echo $data['nom'] . PHP_EOL;                                         // → Alice

// Corps d'une requête JSON : php://input (vide en ligne de commande)
$brut = file_get_contents('php://input');
try {
    $donnees = json_decode($brut, true, 512, JSON_THROW_ON_ERROR);
} catch (JsonException $e) {
    fwrite(STDERR, 'Erreur JSON : ' . $e->getMessage() . PHP_EOL);
}

// Sérialiser un objet : JsonSerializable
class Produit implements JsonSerializable
{
    public function __construct(private int $id, private string $nom) {}
    public function jsonSerialize(): array { return ['id' => $this->id, 'nom' => $this->nom]; }
}
echo json_encode(new Produit(7, 'Stylo')) . PHP_EOL;                // → {"id":7,"nom":"Stylo"}

var_dump(json_validate($texte));                                    // 8.3 : valide sans décoder → true
var_dump(json_validate('{invalide'));                               // → false
```

**Points d'attention :** `$_POST` est **vide** pour un corps JSON (lisez `php://input`) ; `json_encode` renvoie `false` en cas d'échec (ex. UTF-8 invalide) : utilisez `JSON_THROW_ON_ERROR` ; un tableau vide `[]` est encodé `[]` et non `{}` (utilisez `new stdClass()` pour un objet vide) ; les grands entiers et flottants peuvent perdre en précision côté JavaScript (transmettez-les en chaîne) ; le format de date recommandé est **ISO 8601** (`2026-10-11T14:30:00Z`).

### 20.3 Un mini-routeur d'API en PHP pur

```php
<?php
// api.php : « php -S localhost:8000 api.php » (le script sert de routeur)
declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');

$pdo = new PDO('sqlite:' . __DIR__ . '/api.sqlite', null, null, [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
]);
$pdo->exec('CREATE TABLE IF NOT EXISTS utilisateurs (id INTEGER PRIMARY KEY, nom TEXT NOT NULL)');

function reponse(mixed $data, int $statut = 200): never
{
    http_response_code($statut);
    echo json_encode($data, JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR);
    exit;
}

$methode = $_SERVER['REQUEST_METHOD'];
$chemin  = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

try {
    $corps = in_array($methode, ['POST', 'PUT', 'PATCH'], true)
        ? json_decode(file_get_contents('php://input'), true, 512, JSON_THROW_ON_ERROR)
        : null;

    if ($chemin === '/api/utilisateurs' && $methode === 'GET') {
        reponse($pdo->query('SELECT id, nom FROM utilisateurs')->fetchAll());
    }

    if ($chemin === '/api/utilisateurs' && $methode === 'POST') {
        $nom = trim((string) ($corps['nom'] ?? ''));
        if ($nom === '') { reponse(['erreur' => 'Le nom est obligatoire.'], 422); }
        $pdo->prepare('INSERT INTO utilisateurs (nom) VALUES (?)')->execute([$nom]);
        reponse(['id' => (int) $pdo->lastInsertId(), 'nom' => $nom], 201);
    }

    if (preg_match('#^/api/utilisateurs/(\d+)$#', $chemin, $m) && $methode === 'GET') {
        $stmt = $pdo->prepare('SELECT id, nom FROM utilisateurs WHERE id = ?');
        $stmt->execute([(int) $m[1]]);
        $u = $stmt->fetch();
        $u ? reponse($u) : reponse(['erreur' => 'Introuvable'], 404);
    }

    reponse(['erreur' => 'Route inconnue'], 404);
} catch (JsonException) {
    reponse(['erreur' => 'JSON invalide'], 400);
} catch (Throwable $e) {
    error_log((string) $e);
    reponse(['erreur' => 'Erreur interne'], 500);
}
```

Ce code illustre l'ossature de toute API : **routage** (méthode + chemin), **lecture** et **validation** du corps, **accès aux données**, **réponse JSON** avec code adapté, **gestion centralisée des erreurs**. Au-delà de quelques routes, utilisez un framework.

### 20.4 API avec un framework

**Laravel :**

```php
<?php
// routes/api.php
use App\Http\Controllers\ArticleController;
use Illuminate\Support\Facades\Route;

Route::apiResource('articles', ArticleController::class)->middleware('auth:sanctum');
```

```php
<?php
// app/Http/Controllers/ArticleController.php (extrait)
namespace App\Http\Controllers;

use App\Http\Requests\StoreArticleRequest;
use App\Http\Resources\ArticleResource;
use App\Models\Article;
use Illuminate\Http\JsonResponse;

class ArticleController extends Controller
{
    public function store(StoreArticleRequest $request): JsonResponse       // validation par FormRequest
    {
        $article = Article::create($request->validated());
        return (new ArticleResource($article))->response()->setStatusCode(201);
    }
}
```

`apiResource` génère les cinq routes REST ; le **FormRequest** valide automatiquement (réponse `422` si échec) ; la **Resource** décide quels champs exposer.

**Slim :**

```php
<?php
use Slim\Factory\AppFactory;

require __DIR__ . '/vendor/autoload.php';

$pdo = new PDO('sqlite::memory:', null, null, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
$pdo->exec('CREATE TABLE articles (id INTEGER PRIMARY KEY, titre TEXT)');
$pdo->exec("INSERT INTO articles (titre) VALUES ('Premier article')");

$app = AppFactory::create();
$app->get('/api/articles', function ($req, $res) use ($pdo) {
    $res->getBody()->write(json_encode($pdo->query('SELECT * FROM articles')->fetchAll(PDO::FETCH_ASSOC)));
    return $res->withHeader('Content-Type', 'application/json');
});
$app->run();
```

**Symfony / API Platform :** décrivez vos entités avec l'attribut `#[ApiResource]` : l'API REST (ou GraphQL), la **documentation OpenAPI**, la pagination et les filtres sont générés.

### 20.5 Authentification et sécurité d'une API

| Mécanisme | Usage |
| --- | --- |
| **Jeton d'API / Bearer** | Services internes, applications simples (`Authorization: Bearer <jeton>`) |
| **JWT** (*JSON Web Token*) | Jeton signé contenant des revendications ; courte durée + jeton de rafraîchissement ; la révocation est difficile |
| **OAuth 2.0 / OpenID Connect** | Délégation d'accès (« se connecter avec… »), accès tiers limité par *scopes* |
| **Sessions + cookies** | Applications web classiques (avec protection CSRF) |

**Authentification** = qui êtes-vous ? **Autorisation** = avez-vous le droit de faire cela, sur **cette** ressource ? Les deux sont à vérifier **à chaque requête**.

À mettre en place :

- **HTTPS** obligatoire.
- **Validation stricte** des entrées (type, longueur, format) et réponse **`422`** détaillée.
- **Limitation du débit** (*rate limiting*, réponse `429` avec `Retry-After`).
- **CORS** (*Cross-Origin Resource Sharing*) configuré précisément : origines autorisées explicitement, jamais `*` avec des identifiants.
- **Pagination** (`?page=2&per_page=20`) et **filtres/tri** ; ne pas exposer de données internes (champs privés, identifiants séquentiels sensibles : préférez des **UUID**).
- **Versionnement** (`/api/v1/…` ou en-tête) et **documentation OpenAPI / Swagger**.
- **Idempotence** des créations via un en-tête `Idempotency-Key` pour éviter les doublons lors de nouvelles tentatives.
- **Réponses d'erreur cohérentes** au format **RFC 9457** (*Problem Details* : `type`, `title`, `status`, `detail`).

```php
<?php
// cors.php
header('Access-Control-Allow-Origin: https://mon-front.exemple');
header('Access-Control-Allow-Methods: GET, POST, PUT, PATCH, DELETE, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, Authorization');
if (($_SERVER['REQUEST_METHOD'] ?? '') === 'OPTIONS') { http_response_code(204); exit; }   // requête de pré-vérification (preflight)

header('Content-Type: application/json; charset=utf-8');
echo json_encode(['message' => 'Réponse normale']);
```

Le navigateur applique la **politique de même origine** ; CORS est l'autorisation explicite par le **serveur** d'appels venus d'une autre origine. Ce n'est **pas** une protection côté serveur (un client non navigateur l'ignore).

### 20.6 Tester une API

```bash
curl -X POST http://localhost:8000/api/utilisateurs \
     -H "Content-Type: application/json" \
     -d '{"nom":"Alice"}'
```

Outils : **Postman**, **Bruno**, **Insomnia**, extension **REST Client** de VS Code ; tests automatisés avec PHPUnit/Pest et le client HTTP du framework (`$this->postJson('/api/articles', [...])->assertCreated()`). Testez les **cas d'erreur** (401, 403, 404, 422) autant que les succès.

### À retenir

- Ressources au pluriel, verbes HTTP, codes de statut précis, JSON cohérent.
- Valider, authentifier **et** autoriser à chaque requête ; limiter le débit ; configurer CORS.
- `JSON_THROW_ON_ERROR`, pagination, versionnement et documentation OpenAPI.

---

## 21. Sujets avancés

### Objectifs

- Écrire des scripts en ligne de commande.
- Mesurer et améliorer les performances (OPcache, serveurs persistants, requêtes, cache).
- Utiliser Redis, comprendre temps réel, asynchrone et fibers.
- Connaître les chantiers complémentaires d'un projet réel.

### 21.1 Scripts en ligne de commande (CLI)

PHP sert aussi à écrire des **outils en terminal** : migrations, imports, tâches planifiées, traitements de fond. En CLI, il n'y a ni navigateur, ni `$_GET`/`$_POST`, ni session ; on dispose de `$argv`/`$argc`, de `STDIN`, `STDOUT`, `STDERR` et d'un **code de sortie**.

```php
#!/usr/bin/env php
<?php
declare(strict_types=1);

if (PHP_SAPI !== 'cli') { exit("Ce script s'exécute en ligne de commande.\n"); }

$options = getopt('n:v', ['nom:', 'verbeux']);               // php script.php -n Alice --verbeux
echo 'Options : ' . json_encode($options) . PHP_EOL;
echo 'Arguments : ' . implode(', ', array_slice($argv, 1)) . PHP_EOL;

$saisie = trim((string) fgets(STDIN));                        // lecture au clavier
echo 'Saisie : ' . $saisie . PHP_EOL;
fwrite(STDERR, "Message d'erreur\n");                         // sortie d'erreur (séparée de la sortie normale)
exit(0);                                                      // 0 = succès, autre valeur = échec
```

```bash
php script.php -n Alice --verbeux
chmod +x script.php && ./script.php
```

Pour des commandes riches : **Symfony Console** (arguments, options, tableaux, barres de progression), **Laravel Artisan**, **Laravel Prompts**. **Planification :** `cron` (`* * * * * php /chemin/script.php`) ; veillez à éviter les exécutions qui se chevauchent (verrou de fichier ou de base). Utilisez des codes de sortie cohérents pour que l'orchestrateur détecte les échecs.

### 21.2 Performance

> **Règle d'or :** **mesurez avant d'optimiser**. Le goulot d'étranglement est presque toujours la **base de données** ou les **appels externes**, rarement le PHP lui-même.

| Levier | Détails |
| --- | --- |
| **OPcache** | Garde le bytecode compilé en mémoire : **à activer en production** (`opcache.enable=1`, `opcache.validate_timestamps=0` avec redéploiement) |
| **JIT** | Compilation à la volée : utile pour du calcul intensif, peu d'effet sur une application web classique |
| **Preloading** | Précharge des classes au démarrage (`opcache.preload`) |
| **Serveurs d'application persistants** | **FrankenPHP**, **RoadRunner**, **Swoole / OpenSwoole** : l'application reste en mémoire entre requêtes (Laravel Octane) ; attention aux états partagés à ne pas faire fuiter |
| **Requêtes SQL** | Index adaptés, éviter le **problème N+1**, pagination, sélection des colonnes utiles, mise en cache |
| **Autoload optimisé** | `composer install --optimize-autoloader --classmap-authoritative` |
| **Mémoire** | Générateurs, traitement par lots (`chunk`), éviter de charger de gros tableaux |
| **Mesure / profilage** | **Xdebug** (profilage), **Blackfire**, **Tideways**, `microtime(true)`, `hrtime()`, `memory_get_peak_usage()` |

```php
<?php
$debut = microtime(true);

$total = 0;
for ($i = 0; $i < 1_000_000; $i++) { $total += $i; }       // code à mesurer
$tableau = range(1, 100_000);

printf("%.3f s, %.1f Mo\n", microtime(true) - $debut, memory_get_peak_usage(true) / 1048576);
```

Autres leviers : compression (gzip/Brotli) et en-têtes de cache HTTP, **CDN** pour les fichiers statiques, files d'attente pour les tâches lentes (e-mails, traitements d'images), HTTP/2 ou HTTP/3, base de données bien dimensionnée.

### 21.3 Stratégies de cache

Un **cache** mémorise le résultat d'un calcul coûteux pour le resservir rapidement. Il introduit toujours un compromis : fraîcheur contre vitesse.

| Niveau | Technique |
| --- | --- |
| **Code** | OPcache |
| **Données en mémoire locale** | **APCu** (cache par serveur) |
| **Cache distribué** | **Redis**, **Memcached** |
| **Fichiers** | Cache sur disque (pages générées, résultats lourds) |
| **HTTP** | En-têtes `Cache-Control`, `ETag`, `Last-Modified` ; **CDN** (Cloudflare, Fastly) |
| **Applicatif (framework)** | Laravel `Cache::remember()`, **PSR-6 / PSR-16** (`symfony/cache`) |

```php
<?php
function lireAvecCache(string $cle, int $ttl, callable $calcul): mixed
{
    static $local = [];                                   // repli : cache en mémoire du script

    if (function_exists('apcu_fetch') && apcu_enabled()) {
        $valeur = apcu_fetch($cle, $trouve);
        if ($trouve) { return $valeur; }
        $valeur = $calcul();
        apcu_store($cle, $valeur, $ttl);
        return $valeur;
    }

    if (isset($local[$cle]) && $local[$cle][1] > time()) { return $local[$cle][0]; }
    $valeur = $calcul();
    $local[$cle] = [$valeur, time() + $ttl];
    return $valeur;
}

$calcul = function () { echo '(calcul lourd exécuté)' . PHP_EOL; return 42; };
echo lireAvecCache('reponse', 60, $calcul) . PHP_EOL;     // calcul exécuté, puis 42
echo lireAvecCache('reponse', 60, $calcul) . PHP_EOL;     // 42, servi depuis le cache
```

- Définissez toujours une **durée de vie** (TTL) et une stratégie d'**invalidation** (la plus difficile : par expiration, par événement, par clé versionnée).
- Protégez-vous de l'**effet de ruée** (*cache stampede*) : plusieurs requêtes recalculent en même temps une valeur expirée → verrous, TTL avec variation aléatoire, rafraîchissement anticipé.
- Ne mettez pas en cache de données propres à un utilisateur dans un cache partagé sans clé qui l'identifie.

### 21.4 Redis et Memcached

**Redis** est un serveur de structures de données en mémoire (clé/valeur, listes, ensembles, hachages, flux), avec persistance optionnelle ; **Memcached** est plus simple (clé/valeur seulement, sans persistance).

```bash
composer require predis/predis       # bibliothèque en PHP pur ; l'extension native phpredis est plus rapide
```

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$utilisateur = ['id' => 42, 'nom' => 'Alice'];

try {
    $redis = new Predis\Client(['scheme' => 'tcp', 'host' => '127.0.0.1', 'port' => 6379]);

    $redis->setex('utilisateur:42', 3600, json_encode($utilisateur));          // avec expiration (1 h)
    $lu = json_decode($redis->get('utilisateur:42') ?? 'null', true);
    echo $lu['nom'] . PHP_EOL;                                                  // → Alice
    echo $redis->incr('visites') . PHP_EOL;                                     // compteur ATOMIQUE
    $redis->del('utilisateur:42');
} catch (Predis\Connection\ConnectionException $e) {
    fwrite(STDERR, 'Redis inaccessible : ' . $e->getMessage() . PHP_EOL);
}
```

| Usage de Redis | Détails |
| --- | --- |
| **Cache** | Clé/valeur avec TTL |
| **Sessions** | `session.save_handler = redis` : partage entre plusieurs serveurs |
| **Files d'attente** | Laravel Queues, Symfony Messenger |
| **Limitation de débit** | Compteurs avec expiration |
| **Verrous distribués** | Éviter qu'une tâche s'exécute deux fois |
| **Pub/Sub** | Messages en temps réel |

Une clé se nomme par convention `domaine:identifiant:champ`. Les valeurs sont des chaînes : sérialisez en JSON.

### 21.5 WebSockets et temps réel

PHP traite une requête puis s'arrête : pour des **connexions persistantes** (chat, notifications, tableaux de bord en direct) il faut un **processus long** à l'écoute.

| Solution | Description |
| --- | --- |
| **Ratchet** (ReactPHP) | Serveur WebSocket en PHP |
| **Swoole / OpenSwoole**, **Workerman** | Serveurs asynchrones hautes performances |
| **Laravel Reverb**, **Soketi**, **Pusher** | Diffusion d'événements intégrée à Laravel |
| **Mercure** (Symfony) | *Push* via **SSE** (*Server-Sent Events*) |

```php
<?php
// chat-serveur.php : après « composer require cboden/ratchet »
require __DIR__ . '/vendor/autoload.php';

use Ratchet\ConnectionInterface;
use Ratchet\Http\HttpServer;
use Ratchet\MessageComponentInterface;
use Ratchet\Server\IoServer;
use Ratchet\WebSocket\WsServer;

class Chat implements MessageComponentInterface
{
    protected \SplObjectStorage $clients;

    public function __construct() { $this->clients = new \SplObjectStorage(); }
    public function onOpen(ConnectionInterface $c): void { $this->clients->attach($c); }

    public function onMessage(ConnectionInterface $de, $msg): void
    {
        foreach ($this->clients as $client) {
            if ($client !== $de) { $client->send($msg); }          // diffusion aux autres
        }
    }

    public function onClose(ConnectionInterface $c): void { $this->clients->detach($c); }
    public function onError(ConnectionInterface $c, \Exception $e): void { $c->close(); }
}

echo 'Serveur WebSocket sur le port 8080' . PHP_EOL;
IoServer::factory(new HttpServer(new WsServer(new Chat())), 8080)->run();
```

Dans la majorité des cas, les **SSE** (flux unidirectionnel serveur → client, simple) ou l'**interrogation périodique** (*polling*) suffisent. Un processus long exige une supervision (**Supervisor**, systemd), la surveillance de la mémoire et des redémarrages contrôlés.

### 21.6 Programmation asynchrone et *fibers* (8.1)

Par défaut, PHP est **synchrone** : chaque appel attend sa fin. Les **Fibers** permettent de **suspendre** puis **reprendre** l'exécution d'une portion de code ; elles servent de socle à des bibliothèques asynchrones (**Revolt**, **AMPHP**, **ReactPHP**) qui exécutent plusieurs entrées/sorties en parallèle (appels HTTP, requêtes) dans un seul processus.

```php
<?php
$fibre = new Fiber(function (): void {
    $valeur = Fiber::suspend('pause');          // suspend la fibre et renvoie 'pause' à l'appelant
    echo 'Reprise avec ' . $valeur . PHP_EOL;
});
echo $fibre->start() . PHP_EOL;                 // → pause
$fibre->resume('hello');                        // → Reprise avec hello
```

Pour le **parallélisme** (plusieurs cœurs), on utilise plusieurs **processus** (`proc_open`, workers de file d'attente, `pcntl_fork`) ; PHP n'a pas de fils d'exécution partageant la mémoire dans une installation standard.

### 21.7 Autres chantiers utiles

- **Files d'attente et tâches de fond** (Laravel Queues, Symfony Messenger, RabbitMQ, Amazon SQS).
- **Internationalisation** (i18n) : extension `intl`, `gettext`, fichiers de traduction des frameworks, formats de dates et nombres localisés.
- **Manipulation d'images** : GD, Imagick, Intervention Image.
- **PDF / Excel** : Dompdf, TCPDF, PhpSpreadsheet.
- **Recherche** : Elasticsearch/OpenSearch, Meilisearch, `FULLTEXT` MySQL.
- **Observabilité** : journaux structurés (Monolog), métriques, traçage (OpenTelemetry), alertes.
- **Déploiement** : Docker, Nginx + PHP-FPM, FrankenPHP, plateformes (Forge, Fly.io, PaaS) ; intégration et déploiement continus, déploiements sans interruption.
- **`php.ini`** : `memory_limit`, `max_execution_time`, `upload_max_filesize`, `date.timezone`, `opcache.*`.

### À retenir

- CLI : `$argv`, `getopt`, `STDERR`, codes de sortie ; Symfony Console pour du sérieux.
- Mesurer → optimiser : OPcache, bonnes requêtes SQL, cache avec TTL et invalidation.
- Redis pour cache, sessions, files et verrous ; processus longs pour le temps réel.

---

## 22. Nouveautés par version et aide-mémoire

### 22.1 Chronologie des fonctionnalités

Cette table sert de repère pour savoir **à partir de quelle version** une fonctionnalité existe — et donc quelle version minimale de PHP exiger.

| Version | Fonctionnalités marquantes |
| --- | --- |
| **7.0** | Déclarations de types scalaires, opérateurs `<=>` et `??`, classes anonymes, performances ×2 |
| **7.4** | Fonctions fléchées, propriétés typées, `??=`, opérateur de décomposition dans les tableaux |
| **8.0** | **Arguments nommés**, **attributs**, **promotion de propriétés**, **types union**, **`match`**, **opérateur null-safe `?->`**, `str_contains`, JIT, `mixed`, `throw` en expression |
| **8.1** | **Énumérations**, propriétés **`readonly`**, **Fibers**, callables de première classe `f(...)`, types intersection, `never`, `new` dans les initialisateurs, `array_is_list` |
| **8.2** | Classes **`readonly`**, types DNF, types `null` / `false` / `true` autonomes, `#[\SensitiveParameter]`, extension Random ; dépréciation des propriétés dynamiques |
| **8.3** | **Constantes de classe typées**, `#[\Override]`, `json_validate()`, accès dynamique aux constantes de classe `Classe::{$nom}` |
| **8.4** | **Hooks de propriétés**, **visibilité asymétrique** (`private(set)`), `new Classe()->méthode()` sans parenthèses englobantes, `#[\Deprecated]`, `array_find/any/all`, objets paresseux, nouvelle API DOM HTML5, `mb_trim` |
| **8.5** | \*\*Opérateur pipe \` |
| **8.6** | En test (bêta) à la date de rédaction : consultez les notes de version officielles |

Pour les détails exacts de chaque version : **php.net → Migration guides** (php.net/manual/fr/appendices.php). Lors d'une montée de version, lisez les **incompatibilités** et **dépréciations**, activez `E_ALL` et `E_DEPRECATED` en développement, lancez la suite de tests et utilisez **Rector** pour automatiser une partie de la migration.

### 22.2 Fonctions et pratiques dépréciées ou supprimées

| À ne plus utiliser | Remplacement |
| --- | --- |
| `mysql_*` (supprimées en 7.0) | **PDO** / MySQLi |
| `FILTER_SANITIZE_STRING` (déprécié en 8.1) | `htmlspecialchars()` + validation |
| `md5()`, `sha1()` pour les mots de passe | `password_hash()` |
| `rand()`, `mt_rand()`, `uniqid()` en sécurité | `random_int()`, `random_bytes()` |
| `create_function()`, `each()` (supprimées) | Fonctions anonymes, `foreach` |
| `register_globals`, `magic_quotes` (supprimés) | Accès explicite à `$_GET`/`$_POST` |
| `eval()` | À proscrire |
| `@` (suppression d'erreurs) | Gestion explicite des erreurs |
| `$_REQUEST` | `$_GET` / `$_POST` explicites |
| `unserialize()` sur des entrées externes | `json_decode()` |
| Propriétés dynamiques (dépréciées en 8.2) | Déclarer les propriétés / `#[\AllowDynamicProperties]` |
| Paramètre implicitement nullable `Type $x = null` (déprécié en 8.4) | `?Type $x = null` |

### 22.3 Récapitulatif par besoin

| Besoin | Outil |
| --- | --- |
| Accès à la base | **PDO** + requêtes préparées |
| Mots de passe | `password_hash` / `password_verify` |
| Jetons aléatoires | `random_bytes` / `random_int` |
| Affichage sûr | `htmlspecialchars` |
| Validation | `filter_var`, `filter_input` |
| Dates | `DateTimeImmutable` |
| JSON | `json_encode` / `json_decode` + `JSON_THROW_ON_ERROR` |
| Dépendances | **Composer** |
| Tests | **PHPUnit** / **Pest** |
| Qualité | **PHPStan**, Pint / PHP-CS-Fixer |
| Journaux | **Monolog** |
| Appels HTTP sortants | Guzzle / Symfony HttpClient |
| E-mail | PHPMailer / Symfony Mailer |

### 22.4 Aide-mémoire des réflexes à acquérir

1. `declare(strict_types=1);` dans chaque fichier ; typez tout.
2. `===` plutôt que `==` ; `match` plutôt que `switch`.
3. **Valider à l'entrée, échapper à la sortie** ; ne jamais faire confiance au client.
4. Requêtes **préparées** ; mots de passe avec `password_hash`.
5. Exceptions plutôt que codes d'erreur ; **jamais d'erreurs affichées** en production.
6. Composer, PSR-4, injection de dépendances, objets immuables.
7. Tests automatisés + analyse statique + intégration continue.
8. Mesurer avant d'optimiser ; mettre à jour PHP et les dépendances.

### 22.5 Ressources pour poursuivre

- **Manuel officiel** : php.net/manual/fr/
- **PHP : la bonne méthode** (*PHP The Right Way*) : phptherightway.com
- **PHP-FIG (normes PSR)** : php-fig.org
- **OWASP PHP Cheat Sheets** : cheatsheetseries.owasp.org
- **Packagist** : packagist.org
- **3v4l.org** : exécuter un code sur toutes les versions de PHP
- Documentation officielle de Laravel (laravel.com/docs) et de Symfony (symfony.com/doc)

### Pour conclure : parcours conseillé

1. **Fondations** (sections 1 à 8) : langage, types, fonctions, tableaux, chaînes, dates.
2. **Web dynamique** (9 à 13) : formulaires, fichiers, sessions, base de données, erreurs.
3. **Conception** (14, 17) : objet, Composer, espaces de noms.
4. **Production** (15, 16, 19) : web, sécurité, tests.
5. **Écosystème** (18, 20, 21) : frameworks, API, performance.

*Bon développement !*
