<div align="center">

# PHP — Exercices

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

> **Légende** : chaque exercice porte le numéro de la section du cours qu'il illustre (l'exercice 6.4.2 est le deuxième exercice de la section 6.4). *(défi)* = exercice plus difficile ; *(ajout)* et *(à jour)* reprennent les mentions du cours ; *(8.x)* = version de PHP qui introduit la fonctionnalité utilisée. Sauf mention contraire, les exercices s'exécutent en ligne de commande (`php fichier.php`) ou avec le serveur intégré (`php -S localhost:8000`), avec `declare(strict_types=1);` en tête de fichier. Quand l'énoncé demande de « prédire » une sortie, répondez d'abord de tête, puis vérifiez en exécutant le code. Aucune solution n'est fournie dans ce document.

---

# 1. Introduction et installation

## 1.1 Qu'est-ce que PHP ?

**Exercice 1.1.1**

Indiquez si chaque affirmation est vraie ou fausse, en justifiant :

1. Le code PHP est exécuté dans le navigateur de l'utilisateur.
2. PHP ne sert qu'à produire du HTML.
3. PHP est un langage open source.
4. Les déclarations de types sont obligatoires en PHP.
5. L'utilisateur peut lire le code PHP d'une page en affichant son code source dans le navigateur.

**Exercice 1.1.2**

Complétez le tableau avec vos propres mots :

| Caractéristique | Signification |
| --- | --- |
| Exécution côté serveur | |
| Typage dynamique | |
| Multi-paradigme | |
| Extension de fichier | |

**Exercice 1.1.3**

Citez trois frameworks ou CMS écrits en PHP et décrivez en une phrase l'usage de chacun. Pourquoi l'écosystème de PHP est-il si lié au web ?

## 1.2 Brève histoire

**Exercice 1.2.1**

Reconstituez la chronologie : associez chaque événement à son année (1994, 1995, 1998, 2000, 2004, 2015, 2020, 2025) : PHP 7, PHP 8.5, création des premiers outils CGI par Rasmus Lerdorf, PHP 5 et son modèle objet, PHP 8.0, PHP 4 (moteur Zend), PHP 3, PHP/FI.

**Exercice 1.2.2**

Pourquoi n'y a-t-il pas de PHP 6 ? Quelle nouveauté majeure a apporté PHP 7 ? Quelles fonctionnalités apportent les versions 8.0, 8.1, 8.2, 8.3, 8.4 et 8.5 ?

### Versions supportées *(à jour)*

**Exercice 1.2.3**

Quelle est la durée du support actif et du support de sécurité d'une branche de PHP ? Vérifiez sur php.net quelles branches sont encore supportées aujourd'hui, et dites si la version installée sur votre machine l'est.

**Exercice 1.2.4**

Pourquoi est-il dangereux d'exécuter en production une version de PHP qui n'est plus supportée ? Rédigez un plan de migration de PHP 8.2 vers 8.5 (étapes, outils comme Rector, tests, intégration continue).

## 1.3 Ce que PHP sait faire

**Exercice 1.3.1**

Associez chaque besoin à la fonctionnalité de PHP la plus adaptée : traiter un formulaire, mémoriser un utilisateur connecté, stocker des articles, exporter des données en JSON pour une application mobile, lancer une tâche planifiée, envoyer un courriel de confirmation.

**Exercice 1.3.2**

Choisissez trois sites ou applications connus qui utilisent PHP et rédigez pour chacun une courte description de ce que PHP y fait vraisemblablement.

## 1.4 Comment PHP fonctionne

**Exercice 1.4.1**

Replacez dans l'ordre les quatre étapes du traitement d'une page `.php` (navigateur, serveur web, interpréteur PHP, réponse). Dessinez un schéma avec les flèches de requête et de réponse.

**Exercice 1.4.2**

Quelle différence entre Apache avec `mod_php`, Nginx + PHP-FPM et FrankenPHP ? Pourquoi PHP-FPM est-il aujourd'hui le plus répandu ?

**Exercice 1.4.3**

Qu'est-ce qu'une SAPI (`cli`, `fpm-fcgi`, `apache2handler`) ? Écrivez un script qui affiche `PHP_SAPI` et exécutez-le en ligne de commande puis via le serveur intégré.

## 1.5 Installer PHP

### Option 1 : paquets système (recommandé)

**Exercice 1.5.1**

Installez PHP avec le gestionnaire de paquets de votre système (`apt`, `dnf`, `brew`, `winget`, etc.) et les extensions courantes (`mbstring`, `pdo_mysql`, `intl`, `xml`, `curl`, `zip`). Notez les commandes utilisées.

### Option 2 : environnement tout-en-un

**Exercice 1.5.2**

Comparez deux environnements tout-en-un (XAMPP, MAMP, Laragon, Laravel Herd) : composants fournis, facilité d'installation, inconvénients par rapport à une installation native.

### Option 3 : Docker

**Exercice 1.5.3**

Écrivez un fichier `compose.yaml` (ou `docker-compose.yml`) qui lance un conteneur PHP avec Apache ou FPM, monte le dossier du projet et expose le port 8080. Lancez-le et affichez une page de test.

### Vérifier l'installation

**Exercice 1.5.4**

Exécutez `php -v`, `php -m`, `php -i` et `php --ini`. Quelles informations donne chaque commande ? Écrivez un script qui affiche la version de PHP (`PHP_VERSION`), le système (`PHP_OS`), la taille d'un entier (`PHP_INT_SIZE`) et la liste des extensions chargées.

**Exercice 1.5.5**

Où se trouve le fichier `php.ini` utilisé ? Modifiez `display_errors` et `error_reporting` pour un script de test. Pourquoi faut-il des réglages différents en développement et en production ?

## 1.6 Serveur de développement intégré

**Exercice 1.6.1**

Lancez `php -S localhost:8000` dans un dossier contenant un fichier `index.php`. Ouvrez la page dans le navigateur et observez les journaux dans le terminal.

**Exercice 1.6.2**

Utilisez l'option `-t` pour définir le dossier racine (`public/`) et un fichier « routeur » (`php -S localhost:8000 -t public routeur.php`). Écrivez un routeur minimal qui renvoie une page 404 personnalisée.

**Exercice 1.6.3**

Pourquoi le serveur intégré n'est-il pas destiné à la production ? Citez trois limites (un seul processus, pas de HTTPS, sécurité).

## 1.7 Premier script

**Exercice 1.7.1**

Écrivez `bonjour.php` qui affiche `Bonjour, PHP !` avec `echo`. Exécutez-le en ligne de commande, puis via le serveur intégré. Observez la différence de sortie (texte brut / HTML).

**Exercice 1.7.2**

Écrivez un script qui affiche la date du jour, la version de PHP et votre prénom stocké dans une variable, sur trois lignes.

### Mélanger PHP et HTML

**Exercice 1.7.3**

Écrivez une page HTML complète qui insère du PHP à trois endroits : le titre (`<title>`), un paragraphe qui affiche l'heure et une liste construite avec une boucle. Utilisez `<?= ... ?>` pour les affichages courts.

**Exercice 1.7.4**

Quelles précautions prendre pour la sortie dans une page HTML (échappement avec `htmlspecialchars`) ? Montrez ce qui se passe si l'on affiche sans échappement la chaîne `<b>gras</b>`.

---

# 2. Syntaxe et bases

## 2.1 Balises PHP

**Exercice 2.1.1**

Écrivez un fichier contenant du HTML avant et après un bloc PHP. Quelles sont les balises d'ouverture valides (`<?php`, `<?=`) ? Pourquoi les balises courtes `<?` sont-elles déconseillées ?

**Exercice 2.1.2**

Pourquoi omet-on généralement la balise fermante `?>` dans un fichier ne contenant que du PHP ? Montrez le problème d'un espace ou d'une ligne vide après `?>` (« headers already sent »).

**Exercice 2.1.3**

Écrivez un script qui, par erreur, affiche une ligne vide avant un `header('Location: ...')`. Observez l'avertissement obtenu et corrigez-le.

## 2.2 Instructions et commentaires

**Exercice 2.2.1**

Écrivez un script avec un commentaire sur une ligne (`//` et `#`), un commentaire multiligne (`/* */`) et un commentaire de documentation (`/** */`). Que se passe-t-il si l'on oublie un point-virgule ?

**Exercice 2.2.2**

PHP est-il sensible à la casse ? Testez avec des noms de variables (`$a` et `$A`), de fonctions (`strlen` et `STRLEN`), de classes et de mots-clés (`ECHO`, `Echo`). Établissez la règle.

**Exercice 2.2.3**

Écrivez une instruction sur plusieurs lignes et deux instructions sur une même ligne. Pourquoi une indentation et une mise en forme cohérentes (PSR-12) sont-elles recommandées ?

## 2.3 Typage strict *(ajout, à jour)*

**Exercice 2.3.1**

Écrivez une fonction `double(int $n): int`. Appelez-la avec `"5"` sans puis avec `declare(strict_types=1);`. Que se passe-t-il dans chaque cas ? Pourquoi la déclaration doit-elle être la première instruction du fichier ?

**Exercice 2.3.2**

Quelle est la portée de `declare(strict_types=1)` (le fichier où elle est écrite, les appels qui y sont faits) ? Que se passe-t-il pour un appel venant d'un autre fichier sans mode strict vers une fonction définie en mode strict ?

**Exercice 2.3.3**

Quels types de conversion le mode non strict autorise-t-il (`"5"` vers `int`, `"abc"` vers `int`, `5.7` vers `int`, `true` vers `string`) ? Testez et notez les résultats et les avertissements.

## 2.4 Afficher : `echo` et `print`

**Exercice 2.4.1**

Écrivez des affichages avec `echo` (plusieurs arguments séparés par des virgules), `print` (renvoie 1), `printf`, `sprintf`, `print_r`, `var_dump` et `var_export`. Pour une valeur de chaque type (entier, flottant, chaîne, booléen, `null`, tableau), comparez la sortie de `print_r`, `var_dump` et `var_export`.

**Exercice 2.4.2**

Quelle différence entre `echo` et `print` ? Quelles sont les différences entre `echo "a", "b"` et `echo "a" . "b"` ?

**Exercice 2.4.3**

Affichez avec `printf` : un nombre sur 8 caractères complété par des zéros, un flottant avec 2 décimales, un pourcentage littéral, une chaîne alignée à gauche sur 10 colonnes, un nombre en hexadécimal, un caractère ASCII par son code.

**Exercice 2.4.4**

Utilisez `PHP_EOL` et `"\n"`. Quand préférer `PHP_EOL` ? Écrivez un affichage multiligne avec un `heredoc` et un `nowdoc` : quelle différence d'interpolation ?

## 2.5 Variables

**Exercice 2.5.1**

Déclarez des variables de types variés et affichez-les avec `var_dump`. Quelles sont les règles de nommage (début par `$`, lettre ou `_`, pas de chiffre au début, sensible à la casse) ? Quels noms sont invalides : `$2x`, `$mon_nom`, `$mon-nom`, `$_tmp`, `$this`, `$é` ?

**Exercice 2.5.2**

Utilisez les variables variables (`$$nom`) et les noms dynamiques `${'a' . 'b'}`. Pourquoi sont-elles déconseillées ?

**Exercice 2.5.3**

Utilisez `isset`, `empty`, `is_null`, `unset` sur des variables définies, non définies, `null`, `0`, `""`, `"0"`, `[]`. Complétez le tableau des résultats.

**Exercice 2.5.4**

Écrivez les références : `$b = &$a;`, modification d'une variable à travers l'autre, `unset($b)`. Que se passe-t-il à l'affectation par valeur d'un tableau et à la copie d'un objet ?

**Exercice 2.5.5**

Que se passe-t-il à la lecture d'une variable non définie (avertissement `Undefined variable`) ? Comment l'éviter (initialisation, `??`) ?

## 2.6 Types de données

**Exercice 2.6.1**

Donnez un exemple de chaque type : `int`, `float`, `string`, `bool`, `array`, `object`, `null`, `callable`, `iterable`, `resource`. Utilisez `gettype` et `get_debug_type` et comparez leurs sorties (`integer` / `int`, `double` / `float`).

**Exercice 2.6.2**

Que valent `PHP_INT_MAX`, `PHP_INT_MAX + 1`, `PHP_FLOAT_EPSILON`, `0.1 + 0.2 == 0.3`, `intdiv(7, 2)`, `7 / 2`, `10 % 3`, `-10 % 3`, `fmod(10, 3)` ? Comment comparer correctement deux flottants ?

**Exercice 2.6.3**

Écrivez les littéraux numériques `1_000_000`, `0b1010`, `0o17` (ou `017`), `0xFF`, `1.5e3`. Utilisez la fonction `number_format` pour afficher `1234567.891` avec séparateurs français.

### Valeurs « fausses » (*falsy*)

**Exercice 2.6.4**

Classez en « faux » ou « vrai » (par `(bool)`) : `0`, `0.0`, `-0.0`, `""`, `" "`, `"0"`, `"0.0"`, `"false"`, `[]`, `[0]`, `null`, `new stdClass()`, `NAN`. Quel piège présente la chaîne `"0"` ?

**Exercice 2.6.5**

Pourquoi `if ($_POST['nom'])` est-il risqué pour tester qu'un champ a été saisi (cas du texte `"0"`) ? Écrivez un test fiable avec `isset` et `trim`.

## 2.7 Conversion de types (*casting*)

**Exercice 2.7.1**

Prédisez puis vérifiez : `(int) "12abc"`, `(int) "abc"`, `(int) 12.9`, `(int) -12.9`, `(int) true`, `(float) "1.5e3"`, `(string) false`, `(string) null`, `(bool) "0"`, `(array) "a"`, `(object) ['a' => 1]`, `intval("0x1A", 16)`, `intval("012", 0)`.

**Exercice 2.7.2**

Que se passe-t-il pour `"5" + "3"`, `"5" . "3"`, `"abc" + 1` (erreur de type en PHP 8), `"5 apples" + 1` (avertissement), `null + 1`, `true + true` ? Utilisez `is_numeric` pour tester.

**Exercice 2.7.3**

Écrivez `versEntier(string $s): ?int` qui renvoie un entier ou `null` quand la chaîne n'est pas un entier valide, en utilisant `filter_var` avec `FILTER_VALIDATE_INT`.

## 2.8 Constantes

**Exercice 2.8.1**

Définissez des constantes avec `define()` et `const`. Quelle différence (exécution ou compilation, portée de classe, expressions) ? Lisez une constante dont le nom est dynamique avec `constant()`.

**Exercice 2.8.2**

Utilisez les constantes magiques `__LINE__`, `__FILE__`, `__DIR__`, `__FUNCTION__`, `__CLASS__`, `__METHOD__`, `__NAMESPACE__`. Écrivez un exemple pour chacune.

**Exercice 2.8.3**

Utilisez les constantes prédéfinies `PHP_VERSION`, `PHP_OS_FAMILY`, `PHP_INT_MAX`, `DIRECTORY_SEPARATOR`, `M_PI`, `E_ALL`. Écrivez une constante de tableau et une constante typée (`const string NOM = "x";`, 8.3). *(8.3)*

## 2.9 Interpolation de chaînes

**Exercice 2.9.1**

Affichez des variables dans une chaîne entre guillemets doubles : `"$nom"`, `"{$nom}s"`, `"${nom}"` (déprécié), `"{$tableau['cle']}"`, `"$tableau[cle]"`, `"{$objet->prop->sous}"`, `"{$fonction()}"` (invalide). Dans quels cas les accolades sont-elles nécessaires ?

**Exercice 2.9.2**

Quelle différence entre guillemets simples et doubles pour `\n`, `$var`, `\'`, `\"`, `\\` ? Écrivez un `heredoc` avec interpolation d'une expression complexe et un `nowdoc` sans interpolation.

## 2.10 Portée et superglobales

**Exercice 2.10.1**

Montrez qu'une variable globale n'est pas visible dans une fonction. Corrigez avec `global`, avec `$GLOBALS`, avec un paramètre. Quelle est la meilleure solution ?

**Exercice 2.10.2**

Écrivez une fonction qui utilise `static` pour compter ses appels. Quelle est la durée de vie d'une variable statique ? Que se passe-t-il pour les méthodes d'une classe ?

**Exercice 2.10.3**

Listez les superglobales (`$_GET`, `$_POST`, `$_REQUEST`, `$_SERVER`, `$_SESSION`, `$_COOKIE`, `$_FILES`, `$_ENV`, `$GLOBALS`). Écrivez un script qui affiche `$_SERVER['REQUEST_METHOD']`, `['REQUEST_URI']`, `['HTTP_USER_AGENT']`, `['argv']` (en ligne de commande).

**Exercice 2.10.4**

Pourquoi ne faut-il jamais faire confiance aux valeurs de `$_SERVER` comme `HTTP_HOST` ou `HTTP_USER_AGENT` sans validation ? Citez deux exemples d'abus.

## 2.11 Exemple complet

**Exercice 2.11.1**

Écrivez un programme (en ligne de commande) qui, à partir de variables, calcule et affiche une facture : prix HT, TVA (20 %), prix TTC avec `number_format`, avec constantes, interpolation et `printf`. Gérez un arrondi correct à deux décimales (`round`).

**Exercice 2.11.2**

Écrivez un convertisseur de températures (Celsius vers Fahrenheit et Kelvin) avec des fonctions typées et un affichage formaté.

---

# 3. Opérateurs

## 3.1 Arithmétiques

**Exercice 3.1.1**

Prédisez : `7 + 3`, `7 - 10`, `7 * 3`, `7 / 2`, `8 / 2`, `7 % 3`, `-7 % 3`, `2 ** 10`, `2 ** -1`, `2 ** 3 ** 2`, `intdiv(7, 2)`, `7 <=> 3`. Quel est le type de `8 / 2` ? Que se passe-t-il pour `1 / 0` et `1 % 0` ?

**Exercice 3.1.2**

Écrivez des fonctions pour : la moyenne de trois nombres, le reste euclidien positif, l'arrondi à `n` décimales, le pourcentage d'un nombre, le PGCD de deux entiers, la conversion de secondes en `h:m:s`.

**Exercice 3.1.3**

Utilisez les fonctions mathématiques : `abs`, `ceil`, `floor`, `round` (avec précision et modes), `sqrt`, `pow`, `max`, `min`, `intdiv`, `fmod`, `pi()`, `random_int`. Pourquoi `round(2.5)` donne-t-il 3 et `round(-2.5)` donne-t-il -3 ?

## 3.2 Affectation

**Exercice 3.2.1**

