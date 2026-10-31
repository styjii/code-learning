<div align="center">

# Langage C — Exercices

**Des premiers programmes à la gestion de la mémoire, aux fichiers et à la compilation**

*Mis à jour pour C17 / C23 (octobre 2026)*

</div>

---

## Ressources

| Ressource | Lien |
| --- | --- |
| Cours | [c](/language/c) |
| Projets | [projects](/language/projects/c) |
| Référence | [cppreference.com (C)](https://en.cppreference.com/w/c) |
| Normes | [ISO/IEC 9899 (C23)](https://www.iso.org/standard/82075.html) · [Brouillons WG14](https://www.open-std.org/jtc1/sc22/wg14/) |

---

## Sommaire

**Niveau débutant**

1. [Introduction au C](#1-introduction-au-c)
2. [Structure d'un programme C](#2-structure-dun-programme-c)
3. [Syntaxe et mots-clés](#3-syntaxe-et-mots-clés)
4. [Types de données et variables](#4-types-de-données-et-variables)
5. [Constantes et littéraux](#5-constantes-et-littéraux)
6. [Opérateurs et expressions](#6-opérateurs-et-expressions)
7. [Entrées et sorties](#7-entrées-et-sorties)
8. [Structures de contrôle](#8-structures-de-contrôle)
9. [Fonctions](#9-fonctions)
10. [Portée et durée de vie des variables](#10-portée-et-durée-de-vie-des-variables)

**Niveau intermédiaire**

11. [Tableaux](#11-tableaux)
12. [Chaînes de caractères](#12-chaînes-de-caractères)
13. [Pointeurs](#13-pointeurs)
14. [Allocation dynamique de mémoire](#14-allocation-dynamique-de-mémoire)
15. [Retourner des tableaux et des chaînes](#15-retourner-des-tableaux-et-des-chaînes)
16. [Structures de données dynamiques](#16-structures-de-données-dynamiques)
17. [Pointeurs doubles](#17-pointeurs-doubles)
18. [Structures et unions](#18-structures-et-unions)
19. [Énumérations (`enum`)](#19-énumérations-enum)
20. [`typedef`](#20-typedef)
21. [Pointeurs de fonctions](#21-pointeurs-de-fonctions)

**Niveau avancé**

22. [Gestion des fichiers](#22-gestion-des-fichiers)
23. [Arguments de la ligne de commande](#23-arguments-de-la-ligne-de-commande)
24. [Directives du préprocesseur](#24-directives-du-préprocesseur)
25. [Opérateurs bit à bit](#25-opérateurs-bit-à-bit)
26. [Récursivité](#26-récursivité)
27. [Unicode et caractères larges](#27-unicode-et-caractères-larges)
28. [Compilation et exécution](#28-compilation-et-exécution)
29. [Comportements indéfinis et sécurité](#29-comportements-indéfinis-et-sécurité)
30. [Bibliothèque standard et aide-mémoire](#30-bibliothèque-standard-et-aide-mémoire)

> **Légende** : chaque exercice porte le numéro de la section du cours qu'il illustre (l'exercice 7.3.2 est le deuxième exercice de la section 7.3). *(défi)* = exercice plus difficile ; *(C23)* = exercice nécessitant la norme de 2023. Sauf mention contraire, compilez avec `gcc -std=c17 -Wall -Wextra -Wpedantic -g -fsanitize=address,undefined`. Aucune solution n'est fournie dans ce document.

---

# Niveau débutant

---

# 1. Introduction au C

## 1.1 Qu'est-ce que le C ?

**Exercice 1.1.1**

Indiquez si chaque affirmation est vraie ou fausse, en justifiant :

1. Le C est un langage interprété.
2. Le C est faiblement vérifié à la compilation : de nombreuses conversions de types sont implicites.
3. Le C dispose d'un ramasse-miettes.
4. Un même programme C compile sans modification sur n'importe quelle architecture, sans tenir compte des tailles de types.
5. Le C a été créé pour réécrire le système UNIX.

**Exercice 1.1.2**

Complétez le tableau en vous appuyant sur ce que vous savez du langage :

| Caractéristique | Votre réponse |
| --- | --- |
| Paradigme | |
| Typage | |
| Exécution | |
| Gestion de la mémoire | |
| Portabilité | |

**Exercice 1.1.3**

Citez trois langages influencés par la syntaxe du C et, pour chacun, un point commun et une différence majeure avec le C.

## 1.2 Pourquoi apprendre le C ?

**Exercice 1.2.1**

Pour chaque domaine, expliquez en une phrase pourquoi le C y est utilisé : noyaux de systèmes d'exploitation, microcontrôleurs, interpréteurs de langages, bibliothèques appelées depuis Python.

**Exercice 1.2.2**

Qu'est-ce que l'*ABI* du C et pourquoi sert-elle de « langue commune » entre langages ? Donnez un exemple concret d'utilisation.

**Exercice 1.2.3**

Le cours cite le revers de la médaille : « le C ne vous protège pas ». Donnez trois exemples d'erreurs que le langage ne détecte pas à votre place.

## 1.3 Histoire et normes *(à jour)*

**Exercice 1.3.1**

Associez chaque nouveauté à la norme qui l'a introduite (K&R C, C89, C99, C11, C17, C23) :

1. `<stdint.h>` et les commentaires `//`
2. `nullptr`, `constexpr`, littéraux binaires `0b…`
3. Prototypes de fonctions et `void`
4. `_Generic` et la suppression de `gets()`
5. Version de correction sans nouvelle fonctionnalité
6. `inline` et les tableaux à taille variable

**Exercice 1.3.2**

Quelle option de `gcc` choisit la norme du langage ? Écrivez les commandes pour compiler `prog.c` en C17 puis en C23. Pourquoi faut-il toujours préciser cette option ?

**Exercice 1.3.3**

Écrivez un petit programme qui affiche la valeur de la macro `__STDC_VERSION__`. Compilez-le avec `-std=c99`, `-std=c11`, `-std=c17`, puis `-std=c23` et notez les valeurs obtenues.

## 1.4 Fonctionnement d'un programme C

**Exercice 1.4.1**

Replacez dans l'ordre les étapes de la chaîne de production d'un exécutable : compilateur, préprocesseur, éditeur de liens, assembleur. Pour chacune, donnez le type de fichier produit.

**Exercice 1.4.2**

Quelle est la différence entre un fichier source, un fichier objet et un exécutable ?

## 1.5 Installer un compilateur

**Exercice 1.5.1**

Installez un compilateur C sur votre système (en suivant la méthode du tableau du cours). Vérifiez l'installation avec la commande appropriée et recopiez le numéro de version obtenu.

**Exercice 1.5.2**

Installez un second compilateur (par exemple `clang` si vous utilisez `gcc`) et comparez les messages d'erreur produits sur un même programme volontairement erroné.

## 1.6 Premier programme : « Hello, World ! »

**Exercice 1.6.1**

Écrivez un programme qui affiche `Hello, World !` suivi d'un retour à la ligne. Annotez chaque ligne par un commentaire qui explique son rôle (`#include`, `main`, `printf`, `return`).

**Exercice 1.6.2**

Modifiez le programme pour afficher, sur trois lignes séparées, votre prénom, la norme de C utilisée et la date du jour (écrite en dur).

**Exercice 1.6.3**

Que se passe-t-il si l'on retire `#include <stdio.h>` ? Compilez avec `-Wall` et lisez le message obtenu.

## 1.7 Compiler et exécuter

**Exercice 1.7.1**

Écrivez les commandes pour : compiler `hello.c` en un exécutable nommé `hello`, l'exécuter, puis arrêter la compilation après chacune des quatre étapes (`-E`, `-S`, `-c`, exécutable). Examinez le contenu de chaque fichier intermédiaire.

**Exercice 1.7.2**

Comparez la taille du fichier `hello.i` (après préprocesseur) à celle de `hello.c`. Expliquez la différence.

## 1.8 Erreurs fréquentes de débutant

**Exercice 1.8.1**

Corrigez chacun des programmes suivants :

```c
#include <stdio.h>
int main(void) {
    printf("Bonjour\n")
    return 0;
}
```

```c
#include <stdio.h>
int main(void) {
    int x = 5;
    printf("%d\n", y);
    return 0;
}
```

```c
#include <stdio.h>
void main() {
    printf("Salut\n");
}
```

```c
#include <stdio.h>
int main(void) {
    printf("%d\n");
    return 0;
}
```

**Exercice 1.8.2**

Créez volontairement trois erreurs de compilation différentes (syntaxe, identifiant inconnu, type incompatible) et notez le message de votre compilateur pour chacune.

---

# 2. Structure d'un programme C

## 2.1 Organisation générale

**Exercice 2.1.1**

Écrivez un programme respectant l'organisation générale du cours : directives du préprocesseur, constantes/macros, déclarations de fonctions, fonction `main`, définitions de fonctions. Il doit calculer et afficher le prix TTC d'un article (taux de TVA défini par une macro).

**Exercice 2.1.2**

Pourquoi doit-on déclarer (prototype) une fonction avant de l'appeler ? Que se passe-t-il si la définition de la fonction est placée après `main` sans prototype ?

## 2.2 Les composants

**Exercice 2.2.1**

Identifiez, dans le programme de l'exercice 2.1.1, chacun des composants suivants : directive, macro, fonction, instruction, expression, déclaration, commentaire.

**Exercice 2.2.2**

Distinguez une déclaration, une définition et une initialisation. Donnez un exemple de chacune pour une variable et pour une fonction.

## 2.3 Commentaires

**Exercice 2.3.1**

Écrivez un programme comportant un commentaire sur une ligne, un commentaire sur plusieurs lignes et un commentaire de fin de ligne.

**Exercice 2.3.2**

Pourquoi les commentaires imbriqués `/* … /* … */ … */` posent-ils problème ? Donnez un exemple qui ne compile pas et proposez une solution pour désactiver temporairement un bloc de code contenant déjà des commentaires.

## 2.4 Variables et instructions

**Exercice 2.4.1**

Écrivez un programme qui déclare deux entiers, calcule leur somme, leur produit et leur moyenne (en `double`) puis affiche les trois résultats.

**Exercice 2.4.2**

Écrivez un programme qui échange les valeurs de deux variables avec une variable temporaire.

**Exercice 2.4.3**

Quelle est la différence entre une instruction simple, une instruction composée (bloc) et une instruction vide ? Écrivez un exemple de chaque.

## 2.5 Code de sortie

**Exercice 2.5.1**

Écrivez un programme qui renvoie `EXIT_SUCCESS` ou `EXIT_FAILURE` selon qu'une condition est remplie. Après l'exécution, affichez le code de sortie dans votre terminal (`echo $?` sous Linux/macOS).

**Exercice 2.5.2**

Écrivez un petit script shell qui exécute votre programme et affiche un message différent selon son code de sortie (`&&` et `||`).

## 2.6 Les étapes de la compilation (rappel)

**Exercice 2.6.1**

Pour chacun des messages suivants, indiquez à quelle étape de la compilation l'erreur est détectée (préprocesseur, compilation, édition de liens) : fichier d'en-tête introuvable, point-virgule oublié, fonction déclarée mais jamais définie, macro mal formée.

---

# 3. Syntaxe et mots-clés

## 3.1 Règles de syntaxe

**Exercice 3.1.1**

Le C est sensible à la casse. Écrivez un programme qui déclare trois variables `valeur`, `Valeur` et `VALEUR` avec des contenus différents, puis les affiche.

**Exercice 3.1.2**

Réécrivez sur plusieurs lignes, avec une indentation soignée, ce programme tenant sur une seule ligne :

```c
#include <stdio.h>
int main(void){int a=3,b=4;if(a<b){printf("%d\n",a+b);}else{printf("%d\n",a-b);}return 0;}
```

## 3.2 Identifiants

**Exercice 3.2.1**

Indiquez parmi les identifiants suivants ceux qui sont valides et, pour les autres, la raison : `age`, `2eme`, `_tmp`, `mon-nom`, `total_général`, `int`, `__reserve`, `Prix2`, `a b`, `nombre_d_elements`.

**Exercice 3.2.2**

Pourquoi est-il déconseillé de commencer un identifiant par un tiret bas suivi d'une majuscule, ou par deux tirets bas ? Donnez une convention de nommage cohérente (variables, fonctions, constantes, types) et appliquez-la à un exemple.

## 3.3 Mots-clés du langage *(à jour : C23)*

**Exercice 3.3.1**

Classez chacun des mots-clés suivants dans sa catégorie (types, qualificateurs, classes de stockage, types composés, contrôle, divers) : `volatile`, `typedef`, `goto`, `restrict`, `static`, `sizeof`, `_Complex`, `constexpr`, `thread_local`, `typeof`, `enum`, `inline`.

**Exercice 3.3.2**

Quels mots-clés sont devenus de vrais mots-clés en C23 ? Écrivez un programme qui utilise `bool`, `true`, `false` et `nullptr` sans inclure `<stdbool.h>`, et compilez-le avec `-std=c23`. *(C23)*

## 3.4 Ponctuation et délimiteurs

**Exercice 3.4.1**

Pour chaque symbole du tableau du cours (`;` `,` `{ }` `( )` `[ ]` `#` `*` `&` `->` `.`), écrivez une ligne de code où il apparaît avec un rôle différent, puis expliquez son usage.

**Exercice 3.4.2**

Quelle est la différence de sens entre `*` utilisé dans une déclaration (`int *p;`) et dans une expression (`*p = 3;`) ? Entre `&` unaire et `&` binaire ?

## 3.5 Attributs *(C23)*

**Exercice 3.5.1**

Écrivez une fonction marquée `[[nodiscard]]` et appelez-la en ignorant son résultat. Que dit le compilateur ? *(C23)*

**Exercice 3.5.2**

Utilisez `[[maybe_unused]]` pour supprimer l'avertissement d'une variable non utilisée, puis `[[deprecated("message")]]` sur une fonction ancienne. *(C23)*

**Exercice 3.5.3**

Utilisez `[[fallthrough]]` dans un `switch` volontairement « en cascade » et vérifiez que l'avertissement disparaît. *(C23)*

---

# 4. Types de données et variables

## 4.1 Types fondamentaux

**Exercice 4.1.1**

Écrivez un programme qui affiche, avec `sizeof` et les macros de `<limits.h>` et `<float.h>`, la taille en octets et les valeurs minimales et maximales des types `char`, `short`, `int`, `long`, `long long`, `float`, `double`.

**Exercice 4.1.2**

Complétez le tableau en choisissant le type le plus adapté : âge d'une personne, nombre d'habitants d'un pays, température mesurée avec deux décimales, un octet de données brutes, une longueur de tableau.

| Donnée | Type choisi | Justification |
| --- | --- | --- |
| Âge | | |
| Nombre d'habitants | | |
| Température | | |
| Octet de données | | |
| Longueur d'un tableau | | |

**Exercice 4.1.3**

Qu'affiche `printf("%d\n", 7 / 2);` ? `printf("%f\n", 7 / 2);` ? `printf("%f\n", 7.0 / 2);` ? Expliquez chaque résultat, puis vérifiez en exécutant.

## 4.2 Modificateurs : `signed`, `unsigned`, `short`, `long`

**Exercice 4.2.1**

Que se passe-t-il quand on affecte `-1` à un `unsigned int` ? Écrivez le programme qui l'affiche avec `%u` puis `%d`.

**Exercice 4.2.2**

Calculez à la main, puis vérifiez avec un programme, les plages de valeurs d'un entier signé et non signé sur 8, 16 et 32 bits.

**Exercice 4.2.3**

Pourquoi `char` peut-il être signé ou non signé selon la plateforme ? Écrivez un programme qui détermine si `char` est signé sur votre machine.

## 4.3 Entiers à taille fixe : `<stdint.h>` *(ajout, à jour)*

**Exercice 4.3.1**

Déclarez une variable de chaque type `int8_t`, `uint16_t`, `int32_t`, `uint64_t`, `size_t`, `intptr_t` et affichez leur valeur maximale avec les macros de `<inttypes.h>` (`PRId32`, `PRIu64`, etc.).

**Exercice 4.3.2**

Quand préférer `uint32_t` à `unsigned int` ? Donnez deux situations (format de fichier, protocole réseau, registre matériel, etc.).

**Exercice 4.3.3**

Quelle est la différence entre `int_fast16_t` et `int_least16_t` ? Affichez leur taille sur votre machine.

## 4.4 Booléens

**Exercice 4.4.1**

Écrivez une fonction `bool est_pair(int n)` et utilisez-la dans `main`. Que vaut `true` si on l'affiche avec `%d` ?

**Exercice 4.4.2**

Que valent `(bool)5`, `(bool)0`, `(bool)-3`, `(bool)0.1` ? Vérifiez en exécutant.

**Exercice 4.4.3**

En C89, comment représentait-on les booléens ? Écrivez deux manières de simuler un type booléen sans `<stdbool.h>`.

## 4.5 Déclarer, initialiser, affecter

**Exercice 4.5.1**

Expliquez ce qui diffère entre :

```c
int a;
int b = 0;
int c;
c = 0;
```

Que contient `a` s'il est local ? Et s'il est global ou `static` ?

**Exercice 4.5.2**

Écrivez une déclaration multiple `int x = 1, y = 2, z;` et dites quelles variables sont initialisées. Quel piège cache `int *p, q;` ?

**Exercice 4.5.3**

Affichez la valeur d'une variable locale non initialisée. Que remarquez-vous ? Que dit le compilateur avec `-Wall -Wextra` ? Pourquoi est-ce un comportement indéfini ?

### Inférence de type avec `auto` *(C23)*

**Exercice 4.5.4**

Réécrivez avec `auto` : `int a = 3; double b = 2.5; const char *s = "salut";`. Quel type le compilateur déduit-il pour `auto x = 1u;` et pour `auto y = 'a';` ? Vérifiez avec `typeof` et `sizeof`. *(C23)*

## 4.6 Conversions de types (*casts*)

**Exercice 4.6.1**

Écrivez une fonction `double moyenne(int somme, int n)` en deux versions : l'une qui renvoie un résultat tronqué et l'autre qui renvoie le résultat exact. Quel `cast` utiliser et à quel endroit ?

**Exercice 4.6.2**

Prédisez puis vérifiez la sortie :

```c
#include <stdio.h>

int main(void) {
    int a = 3, b = 2;
    double d1 = a / b;
    double d2 = (double)a / b;
    double d3 = (double)(a / b);
    int e = 3.99;
    char c = 321;
    printf("%f %f %f %d %d\n", d1, d2, d3, e, c);
    return 0;
}
```

**Exercice 4.6.3**

Qu'est-ce que la promotion entière ? Que valent `sizeof('a')` en C et `sizeof('a')` en C++ ? Pourquoi `char + char` donne-t-il un `int` ?

**Exercice 4.6.4**

Quel est le résultat de la comparaison `-1 < 1u` ? Expliquez le résultat par les règles de conversion arithmétique habituelle.

## 4.7 Bonnes pratiques

**Exercice 4.7.1**

Relevez dans le code suivant cinq mauvaises pratiques liées aux types et aux variables, puis corrigez-le :

```c
#include <stdio.h>

int main(void) {
    int x, y;
    float moyenne;
    int tailles[5];
    x = 7;
    moyenne = x / 2;
    for (y = 0; y < 5; y++)
        tailles[y] = y * 1000000000;
    printf("%f %d\n", moyenne, tailles[4]);
    return 0;
}
```

---

# 5. Constantes et littéraux

## 5.1 Littéraux

**Exercice 5.1.1**

Écrivez la valeur 255 sous quatre formes : décimale, octale, hexadécimale, binaire (C23). Affichez-les avec `%d`, `%o`, `%x`, `%X`. *(C23)*

**Exercice 5.1.2**

Quelle est la différence entre `10`, `10u`, `10L`, `10UL`, `10LL` ? Entre `3.14`, `3.14f`, `3.14L` ? Affichez la taille de chacun avec `sizeof`.

**Exercice 5.1.3**

Écrivez `1'000'000` comme littéral avec séparateur et affichez-le. *(C23)*

**Exercice 5.1.4**

Que valent `'A'`, `'a'`, `'0'`, `'\n'` en ASCII ? Écrivez un programme qui affiche le code ASCII de chaque caractère d'un mot donné.

### Séquences d'échappement

**Exercice 5.1.5**

Écrivez un programme qui affiche exactement :

```text
Il a dit : "Bonjour !"
Chemin : C:\temp\fichier.txt
Colonne1	Colonne2	Colonne3
Pourcentage : 50%
```

**Exercice 5.1.6**

Quel est le rôle de `\0`, `\a`, `\r`, `\b`, `\'`, `\xHH` et `\ooo` ? Écrivez un exemple d'usage de chacun.

## 5.2 Définir des constantes

**Exercice 5.2.1**

Définissez la constante `PI` de trois façons différentes : `#define`, `const double`, `enum` (pour une constante entière). Comparez leurs avantages et inconvénients (typage, portée, adresse, débogage).

**Exercice 5.2.2**

Pourquoi ne faut-il pas mettre de point-virgule à la fin d'un `#define` ? Que produit `#define N 10;` si l'on écrit `int t[N];` ?

**Exercice 5.2.3**

Écrivez un programme calculant l'aire d'un cercle avec `constexpr double PI = 3.14159;`. Pourquoi `constexpr` est-il plus fort que `const` ? *(C23)*

**Exercice 5.2.4**

Pourquoi `const int n = 10; int t[n];` pose-t-il problème en C89 et est-il accepté comme VLA en C99 ? Quelle alternative sûre utiliser ?

## 5.3 `const` et pointeurs

**Exercice 5.3.1**

Pour chaque déclaration, dites ce qui est constant (le pointeur, la donnée pointée, les deux) et quelles affectations sont interdites :

```c
const int *p1;
int *const p2 = &x;
const int *const p3 = &x;
int const *p4;
```

**Exercice 5.3.2**

Pour chaque ligne suivante, indiquez si elle compile ; justifiez :

```c
const int a = 5;
int *p = &a;
*p = 6;
const int *q = &a;
*q = 7;
q = &b;
```

**Exercice 5.3.3**

Écrivez une fonction `size_t longueur(const char *s)` et expliquez pourquoi `const` y est une bonne pratique.

## 5.4 Constantes prédéfinies utiles

**Exercice 5.4.1**

Affichez `INT_MAX`, `INT_MIN`, `UINT_MAX`, `LONG_MAX`, `CHAR_BIT`, `FLT_EPSILON`, `DBL_MAX` et `RAND_MAX`. Avec quel en-tête obtient-on chacune ?

**Exercice 5.4.2**

Affichez `EXIT_SUCCESS`, `EXIT_FAILURE`, `NULL`, `__FILE__`, `__LINE__`, `__DATE__`, `__TIME__`, `__func__`.

---

# 6. Opérateurs et expressions

## 6.1 Catégories

**Exercice 6.1.1**

Écrivez un programme qui, pour deux entiers `a = 17` et `b = 5`, affiche le résultat de chaque opérateur arithmétique, de comparaison, logique, bit à bit et d'affectation composée (`+=`, `-=`, `*=`, `/=`, `%=`).

**Exercice 6.1.2**

Que valent `-7 / 2`, `-7 % 2`, `7 % -2` et `-7 % -2` ? Vérifiez avec un programme et rappelez la règle donnée par le C99 (division tronquée vers zéro).

**Exercice 6.1.3**

Écrivez une expression qui teste qu'un entier `n` est divisible à la fois par 3 et par 5.

## 6.2 Incrémentation : préfixe et suffixe

**Exercice 6.2.1**

Prédisez les valeurs de `a`, `b`, `c` après chaque ligne :

```c
int a = 5;
int b = a++;
int c = ++a;
int d = a-- + --a;   /* attention : à ne pas écrire */
```

Pourquoi la dernière ligne est-elle à éviter ?

**Exercice 6.2.2**

Quel est le résultat de `i = i++;` ? Justifiez par la notion de comportement indéfini.

**Exercice 6.2.3**

Réécrivez une boucle `while` qui parcourt un tableau en utilisant `i++` dans l'accès, puis la même boucle en séparant l'incrémentation. Laquelle est la plus lisible ?

## 6.3 Opérateurs logiques et évaluation paresseuse

**Exercice 6.3.1**

Qu'affiche le programme suivant ? Expliquez avec l'évaluation paresseuse (court-circuit) :

```c
#include <stdio.h>

int a(void) { puts("a"); return 0; }
int b(void) { puts("b"); return 1; }

int main(void) {
    if (a() && b()) puts("1");
    if (a() || b()) puts("2");
    if (b() || a()) puts("3");
    return 0;
}
```

**Exercice 6.3.2**

Écrivez une condition sûre qui teste `p != NULL && *p > 0` et expliquez pourquoi l'ordre des deux opérandes est essentiel.

**Exercice 6.3.3**

Que valent `!5`, `!0`, `!!7`, `5 && 0`, `3 || 0`, `1 && 2` ? Quel type ont ces résultats en C ?

## 6.4 Ternaire

**Exercice 6.4.1**

Écrivez avec l'opérateur ternaire : le maximum de deux nombres, la valeur absolue d'un entier, le signe d'un entier (`-1`, `0`, `1`) en imbriquant deux ternaires.

**Exercice 6.4.2**

Écrivez `printf("%d fichier%s\n", n, n > 1 ? "s" : "");` et testez-le avec `n` valant 0, 1, 2.

**Exercice 6.4.3**

Quand l'usage du ternaire nuit-il à la lisibilité ? Donnez un exemple et sa réécriture avec `if`.

## 6.5 `sizeof` et opérateur virgule

**Exercice 6.5.1**

Que valent `sizeof(int)`, `sizeof(int[10])`, `sizeof(char *)`, `sizeof("abc")`, `sizeof(struct { char c; int i; })` sur votre machine ? Expliquez chaque résultat.

**Exercice 6.5.2**

Pourquoi `sizeof` appliqué à un paramètre de fonction déclaré `int t[]` ne donne-t-il pas la taille du tableau ? Écrivez un exemple.

**Exercice 6.5.3**

Que vaut `int x = (1, 2, 3);` ? Écrivez une boucle `for` qui utilise l'opérateur virgule pour incrémenter deux variables à la fois.

## 6.6 Priorité et associativité

**Exercice 6.6.1**

Ajoutez toutes les parenthèses implicites, puis évaluez :

1. `2 + 3 * 4 - 1`
2. `1 + 2 << 3`
3. `a = b = 5`
4. `x & 1 == 0` (avec `x = 4`)
5. `!a && b || c`
6. `*p++`
7. `-2 * -3 + 4 % 3`

**Exercice 6.6.2**

Pourquoi `x & 1 == 0` ne teste-t-il pas la parité de `x` ? Écrivez la bonne expression.

**Exercice 6.6.3**

Classez par priorité décroissante : `*` (déréférencement), `+` (binaire), `&&`, `=`, `==`, `<<`, `?:`, `,`, `->`, `!`.

## 6.7 Comportements à éviter

**Exercice 6.7.1**

Parmi les expressions suivantes, repérez celles qui provoquent un comportement indéfini et justifiez :

```c
int x = INT_MAX; x + 1;
unsigned u = UINT_MAX; u + 1;
int d = 5 / 0;
int s = 1 << 32;
int t = -1 << 1;
int i = 0; i = i++ + ++i;
int *p = NULL; *p = 1;
char c = 200;
```

**Exercice 6.7.2**

Écrivez un test portable qui détecte un débordement avant d'ajouter deux entiers signés (sans déclencher le comportement indéfini).

**Exercice 6.7.3**

Pourquoi la comparaison de flottants avec `==` est-elle dangereuse ? Écrivez le test `0.1 + 0.2 == 0.3`, puis une fonction `egaux(double a, double b, double eps)`.

## 6.8 Arithmétique vérifiée *(C23)*

**Exercice 6.8.1**

Utilisez `ckd_add`, `ckd_sub` et `ckd_mul` de `<stdckdint.h>` pour écrire trois fonctions qui renvoient `false` en cas de débordement. Testez avec `INT_MAX`. *(C23)*

**Exercice 6.8.2**

Écrivez `bool factorielle(int n, long long *resultat)` qui s'arrête dès que le débordement est détecté. Pour quelle valeur de `n` la fonction échoue-t-elle ? *(C23)*

---

# 7. Entrées et sorties

## 7.1 Affichage : `printf` et `puts`

**Exercice 7.1.1**

Quelle est la différence entre `puts("abc")` et `printf("abc")` ? Pourquoi `printf(chaine)` est-il dangereux quand `chaine` vient de l'utilisateur ?

**Exercice 7.1.2**

Que renvoie `printf` ? Écrivez un programme qui affiche le nombre de caractères écrits par un appel précédent.

### Spécificateurs de format

**Exercice 7.1.3**

Écrivez le spécificateur adapté pour afficher : un `int`, un `unsigned`, un `long`, un `long long`, un `size_t`, un `double`, un `char`, une chaîne, un pointeur, un `int64_t`, un pourcentage littéral.

**Exercice 7.1.4**

Affichez le nombre 255 en décimal, en octal, en hexadécimal minuscule et majuscule, avec le préfixe `0x`, et en notation scientifique pour `12345.678`.

### Largeur, alignement, remplissage

**Exercice 7.1.5**

Affichez le tableau suivant, aligné avec des largeurs de champ (les noms alignés à gauche sur 10 colonnes, les prix alignés à droite sur 8 colonnes avec 2 décimales) :

```text
Nom       |     Prix
Pomme     |     1.20
Banane    |    12.50
Kiwi      |     0.75
```

**Exercice 7.1.6**

Que produisent `printf("%5d|", 42)`, `printf("%-5d|", 42)`, `printf("%05d|", 42)`, `printf("%+d|", 42)`, `printf("%.3f|", 3.14159)`, `printf("%8.3f|", 3.14159)`, `printf("%.*d|", 4, 7)` ? Vérifiez.

## 7.2 Lecture : `scanf`

**Exercice 7.2.1**

Écrivez un programme qui lit deux entiers avec `scanf` et affiche leur somme. Vérifiez la valeur de retour de `scanf`.

**Exercice 7.2.2**

Que se passe-t-il si l'utilisateur saisit `abc` alors que le programme attend un entier ? Écrivez une version robuste.

**Exercice 7.2.3**

Pourquoi `scanf("%s", tampon)` est-il dangereux ? Écrivez la version avec limite pour un tampon de 20 caractères.

**Exercice 7.2.4**

Pour lire un `double`, faut-il `%f` ou `%lf` avec `scanf` ? Et avec `printf` ? Écrivez un programme qui lit puis affiche un `double`.

**Exercice 7.2.5**

Que fait `scanf("%d-%d-%d", &j, &m, &a)` avec la saisie `25-12-2026` ? Et avec `25/12/2026` ?

## 7.3 Lire une ligne : `fgets` *(à jour)*

**Exercice 7.3.1**

Écrivez un programme qui lit une ligne de 50 caractères au plus avec `fgets`, supprime le `'\n'` final avec `strcspn`, puis affiche la ligne et sa longueur.

**Exercice 7.3.2**

Que se passe-t-il quand la ligne saisie est plus longue que le tampon ? Comment détecter ce cas ?

### Lecture sûre d'un nombre

**Exercice 7.3.3**

Écrivez `bool lire_entier(int *resultat)` qui lit une ligne avec `fgets`, la convertit avec `strtol`, vérifie qu'aucun caractère invalide ne reste et que la valeur tient dans un `int`.

**Exercice 7.3.4**

Écrivez de même `bool lire_double(double *resultat)` avec `strtod`.

### Vider le tampon d'entrée

**Exercice 7.3.5**

Écrivez un programme qui lit un entier avec `scanf` puis une ligne avec `fgets`. Constatez le problème du `'\n'` laissé dans le tampon, puis corrigez-le avec une fonction `vider_tampon()`.

**Exercice 7.3.6**

Pourquoi `fflush(stdin)` n'est-il pas portable ? Quelle est l'alternative standard ?

## 7.4 Autres fonctions d'E/S

**Exercice 7.4.1**

Écrivez un programme qui lit des caractères avec `getchar` jusqu'à `EOF` et compte le nombre de lignes, de mots et de caractères (comme `wc`). Pourquoi `getchar` renvoie-t-il un `int` ?

**Exercice 7.4.2**

Utilisez `snprintf` pour construire la chaîne `"Joueur-007 : 1250 points"` dans un tampon de taille limitée. Que se passe-t-il si le tampon est trop petit, et comment le détecter avec la valeur de retour ?

**Exercice 7.4.3**

Utilisez `sscanf` pour extraire un entier et un mot de `"42 pommes"`.

**Exercice 7.4.4**

Affichez un message d'erreur sur `stderr` avec `fprintf`, puis un message d'erreur système avec `perror` après l'échec de `fopen("absent.txt", "r")`.

## 7.5 Flux standard

**Exercice 7.5.1**

Écrivez un programme qui écrit une ligne sur `stdout` et une ligne sur `stderr`. Exécutez-le en redirigeant seulement `stdout` vers un fichier, puis seulement `stderr`, puis les deux. Notez ce que vous observez.

**Exercice 7.5.2**

Affichez `Entrez un nombre : ` sans retour à la ligne avant de lire un entier. Pourquoi faut-il parfois `fflush(stdout)` ?

**Exercice 7.5.3**

Écrivez un programme qui lit des nombres sur `stdin` jusqu'à `EOF` et affiche leur somme. Testez-le avec `echo "1 2 3" | ./prog` et avec une redirection depuis un fichier.

## 7.6 Erreurs courantes

**Exercice 7.6.1**

Corrigez les six erreurs du programme suivant :

```c
#include <stdio.h>

int main(void) {
    int age;
    double taille;
    char nom[10];
    scanf("%d", age);
    scanf("%f", &taille);
    gets(nom);
    scanf("%s", nom);
    printf("%s a %d ans et mesure %f\n", nom, age);
    return 0;
}
```

---

# 8. Structures de contrôle

## 8.1 Conditions : `if`, `else if`, `else`

**Exercice 8.1.1**

Écrivez un programme qui lit une note sur 20 et affiche la mention (insuffisant, passable, assez bien, bien, très bien) avec une chaîne `if / else if / else`.

**Exercice 8.1.2**

Écrivez un programme qui détermine si une année est bissextile (divisible par 4, sauf les siècles non divisibles par 400).

**Exercice 8.1.3**

Écrivez un programme qui trie trois entiers saisis par ordre croissant avec uniquement des `if`.

**Exercice 8.1.4**

Pourquoi `if (x = 5)` est-il presque toujours une erreur ? Quelle convention (« Yoda ») ou quelle option de compilation permet de l'éviter ?

**Exercice 8.1.5**

Réécrivez ce code ambigu avec des accolades pour lever le problème du « else pendant », puis dites ce qu'il affichait avant :

```c
if (a > 0)
    if (b > 0)
        puts("deux positifs");
else
    puts("a négatif ou nul");
```

## 8.2 `switch`

**Exercice 8.2.1**

Écrivez un programme qui lit un chiffre de 1 à 7 et affiche le jour de la semaine correspondant avec un `switch`. Traitez le cas `default`.

**Exercice 8.2.2**

Écrivez une mini-calculatrice : lire deux nombres et un opérateur (`+`, `-`, `*`, `/`) et afficher le résultat avec `switch`. Traitez la division par zéro.

**Exercice 8.2.3**

Expliquez la chute (*fall-through*) en écrivant un programme qui compte le nombre de voyelles et de consonnes d'une chaîne en regroupant les cas `'a'`, `'e'`, `'i'`, `'o'`, `'u'`.

**Exercice 8.2.4**

Quels types sont autorisés dans l'expression d'un `switch` ? Pourquoi un `switch` sur un `double` ou sur une chaîne est-il refusé ? Comment simuler un `switch` sur chaînes ?

## 8.3 Boucles

**Exercice 8.3.1**

Écrivez les trois types de boucles (`for`, `while`, `do … while`) qui affichent les entiers de 1 à 10. Quelle est la différence essentielle entre `while` et `do … while` ?

**Exercice 8.3.2**

Écrivez un programme qui calcule la somme des chiffres d'un entier positif avec une boucle `while`.

**Exercice 8.3.3**

Écrivez un programme qui affiche la table de multiplication d'un nombre lu au clavier, alignée.

**Exercice 8.3.4**

Écrivez un programme qui calcule la factorielle de `n` avec une boucle et choisit un type suffisant (`unsigned long long`). À partir de quelle valeur de `n` y a-t-il débordement ?

**Exercice 8.3.5**

Écrivez un menu avec `do … while` qui boucle tant que l'utilisateur ne choisit pas « Quitter ».

**Exercice 8.3.6**

Écrivez un programme qui affiche les nombres premiers inférieurs à 100.

**Exercice 8.3.7**

Que fait `for (;;)` ? Que fait `for (int i = 10; i >= 0; i--)` si `i` est de type `unsigned` ? Corrigez.

### Boucle infinie

**Exercice 8.3.8**

Écrivez une boucle infinie volontaire qui lit des nombres jusqu'à ce que l'utilisateur saisisse `0`, puis sort avec `break`. Écrivez ensuite trois exemples de boucles infinies involontaires.

## 8.4 `break`, `continue`, `goto`

**Exercice 8.4.1**

Écrivez un programme qui cherche le premier multiple de 7 supérieur à 100 avec `break`.

**Exercice 8.4.2**

Écrivez un programme qui affiche les entiers de 1 à 20 en sautant les multiples de 3 avec `continue`.

**Exercice 8.4.3**

Montrez, avec deux boucles imbriquées, que `break` ne sort que de la boucle la plus interne. Écrivez deux façons de sortir des deux boucles : avec un drapeau, puis avec `goto`.

**Exercice 8.4.4**

Écrivez une fonction qui ouvre deux fichiers et alloue un tampon, avec un nettoyage unique à la fin grâce à `goto fin;` (modèle d'erreur propre en C).

**Exercice 8.4.5**

Quels sont les usages acceptables de `goto` en C ? Pourquoi est-il déconseillé d'utiliser `goto` pour « remonter » dans le code ?

## 8.5 Boucles imbriquées

**Exercice 8.5.1**

Affichez avec deux boucles `for` imbriquées les triangles suivants (pour `n = 5`) :

```text
*
**
***
****
*****
```

```text
    *
   ***
  *****
 *******
*********
```

**Exercice 8.5.2**

Affichez la table de multiplication de 1 à 10 sous forme de grille.

**Exercice 8.5.3**

Trouvez tous les triplets pythagoriciens `(a, b, c)` avec `a < b < c ≤ 100`.

**Exercice 8.5.4**

Quelle est la complexité (en nombre d'itérations) d'un double `for` de `n` itérations chacun ? Écrivez un compteur pour `n = 1000` pour le vérifier.

## 8.6 Pièges classiques

**Exercice 8.6.1**

Corrigez les erreurs de chacune des boucles suivantes :

```c
for (int i = 0; i < 10; i++);
    printf("%d\n", i);

int i = 0;
while (i < 10)
    printf("%d\n", i);
    i++;

for (int i = 0; i <= 10; i++)
    tab[i] = 0;          /* tab de taille 10 */

while (c = getchar() != EOF)
    putchar(c);
```

**Exercice 8.6.2**

Pourquoi `for (double x = 0; x != 1.0; x += 0.1)` ne s'arrête-t-il peut-être jamais ? Proposez une boucle correcte.

---

# 9. Fonctions

## 9.1 Définir et appeler

**Exercice 9.1.1**

Écrivez les fonctions suivantes, avec leur prototype, et testez-les dans `main` : `int carre(int)`, `int max2(int, int)`, `int max3(int, int, int)`, `bool est_premier(int)`, `unsigned long long factorielle(unsigned)`, `double puissance(double, int)`.

**Exercice 9.1.2**

Écrivez une fonction sans valeur de retour `void afficher_triangle(int n)` puis une fonction sans paramètre `int lire_entier_positif(void)`. Quelle est la différence entre `int f()` et `int f(void)` (selon la norme de votre choix) ?

**Exercice 9.1.3**

Que se passe-t-il si une fonction non `void` n'exécute pas de `return` dans un chemin d'exécution ? Écrivez un exemple et lisez l'avertissement du compilateur.

## 9.2 Passage des arguments : toujours **par valeur**

**Exercice 9.2.1**

Écrivez une fonction `echanger_faux(int a, int b)` qui tente d'échanger deux entiers. Montrez qu'elle ne modifie pas les variables de l'appelant, puis écrivez `echanger(int *a, int *b)` correcte.

**Exercice 9.2.2**

Écrivez une fonction `void min_max(const int *t, size_t n, int *min, int *max)` qui renvoie deux résultats par pointeurs. Testez-la.

**Exercice 9.2.3**

Écrivez une fonction `bool diviser(int a, int b, int *quotient, int *reste)` qui renvoie `false` si `b == 0`. Quel modèle de gestion d'erreur illustre-t-elle ?

**Exercice 9.2.4**

Pourquoi passer un tableau à une fonction modifie-t-il le tableau d'origine alors que C passe tout par valeur ? Écrivez un exemple.

**Exercice 9.2.5**

Qu'affiche ce programme ? Expliquez :

```c
#include <stdio.h>

void f(int n) { n *= 2; }
void g(int *p) { *p *= 2; }
void h(int *p) { p = NULL; }

int main(void) {
    int x = 5;
    f(x); printf("%d\n", x);
    g(&x); printf("%d\n", x);
    int *q = &x;
    h(q); printf("%p\n", (void *)q);
    return 0;
}
```

## 9.3 Plusieurs fichiers : en-têtes et sources

**Exercice 9.3.1**

Créez un module `maths` composé de `maths.h` (avec garde d'inclusion) et de `maths.c` qui contient `somme`, `produit`, `puissance`, `est_premier`. Écrivez `main.c` qui les utilise et la commande pour compiler le tout.

**Exercice 9.3.2**

Que se passe-t-il si l'on met la **définition** d'une fonction dans `maths.h` et que deux `.c` incluent cet en-tête ? Quel message obtient-on à l'édition de liens ?

**Exercice 9.3.3**

Quelle est la différence entre `#include <x.h>` et `#include "x.h"` ? Comment ajouter un dossier de recherche d'en-têtes avec `-I` ?

**Exercice 9.3.4**

Ajoutez à votre module une fonction `static` interne (non visible depuis l'extérieur) et une variable globale partagée déclarée `extern` dans l'en-tête et définie dans le `.c`. Expliquez le rôle de chaque mot-clé.

## 9.4 Fonctions variadiques

**Exercice 9.4.1**

Écrivez `int somme(int n, ...)` qui additionne `n` entiers passés en arguments variables avec `<stdarg.h>`.

**Exercice 9.4.2**

Écrivez `double moyenne(int n, ...)` puis `void journal(const char *format, ...)` qui préfixe chaque message de `[LOG]` en utilisant `vprintf`.

**Exercice 9.4.3**

Quels sont les dangers des fonctions variadiques (aucun contrôle de type, nombre d'arguments) ? Que se passe-t-il si on passe un `double` alors que la fonction lit un `int` avec `va_arg` ?

## 9.5 Fonctions et mémoire : points d'attention

**Exercice 9.5.1**

Quel est le problème de cette fonction ? Corrigez-la de deux façons :

```c
int *creer(void) {
    int x = 42;
    return &x;
}
```

**Exercice 9.5.2**

Pourquoi renvoyer une structure volumineuse par valeur peut-il être coûteux ? Quand préfère-t-on la passer par pointeur `const` ?

**Exercice 9.5.3**

Observez la pile : écrivez une fonction récursive qui affiche l'adresse d'une variable locale à chaque appel. Dans quel sens évoluent les adresses ?

## 9.6 Bonnes pratiques

**Exercice 9.6.1**

Refactorisez ce code monolithique en petites fonctions bien nommées (lecture, calcul, affichage), avec prototypes et `const` là où c'est utile :

```c
#include <stdio.h>

int main(void) {
    int n, s = 0, i, v;
    scanf("%d", &n);
    for (i = 0; i < n; i++) {
        scanf("%d", &v);
        s += v;
    }
    printf("moyenne = %f\n", (double)s / n);
    return 0;
}
```

**Exercice 9.6.2**

Rédigez un commentaire de documentation (but, paramètres, valeur de retour, préconditions, propriété de la mémoire) pour une fonction `char *copier(const char *src)`.

---

# 10. Portée et durée de vie des variables

## 10.1 Les portées

**Exercice 10.1.1**

Identifiez la portée (bloc, fonction, fichier, prototype) de chaque variable du programme suivant, et prédisez la sortie :

```c
#include <stdio.h>

int g = 10;

void f(int p) {
    int g = 20;
    {
        int g = 30;
        printf("%d %d\n", g, p);
    }
    printf("%d\n", g);
}

int main(void) {
    f(1);
    printf("%d\n", g);
    return 0;
}
```

**Exercice 10.1.2**

Qu'est-ce que l'ombrage (*shadowing*) ? Quelle option du compilateur permet de le signaler (`-Wshadow`) ?

**Exercice 10.1.3**

Pourquoi la variable de boucle `for (int i = 0; …)` n'est-elle pas visible après la boucle ? Écrivez un code qui le démontre.

**Exercice 10.1.4**

Écrivez un programme qui utilise une variable globale modifiée par deux fonctions. Énumérez deux inconvénients des variables globales et proposez un remplacement par paramètres.

## 10.2 Classes de stockage et durée de vie

**Exercice 10.2.1**

Complétez le tableau (durée de vie, portée, initialisation par défaut) :

| Déclaration | Durée de vie | Portée | Valeur initiale par défaut |
| --- | --- | --- | --- |
| Variable locale | | | |
| Variable locale `static` | | | |
| Variable globale | | | |
| Variable globale `static` | | | |
| Variable `extern` | | | |
| Allocation `malloc` | | | |

**Exercice 10.2.2**

Écrivez une fonction `compteur()` qui renvoie le nombre de fois où elle a été appelée, grâce à une variable locale `static`. Que se passe-t-il pour une variable locale ordinaire ?

**Exercice 10.2.3**

Écrivez deux fichiers `a.c` et `b.c` : `a.c` définit une variable globale `compteur`, `b.c` la modifie via `extern`. Puis rendez-la privée à `a.c` avec `static` et constatez l'erreur de liaison.

**Exercice 10.2.4**

À quoi servent `register`, `volatile` et `thread_local` ? Donnez un exemple d'usage réaliste de `volatile`. *(C23 pour `thread_local`)*

**Exercice 10.2.5**

Qu'affiche ce programme ? Expliquez :

```c
#include <stdio.h>

void f(void) {
    static int n = 0;
    int m = 0;
    n++; m++;
    printf("%d %d\n", n, m);
}

int main(void) {
    f(); f(); f();
    return 0;
}
```

## 10.3 Organisation de la mémoire d'un programme

**Exercice 10.3.1**

Dessinez la disposition de la mémoire d'un programme (code, données initialisées, données non initialisées, tas, pile). Dans quelle zone se trouve chaque élément : variable globale initialisée, variable globale non initialisée, variable locale, littéral de chaîne, bloc alloué par `malloc`, variable `static` locale, code d'une fonction ?

**Exercice 10.3.2**

Écrivez un programme qui affiche l'adresse d'une variable de chaque zone ci-dessus. Classez-les par adresse croissante et comparez avec votre dessin.

**Exercice 10.3.3**

Que se passe-t-il quand la pile est épuisée ? Écrivez une récursion infinie et observez l'erreur. Quelle commande permet de voir ou modifier la taille maximale de la pile (`ulimit -s`) ?

**Exercice 10.3.4**

Pourquoi un grand tableau local (`int t[10000000];`) est-il dangereux alors que `malloc` permet la même taille sans problème ?

## 10.4 Bonnes pratiques

**Exercice 10.4.1**

Réécrivez ce programme pour supprimer toutes les variables globales en passant les données par paramètres :

```c
#include <stdio.h>

int total = 0;
int n = 0;

void ajouter(int v) { total += v; n++; }
double moyenne(void) { return (double)total / n; }

int main(void) {
    ajouter(4); ajouter(8); ajouter(15);
    printf("%f\n", moyenne());
    return 0;
}
```

**Exercice 10.4.2**

Listez cinq règles pour réduire la portée des variables (déclarer au plus près de l'usage, éviter les globales, préférer `static` pour les symboles privés, etc.) et appliquez-les en réécrivant un de vos programmes précédents.

---

# Niveau intermédiaire

---

# 11. Tableaux

## 11.1 Déclarer et initialiser

**Exercice 11.1.1**

Déclarez et initialisez : un tableau de 5 entiers avec valeurs explicites, un tableau de 10 entiers entièrement à zéro, un tableau dont la taille est déduite de l'initialiseur, un tableau de 6 éléments dont seuls les indices 1 et 4 sont initialisés (initialisation désignée).

**Exercice 11.1.2**

Écrivez la macro `NB_ELEMENTS(t)` qui calcule le nombre d'éléments d'un tableau. Pourquoi ne fonctionne-t-elle pas sur un tableau reçu en paramètre de fonction ?

**Exercice 11.1.3**

Que contiennent `int a[5] = {1, 2};` et `int b[5] = {0};` et `int c[5];` (local) ? Vérifiez en les affichant.

**Exercice 11.1.4**

Écrivez un programme qui lit 10 entiers dans un tableau puis les affiche dans l'ordre inverse.

## 11.2 Parcourir

**Exercice 11.2.1**

Écrivez les fonctions suivantes sur un tableau d'entiers : somme, moyenne, minimum, maximum, indice du maximum, nombre d'éléments pairs.

**Exercice 11.2.2**

Écrivez `int rechercher(const int *t, size_t n, int x)` qui renvoie l'indice de la première occurrence ou `-1`. Pourquoi `size_t` pour la taille et un type signé pour l'indice renvoyé ?

**Exercice 11.2.3**

Écrivez `void inverser(int *t, size_t n)` qui inverse un tableau sur place, sans tableau auxiliaire.

**Exercice 11.2.4**

Écrivez un programme qui affiche l'histogramme des valeurs d'un tableau (une ligne de `*` par élément).

**Exercice 11.2.5**

Qu'est-ce que la boucle `for (size_t i = n - 1; i >= 0; i--)` a de problématique ? Écrivez deux corrections.

## 11.3 Tableaux multidimensionnels

**Exercice 11.3.1**

Déclarez une matrice `int m[3][4]` initialisée avec des valeurs de votre choix et affichez-la ligne par ligne.

**Exercice 11.3.2**

Écrivez des fonctions pour : la somme de chaque ligne, la somme de chaque colonne, la transposée d'une matrice carrée, la trace d'une matrice carrée.

**Exercice 11.3.3**

Écrivez le produit de deux matrices (`m × n` par `n × p`) dans une matrice résultat.

**Exercice 11.3.4**

Un tableau 2D est stocké en mémoire ligne après ligne. Écrivez un programme qui affiche l'adresse de chaque élément de `int m[2][3]` pour le démontrer. Quelle formule donne l'adresse de `m[i][j]` ?

**Exercice 11.3.5**

Écrivez le triangle de Pascal sur 10 lignes dans un tableau 2D.

## 11.4 Tableaux à taille variable (VLA)

**Exercice 11.4.1**

Écrivez un programme qui lit `n` au clavier, déclare un VLA `int t[n]`, le remplit des `n` premiers carrés et l'affiche. Que se passe-t-il pour une grande valeur de `n` ? Pourquoi les VLA sont-ils déconseillés pour des tailles non maîtrisées ?

**Exercice 11.4.2**

Que renvoie `sizeof` appliqué à un VLA ? En quoi est-ce différent d'un tableau classique (évalué à l'exécution) ? Vérifiez.

**Exercice 11.4.3**

Écrivez le même programme avec `malloc` à la place du VLA. Comparez le traitement des erreurs.

## 11.5 Tableaux et fonctions

**Exercice 11.5.1**

Écrivez `void afficher(const int t[], size_t n)` puis `void remplir(int t[], size_t n, int valeur)`. Pourquoi la taille doit-elle toujours être passée en paramètre ?

**Exercice 11.5.2**

Écrivez une fonction qui reçoit une matrice `int m[][4]` avec un nombre de lignes variable. Pourquoi la dernière dimension est-elle obligatoire ? Comment écrire la même fonction avec des tailles variables (`int n, int p, int m[n][p]`) ?

**Exercice 11.5.3**

Écrivez une fonction qui renvoie le nombre d'éléments d'un tableau, avec `sizeof` à l'intérieur de la fonction, puis à l'extérieur. Expliquez la différence de résultat.

## 11.6 Opérations courantes

**Exercice 11.6.1**

Utilisez `memcpy` pour copier un tableau, `memset` pour le mettre à zéro, `memcmp` pour comparer deux tableaux. Pourquoi `memset(t, 1, sizeof t)` ne met-il pas chaque entier à 1 ?

**Exercice 11.6.2**

Écrivez `insérer(int *t, size_t *n, size_t pos, int v)` et `supprimer(int *t, size_t *n, size_t pos)` qui décalent les éléments avec `memmove`. Pourquoi `memmove` et non `memcpy` ?

**Exercice 11.6.3**

Écrivez un tri à bulles, un tri par sélection et un tri par insertion sur un tableau d'entiers. Comparez leur nombre de comparaisons sur 1000 éléments aléatoires.

**Exercice 11.6.4**

Écrivez la recherche dichotomique dans un tableau trié. Quelle précaution prendre pour calculer le milieu sans débordement ?

**Exercice 11.6.5**

Écrivez `supprimer_doublons(int *t, size_t n)` qui renvoie la nouvelle taille pour un tableau trié.

### Tri avec `qsort`

**Exercice 11.6.6**

Triez un tableau d'entiers par ordre croissant, puis décroissant avec `qsort`. Pourquoi `return a - b;` dans le comparateur est-il dangereux ? Écrivez la version correcte.

**Exercice 11.6.7**

Triez un tableau de chaînes (`const char *noms[]`) par ordre alphabétique avec `qsort` et `strcmp`. Que reçoit exactement le comparateur ?

**Exercice 11.6.8**

Après le tri, recherchez un élément avec `bsearch`.

## 11.7 Erreurs courantes

**Exercice 11.7.1**

Pour chaque extrait, indiquez l'erreur et sa conséquence, puis corrigez :

```c
int t[5];
for (int i = 0; i <= 5; i++) t[i] = i;

int a[3] = {1, 2, 3}, b[3] = {1, 2, 3};
if (a == b) puts("égaux");

void f(int t[10]) { printf("%zu\n", sizeof t / sizeof t[0]); }

int u[5];
printf("%d\n", u[2]);

int v[3] = {1, 2, 3, 4};
```

**Exercice 11.7.2**

Utilisez AddressSanitizer pour détecter un accès hors limites sur un tableau local, puis sur un tableau global. Notez les différences dans le rapport.

---

# 12. Chaînes de caractères

## 12.1 Définition

**Exercice 12.1.1**

Qu'est-ce qu'une chaîne en C ? Dessinez la représentation mémoire de `char s[] = "abc";` (indiquez le `'\0'`).

**Exercice 12.1.2**

Quelle est la différence entre `char s[] = "bonjour";` et `char *p = "bonjour";` ? Que se passe-t-il à `s[0] = 'B';` et à `p[0] = 'B';` ? Vérifiez avec `sizeof` et en essayant de modifier.

**Exercice 12.1.3**

Combien d'octets occupent `char a[] = "été";` (UTF-8), `char b[10] = "abc";` et `char c[3] = "abc";` ? Quel est le problème du dernier cas ?

**Exercice 12.1.4**

Déclarez une chaîne vide de trois façons différentes, et affichez `strlen` de chacune.

## 12.2 Fonctions de `<string.h>`

**Exercice 12.2.1**

Implémentez vous-même `mon_strlen`, `mon_strcpy`, `mon_strcmp` et `mon_strcat` sans utiliser la bibliothèque. Testez-les contre les versions standard.

**Exercice 12.2.2**

Complétez le tableau :

| Fonction | Rôle | Danger éventuel |
| --- | --- | --- |
| `strlen` | | |
| `strcpy` | | |
| `strncpy` | | |
| `strcat` | | |
| `strcmp` | | |
| `strchr` / `strrchr` | | |
| `strstr` | | |
| `strtok` | | |

**Exercice 12.2.3**

Écrivez un programme qui compare deux chaînes saisies et affiche si la première est avant, égale ou après la seconde dans l'ordre lexicographique.

**Exercice 12.2.4**

Utilisez `strchr`, `strrchr` et `strstr` pour extraire l'extension d'un nom de fichier (`"archive.tar.gz"`) et la position de la première occurrence d'un motif.

**Exercice 12.2.5**

Utilisez `strtok` pour découper `"a,b;c d"` selon les séparateurs `",; "`. Quel est le défaut de `strtok` (modification de la chaîne, état interne) ? Quelle variante (`strtok_r`) existe en POSIX ?

## 12.3 Copier et concaténer en sécurité

**Exercice 12.3.1**

Pourquoi `strcpy(dest, src)` est-il dangereux ? Écrivez une version sûre avec `snprintf`.

**Exercice 12.3.2**

Écrivez `copier_borne(char *dest, size_t taille, const char *src)` qui copie au plus `taille - 1` caractères et termine toujours par `'\0'`. Quel piège évite-t-elle par rapport à `strncpy` ?

**Exercice 12.3.3**

Écrivez `concatener_borne(char *dest, size_t taille, const char *src)` qui ajoute `src` à `dest` sans dépasser le tampon, et renvoie `false` si la chaîne a été tronquée.

**Exercice 12.3.4**

Construisez un chemin `"dossier/sous/fichier.txt"` à partir de trois morceaux avec `snprintf` dans un tampon de taille fixe, en testant la troncature.

## 12.4 Lire et parcourir

**Exercice 12.4.1**

Écrivez un programme qui lit une ligne et compte les voyelles, consonnes, chiffres, espaces et autres caractères.

**Exercice 12.4.2**

Écrivez `est_palindrome(const char *s)` en ignorant la casse et les espaces.

**Exercice 12.4.3**

Écrivez `inverser_chaine(char *s)` qui inverse une chaîne sur place.

**Exercice 12.4.4**

Écrivez un programme qui compte le nombre de mots d'une phrase (séparés par des espaces multiples).

**Exercice 12.4.5**

Écrivez `supprimer_espaces(char *s)` qui supprime tous les espaces d'une chaîne sur place.

**Exercice 12.4.6**

Écrivez `remplacer(char *s, char ancien, char nouveau)`.

## 12.5 `<ctype.h>` : tester et convertir les caractères

**Exercice 12.5.1**

Écrivez un programme qui convertit une chaîne en majuscules, puis en minuscules, puis inverse la casse de chaque lettre.

**Exercice 12.5.2**

Écrivez `capitaliser(char *s)` qui met en majuscule la première lettre de chaque mot.

**Exercice 12.5.3**

Pourquoi faut-il convertir en `unsigned char` avant d'appeler `isalpha` sur un `char` ? Que peut-il se passer avec des caractères accentués ?

**Exercice 12.5.4**

Écrivez un chiffrement de César : `void cesar(char *s, int decalage)` qui décale les lettres en conservant la casse et les autres caractères. Écrivez le déchiffrement.

**Exercice 12.5.5**

Écrivez `bool mot_de_passe_valide(const char *s)` : au moins 8 caractères, une majuscule, une minuscule, un chiffre et un signe de ponctuation (`ispunct`).

## 12.6 Conversions chaîne ⇄ nombre

**Exercice 12.6.1**

Pourquoi `atoi` est-il déconseillé ? Écrivez `bool vers_entier(const char *s, long *resultat)` avec `strtol`, `errno` et le pointeur de fin.

**Exercice 12.6.2**

Testez votre fonction avec : `"42"`, `"  42"`, `"42abc"`, `"abc"`, `""`, `"99999999999999999999"`, `"-17"`, `"0x1A"` (avec base 0). Notez le résultat attendu et le résultat obtenu.

**Exercice 12.6.3**

Écrivez `bool vers_double(const char *s, double *resultat)` avec `strtod`.

**Exercice 12.6.4**

Convertissez un entier en chaîne dans une base donnée (2 à 16) avec une fonction que vous écrivez, puis comparez avec `snprintf`.

## 12.7 Tableau de chaînes

**Exercice 12.7.1**

Déclarez un tableau de 5 noms (`const char *`), affichez-les avec leur longueur, puis triez-les par ordre alphabétique.

**Exercice 12.7.2**

Quelle est la différence entre `char *noms[] = {"a", "bb"};` et `char noms[2][10] = {"a", "bb"};` en mémoire et en possibilité de modification ? Vérifiez avec `sizeof`.

**Exercice 12.7.3**

Écrivez un programme qui affiche le jour de la semaine à partir d'un entier 1 à 7 à l'aide d'un tableau de chaînes.

## 12.8 Bonnes pratiques

**Exercice 12.8.1**

Relevez et corrigez les cinq erreurs de ce code :

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char nom[5];
    char *p = "hello";
    strcpy(nom, "Alexandre");
    p[0] = 'H';
    if (nom == "Alex") puts("ok");
    char *q;
    strcpy(q, nom);
    printf(nom);
    return 0;
}
```

**Exercice 12.8.2**

Listez cinq règles de sécurité pour manipuler des chaînes (taille du tampon, `'\0'`, valeur de retour de `snprintf`, etc.) et illustrez chacune par un exemple.

---

# 13. Pointeurs

## 13.1 Qu'est-ce qu'un pointeur ?

**Exercice 13.1.1**

Écrivez un programme qui déclare un entier `x`, un pointeur `p` vers `x`, puis affiche `x`, `&x`, `p`, `*p` et `&p`. Modifiez `x` à travers `p`.

**Exercice 13.1.2**

Dessinez la mémoire (adresses fictives) après chacune de ces lignes :

```c
int a = 10, b = 20;
int *p = &a;
int *q = &b;
*p = *q;
p = q;
*p = 30;
```

Donnez les valeurs finales de `a`, `b`, `*p`, `*q`.

**Exercice 13.1.3**

Écrivez un programme qui affiche `sizeof` d'un pointeur vers `char`, `int`, `double`, `void` et vers une structure. Que constatez-vous ?

**Exercice 13.1.4**

Quel spécificateur de `printf` affiche une adresse ? Pourquoi caster en `(void *)` ?

## 13.2 Pointeur nul

**Exercice 13.2.1**

Écrivez une fonction qui renvoie un pointeur vers le premier élément négatif d'un tableau, ou `NULL` s'il n'y en a pas, et testez le résultat de façon sûre.

**Exercice 13.2.2**

Que se passe-t-il quand on déréférence `NULL` ? Écrivez le programme et observez l'erreur (segmentation) puis identifiez la ligne avec `gdb` ou AddressSanitizer.

**Exercice 13.2.3**

En C23, remplacez `NULL` par `nullptr`. Quel est l'avantage de `nullptr` ? *(C23)*

**Exercice 13.2.4**

Quelle valeur donner à un pointeur après `free` ? Pourquoi ?

## 13.3 Arithmétique des pointeurs

**Exercice 13.3.1**

Soit `int t[5] = {10, 20, 30, 40, 50}; int *p = t;`. Que valent `*p`, `*(p + 2)`, `p[3]`, `*p++`, `*(p + 1)` après l'incrémentation, `p - t` ? Vérifiez.

**Exercice 13.3.2**

Parcourez un tableau de `double` avec un pointeur seulement (sans indice), en utilisant deux pointeurs (début et fin).

**Exercice 13.3.3**

De combien d'octets avance `p + 1` pour `char *`, `int *`, `double *` ? Écrivez un programme qui le vérifie avec `(char *)` et `ptrdiff_t`.

**Exercice 13.3.4**

Réécrivez `mon_strlen` en utilisant uniquement l'arithmétique des pointeurs (soustraction de deux pointeurs).

**Exercice 13.3.5**

Quelles opérations sont autorisées entre pointeurs (soustraction, comparaison) et lesquelles sont interdites (addition de deux pointeurs, multiplication) ? Que se passe-t-il pour une arithmétique qui sort du tableau ?

## 13.4 Tableaux ≠ pointeurs

**Exercice 13.4.1**

Pour `int t[10]; int *p = t;`, comparez `sizeof t`, `sizeof p`, `&t`, `&p`, `t + 1`, `&t + 1`. Que remarquez-vous ?

**Exercice 13.4.2**

Dans quels cas un nom de tableau « se dégrade-t-il » en pointeur ? Citez les exceptions (`sizeof`, `&`, initialisation d'une chaîne).

**Exercice 13.4.3**

Peut-on écrire `t = p;` ? `p = t;` ? `t++` ? Expliquez à partir de la notion de valeur modifiable (*lvalue*).

**Exercice 13.4.4**

Montrez que `t[i]` et `i[t]` sont équivalents, et expliquez pourquoi à partir de la définition de l'opérateur `[]`.

## 13.5 Pointeurs et fonctions

**Exercice 13.5.1**

Écrivez `void incrementer_tous(int *t, size_t n)` en notation pointeur, puis une version avec deux pointeurs (début, fin).

**Exercice 13.5.2**

Écrivez `int *chercher_max(int *t, size_t n)` qui renvoie un pointeur vers le plus grand élément. Modifiez ensuite cet élément à travers le pointeur renvoyé.

**Exercice 13.5.3**

Écrivez `void separer(const char *s, char *debut, char *fin)` qui sépare `"clé=valeur"` en deux chaînes.

## 13.6 `const` et pointeurs (rappel)

**Exercice 13.6.1**

Écrivez `const char *trouver(const char *s, char c)` et expliquez pourquoi le type de retour est `const`. Comment gérer le cas où l'appelant veut modifier la chaîne trouvée (`strchr` standard) ?

**Exercice 13.6.2**

Que se passe-t-il à la compilation avec :

```c
void f(char *s);
const char *p = "abc";
f(p);
```

## 13.7 `void *` : pointeur générique

**Exercice 13.7.1**

Écrivez une fonction `void echanger_generique(void *a, void *b, size_t taille)` utilisant `memcpy` (avec un tampon intermédiaire ou un bloc par octets). Testez-la sur des `int`, des `double` et des structures.

**Exercice 13.7.2**

Pourquoi ne peut-on pas déréférencer un `void *` ni faire de l'arithmétique dessus (en C standard) ? Comment convertir ?

**Exercice 13.7.3**

Implémentez `void *mon_memcpy(void *dest, const void *src, size_t n)` et `mon_memset`. Quel est le type de pointeur interne utile ?

## 13.8 Pointeur vers une structure

**Exercice 13.8.1**

Définissez `struct Point { double x, y; };`. Écrivez `void deplacer(struct Point *p, double dx, double dy)` en utilisant l'opérateur `->`. Quelle est la relation entre `p->x` et `(*p).x` ?

**Exercice 13.8.2**

Écrivez une fonction `double distance(const struct Point *a, const struct Point *b)`. Pourquoi passer par pointeur `const` ?

## 13.9 `restrict` *(ajout, C99)*

**Exercice 13.9.1**

Quelle promesse fait `restrict` au compilateur ? Écrivez une fonction `void ajouter(int *restrict a, const int *restrict b, size_t n)` et expliquez ce qui se passe si `a` et `b` se chevauchent.

**Exercice 13.9.2**

Pourquoi `memcpy` utilise-t-il implicitement cette contrainte alors que `memmove` non ? Quand choisir l'un ou l'autre ?

## 13.10 Erreurs classiques

**Exercice 13.10.1**

Identifiez l'erreur de chaque extrait (pointeur sauvage, nul, pendant, dépassement, mauvais type, alias strict) :

```c
int *p;
*p = 5;

int *q = NULL;
printf("%d\n", *q);

int *f(void) { int x = 3; return &x; }

int t[3];
int *r = t + 5;
*r = 1;

double d = 1.5;
int *s = (int *)&d;
printf("%d\n", *s);

int *a = malloc(sizeof *a);
free(a);
*a = 1;
```

**Exercice 13.10.2**

Compilez chaque extrait avec `-fsanitize=address,undefined` et classez les erreurs détectées à l'exécution, celles détectées à la compilation et celles non détectées.

---

# 14. Allocation dynamique de mémoire

## 14.1 Pourquoi ?

**Exercice 14.1.1**

Donnez trois situations où la taille d'une donnée n'est connue qu'à l'exécution. Pourquoi un tableau de taille fixe ne convient-il pas ?

**Exercice 14.1.2**

Comparez la mémoire de la pile et du tas (taille, durée de vie, vitesse, gestion) dans un tableau de synthèse.

## 14.2 Les fonctions de `<stdlib.h>`

**Exercice 14.2.1**

Écrivez un programme qui lit `n`, alloue un tableau de `n` entiers avec `malloc`, le remplit, calcule sa moyenne, puis le libère. Vérifiez le retour de `malloc`.

**Exercice 14.2.2**

Quelle forme préférer : `malloc(n * sizeof(int))` ou `malloc(n * sizeof *t)` ? Pourquoi ?

**Exercice 14.2.3**

Que fait `free(NULL)` ? Que fait `malloc(0)` ? Vérifiez les cas sur votre implémentation.

**Exercice 14.2.4**

Écrivez une fonction `char *dupliquer(const char *s)` équivalent à `strdup` (disponible en C23). Qui doit libérer le résultat ?

**Exercice 14.2.5**

Écrivez `void *allouer_ou_quitter(size_t taille)` qui encapsule `malloc` et termine le programme avec un message sur `stderr` en cas d'échec.

## 14.3 `calloc`

**Exercice 14.3.1**

Comparez `malloc(n * sizeof(int))` suivi d'un `memset` à zéro, et `calloc(n, sizeof(int))`. Quels avantages (initialisation, contrôle du débordement) ?

**Exercice 14.3.2**

Montrez que `malloc` ne vide pas la mémoire en lisant (avant écriture) un bloc fraîchement alloué (comportement non défini : à ne faire que comme expérience), puis que `calloc` renvoie des zéros.

## 14.4 `realloc` : la bonne façon

**Exercice 14.4.1**

Écrivez un programme qui lit des entiers jusqu'à `EOF` dans un tableau dynamique agrandi par `realloc` (capacité doublée à chaque saturation).

**Exercice 14.4.2**

Pourquoi `p = realloc(p, nouvelle_taille);` est-il dangereux ? Écrivez la forme correcte avec un pointeur temporaire.

**Exercice 14.4.3**

Que fait `realloc(NULL, n)` ? Que fait `realloc(p, 0)` ? Pourquoi ce second cas est-il à éviter ?

**Exercice 14.4.4**

Que se passe-t-il pour les pointeurs qui désignaient l'ancien bloc après un `realloc` réussi ? Écrivez un exemple qui provoque un pointeur pendant.

## 14.5 Erreurs classiques de gestion mémoire

**Exercice 14.5.1**

Écrivez un programme minimal pour chacune des erreurs du tableau du cours : fuite, double libération, utilisation après libération, dépassement du tampon du tas, libération d'un pointeur non alloué, débordement de taille, non-vérification de `NULL`. Compilez avec AddressSanitizer et copiez la première ligne du rapport de chacune.

**Exercice 14.5.2**

Corrigez les erreurs du code suivant :

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *saluer(const char *nom) {
    char *s = malloc(strlen(nom) + 6);
    strcpy(s, "Salut ");
    strcat(s, nom);
    return s;
}

int main(void) {
    char *m = saluer("Zoé");
    puts(m);
    free(m);
    free(m);
    int *t = malloc(5);
    t[4] = 1;
    return 0;
}
```

## 14.6 Règle de propriété

**Exercice 14.6.1**

Écrivez un module `Tableau` avec `creer_tableau(n)` et `detruire_tableau(t)`. Documentez qui possède la mémoire dans chaque cas.

**Exercice 14.6.2**

Pour chacune des fonctions suivantes de la bibliothèque standard, indiquez qui doit libérer la mémoire retournée : `strdup`, `fopen`, `getline`, `getenv`, `malloc`, `strerror`.

## 14.7 Outils de détection

**Exercice 14.7.1**

Compilez et exécutez le programme de l'exercice 14.5.2 avec AddressSanitizer, puis avec Valgrind (`--leak-check=full`). Comparez les rapports.

**Exercice 14.7.2**

Écrivez un petit programme qui fuit 1 Mo par itération et observez la progression de la mémoire utilisée avec un outil du système (`top`, `htop`, gestionnaire de tâches).

---

# 15. Retourner des tableaux et des chaînes

## 15.1 Le problème

**Exercice 15.1.1**

Expliquez pourquoi une fonction ne peut pas retourner un tableau local. Écrivez la fonction fautive `int *tableau_carres(int n)` et décrivez la sortie obtenue.

## 15.2 Les quatre solutions

### 1. L'appelant fournit le tampon (recommandé)

**Exercice 15.2.1**

Écrivez `size_t en_majuscules(char *dest, size_t taille, const char *src)` qui écrit le résultat dans le tampon fourni et renvoie le nombre de caractères écrits (ou nécessaires).

**Exercice 15.2.2**

Écrivez `bool remplir_carres(int *dest, size_t n)` : l'appelant fournit un tableau, la fonction le remplit.

### 2. Allocation dynamique

**Exercice 15.2.3**

Écrivez `char *repeter(const char *s, int n)` qui renvoie une nouvelle chaîne contenant `s` répétée `n` fois. Documentez la propriété de la mémoire et libérez correctement dans `main`.

**Exercice 15.2.4**

Écrivez `int *copie_inversee(const int *t, size_t n)` qui renvoie un nouveau tableau alloué. Quelle valeur renvoyer en cas d'échec ?

### 3. Variable `static` (à éviter)

**Exercice 15.2.5**

Écrivez une fonction qui renvoie l'adresse d'un tableau `static` et appelez-la deux fois en conservant les deux résultats. Quel problème apparaît ? Pourquoi est-ce un problème pour les fils d'exécution ?

### 4. Structure

**Exercice 15.2.6**

Écrivez une structure `struct Resultat { int valeurs[5]; size_t n; };` et une fonction qui la renvoie par valeur. Dans quels cas cette approche est-elle raisonnable ?

**Exercice 15.2.7**

Comparez les quatre solutions dans un tableau (propriété, sûreté, performance, limites de taille).

## 15.3 Ce qu'il ne faut jamais faire

**Exercice 15.3.1**

Corrigez chacune des fonctions suivantes de deux façons différentes :

```c
char *date(void) {
    char tampon[20];
    snprintf(tampon, sizeof tampon, "26/10/2026");
    return tampon;
}

int *plage(int n) {
    int t[n];
    for (int i = 0; i < n; i++) t[i] = i;
    return t;
}

char *concat(const char *a, const char *b) {
    char r[100];
    strcpy(r, a);
    strcat(r, b);
    return r;
}
```

---

# 16. Structures de données dynamiques

## 16.1 Liste simplement chaînée

**Exercice 16.1.1**

Définissez `struct Noeud { int valeur; struct Noeud *suivant; };`. Écrivez `ajouter_en_tete`, `ajouter_en_queue`, `afficher`, `longueur`, `liberer`.

**Exercice 16.1.2**

Écrivez `rechercher(Noeud *tete, int v)` qui renvoie un pointeur vers le premier nœud ayant la valeur `v`, et `supprimer(Noeud **tete, int v)`.

**Exercice 16.1.3**

Écrivez `inverser(Noeud *tete)` qui inverse la liste en place.

**Exercice 16.1.4**

Écrivez `insérer_trie(Noeud **tete, int v)` qui garde la liste triée par ordre croissant.

**Exercice 16.1.5**

Écrivez la fusion de deux listes triées en une liste triée, sans allouer de nœud.

**Exercice 16.1.6**

Écrivez `Noeud *milieu(Noeud *tete)` avec deux pointeurs (lent et rapide) puis `bool a_un_cycle(Noeud *tete)`.

**Exercice 16.1.7**

Quelle est la complexité (O(1), O(n)) de chaque opération : accès au `k`-ième élément, insertion en tête, insertion en queue (sans pointeur de queue), recherche, suppression d'un nœud donné ? Comparez avec un tableau.

## 16.2 Autres structures

**Exercice 16.2.1**

Implémentez une **pile** (LIFO) à l'aide d'une liste chaînée avec `empiler`, `depiler`, `sommet`, `est_vide`. Utilisez-la pour vérifier l'équilibre des parenthèses d'une chaîne.

**Exercice 16.2.2**

Implémentez une **file** (FIFO) avec pointeurs de tête et de queue, avec `enfiler`, `defiler`.

**Exercice 16.2.3**

Implémentez une **liste doublement chaînée** avec insertion et suppression d'un nœud donné en O(1).

**Exercice 16.2.4**

Implémentez un **arbre binaire de recherche** : insertion, recherche, parcours infixe, hauteur, libération complète.

**Exercice 16.2.5**

Implémentez une **table de hachage** à chaînage pour associer des mots à des entiers : fonction de hachage, insertion, recherche, suppression, libération.

**Exercice 16.2.6** *(défi)*

Implémentez un tas binaire (file de priorité) dans un tableau dynamique avec `inserer` et `extraire_min`.

## 16.3 Tableau dynamique extensible (vecteur)

**Exercice 16.3.1**

Implémentez `struct Vecteur { int *donnees; size_t taille; size_t capacite; };` avec `vecteur_init`, `vecteur_ajouter`, `vecteur_obtenir`, `vecteur_supprimer_dernier`, `vecteur_liberer`.

**Exercice 16.3.2**

Pourquoi doubler la capacité plutôt qu'ajouter une case à chaque fois ? Mesurez le nombre de `realloc` pour 10⁶ ajouts avec les deux stratégies.

**Exercice 16.3.3**

Généralisez le vecteur à des éléments de taille quelconque grâce à `void *` et `memcpy`.

## 16.4 Matrices dynamiques

### Méthode A : tableau de pointeurs (lignes indépendantes)

**Exercice 16.4.1**

Écrivez `int **creer_matrice(size_t l, size_t c)` avec un tableau de pointeurs, `void liberer_matrice(int **m, size_t l)` et `afficher_matrice`. Gérez correctement l'échec d'allocation d'une ligne au milieu de la création.

### Méthode B : bloc unique contigu (plus efficace)

**Exercice 16.4.2**

Écrivez la version avec un seul bloc `int *m = malloc(l * c * sizeof *m)` et l'accès `m[i * c + j]`. Comparez le nombre d'allocations et la localité mémoire avec la méthode A.

**Exercice 16.4.3**

Écrivez la version avec un pointeur vers tableau (`int (*m)[c] = malloc(l * sizeof *m);`) qui permet la notation `m[i][j]`. Quelle norme exige-t-elle ?

**Exercice 16.4.4**

Écrivez `multiplier(const int *a, const int *b, int *res, size_t n)` pour des matrices stockées en bloc contigu, puis mesurez le temps pour `n = 500` avec la boucle `i, j, k` et avec la boucle `i, k, j`. Expliquez la différence.

---

# 17. Pointeurs doubles

## 17.1 Définition

**Exercice 17.1.1**

Déclarez `int x = 5; int *p = &x; int **pp = &p;` et affichez `x`, `*p`, `**pp`, `&x`, `p`, `*pp`, `&p`, `pp`. Modifiez `x` à travers `pp`.

**Exercice 17.1.2**

Dessinez le schéma mémoire de la configuration précédente avec des flèches.

## 17.2 Usages principaux

### 1. Modifier un pointeur depuis une fonction

**Exercice 17.2.1**

Écrivez `bool allouer_tableau(int **t, size_t n)` qui alloue un tableau et affecte l'adresse au pointeur de l'appelant. Pourquoi une version `int *t` ne fonctionne-t-elle pas ?

**Exercice 17.2.2**

Écrivez `void liberer_et_annuler(void **p)` qui libère un bloc et met le pointeur de l'appelant à `NULL`.

### 2. Tableau de chaînes / matrices

**Exercice 17.2.3**

Écrivez `char **decouper(const char *s, char sep, size_t *n)` qui renvoie un tableau de chaînes allouées dynamiquement, et `void liberer_decoupage(char **t, size_t n)`.

**Exercice 17.2.4**

Écrivez un programme qui lit un nombre arbitraire de lignes sur `stdin` dans un tableau de chaînes allouées dynamiquement, les trie par ordre alphabétique et les affiche.

### 3. Listes chaînées (insertion / suppression élégante)

**Exercice 17.2.5**

Réécrivez `supprimer(Noeud **tete, int v)` sans traiter séparément le cas de la tête, avec un pointeur sur pointeur qui parcourt les liens. Expliquez le gain de simplicité.

**Exercice 17.2.6**

Écrivez de la même façon `inserer_trie(Noeud **tete, int v)`.

### 4. `argv` : `char **argv`

**Exercice 17.2.7**

Écrivez un programme qui affiche tous les éléments de `argv` en utilisant uniquement l'arithmétique de pointeurs sur `char **`.

## 17.3 Libération

**Exercice 17.3.1**

Écrivez la libération complète d'une structure à plusieurs niveaux : un tableau de `char *` lui-même alloué dynamiquement. Dans quel ordre libérer ? Que se passe-t-il si l'on libère d'abord le tableau principal ?

**Exercice 17.3.2**

Corrigez cette fonction qui fuit en cas d'échec au milieu de l'allocation :

```c
char **copier_tableau(const char *const *src, size_t n) {
    char **dst = malloc(n * sizeof *dst);
    for (size_t i = 0; i < n; i++)
        dst[i] = strdup(src[i]);
    return dst;
}
```

---

# 18. Structures et unions

## 18.1 Structures (`struct`)

**Exercice 18.1.1**

Définissez une structure `Etudiant` avec un nom, un âge et une moyenne. Déclarez-en trois, initialisez-les de trois façons différentes (liste, initialisation désignée, affectation membre par membre) et affichez-les.

**Exercice 18.1.2**

Écrivez les fonctions `afficher_etudiant(const struct Etudiant *e)` et `saisir_etudiant(struct Etudiant *e)` avec lecture sûre.

### Opérations

**Exercice 18.1.3**

Peut-on affecter une structure à une autre (`a = b;`) ? La comparer avec `==` ? Écrivez les deux essais et expliquez ce que fait `memcmp` et pourquoi il est risqué sur des structures avec remplissage.

**Exercice 18.1.4**

Que se passe-t-il quand une structure contient un tableau de chars (`char nom[20]`) et qu'on l'affecte à une autre ? Et avec un `char *nom` ? Montrez la différence entre copie superficielle et copie profonde.

**Exercice 18.1.5**

Écrivez `Etudiant copier_profond(const Etudiant *e)` pour une structure qui contient un `char *nom` alloué dynamiquement.

### Littéraux composés (C99)

**Exercice 18.1.6**

Utilisez un littéral composé `(struct Point){ .x = 1, .y = 2 }` pour appeler une fonction `distance_origine` sans variable temporaire nommée. Utilisez aussi un littéral composé pour un tableau `(int[]){1, 2, 3}`.

### Structures imbriquées et tableaux de structures

**Exercice 18.1.7**

Définissez `struct Date { int jour, mois, annee; };` et `struct Personne { char nom[30]; struct Date naissance; };`. Écrivez une fonction qui calcule l'âge à partir d'une date du jour.

**Exercice 18.1.8**

Créez un tableau de 5 étudiants, triez-le par moyenne décroissante avec `qsort`, puis affichez le major de la promotion et la moyenne de la classe.

### Structure auto-référencée

**Exercice 18.1.9**

Écrivez la définition d'un nœud d'arbre binaire `struct Arbre { int valeur; struct Arbre *gauche, *droite; };` puis une fonction qui compte ses nœuds. Pourquoi un nœud ne peut-il pas contenir une structure du même type, mais seulement un pointeur ?

## 18.2 Alignement et remplissage (*padding*)

**Exercice 18.2.1**

Affichez `sizeof` et `offsetof` de chaque membre pour :

```c
struct A { char c; int i; char d; };
struct B { int i; char c; char d; };
struct C { char c; double d; short s; };
```

Dessinez la disposition mémoire de chaque structure avec les octets de remplissage.

**Exercice 18.2.2**

Réordonnez les membres de `struct C` pour minimiser sa taille. Quelle règle générale en déduisez-vous ?

**Exercice 18.2.3**

À quoi servent `alignas`, `alignof` et l'attribut `packed` (extension GCC) ? Quels sont les risques de `packed` ?

**Exercice 18.2.4**

Pourquoi ne faut-il pas écrire une structure directement dans un fichier ou sur le réseau avec `fwrite` si l'on souhaite un format portable ?

## 18.3 Champs de bits

**Exercice 18.3.1**

Définissez une structure `Drapeaux` avec des champs de bits `lecture : 1`, `ecriture : 1`, `execution : 1`, `reserve : 5`. Affichez sa taille et manipulez chaque champ.

**Exercice 18.3.2**

Représentez une date compactée (jour sur 5 bits, mois sur 4 bits, année sur 7 bits à partir de 2000) dans une structure de bits. Quelle taille obtient-on ?

**Exercice 18.3.3**

Quelles sont les limites portables des champs de bits (ordre des bits, signedness, adresse non prenable) ? Quand préférer les masques de bits ?

## 18.4 Membre de tableau flexible (C99)

**Exercice 18.4.1**

Définissez `struct Chaine { size_t longueur; char donnees[]; };` et une fonction `struct Chaine *creer(const char *s)` qui alloue la structure et la chaîne en un seul bloc. Comment libérer ?

**Exercice 18.4.2**

Quelle est la valeur de `sizeof(struct Chaine)` ? Pourquoi n'inclut-elle pas le tableau flexible ?

**Exercice 18.4.3**

Quelles opérations sont interdites sur une structure avec membre de tableau flexible (copie par valeur, tableau de ces structures, imbrication) ?

## 18.5 Unions

**Exercice 18.5.1**

Définissez `union Valeur { int i; float f; char c[4]; };`. Affichez sa taille, affectez un `float` puis lisez l'entier. Que constatez-vous ?

**Exercice 18.5.2**

Utilisez une union pour examiner les octets d'un `uint32_t` et déterminer l'*endianness* de votre machine.

**Exercice 18.5.3**

Que dit la norme sur la lecture d'un membre d'union différent de celui qui a été écrit en dernier (réinterprétation en C, comportement non spécifié en C++) ? Quelle alternative sûre pour réinterpréter les octets (`memcpy`) ?

### Union étiquetée (*tagged union*) : usage sûr

**Exercice 18.5.4**

Écrivez un type `Valeur` qui peut contenir un entier, un réel ou une chaîne, avec une étiquette `enum`. Écrivez `afficher(const Valeur *v)` avec un `switch`. Écrivez des constructeurs `valeur_entier`, `valeur_reel`, `valeur_texte`.

**Exercice 18.5.5**

Écrivez une expression arithmétique sous forme d'arbre à l'aide d'une union étiquetée (nombre, addition, multiplication), puis `evaluer(const Expr *e)`.

## 18.6 Structure ou union ?

**Exercice 18.6.1**

Complétez le tableau suivant en comparant `struct` et `union` (mémoire, membres valides, usage) et donnez un exemple d'utilisation réaliste pour chacune.

**Exercice 18.6.2**

Pour chaque besoin, choisissez `struct`, `union` ou une union étiquetée : un point 2D, un message réseau de type variable, une valeur JSON, un enregistrement d'étudiant, un registre matériel accessible en entier ou par champs.

---

# 19. Énumérations (`enum`)

## 19.1 Définition

**Exercice 19.1.1**

Définissez une énumération `enum Couleur { ROUGE, VERT, BLEU };` et affichez les valeurs de chaque constante. Quel est le type de ces constantes en C ?

### Valeurs explicites

**Exercice 19.1.2**

Définissez `enum Code { OK = 0, ERREUR_FICHIER = 10, ERREUR_MEMOIRE, ERREUR_SAISIE = 20 };` et prédisez la valeur de `ERREUR_MEMOIRE` avant de vérifier.

**Exercice 19.1.3**

Définissez une énumération pour des droits d'accès avec des puissances de 2 (`LECTURE = 1`, `ECRITURE = 2`, `EXECUTION = 4`) et combinez-les avec `|`. Testez la présence d'un droit avec `&`.

### Type sous-jacent *(C23)*

**Exercice 19.1.4**

Définissez `enum Niveau : unsigned char { BAS, MOYEN, HAUT };` et affichez `sizeof(enum Niveau)`. Quel est l'avantage (taille, format de stockage) ? *(C23)*

## 19.2 Avec `typedef` et `switch`

**Exercice 19.2.1**

Définissez `typedef enum { LUNDI, MARDI, … , DIMANCHE } Jour;` et écrivez `bool est_weekend(Jour j)` avec un `switch`. Compilez avec `-Wall` : pourquoi l'oubli d'un cas déclenche-t-il un avertissement lorsque `default` est absent ?

**Exercice 19.2.2**

Écrivez `Jour jour_suivant(Jour j)` avec le modulo, puis `const char *nom_jour(Jour j)`.

**Exercice 19.2.3**

Écrivez une machine à états simple (feu tricolore) avec une énumération pour les états et un `switch` pour la transition.

**Exercice 19.2.4**

Définissez une énumération des opérations (`ADD`, `SUB`, `MUL`, `DIV`) et écrivez `double calculer(Operation op, double a, double b)` avec traitement d'une valeur invalide.

## 19.3 Particularités

**Exercice 19.3.1**

Prédisez et justifiez si le programme compile : deux énumérations différentes contenant la même constante `ROUGE` ; une variable `enum Couleur c = 42;` ; l'addition de deux constantes d'énumération.

**Exercice 19.3.2**

Ajoutez une constante `NB_COULEURS` en fin d'énumération et utilisez-la pour parcourir toutes les valeurs avec une boucle `for` et un tableau de noms indexé par initialisation désignée.

**Exercice 19.3.3**

Quelle différence entre `enum` et `#define` pour des constantes entières (débogage, portée, typage) ? Quand choisir chacun ?

---

# 20. `typedef`

## 20.1 Créer un alias de type

**Exercice 20.1.1**

Définissez les alias `octet` (pour `unsigned char`), `entier32` (pour `int32_t`) et `reel` (pour `double`). Utilisez-les dans une petite fonction. Quel avantage pour la portabilité ?

**Exercice 20.1.2**

Quelle est la différence entre `typedef struct Point { double x, y; } Point;` et `typedef struct { double x, y; } Point;` ? Quand l'étiquette du `struct` reste-t-elle nécessaire ?

## 20.2 Usages courants

**Exercice 20.2.1**

Écrivez un `typedef` pour un tableau de 3 entiers (`Vec3`), pour un pointeur vers une structure de nœud, et pour un pointeur de fonction `int (*)(int, int)`. Utilisez-les.

**Exercice 20.2.2**

Réécrivez la liste chaînée du chapitre 16 avec un `typedef` et une structure opaque : un en-tête qui n'expose que `typedef struct Liste Liste;` et un `.c` qui définit la structure.

**Exercice 20.2.3**

Écrivez un `typedef enum` pour un type `Resultat` (`OK`, `ERREUR`, …) et une fonction qui le renvoie. Quel avantage sur un simple `int` ?

## 20.3 `typedef` ou `#define` ?

**Exercice 20.3.1**

Que déclarent `typedef int *PInt; PInt a, b;` et `#define PInt int *` suivi de `PInt a, b;` ? Écrivez et vérifiez avec `sizeof` et le compilateur.

**Exercice 20.3.2**

Donnez trois différences entre `typedef` et `#define` (traitement, portée, types complexes).

## 20.4 Bonnes pratiques

**Exercice 20.4.1**

Pourquoi est-il déconseillé de masquer un pointeur derrière un `typedef` ? Écrivez un exemple où cela trompe le lecteur (par `const`).

**Exercice 20.4.2**

Pourquoi le suffixe `_t` est-il réservé par POSIX ? Proposez une convention de nommage sûre pour vos propres types.

---

# 21. Pointeurs de fonctions

## 21.1 Principe

**Exercice 21.1.1**

Déclarez un pointeur de fonction `int (*op)(int, int);`, affectez-lui `somme` puis `produit` et appelez-le. Quelle est la différence entre `int (*p)(int)` et `int *p(int)` ?

**Exercice 21.1.2**

Écrivez `int appliquer(int (*f)(int), int x)` et passez-lui `carre`, `double_`, `negation`.

**Exercice 21.1.3**

Écrivez `void appliquer_tableau(int *t, size_t n, int (*f)(int))` qui transforme chaque élément d'un tableau.

## 21.2 Avec `typedef`

**Exercice 21.2.1**

Simplifiez les déclarations suivantes avec `typedef` :

```c
int (*f)(int, int);
void (*gestionnaire(int, void (*)(int)))(int);
int (*table[3])(int, int);
```

**Exercice 21.2.2**

Écrivez un type `Predicat` (`bool (*)(int)`) et une fonction `filtrer(const int *t, size_t n, Predicat p, int *dest)` qui copie les éléments vérifiant `p`.

## 21.3 Callbacks : `qsort`

**Exercice 21.3.1**

Écrivez les comparateurs pour trier : des entiers croissants, des entiers par valeur absolue, des chaînes par longueur puis ordre alphabétique, des structures `Etudiant` par moyenne décroissante puis nom.

**Exercice 21.3.2**

Écrivez votre propre `mon_tri(void *base, size_t n, size_t taille, int (*cmp)(const void *, const void *))` (tri à bulles ou par insertion générique) en manipulant les octets avec `char *`.

**Exercice 21.3.3**

Écrivez `pour_chaque(const void *base, size_t n, size_t taille, void (*f)(const void *))` qui applique un callback sur chaque élément d'un tableau quelconque.

## 21.4 Table de fonctions

**Exercice 21.4.1**

Écrivez une calculatrice en ligne de commande où une table de structures `{ const char *nom; double (*f)(double, double); }` associe `"add"`, `"sub"`, `"mul"`, `"div"` aux fonctions. Remplacez le `switch` par une recherche dans la table.

**Exercice 21.4.2**

Écrivez un menu interactif piloté par un tableau de pointeurs de fonctions. Que se passe-t-il si l'utilisateur saisit un indice invalide ? Comment sécuriser ?

**Exercice 21.4.3**

Écrivez un petit interpréteur de commandes (`aide`, `liste`, `ajouter`, `quitter`) basé sur une table de commandes et de gestionnaires.

## 21.5 Simuler des méthodes (« objets » en C)

**Exercice 21.5.1**

Écrivez une structure `Forme` avec un pointeur de fonction `double (*aire)(const Forme *)` et un pointeur de fonction `void (*afficher)(const Forme *)`. Créez deux « sous-types » `Cercle` et `Rectangle` qui l'utilisent, et un tableau de formes hétérogènes.

**Exercice 21.5.2**

Ajoutez un destructeur `void (*detruire)(Forme *)` et une fonction `liberer_formes` qui libère chaque forme à travers son destructeur. Expliquez l'analogie avec les méthodes virtuelles.

## 21.6 Sélection générique : `_Generic` (C11)

**Exercice 21.6.1**

Écrivez une macro `abs_generique(x)` avec `_Generic` qui choisit entre `abs`, `labs`, `fabs` et `fabsf` selon le type.

**Exercice 21.6.2**

Écrivez une macro `afficher(x)` qui affiche un `int`, un `double`, une chaîne ou un `char` avec le bon format.

**Exercice 21.6.3**

Quelles sont les limites de `_Generic` (sélection à la compilation, pas de réflexion à l'exécution) ? Pourquoi ne remplace-t-il pas les templates du C++ ?

---

# Niveau avancé

---

# 22. Gestion des fichiers

## 22.1 Le type `FILE *` et les opérations

**Exercice 22.1.1**

Complétez le tableau des fonctions de gestion de fichiers :

| Opération | Fonction(s) | Remarque |
| --- | --- | --- |
| Ouvrir | | |
| Fermer | | |
| Écrire du texte | | |
| Lire du texte | | |
| Lire / écrire en binaire | | |
| Se positionner | | |
| Supprimer / renommer | | |

**Exercice 22.1.2**

Qu'est-ce qu'un flux tamponné ? Quelle est la différence entre `FILE *` et un descripteur de fichier POSIX ?

## 22.2 Ouvrir et fermer

**Exercice 22.2.1**

Écrivez un programme qui ouvre un fichier en lecture, vérifie l'échec avec `perror`, puis le ferme. Testez avec un fichier existant et un fichier absent.

**Exercice 22.2.2**

Décrivez chaque mode d'ouverture (`"r"`, `"w"`, `"a"`, `"r+"`, `"w+"`, `"a+"`, et leurs variantes binaires `"rb"`, `"wb"`) : création, troncature, positionnement initial, lecture/écriture autorisées.

**Exercice 22.2.3**

Pourquoi faut-il toujours tester la valeur renvoyée par `fopen` et par `fclose` ? Dans quel cas `fclose` peut-il échouer sur un fichier ouvert en écriture ?

**Exercice 22.2.4**

Que se passe-t-il si l'on oublie de fermer un fichier avant la fin du programme (données dans le tampon) ? Écrivez un test qui l'illustre avec `fflush`.

## 22.3 Écrire du texte

**Exercice 22.3.1**

Écrivez un programme qui crée un fichier `notes.txt` contenant 10 lignes `Ligne n : valeur` avec `fprintf`. Affichez ensuite le fichier avec une commande du système.

**Exercice 22.3.2**

Écrivez un programme qui ajoute (mode `"a"`) la date et un message à la fin d'un fichier de journal à chaque exécution, avec `time` et `strftime`.

**Exercice 22.3.3**

Écrivez un programme qui sauvegarde un tableau d'étudiants (nom, âge, moyenne) dans un fichier CSV (une ligne par étudiant, champs séparés par des points-virgules).

**Exercice 22.3.4**

Utilisez `fputs`, `fputc` et `fwrite` pour écrire la même chaîne. Comparez les résultats et expliquez les différences.

## 22.4 Lire du texte

### Ligne par ligne (recommandé)

**Exercice 22.4.1**

Écrivez un programme qui lit un fichier ligne par ligne avec `fgets` et affiche chaque ligne précédée de son numéro. Gérez les lignes plus longues que le tampon.

**Exercice 22.4.2**

Écrivez un programme qui compte les lignes, mots et caractères d'un fichier (comme `wc`).

**Exercice 22.4.3**

Écrivez `tail` : affichez les 5 dernières lignes d'un fichier avec un tampon circulaire.

**Exercice 22.4.4**

Écrivez un programme qui recherche un mot dans un fichier et affiche le numéro de chaque ligne qui le contient (comme `grep -n`).

### Caractère par caractère

**Exercice 22.4.5**

Écrivez un programme qui copie un fichier texte dans un autre avec `fgetc` et `fputc`, en convertissant les lettres en majuscules. Pourquoi `fgetc` renvoie-t-il un `int` ? Quel piège avec `while (!feof(f))` ?

**Exercice 22.4.6**

Écrivez un programme qui compte la fréquence de chaque lettre d'un fichier et affiche un histogramme.

### Formaté avec `fscanf`

**Exercice 22.4.7**

Écrivez un programme qui lit un fichier contenant des lignes `nom age moyenne` avec `fscanf` et stocke les données dans un tableau de structures. Vérifiez la valeur de retour de `fscanf`.

**Exercice 22.4.8**

Pourquoi `fgets` suivi de `sscanf` est-il plus robuste que `fscanf` seul ? Réécrivez l'exercice précédent avec cette méthode, en ignorant les lignes mal formées avec un message d'erreur indiquant le numéro de ligne.

**Exercice 22.4.9**

Lisez un fichier CSV simple et calculez la moyenne de chaque colonne numérique.

## 22.5 Fichiers binaires

**Exercice 22.5.1**

Écrivez un programme qui écrit un tableau de 100 entiers dans un fichier binaire avec `fwrite`, puis le relit avec `fread` et vérifie l'égalité.

**Exercice 22.5.2**

Écrivez un programme qui sauvegarde et recharge un tableau d'étudiants (structures) dans un fichier binaire. Quel problème de portabilité peut apparaître (remplissage, *endianness*, taille de `long`) ?

**Exercice 22.5.3**

Définissez un format binaire portable : un en-tête (numéro magique, version, nombre d'enregistrements) suivi des enregistrements en entiers à taille fixe et en ordre d'octets défini. Écrivez la lecture avec vérification de l'en-tête.

**Exercice 22.5.4**

Écrivez un programme qui copie un fichier binaire quelconque (une image par exemple) par blocs de 4096 octets avec `fread` / `fwrite`, puis compare les deux fichiers avec `cmp`.

### Texte ou binaire ?

**Exercice 22.5.5**

Complétez le tableau comparatif texte / binaire (lisibilité, portabilité, taille, vitesse, édition manuelle, conversion des fins de ligne).

**Exercice 22.5.6**

Sous Windows, quelle différence y a-t-il entre l'ouverture en mode `"r"` et en mode `"rb"` ? Quel effet sur `\n` ?

## 22.6 Se positionner dans un fichier

**Exercice 22.6.1**

Écrivez un programme qui utilise `fseek`, `ftell` et `rewind` pour déterminer la taille d'un fichier binaire, puis lire seulement ses 10 derniers octets.

**Exercice 22.6.2**

Écrivez un petit « fichier base de données » d'enregistrements de taille fixe et accédez directement au `k`-ième enregistrement avec `fseek`, puis modifiez-le en place.

**Exercice 22.6.3**

Quelles sont les trois origines possibles de `fseek` (`SEEK_SET`, `SEEK_CUR`, `SEEK_END`) ? Pourquoi `fseek` sur un fichier texte est-il à manier avec précaution ? Quelles fonctions (`fgetpos`, `fsetpos`) sont plus sûres ?

### Lire un fichier entier en mémoire

**Exercice 22.6.4**

Écrivez `char *lire_fichier(const char *chemin, size_t *taille)` qui lit tout le contenu dans un tampon alloué (avec un `'\0'` final) et gère toutes les erreurs (ouverture, taille, allocation, lecture). Qui libère la mémoire ?

**Exercice 22.6.5**

Utilisez cette fonction pour écrire un programme qui affiche un fichier à l'envers (caractère par caractère de la fin vers le début).

## 22.7 Opérations sur les fichiers

**Exercice 22.7.1**

Écrivez un programme qui crée un fichier temporaire, le renomme avec `rename`, puis le supprime avec `remove`. Vérifiez chaque valeur de retour.

**Exercice 22.7.2**

Écrivez un programme qui utilise `tmpfile` ou `mkstemp` pour manipuler un fichier temporaire. Quel est l'avantage de `mkstemp` sur `tmpnam` (course critique) ?

**Exercice 22.7.3**

Écrivez un programme qui teste si un fichier existe, d'abord avec `fopen`, puis avec `access` (POSIX). Quelle est la limite de chaque méthode ?

## 22.8 Bonnes pratiques

**Exercice 22.8.1**

Corrigez le code suivant (cinq problèmes) :

```c
#include <stdio.h>

int main(void) {
    FILE *f = fopen("donnees.txt", "r");
    char ligne[10];
    while (!feof(f)) {
        fgets(ligne, 100, f);
        puts(ligne);
    }
    return 0;
}
```

**Exercice 22.8.2**

Écrivez un programme qui écrit dans un fichier de manière atomique : écriture dans un fichier temporaire du même dossier, `fflush`, `fsync` (POSIX), puis `rename` pour remplacer l'ancien fichier.

**Exercice 22.8.3**

Écrivez le modèle d'un programme qui ouvre deux fichiers (entrée et sortie), traite les données et nettoie correctement en cas d'erreur à n'importe quelle étape avec `goto fin;`.

---

# 23. Arguments de la ligne de commande

## 23.1 `argc` et `argv`

**Exercice 23.1.1**

Écrivez un programme qui affiche `argc` et chaque élément de `argv` avec son indice. Lancez-le avec `./prog un "deux mots" 3`. Que contient `argv[0]` ? Que vaut `argv[argc]` ?

**Exercice 23.1.2**

Écrivez un programme qui affiche un message d'usage (`Usage : prog fichier`) et renvoie `EXIT_FAILURE` si le nombre d'arguments est incorrect.

**Exercice 23.1.3**

Écrivez `echo` (affiche ses arguments séparés par des espaces) puis `echo_inverse` (même chose dans l'ordre inverse).

## 23.2 Convertir en nombres (avec contrôle d'erreurs)

**Exercice 23.2.1**

Écrivez une fonction `bool argument_entier(const char *s, long min, long max, long *resultat)` avec `strtol`, `errno`, contrôle du pointeur de fin et de la plage.

**Exercice 23.2.2**

Écrivez un programme `puissance base exposant` qui lit deux arguments entiers, vérifie les erreurs et affiche le résultat. Quels cas d'erreur traiter ?

## 23.3 Exemple : somme d'entiers

**Exercice 23.3.1**

Écrivez un programme `somme` qui additionne tous ses arguments entiers. Que doit-il faire si l'un d'eux n'est pas un entier valide ? Faut-il signaler l'erreur et continuer, ou s'arrêter ?

**Exercice 23.3.2**

Étendez le programme : calculez aussi la moyenne, le minimum et le maximum. Que faire sans argument ?

**Exercice 23.3.3**

Écrivez un programme `cp_simple source destination` qui copie un fichier binaire, avec contrôles d'erreurs complets et codes de sortie distincts.

## 23.4 Options et drapeaux

**Exercice 23.4.1**

Écrivez un programme qui gère manuellement les options `-v` (verbeux), `-n valeur` (un nombre) et `--aide`, puis des arguments positionnels. Comment gérer l'option `--` qui termine les options ?

**Exercice 23.4.2**

Que fait `./prog -abc` si on gère les options combinées ? Écrivez la boucle d'analyse qui les accepte.

### `getopt` (POSIX, Linux/macOS)

**Exercice 23.4.3**

Réécrivez l'exercice 23.4.1 avec `getopt`. Expliquez le rôle de `optarg`, `optind`, `opterr` et de la chaîne de description `"vn:h"`.

**Exercice 23.4.4**

Écrivez un `wc` simplifié avec les options `-l`, `-w`, `-c` et une liste de fichiers (ou `stdin` si aucun fichier).

## 23.5 Variables d'environnement

**Exercice 23.5.1**

Affichez `HOME`, `PATH` et `USER` avec `getenv`. Que renvoie `getenv` pour une variable absente ? Quel contrôle faire avant de l'utiliser ?

**Exercice 23.5.2**

Écrivez un programme qui utilise la variable d'environnement `NIVEAU_LOG` (si elle existe) pour contrôler la verbosité de ses messages, avec une valeur par défaut. Comment la définir pour une seule exécution (`NIVEAU_LOG=2 ./prog`) ?

**Exercice 23.5.3**

Pourquoi ne faut-il pas modifier la chaîne renvoyée par `getenv` ? Quelles sont les différences entre `getenv`, `setenv`, `putenv` (POSIX) ?

## 23.6 Bonnes pratiques

**Exercice 23.6.1**

Listez cinq règles pour un programme en ligne de commande bien élevé (message d'usage, codes de sortie, erreurs sur `stderr`, aide, valeurs par défaut) et appliquez-les à l'un de vos programmes précédents.

**Exercice 23.6.2**

Écrivez un programme `calc` qui accepte en ligne de commande `calc 3 + 4`, `calc 6 x 7` (le `*` est interprété par le shell : expliquez pourquoi on utilise `x` ou un guillemet) et traite toutes les erreurs.

---

# 24. Directives du préprocesseur

## 24.1 Rôle

**Exercice 24.1.1**

Écrivez un petit programme avec `#define`, `#include` et un commentaire. Affichez son résultat après préprocesseur avec `gcc -E` et repérez les remplacements effectués.

**Exercice 24.1.2**

Le préprocesseur connaît-il les types, les variables, les fonctions du C ? Que manipule-t-il réellement ?

## 24.2 `#include`

**Exercice 24.2.1**

Créez un en-tête `monfichier.h` qui définit une macro et un prototype, et incluez-le depuis un `.c`. Quelle est la différence entre `<...>` et `"..."` ? Comment afficher la liste des dossiers de recherche d'en-têtes de votre compilateur (`gcc -v -E - < /dev/null`) ?

**Exercice 24.2.2**

Que se passe-t-il quand un en-tête est inclus deux fois sans garde ? Provoquez l'erreur avec une définition de `struct` dupliquée.

## 24.3 `#define` : macros

**Exercice 24.3.1**

Définissez des macros pour : `CARRE(x)`, `MAX(a, b)`, `MIN(a, b)`, `ABS(x)`, `EST_PAIR(n)`, `NB_ELEMENTS(t)`. Comparez avec les fonctions équivalentes (typage, évaluation multiple).

**Exercice 24.3.2**

Définissez des constantes de configuration `TAILLE_MAX`, `VERSION` (chaîne) et `DEBUG` (0 ou 1). Comment les surcharger à la compilation avec `-D` ?

### Pièges des macros

**Exercice 24.3.3**

Calculez à la main la valeur de chaque expression, sans et avec parenthèses dans la macro :

```c
#define CARRE_FAUX(x) x * x
#define CARRE(x) ((x) * (x))

int a = CARRE_FAUX(2 + 3);
int b = CARRE(2 + 3);
int i = 3;
int c = CARRE(i++);
```

Expliquez le problème de l'évaluation multiple.

**Exercice 24.3.4**

Pourquoi `#define MAX(a, b) a > b ? a : b` est-elle dangereuse dans `2 * MAX(x, y)` ? Écrivez la version correcte, puis une version sûre avec `typeof` et une expression d'instruction GCC ou `_Generic`. *(C23 pour `typeof`)*

### Macros multi-instructions : `do { … } while (0)`

**Exercice 24.3.5**

Écrivez la macro `ECHANGER(a, b)` de deux façons : sans et avec `do { … } while (0)`. Montrez le cas d'utilisation `if (c) ECHANGER(x, y); else …` qui casse la première version.

### Opérateurs `#` et `##`

**Exercice 24.3.6**

Écrivez une macro `AFFICHER(expr)` qui affiche le texte de l'expression et sa valeur (opérateur `#`) : `AFFICHER(3 * 4)` doit afficher `3 * 4 = 12`.

**Exercice 24.3.7**

Écrivez une macro `DEFINIR_MAX(type)` qui génère une fonction `max_type` pour plusieurs types (opérateur `##`). Utilisez-la pour `int` et `double`.

### Macros variadiques

**Exercice 24.3.8**

Écrivez une macro `LOG(format, ...)` qui préfixe chaque message de `[fichier:ligne]` avec `__FILE__`, `__LINE__` et `__VA_ARGS__`. Comment gérer le cas sans argument variable (`__VA_OPT__` en C23) ? *(C23)*

## 24.4 Compilation conditionnelle

**Exercice 24.4.1**

Écrivez un programme qui affiche un message différent selon qu'il est compilé sous Linux, macOS ou Windows (`__linux__`, `__APPLE__`, `_WIN32`).

**Exercice 24.4.2**

Écrivez un code qui utilise `#if`, `#elif`, `#else`, `#endif` pour afficher la norme C utilisée à la compilation (`__STDC_VERSION__`).

**Exercice 24.4.3**

Utilisez `#ifdef`, `#ifndef` et `defined(...)` pour rendre une fonctionnalité optionnelle activée par `-DFONCTION_X`. Quelle différence entre `#if X` et `#ifdef X` ?

**Exercice 24.4.4**

Utilisez `#if 0 … #endif` pour désactiver un bloc de code contenant des commentaires `/* */`. Pourquoi est-ce préférable à un commentaire ?

**Exercice 24.4.5**

Utilisez `#error` pour interrompre la compilation si la norme est inférieure à C11, et `#warning` (extension) pour signaler une fonctionnalité obsolète.

## 24.5 Gardes d'inclusion

**Exercice 24.5.1**

Écrivez un en-tête `point.h` avec une garde `#ifndef POINT_H … #define POINT_H … #endif`, puis deux autres en-têtes qui l'incluent, et un `main.c` qui inclut les deux. Montrez que la compilation passe grâce à la garde, et qu'elle échoue sans.

**Exercice 24.5.2**

Quelle est la différence entre une garde classique et `#pragma once` (portabilité, risques de doublons de fichiers) ?

**Exercice 24.5.3**

Comment nommer correctement la macro de garde pour éviter les collisions entre projets ? Donnez une convention.

## 24.6 `#embed` *(C23)*

**Exercice 24.6.1**

Utilisez `#embed "fichier.bin"` pour initialiser un tableau `unsigned char` avec le contenu d'un fichier, puis affichez sa taille. Comparez avec la lecture à l'exécution. *(C23)*

**Exercice 24.6.2**

Citez deux cas d'usage pertinents (icône, police, ressource) et un inconvénient (taille de l'exécutable). *(C23)*

## 24.7 Macros prédéfinies

**Exercice 24.7.1**

Écrivez un programme qui affiche `__FILE__`, `__LINE__`, `__DATE__`, `__TIME__`, `__STDC__`, `__STDC_VERSION__`, `__func__` et `__STDC_HOSTED__`.

**Exercice 24.7.2**

Écrivez une macro `ECHEC(msg)` qui affiche le message accompagné du fichier, de la ligne et de la fonction, puis quitte le programme.

## 24.8 Exemple : bascule de débogage

**Exercice 24.8.1**

Écrivez la macro `DEBUG_PRINT(...)` qui affiche des messages seulement quand `DEBUG` est défini. Comment la compiler sans trace (production) et avec trace ?

**Exercice 24.8.2**

Quelle forme garantit que la macro de débogage est toujours analysée par le compilateur (même désactivée) : `#define DEBUG_PRINT(...)` (vide) ou `do { if (DEBUG) fprintf(...); } while (0)` ? Quels sont les avantages de la seconde ?

## 24.9 `static_assert` : vérifications à la compilation

**Exercice 24.9.1**

Écrivez des `static_assert` qui vérifient : `sizeof(int) >= 4`, `sizeof(struct S) == 8`, `CHAR_BIT == 8`, la taille d'un tableau constant. Provoquez volontairement un échec et lisez le message.

**Exercice 24.9.2**

Écrivez un `static_assert` qui vérifie qu'une énumération a exactement autant de constantes qu'un tableau de noms. Quel est l'intérêt face à `assert` ?

---

# 25. Opérateurs bit à bit

## 25.1 Principe

**Exercice 25.1.1**

Calculez à la main puis vérifiez avec un programme, pour `a = 0b1100` (12) et `b = 0b1010` (10) : `a & b`, `a | b`, `a ^ b`, `~a` (sur 8 bits non signés), `a << 2`, `a >> 1`.

**Exercice 25.1.2**

Complétez la table de vérité de `&`, `|`, `^` et `~` pour chaque combinaison de bits.

**Exercice 25.1.3**

Quel est l'effet d'un décalage à gauche de `k` bits sur la valeur d'un entier non signé ? D'un décalage à droite ? Écrivez deux fonctions `multiplier_par_8` et `diviser_par_4` avec des décalages.

## 25.2 Manipuler des bits individuels

**Exercice 25.2.1**

Écrivez des fonctions `mettre_a_1(x, n)`, `mettre_a_0(x, n)`, `basculer(x, n)` et `lire_bit(x, n)` pour un entier non signé 32 bits.

**Exercice 25.2.2**

Écrivez `compter_bits(unsigned x)` de trois façons : par boucle, avec l'astuce `x &= x - 1`, et avec une table de 256 entrées.

**Exercice 25.2.3**

Écrivez `est_puissance_de_2(unsigned x)` en une expression avec `x & (x - 1)`.

**Exercice 25.2.4**

Écrivez `bit_le_plus_faible(unsigned x)` (isoler le bit à 1 le plus bas avec `x & -x`) et `plus_haut_bit(unsigned x)`.

**Exercice 25.2.5**

Écrivez `inverser_bits(uint8_t x)` qui renverse l'ordre des 8 bits, puis `rotation_gauche(uint32_t x, unsigned n)` en gérant le cas `n = 0`.

## 25.3 Drapeaux (*flags*) et masques

**Exercice 25.3.1**

Définissez des drapeaux de permissions (lecture, écriture, exécution) avec une énumération en puissances de 2. Écrivez `ajouter`, `retirer`, `a_le_droit` et un affichage sous la forme `rwx`.

**Exercice 25.3.2**

Écrivez un programme qui gère 8 interrupteurs d'un tableau de bord stockés dans un `uint8_t`, avec une interface d'allumage, d'extinction, de basculement et d'affichage.

**Exercice 25.3.3**

Écrivez des fonctions qui extraient et insèrent un champ de bits `[debut, debut + largeur)` dans un entier (par exemple les composantes R, G, B d'un pixel codé sur 24 bits).

**Exercice 25.3.4**

Représentez un ensemble de nombres de 0 à 63 dans un `uint64_t` (ensemble de bits) avec `ajouter`, `retirer`, `contient`, union, intersection, différence, cardinal.

## 25.4 Afficher en binaire

**Exercice 25.4.1**

Écrivez `void afficher_binaire(uint32_t x)` qui affiche les 32 bits, regroupés par octets.

**Exercice 25.4.2**

Écrivez la fonction qui convertit une chaîne `"101101"` en entier, et la fonction inverse qui construit une chaîne binaire dans un tampon fourni.

**Exercice 25.4.3**

Écrivez un programme qui affiche la représentation binaire d'un `float` (reinterpréter avec `memcpy`), puis identifie le signe, l'exposant et la mantisse selon IEEE 754.

## 25.5 Échange sans variable temporaire (curiosité)

**Exercice 25.5.1**

Écrivez la version XOR de l'échange de deux entiers. Que se passe-t-il quand `a` et `b` désignent le même objet (échange d'une variable avec elle-même par pointeurs) ?

**Exercice 25.5.2**

Pourquoi cet échange n'est-il généralement pas plus rapide qu'un échange classique avec une variable temporaire ? Pourquoi ne faut-il pas l'utiliser en production ?

## 25.6 Fonctions de `<stdbit.h>` *(C23)*

**Exercice 25.6.1**

Utilisez `stdc_count_ones`, `stdc_leading_zeros`, `stdc_trailing_zeros`, `stdc_bit_width` et `stdc_has_single_bit` sur plusieurs valeurs de votre choix. Comparez les résultats avec vos implémentations de la section 25.2. *(C23)*

**Exercice 25.6.2**

Réécrivez `est_puissance_de_2` et le calcul de `floor(log2(x))` avec ces fonctions. *(C23)*

## 25.7 Précautions

**Exercice 25.7.1**

Indiquez le problème de chaque expression et corrigez-la :

```c
if (x & 1 == 0) { ... }
int y = 1 << 31;
int z = x >> -1;
int w = -8 >> 1;
unsigned v = ~0u << 32;
uint8_t a = 0xF0;
uint8_t b = ~a;
if (b == ~a) { ... }
```

**Exercice 25.7.2**

Écrivez un programme qui détecte l'*endianness* de la machine et fonctions `vers_big_endian(uint32_t)` / `depuis_big_endian(uint32_t)` qui fonctionnent sur les deux types de machines, sans dépendre de l'ordre natif.

---

# 26. Récursivité

## 26.1 Principe

**Exercice 26.1.1**

Identifiez le cas de base et le cas récursif de chacune des fonctions suivantes, puis dites si elles se terminent :

```c
int f(int n) { return n == 0 ? 0 : n + f(n - 1); }
int g(int n) { return g(n - 1) + 1; }
int h(int n) { return n <= 1 ? 1 : h(n / 2) + 1; }
int k(int a, int b) { return b == 0 ? a : k(b, a % b); }
```

**Exercice 26.1.2**

Écrivez de manière récursive : `factorielle`, `somme_chiffres`, `puissance`, `pgcd`, `longueur_chaine`, `est_palindrome`.

## 26.2 Fonctionnement : la pile d'appels

**Exercice 26.2.1**

Dessinez la pile d'appels de `factorielle(4)` à chaque étape (empilement et dépilement). Notez les valeurs des paramètres et des retours.

**Exercice 26.2.2**

Écrivez une fonction récursive qui affiche `Entrée n` avant l'appel récursif et `Sortie n` après. Prévoyez la sortie pour `n = 3`.

**Exercice 26.2.3**

Mesurez la profondeur de récursion maximale avant plantage sur votre machine (compteur global et récursion infinie). Quelle est la taille d'un cadre de pile par appel ?

## 26.3 Exemples

**Exercice 26.3.1**

Écrivez Fibonacci récursif naïf, comptez le nombre d'appels pour `n = 30`, puis écrivez une version mémoïsée (tableau) et une version itérative. Comparez les temps.

**Exercice 26.3.2**

Écrivez la résolution des tours de Hanoï qui affiche chaque déplacement. Combien de déplacements pour `n` disques ?

**Exercice 26.3.3**

Écrivez la recherche dichotomique récursive dans un tableau trié.

**Exercice 26.3.4**

Écrivez la génération de toutes les permutations d'un tableau (retour sur trace récursif) et de tous les sous-ensembles.

**Exercice 26.3.5**

Écrivez un tri fusion récursif et un tri rapide récursif sur un tableau d'entiers.

**Exercice 26.3.6**

Écrivez `void afficher_binaire_rec(unsigned n)` qui affiche un entier en binaire récursivement, sans tampon.

**Exercice 26.3.7**

Écrivez un parcours récursif d'un arbre binaire (préfixe, infixe, suffixe), le calcul de la hauteur et la libération de l'arbre.

**Exercice 26.3.8**

Écrivez la fonction d'Ackermann `A(m, n)` et testez-la pour de petites valeurs. Que se passe-t-il pour `A(4, 1)` ? *(défi)*

**Exercice 26.3.9**

Écrivez un programme qui parcourt récursivement un répertoire (`opendir`, `readdir`, POSIX) et affiche son arborescence avec une indentation. *(défi)*

## 26.4 Récursivité terminale

**Exercice 26.4.1**

Qu'est-ce qu'un appel terminal ? Parmi `fact(n)` classique et une version avec accumulateur `fact_acc(n, acc)`, laquelle est terminale ? Écrivez les deux.

**Exercice 26.4.2**

Transformez en version terminale puis en boucle : la somme des entiers de 1 à `n`, le PGCD, Fibonacci avec deux accumulateurs.

**Exercice 26.4.3**

Compilez la version terminale avec `-O0` puis `-O2` et lisez le code assembleur (`gcc -S`) pour voir si le compilateur a éliminé l'appel terminal. Le standard C le garantit-il ?

## 26.5 Récursivité ou itération ?

**Exercice 26.5.1**

Réécrivez de façon itérative avec une pile explicite un parcours d'arbre en profondeur. Comparez les deux versions (lisibilité, consommation de pile, risque de dépassement).

**Exercice 26.5.2**

Pour chacun des problèmes suivants, indiquez si la récursivité est naturelle ou si une boucle suffit : factorielle, parcours d'arbre, somme d'un tableau, Hanoï, recherche dans une liste chaînée, tri fusion, calcul de la puissance rapide.

## 26.6 Pièges

**Exercice 26.6.1**

Corrigez les pièges suivants (cas de base manquant, progression absente, double recalcul, tableau local volumineux à chaque appel) :

```c
int somme(int n) { return n + somme(n - 1); }
int boucle(int n) { if (n == 0) return 0; return boucle(n); }
long fib(int n) { return n < 2 ? n : fib(n - 1) + fib(n - 2); }
void traiter(int n) { char tampon[1000000]; if (n > 0) traiter(n - 1); }
```

---

# 27. Unicode et caractères larges

## 27.1 Le problème

**Exercice 27.1.1**

Écrivez un programme qui affiche `strlen` et les octets (en hexadécimal) de `"A"`, `"é"`, `"€"` et `"𝄞"`. Combien d'octets chaque caractère occupe-t-il en UTF-8 ?

**Exercice 27.1.2**

Pourquoi `strlen("éé")` ne donne-t-il pas 2 ? Pourquoi inverser une chaîne UTF-8 octet par octet produit-elle un résultat invalide ?

## 27.2 Les approches

**Exercice 27.2.1**

Écrivez `size_t longueur_utf8(const char *s)` qui compte les caractères (points de code) en ignorant les octets de continuation `10xxxxxx`.

**Exercice 27.2.2**

Écrivez une fonction qui décode un point de code UTF-8 depuis une chaîne, puis une fonction qui encode un point de code (`uint32_t`) en UTF-8 dans un tampon. Testez-les sur `"é"`, `"€"` et `"𝄞"`.

**Exercice 27.2.3**

Utilisez `setlocale`, `wchar_t`, `wprintf` et `wcslen` pour afficher et mesurer `L"Bonjour é"`. Pourquoi ne faut-il pas mélanger `printf` et `wprintf` sur le même flux ?

**Exercice 27.2.4**

Comparez `wchar_t`, `char16_t`, `char32_t` et `char8_t` : taille, encodage, portabilité. Écrivez un programme qui affiche `sizeof` de chacun. *(C23 pour `char8_t`)*

**Exercice 27.2.5**

Écrivez la conversion d'une chaîne `char *` en UTF-8 vers `char32_t[]` avec `mbrtoc32` (de `<uchar.h>`) ou avec votre fonction d'exercice 27.2.2.

## 27.3 Conseils pratiques

**Exercice 27.3.1**

Écrivez une fonction `tronquer_utf8(char *s, size_t max_octets)` qui coupe une chaîne sans jamais couper au milieu d'un caractère multi-octets.

**Exercice 27.3.2**

Pourquoi `toupper` ne fonctionne-t-il pas sur `'é'` en UTF-8 ? Quelle bibliothèque (ICU, utf8proc, libunistring) utiliser pour une vraie conversion de casse ou pour la normalisation ?

**Exercice 27.3.3**

Listez cinq règles pour manipuler des textes Unicode en C (encodage des sources, console Windows, longueur vs octets, comparaison, bibliothèque dédiée) et illustrez-en deux par un exemple.

---

# 28. Compilation et exécution

## 28.1 Les étapes détaillées

**Exercice 28.1.1**

Pour un fichier `prog.c`, écrivez les quatre commandes qui exécutent séparément le préprocesseur, le compilateur, l'assembleur et l'éditeur de liens. Quels fichiers obtenez-vous ?

**Exercice 28.1.2**

Utilisez `nm`, `objdump -d` et `ldd` (ou équivalents) pour examiner les symboles, le code et les bibliothèques d'un exécutable. Notez ce que chaque outil révèle.

## 28.2 Options essentielles de `gcc` / `clang`

**Exercice 28.2.1**

Écrivez les commandes qui répondent à chaque besoin : nommer l'exécutable, choisir C17, activer les avertissements, les traiter comme des erreurs, ajouter les informations de débogage, optimiser, ajouter un dossier d'en-têtes, lier `libm`, définir une macro, activer les sanitizers.

**Exercice 28.2.2**

Compilez un programme qui contient `sqrt(2.0)` sans et avec `-lm`. Que se passe-t-il ? Pourquoi parfois la compilation passe-t-elle sans `-lm` (optimisation, constante) ?

**Exercice 28.2.3**

Écrivez un programme qui produit au moins quatre avertissements différents avec `-Wall -Wextra` (variable inutilisée, comparaison signée / non signée, retour manquant, format erroné). Corrigez-les un à un.

## 28.3 Erreurs de compilation et d'édition de liens

**Exercice 28.3.1**

Provoquez volontairement chacune de ces erreurs et notez le message exact : point-virgule manquant, fonction implicite, variable non déclarée, format `printf` incorrect, référence indéfinie, définition multiple.

**Exercice 28.3.2**

Distinguez erreur de compilation et erreur d'édition de liens. Pour `undefined reference to 'f'`, listez trois causes possibles.

## 28.4 Projets multi-fichiers

**Exercice 28.4.1**

Créez un projet de trois fichiers `.c` (`main.c`, `liste.c`, `outils.c`) et deux en-têtes. Compilez-le en une commande, puis en compilant chaque fichier séparément (`-c`) et en liant ensuite.

**Exercice 28.4.2**

Modifiez un seul fichier source et ne recompilez que ce fichier avant de relier. Quel est l'intérêt pour les grands projets ?

## 28.5 Automatiser avec `make`

**Exercice 28.5.1**

Écrivez un `Makefile` avec les cibles `all`, `clean`, des variables `CC`, `CFLAGS`, `LDFLAGS`, et une règle générique `%.o: %.c`.

**Exercice 28.5.2**

Ajoutez au `Makefile` la gestion automatique des dépendances aux en-têtes (`-MMD -MP`) et une cible `debug` qui compile avec les sanitizers.

**Exercice 28.5.3**

Ajoutez une cible `test` qui exécute un jeu de tests, et une cible `install` qui copie l'exécutable. Quel est l'effet de `.PHONY` ?

## 28.6 Bibliothèques

**Exercice 28.6.1**

Créez une bibliothèque statique `libutil.a` à partir de deux fichiers, puis liez-la à un programme. Que contient `libutil.a` (`ar t`) ?

**Exercice 28.6.2**

Créez une bibliothèque dynamique `libutil.so` (`-fPIC -shared`), liez-y un programme et exécutez-le avec `LD_LIBRARY_PATH`. Que se passe-t-il sans cette variable ?

**Exercice 28.6.3**

Comparez bibliothèque statique et dynamique (taille de l'exécutable, mise à jour, déploiement, mémoire partagée).

## 28.7 Débogage

### `gdb`

**Exercice 28.7.1**

Compilez un programme qui plante (déréférencement de `NULL`) avec `-g`. Lancez `gdb`, exécutez, utilisez `backtrace` et `print` pour trouver la ligne fautive et la valeur de la variable.

**Exercice 28.7.2**

Utilisez `break`, `run`, `next`, `step`, `print`, `watch`, `continue` pour suivre une boucle qui calcule une somme. Observez à quel moment une variable prend une valeur inattendue.

**Exercice 28.7.3**

Placez un point d'arrêt conditionnel (`break ligne if i == 50`) et affichez un tableau avec `print tab[0]@10`.

### Détecteurs d'erreurs

**Exercice 28.7.4**

Écrivez un programme avec trois bugs (dépassement de tampon du tas, utilisation après libération, débordement d'entier signé). Détectez chacun avec AddressSanitizer ou UBSan, puis avec Valgrind.

**Exercice 28.7.5**

Complétez le tableau des outils (AddressSanitizer, UBSan, Valgrind, `-fanalyzer`, `clang-tidy`, `cppcheck`) : ce qu'ils détectent, à quel moment (compilation, exécution), coût en performance.

## 28.8 Optimisation

**Exercice 28.8.1**

Écrivez un programme de calcul intensif (somme d'une boucle sur 10⁹ itérations ou tri d'un grand tableau). Mesurez le temps avec `-O0`, `-O1`, `-O2`, `-O3`, `-Os`. Que constatez-vous ?

**Exercice 28.8.2**

Compilez un petit programme avec `-O0` et `-O2` en produisant l'assembleur (`-S`) et comparez les instructions de la boucle.

**Exercice 28.8.3**

Écrivez un programme avec un comportement indéfini (débordement signé dans une condition) dont le résultat diffère selon le niveau d'optimisation.

**Exercice 28.8.4**

Quelles sont les limites de `-march=native` (portabilité) et de `-flto` (temps de compilation) ?

## 28.9 Compilation croisée

**Exercice 28.9.1**

Compilez un programme pour une autre architecture (ARM par exemple) avec une chaîne d'outils croisée. Comment vérifier le type d'exécutable produit (`file`) ? Comment l'exécuter (émulateur `qemu-user`) ?

**Exercice 28.9.2**

Citez trois différences à prendre en compte en compilation croisée (taille de `long`, *endianness*, bibliothèque C).

## 28.10 Environnement d'exécution

**Exercice 28.10.1**

Décrivez, dans l'ordre, ce qui se passe entre l'appel du programme dans un terminal et le début de `main`, puis entre le `return` de `main` et le retour au terminal.

**Exercice 28.10.2**

Écrivez un programme qui enregistre deux fonctions avec `atexit`. Dans quel ordre sont-elles exécutées ? Que se passe-t-il avec `exit`, `return` depuis `main`, `_Exit` et `abort` ?

### Appels système ou fonctions de bibliothèque ?

**Exercice 28.10.3**

Écrivez le même programme « Hello » avec `printf`, puis avec `write(1, …)` (POSIX). Utilisez `strace` (Linux) pour observer les appels système réellement émis par chacun.

**Exercice 28.10.4**

Pourquoi `printf` en boucle est-il plus rapide que `write` appelé caractère par caractère ? Quel rôle joue le tampon de la bibliothèque ?

---

# 29. Comportements indéfinis et sécurité

## 29.1 Comportement indéfini (UB)

**Exercice 29.1.1**

Pour chaque extrait, indiquez la catégorie d'UB (mémoire, arithmétique, pointeurs, appels, séquencement, chaînes) :

```c
int t[3]; t[3] = 0;
int x = INT_MAX; x++;
int *p = malloc(4); free(p); *p = 1;
printf("%s", 42);
int i = 1; i = i++ + i++;
char *s = "abc"; s[0] = 'X';
int d = 5 % 0;
int u; printf("%d", u);
```

**Exercice 29.1.2**

Écrivez un programme dont l'UB produit des résultats différents avec `-O0` et `-O2`. Expliquez comment le compilateur a pu « supposer que l'UB n'arrive jamais ».

**Exercice 29.1.3**

Écrivez un test qui vérifie `x + 1 > x` pour un entier signé. Le compilateur peut-il le remplacer par `true` ? Quelle est la bonne façon de tester un débordement ?

**Exercice 29.1.4**

Quelle différence y a-t-il entre comportement indéfini, comportement non spécifié et comportement défini par l'implémentation ? Donnez un exemple de chaque.

## 29.2 Les failles de sécurité typiques

**Exercice 29.2.1**

Complétez le tableau : pour chaque faille (dépassement de tampon, chaîne de format, dépassement d'entier avant allocation, use-after-free / double free, lecture de mémoire non initialisée), écrivez un court programme vulnérable, expliquez comment l'exploiter, puis la parade.

**Exercice 29.2.2**

Corrigez ce code vulnérable (au moins quatre problèmes) :

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void traiter(char *entree) {
    char tampon[16];
    strcpy(tampon, entree);
    printf(tampon);
}

int main(int argc, char **argv) {
    int n = atoi(argv[1]);
    int *t = malloc(n * sizeof(int));
    for (int i = 0; i <= n; i++) t[i] = i;
    traiter(argv[2]);
    return 0;
}
```

**Exercice 29.2.3**

Écrivez une fonction `bool multiplication_sure(size_t a, size_t b, size_t *r)` qui détecte le débordement avant une allocation, sans `ckd_mul`, puis une version avec `ckd_mul`. *(C23 pour la seconde)*

**Exercice 29.2.4**

Écrivez un programme qui montre la différence entre `memset` et un effacement sécurisé d'un secret (`explicit_bzero` / `memset_s`) : pourquoi un compilateur peut-il supprimer un `memset` avant `free` ?

## 29.3 Hygiène de programmation

**Exercice 29.3.1**

Prenez un de vos programmes des chapitres précédents et appliquez la liste d'hygiène du cours : avertissements, sanitizers, validation des entrées, taille avec chaque pointeur, initialisation, mise à `NULL` après `free`, `const` et `size_t`, réduction des globales. Notez chaque défaut corrigé.

**Exercice 29.3.2**

Écrivez un petit jeu de tests avec `assert` pour des fonctions de chaînes que vous avez écrites (`mon_strlen`, `copier_borne`, `vers_entier`). Que fait `-DNDEBUG` ? Pourquoi `assert` ne remplace-t-il pas la validation d'entrées utilisateur ?

**Exercice 29.3.3**

Écrivez un test de robustesse (fuzzing simple) : un programme qui envoie des chaînes aléatoires à votre fonction `vers_entier` ou à votre analyseur de ligne de commande pendant 10 000 itérations, compilé avec les sanitizers.

**Exercice 29.3.4**

Rédigez cinq règles CERT C ou MISRA C que vous jugez essentielles (parmi celles que vous trouverez dans leur documentation) et un exemple de code non conforme pour chacune.

---

# 30. Bibliothèque standard et aide-mémoire

## 30.1 En-têtes principaux

**Exercice 30.1.1**

Associez chaque fonction ou type à son en-tête : `printf`, `qsort`, `strlen`, `isalpha`, `sqrt`, `uint32_t`, `size_t`, `INT_MAX`, `errno`, `time`, `assert`, `va_start`, `signal`, `ckd_add`, `stdc_count_ones`, `bool`.

**Exercice 30.1.2**

Pour chaque en-tête suivant, écrivez un mini-programme qui utilise deux de ses fonctions : `<math.h>`, `<time.h>`, `<ctype.h>`, `<errno.h>`, `<stdarg.h>`.

**Exercice 30.1.3**

Écrivez un programme qui mesure le temps d'exécution d'une fonction avec `clock()` (temps processeur) et avec `time()` / `difftime`. Quelles sont les différences de résolution et de signification ?

**Exercice 30.1.4**

Écrivez un programme qui affiche la date et l'heure locales formatées avec `strftime`, puis la même date en UTC avec `gmtime`.

**Exercice 30.1.5**

Écrivez un programme qui installe un gestionnaire de signal pour `SIGINT` (Ctrl-C) qui positionne un drapeau `volatile sig_atomic_t`, et termine proprement la boucle principale. Pourquoi faut-il limiter ce que l'on fait dans un gestionnaire de signal ?

**Exercice 30.1.6**

Utilisez `setjmp` / `longjmp` pour implémenter une sortie d'une boucle profondément imbriquée sur erreur. Quels sont les dangers (variables non `volatile`, ressources non libérées) ?

**Exercice 30.1.7**

Écrivez un programme qui crée deux threads avec `<threads.h>` ou `pthread` pour incrémenter un compteur partagé 10⁶ fois chacun, d'abord sans protection (observez le résultat), puis avec un mutex ou une variable `_Atomic`.

### Nombres aléatoires

**Exercice 30.1.8**

Écrivez un programme qui simule 600 lancers de dé avec `rand()` et affiche la fréquence de chaque face. Que se passe-t-il si l'on appelle `srand(time(NULL))` dans la boucle ?

**Exercice 30.1.9**

Pourquoi `rand() % n` introduit-il un léger biais ? Écrivez une version sans biais avec rejet. Pourquoi `rand()` ne convient-il pas à la cryptographie, et que faut-il utiliser à la place (`getrandom`, `/dev/urandom`, `arc4random`) ?

**Exercice 30.1.10**

Écrivez un mélange de Fisher-Yates pour mélanger un tableau, et un tirage de `k` éléments distincts parmi `n`.

## 30.2 Récapitulatif par thème

**Exercice 30.2.1**

Pour chaque besoin, écrivez l'outil ou le motif recommandé, puis un court exemple de code : tableau de taille variable, chaîne sûre, lecture d'un nombre, entier portable, modification d'un argument, retour d'une valeur d'erreur plus un résultat, callback, variante (type somme), constante, tri, nettoyage en cas d'erreur.

**Exercice 30.2.2**

Concevez un petit programme complet (gestionnaire de contacts) qui met en oeuvre au moins huit lignes du tableau récapitulatif : structure, liste ou tableau dynamique, lecture sûre, tri avec `qsort`, fichiers, arguments de ligne de commande, nettoyage avec `goto`, modules `.h` / `.c`.

## 30.3 Les 12 règles d'or du C

**Exercice 30.3.1**

Pour chacune des 12 règles d'or, écrivez un court exemple de code qui la viole et le même code corrigé.

**Exercice 30.3.2**

Relisez le programme de l'exercice 30.2.2 avec la liste de ces 12 règles et cochez celles que vous avez respectées. Corrigez les violations.

## 30.4 Ressources pour progresser

**Exercice 30.4.1**

Consultez la page de `qsort`, de `strtol` et de `snprintf` sur cppreference. Pour chacune, notez deux précisions qui ne figurent pas dans le cours (comportements indéfinis, valeurs de retour, versions de norme).

**Exercice 30.4.2**

Avec Compiler Explorer (godbolt.org), comparez le code assembleur produit pour une fonction `somme(const int *t, size_t n)` avec `-O0`, `-O2` et `-O3`. Repérez la vectorisation éventuelle.

**Exercice 30.4.3**

Choisissez un chapitre de *Modern C* ou du *K&R*, résolvez deux de ses exercices et comparez votre style avec celui du cours.

**Exercice 30.4.4** *(défi)*

Projet de synthèse : écrivez un petit interpréteur de commandes (mini-shell) qui lit une ligne, la découpe en arguments, exécute des commandes internes (`cd`, `exit`) et lance des programmes externes avec `fork` / `execvp` / `waitpid` (POSIX). Compilez avec les sanitizers, traitez toutes les erreurs et documentez la propriété de chaque bloc de mémoire.

---

<div align="center">

*Bon courage, et que vos pointeurs soient toujours valides !*

</div>
