<div align="center">

# PHP — Guide complet

**Des bases du langage aux API, à la sécurité et aux frameworks modernes**

*Mis à jour pour PHP 8.5 (octobre 2026)*

</div>

---

## Sommaire

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

> **Légende** : *(ajout)* = notion absente du guide d'origine ; *(à jour)* = pratique moderne remplaçant une ancienne ; *(8.x)* = version de PHP qui introduit la fonctionnalité. Dans les exemples de code, `echo` affiche les résultats et `fwrite(STDERR, …)` affiche les erreurs.

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

> **Attention :** **PHP 8.1 et antérieures ne reçoivent plus aucun correctif de sécurité.** Pour un nouveau projet, utilisez **PHP 8.4 ou 8.5**. Consultez [php.net/supported-versions](https://www.php.net/supported-versions.php).

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
$variable = "Bonjour";
?>
<p>HTML ici</p>
<p><?= $variable ?></p>
<p><?php echo $variable; ?></p>
```

`<?= $variable ?>` est le raccourci de `<?php echo $variable; ?>`.

> **Bonne pratique :** Dans un fichier contenant **uniquement du PHP**, **omettez la balise fermante `?>`** : cela évite l'envoi accidentel d'espaces ou de sauts de ligne avant les en-têtes HTTP.

## 2.2 Instructions et commentaires

Chaque instruction se termine par **`;`**. PHP est **insensible à la casse** pour les mots-clés et fonctions, mais **sensible à la casse pour les variables** (`$nom` ≠ `$Nom`).

```php
<?php
// Commentaire sur une ligne
# Autre commentaire sur une ligne
/* Commentaire
   sur plusieurs lignes */
/** Commentaire de documentation (PHPDoc) */

$nom = "Alice";
$Nom = "Bob";                 // variable différente : sensibilité à la casse
ECHO "$nom et $Nom" . PHP_EOL; // echo, ECHO ou Echo : mots-clés insensibles à la casse
```

## 2.3 Typage strict *(ajout, à jour)*

Placez en **première ligne** de chaque fichier :

```php
<?php
declare(strict_types=1);

function addition(int $a, int $b): int
{
    return $a + $b;
}

echo addition(2, 3), PHP_EOL;            // affiche : 5

try {
    echo addition("5", 3);               // "5" est une chaîne : refusée en mode strict
} catch (TypeError $e) {
    fwrite(STDERR, "Erreur : " . $e->getMessage() . PHP_EOL);
}
```

Avec le typage strict, `addition("5", 3)` lève une `TypeError` au lieu de convertir silencieusement.

## 2.4 Afficher : `echo` et `print`

```php
<?php
$tableau = ["a" => 1, "b" => [2, 3]];
$valeur = 42;
$nom = "Alice";
$age = 30;

echo "Bonjour", PHP_EOL;
echo "A", "B", "C", PHP_EOL;              // plusieurs arguments possibles : ABC
$retour = print "Bonjour" . PHP_EOL;      // print renvoie toujours 1 (rarement utile)
echo $retour, PHP_EOL;
print_r($tableau);                        // affichage lisible
var_dump($valeur);                        // type + valeur (débogage) : int(42)
var_export($tableau);                     // représentation PHP valide
echo PHP_EOL;
printf("%s a %d ans" . PHP_EOL, $nom, $age);
echo sprintf("%s a %d ans", $nom, $age), PHP_EOL;
```

`printf("%s a %d ans", $nom, $age)` et `sprintf()` formatent du texte.

## 2.5 Variables

Elles commencent par **`$`** ; aucune déclaration de type obligatoire.

```php
<?php
$nom = "Alice";
$age = 30;
$taille = 1.68;
$actif = true;

echo "$nom, $age ans, $taille m, actif : ", var_export($actif, true), PHP_EOL;
// affiche : Alice, 30 ans, 1.68 m, actif : true
```

Règles : lettres, chiffres, `_`, sans commencer par un chiffre. Convention : **`$camelCase`** (ou `snake_case`, mais restez cohérent ; PSR-12 conseille camelCase).

```php
<?php
$a = 1;
$b = &$a;                    // référence : $b et $a désignent la même valeur
$b = 2;
echo "a = $a, b = $b", PHP_EOL;          // affiche : a = 2, b = 2

$nomVariable = "x";
$$nomVariable = 5;           // variable variable → $x (à éviter)
echo $x, PHP_EOL;                         // affiche : 5
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
<?php
$x = "texte";
$y = 42;

echo gettype($x), " / ", gettype($y), PHP_EOL;                 // string / integer
echo get_debug_type($x), " / ", get_debug_type($y), PHP_EOL;   // string / int (8.0)

var_dump(is_int($y), is_string($y), is_array($y), is_null($y), is_numeric("12.5"));
// bool(true) bool(false) bool(false) bool(false) bool(true)

var_dump(isset($x));        // défini et non null ? bool(true)
var_dump(empty($x));        // vide ? bool(false)
var_dump(empty("0"));       // vide ? ("", 0, "0", [], null, false) : bool(true)
```

### Valeurs « fausses » (*falsy*)

`false`, `0`, `0.0`, `""`, `"0"`, `[]`, `null`. Tout le reste est « vrai ».

## 2.7 Conversion de types (*casting*)

```php
<?php
$n = (int) "42abc";         var_dump($n);       // int(42)
$f = (float) "3.14";        var_dump($f);       // float(3.14)
$s = (string) 123;          var_dump($s);       // string(3) "123"
$b = (bool) "0";            var_dump($b);       // bool(false)
$t = (array) "a";           print_r($t);        // Array ( [0] => a )

var_dump(intval("12"), floatval("1.5"), strval(5), boolval(1));
```

## 2.8 Constantes

```php
<?php
define("TVA", 0.2);                  // à l'exécution
const NOM_SITE = "MonSite";          // à la compilation (préféré)

echo TVA, " ", NOM_SITE, PHP_EOL;    // affiche : 0.2 MonSite

class Config { const VERSION = "1.0"; }
echo Config::VERSION, PHP_EOL;       // affiche : 1.0

echo basename(__FILE__), " ligne ", __LINE__, PHP_EOL;   // constantes magiques
```

Constantes magiques : `__FILE__`, `__DIR__`, `__LINE__`, `__FUNCTION__`, `__CLASS__`, `__METHOD__`, `__NAMESPACE__`.

## 2.9 Interpolation de chaînes

```php
<?php
$nom = "Alice";
$utilisateur = ['age' => 30];

echo "Bonjour $nom !", PHP_EOL;                       // guillemets doubles : variables interprétées
echo "Âge : {$utilisateur['age']}", PHP_EOL;          // expressions complexes entre accolades
echo 'Bonjour $nom', PHP_EOL;                         // guillemets simples : texte brut
```

## 2.10 Portée et superglobales

Une variable définie hors fonction n'est **pas visible** dans les fonctions (voir [section 5](#5-fonctions)). Les **superglobales** sont accessibles partout :

| Superglobale | Contenu |
| --- | --- |
| `$_GET` | Paramètres de l'URL |
| `$_POST` | Données de formulaire (corps de la requête) |
| `$_REQUEST` | GET + POST + COOKIE (à éviter) |
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
<?php
$x = 5;
$x += 2;  echo $x, PHP_EOL;    // 7
$x -= 1;  echo $x, PHP_EOL;    // 6
$x *= 3;  echo $x, PHP_EOL;    // 18
$x /= 2;  echo $x, PHP_EOL;    // 9
$x %= 4;  echo $x, PHP_EOL;    // 1
$x **= 2; echo $x, PHP_EOL;    // 1

$s = "début";
$s .= " fin";                  // concaténation
echo $s, PHP_EOL;              // début fin

$y ??= "défaut";               // affecte seulement si $y est null ou non défini (7.4)
echo $y, PHP_EOL;              // défaut
```

## 3.3 Comparaison

| Opérateur | Signification |
| --- | --- |
| `==` | Égal (valeurs, **avec conversion**) |
| `===` | **Identique** (valeur ET type), recommandé |
| `!=` `<>` | Différent |
| `!==` | Non identique |
| `<` `>` `<=` `>=` | Ordre |
| `<=>` | **Vaisseau spatial** : `-1`, `0` ou `1` |

```php
<?php
var_dump(0 == "a");        // bool(false) en PHP 8 (true avant !)
var_dump("1" == "01");     // bool(true)
var_dump("abc" == 0);      // bool(false) en PHP 8
var_dump(null == false);   // bool(true)
var_dump(0 === "0");       // bool(false)
var_dump(1 <=> 2);         // int(-1)
```

> **Bonne pratique :** Utilisez **`===`** par défaut. PHP 8 a rendu les comparaisons chaîne/nombre plus cohérentes, mais `==` reste source de surprises.

## 3.4 Logiques

| Opérateur | Rôle |
| --- | --- |
| `&&` ou `and` | ET |
| `\|\|` ou `or` | OU |
| `!` | NON |
| `xor` | OU exclusif |

> **Attention :** `and` / `or` ont une **priorité inférieure** à `=` : préférez `&&` et `||`.

## 3.5 Chaînes, incrément, tableaux

```php
<?php
$s = "Bonjour" . " " . "monde";       // concaténation .
echo $s, PHP_EOL;

$i = 5;
$i++; ++$i; $i--; --$i;               // incrémentation / décrémentation
echo $i, PHP_EOL;                      // 5

$a = [1, 2] + [3, 4, 5];              // union : [1, 2, 5] (les clés existantes de gauche gagnent)
print_r($a);

var_dump([0 => "a", 1 => "b"] == [1 => "b", 0 => "a"]);    // true : mêmes paires clé/valeur
var_dump([0 => "a", 1 => "b"] === [1 => "b", 0 => "a"]);   // false : l'ordre diffère
```

## 3.6 Opérateurs modernes *(à jour)*

```php
<?php
declare(strict_types=1);

// Fusion null  ??
$nom = $_GET['nom'] ?? "Invité";
echo $nom, PHP_EOL;                                  // Invité (aucun paramètre dans la console)

// Appel null-safe  ?->  (8.0)
$utilisateur = new stdClass();
$utilisateur->adresse = new stdClass();
$utilisateur->adresse->ville = "Lyon";
$inconnu = null;
echo $utilisateur?->adresse?->ville, PHP_EOL;        // Lyon
var_dump($inconnu?->adresse?->ville);                // NULL, sans erreur

// Ternaire et ternaire court
$age = 20;
$statut = $age >= 18 ? "majeur" : "mineur";
$entree = "";
$valeur = $entree ?: "défaut";                       // valeur si « vrai », sinon défaut
echo "$statut, $valeur", PHP_EOL;                    // majeur, défaut

// match (8.0) : comparaison STRICTE, retourne une valeur
$code = 404;
$libelle = match ($code) {
    200, 201 => "Succès",
    404      => "Introuvable",
    default  => "Erreur",
};
echo $libelle, PHP_EOL;                              // Introuvable

// Spread  ...
$a = [1, 2];
$b = [3, 4];
$tous = [...$a, ...$b];
echo implode(", ", $tous), PHP_EOL;                  // 1, 2, 3, 4
function somme(int ...$nombres) { return array_sum($nombres); }
echo somme(...$tous), PHP_EOL;                       // 10

// Pipe  |>  (8.5) : enchaîne les appels de gauche à droite
$slug = "  Bonjour Le Monde  "
    |> trim(...)
    |> strtolower(...)
    |> (fn($s) => str_replace(" ", "-", $s));
echo $slug, PHP_EOL;                                 // bonjour-le-monde
```

## 3.7 Priorité (extraits)

`**` → `++ --` → `!` → `* / %` → `+ -` → `.` (depuis PHP 8, `+`/`-` priment sur `.`) → `< <= > >=` → `== != === !==` → `&&` → `||` → `??` → `? :` → `=` → `and` → `xor` → `or`.

En cas de doute : **parenthèses**.

---

# 4. Structures de contrôle

## 4.1 Conditions

```php
<?php
$note = 14;

if ($note >= 16) {
    echo "Très bien";
} elseif ($note >= 10) {
    echo "Passable";
} else {
    echo "Insuffisant";
}
echo PHP_EOL;                      // affiche : Passable
```

### `switch` (comparaison souple)

```php
<?php
$jour = "samedi";

switch ($jour) {
    case "samedi":
    case "dimanche":
        echo "Week-end";
        break;
    default:
        echo "Semaine";
}
echo PHP_EOL;                      // affiche : Week-end
```

> **Bonne pratique :** Préférez **`match`** (comparaison stricte, pas de `break`, retourne une valeur, lève `UnhandledMatchError` si aucun cas).

### Syntaxe alternative (dans les gabarits HTML)

```php
<?php
$connecte = true;
$articles = [
    ['titre' => 'Premier article'],
    ['titre' => 'Deuxième article'],
];
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

## 4.2 Boucles

```php
<?php
for ($i = 0; $i < 5; $i++) { echo $i; }
echo PHP_EOL;                                   // 01234

$n = 0;
while ($n < 3) { $n++; }
echo $n, PHP_EOL;                               // 3

do { $n--; } while ($n > 0);
echo $n, PHP_EOL;                               // 0

foreach ([10, 20, 30] as $valeur) { echo $valeur, " "; }
echo PHP_EOL;                                   // 10 20 30
foreach (["a" => 1, "b" => 2] as $cle => $valeur) { echo "$cle=$valeur "; }
echo PHP_EOL;                                   // a=1 b=2

$tableau = [1, 2, 3];
foreach ($tableau as &$element) { $element *= 2; }   // par référence
unset($element);                                     // toujours détruire la référence après la boucle
echo implode(", ", $tableau), PHP_EOL;               // 2, 4, 6
```

## 4.3 `break`, `continue`

```php
<?php
for ($i = 0; $i < 10; $i++) {
    if ($i === 3) continue;      // itération suivante
    if ($i === 7) break;         // sortie de la boucle
    echo $i, " ";
}
echo PHP_EOL;                    // 0 1 2 4 5 6

$lignes = [[1, 2], [3, null, 5], [6, 7]];
foreach ($lignes as $numero => $ligne) {
    foreach ($ligne as $cellule) {
        if ($cellule === null) {
            echo "Ligne $numero ignorée", PHP_EOL;
            continue 2;          // saute à l'itération de la boucle EXTÉRIEURE
        }
    }
    echo "Ligne $numero complète", PHP_EOL;
}
```

## 4.4 Générateurs *(ajout)*

`yield` produit des valeurs **à la demande**, sans charger toute la collection en mémoire :

```php
<?php
function lireLignes(string $chemin): Generator {
    $f = fopen($chemin, 'r');
    while (($ligne = fgets($f)) !== false) {
        yield rtrim($ligne);
    }
    fclose($f);
}

$chemin = tempnam(sys_get_temp_dir(), 'demo');
file_put_contents($chemin, "ligne 1\nligne 2\nligne 3\n");

foreach (lireLignes($chemin) as $ligne) {
    echo $ligne, PHP_EOL;        // une seule ligne en mémoire à la fois
}
unlink($chemin);
```

## 4.5 Inclusion de fichiers

```php
<?php
// Préparation : deux petits fichiers dans le dossier temporaire
$dossier = sys_get_temp_dir();
file_put_contents($dossier . '/config.php', "<?php\nreturn ['site' => 'MonSite'];\n");
file_put_contents($dossier . '/outils.php', "<?php\nfunction bonjour(): string { return 'Bonjour'; }\n");

$config = require $dossier . '/config.php';       // erreur fatale si absent ; peut renvoyer une valeur
require_once $dossier . '/outils.php';            // une seule fois
require_once $dossier . '/outils.php';            // ignoré : déjà inclus
echo bonjour(), " sur ", $config['site'], PHP_EOL;    // Bonjour sur MonSite

include $dossier . '/optionnel.php';              // fichier absent : simple avertissement (Warning)
echo "Le script continue après l'avertissement", PHP_EOL;

unlink($dossier . '/config.php');
unlink($dossier . '/outils.php');
```

Utilisez `__DIR__` pour des chemins fiables, et **ne passez jamais une entrée utilisateur** à `include`/`require`.

---

# 5. Fonctions

## 5.1 Définir et appeler

```php
<?php
function saluer(string $nom): string {
    return "Bonjour $nom !";
}
echo saluer("Alice"), PHP_EOL;       // Bonjour Alice !
```

## 5.2 Paramètres

```php
<?php
function presenter(string $nom, int $age = 18, ?string $ville = null): string {
    return "$nom, $age ans" . ($ville ? " à $ville" : "");
}

echo presenter("Alice"), PHP_EOL;                           // Alice, 18 ans (valeurs par défaut)
echo presenter("Bob", 25, "Paris"), PHP_EOL;                // Bob, 25 ans à Paris
echo presenter(nom: "Chloé", ville: "Lyon"), PHP_EOL;       // arguments NOMMÉS (8.0) : Chloé, 18 ans à Lyon

function total(int ...$nombres): int { return array_sum($nombres); }    // variadique
echo total(1, 2, 3), PHP_EOL;                                           // 6
echo total(...[4, 5, 6]), PHP_EOL;                                      // 15 (déballage d'un tableau)

function ajouter(array &$liste, $x): void { $liste[] = $x; }            // passage par référence
$liste = [1, 2];
ajouter($liste, 3);
echo implode(", ", $liste), PHP_EOL;                                    // 1, 2, 3
```

> Par défaut, les arguments sont passés **par valeur** (les objets, par « poignée » : leur contenu reste modifiable).

## 5.3 Valeurs de retour

```php
<?php
function minMax(array $t): array { return [min($t), max($t)]; }
[$mini, $maxi] = minMax([3, 1, 4]);               // destructuration
echo "min = $mini, max = $maxi", PHP_EOL;         // min = 1, max = 4

function nePasRetourner(): void { echo "rien", PHP_EOL; }
nePasRetourner();

function arreter(): never { exit("Fin" . PHP_EOL); }   // ne retourne jamais (8.1)
arreter();
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
<?php
function trouver(array $liste, int|string $cle): mixed { return $liste[$cle] ?? null; }

var_dump(trouver(["a" => 1, 5 => "cinq"], "a"));    // int(1)
var_dump(trouver(["a" => 1, 5 => "cinq"], 5));      // string(4) "cinq"
var_dump(trouver(["a" => 1], "z"));                  // NULL
```

## 5.5 Portée des variables

```php
<?php
$global = "G";

function sansPortee(): void {
    echo $global;                 // variable hors portée : non définie ici
}

function avecGlobal(): void {
    global $global;               // possible, mais à éviter
    echo $global, PHP_EOL;        // G
    echo $GLOBALS['global'], PHP_EOL;   // G (idem)
}

function compteur(): int {
    static $n = 0;                // conservée entre les appels
    return ++$n;
}

// On convertit les avertissements en exceptions pour afficher l'erreur
set_error_handler(function (int $niveau, string $message): bool {
    throw new ErrorException($message, 0, $niveau);
});
try {
    sansPortee();
} catch (ErrorException $e) {
    fwrite(STDERR, "Erreur : " . $e->getMessage() . PHP_EOL);   // Undefined variable $global
}
restore_error_handler();

avecGlobal();
echo compteur(), compteur(), compteur(), PHP_EOL;               // 123
```

> **Bonne pratique :** Préférez **passer les valeurs en paramètres**. Les variables globales rendent le code difficile à tester.

## 5.6 Fonctions anonymes et fléchées

```php
<?php
$carre = function (int $x): int { return $x * $x; };
echo $carre(4), PHP_EOL;                                              // 16

$facteur = 3;
$multiplier = function ($x) use ($facteur) { return $x * $facteur; }; // use : capture par valeur
echo $multiplier(5), PHP_EOL;                                         // 15

$triple = fn($x) => $x * 3;      // fonction fléchée (7.4) : capture AUTOMATIQUEMENT les variables parentes (par valeur)
echo $triple(7), PHP_EOL;                                             // 21

echo implode(", ", array_map(fn($n) => $n * 2, [1, 2, 3])), PHP_EOL;  // 2, 4, 6
```

### Syntaxe de « callable de première classe » *(8.1)*

```php
<?php
class Outils
{
    public function majuscules(string $s): string { return strtoupper($s); }
    public static function fabrique(): string { return "fabriqué"; }
}

$longueur = strlen(...);                 // crée une Closure à partir d'une fonction existante
echo $longueur("bonjour"), PHP_EOL;      // 7

$objet = new Outils();
$methode = $objet->majuscules(...);
echo $methode("php"), PHP_EOL;           // PHP

$statique = Outils::fabrique(...);
echo $statique(), PHP_EOL;               // fabriqué
```

## 5.7 Récursivité

```php
<?php
function factorielle(int $n): int {
    return $n <= 1 ? 1 : $n * factorielle($n - 1);
}

echo factorielle(5), PHP_EOL;            // 120
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
<?php
// Indexé (clés 0, 1, 2…)
$fruits = ["pomme", "banane", "cerise"];

// Associatif (clés au choix)
$personne = ["nom" => "Alice", "age" => 30];

// Multidimensionnel
$utilisateurs = [
    ["nom" => "Alice", "age" => 30],
    ["nom" => "Bob",   "age" => 25],
];

echo $fruits[0], PHP_EOL;                        // pomme
echo $personne["nom"], PHP_EOL;                  // Alice
echo $utilisateurs[1]["nom"], PHP_EOL;           // Bob
```

> **Bonne pratique :** Utilisez la syntaxe courte `[]` plutôt que `array()`.

## 6.2 Ajouter, modifier, supprimer

```php
<?php
$fruits = ["pomme", "banane", "cerise"];
$personne = ["nom" => "Alice", "age" => 30];

$fruits[] = "fraise";                   // ajout à la fin
$fruits[1] = "kiwi";                    // modification
$personne["ville"] = "Paris";           // ajout d'une clé
unset($personne["age"]);                // suppression
echo implode(", ", $fruits), PHP_EOL;   // pomme, kiwi, cerise, fraise
echo json_encode($personne), PHP_EOL;   // {"nom":"Alice","ville":"Paris"}

array_push($fruits, "a", "b");          // ajoute à la fin
echo array_pop($fruits), PHP_EOL;       // retire et renvoie le dernier : b
array_unshift($fruits, "début");        // ajoute au début
echo array_shift($fruits), PHP_EOL;     // retire et renvoie le premier : début
echo implode(", ", $fruits), PHP_EOL;   // pomme, kiwi, cerise, fraise, a
```

## 6.3 Parcourir

```php
<?php
$fruits = ["pomme", "banane"];
$personne = ["nom" => "Alice", "age" => 30];
$utilisateurs = [
    ["nom" => "Alice", "age" => 30],
    ["nom" => "Bob",   "age" => 25],
];

foreach ($fruits as $indice => $fruit) { echo "$indice : $fruit\n"; }
foreach ($personne as $cle => $valeur) { echo "$cle = $valeur\n"; }

// Destructuration (avec clés)
['nom' => $nom, 'age' => $age] = $personne;
echo "$nom a $age ans\n";
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

> **Attention :** `in_array` et `array_search` : passez **`true`** en 3ᵉ argument pour une comparaison **stricte**.

## 6.5 Fonctions d'ordre supérieur

```php
<?php
$nombres = [1, 2, 3, 4, 5];

echo json_encode(array_map(fn($n) => $n * 2, $nombres)), PHP_EOL;                   // [2,4,6,8,10]
echo json_encode(array_filter($nombres, fn($n) => $n % 2 === 0)), PHP_EOL;          // {"1":2,"3":4} (clés conservées)
echo array_reduce($nombres, fn($somme, $n) => $somme + $n, 0), PHP_EOL;            // 15

array_walk($nombres, function (&$n) { $n *= 2; });                                  // modifie en place
echo json_encode($nombres), PHP_EOL;                                                // [2,4,6,8,10]
```

## 6.6 Trier

| Fonction | Tri |
| --- | --- |
| `sort()` / `rsort()` | Valeurs croissantes / décroissantes (réindexe) |
| `asort()` / `arsort()` | Valeurs, **conserve les clés** |
| `ksort()` / `krsort()` | Par clés |
| `usort($t, fn)` / `uasort` / `uksort` | Tri **personnalisé** |

```php
<?php
$utilisateurs = [
    ["nom" => "Chloé", "age" => 30],
    ["nom" => "Bob",   "age" => 25],
    ["nom" => "Alice", "age" => 30],
];

usort($utilisateurs, fn($a, $b) => $a['age'] <=> $b['age']);                                // par âge
echo implode(", ", array_column($utilisateurs, 'nom')), PHP_EOL;                            // Bob, Chloé, Alice

usort($utilisateurs, fn($a, $b) => [$a['age'], $a['nom']] <=> [$b['age'], $b['nom']]);      // critères multiples
echo implode(", ", array_column($utilisateurs, 'nom')), PHP_EOL;                            // Bob, Alice, Chloé
```

> Ces fonctions **modifient le tableau passé** (par référence) et renvoient un booléen ; le tri est **stable** depuis PHP 8.0.

## 6.7 Copie et références

Les tableaux sont copiés **par valeur** (avec copie différée : *copy-on-write*), contrairement aux objets.

```php
<?php
$a = [1, 2];
$b = $a;
$b[] = 3;                        // $a reste [1, 2]

echo implode(", ", $a), PHP_EOL;   // 1, 2
echo implode(", ", $b), PHP_EOL;   // 1, 2, 3
```

## 6.8 Parcours multidimensionnel

```php
<?php
$utilisateurs = [
    ["nom" => "Alice", "age" => 30],
    ["nom" => "Bob",   "age" => 25],
];

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
<?php
$nom = "Alice";

$simple = 'Texte $brut\n';                 // aucune interprétation (sauf \\ et \')
$double = "Bonjour $nom\n";                // variables et séquences d'échappement interprétées

$heredoc = <<<TEXTE
    Bonjour {$nom},
    Texte sur plusieurs lignes avec "guillemets".
    TEXTE;                                  // l'indentation de la fermeture est retirée (7.3)

$nowdoc = <<<'TEXTE'
    Aucune $interpolation ici.
    TEXTE;

echo $simple, PHP_EOL;
echo $double;
echo $heredoc, PHP_EOL;
echo $nowdoc, PHP_EOL;
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
<?php
var_dump(str_contains("Bonjour", "jour"));                  // bool(true)
echo substr("Bonjour", 0, 3), PHP_EOL;                      // Bon
echo str_replace("a", "o", "banane"), PHP_EOL;              // bonone
echo implode(", ", ["a", "b", "c"]), PHP_EOL;               // a, b, c
echo sprintf("%05.2f", 3.14159), PHP_EOL;                   // 03.14
echo number_format(1234567.891, 2, ',', ' '), PHP_EOL;      // 1 234 567,89
echo mb_strtoupper("élève"), PHP_EOL;                       // ÉLÈVE
echo ucfirst("alice"), PHP_EOL;                             // Alice

echo strlen("é"), " octets, ", mb_strlen("é"), " caractère", PHP_EOL;   // 2 octets, 1 caractère
```

> **Attention :** Avec du texte **UTF-8** (accents, emojis), utilisez les fonctions **`mb_*`** (extension `mbstring`) : `strlen("é")` vaut 2.

## 7.3 Traiter la saisie utilisateur

```php
<?php
// Simulation d'un envoi de formulaire (en ligne de commande, $_POST est vide)
$_POST = ['nom' => '  Alice Dupont  '];
$phrase = "un deux  trois";

$nom = trim($_POST['nom'] ?? '');
$nom = mb_substr($nom, 0, 50);                          // limiter la longueur
$mots = preg_split('/\s+/', $phrase, -1, PREG_SPLIT_NO_EMPTY);

echo "[$nom]", PHP_EOL;                                  // [Alice Dupont]
echo implode("|", $mots), PHP_EOL;                       // un|deux|trois
```

## 7.4 Échappement

```php
<?php
echo "Il a dit \"Salut\"", PHP_EOL;           // guillemets échappés
echo 'L\'été', PHP_EOL;                       // apostrophe échappée
echo "Chemin : C:\\dossier", PHP_EOL;         // antislash
```

## 7.5 Échapper pour la sortie : `htmlspecialchars`

**Toute donnée affichée en HTML doit être échappée** :

```php
<?php
$saisie = '<script>alert("piratage")</script>';

echo htmlspecialchars($saisie, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8'), PHP_EOL;
// &lt;script&gt;alert(&quot;piratage&quot;)&lt;/script&gt;
```

(Raccourci utile : définir `function e(string $s): string { return htmlspecialchars($s, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8'); }`.)

## 7.6 Comparer des chaînes

```php
<?php
$connu = hash('sha256', 'secret');
$saisi = hash('sha256', 'secret');

var_dump("abc" === "abc");                 // bool(true)
echo strcmp("a", "b"), PHP_EOL;            // -1 (< 0)
echo strcasecmp("A", "a"), PHP_EOL;        // 0 (insensible à la casse)
var_dump(hash_equals($connu, $saisi));     // bool(true) : comparaison à temps constant (jetons, signatures)
```

## 7.7 Chaînes et encodage

Enregistrez vos fichiers en **UTF-8**, servez `Content-Type: text/html; charset=UTF-8` et configurez `default_charset = "UTF-8"`. Pour convertir : `mb_convert_encoding()`. En 8.4+, `mb_trim`, `mb_ucfirst` et `mb_str_pad` existent.

---

# 8. Dates, heures et expressions régulières

*(Section ajoutée.)*

## 8.1 Dates et heures

Préférez les classes **`DateTimeImmutable`** (non mutable) et `DateTimeZone` aux fonctions `date()` / `strtotime()`.

```php
<?php
// Date figée pour que le résultat soit reproductible ; utilisez 'now' pour l'heure actuelle
$maintenant = new DateTimeImmutable('2026-10-11 14:30', new DateTimeZone('Europe/Paris'));
echo $maintenant->format('d/m/Y H:i'), PHP_EOL;                  // 11/10/2026 14:30

$dans30Jours = $maintenant->modify('+30 days');
echo $dans30Jours->format('d/m/Y'), PHP_EOL;                     // 10/11/2026

$date = DateTimeImmutable::createFromFormat('!d/m/Y', '25/12/2026', new DateTimeZone('Europe/Paris'));
$difference = $maintenant->diff($date);
echo $difference->days . " jours", PHP_EOL;                      // 74 jours

$autreFuseau = $maintenant->setTimezone(new DateTimeZone('Indian/Antananarivo'));
echo $autreFuseau->format('d/m/Y H:i'), PHP_EOL;                 // 11/10/2026 15:30

date_default_timezone_set('Europe/Paris');                       // fuseau par défaut du script
echo date_default_timezone_get(), PHP_EOL;                       // Europe/Paris
```

Pour l'**affichage localisé** : `IntlDateFormatter` (extension `intl`).

```php
<?php
// Nécessite l'extension intl
$maintenant = new DateTimeImmutable('2026-10-11 14:30', new DateTimeZone('Europe/Paris'));
$fmt = new IntlDateFormatter('fr_FR', IntlDateFormatter::FULL, IntlDateFormatter::SHORT, 'Europe/Paris');
echo $fmt->format($maintenant), PHP_EOL;       // dimanche 11 octobre 2026 à 14:30
```

> **Astuce :** Stockez les dates en **UTC** (ou `DATETIME` / `TIMESTAMP` côté base) et convertissez à l'affichage. Bibliothèque très utilisée : **Carbon**.

## 8.2 Expressions régulières (PCRE)

```php
<?php
$texte = "2026-10-11";

var_dump(preg_match('/^\d{4}-\d{2}-\d{2}$/', $texte));               // int(1) : correspondance
preg_match('/(?<annee>\d{4})-(?<mois>\d{2})/', "2026-10", $m);
echo $m['annee'], " / ", $m['mois'], PHP_EOL;                         // 2026 / 10
preg_match_all('/\d+/', "a1b22c333", $tous);
echo implode(", ", $tous[0]), PHP_EOL;                                // 1, 22, 333
echo preg_replace('/\s+/', ' ', "a   b    c"), PHP_EOL;               // a b c
echo preg_replace_callback('/\d+/', fn($m) => $m[0] * 2, "a1 b2"), PHP_EOL;   // a2 b4
echo implode("|", preg_split('/[\s,]+/', "a, b  c")), PHP_EOL;        // a|b|c

$saisie = "a.b*c";
echo preg_quote($saisie, '/'), PHP_EOL;                               // a\.b\*c (échappe une saisie utilisateur)
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
// traiter.php : à lancer avec « php -S localhost:8000 », puis envoyer le formulaire
if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    http_response_code(405);
    exit("Cette page attend une requête POST (envoyez le formulaire).");
}

$nom = trim($_POST['nom'] ?? '');
echo "Bonjour " . htmlspecialchars($nom, ENT_QUOTES, 'UTF-8');
```

## 9.2 `$_GET` ou `$_POST` ?

| | `$_GET` | `$_POST` |
| --- | --- | --- |
| Transmission | Dans l'**URL** (`?q=php&page=2`) | Dans le **corps** de la requête |
| Visible / mise en favori | Oui | Non |
| Taille | Limitée | Grande |
| Usage | **Lecture** : recherche, filtres, pagination (opérations sans effet de bord) | **Modification** : création, connexion, envoi de fichiers |
| Sécurité | Ne **jamais** y mettre de secrets | Pas plus sûr par nature : il faut **valider** et protéger contre le **CSRF** |

## 9.3 Validation

```php
<?php
// Simulation d'un envoi de formulaire (en ligne de commande, $_POST est vide)
$_POST = ['nom' => '', 'email' => 'pas-un-email', 'age' => '200'];

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
    echo "Formulaire valide : traitement, puis redirection", PHP_EOL;
} else {
    foreach ($erreurs as $champ => $message) {
        fwrite(STDERR, "$champ : $message" . PHP_EOL);
    }
}
```

Filtres utiles : `FILTER_VALIDATE_EMAIL`, `_INT`, `_FLOAT`, `_BOOLEAN`, `_URL`, `_IP`, `_REGEXP` ; lecture directe : `filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL)`.

> **Attention :** **`FILTER_SANITIZE_STRING` est déprécié depuis PHP 8.1** (et supprimé depuis). **Ne l'utilisez plus.** Principe actuel : **valider** à l'entrée, **échapper à la sortie** (`htmlspecialchars` pour le HTML, requêtes préparées pour SQL).

## 9.4 Validation côté client **et** côté serveur

Les attributs HTML (`required`, `type="email"`, `pattern`, `maxlength`) améliorent l'expérience mais **ne remplacent jamais** la validation serveur : n'importe qui peut envoyer une requête sans passer par votre formulaire.

## 9.5 Motif Post/Redirect/Get (PRG)

Évite le double envoi du formulaire lors d'un rechargement :

```php
<?php
// traiter.php : à lancer avec « php -S localhost:8000 »
declare(strict_types=1);
session_start();

function enregistrer(string $nom, string $email): void
{
    file_put_contents(__DIR__ . '/inscrits.csv', "$nom;$email\n", FILE_APPEND | LOCK_EX);
}

// GET : affichage du message flash laissé par la requête POST précédente
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    echo $_SESSION['flash'] ?? "Aucun message.";
    unset($_SESSION['flash']);
    exit;
}

$erreurs = [];
$nom = trim($_POST['nom'] ?? '');
$email = filter_var($_POST['email'] ?? '', FILTER_VALIDATE_EMAIL);
if ($nom === '') { $erreurs['nom'] = "Le nom est obligatoire."; }
if ($email === false) { $erreurs['email'] = "Adresse e-mail invalide."; }

if (!$erreurs) {
    enregistrer($nom, $email);
    $_SESSION['flash'] = "Enregistré !";
    header('Location: /traiter.php', true, 303);     // Post/Redirect/Get
    exit;
}

http_response_code(422);
foreach ($erreurs as $champ => $message) {
    echo "$champ : $message\n";
}
```

## 9.6 Pré-remplir un formulaire après erreur

```php
<?php
$nom = 'Alice <b>';
$erreurs = ['nom' => "Le nom est obligatoire."];
?>
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
<?php
$fichier = sys_get_temp_dir() . '/notes.txt';

file_put_contents($fichier, "Ligne\n");                                    // écrase
file_put_contents($fichier, "Suite\n", FILE_APPEND | LOCK_EX);             // ajoute, avec verrou

$contenu = file_get_contents($fichier);                                    // false en cas d'échec
echo $contenu;                                                             // Ligne / Suite

$lignes = file($fichier, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);   // tableau de lignes
print_r($lignes);

unlink($fichier);

if (!is_file($fichier)) {
    fwrite(STDERR, "Fichier introuvable : $fichier" . PHP_EOL);            // le fichier vient d'être supprimé
}
```

## 10.2 Lecture et écriture avec `fopen`

```php
<?php
$chemin = tempnam(sys_get_temp_dir(), 'donnees');
file_put_contents($chemin, "première ligne\n<b>seconde</b> ligne\n");

$f = fopen($chemin, 'r');
if ($f === false) { throw new RuntimeException("Ouverture impossible"); }

while (($ligne = fgets($f)) !== false) {      // ligne par ligne : économe en mémoire
    echo htmlspecialchars($ligne);
}
fclose($f);
unlink($chemin);

// Cas d'erreur : fichier inexistant
$absent = sys_get_temp_dir() . '/introuvable.txt';
try {
    if (!is_readable($absent)) {
        throw new RuntimeException("Ouverture impossible : $absent");
    }
    $f = fopen($absent, 'r');
} catch (RuntimeException $e) {
    fwrite(STDERR, "Erreur : " . $e->getMessage() . PHP_EOL);
}
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
<?php
$info = pathinfo('/var/www/photo.jpg');
print_r($info);
// ['dirname' => '/var/www', 'basename' => 'photo.jpg', 'extension' => 'jpg', 'filename' => 'photo']
```

## 10.4 CSV et JSON

```php
<?php
$dossier = sys_get_temp_dir();

// CSV : écrire
$f = fopen($dossier . '/sortie.csv', 'w');
fputcsv($f, ['nom', 'age'], ',', '"', '\\');
fputcsv($f, ['Alice', 30], ',', '"', '\\');
fclose($f);

// CSV : lire
if (($f = fopen($dossier . '/sortie.csv', 'r')) !== false) {
    $entete = fgetcsv($f, 0, ',', '"', '\\');
    while (($ligne = fgetcsv($f, 0, ',', '"', '\\')) !== false) {
        $personne = array_combine($entete, $ligne);
        print_r($personne);                              // ['nom' => 'Alice', 'age' => '30']
    }
    fclose($f);
}

// JSON
$donnees = ['nom' => 'Alice', 'villes' => ['Paris', 'Lyon']];
file_put_contents($dossier . '/data.json', json_encode($donnees, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR));
$relu = json_decode(file_get_contents($dossier . '/data.json'), true, 512, JSON_THROW_ON_ERROR);
echo $relu['villes'][1], PHP_EOL;                        // Lyon

// JSON invalide : avec JSON_THROW_ON_ERROR, l'erreur devient une exception
try {
    json_decode('{invalide', true, 512, JSON_THROW_ON_ERROR);
} catch (JsonException $e) {
    fwrite(STDERR, "Erreur JSON : " . $e->getMessage() . PHP_EOL);
}

unlink($dossier . '/sortie.csv');
unlink($dossier . '/data.json');
```

## 10.5 Classes SPL

```php
<?php
$chemin = tempnam(sys_get_temp_dir(), 'gros');
file_put_contents($chemin, "un\ndeux\ntrois\n");

$fichier = new SplFileObject($chemin);
foreach ($fichier as $numero => $ligne) {
    if ($ligne === '') { continue; }                     // dernière ligne vide
    echo ($numero + 1) . " : " . rtrim($ligne) . PHP_EOL;
}

unlink($chemin);
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
// upload.php : à lancer avec « php -S localhost:8000 » ; le formulaire ci-dessus envoie ici
declare(strict_types=1);

const DOSSIER = __DIR__ . '/../uploads';         // idéalement HORS de la racine web
const TAILLE_MAX = 2 * 1024 * 1024;              // 2 Mo
const TYPES_AUTORISES = ['image/jpeg' => 'jpg', 'image/png' => 'png', 'image/webp' => 'webp'];

function refuser(string $message, int $statut = 400): never
{
    http_response_code($statut);
    exit($message);
}

if (!is_dir(DOSSIER)) {
    mkdir(DOSSIER, 0755, true);
}

$fichier = $_FILES['photo'] ?? null;

if (!$fichier || $fichier['error'] !== UPLOAD_ERR_OK) {
    refuser("Erreur de téléversement (code " . ($fichier['error'] ?? '?') . ").");
}
if ($fichier['size'] > TAILLE_MAX) {
    refuser("Fichier trop volumineux.", 413);
}
if (!is_uploaded_file($fichier['tmp_name'])) {
    refuser("Fichier invalide.");
}

// Type RÉEL détecté par le contenu (et non par $_FILES['type'] ni l'extension, falsifiables)
$mime = (new finfo(FILEINFO_MIME_TYPE))->file($fichier['tmp_name']);
if (!isset(TYPES_AUTORISES[$mime])) {
    refuser("Type de fichier non autorisé.", 415);
}

// Nouveau nom aléatoire : on ne réutilise JAMAIS le nom d'origine
$nom = bin2hex(random_bytes(16)) . '.' . TYPES_AUTORISES[$mime];

if (!move_uploaded_file($fichier['tmp_name'], DOSSIER . '/' . $nom)) {
    refuser("Impossible d'enregistrer le fichier.", 500);
}
echo "Fichier enregistré : $nom";
```

Réglages `php.ini` : `file_uploads`, `upload_max_filesize`, `post_max_size`, `max_file_uploads`.

## 10.7 Précautions

- **Traversée de répertoires** : ne construisez jamais un chemin à partir d'une saisie brute (`../../etc/passwd`). Utilisez `basename()`, une **liste blanche**, et vérifiez `realpath()` :

```php
<?php
// Dossier d'envoi de démonstration
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

foreach (['photo.jpg', '../../etc/passwd', 'absent.png'] as $demande) {   // en pratique : $_GET['fichier']
    if (cheminSur($racine, $demande) === null) {
        fwrite(STDERR, "Refusé : $demande" . PHP_EOL);
    } else {
        echo "Accepté : $demande", PHP_EOL;
    }
}

unlink($racine . '/photo.jpg');
rmdir($racine);
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
echo $_SESSION['utilisateur'] ?? "Invité", PHP_EOL;      // Alice

unset($_SESSION['utilisateur']);              // retirer une variable
echo $_SESSION['utilisateur'] ?? "Invité", PHP_EOL;      // Invité
```

### Déconnexion complète

```php
<?php
session_start();
$_SESSION['utilisateur'] = "Alice";

$_SESSION = [];
if (ini_get('session.use_cookies')) {
    $p = session_get_cookie_params();
    setcookie(session_name(), '', ['expires' => time() - 42000, 'path' => $p['path'], 'domain' => $p['domain'],
                                   'secure' => $p['secure'], 'httponly' => $p['httponly'], 'samesite' => $p['samesite'] ?: 'Lax']);
}
session_destroy();
echo "Session détruite", PHP_EOL;
```

## 11.3 Cookies *(à jour : tableau d'options)*

```php
<?php
// cookie.php : à lancer avec « php -S localhost:8000 » ; rechargez la page pour lire le cookie
if (isset($_COOKIE['theme'])) {
    echo "Thème : ", htmlspecialchars($_COOKIE['theme']), PHP_EOL;     // lisible dès la REQUÊTE SUIVANTE
    setcookie('theme', '', ['expires' => time() - 3600, 'path' => '/']);   // supprimer
    exit;
}

setcookie('theme', 'sombre', [
    'expires'  => time() + 30 * 24 * 3600,     // 30 jours
    'path'     => '/',
    'secure'   => true,                        // HTTPS uniquement
    'httponly' => true,                        // inaccessible à JavaScript
    'samesite' => 'Lax',                       // protège du CSRF
]);
echo "Cookie envoyé : rechargez la page.", PHP_EOL;
```

> **Attention :** `setcookie()` doit être appelé **avant toute sortie** (sinon : *« headers already sent »*).
> **Sécurité :** Ne stockez jamais d'informations sensibles dans un cookie ; tout ce qu'il contient doit être considéré comme **modifiable par l'utilisateur**.

## 11.4 Sécuriser les sessions

```php
<?php
// Réglages recommandés (php.ini ou avant session_start)
ini_set('session.use_strict_mode', '1');
ini_set('session.use_only_cookies', '1');
session_set_cookie_params([
    'lifetime' => 0, 'path' => '/', 'secure' => true, 'httponly' => true, 'samesite' => 'Lax',
]);
session_start();

// À la connexion réussie : changer d'identifiant (anti fixation de session)
$utilisateur = ['id' => 42];                       // normalement lu en base après vérification du mot de passe
session_regenerate_id(true);
$_SESSION['user_id'] = $utilisateur['id'];
$_SESSION['derniere_activite'] = time();
echo "Connecté : utilisateur ", $_SESSION['user_id'], PHP_EOL;

// Expiration par inactivité (simulée : dernière activité il y a 31 minutes)
$_SESSION['derniere_activite'] = time() - 31 * 60;
if (isset($_SESSION['derniere_activite']) && time() - $_SESSION['derniere_activite'] > 1800) {
    session_unset();
    session_destroy();
    fwrite(STDERR, "Session expirée par inactivité" . PHP_EOL);
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

| | **PDO** (recommandé) | **MySQLi** |
| --- | --- | --- |
| Bases supportées | MySQL, MariaDB, PostgreSQL, SQLite, SQL Server… | MySQL / MariaDB uniquement |
| API | Orientée objet | Objet et procédural |
| Paramètres nommés (`:nom`) | Oui | Non (uniquement `?`) |
| Recommandation | **Standard actuel** | Acceptable pour du 100 % MySQL |

> **Supprimé :** Les anciennes fonctions `mysql_*` ont été **supprimées en PHP 7**.

## 12.2 Connexion avec PDO

```php
<?php
declare(strict_types=1);

// SQLite en mémoire par défaut, pour que l'exemple tourne sans serveur de base de données.
// Pour MySQL : DB_DSN="mysql:host=localhost;dbname=boutique;charset=utf8mb4" DB_USER=... DB_PASS=...
$dsn = getenv('DB_DSN') ?: 'sqlite::memory:';

try {
    $pdo = new PDO($dsn, getenv('DB_USER') ?: null, getenv('DB_PASS') ?: null, [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,    // erreurs → exceptions
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES   => false,                     // vraies requêtes préparées
    ]);
    echo "Connexion réussie", PHP_EOL;
} catch (PDOException $e) {
    error_log($e->getMessage());                                   // journaliser, ne pas afficher
    exit("Service momentanément indisponible.");
}
```

> **Sécurité :** Chargez les identifiants depuis des **variables d'environnement** (`getenv()`, `.env`), jamais dans le code versionné.

## 12.3 Requêtes préparées (anti-injection SQL)

**Règle absolue : n'insérez jamais une variable directement dans une requête SQL.**

```php
<?php
// Préparation : base SQLite en mémoire
$pdo = new PDO('sqlite::memory:', null, null, [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
]);
$pdo->exec("CREATE TABLE users (id INTEGER PRIMARY KEY, nom TEXT, email TEXT, actif INTEGER DEFAULT 1)");
$pdo->exec("INSERT INTO users (nom, email) VALUES ('Alice', 'alice@exemple.com'), ('Bob', 'bob@exemple.com')");

$email = "' OR '1'='1";          // saisie malveillante

// Vulnérable à l'injection SQL : la condition devient toujours vraie
$lignes = $pdo->query("SELECT * FROM users WHERE email = '$email'")->fetchAll();
echo count($lignes), " ligne(s) renvoyée(s) : l'injection a réussi", PHP_EOL;      // 2

// Requête préparée (paramètres nommés) : la saisie reste une simple valeur
$stmt = $pdo->prepare("SELECT id, nom, email FROM users WHERE email = :email AND actif = :actif");
$stmt->execute([':email' => $email, ':actif' => 1]);
var_dump($stmt->fetch());                                    // bool(false) : aucune ligne

$stmt->execute([':email' => 'alice@exemple.com', ':actif' => 1]);
print_r($stmt->fetch());                                     // une ligne (ou false)

// Paramètres positionnels
$stmt = $pdo->prepare("INSERT INTO users (nom, email) VALUES (?, ?)");
$stmt->execute(["Chloé", "chloe@exemple.com"]);
echo "Identifiant créé : ", $pdo->lastInsertId(), PHP_EOL;   // 3
```

Avec un type précis : `$stmt->bindValue(':id', $id, PDO::PARAM_INT);`.

### Clause `IN` dynamique

```php
<?php
// Préparation : base SQLite en mémoire
$pdo = new PDO('sqlite::memory:', null, null, [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
]);
$pdo->exec("CREATE TABLE produits (id INTEGER PRIMARY KEY, nom TEXT)");
$pdo->exec("INSERT INTO produits (nom) VALUES ('Stylo'), ('Cahier'), ('Règle')");

$ids = [1, 3];

$marqueurs = implode(',', array_fill(0, count($ids), '?'));
$stmt = $pdo->prepare("SELECT * FROM produits WHERE id IN ($marqueurs)");
$stmt->execute($ids);
foreach ($stmt->fetchAll() as $produit) {
    echo $produit['id'], " : ", $produit['nom'], PHP_EOL;     // 1 : Stylo, 3 : Règle
}
```

### Noms de tables / colonnes dynamiques

Les identifiants ne se paramètrent pas : utilisez une **liste blanche**.

```php
<?php
// Préparation : base SQLite en mémoire
$pdo = new PDO('sqlite::memory:', null, null, [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
]);
$pdo->exec("CREATE TABLE produits (id INTEGER PRIMARY KEY, nom TEXT, prix REAL, date TEXT)");
$pdo->exec("INSERT INTO produits (nom, prix, date) VALUES ('Stylo', 1.5, '2026-01-02'), ('Cahier', 3.2, '2026-01-01')");

$_GET['tri'] = 'prix; DROP TABLE produits';      // saisie malveillante simulée

$colonnesTriables = ['nom', 'prix', 'date'];
$tri = in_array($_GET['tri'] ?? '', $colonnesTriables, true) ? $_GET['tri'] : 'nom';   // liste blanche
echo "Tri appliqué : $tri", PHP_EOL;                                                     // nom

$stmt = $pdo->query("SELECT * FROM produits ORDER BY $tri");
foreach ($stmt as $produit) {
    echo $produit['nom'], PHP_EOL;                                                       // Cahier, Stylo
}
```

## 12.4 Opérations CRUD

```php
<?php
// Préparation : base SQLite en mémoire
$pdo = new PDO('sqlite::memory:', null, null, [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
]);
$pdo->exec("CREATE TABLE users (id INTEGER PRIMARY KEY, nom TEXT, email TEXT, actif INTEGER DEFAULT 1)");
$pdo->exec("INSERT INTO users (nom, email) VALUES ('Alice', 'alice@exemple.com'), ('Bob', 'bob@exemple.com')");

$nom = "Chloé";
$email = "chloe@exemple.com";

// CREATE
$stmt = $pdo->prepare("INSERT INTO users (nom, email) VALUES (:nom, :email)");
$stmt->execute([':nom' => $nom, ':email' => $email]);
$id = (int) $pdo->lastInsertId();

// READ
$tous = $pdo->query("SELECT id, nom FROM users ORDER BY nom")->fetchAll();
foreach ($tous as $u) { echo htmlspecialchars($u['nom']) . "<br>" . PHP_EOL; }

$stmt = $pdo->prepare("SELECT * FROM users WHERE id = ?");
$stmt->execute([$id]);
$user = $stmt->fetch();
echo $user['nom'], PHP_EOL;                                  // Chloé

// UPDATE
$stmt = $pdo->prepare("UPDATE users SET nom = :nom WHERE id = :id");
$stmt->execute([':nom' => "Chloé Martin", ':id' => $id]);
echo $stmt->rowCount() . " ligne(s) modifiée(s)", PHP_EOL;   // 1 ligne(s) modifiée(s)

// DELETE
$stmt = $pdo->prepare("DELETE FROM users WHERE id = ?");
$stmt->execute([$id]);
echo $stmt->rowCount() . " ligne(s) supprimée(s)", PHP_EOL;  // 1 ligne(s) supprimée(s)
```

Modes de récupération : `FETCH_ASSOC` (tableau associatif), `FETCH_OBJ`, `FETCH_CLASS` (hydrate une classe), `fetchColumn()`, `FETCH_KEY_PAIR`.

## 12.5 Transactions

Plusieurs opérations **toutes réussies ou toutes annulées** :

```php
<?php
// Préparation : deux comptes ; la contrainte CHECK interdit un solde négatif
$pdo = new PDO('sqlite::memory:', null, null, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
$pdo->exec("CREATE TABLE comptes (id INTEGER PRIMARY KEY, solde REAL CHECK (solde >= 0))");
$pdo->exec("INSERT INTO comptes (id, solde) VALUES (1, 50), (2, 10)");

function virement(PDO $pdo, int $de, int $vers, float $montant): void
{
    try {
        $pdo->beginTransaction();
        $pdo->prepare("UPDATE comptes SET solde = solde - ? WHERE id = ?")->execute([$montant, $de]);
        $pdo->prepare("UPDATE comptes SET solde = solde + ? WHERE id = ?")->execute([$montant, $vers]);
        $pdo->commit();
    } catch (Throwable $e) {
        if ($pdo->inTransaction()) { $pdo->rollBack(); }
        throw $e;
    }
}

virement($pdo, 1, 2, 20);                      // réussit : 30 et 30
echo json_encode($pdo->query("SELECT id, solde FROM comptes")->fetchAll(PDO::FETCH_ASSOC)), PHP_EOL;

try {
    virement($pdo, 1, 2, 100);                 // échoue : solde négatif, tout est annulé
} catch (PDOException $e) {
    fwrite(STDERR, "Virement annulé : " . $e->getMessage() . PHP_EOL);
}
echo json_encode($pdo->query("SELECT id, solde FROM comptes")->fetchAll(PDO::FETCH_ASSOC)), PHP_EOL;   // inchangé
```

## 12.6 MySQLi (rappel)

```php
<?php
// Nécessite l'extension mysqli et un serveur MySQL / MariaDB
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);          // exceptions

try {
    $conn = new mysqli('localhost', 'user', 'mdp', 'boutique');
    $conn->set_charset('utf8mb4');

    $email = 'alice@exemple.com';
    $stmt = $conn->prepare("SELECT id, nom FROM users WHERE email = ?");
    $stmt->bind_param('s', $email);          // s = string, i = int, d = double, b = blob
    $stmt->execute();
    $resultat = $stmt->get_result();
    while ($ligne = $resultat->fetch_assoc()) {
        echo $ligne['id'], " : ", $ligne['nom'], PHP_EOL;
    }
} catch (mysqli_sql_exception $e) {
    fwrite(STDERR, "Erreur MySQL : " . $e->getMessage() . PHP_EOL);
}
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
<?php
try {
    $resultat = intdiv(10, 0);
    echo $resultat;
} catch (DivisionByZeroError $e) {
    fwrite(STDERR, "Division par zéro : " . $e->getMessage() . PHP_EOL);
} catch (InvalidArgumentException | TypeError $e) {    // plusieurs types
    fwrite(STDERR, "Erreur d'argument : " . $e->getMessage() . PHP_EOL);
} catch (Throwable $e) {                                // filet de sécurité
    error_log((string) $e);
} finally {
    echo "Toujours exécuté (nettoyage)", PHP_EOL;
}
```

## 13.4 Lancer et créer des exceptions

```php
<?php
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

function retirer(float $solde, float $montant): float {
    if ($montant > $solde) {
        throw new SoldeInsuffisantException($montant - $solde);
    }
    return $solde - $montant;
}

try {
    echo diviser(10, 4), PHP_EOL;                        // 2.5
    echo diviser(1, 0), PHP_EOL;
} catch (InvalidArgumentException $e) {
    fwrite(STDERR, "Erreur : " . $e->getMessage() . PHP_EOL);
}

try {
    retirer(50, 80);
} catch (SoldeInsuffisantException $e) {
    fwrite(STDERR, $e->getMessage() . " (manque : " . $e->getManque() . ")" . PHP_EOL);
}

// Chaînage d'exceptions
try {
    try {
        json_decode('{invalide', true, 512, JSON_THROW_ON_ERROR);
    } catch (JsonException $e) {
        throw new RuntimeException("Impossible de lire la configuration.", 0, $e);   // $e->getPrevious()
    }
} catch (RuntimeException $e) {
    fwrite(STDERR, $e->getMessage() . " Cause : " . $e->getPrevious()->getMessage() . PHP_EOL);
}

// throw est une expression (8.0)
$x = null;
try {
    $valeur = $x ?? throw new InvalidArgumentException("x manquant");
} catch (InvalidArgumentException $e) {
    fwrite(STDERR, "Erreur : " . $e->getMessage() . PHP_EOL);
}
```

Méthodes utiles : `getMessage()`, `getCode()`, `getFile()`, `getLine()`, `getTraceAsString()`, `getPrevious()`.

## 13.5 Configuration et journalisation

```php
<?php
// Développement
error_reporting(E_ALL);
ini_set('display_errors', '1');

// Production : ne JAMAIS afficher les erreurs à l'utilisateur
ini_set('display_errors', '0');
ini_set('log_errors', '1');
$journal = sys_get_temp_dir() . '/app.log';        // en production : /var/log/php/app.log
ini_set('error_log', $journal);

error_log("Message à journaliser");
echo file_get_contents($journal);                  // [date] Message à journaliser
unlink($journal);
```

Dans `php.ini` : `error_reporting = E_ALL`, `display_errors = Off` (production), `log_errors = On`.

## 13.6 Gestionnaires globaux

```php
<?php
set_error_handler(function (int $niveau, string $message, string $fichier, int $ligne): bool {
    throw new ErrorException($message, 0, $niveau, $fichier, $ligne);     // convertit les erreurs en exceptions
});

set_exception_handler(function (Throwable $e): void {
    error_log((string) $e);                        // détails dans le journal
    http_response_code(500);
    echo "Une erreur est survenue.", PHP_EOL;      // message générique pour l'utilisateur
});

echo $variableInconnue;                            // avertissement → ErrorException → gestionnaire d'exceptions
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
echo $v->marque, " : ", $v->getKilometrage(), " km", PHP_EOL;     // Renault : 120 km
```

`$this` désigne l'objet courant ; `->` accède aux membres d'une instance ; `::` aux membres statiques et constantes.

## 14.2 Promotion de propriétés du constructeur *(8.0, à jour)*

```php
<?php
class Utilisateur
{
    public function __construct(
        public readonly int $id,              // lecture seule (8.1) : assignée une seule fois
        public string $nom,
        private ?string $email = null,
    ) {}
}

$u = new Utilisateur(1, "Alice");
echo $u->id, " ", $u->nom, PHP_EOL;           // 1 Alice

try {
    $u->id = 2;                               // propriété readonly : modification interdite
} catch (Error $e) {
    fwrite(STDERR, "Erreur : " . $e->getMessage() . PHP_EOL);
}

readonly class Point                          // classe readonly (8.2)
{
    public function __construct(public int $x, public int $y) {}
}
$p = new Point(1, 2);
echo $p->x, ",", $p->y, PHP_EOL;              // 1,2
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
<?php
class Compte {
    public private(set) float $solde = 0.0;     // lisible partout, modifiable seulement dans la classe (8.4)
    public function deposer(float $m): void { $this->solde += $m; }
}

$c = new Compte();
$c->deposer(50);
echo $c->solde, PHP_EOL;                         // 50

try {
    $c->solde = 1000;                            // écriture depuis l'extérieur : refusée
} catch (Error $e) {
    fwrite(STDERR, "Erreur : " . $e->getMessage() . PHP_EOL);
}
```

## 14.4 Hooks de propriétés *(8.4, à jour)*

Remplacent la plupart des getters/setters écrits à la main :

```php
<?php
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

$p = new Personne("Alice", "Martin");
echo $p->nomComplet, PHP_EOL;                  // Alice Martin

$p->email = "ALICE@Exemple.COM";
echo $p->email, PHP_EOL;                       // alice@exemple.com

try {
    $p->email = "pas-un-email";
} catch (InvalidArgumentException $e) {
    fwrite(STDERR, "Erreur : " . $e->getMessage() . PHP_EOL);
}
```

## 14.5 Héritage

```php
<?php
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

$rex = new Chien("Rex");
echo $rex->parler(), PHP_EOL;         // Rex dit : Ouaf !
echo $rex->presenter(), PHP_EOL;      // ... (parent)
```

- `final class` : ne peut pas être étendue ; `final function` : ne peut pas être redéfinie.
- `#[\Override]` *(8.3)* : vérifie qu'une méthode redéfinit bien une méthode parente.

## 14.6 Membres statiques et constantes

```php
<?php
class Compteur
{
    public const MAX = 100;                          // constante de classe
    public const string NOM = "Compteur";            // constante TYPÉE (8.3)
    private static int $total = 0;

    public static function incrementer(): int { return ++self::$total; }
}

Compteur::incrementer();
echo Compteur::incrementer(), PHP_EOL;               // 2
echo Compteur::MAX, " ", Compteur::NOM, PHP_EOL;     // 100 Compteur

// Liaison statique tardive : static:: (≠ self::)
class Modele { public static function creer(): static { return new static(); } }
class Article extends Modele {}

echo get_class(Article::creer()), PHP_EOL;           // Article (avec self, on obtiendrait Modele)
```

## 14.7 Classes abstraites, interfaces et traits

```php
<?php
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
echo $c->decrire(), PHP_EOL;                       // Aire : 12.57
echo $c->exporter(), PHP_EOL;                      // {"rayon":2}
echo $c->creeLe() instanceof DateTimeImmutable ? "créé" : "non créé", PHP_EOL;

try {
    $f = new Forme();                              // une classe abstraite ne s'instancie pas
} catch (Error $e) {
    fwrite(STDERR, "Erreur : " . $e->getMessage() . PHP_EOL);
}
```

| | Classe abstraite | Interface | Trait |
| --- | --- | --- | --- |
| Instanciable | Non | Non | Non |
| Héritage / implémentation multiple | Un seul parent | **Plusieurs** | Plusieurs traits |
| Contient du code | Oui | Non (signatures) | Oui |
| Propriétés | Oui | Non (constantes uniquement ; hooks depuis 8.4) | Oui |
| Rôle | Base commune | **Contrat** | **Réutilisation** de code |

## 14.8 Énumérations *(8.1, ajout)*

```php
<?php
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
echo $s->value, " ", $s->name, " ", $s->libelle(), PHP_EOL;     // publie Publie Publié
var_dump($t);                                                    // NULL
echo count(Statut::cases()), " cas", PHP_EOL;                    // 2 cas

try {
    Statut::from('inconnu');
} catch (ValueError $e) {
    fwrite(STDERR, "Erreur : " . $e->getMessage() . PHP_EOL);
}
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
<?php
class Prix implements Stringable
{
    public function __construct(private float $montant) {}
    public function __toString(): string { return number_format($this->montant, 2, ',', ' ') . ' €'; }
}

echo new Prix(12.5), PHP_EOL;       // 12,50 €
```

## 14.10 Objets : copie et comparaison

```php
<?php
class Voiture
{
    public function __construct(public string $marque) {}
}

$a = new Voiture("A");
$b = $a;              // même objet (poignée copiée)
$c = clone $a;        // copie superficielle ; __clone() permet de copier en profondeur

$b->marque = "B";
echo $a->marque, PHP_EOL;                 // B : $a et $b désignent le même objet
echo $c->marque, PHP_EOL;                 // A : $c est une copie indépendante

$d = clone $a;
var_dump($a == $d);                       // true : mêmes propriétés et même classe
var_dump($a === $d);                      // false : instances différentes
var_dump($a === $b);                      // true : même instance
var_dump($a instanceof Voiture);          // true

// (8.5) clone peut modifier des propriétés au passage, pratique pour les objets readonly
final class Coordonnees
{
    public function __construct(public readonly int $x, public readonly int $y) {}

    public function avecX(int $x): static { return clone($this, ['x' => $x]); }   // la modification se fait dans la classe
}
$decale = (new Coordonnees(0, 0))->avecX(5);
echo $decale->x, ",", $decale->y, PHP_EOL;     // 5,0
```

*(8.5)* `clone` peut modifier des propriétés au passage, pratique pour les objets `readonly` : `$b = clone($a, ['marque' => 'B']);`.

## 14.11 Attributs *(8.0, ajout)*

Métadonnées structurées, lues par réflexion, utilisées par les frameworks (routes, validation, ORM) :

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
    #[\Deprecated("Utiliser nouvelleMethode()")]          // 8.4
    public function liste(): string { return "liste des produits"; }
}

