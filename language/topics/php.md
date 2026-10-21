<div align="center">

# 🐘 PHP — Guide complet

**Des bases du langage aux API, à la sécurité et aux frameworks modernes**

*Mis à jour pour PHP 8.5 (octobre 2026)*

</div>

---

## 🗂️ Sommaire

1. [Introduction et installation](#1-introduction-et-installation)
2. [Syntaxe et bases](#2-syntaxe-et-bases)
3. [Opérateurs](#3-opérateurs)
4. [Structures de contrôle](#4-structures-de-contrôle)
5. [Fonctions](#5-fonctions)
6. [Tableaux](#6-tableaux)
7. [Chaînes de caractères](#7-chaînes-de-caractères)
8. [Dates, heures et expressions régulières](#8-dates-heures-et-expressions-régulières)
9. [Formulaires et saisies utilisateur](#9-formulaires-et-saisies-utilisateur)
10. [Système de fichiers](#10-système-de-fichiers)
11. [Sessions et cookies](#11-sessions-et-cookies)
12. [Bases de données avec PDO](#12-bases-de-données-avec-pdo)
13. [Gestion des erreurs et exceptions](#13-gestion-des-erreurs-et-exceptions)
14. [Programmation orientée objet](#14-programmation-orientée-objet)
15. [PHP et le web](#15-php-et-le-web)
16. [Sécurité](#16-sécurité)
17. [Composer et gestion des dépendances](#17-composer-et-gestion-des-dépendances)
18. [Frameworks PHP](#18-frameworks-php)
19. [Tests et qualité du code](#19-tests-et-qualité-du-code)
20. [Créer des API avec PHP](#20-créer-des-api-avec-php)
21. [Sujets avancés](#21-sujets-avancés)
22. [Nouveautés par version et aide-mémoire](#22-nouveautés-par-version-et-aide-mémoire)

> 💡 **Légende** : *(ajout)* = notion absente du guide d'origine ; *(à jour)* = pratique moderne remplaçant une ancienne ; *(8.x)* = version de PHP qui introduit la fonctionnalité.

---

# 1. Introduction et installation

## 1.1 Qu'est-ce que PHP ?

**PHP** (*PHP: Hypertext Preprocessor*) est un langage de script **côté serveur**, **open source**, conçu pour le **développement web**. Le code est exécuté sur le serveur, qui renvoie du **HTML** (ou du JSON, des images…) au navigateur : l'utilisateur ne voit jamais le code PHP.

| Caractéristique | Détail |
| --- | --- |
| Exécution | Côté serveur (aussi en ligne de commande) |
| Typage | Dynamique, avec **déclarations de types** facultatives (de plus en plus utilisées) |
| Paradigmes | Procédural, **orienté objet**, fonctionnel |
| Extension de fichier | `.php` |
| Écosystème | Laravel, Symfony, WordPress, Drupal, Composer / Packagist |

## 1.2 Brève histoire

| Année | Événement |
| --- | --- |
| 1994 | **Rasmus Lerdorf** crée les premiers outils CGI en C |
| 1995 | *Personal Home Page Tools* (PHP/FI) publié |
| 1998 | **PHP 3** : le nom devient *PHP: Hypertext Preprocessor* |
| 2000 | PHP 4 (moteur Zend) |
| 2004 | PHP 5 : vrai modèle objet |
| 2015 | **PHP 7** (la version 6 n'a jamais été publiée) : performances ×2 environ, types scalaires |
| 2020 | **PHP 8.0** : arguments nommés, `match`, attributs, JIT, types union |
| 2021–2024 | 8.1 (énumérations, `readonly`, *fibers*) · 8.2 · 8.3 · **8.4** (hooks de propriétés) |
| **2025** | **PHP 8.5** (novembre 2025) : opérateur pipe `\|>`, extension URI… |
| 2026 | **PHP 8.6** en phase de test (version finale attendue en fin d'année) |

### Versions supportées *(à jour)*

Chaque branche est supportée **2 ans** (correctifs) puis **2 ans** (sécurité uniquement).

| Branche | Sortie | Fin du support actif | Fin du support de sécurité |
| --- | --- | --- | --- |
| 8.2 | déc. 2022 | terminé | **31 déc. 2026** |
| 8.3 | nov. 2023 | terminé | 31 déc. 2027 |
| 8.4 | nov. 2024 | 31 déc. 2026 | 31 déc. 2028 |
| **8.5** | nov. 2025 | 31 déc. 2027 | 31 déc. 2029 |

> ⚠️ **PHP 8.1 et antérieures ne reçoivent plus aucun correctif de sécurité.** Pour un nouveau projet, utilisez **PHP 8.4 ou 8.5**. Consultez [php.net/supported-versions](https://www.php.net/supported-versions.php).

## 1.3 Ce que PHP sait faire

- Générer du **HTML dynamique** et traiter les **formulaires** (GET/POST)
- Gérer **sessions** et **cookies**
- Dialoguer avec des **bases de données** (MySQL/MariaDB, PostgreSQL, SQLite)
- Lire et écrire des **fichiers**, envoyer des **e-mails**
- Construire des **API REST**
- Écrire des scripts en **ligne de commande** (CLI)
- Faire tourner de grands frameworks (Laravel, Symfony…) et des CMS (WordPress…)

## 1.4 Comment PHP fonctionne

1. Le **navigateur** demande une page `.php`.
2. Le **serveur web** (Apache, Nginx + PHP-FPM, FrankenPHP…) transmet le fichier à l'interpréteur PHP.
3. PHP exécute le code et produit une **sortie** (HTML, JSON…).
4. Le serveur renvoie cette sortie au navigateur.

## 1.5 Installer PHP

### Option 1 : paquets système (recommandé)

```bash
# macOS (Homebrew)
brew install php

# Ubuntu / Debian
sudo apt update && sudo apt install php php-cli php-mysql php-mbstring php-xml php-curl

# Windows : télécharger sur https://windows.php.net, ou
winget install PHP.PHP
choco install php
```

### Option 2 : environnement tout-en-un

**XAMPP**, **Laragon** (Windows), **MAMP** (macOS) ou **Laravel Herd** installent PHP, un serveur web et MySQL.

### Option 3 : Docker

```bash
docker run --rm -it -v "$PWD":/app -w /app -p 8000:8000 php:8.5-cli php -S 0.0.0.0:8000
```

### Vérifier l'installation

```bash
php -v          # version
php -m          # extensions chargées
php --ini       # fichiers de configuration (php.ini)
```

## 1.6 Serveur de développement intégré

```bash
php -S localhost:8000                   # sert le dossier courant
php -S localhost:8000 -t public         # avec un dossier racine (public/)
```

Puis ouvrez <http://localhost:8000>. **Réservé au développement**, pas à la production.

## 1.7 Premier script

```php
<?php
echo "Bonjour le monde !";
```

```bash
php index.php        # exécution en terminal
```

### Mélanger PHP et HTML

```php
<!DOCTYPE html>
<html lang="fr">
<head><meta charset="UTF-8"><title>Ma première page PHP</title></head>
<body>
    <h1><?= htmlspecialchars($titre ?? "Bienvenue") ?></h1>
    <p>Nous sommes le <?= date("d/m/Y") ?></p>
</body>
</html>
```

---

# 2. Syntaxe et bases

## 2.1 Balises PHP

```php
<?php
// code PHP
?>
<p>HTML ici</p>
<?= $variable ?>      <!-- raccourci pour <?php echo $variable; ?> -->
```

> ✅ Dans un fichier contenant **uniquement du PHP**, **omettez la balise fermante `?>`** : cela évite l'envoi accidentel d'espaces ou de sauts de ligne avant les en-têtes HTTP.

## 2.2 Instructions et commentaires

Chaque instruction se termine par **`;`**. PHP est **insensible à la casse** pour les mots-clés et fonctions, mais **sensible à la casse pour les variables** (`$nom` ≠ `$Nom`).

```php
// Commentaire sur une ligne
# Autre commentaire sur une ligne
/* Commentaire
   sur plusieurs lignes */
/** Commentaire de documentation (PHPDoc) */
```

## 2.3 Typage strict *(ajout, à jour)*

Placez en **première ligne** de chaque fichier :

```php
<?php
declare(strict_types=1);
```

Avec le typage strict, `addition("5", 3)` lève une `TypeError` au lieu de convertir silencieusement.

## 2.4 Afficher : `echo` et `print`

```php
echo "Bonjour";
echo "A", "B", "C";          // plusieurs arguments possibles
print "Bonjour";             // renvoie toujours 1 (rarement utile)
print_r($tableau);           // affichage lisible
var_dump($valeur);           // type + valeur (débogage)
var_export($valeur);         // représentation PHP valide
```

`printf("%s a %d ans", $nom, $age)` et `sprintf()` formatent du texte.

## 2.5 Variables

Elles commencent par **`$`** ; aucune déclaration de type obligatoire.

```php
$nom = "Alice";
$age = 30;
$taille = 1.68;
$actif = true;
```

Règles : lettres, chiffres, `_`, sans commencer par un chiffre. Convention : **`$camelCase`** (ou `snake_case`, mais restez cohérent ; PSR-12 conseille camelCase).

```php
$a = 1;
$b = &$a;                    // référence : $b et $a désignent la même valeur
$nomVariable = "x";
$$nomVariable = 5;           // variable variable → $x (à éviter)
```

## 2.6 Types de données

| Type | Exemple |
| --- | --- |
| `int` | `42`, `0x1A`, `0b101`, `1_000_000` |
| `float` | `3.14`, `1.5e3` |
| `string` | `"texte"`, `'texte'` |
| `bool` | `true`, `false` |
| `array` | `[1, 2, 3]`, `["a" => 1]` |
| `object` | Instance de classe |
| `null` | `null` |
| `callable` / `iterable` | Fonctions / valeurs parcourables |
| `resource` | Ressource externe (fichier…) |

```php
gettype($x);               // "integer", "string"…
get_debug_type($x);        // "int", "string", nom de classe (8.0)
is_int($x); is_string($x); is_array($x); is_null($x); is_numeric("12.5");
isset($x);                 // défini et non null ?
empty($x);                 // vide ? ("", 0, "0", [], null, false)
```

### Valeurs « fausses » (*falsy*)

`false`, `0`, `0.0`, `""`, `"0"`, `[]`, `null`. Tout le reste est « vrai ».

## 2.7 Conversion de types (*casting*)

```php
$n = (int) "42abc";         // 42
$f = (float) "3.14";
$s = (string) 123;
$b = (bool) "0";            // false
$t = (array) "a";           // ["a"]
intval("12"); floatval("1.5"); strval(5); boolval(1);
```

## 2.8 Constantes

```php
define("TVA", 0.2);                  // à l'exécution
const NOM_SITE = "MonSite";          // à la compilation (préféré)

echo TVA, NOM_SITE;

class Config { const VERSION = "1.0"; }
echo Config::VERSION;
```

Constantes magiques : `__FILE__`, `__DIR__`, `__LINE__`, `__FUNCTION__`, `__CLASS__`, `__METHOD__`, `__NAMESPACE__`.

## 2.9 Interpolation de chaînes

```php
$nom = "Alice";
echo "Bonjour $nom !";                       // guillemets doubles : variables interprétées
echo "Âge : {$utilisateur['age']}";          // expressions complexes entre accolades
echo 'Bonjour $nom';                         // guillemets simples : texte brut
```

## 2.10 Portée et superglobales

Une variable définie hors fonction n'est **pas visible** dans les fonctions (voir [section 5](#5-fonctions)). Les **superglobales** sont accessibles partout :

| Superglobale | Contenu |
| --- | --- |
| `$_GET` | Paramètres de l'URL |
| `$_POST` | Données de formulaire (corps de la requête) |
| `$_REQUEST` | GET + POST + COOKIE (⚠️ à éviter) |
| `$_SERVER` | Informations sur le serveur et la requête |
| `$_FILES` | Fichiers téléversés |
| `$_COOKIE` | Cookies |
| `$_SESSION` | Données de session |
| `$_ENV` | Variables d'environnement |
| `$GLOBALS` | Toutes les variables globales |

## 2.11 Exemple complet

```php
<?php
declare(strict_types=1);

const TVA = 0.2;

$prixHT = 100.0;
$prixTTC = $prixHT * (1 + TVA);
echo "Prix TTC : " . number_format($prixTTC, 2, ',', ' ') . " €";   // 120,00 €
```

---

# 3. Opérateurs

## 3.1 Arithmétiques

| Opérateur | Rôle | Exemple |
| --- | --- | --- |
| `+` `-` `*` `/` | Opérations de base | `7 / 2` → `3.5` |
| `%` | Modulo (reste) | `7 % 3` → `1` |
| `**` | Puissance | `2 ** 3` → `8` |
| `intdiv(a, b)` | Division entière | `intdiv(7, 2)` → `3` |

> `/` ne renvoie un entier que si le résultat est exact ; une division par zéro lève une `DivisionByZeroError` (depuis PHP 8).

## 3.2 Affectation

```php
$x = 5;
$x += 2;  $x -= 1;  $x *= 3;  $x /= 2;  $x %= 4;  $x **= 2;
$s .= " fin";                // concaténation
$x ??= "défaut";             // affecte seulement si $x est null ou non défini (7.4)
```

## 3.3 Comparaison

| Opérateur | Signification |
| --- | --- |
| `==` | Égal (valeurs, **avec conversion**) |
| `===` | **Identique** (valeur ET type) ✅ |
| `!=` `<>` | Différent |
| `!==` | Non identique |
| `<` `>` `<=` `>=` | Ordre |
| `<=>` | **Vaisseau spatial** : `-1`, `0` ou `1` |

```php
0 == "a";        // false en PHP 8 (true avant !)
"1" == "01";     // true
"abc" == 0;      // false en PHP 8
null == false;   // true
0 === "0";       // false
1 <=> 2;         // -1
```

> ✅ Utilisez **`===`** par défaut. PHP 8 a rendu les comparaisons chaîne/nombre plus cohérentes, mais `==` reste source de surprises.

## 3.4 Logiques

| Opérateur | Rôle |
| --- | --- |
| `&&` ou `and` | ET |
| `\|\|` ou `or` | OU |
| `!` | NON |
| `xor` | OU exclusif |

> ⚠️ `and` / `or` ont une **priorité inférieure** à `=` : préférez `&&` et `||`.

## 3.5 Chaînes, incrément, tableaux

```php
$s = "Bonjour" . " " . "monde";      // concaténation .
$i++; ++$i; $i--; --$i;               // incrémentation

$a = [1, 2] + [3, 4, 5];              // union : [1, 2, 5] (les clés existantes de gauche gagnent)
[1, 2] == [1, 2];                     // true
[1, 2] === [2 => 1];                  // false (mêmes paires clé/valeur, même ordre ET types)
```

## 3.6 Opérateurs modernes *(à jour)*

```php
// Fusion null  ??
$nom = $_GET['nom'] ?? "Invité";

// Appel null-safe  ?->  (8.0)
$ville = $utilisateur?->adresse?->ville;

// Ternaire et ternaire court
$statut = $age >= 18 ? "majeur" : "mineur";
$valeur = $entree ?: "défaut";            // valeur si « vrai », sinon défaut

// match (8.0) : comparaison STRICTE, retourne une valeur
$libelle = match ($code) {
    200, 201 => "Succès",
    404      => "Introuvable",
    default  => "Erreur",
};

// Spread  ...
$tous = [...$a, ...$b];
function somme(int ...$nombres) { return array_sum($nombres); }

// Pipe  |>  (8.5) : enchaîne les appels de gauche à droite
$slug = "  Bonjour Le Monde  "
    |> trim(...)
    |> strtolower(...)
    |> (fn($s) => str_replace(" ", "-", $s));      // "bonjour-le-monde"
```

## 3.7 Priorité (extraits)

`**` → `++ --` → `!` → `* / %` → `+ -` → `.` (depuis PHP 8, `+`/`-` priment sur `.`) → `< <= > >=` → `== != === !==` → `&&` → `||` → `??` → `? :` → `=` → `and` → `xor` → `or`.

En cas de doute : **parenthèses**.

---

# 4. Structures de contrôle

## 4.1 Conditions

```php
if ($note >= 16) {
    echo "Très bien";
} elseif ($note >= 10) {
    echo "Passable";
} else {
    echo "Insuffisant";
}
```

### `switch` (comparaison souple)

```php
switch ($jour) {
    case "samedi":
    case "dimanche":
        echo "Week-end";
        break;
    default:
        echo "Semaine";
}
```

> ✅ Préférez **`match`** (comparaison stricte, pas de `break`, retourne une valeur, lève `UnhandledMatchError` si aucun cas).

### Syntaxe alternative (dans les gabarits HTML)

```php
<?php if ($connecte): ?>
    <p>Bienvenue !</p>
<?php else: ?>
    <p>Veuillez vous connecter.</p>
<?php endif; ?>

<?php foreach ($articles as $article): ?>
    <h2><?= htmlspecialchars($article['titre']) ?></h2>
<?php endforeach; ?>
```

## 4.2 Boucles

```php
for ($i = 0; $i < 5; $i++) { echo $i; }

$n = 0;
while ($n < 3) { $n++; }

do { $n--; } while ($n > 0);

foreach ([10, 20, 30] as $valeur) { echo $valeur; }
foreach (["a" => 1, "b" => 2] as $cle => $valeur) { echo "$cle=$valeur "; }

foreach ($tableau as &$element) { $element *= 2; }   // par référence
unset($element);                                       // ⚠️ toujours détruire la référence après la boucle
```

## 4.3 `break`, `continue`

```php
for ($i = 0; $i < 10; $i++) {
    if ($i === 3) continue;      // itération suivante
    if ($i === 7) break;         // sortie de la boucle
}

foreach ($lignes as $ligne) {
    foreach ($ligne as $cellule) {
        if ($cellule === null) continue 2;   // saute à l'itération de la boucle EXTÉRIEURE
    }
}
```

## 4.4 Générateurs *(ajout)*

`yield` produit des valeurs **à la demande**, sans charger toute la collection en mémoire :

```php
function lireLignes(string $chemin): Generator {
    $f = fopen($chemin, 'r');
    while (($ligne = fgets($f)) !== false) {
        yield rtrim($ligne);
    }
    fclose($f);
}

foreach (lireLignes('gros-fichier.txt') as $ligne) { /* traitement */ }
```

## 4.5 Inclusion de fichiers

```php
require __DIR__ . '/config.php';      // erreur fatale si absent
require_once __DIR__ . '/outils.php'; // une seule fois
include 'optionnel.php';              // simple avertissement si absent
```

Utilisez `__DIR__` pour des chemins fiables, et **ne passez jamais une entrée utilisateur** à `include`/`require`.

---

# 5. Fonctions

## 5.1 Définir et appeler

```php
function saluer(string $nom): string {
    return "Bonjour $nom !";
}
echo saluer("Alice");
```

## 5.2 Paramètres

```php
function presenter(string $nom, int $age = 18, ?string $ville = null): string {
    return "$nom, $age ans" . ($ville ? " à $ville" : "");
}

presenter("Alice");                              // valeur par défaut
presenter("Bob", 25, "Paris");
presenter(nom: "Chloé", ville: "Lyon");          // arguments NOMMÉS (8.0) : ordre libre

function total(int ...$nombres): int { return array_sum($nombres); }    // variadique
total(1, 2, 3);
total(...[4, 5, 6]);                                                     // déballage d'un tableau

function ajouter(array &$liste, $x): void { $liste[] = $x; }             // passage par référence
```

> Par défaut, les arguments sont passés **par valeur** (les objets, par « poignée » : leur contenu reste modifiable).

## 5.3 Valeurs de retour

```php
function minMax(array $t): array { return [min($t), max($t)]; }
[$mini, $maxi] = minMax([3, 1, 4]);               // destructuration

function nePasRetourner(): void { echo "rien"; }
function arreter(): never { exit("Fin"); }         // ne retourne jamais (8.1)
```

## 5.4 Déclarations de types *(à jour)*

| Type | Signification |
| --- | --- |
| `int`, `float`, `string`, `bool`, `array`, `object`, `callable`, `iterable` | Types de base |
| `?string` | `string` **ou** `null` |
| `int\|string` | **Union** (8.0) |
| `Countable&Traversable` | **Intersection** (8.1) |
| `mixed` | Toute valeur |
| `void` / `never` | Aucun retour / ne retourne jamais |
| `static`, `self` | Classe courante |
| `null`, `false`, `true` | Types autonomes (8.2) |

```php
function trouver(array $liste, int|string $cle): mixed { return $liste[$cle] ?? null; }
```

## 5.5 Portée des variables

```php
$global = "G";

function test() {
    // echo $global;            // ❌ non défini : variable hors portée
    global $global;             // possible, mais à éviter
    echo $GLOBALS['global'];    // idem
}

function compteur(): int {
    static $n = 0;              // conservée entre les appels
    return ++$n;
}
```

> ✅ Préférez **passer les valeurs en paramètres**. Les variables globales rendent le code difficile à tester.

## 5.6 Fonctions anonymes et fléchées

```php
$carre = function (int $x): int { return $x * $x; };
$facteur = 3;
$multiplier = function ($x) use ($facteur) { return $x * $facteur; };   // use : capture par valeur

$triple = fn($x) => $x * 3;          // fonction fléchée (7.4) : capture AUTOMATIQUEMENT les variables parentes (par valeur)

array_map(fn($n) => $n * 2, [1, 2, 3]);       // [2, 4, 6]
```

### Syntaxe de « callable de première classe » *(8.1)*

```php
$longueur = strlen(...);             // crée une Closure à partir d'une fonction existante
$methode = $objet->methode(...);
$statique = MaClasse::fabrique(...);
```

## 5.7 Récursivité

```php
function factorielle(int $n): int {
    return $n <= 1 ? 1 : $n * factorielle($n - 1);
}
```

## 5.8 Fonctions utiles

`function_exists()`, `is_callable()`, `call_user_func()`, `call_user_func_array()`, `func_get_args()`.

## 5.9 Bonnes pratiques

- Fonctions **courtes** et nommées par un **verbe** (`calculerTotal`).
- **Typez** paramètres et retours ; activez `strict_types`.
- Documentez avec **PHPDoc** quand les types ne suffisent pas (`@param list<int> $nombres`).
- Évitez les effets de bord et les globales.

---

# 6. Tableaux

## 6.1 Types de tableaux

Un **tableau** PHP est une structure ordonnée de paires clé → valeur : il sert de liste, de dictionnaire, de pile ou de file.

```php
// Indexé (clés 0, 1, 2…)
$fruits = ["pomme", "banane", "cerise"];

// Associatif (clés au choix)
$personne = ["nom" => "Alice", "age" => 30];

// Multidimensionnel
$utilisateurs = [
    ["nom" => "Alice", "age" => 30],
    ["nom" => "Bob",   "age" => 25],
];

echo $fruits[0];                        // pomme
echo $personne["nom"];                  // Alice
echo $utilisateurs[1]["nom"];           // Bob
```

> ✅ Utilisez la syntaxe courte `[]` plutôt que `array()`.

## 6.2 Ajouter, modifier, supprimer

```php
$fruits[] = "fraise";                   // ajout à la fin
$fruits[1] = "kiwi";                    // modification
$personne["ville"] = "Paris";           // ajout d'une clé
unset($personne["age"]);                // suppression

array_push($fruits, "a", "b");          // ajoute à la fin
array_pop($fruits);                     // retire le dernier
array_unshift($fruits, "début");        // ajoute au début
array_shift($fruits);                   // retire le premier
```

## 6.3 Parcourir

```php
foreach ($fruits as $indice => $fruit) { echo "$indice : $fruit\n"; }
foreach ($personne as $cle => $valeur) { echo "$cle = $valeur\n"; }

// Destructuration (avec clés)
['nom' => $nom, 'age' => $age] = $personne;
foreach ($utilisateurs as ['nom' => $n, 'age' => $a]) { echo "$n ($a)\n"; }
```

## 6.4 Fonctions essentielles

| Besoin | Fonctions |
| --- | --- |
| **Taille** | `count($t)` |
| **Existence** | `isset($t['k'])`, `array_key_exists('k', $t)`, `in_array($v, $t, true)` |
| **Clés / valeurs** | `array_keys()`, `array_values()` |
| **Recherche** | `array_search($v, $t, true)` |
| **Extraction** | `array_slice($t, $debut, $longueur)`, `array_splice()` |
| **Fusion** | `array_merge($a, $b)`, `[...$a, ...$b]`, `array_combine($cles, $valeurs)` |
| **Unicité** | `array_unique($t)` |
| **Colonne** | `array_column($lignes, 'nom', 'id')` |
| **Découpage** | `array_chunk($t, 3)` |
| **Somme / produit** | `array_sum()`, `array_product()` |
| **Inverser** | `array_reverse()`, `array_flip()` |
| **Tester une liste** | `array_is_list($t)` (8.1) |
| **Premier / dernier** | `array_key_first()`, `array_key_last()` ; `array_first()`, `array_last()` *(8.5)* |
| **Recherche fonctionnelle** | `array_find()`, `array_find_key()`, `array_any()`, `array_all()` *(8.4)* |

> ⚠️ `in_array` et `array_search` : passez **`true`** en 3ᵉ argument pour une comparaison **stricte**.

## 6.5 Fonctions d'ordre supérieur

```php
$nombres = [1, 2, 3, 4, 5];

array_map(fn($n) => $n * 2, $nombres);                          // [2, 4, 6, 8, 10]
array_filter($nombres, fn($n) => $n % 2 === 0);                 // [1 => 2, 3 => 4] (clés conservées)
array_reduce($nombres, fn($somme, $n) => $somme + $n, 0);       // 15
array_walk($nombres, function (&$n) { $n *= 2; });              // modifie en place
```

## 6.6 Trier

| Fonction | Tri |
| --- | --- |
| `sort()` / `rsort()` | Valeurs croissantes / décroissantes (réindexe) |
| `asort()` / `arsort()` | Valeurs, **conserve les clés** |
| `ksort()` / `krsort()` | Par clés |
| `usort($t, fn)` / `uasort` / `uksort` | Tri **personnalisé** |

```php
usort($utilisateurs, fn($a, $b) => $a['age'] <=> $b['age']);                 // par âge
usort($utilisateurs, fn($a, $b) => [$a['age'], $a['nom']] <=> [$b['age'], $b['nom']]);   // critères multiples
```

> Ces fonctions **modifient le tableau passé** (par référence) et renvoient un booléen ; le tri est **stable** depuis PHP 8.0.

## 6.7 Copie et références

Les tableaux sont copiés **par valeur** (avec copie différée : *copy-on-write*), contrairement aux objets.

```php
$a = [1, 2];
$b = $a;
$b[] = 3;          // $a reste [1, 2]
```

## 6.8 Parcours multidimensionnel

```php
foreach ($utilisateurs as $u) {
    echo "{$u['nom']} a {$u['age']} ans\n";
}
```

## 6.9 Interfaces utiles : `ArrayAccess`, `Countable`, `IteratorAggregate`

Permettent à des objets de se comporter comme des tableaux (voir [section 14](#14-programmation-orientée-objet)). Pour des collections riches, voir `Illuminate\Support\Collection` (Laravel) ou `ArrayObject`, `SplStack`, `SplQueue`.

---

# 7. Chaînes de caractères

## 7.1 Créer des chaînes

```php
$simple = 'Texte $brut\n';                 // aucune interprétation (sauf \\ et \')
$double = "Bonjour $nom\n";                // variables et séquences d'échappement interprétées

$heredoc = <<<TEXTE
    Bonjour {$nom},
    Texte sur plusieurs lignes avec "guillemets".
    TEXTE;                                  // l'indentation de la fermeture est retirée (7.3)

$nowdoc = <<<'TEXTE'
    Aucune $interpolation ici.
    TEXTE;
```

Concaténation : `.` et `.=` (`$a . $b`).

## 7.2 Fonctions courantes

| Besoin | Fonctions |
| --- | --- |
| **Longueur** | `strlen($s)` (octets), **`mb_strlen($s)`** (caractères) |
| **Casse** | `strtolower`, `strtoupper`, `ucfirst`, `ucwords` → versions **`mb_`** pour l'Unicode |
| **Recherche** | `str_contains`, `str_starts_with`, `str_ends_with` *(8.0)*, `strpos`, `strrpos`, `stripos` |
| **Extraction** | `substr($s, $debut, $longueur)`, `mb_substr` |
| **Remplacement** | `str_replace`, `str_ireplace`, `substr_replace` |
| **Nettoyage** | `trim`, `ltrim`, `rtrim` |
| **Découpe / assemblage** | `explode(",", $s)`, `implode(", ", $t)`, `str_split` |
| **Formatage** | `sprintf`, `printf`, `number_format`, `str_pad`, `wordwrap`, `nl2br` |
| **Comparaison** | `strcmp`, `strcasecmp`, `similar_text`, `levenshtein` |
| **Répétition** | `str_repeat` |
| **HTML** | `htmlspecialchars`, `strip_tags`, `html_entity_decode` |

```php
str_contains("Bonjour", "jour");                       // true
substr("Bonjour", 0, 3);                               // "Bon"
str_replace("a", "o", "banane");                       // "bonone"
implode(", ", ["a", "b", "c"]);                        // "a, b, c"
sprintf("%05.2f", 3.14159);                            // "03.14"
number_format(1234567.891, 2, ',', ' ');               // "1 234 567,89"
mb_strtoupper("élève");                                // "ÉLÈVE"
ucfirst("alice");                                      // "Alice"
```

> ⚠️ Avec du texte **UTF-8** (accents, emojis), utilisez les fonctions **`mb_*`** (extension `mbstring`) : `strlen("é")` vaut 2.

## 7.3 Traiter la saisie utilisateur

```php
$nom = trim($_POST['nom'] ?? '');
$nom = mb_substr($nom, 0, 50);                          // limiter la longueur
$mots = preg_split('/\s+/', $phrase, -1, PREG_SPLIT_NO_EMPTY);
```

## 7.4 Échappement

```php
echo "Il a dit \"Salut\"";           // guillemets échappés
echo 'L\'été';                       // apostrophe échappée
echo "Chemin : C:\\dossier";         // antislash
```

## 7.5 Échapper pour la sortie : `htmlspecialchars`

**Toute donnée affichée en HTML doit être échappée** :

```php
echo htmlspecialchars($saisie, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
```

(Raccourci utile : définir `function e(string $s): string { return htmlspecialchars($s, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8'); }`.)

## 7.6 Comparer des chaînes

```php
"abc" === "abc";                 // ✅
strcmp("a", "b");                // < 0
strcasecmp("A", "a");            // 0 (insensible à la casse)
hash_equals($connu, $saisi);     // ✅ comparaison à temps constant (jetons, signatures)
```

## 7.7 Chaînes et encodage

Enregistrez vos fichiers en **UTF-8**, servez `Content-Type: text/html; charset=UTF-8` et configurez `default_charset = "UTF-8"`. Pour convertir : `mb_convert_encoding()`. En 8.4+, `mb_trim`, `mb_ucfirst` et `mb_str_pad` existent.

---

# 8. Dates, heures et expressions régulières

*(Section ajoutée.)*

## 8.1 Dates et heures

Préférez les classes **`DateTimeImmutable`** (non mutable) et `DateTimeZone` aux fonctions `date()` / `strtotime()`.

```php
$maintenant = new DateTimeImmutable('now', new DateTimeZone('Europe/Paris'));
echo $maintenant->format('d/m/Y H:i');                       // 11/10/2026 14:30

$dans30Jours = $maintenant->modify('+30 days');
$date = DateTimeImmutable::createFromFormat('d/m/Y', '25/12/2026');

$difference = $maintenant->diff($date);
echo $difference->days . " jours";

$autreFuseau = $maintenant->setTimezone(new DateTimeZone('Indian/Antananarivo'));

date_default_timezone_set('Europe/Paris');                   // fuseau par défaut du script
```

Pour l'**affichage localisé** : `IntlDateFormatter` (extension `intl`).

```php
$fmt = new IntlDateFormatter('fr_FR', IntlDateFormatter::FULL, IntlDateFormatter::SHORT);
echo $fmt->format($maintenant);       // dimanche 11 octobre 2026 à 14:30
```

> 💡 Stockez les dates en **UTC** (ou `DATETIME` / `TIMESTAMP` côté base) et convertissez à l'affichage. Bibliothèque très utilisée : **Carbon**.

## 8.2 Expressions régulières (PCRE)

```php
preg_match('/^\d{4}-\d{2}-\d{2}$/', $texte);                      // 1 si correspondance, 0 sinon
preg_match('/(?<annee>\d{4})-(?<mois>\d{2})/', "2026-10", $m);    // $m['annee'] === "2026"
preg_match_all('/\d+/', "a1b22c333", $tous);                       // $tous[0] = ["1", "22", "333"]
preg_replace('/\s+/', ' ', "a   b    c");                          // "a b c"
preg_replace_callback('/\d+/', fn($m) => $m[0] * 2, "a1 b2");      // "a2 b4"
preg_split('/[\s,]+/', "a, b  c");                                  // ["a", "b", "c"]
preg_quote($saisie, '/');                                           // échappe une saisie utilisateur
```

Drapeaux : `i` (casse), `m` (multiligne), `s` (point = saut de ligne), `u` (**Unicode**, à utiliser avec du texte UTF-8), `x` (commentaires).

---

# 9. Formulaires et saisies utilisateur

## 9.1 Formulaire HTML et traitement

```html
<form action="traiter.php" method="post">
    <label>Nom : <input type="text" name="nom" required></label>
    <label>E-mail : <input type="email" name="email" required></label>
    <button type="submit">Envoyer</button>
</form>
```

```php
<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nom = trim($_POST['nom'] ?? '');
    echo "Bonjour " . htmlspecialchars($nom, ENT_QUOTES, 'UTF-8');
}
```

## 9.2 `$_GET` ou `$_POST` ?

| | `$_GET` | `$_POST` |
| --- | --- | --- |
| Transmission | Dans l'**URL** (`?q=php&page=2`) | Dans le **corps** de la requête |
| Visible / mise en favori | ✅ | ❌ |
| Taille | Limitée | Grande |
| Usage | **Lecture** : recherche, filtres, pagination (opérations sans effet de bord) | **Modification** : création, connexion, envoi de fichiers |
| Sécurité | Ne **jamais** y mettre de secrets | Pas plus sûr par nature : il faut **valider** et protéger contre le **CSRF** |

## 9.3 Validation

```php
$erreurs = [];

$nom = trim($_POST['nom'] ?? '');
if ($nom === '' || mb_strlen($nom) > 50) {
    $erreurs['nom'] = "Le nom est obligatoire (50 caractères max).";
}

$email = filter_var($_POST['email'] ?? '', FILTER_VALIDATE_EMAIL);
if ($email === false) {
    $erreurs['email'] = "Adresse e-mail invalide.";
}

$age = filter_var($_POST['age'] ?? null, FILTER_VALIDATE_INT, ['options' => ['min_range' => 0, 'max_range' => 120]]);
if ($age === false || $age === null) {
    $erreurs['age'] = "Âge invalide.";
}

if (!$erreurs) {
    // traitement… puis redirection
}
```

Filtres utiles : `FILTER_VALIDATE_EMAIL`, `_INT`, `_FLOAT`, `_BOOLEAN`, `_URL`, `_IP`, `_REGEXP` ; lecture directe : `filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL)`.

> ⚠️ **`FILTER_SANITIZE_STRING` est déprécié depuis PHP 8.1** (et supprimé depuis). **Ne l'utilisez plus.** Principe actuel : **valider** à l'entrée, **échapper à la sortie** (`htmlspecialchars` pour le HTML, requêtes préparées pour SQL).

## 9.4 Validation côté client **et** côté serveur

Les attributs HTML (`required`, `type="email"`, `pattern`, `maxlength`) améliorent l'expérience mais **ne remplacent jamais** la validation serveur : n'importe qui peut envoyer une requête sans passer par votre formulaire.

## 9.5 Motif Post/Redirect/Get (PRG)

Évite le double envoi du formulaire lors d'un rechargement :

```php
if (!$erreurs) {
    enregistrer($nom, $email);
    $_SESSION['flash'] = "Enregistré !";
    header('Location: /merci.php', true, 303);
    exit;
}
```

## 9.6 Pré-remplir un formulaire après erreur

```php
<input type="text" name="nom" value="<?= htmlspecialchars($nom ?? '', ENT_QUOTES, 'UTF-8') ?>">
<?php if (isset($erreurs['nom'])): ?>
    <span class="erreur"><?= htmlspecialchars($erreurs['nom']) ?></span>
<?php endif; ?>
```

## 9.7 Protection CSRF

Chaque formulaire qui modifie des données doit inclure un **jeton** : voir [section 16.3](#163-csrf--falsification-de-requête-inter-sites).

---

# 10. Système de fichiers

## 10.1 Lire et écrire rapidement

```php
$contenu = file_get_contents(__DIR__ . '/notes.txt');          // false en cas d'échec
file_put_contents(__DIR__ . '/notes.txt', "Ligne\n");          // écrase
file_put_contents(__DIR__ . '/notes.txt', "Suite\n", FILE_APPEND | LOCK_EX);   // ajoute, avec verrou

$lignes = file(__DIR__ . '/notes.txt', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);   // tableau de lignes
```

## 10.2 Lecture et écriture avec `fopen`

```php
$f = fopen('donnees.txt', 'r');
if ($f === false) { throw new RuntimeException("Ouverture impossible"); }

while (($ligne = fgets($f)) !== false) {      // ligne par ligne : économe en mémoire
    echo htmlspecialchars($ligne);
}
fclose($f);
```

| Mode | Signification |
| --- | --- |
| `r` | Lecture seule |
| `w` | Écriture, **écrase** (crée si absent) |
| `a` | Ajout en fin de fichier |
| `x` | Création exclusive (échoue si existe) |
| `r+` / `w+` / `a+` | Lecture + écriture |
| `b` | Mode binaire (ex. `rb`) |

## 10.3 Fonctions utiles

| Fonction | Rôle |
| --- | --- |
| `file_exists()`, `is_file()`, `is_dir()` | Existence / type |
| `is_readable()`, `is_writable()` | Droits |
| `filesize()`, `filemtime()` | Taille, date de modification |
| `unlink()` | Supprimer un fichier |
| `rename()`, `copy()` | Renommer / déplacer, copier |
| `mkdir($d, 0755, true)`, `rmdir()` | Créer (récursif) / supprimer un dossier vide |
| `scandir()`, `glob('*.txt')` | Lister |
| `basename()`, `dirname()`, `pathinfo()` | Analyser un chemin |
| `realpath()` | Chemin absolu canonique |
| `tempnam()`, `sys_get_temp_dir()` | Fichiers temporaires |

```php
$info = pathinfo('/var/www/photo.jpg');
// ['dirname' => '/var/www', 'basename' => 'photo.jpg', 'extension' => 'jpg', 'filename' => 'photo']
```

## 10.4 CSV et JSON

```php
// CSV : lire
if (($f = fopen('personnes.csv', 'r')) !== false) {
    $entete = fgetcsv($f, 0, ',', '"', '\\');
    while (($ligne = fgetcsv($f, 0, ',', '"', '\\')) !== false) {
        $personne = array_combine($entete, $ligne);
    }
    fclose($f);
}
// CSV : écrire
$f = fopen('sortie.csv', 'w');
fputcsv($f, ['nom', 'age'], ',', '"', '\\');
fputcsv($f, ['Alice', 30], ',', '"', '\\');
fclose($f);

// JSON
file_put_contents('data.json', json_encode($donnees, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR));
$donnees = json_decode(file_get_contents('data.json'), true, 512, JSON_THROW_ON_ERROR);
```

## 10.5 Classes SPL

```php
$fichier = new SplFileObject('gros.txt');
foreach ($fichier as $numero => $ligne) { /* … */ }
```

## 10.6 Téléversement sécurisé de fichiers

```html
<form action="upload.php" method="post" enctype="multipart/form-data">
    <input type="file" name="photo" accept="image/*">
    <button>Envoyer</button>
</form>
```

```php
<?php
declare(strict_types=1);

const DOSSIER = __DIR__ . '/../uploads';         // idéalement HORS de la racine web
const TAILLE_MAX = 2 * 1024 * 1024;              // 2 Mo
const TYPES_AUTORISES = ['image/jpeg' => 'jpg', 'image/png' => 'png', 'image/webp' => 'webp'];

$fichier = $_FILES['photo'] ?? null;

if (!$fichier || $fichier['error'] !== UPLOAD_ERR_OK) {
    exit("Erreur de téléversement (code " . ($fichier['error'] ?? '?') . ").");
}
if ($fichier['size'] > TAILLE_MAX) {
    exit("Fichier trop volumineux.");
}
if (!is_uploaded_file($fichier['tmp_name'])) {
    exit("Fichier invalide.");
}

// Type RÉEL détecté par le contenu (et non par $_FILES['type'] ni l'extension, falsifiables)
$mime = (new finfo(FILEINFO_MIME_TYPE))->file($fichier['tmp_name']);
if (!isset(TYPES_AUTORISES[$mime])) {
    exit("Type de fichier non autorisé.");
}

// Nouveau nom aléatoire : on ne réutilise JAMAIS le nom d'origine
$nom = bin2hex(random_bytes(16)) . '.' . TYPES_AUTORISES[$mime];

if (!move_uploaded_file($fichier['tmp_name'], DOSSIER . '/' . $nom)) {
    exit("Impossible d'enregistrer le fichier.");
}
echo "Fichier enregistré.";
```

Réglages `php.ini` : `file_uploads`, `upload_max_filesize`, `post_max_size`, `max_file_uploads`.

## 10.7 Précautions

- **Traversée de répertoires** : ne construisez jamais un chemin à partir d'une saisie brute (`../../etc/passwd`). Utilisez `basename()`, une **liste blanche**, et vérifiez `realpath()` :

```php
$chemin = realpath(DOSSIER . '/' . basename($_GET['fichier']));
if ($chemin === false || !str_starts_with($chemin, realpath(DOSSIER) . DIRECTORY_SEPARATOR)) { http_response_code(400); exit; }
```

- N'exécutez **jamais** un fichier téléversé ; interdisez l'exécution de PHP dans le dossier d'envoi.
- Utilisez `LOCK_EX` pour les écritures concurrentes.
- Vérifiez les **droits** du système (`chmod 0755` dossiers / `0644` fichiers) ; n'utilisez jamais `0777`.

---

# 11. Sessions et cookies

## 11.1 Principe

HTTP est **sans état** : sessions et cookies permettent de « se souvenir » d'un visiteur.

| | `$_SESSION` | `$_COOKIE` |
| --- | --- | --- |
| Stockage | **Serveur** (le navigateur ne garde qu'un identifiant) | **Navigateur** |
| Sécurité | Plus sûr | Lisible et modifiable par l'utilisateur |
| Taille | Grande | ~4 Ko |
| Durée | Jusqu'à la fermeture du navigateur / expiration | Choisie (`expires`) |
| Usage | Connexion, panier, messages flash | Préférences, « se souvenir de moi » |

## 11.2 Sessions

```php
<?php
session_start();                              // AVANT toute sortie HTML

$_SESSION['utilisateur'] = "Alice";
echo $_SESSION['utilisateur'] ?? "Invité";

unset($_SESSION['utilisateur']);              // retirer une variable
```

### Déconnexion complète

```php
session_start();
$_SESSION = [];
if (ini_get('session.use_cookies')) {
    $p = session_get_cookie_params();
    setcookie(session_name(), '', ['expires' => time() - 42000, 'path' => $p['path'], 'domain' => $p['domain'],
                                   'secure' => $p['secure'], 'httponly' => $p['httponly'], 'samesite' => $p['samesite'] ?? 'Lax']);
}
session_destroy();
```

## 11.3 Cookies *(à jour : tableau d'options)*

```php
setcookie('theme', 'sombre', [
    'expires'  => time() + 30 * 24 * 3600,     // 30 jours
    'path'     => '/',
    'secure'   => true,                        // HTTPS uniquement
    'httponly' => true,                        // inaccessible à JavaScript
    'samesite' => 'Lax',                       // protège du CSRF
]);

echo $_COOKIE['theme'] ?? 'clair';             // lisible dès la REQUÊTE SUIVANTE

setcookie('theme', '', ['expires' => time() - 3600, 'path' => '/']);    // supprimer
```

> ⚠️ `setcookie()` doit être appelé **avant toute sortie** (sinon : *« headers already sent »*).
> 🔒 Ne stockez jamais d'informations sensibles dans un cookie ; tout ce qu'il contient doit être considéré comme **modifiable par l'utilisateur**.

## 11.4 Sécuriser les sessions

```php
// Réglages recommandés (php.ini ou avant session_start)
ini_set('session.use_strict_mode', '1');
ini_set('session.use_only_cookies', '1');
session_set_cookie_params([
    'lifetime' => 0, 'path' => '/', 'secure' => true, 'httponly' => true, 'samesite' => 'Lax',
]);
session_start();

// À la connexion réussie : changer d'identifiant (anti fixation de session)
session_regenerate_id(true);
$_SESSION['user_id'] = $utilisateur['id'];
$_SESSION['derniere_activite'] = time();

// Expiration par inactivité
if (isset($_SESSION['derniere_activite']) && time() - $_SESSION['derniere_activite'] > 1800) {
    session_unset(); session_destroy();
}
```

| Bonne pratique | Pourquoi |
| --- | --- |
| **HTTPS** partout, cookies `Secure` | Empêche l'interception |
| `HttpOnly` | Protège du vol par XSS |
| `SameSite=Lax` ou `Strict` | Réduit le CSRF |
| `session_regenerate_id(true)` après connexion / élévation de droits | Anti-fixation |
| Ne **jamais** mettre l'identifiant de session dans l'URL | Fuite par référent / historique |
| Expiration et déconnexion explicite | Limite les sessions volées |
| Stocker l'**identifiant** de l'utilisateur, jamais son mot de passe | |

---

# 12. Bases de données avec PDO

## 12.1 PDO ou MySQLi ?

| | **PDO** ✅ | **MySQLi** |
| --- | --- | --- |
| Bases supportées | MySQL, MariaDB, PostgreSQL, SQLite, SQL Server… | MySQL / MariaDB uniquement |
| API | Orientée objet | Objet et procédural |
| Paramètres nommés (`:nom`) | ✅ | ❌ (uniquement `?`) |
| Recommandation | **Standard actuel** | Acceptable pour du 100 % MySQL |

> 🚫 Les anciennes fonctions `mysql_*` ont été **supprimées en PHP 7**.

## 12.2 Connexion avec PDO

```php
<?php
declare(strict_types=1);

$dsn = 'mysql:host=localhost;dbname=boutique;charset=utf8mb4';

try {
    $pdo = new PDO($dsn, 'utilisateur', 'mot_de_passe', [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,    // erreurs → exceptions
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES   => false,                     // vraies requêtes préparées
    ]);
} catch (PDOException $e) {
    error_log($e->getMessage());                                   // journaliser, ne pas afficher
    exit("Service momentanément indisponible.");
}
```

> 🔒 Chargez les identifiants depuis des **variables d'environnement** (`getenv()`, `.env`), jamais dans le code versionné.

## 12.3 Requêtes préparées (anti-injection SQL)

**Règle absolue : n'insérez jamais une variable directement dans une requête SQL.**

```php
// ❌ Vulnérable à l'injection SQL
$pdo->query("SELECT * FROM users WHERE email = '$email'");

// ✅ Requête préparée (paramètres nommés)
$stmt = $pdo->prepare("SELECT id, nom, email FROM users WHERE email = :email AND actif = :actif");
$stmt->execute([':email' => $email, ':actif' => 1]);
$utilisateur = $stmt->fetch();            // une ligne (ou false)

// Paramètres positionnels
$stmt = $pdo->prepare("INSERT INTO users (nom, email) VALUES (?, ?)");
$stmt->execute([$nom, $email]);
$idCree = $pdo->lastInsertId();
```

Avec un type précis : `$stmt->bindValue(':id', $id, PDO::PARAM_INT);`.

### Clause `IN` dynamique

```php
$marqueurs = implode(',', array_fill(0, count($ids), '?'));
$stmt = $pdo->prepare("SELECT * FROM produits WHERE id IN ($marqueurs)");
$stmt->execute($ids);
```

### Noms de tables / colonnes dynamiques

Les identifiants ne se paramètrent pas : utilisez une **liste blanche**.

```php
$colonnesTriables = ['nom', 'prix', 'date'];
$tri = in_array($_GET['tri'] ?? '', $colonnesTriables, true) ? $_GET['tri'] : 'nom';
$stmt = $pdo->query("SELECT * FROM produits ORDER BY $tri");
```

## 12.4 Opérations CRUD

```php
// CREATE
$stmt = $pdo->prepare("INSERT INTO users (nom, email) VALUES (:nom, :email)");
$stmt->execute([':nom' => $nom, ':email' => $email]);

// READ
$tous = $pdo->query("SELECT id, nom FROM users ORDER BY nom")->fetchAll();
foreach ($tous as $u) { echo htmlspecialchars($u['nom']) . "<br>"; }

$stmt = $pdo->prepare("SELECT * FROM users WHERE id = ?");
$stmt->execute([$id]);
$user = $stmt->fetch();

// UPDATE
$stmt = $pdo->prepare("UPDATE users SET nom = :nom WHERE id = :id");
$stmt->execute([':nom' => $nom, ':id' => $id]);
echo $stmt->rowCount() . " ligne(s) modifiée(s)";

// DELETE
$stmt = $pdo->prepare("DELETE FROM users WHERE id = ?");
$stmt->execute([$id]);
```

Modes de récupération : `FETCH_ASSOC` (tableau associatif), `FETCH_OBJ`, `FETCH_CLASS` (hydrate une classe), `fetchColumn()`, `FETCH_KEY_PAIR`.

## 12.5 Transactions

Plusieurs opérations **toutes réussies ou toutes annulées** :

```php
try {
    $pdo->beginTransaction();
    $pdo->prepare("UPDATE comptes SET solde = solde - ? WHERE id = ?")->execute([100, 1]);
    $pdo->prepare("UPDATE comptes SET solde = solde + ? WHERE id = ?")->execute([100, 2]);
    $pdo->commit();
} catch (Throwable $e) {
    if ($pdo->inTransaction()) { $pdo->rollBack(); }
    throw $e;
}
```

## 12.6 MySQLi (rappel)

```php
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);          // exceptions
$conn = new mysqli('localhost', 'user', 'mdp', 'boutique');
$conn->set_charset('utf8mb4');

$stmt = $conn->prepare("SELECT id, nom FROM users WHERE email = ?");
$stmt->bind_param('s', $email);          // s = string, i = int, d = double, b = blob
$stmt->execute();
$resultat = $stmt->get_result();
while ($ligne = $resultat->fetch_assoc()) { /* … */ }
```

## 12.7 Bonnes pratiques

- **Requêtes préparées partout.**
- Utilisez **`utf8mb4`** (support complet d'Unicode, emojis compris).
- Compte de base de données aux **privilèges minimaux** (pas de `root`).
- Ne jamais afficher les erreurs SQL à l'utilisateur.
- Créez des **index** sur les colonnes filtrées ; évitez `SELECT *` ; paginez (`LIMIT`/`OFFSET` ou pagination par curseur).
- Versionnez le schéma avec des **migrations** (Phinx, Doctrine Migrations, Laravel).
- Pour gérer la complexité : un **ORM** (Eloquent, Doctrine) ou un constructeur de requêtes.

---

# 13. Gestion des erreurs et exceptions

## 13.1 Types d'erreurs

| Niveau | Constante | Description |
| --- | --- | --- |
| Avis | `E_NOTICE` | Problème mineur (variable non définie…) |
| Avertissement | `E_WARNING` | Problème non bloquant (fichier introuvable…) |
| Fatal | `E_ERROR` | Arrêt du script |
| Analyse | `E_PARSE` | Erreur de syntaxe |
| Dépréciation | `E_DEPRECATED` | Fonctionnalité à ne plus utiliser |
| Utilisateur | `E_USER_*` | Générées avec `trigger_error()` |

> Depuis PHP 7, la plupart des erreurs graves sont des **exceptions** de type **`Error`** (attrapables).

## 13.2 Hiérarchie : `Throwable`

```text
Throwable
 ├── Error
 │    ├── TypeError (ArgumentCountError)
 │    ├── ValueError
 │    ├── ArithmeticError (DivisionByZeroError)
 │    ├── UnhandledMatchError
 │    └── …
 └── Exception
      ├── RuntimeException, LogicException (InvalidArgumentException, …)
      ├── JsonException, PDOException
      └── vos exceptions personnalisées
```

## 13.3 `try` / `catch` / `finally`

```php
try {
    $resultat = intdiv(10, 0);
} catch (DivisionByZeroError $e) {
    echo "Division par zéro : " . $e->getMessage();
} catch (InvalidArgumentException | TypeError $e) {    // plusieurs types
    echo "Erreur d'argument : " . $e->getMessage();
} catch (Throwable $e) {                                // filet de sécurité
    error_log((string) $e);
} finally {
    echo "Toujours exécuté (nettoyage)";
}
```

## 13.4 Lancer et créer des exceptions

```php
function diviser(float $a, float $b): float {
    if ($b === 0.0) {
        throw new InvalidArgumentException("Le diviseur ne peut pas être nul.");
    }
    return $a / $b;
}

class SoldeInsuffisantException extends RuntimeException {
    public function __construct(private float $manque, ?Throwable $precedente = null) {
        parent::__construct("Il manque $manque €.", 0, $precedente);
    }
    public function getManque(): float { return $this->manque; }
}

// Chaînage d'exceptions
try { /* … */ } catch (PDOException $e) {
    throw new RuntimeException("Impossible d'enregistrer la commande.", 0, $e);   // $e->getPrevious()
}

$valeur = $x ?? throw new InvalidArgumentException("x manquant");                // throw est une expression (8.0)
```

Méthodes utiles : `getMessage()`, `getCode()`, `getFile()`, `getLine()`, `getTraceAsString()`, `getPrevious()`.

## 13.5 Configuration et journalisation

```php
// Développement
error_reporting(E_ALL);
ini_set('display_errors', '1');

// ✅ Production : ne JAMAIS afficher les erreurs à l'utilisateur
ini_set('display_errors', '0');
ini_set('log_errors', '1');
ini_set('error_log', '/var/log/php/app.log');

error_log("Message à journaliser");
```

Dans `php.ini` : `error_reporting = E_ALL`, `display_errors = Off` (production), `log_errors = On`.

## 13.6 Gestionnaires globaux

```php
set_error_handler(function (int $niveau, string $message, string $fichier, int $ligne): bool {
    throw new ErrorException($message, 0, $niveau, $fichier, $ligne);     // convertit les erreurs en exceptions
});

set_exception_handler(function (Throwable $e): void {
    error_log((string) $e);
    http_response_code(500);
    echo "Une erreur est survenue.";
});
```

Pour une journalisation professionnelle : **Monolog** (compatible PSR-3), et un service de suivi d'erreurs (Sentry…).

## 13.7 Bonnes pratiques

- Attrapez les exceptions **là où vous savez les traiter**.
- Ne **taisez** jamais une erreur (pas de `@` ni de `catch` vide).
- Messages **génériques** pour l'utilisateur, **détails** dans les journaux.
- Utilisez des exceptions **spécifiques** et `JSON_THROW_ON_ERROR`.
- Libérez les ressources dans `finally`.

---

# 14. Programmation orientée objet

## 14.1 Classes et objets

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
        $this->kilometrage += $km;
    }

    public function getKilometrage(): int
    {
        return $this->kilometrage;
    }
}

$v = new Voiture("Renault");
$v->rouler(120);
echo $v->marque, " : ", $v->getKilometrage(), " km";
```

`$this` désigne l'objet courant ; `->` accède aux membres d'une instance ; `::` aux membres statiques et constantes.

## 14.2 Promotion de propriétés du constructeur *(8.0, à jour)*

```php
class Utilisateur
{
    public function __construct(
        public readonly int $id,              // lecture seule (8.1) : assignée une seule fois
        public string $nom,
        private ?string $email = null,
    ) {}
}

$u = new Utilisateur(1, "Alice");
// $u->id = 2;     // ❌ Error : propriété readonly
```

> **Classes `readonly`** *(8.2)* : `readonly class Point { public function __construct(public int $x, public int $y) {} }`.

## 14.3 Visibilité

| Mot-clé | Accessible depuis |
| --- | --- |
| `public` | Partout |
| `protected` | La classe et ses **sous-classes** |
| `private` | La **classe seule** |

**Visibilité asymétrique** *(8.4)* : lecture publique, écriture restreinte :

```php
class Compte {
    public private(set) float $solde = 0.0;     // lisible partout, modifiable seulement dans la classe
    public function deposer(float $m): void { $this->solde += $m; }
}
```

## 14.4 Hooks de propriétés *(8.4, à jour)*

Remplacent la plupart des getters/setters écrits à la main :

```php
class Personne
{
    public string $nomComplet {
        get => $this->prenom . ' ' . $this->nom;           // propriété calculée
    }

    public string $email {
        set (string $valeur) {
            if (!filter_var($valeur, FILTER_VALIDATE_EMAIL)) {
                throw new InvalidArgumentException("E-mail invalide");
            }
            $this->email = strtolower($valeur);
        }
    }

    public function __construct(public string $prenom, public string $nom) {}
}
```

## 14.5 Héritage

```php
class Animal
{
    public function __construct(protected string $nom) {}

    public function parler(): string { return "..."; }
}

class Chien extends Animal
{
    public function parler(): string { return "{$this->nom} dit : Ouaf !"; }

    public function presenter(): string { return parent::parler() . " (parent)"; }   // appel du parent
}

echo (new Chien("Rex"))->parler();
```

- `final class` : ne peut pas être étendue ; `final function` : ne peut pas être redéfinie.
- `#[\Override]` *(8.3)* : vérifie qu'une méthode redéfinit bien une méthode parente.

## 14.6 Membres statiques et constantes

```php
class Compteur
{
    public const MAX = 100;                          // constante de classe
    public const string NOM = "Compteur";            // constante TYPÉE (8.3)
    private static int $total = 0;

    public static function incrementer(): int { return ++self::$total; }
}

Compteur::incrementer();
echo Compteur::MAX;

// Liaison statique tardive : static:: (≠ self::)
class Modele { public static function creer(): static { return new static(); } }
```

## 14.7 Classes abstraites, interfaces et traits

```php
// Classe abstraite : non instanciable, impose des méthodes
abstract class Forme
{
    abstract public function aire(): float;
    public function decrire(): string { return sprintf("Aire : %.2f", $this->aire()); }
}

// Interface : contrat de méthodes publiques (implémentation multiple possible)
interface Exportable { public function exporter(): string; }
interface Journalisable { const NIVEAU = 'info'; public function journaliser(string $m): void; }

// Trait : réutilisation de code horizontale
trait Horodatage
{
    private ?DateTimeImmutable $creeLe = null;
    public function marquerCreation(): void { $this->creeLe = new DateTimeImmutable(); }
}

class Cercle extends Forme implements Exportable
{
    use Horodatage;

    public function __construct(private float $rayon) {}
    public function aire(): float { return M_PI * $this->rayon ** 2; }
    public function exporter(): string { return json_encode(['rayon' => $this->rayon]); }
}
```

| | Classe abstraite | Interface | Trait |
| --- | --- | --- | --- |
| Instanciable | ❌ | ❌ | ❌ |
| Héritage / implémentation multiple | Un seul parent | **Plusieurs** | Plusieurs traits |
| Contient du code | ✅ | ❌ (signatures) | ✅ |
| Propriétés | ✅ | ❌ (constantes uniquement ; hooks depuis 8.4) | ✅ |
| Rôle | Base commune | **Contrat** | **Réutilisation** de code |

## 14.8 Énumérations *(8.1, ajout)*

```php
enum Statut: string
{
    case Brouillon = 'brouillon';
    case Publie = 'publie';

    public function libelle(): string
    {
        return match ($this) {
            self::Brouillon => "Brouillon",
            self::Publie    => "Publié",
        };
    }
}

$s = Statut::from('publie');          // lève ValueError si inconnu
$t = Statut::tryFrom('inconnu');      // null
echo $s->value, $s->name, $s->libelle();
Statut::cases();                      // tous les cas
```

## 14.9 Méthodes magiques

| Méthode | Déclenchement |
| --- | --- |
| `__construct()` / `__destruct()` | Création / destruction de l'objet |
| `__toString()` | Conversion en chaîne (`echo $objet`) |
| `__get()` / `__set()` / `__isset()` / `__unset()` | Accès à une propriété **inaccessible** |
| `__call()` / `__callStatic()` | Appel d'une méthode inexistante |
| `__invoke()` | Utilisation de l'objet comme fonction |
| `__clone()` | Après `clone` |
| `__serialize()` / `__unserialize()` | Sérialisation |

```php
class Prix implements Stringable
{
    public function __construct(private float $montant) {}
    public function __toString(): string { return number_format($this->montant, 2, ',', ' ') . ' €'; }
}
echo new Prix(12.5);       // 12,50 €
```

## 14.10 Objets : copie et comparaison

```php
$a = new Voiture("A");
$b = $a;              // même objet (poignée copiée)
$c = clone $a;        // copie superficielle ; __clone() permet de copier en profondeur

$a == $c;             // true : mêmes propriétés et même classe
$a === $c;            // false : instances différentes
$a instanceof Voiture;
```

*(8.5)* `clone` peut modifier des propriétés au passage, pratique pour les objets `readonly` : `$b = clone($a, ['marque' => 'B']);`.

## 14.11 Attributs *(8.0, ajout)*

Métadonnées structurées, lues par réflexion, utilisées par les frameworks (routes, validation, ORM) :

```php
#[Route('/produits', methods: ['GET'])]
#[\Deprecated("Utiliser nouvelleMethode()")]          // 8.4
#[\NoDiscard]                                         // 8.5 : avertit si le résultat est ignoré
public function liste(): Response { /* … */ }
```

## 14.12 Espaces de noms et chargement automatique

```php
<?php
declare(strict_types=1);

namespace App\Service;

use App\Model\Utilisateur;
use InvalidArgumentException;                    // classe globale à importer
use function strlen;                             // facultatif

final class UtilisateurService
{
    public function creer(string $nom): Utilisateur { return new Utilisateur(1, $nom); }
}
```

**PSR-4** : le nom complet de la classe correspond au chemin du fichier (`App\Service\UtilisateurService` → `src/Service/UtilisateurService.php`). **Composer** génère l'autoloader (voir [section 17](#17-composer-et-gestion-des-dépendances)) :

```php
require __DIR__ . '/vendor/autoload.php';
```

## 14.13 Autres notions

- **Fermetures liées** : `Closure::bind()`, `$this` dans les closures.
- **Objets de valeur** (*value objects*) immuables, **injection de dépendances** (passer les collaborateurs au constructeur) et **interfaces** pour découpler.
- **`new` dans les initialiseurs** *(8.1)* : `public function __construct(private Logger $log = new NullLogger()) {}`.
- **Instanciation sans parenthèses** *(8.4)* : `new Voiture("A")->rouler(10);`.
- **Objets paresseux** *(8.4)* : instanciation différée pour les ORM.
- Principes **SOLID**, **DRY**, **KISS** ; préférez la **composition** à l'héritage.

---

# 15. PHP et le web

## 15.1 En-têtes HTTP

```php
<?php
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
http_response_code(201);                         // code de statut

header_remove('X-Powered-By');                   // masquer des informations inutiles
```

> ⚠️ `header()` doit être appelé **avant toute sortie** (HTML, espace, BOM). Sinon : *« Cannot modify header information – headers already sent »*. Vérification : `headers_sent($fichier, $ligne)`.

### Lire les en-têtes de la requête

```php
$methode = $_SERVER['REQUEST_METHOD'];
$agent   = $_SERVER['HTTP_USER_AGENT'] ?? '';
$autorisation = $_SERVER['HTTP_AUTHORIZATION'] ?? '';
$tousLesEntetes = getallheaders();               // selon l'environnement (PHP-FPM / Apache)
```

## 15.2 Redirections

```php
header('Location: /tableau-de-bord.php', true, 302);
exit;                                            // ⚠️ toujours arrêter le script après
```

| Code | Usage |
| --- | --- |
| `301` | Redirection **permanente** |
| `302` / `307` | Temporaire |
| `303` | « Voir ailleurs » : après un POST (motif PRG) |

> 🔒 **Ne redirigez jamais vers une URL provenant directement de l'utilisateur** (*open redirect*) : vérifiez-la par liste blanche ou n'acceptez que des chemins internes.

## 15.3 Télécharger un fichier

```php
$dossier = realpath(__DIR__ . '/../fichiers');
$chemin  = realpath($dossier . '/' . basename($_GET['f'] ?? ''));

if ($chemin === false || !str_starts_with($chemin, $dossier . DIRECTORY_SEPARATOR)) {
    http_response_code(404);
    exit;
}

header('Content-Type: application/octet-stream');
header('Content-Disposition: attachment; filename="' . rawurlencode(basename($chemin)) . '"');
header('Content-Length: ' . filesize($chemin));
header('X-Content-Type-Options: nosniff');
readfile($chemin);                               // flux sans tout charger en mémoire
exit;
```

Pour de gros fichiers, déléguez au serveur web (`X-Accel-Redirect` avec Nginx, `X-Sendfile` avec Apache).

## 15.4 Envoyer des e-mails

### La fonction `mail()` (basique)

```php
$ok = mail('dest@exemple.com', 'Sujet', "Corps du message", [
    'From' => 'noreply@monsite.fr',
    'Content-Type' => 'text/plain; charset=UTF-8',
]);
```

⚠️ Limites : pas d'authentification SMTP, forte probabilité de classement en **spam**, peu de contrôle. 🔒 **Injection d'en-têtes** : n'insérez jamais une saisie utilisateur non nettoyée dans `From`, `To` ou `Subject` (retours à la ligne).

### Bibliothèques (recommandé) : PHPMailer, Symfony Mailer

```bash
composer require phpmailer/phpmailer
```

```php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

$mail = new PHPMailer(true);                     // true : exceptions
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
    $mail->AltBody = 'Bonjour !';
    $mail->send();
} catch (Exception $e) {
    error_log($mail->ErrorInfo);
}
```

**Délivrabilité** : configurez **SPF, DKIM et DMARC** pour votre domaine, ou utilisez un service transactionnel (Mailgun, Postmark, Amazon SES, Brevo…). Envoyez les e-mails via une **file d'attente** pour ne pas ralentir la requête.

## 15.5 Requêtes HTTP sortantes

```php
// cURL
$ch = curl_init('https://api.exemple.com/data');
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_TIMEOUT        => 10,
    CURLOPT_HTTPHEADER     => ['Accept: application/json', 'Authorization: Bearer ' . $jeton],
]);
$reponse = curl_exec($ch);
$code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);
```

Plus confortable : **Guzzle** ou **Symfony HttpClient** (`composer require guzzlehttp/guzzle`). Définissez toujours un **délai d'expiration**.

## 15.6 Utiliser l'URL

```php
$url = parse_url('https://exemple.com:8080/chemin?x=1#haut');
parse_str($url['query'], $parametres);
http_build_query(['q' => 'café', 'page' => 2]);           // q=caf%C3%A9&page=2
urlencode($texte); rawurlencode($texte);
```

*(8.5)* L'extension **URI** (`Uri\Rfc3986\Uri`, `Uri\WhatWg\Url`) offre une analyse d'URL conforme aux standards.

## 15.7 Bonnes pratiques

- Envoyez les en-têtes **avant** toute sortie ; terminez par `exit` après une redirection.
- Définissez le bon `Content-Type` et l'encodage.
- Validez ce que vous redirigez ou téléchargez.
- Pour les e-mails : SMTP authentifié, SPF/DKIM/DMARC, file d'attente.

---

# 16. Sécurité

## 16.1 Principe général

> **Ne faites jamais confiance aux données venant de l'utilisateur** (formulaires, URL, cookies, en-têtes, fichiers, API tierces). **Validez à l'entrée, échappez à la sortie.**

| Menace | Protection |
| --- | --- |
| **Injection SQL** | Requêtes préparées (PDO) |
| **XSS** (injection de scripts) | `htmlspecialchars()` à l'affichage, CSP |
| **CSRF** | Jeton anti-CSRF, cookies `SameSite` |
| **Fixation / vol de session** | `session_regenerate_id`, `HttpOnly`, HTTPS |
| **Mots de passe faibles** | `password_hash`, limitation des tentatives |
| **Téléversements dangereux** | Validation du type réel, renommage, dossier hors web |
| **Traversée de chemin** | `basename`, `realpath`, liste blanche |
| **Injection de commandes** | Éviter `exec`/`shell_exec` ; `escapeshellarg` |
| **Désérialisation non fiable** | Pas de `unserialize()` sur des données externes → JSON |
| **Inclusion de fichiers** | Jamais de chemin issu de l'utilisateur dans `include` |
| **SSRF** | Valider / filtrer les URL appelées côté serveur |

## 16.2 Validation, assainissement et échappement

```php
// Validation
$email = filter_var($_POST['email'] ?? '', FILTER_VALIDATE_EMAIL);

// Échappement à la SORTIE, selon le contexte
echo htmlspecialchars($saisie, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');      // HTML
echo json_encode($donnees, JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT);   // JSON dans du HTML
echo urlencode($saisie);                                                    // URL
// SQL : requêtes préparées (jamais d'échappement manuel)
```

> ⚠️ `FILTER_SANITIZE_STRING` est **supprimé** : n'utilisez ni lui ni `strip_tags()` comme protection XSS. `strip_tags` ne remplace pas `htmlspecialchars`.

### Protection XSS supplémentaire : Content Security Policy

```php
header("Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'self'");
```

## 16.3 CSRF : falsification de requête inter-sites

```php
// Génération du jeton (une fois par session)
session_start();
if (empty($_SESSION['csrf'])) {
    $_SESSION['csrf'] = bin2hex(random_bytes(32));
}
```

```php
<form method="post" action="supprimer.php">
    <input type="hidden" name="csrf" value="<?= htmlspecialchars($_SESSION['csrf']) ?>">
    <button>Supprimer</button>
</form>
```

```php
// Vérification
if (!hash_equals($_SESSION['csrf'] ?? '', $_POST['csrf'] ?? '')) {
    http_response_code(403);
    exit("Requête refusée (jeton CSRF invalide).");
}
```

Complément : cookies `SameSite=Lax/Strict`, vérification de l'en-tête `Origin`, et **méthodes HTTP appropriées** (jamais d'action destructive sur un `GET`). Les frameworks intègrent déjà cette protection.

## 16.4 Hachage des mots de passe

Ne stockez **jamais** un mot de passe en clair, ni avec `md5()` / `sha1()` (trop rapides, cassables), ni avec un sel « maison ».

```php
$hash = password_hash($motDePasse, PASSWORD_DEFAULT);          // algorithme sûr du moment (bcrypt aujourd'hui) + sel intégré
// Option plus robuste : PASSWORD_ARGON2ID

if (password_verify($saisie, $hash)) {
    if (password_needs_rehash($hash, PASSWORD_DEFAULT)) {      // migrer vers un meilleur algorithme au fil des connexions
        $nouveau = password_hash($saisie, PASSWORD_DEFAULT);
        // … mise à jour en base
    }
    session_regenerate_id(true);
    // connecté
}
```

- La colonne en base doit pouvoir contenir **255 caractères** (`VARCHAR(255)`).
- Imposez une longueur minimale (12 caractères conseillés), vérifiez les mots de passe compromis (API *Have I Been Pwned*), **limitez les tentatives** (*rate limiting*), proposez l'**authentification à deux facteurs** et les **passkeys** (WebAuthn).
- Message de connexion **identique** que l'e-mail ou le mot de passe soit faux (évite l'énumération de comptes).

## 16.5 Aléatoire et jetons

```php
random_bytes(32);                       // octets cryptographiquement sûrs
bin2hex(random_bytes(16));              // jeton hexadécimal
random_int(100000, 999999);             // entier sûr (codes à usage unique)
// ❌ rand(), mt_rand(), uniqid() : prévisibles, pas pour la sécurité
```

## 16.6 Téléversements sécurisés (rappel)

Taille limitée · type **réel** (`finfo`) · nom **aléatoire** · dossier **hors de la racine web** ou exécution PHP interdite · jamais de confiance dans l'extension ou le type MIME envoyés par le navigateur. Voir [section 10.6](#106-téléversement-sécurisé-de-fichiers).

## 16.7 HTTPS et en-têtes de sécurité

```php
// Forcer HTTPS (mieux vaut le faire au niveau du serveur web / proxy)
if (empty($_SERVER['HTTPS']) || $_SERVER['HTTPS'] === 'off') {
    header('Location: https://' . $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI'], true, 301);
    exit;
}

header('Strict-Transport-Security: max-age=31536000; includeSubDomains');   // HSTS
header('X-Content-Type-Options: nosniff');
header('X-Frame-Options: DENY');                                           // ou CSP : frame-ancestors 'none'
header('Referrer-Policy: strict-origin-when-cross-origin');
header('Permissions-Policy: camera=(), microphone=(), geolocation=()');
```

> ⚠️ `$_SERVER['HTTP_HOST']` est fourni par le client : utilisez un **nom de domaine fixe** issu de la configuration.

## 16.8 Configuration et déploiement sûrs

| Réglage | Valeur recommandée en production |
| --- | --- |
| `display_errors` | `Off` |
| `expose_php` | `Off` |
| `allow_url_include` | `Off` |
| `session.cookie_httponly`, `session.cookie_secure`, `session.use_strict_mode` | `1` |
| `disable_functions` | `exec, shell_exec, system, passthru, proc_open` si non nécessaires |
| `open_basedir` | Restreindre les dossiers accessibles |

- **Secrets** (clés d'API, mots de passe) dans des **variables d'environnement** ou un coffre-fort (jamais dans Git) ; `.env` hors de la racine web (bibliothèque `vlucas/phpdotenv`).
- Racine web = dossier **`public/`** seulement.
- **Mises à jour** régulières de PHP, du serveur et des dépendances ; `composer audit` détecte les vulnérabilités connues.
- Journalisez les événements de sécurité ; sauvegardez ; sécurisez l'accès administrateur (2FA, IP limitées).
- **Dépendances** : n'installez que des paquets maintenus ; verrouillez les versions (`composer.lock`).

## 16.9 Liste de contrôle

- [ ] Requêtes préparées partout
- [ ] Sortie HTML échappée
- [ ] Jeton CSRF sur chaque formulaire d'action
- [ ] `password_hash` / `password_verify`
- [ ] Sessions durcies et HTTPS
- [ ] Téléversements contrôlés
- [ ] Erreurs masquées, journaux actifs
- [ ] Secrets hors du dépôt
- [ ] Dépendances à jour (`composer audit`)

Référence : **OWASP Top 10** (<https://owasp.org/www-project-top-ten/>).

---

# 17. Composer et gestion des dépendances

## 17.1 Qu'est-ce que Composer ?

**Composer** est le **gestionnaire de dépendances** de PHP : il télécharge les bibliothèques déclarées dans `composer.json`, résout leurs versions, et génère un **autoloader**. Les paquets sont référencés sur **Packagist** (<https://packagist.org>).

### Installation

```bash
# Linux / macOS : voir https://getcomposer.org/download/ (script d'installation vérifié)
brew install composer         # macOS
winget install Composer.Composer   # Windows
composer --version
```

## 17.2 `composer.json`

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

## 17.3 Gérer les paquets

```bash
composer init                              # créer composer.json
composer require monolog/monolog           # ajouter une dépendance
composer require --dev phpunit/phpunit     # dépendance de développement
composer install                           # installer d'après composer.lock (reproductible)
composer update                            # mettre à jour dans les contraintes → met à jour composer.lock
composer update monolog/monolog            # un seul paquet
composer remove monolog/monolog
composer outdated                          # paquets obsolètes
composer audit                             # vulnérabilités connues ✅
composer show                              # liste des paquets
composer why-not php 8.5                   # pourquoi un paquet bloque une version
composer run test                          # exécuter un script
composer install --no-dev --optimize-autoloader    # production
```

### Contraintes de version (SemVer)

| Écriture | Signification |
| --- | --- |
| `^1.2` | `>= 1.2.0` et `< 2.0.0` (le plus courant) |
| `~1.2` | `>= 1.2.0` et `< 1.3.0`… (mineure fixée) |
| `1.2.*` | N'importe quel correctif de 1.2 |
| `>=1.2 <2.0` | Intervalle |
| `dev-main` | Branche de développement |

> ✅ **Versionnez `composer.lock`** (applications) pour que tous les environnements aient exactement les mêmes versions. Ne versionnez pas `vendor/`.

## 17.4 Chargement automatique

```php
<?php
require __DIR__ . '/vendor/autoload.php';       // une seule inclusion

use App\Service\Mailer;
$mailer = new Mailer();
```

Après avoir modifié la section `autoload` : `composer dump-autoload` (avec `-o` pour optimiser en production).

## 17.5 Créer et publier son propre paquet

1. Structure : `src/`, `tests/`, `composer.json`, `README.md`, licence.
2. `"name": "vendeur/paquet"`, `"autoload"` en PSR-4, `"require": {"php": "^8.2"}`.
3. Dépôt Git public avec des **tags SemVer** (`v1.0.0`).
4. Soumission sur Packagist ; webhook pour la mise à jour automatique.
5. Vérifiez : `composer validate`.

Paquet local pendant le développement :

```json
"repositories": [{ "type": "path", "url": "../mon-paquet" }]
```

## 17.6 Bonnes pratiques

- Exigez une **version de PHP** (`"php": "^8.3"`) dans `require`.
- Lancez régulièrement `composer audit` et `composer outdated`.
- Préférez des paquets **maintenus** et largement utilisés ; évitez les dépendances inutiles.
- Utilisez **PSR-4** et respectez les PSR (**PSR-1/12** style, **PSR-3** journaux, **PSR-7/17/18** HTTP, **PSR-11** conteneur).

---

# 18. Frameworks PHP

## 18.1 Pourquoi un framework ?

Un **framework** fournit une structure et des composants éprouvés : routage, accès aux données, gabarits, sécurité (CSRF, XSS, authentification), validation, tests, CLI.

| Avantage | Inconvénient |
| --- | --- |
| Productivité, conventions | Courbe d'apprentissage |
| Sécurité intégrée | Dépendance au framework |
| Architecture claire, tests facilités | Surcoût pour de très petits scripts |

Architecture courante : **MVC** (Modèle – Vue – Contrôleur).

## 18.2 Laravel

Le framework **le plus populaire** : syntaxe expressive, écosystème complet.

```bash
composer create-project laravel/laravel mon-app
cd mon-app
php artisan serve
```

```php
// routes/web.php
Route::get('/articles/{id}', [ArticleController::class, 'show']);

// app/Http/Controllers/ArticleController.php
class ArticleController extends Controller
{
    public function show(int $id)
    {
        return view('articles.show', ['article' => Article::findOrFail($id)]);
    }
}
```

| Fonctionnalité | Description |
| --- | --- |
| **Artisan** | CLI (`make:model`, `migrate`, `queue:work`…) |
| **Eloquent** | ORM (*Active Record*) |
| **Blade** | Moteur de gabarits |
| **Migrations / seeders** | Versionnement du schéma et jeux de données |
| **Files d'attente, planificateur, événements** | Tâches asynchrones |
| **Auth** | Kits de démarrage (Breeze, Jetstream), **Sanctum** (API), **Passport** (OAuth) |
| **Front** | Livewire, Inertia, Vite |
| **Performance** | Octane (FrankenPHP / Swoole / RoadRunner) |
| **Outils** | Sail (Docker), Pint (style), Forge / Cloud (déploiement) |

## 18.3 Symfony

Framework **modulaire** de niveau entreprise ; ses **composants** sont utilisés par Laravel, Drupal et d'autres.

```bash
composer create-project symfony/skeleton:"7.*" mon-app     # ou la dernière version stable
# Symfony CLI : symfony new mon-app --webapp
```

| Élément | Rôle |
| --- | --- |
| **Twig** | Moteur de gabarits |
| **Doctrine** | ORM (*Data Mapper*) |
| **Flex / Maker** | Recettes d'installation, génération de code |
| **Messenger, Mailer, HttpClient, Security, Console** | Composants indépendants |
| Versions LTS | Support long terme, adapté aux grands projets |

## 18.4 CodeIgniter 4

Framework **léger** et rapide à prendre en main, à faible empreinte.

```bash
composer create-project codeigniter4/appstarter mon-app
php spark serve
```

## 18.5 Slim (micro-framework)

Idéal pour des **API** et petits services.

```bash
composer require slim/slim slim/psr7
```

```php
<?php
use Slim\Factory\AppFactory;
require __DIR__ . '/vendor/autoload.php';

$app = AppFactory::create();
$app->get('/bonjour/{nom}', function ($request, $response, array $args) {
    $response->getBody()->write("Bonjour " . htmlspecialchars($args['nom']));
    return $response;
});
$app->run();
```

## 18.6 Comparaison

| Framework | Idéal pour | Courbe d'apprentissage | Points forts |
| --- | --- | --- | --- |
| **Laravel** | Applications web complètes, startups | Moyenne | Écosystème, productivité |
| **Symfony** | Grands projets, entreprise | Élevée | Modularité, stabilité, LTS |
| **CodeIgniter** | Petits projets, hébergement simple | Faible | Légèreté |
| **Slim** | API, microservices | Faible | Minimaliste, PSR-7 |
| **API Platform** | API REST/GraphQL | Moyenne | Génération d'API depuis le modèle (Symfony) |

Autres : **CakePHP**, **Yii**, **Laminas** ; CMS : **WordPress**, **Drupal**.

> 📌 Vérifiez toujours la **version actuelle** et la **version minimale de PHP** requise sur le site officiel de chaque framework avant de démarrer un projet.

---

# 19. Tests et qualité du code

## 19.1 Tests unitaires avec PHPUnit

```bash
composer require --dev phpunit/phpunit
vendor/bin/phpunit --version
```

`phpunit.xml` minimal :

```xml
<?xml version="1.0" encoding="UTF-8"?>
<phpunit bootstrap="vendor/autoload.php" colors="true">
    <testsuites>
        <testsuite name="Unit"><directory>tests</directory></testsuite>
    </testsuites>
</phpunit>
```

Classe à tester :

```php
// src/Calculatrice.php
namespace App;

class Calculatrice
{
    public function additionner(int $a, int $b): int { return $a + $b; }

    public function diviser(float $a, float $b): float
    {
        if ($b === 0.0) { throw new \InvalidArgumentException("Division par zéro"); }
        return $a / $b;
    }
}
```

Test :

```php
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

> ℹ️ Dans les versions récentes de PHPUnit, les **attributs** (`#[Test]`, `#[DataProvider]`) remplacent les annotations de commentaires (`@dataProvider`), dépréciées puis supprimées.

### Assertions courantes

`assertSame` (strict), `assertEquals`, `assertTrue`, `assertFalse`, `assertNull`, `assertCount`, `assertContains`, `assertInstanceOf`, `assertStringContainsString`, `expectException`.

## 19.2 Doublures (*mocks*)

Isoler la classe testée de ses dépendances :

```php
public function testEnvoiEmailInscription(): void
{
    $mailer = $this->createMock(MailerInterface::class);
    $mailer->expects($this->once())
           ->method('envoyer')
           ->with('alice@exemple.com')
           ->willReturn(true);

    $service = new InscriptionService($mailer);       // injection de dépendance
    $this->assertTrue($service->inscrire('alice@exemple.com'));
}
```

| Type | Rôle |
| --- | --- |
| **Stub** | Renvoie des valeurs prédéfinies |
| **Mock** | Vérifie les appels reçus |
| **Fake** | Implémentation simplifiée (ex. base en mémoire) |

Outils : **Mockery**, **Prophecy**. 💡 Programmez **vers des interfaces** et utilisez l'**injection de dépendances** pour rendre le code testable.

## 19.3 TDD (*Test-Driven Development*)

1. 🔴 **Rouge** : écrire un test qui échoue.
2. 🟢 **Vert** : écrire le code minimal pour le faire passer.
3. 🔵 **Refactoriser** : améliorer le code, tests toujours verts.

## 19.4 Autres outils *(ajout)*

| Besoin | Outils |
| --- | --- |
| Tests expressifs | **Pest** (au-dessus de PHPUnit) |
| **Analyse statique** | **PHPStan**, **Psalm** (détectent des bugs sans exécuter le code) |
| Style de code | **PHP-CS-Fixer**, **Laravel Pint**, PHP_CodeSniffer (PSR-12) |
| Modernisation automatique | **Rector** |
| Tests de bout en bout | Playwright, Laravel Dusk, Codeception |
| Tests d'API | Pest / PHPUnit + client HTTP, Postman, Bruno |
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

## 19.5 Bonnes pratiques

- Un test = **un comportement**, nom explicite, indépendant des autres.
- Respectez le schéma **Arrange – Act – Assert**.
- Testez les **cas limites** et les erreurs.
- N'utilisez pas de vraie base de données / réseau dans les tests unitaires.
- Lancez les tests **automatiquement** (CI).

---

# 20. Créer des API avec PHP

## 20.1 Principes REST

| Principe | Application |
| --- | --- |
| **Ressources** identifiées par des URL | `/api/utilisateurs/42` (noms au pluriel) |
| **Verbes HTTP** pour les actions | `GET`, `POST`, `PUT`, `PATCH`, `DELETE` |
| **Sans état** | Chaque requête contient tout le nécessaire (jeton) |
| **Codes de statut** significatifs | `200`, `201`, `204`, `400`, `401`, `403`, `404`, `422`, `429`, `500` |
| **Format** | JSON |

| Action | Méthode + URL | Succès |
| --- | --- | --- |
| Lister | `GET /api/utilisateurs` | `200` |
| Lire | `GET /api/utilisateurs/42` | `200` |
| Créer | `POST /api/utilisateurs` | `201` + `Location` |
| Remplacer | `PUT /api/utilisateurs/42` | `200` / `204` |
| Modifier | `PATCH /api/utilisateurs/42` | `200` |
| Supprimer | `DELETE /api/utilisateurs/42` | `204` |

## 20.2 JSON en PHP

```php
// Encoder
echo json_encode(['id' => 1, 'nom' => 'Alice'], JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR);

// Décoder
$data = json_decode($texte, true, 512, JSON_THROW_ON_ERROR);      // true : tableau associatif

// Corps d'une requête JSON
$brut = file_get_contents('php://input');
$donnees = json_decode($brut, true, 512, JSON_THROW_ON_ERROR);

// Objets : implémenter JsonSerializable
class Produit implements JsonSerializable {
    public function __construct(private int $id, private string $nom) {}
    public function jsonSerialize(): array { return ['id' => $this->id, 'nom' => $this->nom]; }
}

json_validate($texte);       // 8.3 : valide sans décoder
```

## 20.3 Un mini-routeur d'API en PHP pur

```php
<?php
declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');

function reponse(mixed $data, int $statut = 200): never {
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
        reponse($pdo->query("SELECT id, nom FROM utilisateurs")->fetchAll());
    }

    if ($chemin === '/api/utilisateurs' && $methode === 'POST') {
        $nom = trim((string) ($corps['nom'] ?? ''));
        if ($nom === '') reponse(['erreur' => 'Le nom est obligatoire.'], 422);
        $pdo->prepare("INSERT INTO utilisateurs (nom) VALUES (?)")->execute([$nom]);
        reponse(['id' => (int) $pdo->lastInsertId(), 'nom' => $nom], 201);
    }

    if (preg_match('#^/api/utilisateurs/(\d+)$#', $chemin, $m) && $methode === 'GET') {
        $stmt = $pdo->prepare("SELECT id, nom FROM utilisateurs WHERE id = ?");
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

## 20.4 API avec un framework

### Laravel

```php
// routes/api.php
Route::apiResource('articles', ArticleController::class)->middleware('auth:sanctum');

// Contrôleur
public function store(StoreArticleRequest $request): JsonResponse        // validation par FormRequest
{
    $article = Article::create($request->validated());
    return (new ArticleResource($article))->response()->setStatusCode(201);
}
```

### Slim

```php
$app->get('/api/articles', function ($req, $res) use ($pdo) {
    $res->getBody()->write(json_encode($pdo->query("SELECT * FROM articles")->fetchAll()));
    return $res->withHeader('Content-Type', 'application/json');
});
```

### Symfony / API Platform

Décrivez vos entités avec l'attribut `#[ApiResource]` : l'API REST, la documentation OpenAPI et la pagination sont générées.

## 20.5 Authentification et sécurité d'une API

| Mécanisme | Usage |
| --- | --- |
| **Jeton d'API / Bearer** | Services internes, applications simples |
| **JWT** | Jetons signés ; courte durée + jeton de rafraîchissement |
| **OAuth 2.0 / OpenID Connect** | Délégation d'accès, connexion via un fournisseur |
| **Sessions + cookies** | Applications web classiques (avec CSRF) |

À mettre en place :

- **HTTPS** obligatoire.
- **Validation stricte** des entrées (type, longueur, format) et réponse `422` détaillée.
- **Limitation du débit** (*rate limiting*, `429`).
- **CORS** configuré précisément (origines autorisées, jamais `*` avec des identifiants).
- **Pagination** (`?page=2&per_page=20`) et **filtres** ; ne pas exposer de données internes (IDs séquentiels sensibles, champs privés).
- **Versionnement** (`/api/v1/…`) et **documentation OpenAPI / Swagger**.
- Réponses d'erreur cohérentes (format **RFC 9457** *Problem Details* : `type`, `title`, `status`, `detail`).

```php
header('Access-Control-Allow-Origin: https://mon-front.exemple');
header('Access-Control-Allow-Methods: GET, POST, PUT, PATCH, DELETE, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, Authorization');
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') { http_response_code(204); exit; }     // requête de pré-vérification
```

## 20.6 Tester une API

- **curl** :

```bash
curl -X POST http://localhost:8000/api/utilisateurs \
     -H "Content-Type: application/json" \
     -d '{"nom":"Alice"}'
```

- **Postman**, **Bruno**, **Insomnia**, extension **REST Client** de VS Code.
- Tests automatisés (PHPUnit / Pest avec le client HTTP du framework).

---

# 21. Sujets avancés

## 21.1 Scripts en ligne de commande (CLI)

```php
#!/usr/bin/env php
<?php
declare(strict_types=1);

if (PHP_SAPI !== 'cli') { exit("Ce script s'exécute en ligne de commande.\n"); }

$options = getopt('n:v', ['nom:', 'verbeux']);              // -n Alice --verbeux
echo "Arguments : " . implode(', ', array_slice($argv, 1)) . PHP_EOL;

$saisie = trim((string) fgets(STDIN));                       // lecture au clavier
fwrite(STDERR, "Message d'erreur\n");                        // sortie d'erreur
exit(0);                                                     // code de sortie
```

```bash
php script.php Alice --verbeux
chmod +x script.php && ./script.php
```

Pour des commandes riches : **Symfony Console**, **Laravel Artisan**, **Laravel Prompts**. Planification : `cron` (`* * * * * php /chemin/script.php`).

## 21.2 Performance

| Levier | Détails |
| --- | --- |
| **OPcache** ✅ | Garde le bytecode en mémoire : **à activer en production** (`opcache.enable=1`, `opcache.validate_timestamps=0` avec redéploiement) |
| **JIT** | Utile pour du calcul intensif, peu d'effet sur les applications web classiques |
| **Preloading** | Précharge des classes au démarrage (`opcache.preload`) |
| **Serveurs d'application persistants** | **FrankenPHP**, **RoadRunner**, **Swoole / OpenSwoole** : application gardée en mémoire (Laravel Octane) |
| **Requêtes SQL** | Index, éviter le problème « N+1 », pagination, mise en cache |
| **Autoload optimisé** | `composer install --optimize-autoloader --classmap-authoritative` |
| **Mémoire** | Générateurs, traitement par lots (`chunk`), éviter de charger de gros tableaux |
| **Mesure** | **Xdebug** (profilage), **Blackfire**, **Tideways**, `microtime(true)`, `memory_get_peak_usage()` |

> 💡 **Mesurez avant d'optimiser** : le goulot d'étranglement est presque toujours la base de données ou les appels externes.

```php
$debut = microtime(true);
/* … code à mesurer … */
printf("%.3f s, %.1f Mo\n", microtime(true) - $debut, memory_get_peak_usage(true) / 1048576);
```

## 21.3 Stratégies de cache

| Niveau | Technique |
| --- | --- |
| **Code** | OPcache |
| **Données en mémoire locale** | **APCu** (cache par serveur) |
| **Cache distribué** | **Redis**, **Memcached** |
| **Fichiers** | Cache sur disque (pages générées, résultats lourds) |
| **HTTP** | En-têtes `Cache-Control`, `ETag`, `Last-Modified` ; **CDN** (Cloudflare, Fastly) |
| **Applicatif (framework)** | Laravel `Cache::remember()`, PSR-6 / **PSR-16** (`symfony/cache`) |

```php
function lireAvecCache(string $cle, int $ttl, callable $calcul): mixed
{
    $valeur = apcu_fetch($cle, $trouve);
    if ($trouve) return $valeur;

    $valeur = $calcul();
    apcu_store($cle, $valeur, $ttl);
    return $valeur;
}
```

- Définissez toujours une **durée de vie** (TTL) et une stratégie d'**invalidation** (« il n'y a que deux problèmes difficiles en informatique… »).
- Protégez-vous contre l'**effet de ruée** (*cache stampede*) : verrous, TTL avec variation aléatoire.

## 21.4 Redis et Memcached

```bash
# Extension native phpredis ou bibliothèque Predis
composer require predis/predis
```

```php
$redis = new Predis\Client(['scheme' => 'tcp', 'host' => '127.0.0.1', 'port' => 6379]);

$redis->setex('utilisateur:42', 3600, json_encode($utilisateur));     // avec expiration
$utilisateur = json_decode($redis->get('utilisateur:42') ?? 'null', true);
$redis->incr('visites');                                               // compteur atomique
$redis->del('utilisateur:42');
```

| Usage de Redis | Détails |
| --- | --- |
| **Cache** | Clé/valeur avec TTL |
| **Sessions** | `session.save_handler = redis` (partage entre serveurs) |
| **Files d'attente** | Laravel Queues, Symfony Messenger |
| **Limitation de débit** | Compteurs avec expiration |
| **Pub/Sub** | Messages en temps réel |

**Memcached** : plus simple (clé/valeur uniquement, sans persistance), utile pour du cache pur. **Redis** : structures de données riches (listes, ensembles, hachages), persistance, publication/abonnement.

## 21.5 WebSockets et temps réel

PHP traite une requête puis s'arrête : pour des connexions **persistantes** (chat, notifications), il faut un **processus long** :

| Solution | Description |
| --- | --- |
| **Ratchet** (ReactPHP) | Serveur WebSocket en PHP |
| **Swoole / OpenSwoole**, **Workerman** | Serveurs asynchrones hautes performances |
| **Laravel Reverb**, **Soketi**, **Pusher** | Diffusion d'événements intégrée à Laravel |
| **Mercure** (Symfony) | Push via **SSE** (*Server-Sent Events*) |

```php
// Ratchet (extrait)
use Ratchet\MessageComponentInterface;
use Ratchet\ConnectionInterface;

class Chat implements MessageComponentInterface
{
    protected \SplObjectStorage $clients;
    public function __construct() { $this->clients = new \SplObjectStorage; }
    public function onOpen(ConnectionInterface $c) { $this->clients->attach($c); }
    public function onMessage(ConnectionInterface $de, $msg) {
        foreach ($this->clients as $client) { if ($client !== $de) $client->send($msg); }
    }
    public function onClose(ConnectionInterface $c) { $this->clients->detach($c); }
    public function onError(ConnectionInterface $c, \Exception $e) { $c->close(); }
}
```

Dans la majorité des cas, les **SSE** ou l'**interrogation périodique** (*polling*) suffisent.

## 21.6 Programmation asynchrone et *fibers* *(8.1)*

Les **Fibers** permettent de suspendre / reprendre l'exécution et servent de socle à des bibliothèques asynchrones (**Revolt**, **AMPHP**, **ReactPHP**) :

```php
$fibre = new Fiber(function (): void {
    $valeur = Fiber::suspend('pause');
    echo "Reprise avec $valeur\n";
});
echo $fibre->start();           // "pause"
$fibre->resume('hello');
```

## 21.7 Autres sujets utiles

- **Files d'attente** et tâches de fond (Laravel Queues, Symfony Messenger, RabbitMQ).
- **Internationalisation** : extension `intl`, `gettext`, fichiers de traduction des frameworks.
- **Manipulation d'images** : GD, Imagick, Intervention Image.
- **PDF / Excel** : Dompdf, TCPDF, PhpSpreadsheet.
- **Déploiement** : Docker, Nginx + PHP-FPM, FrankenPHP, plateformes (Forge, Fly.io, plateformes PaaS) ; intégration continue.
- **`php.ini`** : `memory_limit`, `max_execution_time`, `upload_max_filesize`, `date.timezone`, `opcache.*`.

---

# 22. Nouveautés par version et aide-mémoire

## 22.1 Chronologie des fonctionnalités

| Version | Fonctionnalités marquantes |
| --- | --- |
| **7.0** | Déclarations de types scalaires, opérateur `<=>` et `??`, classes anonymes, performances ×2 |
| **7.4** | Fonctions fléchées, propriétés typées, `??=`, opérateur de décomposition dans les tableaux |
| **8.0** | **Arguments nommés**, **attributs**, **promotion de propriétés**, **types union**, **`match`**, **opérateur null-safe `?->`**, `str_contains`, JIT, `mixed`, `throw` expression |
| **8.1** | **Énumérations**, propriétés **`readonly`**, **Fibers**, callables de première classe `f(...)`, types intersection, `never`, `new` dans les initialiseurs, `array_is_list` |
| **8.2** | Classes **`readonly`**, types DNF, types `null` / `false` / `true` autonomes, `#[\SensitiveParameter]`, extension Random |
| **8.3** | **Constantes de classe typées**, `#[\Override]`, `json_validate()`, accès dynamique aux constantes de classe `Classe::{$nom}` |
| **8.4** | **Hooks de propriétés**, **visibilité asymétrique** (`private(set)`), `new Classe()->méthode()` sans parenthèses, `#[\Deprecated]`, `array_find/any/all`, objets paresseux, nouvelle API DOM HTML5, `mb_trim` |
| **8.5** | **Opérateur pipe `\|>`**, **extension URI**, `#[\NoDiscard]`, `clone` avec modification de propriétés, `array_first()` / `array_last()` |
| **8.6** | En test (bêta) à la date de rédaction : consultez les notes de version officielles |

> 📌 Pour les détails exacts de chaque version : **php.net → Migration guides** ([php.net/manual/fr/appendices.php](https://www.php.net/manual/fr/appendices.php)).

## 22.2 Fonctions et pratiques dépréciées ou supprimées

| À ne plus utiliser | Remplacement |
| --- | --- |
| `mysql_*` | **PDO** / MySQLi |
| `FILTER_SANITIZE_STRING` | `htmlspecialchars()` + validation |
| `md5()`, `sha1()` pour les mots de passe | `password_hash()` |
| `rand()`, `mt_rand()`, `uniqid()` en sécurité | `random_int()`, `random_bytes()` |
| `create_function()`, `each()` | Fonctions anonymes, `foreach` |
| `register_globals`, `magic_quotes` | Supprimés depuis longtemps |
| `eval()` | À proscrire |
| `@` (suppression d'erreurs) | Gestion explicite des erreurs |
| `$_REQUEST` | `$_GET` / `$_POST` explicites |
| `unserialize()` sur des entrées externes | `json_decode()` |
| Propriétés dynamiques (dépréciées en 8.2) | Déclarer les propriétés / `#[\AllowDynamicProperties]` |
| Paramètre implicitement nullable `Type $x = null` (déprécié en 8.4) | `?Type $x = null` |

## 22.3 Récapitulatif par besoin

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

## 22.4 Ressources

- 📘 **Manuel officiel** : <https://www.php.net/manual/fr/>
- 📗 **PHP : la bonne méthode** (*PHP The Right Way*) : <https://phptherightway.com>
- 📜 **PHP-FIG (PSR)** : <https://www.php-fig.org>
- 🔒 **OWASP PHP Cheat Sheets** : <https://cheatsheetseries.owasp.org>
- 📦 **Packagist** : <https://packagist.org>
- 🧪 **3v4l.org** : exécuter un code sur toutes les versions de PHP

---

<div align="center">

*Bon développement ! 🐘*

</div>