Utilisez `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `.=`, `??=`, `<<=`, `|=`. Écrivez une séquence d'instructions et donnez la valeur finale de la variable.

**Exercice 3.2.2**

Écrivez l'échange de deux variables avec la décomposition de tableaux (`[$a, $b] = [$b, $a]`). Décomposez un tableau associatif avec `['x' => $x, 'y' => $y] = $point`.

**Exercice 3.2.3**

Utilisez l'affectation conditionnelle `??=` pour initialiser une valeur de configuration absente. Quelle différence avec `if (!isset($x)) $x = ...` ?

## 3.3 Comparaison

**Exercice 3.3.1**

Prédisez (PHP 8) : `0 == "a"`, `"1" == "01"`, `"10" == "1e1"`, `100 == "1e2"`, `"abc" == 0`, `null == false`, `[] == false`, `"0" == false`, `"" == null`, `0 === "0"`, `1.0 === 1`, `"a" <=> "b"`.

**Exercice 3.3.2**

Pourquoi PHP 8 a-t-il changé la comparaison entre un nombre et une chaîne non numérique (`0 == "a"` valait `true` en PHP 7) ? Pourquoi recommande-t-on `===` ?

**Exercice 3.3.3**

Utilisez l'opérateur « vaisseau spatial » `<=>` pour écrire un comparateur de tri. Comparez des tableaux (`[1, 2] <=> [1, 3]`).

**Exercice 3.3.4**

Écrivez la comparaison de chaînes sûre pour des secrets (`hash_equals`) et la comparaison de nombres flottants avec une marge.

## 3.4 Logiques

**Exercice 3.4.1**

Évaluez : `true && false`, `true || false`, `!true`, `true xor true`, `$a = true and false` (piège de priorité), `$a = (true and false)`. Pourquoi `and` / `or` ont-ils une priorité plus faible que `=` ?

**Exercice 3.4.2**

Montrez l'évaluation paresseuse (court-circuit) avec `&&` et `||` en appelant des fonctions qui affichent un message. Utilisez-la pour écrire `$fichier = ouvrir() or die("échec")`. Pourquoi ce style est-il déconseillé aujourd'hui ?

## 3.5 Chaînes, incrément, tableaux

**Exercice 3.5.1**

Concaténez avec `.` et `.=`. Prédisez `"a" . 1 + 2` (priorité de `+` sur `.` depuis PHP 8). Prédisez `"5" + "5"` et `"5" . "5"`.

**Exercice 3.5.2**

Incrémentez des chaînes : `$s = "a"; $s++;`, `"Az"++`, `"zz"++`, `"a9"++`. Que valent-elles ? Décrémentez `null` et incrémentez `null`.

**Exercice 3.5.3**

Utilisez les opérateurs de tableaux : `+` (union), `==`, `===`, `!=`, `<>`, `!==`. Prédisez `[1, 2] + [3, 4, 5]`, `['a' => 1] + ['a' => 2, 'b' => 3]`, `[1, 2] == [2 => 1]`, `[0 => 'a', 1 => 'b'] === [1 => 'b', 0 => 'a']`.

## 3.6 Opérateurs modernes *(à jour)*

**Exercice 3.6.1**

Écrivez `$nom = $_GET['nom'] ?? "Invité"` et explicitez la différence avec `isset` + ternaire, avec le ternaire court `?:` et avec `empty`. Testez avec `null`, `""`, `0`, `"0"`, `false`.

**Exercice 3.6.2**

Écrivez un accès sécurisé à une valeur profondément imbriquée avec `??` sur un tableau (`$config['db']['hote'] ?? "localhost"`) et avec l'opérateur null-safe `?->` sur des objets. *(8.0)*

**Exercice 3.6.3**

Écrivez un `match` qui renvoie le nom d'un jour, un libellé de code HTTP, une catégorie d'âge (avec `match (true)`). Quelles sont les différences avec `switch` (comparaison stricte, valeur de retour, absence de chute, `UnhandledMatchError`) ? *(8.0)*

**Exercice 3.6.4**

Utilisez l'opérateur de décomposition `...` : fusion de tableaux (`[...$a, ...$b]`), tableaux associatifs (8.1), paramètre variadique `int ...$nombres`, appel avec dépliage. *(8.1)*

**Exercice 3.6.5**

Utilisez l'opérateur pipe `|>` pour enchaîner `trim`, `strtolower` et un remplacement d'espaces par des tirets (slug). Réécrivez le même traitement avec des appels imbriqués puis avec des variables intermédiaires. Comparez la lisibilité. *(8.5)*

**Exercice 3.6.6**

Utilisez les arguments nommés (`str_pad(string: "x", length: 5, pad_type: STR_PAD_LEFT)`) et les paramètres nommés dans vos propres fonctions. Quels avantages (lisibilité, paramètres optionnels sautés) ? *(8.0)*

## 3.7 Priorité (extraits)

**Exercice 3.7.1**

Ajoutez des parenthèses implicites et évaluez : `1 + 2 * 3 ** 2`, `!$a && $b`, `$x = $y ?? $z ? 1 : 2` (erreur ?), `"a" . 1 + 2`, `-2 ** 2`, `true ? "a" : (false ? "b" : "c")`, `$a = 1 and $b = 2`.

**Exercice 3.7.2**

Pourquoi les ternaires imbriqués sans parenthèses sont-ils interdits depuis PHP 8 ? Réécrivez avec `match` ou `if`.

---

# 4. Structures de contrôle

## 4.1 Conditions

**Exercice 4.1.1**

Écrivez un programme qui affiche la mention d'une note sur 20 avec `if` / `elseif` / `else`. Écrivez ensuite `estBissextile(int $annee): bool` et `typeTriangle(float $a, float $b, float $c): string`.

**Exercice 4.1.2**

Pourquoi `if ($a = 5)` est-il presque toujours une erreur ? Quelle convention de comparaison (« Yoda ») permet de s'en prémunir ?

**Exercice 4.1.3**

Écrivez avec des clauses de garde (sorties anticipées) une fonction `traiter(?array $utilisateur): string` qui renvoie « Inconnu », « Inactif », « Mineur » ou « Bienvenue X » sans imbrication profonde.

### `switch` (comparaison souple)

**Exercice 4.1.4**

Écrivez `nomDuJour(int $n): string` avec `switch`. Montrez le piège de la comparaison souple (`switch ("1e1") { case 10: ... }`) et de la chute (oubli de `break`). Réécrivez avec `match`.

**Exercice 4.1.5**

Regroupez des cas avec la chute volontaire (week-end) et utilisez `default`. Que fait `continue` dans un `switch` à l'intérieur d'une boucle ?

### Syntaxe alternative (dans les gabarits HTML)

**Exercice 4.1.6**

Écrivez une portion de gabarit qui utilise `if: ... elseif: ... else: ... endif;`, `foreach: ... endforeach;`, `for: ... endfor;`, `while: ... endwhile;` pour afficher une liste de produits ou un message « Aucun produit ». Pourquoi cette syntaxe est-elle plus lisible dans du HTML ?

## 4.2 Boucles

**Exercice 4.2.1**

Affichez les entiers de 1 à 10 avec `for`, `while`, `do...while`. Quelle différence essentielle entre `while` et `do...while` ?

**Exercice 4.2.2**

Calculez : la somme de 1 à 100, la factorielle de 10, la somme des chiffres d'un entier, le PGCD de deux entiers, les nombres premiers inférieurs à 100, la suite de Fibonacci jusqu'à `n` termes.

**Exercice 4.2.3**

Écrivez FizzBuzz de 1 à 100, la table de multiplication de 1 à 10 sous forme de grille alignée avec `str_pad`, et les triangles d'étoiles :

```text
*
**
***
****
*****
```

**Exercice 4.2.4**

Parcourez un tableau avec `foreach` (valeurs seules, clés et valeurs, valeurs par référence). Que se passe-t-il si l'on oublie `unset($valeur)` après un `foreach` par référence ? Montrez le piège.

**Exercice 4.2.5**

Écrivez une boucle `for` avec plusieurs expressions (`for ($i = 0, $j = 10; $i < $j; $i++, $j--)`). Que se passe-t-il si une boucle `for` a des clauses vides (`for (;;)`) ?

**Exercice 4.2.6**

Écrivez des boucles imbriquées pour afficher un damier 8×8 et pour générer toutes les paires `(i, j)` avec `i < j` parmi 1 à 5.

## 4.3 `break`, `continue`

**Exercice 4.3.1**

Utilisez `break` pour trouver le premier multiple de 7 supérieur à 100 et `continue` pour sauter les multiples de 3. Utilisez `break 2` et `continue 2` pour agir sur des boucles imbriquées.

**Exercice 4.3.2**

Écrivez une recherche d'une valeur dans un tableau à deux dimensions qui s'interrompt dès qu'elle est trouvée, avec `break 2`. Proposez une version avec une fonction et `return`.

## 4.4 Générateurs *(ajout)*

**Exercice 4.4.1**

Écrivez un générateur `plage(int $debut, int $fin, int $pas = 1)` avec `yield` et utilisez-le dans `foreach`. Comparez la mémoire avec `range()` pour un million d'éléments (`memory_get_peak_usage`).

**Exercice 4.4.2**

Écrivez un générateur de Fibonacci infini, un générateur de nombres premiers et une fonction `prendre(iterable $it, int $n)` qui renvoie les `n` premiers éléments.

**Exercice 4.4.3**

Utilisez `yield $cle => $valeur`, `yield from` (délégation), `$gen->send()` et `$gen->getReturn()`. Écrivez un générateur qui lit un fichier ligne par ligne.

**Exercice 4.4.4**

Écrivez un pipeline de générateurs : lire des lignes, les filtrer, les transformer. Pourquoi consomme-t-il très peu de mémoire ?

## 4.5 Inclusion de fichiers

**Exercice 4.5.1**

Utilisez `include`, `include_once`, `require`, `require_once`. Quelle différence de comportement quand le fichier est absent (avertissement ou erreur fatale) ? Quand préférer `require_once` ?

**Exercice 4.5.2**

Pourquoi faut-il utiliser des chemins absolus avec `__DIR__` (`require __DIR__ . '/config.php'`) ? Montrez le problème d'un chemin relatif selon le dossier de travail.

**Exercice 4.5.3**

Un fichier inclus peut renvoyer une valeur : écrivez `config.php` qui `return [...]` et chargez-le dans une variable. Découpez une page en `entete.php`, `pied.php` et un fichier de gabarit.

**Exercice 4.5.4**

Quel danger présente `include $_GET['page'] . '.php'` (inclusion de fichier locale ou distante) ? Écrivez une version sûre avec une liste blanche de pages.

---

# 5. Fonctions

## 5.1 Définir et appeler

**Exercice 5.1.1**

Écrivez et appelez : `carre(int $n): int`, `max3(float $a, float $b, float $c): float`, `estPremier(int $n): bool`, `factorielle(int $n): int`, `saluer(string $nom): void`, `puissance(float $x, int $n): float`.

**Exercice 5.1.2**

Les noms de fonctions sont-ils sensibles à la casse ? Peut-on appeler une fonction avant sa définition (fonctions déclarées au niveau supérieur) ? Et une fonction définie dans un `if` ? Testez.

**Exercice 5.1.3**

Appelez une fonction dont le nom est dans une variable (`$f = 'strtoupper'; $f('a')`), avec `call_user_func` et `call_user_func_array`. Quels sont les risques si le nom vient d'une entrée utilisateur ?

## 5.2 Paramètres

**Exercice 5.2.1**

Écrivez `saluer(string $nom, string $titre = "M.")` avec une valeur par défaut. Appelez-la de plusieurs façons. Pourquoi les paramètres facultatifs doivent-ils être placés en dernier ?

**Exercice 5.2.2**

Écrivez une fonction `somme(int ...$nombres): int` (variadique), une fonction qui reçoit un tableau déplié avec `...`, et une fonction avec arguments nommés (`creerUtilisateur(nom: "A", role: "admin")`).

**Exercice 5.2.3**

Écrivez une fonction qui modifie son argument par référence (`function ajouter(array &$tableau, $valeur)`). Quand utiliser une référence ? Quels sont les risques ?

**Exercice 5.2.4**

Écrivez `swap(&$a, &$b)`, une fonction qui remplit un tableau passé par référence, et montrez la différence avec la valeur de retour. Les objets sont-ils passés par référence ? Que se passe-t-il à la réaffectation d'un objet passé en paramètre ?

**Exercice 5.2.5**

Utilisez `func_get_args()` et `func_num_args()`. Pourquoi les paramètres variadiques typés sont-ils préférables ?

**Exercice 5.2.6**

Écrivez une fonction avec un paramètre nullable (`?string`), un paramètre union (`int|string`) et un paramètre avec valeur par défaut `null`. Quelle différence entre `?string $x` et `string $x = null` (déprécié en 8.4) ? *(8.4)*

## 5.3 Valeurs de retour

**Exercice 5.3.1**

Écrivez une fonction qui renvoie plusieurs valeurs avec un tableau, puis avec un tableau associatif, et décomposez le résultat avec `[$a, $b] = ...`. Quand préférer un objet ?

**Exercice 5.3.2**

Que renvoie une fonction sans `return` ? Avec `return;` ? Que renvoie une fonction de type `void` ? Testez avec `var_dump`.

**Exercice 5.3.3**

Écrivez `trouver(array $tab, mixed $x): int|false` qui renvoie l'indice ou `false`. Pourquoi le piège `if (trouver(...))` échoue-t-il pour l'indice 0 ? Corrigez avec `!== false`.

**Exercice 5.3.4**

Utilisez `never` comme type de retour pour une fonction qui termine toujours le script ou lève une exception. *(8.1)*

## 5.4 Déclarations de types *(à jour)*

**Exercice 5.4.1**

Utilisez les types scalaires (`int`, `float`, `string`, `bool`), `array`, `callable`, `iterable`, `object`, `mixed`, `self`, `static`, `void`, `never`, `null`. Écrivez une fonction avec chacun.

**Exercice 5.4.2**

Utilisez les types union (`int|float`), nullables (`?int`), d'intersection (`Countable&Traversable`, 8.1) et les types DNF (`(A&B)|null`, 8.2). Pour chacun, écrivez un exemple pertinent. *(8.1, 8.2)*

**Exercice 5.4.3**

Que se passe-t-il quand on passe une valeur du mauvais type avec et sans mode strict ? Quelle exception est levée (`TypeError`) ? Capturez-la.

**Exercice 5.4.4**

Utilisez `true` et `false` comme types autonomes (8.2) et `null` comme type autonome. Quand est-ce utile ? *(8.2)*

**Exercice 5.4.5**

Écrivez une fonction `typeDe(mixed $v): string` qui renvoie `get_debug_type($v)`. Pourquoi est-ce plus fiable que `gettype` ?

## 5.5 Portée des variables

**Exercice 5.5.1**

Prédisez la sortie, puis corrigez de trois façons (paramètre, `global`, constante) :

```php
<?php
$taux = 0.2;
function ttc(float $ht): float {
    return $ht * (1 + $taux);
}
echo ttc(100), PHP_EOL;
```

**Exercice 5.5.2**

Écrivez une fermeture qui capture une variable par valeur avec `use ($x)` et une autre par référence avec `use (&$x)`. Montrez la différence quand la variable change après la création de la fermeture.

**Exercice 5.5.3**

Écrivez un compteur avec une variable `static` dans une fonction, puis avec une fermeture. Comparez.

**Exercice 5.5.4**

Pourquoi les fonctions fléchées (`fn`) capturent-elles automatiquement les variables du parent par valeur ? Quelles sont leurs limites (une seule expression, pas de modification de variable extérieure) ?

## 5.6 Fonctions anonymes et fléchées

**Exercice 5.6.1**

Écrivez une fonction anonyme assignée à une variable, une fonction fléchée `fn($x) => $x * 2`, et utilisez-les avec `array_map`, `array_filter`, `usort`.

**Exercice 5.6.2**

Écrivez une fabrique `multiplicateur(int $n): Closure` qui renvoie une fermeture. Écrivez `compose(callable ...$fns)` qui compose des fonctions. Écrivez `curry` pour une fonction à deux paramètres. *(défi)*

**Exercice 5.6.3**

Utilisez `Closure::bind`, `bindTo`, `call` et `Closure::fromCallable`. Quand `$this` est-il disponible dans une fermeture ? Que fait le mot-clé `static` devant une fonction anonyme ?

### Syntaxe de « callable de première classe » *(8.1)*

**Exercice 5.6.4**

Créez des `Closure` avec la syntaxe `strlen(...)`, `$objet->methode(...)`, `Classe::methodeStatique(...)`. Utilisez-les avec `array_map`. Quels avantages face aux chaînes de caractères (`'strlen'`) et aux tableaux (`[$obj, 'm']`) ? *(8.1)*

## 5.7 Récursivité

**Exercice 5.7.1**

Écrivez de manière récursive : `factorielle`, `somme(array)`, `puissance`, `fibonacci`, `inverser(string)`, `estPalindrome`, `pgcd`, `aplatir(array)`, `profondeur(array)`.

**Exercice 5.7.2**

Écrivez un parcours récursif d'un tableau multidimensionnel (arbre de catégories) avec affichage indenté. Écrivez aussi la recherche récursive d'un fichier dans un répertoire.

**Exercice 5.7.3**

Que se passe-t-il pour une récursion infinie (limite mémoire ou profondeur, extension `xdebug.max_nesting_level`) ? Écrivez la version itérative d'une récursion avec une pile explicite.

**Exercice 5.7.4**

Écrivez la mémoïsation d'une fonction récursive avec un tableau statique (Fibonacci) et comparez les temps pour `fib(35)`.

## 5.8 Fonctions utiles

**Exercice 5.8.1**

Utilisez `function_exists`, `is_callable`, `call_user_func`, `array_map`, `usleep`, `microtime(true)`, `memory_get_usage`, `register_shutdown_function`, `get_defined_vars`. Écrivez un exemple de chacune.

**Exercice 5.8.2**

Écrivez une fonction `mesurer(callable $f): array` qui renvoie le résultat, le temps d'exécution et la mémoire utilisée.

## 5.9 Bonnes pratiques

**Exercice 5.9.1**

Refactorisez ce code monolithique en fonctions courtes, typées et bien nommées :

```php
<?php
$notes = [12, 15, 9, 18];
$s = 0;
foreach ($notes as $n) { $s += $n; }
echo "Moyenne : " . ($s / count($notes)) . "\n";
$max = $notes[0];
foreach ($notes as $n) { if ($n > $max) $max = $n; }
echo "Max : " . $max . "\n";
```

**Exercice 5.9.2**

Listez cinq bonnes pratiques sur les fonctions (types, petite taille, pureté, noms explicites, pas de globales) et illustrez chacune.

---

# 6. Tableaux

## 6.1 Types de tableaux

**Exercice 6.1.1**

Créez un tableau indexé, un tableau associatif et un tableau multidimensionnel avec les deux syntaxes (`array()` et `[]`). Que valent les clés de `[5 => 'a', 'b', 'c']` ? Que se passe-t-il avec des clés dupliquées, des clés `"1"` (chaîne) et `1.7`, `true`, `null` ?

**Exercice 6.1.2**

Créez les tableaux : des entiers de 1 à 20 (`range`), des lettres de `a` à `j`, des multiples de 5 de 0 à 50, un tableau de 10 zéros (`array_fill`), un tableau à partir de deux tableaux (`array_combine`). Quelle différence entre `array_fill` et `array_pad` ?

**Exercice 6.1.3**

Écrivez un tableau associatif décrivant un utilisateur (nom, âge, email, adresse imbriquée). Lisez en sécurité `$utilisateur['adresse']['ville'] ?? 'inconnue'`.

## 6.2 Ajouter, modifier, supprimer

**Exercice 6.2.1**

Utilisez `$t[] = ...`, `array_push`, `array_pop`, `array_shift`, `array_unshift`, `unset`, `array_splice`. Pour chacune, indiquez la valeur de retour et si les clés sont réindexées.

**Exercice 6.2.2**

Écrivez les fonctions `inserer(array $t, int $pos, mixed $v): array`, `supprimerValeur(array $t, mixed $v): array`, `deplacer(array $t, int $de, int $vers): array` sans modifier l'original.

**Exercice 6.2.3**

Pourquoi `unset($t[1])` ne réindexe-t-il pas ? Utilisez `array_values` pour réindexer. Que se passe-t-il à l'ajout `$t[] = x` après un `unset` du dernier indice ?

**Exercice 6.2.4**

Modifiez des éléments imbriqués : ajoutez un élément dans un sous-tableau (`$t['liste'][] = 3`), supprimez une clé profonde, créez automatiquement des niveaux intermédiaires.

## 6.3 Parcourir

**Exercice 6.3.1**

Parcourez un tableau avec `for` (indexé), `foreach` (valeurs), `foreach` (clé / valeur), `array_walk`, `each` (supprimé), `current` / `next` / `reset` / `key`. Quand `for` est-il inapproprié (clés non consécutives) ?

**Exercice 6.3.2**

Modifiez les éléments d'un tableau en cours de parcours : par référence (`foreach ($t as &$v)`), avec `array_walk` (rappel par référence), avec `array_map`. Montrez le piège de la référence résiduelle.

**Exercice 6.3.3**

Parcourez deux tableaux en parallèle (`array_map(null, $a, $b)`, `MultipleIterator`, boucle avec indice). Parcourez un tableau en sens inverse.

## 6.4 Fonctions essentielles

**Exercice 6.4.1**

Utilisez `count`, `in_array` (avec le paramètre strict), `array_search`, `array_key_exists`, `isset`, `array_keys`, `array_values`, `array_merge`, `array_slice`, `array_unique`, `array_reverse`, `array_flip`, `array_sum`, `array_product`, `array_column`, `array_chunk`, `array_fill_keys`, `array_diff`, `array_intersect`, `array_key_first`, `array_key_last`, `array_is_list`.

**Exercice 6.4.2**

Quelle différence entre `array_key_exists` et `isset` pour une clé dont la valeur est `null` ? Entre `in_array("abc", [0])` en mode souple et strict ? Entre `array_merge` et l'opérateur `+` pour des clés numériques et des clés textuelles ?

**Exercice 6.4.3**

À partir d'une liste de produits (`nom`, `prix`, `categorie`), écrivez : la liste des noms (`array_column`), le prix moyen, le produit le plus cher, les produits groupés par catégorie, le total par catégorie, la liste triée par prix.

**Exercice 6.4.4**

Écrivez `chunk($tab, $taille)`, `zip($a, $b)`, `unzip($paires)`, `union($a, $b)`, `intersection($a, $b)`, `difference($a, $b)`, `rotation($tab, $n)`, `transposer($matrice)`, `produitCartesien($a, $b)`.

**Exercice 6.4.5**

Utilisez les fonctions de comparaison avec `u` (`array_udiff`, `array_uintersect`) pour comparer des tableaux d'objets selon une propriété.

## 6.5 Fonctions d'ordre supérieur

**Exercice 6.5.1**

Avec `array_map`, `array_filter` (avec `ARRAY_FILTER_USE_KEY` et `ARRAY_FILTER_USE_BOTH`), `array_reduce` : à partir de `[1, 2, 3, 4, 5, 6]`, obtenez les carrés, les pairs, la somme, le produit, le maximum et la somme des carrés des impairs.

**Exercice 6.5.2**

Pourquoi `array_filter` conserve-t-il les clés ? Comment réindexer ? Quelle est la sortie de `array_filter([0, 1, "", "a", null, []])` ?

**Exercice 6.5.3**

Écrivez avec `array_reduce` : le comptage de fréquence, le regroupement par clé, la fusion d'un tableau de tableaux, l'inversion d'un tableau.

**Exercice 6.5.4**

Utilisez `array_map` avec plusieurs tableaux et avec `null` comme rappel. Que se passe-t-il quand les tableaux ont des longueurs différentes ? Quelle différence avec `array_walk` ?

## 6.6 Trier

**Exercice 6.6.1**

Triez un tableau de nombres, de chaînes, de nombres mélangés avec `sort`, `rsort`, `asort`, `arsort`, `ksort`, `krsort`. Pour chaque fonction, indiquez : tri sur valeurs ou clés, conservation des associations, ordre.

**Exercice 6.6.2**

Triez avec `usort` des produits par prix croissant, puis par catégorie puis par prix décroissant (`<=>` sur des tableaux). Triez des chaînes accentuées avec `setlocale` / `strcoll` ou `Collator` (intl).

**Exercice 6.6.3**

Pourquoi le tri est-il stable depuis PHP 8.0 ? Quels indicateurs (`SORT_STRING`, `SORT_NUMERIC`, `SORT_NATURAL | SORT_FLAG_CASE`) règlent la façon de comparer ? Triez `["img12", "img10", "img2", "IMG1"]` avec `natcasesort`.

**Exercice 6.6.4**

Utilisez `array_multisort` pour trier plusieurs tableaux en parallèle (par exemple des colonnes séparées). Triez de façon aléatoire avec `shuffle` et avec `array_rand`.

## 6.7 Copie et références

**Exercice 6.7.1**

Montrez que les tableaux sont copiés par valeur (copie à l'écriture) : modifiez la copie et vérifiez l'original. Comparez avec les objets (références d'objet). Que se passe-t-il pour un tableau d'objets copié ?

**Exercice 6.7.2**

Copiez en profondeur un tableau contenant des objets (`unserialize(serialize())` avec réserve, `clone` récursif). Quels sont les risques de `serialize` ?

**Exercice 6.7.3**

Reproduisez le piège classique de `foreach` par référence suivi d'un second `foreach` sur le même tableau. Prédisez le résultat puis expliquez.

## 6.8 Parcours multidimensionnel

**Exercice 6.8.1**

Parcourez une matrice avec deux `foreach` imbriqués. Écrivez la somme des lignes, des colonnes, de la diagonale, la transposée et le produit de deux matrices.

**Exercice 6.8.2**

Utilisez `RecursiveIteratorIterator` et `RecursiveArrayIterator` pour aplatir un tableau imbriqué. Écrivez la même chose avec une fonction récursive et avec une pile.

**Exercice 6.8.3**

Écrivez une fonction qui lit un tableau imbriqué avec un chemin en notation pointée (`lire($config, "db.hote.port", $defaut)`) et la fonction réciproque qui l'écrit.

## 6.9 Interfaces utiles : `ArrayAccess`, `Countable`, `IteratorAggregate`

**Exercice 6.9.1**

Écrivez une classe `Collection` qui implémente `ArrayAccess` (`offsetGet`, `offsetSet`, `offsetExists`, `offsetUnset`), `Countable` et `IteratorAggregate` pour être utilisée comme un tableau (`$c[] = 1`, `count($c)`, `foreach ($c as ...)`).

**Exercice 6.9.2**

Ajoutez à `Collection` des méthodes `map`, `filter`, `reduce`, `trier`, `premier`, `dernier`, `toArray` sous forme fluide. Les méthodes renvoient-elles de nouvelles collections (immuabilité) ?

---

# 7. Chaînes de caractères

## 7.1 Créer des chaînes

**Exercice 7.1.1**

Créez des chaînes avec des apostrophes, des guillemets doubles, un `heredoc` et un `nowdoc`. Que se passe-t-il pour l'indentation d'un `heredoc` depuis PHP 7.3 (indentation de la fermeture) ?

**Exercice 7.1.2**

Accédez aux caractères d'une chaîne : `$s[0]`, `$s[-1]`, `$s{0}` (supprimé), `substr`. Modifiez un caractère (`$s[0] = 'X'`). Que se passe-t-il pour un indice hors limites ?

**Exercice 7.1.3**

Concaténez efficacement de nombreux morceaux (`implode`, `.=`, `sprintf`). Pourquoi les chaînes PHP sont-elles des suites d'octets et non de caractères ?

## 7.2 Fonctions courantes

**Exercice 7.2.1**

Utilisez : `strlen`, `mb_strlen`, `strtoupper`, `mb_strtoupper`, `strtolower`, `ucfirst`, `ucwords`, `lcfirst`, `trim` (avec liste de caractères), `ltrim`, `rtrim`, `str_pad`, `str_repeat`, `strrev`, `substr`, `mb_substr`, `strpos`, `stripos`, `strrpos`, `str_contains`, `str_starts_with`, `str_ends_with`, `str_replace`, `str_ireplace`, `substr_count`, `explode`, `implode`, `str_split`, `mb_str_split`, `wordwrap`, `nl2br`, `strcmp`, `similar_text`, `levenshtein`, `soundex`, `metaphone`.

**Exercice 7.2.2**

Pourquoi `strpos` peut-il renvoyer `0` ou `false` ? Corrigez `if (strpos($s, "a"))` avec `!== false` ou `str_contains`. *(8.0)*

**Exercice 7.2.3**

Quelle est la différence entre `strlen` et `mb_strlen` pour `"éàü"` (en UTF-8) ? Pour quelles fonctions utiliser la version `mb_*` ? Que se passe-t-il pour `strtoupper("é")` ?

**Exercice 7.2.4**

Écrivez : `capitaliser`, `titre` (chaque mot avec majuscule), `inverser`, `estPalindrome` (insensible à la casse et aux accents), `compterVoyelles`, `tronquer($texte, $n)` (avec `…`), `slugifier($texte)` (minuscules, suppression des accents avec `iconv` ou `Transliterator`, tirets).

**Exercice 7.2.5**

Écrivez `compterMots(string $texte): array` : fréquence de chaque mot (`str_word_count` avec `mb_`, ou `preg_split`), puis les trois mots les plus fréquents (`arsort`, `array_slice`).

**Exercice 7.2.6**

Utilisez `explode` avec limite (`explode(",", $s, 2)`, négatif), `implode`, `str_getcsv`, `strtok`, `sscanf` pour découper `"2026-10-21 14:30"`.

**Exercice 7.2.7**

Utilisez `sprintf` / `printf` pour formater : une date, un prix, un pourcentage, un tableau de résultats aligné. Utilisez `number_format` avec séparateurs français.

**Exercice 7.2.8**

Écrivez le chiffrement de César (`cesar(string $s, int $decalage): string`) avec `ord`, `chr` et la conservation de la casse.

## 7.3 Traiter la saisie utilisateur

**Exercice 7.3.1**

Nettoyez une saisie : `trim`, suppression des espaces multiples (`preg_replace('/\s+/', ' ', ...)`), normalisation de la casse, suppression des caractères de contrôle. Écrivez `nettoyer(string $s): string`.

**Exercice 7.3.2**

Écrivez `valeurPost(string $cle, string $defaut = ''): string` qui lit `$_POST[$cle]` en sécurité, vérifie que c'est une chaîne (pas un tableau) et la nettoie. Pourquoi `$_POST['x']` peut-il être un tableau (`x[]`) ?

**Exercice 7.3.3**

Écrivez une fonction qui limite la longueur d'une saisie (`mb_substr`) et refuse les chaînes qui contiennent des octets invalides (`mb_check_encoding`).

## 7.4 Échappement

**Exercice 7.4.1**

Quels sont les contextes d'échappement : HTML, attribut HTML, URL, JavaScript, SQL, shell, expressions régulières ? Associez chaque contexte à la bonne fonction (`htmlspecialchars`, `urlencode`, `rawurlencode`, `json_encode`, requêtes préparées, `escapeshellarg`, `preg_quote`).

**Exercice 7.4.2**

Écrivez des exemples d'injection pour chaque contexte (HTML, SQL, shell) et la parade correspondante. Pourquoi l'échappement doit-il se faire à la sortie, selon le contexte, et non à l'entrée ?

**Exercice 7.4.3**

Utilisez `addslashes` et `stripslashes` : pourquoi `addslashes` est-il inadapté pour la sécurité SQL ? Quelle est la seule bonne protection ?

## 7.5 Échapper pour la sortie : `htmlspecialchars`

**Exercice 7.5.1**

Écrivez une fonction `e(string $s): string` qui appelle `htmlspecialchars($s, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8')`. Expliquez le rôle de chaque indicateur. Testez avec `<script>alert(1)</script>`, `"onmouseover="x"` dans un attribut, et `'`.

**Exercice 7.5.2**

Quelle différence entre `htmlspecialchars` et `htmlentities` ? Entre `htmlspecialchars` et `strip_tags` ? Pourquoi ne faut-il pas utiliser `strip_tags` comme protection XSS ?

**Exercice 7.5.3**

Écrivez un gabarit simple qui affiche un commentaire d'utilisateur de façon sûre, avec un lien construit à partir d'une saisie (`urlencode`) et un attribut (`e()`).

## 7.6 Comparer des chaînes

**Exercice 7.6.1**

Comparez avec `==`, `===`, `strcmp`, `strcasecmp`, `strncmp`, `strnatcmp`, `strnatcasecmp`. Quelles valeurs renvoient-elles ? Prédisez `"abc" == "ABC"`, `"10" == "1e1"`, `"abc" <=> "abd"`, `strcmp("a", "b")`.

**Exercice 7.6.2**

Comparez des chaînes accentuées (`Collator` / `strcoll`). Comparez des secrets avec `hash_equals`. Pourquoi une comparaison classique est-elle vulnérable aux attaques temporelles ?

**Exercice 7.6.3**

Mesurez la similarité de deux mots avec `similar_text`, `levenshtein`, `soundex`. Écrivez un correcteur simple qui propose le mot le plus proche d'un dictionnaire.

## 7.7 Chaînes et encodage

**Exercice 7.7.1**

Pourquoi UTF-8 est-il l'encodage à privilégier ? Utilisez `mb_internal_encoding`, `mb_detect_encoding`, `mb_convert_encoding`, `utf8_encode` (déprécié). Convertissez un texte de ISO-8859-1 vers UTF-8.

**Exercice 7.7.2**

Que produit une conversion incorrecte (« Ã© » à la place de « é ») ? Reproduisez le problème (affichage d'un fichier UTF-8 en Latin-1) et corrigez avec l'en-tête `Content-Type: text/html; charset=UTF-8` et la balise `<meta charset>`.

**Exercice 7.7.3**

Avec l'extension `intl`, utilisez `Normalizer::normalize` et `Transliterator` pour supprimer les accents d'un texte. Quelle différence entre formes NFC et NFD ?

---

# 8. Dates, heures et expressions régulières

*(Section ajoutée.)*

## 8.1 Dates et heures

**Exercice 8.1.1**

Créez des dates avec `new DateTimeImmutable('2026-10-11 14:30', new DateTimeZone('Europe/Paris'))`, `createFromFormat`, `'now'`, `'tomorrow'`, `'last day of next month'`. Pourquoi préférer `DateTimeImmutable` à `DateTime` ?

**Exercice 8.1.2**

Formatez une date au format `d/m/Y H:i`, `l j F Y`, `c`, `U`, `N`, `W`, `L`. Écrivez la table de correspondance de dix caractères de format.

**Exercice 8.1.3**

Ajoutez 30 jours, 2 mois, 1 an à une date avec `modify` et avec `add(new DateInterval('P1M2D'))`. Que renvoie `modify('+1 month')` à partir du 31 janvier ? Corrigez avec `last day of next month`.

**Exercice 8.1.4**

Calculez la différence entre deux dates avec `diff`, et lisez `days`, `y`, `m`, `d`, `invert`. Écrivez `age(string $naissance): int` et `joursAvantAnniversaire`.

**Exercice 8.1.5**

Convertissez une réunion de 14:30 à Antananarivo en heures de Paris, New York et Tokyo avec `setTimezone`. Que se passe-t-il autour d'un changement d'heure ?

**Exercice 8.1.6**

Utilisez `DatePeriod` pour lister tous les lundis d'un mois et les jours ouvrés entre deux dates. Écrivez `joursOuvres(DateTimeImmutable $debut, DateTimeImmutable $fin): int`.

**Exercice 8.1.7**

Écrivez un calendrier mensuel en HTML (tableau, semaines commençant le lundi) à partir d'un mois et d'une année.

**Exercice 8.1.8**

Utilisez `IntlDateFormatter` pour afficher une date en français (`dimanche 11 octobre 2026 à 14:30`) et en anglais. Quels avantages face à `strftime` (supprimé) et `date` ?

**Exercice 8.1.9**

Que fait `date_default_timezone_set` ? Pourquoi recommande-t-on de stocker les dates en UTC et de convertir à l'affichage ? Écrivez `versStockage()` et `versAffichage()`.

**Exercice 8.1.10**

Validez une date saisie par l'utilisateur : `DateTimeImmutable::createFromFormat('Y-m-d', $s)` et `getLastErrors()` pour refuser `2026-02-31`.

**Exercice 8.1.11**

Comparez les dates avec `<`, `>`, `==` (sur objets `DateTimeImmutable`). Triez un tableau de dates. Que renvoie `strtotime("garbage")` ?

## 8.2 Expressions régulières (PCRE)

**Exercice 8.2.1**

Utilisez `preg_match`, `preg_match_all`, `preg_replace`, `preg_replace_callback`, `preg_split`, `preg_quote`, `preg_grep`, `preg_last_error_msg`. Notez les types de retour de chacune.

**Exercice 8.2.2**

Écrivez les expressions régulières pour : un code postal français, un numéro de téléphone français, une date `JJ/MM/AAAA`, une couleur hexadécimale, un identifiant (lettres, chiffres, `_`, 3 à 16 caractères), une adresse IPv4 simple.

**Exercice 8.2.3**

Utilisez des groupes de capture nommés (`(?<annee>\d{4})`) pour extraire l'année, le mois et le jour d'une date. Utilisez `PREG_SET_ORDER` avec `preg_match_all`.

**Exercice 8.2.4**

Expliquez les drapeaux `i`, `m`, `s`, `u`, `x`. Pourquoi `u` est-il nécessaire pour du texte UTF-8 (`\p{L}`, `.` sur un caractère multi-octets) ?

**Exercice 8.2.5**

Écrivez `extraireHashtags`, `masquerCarte` (4 derniers chiffres), `camelVersSnake`, `snakeVersCamel`, `normaliserEspaces`. Écrivez un analyseur de journaux (`2026-10-21 14:03:05 [ERROR] Message`) avec groupes nommés.

**Exercice 8.2.6**

Pourquoi faut-il échapper une saisie utilisateur avec `preg_quote($saisie, '/')` avant de l'inclure dans une expression ? Écrivez une recherche de mot entier (`\b`) avec une saisie variable.

**Exercice 8.2.7**

Qu'est-ce que le retour sur trace catastrophique (ReDoS) ? Reproduisez-le avec `(a+)+$` et un texte de `aaaa…b`. Utilisez `preg_last_error()` et la limite `pcre.backtrack_limit`.

---

# 9. Formulaires et saisies utilisateur

## 9.1 Formulaire HTML et traitement

**Exercice 9.1.1**

Écrivez un formulaire HTML (nom, e-mail, message, bouton) qui envoie ses données en `POST` à un script PHP qui les affiche de façon sûre (`htmlspecialchars`). Testez avec le serveur intégré.

**Exercice 9.1.2**

Écrivez un script qui affiche `$_SERVER['REQUEST_METHOD']` et traite le formulaire seulement en `POST`. Que se passe-t-il à l'ouverture directe de la page (`GET`) ? Que contient `$_POST` ?

**Exercice 9.1.3**

Écrivez un formulaire avec tous les types de champs : texte, mot de passe, e-mail, nombre, date, case à cocher unique et multiple (`name="options[]"`), boutons radio, liste déroulante simple et multiple, zone de texte, champ caché. Affichez `$_POST` avec `print_r` et expliquez la forme de chaque donnée.

**Exercice 9.1.4**

Que se passe-t-il pour une case à cocher non cochée (absente de `$_POST`) ? Écrivez `estCochee(string $nom): bool`.

**Exercice 9.1.5**

Quelle différence entre `name` et `id` dans un champ ? Quel est le rôle de l'attribut `enctype="multipart/form-data"` ? Pourquoi un champ `disabled` n'est-il pas envoyé ?

## 9.2 `$_GET` ou `$_POST` ?

**Exercice 9.2.1**

Complétez le tableau comparatif `GET` / `POST` : usage, visibilité des données dans l'URL, taille, mise en favori, cache, idempotence, sécurité (jamais de secrets dans `GET`).

**Exercice 9.2.2**

Écrivez une page de recherche (`GET`, paramètre `q`, pagination `page`) avec une URL partageable. Utilisez `http_build_query` pour construire les liens de pagination en conservant les paramètres existants.

**Exercice 9.2.3**

Pourquoi faut-il éviter `$_REQUEST` ? Quel problème d'ambiguïté et de sécurité pose-t-il (cookies, `variables_order`) ?

## 9.3 Validation

**Exercice 9.3.1**

Écrivez un formulaire d'inscription (nom 2 à 50 caractères, e-mail valide, âge 18 à 120, mot de passe de 12 caractères minimum avec confirmation) et validez-le côté serveur. Affichez un message d'erreur sous chaque champ.

**Exercice 9.3.2**

Utilisez `filter_var` et `filter_input` avec `FILTER_VALIDATE_EMAIL`, `FILTER_VALIDATE_INT` (avec `options`), `FILTER_VALIDATE_FLOAT`, `FILTER_VALIDATE_URL`, `FILTER_VALIDATE_BOOLEAN` (avec `FILTER_NULL_ON_FAILURE`), `FILTER_VALIDATE_IP`, `FILTER_VALIDATE_REGEXP`.

**Exercice 9.3.3**

Écrivez une petite classe `Validateur` avec des règles (`requis`, `email`, `min`, `max`, `entre`, `regex`, `identique`) qui renvoie un tableau d'erreurs par champ. Écrivez des tests simples.

**Exercice 9.3.4**

Pourquoi `FILTER_SANITIZE_STRING` est-il déprécié (8.1) ? Quelle est la différence entre validation (accepter ou refuser), assainissement (nettoyer) et échappement (afficher)? Quelle approche privilégier ?

**Exercice 9.3.5**

Écrivez la validation d'une liste de cases à cocher (valeurs autorisées dans une liste blanche) et d'une liste déroulante (valeur parmi des options connues). Pourquoi ne faut-il pas se fier aux valeurs proposées par le HTML ?

**Exercice 9.3.6**

Validez un numéro de téléphone, un code postal, une date de naissance (pas dans le futur, pas plus de 120 ans) et une URL (schéma `http` ou `https` seulement). Quels pièges pour les adresses e-mail (internationalisation, longueur) ?

## 9.4 Validation côté client **et** côté serveur

**Exercice 9.4.1**

Ajoutez au formulaire des attributs de validation HTML5 (`required`, `type="email"`, `minlength`, `pattern`, `min`, `max`). Contournez-les avec les outils de développement ou `curl`. Qu'en déduisez-vous ?

**Exercice 9.4.2**

Envoyez une requête `POST` forgée avec `curl -d` et un champ non prévu, un champ manquant, un tableau à la place d'une chaîne. Votre script résiste-t-il ?

## 9.5 Motif Post/Redirect/Get (PRG)

**Exercice 9.5.1**

Reproduisez le problème de la double soumission (rafraîchir la page après un `POST`). Corrigez-le avec une redirection `header('Location: ...')` suivie de `exit`.

**Exercice 9.5.2**

Implémentez le motif PRG avec un message « flash » stocké en session et affiché une seule fois après la redirection.

**Exercice 9.5.3**

Quel code de statut HTTP utiliser pour la redirection après un `POST` (`303 See Other`, `302`) ? Pourquoi `exit` est-il nécessaire après `header('Location: ...')` ?

## 9.6 Pré-remplir un formulaire après erreur

**Exercice 9.6.1**

Réaffichez le formulaire avec les valeurs saisies (échappées) après une erreur de validation, y compris pour les cases à cocher, boutons radio et listes déroulantes. Ne pré-remplissez jamais un champ mot de passe.

**Exercice 9.6.2**

Écrivez une fonction `ancienneValeur(string $cle, string $defaut = ''): string` qui lit une valeur en session ou dans `$_POST` et l'échappe. Où l'utiliser dans le gabarit ?

## 9.7 Protection CSRF

**Exercice 9.7.1**

Expliquez l'attaque CSRF avec un scénario (une page malveillante qui soumet un formulaire à votre site). Pourquoi un utilisateur connecté est-il vulnérable ?

**Exercice 9.7.2**

Générez un jeton avec `bin2hex(random_bytes(32))`, stockez-le en session, insérez-le dans un champ caché et vérifiez-le avec `hash_equals` à la réception. Écrivez `genererJeton()` et `verifierJeton()`.

**Exercice 9.7.3**

Quelles autres protections existent (attribut de cookie `SameSite`, en-tête `Origin`, jetons à usage unique) ? Quand un jeton doit-il être renouvelé ?

---

# 10. Système de fichiers

## 10.1 Lire et écrire rapidement

**Exercice 10.1.1**

Écrivez un programme qui crée un fichier `notes.txt` avec `file_put_contents`, y ajoute des lignes avec le drapeau `FILE_APPEND | LOCK_EX`, puis le relit avec `file_get_contents`. Que renvoient ces fonctions en cas d'échec ?

**Exercice 10.1.2**

Lisez un fichier de trois façons : `file_get_contents`, `file` (avec `FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES`), `readfile`. Pour chacune, notez le type du résultat et le cas d'usage.

**Exercice 10.1.3**

Écrivez un compteur de visites persistant dans un fichier. Quel problème de concurrence apparaît quand deux requêtes écrivent simultanément ? Corrigez avec `flock`.

**Exercice 10.1.4**

Écrivez un petit journal d'événements (`journaliser(string $niveau, string $message)`) qui ajoute une ligne horodatée à un fichier. Faites-le tourner par jour (nom de fichier contenant la date).

## 10.2 Lecture et écriture avec `fopen`

**Exercice 10.2.1**

Décrivez tous les modes de `fopen` (`r`, `r+`, `w`, `w+`, `a`, `a+`, `x`, `c`, avec `b`). Pour chacun : lecture, écriture, création, troncature, position initiale.

**Exercice 10.2.2**

Lisez un fichier ligne par ligne avec `fgets` dans une boucle `while (($ligne = fgets($f)) !== false)`. Pourquoi cette approche consomme-t-elle peu de mémoire ? Comptez les lignes, mots et caractères (comme `wc`).

**Exercice 10.2.3**

Utilisez `fread`, `fwrite`, `fgetc`, `feof`, `fseek`, `ftell`, `rewind`, `ftruncate`, `fflush`, `fclose`. Lisez les 10 derniers octets d'un fichier. Pourquoi faut-il toujours tester la valeur renvoyée par `fopen` ?

**Exercice 10.2.4**

Écrivez une fonction `dernieresLignes(string $chemin, int $n): array` qui renvoie les `n` dernières lignes d'un gros fichier sans le charger entièrement (lecture à rebours avec `fseek`).

**Exercice 10.2.5**

Utilisez `flock(LOCK_SH)` et `flock(LOCK_EX)` pour verrouiller en lecture et en écriture. Qu'est-ce qu'un verrou consultatif ?

**Exercice 10.2.6**

Utilisez les flux spéciaux `php://stdin`, `php://stdout`, `php://stderr`, `php://memory`, `php://temp`, `php://input`. Écrivez des exemples pour deux d'entre eux.

## 10.3 Fonctions utiles

**Exercice 10.3.1**

Utilisez `file_exists`, `is_file`, `is_dir`, `is_readable`, `is_writable`, `filesize`, `filemtime`, `touch`, `copy`, `rename`, `unlink`, `mkdir` (récursif), `rmdir`, `scandir`, `glob`, `tempnam`, `sys_get_temp_dir`, `disk_free_space`.

**Exercice 10.3.2**

Utilisez `pathinfo`, `basename`, `dirname`, `realpath`, `DIRECTORY_SEPARATOR`. Extrayez le nom, l'extension et le dossier de `/var/www/site/archive.tar.gz`. Pourquoi `realpath` est-il utile contre les traversées de répertoires ?

**Exercice 10.3.3**

Écrivez `listerFichiers(string $dossier, string $extension): array` avec `glob`, puis la version récursive avec `RecursiveDirectoryIterator`.

**Exercice 10.3.4**

Écrivez `tailleDossier(string $chemin): int` récursive et `supprimerDossier(string $chemin)` qui supprime un dossier non vide. Quelles précautions (ne jamais supprimer un chemin fourni par l'utilisateur sans validation) ?

**Exercice 10.3.5**

Écrivez un petit programme de rangement : déplacer les fichiers d'un dossier dans des sous-dossiers selon leur extension, avec un mode « simulation ».

## 10.4 CSV et JSON

**Exercice 10.4.1**

Écrivez un fichier CSV de cinq personnes avec `fputcsv`, puis relisez-le avec `fgetcsv`. Gérez un séparateur `;` et des champs contenant des virgules, des guillemets et des retours à la ligne.

**Exercice 10.4.2**

Lisez un CSV avec en-tête et construisez un tableau associatif par ligne (`array_combine`). Calculez la moyenne d'une colonne, filtrez des lignes, réécrivez le résultat dans un nouveau fichier. Utilisez un générateur pour un gros fichier.

**Exercice 10.4.3**

Écrivez un tableau associatif dans un fichier JSON (`json_encode` avec `JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES`) puis relisez-le avec `json_decode` (en tableau et en objet). Utilisez `JSON_THROW_ON_ERROR`.

**Exercice 10.4.4**

Écrivez un carnet d'adresses persistant en JSON (ajout, recherche, suppression, sauvegarde atomique par écriture dans un fichier temporaire puis `rename`).

**Exercice 10.4.5**

Convertissez un fichier CSV en JSON et inversement. Que se passe-t-il pour les types (nombres lus comme chaînes) ?

**Exercice 10.4.6**

Exportez des données en CSV vers le navigateur avec les en-têtes `Content-Type: text/csv` et `Content-Disposition: attachment`, en écrivant sur `php://output`. Pourquoi ajouter un BOM UTF-8 pour Excel ?

## 10.5 Classes SPL

**Exercice 10.5.1**

Utilisez `SplFileObject` pour lire un fichier ligne par ligne, avec les drapeaux `READ_CSV`, `SKIP_EMPTY`, `DROP_NEW_LINE`. Utilisez `SplFileInfo` pour lire les métadonnées.

**Exercice 10.5.2**

Utilisez `DirectoryIterator`, `FilesystemIterator`, `RecursiveDirectoryIterator`, `RecursiveIteratorIterator`, `GlobIterator` pour lister les fichiers `.php` d'un projet avec leur taille.

**Exercice 10.5.3**

Utilisez `SplQueue`, `SplStack`, `SplPriorityQueue`, `SplObjectStorage`, `ArrayObject`, `SplFixedArray` pour trois petits problèmes (file d'attente, pile d'annulation, tâches prioritaires).

## 10.6 Téléversement sécurisé de fichiers

**Exercice 10.6.1**

Écrivez un formulaire de téléversement d'image (`enctype="multipart/form-data"`, `<input type="file">`) et le script qui lit `$_FILES`. Décrivez chaque clé : `name`, `type`, `tmp_name`, `error`, `size`.

**Exercice 10.6.2**

Vérifiez l'erreur de téléversement (`UPLOAD_ERR_OK`, `UPLOAD_ERR_INI_SIZE`, `UPLOAD_ERR_FORM_SIZE`, `UPLOAD_ERR_PARTIAL`, `UPLOAD_ERR_NO_FILE`, …) et affichez un message adapté à chaque code. Quelles directives de `php.ini` limitent la taille (`upload_max_filesize`, `post_max_size`, `max_file_uploads`) ?

**Exercice 10.6.3**

Écrivez la validation sécurisée d'un fichier : taille maximale, type réel détecté avec `finfo` (et non `$_FILES['type']` ni l'extension), liste blanche d'extensions, `getimagesize` pour une image, `is_uploaded_file`, nom généré aléatoirement, stockage hors de la racine web, droits restreints, `move_uploaded_file`.

**Exercice 10.6.4**

Pourquoi ne faut-il jamais utiliser le nom d'origine du fichier, ni faire confiance à l'extension ou au type MIME envoyé par le client ? Écrivez un exemple de téléversement de `shell.php.jpg` ou d'un fichier PHP renommé en image, et la parade.

**Exercice 10.6.5**

Servez les fichiers téléversés via un script PHP qui vérifie les droits et envoie les bons en-têtes, plutôt que d'y donner un accès direct. Écrivez ce script (`readfile`, `Content-Type`, `X-Content-Type-Options: nosniff`).

**Exercice 10.6.6**

Écrivez une version avec téléversements multiples (`name="fichiers[]"`) et une barre de progression. Comment réorganiser la structure déroutante de `$_FILES` pour les champs multiples ?

## 10.7 Précautions

**Exercice 10.7.1**

Écrivez un exemple de traversée de répertoires (`../../etc/passwd`) dans une fonction qui lit un fichier à partir d'un nom fourni par l'utilisateur. Corrigez avec `basename`, `realpath` et la vérification que le chemin reste dans un dossier autorisé.

**Exercice 10.7.2**

Quelles autres précautions s'appliquent (droits des fichiers, `open_basedir`, fichiers temporaires, octet nul, suppression de fichiers sur entrée utilisateur, sauvegardes accessibles par le web comme `.env`, `.git`, `*.bak`) ? Dressez une liste de contrôle.

**Exercice 10.7.3**

Que se passe-t-il quand le disque est plein ou que les droits sont insuffisants ? Écrivez une fonction d'écriture robuste qui gère toutes les erreurs et lève des exceptions.

---

# 11. Sessions et cookies

## 11.1 Principe

**Exercice 11.1.1**

Expliquez pourquoi HTTP est « sans état » et comment les cookies et les sessions permettent de reconnaître un visiteur. Dessinez les échanges entre navigateur et serveur pour une session (identifiant dans un cookie, données côté serveur).

**Exercice 11.1.2**

Complétez le tableau comparatif cookies / sessions : lieu de stockage, taille, sécurité, durée de vie, accessible par JavaScript, envoyé à chaque requête.

## 11.2 Sessions

**Exercice 11.2.1**

Écrivez un compteur de visites par session avec `session_start()` et `$_SESSION`. Observez le cookie `PHPSESSID` dans les outils de développement. Où PHP stocke-t-il les données de session par défaut (`session.save_path`) ?

**Exercice 11.2.2**

Écrivez un panier d'achat en session : ajout d'un produit (avec quantité), modification, suppression, total, vidage. Validez toutes les entrées.

**Exercice 11.2.3**

Pourquoi `session_start()` doit-il être appelé avant toute sortie ? Que se passe-t-il sinon ? Quelle différence entre `session_start`, `session_status`, `session_id`, `session_regenerate_id`, `session_destroy`, `session_unset` ?

**Exercice 11.2.4**

Écrivez un système de connexion simple : formulaire, vérification d'identifiants (tableau d'utilisateurs avec mots de passe hachés), stockage de l'identifiant en session, page protégée, déconnexion.