// Lecture des attributs par réflexion (c'est ce que font les frameworks)
$methode = new ReflectionMethod(Controleur::class, 'liste');
foreach ($methode->getAttributes(Route::class) as $attribut) {
    $route = $attribut->newInstance();
    echo $route->chemin, " ", implode(",", $route->methods), PHP_EOL;     // /produits GET
}
```

## 14.12 Espaces de noms et chargement automatique

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
    use InvalidArgumentException;                    // classe globale à importer
    use function strlen;                             // facultatif

    final class UtilisateurService
    {
        public function creer(string $nom): Utilisateur
        {
            if (strlen($nom) === 0) {
                throw new InvalidArgumentException("Nom vide");
            }
            return new Utilisateur(1, $nom);
        }
    }
}

namespace {
    use App\Service\UtilisateurService;

    $u = (new UtilisateurService())->creer("Alice");
    echo $u::class, " : ", $u->nom, PHP_EOL;         // App\Model\Utilisateur : Alice
}
```

**PSR-4** : le nom complet de la classe correspond au chemin du fichier (`App\Service\UtilisateurService` → `src/Service/UtilisateurService.php`). **Composer** génère l'autoloader (voir [section 17](#17-composer-et-gestion-des-dépendances)) :

```php
<?php
// Autoloader PSR-4 minimal : Composer génère l'équivalent dans vendor/autoload.php
// (avec Composer : require __DIR__ . '/vendor/autoload.php';)
$racine = sys_get_temp_dir() . '/psr4_demo';
if (!is_dir($racine . '/src/Service')) { mkdir($racine . '/src/Service', 0755, true); }
file_put_contents($racine . '/src/Service/UtilisateurService.php', <<<'CLASSE'
    <?php
    namespace App\Service;

    final class UtilisateurService
    {
        public function creer(string $nom): string { return "Utilisateur $nom créé"; }
    }
    CLASSE);

spl_autoload_register(function (string $classe) use ($racine): void {
    $prefixe = 'App\\';
    if (!str_starts_with($classe, $prefixe)) { return; }
    $fichier = $racine . '/src/' . str_replace('\\', '/', substr($classe, strlen($prefixe))) . '.php';
    if (is_file($fichier)) { require $fichier; }
});

echo (new App\Service\UtilisateurService())->creer("Alice"), PHP_EOL;     // Utilisateur Alice créé
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
// api.php : à lancer avec « php -S localhost:8000 » puis « curl -i http://localhost:8000/api.php »
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
http_response_code(201);                         // code de statut

header_remove('X-Powered-By');                   // masquer des informations inutiles

if (headers_sent($fichier, $ligne)) {
    exit("En-têtes déjà envoyés ($fichier:$ligne)");
}
echo json_encode(['cree' => true]);
```

