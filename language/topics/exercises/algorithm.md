<div align="center">

# Algorithmique — Exercices

**Des fondements à la programmation dynamique, aux graphes et aux flots**

*Exemples en Python 3.12+ · Mis à jour en octobre 2026*

</div>

---

## Outils

| Ressource | Lien |
| --- | --- |
| Cours | [algorithm](/language/algorithm) |

---

## Sommaire

**Niveau débutant**

1. [Introduction aux algorithmes](#1-introduction-aux-algorithmes)
2. [Analyse des algorithmes](#2-analyse-des-algorithmes)
3. [Structures de données essentielles](#3-structures-de-données-essentielles)
4. [Récursivité de base](#4-récursivité-de-base)
5. [Algorithmes de tri simples](#5-algorithmes-de-tri-simples)
6. [Algorithmes de recherche](#6-algorithmes-de-recherche)
7. [Algorithmes mathématiques de base](#7-algorithmes-mathématiques-de-base)

**Niveau intermédiaire**

8. [Algorithmes de tri avancés](#8-algorithmes-de-tri-avancés)
9. [Diviser pour régner](#9-diviser-pour-régner)
10. [Algorithmes gloutons](#10-algorithmes-gloutons)
11. [Retour sur trace (*backtracking*)](#11-retour-sur-trace-backtracking)
12. [Technique des deux pointeurs](#12-technique-des-deux-pointeurs)
13. [Fenêtre glissante](#13-fenêtre-glissante)
14. [Sommes préfixes et tableaux de différences](#14-sommes-préfixes-et-tableaux-de-différences)
15. [Recherche binaire sur la réponse](#15-recherche-binaire-sur-la-réponse)
16. [Algorithmes de théorie des nombres](#16-algorithmes-de-théorie-des-nombres)
17. [Hachage](#17-hachage)

**Niveau avancé**

18. [Programmation dynamique](#18-programmation-dynamique)
19. [Algorithmes sur les graphes](#19-algorithmes-sur-les-graphes)
20. [Plus courts chemins dans les graphes pondérés](#20-plus-courts-chemins-dans-les-graphes-pondérés)
21. [Composantes fortement connexes](#21-composantes-fortement-connexes)
22. [Flots dans les réseaux](#22-flots-dans-les-réseaux)
23. [Arbres de segments et arbres de Fenwick](#23-arbres-de-segments-et-arbres-de-fenwick)
24. [Algorithmes sur les chaînes](#24-algorithmes-sur-les-chaînes)
25. [Aller plus loin](#25-aller-plus-loin)

> **Légende** : chaque exercice porte le numéro de la section du cours qu'il illustre (l'exercice 5.2.1 est le premier exercice de la section 5.2). *(défi)* = exercice plus difficile ; les exemples utilisent Python, mais les idées s'appliquent à tout langage. Aucune solution n'est fournie dans ce document.

---

# Niveau débutant

---

# 1. Introduction aux algorithmes

*Comprendre les fondements de l'informatique et de la résolution de problèmes.*

## 1.1 Qu'est-ce qu'un algorithme ?

**Exercice 1.1.1**

Pour chacune des descriptions suivantes, indiquez laquelle des six propriétés d'un algorithme (entrée, sortie, précision, finitude, efficacité, correction) n'est pas respectée, et justifiez.

| Description | Propriété violée ? |
| --- | --- |
| « Tant que `x` est positif, ajouter 1 à `x`. » | |
| « Choisir un nombre convenable et l'afficher. » | |
| « Pour trouver le minimum d'une liste, renvoyer son premier élément. » | |
| « Afficher la liste de tous les nombres premiers. » | |
| « Calculer la racine carrée de 2 avec une précision infinie en un seul pas. » | |

**Exercice 1.1.2**

En vous inspirant de la fonction `maximum` du cours, écrivez une fonction `minimum(valeurs)` qui renvoie le plus petit élément d'une liste non vide. Testez-la sur `[3, 8, 2, 9, 4]` et sur une liste d'un seul élément.

**Exercice 1.1.3**

Écrivez une fonction `deux_plus_grands(valeurs)` qui renvoie le plus grand et le deuxième plus grand élément d'une liste d'au moins deux éléments, en **un seul parcours** et sans trier la liste.

**Exercice 1.1.4**

Écrivez une fonction `contient(valeurs, x)` qui indique si `x` apparaît dans la liste, sans utiliser l'opérateur `in`. Quelle est la sortie de votre algorithme pour une liste vide ?

## 1.2 Pourquoi les algorithmes sont-ils importants ?

**Exercice 1.2.1**

Complétez le tableau suivant (ordres de grandeur) :

| Taille `n` | Algorithme en O(n²) | Algorithme en O(n log n) |
| --- | --- | --- |
| 100 | | |
| 10 000 | | |
| 100 000 | | |

**Exercice 1.2.2**

En supposant qu'un programme Python effectue environ 10⁷ opérations simples par seconde, estimez le temps d'exécution d'un algorithme O(n²) puis O(n log n) pour `n = 10⁵`.

**Exercice 1.2.3**

Citez trois applications concrètes (autres que celles du cours) où le choix de l'algorithme change radicalement l'expérience de l'utilisateur, et précisez pour chacune ce qui rend l'efficacité critique.

## 1.3 Représenter un algorithme

**Exercice 1.3.1**

Soit le pseudo-code suivant :

```text
ALGORITHME Mystère(tableau)
  Entrée : un tableau de nombres entiers
  Sortie : un entier
  c ← 0
  POUR chaque x DANS tableau FAIRE
      SI x MODULO 2 = 0 ALORS c ← c + 1
  RETOURNER c
```

1. Que calcule cet algorithme ?
2. Traduisez-le en Python.
3. Dessinez l'organigramme correspondant (début, actions, décisions, fin).

**Exercice 1.3.2**

Écrivez en pseudo-code (dans le même format que le cours) un algorithme `Somme(tableau)` puis un algorithme `EstTrié(tableau)` qui indique si un tableau est trié par ordre croissant.

**Exercice 1.3.3**

Décrivez en langage naturel, puis sous forme d'organigramme, l'algorithme qui détermine si un entier est pair ou impair, et affiche le résultat.

## 1.4 Écrire son premier algorithme

**Exercice 1.4.1**

Écrivez un algorithme (étapes numérotées, puis code Python) qui calcule la moyenne de `n` notes saisies dans une liste.

**Exercice 1.4.2**

Écrivez un algorithme qui convertit une température de degrés Celsius en degrés Fahrenheit, puis l'inverse.

**Exercice 1.4.3**

Écrivez un algorithme qui échange les valeurs de deux variables `a` et `b` : d'abord avec une variable temporaire, puis sans.

**Exercice 1.4.4**

Écrivez un algorithme qui calcule le prix TTC d'un article à partir de son prix hors taxe et d'un taux de TVA en pourcentage.

## 1.5 Méthode pour résoudre un problème algorithmique *(ajout)*

**Exercice 1.5.1**

Appliquez les six étapes de la méthode au problème suivant : « Étant donné un tableau d'entiers et une cible `T`, déterminer s'il existe deux éléments distincts dont la somme vaut `T`. » Complétez le tableau :

| Étape | Votre réponse |
| --- | --- |
| 1. Comprendre | |
| 2. Exemples | |
| 3. Solution naïve | |
| 4. Optimiser | |
| 5. Analyser | |
| 6. Coder et tester | |

**Exercice 1.5.2**

Listez au moins six cas limites à tester pour une fonction `moyenne(valeurs)` qui renvoie la moyenne d'une liste de nombres.

**Exercice 1.5.3**

Pour chacune des contraintes suivantes, indiquez la complexité maximale raisonnable : `n ≤ 20`, `n ≤ 5 000`, `n ≤ 10⁵`, `n ≤ 10⁶`.

## 1.6 Grandes familles d'algorithmes

**Exercice 1.6.1**

Associez chaque problème à la famille d'algorithmes la plus naturelle (force brute, diviser pour régner, glouton, programmation dynamique, retour sur trace, graphes, probabiliste) :

1. Trier un tableau en le coupant en deux moitiés.
2. Placer 8 reines sur un échiquier sans qu'elles se menacent.
3. Trouver le chemin le plus court entre deux stations de métro.
4. Rendre la monnaie avec un système de pièces « canonique ».
5. Calculer la plus longue sous-séquence commune de deux textes.
6. Tester tous les codes à 4 chiffres d'un cadenas.
7. Tester la primalité d'un très grand nombre avec une petite probabilité d'erreur.

**Exercice 1.6.2**

Écrivez une attaque par force brute sur un cadenas à code de 4 chiffres : une fonction `forcer(code_secret)` qui renvoie le nombre d'essais nécessaires. Quel est le nombre d'essais dans le pire cas ?

## 1.7 Algorithme ou programme ?

**Exercice 1.7.1**

Indiquez si chaque affirmation est vraie ou fausse, en justifiant :

1. Un algorithme dépend du langage de programmation utilisé.
2. Un serveur web qui tourne sans fin est un programme, mais son comportement ne correspond pas à un algorithme au sens strict.
3. `sorted(liste)` est un algorithme.
4. Deux programmes écrits dans des langages différents peuvent implémenter le même algorithme.

**Exercice 1.7.2**

Écrivez le même algorithme de calcul de la somme des carrés des `n` premiers entiers sous trois formes : langage naturel, pseudo-code et code Python.

---

# 2. Analyse des algorithmes

## 2.1 Pourquoi analyser ?

**Exercice 2.1.1**

Donnez trois raisons pour lesquelles mesurer le temps d'exécution en secondes ne suffit pas pour comparer deux algorithmes.

**Exercice 2.1.2**

Distinguez complexité en temps et complexité en espace. Pour la fonction `maximum` de la section 1.1, donnez les deux.

## 2.2 Compter les opérations

**Exercice 2.2.1**

Déterminez `T(n)` (en comptant les opérations élémentaires) puis la complexité asymptotique de chaque fonction :

```python
def f1(t):
    c = 0
    for x in t:
        if x > 0:
            c += 1
    return c

def f2(t):
    n = len(t)
    c = 0
    for i in range(n):
        for j in range(n):
            if t[i] == t[j]:
                c += 1
    return c

def f3(n):
    c = 0
    while n > 1:
        n //= 2
        c += 1
    return c

def f4(t):
    for x in t:
        print(x)
    for x in t:
        print(2 * x)

def f5(n):
    c = 0
    for i in range(n):
        for j in range(i):
            c += 1
    return c

def f6(n):
    c = 0
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
            c += 1
    return c
```

**Exercice 2.2.2**

Réécrivez `f2` pour qu'elle ne compare chaque paire d'indices `(i, j)` avec `i < j` qu'une seule fois. Quelle est la nouvelle complexité ? Le gain est-il asymptotique ?

**Exercice 2.2.3**

Simplifiez en gardant le terme dominant : `5n + 100`, `n² + 1000n`, `3n log n + n`, `2ⁿ + n³`, `n! + 2ⁿ`.

## 2.3 Notations asymptotiques *(à jour : correction d'une erreur fréquente)*

**Exercice 2.3.1**

Pour `f(n) = 3n² + 5n`, trouvez explicitement des constantes `c` et `n₀` prouvant que `f ∈ O(n²)`, puis des constantes prouvant que `f ∈ Ω(n²)`. Concluez sur `Θ`.

**Exercice 2.3.2**

Indiquez si chaque affirmation est vraie ou fausse :

1. `n log n ∈ O(n²)`
2. `2ⁿ ∈ O(n¹⁰)`
3. `n² ∈ Ω(n)`
4. `5n ∈ o(n)`
5. `n + 10 ∈ Θ(n)`
6. `log n ∈ o(√n)`
7. `n³ ∈ Θ(n²)`

**Exercice 2.3.3**

Un étudiant affirme : « O désigne le pire cas, Ω le meilleur cas, Θ le cas moyen. » Expliquez pourquoi c'est faux. Illustrez avec le tri par insertion : donnez la fonction `T(n)` du meilleur cas et celle du pire cas, puis une borne `Θ` pour chacune.

**Exercice 2.3.4**

Classez par ordre de croissance et justifiez : `n log n`, `n²`, `√n`, `2ⁿ`, `log n`, `n`, `n!`, `n³`, `1`.

## 2.4 Pire, meilleur et cas moyen

**Exercice 2.4.1**

Pour la recherche linéaire dans une liste de `n` éléments distincts, où la cible est présente avec une probabilité uniforme sur chaque position, donnez `T(n)` dans le meilleur cas, le pire cas et le cas moyen.

**Exercice 2.4.2**

Donnez un exemple d'entrée de taille `n` qui déclenche le meilleur cas du tri par insertion, et un exemple qui déclenche le pire cas.

**Exercice 2.4.3**

Un quicksort choisit toujours le premier élément comme pivot. Donnez une entrée de taille `n` pour laquelle il atteint son pire cas, et expliquez pourquoi.

## 2.5 Classes de complexité usuelles

**Exercice 2.5.1**

En supposant 10⁷ opérations par seconde, estimez le temps d'exécution pour `n = 10⁶` d'un algorithme en O(n), O(n log n), O(n²) puis pour `n = 30` d'un algorithme en O(2ⁿ).

**Exercice 2.5.2**

Quelle est la plus grande valeur de `n` pour laquelle un algorithme en O(n²), O(n³), O(2ⁿ) puis O(n!) s'exécute en moins d'une seconde à raison de 10⁸ opérations par seconde ?

**Exercice 2.5.3**

Associez chaque fonction à une classe de complexité usuelle : accès à un indice d'un tableau, recherche binaire, test de primalité naïf, parcours d'une liste, tri efficace, deux boucles imbriquées, énumération de tous les sous-ensembles, énumération de toutes les permutations.

## 2.6 Complexité en espace

**Exercice 2.6.1**

Donnez la complexité en espace supplémentaire de chacune de ces fonctions :

```python
def a(t):
    return sum(t)

def b(t):
    return [x * x for x in t]

def c(n):
    return 1 if n == 0 else n * c(n - 1)

def d(n):
    return [[0] * n for _ in range(n)]

def e(t):
    t.sort()
    return t[0]
```

**Exercice 2.6.2**

Que se passe-t-il en Python quand on appelle `c(5000)` ? Proposez deux manières d'éviter le problème.

## 2.7 Compromis temps / espace

**Exercice 2.7.1**

On vous pose `10⁵` questions de la forme « `x` appartient-il à cette liste de `10⁵` éléments ? ». Comparez deux solutions (recherche linéaire à chaque question, et conversion préalable en `set`) en temps et en espace. Laquelle choisir ?

**Exercice 2.7.2**

Citez un exemple où l'on échange du temps contre de l'espace dans l'autre sens (économiser de la mémoire au prix de plus de calcul).

## 2.8 Analyse amortie *(ajout)*

**Exercice 2.8.1**

Un tableau dynamique double sa capacité quand il est plein (capacité initiale 1). Calculez le nombre total de copies d'éléments effectuées pendant `n = 2ᵏ` appels à `append`, puis le coût amorti par insertion.

**Exercice 2.8.2**

Un compteur binaire de `k` bits est incrémenté `n` fois à partir de 0. Dans le pire cas, une seule incrémentation modifie `k` bits. Montrez que le coût total des `n` incrémentations est cependant en O(n).

**Exercice 2.8.3**

Distinguez en deux phrases le coût amorti et le coût moyen au sens probabiliste.

## 2.9 Récurrences

**Exercice 2.9.1**

Donnez la solution asymptotique de chaque récurrence :

1. `T(n) = T(n − 1) + O(1)`
2. `T(n) = T(n/2) + O(1)`
3. `T(n) = 2T(n/2) + O(n)`
4. `T(n) = 2T(n − 1) + O(1)`
5. `T(n) = T(n − 1) + O(n)`
6. `T(n) = T(n/2) + O(n)`

**Exercice 2.9.2**

Écrivez la récurrence satisfaite par le nombre d'opérations de chacune des fonctions suivantes, puis résolvez-la :

```python
def puissance(x, n):
    if n == 0:
        return 1
    return x * puissance(x, n - 1)

def hanoi(n, a, b, c):
    if n == 0:
        return
    hanoi(n - 1, a, c, b)
    print(a, "->", c)
    hanoi(n - 1, b, a, c)

def somme_dc(t, g, d):
    if g == d:
        return t[g]
    m = (g + d) // 2
    return somme_dc(t, g, m) + somme_dc(t, m + 1, d)
```

## 2.10 Conseils pratiques

**Exercice 2.10.1**

Avec `timeit`, comparez le temps de `x in liste` et de `x in ensemble` pour des listes de taille `10³`, `10⁴`, `10⁵`. Tracez ou tabulez vos résultats et commentez.

**Exercice 2.10.2**

Identifiez l'opération cachée coûteuse et proposez une version plus rapide :

```python
def construire(n):
    s = ""
    for i in range(n):
        s += "a"
    return s

def file_naive(t):
    resultat = []
    while t:
        resultat.append(t.pop(0))
    return resultat

def inverser_naif(t):
    r = []
    for x in t:
        r.insert(0, x)
    return r
```

**Exercice 2.10.3**

Un tableau `n × n` d'entiers Python est-il envisageable pour `n = 10⁵` ? Justifiez par un calcul de mémoire.

---

# 3. Structures de données essentielles

## 3.1 Aperçu et complexités

**Exercice 3.1.1**

Complétez les cases vides du tableau (accès, recherche, insertion, suppression) :

| Structure | Accès | Recherche | Insertion | Suppression |
| --- | --- | --- | --- | --- |
| Tableau / `list` | | | | |
| Liste chaînée | | | | |
| Pile | | | | |
| File (`deque`) | | | | |
| Table de hachage | | | | |
| Tas | | | | |
| ABR équilibré | | | | |

**Exercice 3.1.2**

Pourquoi `list.insert(0, x)` est-il en O(n) alors que `deque.appendleft(x)` est en O(1) ?

## 3.2 Pile, file et file à double entrée

**Exercice 3.2.1**

Écrivez une fonction `parentheses_valides(s)` qui indique si une chaîne composée de `()[]{}` est correctement parenthésée, à l'aide d'une pile. Testez : `"([]{})"`, `"([)]"`, `"(("`, `""`.

**Exercice 3.2.2**

Implémentez une classe `FileAvecDeuxPiles` offrant `enfiler(x)` et `defiler()` en n'utilisant que deux piles (listes avec `append` / `pop`). Quelle est la complexité amortie de `defiler` ?

**Exercice 3.2.3**

Résolvez le problème de Josèphe : `n` personnes sont placées en cercle, on élimine une personne sur `k` jusqu'à ce qu'il n'en reste qu'une. Écrivez `josephe(n, k)` avec une `deque` et renvoyez la position du survivant.

**Exercice 3.2.4**

Évaluez une expression en notation polonaise inverse (par exemple `"3 4 + 2 *"`) à l'aide d'une pile.

**Exercice 3.2.5**

Mesurez le temps de `n` retraits en tête avec `list.pop(0)` puis avec `deque.popleft()` pour `n = 10⁵`. Commentez.

## 3.3 Liste chaînée

**Exercice 3.3.1**

À partir de la classe `Noeud`, écrivez les fonctions suivantes : `longueur(tete)`, `inserer_en_tete(tete, valeur)`, `inserer_en_queue(tete, valeur)`, `supprimer(tete, valeur)` (première occurrence), `vers_liste(tete)` (liste Python des valeurs).

**Exercice 3.3.2**

Écrivez une version **récursive** de `inverser(tete)`.

**Exercice 3.3.3**

Écrivez `milieu(tete)` qui renvoie le nœud du milieu en un seul parcours.

**Exercice 3.3.4**

Écrivez `fusionner(a, b)` qui fusionne deux listes chaînées triées en une liste chaînée triée.

**Exercice 3.3.5** *(défi)*

Écrivez `supprimer_nieme_depuis_la_fin(tete, n)` en un seul parcours.

## 3.4 Tas et file de priorité

**Exercice 3.4.1**

Écrivez `k_plus_grands(t, k)` qui renvoie les `k` plus grands éléments d'une liste avec un tas-min de taille `k`. Quelle est la complexité en fonction de `n` et `k` ?

**Exercice 3.4.2**

Implémentez une classe `TasMax` à l'aide de `heapq` (astuce de l'opposé) avec `inserer`, `extraire_max` et `max`.

**Exercice 3.4.3**

Fusionnez `k` listes triées en une seule liste triée avec un tas. Quelle est la complexité ?

**Exercice 3.4.4** *(défi)*

Maintenez la médiane d'un flux d'entiers avec deux tas. Écrivez une classe `Mediane` avec `ajouter(x)` et `valeur()`.

**Exercice 3.4.5**

Simulez à la main l'insertion successive de `5, 3, 8, 1, 9, 2` dans un tas-min, puis les trois premières extractions. Dessinez le tas après chaque opération.

## 3.5 Arbres

**Exercice 3.5.1**

Pour l'arbre binaire suivant, donnez les parcours préfixe, infixe, suffixe et en largeur :

```text
         8
       /   \
      3     10
     / \      \
    1   6      14
       / \    /
      4   7  13
```

**Exercice 3.5.2**

Écrivez les parcours préfixe, suffixe et en largeur (avec une `deque`) sur la classe `NoeudArbre`.

**Exercice 3.5.3**

Écrivez `hauteur(n)`, `nombre_noeuds(n)` et `nombre_feuilles(n)` pour un arbre binaire.

**Exercice 3.5.4**

Implémentez l'insertion et la recherche dans un arbre binaire de recherche. Quelle est la hauteur obtenue en insérant `1, 2, 3, 4, 5` dans cet ordre ? Qu'en conclure ?

**Exercice 3.5.5**

Écrivez `est_abr(n)` qui vérifie qu'un arbre binaire est un arbre binaire de recherche valide. Piège à éviter : comparer uniquement avec les enfants directs.

## 3.6 Choisir la bonne structure

**Exercice 3.6.1**

Pour chaque besoin, choisissez la structure la plus adaptée et justifiez :

1. Annuler la dernière action dans un éditeur de texte.
2. Parcourir un graphe en largeur.
3. Compter les mots d'un texte.
4. Toujours traiter la tâche la plus urgente en premier.
5. Maintenir une liste triée avec de nombreuses insertions.
6. Autocompléter une saisie à partir d'un dictionnaire.
7. Tester rapidement si un élément a déjà été vu.

---

# 4. Récursivité de base

## 4.1 Qu'est-ce que la récursivité ?

**Exercice 4.1.1**

Écrivez de manière récursive : `somme(n)` (somme des entiers de 1 à `n`), `compte_a_rebours(n)` (affiche `n, n−1, …, 1`), `longueur(t)` (longueur d'une liste sans `len`).

**Exercice 4.1.2**

Donnez une définition récursive (cas de base et relation de récurrence) de : la somme des chiffres d'un entier, le nombre de `1` dans l'écriture binaire d'un entier, et le maximum d'une liste.

## 4.2 Structure d'une fonction récursive

**Exercice 4.2.1**

Pour chaque fonction, identifiez le cas de base, l'appel récursif et la quantité qui décroît :

```python
def a(n):
    if n <= 1:
        return 1
    return n * a(n - 1)

def b(t):
    if not t:
        return 0
    return t[0] + b(t[1:])

def c(x, y):
    if y == 0:
        return x
    return c(y, x % y)
```

**Exercice 4.2.2**

Écrivez `puissance(x, n)` de manière récursive pour `n ≥ 0`. Donnez le cas de base, la relation de récurrence, et la complexité.

## 4.3 Fonctionnement : la pile d'appels

**Exercice 4.3.1**

Dessinez l'état de la pile d'appels, à chaque étape, pour `factorielle(4)`, puis écrivez l'ordre dans lequel les valeurs sont renvoyées.

**Exercice 4.3.2**

Quelle est la profondeur maximale de la pile pour `somme(n)` de l'exercice 4.1.1 ? Pour quelles valeurs de `n` obtient-on une `RecursionError` en Python ? Comment consulter et modifier la limite ?

## 4.4 Erreurs courantes

**Exercice 4.4.1**

Trouvez l'erreur de chacune des fonctions suivantes et corrigez-la :

```python
def f1(n):
    return n * f1(n - 1)

def f2(n):
    if n == 0:
        return 0
    return f2(n + 1)

def f3(t):
    if len(t) == 1:
        return t[0]
    return max(t[0], f3(t))

def f4(n):
    if n == 0:
        return 1
    return f4(n - 1) + f4(n - 1)
```

**Exercice 4.4.2**

Expliquez pourquoi la fonction `f4` ci-dessus est inutilement lente, et donnez sa complexité.

## 4.5 Exemples classiques

**Exercice 4.5.1**

Écrivez `fib(n)` de manière récursive naïve. Dessinez l'arbre d'appels pour `fib(5)` et comptez le nombre total d'appels.

**Exercice 4.5.2**

Corrigez `fib` par mémoïsation de trois manières : avec un dictionnaire, avec `functools.cache`, et en passant un paramètre `memo`. Comparez les temps pour `n = 35`.

**Exercice 4.5.3**

Écrivez de manière récursive : l'inversion d'une chaîne, un test de palindrome, la somme des chiffres d'un entier, le PGCD de deux entiers.

**Exercice 4.5.4**

Écrivez `hanoi(n, source, cible, auxiliaire)` qui affiche les déplacements. Combien de déplacements pour `n = 5` ? Pour `n` quelconque ?

**Exercice 4.5.5**

Écrivez la puissance rapide récursive (`x**n` en O(log n) multiplications). Combien de multiplications pour `n = 1000` ?

**Exercice 4.5.6**

Écrivez une recherche binaire récursive dans un tableau trié.

**Exercice 4.5.7**

Écrivez une fonction `aplatir(t)` qui aplatit une liste de listes imbriquées à profondeur arbitraire : `aplatir([1, [2, [3, 4]], 5])` doit donner `[1, 2, 3, 4, 5]`.

## 4.6 Récursivité ou itération ?

**Exercice 4.6.1**

Convertissez en version itérative : la factorielle, Fibonacci en O(n) temps et O(1) espace, la somme d'une liste.

**Exercice 4.6.2**

Convertissez en version récursive : le PGCD itératif d'Euclide, le calcul de `2**n` par boucle.

**Exercice 4.6.3**

Comparez les complexités en espace d'une version récursive et d'une version itérative de la factorielle.

## 4.7 Quand l'utiliser ?

**Exercice 4.7.1**

Pour chaque problème, dites si une solution récursive est naturelle ou si une boucle suffit : somme d'une liste, parcours d'un arbre, calcul de toutes les permutations, parcours d'une liste chaînée, calcul de `n!`, exploration d'un labyrinthe.

---

# 5. Algorithmes de tri simples

## 5.1 Introduction

**Exercice 5.1.1**

Définissez : tri **stable**, tri **en place**, tri **par comparaisons**. Donnez un exemple de liste de tuples `(nom, âge)` qui montre la différence entre un tri stable et un tri instable lorsqu'on trie sur l'âge.

**Exercice 5.1.2**

Écrivez une fonction `est_trie(t)` qui indique si une liste est triée par ordre croissant, et une fonction `est_stable(avant, apres, cle)` qui vérifie qu'un tri a préservé l'ordre relatif des éléments de même clé.

## 5.2 Tri à bulles (*Bubble Sort*)

**Exercice 5.2.1**

Déroulez à la main le tri à bulles sur `[5, 1, 4, 2, 8]` : écrivez l'état de la liste après chaque passage.

**Exercice 5.2.2**

Implémentez le tri à bulles avec arrêt anticipé (si aucun échange n'a eu lieu pendant un passage). Quelle est la complexité dans le meilleur cas ?

**Exercice 5.2.3**

Modifiez votre implémentation pour qu'elle renvoie le nombre d'échanges effectués. Quel lien y a-t-il avec le nombre d'inversions de la liste ?

**Exercice 5.2.4**

Écrivez une version qui trie par ordre **décroissant**, puis une version qui trie une liste de chaînes selon leur longueur.

## 5.3 Tri par sélection (*Selection Sort*)

**Exercice 5.3.1**

Déroulez à la main le tri par sélection sur `[64, 25, 12, 22, 11]` et notez le minimum choisi à chaque étape.

**Exercice 5.3.2**

Implémentez le tri par sélection. Combien de comparaisons effectue-t-il pour une liste de `n` éléments, quelle que soit sa disposition initiale ? Combien d'échanges au maximum ?

**Exercice 5.3.3**

Montrez par un exemple que le tri par sélection (version avec échanges) n'est pas stable.

## 5.4 Tri par insertion (*Insertion Sort*)

**Exercice 5.4.1**

Déroulez à la main le tri par insertion sur `[12, 11, 13, 5, 6]`.

**Exercice 5.4.2**

Implémentez le tri par insertion. Combien de décalages effectue-t-il sur une liste déjà triée ? Sur une liste triée par ordre décroissant ?

**Exercice 5.4.3**

Écrivez une version qui trie des tuples `(nom, âge)` par âge en restant stable, puis vérifiez la stabilité avec la fonction `est_stable` de l'exercice 5.1.2.

**Exercice 5.4.4**

Réécrivez le tri par insertion en utilisant `bisect.insort` pour trouver la position d'insertion. La complexité totale change-t-elle ?

## 5.5 Comparaison

**Exercice 5.5.1**

Complétez le tableau :

| Tri | Meilleur | Moyen | Pire | Stable | En place |
| --- | --- | --- | --- | --- | --- |
| Bulles | | | | | |
| Sélection | | | | | |
| Insertion | | | | | |

**Exercice 5.5.2**

Chronométrez les trois tris sur des listes aléatoires de tailles `10²`, `10³`, `5 × 10³`, puis sur des listes déjà triées et inversées. Commentez les résultats.

**Exercice 5.5.3**

Quel tri simple choisiriez-vous pour une liste presque triée ? Pour minimiser le nombre d'écritures en mémoire ? Justifiez.

**Exercice 5.5.4**

Écrivez une fonction `inversions(t)` en O(n²) qui compte le nombre de paires `(i, j)` avec `i < j` et `t[i] > t[j]`.

---

# 6. Algorithmes de recherche

## 6.1 Recherche linéaire

**Exercice 6.1.1**

Écrivez `chercher(t, x)` qui renvoie l'indice de la première occurrence de `x` ou `-1`.

**Exercice 6.1.2**

Écrivez `toutes_positions(t, x)` qui renvoie la liste de tous les indices où `x` apparaît, puis `derniere_position(t, x)`.

**Exercice 6.1.3**

Écrivez `chercher_avec_condition(t, predicat)` qui renvoie le premier élément vérifiant un prédicat (par exemple « premier nombre pair supérieur à 10 »).

## 6.2 Recherche binaire (dichotomique)

**Exercice 6.2.1**

Déroulez à la main la recherche binaire de `11`, puis de `4`, dans `[1, 3, 5, 7, 9, 11, 13]`. Notez `bas`, `haut` et `milieu` à chaque étape.

**Exercice 6.2.2**

Implémentez la recherche binaire de manière itérative, puis récursive.

**Exercice 6.2.3**

Quel est le nombre maximal de comparaisons pour une liste de 1 000 éléments ? De 10⁶ éléments ?

**Exercice 6.2.4**

Pourquoi la recherche binaire exige-t-elle un tableau trié ? Donnez un exemple de tableau non trié où l'algorithme échoue.

### Variantes : première / dernière position, insertion

**Exercice 6.2.5**

Écrivez `premiere_position(t, x)` et `derniere_position(t, x)` en O(log n) pour un tableau trié avec doublons. En déduire `compter(t, x)`.

**Exercice 6.2.6**

Écrivez `position_insertion(t, x)` : l'indice où insérer `x` pour garder le tableau trié. Comparez avec `bisect.bisect_left` et `bisect.bisect_right`.

**Exercice 6.2.7**

Dans un tableau trié, écrivez `plus_petit_superieur(t, x)` : le plus petit élément strictement supérieur à `x`, ou `None`.

## 6.3 Comparaison

**Exercice 6.3.1**

On doit effectuer une seule recherche dans un tableau non trié de `n` éléments, puis `q` recherches sur le même tableau. Pour quelles valeurs de `q` vaut-il la peine de trier d'abord ?

**Exercice 6.3.2**

Un tableau trié a été « tourné » : `[6, 7, 8, 1, 2, 3, 4, 5]`. Adaptez la recherche binaire pour y chercher un élément en O(log n). *(défi)*

---

# 7. Algorithmes mathématiques de base

## 7.1 PGCD (algorithme d'Euclide)

**Exercice 7.1.1**

Déroulez à la main l'algorithme d'Euclide pour `pgcd(252, 105)` et pour `pgcd(17, 5)`.

**Exercice 7.1.2**

Implémentez `pgcd(a, b)` de manière itérative, puis `ppcm(a, b)` à partir du PGCD.

**Exercice 7.1.3**

Écrivez `simplifier(num, den)` qui renvoie une fraction irréductible. Écrivez ensuite l'addition de deux fractions renvoyant une fraction irréductible.

**Exercice 7.1.4**

Écrivez `pgcd_liste(t)` qui calcule le PGCD de tous les éléments d'une liste.

**Exercice 7.1.5** *(défi)*

Implémentez l'algorithme d'Euclide étendu : `euclide_etendu(a, b)` renvoie `(g, x, y)` tels que `a·x + b·y = g`.

## 7.2 Nombres premiers : test naïf

**Exercice 7.2.1**

Écrivez `est_premier(n)` en testant les diviseurs jusqu'à `√n`. Expliquez pourquoi il suffit de s'arrêter à `√n`.

**Exercice 7.2.2**

Affichez tous les nombres premiers inférieurs à 100, puis donnez la complexité du calcul des premiers inférieurs à `N` avec cette méthode.

**Exercice 7.2.3**

Écrivez `n_ieme_premier(n)` et `premier_suivant(n)`.

**Exercice 7.2.4**

Trouvez deux nombres premiers jumeaux (différence de 2) supérieurs à 1000.

## 7.3 Factorielle

**Exercice 7.3.1**

Écrivez `factorielle(n)` de manière itérative et vérifiez-la avec `math.factorial`.

**Exercice 7.3.2**

Combien de zéros terminent l'écriture décimale de `100!` ? Écrivez une fonction `zeros_terminaux(n)` qui le calcule sans calculer `n!`.

**Exercice 7.3.3**

Combien de chiffres comporte `1000!` ? Calculez-le à l'aide de Python, puis à l'aide de la somme des logarithmes décimaux.

## 7.4 Suite de Fibonacci

**Exercice 7.4.1**

Écrivez `fib(n)` en O(n) temps et O(1) espace. Affichez les 15 premiers termes.

**Exercice 7.4.2**

Calculez la somme des termes pairs de la suite de Fibonacci qui ne dépassent pas 4 000 000.

**Exercice 7.4.3**

Quel est le plus petit indice `n` tel que `fib(n)` possède 100 chiffres ?

**Exercice 7.4.4**

Montrez, en calculant les premiers termes, que `fib(n)` est pair exactement quand `n` est multiple de 3. Vérifiez numériquement sur les 50 premiers termes.

## 7.5 Autres outils intégrés à Python *(ajout)*

**Exercice 7.5.1**

Sans écrire de boucle, utilisez les outils de la bibliothèque standard pour calculer :

1. le nombre de manières de choisir 3 éléments parmi 10 ;
2. le nombre d'arrangements de 4 éléments parmi 8 ;
3. le quotient et le reste de la division de 1000 par 37 ;
4. les trois derniers chiffres de `7¹⁰⁰` ;
5. l'écriture binaire de 255 et la valeur décimale de `"101101"` ;
6. la somme des chiffres de `2¹⁰⁰⁰`.

**Exercice 7.5.2**

Écrivez `est_carre_parfait(n)` à l'aide de `math.isqrt`, sans utiliser de nombres flottants. Pourquoi `int(n ** 0.5) ** 2 == n` est-il risqué pour de grands `n` ?

---

# Niveau intermédiaire

---

# 8. Algorithmes de tri avancés

## 8.1 Vue d'ensemble

**Exercice 8.1.1**

Complétez le tableau de synthèse :

| Tri | Meilleur | Moyen | Pire | Espace | Stable |
| --- | --- | --- | --- | --- | --- |
| Fusion | | | | | |
| Rapide | | | | | |
| Tas | | | | | |
| Comptage | | | | | |
| Radix | | | | | |

**Exercice 8.1.2**

Un tri par comparaisons ne peut pas faire mieux que `Ω(n log n)` dans le pire cas. Justifiez en comptant le nombre de permutations possibles d'une liste de `n` éléments et en utilisant l'arbre de décision.

## 8.2 Tri fusion (*Merge Sort*)

**Exercice 8.2.1**

Déroulez à la main le tri fusion sur `[38, 27, 43, 3, 9, 82, 10]` : dessinez l'arbre des divisions puis celui des fusions.

**Exercice 8.2.2**

Implémentez `fusionner(a, b)` qui fusionne deux listes triées, puis `tri_fusion(t)`.

**Exercice 8.2.3**

Pourquoi la fusion préserve-t-elle la stabilité ? Quelle condition faut-il respecter lors de la comparaison de deux éléments égaux ?

**Exercice 8.2.4** *(défi)*

Modifiez le tri fusion pour qu'il compte le nombre d'inversions d'un tableau en O(n log n).

**Exercice 8.2.5**

Écrivez une version itérative (ascendante) du tri fusion qui fusionne des blocs de taille 1, 2, 4, 8…

## 8.3 Tri rapide (*Quick Sort*)

**Exercice 8.3.1**

Déroulez à la main le tri rapide sur `[10, 80, 30, 90, 40, 50, 70]` avec le dernier élément comme pivot (partition de Lomuto).

**Exercice 8.3.2**

Implémentez le tri rapide fonctionnel (avec listes `gauche`, `milieu`, `droite`), puis sa version en place avec la partition de Lomuto.

**Exercice 8.3.3**

Implémentez un pivot choisi au hasard. Pourquoi cela rend-il le pire cas très improbable ?

**Exercice 8.3.4**

Comparez le nombre d'appels récursifs de votre tri rapide (pivot = premier élément) sur une liste triée de 1000 éléments et sur une liste mélangée.

**Exercice 8.3.5** *(défi)*

Implémentez la partition en trois parties (`< pivot`, `= pivot`, `> pivot`) pour traiter efficacement les listes contenant beaucoup de doublons.

**Exercice 8.3.6**

Limitez la profondeur de récursion à O(log n) en traitant récursivement la plus petite partition et itérativement la plus grande.

## 8.4 Tri par tas (*Heap Sort*)

**Exercice 8.4.1**

Écrivez un tri par tas avec `heapq` (poussez tous les éléments, puis extrayez). Quelle est la complexité en temps et en espace ?

**Exercice 8.4.2**

Construisez à la main un tas-max à partir de `[4, 10, 3, 5, 1]` (construction ascendante), puis déroulez les extractions successives.

**Exercice 8.4.3** *(défi)*

Écrivez la version **en place** du tri par tas avec les fonctions `sift_down` et `construire_tas`.

## 8.5 Tri par comptage (*Counting Sort*)

**Exercice 8.5.1**

Implémentez le tri par comptage pour des entiers compris entre `0` et `k`. Quelle est la complexité en fonction de `n` et `k` ?

**Exercice 8.5.2**

Adaptez-le pour gérer des entiers négatifs.

**Exercice 8.5.3**

Écrivez une version **stable** (avec tableau de comptages cumulés) qui trie des couples `(clé, valeur)` selon la clé. Pourquoi la stabilité est-elle indispensable pour le tri radix ?

**Exercice 8.5.4**

Pour quels types de données le tri par comptage n'est-il pas adapté ? Donnez deux exemples.

## 8.6 Tri radix (par base)

**Exercice 8.6.1**

Déroulez à la main le tri radix (base 10, chiffres de droite à gauche) sur `[170, 45, 75, 90, 802, 24, 2, 66]`.

**Exercice 8.6.2**

Implémentez le tri radix pour des entiers positifs. Quelle est la complexité en fonction de `n`, du nombre de chiffres `d` et de la base `b` ?

**Exercice 8.6.3**

Adaptez-le au tri de chaînes de même longueur.

## 8.7 Timsort et tri en Python *(à jour, ajout)*

**Exercice 8.7.1**

Triez la liste `[("Alice", 30), ("Bob", 25), ("Chloé", 30), ("David", 25)]` : par âge croissant, par âge décroissant puis par nom croissant, et par nom décroissant, en n'utilisant que `sorted` et `key`.

**Exercice 8.7.2**

Triez une liste de chaînes par longueur croissante, puis par ordre alphabétique en cas d'égalité, sans comparateur personnalisé.

**Exercice 8.7.3**

Expliquez comment la stabilité de `sorted` permet de trier en deux passes (d'abord sur la clé secondaire, puis sur la clé principale) pour obtenir un tri multi-critères.

**Exercice 8.7.4**

Chronométrez `sorted` sur une liste aléatoire, une liste déjà triée et une liste presque triée de `10⁶` éléments. Que constatez-vous ?

## 8.8 Quel tri choisir ?

**Exercice 8.8.1**

Pour chaque situation, choisissez un tri et justifiez : tri d'une liste de 15 éléments, tri de 10⁷ entiers compris entre 0 et 1000, tri d'un fichier de 100 Go, tri d'objets en conservant l'ordre d'origine des égalités, tri avec une mémoire très limitée et un pire cas garanti.

---

# 9. Diviser pour régner

## 9.1 Principe

**Exercice 9.1.1**

Pour chacun des problèmes suivants, décrivez les trois phases (diviser, résoudre, combiner) : tri fusion, recherche binaire, calcul de `xⁿ`, comptage des inversions.

**Exercice 9.1.2**

Quelles conditions doit remplir un problème pour être résolu efficacement par « diviser pour régner » ? Donnez un exemple où cette approche n'apporte rien.

## 9.2 Exemple : maximum d'une liste

**Exercice 9.2.1**

Écrivez `maximum_dc(t, g, d)` par diviser pour régner. Écrivez la récurrence et résolvez-la. Gagne-t-on par rapport à la version itérative ?

**Exercice 9.2.2**

Écrivez `min_et_max(t)` qui renvoie le minimum et le maximum en effectuant environ `3n/2` comparaisons (au lieu de `2n`).

## 9.3 Exemple : sous-tableau de somme maximale

**Exercice 9.3.1**

Calculez à la main le sous-tableau de somme maximale de `[-2, 1, -3, 4, -1, 2, 1, -5, 4]` par diviser pour régner : pour chaque niveau, donnez le meilleur sous-tableau à gauche, à droite et à cheval sur le milieu.

**Exercice 9.3.2**

Implémentez la méthode diviser pour régner et la force brute O(n²). Comparez leurs résultats sur des tableaux aléatoires.

**Exercice 9.3.3**

Quelle est la complexité de la version diviser pour régner ? Quel algorithme linéaire connaissez-vous pour ce problème (voir la section 18) ?

## 9.4 Quickselect : le k-ième plus petit élément

**Exercice 9.4.1**

Implémentez `quickselect(t, k)` renvoyant le `k`-ième plus petit élément (indexé à partir de 0).

**Exercice 9.4.2**

Quelle est la complexité en moyenne et au pire ? Donnez une entrée de pire cas pour un pivot choisi comme premier élément.

**Exercice 9.4.3**

Utilisez `quickselect` pour calculer la médiane d'une liste de taille impaire, puis d'une liste de taille paire.

## 9.5 Le théorème maître

**Exercice 9.5.1**

Donnez la complexité de chacune des récurrences à l'aide du théorème maître :

1. `T(n) = 4T(n/2) + n`
2. `T(n) = 2T(n/2) + n²`
3. `T(n) = 2T(n/2) + n`
4. `T(n) = T(n/2) + 1`
5. `T(n) = 8T(n/2) + n²`
6. `T(n) = 9T(n/3) + n`
7. `T(n) = 3T(n/4) + n`

**Exercice 9.5.2**

Pour chacune, précisez à quel cas du théorème (feuilles dominantes, équilibre, racine dominante) elle appartient.

**Exercice 9.5.3**

Écrivez la récurrence de la recherche binaire, du tri fusion et de la multiplication naïve de deux entiers de `n` chiffres découpés en deux moitiés (4 sous-multiplications). Résolvez-les.

## 9.6 Multiplication de matrices (Strassen)

**Exercice 9.6.1**

Combien de multiplications scalaires la multiplication naïve de deux matrices `n × n` effectue-t-elle ? Écrivez la récurrence obtenue en découpant chaque matrice en 4 blocs et en effectuant 8 multiplications de blocs.

**Exercice 9.6.2**

Strassen réduit à 7 le nombre de multiplications de blocs. Écrivez la récurrence correspondante et donnez l'exposant de la complexité.

**Exercice 9.6.3**

Implémentez la multiplication naïve de matrices en Python, puis l'approche récursive par blocs pour des matrices de taille puissance de 2.

---

# 10. Algorithmes gloutons

## 10.1 Principe

**Exercice 10.1.1**

Décrivez en deux phrases la stratégie gloutonne. Donnez trois exemples de problèmes de la vie courante où l'on applique naturellement un choix glouton.

## 10.2 Quand fonctionne-t-il ?

**Exercice 10.2.1**

Trouvez un système de pièces et un montant pour lesquels l'algorithme glouton de rendu de monnaie échoue (différent de celui du cours), et donnez la solution optimale.

**Exercice 10.2.2**

Pourquoi le système `[1, 2, 5, 10, 20, 50, 100, 200]` est-il « canonique » ? Vérifiez expérimentalement, avec un programme comparant glouton et programmation dynamique, pour tous les montants jusqu'à 500.

**Exercice 10.2.3**

Quelles deux propriétés (choix glouton, sous-structure optimale) doit vérifier un problème pour qu'un algorithme glouton soit correct ? Expliquez chacune avec un exemple.

## 10.3 Cadre général

**Exercice 10.3.1**

Complétez le cadre général (définir les candidats, trier selon un critère, choisir si faisable, mettre à jour) pour le problème : « Choisir un nombre maximal de fichiers à copier sur une clé USB de capacité C, connaissant la taille de chaque fichier. »

## 10.4 Sélection d'activités (*Activity Selection*)

**Exercice 10.4.1**

Appliquez à la main l'algorithme de sélection d'activités sur `[(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]`.

**Exercice 10.4.2**

Implémentez `selection_activites(intervalles)`. Donnez la complexité.

**Exercice 10.4.3**

Montrez par un contre-exemple que trier par **durée croissante** ou par **date de début** ne donne pas toujours l'optimum.

**Exercice 10.4.4**

Planifiez le nombre minimal de salles nécessaires pour tenir toutes les réunions d'une liste d'intervalles (indice : trier les débuts et les fins).

## 10.5 Sac à dos fractionnaire

**Exercice 10.5.1**

Soit les objets `(valeur, poids)` : `(60, 10)`, `(100, 20)`, `(120, 30)` et une capacité de 50. Calculez à la main la valeur maximale pour le sac à dos fractionnaire, puis pour le sac à dos 0/1 (par énumération).

**Exercice 10.5.2**

Implémentez `sac_fractionnaire(objets, capacite)`. Quelle est la complexité ?

**Exercice 10.5.3**

Pourquoi le glouton par rapport `valeur/poids` n'est-il pas optimal pour le sac à dos 0/1 ? Donnez un contre-exemple.

## 10.6 Codage de Huffman

**Exercice 10.6.1**

On donne les fréquences : `a:45`, `b:13`, `c:12`, `d:16`, `e:9`, `f:5`. Construisez à la main l'arbre de Huffman en notant chaque fusion, puis donnez le code de chaque lettre.

**Exercice 10.6.2**

Calculez la longueur totale du texte encodé (en bits) pour 100 caractères avec ces fréquences, et comparez à un code de longueur fixe.

**Exercice 10.6.3**

Implémentez la construction de l'arbre de Huffman avec `heapq`, la génération de la table de codes, l'encodage et le décodage d'une chaîne.

**Exercice 10.6.4**

Pourquoi un code de Huffman est-il un code **préfixe** ? Que se passerait-il si ce n'était pas le cas ?

## 10.7 Autres exemples gloutons

**Exercice 10.7.1**

Cinq tâches ont pour durées `[3, 1, 4, 2, 5]`. Dans quel ordre les traiter pour minimiser la somme des temps d'attente ? Calculez cette somme et comparez avec l'ordre initial.

**Exercice 10.7.2**

Ordonnancement avec échéances : on donne des tâches `(profit, échéance)` de durée unitaire ; écrivez un algorithme glouton maximisant le profit total.

**Exercice 10.7.3**

Un voyageur peut parcourir `d` kilomètres avec un plein et doit traverser une route avec des stations à des positions données. Écrivez un algorithme glouton qui minimise le nombre d'arrêts.

**Exercice 10.7.4**

Rendu de monnaie : écrivez la version gloutonne et la version par programmation dynamique, et trouvez par un programme un système de 3 pièces dont le glouton n'est pas optimal.

## 10.8 Glouton ou programmation dynamique ?

**Exercice 10.8.1**

Pour chaque problème, dites si le glouton suffit ou si la programmation dynamique est nécessaire, en justifiant : sac à dos fractionnaire, sac à dos 0/1, sélection d'activités, plus longue sous-séquence commune, rendu de monnaie (système quelconque), arbre couvrant minimal.

---

# 11. Retour sur trace (*backtracking*)

## 11.1 Principe

**Exercice 11.1.1**

Expliquez en quelques phrases la différence entre la force brute et le retour sur trace. Qu'est-ce que l'**élagage** ?

**Exercice 11.1.2**

Dessinez l'arbre d'exploration pour le choix de 2 éléments parmi `{1, 2, 3}` (avec ordre croissant imposé), en marquant les branches élaguées.

## 11.2 Schéma général

**Exercice 11.2.1**

Écrivez le schéma général d'un retour sur trace (choisir, explorer, annuler) sous forme de pseudo-code, puis adaptez-le pour énumérer tous les mots binaires de longueur `n`.

**Exercice 11.2.2**

Écrivez un retour sur trace qui énumère tous les mots de longueur `n` sur l'alphabet `{a, b, c}` sans deux lettres identiques consécutives.

## 11.3 Exemple : sous-ensembles et permutations

**Exercice 11.3.1**

Écrivez `sous_ensembles(t)` par retour sur trace. Combien de sous-ensembles pour `n = 10` ? Retrouvez le résultat avec `itertools`.

**Exercice 11.3.2**

Écrivez `permutations(t)` par retour sur trace. Combien d'appels récursifs pour `n = 4` ?

**Exercice 11.3.3**

Écrivez `combinaisons(t, k)` qui renvoie toutes les combinaisons de `k` éléments. Comparez avec `itertools.combinations`.

**Exercice 11.3.4**

Écrivez `permutations_uniques(t)` pour une liste contenant des doublons (par exemple `[1, 1, 2]`), sans générer deux fois la même permutation.

**Exercice 11.3.5**

Écrivez `sous_ensembles_somme(t, cible)` : tous les sous-ensembles dont la somme vaut `cible`, avec élagage (les éléments sont positifs).

**Exercice 11.3.6**

Générez toutes les chaînes de `n` paires de parenthèses bien formées. Combien y en a-t-il pour `n = 4` ?

## 11.4 Problème des N reines

**Exercice 11.4.1**

Pour `n = 4`, déroulez à la main le retour sur trace (ligne par ligne) et trouvez les solutions.

**Exercice 11.4.2**

Implémentez `n_reines(n)` qui renvoie toutes les solutions, puis le nombre de solutions pour `n = 1` à `8`.

**Exercice 11.4.3**

Optimisez le test de conflit en O(1) avec trois ensembles (colonnes, diagonales, anti-diagonales).

**Exercice 11.4.4**

Combien de solutions pour `n = 8` ? Combien d'entre elles sont distinctes à rotation et symétrie près ? *(défi)*

## 11.5 Solveur de Sudoku

**Exercice 11.5.1**

Écrivez `est_valide(grille, ligne, colonne, valeur)` pour une grille 9×9.

**Exercice 11.5.2**

Écrivez un solveur de Sudoku par retour sur trace. Testez-le sur une grille de votre choix et mesurez le nombre de retours en arrière.

**Exercice 11.5.3**

Améliorez-le avec l'heuristique « case la plus contrainte d'abord » (celle qui a le moins de valeurs possibles). Quel gain observez-vous ?

## 11.6 Autres problèmes classiques

**Exercice 11.6.1**

Rat dans un labyrinthe : écrivez un programme qui trouve un chemin du coin supérieur gauche au coin inférieur droit d'une grille de 0 (libre) et 1 (mur).

**Exercice 11.6.2**

Coloration de graphe : écrivez `colorier(graphe, k)` qui cherche une coloration avec `k` couleurs.

**Exercice 11.6.3**

Somme de sous-ensemble : déterminez s'il existe un sous-ensemble de `[3, 34, 4, 12, 5, 2]` dont la somme vaut 9.

**Exercice 11.6.4**

Chemin hamiltonien : écrivez un retour sur trace qui cherche un chemin passant exactement une fois par chaque sommet d'un graphe.

**Exercice 11.6.5**

Recherche de mots dans une grille : étant donné une grille de lettres et un mot, déterminez si le mot s'écrit en se déplaçant de case en case (voisines horizontalement ou verticalement), sans réutiliser une case.

**Exercice 11.6.6** *(défi)*

Parcours du cavalier : écrivez un programme qui trouve un tour complet sur un échiquier 6×6 avec l'heuristique de Warnsdorff.

## 11.7 Complexité et comparaison

**Exercice 11.7.1**

Donnez la complexité dans le pire cas pour : énumérer les sous-ensembles, énumérer les permutations, résoudre les `n` reines naïvement. Expliquez pourquoi l'élagage ne change pas le pire cas.

**Exercice 11.7.2**

Ajoutez de la mémoïsation au problème de la somme de sous-ensemble (état `(indice, reste)`). Que devient la complexité ? Quel nom donne-t-on alors à la technique ?

**Exercice 11.7.3**

Remplissez le tableau comparatif (exploration, retour en arrière, sous-problèmes répétés, optimalité) pour retour sur trace, glouton et programmation dynamique, sans consulter le cours.

---

# 12. Technique des deux pointeurs

## 12.1 Principe

**Exercice 12.1.1**

Décrivez les deux grandes variantes de la technique (pointeurs aux extrémités, pointeurs rapide et lent). Donnez un problème pour chaque variante.

## 12.2 Somme de deux nombres dans un tableau trié

**Exercice 12.2.1**

Écrivez `deux_somme_trie(t, cible)` qui renvoie un couple d'indices `(i, j)` avec `i < j` tels que `t[i] + t[j] == cible`, en O(n) temps et O(1) espace.

**Exercice 12.2.2**

Déroulez à la main votre algorithme sur `t = [1, 3, 4, 6, 8, 11]` et `cible = 10`, puis `cible = 20`.

**Exercice 12.2.3**

Justifiez la correction : pourquoi peut-on écarter un des deux pointeurs lorsque la somme est trop grande ou trop petite ?

**Exercice 12.2.4**

Adaptez l'algorithme pour compter le nombre de paires distinctes de somme `cible` dans un tableau trié avec doublons.

## 12.3 Autres exemples

**Exercice 12.3.1**

Écrivez `est_palindrome(s)` qui ignore la casse et les caractères non alphanumériques. Testez : `"A man, a plan, a canal: Panama"`.

**Exercice 12.3.2**

Écrivez `supprimer_doublons_tries(t)` en place, qui renvoie la nouvelle longueur.

**Exercice 12.3.3**

Écrivez `trois_somme(t)` qui renvoie tous les triplets distincts de somme nulle. Quelle est la complexité ?

**Exercice 12.3.4**

Écrivez `aire_max_conteneur(h)` (« Container With Most Water »). Pourquoi déplacer le pointeur sur la plus petite hauteur est-il correct ?

**Exercice 12.3.5**

Écrivez `fusion_triee(a, b)` qui fusionne deux tableaux triés avec deux pointeurs, puis `intersection_triee(a, b)`.

**Exercice 12.3.6**

Écrivez `deplacer_zeros(t)` qui déplace tous les zéros à la fin en conservant l'ordre des autres éléments, en place.

**Exercice 12.3.7**

Écrivez `trier_couleurs(t)` qui trie en place un tableau ne contenant que des 0, des 1 et des 2, en un seul parcours (drapeau hollandais, trois pointeurs).

### Détection de cycle (lièvre et tortue de Floyd)

**Exercice 12.3.8**

Écrivez `a_un_cycle(tete)`. Pourquoi les deux pointeurs finissent-ils par se rencontrer s'il y a un cycle ?

**Exercice 12.3.9** *(défi)*

Écrivez `debut_du_cycle(tete)` qui renvoie le premier nœud du cycle, ou `None`.

**Exercice 12.3.10**

Détectez un doublon dans un tableau de `n + 1` entiers compris entre `1` et `n` en O(1) espace en interprétant le tableau comme une liste chaînée. *(défi)*

## 12.4 Quand l'utiliser ?

**Exercice 12.4.1**

Pour chaque énoncé, dites si les deux pointeurs conviennent : chercher une paire de somme donnée dans un tableau non trié, dans un tableau trié, trouver le milieu d'une liste chaînée, trouver le plus long sous-tableau de somme nulle avec des valeurs négatives, vérifier un palindrome.

---

# 13. Fenêtre glissante

## 13.1 Principe

**Exercice 13.1.1**

Distinguez fenêtre de taille fixe et fenêtre de taille variable. Que maintient-on d'une itération à l'autre pour éviter de tout recalculer ?

## 13.2 Taille fixe : somme maximale de `k` éléments consécutifs

**Exercice 13.2.1**

Écrivez `somme_max_k(t, k)` en O(n). Testez sur `[2, 1, 5, 1, 3, 2]` avec `k = 3`.

**Exercice 13.2.2**

Écrivez `moyennes_glissantes(t, k)` qui renvoie la moyenne de chaque fenêtre de taille `k`.

**Exercice 13.2.3**

Combien de voyelles contient au maximum une sous-chaîne de longueur `k` d'une chaîne donnée ?

## 13.3 Taille variable : plus longue sous-chaîne sans répétition

**Exercice 13.3.1**

Écrivez `plus_longue_sans_repetition(s)`. Testez : `"abcabcbb"`, `"bbbbb"`, `"pwwkew"`, `""`.

**Exercice 13.3.2**

Déroulez votre algorithme sur `"abcabcbb"` en notant la fenêtre `[gauche, droite]` à chaque étape.

**Exercice 13.3.3**

Quelle est la complexité ? Pourquoi est-elle linéaire alors que le pointeur gauche avance dans une boucle imbriquée ?

## 13.4 Taille variable : plus petit sous-tableau de somme ≥ S (valeurs positives)

**Exercice 13.4.1**

Écrivez `plus_petit_sous_tableau(t, S)` renvoyant la longueur minimale, ou 0 s'il n'existe pas. Testez sur `[2, 3, 1, 2, 4, 3]` avec `S = 7`.

**Exercice 13.4.2**

Pourquoi la fenêtre glissante échoue-t-elle si le tableau contient des valeurs négatives ? Donnez un contre-exemple.

## 13.5 Maximum de chaque fenêtre : file monotone *(ajout)*

**Exercice 13.5.1**

Écrivez `maximum_fenetres(t, k)` en O(n) avec une `deque` qui stocke des indices à valeurs décroissantes. Testez sur `[1, 3, -1, -3, 5, 3, 6, 7]` avec `k = 3`.

**Exercice 13.5.2**

Expliquez pourquoi chaque élément est inséré et retiré au plus une fois. Adaptez l'algorithme pour calculer le **minimum** de chaque fenêtre.

## 13.6 Autres problèmes classiques

**Exercice 13.6.1**

Trouvez toutes les positions de départ des anagrammes d'un motif `p` dans un texte `s` (fenêtre de taille fixe et compteurs).

**Exercice 13.6.2**

Écrivez `plus_long_avec_k_distincts(t, k)` : la longueur du plus long sous-tableau contenant au plus `k` valeurs distinctes.

**Exercice 13.6.3**

Écrivez `fenetre_minimale(s, t)` : la plus petite sous-chaîne de `s` contenant tous les caractères de `t` (avec multiplicité). *(défi)*

**Exercice 13.6.4**

Fruits dans des paniers : un tableau représente des arbres, chacun portant un type de fruit ; deux paniers acceptent chacun un seul type. Trouvez la plus longue suite d'arbres consécutifs cueillables.

**Exercice 13.6.5**

Plus longue sous-chaîne avec remplacement : on peut remplacer au plus `k` caractères ; quelle est la plus longue sous-chaîne composée d'un même caractère ?

---

# 14. Sommes préfixes et tableaux de différences

## 14.1 Sommes préfixes

**Exercice 14.1.1**

Écrivez `prefixes(t)` qui renvoie le tableau `P` de longueur `n + 1` avec `P[0] = 0`, puis `somme_intervalle(P, l, r)` en O(1) pour la somme de `t[l..r]` (bornes incluses).

**Exercice 14.1.2**

Pour `t = [3, 1, 4, 1, 5, 9, 2, 6]`, calculez à la main `P` puis les sommes des intervalles `[0, 3]`, `[2, 5]` et `[4, 7]`.

**Exercice 14.1.3**

On répond à `q = 10⁵` requêtes sur un tableau de taille `10⁵`. Comparez le coût total avec et sans sommes préfixes.

**Exercice 14.1.4**

Calculez l'indice d'équilibre d'un tableau : un indice `i` tel que la somme des éléments à gauche est égale à celle des éléments à droite.

**Exercice 14.1.5**

Écrivez `produit_sauf_soi(t)` : pour chaque indice, le produit de tous les autres éléments, sans division, en O(n) (préfixes et suffixes de produits).

### Sous-tableaux de somme `k` (avec valeurs négatives possibles)

**Exercice 14.1.6**

Écrivez `nombre_sous_tableaux_somme(t, k)` avec un dictionnaire de fréquences de préfixes. Testez sur `[1, 2, 3, -2, 5]` avec `k = 3`.

**Exercice 14.1.7**

Écrivez `plus_long_sous_tableau_somme_nulle(t)` en O(n).

**Exercice 14.1.8**

Comptez le nombre de sous-tableaux dont la somme est divisible par `k`. *(défi)*

### Version 2D

**Exercice 14.1.9**

Écrivez `prefixes_2d(grille)` et `somme_rectangle(P, r1, c1, r2, c2)` en O(1). Écrivez la formule d'inclusion-exclusion utilisée.

**Exercice 14.1.10**

Trouvez le carré de côté `k` de somme maximale dans une grille.

## 14.2 Tableau de différences

**Exercice 14.2.1**

Écrivez `appliquer_mises_a_jour(n, mises_a_jour)` où chaque mise à jour `(l, r, v)` ajoute `v` à `t[l..r]`, en O(n + q). Testez avec `n = 5` et les mises à jour `(1, 3, 2)`, `(2, 4, 3)`, `(0, 1, -1)`.

**Exercice 14.2.2**

Expliquez le lien entre le tableau de différences et les sommes préfixes (opération réciproque).

**Exercice 14.2.3**

Covoiturage : une voiture de capacité `C` effectue des trajets `(passagers, départ, arrivée)`. Déterminez si tous les trajets peuvent être effectués.

**Exercice 14.2.4**

Écrivez la version 2D du tableau de différences pour ajouter une valeur à un rectangle, et appliquez-la à une liste de rectangles.

## 14.3 Applications

**Exercice 14.3.1**

Pour une chaîne de `10⁵` lettres, répondez à `10⁵` requêtes « combien de fois la lettre `c` apparaît-elle dans `[l, r]` ? » à l'aide de 26 tableaux de préfixes.

**Exercice 14.3.2**

Pour chaque application, indiquez la technique la plus adaptée (préfixes, différences, ou préfixes + dictionnaire) : moyenne d'un intervalle, réservations qui se chevauchent, sous-tableau de somme `k`, dessin de rectangles sur une grille, nombre d'occurrences d'une lettre dans un intervalle.

**Exercice 14.3.3**

Si le tableau est modifié entre les requêtes, les sommes préfixes ne suffisent plus. Quelle structure du chapitre 23 utiliser ? Quel est le coût d'une mise à jour avec les sommes préfixes ?

---

# 15. Recherche binaire sur la réponse

## 15.1 Principe

**Exercice 15.1.1**

Qu'est-ce qu'une fonction de décision monotone ? Donnez un exemple de problème dont la fonction de décision est monotone et un exemple où elle ne l'est pas.

## 15.2 Modèle : plus petite valeur valide

**Exercice 15.2.1**

Écrivez le modèle générique `plus_petite_valeur(bas, haut, est_valide)` qui renvoie la plus petite valeur `x` de `[bas, haut]` telle que `est_valide(x)` est vrai, en supposant que `est_valide` est faux puis vrai.

**Exercice 15.2.2**

Utilisez-le pour calculer la racine carrée entière `⌊√n⌋` sans fonction mathématique.

**Exercice 15.2.3**

« Première mauvaise version » : les versions `1..n` sont bonnes jusqu'à une version à partir de laquelle toutes sont mauvaises. Trouvez la première mauvaise version avec le moins d'appels possible à `est_mauvaise(v)`.

## 15.3 Exemple : expédier des colis en D jours

**Exercice 15.3.1**

Des colis de poids `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` doivent être expédiés dans l'ordre en 5 jours. Quelle est la capacité minimale du bateau ? Écrivez la fonction de décision, puis la recherche binaire.

**Exercice 15.3.2**

Quelles bornes choisir pour `bas` et `haut` ? Justifiez chacune.

**Exercice 15.3.3**

Quelle est la complexité en fonction de `n` (nombre de colis) et de la somme des poids `S` ?

## 15.4 Exemple : vitesse minimale pour manger toutes les bananes

**Exercice 15.4.1**

Des piles de bananes `[3, 6, 7, 11]` doivent être mangées en `H = 8` heures, à raison d'une pile par heure au plus (on mange `k` bananes par heure dans une seule pile). Quelle est la vitesse minimale `k` ? Écrivez la solution.

**Exercice 15.4.2**

Diviser un tableau en `m` sous-tableaux contigus de façon à minimiser la plus grande somme parmi les sous-tableaux : écrivez la solution par recherche binaire sur la réponse.

## 15.5 Schémas fréquents

**Exercice 15.5.1**

Pour chaque problème, dites s'il faut chercher à gauche ou à droite quand la valeur testée est valide :

1. minimiser la capacité maximale d'un camion ;
2. maximiser la distance minimale entre des vaches placées dans des stalles ;
3. la plus petite durée pour terminer des tâches ;
4. la plus grande longueur de ruban coupée en `k` morceaux égaux.

**Exercice 15.5.2**

Placer `c` vaches dans des stalles aux positions `[1, 2, 8, 4, 9]` de manière à maximiser la plus petite distance entre deux vaches (`c = 3`). Écrivez la solution.

**Exercice 15.5.3**

Des ouvriers doivent peindre `n` planches de longueurs données, chaque ouvrier peignant une suite contiguë ; minimisez le temps total pour `k` ouvriers.

## 15.6 Réels : recherche binaire flottante

**Exercice 15.6.1**

Calculez `∛x` par recherche binaire flottante avec un nombre fixe d'itérations. Combien d'itérations faut-il pour une précision de `10⁻⁹` sur `[0, 1000]` ?

**Exercice 15.6.2**

Pourquoi préfère-t-on un nombre fixe d'itérations à une condition `haut - bas > eps` ? Donnez un cas où la seconde peut boucler indéfiniment.

## 15.7 Conseils

**Exercice 15.7.1**

Trouvez les trois erreurs de cette recherche binaire sur la réponse et corrigez-les :

```python
def plus_petite_capacite(poids, jours):
    bas, haut = 0, sum(poids)
    while bas < haut:
        milieu = (bas + haut) // 2
        if est_valide(milieu):
            bas = milieu
        else:
            haut = milieu - 1
    return bas
```

**Exercice 15.7.2**

Listez les quatre vérifications à faire avant d'appliquer une recherche binaire sur la réponse.

---

# 16. Algorithmes de théorie des nombres

## 16.1 Crible d'Ératosthène

**Exercice 16.1.1**

Déroulez à la main le crible d'Ératosthène pour `N = 50`. Quels nombres sont barrés à chaque étape ?

**Exercice 16.1.2**

Implémentez `crible(N)` qui renvoie la liste des nombres premiers `≤ N`. Quelle est la complexité en temps et en espace ?

**Exercice 16.1.3**

Pourquoi peut-on commencer le marquage des multiples de `p` à `p²` ?

**Exercice 16.1.4**

Combien de nombres premiers y a-t-il en dessous de 10⁶ ? Vérifiez avec votre crible et comparez avec l'approximation `N / ln N`.

**Exercice 16.1.5** *(défi)*

Implémentez un crible segmenté qui liste les nombres premiers dans l'intervalle `[L, R]` pour `R` jusqu'à 10¹² et `R − L ≤ 10⁶`.

## 16.2 Factorisation

**Exercice 16.2.1**

Écrivez `factoriser(n)` par divisions successives. Factorisez `360`, `97`, `1001`.

**Exercice 16.2.2**

Construisez un tableau `plus_petit_facteur` par crible, puis factorisez en O(log n) un nombre inférieur à `N`.

**Exercice 16.2.3**

Écrivez `nombre_de_diviseurs(n)` et `somme_des_diviseurs(n)` à partir de la décomposition en facteurs premiers. Calculez-les pour `360`.

**Exercice 16.2.4**

Combien de diviseurs possède `10!` ? Quel est le plus petit entier ayant exactement 12 diviseurs ?

## 16.3 Arithmétique modulaire

**Exercice 16.3.1**

Calculez à la main `(123456789 × 987654321) mod 1000` en utilisant les propriétés de la congruence, puis vérifiez avec Python.

### Exponentiation rapide : `a^b mod m` en O(log b)

**Exercice 16.3.2**

Implémentez `puissance_mod(a, b, m)` sans utiliser `pow`. Déroulez-la à la main pour `3^13 mod 7`.

**Exercice 16.3.3**

Calculez le dernier chiffre de `7^(10^9)` sans calculer la puissance. *(défi)*

### Inverse modulaire

**Exercice 16.3.4**

Calculez à la main l'inverse de 3 modulo 11 et de 7 modulo 26.

**Exercice 16.3.5**

Implémentez l'inverse modulaire de deux manières : avec l'algorithme d'Euclide étendu, et avec le petit théorème de Fermat pour un modulo premier. Comparez avec `pow(a, -1, m)`.

**Exercice 16.3.6**

Quand l'inverse de `a` modulo `m` n'existe-t-il pas ? Donnez un exemple.

### Binôme de Newton modulo un premier

**Exercice 16.3.7**

Calculez `C(n, k) mod p` pour `n ≤ 10⁶` et `p = 10⁹ + 7` avec des tableaux de factorielles et d'inverses de factorielles.

**Exercice 16.3.8**

Calculez le nombre de chemins dans une grille `m × n` (déplacements droite et bas uniquement) modulo `10⁹ + 7`.

## 16.4 Autres outils

**Exercice 16.4.1**

Calculez `φ(36)`, `φ(97)` et `φ(100)` à la main, puis avec la fonction `phi` du cours. Vérifiez le théorème d'Euler pour `a = 7`, `m = 10`.

**Exercice 16.4.2**

Théorème des restes chinois : résolvez le système `x ≡ 2 (mod 3)`, `x ≡ 3 (mod 5)`, `x ≡ 2 (mod 7)`. Écrivez un programme générique pour deux congruences à modules premiers entre eux.

**Exercice 16.4.3**

Calculez `fib(10¹⁸) mod (10⁹ + 7)` par exponentiation de matrices. Quelle est la complexité ?

**Exercice 16.4.4**

Calculez les nombres de Catalan `C₀` à `C₁₀` par la formule `Cₙ = C(2n, n) / (n + 1)`. Combien y a-t-il de façons de parenthéser correctement 5 paires de parenthèses ?

## 16.5 Test de primalité de Miller-Rabin *(ajout)*

**Exercice 16.5.1**

Écrivez `n − 1 = 2ˢ · d` avec `d` impair pour `n = 561`, `n = 97` et `n = 1009`.

**Exercice 16.5.2**

Expliquez pourquoi 561 (nombre de Carmichael) trompe le test de Fermat mais pas Miller-Rabin.

**Exercice 16.5.3**

Implémentez Miller-Rabin avec un ensemble de témoins déterministes pour `n < 3 × 10¹⁸`. Testez-le sur des nombres premiers connus (`10⁹ + 7`, `998244353`) et sur des composés (`561`, `10⁹ + 1`).

**Exercice 16.5.4**

Quelle est la probabilité d'erreur du test probabiliste avec `k` témoins aléatoires ? Quelle valeur de `k` choisir pour descendre sous `2⁻⁶⁴` ?

---

# 17. Hachage

## 17.1 Principe

**Exercice 17.1.1**

Qu'est-ce qu'une fonction de hachage ? Quelles propriétés doit-elle posséder pour être utilisable dans une table de hachage ?

**Exercice 17.1.2**

Soit la fonction de hachage `h(mot) = somme des codes ASCII mod 7`. Calculez `h` pour `"chat"`, `"chien"`, `"rat"` et `"tac"`. Que remarquez-vous ?

## 17.2 Les structures en Python

**Exercice 17.2.1**

Quels types peuvent servir de clé de dictionnaire ? Expliquez pourquoi `{[1, 2]: "a"}` provoque une erreur et proposez une correction.

**Exercice 17.2.2**

Écrivez un programme qui calcule l'union, l'intersection, la différence et la différence symétrique de deux ensembles d'entiers, d'abord avec des opérateurs, puis avec des boucles et un dictionnaire.

**Exercice 17.2.3**

Écrivez `frequences(s)` qui renvoie le dictionnaire des occurrences de chaque caractère d'une chaîne, sans utiliser `Counter`.

## 17.3 Gestion des collisions

**Exercice 17.3.1**

On insère les clés `10, 22, 31, 4, 15, 28, 17, 88, 59` dans une table de taille 11 avec `h(k) = k mod 11`. Dessinez la table obtenue avec le chaînage séparé, puis avec le sondage linéaire.

**Exercice 17.3.2**

Implémentez une table de hachage avec chaînage séparé (`inserer`, `chercher`, `supprimer`) et redimensionnement lorsque le facteur de charge dépasse 0,75.

**Exercice 17.3.3**

Pourquoi la suppression est-elle plus délicate avec l'adressage ouvert ? Quelle technique (marqueurs de suppression) utilise-t-on ?

## 17.4 Complexité

**Exercice 17.4.1**

Quelle est la complexité moyenne et la complexité au pire des opérations d'une table de hachage ? Donnez une situation où l'on atteint le pire cas.

**Exercice 17.4.2**

Définissez le facteur de charge. Comment évolue le coût moyen d'une recherche en fonction de celui-ci pour le chaînage ?

## 17.5 Problèmes classiques

### Deux sommes

**Exercice 17.5.1**

Écrivez `deux_sommes(t, cible)` en O(n) avec un dictionnaire (valeur → indice). Testez sur `[2, 7, 11, 15]` avec `cible = 9`.

**Exercice 17.5.2**

Écrivez `quatre_sommes_comptage(a, b, c, d)` qui compte les quadruplets `(i, j, k, l)` avec `a[i] + b[j] + c[k] + d[l] == 0` en O(n²). *(défi)*

### Regrouper les anagrammes

**Exercice 17.5.3**

Écrivez `regrouper_anagrammes(mots)`. Testez sur `["eat", "tea", "tan", "ate", "nat", "bat"]`. Proposez deux clés possibles (mot trié, tuple de comptages) et comparez leurs coûts.

### Plus longue suite consécutive

**Exercice 17.5.4**

Écrivez `plus_longue_suite(t)` : la longueur de la plus longue suite d'entiers consécutifs (par exemple `[100, 4, 200, 1, 3, 2]` donne 4), en O(n).

### Autres

**Exercice 17.5.5**

Écrivez `premier_caractere_unique(s)` et `contient_doublon(t)`.

**Exercice 17.5.6**

Deux chaînes `s` et `t` sont isomorphes si l'on peut remplacer les caractères de `s` pour obtenir `t` (même correspondance, sans fusion de deux caractères distincts). Écrivez le test avec deux dictionnaires.

**Exercice 17.5.7**

Détectez un cycle dans un graphe orienté à l'aide d'un ensemble des sommets visités, ou dans une séquence de nombres (par exemple la suite des sommes des carrés des chiffres d'un nombre : « nombre heureux »).

## 17.6 Outils du module `collections`

**Exercice 17.6.1**

Avec `Counter`, trouvez les trois mots les plus fréquents d'un texte et le nombre d'occurrences de chacun.

**Exercice 17.6.2**

Avec `defaultdict(list)`, construisez un index inversé : pour chaque mot, la liste des numéros de lignes où il apparaît.

**Exercice 17.6.3**

Avec `frozenset`, regroupez des ensembles égaux dans un dictionnaire. Pourquoi `set` ne peut-il pas être une clé ?

## 17.7 Hachage d'objets et autres usages

**Exercice 17.7.1**

Définissez une classe `Point` utilisable comme clé de dictionnaire, avec `__eq__` et `__hash__` cohérents. Que se passe-t-il si l'on définit `__eq__` sans `__hash__` ?

**Exercice 17.7.2**

Calculez les empreintes SHA-256 de deux chaînes qui ne diffèrent que d'un caractère avec `hashlib`. Que constatez-vous ? Pourquoi ne faut-il pas utiliser SHA-256 seul pour stocker des mots de passe ?

**Exercice 17.7.3** *(défi)*

Implémentez un filtre de Bloom avec `m` bits et `k` fonctions de hachage. Quelles erreurs peut-il commettre : faux positifs, faux négatifs, ou les deux ?

## 17.8 Bonnes pratiques

**Exercice 17.8.1**

Trouvez les problèmes dans le code suivant et corrigez-le :

```python
cache = {}
def traiter(point):
    if point in cache:
        return cache[point]
    resultat = calcul_long(point)
    cache[point] = resultat
    return resultat

traiter([1, 2])
```

**Exercice 17.8.2**

Pourquoi ne faut-il pas s'appuyer sur l'ordre d'itération d'un `set` ? Quelle est la garantie offerte par `dict` ?

---

# Niveau avancé

---

# 18. Programmation dynamique

## 18.1 Principe

**Exercice 18.1.1**

Dessinez l'arbre d'appels de `fib(6)` et repérez les sous-problèmes qui se répètent. Combien de fois `fib(2)` est-il calculé ?

**Exercice 18.1.2**

Distinguez les deux propriétés nécessaires à la programmation dynamique : sous-structure optimale et sous-problèmes qui se chevauchent. Donnez un problème qui a la première mais pas la seconde.

## 18.2 Démarche en 5 étapes

**Exercice 18.2.1**

Montée d'escaliers : on peut monter 1 ou 2 marches à la fois. Combien de façons de monter `n` marches ? Appliquez les cinq étapes (état, transition, cas de base, ordre de calcul, réponse), puis codez la solution.

**Exercice 18.2.2**

Même question avec des pas de 1, 2 ou 3 marches, puis avec des marches interdites (une liste d'indices que l'on ne peut pas toucher).

**Exercice 18.2.3**

Énoncez pour chacun des problèmes suivants l'état `dp[...]` et la transition, sans coder : plus longue sous-suite croissante, sac à dos 0/1, distance d'édition.

## 18.3 Descendante (mémoïsation) ou ascendante (tabulation)

**Exercice 18.3.1**

Implémentez la suite de Tribonacci (`T(n) = T(n−1) + T(n−2) + T(n−3)`, `T(0) = 0`, `T(1) = T(2) = 1`) en descendante, en ascendante avec tableau, puis en ascendante avec mémoire O(1).

**Exercice 18.3.2**

Comparez les avantages et inconvénients de la descendante et de l'ascendante (profondeur de récursion, nombre de sous-problèmes calculés, optimisation de mémoire).

**Exercice 18.3.3**

Pourquoi `functools.cache` est-il pratique mais parfois insuffisant (limite de récursion, mémoire) ? Quelle solution adopter pour `n = 10⁵` ?

## 18.4 Problèmes 1D

### Rendu de monnaie (minimum de pièces)

**Exercice 18.4.1**

Écrivez `monnaie_min(pieces, montant)` qui renvoie le nombre minimal de pièces, ou `-1` si c'est impossible. Testez avec `[1, 3, 4]` et `6`, puis `[2]` et `3`.

**Exercice 18.4.2**

Modifiez-la pour renvoyer la liste des pièces utilisées.

**Exercice 18.4.3**

Écrivez `nombre_de_facons(pieces, montant)` qui compte les façons distinctes de former le montant (l'ordre des pièces ne compte pas). Que se passe-t-il si l'on permute les deux boucles ?

### Voleur de maisons (*House Robber*)

**Exercice 18.4.4**

Écrivez `voleur(t)` : montant maximal volé sans prendre deux maisons adjacentes. Testez avec `[2, 7, 9, 3, 1]`.

**Exercice 18.4.5**

Variante circulaire : la première et la dernière maison sont voisines. Adaptez votre solution.

### Sous-tableau de somme maximale (Kadane)

**Exercice 18.4.6**

Écrivez `kadane(t)` en O(n). Testez avec `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`.

**Exercice 18.4.7**

Modifiez-le pour renvoyer aussi les bornes du sous-tableau, puis pour gérer un tableau ne contenant que des valeurs négatives.

**Exercice 18.4.8**

Sous-tableau de produit maximal : adaptez Kadane en gardant à la fois le produit maximal et minimal en cours. *(défi)*

### Plus longue sous-suite croissante (LIS)

**Exercice 18.4.9**

Écrivez `lis_quadratique(t)` en O(n²). Testez avec `[10, 9, 2, 5, 3, 7, 101, 18]`.

**Exercice 18.4.10**

Écrivez `lis_rapide(t)` en O(n log n) avec `bisect`. Pourquoi le tableau auxiliaire n'est-il pas forcément une sous-suite valide ?

**Exercice 18.4.11**

Reconstituez une plus longue sous-suite croissante (et pas seulement sa longueur).

## 18.5 Problèmes 2D

### Sac à dos 0/1

**Exercice 18.5.1**

Remplissez à la main le tableau DP du sac à dos 0/1 pour les objets `(valeur, poids)` : `(1, 1)`, `(4, 3)`, `(5, 4)`, `(7, 5)` et une capacité de 7.

**Exercice 18.5.2**

Implémentez `sac_a_dos(objets, capacite)` en O(n · C), puis optimisez la mémoire à un tableau 1D (attention au sens de parcours des capacités).

**Exercice 18.5.3**

Partition en deux sous-ensembles de même somme : écrivez `partition_egale(t)`.

**Exercice 18.5.4**

Pourquoi O(n · C) n'est-il pas un temps polynomial au sens strict ? Quel nom donne-t-on à cette complexité ?

### Plus longue sous-séquence commune (LCS)

**Exercice 18.5.5**

Remplissez à la main le tableau LCS pour `"AGGTAB"` et `"GXTXAYB"`.

**Exercice 18.5.6**

Écrivez `lcs(a, b)` renvoyant la longueur, puis `lcs_texte(a, b)` renvoyant une sous-séquence commune la plus longue par remontée dans le tableau.

**Exercice 18.5.7**

Écrivez `plus_longue_sous_chaine_commune(a, b)` (sous-chaîne contiguë, et non plus sous-séquence).

### Distance d'édition (Levenshtein)

**Exercice 18.5.8**

Calculez à la main la distance d'édition entre `"kitten"` et `"sitting"` en remplissant le tableau.

**Exercice 18.5.9**

Implémentez `distance_edition(a, b)`, puis optimisez la mémoire à deux lignes. Écrivez enfin la liste des opérations à effectuer.

**Exercice 18.5.10**

Écrivez un correcteur orthographique simple : pour un mot donné, renvoyer les mots d'un dictionnaire à distance d'édition minimale.

### Chemins dans une grille

**Exercice 18.5.11**

Écrivez `chemins(m, n)` : nombre de chemins du coin supérieur gauche au coin inférieur droit avec déplacements droite / bas.

**Exercice 18.5.12**

Même question avec des obstacles dans la grille, puis calculez le chemin de **coût minimal** pour une grille de coûts.

### Autres classiques

**Exercice 18.5.13**

Écrivez un programme pour chacun des problèmes suivants :

1. plus longue sous-chaîne palindromique ;
2. découpage de tige (prix par longueur, longueur totale `n`) ;
3. plus grand carré composé uniquement de 1 dans une grille binaire ;
4. produit de chaînes de matrices (coût minimal de multiplication) ;
5. nombre de façons de décoder une chaîne de chiffres (`"12"` : `"AB"` ou `"L"`).

**Exercice 18.5.14**

Sur l'arbre binaire de votre choix, calculez par DP sur les arbres le poids maximal d'un ensemble de sommets sans deux sommets adjacents (ensemble indépendant de poids maximal).

**Exercice 18.5.15** *(défi)*

DP par chiffres : combien d'entiers de `1` à `N` ne contiennent pas le chiffre `4` ?

## 18.6 DP avec masque de bits

**Exercice 18.6.1**

Pour un ensemble de 4 éléments, listez les masques de `0000` à `1111` et le sous-ensemble correspondant. Écrivez des fonctions : tester si `i ∈ S`, ajouter `i`, retirer `i`, compter les éléments, énumérer les sous-ensembles d'un masque.

### Voyageur de commerce (TSP)

**Exercice 18.6.2**

Résolvez à la main le TSP pour 4 villes avec la matrice de distances :

```text
      0   1   2   3
  0   0  10  15  20
  1  10   0  35  25
  2  15  35   0  30
  3  20  25  30   0
```

**Exercice 18.6.3**

Implémentez `tsp(distances)` avec `dp[masque][dernier]`. Quelles sont les complexités en temps et en espace ? Jusqu'à quel `n` est-ce praticable ?

**Exercice 18.6.4**

Affectation de tâches : `n` ouvriers, `n` tâches, une matrice de coûts. Trouvez l'affectation de coût minimal par DP sur les masques.

## 18.7 Reconstituer la solution

**Exercice 18.7.1**

Pour chacun des problèmes suivants, ajoutez une structure de « parents » (ou une remontée dans le tableau) afin de reconstituer une solution optimale : rendu de monnaie, sac à dos 0/1, LCS, plus court chemin dans une grille.

## 18.8 Conseils

**Exercice 18.8.1**

Pour chaque problème, définissez l'état, la transition, les cas de base et la complexité :

1. « Mots les plus longs » : la plus longue chaîne de mots où chacun s'obtient du précédent en ajoutant une lettre.
2. Nombre de façons d'atteindre la somme `S` avec `n` dés à `f` faces.
3. Gain maximal en achetant et vendant une action avec au plus `k` transactions.

**Exercice 18.8.2**

Dans quels cas doit-on essayer la programmation dynamique ? Dans quels cas un algorithme glouton ou une recherche binaire sont-ils plus adaptés ?

---

# 19. Algorithmes sur les graphes

## 19.1 Représentation

**Exercice 19.1.1**

Pour le graphe non orienté ayant les arêtes `(0,1), (0,2), (1,2), (1,3), (3,4)` (5 sommets), donnez la liste d'adjacence, la matrice d'adjacence et le degré de chaque sommet.

**Exercice 19.1.2**

Écrivez `construire_graphe(n, aretes, oriente=False)` qui construit une liste d'adjacence, puis une version pondérée où chaque entrée contient `(voisin, poids)`.

**Exercice 19.1.3**

Comparez liste et matrice d'adjacence en espace, en test d'existence d'une arête et en parcours des voisins. Pour quelle densité de graphe la matrice est-elle préférable ?

**Exercice 19.1.4**

Écrivez `degres(graphe)` pour un graphe orienté (degré entrant et sortant de chaque sommet). Vérifiez que la somme des degrés sortants vaut le nombre d'arêtes.

## 19.2 Parcours en largeur (BFS)

**Exercice 19.2.1**

Déroulez à la main un BFS depuis le sommet 0 sur le graphe de l'exercice 19.1.1, en notant le contenu de la file à chaque étape.

**Exercice 19.2.2**

Implémentez `bfs(graphe, source)` qui renvoie la liste des distances (en nombre d'arêtes) depuis `source`, ou `-1` pour les sommets inaccessibles.

**Exercice 19.2.3**

Modifiez-le pour reconstituer un plus court chemin entre deux sommets (tableau des parents).

**Exercice 19.2.4**

Labyrinthe : dans une grille de `0` (libre) et `1` (mur), trouvez la longueur du plus court chemin entre deux cases avec des déplacements dans 4 directions, puis dans 8 directions.

**Exercice 19.2.5**

Orange pourrie : dans une grille, certaines oranges sont pourries et contaminent leurs voisines chaque minute. En combien de minutes toutes les oranges sont-elles pourries (ou `-1`) ? *(BFS multi-sources)*

**Exercice 19.2.6**

Échelle de mots : transformez un mot en un autre en changeant une lettre à la fois, chaque mot intermédiaire devant appartenir à un dictionnaire. Trouvez la plus courte séquence.

## 19.3 Parcours en profondeur (DFS)

**Exercice 19.3.1**

Déroulez à la main un DFS depuis le sommet 0 sur le graphe de l'exercice 19.1.1, avec les voisins parcourus dans l'ordre croissant. Notez l'ordre de visite.

**Exercice 19.3.2**

Écrivez `dfs_recursif` et `dfs_iteratif` (avec une pile explicite). Pourquoi la version itérative est-elle préférable pour un graphe de 10⁶ sommets en Python ?

**Exercice 19.3.3**

Écrivez `composantes_connexes(graphe)` qui renvoie la liste des composantes d'un graphe non orienté.

### Applications

**Exercice 19.3.4**

Nombre d'îles : dans une grille de `'1'` (terre) et `'0'` (eau), comptez les îles. Calculez aussi l'aire de la plus grande.

**Exercice 19.3.5**

Détection de cycle dans un graphe non orienté, puis dans un graphe orienté (trois états : non visité, en cours, terminé).

**Exercice 19.3.6**

Test de bipartition : écrivez `est_biparti(graphe)` par coloration à deux couleurs avec DFS ou BFS.

**Exercice 19.3.7**

Trouvez tous les chemins entre deux sommets d'un DAG.

**Exercice 19.3.8**

Clonage de graphe : écrivez une fonction qui copie en profondeur un graphe représenté par des nœuds avec une liste de voisins.

## 19.4 Tri topologique (graphes orientés acycliques)

**Exercice 19.4.1**

Donnez deux tris topologiques valides pour le DAG d'arêtes `5→2, 5→0, 4→0, 4→1, 2→3, 3→1` (6 sommets).

**Exercice 19.4.2**

Implémentez le tri topologique de deux manières : par DFS (ordre inverse des sorties) et par l'algorithme de Kahn (degrés entrants).

**Exercice 19.4.3**

Cours à suivre : `n` cours, des prérequis `(a, b)` signifiant « suivre `b` avant `a` ». Déterminez s'il est possible de tous les suivre, et dans quel ordre.

**Exercice 19.4.4**

Comment détecter un cycle avec l'algorithme de Kahn ? Quelle est la complexité ?

**Exercice 19.4.5**

Ordre alphabétique d'un langage extraterrestre : étant donné une liste de mots triés dans cet ordre, reconstituez un ordre possible de l'alphabet. *(défi)*

## 19.5 Arbre couvrant de poids minimal (MST)

### Union-Find (ensembles disjoints)

**Exercice 19.5.1**

Implémentez la structure `UnionFind` avec compression de chemins et union par rang (`trouver`, `unir`, `meme_ensemble`). Déroulez-la à la main pour les unions `(0,1), (2,3), (1,3), (4,5)` sur 6 éléments.

**Exercice 19.5.2**

Utilisez-la pour compter les composantes connexes d'un graphe donné par une liste d'arêtes, puis pour détecter la première arête qui crée un cycle.

**Exercice 19.5.3**

Comptage d'îles dynamique : des cases de terre sont ajoutées une à une dans une grille ; après chaque ajout, donnez le nombre d'îles avec Union-Find. *(défi)*

### Algorithme de Kruskal (glouton, trie les arêtes)

**Exercice 19.5.4**

Appliquez Kruskal à la main au graphe pondéré d'arêtes `(A,B,4), (A,C,3), (B,C,1), (B,D,2), (C,D,4), (C,E,2), (D,E,3)` : notez l'ordre d'examen et le poids total de l'arbre.

**Exercice 19.5.5**

Implémentez `kruskal(n, aretes)`. Quelle est la complexité ? Que renvoie-t-il si le graphe n'est pas connexe ?

### Algorithme de Prim (glouton, fait grossir un arbre)

**Exercice 19.5.6**

Appliquez Prim à la main au même graphe, en partant de `A`.

**Exercice 19.5.7**

Implémentez `prim(graphe)` avec un tas. Quand préférer Prim à Kruskal ?

**Exercice 19.5.8**

Réseau de connexions : étant donné des points du plan, reliez-les tous au coût minimal (distance de Manhattan). Comment modéliser ? Quelle complexité ?

## 19.6 Exercices recommandés

**Exercice 19.6.1**

Résolvez les cinq problèmes suivants et donnez pour chacun l'algorithme choisi et sa complexité : nombre d'îles, cours à suivre (tri topologique), clonage de graphe, plus court chemin dans une grille, réseau de connexions au coût minimal (MST).

---

# 20. Plus courts chemins dans les graphes pondérés

## 20.1 Choisir l'algorithme

**Exercice 20.1.1**

Choisissez l'algorithme (BFS, BFS 0-1, Dijkstra, Bellman-Ford, Floyd-Warshall, programmation dynamique sur DAG) pour chaque situation :

1. graphe non pondéré, source unique ;
2. poids positifs, source unique ;
3. poids pouvant être négatifs, source unique ;
4. toutes les paires de sommets, petit graphe (`n ≤ 400`) ;
5. poids égaux à 0 ou 1 ;
6. graphe orienté acyclique pondéré ;
7. détection d'un cycle de poids négatif.

## 20.2 Dijkstra

**Exercice 20.2.1**

Déroulez à la main Dijkstra depuis `A` sur le graphe orienté `A→B (7), A→C (9), A→F (14), B→C (10), B→D (15), C→D (11), C→F (2), D→E (6), F→E (9)`. Notez le tableau des distances et l'ordre d'extraction.

**Exercice 20.2.2**

Implémentez `dijkstra(graphe, source)` avec `heapq` et gestion des entrées obsolètes. Quelle est la complexité ?

**Exercice 20.2.3**

Reconstituez le plus court chemin de `A` à `E` avec un tableau des prédécesseurs.

**Exercice 20.2.4**

Donnez un contre-exemple (petit graphe avec une arête négative) pour lequel Dijkstra renvoie une distance fausse. Expliquez quelle hypothèse de la preuve est violée.

**Exercice 20.2.5**

Fiabilité de réseau : dans un réseau, la probabilité qu'un message passe par une arête est donnée ; trouvez le chemin de probabilité maximale entre deux nœuds. Comment se ramener à un plus court chemin ?

**Exercice 20.2.6**

Délai de propagation : étant donnés des temps de transmission entre nœuds, calculez le temps nécessaire pour qu'un signal émis depuis un nœud atteigne tous les autres.

## 20.3 Bellman-Ford

**Exercice 20.3.1**

Déroulez Bellman-Ford à la main sur le graphe d'arêtes `S→A (4), S→B (5), A→B (−3), B→C (4), A→C (6)`.

**Exercice 20.3.2**

Implémentez `bellman_ford(n, aretes, source)` avec détection de cycle de poids négatif. Quelle est la complexité ?

**Exercice 20.3.3**

Montrez qu'il suffit de `n − 1` relaxations de toutes les arêtes pour obtenir les distances en l'absence de cycle négatif.

**Exercice 20.3.4**

Arbitrage de devises : étant donné des taux de change, détectez une suite d'échanges qui augmente le capital. Montrez que cela équivaut à chercher un cycle négatif (avec des logarithmes). *(défi)*

**Exercice 20.3.5**

Prix le moins cher avec au plus `k` escales : modifiez Bellman-Ford pour limiter le nombre d'arêtes du chemin.

## 20.4 Floyd-Warshall

**Exercice 20.4.1**

Déroulez Floyd-Warshall à la main sur le graphe à 4 sommets de matrice (`∞` = pas d'arête) :

```text
      0   1   2   3
  0   0   5   ∞  10
  1   ∞   0   3   ∞
  2   ∞   ∞   0   1
  3   ∞   ∞   ∞   0
```

**Exercice 20.4.2**

Implémentez `floyd_warshall(distances)`. Pourquoi l'ordre des trois boucles est-il important (l'indice intermédiaire `k` doit être la boucle extérieure) ?

**Exercice 20.4.3**

Adaptez-le pour calculer la fermeture transitive d'un graphe (existence d'un chemin entre toutes les paires).

**Exercice 20.4.4**

Ville la plus proche : à partir de `n` villes et de routes pondérées, trouvez la ville qui a le moins de voisines à distance `≤ seuil` (en cas d'égalité, le plus grand indice).

**Exercice 20.4.5**

Reconstituez les chemins en conservant une matrice des « sommets suivants ».

## 20.5 BFS 0-1

**Exercice 20.5.1**

Implémentez `bfs_01(graphe, source)` avec une `deque` : les arêtes de poids 0 sont ajoutées à gauche, celles de poids 1 à droite. Quelle est la complexité ?

**Exercice 20.5.2**

Dans une grille où certaines cases contiennent des obstacles que l'on peut franchir au coût de 1 (les cases libres coûtant 0), trouvez le nombre minimal d'obstacles à franchir pour aller du coin supérieur gauche au coin inférieur droit.

## 20.6 SPFA (Bellman-Ford avec file)

**Exercice 20.6.1**

Implémentez SPFA avec une file et un tableau `dans_la_file`. Comment détecter un cycle négatif ?

**Exercice 20.6.2**

Quel est son pire cas ? Pourquoi est-il souvent rapide en pratique mais n'offre pas de garantie meilleure que Bellman-Ford ?

## 20.7 A\* *(ajout)*

**Exercice 20.7.1**

Qu'est-ce qu'une heuristique **admissible** ? **cohérente** ? Pourquoi la distance de Manhattan est-elle admissible sur une grille à déplacements dans 4 directions ?

**Exercice 20.7.2**

Implémentez A\* sur une grille avec la distance de Manhattan. Comparez le nombre de cases explorées avec Dijkstra sur plusieurs grilles aléatoires.

**Exercice 20.7.3**

Que devient A\* avec `h = 0` ? Que se passe-t-il avec une heuristique non admissible ?

**Exercice 20.7.4**

Quelle heuristique choisir si les déplacements en diagonale sont autorisés au même coût que les déplacements orthogonaux ? Et avec un coût de `√2` pour la diagonale ?

## 20.8 Plus courts chemins dans un DAG

**Exercice 20.8.1**

Écrivez `plus_court_chemin_dag(graphe, source)` : tri topologique puis relaxation dans l'ordre. Quelle est la complexité ? Fonctionne-t-il avec des poids négatifs ?

**Exercice 20.8.2**

Écrivez `plus_long_chemin_dag(graphe)` et utilisez-le pour calculer la durée minimale d'un projet dont les tâches ont des durées et des dépendances (chemin critique).

## 20.9 Conseils de choix

**Exercice 20.9.1**

Une carte routière comporte 10⁶ sommets et 3 × 10⁶ arêtes pondérées positives, et l'on doit répondre à 10³ requêtes « distance entre deux sommets ». Quel algorithme choisir ? Que changer si l'on a 10⁶ requêtes ?

**Exercice 20.9.2**

Complétez le tableau suivant :

| Algorithme | Poids négatifs ? | Complexité | Cas d'usage |
| --- | --- | --- | --- |
| BFS | | | |
| BFS 0-1 | | | |
| Dijkstra | | | |
| Bellman-Ford | | | |
| Floyd-Warshall | | | |
| A\* | | | |

---

# 21. Composantes fortement connexes

## 21.1 Définition

**Exercice 21.1.1**

Définissez « composante fortement connexe ». Pour le graphe orienté `0→1, 1→2, 2→0, 1→3, 3→4, 4→5, 5→3, 6→5, 6→7, 7→6`, listez à la main les composantes fortement connexes.

**Exercice 21.1.2**

Dessinez le graphe des composantes (condensation) du graphe précédent. Montrez qu'il est toujours acyclique.

### Applications

**Exercice 21.1.3**

Citez trois applications des composantes fortement connexes (par exemple dépendances cycliques entre modules, analyse de liens web, 2-SAT) et décrivez en une phrase ce qu'on y calcule.

## 21.2 Algorithme de Kosaraju (deux parcours)

**Exercice 21.2.1**

Déroulez Kosaraju à la main sur le graphe de l'exercice 21.1.1 : premier parcours (ordre de fin), graphe transposé, second parcours.

**Exercice 21.2.2**

Implémentez `kosaraju(graphe)` qui renvoie la liste des composantes. Quelle est la complexité ?

**Exercice 21.2.3**

Pourquoi le second parcours doit-il être effectué sur le graphe **transposé** et dans l'ordre **décroissant** des temps de fin ?

## 21.3 Algorithme de Tarjan (un seul parcours)

**Exercice 21.3.1**

Déroulez Tarjan sur le graphe de l'exercice 21.1.1 : notez, pour chaque sommet, `indice` et `bas_lien` (low-link), et l'état de la pile.

**Exercice 21.3.2**

Implémentez `tarjan(graphe)`. Quelle est la complexité en temps et en espace ?

**Exercice 21.3.3**

Quand un sommet est-il la racine d'une composante fortement connexe ? Que contient la pile à ce moment ?

## 21.4 Kosaraju ou Tarjan ?

**Exercice 21.4.1**

Comparez les deux algorithmes (nombre de parcours, graphe transposé, ordre des composantes produites, simplicité de l'implémentation).

**Exercice 21.4.2**

Étant donné un graphe orienté, déterminez le nombre minimal d'arcs à ajouter pour le rendre fortement connexe (à partir du graphe de condensation : sources et puits). *(défi)*

---

# 22. Flots dans les réseaux

## 22.1 Définition

**Exercice 22.1.1**

On donne le réseau `s→a (10), s→b (5), a→b (15), a→t (5), b→t (10)` et le flot `s→a : 8, s→b : 3, a→b : 3, a→t : 5, b→t : 6`. Vérifiez les deux contraintes (capacité et conservation du flot) et calculez la valeur du flot.

**Exercice 22.1.2**

Donnez la définition d'une **coupe** `(S, T)` et de sa capacité. Calculez la capacité de la coupe `S = {s, a}` dans le réseau précédent.

**Exercice 22.1.3**

Énoncez le théorème flot maximal / coupe minimale.

## 22.2 Réseau résiduel et arêtes inverses

**Exercice 22.2.1**

Construisez le réseau résiduel pour le flot de l'exercice 22.1.1. Trouvez un chemin augmentant s'il en existe un.

**Exercice 22.2.2**

Pourquoi faut-il ajouter des arêtes inverses ? Donnez un exemple de réseau où un algorithme glouton sans arêtes inverses est bloqué sur un flot non maximal.

## 22.3 Ford-Fulkerson et Edmonds-Karp

**Exercice 22.3.1**

Appliquez Edmonds-Karp à la main à `s→a (16), s→c (13), a→b (12), a→c (10), c→a (4), c→d (14), b→c (9), b→t (20), d→b (7), d→t (4)`. Notez chaque chemin augmentant (par BFS) et la valeur du flot après chacun.

**Exercice 22.3.2**

Implémentez Edmonds-Karp avec une liste d'adjacence d'arêtes et d'arêtes inverses. Quelle est sa complexité ? Pourquoi Ford-Fulkerson avec DFS peut-il être mal comporté sur des capacités irrationnelles ou très grandes ?

**Exercice 22.3.3**

Construisez un petit réseau de 4 sommets sur lequel Ford-Fulkerson avec un mauvais choix de chemins nécessite de très nombreuses itérations (capacités de 1000 autour d'une arête de capacité 1).

## 22.4 Dinic

**Exercice 22.4.1**

Construisez à la main le graphe de niveaux (BFS) puis un flot bloquant pour le réseau de l'exercice 22.3.1.

**Exercice 22.4.2**

Implémentez Dinic avec BFS de niveaux et DFS avec pointeurs d'arêtes courantes. Quel rôle joue le pointeur « courant » ?

**Exercice 22.4.3**

Comparez expérimentalement Edmonds-Karp et Dinic sur des réseaux aléatoires de taille croissante.

## 22.5 Complexités

**Exercice 22.5.1**

Complétez le tableau :

| Algorithme | Complexité | Remarque |
| --- | --- | --- |
| Ford-Fulkerson (DFS) | | |
| Edmonds-Karp | | |
| Dinic | | |
| Dinic sur réseau unitaire | | |
| Hopcroft-Karp (couplage biparti) | | |

## 22.6 Applications

**Exercice 22.6.1**

Couplage biparti maximum : modélisez par un flot, puis résolvez avec votre implémentation le problème suivant : 4 candidats et 4 postes ; le candidat 1 peut occuper les postes A et B, le candidat 2 les postes B et C, le candidat 3 le poste A, le candidat 4 les postes C et D.

**Exercice 22.6.2**

Coupe minimale : après un flot maximal, identifiez les sommets atteignables depuis `s` dans le réseau résiduel et listez les arêtes de la coupe minimale pour le réseau de l'exercice 22.3.1.

**Exercice 22.6.3**

Chemins disjoints : calculez le nombre maximal de chemins disjoints par les arêtes entre deux sommets d'un graphe orienté. Adaptez ensuite le modèle pour des chemins disjoints par les sommets (division des sommets).

**Exercice 22.6.4**

Affectation de tâches : `n` ouvriers, `m` tâches, chaque ouvrier peut effectuer un sous-ensemble de tâches et accepte au plus `c` tâches. Modélisez par un flot.

**Exercice 22.6.5**

Sélection de projets : chaque projet a un profit (positif ou négatif) et des dépendances. Modélisez par une coupe minimale pour maximiser le profit total. *(défi)*

**Exercice 22.6.6**

Expliquez ce qui distingue un flot à coût minimal d'un flot maximal, et pourquoi les algorithmes de flot ordinaires ne le résolvent pas directement.

---

# 23. Arbres de segments et arbres de Fenwick

## 23.1 Le problème

**Exercice 23.1.1**

On veut gérer un tableau de `n` éléments avec deux opérations : modifier un élément, et calculer la somme d'un intervalle. Donnez le coût de chaque opération avec un simple tableau, avec des sommes préfixes, puis avec un arbre de Fenwick. Pour `q` opérations mélangées, quelle solution choisir ?

## 23.2 Arbre de Fenwick (*Binary Indexed Tree*, BIT)

**Exercice 23.2.1**

Pour `n = 8`, donnez, pour chaque indice `i` de 1 à 8, la plage `(i − (i & −i), i]` couverte par `BIT[i]`.

**Exercice 23.2.2**

Implémentez `Fenwick(n)` avec `ajouter(i, delta)`, `prefixe(i)` et `somme(l, r)`. Testez sur un tableau aléatoire en comparant avec un calcul direct.

**Exercice 23.2.3**

Construisez l'arbre de Fenwick d'un tableau donné en O(n). Quelle est la complexité d'un `ajouter` et d'un `prefixe` ?

**Exercice 23.2.4**

Comptage d'inversions : écrivez `inversions(t)` en O(n log n) avec un arbre de Fenwick (après compression des valeurs).

**Exercice 23.2.5**

Rang : pour chaque élément d'un tableau, calculez le nombre d'éléments strictement plus petits situés à sa droite.

**Exercice 23.2.6**

Écrivez la recherche du `k`-ième plus petit élément dans un Fenwick de comptages (descente binaire en O(log n)). *(défi)*

## 23.3 Arbre de segments (*Segment Tree*)

**Exercice 23.3.1**

Dessinez l'arbre de segments (sommes) pour `[2, 4, 5, 7, 1, 3]` et déroulez la requête sur l'intervalle `[1, 4]` en indiquant les nœuds visités.

**Exercice 23.3.2**

Implémentez un arbre de segments avec `construire`, `modifier(i, valeur)` et `requete(l, r)` pour la somme. Quelle est la complexité de chaque opération ?

**Exercice 23.3.3**

Adaptez-le pour le **minimum** d'un intervalle, puis pour le **maximum** et sa position. Quelle propriété doit vérifier l'opération (associativité, élément neutre) ?

**Exercice 23.3.4**

Écrivez une version itérative (ascendante) de l'arbre de segments avec un tableau de taille `2n`.

**Exercice 23.3.5**

Gardez dans chaque nœud un quadruplet (somme, meilleur préfixe, meilleur suffixe, meilleur sous-tableau) pour répondre à des requêtes « sous-tableau de somme maximale dans `[l, r]` ». *(défi)*

## 23.4 Propagation paresseuse (*Lazy Propagation*)

**Exercice 23.4.1**

Pourquoi une mise à jour d'intervalle naïve (modifier chaque élément) est-elle trop lente ? Expliquez le principe de la propagation paresseuse en quelques phrases.

**Exercice 23.4.2**

Implémentez un arbre de segments avec propagation paresseuse pour : « ajouter `v` à tous les éléments de `[l, r]` » et « somme de `[l, r]` ».

**Exercice 23.4.3**

Adaptez-le pour : « affecter la valeur `v` à tous les éléments de `[l, r]` » et « somme de `[l, r]` ». Quelle différence dans la composition des étiquettes paresseuses ?

**Exercice 23.4.4**

Écrivez le cas particulier d'un arbre de Fenwick avec mise à jour d'intervalle et requête de point (via le tableau de différences).

## 23.5 Fenwick ou arbre de segments ?

**Exercice 23.5.1**

Pour chacun des besoins suivants, choisissez la structure et justifiez : somme de préfixe avec mises à jour de points, minimum d'intervalle avec mises à jour, somme d'intervalle avec ajout sur intervalle, comptage d'inversions, maximum d'intervalle statique avec de très nombreuses requêtes.

## 23.6 Applications

**Exercice 23.6.1**

Implémentez une table creuse (*sparse table*) pour le minimum d'un intervalle en O(1) après un précalcul en O(n log n).

**Exercice 23.6.2**

Décomposition en racine carrée : implémentez une structure qui supporte la mise à jour d'un point et la somme d'un intervalle en O(√n). Comparez-la au Fenwick.

**Exercice 23.6.3**

Rangs et statistiques d'ordre : maintenez un multi-ensemble d'entiers de `[1, 10⁵]` avec `ajouter(x)`, `supprimer(x)` et `kieme(k)`.

**Exercice 23.6.4**

Requêtes hors ligne : on connaît à l'avance `q` requêtes « nombre d'éléments distincts dans `[l, r]` ». Expliquez comment les trier par borne droite et utiliser un Fenwick pour y répondre en `O((n + q) log n)`. *(défi)*

---

# 24. Algorithmes sur les chaînes

## 24.1 Recherche de motif naïve

**Exercice 24.1.1**

Implémentez `recherche_naive(texte, motif)` qui renvoie toutes les positions d'occurrence. Quelle est la complexité dans le pire cas ?

**Exercice 24.1.2**

Donnez un texte et un motif de tailles `n` et `m` pour lesquels l'algorithme naïf effectue environ `n · m` comparaisons.

## 24.2 Algorithme de Knuth-Morris-Pratt (KMP)

**Exercice 24.2.1**

Calculez à la main la table des préfixes (fonction d'échec) pour les motifs `"ababaca"` et `"aabaaab"`.

**Exercice 24.2.2**

Implémentez la construction de la table puis `kmp(texte, motif)`. Déroulez la recherche de `"abab"` dans `"abababcabab"` en notant les décalages.

**Exercice 24.2.3**

Expliquez pourquoi KMP ne revient jamais en arrière dans le texte. Pourquoi la complexité est-elle O(n + m) ?

**Exercice 24.2.4**

Utilisez la table des préfixes pour trouver la plus petite période d'une chaîne (le plus petit `p` tel que la chaîne soit une répétition d'un bloc de longueur `p`).

**Exercice 24.2.5**

Déterminez si une chaîne `b` est une rotation d'une chaîne `a` en utilisant une seule recherche de motif.

## 24.3 Algorithme de Rabin-Karp

**Exercice 24.3.1**

Soit un texte composé de chiffres `"2359023141526739921"` et un motif `"31415"`. Avec une base 10 et un module 13, calculez à la main le hachage du motif puis le hachage de chaque fenêtre en utilisant la mise à jour glissante. Combien de fausses correspondances (collisions) rencontrez-vous ?

**Exercice 24.3.2**

Implémentez `rabin_karp(texte, motif)`. Pourquoi faut-il vérifier la correspondance caractère par caractère quand les hachages sont égaux ?

**Exercice 24.3.3**

Adaptez-le à la recherche **simultanée** de plusieurs motifs de même longueur.

**Exercice 24.3.4**

Détection de doublons de sous-chaînes : trouvez la plus longue sous-chaîne qui apparaît au moins deux fois dans une chaîne (recherche binaire sur la longueur + hachage). *(défi)*

**Exercice 24.3.5**

Quelle est la probabilité de collision pour un module de l'ordre de 10⁹ ? Pourquoi utilise-t-on parfois deux modules ?

## 24.4 Algorithme Z

**Exercice 24.4.1**

Calculez à la main le tableau Z de `"aabcaabxaaz"` et de `"aaaaa"`.

**Exercice 24.4.2**

Implémentez `z_algorithme(s)`, puis la recherche de motif `z_algorithme(motif + "#" + texte)`. Pourquoi le séparateur `#` est-il nécessaire ?

**Exercice 24.4.3**

Utilisez le tableau Z pour calculer le nombre de sous-chaînes distinctes d'une chaîne, ou la plus petite période d'une chaîne.

**Exercice 24.4.4**

Comptez, pour chaque préfixe d'une chaîne, combien de fois il apparaît dans la chaîne. *(défi)*

## 24.5 Trie (arbre préfixe)

**Exercice 24.5.1**

Dessinez le trie obtenu en insérant `["tea", "ten", "to", "inn", "in", "i"]` et marquez les fins de mots.

**Exercice 24.5.2**

Implémentez un `Trie` avec `inserer`, `contient`, `commence_par` et `completions`. Quelle est la complexité de chaque opération ?

**Exercice 24.5.3**

Ajoutez un compteur à chaque nœud pour répondre à « combien de mots du dictionnaire commencent par ce préfixe ? » en O(L).

**Exercice 24.5.4**

Autocomplétion : étant donné un dictionnaire avec une fréquence par mot, renvoyez les 3 mots les plus fréquents commençant par un préfixe donné.

**Exercice 24.5.5**

Recherche de mots dans une grille : étant donné une grille de lettres et une liste de mots, trouvez tous les mots présents, en utilisant un trie pour élaguer le retour sur trace. *(défi)*

**Exercice 24.5.6**

Plus grand XOR de deux nombres d'une liste : utilisez un trie binaire des écritures en bits. *(défi)*

**Exercice 24.5.7**

Routage IP : expliquez comment un trie binaire permet de trouver le préfixe le plus long correspondant à une adresse.

## 24.6 Autres outils

**Exercice 24.6.1**

Algorithme de Manacher : calculez à la main les rayons de palindromes pour `"abacaba"`. Utilisez-les pour trouver la plus longue sous-chaîne palindromique.

**Exercice 24.6.2**

Calculez à la main le tableau des suffixes et le tableau LCP de `"banana"`. Utilisez-les pour trouver la plus longue sous-chaîne répétée.

**Exercice 24.6.3**

Implémentez le hachage polynomial avec précalcul des préfixes et des puissances, afin de comparer deux sous-chaînes en O(1). Utilisez-le pour tester si deux sous-chaînes de même longueur sont égales, sur 10⁵ requêtes.

**Exercice 24.6.4**

Décrivez le fonctionnement d'Aho-Corasick sur l'ensemble de motifs `{"he", "she", "his", "hers"}` : construction du trie, liens d'échec, puis recherche dans le texte `"ushers"`. *(défi)*

**Exercice 24.6.5**

Rappelez la définition de la distance d'édition. Calculez-la pour `"intention"` et `"execution"`.

## 24.7 Comparaison des recherches de motif

**Exercice 24.7.1**

Complétez le tableau :

| Algorithme | Précalcul | Recherche | Remarque |
| --- | --- | --- | --- |
| Naïf | | | |
| KMP | | | |
| Rabin-Karp | | | |
| Z | | | |

**Exercice 24.7.2**

Pour chaque situation, choisissez l'algorithme et justifiez : un motif très court recherché une seule fois, un texte énorme avec un motif de 10⁵ caractères, la recherche de 1000 motifs simultanés, la détection de plagiat par sous-chaînes communes.

**Exercice 24.7.3**

Chronométrez `str.find`, la recherche naïve, KMP et Rabin-Karp sur un texte aléatoire de 10⁶ caractères. Commentez.

---

# 25. Aller plus loin

## 25.1 Sujets avancés et de compétition

**Exercice 25.1.1**

Pour chacun des sujets suivants, rédigez en quelques lignes une définition, puis résolvez un petit exemple à la main :

1. ancêtre commun le plus bas (LCA) dans un arbre de 7 nœuds de votre choix ;
2. enveloppe convexe d'un ensemble de 8 points (parcours de Graham) ;
3. nombres de Grundy pour le jeu de Nim à deux tas de tailles 3 et 5 ;
4. nombre de Catalan `C₅` ;
5. circuit eulérien dans un graphe de votre choix (conditions d'existence) ;
6. une instance de 2-SAT à 4 variables et sa résolution par composantes fortement connexes.

**Exercice 25.1.2**

Jeu de Nim : écrivez une fonction qui décide si le joueur qui commence gagne avec les tas donnés (XOR des tailles) et indique un coup gagnant.

**Exercice 25.1.3**

Écrivez un petit moteur de minimax avec élagage alpha-bêta pour le morpion. Comptez le nombre de positions explorées avec et sans élagage.

**Exercice 25.1.4**

Écrivez l'exponentiation de matrices et utilisez-la pour calculer le `n`-ième terme de la suite `u₀ = 0`, `u₁ = 1`, `uₙ = 3uₙ₋₁ − uₙ₋₂`, modulo `10⁹ + 7`.

**Exercice 25.1.5**

Inclusion-exclusion : combien d'entiers de `1` à `1000` ne sont divisibles ni par 2, ni par 3, ni par 5 ?

**Exercice 25.1.6**

Implémentez une transformée de Fourier rapide (FFT) ou une NTT pour multiplier deux polynômes de degré `10⁵`. Comparez avec la multiplication naïve en O(n²). *(défi)*

## 25.2 Complexité et difficulté : P, NP et au-delà *(ajout)*

**Exercice 25.2.1**

Classez chaque problème parmi P, NP-complet ou NP-difficile (sans être dans NP), et justifiez brièvement : tri, plus court chemin dans un graphe à poids positifs, SAT, voyageur de commerce (version optimisation), sac à dos (version décision), cycle hamiltonien, flot maximal, coloration d'un graphe avec 3 couleurs.

**Exercice 25.2.2**

Écrivez un **vérificateur** polynomial pour chacun des problèmes de décision suivants : somme de sous-ensemble (certificat : le sous-ensemble), cycle hamiltonien (certificat : la suite de sommets), coloration (certificat : la coloration). Quelle est la complexité de chaque vérificateur ?

**Exercice 25.2.3**

Qu'est-ce qu'une réduction polynomiale ? Décrivez une réduction du problème de l'ensemble indépendant maximum au problème de la clique, ou de la couverture de sommets à l'ensemble indépendant.

**Exercice 25.2.4**

Pour un problème NP-difficile, on peut utiliser un algorithme exact exponentiel, une approximation, une heuristique ou un solveur. Associez à chaque approche un exemple concret : DP par masques, couverture de sommets par arêtes d'un couplage maximal (2-approximation), recuit simulé, solveur SAT.

**Exercice 25.2.5**

Que signifie « P = NP ? » Quelles conséquences pratiques aurait une réponse positive pour la cryptographie et l'optimisation ?

## 25.3 Résumé : quel algorithme pour quel problème ?

**Exercice 25.3.1**

Pour chaque énoncé, indiquez la technique ou l'algorithme le plus adapté (et justifiez en une phrase) :

1. Chercher un élément dans un tableau trié.
2. Trouver le plus petit débit permettant de transférer des fichiers dans un délai donné.
3. Trouver deux éléments d'un tableau trié dont la somme vaut `T`.
4. Trouver la plus longue sous-chaîne sans caractères répétés.
5. Répondre à de nombreuses requêtes de somme sur un tableau fixe.
6. Répondre à des requêtes de somme avec des mises à jour de valeurs.
7. Regrouper des mots qui sont des anagrammes.
8. Maximiser le nombre de réunions dans une seule salle.
9. Calculer la plus longue sous-séquence commune de deux textes.
10. Placer `n` reines sans conflit.
11. Trouver le plus court chemin dans un labyrinthe sans poids.
12. Trouver le plus court chemin avec des poids positifs.
13. Trouver le plus court chemin avec des poids négatifs.
14. Calculer les distances entre toutes les paires de villes (`n = 300`).
15. Ordonner des tâches avec dépendances.
16. Relier des villes au coût minimal.
17. Savoir si deux sommets sont dans la même composante, avec des ajouts d'arêtes.
18. Trouver les groupes de pages web qui se référencent mutuellement.
19. Affecter des étudiants à des projets au mieux (compatibilités données).
20. Rechercher un motif dans un texte long.

**Exercice 25.3.2**

Inventez un énoncé pour chacune des lignes suivantes du tableau de synthèse, sans reprendre les exemples du cours : glouton, programmation dynamique, recherche binaire sur la réponse, retour sur trace, Fenwick.

## 25.4 Conseils de progression

**Exercice 25.4.1**

Écrivez un **test de stress** : pour un problème de votre choix (par exemple la somme maximale d'un sous-tableau), implémentez une solution naïve et une solution optimisée, générez des entrées aléatoires de petite taille et comparez les sorties jusqu'à trouver une divergence.

**Exercice 25.4.2**

Choisissez un schéma parmi : deux pointeurs, fenêtre glissante, préfixes, hachage, recherche binaire sur la réponse. Rédigez un mini-fichier de révision comprenant : un énoncé type, la fiche des cas limites, la complexité attendue, et un exemple de code commenté.

**Exercice 25.4.3**

Établissez un plan de progression sur 8 semaines : pour chaque semaine, un thème du cours, trois problèmes à résoudre et un critère pour juger que le thème est maîtrisé.

## 25.5 Ressources

**Exercice 25.5.1**

Choisissez une plateforme d'entraînement (par exemple LeetCode, Codeforces, AtCoder, Kattis, France-IOI, Project Euler) et résolvez un problème pour chacun des trois niveaux du cours. Pour chaque problème, rédigez l'énoncé reformulé, la méthode retenue, la complexité et les cas limites testés.

**Exercice 25.5.2**

Avec un outil de visualisation d'algorithmes (par exemple VisuAlgo ou Python Tutor), exécutez pas à pas un tri, un parcours de graphe et un algorithme de plus court chemin, puis comparez la trace obtenue avec celle que vous avez faite à la main dans les exercices correspondants.

---

<div align="center">

*Bon courage et bon voyage au pays des algorithmes !*

</div>