### Déconnexion complète

**Exercice 11.2.5**

Écrivez une déconnexion complète : vider `$_SESSION`, supprimer le cookie de session (`setcookie` avec expiration passée et mêmes paramètres), `session_destroy()`. Pourquoi `session_destroy()` seul ne suffit-il pas ?

**Exercice 11.2.6**

Utilisez des messages « flash » en session (affichés une seule fois). Écrivez `flash(string $cle, ?string $message = null): ?string`.

**Exercice 11.2.7**

Écrivez un délai d'inactivité : déconnecter l'utilisateur après 15 minutes sans activité (`$_SESSION['derniere_activite']`), et une durée de vie absolue maximale.

## 11.3 Cookies *(à jour : tableau d'options)*

**Exercice 11.3.1**

Créez, lisez et supprimez un cookie avec `setcookie` en utilisant la signature à tableau d'options (`expires`, `path`, `domain`, `secure`, `httponly`, `samesite`). Pourquoi la lecture se fait-elle à la requête suivante ?

**Exercice 11.3.2**

Écrivez un cookie de préférence (thème clair/sombre) valable 30 jours. Pourquoi un cookie ne doit-il jamais contenir d'informations sensibles en clair ? Que faire pour des données qu'on veut protéger de la modification (signature `hash_hmac`) ?