> **Attention :** `header()` doit être appelé **avant toute sortie** (HTML, espace, BOM). Sinon : *« Cannot modify header information – headers already sent »*. Vérification : `headers_sent($fichier, $ligne)`.

### Lire les en-têtes de la requête

```php
<?php
// entetes.php : à lancer avec « php -S localhost:8000 »
$methode = $_SERVER['REQUEST_METHOD'] ?? 'CLI';
$agent   = $_SERVER['HTTP_USER_AGENT'] ?? '';
$autorisation = $_SERVER['HTTP_AUTHORIZATION'] ?? '';
$tousLesEntetes = function_exists('getallheaders') ? getallheaders() : [];   // selon l'environnement (PHP-FPM / Apache)

echo "Méthode : $methode", PHP_EOL;
echo "Agent : $agent", PHP_EOL;
echo "Nombre d'en-têtes reçus : ", count($tousLesEntetes), PHP_EOL;
```

## 15.2 Redirections

```php
<?php
// redirection.php : à lancer avec « php -S localhost:8000 » puis « curl -i http://localhost:8000/redirection.php »
header('Location: /tableau-de-bord.php', true, 302);
exit;                                            // toujours arrêter le script après
```

| Code | Usage |
| --- | --- |
| `301` | Redirection **permanente** |
| `302` / `307` | Temporaire |
| `303` | « Voir ailleurs » : après un POST (motif PRG) |

