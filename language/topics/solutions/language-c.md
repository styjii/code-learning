# ✅ Corrigés : exercices et projets en langage C

> Corrigés du document `language-c_1.md` : **13 séries d'exercices** puis **17 projets**. Tous les programmes ont été **compilés avec `gcc -std=c17 -Wall -Wextra -Wpedantic` sans aucun avertissement**, **exécutés** et, pour les parties mémoire et threads, **vérifiés avec les sanitizers** (`-fsanitize=address,undefined` et `-fsanitize=thread`).
>
> 💡 Essayez d'abord seul. Un programme C qui « marche » peut contenir un comportement indéfini : compilez toujours avec les avertissements et les sanitizers.

## 📑 Sommaire

[Compilation](#compilation) · [Partie 1 : séries 1 à 13](#partie-1--séries-dexercices) · [Partie 2 : projets 1 à 5](#partie-2--mini-programmes) · [Partie 3 : projets 6 à 8](#partie-3--structures-de-données-et-fichiers) · [Partie 4 : projets 9 à 12](#partie-4--threads) · [Partie 5 : projets 13 à 17](#partie-5--graphes)

## Compilation

```bash
gcc -std=c17 -Wall -Wextra -Wpedantic -g fichier.c -o programme    # programmes simples
gcc -std=c17 -Wall -Wextra -Wpedantic -g -pthread fichier.c -o p   # programmes à threads
gcc ... -fsanitize=address,undefined fichier.c -o programme        # mémoire et comportements indéfinis
gcc ... -fsanitize=thread -pthread fichier.c -o programme          # courses de données
```

---

# Partie 1 : séries d'exercices

## Série 1 : premiers pas

```c
// fichier: serie01.c
#include <stdio.h>

int main(void) {
    printf("Je m'appelle Alice et j'ai 30 ans.\n");    // 1. nom et âge
    printf("\nLe C est puissant !\n");                  // 2. sur une nouvelle ligne
    printf("Bonjour,\nmonde !\n");                      // 4. deux lignes avec \n
    return 0;
}
```

3. **Compiler et exécuter** (terminal) : `gcc serie01.c -o serie01` puis `./serie01` (sous Windows : `serie01.exe`).

## Série 2 : structure d'un programme

```c
// fichier: serie02.c
#include <assert.h>
#include <stdio.h>

#define PI 3.14159265358979
#define CARRE(x) ((x) * (x)) /* les parenthèses protègent contre CARRE(1 + 2) */

int compteur_global = 0; // variable globale

/* Fonction définie par l'utilisateur */
int carre(int x) {
    return x * x;
}

void incrementer(void) {
    compteur_global++;
}

int main(void) {
    double rayon = 2.0;
    printf("Aire du cercle de rayon %.1f : %.2f\n", rayon, PI * CARRE(rayon)); // 12.57

    incrementer();
    incrementer();
    printf("compteur_global = %d, carre(7) = %d\n", compteur_global, carre(7));

    assert(CARRE(1 + 2) == 9); // sans les parenthèses de la macro : 1 + 2 * 1 + 2 = 5 !
    return 0;
}
```

## Série 3 : identifiants, mots-clés et syntaxe

```c
// fichier: serie03.c
#include <stdio.h>

// 4. Version corrigée du code de l'énoncé (4 erreurs : { manquante, deux ; manquants, } manquante)
int corrige(void) {
    int x = 10;
    printf("X is %d\n", x);
    return 0;
}

int main(void) {
    // 1. Variables de trois types
    int entier = 7;
    float flottant = 2.5f;
    char lettre = 'C';
    printf("%d %.1f %c\n", entier, flottant, lettre);

    // 3. Au moins 5 mots-clés : int, for, if, return, while, const, static, void, char…
    static int appels = 0; // static
    const int LIMITE = 3;  // const
    for (int i = 0; i < LIMITE; i++) { // for
        if (i % 2 == 0) { // if
            appels++;
        }
    }
    int k = 0;
    while (k < 2) { // while
        k++;
    }
    printf("appels = %d, k = %d\n", appels, k);

    return corrige(); // return
}
```

> Rappel (2) : `3value` (commence par un chiffre) et `float` (mot-clé) sont invalides ; `__init__` est accepté par le compilateur mais **réservé** (double soulignement) ; `main` et `total_sum` sont valides.

## Série 4 : types de données

```c
// fichier: serie04.c
#include <limits.h>
#include <stdint.h>
#include <stdio.h>

#define G 9.81 // accélération de la pesanteur (m/s²)

int main(void) {
    // 1. Les types de base
    int entier = 42;
    float flottant = 3.14f;
    char lettre = 'A';
    double precis = 2.718281828;
    printf("%d %.2f %c %.9f\n", entier, flottant, lettre, precis);

    // 2. Poids = masse × g
    double masse = 70.0;
    printf("Poids : %.1f N\n", masse * G); // 686.7

    // 3. Rectangle
    double largeur = 4.0, hauteur = 2.5;
    printf("Aire : %.1f, périmètre : %.1f\n", largeur * hauteur, 2 * (largeur + hauteur)); // 10.0 et 13.0

    // 4. Tailles et limites (%zu pour sizeof)
    printf("short : %zu o, int : %zu o, long : %zu o, long long : %zu o\n",
           sizeof(short), sizeof(int), sizeof(long), sizeof(long long));
    printf("INT_MAX = %d, UINT_MAX = %u, SHRT_MAX = %d\n", INT_MAX, UINT_MAX, SHRT_MAX);

    // 5. Largeurs fixes et débordement
    uint8_t octet = 255;
    octet++; // non signé : le débordement est DÉFINI par le standard (modulo 256)
    printf("uint8_t 255 + 1 = %u\n", (unsigned)octet); // 0

    int a = INT_MAX;
    // a + 1 sur un entier SIGNÉ est un comportement INDÉFINI : on teste avant d'additionner
    if (a > INT_MAX - 1) {
        printf("a + 1 déborderait : on ne le calcule pas\n");
    }
    int64_t grand = (int64_t)a + 1; // la solution : un type plus large
    printf("(int64_t)INT_MAX + 1 = %lld\n", (long long)grand);
    return 0;
}
```

## Série 5 : constantes

```c
// fichier: serie05.c
#include <stdio.h>

#define VITESSE_LUMIERE_DEF 299792458L          // macro : simple substitution de texte
static const long VITESSE_LUMIERE_CONST = 299792458L; // vraie variable en lecture seule

enum Jour { LUNDI = 1, MARDI, MERCREDI, JEUDI, VENDREDI, SAMEDI, DIMANCHE }; // 5. constantes enum

int main(void) {
    // 1. Comparaison : const a un type, une portée et une adresse ; #define n'a ni l'un ni l'autre
    const long *adresse = &VITESSE_LUMIERE_CONST; // OK ; &VITESSE_LUMIERE_DEF serait une erreur
    printf("%ld %ld (adresse valide : %s)\n", VITESSE_LUMIERE_DEF, VITESSE_LUMIERE_CONST,
           adresse != NULL ? "oui" : "non");

    // 2. Séquences d'échappement
    printf("Tabulation :\tfin\nGuillemets : \"x\"\nAntislash : \\\n");

    // 3. Constantes caractère et chaîne
    const char LETTRE = 'Z';
    const char *const MESSAGE = "Bonjour";
    printf("%c %s\n", LETTRE, MESSAGE);

    // 4. Fahrenheit → Celsius : 5.0 / 9.0 (et NON 5 / 9, qui vaut 0)
    double fahrenheit = 98.6;
    printf("%.1f °F = %.1f °C\n", fahrenheit, (fahrenheit - 32.0) * 5.0 / 9.0); // 37.0
    printf("5 / 9 = %d, mais 5.0 / 9.0 = %.4f\n", 5 / 9, 5.0 / 9.0);

    // 5. enum
    printf("MERCREDI = %d, DIMANCHE = %d\n", MERCREDI, DIMANCHE);
    return 0;
}
```

## Série 6 : opérateurs

```c
// fichier: serie06.c
#include <assert.h>
#include <stdio.h>

int main(void) {
    // 1. Moyenne de trois nombres
    double a = 10, b = 20, c = 30;
    printf("Moyenne : %.2f\n", (a + b + c) / 3);

    // 2. Opérateurs relationnels et logiques
    int age = 20, est_citoyen = 1;
    printf("Peut voter : %s\n", (age >= 18 && est_citoyen) ? "oui" : "non");

    // 3. a++ (valeur AVANT l'incrément) contre ++a (valeur APRÈS)
    int x = 5, y = x++; // y = 5, x = 6
    int z = 5, t = ++z; // t = 6, z = 6
    printf("x = %d, y = %d | z = %d, t = %d\n", x, y, z, t);

    // 4. Opérateur ternaire
    int p = 8, q = 3;
    printf("Plus petit : %d\n", p < q ? p : q);

    // 5. Trois pièges classiques
    assert(7 / 2 == 3);   // division ENTIÈRE entre deux int
    assert(-7 % 3 == -1); // le reste prend le signe du dividende (depuis C99)
    int v = 0;
    if (v == 0) {         // `if (v = 0)` serait une affectation, pas une comparaison !
        printf("v == 0 est vrai\n");
    }
    return 0;
}
```

## Série 7 : entrées et sorties

```c
// fichier: serie07.c
// @stdin: Alice Martin\n30\n6 7\nB\nBonjour tout le monde
#include <stdio.h>
#include <string.h>

// Lit une ligne sans '\n' ; renvoie 0 en cas de fin d'entrée
static int lire_ligne(char *tampon, size_t taille) {
    if (fgets(tampon, (int)taille, stdin) == NULL) {
        return 0;
    }
    tampon[strcspn(tampon, "\n")] = '\0';
    return 1;
}

int main(void) {
    char nom[50], ligne[64], phrase[100];
    int age, a, b;
    char note;

    // 1. Nom et âge
    printf("Nom : ");
    if (!lire_ligne(nom, sizeof nom)) return 1;
    printf("Âge : ");
    if (!lire_ligne(ligne, sizeof ligne) || sscanf(ligne, "%d", &age) != 1) return 1;
    printf("\nBonjour %s, vous avez %d ans.\n", nom, age);

    // 2. Somme et produit
    printf("Deux entiers : ");
    if (!lire_ligne(ligne, sizeof ligne) || sscanf(ligne, "%d %d", &a, &b) != 2) return 1;
    printf("Somme = %d, produit = %d\n", a + b, a * b);

    // 3. Note sous forme de lettre (l'espace avant %c ignore les blancs)
    printf("Note (A à F) : ");
    if (!lire_ligne(ligne, sizeof ligne) || sscanf(ligne, " %c", &note) != 1) return 1;
    switch (note) {
        case 'A': printf("Excellent\n"); break;
        case 'B': printf("Très bien\n"); break;
        case 'C': printf("Bien\n"); break;
        default:  printf("À améliorer\n");
    }

    // 4. Une phrase avec fgets() puis puts() (puts ajoute le saut de ligne)
    printf("Une phrase : ");
    if (!lire_ligne(phrase, sizeof phrase)) return 1;
    puts(phrase);
    return 0;
}
```

## Série 8 : structures de contrôle

```c
// fichier: serie08.c
#include <stdio.h>

static const char *signe(int n) {
    if (n > 0) return "positif";
    else if (n < 0) return "négatif";
    return "nul";
}

static const char *jour(int n) {
    switch (n) {
        case 1: return "lundi";
        case 2: return "mardi";
        case 3: return "mercredi";
        case 4: return "jeudi";
        case 5: return "vendredi";
        case 6: return "samedi";
        case 7: return "dimanche";
        default: return "jour invalide";
    }
}

int main(void) {
    printf("%s %s %s\n", signe(5), signe(-2), signe(0));   // positif négatif nul
    printf("%s %s\n", jour(3), jour(9));                   // mercredi jour invalide

    // 3. Les 10 premiers entiers avec les trois boucles
    for (int i = 1; i <= 10; i++) printf("%d ", i);
    printf("\n");
    int j = 1;
    while (j <= 10) { printf("%d ", j); j++; }
    printf("\n");
    int k = 1;
    do { printf("%d ", k); k++; } while (k <= 10);
    printf("\n");

    // 4. Somme des chiffres avec while
    int n = 1234, somme = 0;
    while (n > 0) {
        somme += n % 10;
        n /= 10;
    }
    printf("Somme des chiffres de 1234 : %d\n", somme); // 10

    // 5. continue : n'afficher que les impairs
    for (int i = 1; i <= 10; i++) {
        if (i % 2 == 0) continue;
        printf("%d ", i);
    }
    printf("\n");
    return 0;
}
```

## Série 9 : fonctions

```c
// fichier: serie09.c
#include <assert.h>
#include <stdio.h>
#include <string.h>

static int somme_chiffres(int n) {
    n = n < 0 ? -n : n;
    int somme = 0;
    while (n > 0) {
        somme += n % 10;
        n /= 10;
    }
    return somme;
}

// `d <= n / d` plutôt que `d * d <= n` : évite le débordement d'entier pour les grands n
static int est_premier(int n) {
    if (n < 2) return 0;
    for (int d = 2; d <= n / d; d++) {
        if (n % d == 0) return 0;
    }
    return 1;
}

static long fibonacci(int n) {
    return n < 2 ? n : fibonacci(n - 1) + fibonacci(n - 2); // récursif : lent pour n > 40
}

// Inverse la chaîne SUR PLACE (le tableau doit être modifiable : pas un littéral "...")
static void inverser(char *s) {
    size_t n = strlen(s);
    if (n < 2) return;
    for (size_t i = 0, j = n - 1; i < j; i++, j--) {
        char tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;
    }
}

// Passage d'adresses : c'est ainsi qu'on SIMULE le passage par référence
static void echanger(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

static void essai_par_valeur(int x) {
    x = 99; // ne modifie que la copie locale
    printf("Dans la fonction : x = %d\n", x);
}

int main(void) {
    assert(somme_chiffres(1234) == 10);
    assert(est_premier(2) && est_premier(97) && !est_premier(1) && !est_premier(91));
    assert(est_premier(2147483647)); // 2^31 − 1 est premier : pas de débordement grâce à `n / d`
    assert(fibonacci(10) == 55);

    char mot[] = "bonjour";
    inverser(mot);
    assert(strcmp(mot, "ruojnob") == 0);

    int a = 1, b = 2;
    echanger(&a, &b);
    assert(a == 2 && b == 1);

    int v = 5;
    essai_par_valeur(v);
    assert(v == 5); // inchangée : le C passe tout par valeur

    printf("Tous les tests de la série 9 passent.\n");
    return 0;
}
```

## Série 10 : pointeurs et tableaux

```c
// fichier: serie10.c
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

// 1. Parcours avec l'arithmétique des pointeurs
static void afficher(const int *debut, size_t n) {
    for (const int *p = debut; p < debut + n; p++) {
        printf("%d ", *p); // *(p + i) équivaut à p[i]
    }
    printf("\n");
}

// 2. Un « tableau » en paramètre est en réalité un pointeur : sizeof donne la taille d'un pointeur
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wsizeof-array-argument" // on veut justement montrer le piège
static size_t taille_vue_par_la_fonction(int tab[10]) {
    return sizeof(tab);
}
#pragma GCC diagnostic pop

// 3. ❌ int *mauvais(void) { int x = 42; return &x; }  → pointeur PENDANT (x n'existe plus)
//    ✅ Correction 1 : l'appelant fournit la mémoire
static void ecrire_valeur(int *sortie) {
    *sortie = 42;
}
//    ✅ Correction 2 : allocation dynamique (l'appelant doit appeler free)
static int *creer_valeur(void) {
    int *p = malloc(sizeof *p);
    if (p != NULL) *p = 42;
    return p;
}

// 4. Somme de deux matrices 3×3
static void additionner(int a[3][3], int b[3][3], int r[3][3]) {
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            r[i][j] = a[i][j] + b[i][j];
}

int main(void) {
    int tab[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    afficher(tab, 5);

    assert(sizeof(tab) == 10 * sizeof(int));                 // dans main : 40 octets
    assert(taille_vue_par_la_fonction(tab) == sizeof(int *)); // dans la fonction : 8 octets (pointeur)

    int x = 0;
    ecrire_valeur(&x);
    int *y = creer_valeur();
    assert(y != NULL && x == 42 && *y == 42);
    free(y);

    int a[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int b[3][3] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};
    int r[3][3];
    additionner(a, b, r);
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) assert(r[i][j] == 10);
    }
    printf("Série 10 : OK\n");
    return 0;
}
```

## Série 11 : chaînes de caractères

```c
// fichier: serie11.c
#include <assert.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// 1. Réécriture de strlen, strcmp, strcpy
static size_t mon_strlen(const char *s) {
    const char *p = s;
    while (*p != '\0') p++;
    return (size_t)(p - s);
}

static int mon_strcmp(const char *a, const char *b) {
    while (*a != '\0' && *a == *b) { a++; b++; }
    return (unsigned char)*a - (unsigned char)*b;
}

static char *mon_strcpy(char *dest, const char *src) {
    char *debut = dest;
    while ((*dest++ = *src++) != '\0') { }
    return debut;
}

// 2. Concaténation SANS dépassement : snprintf tronque et ajoute toujours le '\0'
static int concatener(char *dest, size_t taille, const char *a, const char *b) {
    int n = snprintf(dest, taille, "%s%s", a, b);
    return n >= 0 && (size_t)n < taille; // faux si le résultat a été tronqué
}

// 3. Compter mots et voyelles
static int compter_mots(const char *s) {
    int mots = 0, dans_un_mot = 0;
    for (; *s != '\0'; s++) {
        if (isspace((unsigned char)*s)) {
            dans_un_mot = 0;
        } else if (!dans_un_mot) {
            dans_un_mot = 1;
            mots++;
        }
    }
    return mots;
}

static int compter_voyelles(const char *s) {
    int n = 0;
    for (; *s != '\0'; s++) {
        if (strchr("aeiouAEIOU", *s) != NULL) n++; // (la boucle s'arrête avant le '\0')
    }
    return n;
}

// 4. Palindrome (lettres et chiffres uniquement, sans tenir compte de la casse)
static int est_palindrome(const char *s) {
    size_t i = 0, j = strlen(s);
    while (i < j) {
        if (!isalnum((unsigned char)s[i])) { i++; continue; }
        if (j > 0 && !isalnum((unsigned char)s[j - 1])) { j--; continue; }
        if (tolower((unsigned char)s[i]) != tolower((unsigned char)s[j - 1])) return 0;
        i++;
        j--;
    }
    return 1;
}

int main(void) {
    assert(mon_strlen("bonjour") == strlen("bonjour") && mon_strlen("") == 0);
    assert(mon_strcmp("abc", "abc") == 0 && mon_strcmp("abc", "abd") < 0 && mon_strcmp("b", "a") > 0);

    char copie[20];
    mon_strcpy(copie, "copie");
    assert(strcmp(copie, "copie") == 0);

    char petit[8];
    assert(concatener(petit, sizeof petit, "abc", "def") == 1 && strcmp(petit, "abcdef") == 0);
    assert(concatener(petit, sizeof petit, "abcd", "efgh") == 0); // tronqué : détecté

    assert(compter_mots("  Le C est puissant  ") == 4);
    assert(compter_voyelles("Programmation") == 5);

    assert(est_palindrome("radar") && est_palindrome("A man, a plan, a canal: Panama"));
    assert(!est_palindrome("hello"));

    printf("Série 11 : OK\n");
    return 0;
}
```

> ⚠️ `strncpy` ne garantit **pas** le `'\0'` final. Préférez `snprintf` (comme ci-dessus), qui tronque proprement et termine toujours la chaîne.

## Série 12 : projet en plusieurs fichiers et Makefile

`outils.h` (avec **gardes d'inclusion**) :

```c
// fichier: serie12/outils.h
#ifndef OUTILS_H
#define OUTILS_H

int additionner(int a, int b);
int maximum(int a, int b);

#endif /* OUTILS_H */
```

`outils.c` :

```c
// fichier: serie12/outils.c
#include "outils.h"

int additionner(int a, int b) {
    return a + b;
}

int maximum(int a, int b) {
    return a > b ? a : b;
}
```

`main.c` :

```c
// fichier: serie12/main.c
#include <stdio.h>
#include "outils.h"

int main(void) {
    printf("3 + 4 = %d, max(3, 4) = %d\n", additionner(3, 4), maximum(3, 4));
    return 0;
}
```

`Makefile` (les lignes de commande commencent par une **tabulation**, pas par des espaces) :

```makefile
CC     = gcc
CFLAGS = -std=c17 -Wall -Wextra -Wpedantic -g

all: programme

programme: main.o outils.o
	$(CC) $(CFLAGS) main.o outils.o -o programme

%.o: %.c outils.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f *.o programme

.PHONY: all clean
```

Compilation manuelle équivalente : `gcc -c outils.c`, `gcc -c main.c`, puis `gcc outils.o main.o -o programme` (édition des liens). Sans les gardes d'inclusion, un fichier qui inclut deux en-têtes qui incluent tous deux `outils.h` provoquerait une erreur de redéfinition.

## Série 13 : tri et recherche

```c
// fichier: serie13.c
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

// 1. Tri à bulles : on échange les voisins mal ordonnés, jusqu'à ce qu'il n'y en ait plus
static void tri_bulles(int *t, size_t n) {
    int echange;
    do {
        echange = 0;
        for (size_t i = 1; i < n; i++) {
            if (t[i - 1] > t[i]) {
                int tmp = t[i - 1];
                t[i - 1] = t[i];
                t[i] = tmp;
                echange = 1;
            }
        }
    } while (echange);
}

// 2. Fonction de comparaison pour qsort : `(x > y) - (x < y)` plutôt que `x - y`,
//    qui peut déborder (par exemple INT_MIN - 1)
static int comparer(const void *a, const void *b) {
    int x = *(const int *)a, y = *(const int *)b;
    return (x > y) - (x < y);
}

int main(void) {
    int t1[] = {5, 2, 9, 1, 5, 6};
    int t2[] = {5, 2, 9, 1, 5, 6};
    int attendu[] = {1, 2, 5, 5, 6, 9};
    size_t n = sizeof t1 / sizeof t1[0];

    tri_bulles(t1, n);
    qsort(t2, n, sizeof t2[0], comparer);
    for (size_t i = 0; i < n; i++) {
        assert(t1[i] == attendu[i] && t2[i] == attendu[i]);
    }

    // 3. bsearch : le tableau DOIT être trié ; renvoie un pointeur sur l'élément, ou NULL
    int cle = 6;
    int *trouve = bsearch(&cle, t2, n, sizeof t2[0], comparer);
    assert(trouve != NULL && trouve - t2 == 4);
    printf("6 trouvé à l'indice %td\n", trouve - t2);

    cle = 7;
    assert(bsearch(&cle, t2, n, sizeof t2[0], comparer) == NULL);
    return 0;
}
```

---

# Partie 2 : mini-programmes

## Projet 1 : moyenne de trois nombres

```c
// fichier: projet01.c
// @stdin: 10 20.5 30
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    float a, b, c;

    printf("Entrez trois nombres : ");
    if (scanf("%f %f %f", &a, &b, &c) != 3) { // on vérifie TOUJOURS le retour de scanf
        fprintf(stderr, "Saisie invalide.\n");
        return EXIT_FAILURE;
    }
    printf("La moyenne est : %.2f\n", (a + b + c) / 3);
    return EXIT_SUCCESS;
}
```

```text
Entrez trois nombres : 10 20.5 30
La moyenne est : 20.17
```

## Projet 2 : le plus grand de N nombres

```c
// fichier: projet02.c
// @stdin: 4\n12\n7\n29\n21
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    printf("Combien de nombres allez-vous saisir ? ");
    if (scanf("%d", &n) != 1 || n < 1) {
        fprintf(stderr, "Nombre invalide.\n");
        return EXIT_FAILURE;
    }

    int maximum = 0;
    for (int i = 1; i <= n; i++) {
        int x;
        printf("Nombre %d : ", i);
        if (scanf("%d", &x) != 1) {
            fprintf(stderr, "Saisie invalide.\n");
            return EXIT_FAILURE;
        }
        if (i == 1 || x > maximum) { // le maximum démarre au PREMIER nombre lu, pas à 0
            maximum = x;
        }
    }
    printf("Le plus grand nombre est : %d\n", maximum);
    return EXIT_SUCCESS;
}
```

## Projet 3 : fonctions et tableaux

```c
// fichier: projet03.c
// @stdin: 5\n10\n20\n5\n30\n25
#include <stdio.h>
#include <stdlib.h>

#define MAX 100

// `const int tab[]` : la fonction promet de ne pas modifier le tableau
static float calculer_moyenne(const int tab[], int n) {
    long somme = 0;
    for (int i = 0; i < n; i++) somme += tab[i];
    return (float)somme / (float)n;
}

static int maximum(const int tab[], int n) {
    int m = tab[0];
    for (int i = 1; i < n; i++) {
        if (tab[i] > m) m = tab[i];
    }
    return m;
}

static int minimum(const int tab[], int n) {
    int m = tab[0];
    for (int i = 1; i < n; i++) {
        if (tab[i] < m) m = tab[i];
    }
    return m;
}

int main(void) {
    int n, tab[MAX];

    printf("Nombre d'éléments (max %d) : ", MAX);
    if (scanf("%d", &n) != 1 || n < 1 || n > MAX) {
        fprintf(stderr, "Nombre invalide.\n");
        return EXIT_FAILURE;
    }
    for (int i = 0; i < n; i++) {
        printf("Nombre %d : ", i + 1);
        if (scanf("%d", &tab[i]) != 1) {
            fprintf(stderr, "Saisie invalide.\n");
            return EXIT_FAILURE;
        }
    }
    printf("Moyenne : %.2f\n", calculer_moyenne(tab, n));
    printf("Maximum : %d\n", maximum(tab, n));
    printf("Minimum : %d\n", minimum(tab, n));
    return EXIT_SUCCESS;
}
```

## Projet 4 : structures et chaînes

```c
// fichier: projet04.c
// @stdin: 2\nAlice\n20\n88.5\nBob\n22\n92.0
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TAILLE_NOM 50

typedef struct {
    char  nom[TAILLE_NOM];
    int   age;
    float note;
} Etudiant;

// Lit une ligne sans dépasser `taille` ; vide le reste de la ligne si elle était trop longue
static int lire_ligne(char *tampon, size_t taille) {
    if (fgets(tampon, (int)taille, stdin) == NULL) return 0;
    char *fin = strchr(tampon, '\n');
    if (fin != NULL) {
        *fin = '\0';
    } else {
        int c;
        while ((c = getchar()) != '\n' && c != EOF) { }
    }
    return 1;
}

static int saisir(Etudiant *e) {
    char ligne[64];
    printf("Nom : ");
    if (!lire_ligne(e->nom, sizeof e->nom)) return 0;
    printf("Âge : ");
    if (!lire_ligne(ligne, sizeof ligne) || sscanf(ligne, "%d", &e->age) != 1) return 0;
    printf("Note : ");
    if (!lire_ligne(ligne, sizeof ligne) || sscanf(ligne, "%f", &e->note) != 1) return 0;
    return 1;
}

int main(void) {
    char ligne[64];
    int n;

    printf("Nombre d'étudiants : ");
    if (!lire_ligne(ligne, sizeof ligne) || sscanf(ligne, "%d", &n) != 1 || n < 1) {
        fprintf(stderr, "Nombre invalide.\n");
        return EXIT_FAILURE;
    }

    Etudiant *liste = calloc((size_t)n, sizeof *liste);
    if (liste == NULL) {
        fprintf(stderr, "Échec de l'allocation.\n");
        return EXIT_FAILURE;
    }

    for (int i = 0; i < n; i++) {
        printf("\nÉtudiant %d :\n", i + 1);
        if (!saisir(&liste[i])) {
            fprintf(stderr, "Saisie invalide.\n");
            free(liste);
            return EXIT_FAILURE;
        }
    }

    printf("\n--- Récapitulatif ---\n");
    for (int i = 0; i < n; i++) {
        printf("\nÉtudiant %d :\nNom : %s\nÂge : %d\nNote : %.2f\n",
               i + 1, liste[i].nom, liste[i].age, liste[i].note);
    }

    free(liste);
    return EXIT_SUCCESS;
}
```

## Projet 5 : tableau dynamique

```c
// fichier: projet05.c
// @stdin: 5\n10\n20\n30\n40\n50
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    printf("Nombre d'entiers : ");
    if (scanf("%d", &n) != 1 || n < 1) {
        fprintf(stderr, "Nombre invalide.\n");
        return EXIT_FAILURE;
    }

    int *tab = malloc((size_t)n * sizeof *tab); // `sizeof *tab` suit automatiquement le type de tab
    if (tab == NULL) {
        fprintf(stderr, "Échec de l'allocation.\n");
        return EXIT_FAILURE;
    }

    for (int i = 0; i < n; i++) {
        printf("Nombre %d : ", i + 1);
        if (scanf("%d", &tab[i]) != 1) {
            fprintf(stderr, "Saisie invalide.\n");
            free(tab);
            return EXIT_FAILURE;
        }
    }

    printf("\nEntiers saisis :\n");
    for (int i = 0; i < n; i++) printf("%d ", tab[i]);
    printf("\n");

    free(tab);
    tab = NULL; // évite un pointeur pendant : un second free(NULL) est sans danger
    return EXIT_SUCCESS;
}
```

### Bonus : un tableau qui grandit avec `realloc`

```c
// fichier: projet05_vecteur.c
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int    *donnees;
    size_t  taille;
    size_t  capacite;
} Vecteur;

static int vecteur_ajouter(Vecteur *v, int valeur) {
    if (v->taille == v->capacite) {
        size_t nouvelle = v->capacite == 0 ? 4 : v->capacite * 2; // on double : coût moyen constant
        // ⚠️ On range le résultat dans une variable TEMPORAIRE : si realloc échoue (NULL),
        //    écrire v->donnees = realloc(...) ferait perdre l'ancien bloc (fuite mémoire)
        int *tmp = realloc(v->donnees, nouvelle * sizeof *tmp);
        if (tmp == NULL) return 0;
        v->donnees = tmp;
        v->capacite = nouvelle;
    }
    v->donnees[v->taille++] = valeur;
    return 1;
}

int main(void) {
    Vecteur v = {0};
    for (int i = 0; i < 100; i++) {
        if (!vecteur_ajouter(&v, i * i)) {
            fprintf(stderr, "Mémoire insuffisante.\n");
            free(v.donnees);
            return EXIT_FAILURE;
        }
    }
    assert(v.taille == 100 && v.donnees[99] == 9801 && v.capacite == 128);
    printf("Taille : %zu, capacité : %zu\n", v.taille, v.capacite);
    free(v.donnees);
    return EXIT_SUCCESS;
}
```

---

# Partie 3 : structures de données et fichiers

## Projet 6 : liste chaînée simple

```c
// fichier: projet06.c
// @stdin: 3\n10\n20\n30
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct Noeud {
    int valeur;
    struct Noeud *suivant;
} Noeud;

// `Noeud **tete` : pointeur sur le pointeur de tête, pour pouvoir MODIFIER la tête
static int ajouter_fin(Noeud **tete, int valeur) {
    Noeud *n = malloc(sizeof *n);
    if (n == NULL) return 0;
    n->valeur = valeur;
    n->suivant = NULL;

    if (*tete == NULL) {
        *tete = n;
        return 1;
    }
    Noeud *courant = *tete;
    while (courant->suivant != NULL) courant = courant->suivant;
    courant->suivant = n;
    return 1;
}

static void afficher(const Noeud *tete) {
    for (const Noeud *c = tete; c != NULL; c = c->suivant) printf("%d ", c->valeur);
    printf("\n");
}

static void liberer(Noeud *tete) {
    while (tete != NULL) {
        Noeud *suivant = tete->suivant; // on SAUVEGARDE le suivant AVANT de libérer le nœud
        free(tete);
        tete = suivant;
    }
}

// ➕ Pour aller plus loin
static int inserer_debut(Noeud **tete, int valeur) {
    Noeud *n = malloc(sizeof *n);
    if (n == NULL) return 0;
    n->valeur = valeur;
    n->suivant = *tete;
    *tete = n;
    return 1;
}

static int supprimer(Noeud **tete, int valeur) {
    for (Noeud **p = tete; *p != NULL; p = &(*p)->suivant) { // p pointe sur le « lien » à modifier
        if ((*p)->valeur == valeur) {
            Noeud *a_liberer = *p;
            *p = a_liberer->suivant;
            free(a_liberer);
            return 1;
        }
    }
    return 0;
}

static void inverser(Noeud **tete) {
    Noeud *precedent = NULL, *courant = *tete;
    while (courant != NULL) {
        Noeud *suivant = courant->suivant;
        courant->suivant = precedent;
        precedent = courant;
        courant = suivant;
    }
    *tete = precedent;
}

static int valeur_a(const Noeud *tete, int indice) {
    while (indice-- > 0) tete = tete->suivant;
    return tete->valeur;
}

int main(void) {
    int n;
    printf("Nombre d'éléments de la liste : ");
    if (scanf("%d", &n) != 1 || n < 0) return EXIT_FAILURE;

    Noeud *tete = NULL;
    for (int i = 1; i <= n; i++) {
        int x;
        printf("Élément %d : ", i);
        if (scanf("%d", &x) != 1 || !ajouter_fin(&tete, x)) {
            liberer(tete);
            return EXIT_FAILURE;
        }
    }
    printf("\nListe chaînée : ");
    afficher(tete);

    // Tests des extensions : 10 20 30 → 5 10 20 30 → 5 10 30 → 30 10 5
    inserer_debut(&tete, 5);
    assert(valeur_a(tete, 0) == 5 && valeur_a(tete, 3) == 30);
    assert(supprimer(&tete, 20) == 1 && supprimer(&tete, 99) == 0);
    inverser(&tete);
    assert(valeur_a(tete, 0) == 30 && valeur_a(tete, 1) == 10 && valeur_a(tete, 2) == 5);

    liberer(tete);
    return EXIT_SUCCESS;
}
```

## Projet 7 : fichiers texte

```c
// fichier: projet07.c
// @stdin: 3\n10\n20\n30
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    printf("Nombre d'entiers : ");
    if (scanf("%d", &n) != 1 || n < 1) return EXIT_FAILURE;

    int *valeurs = malloc((size_t)n * sizeof *valeurs);
    if (valeurs == NULL) return EXIT_FAILURE;
    printf("Saisissez %d entiers à écrire dans le fichier :\n", n);
    for (int i = 0; i < n; i++) {
        printf("Nombre %d : ", i + 1);
        if (scanf("%d", &valeurs[i]) != 1) {
            free(valeurs);
            return EXIT_FAILURE;
        }
    }

    // Écriture
    FILE *f = fopen("nombres.txt", "w");
    if (f == NULL) {
        perror("nombres.txt");
        free(valeurs);
        return EXIT_FAILURE;
    }
    for (int i = 0; i < n; i++) fprintf(f, "%d\n", valeurs[i]);
    if (fclose(f) != 0) { // fclose peut échouer : c'est à ce moment que les dernières données sont écrites
        perror("fclose");
        free(valeurs);
        return EXIT_FAILURE;
    }
    free(valeurs);

    // Lecture
    f = fopen("nombres.txt", "r");
    if (f == NULL) {
        perror("nombres.txt");
        return EXIT_FAILURE;
    }
    printf("\nNombres lus dans le fichier :\n");
    int x;
    while (fscanf(f, "%d", &x) == 1) { // fscanf renvoie 1 tant qu'il lit un entier
        printf("%d ", x);
    }
    printf("\n");
    fclose(f);
    return EXIT_SUCCESS;
}
```

## Projet 8 : fichiers binaires

```c
// fichier: projet08.c
// @stdin: 2\nAlice\n20\n88.5\nBob\n22\n92.0
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char  nom[50];
    int   age;
    float note;
} Etudiant;

static int lire_ligne(char *tampon, size_t taille) {
    if (fgets(tampon, (int)taille, stdin) == NULL) return 0;
    char *fin = strchr(tampon, '\n');
    if (fin != NULL) *fin = '\0';
    return 1;
}

int main(void) {
    char ligne[64];
    int n;
    printf("Nombre d'étudiants : ");
    if (!lire_ligne(ligne, sizeof ligne) || sscanf(ligne, "%d", &n) != 1 || n < 1) return EXIT_FAILURE;

    // calloc met tout à zéro, y compris les octets de remplissage (padding) de la structure
    Etudiant *liste = calloc((size_t)n, sizeof *liste);
    if (liste == NULL) return EXIT_FAILURE;

    for (int i = 0; i < n; i++) {
        printf("\nÉtudiant %d :\nNom : ", i + 1);
        if (!lire_ligne(liste[i].nom, sizeof liste[i].nom)) { free(liste); return EXIT_FAILURE; }
        printf("Âge : ");
        if (!lire_ligne(ligne, sizeof ligne) || sscanf(ligne, "%d", &liste[i].age) != 1) { free(liste); return EXIT_FAILURE; }
        printf("Note : ");
        if (!lire_ligne(ligne, sizeof ligne) || sscanf(ligne, "%f", &liste[i].note) != 1) { free(liste); return EXIT_FAILURE; }
    }

    // Écriture binaire : fwrite renvoie le nombre d'éléments écrits
    FILE *f = fopen("etudiants.bin", "wb");
    if (f == NULL) { perror("etudiants.bin"); free(liste); return EXIT_FAILURE; }
    if (fwrite(liste, sizeof *liste, (size_t)n, f) != (size_t)n) {
        fprintf(stderr, "Erreur d'écriture.\n");
        fclose(f);
        free(liste);
        return EXIT_FAILURE;
    }
    fclose(f);
    free(liste);

    // Lecture binaire : on lit un étudiant à la fois, jusqu'à la fin du fichier
    f = fopen("etudiants.bin", "rb");
    if (f == NULL) { perror("etudiants.bin"); return EXIT_FAILURE; }
    printf("\nLecture des étudiants depuis le fichier :\n");
    Etudiant e;
    while (fread(&e, sizeof e, 1, f) == 1) {
        printf("Nom : %s\nÂge : %d\nNote : %.2f\n-----------------------\n", e.nom, e.age, e.note);
    }
    fclose(f);
    return EXIT_SUCCESS;
}
```

> ⚠️ Le fichier dépend de la machine et du compilateur (remplissage de la structure, taille des types, ordre des octets) : il n'est pas portable. Pour échanger des données, préférez un format texte (CSV, JSON).

---

# Partie 4 : threads

## Projet 9 : somme parallèle d'un tableau

```c
// fichier: projet09.c
// @stdin: 6\n1 2 3 4 5 6
#define _POSIX_C_SOURCE 200809L
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    const int *tab;
    size_t     debut, fin; // plage [debut, fin)
    long       somme;      // résultat partiel : chaque thread écrit dans SA structure
} Donnees;

static void *somme_partielle(void *arg) {
    Donnees *d = arg;
    d->somme = 0;
    for (size_t i = d->debut; i < d->fin; i++) d->somme += d->tab[i];
    return NULL;
}

int main(void) {
    int n;
    printf("Nombre d'éléments du tableau : ");
    if (scanf("%d", &n) != 1 || n < 1) return EXIT_FAILURE;

    int *tab = malloc((size_t)n * sizeof *tab);
    if (tab == NULL) return EXIT_FAILURE;
    printf("Saisissez %d entiers :\n", n);
    for (int i = 0; i < n; i++) {
        if (scanf("%d", &tab[i]) != 1) { free(tab); return EXIT_FAILURE; }
    }

    size_t milieu = (size_t)n / 2;
    Donnees d[2] = {
        { tab, 0, milieu, 0 },
        { tab, milieu, (size_t)n, 0 },
    };

    pthread_t threads[2];
    for (int i = 0; i < 2; i++) {
        int rc = pthread_create(&threads[i], NULL, somme_partielle, &d[i]);
        if (rc != 0) { // pthread_create renvoie un code d'erreur (et ne modifie pas errno)
            fprintf(stderr, "pthread_create a échoué (code %d)\n", rc);
            free(tab);
            return EXIT_FAILURE;
        }
    }
    for (int i = 0; i < 2; i++) pthread_join(threads[i], NULL); // on attend la fin des deux

    printf("Somme totale : %ld\n", d[0].somme + d[1].somme);
    free(tab);
    return EXIT_SUCCESS;
}
```

```text
Nombre d'éléments du tableau : 6
Saisissez 6 entiers :
Somme totale : 21
```

## Projet 10 : mutex

```c
// fichier: projet10.c
// @cflags: -DINCREMENTS=200000
#define _POSIX_C_SOURCE 200809L
#include <pthread.h>
#include <stdatomic.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NB_THREADS 10
#ifndef INCREMENTS
#define INCREMENTS 1000000
#endif

static long compteur = 0;
static pthread_mutex_t verrou = PTHREAD_MUTEX_INITIALIZER;
static atomic_long compteur_atomique = 0;

// 1. Avec mutex : correct, mais chaque incrément paie un verrouillage
static void *avec_mutex(void *arg) {
    (void)arg;
    for (long i = 0; i < INCREMENTS; i++) {
        pthread_mutex_lock(&verrou);
        compteur++;
        pthread_mutex_unlock(&verrou);
    }
    return NULL;
}

// 2. SANS protection : course de données (comportement indéfini), à ne montrer que pour comprendre
static void *sans_mutex(void *arg) {
    (void)arg;
    for (long i = 0; i < INCREMENTS; i++) compteur++;
    return NULL;
}

// 3. Accumulation locale puis UN SEUL verrouillage par thread : correct et beaucoup plus rapide
static void *accumulation_locale(void *arg) {
    (void)arg;
    long local = 0;
    for (long i = 0; i < INCREMENTS; i++) local++;
    pthread_mutex_lock(&verrou);
    compteur += local;
    pthread_mutex_unlock(&verrou);
    return NULL;
}

// 4. Variable atomique (C11) : correct sans mutex pour un simple compteur
static void *avec_atomique(void *arg) {
    (void)arg;
    for (long i = 0; i < INCREMENTS; i++) atomic_fetch_add(&compteur_atomique, 1);
    return NULL;
}

static void lancer(void *(*fonction)(void *)) {
    pthread_t threads[NB_THREADS];
    for (int i = 0; i < NB_THREADS; i++) {
        if (pthread_create(&threads[i], NULL, fonction, NULL) != 0) {
            fprintf(stderr, "pthread_create a échoué\n");
            exit(EXIT_FAILURE);
        }
    }
    for (int i = 0; i < NB_THREADS; i++) pthread_join(threads[i], NULL);
}

int main(int argc, char *argv[]) {
    const long attendu = (long)NB_THREADS * INCREMENTS;

    if (argc > 1 && strcmp(argv[1], "--sans-mutex") == 0) {
        lancer(sans_mutex);
        printf("Sans mutex : %ld (attendu : %ld) → en général FAUX, différent à chaque exécution\n", compteur, attendu);
        return EXIT_SUCCESS;
    }

    compteur = 0;
    lancer(avec_mutex);
    printf("Avec mutex           : %ld\n", compteur);

    compteur = 0;
    lancer(accumulation_locale);
    printf("Accumulation locale  : %ld\n", compteur);

    lancer(avec_atomique);
    printf("Variable atomique    : %ld\n", (long)atomic_load(&compteur_atomique));

    pthread_mutex_destroy(&verrou);
    return (compteur == attendu && atomic_load(&compteur_atomique) == attendu) ? EXIT_SUCCESS : EXIT_FAILURE;
}
```

Avec `INCREMENTS` à `1000000` (valeur par défaut), les trois versions correctes affichent `10000000`. Pour **détecter** la course de données de la version sans protection : `gcc -std=c17 -g -pthread -fsanitize=thread projet10.c -o p && ./p --sans-mutex` (ThreadSanitizer signale un `data race`).

## Projet 11 : producteur-consommateur

```c
// fichier: projet11.c
#define _POSIX_C_SOURCE 200809L
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

#define TAILLE 5       // capacité du tampon circulaire
#define NB_VALEURS 10

static int tampon[TAILLE];
static int tete = 0, queue = 0, compte = 0; // `compte` : nombre d'éléments présents
static int termine = 0;                     // le producteur a-t-il fini ?

static pthread_mutex_t verrou = PTHREAD_MUTEX_INITIALIZER;
static pthread_cond_t non_plein = PTHREAD_COND_INITIALIZER;
static pthread_cond_t non_vide = PTHREAD_COND_INITIALIZER;

static void *producteur(void *arg) {
    (void)arg;
    for (int i = 1; i <= NB_VALEURS; i++) {
        int valeur = i * 11;

        pthread_mutex_lock(&verrou);
        while (compte == TAILLE) {                      // `while`, jamais `if` (réveils intempestifs)
            pthread_cond_wait(&non_plein, &verrou);     // libère le mutex et s'endort
        }
        tampon[queue] = valeur;
        queue = (queue + 1) % TAILLE;
        compte++;
        printf("Produit : %d\n", valeur);
        pthread_cond_signal(&non_vide);
        pthread_mutex_unlock(&verrou);
    }

    pthread_mutex_lock(&verrou);
    termine = 1;                                        // signal de fin
    pthread_cond_broadcast(&non_vide);                  // réveille le consommateur s'il dort
    pthread_mutex_unlock(&verrou);
    return NULL;
}

static void *consommateur(void *arg) {
    (void)arg;
    for (;;) {
        pthread_mutex_lock(&verrou);
        while (compte == 0 && !termine) {
            pthread_cond_wait(&non_vide, &verrou);
        }
        if (compte == 0) {                              // vide ET terminé : on s'arrête
            pthread_mutex_unlock(&verrou);
            break;
        }
        int valeur = tampon[tete];
        tete = (tete + 1) % TAILLE;
        compte--;
        printf("Consommé : %d\n", valeur);
        pthread_cond_signal(&non_plein);
        pthread_mutex_unlock(&verrou);
    }
    return NULL;
}

int main(void) {
    pthread_t p, c;
    if (pthread_create(&p, NULL, producteur, NULL) != 0 || pthread_create(&c, NULL, consommateur, NULL) != 0) {
        fprintf(stderr, "pthread_create a échoué\n");
        return EXIT_FAILURE;
    }
    pthread_join(p, NULL);
    pthread_join(c, NULL);
    return EXIT_SUCCESS;
}
```

## Projet 12 : verrous lecteurs-rédacteur

```c
// fichier: projet12.c
#define _POSIX_C_SOURCE 200809L
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NB_LECTEURS 3
#define NB_REDACTEURS 2

static int donnee = 0;
static pthread_rwlock_t verrou = PTHREAD_RWLOCK_INITIALIZER;

static void pause_ms(long ms) {
    struct timespec t = { ms / 1000, (ms % 1000) * 1000000L };
    nanosleep(&t, NULL);
}

static void *lecteur(void *arg) {
    int id = *(int *)arg;
    for (int i = 0; i < 3; i++) {
        pthread_rwlock_rdlock(&verrou);           // plusieurs lecteurs peuvent entrer ensemble
        printf("Lecteur %d : donnée lue = %d\n", id, donnee);
        pthread_rwlock_unlock(&verrou);
        pause_ms(10);
    }
    return NULL;
}

static void *redacteur(void *arg) {
    int id = *(int *)arg;
    for (int i = 0; i < 2; i++) {
        pthread_rwlock_wrlock(&verrou);           // accès EXCLUSIF : aucun lecteur, aucun autre rédacteur
        donnee++;
        printf("Rédacteur %d : donnée modifiée = %d\n", id, donnee);
        pthread_rwlock_unlock(&verrou);
        pause_ms(25);
    }
    return NULL;
}

int main(void) {
    pthread_t lecteurs[NB_LECTEURS], redacteurs[NB_REDACTEURS];
    int id_l[NB_LECTEURS], id_r[NB_REDACTEURS];

    for (int i = 0; i < NB_LECTEURS; i++) {
        id_l[i] = i + 1;
        pthread_create(&lecteurs[i], NULL, lecteur, &id_l[i]);
    }
    for (int i = 0; i < NB_REDACTEURS; i++) {
        id_r[i] = i + 1;
        pthread_create(&redacteurs[i], NULL, redacteur, &id_r[i]);
    }
    for (int i = 0; i < NB_LECTEURS; i++) pthread_join(lecteurs[i], NULL);
    for (int i = 0; i < NB_REDACTEURS; i++) pthread_join(redacteurs[i], NULL);

    printf("Valeur finale : %d\n", donnee); // 4 : deux rédacteurs × deux modifications
    pthread_rwlock_destroy(&verrou);
    return EXIT_SUCCESS;
}
```

---

# Partie 5 : graphes

> Les graphes G1, G2 et G3 sont ceux définis dans l'énoncé (section « Graphes de référence »).

## Projets 13 et 14 : BFS et DFS sur le graphe G1

```c
// fichier: projet13_14.c
#include <stdio.h>
#include <stdlib.h>

#define N 6

typedef struct Arc {
    int vers;
    struct Arc *suivant;
} Arc;

// Ajout EN FIN de liste : les voisins sont parcourus dans l'ordre des appels (0→1 avant 0→2)
static void ajouter_arc(Arc *adj[], int u, int v) {
    Arc *a = malloc(sizeof *a);
    if (a == NULL) {
        perror("malloc");
        exit(EXIT_FAILURE);
    }
    a->vers = v;
    a->suivant = NULL;
    Arc **p = &adj[u];
    while (*p != NULL) p = &(*p)->suivant;
    *p = a;
}

static void liberer_graphe(Arc *adj[]) {
    for (int u = 0; u < N; u++) {
        Arc *a = adj[u];
        while (a != NULL) {
            Arc *suivant = a->suivant;
            free(a);
            a = suivant;
        }
    }
}

// Projet 13 : parcours en largeur, avec une FILE (chaque sommet n'y entre qu'une fois :
// un simple tableau de taille N suffit, sans qu'il soit nécessaire de le rendre circulaire)
static void bfs(Arc *adj[], int depart) {
    int visite[N] = {0}, file[N], tete = 0, queue = 0;

    visite[depart] = 1; // on marque À L'ENTRÉE dans la file, pas à la sortie
    file[queue++] = depart;
    while (tete < queue) {
        int u = file[tete++];
        printf("%d ", u);
        for (Arc *a = adj[u]; a != NULL; a = a->suivant) {
            if (!visite[a->vers]) {
                visite[a->vers] = 1;
                file[queue++] = a->vers;
            }
        }
    }
    printf("\n");
}

// Projet 14 : parcours en profondeur, version récursive
static void dfs_rec(Arc *adj[], int u, int visite[]) {
    visite[u] = 1;
    printf("%d ", u);
    for (Arc *a = adj[u]; a != NULL; a = a->suivant) {
        if (!visite[a->vers]) dfs_rec(adj, a->vers, visite);
    }
}

static void dfs(Arc *adj[], int depart) {
    int visite[N] = {0};
    dfs_rec(adj, depart, visite);
    printf("\n");
}

// ➕ Bonus 1 : version itérative. La pile mémorise, pour chaque sommet en cours, le PROCHAIN arc à explorer
static void dfs_iteratif(Arc *adj[], int depart) {
    int visite[N] = {0};
    Arc *pile[N]; // pile[i] : prochain arc à examiner du i-ème sommet de la pile
    int hauteur = 0;

    visite[depart] = 1;
    printf("%d ", depart);
    pile[hauteur++] = adj[depart];
    while (hauteur > 0) {
        Arc *a = pile[hauteur - 1];
        if (a == NULL) { // plus de voisins : on « remonte »
            hauteur--;
            continue;
        }
        pile[hauteur - 1] = a->suivant; // on avance dans la liste de ce sommet
        if (!visite[a->vers]) {
            visite[a->vers] = 1;
            printf("%d ", a->vers);
            pile[hauteur++] = adj[a->vers];
        }
    }
    printf("\n");
}

// ➕ Bonus 2 : graphe non connexe : on relance le parcours depuis chaque sommet non visité
static void dfs_tout(Arc *adj[], int depart) {
    int visite[N] = {0};
    dfs_rec(adj, depart, visite);
    for (int s = 0; s < N; s++) {
        if (!visite[s]) dfs_rec(adj, s, visite);
    }
    printf("\n");
}

int main(void) {
    Arc *adj[N] = {NULL};
    // Graphe G1 (orienté) : 0→1, 0→2, 1→3, 1→4, 2→5
    ajouter_arc(adj, 0, 1);
    ajouter_arc(adj, 0, 2);
    ajouter_arc(adj, 1, 3);
    ajouter_arc(adj, 1, 4);
    ajouter_arc(adj, 2, 5);

    printf("Parcours BFS à partir du sommet 0 :\n");
    bfs(adj, 0);
    printf("Parcours DFS à partir du sommet 0 :\n");
    dfs(adj, 0);
    printf("DFS itératif à partir du sommet 0 :\n");
    dfs_iteratif(adj, 0);
    printf("DFS depuis le sommet 1, puis les sommets non atteints :\n");
    dfs_tout(adj, 1);

    liberer_graphe(adj);
    return EXIT_SUCCESS;
}
```

```text
Parcours BFS à partir du sommet 0 :
0 1 2 3 4 5
Parcours DFS à partir du sommet 0 :
0 1 3 4 2 5
DFS itératif à partir du sommet 0 :
0 1 3 4 2 5
DFS depuis le sommet 1, puis les sommets non atteints :
1 3 4 0 2 5
```

## Projet 15 : Dijkstra sur le graphe G2

**Version simple, `O(V²)`** (matrice d'adjacence, recherche linéaire du minimum) :

```c
// fichier: projet15.c
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

#define N 6
#define INF INT_MAX

static int poids[N][N]; // 0 : pas d'arête (tous les poids sont strictement positifs)

static void ajouter_arete(int u, int v, int w) {
    poids[u][v] = w;
    poids[v][u] = w; // graphe non orienté
}

static void dijkstra(int depart, int dist[N], int parent[N]) {
    int traite[N] = {0};
    for (int i = 0; i < N; i++) {
        dist[i] = INF;
        parent[i] = -1;
    }
    dist[depart] = 0;

    for (int etape = 0; etape < N; etape++) {
        // Le sommet non traité de plus petite distance connue
        int u = -1;
        for (int i = 0; i < N; i++) {
            if (!traite[i] && dist[i] != INF && (u == -1 || dist[i] < dist[u])) u = i;
        }
        if (u == -1) break; // les sommets restants sont inaccessibles
        traite[u] = 1;

        for (int v = 0; v < N; v++) {
            // dist[u] != INF ici, donc dist[u] + poids ne peut pas déborder
            if (poids[u][v] > 0 && !traite[v] && dist[u] + poids[u][v] < dist[v]) {
                dist[v] = dist[u] + poids[u][v];
                parent[v] = u;
            }
        }
    }
}

// ➕ Bonus : reconstruire le chemin grâce aux prédécesseurs
static void afficher_chemin(const int parent[N], int v) {
    if (parent[v] != -1) {
        afficher_chemin(parent, parent[v]);
        printf(" → ");
    }
    printf("%d", v);
}

int main(void) {
    // Graphe G2
    ajouter_arete(0, 1, 10);
    ajouter_arete(0, 3, 15);
    ajouter_arete(1, 2, 10);
    ajouter_arete(3, 4, 20);
    ajouter_arete(3, 5, 10);
    ajouter_arete(2, 4, 30);

    int dist[N], parent[N];
    dijkstra(0, dist, parent);

    printf("Distances les plus courtes depuis le sommet 0 :\n");
    for (int i = 0; i < N; i++) {
        if (dist[i] == INF) printf("Sommet %d : inaccessible\n", i);
        else printf("Sommet %d : %d\n", i, dist[i]);
    }
    printf("Chemin vers le sommet 4 : ");
    afficher_chemin(parent, 4);
    printf("\n");
    return EXIT_SUCCESS;
}
```

```text
Distances les plus courtes depuis le sommet 0 :
Sommet 0 : 0
Sommet 1 : 10
Sommet 2 : 20
Sommet 3 : 15
Sommet 4 : 35
Sommet 5 : 25
Chemin vers le sommet 4 : 0 → 3 → 4
```

**Version optimisée, `O((V + E) log V)`** (listes d'adjacence et tas-minimum écrit à la main) :

```c
// fichier: projet15_tas.c
#include <stdio.h>
#include <stdlib.h>

#define N 6

typedef struct Arete {
    int vers, poids;
    struct Arete *suivant;
} Arete;

typedef struct {
    int dist, sommet;
} Entree;

typedef struct {
    Entree *tab;
    size_t  taille, capacite;
} Tas;

static void tas_ajouter(Tas *t, Entree e) {
    if (t->taille == t->capacite) {
        size_t nouvelle = t->capacite ? t->capacite * 2 : 8;
        Entree *tmp = realloc(t->tab, nouvelle * sizeof *tmp);
        if (tmp == NULL) {
            perror("realloc");
            exit(EXIT_FAILURE);
        }
        t->tab = tmp;
        t->capacite = nouvelle;
    }
    size_t i = t->taille++;
    while (i > 0) { // on « remonte » e tant qu'il est plus petit que son parent
        size_t p = (i - 1) / 2;
        if (t->tab[p].dist <= e.dist) break;
        t->tab[i] = t->tab[p];
        i = p;
    }
    t->tab[i] = e;
}

static Entree tas_extraire_min(Tas *t) {
    Entree min = t->tab[0];
    Entree dernier = t->tab[--t->taille];
    size_t i = 0;
    for (;;) { // on « descend » le dernier élément à sa place
        size_t g = 2 * i + 1;
        if (g >= t->taille) break;
        size_t d = g + 1;
        size_t m = (d < t->taille && t->tab[d].dist < t->tab[g].dist) ? d : g;
        if (dernier.dist <= t->tab[m].dist) break;
        t->tab[i] = t->tab[m];
        i = m;
    }
    if (t->taille > 0) t->tab[i] = dernier;
    return min;
}

static void ajouter_arete(Arete *adj[], int u, int v, int w) {
    Arete *a = malloc(sizeof *a), *b = malloc(sizeof *b);
    if (a == NULL || b == NULL) {
        perror("malloc");
        exit(EXIT_FAILURE);
    }
    *a = (Arete){ v, w, adj[u] };
    adj[u] = a;
    *b = (Arete){ u, w, adj[v] };
    adj[v] = b;
}

int main(void) {
    Arete *adj[N] = {NULL};
    ajouter_arete(adj, 0, 1, 10);
    ajouter_arete(adj, 0, 3, 15);
    ajouter_arete(adj, 1, 2, 10);
    ajouter_arete(adj, 3, 4, 20);
    ajouter_arete(adj, 3, 5, 10);
    ajouter_arete(adj, 2, 4, 30);

    int dist[N];
    for (int i = 0; i < N; i++) dist[i] = -1; // -1 : pas encore atteint
    dist[0] = 0;

    Tas tas = {0};
    tas_ajouter(&tas, (Entree){ 0, 0 });
    while (tas.taille > 0) {
        Entree e = tas_extraire_min(&tas);
        if (e.dist > dist[e.sommet]) continue; // entrée périmée (« suppression paresseuse »)
        for (Arete *a = adj[e.sommet]; a != NULL; a = a->suivant) {
            int nouvelle = e.dist + a->poids;
            if (dist[a->vers] == -1 || nouvelle < dist[a->vers]) {
                dist[a->vers] = nouvelle;
                tas_ajouter(&tas, (Entree){ nouvelle, a->vers });
            }
        }
    }

    for (int i = 0; i < N; i++) printf("Sommet %d : %d\n", i, dist[i]);

    free(tas.tab);
    for (int u = 0; u < N; u++) {
        Arete *a = adj[u];
        while (a != NULL) {
            Arete *suivant = a->suivant;
            free(a);
            a = suivant;
        }
    }
    return EXIT_SUCCESS;
}
```

## Projet 16 : Kruskal sur le graphe G3

```c
// fichier: projet16.c
#include <stdio.h>
#include <stdlib.h>

#define V 5 // nombre de sommets
#define E 6 // nombre d'arêtes

typedef struct {
    int u, v, poids;
} Arete;

// --- Union-Find (ensembles disjoints) avec compression de chemin et union par rang ---
static int parent[V], rang[V];

static void initialiser(void) {
    for (int i = 0; i < V; i++) {
        parent[i] = i; // chaque sommet est d'abord seul dans son ensemble
        rang[i] = 0;
    }
}

static int trouver(int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]]; // compression de chemin (« path halving »)
        x = parent[x];
    }
    return x;
}

// Renvoie 0 si a et b étaient DÉJÀ dans le même ensemble (l'arête créerait un cycle)
static int unir(int a, int b) {
    int ra = trouver(a), rb = trouver(b);
    if (ra == rb) return 0;
    if (rang[ra] < rang[rb]) {
        int tmp = ra;
        ra = rb;
        rb = tmp;
    }
    parent[rb] = ra;
    if (rang[ra] == rang[rb]) rang[ra]++;
    return 1;
}

static int comparer(const void *a, const void *b) {
    const Arete *x = a, *y = b;
    return (x->poids > y->poids) - (x->poids < y->poids);
}

int main(void) {
    // Graphe G3
    Arete aretes[E] = {
        {2, 4, 2}, {0, 3, 5}, {1, 2, 7}, {0, 1, 10}, {0, 2, 12}, {3, 4, 15},
    };

    qsort(aretes, E, sizeof aretes[0], comparer); // par poids croissant
    initialiser();

    printf("Arêtes du MST :\n");
    int total = 0, retenues = 0;
    for (int i = 0; i < E && retenues < V - 1; i++) { // un MST a V − 1 arêtes
        if (unir(aretes[i].u, aretes[i].v)) {
            printf("%d - %d : %d\n", aretes[i].u, aretes[i].v, aretes[i].poids);
            total += aretes[i].poids;
            retenues++;
        }
    }
    printf("Poids total : %d\n", total);
    return retenues == V - 1 ? EXIT_SUCCESS : EXIT_FAILURE; // sinon : graphe non connexe
}
```

```text
Arêtes du MST :
2 - 4 : 2
0 - 3 : 5
1 - 2 : 7
0 - 1 : 10
Poids total : 24
```

## Projet 17 : Prim sur le graphe G3

```c
// fichier: projet17.c
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

#define V 5

static int poids[V][V]; // 0 : pas d'arête

static void ajouter_arete(int u, int v, int w) {
    poids[u][v] = w;
    poids[v][u] = w;
}

int main(void) {
    // Graphe G3
    ajouter_arete(2, 4, 2);
    ajouter_arete(0, 3, 5);
    ajouter_arete(1, 2, 7);
    ajouter_arete(0, 1, 10);
    ajouter_arete(0, 2, 12);
    ajouter_arete(3, 4, 15);

    int cle[V];      // cle[v] : poids de la plus petite arête reliant v à l'arbre
    int parent[V];   // parent[v] : l'autre extrémité de cette arête
    int dans_arbre[V] = {0};
    for (int i = 0; i < V; i++) {
        cle[i] = INT_MAX;
        parent[i] = -1;
    }
    cle[0] = 0; // on part du sommet 0

    printf("Arêtes du MST :\n");
    int total = 0;
    for (int etape = 0; etape < V; etape++) {
        // Le sommet hors de l'arbre dont la clé est la plus petite
        int u = -1;
        for (int i = 0; i < V; i++) {
            if (!dans_arbre[i] && cle[i] != INT_MAX && (u == -1 || cle[i] < cle[u])) u = i;
        }
        if (u == -1) {
            fprintf(stderr, "Graphe non connexe.\n");
            return EXIT_FAILURE;
        }
        dans_arbre[u] = 1;
        if (parent[u] != -1) {
            printf("%d - %d : %d\n", parent[u], u, cle[u]);
            total += cle[u];
        }

        // Mise à jour des clés des voisins de u
        for (int v = 0; v < V; v++) {
            if (poids[u][v] > 0 && !dans_arbre[v] && poids[u][v] < cle[v]) {
                cle[v] = poids[u][v];
                parent[v] = u;
            }
        }
    }
    printf("Poids total : %d\n", total);
    return EXIT_SUCCESS;
}
```

```text
Arêtes du MST :
0 - 3 : 5
0 - 1 : 10
1 - 2 : 7
2 - 4 : 2
Poids total : 24
```

> ✅ Kruskal et Prim donnent le **même poids total** (24) : ici les poids sont tous différents, donc l'arbre couvrant minimal est unique et seul l'ordre d'affichage change.
>
> 💡 Pour la version optimisée de Prim (`O((V + E) log V)`), remplacez la recherche linéaire du minimum par le **tas-minimum** de Dijkstra : on y range des paires `(clé, sommet)` et on ignore les entrées périmées à la sortie.

---

## 🧾 Récapitulatif

| Notion | Où ? |
| --- | --- |
| Entrées sécurisées : `fgets` + `sscanf`, retour de `scanf` | Séries 7, projets 1 à 8 |
| Comportements indéfinis évités (débordement signé, pointeur pendant, `d * d`) | Séries 4, 9, 10 |
| Mémoire dynamique : `malloc` / `calloc` / `realloc` / `free` | Projets 4 à 8, 15 (tas) |
| `realloc` sûr (variable temporaire) | Projet 5 (bonus), 15 (tas) |
| Listes chaînées, pointeur sur pointeur | Projet 6, 13 |
| Fichiers texte et binaires, `fclose` vérifié | Projets 7 et 8 |
| `pthread_create` / `join`, `mutex`, variables de condition, verrou R/W, atomiques | Projets 9 à 12 |
| ThreadSanitizer, `-fsanitize=address,undefined` | Projet 10 et toute la partie 1 |
| BFS, DFS (récursif et itératif), graphe non connexe | Projets 13 et 14 |
| Dijkstra (`O(V²)` puis tas), prédécesseurs | Projet 15 |
| Union-Find, Kruskal, Prim | Projets 16 et 17 |