**Exercice 11.3.3**

Écrivez les fonctions `ecrireCookieSigne(string $nom, string $valeur)` et `lireCookieSigne(string $nom): ?string` avec HMAC pour détecter toute altération. Utilisez `hash_equals`.

**Exercice 11.3.4**

Écrivez un bandeau de consentement aux cookies qui mémorise le choix et conditionne l'activation de traceurs. Quelles obligations légales (RGPD) s'appliquent ?

## 11.4 Sécuriser les sessions

**Exercice 11.4.1**

Configurez les paramètres de session sécurisés : `session.use_strict_mode`, `session.cookie_httponly`, `session.cookie_secure`, `session.cookie_samesite`, `session.use_only_cookies`, `session.gc_maxlifetime`. Écrivez la configuration avec `session_set_cookie_params` ou `ini_set`.

**Exercice 11.4.2**

Qu'est-ce que la fixation de session ? Montrez-la avec un identifiant imposé dans l'URL. Corrigez avec `session_regenerate_id(true)` à chaque changement de privilège (connexion).

**Exercice 11.4.3**

Qu'est-ce que le détournement de session (vol de cookie) ? Quelles contre-mesures : HTTPS, `HttpOnly`, `Secure`, régénération de l'identifiant, expiration, liaison à l'agent utilisateur (limitée) ?

**Exercice 11.4.4**

Implémentez un gestionnaire de session personnalisé qui stocke les sessions en base de données (`SessionHandlerInterface`) ou dans Redis. Quand est-ce utile (plusieurs serveurs) ?

**Exercice 11.4.5**

Écrivez une fonction `exigerConnexion()` qui redirige vers la page de connexion si l'utilisateur n'est pas authentifié et vérifie aussi un rôle (`exigerRole('admin')`). Pourquoi faut-il vérifier côté serveur à chaque requête ?

---

# 12. Bases de données avec PDO

## 12.1 PDO ou MySQLi ?

**Exercice 12.1.1**

Complétez le tableau comparatif PDO / MySQLi : bases prises en charge, paramètres nommés, style objet et procédural, requêtes préparées, migration entre SGBD. Pourquoi recommande-t-on PDO ?

**Exercice 12.1.2**

Vérifiez les pilotes disponibles avec `PDO::getAvailableDrivers()` et installez celui de votre base (MySQL, PostgreSQL, SQLite). Pourquoi SQLite est-il pratique pour les exercices (aucun serveur à installer) ?

## 12.2 Connexion avec PDO

**Exercice 12.2.1**

Écrivez une fonction `connexion(): PDO` qui se connecte avec un DSN, un utilisateur et un mot de passe lus depuis des variables d'environnement, avec les options `ERRMODE_EXCEPTION`, `FETCH_ASSOC`, `EMULATE_PREPARES => false`, charset `utf8mb4`.

**Exercice 12.2.2**

Pourquoi ne faut-il pas écrire les identifiants de la base directement dans le code source ? Où les stocker (variables d'environnement, fichier `.env` hors de la racine web, gestionnaire de secrets) ?

**Exercice 12.2.3**

Gérez l'échec de la connexion avec `try/catch (PDOException $e)` sans divulguer le mot de passe dans le message affiché. Que faut-il journaliser et que faut-il montrer à l'utilisateur ?

**Exercice 12.2.4**

Écrivez un petit script qui se connecte à une base SQLite en mémoire (`sqlite::memory:`), crée une table `clients` et affiche son contenu.

## 12.3 Requêtes préparées (anti-injection SQL)

**Exercice 12.3.1**

Montrez une injection SQL sur une requête construite par concaténation (`"SELECT * FROM users WHERE nom = '$nom'"` avec `' OR '1'='1`). Écrivez la version avec requête préparée (paramètres positionnels `?` puis nommés `:nom`).

**Exercice 12.3.2**

Utilisez `prepare`, `execute`, `bindValue`, `bindParam` (avec `PDO::PARAM_INT`, `PARAM_STR`, `PARAM_BOOL`, `PARAM_NULL`). Quelle différence entre `bindValue` et `bindParam` ? Comment lier une valeur `LIMIT` entière ?

**Exercice 12.3.3**

Utilisez `fetch`, `fetchAll`, `fetchColumn`, `fetchObject`, `fetchAll(PDO::FETCH_KEY_PAIR)`, `fetchAll(PDO::FETCH_GROUP)`, `FETCH_CLASS`. Écrivez un exemple de chacun.

**Exercice 12.3.4**

Expliquez pourquoi les requêtes préparées protègent de l'injection (séparation de la structure et des données). Les requêtes préparées protègent-elles contre XSS ? Contre les noms de colonnes dynamiques ?

### Clause `IN` dynamique

**Exercice 12.3.5**

Écrivez `trouverParIds(PDO $pdo, array $ids): array` qui construit dynamiquement les marqueurs `?, ?, ?` (`str_repeat`, `implode`). Gérez le cas du tableau vide.

### Noms de tables / colonnes dynamiques

**Exercice 12.3.6**

Écrivez `trier(PDO $pdo, string $colonne, string $sens)` : les identifiants ne peuvent pas être des paramètres liés. Validez avec une liste blanche (`in_array`) et échappez avec des accents graves seulement après validation.

**Exercice 12.3.7**

Écrivez un constructeur de requêtes minimal (filtres facultatifs, tri, pagination) qui génère du SQL paramétré sans jamais concaténer de saisies utilisateur. *(défi)*

## 12.4 Opérations CRUD

**Exercice 12.4.1**

Créez la table `articles` (`id`, `titre`, `contenu`, `auteur_id`, `cree_le`). Écrivez les fonctions `creer`, `lire`, `lister`, `modifier`, `supprimer` avec requêtes préparées. Utilisez `lastInsertId()` et `rowCount()`.

**Exercice 12.4.2**

Écrivez une page de liste paginée (`LIMIT` / `OFFSET`, nombre total avec `COUNT(*)`, liens de pagination). Quels problèmes de performance pour un `OFFSET` très grand ? Proposez la pagination par curseur (clé précédente).

**Exercice 12.4.3**

Écrivez une recherche par mot-clé (`LIKE`) en échappant les caractères `%` et `_` de la saisie. Utilisez `LIKE :terme ESCAPE '\\'`.

**Exercice 12.4.4**

Écrivez une jointure (`articles` et `utilisateurs`), un regroupement (`COUNT`, `GROUP BY`) et une sous-requête. Récupérez le résultat sous forme de tableau imbriqué (articles avec leur auteur).

**Exercice 12.4.5**

Écrivez un petit dépôt `ArticleRepository` (classe) avec une interface, qui encapsule toutes les requêtes. Écrivez des tests sur SQLite en mémoire.

**Exercice 12.4.6**

Gérez la suppression « douce » (colonne `supprime_le`) et les horodatages (`cree_le`, `modifie_le`). Écrivez les requêtes adaptées.

**Exercice 12.4.7**

Gérez les contraintes d'unicité : insérez deux fois le même e-mail et interceptez l'erreur (`PDOException`, code SQLSTATE `23000`). Affichez un message clair sans divulguer la structure de la base.

## 12.5 Transactions

**Exercice 12.5.1**

Écrivez un virement bancaire : débiter un compte et en créditer un autre dans une transaction (`beginTransaction`, `commit`, `rollBack`) avec `try/catch`. Simulez une erreur au milieu et vérifiez l'annulation.

**Exercice 12.5.2**

Expliquez les propriétés ACID. Que se passe-t-il quand une exception survient entre deux requêtes sans transaction ? Quel moteur de stockage MySQL est transactionnel (InnoDB) ?

**Exercice 12.5.3**

Écrivez `avecTransaction(PDO $pdo, callable $travail): mixed` qui exécute le travail dans une transaction et annule en cas d'exception.

**Exercice 12.5.4**

Utilisez un verrou de ligne (`SELECT ... FOR UPDATE`) pour éviter une double vente du dernier article en stock. Décrivez la condition de concurrence sans transaction ni verrou.

## 12.6 MySQLi (rappel)

**Exercice 12.6.1**

Écrivez la même requête préparée en MySQLi (style objet) : `prepare`, `bind_param` (types `s`, `i`, `d`, `b`), `execute`, `get_result`, `fetch_assoc`. Comparez la longueur et la lisibilité avec PDO.

**Exercice 12.6.2**

Activez les exceptions pour MySQLi avec `mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT)`. Pourquoi cela évite-t-il les erreurs silencieuses ?

## 12.7 Bonnes pratiques

**Exercice 12.7.1**

Listez cinq bonnes pratiques d'accès aux données (requêtes préparées, exceptions, droits minimaux de l'utilisateur de la base, transactions, ne pas exposer les erreurs SQL) et corrigez ce code :