> **Sécurité :** **Ne redirigez jamais vers une URL provenant directement de l'utilisateur** (*open redirect*) : vérifiez-la par liste blanche ou n'acceptez que des chemins internes.

## 15.3 Télécharger un fichier

```php
<?php
// telecharger.php?f=rapport.txt : à lancer avec « php -S localhost:8000 »
$dossier = __DIR__ . '/fichiers';
if (!is_dir($dossier)) {
    mkdir($dossier);
    file_put_contents($dossier . '/rapport.txt', "Contenu du rapport\n");      // fichier de démonstration
}
$dossier = realpath($dossier);
$chemin  = realpath($dossier . '/' . basename($_GET['f'] ?? ''));

if ($chemin === false || !str_starts_with($chemin, $dossier . DIRECTORY_SEPARATOR)) {
    http_response_code(404);
    exit("Fichier introuvable.");
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
<?php
// Nécessite un serveur de messagerie local configuré (sendmail, msmtp…)
$ok = mail('dest@exemple.com', 'Sujet', "Corps du message", [
    'From' => 'noreply@monsite.fr',
    'Content-Type' => 'text/plain; charset=UTF-8',
]);

if ($ok) {
    echo "Message remis au serveur de messagerie", PHP_EOL;
} else {
    fwrite(STDERR, "Échec de l'envoi : aucun serveur de messagerie configuré" . PHP_EOL);
}
```

Limites : pas d'authentification SMTP, forte probabilité de classement en **spam**, peu de contrôle. **Sécurité** : **Injection d'en-têtes** : n'insérez jamais une saisie utilisateur non nettoyée dans `From`, `To` ou `Subject` (retours à la ligne).

### Bibliothèques (recommandé) : PHPMailer, Symfony Mailer

```bash
composer require phpmailer/phpmailer
```

```php
<?php
// Après « composer require phpmailer/phpmailer »
require __DIR__ . '/vendor/autoload.php';

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
    echo "Message envoyé", PHP_EOL;
} catch (Exception $e) {
    fwrite(STDERR, "Erreur d'envoi : " . $mail->ErrorInfo . PHP_EOL);
}
```

**Délivrabilité** : configurez **SPF, DKIM et DMARC** pour votre domaine, ou utilisez un service transactionnel (Mailgun, Postmark, Amazon SES, Brevo…). Envoyez les e-mails via une **file d'attente** pour ne pas ralentir la requête.

## 15.5 Requêtes HTTP sortantes

```php
<?php
// Requête cURL vers une API publique (nécessite l'extension curl et l'accès au réseau)
$jeton = getenv('API_JETON') ?: 'jeton-de-demonstration';

$ch = curl_init('https://api.github.com/zen');
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_TIMEOUT        => 10,
    CURLOPT_HTTPHEADER     => ['Accept: application/json', 'Authorization: Bearer ' . $jeton, 'User-Agent: guide-php'],
]);
$reponse = curl_exec($ch);

if ($reponse === false) {
    fwrite(STDERR, "Erreur cURL : " . curl_error($ch) . PHP_EOL);
} else {
    $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    echo "Code HTTP : $code", PHP_EOL;
    echo $reponse, PHP_EOL;
}
curl_close($ch);
```