```php
<?php
$c = mysqli_connect("localhost", "root", "", "site");
$r = mysqli_query($c, "SELECT * FROM users WHERE id = " . $_GET['id']);
while ($l = mysqli_fetch_assoc($r)) {
    echo "<p>" . $l['nom'] . "</p>";
}
```

**Exercice 12.7.2**

Mini-projet : un blog minimal (inscription, connexion, création et modification d'articles, commentaires) avec PDO, sessions, validation, CSRF et échappement de toutes les sorties.

---

# 13. Gestion des erreurs et exceptions

## 13.1 Types d'erreurs

**Exercice 13.1.1**

Provoquez volontairement une erreur de chaque niveau : `E_NOTICE` / `E_WARNING` (variable non définie, division, fichier absent), `E_DEPRECATED`, `E_ERROR` (erreur fatale), `E_PARSE` (erreur de syntaxe). Notez le message pour chacune.

**Exercice 13.1.2**

Quelle différence entre une erreur (traditionnelle) et une exception ? Quelles erreurs fatales de PHP 5 sont devenues des exceptions `Error` en PHP 7 (`TypeError`, `DivisionByZeroError`, `ArgumentCountError`, `ValueError`) ? Provoquez chacune.

**Exercice 13.1.3**

Écrivez un tableau qui associe les constantes `E_*` (`E_ALL`, `E_STRICT`, `E_USER_ERROR`, `E_USER_WARNING`, `E_USER_NOTICE`, `E_USER_DEPRECATED`) à leur sens. Déclenchez des erreurs utilisateur avec `trigger_error`.

## 13.2 Hiérarchie : `Throwable`

**Exercice 13.2.1**

Dessinez la hiérarchie `Throwable` → `Error` / `Exception` et leurs sous-classes (`TypeError`, `ValueError`, `ArithmeticError`, `DivisionByZeroError`, `ErrorException`, `LogicException`, `InvalidArgumentException`, `DomainException`, `LengthException`, `OutOfRangeException`, `RuntimeException`, `OutOfBoundsException`, `OverflowException`, `RangeException`, `UnexpectedValueException`, `JsonException`).

**Exercice 13.2.2**

Quelle différence conceptuelle entre `LogicException` (erreur du programmeur) et `RuntimeException` (erreur d'exécution imprévisible) ? Classez dix situations selon cette distinction.

**Exercice 13.2.3**

Pourquoi attraper `Throwable` est-il parfois justifié (gestionnaire global) et `Exception` insuffisant pour attraper un `TypeError` ? Écrivez les deux cas.

## 13.3 `try` / `catch` / `finally`

**Exercice 13.3.1**

Écrivez `diviser(int $a, int $b): float` qui lève une exception pour `$b === 0`. Attrapez-la. Écrivez plusieurs blocs `catch`, et un bloc `catch (A | B $e)` (types multiples).

**Exercice 13.3.2**

Prédisez la sortie, puis expliquez le rôle de `finally` (y compris avec `return`) :

```php
<?php
function f(): string {
    try {
        echo "try\n";
        return "retour try";
    } catch (Exception $e) {
        echo "catch\n";
    } finally {
        echo "finally\n";
    }
}
echo f(), PHP_EOL;

function g(): string {
    try { return "a"; } finally { return "b"; }
}
echo g(), PHP_EOL;
```

**Exercice 13.3.3**

Utilisez `catch (Exception)` sans variable (8.0). Quand est-ce légitime ? Propagez une exception en la relançant (`throw $e`) après avoir journalisé.

**Exercice 13.3.4**

Écrivez un `finally` qui libère une ressource (fichier, verrou, connexion) même en cas d'erreur. Que se passe-t-il pour les exceptions levées dans un `finally` ?

## 13.4 Lancer et créer des exceptions

**Exercice 13.4.1**

Écrivez `racine(float $x): float` qui lève `InvalidArgumentException` si `$x < 0`, `validerAge(mixed $age): int` qui lève `TypeError` ou `RangeException` selon le cas. Quand choisir quelle exception standard ?

**Exercice 13.4.2**

Définissez une hiérarchie d'exceptions personnalisées : `ErreurApplication`, `ErreurValidation` (avec les erreurs par champ), `ErreurBaseDeDonnees`, `UtilisateurIntrouvable` (avec l'identifiant). Ajoutez des propriétés et un constructeur.

**Exercice 13.4.3**

Utilisez le chaînage d'exceptions avec le troisième paramètre (`$previous`) : capturez une `PDOException` et lancez une exception métier qui la contient. Parcourez la chaîne avec `getPrevious()`.

**Exercice 13.4.4**

Affichez les informations d'une exception : `getMessage`, `getCode`, `getFile`, `getLine`, `getTrace`, `getTraceAsString`, `__toString`. Écrivez une fonction `decrire(Throwable $e): string` lisible.

**Exercice 13.4.5**

Utilisez `throw` comme expression (8.0) : `$valeur = $_GET['x'] ?? throw new InvalidArgumentException("x requis");` et dans une fonction fléchée.

**Exercice 13.4.6**

Écrivez `ErreurValidation::deLaListe(array $erreurs): self` (constructeur nommé) et gérez-la dans un contrôleur pour afficher les erreurs sous chaque champ.

## 13.5 Configuration et journalisation

**Exercice 13.5.1**

Configurez `display_errors`, `log_errors`, `error_log`, `error_reporting` pour le développement et la production. Pourquoi `display_errors` doit-il être désactivé en production ? Testez avec `ini_set`.

**Exercice 13.5.2**

Écrivez dans le journal avec `error_log("message")`, `error_log($message, 3, "/chemin/app.log")`. Utilisez Monolog avec des niveaux (debug, info, warning, error) et des gestionnaires (fichier, sortie d'erreur).

**Exercice 13.5.3**

Écrivez un journal structuré (JSON) avec contexte (identifiant de requête, utilisateur, adresse IP) et une rotation quotidienne. Que ne faut-il jamais journaliser (mots de passe, numéros de carte, jetons) ?

## 13.6 Gestionnaires globaux

**Exercice 13.6.1**

Installez un gestionnaire d'exceptions global avec `set_exception_handler` qui affiche une page d'erreur générique et journalise le détail. Que se passe-t-il pour une exception non attrapée sans gestionnaire ?

**Exercice 13.6.2**

Convertissez les erreurs PHP en exceptions avec `set_error_handler` et `ErrorException`. Pourquoi cela simplifie-t-il la gestion ? Quelles erreurs ne passent pas par le gestionnaire (fatales, de compilation) ?

**Exercice 13.6.3**

Utilisez `register_shutdown_function` et `error_get_last()` pour détecter une erreur fatale et produire une réponse propre. Écrivez une page 500 qui n'expose aucun détail interne.

**Exercice 13.6.4**

Restaurez les gestionnaires précédents avec `restore_error_handler` et `restore_exception_handler`. Dans quel cas est-ce utile (tests, bibliothèques) ?

## 13.7 Bonnes pratiques

**Exercice 13.7.1**

Listez cinq bonnes pratiques de gestion des erreurs (lancer des exceptions précises, ne jamais avaler une erreur, ne pas utiliser `@`, journaliser, traiter au bon niveau) et corrigez ces exemples :

```php
<?php
$f = @fopen("absent.txt", "r");

try { traiter(); } catch (Exception $e) {}

function lire($c) { return file_get_contents($c) or die("erreur"); }

throw new Exception("Erreur");
```

**Exercice 13.7.2**

Écrivez un utilitaire `reessayer(callable $f, int $tentatives, int $delaiMs)` qui relance une opération en cas d'exception, avec attente exponentielle, et lève une exception finale chaînant la dernière erreur.

---

# 14. Programmation orientée objet

## 14.1 Classes et objets

**Exercice 14.1.1**

Écrivez une classe `Rectangle` avec des propriétés typées `largeur` et `hauteur`, un constructeur, des méthodes `aire()` et `perimetre()` et une méthode `__toString()`. Instanciez-la avec `new` et utilisez `$this`.

**Exercice 14.1.2**

Quelle différence entre une classe, un objet et une instance ? Que renvoient `get_class`, `$o instanceof Classe`, `get_object_vars`, `method_exists`, `property_exists` ?

**Exercice 14.1.3**

Écrivez une classe `Compteur` avec une propriété `private int $valeur = 0` et des méthodes fluides (`incrementer(): static`, `decrementer(): static`) qui permettent le chaînage (`$c->incrementer()->incrementer()`).

**Exercice 14.1.4**

Écrivez une classe `Pile` (LIFO) et une classe `File` (FIFO) avec `empiler`/`enfiler`, `depiler`/`defiler`, `estVide`, `taille`. Gérez l'erreur de retrait sur une structure vide par une exception.

**Exercice 14.1.5**

Écrivez une classe `Fraction` immuable avec simplification automatique, addition, multiplication, comparaison et `__toString`.

## 14.2 Promotion de propriétés du constructeur *(8.0, à jour)*

**Exercice 14.2.1**

Réécrivez avec la promotion de propriétés cette classe :

```php
<?php
class Personne {
    private string $nom;
    private int $age;
    public function __construct(string $nom, int $age) {
        $this->nom = $nom;
        $this->age = $age;
    }
}
```

**Exercice 14.2.2**

Combinez promotion, valeurs par défaut, `readonly` (8.1), et `new` dans un initialiseur (8.1) : `public function __construct(private readonly Logger $log = new NullLogger())`. Quelles sont les limites (promotion interdite dans les constructeurs abstraits et d'interface) ? *(8.1)*

**Exercice 14.2.3**

Utilisez les classes `readonly` (8.2) pour définir un objet de valeur `Argent` (montant, devise) avec une méthode `ajouter()` qui renvoie un nouvel objet. Que se passe-t-il à la modification d'une propriété ? *(8.2)*

## 14.3 Visibilité

**Exercice 14.3.1**

Écrivez une classe `CompteBancaire` avec un solde `private`, des méthodes publiques `deposer`, `retirer` (refus si solde insuffisant), et un accesseur `getSolde()`. Montrez les erreurs obtenues en accédant au solde de l'extérieur.

**Exercice 14.3.2**

Complétez le tableau de visibilité `public` / `protected` / `private` : accès depuis la classe, une classe fille, l'extérieur. Écrivez un exemple pour chaque combinaison.

**Exercice 14.3.3**

Utilisez la visibilité asymétrique (`public private(set) int $solde`) pour exposer une propriété en lecture publique et en écriture privée. Comparez avec `readonly` et avec un getter. *(8.4)*

**Exercice 14.3.4**

Utilisez les propriétés typées avec valeur par défaut, les propriétés non initialisées (`Typed property must not be accessed before initialization`) et le mot-clé `readonly`. Provoquez l'erreur et corrigez.

## 14.4 Hooks de propriétés *(8.4, à jour)*

**Exercice 14.4.1**

Écrivez une classe `Personne` avec une propriété virtuelle `nomComplet` en lecture (`get =>`) et une propriété `email` avec un hook `set` qui valide et normalise l'adresse. *(8.4)*

**Exercice 14.4.2**

Écrivez une classe `Temperature` avec `celsius` stocké et `fahrenheit` calculé en lecture et en écriture. Que se passe-t-il à l'écriture d'une propriété virtuelle sans hook `set` ? *(8.4)*

**Exercice 14.4.3**

Réécrivez une classe qui possède des getters et setters écrits à la main (`getNom`, `setNom` avec validation) avec des hooks. Quels avantages (moins de code, compatibilité de l'API) ? *(8.4)*

**Exercice 14.4.4**

Utilisez les hooks dans une interface (propriété déclarée `public string $nom { get; }`) et dans une classe abstraite. *(8.4)*

## 14.5 Héritage

**Exercice 14.5.1**

Écrivez `Animal` (nom, `parler()`), `Chien`, `Chat` qui redéfinissent `parler()`. Utilisez `parent::__construct()`. Montrez le polymorphisme avec un tableau d'animaux.

**Exercice 14.5.2**

Écrivez une hiérarchie `Employe` → `Manager`, `Developpeur` avec un salaire calculé différemment, et une fonction qui calcule la masse salariale. Utilisez `instanceof` pour tester les sous-types.

**Exercice 14.5.3**

Utilisez `final` sur une classe et sur une méthode. Quand l'utiliser ? Utilisez l'attribut `#[\Override]` (8.3) pour garantir qu'une méthode redéfinit bien une méthode du parent. *(8.3)*

**Exercice 14.5.4**

Quelles sont les règles de compatibilité pour une méthode redéfinie (types des paramètres contravariants, type de retour covariant, visibilité non réduite) ? Écrivez un exemple valide et un exemple invalide.

**Exercice 14.5.5**

Quel est l'ordre d'appel des constructeurs en cas d'héritage ? Que se passe-t-il si le constructeur de la classe fille n'appelle pas `parent::__construct()` ?

## 14.6 Membres statiques et constantes

**Exercice 14.6.1**

Écrivez une classe avec une propriété statique compteur d'instances, une méthode statique, une constante de classe et une constante typée (8.3). Accédez-y avec `::`, `self::`, `static::`. *(8.3)*

**Exercice 14.6.2**

Quelle différence entre `self::` et `static::` (liaison statique tardive) ? Écrivez deux classes qui illustrent la différence avec une méthode de fabrique `creer()`.

**Exercice 14.6.3**

Écrivez le patron Singleton avec un constructeur privé, `__clone` privé et `getInstance()`. Pourquoi ce patron est-il critiqué (état global, tests) ? Proposez l'injection de dépendances à la place.

**Exercice 14.6.4**

Utilisez les constantes de classe `final` et les constantes d'énumération. Utilisez `Classe::class`, `static::class`, `$objet::class` pour obtenir le nom d'une classe.

## 14.7 Classes abstraites, interfaces et traits

**Exercice 14.7.1**

Écrivez une classe abstraite `Forme` avec une méthode abstraite `aire(): float` et une méthode concrète `decrire(): string`. Écrivez `Cercle` et `Carre`. Que se passe-t-il quand on instancie `Forme` ?

**Exercice 14.7.2**

Écrivez une interface `Exportable` (`exporter(): string`) et deux classes qui l'implémentent (CSV, JSON). Utilisez-la comme type de paramètre. Une classe peut-elle implémenter plusieurs interfaces ? En étendre plusieurs ?

**Exercice 14.7.3**

Écrivez un trait `Horodate` (propriétés `creeLe` et `modifieLe`, méthode `toucher()`) et un trait `Journalise`. Utilisez-les dans deux classes. Que se passe-t-il en cas de conflit de noms (`insteadof`, `as`) ?

**Exercice 14.7.4**

Complétez le tableau comparatif classe abstraite / interface / trait : état, héritage multiple, code partagé, constantes, usage typique.

**Exercice 14.7.5**

Utilisez les interfaces standard `Stringable`, `Countable`, `ArrayAccess`, `IteratorAggregate`, `JsonSerializable`. Écrivez une classe `Collection` qui les implémente et l'utilise comme un tableau.

**Exercice 14.7.6**

Écrivez un exemple de « programmer contre une interface » : une classe `Commande` qui dépend d'une interface `Paiement` avec deux implémentations (réelle et factice pour les tests).

## 14.8 Énumérations *(8.1, ajout)*

**Exercice 14.8.1**

Écrivez une énumération pure `Statut { Brouillon, Publie, Archive }` et une énumération « backed » (`enum Role: string`). Utilisez `from`, `tryFrom`, `cases()`, `->name`, `->value`. Que se passe-t-il pour `Role::from("inconnu")` ? *(8.1)*

**Exercice 14.8.2**

Ajoutez des méthodes, des constantes et une interface à une énumération. Écrivez `Statut::libelle()` et `Statut::estFinal()`. Utilisez une énumération avec `match` pour un traitement exhaustif. *(8.1)*

**Exercice 14.8.3**

Utilisez une énumération dans une propriété typée, un paramètre et un tableau de résultats. Convertissez depuis une saisie utilisateur avec `tryFrom` et validation.

**Exercice 14.8.4**

Quelles sont les limites des énumérations (pas d'instanciation, pas de propriétés d'instance, pas d'héritage) ? Comparez avec des constantes de classe.

## 14.9 Méthodes magiques

**Exercice 14.9.1**

Implémentez dans une classe : `__construct`, `__destruct`, `__toString`, `__get`, `__set`, `__isset`, `__unset`, `__call`, `__callStatic`, `__invoke`, `__clone`, `__serialize` / `__unserialize`, `__debugInfo`. Écrivez un exemple pour chacune.

**Exercice 14.9.2**

Écrivez une classe `Config` dont `__get` lit dans un tableau interne et `__set` refuse les propriétés inconnues. Quels inconvénients (pas de typage, pas d'autocomplétion) ?

**Exercice 14.9.3**

Écrivez un objet appelable avec `__invoke` (par exemple un middleware ou un comparateur). Utilisez `__call` pour implémenter des méthodes dynamiques (`getNom()` à partir d'un tableau).

**Exercice 14.9.4**

Quand `__destruct` est-il appelé ? Écrivez un exemple de libération de ressource. Pourquoi est-il peu fiable pour la logique métier ?

## 14.10 Objets : copie et comparaison

**Exercice 14.10.1**

Montrez que les variables d'objet contiennent des références (identifiants d'objet) : modifiez l'objet via une copie de la variable. Faites une copie avec `clone`. Que se passe-t-il pour les propriétés qui sont des objets (copie superficielle) ?

**Exercice 14.10.2**

Implémentez `__clone()` pour une copie profonde d'une classe qui contient un autre objet et un tableau d'objets.

**Exercice 14.10.3**

Comparez deux objets avec `==` (mêmes propriétés et même classe) et `===` (même instance). Prédisez les résultats pour des objets identiques, clonés, de classes différentes, avec propriétés différentes.

**Exercice 14.10.4**

Écrivez `egal(self $autre): bool` pour un objet de valeur `Point` et utilisez `spl_object_id` / `SplObjectStorage` pour identifier des instances.

## 14.11 Attributs *(8.0, ajout)*

**Exercice 14.11.1**

Définissez un attribut `#[Route(chemin: "/accueil", methodes: ["GET"])]` (classe avec `#[Attribute]`) et appliquez-le à une méthode. Lisez-le avec la réflexion (`ReflectionMethod::getAttributes()`, `newInstance()`). *(8.0)*

**Exercice 14.11.2**

Écrivez un mini-routeur qui parcourt les méthodes d'un contrôleur, lit leurs attributs `#[Route]` et construit la table de routage. *(défi)*

**Exercice 14.11.3**

Écrivez un attribut de validation (`#[Longueur(min: 3, max: 50)]`, `#[Email]`) sur des propriétés et un validateur générique qui les lit par réflexion.

**Exercice 14.11.4**

Utilisez les attributs intégrés : `#[\Override]`, `#[\Deprecated]` (8.4), `#[\SensitiveParameter]`, `#[\ReturnTypeWillChange]`, `#[\AllowDynamicProperties]`, `#[\NoDiscard]` (8.5). Écrivez un exemple pour deux d'entre eux. *(8.4, 8.5)*

## 14.12 Espaces de noms et chargement automatique

**Exercice 14.12.1**

Créez deux classes dans des espaces de noms différents (`App\Modeles\Utilisateur`, `App\Services\Utilisateur`). Utilisez `namespace`, `use`, `use ... as`, `use function`, `use const`. Que se passe-t-il pour une fonction globale appelée dans un espace de noms (`\strlen`) ?

**Exercice 14.12.2**

Écrivez un chargeur automatique PSR-4 minimal avec `spl_autoload_register` qui associe le préfixe `App\` au dossier `src/`. Testez avec trois classes.

**Exercice 14.12.3**

Organisez un petit projet en dossiers (`src/Modele`, `src/Controleur`, `src/Service`, `public/index.php`) et configurez l'autoload avec Composer (`psr-4`). Pourquoi le dossier `public/` est-il le seul exposé au web ?

**Exercice 14.12.4**

Utilisez la résolution de noms : `Namespace\Classe::class`, `namespace\fonction()`, `__NAMESPACE__`, les noms relatifs, qualifiés et pleinement qualifiés. Complétez le tableau avec un exemple de chacun.

## 14.13 Autres notions

**Exercice 14.13.1**

Utilisez `Closure::bind` pour accéder à un état privé et `$this` dans une fermeture. Écrivez un exemple de fermeture liée à un objet.

**Exercice 14.13.2**

Écrivez un objet de valeur immuable (`Email`, `Montant`, `Adresse`) avec validation dans le constructeur. Utilisez l'injection de dépendances pour un service `Notificateur` qui dépend d'une interface `Canal`.

**Exercice 14.13.3**

Instanciez sans parenthèses (`new Voiture("A")->rouler(10)`, 8.4) et utilisez `new` dans un initialiseur. Utilisez les objets paresseux (8.4) pour différer une instanciation coûteuse. *(8.4)*

**Exercice 14.13.4**

Appliquez les principes SOLID à un exemple : refactorisez une classe qui crée des utilisateurs, envoie des courriels et écrit des journaux en trois classes collaborant par interfaces. Quels principes illustrez-vous ?

**Exercice 14.13.5**

Mini-projet : un système de gestion de bibliothèque (`Livre`, `Membre`, `Emprunt`, `Bibliotheque`) avec énumérations, classes `readonly`, interfaces, exceptions personnalisées, injection de dépendances, persistance JSON et tests.

---

# 15. PHP et le web

## 15.1 En-têtes HTTP

**Exercice 15.1.1**

Envoyez des en-têtes avec `header()` : `Content-Type: application/json; charset=utf-8`, `Cache-Control`, `X-Frame-Options`, un code de statut avec `http_response_code`. Pourquoi les en-têtes doivent-ils être envoyés avant toute sortie ? Utilisez `headers_sent()`.

**Exercice 15.1.2**

Écrivez une page qui renvoie du JSON, une autre du texte brut, une autre du XML, une autre une image générée (`imagepng` avec GD). Quel est l'effet du mauvais en-tête `Content-Type` ?

**Exercice 15.1.3**

Écrivez une petite fonction `repondreJson(mixed $donnees, int $statut = 200): never` qui envoie les en-têtes, encode en JSON avec `JSON_THROW_ON_ERROR` et termine le script.

### Lire les en-têtes de la requête

**Exercice 15.1.4**

Lisez les en-têtes avec `getallheaders()` et `$_SERVER['HTTP_*']`. Écrivez `entete(string $nom): ?string`. Écrivez un script qui affiche `Accept`, `User-Agent`, `Accept-Language`, `Authorization`, `X-Forwarded-For`. Lesquels ne doivent jamais être considérés comme fiables ?

**Exercice 15.1.5**

Implémentez la négociation de contenu : renvoyer du JSON ou du HTML selon l'en-tête `Accept`. Implémentez la détection de la langue préférée avec `Accept-Language` (ou `Locale::acceptFromHttp`).

## 15.2 Redirections

**Exercice 15.2.1**

Écrivez `rediriger(string $url, int $statut = 303): never`. Quelle différence entre les codes `301`, `302`, `303`, `307`, `308` ? Pourquoi `exit` est-il indispensable ?

**Exercice 15.2.2**

Pourquoi une redirection construite à partir d'un paramètre utilisateur (`?retour=...`) est-elle dangereuse (redirection ouverte) ? Écrivez une validation par liste blanche ou limitée aux chemins relatifs.

**Exercice 15.2.3**

Écrivez une redirection `http` vers `https` et une redirection d'URL canonique (avec ou sans `www`, avec ou sans barre oblique finale).

## 15.3 Télécharger un fichier

**Exercice 15.3.1**

Écrivez `telecharger(string $chemin, string $nom)` qui envoie un fichier avec `Content-Type`, `Content-Disposition: attachment; filename*=UTF-8''...`, `Content-Length` et `readfile`. Validez le chemin pour éviter la traversée de répertoires.

**Exercice 15.3.2**

Gérez les gros fichiers (lecture par blocs avec `fread` et `flush`) et la reprise partielle (en-tête `Range`, réponse `206 Partial Content`). *(défi)*

**Exercice 15.3.3**

Générez un fichier à la volée (CSV, PDF, archive ZIP avec `ZipArchive`) et envoyez-le directement sans l'écrire sur le disque. Écrivez un export CSV en flux depuis la base de données.

**Exercice 15.3.4**

Écrivez des téléchargements protégés : vérifier que l'utilisateur est connecté et propriétaire du fichier avant l'envoi.

## 15.4 Envoyer des e-mails

### La fonction `mail()` (basique)

**Exercice 15.4.1**

Envoyez un courriel texte avec `mail()` (ou simulez-le avec un fichier). Quelles limites (authentification, délivrabilité, SPF/DKIM/DMARC) ? Pourquoi les messages risquent-ils de finir en spam ?

**Exercice 15.4.2**

Montrez l'injection d'en-têtes (`\r\nBcc: ...`) dans un formulaire de contact qui utilise `mail()`. Corrigez en validant l'adresse et en refusant les retours à la ligne dans les en-têtes.

### Bibliothèques (recommandé) : PHPMailer, Symfony Mailer

**Exercice 15.4.3**

Installez PHPMailer ou Symfony Mailer avec Composer et envoyez un courriel via un serveur SMTP de test (MailHog, Mailpit, Mailtrap). Ajoutez un corps HTML et un corps texte alternatif, une pièce jointe, un destinataire en copie.

**Exercice 15.4.4**

Écrivez un service `Mailer` (classe) avec une interface, que vous pouvez remplacer par une version factice dans les tests. Écrivez des gabarits de courriel (confirmation d'inscription, réinitialisation de mot de passe).

**Exercice 15.4.5**

Écrivez un formulaire de contact complet : validation, protection CSRF, limitation du débit, pot de miel anti-spam (champ caché), envoi de courriel, message de confirmation avec PRG.

**Exercice 15.4.6**

Pourquoi faut-il envoyer les courriels via une file d'attente plutôt que pendant la requête ? Décrivez le principe de la file (Laravel Queues, Symfony Messenger).

## 15.5 Requêtes HTTP sortantes

**Exercice 15.5.1**

Interrogez une API publique JSON avec `file_get_contents` et un contexte de flux (`stream_context_create`), puis avec cURL (`curl_init`, `curl_setopt_array`, `curl_exec`, `curl_getinfo`, `curl_error`, `curl_close`).

**Exercice 15.5.2**

Écrivez une fonction `get(string $url, array $entetes = [], int $delai = 5): array` avec cURL qui renvoie le statut, les en-têtes et le corps décodé. Gérez les erreurs réseau, les délais d'attente, les redirections, la vérification des certificats (ne jamais désactiver `CURLOPT_SSL_VERIFYPEER`).

**Exercice 15.5.3**

Envoyez une requête `POST` avec un corps JSON et un jeton d'authentification, puis un envoi de formulaire. Utilisez Guzzle ou Symfony HttpClient pour la même opération et comparez la longueur du code.

**Exercice 15.5.4**

Écrivez un client d'API avec nouvelles tentatives, mise en cache de la réponse (fichier ou APCu) et limite de débit. Quel est le rôle des en-têtes `ETag` et `If-None-Match` ?

**Exercice 15.5.5**

Qu'est-ce que la falsification de requête côté serveur (SSRF) ? Montrez le danger d'une fonction qui télécharge une URL fournie par l'utilisateur (accès à `http://localhost`, `http://169.254.169.254`). Écrivez des protections (liste blanche de domaines, résolution DNS et interdiction des adresses privées).

## 15.6 Utiliser l'URL

**Exercice 15.6.1**

Décomposez une URL avec `parse_url`, `parse_str`. Construisez une URL avec `http_build_query`. Encodez avec `urlencode`, `rawurlencode`, `urldecode`. Quelle différence entre `urlencode` et `rawurlencode` pour l'espace ?

**Exercice 15.6.2**

Utilisez la classe `Uri\Rfc3986\Uri` (extension URI, 8.5) ou `Uri\WhatWg\Url` pour analyser, modifier et résoudre une URL. Comparez avec `parse_url`. *(8.5)*

**Exercice 15.6.3**

Écrivez des fonctions `urlAvecParametre(string $url, string $cle, string $valeur): string` et `retirerParametre()`. Écrivez un générateur de liens canoniques.

**Exercice 15.6.4**

Écrivez un raccourcisseur d'URL minimal : enregistrement d'une URL longue, génération d'un code court unique (`random_bytes` encodé), redirection avec validation du schéma (`http`/`https` seulement).

## 15.7 Bonnes pratiques

**Exercice 15.7.1**

Listez cinq bonnes pratiques web (en-têtes explicites, redirections avec `exit`, clients HTTP avec délais, journalisation, ne jamais faire confiance aux en-têtes) et corrigez ce code :

```php
<?php
echo "Bonjour";
header("Location: " . $_GET['url']);
$r = file_get_contents($_GET['api']);
mail($_POST['dest'], "Sujet", $_POST['msg'], "From: " . $_POST['de']);
```

**Exercice 15.7.2**

Mini-projet : un petit agrégateur qui télécharge plusieurs flux ou API publiques, met les réponses en cache, affiche une page HTML avec tri et filtres, et gère proprement les échecs de certaines sources.

---

# 16. Sécurité

## 16.1 Principe général

**Exercice 16.1.1**

Expliquez les principes de la défense en profondeur, du moindre privilège, de la validation des entrées et de l'échappement des sorties, et de « ne jamais faire confiance au client ». Illustrez chacun par un exemple concret en PHP.

**Exercice 16.1.2**

Parcourez le Top 10 de l'OWASP. Pour chacune des dix catégories, associez une faille PHP typique et une contre-mesure (injection SQL, XSS, CSRF, authentification faible, mauvaise configuration, composants vulnérables, inclusion de fichiers, désérialisation, etc.).

## 16.2 Validation, assainissement et échappement

**Exercice 16.2.1**

Distinguez validation, assainissement et échappement avec un exemple chacun, pour un champ « commentaire » affiché en HTML. Dans quel ordre et à quel moment les appliquer ?

**Exercice 16.2.2**

Écrivez un petit code vulnérable à XSS (réflexion d'un paramètre) et un code vulnérable à XSS stockée (commentaire enregistré puis affiché). Corrigez avec `htmlspecialchars`. Montrez les vecteurs : balise `<script>`, attribut `onerror`, URL `javascript:`.

**Exercice 16.2.3**

Affichez des données dans les contextes HTML, attribut, URL et JavaScript (`json_encode` avec `JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT`). Quelle fonction pour chaque contexte ? Pourquoi un échappement unique ne convient-il pas à tous ?

**Exercice 16.2.4**

Pour permettre un peu de HTML dans un commentaire (gras, liens), utilisez une bibliothèque d'assainissement (HTMLPurifier) avec une liste blanche de balises. Pourquoi `strip_tags` ne suffit-il pas ?

### Protection XSS supplémentaire : Content Security Policy

**Exercice 16.2.5**

Ajoutez l'en-tête `Content-Security-Policy` (`default-src 'self'`, `script-src` avec un nonce généré à chaque requête). Écrivez le code qui génère le nonce et l'insère dans les balises `<script>`. Quels effets sur les scripts en ligne ?

## 16.3 CSRF : falsification de requête inter-sites

**Exercice 16.3.1**

Écrivez une page malveillante qui soumet automatiquement un formulaire vers un site vulnérable. Protégez ce site avec un jeton CSRF vérifié avec `hash_equals`. Testez l'attaque avant et après.

**Exercice 16.3.2**

Écrivez un intergiciel (fonction) qui vérifie le jeton sur toutes les requêtes `POST`, `PUT`, `PATCH`, `DELETE`, exige l'en-tête `Origin` ou `Referer` cohérent et définit `SameSite=Lax`. Pourquoi une API stateless avec jeton `Authorization` n'est-elle pas concernée ?

**Exercice 16.3.3**

Pourquoi une action qui modifie des données ne doit-elle jamais être déclenchée par une requête `GET` ? Montrez l'exploitation avec une balise `<img src="...">`.

## 16.4 Hachage des mots de passe

**Exercice 16.4.1**

Écrivez l'inscription (`password_hash($mdp, PASSWORD_DEFAULT)` ou `PASSWORD_ARGON2ID`) et la connexion (`password_verify`). Pourquoi `md5`, `sha1`, `sha256` seuls sont-ils inadaptés ? Qu'est-ce que le sel, qui le gère ici ?

**Exercice 16.4.2**

Utilisez `password_needs_rehash` pour mettre à jour les hachages au fil des connexions. Mesurez le temps d'un hachage avec différents coûts (`['cost' => 10..14]`) et choisissez un coût qui prend environ 100 à 300 ms.

**Exercice 16.4.3**

Écrivez une politique de mots de passe (longueur minimale, vérification contre une liste de mots de passe courants, pas de règles de composition abusives) et la limitation des tentatives de connexion (blocage temporaire, délai croissant).

**Exercice 16.4.4**

Écrivez le flux de réinitialisation de mot de passe : jeton aléatoire à usage unique (`random_bytes`), stocké haché, avec expiration, envoyé par courriel, invalidé après usage. Quelles fuites d'information éviter (« cet e-mail n'existe pas ») ?

**Exercice 16.4.5**

Décrivez l'authentification à deux facteurs (TOTP) et écrivez la vérification d'un code à six chiffres avec une bibliothèque. *(défi)*

## 16.5 Aléatoire et jetons

**Exercice 16.5.1**

Comparez `rand`, `mt_rand`, `uniqid`, `random_int`, `random_bytes`, `bin2hex(random_bytes())` : quelles sont adaptées à la sécurité ? Écrivez `jetonAleatoire(int $octets = 32): string`.

**Exercice 16.5.2**

Écrivez un générateur de mots de passe aléatoires sûr (alphabet défini, `random_int`) et un générateur d'identifiants publics non devinables (UUID v4 avec `random_bytes`, ou ULID).

**Exercice 16.5.3**

Pourquoi un jeton prévisible (basé sur `time()` ou `uniqid`) est-il exploitable ? Montrez comment deviner un jeton de réinitialisation basé sur `md5(time())`.

## 16.6 Téléversements sécurisés (rappel)

**Exercice 16.6.1**

Rédigez la liste de contrôle d'un téléversement sécurisé (taille, type réel, extension, nom aléatoire, stockage hors racine, droits, antivirus éventuel, pas d'exécution) et vérifiez votre script de l'exercice 10.6.3 point par point.

## 16.7 HTTPS et en-têtes de sécurité

**Exercice 16.7.1**

Envoyez les en-têtes de sécurité : `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, `X-Frame-Options` ou `Content-Security-Policy: frame-ancestors`, `Referrer-Policy`, `Permissions-Policy`. Expliquez ce que protège chacun.

**Exercice 16.7.2**

Forcez HTTPS (redirection, cookies `Secure`, HSTS). Testez la configuration de votre site avec un outil en ligne (Mozilla Observatory, SSL Labs) et corrigez trois remarques.

**Exercice 16.7.3**

Que fait CORS ? Écrivez les en-têtes `Access-Control-Allow-Origin`, `Access-Control-Allow-Methods`, `Access-Control-Allow-Headers` pour une API consommée par un front-end d'une autre origine, avec la gestion de la requête préliminaire `OPTIONS`. Pourquoi `*` avec des identifiants est-il interdit ?

## 16.8 Configuration et déploiement sûrs

**Exercice 16.8.1**

Rédigez le `php.ini` de production : `display_errors=Off`, `expose_php=Off`, `session.*`, `open_basedir`, `disable_functions`, `allow_url_include=Off`, `memory_limit`, `upload_max_filesize`. Justifiez chaque réglage.

**Exercice 16.8.2**

Pourquoi la racine web ne doit-elle contenir que `public/` ? Listez les fichiers à ne jamais exposer (`.env`, `.git`, `composer.json`, `vendor/`, sauvegardes, journaux, `phpinfo()`). Testez l'accès à ces chemins sur un projet.

**Exercice 16.8.3**

Gérez les secrets : fichier `.env` hors dépôt, variables d'environnement, gestionnaire de secrets. Écrivez un chargeur de configuration qui échoue clairement quand une variable obligatoire est absente.

**Exercice 16.8.4**

Mettez à jour les dépendances : `composer audit`, `composer outdated`, Dependabot ou Renovate. Pourquoi les mises à jour de sécurité doivent-elles être rapides ?

## 16.9 Liste de contrôle

**Exercice 16.9.1**

Auditez l'un de vos projets avec la liste de contrôle du cours : cochez chaque point (requêtes préparées, échappement, CSRF, hachage, sessions, HTTPS, en-têtes, téléversements, configuration, dépendances) et corrigez les écarts.

**Exercice 16.9.2**

Corrigez ce code qui cumule plusieurs failles (au moins sept) :

```php
<?php
session_start();
$u = $_POST['user'];
$p = md5($_POST['pass']);
$r = mysqli_query($c, "SELECT * FROM users WHERE user='$u' AND pass='$p'");
if (mysqli_num_rows($r) > 0) {
    $_SESSION['user'] = $u;
    setcookie("role", "admin");
    echo "Bienvenue " . $_GET['nom'];
    include($_GET['page'] . ".php");
    move_uploaded_file($_FILES['f']['tmp_name'], "uploads/" . $_FILES['f']['name']);
}
```

**Exercice 16.9.3**

Mettez en place une attaque simulée sur une application volontairement vulnérable (DVWA, Juice Shop, ou votre propre code) pour reproduire une injection SQL, une XSS et une CSRF, puis corrigez chacune. Notez ce que l'attaquant gagne à chaque étape.

---

# 17. Composer et gestion des dépendances

## 17.1 Qu'est-ce que Composer ?

**Exercice 17.1.1**

Expliquez le rôle de Composer (gestion des dépendances, chargement automatique, scripts) et celui de Packagist. Quelle différence entre Composer et un gestionnaire de paquets système (`apt`) ou PEAR ?

**Exercice 17.1.2**

Citez trois problèmes que Composer résout par rapport à un téléchargement manuel de bibliothèques (versions, dépendances transitives, mises à jour, autoload).

### Installation

**Exercice 17.1.3**

Installez Composer (installateur officiel avec vérification de la somme de contrôle, ou gestionnaire de paquets du système). Vérifiez avec `composer --version` et `composer diagnose`. Pourquoi faut-il vérifier la signature de l'installateur ?

## 17.2 `composer.json`

**Exercice 17.2.1**

Créez un projet avec `composer init`. Examinez `composer.json` : `name`, `description`, `type`, `license`, `require`, `require-dev`, `autoload`, `autoload-dev`, `scripts`, `config`, `minimum-stability`. Décrivez chaque clé.

**Exercice 17.2.2**

Écrivez un `composer.json` pour un projet qui exige PHP `^8.3`, les extensions `ext-mbstring` et `ext-pdo`, la bibliothèque `monolog/monolog` et, en développement, `phpunit/phpunit` et `phpstan/phpstan`.

**Exercice 17.2.3**

Ajoutez des scripts Composer (`"test": "phpunit"`, `"stan": "phpstan analyse src"`, `"qualite": ["@stan", "@test"]`) et lancez-les avec `composer test`. Quels événements (`post-install-cmd`, `post-autoload-dump`) peut-on accrocher ?

**Exercice 17.2.4**

Quelle est la différence entre `require` et `require-dev` ? Entre `composer install` et `composer install --no-dev` ? Pourquoi déployer sans les dépendances de développement ?

## 17.3 Gérer les paquets

**Exercice 17.3.1**

Utilisez `composer require`, `composer remove`, `composer update`, `composer install`, `composer show`, `composer outdated`, `composer why`, `composer why-not`, `composer audit`, `composer dump-autoload`, `composer validate`. Pour chaque commande, décrivez l'effet et un cas d'usage.

**Exercice 17.3.2**

Quel est le rôle du fichier `composer.lock` ? Pourquoi doit-il être versionné dans un projet applicatif ? Quelle différence entre `composer install` (utilise le verrou) et `composer update` (le recalcule) ? Pour une bibliothèque, que recommande-t-on ?

**Exercice 17.3.3**

Résolvez un conflit de dépendances : deux paquets exigent des versions incompatibles d'une même bibliothèque. Utilisez `composer why-not` pour comprendre et proposez des solutions.

### Contraintes de version (SemVer)

**Exercice 17.3.4**

Expliquez le versionnage sémantique (`MAJEUR.MINEUR.CORRECTIF`). Donnez les versions acceptées par `^1.2.3`, `~1.2.3`, `1.2.*`, `>=1.2 <2.0`, `1.2.3`, `dev-main`, `^0.3`, `^1.0 || ^2.0`. Pourquoi `^0.3` est-il plus restrictif ?

**Exercice 17.3.5**

Quels risques présente l'utilisation de `*` ou de `dev-master` pour une dépendance ? Quelle est la contrainte la plus usuelle et pourquoi ?

## 17.4 Chargement automatique

**Exercice 17.4.1**

Configurez l'autoload PSR-4 (`"App\\": "src/"`), lancez `composer dump-autoload` et utilisez `require 'vendor/autoload.php'` pour charger vos classes. Que se passe-t-il si le nom du fichier ne correspond pas à celui de la classe ?

**Exercice 17.4.2**

Quelle différence entre `psr-4`, `classmap` et `files` ? Écrivez un exemple pour chacune. Comment optimiser l'autoload pour la production (`--optimize-autoloader`, `--classmap-authoritative`, `--apcu-autoloader`) ?

**Exercice 17.4.3**

Écrivez `autoload-dev` pour les tests (`"Tests\\": "tests/"`). Pourquoi séparer l'autoload de production et de développement ?

## 17.5 Créer et publier son propre paquet

**Exercice 17.5.1**

Créez une petite bibliothèque (par exemple un utilitaire de chaînes ou un validateur), avec sa structure (`src/`, `tests/`, `composer.json`, `README.md`, `LICENSE`, `.gitattributes`). Installez-la dans un autre projet via un dépôt de type `path`.

**Exercice 17.5.2**

Décrivez les étapes de publication sur Packagist : dépôt Git public, étiquettes de version (`v1.0.0`), enregistrement du paquet, mise à jour automatique par webhook. Quelles bonnes pratiques de documentation et de versionnement ?

**Exercice 17.5.3**

Écrivez un `CHANGELOG.md` suivant le format « Keep a Changelog ». Quels changements justifient une version majeure, mineure, corrective ?

## 17.6 Bonnes pratiques

**Exercice 17.6.1**

Listez cinq bonnes pratiques Composer (versionner `composer.lock`, ne pas versionner `vendor/`, contraintes explicites, `composer audit`, mises à jour régulières) et corrigez ce `composer.json` :

```json
{
    "require": {
        "monolog/monolog": "*",
        "phpunit/phpunit": "dev-master"
    },
    "autoload": {
        "files": ["src/Tout.php"]
    }
}
```

**Exercice 17.6.2**

Évaluez la qualité d'un paquet avant de l'adopter (dernière version, activité, nombre de dépendances, licence, sécurité, documentation, tests). Appliquez la grille à deux paquets concurrents de votre choix.

---

# 18. Frameworks PHP

## 18.1 Pourquoi un framework ?

**Exercice 18.1.1**

Citez cinq composants fournis par un framework (routage, ORM, gabarits, validation, authentification, CLI, tests) et, pour chacun, expliquez ce qu'il vous fait gagner par rapport à du PHP « à la main ».

**Exercice 18.1.2**

Expliquez le patron MVC (Modèle – Vue – Contrôleur). Pour une page « liste d'articles », indiquez ce qui appartient au modèle, à la vue et au contrôleur. Écrivez un mini-MVC en PHP pur (routeur, contrôleur, modèle, vue) en moins de 100 lignes. *(défi)*

**Exercice 18.1.3**

Dans quels cas un framework est-il excessif (petit script, page unique) ? Quels risques d'une dépendance forte à un framework (mises à jour majeures, verrouillage) ?

## 18.2 Laravel

**Exercice 18.2.1**

Créez un projet Laravel (`composer create-project laravel/laravel` ou l'installateur) et lancez-le avec `php artisan serve`. Décrivez la structure des dossiers (`app`, `routes`, `resources`, `database`, `public`, `config`, `storage`).

**Exercice 18.2.2**

Définissez des routes (`routes/web.php`) : simple, avec paramètre, avec contrainte (`where`), nommée, groupée avec préfixe et intergiciel, de ressource (`Route::resource`). Listez-les avec `php artisan route:list`.

**Exercice 18.2.3**

Créez un modèle `Article` avec sa migration, son contrôleur et sa fabrique en une commande (`php artisan make:model Article -mcf`). Écrivez la migration (`Schema::create`) et exécutez-la (`php artisan migrate`).

**Exercice 18.2.4**

Utilisez Eloquent : création, lecture, modification, suppression, `where`, `orderBy`, pagination, relations (`hasMany`, `belongsTo`, `belongsToMany`), chargement anticipé (`with`) pour éviter le problème N+1. Écrivez un exemple de chaque.

**Exercice 18.2.5**

Écrivez un formulaire Blade avec `@csrf`, `@method('PUT')`, `{{ }}` (échappé) et `{!! !!}` (non échappé, à éviter), `@foreach`, `@if`, `@include`, `@extends`, `@section`. Validez avec `$request->validate([...])` et affichez les erreurs.

**Exercice 18.2.6**

Mettez en place l'authentification avec un kit de démarrage (Breeze, Jetstream, Fortify) ou à la main (`Auth::attempt`). Protégez des routes avec l'intergiciel `auth` et des autorisations avec une politique (`Policy`) ou une porte (`Gate`).

**Exercice 18.2.7**

Écrivez un test fonctionnel Laravel (`$this->get('/')->assertStatus(200)`), un test de création d'article avec `actingAs` et une base de test (`RefreshDatabase`). Lancez avec `php artisan test`.

**Exercice 18.2.8**

Utilisez la file d'attente (`php artisan queue:work`), les tâches planifiées (`Schedule`), les événements / écouteurs et les notifications. Écrivez l'envoi d'un courriel de bienvenue en tâche de fond.

**Exercice 18.2.9**

Écrivez un mini-projet Laravel : une application de gestion de tâches avec authentification, CRUD, validation, pagination, API JSON, tests.

## 18.3 Symfony

**Exercice 18.3.1**

Créez un projet Symfony (`symfony new` ou `composer create-project symfony/skeleton`) et lancez-le avec `symfony serve`. Décrivez la structure (`src`, `config`, `templates`, `public`, `var`, `migrations`) et le rôle de `bin/console`.

**Exercice 18.3.2**

Écrivez un contrôleur avec l'attribut `#[Route('/hello/{nom}', name: 'hello')]`, un gabarit Twig (`{{ nom }}`, `{% for %}`, `{% extends %}`, `{% block %}`) et un formulaire avec `FormType`. Que fait Twig par défaut pour l'échappement ?

**Exercice 18.3.3**

Utilisez l'injection de dépendances (autowiring) pour injecter un service dans un contrôleur. Écrivez un service `Calculatrice` et un autre qui dépend d'une interface. Listez-les avec `bin/console debug:container`.

**Exercice 18.3.4**

Utilisez Doctrine : entité avec attributs (`#[ORM\Entity]`, `#[ORM\Column]`), dépôt, migration (`make:migration`, `doctrine:migrations:migrate`), requêtes DQL. Comparez avec Eloquent (Active Record) : Doctrine est un « Data Mapper ».

**Exercice 18.3.5**

Utilisez le Maker Bundle (`make:controller`, `make:entity`, `make:crud`, `make:auth`) et le composant Security (pare-feu, fournisseurs, contrôle d'accès). Protégez une route avec `#[IsGranted('ROLE_ADMIN')]`.

**Exercice 18.3.6**

Utilisez des composants Symfony seuls dans un projet sans framework : `symfony/http-foundation` (Request, Response), `symfony/routing`, `symfony/console`, `symfony/validator`, `symfony/var-dumper`. Écrivez un exemple pour deux d'entre eux.

## 18.4 CodeIgniter 4

**Exercice 18.4.1**

Décrivez la structure d'un projet CodeIgniter 4 et ses avantages (légèreté, peu de configuration, hébergement mutualisé). Écrivez une route, un contrôleur et une vue. *(selon la version installée)*

**Exercice 18.4.2**

Écrivez un modèle CodeIgniter avec validation et une page de liste. Comparez la quantité de code avec Laravel pour le même exercice.

## 18.5 Slim (micro-framework)

**Exercice 18.5.1**

Créez une application Slim avec deux routes (`GET /`, `GET /bonjour/{nom}`), un groupe de routes, un intergiciel (journalisation) et une réponse JSON. Quel est le rôle de PSR-7 (messages HTTP) et PSR-15 (intergiciels) ?

**Exercice 18.5.2**

Ajoutez un conteneur d'injection de dépendances (PHP-DI) et un gestionnaire d'erreurs. Écrivez une petite API de notes (CRUD en mémoire ou SQLite).

## 18.6 Comparaison

**Exercice 18.6.1**

Complétez le tableau comparatif Laravel / Symfony / CodeIgniter / Slim / API Platform : idéal pour, courbe d'apprentissage, points forts, points faibles. Pour chaque projet suivant, choisissez un framework et justifiez : application web complète avec authentification, API REST minimaliste, application d'entreprise de longue durée, site sur hébergement mutualisé, API générée depuis le modèle de données.

**Exercice 18.6.2**

Réalisez le même mini-projet (liste de tâches avec API) dans deux frameworks de votre choix et comparez : temps de mise en place, quantité de code, lisibilité, performances, tests. Rédigez un compte rendu d'une page.

**Exercice 18.6.3**

Que faire quand la version majeure d'un framework change (migration de Laravel 11 vers 12, Symfony LTS) ? Établissez un plan : lire le guide de migration, mettre à jour les dépendances, lancer les tests, corriger les dépréciations, utiliser Rector.

---

# 19. Tests et qualité du code

## 19.1 Tests unitaires avec PHPUnit

**Exercice 19.1.1**

Installez PHPUnit (`composer require --dev phpunit/phpunit`), créez `phpunit.xml` et écrivez un test pour une fonction `estPalindrome`. Lancez avec `vendor/bin/phpunit`. Quelle est la convention de nommage des classes et méthodes de test (suffixe `Test`, préfixe `test` ou attribut `#[Test]`) ?

**Exercice 19.1.2**

Écrivez une classe `Calculatrice` (addition, division avec exception pour zéro) et les tests : cas nominal, limites, exception attendue (`expectException`, `expectExceptionMessage`). Écrivez les tests avant le code (TDD).

**Exercice 19.1.3**

Utilisez les fournisseurs de données (`#[DataProvider('cas')]`) pour tester `slugifier` avec dix cas. Pourquoi sont-ils préférables à des boucles dans un seul test ?

**Exercice 19.1.4**

Utilisez `setUp()` et `tearDown()` (ou `#[Before]`, `#[After]`) pour préparer et nettoyer un environnement (fichier temporaire, base SQLite en mémoire). Quelle est la différence avec `setUpBeforeClass`?

**Exercice 19.1.5**

Écrivez les tests d'une classe `Panier` (ajout, suppression, total, remise, panier vide) en appliquant la structure Arrange / Act / Assert. Un test ne doit vérifier qu'un seul comportement.

**Exercice 19.1.6**

Testez du code qui utilise des fichiers (répertoire temporaire), du temps (horloge injectable ou `DateTimeImmutable` fourni), de l'aléatoire (graine ou générateur injecté). Comment rendre ces dépendances testables ?

**Exercice 19.1.7**

Mesurez la couverture de code (`--coverage-text`, `--coverage-html`) avec Xdebug ou PCOV. Que signifie une couverture de 100 % ? Garantit-elle l'absence de bogues ? Comment lire le rapport et ajouter les tests manquants ?

### Assertions courantes

**Exercice 19.1.8**

Écrivez un test pour chaque assertion : `assertSame`, `assertEquals`, `assertTrue`, `assertFalse`, `assertNull`, `assertNotNull`, `assertCount`, `assertContains`, `assertArrayHasKey`, `assertInstanceOf`, `assertStringContainsString`, `assertMatchesRegularExpression`, `assertEqualsWithDelta`, `assertJsonStringEqualsJsonString`, `expectException`. Quelle différence entre `assertSame` (`===`) et `assertEquals` (`==`) ?

## 19.2 Doublures (*mocks*)

**Exercice 19.2.1**

Définissez doublure, bouchon (*stub*), simulacre (*mock*), espion (*spy*) et faux (*fake*). Écrivez un exemple pour chacun sur un service d'envoi de courriels.

**Exercice 19.2.2**

Écrivez un test de `Inscription` qui dépend d'une interface `Mailer` : créez un mock (`createMock`, `expects($this->once())`, `method('envoyer')`, `with(...)`, `willReturn`) et vérifiez que le courriel est envoyé une seule fois avec les bons arguments.

**Exercice 19.2.3**

Écrivez un bouchon (`createStub`) qui renvoie des valeurs différentes selon les appels (`willReturnOnConsecutiveCalls`, `willReturnCallback`) et lève une exception (`willThrowException`).

**Exercice 19.2.4**

Utilisez Mockery ou Prophecy et comparez la syntaxe avec les doublures de PHPUnit. Pourquoi faut-il éviter de « mocker » les types que l'on ne possède pas (bibliothèques externes) ? Quelle alternative (adaptateur, faux en mémoire) ?

**Exercice 19.2.5**

Testez un dépôt (`Repository`) avec une base SQLite en mémoire plutôt qu'avec des doublures. Quand les tests d'intégration sont-ils préférables aux tests unitaires avec doublures ?

## 19.3 TDD (*Test-Driven Development*)

**Exercice 19.3.1**

Appliquez le cycle rouge / vert / refactorisation pour écrire `FizzBuzz`, puis `Pile` : écrivez un test qui échoue, le code minimal qui le fait passer, puis refactorisez. Notez chaque étape.

**Exercice 19.3.2**

Appliquez le TDD à un petit problème de votre choix (calcul de prix avec remises, convertisseur de chiffres romains, kata du bowling). Quels avantages observez-vous (conception, confiance, documentation) ? Quelles difficultés ?

**Exercice 19.3.3**

Écrivez des tests de caractérisation pour un code existant sans tests (« legacy ») avant de le modifier. Quelle stratégie pour ajouter des tests dans du code très couplé (couture, extraction de méthode, injection) ?

## 19.4 Autres outils *(ajout)*

**Exercice 19.4.1**

Installez Pest et réécrivez trois tests PHPUnit avec sa syntaxe (`it(...)`, `expect(...)->toBe(...)`). Comparez la lisibilité.

**Exercice 19.4.2**

Installez PHPStan (ou Psalm), analysez votre projet au niveau 0 puis montez progressivement jusqu'au niveau le plus élevé. Corrigez cinq erreurs détectées. Quelles erreurs sont trouvées sans exécuter le code ?

**Exercice 19.4.3**

Installez PHP-CS-Fixer ou Laravel Pint, configurez la norme PSR-12 et formatez le projet. Quelle différence entre un formateur, un linter et un analyseur statique ?

**Exercice 19.4.4**

Installez Rector et appliquez un jeu de règles de modernisation (de PHP 8.1 vers 8.4 : promotion de propriétés, `readonly`, `match`). Examinez le diff avant de l'accepter. Pourquoi lancer les tests après ?

**Exercice 19.4.5**

Écrivez un flux d'intégration continue (GitHub Actions) qui installe PHP, met en cache Composer, lance le style, l'analyse statique et les tests sur plusieurs versions de PHP (matrice 8.3, 8.4, 8.5), puis échoue à la première erreur.

**Exercice 19.4.6**

Mettez en place des crochets Git (`pre-commit`, avec `captainhook` ou un script) qui lancent le formateur et l'analyse sur les fichiers modifiés. Quelles sont leurs limites ?

**Exercice 19.4.7**

Utilisez Xdebug pour déboguer pas à pas (points d'arrêt, pile d'appels, inspection de variables) depuis votre éditeur et pour le profilage. Quelle commande pour vérifier qu'il est actif ?

## 19.5 Bonnes pratiques

**Exercice 19.5.1**

Listez cinq bonnes pratiques de test (tests rapides, indépendants, nommés explicitement, pas de logique dans les tests, tester le comportement) et corrigez ce test :

```php
<?php
class PanierTest extends TestCase {
    public function testTout() {
        $p = new Panier();
        $p->ajouter("a", 2);
        $this->assertTrue($p->total() > 0);
        if ($p->total() > 10) {
            $p->vider();
        }
        $this->assertEquals(1, 1);
    }
}
```

**Exercice 19.5.2**

Appliquez la pyramide des tests à une petite application : écrivez des tests unitaires, un test d'intégration (base de données) et un test de bout en bout (requête HTTP). Justifiez la proportion de chaque.

**Exercice 19.5.3**

Écrivez des tests basés sur les propriétés (avec une bibliothèque de génération de données aléatoires) pour une fonction de tri ou de sérialisation. Quels invariants vérifier ? *(défi)*

---

# 20. Créer des API avec PHP

## 20.1 Principes REST

**Exercice 20.1.1**

Expliquez les principes REST (ressources, URI, méthodes HTTP, sans état, représentations, codes de statut, HATEOAS). Concevez les URL et les méthodes d'une API de gestion d'articles (`GET /articles`, `POST /articles`, `GET /articles/{id}`, `PUT`, `PATCH`, `DELETE`).

**Exercice 20.1.2**

Associez chaque situation au bon code de statut : création réussie, suppression sans contenu, requête invalide, non authentifié, interdit, introuvable, conflit, trop de requêtes, erreur serveur, service indisponible. Quelle différence entre `401` et `403` ? Entre `PUT` et `PATCH` ?

**Exercice 20.1.3**

Concevez les erreurs de l'API : un format uniforme (`type`, `titre`, `statut`, `detail`, `erreurs` par champ, comme RFC 9457 « Problem Details »). Écrivez des exemples pour une validation échouée et une ressource absente.

**Exercice 20.1.4**

Définissez la pagination (paramètres `page`, `limite` ou curseur), le tri, le filtrage et le versionnement (`/v1/...` ou en-tête). Quels en-têtes ou champs inclure (`Link`, total, prochaine page) ?

## 20.2 JSON en PHP

**Exercice 20.2.1**

Utilisez `json_encode` (options `JSON_PRETTY_PRINT`, `JSON_UNESCAPED_UNICODE`, `JSON_THROW_ON_ERROR`, `JSON_PRESERVE_ZERO_FRACTION`) et `json_decode` (tableau ou objet, profondeur). Que renvoient-ils en cas d'erreur sans `JSON_THROW_ON_ERROR` ? Utilisez `json_last_error_msg`.

**Exercice 20.2.2**

Que devient un tableau vide, un tableau associatif, une liste à clés non consécutives, un objet, un `float`, une date, une valeur `NAN` ou `INF`, une chaîne UTF-8 invalide à l'encodage JSON ? Testez chaque cas.

**Exercice 20.2.3**

Implémentez `JsonSerializable` dans une classe (`jsonSerialize`) pour contrôler la sortie (masquer un mot de passe, formater une date). Écrivez un objet de transfert (DTO) et un « transformeur » de ressource.

**Exercice 20.2.4**

Utilisez `json_validate()` (8.3) pour valider une chaîne sans la décoder. Écrivez une fonction `lireCorpsJson(): array` qui lit `php://input`, vérifie le `Content-Type`, décode, et renvoie une erreur `400` explicite si le JSON est invalide. *(8.3)*

**Exercice 20.2.5**

Limitez la taille du corps de la requête et la profondeur de décodage. Pourquoi est-ce utile contre les attaques par déni de service ?

## 20.3 Un mini-routeur d'API en PHP pur

**Exercice 20.3.1**

Écrivez un routeur qui associe méthode et chemin à un gestionnaire, avec des paramètres de chemin (`/articles/{id}`) transformés en expressions régulières. Écrivez `Routeur::ajouter(string $methode, string $motif, callable $gestionnaire)` et `Routeur::repondre(Requete $r): Reponse`.

**Exercice 20.3.2**

Écrivez des classes `Requete` (méthode, chemin, en-têtes, corps JSON, paramètres de requête) et `Reponse` (statut, en-têtes, corps JSON, méthode `envoyer()`). Utilisez-les dans le routeur.

**Exercice 20.3.3**

Gérez les erreurs : `404` (route absente), `405` (méthode non autorisée, avec l'en-tête `Allow`), `400` (JSON invalide), `422` (validation), `500` (exception non gérée, sans fuite de détails). Écrivez un gestionnaire d'exceptions central.

**Exercice 20.3.4**

Ajoutez des intergiciels (pipeline) : journalisation, CORS, authentification, limitation de débit. Écrivez `Intergiciel` (interface) et la chaîne d'exécution.

**Exercice 20.3.5**

Implémentez une API CRUD complète pour des `notes` (stockage SQLite via PDO), avec validation, pagination, codes de statut corrects, en-têtes `Location` à la création. Écrivez le fichier `public/index.php` comme unique point d'entrée.

**Exercice 20.3.6**

Configurez Apache ou Nginx (ou le serveur intégré avec routeur) pour que toutes les requêtes passent par `public/index.php`. Écrivez les règles de réécriture.

## 20.4 API avec un framework

### Laravel

**Exercice 20.4.1**

Dans Laravel, écrivez `routes/api.php`, un contrôleur `ArticleController` de ressource (`apiResource`), une `FormRequest` de validation, une `JsonResource` / `ResourceCollection` et une pagination automatique. Testez avec `curl` ou un client HTTP.

**Exercice 20.4.2**

Utilisez Laravel Sanctum pour l'authentification par jeton : émettre un jeton à la connexion, le révoquer à la déconnexion, protéger des routes (`auth:sanctum`), gérer les capacités (`abilities`).

### Slim

**Exercice 20.4.3**

Écrivez la même API avec Slim : routes, groupe `/api/v1`, intergiciels (analyse du corps JSON, CORS, gestion d'erreurs), réponses JSON, PDO via le conteneur d'injection.

### Symfony / API Platform

**Exercice 20.4.4**

Annotez une entité Doctrine avec `#[ApiResource]` (API Platform) et observez les routes générées, la documentation OpenAPI et l'interface Swagger. Quelles opérations sont fournies automatiquement (collection, élément, filtres, pagination) ?

**Exercice 20.4.5**

Personnalisez une ressource API Platform : groupes de sérialisation, validation avec des contraintes (`#[Assert\NotBlank]`), filtres de recherche, processeurs d'état. Comparez la productivité avec le mini-routeur de l'exercice 20.3.5.

## 20.5 Authentification et sécurité d'une API

**Exercice 20.5.1**

Comparez les mécanismes d'authentification : clé d'API, authentification de base, jeton opaque, JWT, OAuth 2.0, sessions avec cookie. Pour chacun : avantages, inconvénients, cas d'usage.

**Exercice 20.5.2**

Écrivez une authentification par jeton porteur (`Authorization: Bearer ...`) dans votre mini-routeur : lecture de l'en-tête, vérification du jeton haché en base, identification de l'utilisateur, `401` avec `WWW-Authenticate` en cas d'échec.

**Exercice 20.5.3**

Décodez et vérifiez un JWT avec une bibliothèque (`firebase/php-jwt`) : signature, expiration (`exp`), émetteur (`iss`), audience (`aud`). Quels pièges (algorithme `none`, secret faible, durée de vie trop longue, stockage côté client) ?

**Exercice 20.5.4**

Écrivez une limitation de débit (*rate limiting*) : N requêtes par minute par clé ou adresse IP, avec Redis ou APCu, en-têtes `X-RateLimit-*` et `Retry-After`, code `429`.

**Exercice 20.5.5**

Configurez CORS pour une API : origines autorisées, méthodes, en-têtes, identifiants, durée de mise en cache de la requête préliminaire. Écrivez le gestionnaire de `OPTIONS`.

**Exercice 20.5.6**

Listez les mesures de sécurité d'une API : HTTPS, validation stricte des entrées, autorisations par ressource (éviter l'accès direct non contrôlé aux objets, « IDOR »), limites de taille, journalisation, pas de secrets dans les URL, désactivation des messages d'erreur détaillés, en-têtes de sécurité. Auditez votre API avec cette liste.

## 20.6 Tester une API

**Exercice 20.6.1**

Testez votre API manuellement avec `curl` (méthodes, en-têtes, corps JSON, `-i`, `-v`, `-w`) puis avec un client graphique (Postman, Bruno, HTTPie). Enregistrez une collection de requêtes pour le CRUD complet.

**Exercice 20.6.2**

Écrivez des tests automatisés : avec Pest / PHPUnit et le client HTTP du framework (`$this->getJson('/api/articles')->assertOk()->assertJsonCount(3)`) ou avec Guzzle contre un serveur de test. Testez les cas de succès et d'erreur (`401`, `404`, `422`).

**Exercice 20.6.3**

Décrivez votre API avec une spécification OpenAPI (YAML ou JSON) : chemins, paramètres, schémas, réponses, sécurité. Générez la documentation (Swagger UI, Redoc) et validez les réponses par rapport au schéma dans vos tests.

**Exercice 20.6.4**

Mesurez les performances de l'API avec un outil de charge (`ab`, `wrk`, `k6`, `hey`) : requêtes par seconde, latence p95. Identifiez un goulot d'étranglement (requêtes SQL N+1, absence d'index, OPcache désactivé) et améliorez-le.

**Exercice 20.6.5**

Mini-projet : une API de gestion de bibliothèque (livres, auteurs, emprunts) avec authentification par jeton, validation, pagination, filtres, documentation OpenAPI, tests automatisés et intégration continue.

---

# 21. Sujets avancés

## 21.1 Scripts en ligne de commande (CLI)

**Exercice 21.1.1**

Écrivez un script CLI qui vérifie `PHP_SAPI === 'cli'`, lit des options avec `getopt('n:v', ['nom:', 'verbeux'])` et des arguments positionnels avec `$argv`. Affichez une aide (`--aide`) et renvoyez un code de sortie adapté.

**Exercice 21.1.2**

Lisez au clavier avec `fgets(STDIN)`, écrivez sur `STDOUT` et `STDERR`. Écrivez un petit assistant interactif (questions, validation de la saisie, valeurs par défaut) et un programme qui lit des données depuis un tube (`cat fichier | php script.php`).

**Exercice 21.1.3**

Rendez votre script exécutable (`#!/usr/bin/env php`, `chmod +x`) et planifiez-le avec `cron` (`* * * * * php /chemin/script.php >> /var/log/script.log 2>&1`). Quelles précautions pour éviter le chevauchement de deux exécutions (verrou `flock`) ?

**Exercice 21.1.4**

Écrivez une commande avec Symfony Console (`Command`, arguments, options, `SymfonyStyle`, barre de progression, tableau) ou avec Laravel Artisan (`make:command`). Comparez avec le script en PHP pur.

**Exercice 21.1.5**

Écrivez un outil CLI utile : renommage en masse de fichiers (avec mode simulation), analyseur de journaux (comptage d'erreurs par niveau), générateur de mots de passe, convertisseur CSV vers JSON.

**Exercice 21.1.6**

Gérez les signaux dans un script long (`pcntl_signal`, `SIGTERM`, `SIGINT`) pour un arrêt propre. Écrivez un travailleur qui traite une file de tâches et s'arrête proprement.

## 21.2 Performance

**Exercice 21.2.1**

Mesurez le temps et la mémoire d'une boucle d'un million d'itérations avec `microtime(true)` et `memory_get_peak_usage(true)`. Comparez `foreach` et `array_map`, `range` et un générateur, concaténation et `implode`.

**Exercice 21.2.2**

Activez OPcache (`opcache.enable=1`, `opcache.validate_timestamps`) et mesurez le gain sur un projet avec de nombreux fichiers. Vérifiez avec `opcache_get_status()`. Qu'est-ce que le préchargement (`opcache.preload`) ?

**Exercice 21.2.3**

Profilez une page lente avec Xdebug (profileur, KCachegrind / Webgrind) ou Blackfire. Identifiez les trois fonctions les plus coûteuses et proposez des optimisations.

**Exercice 21.2.4**

Reproduisez le problème de requêtes « N+1 » (une requête par ligne pour charger les relations) et corrigez-le avec une jointure ou un chargement par lot (`IN`). Comptez les requêtes avant et après.

**Exercice 21.2.5**

Ajoutez des index à une table de 100 000 lignes et mesurez l'effet sur une recherche (`EXPLAIN`). Quels critères de choix d'index (colonnes filtrées, tri, cardinalité) ?

**Exercice 21.2.6**

Comparez l'architecture classique (processus par requête avec PHP-FPM) et les serveurs persistants (FrankenPHP mode worker, RoadRunner, Swoole / Octane). Quels sont les gains et les pièges (état partagé, fuites de mémoire) ?

**Exercice 21.2.7**

Traitez un fichier de plusieurs gigaoctets avec une mémoire constante : lecture par générateur, traitement par lots (`chunk`), écriture en flux. Mesurez la mémoire de pointe.

## 21.3 Stratégies de cache

**Exercice 21.3.1**

Mettez en cache le résultat d'une opération coûteuse dans un fichier avec une durée de validité (TTL). Écrivez une classe `CacheFichier` (`obtenir`, `stocker`, `oublier`, `souvenir(cle, ttl, callable)`) avec sérialisation sûre (JSON ou `var_export`).

**Exercice 21.3.2**

Utilisez APCu (`apcu_store`, `apcu_fetch`, `apcu_delete`) pour un cache local au serveur. Quelles limites en CLI et avec plusieurs serveurs ?

**Exercice 21.3.3**

Implémentez le cache HTTP : en-têtes `Cache-Control`, `ETag`, `Last-Modified`, gestion de `If-None-Match` et `If-Modified-Since` avec la réponse `304 Not Modified`. Mesurez l'économie de bande passante.

**Exercice 21.3.4**

Utilisez l'interface PSR-6 ou PSR-16 (`CacheInterface`) pour écrire du code indépendant du système de cache (fichier, APCu, Redis). Écrivez deux implémentations et testez-les avec la même suite de tests.

**Exercice 21.3.5**

Décrivez les stratégies d'invalidation (TTL, invalidation à l'écriture, étiquettes, versionnement de clés) et le problème de la « ruée » sur un cache expiré (*cache stampede*). Proposez une solution (verrou, rafraîchissement anticipé). *(défi)*

## 21.4 Redis et Memcached

**Exercice 21.4.1**

Lancez Redis (Docker ou installation locale) et utilisez-le depuis PHP (extension `phpredis` ou `predis/predis`) : `set`, `get`, `del`, `expire`, `ttl`, `incr`, structures (listes, ensembles, tables de hachage, ensembles triés).

**Exercice 21.4.2**

Utilisez Redis comme cache de requêtes SQL, comme stockage de sessions (`session.save_handler = redis`), comme file d'attente simple (`lpush` / `brpop`) et comme limiteur de débit (`incr` + `expire`).

**Exercice 21.4.3**

Comparez Redis et Memcached : structures de données, persistance, réplication, cas d'usage. Quand Memcached suffit-il ?

**Exercice 21.4.4**

Écrivez un verrou distribué avec Redis (`SET cle valeur NX PX delai`) pour empêcher deux processus d'exécuter la même tâche. Quels pièges (expiration, libération par le bon propriétaire) ? *(défi)*

## 21.5 WebSockets et temps réel

**Exercice 21.5.1**

Expliquez pourquoi PHP classique (un processus par requête) se prête mal aux connexions persistantes, et comparez les solutions : Ratchet, Swoole / OpenSwoole, Workerman, Laravel Reverb, Soketi / Pusher, Mercure (SSE).

**Exercice 21.5.2**

Écrivez un serveur de « chat » minimal avec Ratchet et une page HTML avec un client WebSocket JavaScript. Testez avec deux onglets.

**Exercice 21.5.3**

Implémentez un flux d'événements serveur (SSE) en PHP : en-têtes `Content-Type: text/event-stream`, envoi périodique avec `flush()`, reconnexion automatique côté navigateur (`EventSource`). Comparez avec l'interrogation périodique (polling) et les WebSockets.

**Exercice 21.5.4**

Pour chacun des cas suivants, choisissez la technique adaptée (interrogation, SSE, WebSocket) : notifications occasionnelles, tableau de bord de supervision, chat multi-utilisateurs, jeu en ligne, barre de progression d'une tâche.

## 21.6 Programmation asynchrone et *fibers* *(8.1)*

**Exercice 21.6.1**

Écrivez un exemple avec `Fiber` : démarrage, `Fiber::suspend()`, `resume()`, `getReturn()`, `isTerminated()`. Écrivez un petit planificateur qui exécute plusieurs fibres en alternance. *(8.1)*

**Exercice 21.6.2**

Utilisez ReactPHP, AMPHP ou Revolt pour exécuter plusieurs requêtes HTTP en parallèle et mesurez le gain par rapport à des appels séquentiels. Pourquoi les fibres seules ne rendent-elles pas le code non bloquant ?

**Exercice 21.6.3**

Utilisez `proc_open`, `pcntl_fork` ou une bibliothèque de processus parallèles (Symfony Process, Spatie Async) pour exécuter des tâches en parallèle. Comparez avec les files d'attente.

## 21.7 Autres sujets utiles

**Exercice 21.7.1**

Utilisez l'internationalisation : `gettext` ou les fichiers de traduction d'un framework, `NumberFormatter`, `IntlDateFormatter`, `MessageFormatter` (pluriels). Écrivez un site bilingue avec choix de la langue mémorisé.

**Exercice 21.7.2**

Manipulez des images : redimensionnement et miniature avec GD ou Imagick, vérification du type réel, suppression des métadonnées EXIF. Écrivez une fonction `miniature(string $source, string $destination, int $largeur)`.

**Exercice 21.7.3**

Générez un PDF (Dompdf, TCPDF) à partir d'un gabarit HTML et un fichier Excel (PhpSpreadsheet). Envoyez-les en téléchargement.

**Exercice 21.7.4**

Mettez en place une file d'attente et un travailleur (Laravel Queues, Symfony Messenger, ou une table de base de données et un script CLI). Écrivez la gestion des échecs, des nouvelles tentatives et de la file des tâches échouées.

**Exercice 21.7.5**

Écrivez un `Dockerfile` et un `compose.yaml` pour une application PHP (PHP-FPM + Nginx + base de données), avec une image de production allégée (build en plusieurs étapes, `composer install --no-dev --optimize-autoloader`, OPcache activé).

**Exercice 21.7.6**

Décrivez le déploiement d'une application PHP : récupération du code, installation des dépendances, migrations, vidage et réchauffement des caches, redémarrage de PHP-FPM, retour arrière. Écrivez un script de déploiement ou un flux d'intégration et de livraison continue.

**Exercice 21.7.7**

Consultez les principaux réglages de `php.ini` (`memory_limit`, `max_execution_time`, `upload_max_filesize`, `post_max_size`, `date.timezone`, `opcache.*`) et proposez les valeurs adaptées à une application de production moyenne. Justifiez chacune.

---

# 22. Nouveautés par version et aide-mémoire

## 22.1 Chronologie des fonctionnalités

**Exercice 22.1.1**

Associez chaque fonctionnalité à la version qui l'a introduite : `<=>` et `??`, fonctions fléchées, arguments nommés, `match`, `?->`, énumérations, propriétés `readonly`, callables de première classe, classes `readonly`, constantes de classe typées, `#[\Override]`, `json_validate()`, hooks de propriétés, visibilité asymétrique, `array_find`, opérateur pipe `|>`, extension URI, `array_first()` / `array_last()`.

**Exercice 22.1.2**

Pour chaque version de 7.0 à 8.5, écrivez un court exemple (3 à 6 lignes) qui illustre l'une de ses nouveautés et le problème qu'elle résout.

**Exercice 22.1.3**

Modernisez ce code écrit dans le style PHP 5 en utilisant les fonctionnalités récentes :

```php
<?php
class Utilisateur {
    private $nom;
    private $role;
    const ADMIN = 'admin';
    public function __construct($nom, $role) {
        $this->nom = $nom;
        $this->role = $role;
    }
    public function getNom() { return $this->nom; }
    public function estAdmin() { return $this->role == self::ADMIN; }
}
function nomOuDefaut($u) {
    return isset($u) && isset($u->nom) ? $u->nom : 'Invité';
}
switch ($code) {
    case 200: $m = "ok"; break;
    case 404: $m = "absent"; break;
    default: $m = "erreur";
}
$noms = array_map(function ($u) { return $u->getNom(); }, $utilisateurs);
```

**Exercice 22.1.4**

Écrivez un script qui détecte les fonctionnalités disponibles dans l'environnement courant (`PHP_VERSION_ID`, `function_exists('array_find')`, `enum_exists`, `class_exists(Fiber::class)`) et affiche un tableau de compatibilité.

**Exercice 22.1.5**

Consultez les notes de version de PHP 8.6 (en phase de test) et le guide de migration. Choisissez trois nouveautés ou changements et résumez-les avec un exemple. Comment tester votre code sur toutes les versions (3v4l.org, Docker, matrice CI) ?

## 22.2 Fonctions et pratiques dépréciées ou supprimées

**Exercice 22.2.1**

Pour chaque ligne du tableau « à ne plus utiliser », écrivez un exemple de code ancien et son remplacement moderne : `mysql_*`, `FILTER_SANITIZE_STRING`, `md5` / `sha1` pour les mots de passe, `rand` / `mt_rand` / `uniqid` en sécurité, `create_function`, `each`, `eval`, `@`, `$_REQUEST`, `unserialize` sur entrées externes, propriétés dynamiques, paramètre implicitement nullable.

**Exercice 22.2.2**

Corrigez ce code ancien en supprimant toutes les pratiques dépréciées ou dangereuses :

```php
<?php
mysql_connect("localhost", "root", "");
$id = $_REQUEST['id'];
$r = mysql_query("SELECT * FROM t WHERE id = $id");
$mdp = md5($_POST['mdp']);
$jeton = md5(uniqid());
$obj = new stdClass();
$obj->nouvelle = 1;
function f(Utilisateur $u = null) {}
$donnees = unserialize($_COOKIE['d']);
```

**Exercice 22.2.3**

Reproduisez l'avertissement de dépréciation des propriétés dynamiques (8.2) puis corrigez-le de trois façons : déclarer la propriété, utiliser `#[\AllowDynamicProperties]`, utiliser un tableau ou `stdClass`.

**Exercice 22.2.4**

Activez `error_reporting(E_ALL)` et `E_DEPRECATED` sur un projet existant, lancez ses tests et listez toutes les dépréciations. Établissez un plan de correction par ordre de risque. Utilisez PHPStan avec l'extension de dépréciations.

## 22.3 Récapitulatif par besoin

**Exercice 22.3.1**

Pour chaque besoin du tableau (accès à la base, mots de passe, jetons aléatoires, affichage sûr, validation, dates, JSON, dépendances, tests, qualité, journaux, appels HTTP sortants, e-mail), écrivez un petit extrait de code qui illustre l'outil recommandé.

**Exercice 22.3.2**

Concevez un petit projet complet (une API de gestion de contacts) qui met en oeuvre au moins dix lignes du tableau récapitulatif : PDO et requêtes préparées, `password_hash`, `random_bytes`, `htmlspecialchars`, `filter_var`, `DateTimeImmutable`, `json_encode` avec `JSON_THROW_ON_ERROR`, Composer, PHPUnit ou Pest, PHPStan, Monolog, client HTTP, courriel.

**Exercice 22.3.3**

Créez votre propre aide-mémoire d'une page : pour vingt fonctions ou notions du cours, écrivez la signature, un exemple et un piège à éviter.

## 22.4 Ressources

**Exercice 22.4.1**

Parcourez le manuel officiel (php.net/manual/fr). Choisissez cinq fonctions que vous ne connaissiez pas, lisez leur page (paramètres, valeurs de retour, notes de version, exemples) et écrivez un exemple d'utilisation de chacune.

**Exercice 22.4.2**

Lisez « PHP : la bonne méthode » et la recommandation PSR-12. Choisissez cinq règles que vous ne respectiez pas, appliquez-les à un de vos scripts et vérifiez avec un outil (PHP_CodeSniffer, Pint).

**Exercice 22.4.3**

Consultez les fiches OWASP pour PHP. Choisissez trois fiches (injection SQL, XSS, gestion de sessions) et résumez les recommandations. Comparez-les avec ce que fait votre code.

**Exercice 22.4.4**

Utilisez 3v4l.org pour exécuter un même code sur plusieurs versions de PHP. Choisissez trois exemples du chapitre 22.2 et notez le comportement dans chaque version (erreur, avertissement, dépréciation, résultat).

**Exercice 22.4.5** *(défi)*

Projet de synthèse : réalisez une application web complète (par exemple un gestionnaire de tâches ou un blog) avec : PHP 8.5 moderne et typage strict, POO avec énumérations et objets de valeur, PDO et migrations, validation, sessions sécurisées, protection CSRF, hachage des mots de passe, API JSON authentifiée, journalisation, Composer et autoload PSR-4, tests (unitaires et d'intégration), analyse statique et formatage, intégration continue, `Dockerfile`, et un `README` décrivant l'architecture et les choix de sécurité.

---

<div align="center">

*Bon développement !*

</div>