Plus confortable : **Guzzle** ou **Symfony HttpClient** (`composer require guzzlehttp/guzzle`). Définissez toujours un **délai d'expiration**.

## 15.6 Utiliser l'URL

```php
<?php
$url = parse_url('https://exemple.com:8080/chemin?x=1#haut');
print_r($url);                                              // scheme, host, port, path, query, fragment

parse_str($url['query'], $parametres);
print_r($parametres);                                       // ['x' => '1']

echo http_build_query(['q' => 'café', 'page' => 2]), PHP_EOL;   // q=caf%C3%A9&page=2

$texte = "a b&c";
echo urlencode($texte), PHP_EOL;                            // a+b%26c
echo rawurlencode($texte), PHP_EOL;                         // a%20b%26c
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
<?php
// Simulation d'un envoi de formulaire (en ligne de commande)
$_POST = ['email' => 'alice@exemple.com'];
$saisie = '<img src=x onerror="alert(1)">';
$donnees = ['titre' => '</script><script>alert(1)</script>'];

// Validation
$email = filter_var($_POST['email'] ?? '', FILTER_VALIDATE_EMAIL);
var_dump($email);                                                           // string(17) "alice@exemple.com"

// Échappement à la SORTIE, selon le contexte
echo htmlspecialchars($saisie, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8'), PHP_EOL;      // HTML
echo json_encode($donnees, JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT), PHP_EOL;   // JSON dans du HTML
echo urlencode($saisie), PHP_EOL;                                                   // URL
// SQL : requêtes préparées (jamais d'échappement manuel)
```

> **Attention :** `FILTER_SANITIZE_STRING` est **supprimé** : n'utilisez ni lui ni `strip_tags()` comme protection XSS. `strip_tags` ne remplace pas `htmlspecialchars`.

### Protection XSS supplémentaire : Content Security Policy

```php
<?php
// csp.php : à lancer avec « php -S localhost:8000 » puis « curl -i http://localhost:8000/csp.php »
header("Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'self'");
echo "Page protégée par une politique CSP";
```

## 16.3 CSRF : falsification de requête inter-sites

```php
<?php
// Génération du jeton (une fois par session)
session_start();
if (empty($_SESSION['csrf'])) {
    $_SESSION['csrf'] = bin2hex(random_bytes(32));
}
echo "Jeton : ", $_SESSION['csrf'], PHP_EOL;
```

```php
<?php
session_start();
if (empty($_SESSION['csrf'])) {
    $_SESSION['csrf'] = bin2hex(random_bytes(32));
}
?>
<form method="post" action="supprimer.php">
    <input type="hidden" name="csrf" value="<?= htmlspecialchars($_SESSION['csrf']) ?>">
    <button>Supprimer</button>
</form>
```

```php
<?php
// supprimer.php : à lancer avec « php -S localhost:8000 »
session_start();

// Vérification
if (!hash_equals($_SESSION['csrf'] ?? '', $_POST['csrf'] ?? '')) {
    http_response_code(403);
    exit("Requête refusée (jeton CSRF invalide).");
}
echo "Suppression effectuée";
```

Complément : cookies `SameSite=Lax/Strict`, vérification de l'en-tête `Origin`, et **méthodes HTTP appropriées** (jamais d'action destructive sur un `GET`). Les frameworks intègrent déjà cette protection.

## 16.4 Hachage des mots de passe

Ne stockez **jamais** un mot de passe en clair, ni avec `md5()` / `sha1()` (trop rapides, cassables), ni avec un sel « maison ».

```php
<?php
$motDePasse = "correct horse battery staple";
$hash = password_hash($motDePasse, PASSWORD_DEFAULT);          // algorithme sûr du moment (bcrypt aujourd'hui) + sel intégré
// Option plus robuste : PASSWORD_ARGON2ID
echo strlen($hash), " caractères : ", substr($hash, 0, 7), "...", PHP_EOL;

$saisie = "correct horse battery staple";
if (password_verify($saisie, $hash)) {
    if (password_needs_rehash($hash, PASSWORD_DEFAULT)) {      // migrer vers un meilleur algorithme au fil des connexions
        $nouveau = password_hash($saisie, PASSWORD_DEFAULT);
        // … mise à jour en base
    }
    echo "Connecté", PHP_EOL;
} else {
    fwrite(STDERR, "Identifiants invalides" . PHP_EOL);
}

if (!password_verify("mauvais mot de passe", $hash)) {
    fwrite(STDERR, "Identifiants invalides" . PHP_EOL);        // message identique que l'e-mail ou le mot de passe soit faux
}
```

- La colonne en base doit pouvoir contenir **255 caractères** (`VARCHAR(255)`).
- Imposez une longueur minimale (12 caractères conseillés), vérifiez les mots de passe compromis (API *Have I Been Pwned*), **limitez les tentatives** (*rate limiting*), proposez l'**authentification à deux facteurs** et les **passkeys** (WebAuthn).
- Message de connexion **identique** que l'e-mail ou le mot de passe soit faux (évite l'énumération de comptes).

## 16.5 Aléatoire et jetons

```php
<?php
echo strlen(random_bytes(32)), " octets", PHP_EOL;           // 32 : octets cryptographiquement sûrs
echo bin2hex(random_bytes(16)), PHP_EOL;                     // jeton hexadécimal (32 caractères)
echo random_int(100000, 999999), PHP_EOL;                    // entier sûr (codes à usage unique)
// À éviter pour la sécurité : rand(), mt_rand(), uniqid() sont prévisibles
```

## 16.6 Téléversements sécurisés (rappel)

Taille limitée · type **réel** (`finfo`) · nom **aléatoire** · dossier **hors de la racine web** ou exécution PHP interdite · jamais de confiance dans l'extension ou le type MIME envoyés par le navigateur. Voir [section 10.6](#106-téléversement-sécurisé-de-fichiers).

## 16.7 HTTPS et en-têtes de sécurité

```php
<?php
// securite.php : à lancer avec « php -S localhost:8000 » puis « curl -i http://localhost:8000/securite.php »
const DOMAINE = 'exemple.com';        // nom de domaine fixe issu de la configuration

// Forcer HTTPS (mieux vaut le faire au niveau du serveur web / proxy)
if (empty($_SERVER['HTTPS']) || $_SERVER['HTTPS'] === 'off') {
    header('Location: https://' . DOMAINE . $_SERVER['REQUEST_URI'], true, 301);
    exit;
}

header('Strict-Transport-Security: max-age=31536000; includeSubDomains');   // HSTS
header('X-Content-Type-Options: nosniff');
header('X-Frame-Options: DENY');                                           // ou CSP : frame-ancestors 'none'
header('Referrer-Policy: strict-origin-when-cross-origin');
header('Permissions-Policy: camera=(), microphone=(), geolocation=()');
echo "En-têtes de sécurité envoyés";
```

> **Attention :** `$_SERVER['HTTP_HOST']` est fourni par le client : utilisez un **nom de domaine fixe** issu de la configuration.

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
composer audit                             # vulnérabilités connues
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

> **Bonne pratique :** **Versionnez `composer.lock`** (applications) pour que tous les environnements aient exactement les mêmes versions. Ne versionnez pas `vendor/`.

## 17.4 Chargement automatique

```php
<?php
// Prérequis : composer.json avec "autoload": {"psr-4": {"App\\": "src/"}}
// et une classe App\Service\Mailer dans src/Service/Mailer.php
require __DIR__ . '/vendor/autoload.php';       // une seule inclusion

use App\Service\Mailer;

$mailer = new Mailer();
echo $mailer::class, PHP_EOL;                   // App\Service\Mailer
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
<?php
// routes/web.php
use App\Http\Controllers\ArticleController;
use Illuminate\Support\Facades\Route;

Route::get('/articles/{id}', [ArticleController::class, 'show']);
```

Contrôleur associé :

```php
<?php
// app/Http/Controllers/ArticleController.php
namespace App\Http\Controllers;

use App\Models\Article;

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
// index.php : à lancer avec « php -S localhost:8000 index.php » après « composer require slim/slim slim/psr7 »
use Slim\Factory\AppFactory;

require __DIR__ . '/vendor/autoload.php';

$app = AppFactory::create();
$app->addErrorMiddleware(true, true, true);

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

> **Remarque :** Vérifiez toujours la **version actuelle** et la **version minimale de PHP** requise sur le site officiel de chaque framework avant de démarrer un projet.

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
<?php
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

> **Information :** Dans les versions récentes de PHPUnit, les **attributs** (`#[Test]`, `#[DataProvider]`) remplacent les annotations de commentaires (`@dataProvider`), dépréciées puis supprimées.

### Assertions courantes

`assertSame` (strict), `assertEquals`, `assertTrue`, `assertFalse`, `assertNull`, `assertCount`, `assertContains`, `assertInstanceOf`, `assertStringContainsString`, `expectException`.

## 19.2 Doublures (*mocks*)

Isoler la classe testée de ses dépendances :

```php
<?php
// src/MailerInterface.php et src/InscriptionService.php
namespace App;

interface MailerInterface
{
    public function envoyer(string $destinataire): bool;
}

final class InscriptionService
{
    public function __construct(private MailerInterface $mailer) {}

    public function inscrire(string $email): bool
    {
        return $this->mailer->envoyer($email);
    }
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

        $service = new InscriptionService($mailer);       // injection de dépendance
        $this->assertTrue($service->inscrire('alice@exemple.com'));
    }
}
```

| Type | Rôle |
| --- | --- |
| **Stub** | Renvoie des valeurs prédéfinies |
| **Mock** | Vérifie les appels reçus |
| **Fake** | Implémentation simplifiée (ex. base en mémoire) |

Outils : **Mockery**, **Prophecy**. Conseil : programmez **vers des interfaces** et utilisez l'**injection de dépendances** pour rendre le code testable.

## 19.3 TDD (*Test-Driven Development*)

1. **Rouge** : écrire un test qui échoue.
2. **Vert** : écrire le code minimal pour le faire passer.
3. **Refactoriser** : améliorer le code, tests toujours verts.

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
<?php
// Encoder
echo json_encode(['id' => 1, 'nom' => 'Alice'], JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR), PHP_EOL;

// Décoder
$texte = '{"id":1,"nom":"Alice"}';
$data = json_decode($texte, true, 512, JSON_THROW_ON_ERROR);      // true : tableau associatif
echo $data['nom'], PHP_EOL;                                        // Alice

// Corps d'une requête JSON (php://input est vide en ligne de commande)
$brut = file_get_contents('php://input');
var_dump($brut);                                                   // string(0) ""
try {
    $donnees = json_decode($brut, true, 512, JSON_THROW_ON_ERROR);
} catch (JsonException $e) {
    fwrite(STDERR, "Erreur JSON : " . $e->getMessage() . PHP_EOL);
}

// Objets : implémenter JsonSerializable
class Produit implements JsonSerializable {
    public function __construct(private int $id, private string $nom) {}
    public function jsonSerialize(): array { return ['id' => $this->id, 'nom' => $this->nom]; }
}
echo json_encode(new Produit(7, "Stylo")), PHP_EOL;                // {"id":7,"nom":"Stylo"}

var_dump(json_validate($texte));                                   // 8.3 : valide sans décoder : bool(true)
var_dump(json_validate('{invalide'));                              // bool(false)
```

## 20.3 Un mini-routeur d'API en PHP pur

```php
<?php
// api.php : à lancer avec « php -S localhost:8000 api.php » (le script sert de routeur)
declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');

// SQLite pour que l'exemple soit autonome ; remplacez le DSN par celui de votre base
$pdo = new PDO('sqlite:' . __DIR__ . '/api.sqlite', null, null, [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
]);
$pdo->exec("CREATE TABLE IF NOT EXISTS utilisateurs (id INTEGER PRIMARY KEY, nom TEXT NOT NULL)");

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
<?php
// routes/api.php
use App\Http\Controllers\ArticleController;
use Illuminate\Support\Facades\Route;

Route::apiResource('articles', ArticleController::class)->middleware('auth:sanctum');
```

Contrôleur associé :

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
    public function store(StoreArticleRequest $request): JsonResponse        // validation par FormRequest
    {
        $article = Article::create($request->validated());
        return (new ArticleResource($article))->response()->setStatusCode(201);
    }
}
```

### Slim

```php
<?php
// index.php : à lancer avec « php -S localhost:8000 index.php » après « composer require slim/slim slim/psr7 »
use Slim\Factory\AppFactory;

require __DIR__ . '/vendor/autoload.php';

$pdo = new PDO('sqlite::memory:', null, null, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
$pdo->exec("CREATE TABLE articles (id INTEGER PRIMARY KEY, titre TEXT)");
$pdo->exec("INSERT INTO articles (titre) VALUES ('Premier article')");

$app = AppFactory::create();

$app->get('/api/articles', function ($req, $res) use ($pdo) {
    $res->getBody()->write(json_encode($pdo->query("SELECT * FROM articles")->fetchAll(PDO::FETCH_ASSOC)));
    return $res->withHeader('Content-Type', 'application/json');
});
$app->run();
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
<?php
// cors.php : à lancer avec « php -S localhost:8000 »
header('Access-Control-Allow-Origin: https://mon-front.exemple');
header('Access-Control-Allow-Methods: GET, POST, PUT, PATCH, DELETE, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, Authorization');
if (($_SERVER['REQUEST_METHOD'] ?? '') === 'OPTIONS') { http_response_code(204); exit; }     // requête de pré-vérification

header('Content-Type: application/json; charset=utf-8');
echo json_encode(['message' => 'Réponse normale']);
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

$options = getopt('n:v', ['nom:', 'verbeux']);              // php script.php -n Alice --verbeux
echo "Options : " . json_encode($options) . PHP_EOL;
echo "Arguments : " . implode(', ', array_slice($argv, 1)) . PHP_EOL;

$saisie = trim((string) fgets(STDIN));                       // lecture au clavier
echo "Saisie : $saisie" . PHP_EOL;
fwrite(STDERR, "Message d'erreur\n");                        // sortie d'erreur
exit(0);                                                     // code de sortie
```

```bash
php script.php -n Alice --verbeux
chmod +x script.php && ./script.php
```

Pour des commandes riches : **Symfony Console**, **Laravel Artisan**, **Laravel Prompts**. Planification : `cron` (`* * * * * php /chemin/script.php`).

## 21.2 Performance

| Levier | Détails |
| --- | --- |
| **OPcache** | Garde le bytecode en mémoire : **à activer en production** (`opcache.enable=1`, `opcache.validate_timestamps=0` avec redéploiement) |
| **JIT** | Utile pour du calcul intensif, peu d'effet sur les applications web classiques |
| **Preloading** | Précharge des classes au démarrage (`opcache.preload`) |
| **Serveurs d'application persistants** | **FrankenPHP**, **RoadRunner**, **Swoole / OpenSwoole** : application gardée en mémoire (Laravel Octane) |
| **Requêtes SQL** | Index, éviter le problème « N+1 », pagination, mise en cache |
| **Autoload optimisé** | `composer install --optimize-autoloader --classmap-authoritative` |
| **Mémoire** | Générateurs, traitement par lots (`chunk`), éviter de charger de gros tableaux |
| **Mesure** | **Xdebug** (profilage), **Blackfire**, **Tideways**, `microtime(true)`, `memory_get_peak_usage()` |

> **Astuce :** **Mesurez avant d'optimiser** : le goulot d'étranglement est presque toujours la base de données ou les appels externes.

```php
<?php
$debut = microtime(true);

$total = 0;
for ($i = 0; $i < 1_000_000; $i++) { $total += $i; }          // code à mesurer
$tableau = range(1, 100_000);

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
<?php
// Utilise APCu s'il est actif, sinon un cache en mémoire du script (pour que l'exemple tourne partout)
function lireAvecCache(string $cle, int $ttl, callable $calcul): mixed
{
    static $local = [];

    if (function_exists('apcu_fetch') && apcu_enabled()) {
        $valeur = apcu_fetch($cle, $trouve);
        if ($trouve) return $valeur;
        $valeur = $calcul();
        apcu_store($cle, $valeur, $ttl);
        return $valeur;
    }

    if (isset($local[$cle]) && $local[$cle][1] > time()) return $local[$cle][0];
    $valeur = $calcul();
    $local[$cle] = [$valeur, time() + $ttl];
    return $valeur;
}

$calcul = function () { echo "(calcul lourd exécuté)", PHP_EOL; return 42; };

echo lireAvecCache('reponse', 60, $calcul), PHP_EOL;    // calcul exécuté, puis 42
echo lireAvecCache('reponse', 60, $calcul), PHP_EOL;    // 42, servi depuis le cache
```

- Définissez toujours une **durée de vie** (TTL) et une stratégie d'**invalidation** (« il n'y a que deux problèmes difficiles en informatique… »).
- Protégez-vous contre l'**effet de ruée** (*cache stampede*) : verrous, TTL avec variation aléatoire.

## 21.4 Redis et Memcached

```bash
# Extension native phpredis ou bibliothèque Predis
composer require predis/predis
```

```php
<?php
// Après « composer require predis/predis » ; nécessite un serveur Redis sur 127.0.0.1:6379
require __DIR__ . '/vendor/autoload.php';

$utilisateur = ['id' => 42, 'nom' => 'Alice'];

try {
    $redis = new Predis\Client(['scheme' => 'tcp', 'host' => '127.0.0.1', 'port' => 6379]);

    $redis->setex('utilisateur:42', 3600, json_encode($utilisateur));     // avec expiration
    $lu = json_decode($redis->get('utilisateur:42') ?? 'null', true);
    echo $lu['nom'], PHP_EOL;                                              // Alice
    echo $redis->incr('visites'), PHP_EOL;                                 // compteur atomique
    $redis->del('utilisateur:42');
} catch (Predis\Connection\ConnectionException $e) {
    fwrite(STDERR, "Redis inaccessible : " . $e->getMessage() . PHP_EOL);
}
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
<?php
// chat-serveur.php : après « composer require cboden/ratchet » ; lancer avec « php chat-serveur.php »
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
            if ($client !== $de) { $client->send($msg); }
        }
    }

    public function onClose(ConnectionInterface $c): void { $this->clients->detach($c); }

    public function onError(ConnectionInterface $c, \Exception $e): void { $c->close(); }
}

echo "Serveur WebSocket sur le port 8080", PHP_EOL;
IoServer::factory(new HttpServer(new WsServer(new Chat())), 8080)->run();
```

Dans la majorité des cas, les **SSE** ou l'**interrogation périodique** (*polling*) suffisent.

## 21.6 Programmation asynchrone et *fibers* *(8.1)*

Les **Fibers** permettent de suspendre / reprendre l'exécution et servent de socle à des bibliothèques asynchrones (**Revolt**, **AMPHP**, **ReactPHP**) :

```php
<?php
$fibre = new Fiber(function (): void {
    $valeur = Fiber::suspend('pause');
    echo "Reprise avec $valeur\n";
});
echo $fibre->start(), PHP_EOL;       // pause
$fibre->resume('hello');             // Reprise avec hello
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

> **Remarque :** Pour les détails exacts de chaque version : **php.net → Migration guides** ([php.net/manual/fr/appendices.php](https://www.php.net/manual/fr/appendices.php)).

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

- **Manuel officiel** : <https://www.php.net/manual/fr/>
- **PHP : la bonne méthode** (*PHP The Right Way*) : <https://phptherightway.com>
- **PHP-FIG (PSR)** : <https://www.php-fig.org>
- **OWASP PHP Cheat Sheets** : <https://cheatsheetseries.owasp.org>
- **Packagist** : <https://packagist.org>
- **3v4l.org** : exécuter un code sur toutes les versions de PHP

---

<div align="center">

*Bon développement !*

</div>
