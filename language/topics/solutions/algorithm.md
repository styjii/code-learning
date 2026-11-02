<div align="center">

# Algorithmique — Exercices corrigés

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

> **Légende** : chaque exercice porte le numéro de la section du cours qu'il illustre (l'exercice 5.2.1 est le premier exercice de la section 5.2). *(défi)* = exercice plus difficile ; les exemples utilisent Python, mais les idées s'appliquent à tout langage. Chaque exercice est suivi de sa correction.

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

**Correction**

| Description | Propriété violée ? |
| --- | --- |
| « Tant que `x` est positif, ajouter 1 à `x`. » | **Finitude** : si `x > 0` au départ, la condition reste vraie indéfiniment et l'algorithme ne s'arrête jamais. |
| « Choisir un nombre convenable et l'afficher. » | **Précision** : « convenable » n'est pas défini, l'instruction est ambiguë et deux exécutants feraient des choix différents. |
| « Pour trouver le minimum d'une liste, renvoyer son premier élément. » | **Correction** : l'algorithme se termine et est précis, mais sa sortie est fausse dans le cas général (par exemple `[3, 1, 2]`). |
| « Afficher la liste de tous les nombres premiers. » | **Finitude** : il y a une infinité de nombres premiers, la sortie ne peut jamais être complète. |
| « Calculer la racine carrée de 2 avec une précision infinie en un seul pas. » | **Efficacité** (au sens « réalisable ») : aucune suite finie d'opérations élémentaires ne produit une précision infinie ; la finitude est également compromise. |

**Exercice 1.1.2**

En vous inspirant de la fonction `maximum` du cours, écrivez une fonction `minimum(valeurs)` qui renvoie le plus petit élément d'une liste non vide. Testez-la sur `[3, 8, 2, 9, 4]` et sur une liste d'un seul élément.

**Correction**

On initialise le minimum avec le premier élément (la liste est non vide), puis on parcourt les éléments suivants.

```python
def minimum(valeurs):
    plus_petit = valeurs[0]
    for v in valeurs[1:]:
        if v < plus_petit:
            plus_petit = v
    return plus_petit


print(minimum([3, 8, 2, 9, 4]))  # 2
print(minimum([7]))              # 7 : liste d'un seul élément
```

Pour une liste d'un seul élément, la boucle ne s'exécute pas et on renvoie directement cet élément.

**Exercice 1.1.3**

Écrivez une fonction `deux_plus_grands(valeurs)` qui renvoie le plus grand et le deuxième plus grand élément d'une liste d'au moins deux éléments, en **un seul parcours** et sans trier la liste.

**Correction**

On maintient deux variables `a` (le plus grand) et `b` (le deuxième plus grand) pendant un seul parcours.

```python
def deux_plus_grands(valeurs):
    a, b = valeurs[0], valeurs[1]
    if b > a:
        a, b = b, a
    for v in valeurs[2:]:
        if v > a:
            a, b = v, a
        elif v > b:
            b = v
    return a, b


print(deux_plus_grands([3, 8, 2, 9, 4]))  # (9, 8)
print(deux_plus_grands([5, 5, 3]))        # (5, 5) : les doublons comptent
```

Complexité : O(n) en temps, O(1) en espace.

**Exercice 1.1.4**

Écrivez une fonction `contient(valeurs, x)` qui indique si `x` apparaît dans la liste, sans utiliser l'opérateur `in`. Quelle est la sortie de votre algorithme pour une liste vide ?

**Correction**

```python
def contient(valeurs, x):
    for v in valeurs:
        if v == x:
            return True
    return False
```

Pour une liste vide, la boucle ne s'exécute pas et la fonction renvoie `False` : aucun élément n'est égal à `x`.

## 1.2 Pourquoi les algorithmes sont-ils importants ?

**Exercice 1.2.1**

Complétez le tableau suivant (ordres de grandeur) :

| Taille `n` | Algorithme en O(n²) | Algorithme en O(n log n) |
| --- | --- | --- |
| 100 | | |
| 10 000 | | |
| 100 000 | | |

**Correction**

Les valeurs sont des ordres de grandeur (logarithme en base 2) :

| Taille `n` | Algorithme en O(n²) | Algorithme en O(n log n) |
| --- | --- | --- |
| 100 | 10 000 | environ 660 |
| 10 000 | 10⁸ | environ 1,3 × 10⁵ |
| 100 000 | 10¹⁰ | environ 1,7 × 10⁶ |

Le rapport entre les deux croît avec `n` : environ 15 pour `n = 100`, 750 pour `n = 10⁴` et 6 000 pour `n = 10⁵`.

**Exercice 1.2.2**

En supposant qu'un programme Python effectue environ 10⁷ opérations simples par seconde, estimez le temps d'exécution d'un algorithme O(n²) puis O(n log n) pour `n = 10⁵`.

**Correction**

Pour `n = 10⁵` :

- O(n²) : 10¹⁰ opérations, soit 10¹⁰ / 10⁷ = 1 000 secondes, environ 17 minutes.
- O(n log n) : environ 1,7 × 10⁶ opérations, soit environ 0,17 seconde.

L'écart est d'un facteur de l'ordre de 6 000.

**Exercice 1.2.3**

Citez trois applications concrètes (autres que celles du cours) où le choix de l'algorithme change radicalement l'expérience de l'utilisateur, et précisez pour chacune ce qui rend l'efficacité critique.

**Correction**

Exemples possibles :

1. **Moteur de recherche** : il faut répondre en quelques millisecondes parmi des milliards de pages. Sans index inversé et sans algorithmes de classement efficaces, une recherche linéaire serait impraticable.
2. **Navigation GPS** : le calcul d'un plus court chemin sur un graphe de millions de routes doit être instantané et se refaire à chaque déviation. Dijkstra, A\* ou des méthodes de prétraitement rendent cela possible.
3. **Compression et streaming vidéo** : l'encodage et le décodage doivent tenir en temps réel (30 images par seconde) avec peu de mémoire ; un algorithme trop lent provoque saccades et latence.

On peut aussi citer la correction orthographique en temps réel, la recommandation de contenus ou l'alignement de séquences ADN.

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

**Correction**

1. L'algorithme compte le nombre d'éléments **pairs** du tableau.
2. Traduction en Python :

```python
def mystere(tableau):
    c = 0
    for x in tableau:
        if x % 2 == 0:
            c += 1
    return c
```

3. Organigramme :

```text
          +---------+
          |  DEBUT  |
          +----+----+
               |
        c <- 0 ; parcourir tableau
               |
               v
      +-----------------+   non (fin du tableau)
 +--->| reste un x ?    |------------------+
 |    +--------+--------+                   |
 |             | oui                        v
 |             v                     +--------------+
 |      +-------------+              | RETOURNER c  |
 |      | x mod 2 = 0 |              +------+-------+
 |      +------+------+                     |
 |        oui  |   non                      v
 |             v    |                  +--------+
 |        c <- c+1  |                  |  FIN   |
 |             |    |                  +--------+
 +-------------+----+
```

**Exercice 1.3.2**

Écrivez en pseudo-code (dans le même format que le cours) un algorithme `Somme(tableau)` puis un algorithme `EstTrié(tableau)` qui indique si un tableau est trié par ordre croissant.

**Correction**

```text
ALGORITHME Somme(tableau)
  Entrée : un tableau de nombres
  Sortie : la somme de ses éléments
  s ← 0
  POUR chaque x DANS tableau FAIRE
      s ← s + x
  RETOURNER s

ALGORITHME EstTrié(tableau)
  Entrée : un tableau de nombres
  Sortie : VRAI si le tableau est trié par ordre croissant, FAUX sinon
  POUR i DE 1 À longueur(tableau) − 1 FAIRE
      SI tableau[i − 1] > tableau[i] ALORS
          RETOURNER FAUX
  RETOURNER VRAI
```

Un tableau vide ou d'un seul élément est considéré comme trié (la boucle ne s'exécute pas).

**Exercice 1.3.3**

Décrivez en langage naturel, puis sous forme d'organigramme, l'algorithme qui détermine si un entier est pair ou impair, et affiche le résultat.

**Correction**

**Langage naturel** :

1. Lire l'entier `n`.
2. Calculer le reste de la division de `n` par 2.
3. Si le reste vaut 0, afficher « pair » ; sinon afficher « impair ».

**Organigramme** :

```text
  +-------+     +-----------+     +-----------------+
  | DEBUT |---->| Lire n    |---->| n mod 2 = 0 ?   |
  +-------+     +-----------+     +----+-------+----+
                                    oui|       |non
                                       v       v
                              +----------+  +------------+
                              | Afficher |  | Afficher   |
                              | "pair"   |  | "impair"   |
                              +----+-----+  +-----+------+
                                   |              |
                                   +------+-------+
                                          v
                                      +-------+
                                      |  FIN  |
                                      +-------+
```

## 1.4 Écrire son premier algorithme

**Exercice 1.4.1**

Écrivez un algorithme (étapes numérotées, puis code Python) qui calcule la moyenne de `n` notes saisies dans une liste.

**Correction**

**Étapes** :

1. Initialiser une somme `s` à 0.
2. Pour chaque note de la liste, l'ajouter à `s`.
3. Diviser `s` par le nombre de notes `n`.
4. Renvoyer le résultat (la liste doit contenir au moins une note).

```python
def moyenne(notes):
    s = 0
    for note in notes:
        s += note
    return s / len(notes)


print(moyenne([12, 15, 9, 18]))  # 13.5
```

**Exercice 1.4.2**

Écrivez un algorithme qui convertit une température de degrés Celsius en degrés Fahrenheit, puis l'inverse.

**Correction**

Formules : `F = C × 9/5 + 32` et `C = (F − 32) × 5/9`.

**Étapes** : lire la température, appliquer la formule correspondante, renvoyer le résultat.

```python
def celsius_vers_fahrenheit(c):
    return c * 9 / 5 + 32


def fahrenheit_vers_celsius(f):
    return (f - 32) * 5 / 9


print(celsius_vers_fahrenheit(100))   # 212.0
print(fahrenheit_vers_celsius(32))    # 0.0
```

**Exercice 1.4.3**

Écrivez un algorithme qui échange les valeurs de deux variables `a` et `b` : d'abord avec une variable temporaire, puis sans.

**Correction**

Avec une variable temporaire :

```python
tmp = a
a = b
b = tmp
```

Sans variable temporaire (plusieurs possibilités) :

```python
# Affectation multiple (idiomatique en Python)
a, b = b, a

# Par arithmétique (entiers)
a = a + b
b = a - b
a = a - b

# Par XOR (entiers)
a ^= b
b ^= a
a ^= b
```

L'affectation multiple évalue d'abord le membre droit `(b, a)` puis l'affecte, ce qui évite tout écrasement.

**Exercice 1.4.4**

Écrivez un algorithme qui calcule le prix TTC d'un article à partir de son prix hors taxe et d'un taux de TVA en pourcentage.

**Correction**

Formule : `prix_ttc = prix_ht × (1 + taux / 100)`.

```python
def prix_ttc(prix_ht, taux_tva):
    return prix_ht * (1 + taux_tva / 100)


print(prix_ttc(100, 20))   # 120.0
print(prix_ttc(50, 5.5))   # 52.75
```

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

**Correction**

| Étape | Votre réponse |
| --- | --- |
| 1. Comprendre | Entrée : tableau d'entiers et cible `T`. Sortie : booléen indiquant s'il existe `i ≠ j` avec `t[i] + t[j] = T`. Questions : doublons possibles ? tableau trié ? nombres négatifs ? taille maximale ? |
| 2. Exemples | `[2, 7, 11, 15]`, `T = 9` : vrai (2 + 7). `[3, 3]`, `T = 6` : vrai (deux éléments distincts de même valeur). `[3]`, `T = 6` : faux (un seul élément, on ne peut pas réutiliser le même). `[]` : faux. |
| 3. Solution naïve | Deux boucles imbriquées sur toutes les paires `(i, j)` avec `i < j` : O(n²) temps, O(1) espace. |
| 4. Optimiser | Parcourir le tableau en mémorisant dans un ensemble les valeurs déjà vues ; pour chaque `x`, tester si `T − x` est dans l'ensemble : O(n) temps, O(n) espace. Si le tableau est trié : deux pointeurs, O(n) temps, O(1) espace. |
| 5. Analyser | Version hachage : n itérations, chacune en O(1) en moyenne, soit O(n) ; mémoire O(n). La version naïve fait n(n−1)/2 comparaisons. |
| 6. Coder et tester | Voir ci-dessous. |

```python
def existe_somme(t, cible):
    vus = set()
    for x in t:
        if cible - x in vus:
            return True
        vus.add(x)
    return False


assert existe_somme([2, 7, 11, 15], 9)
assert existe_somme([3, 3], 6)
assert not existe_somme([3], 6)
assert not existe_somme([], 5)
```

L'élément est ajouté à `vus` après le test, ce qui garantit que les deux éléments sont distincts (par leur position).

**Exercice 1.5.2**

Listez au moins six cas limites à tester pour une fonction `moyenne(valeurs)` qui renvoie la moyenne d'une liste de nombres.

**Correction**

Cas limites pour `moyenne(valeurs)` :

1. liste vide (division par zéro : lever une exception ou renvoyer une valeur convenue) ;
2. liste d'un seul élément ;
3. tous les éléments égaux ;
4. valeurs négatives et valeurs mélangées de signes ;
5. valeurs nulles uniquement ;
6. très grandes valeurs (débordement dans d'autres langages, perte de précision en flottants) ;
7. flottants (par exemple `[0.1, 0.2, 0.3]`, erreurs d'arrondi) ;
8. liste très longue (performance et précision de la somme).

**Exercice 1.5.3**

Pour chacune des contraintes suivantes, indiquez la complexité maximale raisonnable : `n ≤ 20`, `n ≤ 5 000`, `n ≤ 10⁵`, `n ≤ 10⁶`.

**Correction**

En supposant environ 10⁸ opérations simples par seconde :

| Contrainte | Complexité maximale raisonnable |
| --- | --- |
| `n ≤ 20` | O(2ⁿ) ou O(2ⁿ · n) (énumération de sous-ensembles) ; O(n!) jusqu'à environ 10 |
| `n ≤ 5 000` | O(n²) (25 × 10⁶ opérations) |
| `n ≤ 10⁵` | O(n log n), éventuellement O(n √n) |
| `n ≤ 10⁶` | O(n) ou O(n log n) avec une petite constante |

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

**Correction**

1. Trier un tableau en le coupant en deux moitiés : **diviser pour régner** (tri fusion).
2. Placer 8 reines : **retour sur trace**.
3. Chemin le plus court entre deux stations : **graphes** (BFS ou Dijkstra).
4. Rendu de monnaie avec un système canonique : **glouton**.
5. Plus longue sous-séquence commune : **programmation dynamique**.
6. Tester tous les codes d'un cadenas : **force brute**.
7. Test de primalité avec petite probabilité d'erreur : **probabiliste** (Miller-Rabin).

**Exercice 1.6.2**

Écrivez une attaque par force brute sur un cadenas à code de 4 chiffres : une fonction `forcer(code_secret)` qui renvoie le nombre d'essais nécessaires. Quel est le nombre d'essais dans le pire cas ?

**Correction**

```python
def forcer(code_secret):
    essais = 0
    for tentative in range(10000):      # 0000 à 9999
        essais += 1
        if tentative == code_secret:
            return essais
    return None                          # code invalide


print(forcer(0))      # 1
print(forcer(1234))   # 1235
print(forcer(9999))   # 10000
```

Dans le pire cas (code `9999`), il faut **10 000 essais** (10⁴ codes possibles). En moyenne, environ 5 000.

## 1.7 Algorithme ou programme ?

**Exercice 1.7.1**

Indiquez si chaque affirmation est vraie ou fausse, en justifiant :

1. Un algorithme dépend du langage de programmation utilisé.
2. Un serveur web qui tourne sans fin est un programme, mais son comportement ne correspond pas à un algorithme au sens strict.
3. `sorted(liste)` est un algorithme.
4. Deux programmes écrits dans des langages différents peuvent implémenter le même algorithme.

**Correction**

1. **Faux.** Un algorithme est une méthode abstraite ; il ne dépend pas du langage, seule son implémentation en dépend.
2. **Vrai.** Un algorithme au sens strict doit se terminer (finitude). Un serveur qui tourne indéfiniment est un programme ; chaque traitement de requête, lui, est un algorithme qui se termine.
3. **Vrai (en nuançant).** `sorted(liste)` est l'appel d'une fonction qui implémente un algorithme (Timsort) : entrée, sortie, finitude, correction. On parle plutôt d'implémentation que d'algorithme.
4. **Vrai.** Un même algorithme (par exemple le tri fusion) peut être programmé en Python, C ou Java.

**Exercice 1.7.2**

Écrivez le même algorithme de calcul de la somme des carrés des `n` premiers entiers sous trois formes : langage naturel, pseudo-code et code Python.

**Correction**

**Langage naturel** : on part d'une somme égale à 0 ; pour chaque entier `i` de 1 à `n`, on ajoute le carré de `i` à la somme ; à la fin on renvoie la somme.

**Pseudo-code** :

```text
ALGORITHME SommeDesCarrés(n)
  Entrée : un entier n ≥ 0
  Sortie : 1² + 2² + ... + n²
  s ← 0
  POUR i DE 1 À n FAIRE
      s ← s + i × i
  RETOURNER s
```

**Python** :

```python
def somme_des_carres(n):
    s = 0
    for i in range(1, n + 1):
        s += i * i
    return s


print(somme_des_carres(4))  # 30
```

Vérification par la formule : `n(n + 1)(2n + 1) / 6 = 4 × 5 × 9 / 6 = 30`.

---

# 2. Analyse des algorithmes

## 2.1 Pourquoi analyser ?

**Exercice 2.1.1**

Donnez trois raisons pour lesquelles mesurer le temps d'exécution en secondes ne suffit pas pour comparer deux algorithmes.

**Correction**

Trois raisons parmi d'autres :

1. **Dépendance à la machine** : processeur, mémoire, système, charge du moment ; le même programme n'a pas le même temps sur deux ordinateurs.
2. **Dépendance à l'implémentation** : langage, compilateur ou interpréteur, optimisations ; on compare alors des programmes et non des algorithmes.
3. **Dépendance aux données testées** : un test sur quelques entrées ne dit rien du comportement sur des entrées plus grandes ou plus défavorables ; on ne sait pas extrapoler.

On peut ajouter la non-reproductibilité des mesures (bruit, cache, ramasse-miettes). L'analyse asymptotique compte les opérations en fonction de la taille `n`, indépendamment de ces facteurs.

**Exercice 2.1.2**

Distinguez complexité en temps et complexité en espace. Pour la fonction `maximum` de la section 1.1, donnez les deux.

**Correction**

- **Complexité en temps** : nombre d'opérations élémentaires en fonction de la taille de l'entrée.
- **Complexité en espace** : quantité de mémoire utilisée (souvent la mémoire supplémentaire, hors entrée) en fonction de la taille de l'entrée.

Pour `maximum` (parcours d'une liste de `n` éléments avec une variable `max`) : temps **O(n)** (n − 1 comparaisons), espace supplémentaire **O(1)**.

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

**Correction**

| Fonction | `T(n)` (opérations élémentaires) | Complexité |
| --- | --- | --- |
| `f1` | `n` comparaisons plus au plus `n` incréments : `T(n) ≤ 2n` | O(n) |
| `f2` | `n²` comparaisons plus au plus `n²` incréments : `T(n) ≤ 2n²` | O(n²) |
| `f3` | `⌊log₂ n⌋` itérations (division par 2 à chaque tour) | O(log n) |
| `f4` | `n` affichages puis `n` affichages : `T(n) = 2n` | O(n) |
| `f5` | `0 + 1 + ... + (n−1) = n(n−1)/2` | O(n²) |
| `f6` | `n` itérations externes, chacune avec `⌈log₂ n⌉` doublements : `T(n) ≈ n log₂ n` | O(n log n) |

**Exercice 2.2.2**

Réécrivez `f2` pour qu'elle ne compare chaque paire d'indices `(i, j)` avec `i < j` qu'une seule fois. Quelle est la nouvelle complexité ? Le gain est-il asymptotique ?

**Correction**

```python
def f2_optimisee(t):
    n = len(t)
    c = 0
    for i in range(n):
        for j in range(i + 1, n):   # uniquement j > i
            if t[i] == t[j]:
                c += 1
    return c
```

Nombre de comparaisons : `n(n−1)/2`. La complexité reste **O(n²)** : on divise le nombre d'opérations par environ 2, ce qui est un gain de constante et **non un gain asymptotique**. (Remarque : `f2` compte aussi les paires `i = j` et les deux ordres, donc `f2(t) = n + 2 × f2_optimisee(t)`.)

**Exercice 2.2.3**

Simplifiez en gardant le terme dominant : `5n + 100`, `n² + 1000n`, `3n log n + n`, `2ⁿ + n³`, `n! + 2ⁿ`.

**Correction**

On garde le terme de plus forte croissance et on ignore les constantes multiplicatives :

- `5n + 100` donne **O(n)**
- `n² + 1000n` donne **O(n²)**
- `3n log n + n` donne **O(n log n)**
- `2ⁿ + n³` donne **O(2ⁿ)**
- `n! + 2ⁿ` donne **O(n!)**

## 2.3 Notations asymptotiques *(à jour : correction d'une erreur fréquente)*

**Exercice 2.3.1**

Pour `f(n) = 3n² + 5n`, trouvez explicitement des constantes `c` et `n₀` prouvant que `f ∈ O(n²)`, puis des constantes prouvant que `f ∈ Ω(n²)`. Concluez sur `Θ`.

**Correction**

`f(n) = 3n² + 5n`.

**Borne supérieure** : pour `n ≥ 1`, `5n ≤ 5n²`, donc `f(n) ≤ 3n² + 5n² = 8n²`. Avec `c = 8` et `n₀ = 1`, `f ∈ O(n²)`.

**Borne inférieure** : pour `n ≥ 1`, `f(n) = 3n² + 5n ≥ 3n²`. Avec `c = 3` et `n₀ = 1`, `f ∈ Ω(n²)`.

**Conclusion** : `f` est bornée au-dessus et au-dessous par des multiples de `n²` à partir de `n₀ = 1`, donc `f ∈ Θ(n²)` (avec `3n² ≤ f(n) ≤ 8n²`).

**Exercice 2.3.2**

Indiquez si chaque affirmation est vraie ou fausse :

1. `n log n ∈ O(n²)`
2. `2ⁿ ∈ O(n¹⁰)`
3. `n² ∈ Ω(n)`
4. `5n ∈ o(n)`
5. `n + 10 ∈ Θ(n)`
6. `log n ∈ o(√n)`
7. `n³ ∈ Θ(n²)`

**Correction**

1. `n log n ∈ O(n²)` : **vrai** (`log n ≤ n`).
2. `2ⁿ ∈ O(n¹⁰)` : **faux** (une exponentielle dépasse tout polynôme).
3. `n² ∈ Ω(n)` : **vrai** (`n² ≥ n` pour `n ≥ 1`).
4. `5n ∈ o(n)` : **faux** (`5n / n = 5` ne tend pas vers 0 ; `5n ∈ Θ(n)`).
5. `n + 10 ∈ Θ(n)` : **vrai**.
6. `log n ∈ o(√n)` : **vrai** (`log n / √n → 0`).
7. `n³ ∈ Θ(n²)` : **faux** (`n³` croît strictement plus vite ; on a seulement `n³ ∈ Ω(n²)`).

**Exercice 2.3.3**

Un étudiant affirme : « O désigne le pire cas, Ω le meilleur cas, Θ le cas moyen. » Expliquez pourquoi c'est faux. Illustrez avec le tri par insertion : donnez la fonction `T(n)` du meilleur cas et celle du pire cas, puis une borne `Θ` pour chacune.

**Correction**

Les notations O, Ω et Θ décrivent des **bornes sur la croissance d'une fonction** ; elles n'ont aucun lien intrinsèque avec un cas particulier. Chaque cas (meilleur, pire, moyen) correspond à sa **propre fonction** `T(n)`, et on peut donner pour chacune une borne O, Ω ou Θ.

Exemple avec le tri par insertion :

- **Meilleur cas** (liste déjà triée) : `T_meilleur(n) = n − 1` comparaisons, donc `T_meilleur ∈ Θ(n)`.
- **Pire cas** (liste triée en ordre décroissant) : `T_pire(n) = n(n−1)/2` comparaisons, donc `T_pire ∈ Θ(n²)`.

On peut dire que le tri par insertion est en `O(n²)` dans tous les cas, mais aussi que son pire cas est en `Ω(n²)` : les trois notations s'appliquent au pire cas comme au meilleur cas.

**Exercice 2.3.4**

Classez par ordre de croissance et justifiez : `n log n`, `n²`, `√n`, `2ⁿ`, `log n`, `n`, `n!`, `n³`, `1`.

**Correction**

Ordre de croissance :

`1 < log n < √n < n < n log n < n² < n³ < 2ⁿ < n!`

Justifications : une constante ne croît pas ; le logarithme croît moins vite que toute puissance positive de `n` (donc que `√ n = n^0,5`) ; `n log n` est entre `n` et `n²` car `1 < log n < n` ; les polynômes sont dominés par les exponentielles ; la factorielle domine l'exponentielle (par exemple `n! ≥ (n/2)^(n/2)`, ou la formule de Stirling).

## 2.4 Pire, meilleur et cas moyen

**Exercice 2.4.1**

Pour la recherche linéaire dans une liste de `n` éléments distincts, où la cible est présente avec une probabilité uniforme sur chaque position, donnez `T(n)` dans le meilleur cas, le pire cas et le cas moyen.

**Correction**

Position de la cible équiprobable parmi `n` positions :

- **Meilleur cas** : `T(n) = 1` (cible en première position).
- **Pire cas** : `T(n) = n` (cible en dernière position).
- **Cas moyen** : `T(n) = (1 + 2 + ... + n) / n = (n + 1) / 2`, soit environ `n/2`.

Les trois sont respectivement O(1), O(n) et O(n).

**Exercice 2.4.2**

Donnez un exemple d'entrée de taille `n` qui déclenche le meilleur cas du tri par insertion, et un exemple qui déclenche le pire cas.

**Correction**

- **Meilleur cas** : une liste déjà triée par ordre croissant, par exemple `[1, 2, 3, ..., n]` : chaque insertion ne fait qu'une comparaison, `T(n) = n − 1`.
- **Pire cas** : une liste triée par ordre décroissant, par exemple `[n, n−1, ..., 1]` : chaque élément doit être comparé à tous les précédents, `T(n) = n(n−1)/2`.

**Exercice 2.4.3**

Un quicksort choisit toujours le premier élément comme pivot. Donnez une entrée de taille `n` pour laquelle il atteint son pire cas, et expliquez pourquoi.

**Correction**

Entrée de pire cas : une liste **déjà triée** (croissante, ou décroissante), par exemple `[1, 2, ..., n]`.

Avec le premier élément comme pivot, le pivot est le plus petit élément : la partition produit une partie vide et une partie de taille `n − 1`. La récurrence devient `T(n) = T(n − 1) + O(n)`, soit `O(n²)`, et la profondeur de récursion vaut `n`.

## 2.5 Classes de complexité usuelles

**Exercice 2.5.1**

En supposant 10⁷ opérations par seconde, estimez le temps d'exécution pour `n = 10⁶` d'un algorithme en O(n), O(n log n), O(n²) puis pour `n = 30` d'un algorithme en O(2ⁿ).

**Correction**

À 10⁷ opérations par seconde :

| Algorithme | Nombre d'opérations | Temps |
| --- | --- | --- |
| O(n), `n = 10⁶` | 10⁶ | 0,1 s |
| O(n log n), `n = 10⁶` | environ 2 × 10⁷ | environ 2 s |
| O(n²), `n = 10⁶` | 10¹² | 10⁵ s, soit environ 28 heures |
| O(2ⁿ), `n = 30` | 2³⁰ ≈ 1,07 × 10⁹ | environ 107 s, soit près de 2 minutes |

**Exercice 2.5.2**

Quelle est la plus grande valeur de `n` pour laquelle un algorithme en O(n²), O(n³), O(2ⁿ) puis O(n!) s'exécute en moins d'une seconde à raison de 10⁸ opérations par seconde ?

**Correction**

Avec 10⁸ opérations par seconde (on cherche `n` maximal tel que le coût soit au plus 10⁸) :

- O(n²) : `n ≈ 10⁴` (`10⁸`).
- O(n³) : `n ≈ 464` (`464³ ≈ 10⁸`).
- O(2ⁿ) : `n = 26` (`2²⁶ ≈ 6,7 × 10⁷` ; `2²⁷ ≈ 1,3 × 10⁸` dépasse déjà).
- O(n!) : `n = 11` (`11! ≈ 4,0 × 10⁷` ; `12! ≈ 4,8 × 10⁸` dépasse).

**Exercice 2.5.3**

Associez chaque fonction à une classe de complexité usuelle : accès à un indice d'un tableau, recherche binaire, test de primalité naïf, parcours d'une liste, tri efficace, deux boucles imbriquées, énumération de tous les sous-ensembles, énumération de toutes les permutations.

**Correction**

| Fonction | Classe |
| --- | --- |
| accès à un indice d'un tableau | O(1) |
| recherche binaire | O(log n) |
| test de primalité naïf | O(√n) |
| parcours d'une liste | O(n) |
| tri efficace | O(n log n) |
| deux boucles imbriquées | O(n²) |
| énumération de tous les sous-ensembles | O(2ⁿ) |
| énumération de toutes les permutations | O(n!) |

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

**Correction**

- `a(t)` : `sum(t)` n'utilise qu'un accumulateur, espace supplémentaire **O(1)**.
- `b(t)` : construit une nouvelle liste de `n` éléments, **O(n)**.
- `c(n)` : récursion de profondeur `n`, donc `n` cadres sur la pile, **O(n)**.
- `d(n)` : matrice `n × n`, **O(n²)**.
- `e(t)` : `t.sort()` ne crée pas de nouvelle liste, mais Timsort utilise un tampon interne pouvant atteindre `n/2` éléments : **O(n)** au pire (on le qualifie souvent de tri « en place » car la liste n'est pas copiée explicitement).

**Exercice 2.6.2**

Que se passe-t-il en Python quand on appelle `c(5000)` ? Proposez deux manières d'éviter le problème.

**Correction**

`c(5000)` déclenche une `RecursionError : maximum recursion depth exceeded`, car la limite par défaut de Python est d'environ 1000 appels imbriqués.

Deux solutions :

1. **Écrire une version itérative** (boucle `for`), qui n'utilise que O(1) de mémoire supplémentaire :

```python
def c_iteratif(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r
```

2. **Relever la limite** avec `sys.setrecursionlimit(10000)` (à utiliser avec prudence : une limite trop haute peut faire planter l'interpréteur par dépassement de la pile système). On peut aussi utiliser `math.factorial(n)`.

## 2.7 Compromis temps / espace

**Exercice 2.7.1**

On vous pose `10⁵` questions de la forme « `x` appartient-il à cette liste de `10⁵` éléments ? ». Comparez deux solutions (recherche linéaire à chaque question, et conversion préalable en `set`) en temps et en espace. Laquelle choisir ?

**Correction**

- **Recherche linéaire à chaque question** : O(n) par question, soit `10⁵ × 10⁵ = 10¹⁰` opérations au total ; mémoire supplémentaire O(1). Mesure typique : environ 0,7 ms par recherche à `n = 10⁵`, soit plus d'une minute pour 10⁵ questions.
- **Conversion en `set`** : construction en O(n), puis chaque question en O(1) en moyenne : environ `2 × 10⁵` opérations au total ; mémoire supplémentaire O(n) (quelques mégaoctets).

On choisit le `set` : le coût mémoire est modeste pour un gain de temps considérable (l'investissement initial est amorti dès que le nombre de questions dépasse quelques unités).

**Exercice 2.7.2**

Citez un exemple où l'on échange du temps contre de l'espace dans l'autre sens (économiser de la mémoire au prix de plus de calcul).

**Correction**

Exemples où l'on économise de la mémoire au prix de plus de calcul :

- **Ne pas mémoriser** : calculer Fibonacci avec deux variables plutôt qu'un tableau, ou recalculer une valeur plutôt que la stocker.
- **Utiliser un générateur** : produire les éléments à la demande plutôt que de construire une liste complète.
- **Compression** : stocker des données compressées et les décompresser à chaque accès.
- **Filtre de Bloom** ou structure compacte : moins de mémoire au prix d'une approximation ou d'un calcul de plusieurs hachages.

## 2.8 Analyse amortie *(ajout)*

**Exercice 2.8.1**

Un tableau dynamique double sa capacité quand il est plein (capacité initiale 1). Calculez le nombre total de copies d'éléments effectuées pendant `n = 2ᵏ` appels à `append`, puis le coût amorti par insertion.

**Correction**

Capacité initiale 1, doublement quand le tableau est plein. Pour `n = 2ᵏ` ajouts, un doublement a lieu lorsque la taille atteint `1, 2, 4, ..., 2ᵏ⁻¹`, et copie à chaque fois ce nombre d'éléments :

`1 + 2 + 4 + ... + 2ᵏ⁻¹ = 2ᵏ − 1 = n − 1` copies.

Coût total : `n` écritures plus `n − 1` copies, soit moins de `2n` opérations. Le **coût amorti** par insertion est donc `< 2`, c'est-à-dire **O(1)**, même si une insertion isolée peut coûter O(n).

**Exercice 2.8.2**

Un compteur binaire de `k` bits est incrémenté `n` fois à partir de 0. Dans le pire cas, une seule incrémentation modifie `k` bits. Montrez que le coût total des `n` incrémentations est cependant en O(n).

**Correction**

Le bit `i` (de poids `2ⁱ`) change de valeur une fois toutes les `2ⁱ` incrémentations. Sur `n` incrémentations, le nombre total de changements de bits est :

`Σ ⌊n / 2ⁱ⌋ ≤ n × (1 + 1/2 + 1/4 + ...) < 2n`.

Le coût total est donc **O(n)**, soit un coût amorti inférieur à 2 par incrémentation. (Argument par crédit : chaque incrémentation met exactement un bit à 1 et paie à l'avance 1 unité pour sa future remise à 0 ; toutes les remises à 0 sont ainsi déjà payées.)

**Exercice 2.8.3**

Distinguez en deux phrases le coût amorti et le coût moyen au sens probabiliste.

**Correction**

- Le **coût amorti** est une garantie **déterministe** sur le coût total d'une séquence d'opérations, en pire cas, divisé par le nombre d'opérations : aucune hypothèse de hasard n'est faite.
- Le **coût moyen** (au sens probabiliste) est une espérance sur une distribution des entrées ou sur l'aléa de l'algorithme : il ne dit rien du coût d'une séquence précise, qui peut être bien pire.

## 2.9 Récurrences

**Exercice 2.9.1**

Donnez la solution asymptotique de chaque récurrence :

1. `T(n) = T(n − 1) + O(1)`
2. `T(n) = T(n/2) + O(1)`
3. `T(n) = 2T(n/2) + O(n)`
4. `T(n) = 2T(n − 1) + O(1)`
5. `T(n) = T(n − 1) + O(n)`
6. `T(n) = T(n/2) + O(n)`

**Correction**

1. `T(n) = T(n − 1) + O(1)` : **O(n)**.
2. `T(n) = T(n/2) + O(1)` : **O(log n)**.
3. `T(n) = 2T(n/2) + O(n)` : **O(n log n)**.
4. `T(n) = 2T(n − 1) + O(1)` : **O(2ⁿ)**.
5. `T(n) = T(n − 1) + O(n)` : **O(n²)**.
6. `T(n) = T(n/2) + O(n)` : **O(n)** (somme géométrique `n + n/2 + n/4 + ... < 2n`).

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

**Correction**

- `puissance` : `T(n) = T(n − 1) + O(1)`, `T(0) = O(1)`, donc `T(n) = O(n)`.
- `hanoi` : `T(n) = 2T(n − 1) + 1`, `T(0) = 0`, donc `T(n) = 2ⁿ − 1`, soit **O(2ⁿ)**.
- `somme_dc` : `T(n) = 2T(n/2) + O(1)`, `T(1) = O(1)`, donc `T(n) = O(n)` (théorème maître, cas où les feuilles dominent).

## 2.10 Conseils pratiques

**Exercice 2.10.1**

Avec `timeit`, comparez le temps de `x in liste` et de `x in ensemble` pour des listes de taille `10³`, `10⁴`, `10⁵`. Tracez ou tabulez vos résultats et commentez.

**Correction**

```python
import timeit

for n in (10**3, 10**4, 10**5):
    liste = list(range(n))
    ensemble = set(liste)
    x = -1                       # élément absent : pire cas pour la liste
    t_liste = timeit.timeit(lambda: x in liste, number=200) / 200
    t_ens = timeit.timeit(lambda: x in ensemble, number=200_000) / 200_000
    print(f"{n:>7}  liste : {t_liste * 1e6:8.1f} us   ensemble : {t_ens * 1e9:6.0f} ns")
```

Résultats typiques (l'ordre de grandeur compte, pas les valeurs exactes) :

| `n` | `x in liste` | `x in ensemble` |
| --- | --- | --- |
| 10³ | environ 7 µs | environ 50 ns |
| 10⁴ | environ 100 µs | environ 40 ns |
| 10⁵ | environ 700 µs | environ 30 ns |

Commentaire : le temps de la liste est proportionnel à `n` (O(n)), celui de l'ensemble est constant (O(1) en moyenne). Pour `n = 10⁵`, l'ensemble est plus de 10 000 fois plus rapide.

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

**Correction**

- `construire` : `s += "a"` copie potentiellement la chaîne à chaque ajout (les chaînes sont immuables), soit O(n²) en théorie (CPython l'optimise souvent, sans garantie). Version rapide : `"a" * n` ou `"".join(["a"] * n)`, en O(n).
- `file_naive` : `t.pop(0)` décale tous les éléments restants, O(n) à chaque retrait, soit O(n²). Version rapide : utiliser `collections.deque` avec `popleft()` en O(1), ou simplement `resultat = list(t)` ; `t.clear()`.
- `inverser_naif` : `r.insert(0, x)` décale tout le tableau, O(n) par insertion, soit O(n²). Version rapide : `r = t[::-1]` ou `t.reverse()`, en O(n).

**Exercice 2.10.3**

Un tableau `n × n` d'entiers Python est-il envisageable pour `n = 10⁵` ? Justifiez par un calcul de mémoire.

**Correction**

Un tableau `n × n` avec `n = 10⁵` contient `n² = 10¹⁰` cases. Une liste Python stocke une référence (8 octets) par case : `10¹⁰ × 8 = 8 × 10¹⁰` octets, soit **80 Go**, sans compter les objets entiers eux-mêmes. Même avec NumPy en `int8`, il faudrait 10 Go. Ce n'est donc **pas envisageable** sur une machine courante ; il faut une structure creuse, un calcul à la volée ou un autre algorithme.

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

**Correction**

| Structure | Accès | Recherche | Insertion | Suppression |
| --- | --- | --- | --- | --- |
| Tableau / `list` | O(1) par indice | O(n) | O(1) amorti en fin, O(n) ailleurs | O(1) en fin, O(n) ailleurs |
| Liste chaînée | O(n) | O(n) | O(1) en tête (ou après un nœud connu) | O(1) si le nœud précédent est connu, sinon O(n) |
| Pile | O(1) sommet seulement | O(n) | O(1) (`push`) | O(1) (`pop`) |
| File (`deque`) | O(1) aux extrémités | O(n) | O(1) aux extrémités | O(1) aux extrémités |
| Table de hachage | O(1) en moyenne par clé (O(n) pire cas) | O(1) en moyenne (O(n) pire cas) | O(1) en moyenne | O(1) en moyenne |
| Tas | O(1) pour le minimum (ou maximum) | O(n) | O(log n) | O(log n) pour le minimum, O(n) pour un élément quelconque |
| ABR équilibré | O(log n) | O(log n) | O(log n) | O(log n) |

**Exercice 3.1.2**

Pourquoi `list.insert(0, x)` est-il en O(n) alors que `deque.appendleft(x)` est en O(1) ?

**Correction**

Une `list` Python est un **tableau dynamique contigu** : insérer en position 0 oblige à décaler les `n` éléments existants d'une case, soit O(n). Un `deque` est une **liste doublement chaînée de blocs** (ou un tampon circulaire) qui conserve des pointeurs vers les deux extrémités : ajouter ou retirer à gauche ou à droite ne déplace aucun autre élément, d'où O(1). En contrepartie, l'accès par indice au milieu d'un `deque` est en O(n).

## 3.2 Pile, file et file à double entrée

**Exercice 3.2.1**

Écrivez une fonction `parentheses_valides(s)` qui indique si une chaîne composée de `()[]{}` est correctement parenthésée, à l'aide d'une pile. Testez : `"([]{})"`, `"([)]"`, `"(("`, `""`.

**Correction**

```python
def parentheses_valides(s):
    ouvrantes = "([{"
    paires = {")": "(", "]": "[", "}": "{"}
    pile = []
    for c in s:
        if c in ouvrantes:
            pile.append(c)
        elif c in paires:
            if not pile or pile.pop() != paires[c]:
                return False
    return not pile          # la pile doit être vide à la fin


print(parentheses_valides("([]{})"))  # True
print(parentheses_valides("([)]"))    # False : ')' arrive alors que le sommet est '['
print(parentheses_valides("(("))      # False : la pile n'est pas vide
print(parentheses_valides(""))        # True
```

Complexité : O(n) en temps, O(n) en espace.

**Exercice 3.2.2**

Implémentez une classe `FileAvecDeuxPiles` offrant `enfiler(x)` et `defiler()` en n'utilisant que deux piles (listes avec `append` / `pop`). Quelle est la complexité amortie de `defiler` ?

**Correction**

On utilise une pile d'**entrée** et une pile de **sortie**. Quand la pile de sortie est vide, on y transfère tous les éléments de la pile d'entrée (ce qui inverse leur ordre et restitue l'ordre d'arrivée).

```python
class FileAvecDeuxPiles:
    def __init__(self):
        self.entree = []
        self.sortie = []

    def enfiler(self, x):
        self.entree.append(x)

    def defiler(self):
        if not self.sortie:
            while self.entree:
                self.sortie.append(self.entree.pop())
        if not self.sortie:
            raise IndexError("file vide")
        return self.sortie.pop()


f = FileAvecDeuxPiles()
for x in (1, 2, 3):
    f.enfiler(x)
print(f.defiler(), f.defiler())  # 1 2
f.enfiler(4)
print(f.defiler(), f.defiler())  # 3 4
```

Complexité amortie de `defiler` : **O(1)**. Chaque élément est empilé deux fois et dépilé deux fois au plus (entrée puis sortie), donc `n` opérations coûtent O(n) au total, même si un `defiler` isolé peut coûter O(n).

**Exercice 3.2.3**

Résolvez le problème de Josèphe : `n` personnes sont placées en cercle, on élimine une personne sur `k` jusqu'à ce qu'il n'en reste qu'une. Écrivez `josephe(n, k)` avec une `deque` et renvoyez la position du survivant.

**Correction**

On fait tourner le cercle de `k − 1` positions, puis on élimine la personne en tête.

```python
from collections import deque


def josephe(n, k):
    cercle = deque(range(1, n + 1))
    while len(cercle) > 1:
        cercle.rotate(-(k - 1))   # amène la k-ième personne en tête
        cercle.popleft()          # elle est éliminée
    return cercle[0]


print(josephe(7, 3))   # 4
print(josephe(41, 3))  # 31 (problème historique de Flavius Josèphe)
```

Complexité : O(n · k) (chaque rotation coûte O(k)). Il existe aussi une récurrence O(n) : `J(1) = 0`, `J(m) = (J(m − 1) + k) mod m` (positions comptées à partir de 0).

**Exercice 3.2.4**

Évaluez une expression en notation polonaise inverse (par exemple `"3 4 + 2 *"`) à l'aide d'une pile.

**Correction**

```python
def evaluer_npi(expression):
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }
    pile = []
    for jeton in expression.split():
        if jeton in operations:
            b = pile.pop()          # opérande de droite d'abord
            a = pile.pop()
            pile.append(operations[jeton](a, b))
        else:
            pile.append(float(jeton))
    return pile.pop()


print(evaluer_npi("3 4 + 2 *"))   # 14.0
print(evaluer_npi("5 1 2 + 4 * + 3 -"))  # 14.0
```

Déroulement pour `"3 4 + 2 *"` : pile `[3]`, `[3, 4]`, `+` donne `[7]`, `[7, 2]`, `*` donne `[14]`.

**Exercice 3.2.5**

Mesurez le temps de `n` retraits en tête avec `list.pop(0)` puis avec `deque.popleft()` pour `n = 10⁵`. Commentez.

**Correction**

```python
import timeit
from collections import deque

n = 10**5
t_liste = timeit.timeit("l = list(range(n))\nwhile l: l.pop(0)",
                        globals={"n": n}, number=1)
t_deque = timeit.timeit("d = deque(range(n))\nwhile d: d.popleft()",
                        globals={"n": n, "deque": deque}, number=1)
print(t_liste, t_deque)
```

Résultat typique : environ 0,8 s pour `list.pop(0)` contre environ 4 ms pour `deque.popleft()`, soit un rapport de plusieurs centaines. `list.pop(0)` est en O(n) (décalage de tous les éléments), donc `n` retraits coûtent O(n²), alors que `popleft()` est en O(1), soit O(n) au total. Le rapport croît avec `n`.

## 3.3 Liste chaînée

**Exercice 3.3.1**

À partir de la classe `Noeud`, écrivez les fonctions suivantes : `longueur(tete)`, `inserer_en_tete(tete, valeur)`, `inserer_en_queue(tete, valeur)`, `supprimer(tete, valeur)` (première occurrence), `vers_liste(tete)` (liste Python des valeurs).

**Correction**

```python
class Noeud:
    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant


def longueur(tete):
    n = 0
    while tete is not None:
        n += 1
        tete = tete.suivant
    return n


def inserer_en_tete(tete, valeur):
    return Noeud(valeur, tete)            # nouvelle tête


def inserer_en_queue(tete, valeur):
    nouveau = Noeud(valeur)
    if tete is None:
        return nouveau
    courant = tete
    while courant.suivant is not None:
        courant = courant.suivant
    courant.suivant = nouveau
    return tete


def supprimer(tete, valeur):
    if tete is None:
        return None
    if tete.valeur == valeur:             # la tête est supprimée
        return tete.suivant
    courant = tete
    while courant.suivant is not None:
        if courant.suivant.valeur == valeur:
            courant.suivant = courant.suivant.suivant
            break
        courant = courant.suivant
    return tete


def vers_liste(tete):
    resultat = []
    while tete is not None:
        resultat.append(tete.valeur)
        tete = tete.suivant
    return resultat
```

Complexités : `longueur`, `inserer_en_queue`, `supprimer`, `vers_liste` en O(n) ; `inserer_en_tete` en O(1).

**Exercice 3.3.2**

Écrivez une version **récursive** de `inverser(tete)`.

**Correction**

```python
def inverser(tete):
    if tete is None or tete.suivant is None:   # cas de base
        return tete
    nouvelle_tete = inverser(tete.suivant)     # inverse le reste
    tete.suivant.suivant = tete                # le suivant pointe vers nous
    tete.suivant = None                        # nous devenons la fin
    return nouvelle_tete
```

Pour `1 → 2 → 3`, l'appel sur `3` renvoie `3` ; au retour sur `2`, on fait `3.suivant = 2` et `2.suivant = None` ; au retour sur `1`, on fait `2.suivant = 1` et `1.suivant = None`, d'où `3 → 2 → 1`. Complexité O(n) en temps et O(n) en pile d'appels.

**Exercice 3.3.3**

Écrivez `milieu(tete)` qui renvoie le nœud du milieu en un seul parcours.

**Correction**

Méthode des deux pointeurs : `lent` avance d'un nœud, `rapide` de deux. Quand `rapide` atteint la fin, `lent` est au milieu.

```python
def milieu(tete):
    lent = rapide = tete
    while rapide is not None and rapide.suivant is not None:
        lent = lent.suivant
        rapide = rapide.suivant.suivant
    return lent
```

Pour une longueur paire, la fonction renvoie le **deuxième** des deux nœuds centraux. Complexité O(n), espace O(1).

**Exercice 3.3.4**

Écrivez `fusionner(a, b)` qui fusionne deux listes chaînées triées en une liste chaînée triée.

**Correction**

```python
def fusionner(a, b):
    sentinelle = Noeud(None)
    queue = sentinelle
    while a is not None and b is not None:
        if a.valeur <= b.valeur:      # <= : fusion stable
            queue.suivant, a = a, a.suivant
        else:
            queue.suivant, b = b, b.suivant
        queue = queue.suivant
    queue.suivant = a if a is not None else b   # reste de l'une des listes
    return sentinelle.suivant
```

Complexité O(n + m) en temps, O(1) en espace (les nœuds sont réutilisés, aucune copie).

**Exercice 3.3.5** *(défi)*

Écrivez `supprimer_nieme_depuis_la_fin(tete, n)` en un seul parcours.

**Correction**

On crée une sentinelle devant la tête (pour gérer la suppression de la tête), on avance `rapide` de `n` nœuds, puis on avance `rapide` et `lent` ensemble jusqu'à ce que `rapide` soit au dernier nœud : `lent` est alors juste avant le nœud à supprimer.

```python
def supprimer_nieme_depuis_la_fin(tete, n):
    sentinelle = Noeud(None, tete)
    rapide = lent = sentinelle
    for _ in range(n):
        rapide = rapide.suivant
    while rapide.suivant is not None:
        rapide = rapide.suivant
        lent = lent.suivant
    lent.suivant = lent.suivant.suivant
    return sentinelle.suivant
```

Un seul parcours, O(L) en temps pour une liste de longueur L, O(1) en espace (on suppose `1 ≤ n ≤ L`).

## 3.4 Tas et file de priorité

**Exercice 3.4.1**

Écrivez `k_plus_grands(t, k)` qui renvoie les `k` plus grands éléments d'une liste avec un tas-min de taille `k`. Quelle est la complexité en fonction de `n` et `k` ?

**Correction**

On garde dans un tas-min les `k` plus grands éléments rencontrés ; la racine est le plus petit d'entre eux et sert de seuil.

```python
import heapq


def k_plus_grands(t, k):
    tas = []
    for x in t:
        if len(tas) < k:
            heapq.heappush(tas, x)
        elif x > tas[0]:
            heapq.heapreplace(tas, x)   # retire le minimum et insère x
    return sorted(tas, reverse=True)


print(k_plus_grands([5, 1, 9, 3, 7, 2, 8], 3))  # [9, 8, 7]
```

Complexité : **O(n log k)** en temps (chaque élément coûte au plus une opération en O(log k)), **O(k)** en espace.

**Exercice 3.4.2**

Implémentez une classe `TasMax` à l'aide de `heapq` (astuce de l'opposé) avec `inserer`, `extraire_max` et `max`.

**Correction**

`heapq` ne fournit qu'un tas-min : on stocke les **opposés** des valeurs.

```python
import heapq


class TasMax:
    def __init__(self):
        self._tas = []

    def inserer(self, x):
        heapq.heappush(self._tas, -x)

    def extraire_max(self):
        return -heapq.heappop(self._tas)

    def max(self):
        return -self._tas[0]

    def __len__(self):
        return len(self._tas)


t = TasMax()
for x in (4, 9, 1):
    t.inserer(x)
print(t.max(), t.extraire_max(), t.max())  # 9 9 4
```

`inserer` et `extraire_max` : O(log n) ; `max` : O(1).

**Exercice 3.4.3**

Fusionnez `k` listes triées en une seule liste triée avec un tas. Quelle est la complexité ?

**Correction**

```python
import heapq


def fusionner_k_listes(listes):
    tas = [(l[0], i, 0) for i, l in enumerate(listes) if l]
    heapq.heapify(tas)
    resultat = []
    while tas:
        valeur, i, j = heapq.heappop(tas)
        resultat.append(valeur)
        if j + 1 < len(listes[i]):
            heapq.heappush(tas, (listes[i][j + 1], i, j + 1))
    return resultat


print(fusionner_k_listes([[1, 4, 7], [2, 5], [3, 6, 8, 9]]))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Le tas contient au plus `k` éléments (un par liste) ; chaque élément est inséré et extrait une fois. Pour `N` éléments au total : **O(N log k)** en temps, O(k) en espace supplémentaire (hors résultat). (La bibliothèque propose aussi `heapq.merge`.)

**Exercice 3.4.4** *(défi)*

Maintenez la médiane d'un flux d'entiers avec deux tas. Écrivez une classe `Mediane` avec `ajouter(x)` et `valeur()`.

**Correction**

On maintient un tas-max pour la moitié basse et un tas-min pour la moitié haute, de tailles égales ou différant de 1.

```python
import heapq


class Mediane:
    def __init__(self):
        self.bas = []     # tas-max (valeurs opposées)
        self.haut = []    # tas-min

    def ajouter(self, x):
        if not self.bas or x <= -self.bas[0]:
            heapq.heappush(self.bas, -x)
        else:
            heapq.heappush(self.haut, x)
        # rééquilibrage : len(bas) = len(haut) ou len(haut) + 1
        if len(self.bas) > len(self.haut) + 1:
            heapq.heappush(self.haut, -heapq.heappop(self.bas))
        elif len(self.haut) > len(self.bas):
            heapq.heappush(self.bas, -heapq.heappop(self.haut))

    def valeur(self):
        if len(self.bas) > len(self.haut):
            return -self.bas[0]
        return (-self.bas[0] + self.haut[0]) / 2


m = Mediane()
for x in (5, 2, 8, 1):
    m.ajouter(x)
    print(m.valeur())     # 5, 3.5, 5, 3.5
```

`ajouter` : O(log n) ; `valeur` : O(1).

**Exercice 3.4.5**

Simulez à la main l'insertion successive de `5, 3, 8, 1, 9, 2` dans un tas-min, puis les trois premières extractions. Dessinez le tas après chaque opération.

**Correction**

On représente le tas par un tableau (les enfants de l'indice `i` sont `2i + 1` et `2i + 2`) et par ses niveaux.

**Insertions** (insertion en fin de tableau, puis remontée) :

| Opération | Tableau | Niveaux (0 / 1 / 2) |
| --- | --- | --- |
| insérer 5 | `[5]` | 5 |
| insérer 3 (3 < 5 : échange) | `[3, 5]` | 3 / 5 |
| insérer 8 | `[3, 5, 8]` | 3 / 5 8 |
| insérer 1 (échange avec 5, puis avec 3) | `[1, 3, 8, 5]` | 1 / 3 8 / 5 |
| insérer 9 (9 > 3 : reste) | `[1, 3, 8, 5, 9]` | 1 / 3 8 / 5 9 |
| insérer 2 (échange avec 8, 2 > 1 : stop) | `[1, 3, 2, 5, 9, 8]` | 1 / 3 2 / 5 9 8 |

**Extractions** (on place le dernier élément à la racine puis on le fait descendre) :

| Opération | Détail | Tableau obtenu |
| --- | --- | --- |
| extraire : renvoie 1 | 8 monte en racine, échange avec le plus petit enfant 2 | `[2, 3, 8, 5, 9]` |
| extraire : renvoie 2 | 9 en racine, échange avec 3, puis avec 5 | `[3, 5, 8, 9]` |
| extraire : renvoie 3 | 9 en racine, échange avec 5 | `[5, 9, 8]` |

Les trois premiers éléments extraits sont `1, 2, 3` (ordre croissant).

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

**Correction**

```text
         8
       /   \
      3     10
     / \      \
    1   6      14
       / \    /
      4   7  13
```

- **Préfixe** (racine, gauche, droite) : `8, 3, 1, 6, 4, 7, 10, 14, 13`
- **Infixe** (gauche, racine, droite) : `1, 3, 4, 6, 7, 8, 10, 13, 14` (ordre croissant : c'est un ABR)
- **Suffixe** (gauche, droite, racine) : `1, 4, 7, 6, 3, 13, 14, 10, 8`
- **En largeur** (niveau par niveau) : `8, 3, 10, 1, 6, 14, 4, 7, 13`

**Exercice 3.5.2**

Écrivez les parcours préfixe, suffixe et en largeur (avec une `deque`) sur la classe `NoeudArbre`.

**Correction**

```python
from collections import deque


class NoeudArbre:
    def __init__(self, valeur, gauche=None, droite=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite


def prefixe(n, res=None):
    if res is None:
        res = []
    if n is not None:
        res.append(n.valeur)
        prefixe(n.gauche, res)
        prefixe(n.droite, res)
    return res


def suffixe(n, res=None):
    if res is None:
        res = []
    if n is not None:
        suffixe(n.gauche, res)
        suffixe(n.droite, res)
        res.append(n.valeur)
    return res


def largeur(racine):
    res = []
    if racine is None:
        return res
    file = deque([racine])
    while file:
        n = file.popleft()
        res.append(n.valeur)
        if n.gauche:
            file.append(n.gauche)
        if n.droite:
            file.append(n.droite)
    return res
```

Les trois parcours sont en O(n) ; la file du parcours en largeur contient au plus la largeur maximale de l'arbre.

**Exercice 3.5.3**

Écrivez `hauteur(n)`, `nombre_noeuds(n)` et `nombre_feuilles(n)` pour un arbre binaire.

**Correction**

Convention : la hauteur d'un arbre vide vaut `-1` (donc une feuille seule a pour hauteur 0, mesurée en arêtes). On peut aussi choisir 0 pour l'arbre vide si l'on compte les nœuds.

```python
def hauteur(n):
    if n is None:
        return -1
    return 1 + max(hauteur(n.gauche), hauteur(n.droite))


def nombre_noeuds(n):
    if n is None:
        return 0
    return 1 + nombre_noeuds(n.gauche) + nombre_noeuds(n.droite)


def nombre_feuilles(n):
    if n is None:
        return 0
    if n.gauche is None and n.droite is None:
        return 1
    return nombre_feuilles(n.gauche) + nombre_feuilles(n.droite)
```

Chacune est en O(n) en temps et O(h) en pile d'appels (h = hauteur).

**Exercice 3.5.4**

Implémentez l'insertion et la recherche dans un arbre binaire de recherche. Quelle est la hauteur obtenue en insérant `1, 2, 3, 4, 5` dans cet ordre ? Qu'en conclure ?

**Correction**

```python
def inserer(n, valeur):
    if n is None:
        return NoeudArbre(valeur)
    if valeur < n.valeur:
        n.gauche = inserer(n.gauche, valeur)
    elif valeur > n.valeur:
        n.droite = inserer(n.droite, valeur)
    return n                      # les doublons sont ignorés


def chercher(n, valeur):
    while n is not None:
        if valeur == n.valeur:
            return n
        n = n.gauche if valeur < n.valeur else n.droite
    return None


racine = None
for x in (1, 2, 3, 4, 5):
    racine = inserer(racine, x)
print(hauteur(racine))            # 4
```

En insérant `1, 2, 3, 4, 5` dans cet ordre, chaque valeur devient le fils droit de la précédente : l'arbre est une **chaîne** de hauteur 4 (soit `n − 1`). Conclusion : sans équilibrage, un ABR dégénère en liste chaînée et ses opérations deviennent O(n) au lieu de O(log n) ; il faut des arbres auto-équilibrés (AVL, rouge-noir) ou mélanger les insertions.

**Exercice 3.5.5**

Écrivez `est_abr(n)` qui vérifie qu'un arbre binaire est un arbre binaire de recherche valide. Piège à éviter : comparer uniquement avec les enfants directs.

**Correction**

Piège : comparer uniquement un nœud avec ses enfants directs ne suffit pas, car un descendant à droite du sous-arbre gauche peut être plus grand que la racine. Il faut propager des **bornes** `(minimum, maximum)` le long de la descente.

```python
def est_abr(n, bas=float("-inf"), haut=float("inf")):
    if n is None:
        return True
    if not (bas < n.valeur < haut):
        return False
    return (est_abr(n.gauche, bas, n.valeur) and
            est_abr(n.droite, n.valeur, haut))
```

Contre-exemple du piège : racine 5, fils gauche 3, dont le fils droit est 6. Chaque nœud est cohérent avec ses enfants directs, mais 6 > 5 se trouve dans le sous-arbre gauche. Complexité O(n).

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

**Correction**

1. **Annuler la dernière action** : une **pile** (dernier entré, premier sorti).
2. **Parcours en largeur d'un graphe** : une **file** (`deque`).
3. **Compter les mots d'un texte** : un **dictionnaire** (table de hachage), ou `Counter`.
4. **Traiter la tâche la plus urgente** : une **file de priorité** (tas).
5. **Liste triée avec de nombreuses insertions** : un **arbre binaire de recherche équilibré** (ou une structure du type `SortedList`) ; un tableau trié coûterait O(n) par insertion.
6. **Autocomplétion** : un **trie** (arbre préfixe).
7. **Tester si un élément a déjà été vu** : un **ensemble** (`set`), test en O(1) en moyenne.

---

# 4. Récursivité de base

## 4.1 Qu'est-ce que la récursivité ?

**Exercice 4.1.1**

Écrivez de manière récursive : `somme(n)` (somme des entiers de 1 à `n`), `compte_a_rebours(n)` (affiche `n, n−1, …, 1`), `longueur(t)` (longueur d'une liste sans `len`).

**Correction**

```python
def somme(n):
    if n == 0:                      # cas de base
        return 0
    return n + somme(n - 1)


def compte_a_rebours(n):
    if n == 0:                      # cas de base : rien à afficher
        return
    print(n)
    compte_a_rebours(n - 1)


def longueur(t):
    if not t:                       # liste vide
        return 0
    return 1 + longueur(t[1:])


print(somme(4))            # 10
compte_a_rebours(3)        # 3, 2, 1
print(longueur([5, 6, 7])) # 3
```

**Exercice 4.1.2**

Donnez une définition récursive (cas de base et relation de récurrence) de : la somme des chiffres d'un entier, le nombre de `1` dans l'écriture binaire d'un entier, et le maximum d'une liste.

**Correction**

- **Somme des chiffres** `s(n)` : cas de base `s(n) = n` si `n < 10` ; récurrence `s(n) = (n mod 10) + s(n // 10)`.
- **Nombre de `1` en binaire** `b(n)` : cas de base `b(0) = 0` ; récurrence `b(n) = (n mod 2) + b(n // 2)`.
- **Maximum d'une liste** `m(t)` : cas de base `m([x]) = x` ; récurrence `m(t) = max(t[0], m(t[1:]))`.

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

**Correction**

| Fonction | Cas de base | Appel récursif | Quantité qui décroît |
| --- | --- | --- | --- |
| `a` | `n <= 1` : renvoie 1 | `a(n - 1)` | `n` (c'est la factorielle) |
| `b` | `t` vide : renvoie 0 | `b(t[1:])` | la longueur de `t` (somme des éléments) |
| `c` | `y == 0` : renvoie `x` | `c(y, x % y)` | `y`, car `x % y < y` (algorithme d'Euclide, PGCD) |

**Exercice 4.2.2**

Écrivez `puissance(x, n)` de manière récursive pour `n ≥ 0`. Donnez le cas de base, la relation de récurrence, et la complexité.

**Correction**

- **Cas de base** : `x⁰ = 1`.
- **Relation de récurrence** : `xⁿ = x × xⁿ⁻¹` pour `n ≥ 1`.

```python
def puissance(x, n):
    if n == 0:
        return 1
    return x * puissance(x, n - 1)
```

Complexité : `T(n) = T(n − 1) + O(1)`, donc **O(n)** multiplications et une profondeur de récursion de `n`. (La version rapide de l'exercice 4.5.5 réduit cela à O(log n).)

## 4.3 Fonctionnement : la pile d'appels

**Exercice 4.3.1**

Dessinez l'état de la pile d'appels, à chaque étape, pour `factorielle(4)`, puis écrivez l'ordre dans lequel les valeurs sont renvoyées.

**Correction**

Avec le cas de base `factorielle(n) = 1` si `n <= 1`, la pile (le sommet est en bas) évolue ainsi :

```text
factorielle(4)
factorielle(4)  factorielle(3)
factorielle(4)  factorielle(3)  factorielle(2)
factorielle(4)  factorielle(3)  factorielle(2)  factorielle(1)   <- cas de base, renvoie 1
factorielle(4)  factorielle(3)  factorielle(2)                   <- renvoie 2 * 1 = 2
factorielle(4)  factorielle(3)                                   <- renvoie 3 * 2 = 6
factorielle(4)                                                   <- renvoie 4 * 6 = 24
```

Ordre dans lequel les valeurs sont renvoyées : `1, 2, 6, 24`. La pile atteint une hauteur maximale de 4 cadres.

**Exercice 4.3.2**

Quelle est la profondeur maximale de la pile pour `somme(n)` de l'exercice 4.1.1 ? Pour quelles valeurs de `n` obtient-on une `RecursionError` en Python ? Comment consulter et modifier la limite ?

**Correction**

`somme(n)` empile les appels `somme(n)`, `somme(n − 1)`, ..., `somme(0)` : la **profondeur maximale est `n + 1`** cadres (O(n)).

En Python la limite par défaut est de 1000 appels imbriqués : une `RecursionError` apparaît quand `n + 1` dépasse cette limite (en pratique pour `n` autour de 990 à 1000, car quelques cadres sont déjà occupés par le programme appelant).

```python
import sys
print(sys.getrecursionlimit())     # 1000 par défaut
sys.setrecursionlimit(10_000)      # relève la limite (avec prudence)
```

Relever la limite ne supprime pas le coût mémoire et peut provoquer un plantage de l'interpréteur si elle est trop haute ; une version itérative est plus sûre.

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

**Correction**

- `f1` : **pas de cas de base**, la récursion ne s'arrête jamais (`RecursionError`). Correction : ajouter `if n == 0: return 1`.
- `f2` : le cas de base existe mais l'appel `f2(n + 1)` **s'éloigne** du cas de base. Correction : `return f2(n - 1)`.
- `f3` : l'appel `f3(t)` est fait avec **la même liste**, il n'y a aucune progression (et `len(t) == 0` n'est pas géré). Correction : `return max(t[0], f3(t[1:]))`.
- `f4` : correcte mais **inefficace** : elle effectue deux appels identiques à chaque niveau et renvoie `2ⁿ`. Correction : `return 2 * f4(n - 1)` (un seul appel).

```python
def f1(n):
    if n == 0:
        return 1
    return n * f1(n - 1)

def f2(n):
    if n == 0:
        return 0
    return f2(n - 1)

def f3(t):
    if len(t) == 1:
        return t[0]
    return max(t[0], f3(t[1:]))

def f4(n):
    if n == 0:
        return 1
    return 2 * f4(n - 1)
```

**Exercice 4.4.2**

Expliquez pourquoi la fonction `f4` ci-dessus est inutilement lente, et donnez sa complexité.

**Correction**

`f4` effectue deux appels récursifs identiques `f4(n − 1)` : le nombre d'appels vérifie `C(n) = 2C(n − 1) + 1`, soit `C(n) = 2ⁿ⁺¹ − 1`, donc une complexité **O(2ⁿ)**. Or la valeur renvoyée est simplement `2ⁿ` : on recalcule inutilement deux fois la même chose. Avec un seul appel, la complexité devient **O(n)**, et avec `2 ** n` elle devient quasi constante.

## 4.5 Exemples classiques

**Exercice 4.5.1**

Écrivez `fib(n)` de manière récursive naïve. Dessinez l'arbre d'appels pour `fib(5)` et comptez le nombre total d'appels.

**Correction**

```python
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

Arbre d'appels pour `fib(5)` :

```text
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2)
│   │   │   ├── fib(1)
│   │   │   └── fib(0)
│   │   └── fib(1)
│   └── fib(2)
│       ├── fib(1)
│       └── fib(0)
└── fib(3)
    ├── fib(2)
    │   ├── fib(1)
    │   └── fib(0)
    └── fib(1)
```

Nombre total d'appels : **15**. En notant `C(n)` le nombre d'appels, `C(0) = C(1) = 1` et `C(n) = 1 + C(n − 1) + C(n − 2)` : `C(2) = 3`, `C(3) = 5`, `C(4) = 9`, `C(5) = 15`. La croissance est exponentielle (environ `1,618ⁿ`).

**Exercice 4.5.2**

Corrigez `fib` par mémoïsation de trois manières : avec un dictionnaire, avec `functools.cache`, et en passant un paramètre `memo`. Comparez les temps pour `n = 35`.

**Correction**

```python
import functools
import timeit

# 1. Dictionnaire global
memo_global = {}
def fib_dict(n):
    if n < 2:
        return n
    if n not in memo_global:
        memo_global[n] = fib_dict(n - 1) + fib_dict(n - 2)
    return memo_global[n]

# 2. functools.cache
@functools.cache
def fib_cache(n):
    if n < 2:
        return n
    return fib_cache(n - 1) + fib_cache(n - 2)

# 3. Paramètre memo
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n < 2:
        return n
    if n not in memo:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

print(fib_dict(35), fib_cache(35), fib_memo(35))   # 9227465 pour les trois
```

Comparaison pour `n = 35` : la version naïve met environ 0,9 s (environ 3 × 10⁷ appels), tandis que les trois versions mémoïsées s'exécutent en quelques microsecondes (70 appels environ). La complexité passe de O(φⁿ) à **O(n)** : chaque sous-problème est calculé une seule fois. Attention : `fib_dict` et `fib_cache` conservent leur cache entre appels, ce qui fausse un chronométrage répété ; `fib_memo` repart d'un dictionnaire vide à chaque appel.

**Exercice 4.5.3**

Écrivez de manière récursive : l'inversion d'une chaîne, un test de palindrome, la somme des chiffres d'un entier, le PGCD de deux entiers.

**Correction**

```python
def inverser(s):
    if len(s) <= 1:
        return s
    return inverser(s[1:]) + s[0]


def est_palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and est_palindrome(s[1:-1])


def somme_chiffres(n):
    if n < 10:
        return n
    return n % 10 + somme_chiffres(n // 10)


def pgcd(a, b):
    if b == 0:
        return a
    return pgcd(b, a % b)


print(inverser("abc"))            # cba
print(est_palindrome("radar"))    # True
print(somme_chiffres(1234))       # 10
print(pgcd(252, 105))             # 21
```

**Exercice 4.5.4**

Écrivez `hanoi(n, source, cible, auxiliaire)` qui affiche les déplacements. Combien de déplacements pour `n = 5` ? Pour `n` quelconque ?

**Correction**

```python
def hanoi(n, source, cible, auxiliaire):
    if n == 0:
        return
    hanoi(n - 1, source, auxiliaire, cible)     # déplace n-1 disques vers l'auxiliaire
    print(f"{source} -> {cible}")               # déplace le plus grand disque
    hanoi(n - 1, auxiliaire, cible, source)     # remet les n-1 disques sur la cible


hanoi(3, "A", "C", "B")
```

Le nombre de déplacements vérifie `D(n) = 2D(n − 1) + 1` avec `D(0) = 0`, donc `D(n) = 2ⁿ − 1`. Pour `n = 5` : **31 déplacements**. Pour `n` quelconque : **2ⁿ − 1**.

**Exercice 4.5.5**

Écrivez la puissance rapide récursive (`x**n` en O(log n) multiplications). Combien de multiplications pour `n = 1000` ?

**Correction**

```python
def puissance_rapide(x, n):
    if n == 0:
        return 1
    moitie = puissance_rapide(x, n // 2)
    if n % 2 == 0:
        return moitie * moitie
    return moitie * moitie * x
```

On utilise `x²ᵏ = (xᵏ)²` et `x²ᵏ⁺¹ = (xᵏ)² × x`. La profondeur est `⌊log₂ n⌋ + 1`, donc la complexité est **O(log n)** multiplications.

Pour `n = 1000` (écriture binaire `1111101000`, 10 chiffres dont 6 valent 1) : 9 élévations au carré utiles et 5 multiplications par `x`, soit environ **14 multiplications** (contre 999 pour la méthode naïve).

**Exercice 4.5.6**

Écrivez une recherche binaire récursive dans un tableau trié.

**Correction**

```python
def recherche_binaire_rec(t, x, bas=0, haut=None):
    if haut is None:
        haut = len(t) - 1
    if bas > haut:
        return -1
    milieu = (bas + haut) // 2
    if t[milieu] == x:
        return milieu
    if t[milieu] < x:
        return recherche_binaire_rec(t, x, milieu + 1, haut)
    return recherche_binaire_rec(t, x, bas, milieu - 1)


print(recherche_binaire_rec([1, 3, 5, 7, 9, 11], 7))   # 3
print(recherche_binaire_rec([1, 3, 5, 7, 9, 11], 4))   # -1
```

Complexité : `T(n) = T(n/2) + O(1)`, donc O(log n) ; profondeur de récursion O(log n).

**Exercice 4.5.7**

Écrivez une fonction `aplatir(t)` qui aplatit une liste de listes imbriquées à profondeur arbitraire : `aplatir([1, [2, [3, 4]], 5])` doit donner `[1, 2, 3, 4, 5]`.

**Correction**

```python
def aplatir(t):
    resultat = []
    for element in t:
        if isinstance(element, list):
            resultat.extend(aplatir(element))   # récursion sur la sous-liste
        else:
            resultat.append(element)
    return resultat


print(aplatir([1, [2, [3, 4]], 5]))   # [1, 2, 3, 4, 5]
```

## 4.6 Récursivité ou itération ?

**Exercice 4.6.1**

Convertissez en version itérative : la factorielle, Fibonacci en O(n) temps et O(1) espace, la somme d'une liste.

**Correction**

```python
def factorielle_iter(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


def fib_iter(n):                 # O(n) temps, O(1) espace
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def somme_iter(t):
    s = 0
    for x in t:
        s += x
    return s


print(factorielle_iter(5), fib_iter(10), somme_iter([1, 2, 3]))  # 120 55 6
```

**Exercice 4.6.2**

Convertissez en version récursive : le PGCD itératif d'Euclide, le calcul de `2**n` par boucle.

**Correction**

```python
def pgcd_iter(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def pgcd_rec(a, b):
    return a if b == 0 else pgcd_rec(b, a % b)


def deux_puissance_iter(n):
    r = 1
    for _ in range(n):
        r *= 2
    return r


def deux_puissance_rec(n):
    if n == 0:
        return 1
    return 2 * deux_puissance_rec(n - 1)
```

Version récursive de la puissance de 2 plus rapide : `2 ** n = (2 ** (n // 2)) ** 2` (fois 2 si `n` est impair).

**Exercice 4.6.3**

Comparez les complexités en espace d'une version récursive et d'une version itérative de la factorielle.

**Correction**

- **Récursive** : temps O(n), espace **O(n)** (une pile de `n` cadres d'appel).
- **Itérative** : temps O(n), espace **O(1)** (une seule variable accumulateur).

Les temps sont du même ordre ; la version itérative est préférable en espace et évite la `RecursionError`.

## 4.7 Quand l'utiliser ?

**Exercice 4.7.1**

Pour chaque problème, dites si une solution récursive est naturelle ou si une boucle suffit : somme d'une liste, parcours d'un arbre, calcul de toutes les permutations, parcours d'une liste chaînée, calcul de `n!`, exploration d'un labyrinthe.

**Correction**

| Problème | Choix |
| --- | --- |
| somme d'une liste | une boucle suffit |
| parcours d'un arbre | récursion naturelle (structure elle-même récursive) |
| toutes les permutations | récursion naturelle (retour sur trace) |
| parcours d'une liste chaînée | une boucle suffit |
| calcul de `n!` | une boucle suffit |
| exploration d'un labyrinthe | récursion naturelle (parcours en profondeur avec retour arrière) |

---

# 5. Algorithmes de tri simples

## 5.1 Introduction

**Exercice 5.1.1**

Définissez : tri **stable**, tri **en place**, tri **par comparaisons**. Donnez un exemple de liste de tuples `(nom, âge)` qui montre la différence entre un tri stable et un tri instable lorsqu'on trie sur l'âge.

**Correction**

- **Tri stable** : deux éléments de même clé conservent leur ordre relatif d'origine après le tri.
- **Tri en place** : le tri utilise une quantité de mémoire supplémentaire constante, O(1), en plus du tableau lui-même (les éléments sont réorganisés dans le tableau d'origine).
- **Tri par comparaisons** : l'algorithme ne connaît l'ordre des éléments qu'en les comparant deux à deux (il ne s'appuie pas sur leur valeur numérique, comme le fait le tri par comptage).

Exemple avec la liste `[("Alice", 20), ("Bob", 20), ("Chloé", 15)]` triée sur l'âge :

- tri **stable** : `[("Chloé", 15), ("Alice", 20), ("Bob", 20)]` (Alice reste avant Bob) ;
- tri **instable** (par exemple le tri par sélection par échanges) : le premier passage échange `("Alice", 20)` et `("Chloé", 15)`, ce qui donne `[("Chloé", 15), ("Bob", 20), ("Alice", 20)]` : Bob est maintenant avant Alice.

**Exercice 5.1.2**

Écrivez une fonction `est_trie(t)` qui indique si une liste est triée par ordre croissant, et une fonction `est_stable(avant, apres, cle)` qui vérifie qu'un tri a préservé l'ordre relatif des éléments de même clé.

**Correction**

```python
from collections import defaultdict


def est_trie(t):
    return all(t[i] <= t[i + 1] for i in range(len(t) - 1))


def est_stable(avant, apres, cle):
    """Vrai si, pour chaque clé, les éléments gardent le même ordre relatif."""
    def groupes(liste):
        g = defaultdict(list)
        for x in liste:
            g[cle(x)].append(x)
        return dict(g)

    return groupes(avant) == groupes(apres)


donnees = [("Alice", 20), ("Bob", 20), ("Chloé", 15)]
print(est_trie([1, 2, 2, 5]))                                          # True
print(est_stable(donnees, sorted(donnees, key=lambda p: p[1]),
                 lambda p: p[1]))                                      # True
print(est_stable(donnees, [("Chloé", 15), ("Bob", 20), ("Alice", 20)],
                 lambda p: p[1]))                                      # False
```

Chaque groupe (ensemble des éléments de même clé) doit apparaître dans le même ordre avant et après le tri. Complexité O(n). (Si deux éléments sont totalement identiques, on ne peut pas les distinguer ; on peut ajouter un identifiant pour un test rigoureux.)

## 5.2 Tri à bulles (*Bubble Sort*)

**Exercice 5.2.1**

Déroulez à la main le tri à bulles sur `[5, 1, 4, 2, 8]` : écrivez l'état de la liste après chaque passage.

**Correction**

Tri à bulles de `[5, 1, 4, 2, 8]` :

- **Passage 1** : `(5,1)` échange, `(5,4)` échange, `(5,2)` échange, `(5,8)` pas d'échange. Résultat : `[1, 4, 2, 5, 8]`.
- **Passage 2** : `(1,4)` non, `(4,2)` échange, `(4,5)` non. Résultat : `[1, 2, 4, 5, 8]`.
- **Passage 3** : aucune comparaison ne provoque d'échange ; la liste est triée : `[1, 2, 4, 5, 8]`.

**Exercice 5.2.2**

Implémentez le tri à bulles avec arrêt anticipé (si aucun échange n'a eu lieu pendant un passage). Quelle est la complexité dans le meilleur cas ?

**Correction**

```python
def tri_bulles(t):
    n = len(t)
    for i in range(n - 1):
        echange = False
        for j in range(n - 1 - i):          # les i derniers sont déjà en place
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]
                echange = True
        if not echange:                      # arrêt anticipé
            break
    return t


print(tri_bulles([5, 1, 4, 2, 8]))   # [1, 2, 4, 5, 8]
```

Meilleur cas (liste déjà triée) : un seul passage de `n − 1` comparaisons et aucun échange, donc **O(n)**. Moyen et pire cas : O(n²).

**Exercice 5.2.3**

Modifiez votre implémentation pour qu'elle renvoie le nombre d'échanges effectués. Quel lien y a-t-il avec le nombre d'inversions de la liste ?

**Correction**

```python
def tri_bulles_echanges(t):
    n = len(t)
    echanges = 0
    for i in range(n - 1):
        echange = False
        for j in range(n - 1 - i):
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]
                echanges += 1
                echange = True
        if not echange:
            break
    return echanges


print(tri_bulles_echanges([5, 1, 4, 2, 8]))   # 4
```

Le nombre d'échanges est **exactement égal au nombre d'inversions** de la liste (paires `i < j` avec `t[i] > t[j]`) : un échange de deux éléments adjacents mal ordonnés supprime exactement une inversion, et le tri se termine quand il n'en reste aucune. Pour `[5, 1, 4, 2, 8]` : inversions `(5,1), (5,4), (5,2), (4,2)`, soit 4.

**Exercice 5.2.4**

Écrivez une version qui trie par ordre **décroissant**, puis une version qui trie une liste de chaînes selon leur longueur.

**Correction**

```python
def tri_bulles_decroissant(t):
    n = len(t)
    for i in range(n - 1):
        echange = False
        for j in range(n - 1 - i):
            if t[j] < t[j + 1]:                  # comparaison inversée
                t[j], t[j + 1] = t[j + 1], t[j]
                echange = True
        if not echange:
            break
    return t


def tri_bulles_cle(t, cle):
    n = len(t)
    for i in range(n - 1):
        echange = False
        for j in range(n - 1 - i):
            if cle(t[j]) > cle(t[j + 1]):
                t[j], t[j + 1] = t[j + 1], t[j]
                echange = True
        if not echange:
            break
    return t


print(tri_bulles_decroissant([5, 1, 4, 2, 8]))                   # [8, 5, 4, 2, 1]
print(tri_bulles_cle(["pomme", "kiwi", "fraise", "fig"], len))
# ['fig', 'kiwi', 'pomme', 'fraise']
```

Pour le tri par longueur, le résultat est `['fig', 'kiwi', 'pomme', 'fraise']` (longueurs 3, 4, 5, 6). Comme le tri à bulles est stable, deux chaînes de même longueur gardent leur ordre d'origine.

## 5.3 Tri par sélection (*Selection Sort*)

**Exercice 5.3.1**

Déroulez à la main le tri par sélection sur `[64, 25, 12, 22, 11]` et notez le minimum choisi à chaque étape.

**Correction**

Tri par sélection de `[64, 25, 12, 22, 11]` :

| Étape | Minimum choisi (dans la partie non triée) | Échange | Liste obtenue |
| --- | --- | --- | --- |
| 1 | 11 | avec la position 0 | `[11, 25, 12, 22, 64]` |
| 2 | 12 | avec la position 1 | `[11, 12, 25, 22, 64]` |
| 3 | 22 | avec la position 2 | `[11, 12, 22, 25, 64]` |
| 4 | 25 | déjà en place | `[11, 12, 22, 25, 64]` |

**Exercice 5.3.2**

Implémentez le tri par sélection. Combien de comparaisons effectue-t-il pour une liste de `n` éléments, quelle que soit sa disposition initiale ? Combien d'échanges au maximum ?

**Correction**

```python
def tri_selection(t):
    n = len(t)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if t[j] < t[m]:
                m = j
        if m != i:
            t[i], t[m] = t[m], t[i]
    return t


print(tri_selection([64, 25, 12, 22, 11]))   # [11, 12, 22, 25, 64]
```

Nombre de comparaisons : `(n − 1) + (n − 2) + ... + 1 = n(n − 1)/2`, **quelle que soit la disposition initiale** (le tri n'a pas d'arrêt anticipé). Nombre d'échanges : **au plus `n − 1`**, ce qui est le plus faible des tris simples.

**Exercice 5.3.3**

Montrez par un exemple que le tri par sélection (version avec échanges) n'est pas stable.

**Correction**

Exemple : `[(3, "a"), (3, "b"), (1, "c")]` trié sur la première composante.

1. Le minimum de la liste est `(1, "c")` en position 2 : on l'échange avec la position 0, ce qui donne `[(1, "c"), (3, "b"), (3, "a")]`.
2. Le minimum du reste est `(3, "b")` (première occurrence), déjà en place.

Résultat : `[(1, "c"), (3, "b"), (3, "a")]`. Les éléments `(3, "a")` et `(3, "b")` ont **inversé** leur ordre relatif : le tri par sélection avec échanges n'est pas stable (l'échange à longue distance fait « sauter » un élément par-dessus des éléments de même clé).

## 5.4 Tri par insertion (*Insertion Sort*)

**Exercice 5.4.1**

Déroulez à la main le tri par insertion sur `[12, 11, 13, 5, 6]`.

**Correction**

Tri par insertion de `[12, 11, 13, 5, 6]` (la partie gauche est triée) :

| Itération | Élément inséré | Décalages | Liste obtenue |
| --- | --- | --- | --- |
| `i = 1` | 11 | 12 décalé | `[11, 12, 13, 5, 6]` |
| `i = 2` | 13 | aucun | `[11, 12, 13, 5, 6]` |
| `i = 3` | 5 | 13, 12 et 11 décalés | `[5, 11, 12, 13, 6]` |
| `i = 4` | 6 | 13, 12 et 11 décalés | `[5, 6, 11, 12, 13]` |

**Exercice 5.4.2**

Implémentez le tri par insertion. Combien de décalages effectue-t-il sur une liste déjà triée ? Sur une liste triée par ordre décroissant ?

**Correction**

```python
def tri_insertion(t):
    for i in range(1, len(t)):
        cle = t[i]
        j = i - 1
        while j >= 0 and t[j] > cle:
            t[j + 1] = t[j]          # décalage vers la droite
            j -= 1
        t[j + 1] = cle
    return t


print(tri_insertion([12, 11, 13, 5, 6]))   # [5, 6, 11, 12, 13]
```

- Liste **déjà triée** : **aucun décalage** (`n − 1` comparaisons), soit O(n).
- Liste triée par ordre **décroissant** : le `i`-ième élément est décalé `i` fois, soit `n(n − 1)/2` décalages, donc O(n²).

**Exercice 5.4.3**

Écrivez une version qui trie des tuples `(nom, âge)` par âge en restant stable, puis vérifiez la stabilité avec la fonction `est_stable` de l'exercice 5.1.2.

**Correction**

La stabilité exige de ne décaler que les éléments **strictement** plus grands que la clé.

```python
def tri_insertion_age(t):
    for i in range(1, len(t)):
        courant = t[i]
        j = i - 1
        while j >= 0 and t[j][1] > courant[1]:    # '>' strict : stable
            t[j + 1] = t[j]
            j -= 1
        t[j + 1] = courant
    return t


avant = [("Alice", 20), ("Bob", 20), ("Chloé", 15), ("David", 15)]
apres = tri_insertion_age(avant[:])
print(apres)   # [('Chloé', 15), ('David', 15), ('Alice', 20), ('Bob', 20)]
print(est_stable(avant, apres, lambda p: p[1]))   # True
```

Avec `>=` à la place de `>`, les éléments égaux seraient inversés et `est_stable` renverrait `False`.

**Exercice 5.4.4**

Réécrivez le tri par insertion en utilisant `bisect.insort` pour trouver la position d'insertion. La complexité totale change-t-elle ?

**Correction**

```python
import bisect


def tri_insertion_bisect(t):
    resultat = []
    for x in t:
        bisect.insort(resultat, x)     # insort = insort_right : stable
    return resultat


print(tri_insertion_bisect([12, 11, 13, 5, 6]))   # [5, 6, 11, 12, 13]
```

La recherche de la position coûte O(log n) comparaisons au lieu de O(n), donc le nombre de **comparaisons** total passe à O(n log n). Mais l'insertion elle-même décale les éléments à droite de la position, ce qui coûte O(n) déplacements : la complexité **totale reste O(n²)** dans le pire cas (même si le décalage est une copie mémoire très rapide en pratique). `insort_right` insère après les éléments égaux, ce qui préserve la stabilité.

## 5.5 Comparaison

**Exercice 5.5.1**

Complétez le tableau :

| Tri | Meilleur | Moyen | Pire | Stable | En place |
| --- | --- | --- | --- | --- | --- |
| Bulles | | | | | |
| Sélection | | | | | |
| Insertion | | | | | |

**Correction**

| Tri | Meilleur | Moyen | Pire | Stable | En place |
| --- | --- | --- | --- | --- | --- |
| Bulles | O(n) (avec arrêt anticipé) | O(n²) | O(n²) | Oui | Oui |
| Sélection | O(n²) | O(n²) | O(n²) | Non (version avec échanges) | Oui |
| Insertion | O(n) | O(n²) | O(n²) | Oui | Oui |

**Exercice 5.5.2**

Chronométrez les trois tris sur des listes aléatoires de tailles `10²`, `10³`, `5 × 10³`, puis sur des listes déjà triées et inversées. Commentez les résultats.

**Correction**

```python
import random
import time


def chrono(tri, t):
    copie = t[:]
    debut = time.perf_counter()
    tri(copie)
    return time.perf_counter() - debut


for n in (100, 1000, 5000):
    jeux = {
        "aléatoire": random.sample(range(10 * n), n),
        "trié": list(range(n)),
        "inversé": list(range(n, 0, -1)),
    }
    for nom, t in jeux.items():
        resultats = {f.__name__: chrono(f, t) for f in (tri_bulles, tri_selection, tri_insertion)}
        print(n, nom, {k: f"{v * 1000:.1f} ms" for k, v in resultats.items()})
```

Ordres de grandeur observés pour `n = 5000` (en Python pur) :

| Entrée | Bulles | Sélection | Insertion |
| --- | --- | --- | --- |
| aléatoire | environ 1,0 s | environ 0,35 s | environ 0,3 s |
| déjà triée | moins de 1 ms | environ 0,3 s | moins de 1 ms |
| inversée | environ 1,0 s | environ 0,4 s | environ 0,6 s |

Commentaires : tous sont quadratiques (le temps est multiplié par environ 25 quand `n` est multiplié par 5). Sur liste triée, bulles (avec arrêt anticipé) et insertion sont linéaires, alors que la sélection ne change pas. L'insertion est en général le plus rapide des trois ; le tri à bulles est le plus lent à cause du grand nombre d'échanges.

**Exercice 5.5.3**

Quel tri simple choisiriez-vous pour une liste presque triée ? Pour minimiser le nombre d'écritures en mémoire ? Justifiez.

**Correction**

- **Liste presque triée** : le **tri par insertion**, dont le coût est O(n + I) où `I` est le nombre d'inversions (petit pour une liste presque triée) ; il est en outre stable et en ligne.
- **Minimiser le nombre d'écritures en mémoire** : le **tri par sélection**, qui effectue au plus `n − 1` échanges (contre O(n²) écritures pour les bulles et l'insertion), utile si l'écriture est coûteuse (mémoire flash par exemple).

**Exercice 5.5.4**

Écrivez une fonction `inversions(t)` en O(n²) qui compte le nombre de paires `(i, j)` avec `i < j` et `t[i] > t[j]`.

**Correction**

```python
def inversions(t):
    compte = 0
    n = len(t)
    for i in range(n):
        for j in range(i + 1, n):
            if t[i] > t[j]:
                compte += 1
    return compte


print(inversions([5, 1, 4, 2, 8]))   # 4
print(inversions([3, 2, 1]))         # 3
```

Complexité O(n²). Le nombre maximal d'inversions est `n(n − 1)/2` (liste triée en ordre décroissant). Une version en O(n log n) est proposée à l'exercice 8.2.4.

---

# 6. Algorithmes de recherche

## 6.1 Recherche linéaire

**Exercice 6.1.1**

Écrivez `chercher(t, x)` qui renvoie l'indice de la première occurrence de `x` ou `-1`.

**Correction**

```python
def chercher(t, x):
    for i in range(len(t)):
        if t[i] == x:
            return i
    return -1


print(chercher([4, 8, 15, 16], 15))   # 2
print(chercher([4, 8, 15, 16], 23))   # -1
```

Complexité O(n) au pire.

**Exercice 6.1.2**

Écrivez `toutes_positions(t, x)` qui renvoie la liste de tous les indices où `x` apparaît, puis `derniere_position(t, x)`.

**Correction**

```python
def toutes_positions(t, x):
    return [i for i in range(len(t)) if t[i] == x]


def derniere_position(t, x):
    for i in range(len(t) - 1, -1, -1):     # parcours depuis la fin
        if t[i] == x:
            return i
    return -1


t = [3, 7, 3, 9, 3]
print(toutes_positions(t, 3))     # [0, 2, 4]
print(derniere_position(t, 3))    # 4
```

**Exercice 6.1.3**

Écrivez `chercher_avec_condition(t, predicat)` qui renvoie le premier élément vérifiant un prédicat (par exemple « premier nombre pair supérieur à 10 »).

**Correction**

```python
def chercher_avec_condition(t, predicat):
    for x in t:
        if predicat(x):
            return x
    return None


print(chercher_avec_condition([3, 8, 12, 15, 20], lambda x: x % 2 == 0 and x > 10))  # 12
```

Équivalent concis : `next((x for x in t if predicat(x)), None)`.

## 6.2 Recherche binaire (dichotomique)

**Exercice 6.2.1**

Déroulez à la main la recherche binaire de `11`, puis de `4`, dans `[1, 3, 5, 7, 9, 11, 13]`. Notez `bas`, `haut` et `milieu` à chaque étape.

**Correction**

Recherche dans `t = [1, 3, 5, 7, 9, 11, 13]` (indices 0 à 6).

**Recherche de 11** :

| `bas` | `haut` | `milieu` | `t[milieu]` | Décision |
| --- | --- | --- | --- | --- |
| 0 | 6 | 3 | 7 | 7 < 11 : `bas = 4` |
| 4 | 6 | 5 | 11 | trouvé à l'indice 5 |

**Recherche de 4** :

| `bas` | `haut` | `milieu` | `t[milieu]` | Décision |
| --- | --- | --- | --- | --- |
| 0 | 6 | 3 | 7 | 7 > 4 : `haut = 2` |
| 0 | 2 | 1 | 3 | 3 < 4 : `bas = 2` |
| 2 | 2 | 2 | 5 | 5 > 4 : `haut = 1` |
| 2 | 1 | | | `bas > haut` : absent, résultat `-1` |

**Exercice 6.2.2**

Implémentez la recherche binaire de manière itérative, puis récursive.

**Correction**

```python
def recherche_binaire(t, x):
    bas, haut = 0, len(t) - 1
    while bas <= haut:
        milieu = (bas + haut) // 2
        if t[milieu] == x:
            return milieu
        if t[milieu] < x:
            bas = milieu + 1
        else:
            haut = milieu - 1
    return -1


def recherche_binaire_rec(t, x, bas=0, haut=None):
    if haut is None:
        haut = len(t) - 1
    if bas > haut:
        return -1
    milieu = (bas + haut) // 2
    if t[milieu] == x:
        return milieu
    if t[milieu] < x:
        return recherche_binaire_rec(t, x, milieu + 1, haut)
    return recherche_binaire_rec(t, x, bas, milieu - 1)


t = [1, 3, 5, 7, 9, 11, 13]
print(recherche_binaire(t, 11), recherche_binaire_rec(t, 4))   # 5 -1
```

Complexité O(log n) ; la version itérative utilise O(1) d'espace, la récursive O(log n) de pile.

**Exercice 6.2.3**

Quel est le nombre maximal de comparaisons pour une liste de 1 000 éléments ? De 10⁶ éléments ?

**Correction**

À chaque comparaison, l'intervalle est au moins divisé par 2. Le nombre maximal de comparaisons est `⌊log₂ n⌋ + 1`.

- `n = 1000` : `⌊log₂ 1000⌋ + 1 = 9 + 1 = ` **10** comparaisons.
- `n = 10⁶` : `⌊log₂ 10⁶⌋ + 1 = 19 + 1 = ` **20** comparaisons.

Une recherche linéaire en demanderait jusqu'à 1000 et 10⁶.

**Exercice 6.2.4**

Pourquoi la recherche binaire exige-t-elle un tableau trié ? Donnez un exemple de tableau non trié où l'algorithme échoue.

**Correction**

La recherche binaire se fonde sur l'ordre : après avoir comparé `x` à l'élément du milieu, elle **élimine toute une moitié** en déduisant que `x` ne peut s'y trouver. Si le tableau n'est pas trié, cette déduction est fausse.

Exemple : `t = [5, 1, 9, 3, 7]` et `x = 1`. On a `bas = 0`, `haut = 4`, `milieu = 2`, `t[2] = 9 > 1` : on garde la moitié gauche `[5, 1]`, puis `milieu = 0`, `t[0] = 5 > 1` : on garde la moitié `[]` à gauche de l'indice 0. L'algorithme conclut « absent » alors que `1` est en position 1.

### Variantes : première / dernière position, insertion

**Exercice 6.2.5**

Écrivez `premiere_position(t, x)` et `derniere_position(t, x)` en O(log n) pour un tableau trié avec doublons. En déduire `compter(t, x)`.

**Correction**

On utilise une recherche binaire qui continue après avoir trouvé `x`, pour chercher la frontière.

```python
def premiere_position(t, x):
    bas, haut, res = 0, len(t) - 1, -1
    while bas <= haut:
        milieu = (bas + haut) // 2
        if t[milieu] == x:
            res = milieu
            haut = milieu - 1          # continuer à gauche
        elif t[milieu] < x:
            bas = milieu + 1
        else:
            haut = milieu - 1
    return res


def derniere_position(t, x):
    bas, haut, res = 0, len(t) - 1, -1
    while bas <= haut:
        milieu = (bas + haut) // 2
        if t[milieu] == x:
            res = milieu
            bas = milieu + 1           # continuer à droite
        elif t[milieu] < x:
            bas = milieu + 1
        else:
            haut = milieu - 1
    return res


def compter(t, x):
    p = premiere_position(t, x)
    if p == -1:
        return 0
    return derniere_position(t, x) - p + 1


t = [1, 2, 2, 2, 3, 5, 5]
print(premiere_position(t, 2), derniere_position(t, 2), compter(t, 2))   # 1 3 3
```

Chaque fonction est en O(log n), donc `compter` aussi.

**Exercice 6.2.6**

Écrivez `position_insertion(t, x)` : l'indice où insérer `x` pour garder le tableau trié. Comparez avec `bisect.bisect_left` et `bisect.bisect_right`.

**Correction**

```python
import bisect


def position_insertion(t, x):
    """Premier indice i tel que t[i] >= x (insertion avant les égaux)."""
    bas, haut = 0, len(t)
    while bas < haut:
        milieu = (bas + haut) // 2
        if t[milieu] < x:
            bas = milieu + 1
        else:
            haut = milieu
    return bas


t = [1, 3, 3, 5]
print(position_insertion(t, 3), bisect.bisect_left(t, 3), bisect.bisect_right(t, 3))  # 1 1 3
print(position_insertion(t, 4), position_insertion(t, 0), position_insertion(t, 9))  # 3 0 4
```

`bisect_left(t, x)` renvoie l'indice avant les éléments égaux à `x` (c'est notre fonction) ; `bisect_right(t, x)` renvoie l'indice juste **après** les éléments égaux à `x` (remplacer `t[milieu] < x` par `t[milieu] <= x`).

**Exercice 6.2.7**

Dans un tableau trié, écrivez `plus_petit_superieur(t, x)` : le plus petit élément strictement supérieur à `x`, ou `None`.

**Correction**

Le plus petit élément strictement supérieur à `x` se trouve à l'indice `bisect_right(t, x)`.

```python
import bisect


def plus_petit_superieur(t, x):
    i = bisect.bisect_right(t, x)
    return t[i] if i < len(t) else None


t = [1, 3, 3, 5, 8]
print(plus_petit_superieur(t, 3))   # 5
print(plus_petit_superieur(t, 8))   # None
print(plus_petit_superieur(t, 0))   # 1
```

Complexité O(log n).

## 6.3 Comparaison

**Exercice 6.3.1**

On doit effectuer une seule recherche dans un tableau non trié de `n` éléments, puis `q` recherches sur le même tableau. Pour quelles valeurs de `q` vaut-il la peine de trier d'abord ?

**Correction**

- **Une seule recherche** : la recherche linéaire coûte O(n) ; trier d'abord coûte O(n log n), donc ce n'est jamais rentable.
- **`q` recherches** : sans tri, `q × n` opérations ; avec tri, `n log n + q log n`. Le tri est rentable quand `q · n > n log n + q log n`, c'est-à-dire pour `q > (n log n) / (n − log n)`, soit environ **`q > log₂ n`**.

Exemple : pour `n = 10⁶`, dès qu'on fait plus d'une vingtaine de recherches il vaut mieux trier d'abord. Pour un très grand nombre de recherches, un `set` (O(n) de préparation, O(1) par recherche) est encore meilleur si l'on n'a pas besoin de l'ordre.

**Exercice 6.3.2**

Un tableau trié a été « tourné » : `[6, 7, 8, 1, 2, 3, 4, 5]`. Adaptez la recherche binaire pour y chercher un élément en O(log n). *(défi)*

**Correction**

Dans un tableau trié tourné (éléments distincts), à chaque étape **au moins une des deux moitiés est triée** ; on la détecte et on regarde si `x` s'y trouve.

```python
def chercher_tourne(t, x):
    bas, haut = 0, len(t) - 1
    while bas <= haut:
        milieu = (bas + haut) // 2
        if t[milieu] == x:
            return milieu
        if t[bas] <= t[milieu]:                      # moitié gauche triée
            if t[bas] <= x < t[milieu]:
                haut = milieu - 1
            else:
                bas = milieu + 1
        else:                                        # moitié droite triée
            if t[milieu] < x <= t[haut]:
                bas = milieu + 1
            else:
                haut = milieu - 1
    return -1


t = [6, 7, 8, 1, 2, 3, 4, 5]
print(chercher_tourne(t, 3))   # 5
print(chercher_tourne(t, 7))   # 1
print(chercher_tourne(t, 9))   # -1
```

Complexité O(log n). (Avec des doublons, le pire cas peut dégrader à O(n).)

---

# 7. Algorithmes mathématiques de base

## 7.1 PGCD (algorithme d'Euclide)

**Exercice 7.1.1**

Déroulez à la main l'algorithme d'Euclide pour `pgcd(252, 105)` et pour `pgcd(17, 5)`.

**Correction**

**`pgcd(252, 105)`** :

- `252 = 2 × 105 + 42`
- `105 = 2 × 42 + 21`
- `42 = 2 × 21 + 0`

Le dernier reste non nul est 21, donc `pgcd(252, 105) = 21`.

**`pgcd(17, 5)`** :

- `17 = 3 × 5 + 2`
- `5 = 2 × 2 + 1`
- `2 = 2 × 1 + 0`

Donc `pgcd(17, 5) = 1` (17 et 5 sont premiers entre eux).

**Exercice 7.1.2**

Implémentez `pgcd(a, b)` de manière itérative, puis `ppcm(a, b)` à partir du PGCD.

**Correction**

```python
def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)


def ppcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // pgcd(a, b)


print(pgcd(252, 105))   # 21
print(ppcm(4, 6))       # 12
```

On utilise `ppcm(a, b) = |a · b| / pgcd(a, b)`. Pour éviter un grand produit intermédiaire, on peut écrire `abs(a // pgcd(a, b) * b)`. Complexité de `pgcd` : O(log min(a, b)).

**Exercice 7.1.3**

Écrivez `simplifier(num, den)` qui renvoie une fraction irréductible. Écrivez ensuite l'addition de deux fractions renvoyant une fraction irréductible.

**Correction**

```python
def simplifier(num, den):
    if den == 0:
        raise ZeroDivisionError("dénominateur nul")
    g = pgcd(num, den)
    num, den = num // g, den // g
    if den < 0:                          # dénominateur toujours positif
        num, den = -num, -den
    return num, den


def additionner(f1, f2):
    (a, b), (c, d) = f1, f2
    return simplifier(a * d + c * b, b * d)


print(simplifier(6, 8))               # (3, 4)
print(simplifier(-10, -15))           # (2, 3)
print(additionner((1, 2), (1, 3)))    # (5, 6)
print(additionner((1, 6), (1, 3)))    # (1, 2)
```

**Exercice 7.1.4**

Écrivez `pgcd_liste(t)` qui calcule le PGCD de tous les éléments d'une liste.

**Correction**

Le PGCD est associatif : `pgcd(a, b, c) = pgcd(pgcd(a, b), c)`.

```python
from functools import reduce


def pgcd_liste(t):
    g = 0
    for x in t:
        g = pgcd(g, x)
        if g == 1:              # on ne peut plus descendre
            break
    return g


print(pgcd_liste([12, 18, 24]))     # 6
print(pgcd_liste([7, 13, 21]))      # 1
print(reduce(pgcd, [12, 18, 24]))   # 6
```

**Exercice 7.1.5** *(défi)*

Implémentez l'algorithme d'Euclide étendu : `euclide_etendu(a, b)` renvoie `(g, x, y)` tels que `a·x + b·y = g`.

**Correction**

Invariant : à chaque étape, on exprime le reste comme combinaison de `a` et `b`. Si `b = 0`, `g = a = a·1 + b·0`. Sinon, avec `a = q·b + r` et `g = b·x' + r·y'`, on obtient `g = a·y' + b·(x' − q·y')`.

```python
def euclide_etendu(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = euclide_etendu(b, a % b)
    return g, y1, x1 - (a // b) * y1


print(euclide_etendu(252, 105))   # (21, -2, 5) : 252*(-2) + 105*5 = 21
print(euclide_etendu(17, 5))      # (1, -2, 7)  : 17*(-2) + 5*7 = 1
```

Complexité O(log min(a, b)). Application : inverse modulaire (exercice 16.3.5).

## 7.2 Nombres premiers : test naïf

**Exercice 7.2.1**

Écrivez `est_premier(n)` en testant les diviseurs jusqu'à `√n`. Expliquez pourquoi il suffit de s'arrêter à `√n`.

**Correction**

```python
def est_premier(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


print([est_premier(k) for k in (1, 2, 17, 21, 97)])   # [False, True, True, False, True]
```

**Pourquoi s'arrêter à √n** : si `n = a × b` avec `1 < a ≤ b`, alors `a² ≤ a × b = n`, donc `a ≤ √n`. Tout nombre composé possède donc un diviseur (non trivial) inférieur ou égal à `√n` : si aucun n'existe jusqu'à `√n`, `n` est premier. Complexité : O(√n).

**Exercice 7.2.2**

Affichez tous les nombres premiers inférieurs à 100, puis donnez la complexité du calcul des premiers inférieurs à `N` avec cette méthode.

**Correction**

```python
print([n for n in range(2, 100) if est_premier(n)])
```

Résultat : `2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97` (25 nombres premiers).

Complexité pour trouver tous les premiers inférieurs à `N` avec ce test : chaque test coûte O(√k) pour un nombre `k ≤ N`, donc au total **O(N √N)**. Le crible d'Ératosthène (section 16.1) fait O(N log log N).

**Exercice 7.2.3**

Écrivez `n_ieme_premier(n)` et `premier_suivant(n)`.

**Correction**

```python
def premier_suivant(n):
    n += 1
    while not est_premier(n):
        n += 1
    return n


def n_ieme_premier(n):
    compte, k = 0, 1
    while compte < n:
        k += 1
        if est_premier(k):
            compte += 1
    return k


print(premier_suivant(100))     # 101
print(n_ieme_premier(1))        # 2
print(n_ieme_premier(10))       # 29
print(n_ieme_premier(1000))     # 7919
```

**Exercice 7.2.4**

Trouvez deux nombres premiers jumeaux (différence de 2) supérieurs à 1000.

**Correction**

```python
n = 1001
while not (est_premier(n) and est_premier(n + 2)):
    n += 1
print(n, n + 2)    # 1019 1021
```

Les premiers nombres premiers jumeaux supérieurs à 1000 sont **(1019, 1021)** ; suivent (1031, 1033), (1049, 1051), (1061, 1063).

## 7.3 Factorielle

**Exercice 7.3.1**

Écrivez `factorielle(n)` de manière itérative et vérifiez-la avec `math.factorial`.

**Correction**

```python
import math


def factorielle(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


assert all(factorielle(n) == math.factorial(n) for n in range(0, 30))
print(factorielle(10))   # 3628800
```

**Exercice 7.3.2**

Combien de zéros terminent l'écriture décimale de `100!` ? Écrivez une fonction `zeros_terminaux(n)` qui le calcule sans calculer `n!`.

**Correction**

Chaque zéro final vient d'un facteur 10 = 2 × 5. Dans `n!`, les facteurs 2 sont plus nombreux que les facteurs 5 : le nombre de zéros est donc l'exposant de 5, soit `⌊n/5⌋ + ⌊n/25⌋ + ⌊n/125⌋ + ...`.

```python
def zeros_terminaux(n):
    z, p = 0, 5
    while p <= n:
        z += n // p
        p *= 5
    return z


print(zeros_terminaux(100))   # 24
```

`100!` se termine par **24 zéros** (`20 + 4`). Complexité O(log n).

**Exercice 7.3.3**

Combien de chiffres comporte `1000!` ? Calculez-le à l'aide de Python, puis à l'aide de la somme des logarithmes décimaux.

**Correction**

```python
import math

print(len(str(math.factorial(1000))))                         # 2568
print(int(sum(math.log10(i) for i in range(1, 1001))) + 1)    # 2568
```

`1000!` possède **2568 chiffres**. Le nombre de chiffres d'un entier `N` est `⌊log₁₀ N⌋ + 1`, et `log₁₀(1000!) = Σ log₁₀(i) ≈ 2567,6`, d'où `2567 + 1 = 2568`. Cette méthode évite de calculer l'énorme factorielle.

## 7.4 Suite de Fibonacci

**Exercice 7.4.1**

Écrivez `fib(n)` en O(n) temps et O(1) espace. Affichez les 15 premiers termes.

**Correction**

```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print([fib(i) for i in range(15)])
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
```

Temps O(n), espace O(1) (en comptant les additions d'entiers comme des opérations élémentaires).

**Exercice 7.4.2**

Calculez la somme des termes pairs de la suite de Fibonacci qui ne dépassent pas 4 000 000.

**Correction**

```python
a, b = 0, 1
somme = 0
while a <= 4_000_000:
    if a % 2 == 0:
        somme += a
    a, b = b, a + b
print(somme)     # 4613732
```

La somme des termes pairs de Fibonacci ne dépassant pas 4 000 000 vaut **4 613 732**.

**Exercice 7.4.3**

Quel est le plus petit indice `n` tel que `fib(n)` possède 100 chiffres ?

**Correction**

```python
a, b, n = 0, 1, 0
while len(str(a)) < 100:
    a, b = b, a + b
    n += 1
print(n)    # 476
```

Le plus petit indice est **n = 476** (avec `fib(0) = 0`, `fib(1) = 1`). On peut le retrouver avec la formule de Binet : `fib(n) ≈ φⁿ / √5`, donc `n log₁₀ φ − log₁₀ √5 ≥ 99`, soit `n ≥ 475,4`, d'où 476.

**Exercice 7.4.4**

Montrez, en calculant les premiers termes, que `fib(n)` est pair exactement quand `n` est multiple de 3. Vérifiez numériquement sur les 50 premiers termes.

**Correction**

Premiers termes avec leur parité :

| `n` | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `fib(n)` | 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 |
| parité | pair | impair | impair | pair | impair | impair | pair | impair | impair |

**Preuve** : modulo 2, `fib(n + 2) = fib(n + 1) + fib(n)`. Les parités commencent par `(pair, impair)` puis `impair + pair = impair`, puis `impair + impair = pair`, ce qui redonne `(pair, impair)` : la suite des parités est périodique de période 3, et `fib(n)` est pair exactement pour `n ≡ 0 (mod 3)`.

Vérification numérique :

```python
fibs = [fib(i) for i in range(50)]
print(all((fibs[i] % 2 == 0) == (i % 3 == 0) for i in range(50)))   # True
```

## 7.5 Autres outils intégrés à Python *(ajout)*

**Exercice 7.5.1**

Sans écrire de boucle, utilisez les outils de la bibliothèque standard pour calculer :

1. le nombre de manières de choisir 3 éléments parmi 10 ;
2. le nombre d'arrangements de 4 éléments parmi 8 ;
3. le quotient et le reste de la division de 1000 par 37 ;
4. les trois derniers chiffres de `7¹⁰⁰` ;
5. l'écriture binaire de 255 et la valeur décimale de `"101101"` ;
6. la somme des chiffres de `2¹⁰⁰⁰`.

**Correction**

```python
import math

print(math.comb(10, 3))              # 1. 120 manières de choisir 3 parmi 10
print(math.perm(8, 4))               # 2. 1680 arrangements de 4 parmi 8
print(divmod(1000, 37))              # 3. (27, 1) : 1000 = 27 * 37 + 1
print(pow(7, 100, 1000))             # 4. 1 : les trois derniers chiffres sont 001
print(bin(255), int("101101", 2))    # 5. 0b11111111  45
print(sum(map(int, str(2 ** 1000)))) # 6. 1366
```

Détail pour la question 4 : `pow(a, b, m)` fait de l'exponentiation modulaire rapide ; on obtient `7¹⁰⁰ ≡ 1 (mod 1000)` (le groupe multiplicatif modulo 1000 a un exposant égal à 100), donc les trois derniers chiffres sont `001`.

**Exercice 7.5.2**

Écrivez `est_carre_parfait(n)` à l'aide de `math.isqrt`, sans utiliser de nombres flottants. Pourquoi `int(n ** 0.5) ** 2 == n` est-il risqué pour de grands `n` ?

**Correction**

```python
import math


def est_carre_parfait(n):
    if n < 0:
        return False
    r = math.isqrt(n)       # racine carrée entière exacte
    return r * r == n


print(est_carre_parfait(49), est_carre_parfait(50))       # True False
print(est_carre_parfait((10**16 + 1) ** 2))               # True
```

`int(n ** 0.5) ** 2 == n` est **risqué** pour de grands `n` : `n ** 0.5` passe par des nombres flottants à 53 bits de mantisse, donc la racine perd de la précision au-delà de 2⁵³ (environ 9 × 10¹⁵), et pour `n > 10³⁰⁸` le calcul échoue par dépassement. Exemple : avec `n = (10**16 + 1) ** 2`, `int(n ** 0.5) ** 2 == n` renvoie `False` (la racine flottante vaut `1e16` et non `10**16 + 1`), alors que `n` est bien un carré parfait. `math.isqrt` travaille en arithmétique entière exacte.

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

**Correction**

| Tri | Meilleur | Moyen | Pire | Espace | Stable |
| --- | --- | --- | --- | --- | --- |
| Fusion | O(n log n) | O(n log n) | O(n log n) | O(n) | Oui |
| Rapide | O(n log n) | O(n log n) | O(n²) | O(log n) (pile de récursion) | Non |
| Tas | O(n log n) | O(n log n) | O(n log n) | O(1) (en place) | Non |
| Comptage | O(n + k) | O(n + k) | O(n + k) | O(n + k) | Oui (version à comptages cumulés) |
| Radix | O(d (n + b)) | O(d (n + b)) | O(d (n + b)) | O(n + b) | Oui |

Ici `k` est la valeur maximale, `d` le nombre de chiffres et `b` la base.

**Exercice 8.1.2**

Un tri par comparaisons ne peut pas faire mieux que `Ω(n log n)` dans le pire cas. Justifiez en comptant le nombre de permutations possibles d'une liste de `n` éléments et en utilisant l'arbre de décision.

**Correction**

Une liste de `n` éléments distincts peut être dans `n!` ordres différents, et un tri par comparaisons doit distinguer chacun d'eux. L'exécution de l'algorithme se représente par un **arbre de décision binaire** (chaque nœud est une comparaison, chaque feuille une permutation de sortie) : il possède au moins `n!` feuilles.

Un arbre binaire de hauteur `h` a au plus `2ʰ` feuilles, donc `2ʰ ≥ n!` et `h ≥ log₂(n!)`. Or `n! ≥ (n/2)^(n/2)`, donc `log₂(n!) ≥ (n/2) log₂(n/2) = Ω(n log n)` (ou, par la formule de Stirling, `log₂(n!) ≈ n log₂ n − 1,44 n`). La hauteur est le nombre de comparaisons dans le pire cas : tout tri par comparaisons effectue **Ω(n log n)** comparaisons dans le pire cas.

## 8.2 Tri fusion (*Merge Sort*)

**Exercice 8.2.1**

Déroulez à la main le tri fusion sur `[38, 27, 43, 3, 9, 82, 10]` : dessinez l'arbre des divisions puis celui des fusions.

**Correction**

Tri fusion de `[38, 27, 43, 3, 9, 82, 10]`.

**Arbre des divisions** :

```text
[38, 27, 43, 3, 9, 82, 10]
├── [38, 27, 43, 3]
│   ├── [38, 27]
│   │   ├── [38]
│   │   └── [27]
│   └── [43, 3]
│       ├── [43]
│       └── [3]
└── [9, 82, 10]
    ├── [9]
    └── [82, 10]
        ├── [82]
        └── [10]
```

**Arbre des fusions** (de bas en haut) :

```text
[38] + [27]        -> [27, 38]
[43] + [3]         -> [3, 43]
[27, 38] + [3, 43] -> [3, 27, 38, 43]
[82] + [10]        -> [10, 82]
[9] + [10, 82]     -> [9, 10, 82]
[3, 27, 38, 43] + [9, 10, 82] -> [3, 9, 10, 27, 38, 43, 82]
```

**Exercice 8.2.2**

Implémentez `fusionner(a, b)` qui fusionne deux listes triées, puis `tri_fusion(t)`.

**Correction**

```python
def fusionner(a, b):
    resultat = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:               # <= : l'élément de gauche d'abord (stabilité)
            resultat.append(a[i])
            i += 1
        else:
            resultat.append(b[j])
            j += 1
    resultat.extend(a[i:])
    resultat.extend(b[j:])
    return resultat


def tri_fusion(t):
    if len(t) <= 1:
        return t
    milieu = len(t) // 2
    return fusionner(tri_fusion(t[:milieu]), tri_fusion(t[milieu:]))


print(tri_fusion([38, 27, 43, 3, 9, 82, 10]))   # [3, 9, 10, 27, 38, 43, 82]
```

Récurrence `T(n) = 2T(n/2) + O(n)`, donc O(n log n) dans tous les cas ; espace O(n).

**Exercice 8.2.3**

Pourquoi la fusion préserve-t-elle la stabilité ? Quelle condition faut-il respecter lors de la comparaison de deux éléments égaux ?

**Correction**

La fusion préserve la stabilité parce qu'elle ne fait jamais passer un élément de la moitié droite devant un élément de la moitié gauche, sauf s'il est **strictement plus petit**. Or, dans la liste d'origine, les éléments de la moitié gauche précèdent ceux de la moitié droite.

Condition à respecter : lors de la comparaison de deux éléments égaux, on prend celui de la liste **de gauche** (`a[i] <= b[j]` et non `<`). Avec `<`, les éléments égaux de droite passeraient en premier et la stabilité serait perdue.

**Exercice 8.2.4** *(défi)*

Modifiez le tri fusion pour qu'il compte le nombre d'inversions d'un tableau en O(n log n).

**Correction**

Quand on fusionne et qu'on prend un élément de la moitié droite alors qu'il reste `len(g) − i` éléments dans la moitié gauche, ces éléments sont tous strictement plus grands : chacun forme une inversion avec lui.

```python
def tri_et_inversions(t):
    if len(t) <= 1:
        return t, 0
    m = len(t) // 2
    g, cg = tri_et_inversions(t[:m])
    d, cd = tri_et_inversions(t[m:])
    res, inv = [], cg + cd
    i = j = 0
    while i < len(g) and j < len(d):
        if g[i] <= d[j]:
            res.append(g[i])
            i += 1
        else:
            res.append(d[j])
            j += 1
            inv += len(g) - i          # inversions avec les éléments restants de g
    res.extend(g[i:])
    res.extend(d[j:])
    return res, inv


print(tri_et_inversions([5, 1, 4, 2, 8])[1])   # 4
print(tri_et_inversions([3, 2, 1])[1])         # 3
```

Complexité O(n log n).

**Exercice 8.2.5**

Écrivez une version itérative (ascendante) du tri fusion qui fusionne des blocs de taille 1, 2, 4, 8…

**Correction**

```python
def tri_fusion_iteratif(t):
    t = t[:]
    n = len(t)
    largeur = 1
    while largeur < n:
        for debut in range(0, n, 2 * largeur):
            milieu = min(debut + largeur, n)
            fin = min(debut + 2 * largeur, n)
            t[debut:fin] = fusionner(t[debut:milieu], t[milieu:fin])
        largeur *= 2
    return t


print(tri_fusion_iteratif([38, 27, 43, 3, 9, 82, 10]))   # [3, 9, 10, 27, 38, 43, 82]
```

On fusionne d'abord les blocs de taille 1, puis 2, 4, 8, etc. Même complexité O(n log n), sans récursion.

## 8.3 Tri rapide (*Quick Sort*)

**Exercice 8.3.1**

Déroulez à la main le tri rapide sur `[10, 80, 30, 90, 40, 50, 70]` avec le dernier élément comme pivot (partition de Lomuto).

**Correction**

Tri rapide de `[10, 80, 30, 90, 40, 50, 70]`, pivot = dernier élément, partition de Lomuto.

**Partition 1** (pivot 70, `i` = indice de la dernière valeur ≤ pivot) :

| `j` | `t[j]` | Action | Tableau |
| --- | --- | --- | --- |
| 0 | 10 | ≤ 70 : échange avec `i + 1 = 0` | `[10, 80, 30, 90, 40, 50, 70]` |
| 1 | 80 | > 70 : rien | |
| 2 | 30 | ≤ 70 : échange avec 1 | `[10, 30, 80, 90, 40, 50, 70]` |
| 3 | 90 | > 70 : rien | |
| 4 | 40 | ≤ 70 : échange avec 2 | `[10, 30, 40, 90, 80, 50, 70]` |
| 5 | 50 | ≤ 70 : échange avec 3 | `[10, 30, 40, 50, 80, 90, 70]` |
| fin | | le pivot va en position 4 | `[10, 30, 40, 50, 70, 90, 80]` |

Puis on trie récursivement :

- `[10, 30, 40, 50]` (pivot 50, déjà bien placé) puis `[10, 30, 40]` (pivot 40) puis `[10, 30]` (pivot 30) : la partie gauche est déjà triée.
- `[90, 80]` (pivot 80) : `90 > 80` donc le pivot est échangé avec 90, ce qui donne `[80, 90]`.

Résultat : `[10, 30, 40, 50, 70, 80, 90]`.

**Exercice 8.3.2**

Implémentez le tri rapide fonctionnel (avec listes `gauche`, `milieu`, `droite`), puis sa version en place avec la partition de Lomuto.

**Correction**

```python
def tri_rapide_fonctionnel(t):
    if len(t) <= 1:
        return t
    pivot = t[len(t) // 2]
    gauche = [x for x in t if x < pivot]
    milieu = [x for x in t if x == pivot]
    droite = [x for x in t if x > pivot]
    return tri_rapide_fonctionnel(gauche) + milieu + tri_rapide_fonctionnel(droite)


def partition_lomuto(t, bas, haut):
    pivot = t[haut]
    i = bas - 1
    for j in range(bas, haut):
        if t[j] <= pivot:
            i += 1
            t[i], t[j] = t[j], t[i]
    t[i + 1], t[haut] = t[haut], t[i + 1]
    return i + 1


def tri_rapide(t, bas=0, haut=None):
    if haut is None:
        haut = len(t) - 1
    if bas < haut:
        p = partition_lomuto(t, bas, haut)
        tri_rapide(t, bas, p - 1)
        tri_rapide(t, p + 1, haut)
    return t


print(tri_rapide([10, 80, 30, 90, 40, 50, 70]))   # [10, 30, 40, 50, 70, 80, 90]
```

La version fonctionnelle utilise O(n) de mémoire supplémentaire ; la version en place n'utilise que la pile de récursion.

**Exercice 8.3.3**

Implémentez un pivot choisi au hasard. Pourquoi cela rend-il le pire cas très improbable ?

**Correction**

```python
import random


def tri_rapide_aleatoire(t, bas=0, haut=None):
    if haut is None:
        haut = len(t) - 1
    if bas < haut:
        k = random.randint(bas, haut)
        t[k], t[haut] = t[haut], t[k]          # le pivot aléatoire passe en dernier
        p = partition_lomuto(t, bas, haut)
        tri_rapide_aleatoire(t, bas, p - 1)
        tri_rapide_aleatoire(t, p + 1, haut)
    return t
```

Avec un pivot aléatoire, aucune entrée particulière n'est systématiquement défavorable : le pire cas exigerait de tirer un très mauvais pivot (un des extrêmes) à presque chaque niveau, ce qui a une probabilité négligeable. L'espérance du nombre de comparaisons est `O(n log n)` pour **toute** entrée, ce qui empêche aussi un adversaire de construire une entrée pathologique.

**Exercice 8.3.4**

Comparez le nombre d'appels récursifs de votre tri rapide (pivot = premier élément) sur une liste triée de 1000 éléments et sur une liste mélangée.

**Correction**

```python
import random
import sys

sys.setrecursionlimit(10_000)
stats = {"appels": 0, "profondeur": 0}


def tri_rapide_premier(t, prof=1):
    stats["appels"] += 1
    stats["profondeur"] = max(stats["profondeur"], prof)
    if len(t) <= 1:
        return t
    pivot = t[0]
    gauche = [x for x in t[1:] if x < pivot]
    droite = [x for x in t[1:] if x >= pivot]
    return tri_rapide_premier(gauche, prof + 1) + [pivot] + tri_rapide_premier(droite, prof + 1)
```

Résultats typiques pour 1000 éléments :

| Entrée | Appels récursifs | Comparaisons | Profondeur |
| --- | --- | --- | --- |
| liste triée | 1999 | 499 500 (`n(n − 1)/2`) | 1000 |
| liste mélangée | environ 1300 | environ 10 500 | environ 22 |

Sur une liste triée, chaque partition retire un seul élément : comparaisons quadratiques et profondeur `n` (qui dépasse la limite de récursion par défaut de Python, d'où le `setrecursionlimit`). Sur une liste mélangée, les partitions sont à peu près équilibrées (profondeur O(log n)).

**Exercice 8.3.5** *(défi)*

Implémentez la partition en trois parties (`< pivot`, `= pivot`, `> pivot`) pour traiter efficacement les listes contenant beaucoup de doublons.

**Correction**

Partition en trois (drapeau hollandais) : les éléments `< pivot` à gauche, `= pivot` au milieu, `> pivot` à droite.

```python
import random


def tri_rapide_3(t, bas=0, haut=None):
    if haut is None:
        haut = len(t) - 1
    if bas >= haut:
        return t
    pivot = t[random.randint(bas, haut)]
    lt, i, gt = bas, bas, haut
    while i <= gt:
        if t[i] < pivot:
            t[lt], t[i] = t[i], t[lt]
            lt += 1
            i += 1
        elif t[i] > pivot:
            t[i], t[gt] = t[gt], t[i]
            gt -= 1
        else:
            i += 1
    tri_rapide_3(t, bas, lt - 1)       # strictement plus petits
    tri_rapide_3(t, gt + 1, haut)      # strictement plus grands
    return t


print(tri_rapide_3([2, 1, 2, 3, 2, 1, 2, 2]))   # [1, 1, 2, 2, 2, 2, 2, 3]
```

Les éléments égaux au pivot ne sont plus retraités : avec beaucoup de doublons, le coût tombe vers O(n) (par exemple pour une liste de valeurs toutes égales, une seule partition suffit), alors que la partition de Lomuto classique deviendrait quadratique.

**Exercice 8.3.6**

Limitez la profondeur de récursion à O(log n) en traitant récursivement la plus petite partition et itérativement la plus grande.

**Correction**

On traite récursivement la **plus petite** partition (taille ≤ n/2) et on boucle sur la plus grande : la profondeur de récursion est au plus `log₂ n`.

```python
def tri_rapide_profondeur_log(t, bas=0, haut=None):
    if haut is None:
        haut = len(t) - 1
    while bas < haut:
        p = partition_lomuto(t, bas, haut)
        if p - bas < haut - p:
            tri_rapide_profondeur_log(t, bas, p - 1)   # petite partie : récursion
            bas = p + 1                                # grande partie : itération
        else:
            tri_rapide_profondeur_log(t, p + 1, haut)
            haut = p - 1
    return t
```

Chaque appel récursif porte sur au plus la moitié des éléments, donc la pile ne dépasse pas O(log n), même si le temps reste O(n²) au pire.

## 8.4 Tri par tas (*Heap Sort*)

**Exercice 8.4.1**

Écrivez un tri par tas avec `heapq` (poussez tous les éléments, puis extrayez). Quelle est la complexité en temps et en espace ?

**Correction**

```python
import heapq


def tri_tas(t):
    tas = list(t)
    heapq.heapify(tas)                                    # O(n)
    return [heapq.heappop(tas) for _ in range(len(tas))]  # n extractions en O(log n)


print(tri_tas([4, 10, 3, 5, 1]))   # [1, 3, 4, 5, 10]
```

Temps : **O(n log n)**. Espace : **O(n)** (le tas est une copie). La version en place (exercice 8.4.3) ne nécessite que O(1) de mémoire supplémentaire.

**Exercice 8.4.2**

Construisez à la main un tas-max à partir de `[4, 10, 3, 5, 1]` (construction ascendante), puis déroulez les extractions successives.

**Correction**

**Construction ascendante** du tas-max à partir de `[4, 10, 3, 5, 1]` (on fait descendre les nœuds internes, de l'indice 1 à l'indice 0) :

1. Nœud d'indice 1 (valeur 10) : ses enfants valent 5 et 1, il est déjà plus grand, rien à faire.
2. Nœud d'indice 0 (valeur 4) : enfants 10 et 3. On échange avec 10 : `[10, 4, 3, 5, 1]`. Le 4 est maintenant à l'indice 1 avec enfants 5 et 1 : on échange avec 5 : `[10, 5, 3, 4, 1]`.

Tas-max obtenu : `[10, 5, 3, 4, 1]`.

**Extractions successives** (on échange la racine avec le dernier élément du tas, on réduit le tas, on fait descendre la racine) :

| Étape | Après échange | Après descente (la partie triée suit le point-virgule) |
| --- | --- | --- |
| 1 | `[1, 5, 3, 4 ; 10]` | `[5, 4, 3, 1 ; 10]` |
| 2 | `[1, 4, 3 ; 5, 10]` | `[4, 1, 3 ; 5, 10]` |
| 3 | `[3, 1 ; 4, 5, 10]` | `[3, 1 ; 4, 5, 10]` |
| 4 | `[1 ; 3, 4, 5, 10]` | `[1, 3, 4, 5, 10]` |

Résultat : `[1, 3, 4, 5, 10]`.

**Exercice 8.4.3** *(défi)*

Écrivez la version **en place** du tri par tas avec les fonctions `sift_down` et `construire_tas`.

**Correction**

```python
def sift_down(t, i, n):
    """Fait descendre t[i] dans le tas-max formé par t[0:n]."""
    while True:
        gauche, droite = 2 * i + 1, 2 * i + 2
        plus_grand = i
        if gauche < n and t[gauche] > t[plus_grand]:
            plus_grand = gauche
        if droite < n and t[droite] > t[plus_grand]:
            plus_grand = droite
        if plus_grand == i:
            return
        t[i], t[plus_grand] = t[plus_grand], t[i]
        i = plus_grand


def construire_tas(t):
    n = len(t)
    for i in range(n // 2 - 1, -1, -1):     # nœuds internes, de bas en haut
        sift_down(t, i, n)


def tri_tas_en_place(t):
    n = len(t)
    construire_tas(t)                       # O(n)
    for fin in range(n - 1, 0, -1):
        t[0], t[fin] = t[fin], t[0]         # le maximum va à sa place
        sift_down(t, 0, fin)
    return t


print(tri_tas_en_place([4, 10, 3, 5, 1]))   # [1, 3, 4, 5, 10]
```

Complexité : O(n log n) dans tous les cas, O(1) d'espace supplémentaire. Le tri n'est pas stable.

## 8.5 Tri par comptage (*Counting Sort*)

**Exercice 8.5.1**

Implémentez le tri par comptage pour des entiers compris entre `0` et `k`. Quelle est la complexité en fonction de `n` et `k` ?

**Correction**

```python
def tri_comptage(t, k):
    compte = [0] * (k + 1)
    for x in t:
        compte[x] += 1
    resultat = []
    for valeur, c in enumerate(compte):
        resultat.extend([valeur] * c)
    return resultat


print(tri_comptage([4, 2, 2, 8, 3, 3, 1], 8))   # [1, 2, 2, 3, 3, 4, 8]
```

Complexité : **O(n + k)** en temps et en espace. Il est avantageux quand `k = O(n)`.

**Exercice 8.5.2**

Adaptez-le pour gérer des entiers négatifs.

**Correction**

On décale toutes les valeurs par le minimum, de sorte que la plus petite devienne 0.

```python
def tri_comptage_negatifs(t):
    if not t:
        return []
    mini, maxi = min(t), max(t)
    compte = [0] * (maxi - mini + 1)
    for x in t:
        compte[x - mini] += 1
    resultat = []
    for i, c in enumerate(compte):
        resultat.extend([i + mini] * c)
    return resultat


print(tri_comptage_negatifs([3, -1, 0, -5, 3, -1]))   # [-5, -1, -1, 0, 3, 3]
```

La complexité devient O(n + (max − min)).

**Exercice 8.5.3**

Écrivez une version **stable** (avec tableau de comptages cumulés) qui trie des couples `(clé, valeur)` selon la clé. Pourquoi la stabilité est-elle indispensable pour le tri radix ?

**Correction**

```python
def tri_comptage_stable(t, cle, k):
    compte = [0] * (k + 1)
    for x in t:
        compte[cle(x)] += 1
    for i in range(1, k + 1):                # comptages cumulés : fin de chaque bloc
        compte[i] += compte[i - 1]
    resultat = [None] * len(t)
    for x in reversed(t):                    # parcours à l'envers : stabilité
        compte[cle(x)] -= 1
        resultat[compte[cle(x)]] = x
    return resultat


donnees = [(2, "a"), (1, "b"), (2, "c"), (1, "d")]
print(tri_comptage_stable(donnees, lambda p: p[0], 2))
# [(1, 'b'), (1, 'd'), (2, 'a'), (2, 'c')]
```

Pour chaque clé, le comptage cumulé donne la position juste après le dernier élément de cette clé ; en parcourant l'entrée de droite à gauche, les éléments de même clé sont placés dans le même ordre qu'à l'entrée.

La stabilité est **indispensable au tri radix** : on trie successivement par chiffre, du moins significatif au plus significatif ; à chaque passe, l'ordre déjà établi par les chiffres précédents doit être conservé pour les éléments ayant le même chiffre courant.

**Exercice 8.5.4**

Pour quels types de données le tri par comptage n'est-il pas adapté ? Donnez deux exemples.

**Correction**

Le tri par comptage convient mal quand les clés ne sont pas de petits entiers :

1. **Entiers de très grande amplitude** (par exemple des identifiants sur 64 bits) : le tableau de comptage aurait `k` cases, soit une mémoire et un temps O(k) prohibitifs devant `n`.
2. **Nombres flottants, chaînes de caractères ou objets sans clé entière bornée** : on ne peut pas les utiliser comme indices d'un tableau de comptage.

## 8.6 Tri radix (par base)

**Exercice 8.6.1**

Déroulez à la main le tri radix (base 10, chiffres de droite à gauche) sur `[170, 45, 75, 90, 802, 24, 2, 66]`.

**Correction**

Tri radix de `[170, 45, 75, 90, 802, 24, 2, 66]` (passes stables, chiffre des unités, dizaines puis centaines).

| Passe | Ordre des éléments après la passe |
| --- | --- |
| Unités | `[170, 90, 802, 2, 24, 45, 75, 66]` |
| Dizaines | `[802, 2, 24, 45, 66, 170, 75, 90]` |
| Centaines | `[2, 24, 45, 66, 75, 90, 170, 802]` |

Détail de la passe des unités : les chiffres sont 0 (170), 5 (45), 5 (75), 0 (90), 2 (802), 4 (24), 2 (2), 6 (66) ; on regroupe par chiffre croissant en conservant l'ordre : 0 : 170, 90 ; 2 : 802, 2 ; 4 : 24 ; 5 : 45, 75 ; 6 : 66.

**Exercice 8.6.2**

Implémentez le tri radix pour des entiers positifs. Quelle est la complexité en fonction de `n`, du nombre de chiffres `d` et de la base `b` ?

**Correction**

```python
def tri_radix(t, base=10):
    if not t:
        return []
    maximum = max(t)
    exposant = 1
    while maximum // exposant > 0:
        t = _comptage_par_chiffre(t, exposant, base)
        exposant *= base
    return t


def _comptage_par_chiffre(t, exposant, base):
    compte = [0] * base
    for x in t:
        compte[(x // exposant) % base] += 1
    for i in range(1, base):
        compte[i] += compte[i - 1]
    sortie = [0] * len(t)
    for x in reversed(t):
        d = (x // exposant) % base
        compte[d] -= 1
        sortie[compte[d]] = x
    return sortie


print(tri_radix([170, 45, 75, 90, 802, 24, 2, 66]))
# [2, 24, 45, 66, 75, 90, 170, 802]
```

Complexité : `d` passes de tri par comptage en O(n + b), soit **O(d (n + b))**, avec `d = ⌊log_b(max)⌋ + 1`. Espace O(n + b).

**Exercice 8.6.3**

Adaptez-le au tri de chaînes de même longueur.

**Correction**

Pour des chaînes de même longueur `L`, on trie par caractère de droite à gauche, avec un comptage sur le code du caractère.

```python
def tri_radix_chaines(mots):
    if not mots:
        return []
    longueur = len(mots[0])
    for pos in range(longueur - 1, -1, -1):
        compte = [0] * 257
        for m in mots:
            compte[ord(m[pos]) + 1] += 1
        for i in range(256):
            compte[i + 1] += compte[i]
        sortie = [None] * len(mots)
        for m in mots:                       # parcours dans l'ordre : positions de départ
            c = ord(m[pos])
            sortie[compte[c]] = m
            compte[c] += 1
        mots = sortie
    return mots


print(tri_radix_chaines(["dab", "cab", "fad", "bad", "dad", "ebb", "ace"]))
# ['ace', 'bad', 'cab', 'dab', 'dad', 'ebb', 'fad']
```

Les codes sont supposés inférieurs à 256. Complexité O(L (n + 256)).

## 8.7 Timsort et tri en Python *(à jour, ajout)*

**Exercice 8.7.1**

Triez la liste `[("Alice", 30), ("Bob", 25), ("Chloé", 30), ("David", 25)]` : par âge croissant, par âge décroissant puis par nom croissant, et par nom décroissant, en n'utilisant que `sorted` et `key`.

**Correction**

```python
personnes = [("Alice", 30), ("Bob", 25), ("Chloé", 30), ("David", 25)]

# Âge croissant (stable : à âge égal, l'ordre initial est conservé)
print(sorted(personnes, key=lambda p: p[1]))
# [('Bob', 25), ('David', 25), ('Alice', 30), ('Chloé', 30)]

# Âge décroissant puis nom croissant
print(sorted(personnes, key=lambda p: (-p[1], p[0])))
# [('Alice', 30), ('Chloé', 30), ('Bob', 25), ('David', 25)]

# Nom décroissant
print(sorted(personnes, key=lambda p: p[0], reverse=True))
# [('David', 25), ('Chloé', 30), ('Bob', 25), ('Alice', 30)]
```

Pour inverser un critère numérique dans un tuple-clé, on utilise son opposé.

**Exercice 8.7.2**

Triez une liste de chaînes par longueur croissante, puis par ordre alphabétique en cas d'égalité, sans comparateur personnalisé.

**Correction**

```python
mots = ["pomme", "kiwi", "fraise", "fig", "poire", "banane"]
print(sorted(mots, key=lambda m: (len(m), m)))
# ['fig', 'kiwi', 'poire', 'pomme', 'banane', 'fraise']
```

La clé est le tuple `(longueur, mot)` : Python compare d'abord les longueurs, puis, en cas d'égalité, l'ordre alphabétique.

**Exercice 8.7.3**

Expliquez comment la stabilité de `sorted` permet de trier en deux passes (d'abord sur la clé secondaire, puis sur la clé principale) pour obtenir un tri multi-critères.

**Correction**

`sorted` (Timsort) est **stable** : il conserve l'ordre relatif des éléments ayant la même clé. On peut donc trier d'abord selon la clé **secondaire**, puis selon la clé **principale** : le second tri ne touche pas à l'ordre des éléments de même clé principale, qui restent classés selon la clé secondaire.

```python
personnes = [("Alice", 30), ("Bob", 25), ("Chloé", 30), ("David", 25)]
personnes = sorted(personnes, key=lambda p: p[0])      # 1. clé secondaire : nom
personnes = sorted(personnes, key=lambda p: p[1])      # 2. clé principale : âge
print(personnes)
# [('Bob', 25), ('David', 25), ('Alice', 30), ('Chloé', 30)]
```

C'est utile quand les critères n'ont pas le même sens (un croissant, un décroissant) et qu'une clé-tuple ne convient pas.

**Exercice 8.7.4**

Chronométrez `sorted` sur une liste aléatoire, une liste déjà triée et une liste presque triée de `10⁶` éléments. Que constatez-vous ?

**Correction**

```python
import random
import time

n = 10**6
aleatoire = random.sample(range(n), n)
triee = sorted(aleatoire)
presque = triee[:]
for _ in range(1000):                       # 1000 échanges au hasard
    i, j = random.randrange(n), random.randrange(n)
    presque[i], presque[j] = presque[j], presque[i]

for nom, liste in (("aléatoire", aleatoire), ("triée", triee), ("presque triée", presque)):
    debut = time.perf_counter()
    sorted(liste)
    print(nom, round(time.perf_counter() - debut, 3), "s")
```

Ordres de grandeur : environ 0,3 s pour la liste aléatoire, environ 0,01 s pour la liste déjà triée, environ 0,015 s pour la liste presque triée. Timsort détecte les suites déjà ordonnées (*runs*) et les fusionne : il est en **O(n)** sur une liste déjà triée et très rapide sur une liste presque triée, tout en restant en O(n log n) dans le pire cas.

## 8.8 Quel tri choisir ?

**Exercice 8.8.1**

Pour chaque situation, choisissez un tri et justifiez : tri d'une liste de 15 éléments, tri de 10⁷ entiers compris entre 0 et 1000, tri d'un fichier de 100 Go, tri d'objets en conservant l'ordre d'origine des égalités, tri avec une mémoire très limitée et un pire cas garanti.

**Correction**

1. **Liste de 15 éléments** : le tri par insertion (ou simplement `sorted`) : la constante est petite et la mise en œuvre immédiate ; l'asymptotique ne compte pas pour `n` aussi petit.
2. **10⁷ entiers compris entre 0 et 1000** : le **tri par comptage**, en O(n + k) avec `k = 1001`.
3. **Fichier de 100 Go** : un **tri fusion externe** : on trie des blocs qui tiennent en mémoire, on les écrit sur disque, puis on les fusionne par lecture séquentielle.
4. **Objets dont on conserve l'ordre d'origine pour les égalités** : un tri **stable** (tri fusion, Timsort via `sorted`).
5. **Mémoire très limitée et pire cas garanti** : le **tri par tas**, en O(n log n) dans le pire cas et O(1) d'espace supplémentaire.

---

# 9. Diviser pour régner

## 9.1 Principe

**Exercice 9.1.1**

Pour chacun des problèmes suivants, décrivez les trois phases (diviser, résoudre, combiner) : tri fusion, recherche binaire, calcul de `xⁿ`, comptage des inversions.

**Correction**

| Problème | Diviser | Résoudre | Combiner |
| --- | --- | --- | --- |
| Tri fusion | couper la liste en deux moitiés | trier récursivement chaque moitié | fusionner les deux moitiés triées |
| Recherche binaire | comparer `x` à l'élément du milieu et choisir la moitié concernée | chercher récursivement dans cette seule moitié | rien à faire : on renvoie le résultat |
| Calcul de `xⁿ` | ramener à l'exposant `n // 2` | calculer `x^(n // 2)` | élever au carré (et multiplier par `x` si `n` est impair) |
| Comptage des inversions | couper le tableau en deux moitiés | compter les inversions dans chaque moitié (et la trier) | fusionner en comptant les inversions « croisées » entre les moitiés |

**Exercice 9.1.2**

Quelles conditions doit remplir un problème pour être résolu efficacement par « diviser pour régner » ? Donnez un exemple où cette approche n'apporte rien.

**Correction**

Conditions pour que « diviser pour régner » soit efficace :

1. le problème se décompose en **sous-problèmes de même nature**, plus petits, **indépendants** (qui ne se chevauchent pas) ;
2. il existe un ou plusieurs **cas de base** simples ;
3. la **combinaison** des solutions partielles est peu coûteuse (au plus de l'ordre du coût de la division).

Exemples où l'approche n'apporte rien : le calcul récursif de Fibonacci (les sous-problèmes se **chevauchent**, d'où un coût exponentiel : la programmation dynamique est la bonne approche), ou la somme/le maximum d'une liste (on fait toujours `n − 1` opérations, comme une simple boucle, avec un surcoût de récursion).

## 9.2 Exemple : maximum d'une liste

**Exercice 9.2.1**

Écrivez `maximum_dc(t, g, d)` par diviser pour régner. Écrivez la récurrence et résolvez-la. Gagne-t-on par rapport à la version itérative ?

**Correction**

```python
def maximum_dc(t, g, d):
    if g == d:
        return t[g]
    m = (g + d) // 2
    return max(maximum_dc(t, g, m), maximum_dc(t, m + 1, d))


t = [3, 8, 2, 9, 4, 7]
print(maximum_dc(t, 0, len(t) - 1))   # 9
```

Récurrence du nombre de comparaisons : `T(n) = 2T(n/2) + 1`, `T(1) = 0`, soit `T(n) = n − 1` (théorème maître : les feuilles dominent, Θ(n)). On ne gagne **rien** par rapport à la version itérative (même nombre de comparaisons, mais une surcharge d'appels et une pile O(log n)). L'intérêt serait seulement de paralléliser les deux moitiés.

**Exercice 9.2.2**

Écrivez `min_et_max(t)` qui renvoie le minimum et le maximum en effectuant environ `3n/2` comparaisons (au lieu de `2n`).

**Correction**

Idée : traiter les éléments **par paires**. On compare les deux éléments de la paire entre eux (1 comparaison), puis le plus petit au minimum courant (1) et le plus grand au maximum courant (1) : 3 comparaisons pour 2 éléments, soit environ `3n/2` au lieu de `2n`.

```python
def min_et_max(t):
    n = len(t)
    if n % 2 == 1:
        mini = maxi = t[0]
        debut = 1
    else:
        mini, maxi = (t[0], t[1]) if t[0] < t[1] else (t[1], t[0])
        debut = 2
    for i in range(debut, n - 1, 2):
        a, b = t[i], t[i + 1]
        if a > b:
            a, b = b, a
        if a < mini:
            mini = a
        if b > maxi:
            maxi = b
    return mini, maxi


print(min_et_max([3, 8, 2, 9, 4, 7]))   # (2, 9)
print(min_et_max([5]))                   # (5, 5)
```

Une version diviser pour régner donne aussi `T(n) = 2T(n/2) + 2`, soit `T(n) = 3n/2 − 2` comparaisons pour `n` puissance de 2.

## 9.3 Exemple : sous-tableau de somme maximale

**Exercice 9.3.1**

Calculez à la main le sous-tableau de somme maximale de `[-2, 1, -3, 4, -1, 2, 1, -5, 4]` par diviser pour régner : pour chaque niveau, donnez le meilleur sous-tableau à gauche, à droite et à cheval sur le milieu.

**Correction**

Tableau `[-2, 1, -3, 4, -1, 2, 1, -5, 4]` (indices 0 à 8).

| Niveau | Intervalle (milieu) | Meilleur à gauche | Meilleur à droite | Meilleur à cheval | Résultat |
| --- | --- | --- | --- | --- | --- |
| 0 | `[0..8]` (milieu 4) | 4 (`[4]`) | 4 (`[4]`) | 6 (`[4, -1, 2, 1]`, indices 3 à 6) | **6** |
| 1 | `[0..4]` (milieu 2) | 1 (`[1]`) | 4 (`[4]`) | 2 | 4 |
| 1 | `[5..8]` (milieu 6) | 3 (`[2, 1]`) | 4 (`[4]`) | 2 | 4 |

Détail du calcul « à cheval » au niveau 0 : meilleur suffixe de la partie gauche terminant à l'indice 4 : `-1`, `3`, `0`, `1`, `-1`, donc 3 (éléments `4, -1`) ; meilleur préfixe de la partie droite commençant à l'indice 5 : `2`, `3`, `-2`, `2`, donc 3 (éléments `2, 1`). Total : `3 + 3 = 6`.

Le sous-tableau de somme maximale est `[4, -1, 2, 1]`, de somme **6**.

**Exercice 9.3.2**

Implémentez la méthode diviser pour régner et la force brute O(n²). Comparez leurs résultats sur des tableaux aléatoires.

**Correction**

```python
import random


def meilleur_dc(t, g, d):
    if g == d:
        return t[g]
    m = (g + d) // 2
    gauche = meilleur_dc(t, g, m)
    droite = meilleur_dc(t, m + 1, d)
    s, meilleur_g = 0, float("-inf")
    for i in range(m, g - 1, -1):          # suffixe de la partie gauche
        s += t[i]
        meilleur_g = max(meilleur_g, s)
    s, meilleur_d = 0, float("-inf")
    for j in range(m + 1, d + 1):          # préfixe de la partie droite
        s += t[j]
        meilleur_d = max(meilleur_d, s)
    return max(gauche, droite, meilleur_g + meilleur_d)


def meilleur_force_brute(t):
    n = len(t)
    meilleur = float("-inf")
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += t[j]
            meilleur = max(meilleur, s)
    return meilleur


for _ in range(1000):
    t = [random.randint(-10, 10) for _ in range(random.randint(1, 15))]
    assert meilleur_dc(t, 0, len(t) - 1) == meilleur_force_brute(t)
print(meilleur_dc([-2, 1, -3, 4, -1, 2, 1, -5, 4], 0, 8))   # 6
```

Les deux méthodes donnent toujours le même résultat.

**Exercice 9.3.3**

Quelle est la complexité de la version diviser pour régner ? Quel algorithme linéaire connaissez-vous pour ce problème (voir la section 18) ?

**Correction**

Récurrence : `T(n) = 2T(n/2) + O(n)` (le calcul « à cheval » parcourt les deux moitiés), donc **O(n log n)**.

L'algorithme linéaire est celui de **Kadane** (programmation dynamique, section 18.4) : `meilleur_fin_ici = max(t[i], meilleur_fin_ici + t[i])`, en O(n) temps et O(1) espace.

## 9.4 Quickselect : le k-ième plus petit élément

**Exercice 9.4.1**

Implémentez `quickselect(t, k)` renvoyant le `k`-ième plus petit élément (indexé à partir de 0).

**Correction**

```python
import random


def quickselect(t, k):
    t = list(t)
    bas, haut = 0, len(t) - 1
    while True:
        if bas == haut:
            return t[bas]
        r = random.randint(bas, haut)
        t[r], t[haut] = t[haut], t[r]
        pivot = t[haut]
        i = bas - 1
        for j in range(bas, haut):
            if t[j] <= pivot:
                i += 1
                t[i], t[j] = t[j], t[i]
        t[i + 1], t[haut] = t[haut], t[i + 1]
        p = i + 1
        if k == p:
            return t[p]
        if k < p:
            haut = p - 1
        else:
            bas = p + 1


t = [7, 2, 9, 4, 1, 8]
print([quickselect(t, k) for k in range(6)])   # [1, 2, 4, 7, 8, 9]
```

On ne poursuit que dans la partie qui contient l'indice `k`.

**Exercice 9.4.2**

Quelle est la complexité en moyenne et au pire ? Donnez une entrée de pire cas pour un pivot choisi comme premier élément.

**Correction**

- **Moyenne** : **O(n)** : en prenant un pivot au hasard, la taille de la partie conservée diminue en moyenne géométriquement, d'où `n + n/2 + n/4 + ... ≈ 2n` comparaisons.
- **Pire cas** : **O(n²)** : si chaque pivot est un extrême, la taille ne diminue que de 1 : `n + (n − 1) + ... + 1`.

Entrée de pire cas pour un pivot choisi comme premier élément : un tableau **déjà trié** `[1, 2, ..., n]` avec `k = n − 1` (ou trié à l'envers avec `k = 0`) : le pivot est toujours le plus petit élément restant et une seule valeur est éliminée à chaque tour. Une sélection « médiane des médianes » garantit O(n) au pire cas, au prix d'une grosse constante.

**Exercice 9.4.3**

Utilisez `quickselect` pour calculer la médiane d'une liste de taille impaire, puis d'une liste de taille paire.

**Correction**

```python
def mediane(t):
    n = len(t)
    if n % 2 == 1:
        return quickselect(t, n // 2)
    return (quickselect(t, n // 2 - 1) + quickselect(t, n // 2)) / 2


print(mediane([7, 2, 9, 4, 1]))      # 4
print(mediane([7, 2, 9, 4, 1, 8]))   # 5.5
```

Complexité moyenne O(n), contre O(n log n) en passant par un tri.

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

**Correction**

On compare `f(n)` à `n^(log_b a)` pour `T(n) = aT(n/b) + f(n)`.

| Récurrence | `n^(log_b a)` | `f(n)` | Résultat |
| --- | --- | --- | --- |
| 1. `T(n) = 4T(n/2) + n` | `n²` | `n` | **Θ(n²)** |
| 2. `T(n) = 2T(n/2) + n²` | `n` | `n²` | **Θ(n²)** |
| 3. `T(n) = 2T(n/2) + n` | `n` | `n` | **Θ(n log n)** |
| 4. `T(n) = T(n/2) + 1` | `n⁰ = 1` | `1` | **Θ(log n)** |
| 5. `T(n) = 8T(n/2) + n²` | `n³` | `n²` | **Θ(n³)** |
| 6. `T(n) = 9T(n/3) + n` | `n²` | `n` | **Θ(n²)** |
| 7. `T(n) = 3T(n/4) + n` | `n^0,79` | `n` | **Θ(n)** |

**Exercice 9.5.2**

Pour chacune, précisez à quel cas du théorème (feuilles dominantes, équilibre, racine dominante) elle appartient.

**Correction**

| Récurrence | Cas du théorème | Interprétation |
| --- | --- | --- |
| 1 | cas 1 | **feuilles dominantes** (`f(n)` polynomialement plus petite que `n^(log_b a)`) |
| 2 | cas 3 | **racine dominante** (`f(n)` plus grande ; condition de régularité : `2(n/2)² = n²/2 ≤ c n²`) |
| 3 | cas 2 | **équilibre** (même ordre : un facteur `log n` apparaît) |
| 4 | cas 2 | **équilibre** (`f(n) = Θ(n⁰)`) |
| 5 | cas 1 | **feuilles dominantes** |
| 6 | cas 1 | **feuilles dominantes** |
| 7 | cas 3 | **racine dominante** (régularité : `3(n/4) = 0,75 n ≤ c n`) |

**Exercice 9.5.3**

Écrivez la récurrence de la recherche binaire, du tri fusion et de la multiplication naïve de deux entiers de `n` chiffres découpés en deux moitiés (4 sous-multiplications). Résolvez-les.

**Correction**

- **Recherche binaire** : `T(n) = T(n/2) + O(1)`, soit `a = 1`, `b = 2`, `n^0 = 1 = f(n)` : cas d'équilibre, **Θ(log n)**.
- **Tri fusion** : `T(n) = 2T(n/2) + Θ(n)` : équilibre, **Θ(n log n)**.
- **Multiplication naïve de deux entiers de `n` chiffres** découpés en deux moitiés (`xy = (a·10^(n/2) + b)(c·10^(n/2) + d)` avec 4 sous-multiplications `ac`, `ad`, `bc`, `bd`) : `T(n) = 4T(n/2) + O(n)`, soit `n^(log₂ 4) = n²` : feuilles dominantes, **Θ(n²)**, aucun gain sur l'école primaire. (Karatsuba, avec 3 sous-multiplications, donne `Θ(n^(log₂ 3)) ≈ Θ(n^1,585)`.)

## 9.6 Multiplication de matrices (Strassen)

**Exercice 9.6.1**

Combien de multiplications scalaires la multiplication naïve de deux matrices `n × n` effectue-t-elle ? Écrivez la récurrence obtenue en découpant chaque matrice en 4 blocs et en effectuant 8 multiplications de blocs.

**Correction**

La multiplication naïve de deux matrices `n × n` effectue `n³` multiplications scalaires (`n²` coefficients, chacun somme de `n` produits).

En découpant en 4 blocs de taille `n/2` : `C₁₁ = A₁₁B₁₁ + A₁₂B₂₁`, etc., ce qui donne 8 multiplications de blocs et 4 additions de blocs :

`T(n) = 8T(n/2) + O(n²)`.

Avec `n^(log₂ 8) = n³` dominant `n²` : **Θ(n³)**. Le découpage récursif en lui-même ne fait donc pas mieux que la méthode naïve.

**Exercice 9.6.2**

Strassen réduit à 7 le nombre de multiplications de blocs. Écrivez la récurrence correspondante et donnez l'exposant de la complexité.

**Correction**

Strassen calcule les 4 blocs de `C` avec **7** multiplications de blocs (au prix de plus d'additions, toujours en O(n²)) :

`T(n) = 7T(n/2) + O(n²)`.

On a `n^(log₂ 7) ≈ n^2,807` qui domine `n²` : `T(n) = Θ(n^(log₂ 7)) ≈ Θ(n^2,81)`, meilleur que `Θ(n³)`. En pratique, Strassen ne devient avantageux que pour de grandes matrices, à cause de ses constantes.

**Exercice 9.6.3**

Implémentez la multiplication naïve de matrices en Python, puis l'approche récursive par blocs pour des matrices de taille puissance de 2.

**Correction**

```python
def mult_naive(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            aik = A[i][k]
            for j in range(n):
                C[i][j] += aik * B[k][j]
    return C


def ajouter(A, B):
    return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def mult_blocs(A, B):
    """Taille n puissance de 2 ; 8 multiplications de blocs."""
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    m = n // 2

    def bloc(M, i, j):
        return [ligne[j:j + m] for ligne in M[i:i + m]]

    A11, A12, A21, A22 = bloc(A, 0, 0), bloc(A, 0, m), bloc(A, m, 0), bloc(A, m, m)
    B11, B12, B21, B22 = bloc(B, 0, 0), bloc(B, 0, m), bloc(B, m, 0), bloc(B, m, m)
    C11 = ajouter(mult_blocs(A11, B11), mult_blocs(A12, B21))
    C12 = ajouter(mult_blocs(A11, B12), mult_blocs(A12, B22))
    C21 = ajouter(mult_blocs(A21, B11), mult_blocs(A22, B21))
    C22 = ajouter(mult_blocs(A21, B12), mult_blocs(A22, B22))
    haut = [r1 + r2 for r1, r2 in zip(C11, C12)]
    bas = [r1 + r2 for r1, r2 in zip(C21, C22)]
    return haut + bas


A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(mult_naive(A, B))     # [[19, 22], [43, 50]]
print(mult_blocs(A, B))     # [[19, 22], [43, 50]]
```

---

# 10. Algorithmes gloutons

## 10.1 Principe

**Exercice 10.1.1**

Décrivez en deux phrases la stratégie gloutonne. Donnez trois exemples de problèmes de la vie courante où l'on applique naturellement un choix glouton.

**Correction**

**Stratégie gloutonne** : à chaque étape, on effectue le choix qui paraît le meilleur localement, sans jamais le remettre en cause, en espérant que la suite de ces choix locaux conduise à un optimum global.

Exemples de la vie courante : rendre la monnaie en donnant d'abord les plus grosses pièces possibles ; choisir à chaque carrefour la route la plus directe vers la destination ; remplir une valise en commençant par les objets les plus utiles ; avancer ses tâches de la journée en commençant par la plus rapide à terminer.

## 10.2 Quand fonctionne-t-il ?

**Exercice 10.2.1**

Trouvez un système de pièces et un montant pour lesquels l'algorithme glouton de rendu de monnaie échoue (différent de celui du cours), et donnez la solution optimale.

**Correction**

Système `[1, 5, 6, 9]` et montant 11 :

- **Glouton** : 9, puis il reste 2 : 1 + 1, soit `9 + 1 + 1`, **3 pièces**.
- **Optimal** : `5 + 6`, soit **2 pièces**.

Le glouton échoue donc. (Un autre exemple classique : `[1, 3, 4]` avec le montant 6 : glouton `4 + 1 + 1` = 3 pièces, optimal `3 + 3` = 2 pièces.)

**Exercice 10.2.2**

Pourquoi le système `[1, 2, 5, 10, 20, 50, 100, 200]` est-il « canonique » ? Vérifiez expérimentalement, avec un programme comparant glouton et programmation dynamique, pour tous les montants jusqu'à 500.

**Correction**

Le système `[1, 2, 5, 10, 20, 50, 100, 200]` est **canonique** : le glouton y est toujours optimal. Idée de preuve par échange : dans une solution optimale, on ne trouve jamais deux pièces de 1 (remplaçables par un 2), trois pièces de 2 (remplaçables par `5 + 1`, donc moins de pièces), deux pièces de 5 (par un 10), et le même raisonnement se répète à chaque décade (10, 20, 50 puis 100, 200). Ces contraintes forcent la décomposition qu'effectue le glouton.

Vérification expérimentale :

```python
def glouton(pieces, montant):
    n = 0
    for p in sorted(pieces, reverse=True):
        n += montant // p
        montant %= p
    return n


def dp_monnaie(pieces, montant):
    inf = float("inf")
    dp = [0] + [inf] * montant
    for m in range(1, montant + 1):
        for p in pieces:
            if p <= m and dp[m - p] + 1 < dp[m]:
                dp[m] = dp[m - p] + 1
    return dp[montant]


pieces = [1, 2, 5, 10, 20, 50, 100, 200]
print(all(glouton(pieces, m) == dp_monnaie(pieces, m) for m in range(1, 501)))   # True
```

**Exercice 10.2.3**

Quelles deux propriétés (choix glouton, sous-structure optimale) doit vérifier un problème pour qu'un algorithme glouton soit correct ? Expliquez chacune avec un exemple.

**Correction**

Un algorithme glouton est correct si le problème possède :

1. **La propriété du choix glouton** : il existe toujours une solution optimale qui commence par le choix glouton. Exemple : en sélection d'activités, il existe une solution optimale contenant l'activité qui se termine le plus tôt (on le prouve par échange : on remplace la première activité d'une solution optimale par celle-là sans rien perdre).
2. **La sous-structure optimale** : une fois le choix fait, le reste du problème est un sous-problème de même nature, et une solution optimale du problème contient une solution optimale du sous-problème. Exemple : après avoir pris la première activité, il reste à choisir un ensemble optimal parmi les activités qui commencent après sa fin.

Contre-exemple : le rendu de monnaie avec `[1, 3, 4]` possède la sous-structure optimale mais pas la propriété du choix glouton (pour 6, prendre 4 n'est pas compatible avec l'optimum `3 + 3`).

## 10.3 Cadre général

**Exercice 10.3.1**

Complétez le cadre général (définir les candidats, trier selon un critère, choisir si faisable, mettre à jour) pour le problème : « Choisir un nombre maximal de fichiers à copier sur une clé USB de capacité C, connaissant la taille de chaque fichier. »

**Correction**

Pour maximiser le **nombre** de fichiers copiés, on prend les plus petits d'abord.

- **Candidats** : l'ensemble des fichiers.
- **Critère de tri** : taille croissante.
- **Test de faisabilité** : la taille déjà occupée plus celle du fichier ne dépasse pas `C`.
- **Mise à jour** : ajouter le fichier choisi et sa taille à la sélection.

```python
def fichiers_a_copier(tailles, capacite):
    choisis, utilise = [], 0
    for t in sorted(tailles):
        if utilise + t <= capacite:
            choisis.append(t)
            utilise += t
        else:
            break                  # les suivants sont encore plus gros
    return choisis


print(fichiers_a_copier([700, 200, 400, 100, 500], 1000))   # [100, 200, 400]
```

Correction (par échange) : si une solution optimale ne contient pas le plus petit fichier, on peut remplacer n'importe lequel de ses fichiers par lui sans dépasser la capacité. Complexité O(n log n).

## 10.4 Sélection d'activités (*Activity Selection*)

**Exercice 10.4.1**

Appliquez à la main l'algorithme de sélection d'activités sur `[(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]`.

**Correction**

On trie par **heure de fin** croissante : `(1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16)`.

| Activité examinée | Début ≥ dernière fin ? | Décision |
| --- | --- | --- |
| `(1,4)` | oui (aucune activité choisie) | choisie, fin = 4 |
| `(3,5)` | 3 < 4 | rejetée |
| `(0,6)` | 0 < 4 | rejetée |
| `(5,7)` | 5 ≥ 4 | choisie, fin = 7 |
| `(3,9)`, `(5,9)`, `(6,10)` | début < 7 | rejetées |
| `(8,11)` | 8 ≥ 7 | choisie, fin = 11 |
| `(8,12)`, `(2,14)` | début < 11 | rejetées |
| `(12,16)` | 12 ≥ 11 | choisie |

Sélection : `(1,4), (5,7), (8,11), (12,16)`, soit **4 activités**.

**Exercice 10.4.2**

Implémentez `selection_activites(intervalles)`. Donnez la complexité.

**Correction**

```python
def selection_activites(intervalles):
    selection = []
    derniere_fin = float("-inf")
    for debut, fin in sorted(intervalles, key=lambda iv: iv[1]):
        if debut >= derniere_fin:
            selection.append((debut, fin))
            derniere_fin = fin
    return selection


iv = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
print(selection_activites(iv))   # [(1, 4), (5, 7), (8, 11), (12, 16)]
```

Complexité : O(n log n) pour le tri, plus O(n) pour le parcours, soit **O(n log n)**.

**Exercice 10.4.3**

Montrez par un contre-exemple que trier par **durée croissante** ou par **date de début** ne donne pas toujours l'optimum.

**Correction**

- **Tri par durée croissante** : activités `(0,5)`, `(4,6)`, `(5,10)`. La plus courte est `(4,6)` (durée 2) ; elle chevauche les deux autres, donc le glouton ne choisit qu'**1 activité**, alors que `(0,5)` et `(5,10)` sont compatibles : l'optimum est **2**.
- **Tri par date de début** : activités `(0,10)`, `(1,2)`, `(3,4)`. Le glouton prend `(0,10)` qui bloque tout : **1 activité**, alors que `(1,2)` et `(3,4)` sont compatibles : l'optimum est **2**.

Seul le tri par **heure de fin** donne toujours l'optimum.

**Exercice 10.4.4**

Planifiez le nombre minimal de salles nécessaires pour tenir toutes les réunions d'une liste d'intervalles (indice : trier les débuts et les fins).

**Correction**

On trie séparément les débuts et les fins. À chaque début, si une réunion déjà terminée libère une salle (le plus petit instant de fin est ≤ au début), on la réutilise ; sinon on ouvre une salle.

```python
def salles_minimum(intervalles):
    debuts = sorted(d for d, _ in intervalles)
    fins = sorted(f for _, f in intervalles)
    salles = j = 0
    for d in debuts:
        if d >= fins[j]:
            j += 1                 # une salle se libère : on la réutilise
        else:
            salles += 1            # il faut une salle de plus
    return salles


print(salles_minimum([(0, 30), (5, 10), (15, 20)]))   # 2
print(salles_minimum([(7, 10), (2, 4)]))              # 1
```

Complexité O(n log n). Le résultat est le nombre maximal de réunions simultanées.

## 10.5 Sac à dos fractionnaire

**Exercice 10.5.1**

Soit les objets `(valeur, poids)` : `(60, 10)`, `(100, 20)`, `(120, 30)` et une capacité de 50. Calculez à la main la valeur maximale pour le sac à dos fractionnaire, puis pour le sac à dos 0/1 (par énumération).

**Correction**

Rapports `valeur/poids` : `(60, 10)` : 6 ; `(100, 20)` : 5 ; `(120, 30)` : 4.

**Sac à dos fractionnaire** (capacité 50) : on prend l'objet 1 en entier (poids 10, valeur 60), l'objet 2 en entier (poids 20, valeur 100), puis les 20 unités restantes de l'objet 3 : `20/30 × 120 = 80`. Total : `60 + 100 + 80 = ` **240**.

**Sac à dos 0/1** (énumération) :

| Sous-ensemble | Poids | Valeur |
| --- | --- | --- |
| objets 1 et 2 | 30 | 160 |
| objets 1 et 3 | 40 | 180 |
| objets 2 et 3 | 50 | **220** |
| objets 1, 2 et 3 | 60 | interdit (> 50) |

Optimum 0/1 : **220** (objets 2 et 3).

**Exercice 10.5.2**

Implémentez `sac_fractionnaire(objets, capacite)`. Quelle est la complexité ?

**Correction**

```python
def sac_fractionnaire(objets, capacite):
    """objets : liste de (valeur, poids). Renvoie la valeur maximale."""
    total = 0.0
    for valeur, poids in sorted(objets, key=lambda o: o[0] / o[1], reverse=True):
        if capacite == 0:
            break
        pris = min(poids, capacite)
        total += valeur * pris / poids
        capacite -= pris
    return total


print(sac_fractionnaire([(60, 10), (100, 20), (120, 30)], 50))   # 240.0
```

Complexité : O(n log n) (tri) puis O(n).

**Exercice 10.5.3**

Pourquoi le glouton par rapport `valeur/poids` n'est-il pas optimal pour le sac à dos 0/1 ? Donnez un contre-exemple.

**Correction**

En 0/1, on ne peut pas prendre une fraction d'objet : la capacité restante peut être mal utilisée.

Contre-exemple (mêmes objets, capacité 50) : le glouton par rapport `valeur/poids` prend `(60, 10)` puis `(100, 20)` (poids total 30, valeur 160) ; l'objet `(120, 30)` ne tient plus (30 + 30 > 50). Il obtient **160**, alors que l'optimum 0/1 est **220** (objets 2 et 3). Il faut la programmation dynamique (section 18).

## 10.6 Codage de Huffman

**Exercice 10.6.1**

On donne les fréquences : `a:45`, `b:13`, `c:12`, `d:16`, `e:9`, `f:5`. Construisez à la main l'arbre de Huffman en notant chaque fusion, puis donnez le code de chaque lettre.

**Correction**

Fréquences : `a:45, b:13, c:12, d:16, e:9, f:5`. On fusionne à chaque étape les deux nœuds de plus faible fréquence.

| Étape | Nœuds fusionnés | Nouveau nœud |
| --- | --- | --- |
| 1 | `f:5` et `e:9` | 14 |
| 2 | `c:12` et `b:13` | 25 |
| 3 | `14` et `d:16` | 30 |
| 4 | `25` et `30` | 55 |
| 5 | `a:45` et `55` | 100 |

Arbre (0 = branche gauche, 1 = branche droite) :

```text
          100
         /    \
      a:45     55
              /  \
            25    30
           /  \   /  \
        c:12 b:13 14  d:16
                 /  \
              f:5   e:9
```

Codes : `a = 0`, `c = 100`, `b = 101`, `f = 1100`, `e = 1101`, `d = 111`. (D'autres choix de côté donnent des codes équivalents de mêmes longueurs.)

**Exercice 10.6.2**

Calculez la longueur totale du texte encodé (en bits) pour 100 caractères avec ces fréquences, et comparez à un code de longueur fixe.

**Correction**

Longueur totale pour 100 caractères (fréquence × longueur du code) :

`45 × 1 + 13 × 3 + 12 × 3 + 16 × 3 + 9 × 4 + 5 × 4 = 45 + 39 + 36 + 48 + 36 + 20 = ` **224 bits**.

Code de longueur fixe : 6 symboles nécessitent `⌈log₂ 6⌉ = 3` bits, soit `100 × 3 = 300` bits. Huffman fait gagner `76` bits, environ **25 %**.

**Exercice 10.6.3**

Implémentez la construction de l'arbre de Huffman avec `heapq`, la génération de la table de codes, l'encodage et le décodage d'une chaîne.

**Correction**

```python
import heapq
from collections import Counter


def arbre_huffman(texte):
    tas = [(freq, i, c) for i, (c, freq) in enumerate(Counter(texte).items())]
    heapq.heapify(tas)
    compteur = len(tas)                     # départage les égalités de fréquence
    while len(tas) > 1:
        f1, _, a = heapq.heappop(tas)
        f2, _, b = heapq.heappop(tas)
        heapq.heappush(tas, (f1 + f2, compteur, (a, b)))
        compteur += 1
    return tas[0][2]                        # un caractère (feuille) ou un tuple (gauche, droite)


def table_codes(noeud, prefixe="", table=None):
    if table is None:
        table = {}
    if isinstance(noeud, str):
        table[noeud] = prefixe or "0"       # cas d'un seul symbole
    else:
        table_codes(noeud[0], prefixe + "0", table)
        table_codes(noeud[1], prefixe + "1", table)
    return table


def encoder(texte, table):
    return "".join(table[c] for c in texte)


def decoder(bits, arbre):
    if isinstance(arbre, str):
        return arbre * len(bits)
    resultat, noeud = [], arbre
    for b in bits:
        noeud = noeud[int(b)]
        if isinstance(noeud, str):
            resultat.append(noeud)
            noeud = arbre
    return "".join(resultat)


texte = "abracadabra"
arbre = arbre_huffman(texte)
table = table_codes(arbre)
bits = encoder(texte, table)
print(table, len(bits))
assert decoder(bits, arbre) == texte
```

Complexité : O(k log k) pour `k` symboles distincts (plus O(n) pour compter et encoder).

**Exercice 10.6.4**

Pourquoi un code de Huffman est-il un code **préfixe** ? Que se passerait-il si ce n'était pas le cas ?

**Correction**

Dans un arbre de Huffman, les symboles sont uniquement aux **feuilles** : le chemin menant à une feuille ne passe jamais par une autre feuille, donc aucun code n'est le préfixe d'un autre. C'est un **code préfixe**, ce qui permet un décodage sans ambiguïté en un seul parcours.

Sans cette propriété, le décodage serait ambigu. Par exemple avec `a = 0`, `b = 01`, `c = 1`, la chaîne `01` peut se lire `b` ou `ac`.

## 10.7 Autres exemples gloutons

**Exercice 10.7.1**

Cinq tâches ont pour durées `[3, 1, 4, 2, 5]`. Dans quel ordre les traiter pour minimiser la somme des temps d'attente ? Calculez cette somme et comparez avec l'ordre initial.

**Correction**

Pour minimiser la somme des temps d'attente, on traite les tâches par **durée croissante** : `1, 2, 3, 4, 5`. Une tâche courte placée tôt retarde moins de tâches (échange : permuter deux tâches voisines dans l'ordre inverse fait strictement baisser la somme).

- Ordre glouton `1, 2, 3, 4, 5` : temps d'attente (avant démarrage) `0, 1, 3, 6, 10`, soit **20** (ou **35** si l'on additionne les temps de fin `1, 3, 6, 10, 15`).
- Ordre initial `3, 1, 4, 2, 5` : temps d'attente `0, 3, 4, 8, 10`, soit **25** (ou **40** avec les temps de fin).

Le gain est de 5 dans les deux conventions.

**Exercice 10.7.2**

Ordonnancement avec échéances : on donne des tâches `(profit, échéance)` de durée unitaire ; écrivez un algorithme glouton maximisant le profit total.

**Correction**

Glouton : on trie les tâches par profit décroissant, et on place chacune au **dernier créneau libre** avant son échéance (si aucun n'existe, on la rejette).

```python
def ordonnancement(taches):
    """taches : liste de (profit, echeance), chaque tache dure 1 unité."""
    taches = sorted(taches, reverse=True)
    maxi = max(e for _, e in taches)
    creneaux = [None] * (maxi + 1)             # créneaux 1..maxi
    total = 0
    for profit, echeance in taches:
        for t in range(min(echeance, maxi), 0, -1):
            if creneaux[t] is None:
                creneaux[t] = (profit, echeance)
                total += profit
                break
    return total, creneaux[1:]


print(ordonnancement([(100, 2), (19, 1), (27, 2), (25, 1), (15, 3)]))
# (142, [(27, 2), (100, 2), (15, 3)])
```

Complexité : O(n log n + n · D) avec `D` l'échéance maximale (O(n log n) en utilisant une structure Union-Find pour trouver le créneau libre).

**Exercice 10.7.3**

Un voyageur peut parcourir `d` kilomètres avec un plein et doit traverser une route avec des stations à des positions données. Écrivez un algorithme glouton qui minimise le nombre d'arrêts.

**Correction**

Stratégie : partir de la position courante, aller à la **station la plus lointaine atteignable** avec un plein, s'y arrêter, et recommencer ; on s'arrête à la destination.

```python
def arrets_minimum(stations, destination, d):
    """stations : positions (en km depuis le départ) ; d : autonomie."""
    stations = sorted(stations)
    arrets, position, i, n = 0, 0, 0, len(stations)
    while position + d < destination:
        derniere = None
        while i < n and stations[i] <= position + d:
            derniere = stations[i]
            i += 1
        if derniere is None:
            return -1                      # aucune station atteignable : impossible
        position = derniere
        arrets += 1
    return arrets


print(arrets_minimum([10, 20, 30, 40, 50, 60], 70, 25))   # 3 (arrêts à 20, 40, 60)
```

Complexité O(n log n) (tri) puis O(n). Correction par échange : s'arrêter à la dernière station atteignable ne peut pas faire plus d'arrêts que toute autre stratégie.

**Exercice 10.7.4**

Rendu de monnaie : écrivez la version gloutonne et la version par programmation dynamique, et trouvez par un programme un système de 3 pièces dont le glouton n'est pas optimal.

**Correction**

```python
def glouton(pieces, montant):
    n = 0
    for p in sorted(pieces, reverse=True):
        n += montant // p
        montant %= p
    return n if montant == 0 else None


def dp_monnaie(pieces, montant):
    inf = float("inf")
    dp = [0] + [inf] * montant
    for m in range(1, montant + 1):
        for p in pieces:
            if p <= m:
                dp[m] = min(dp[m], dp[m - p] + 1)
    return dp[montant]


def chercher_contre_exemple(max_piece=10):
    for b in range(2, max_piece + 1):
        for c in range(b + 1, max_piece + 1):
            pieces = [1, b, c]
            for montant in range(1, 2 * c + 1):
                if glouton(pieces, montant) != dp_monnaie(pieces, montant):
                    return pieces, montant, glouton(pieces, montant), dp_monnaie(pieces, montant)


print(chercher_contre_exemple())   # ([1, 3, 4], 6, 3, 2)
```

Le premier système de 3 pièces trouvé est `[1, 3, 4]` avec le montant 6 : le glouton donne 3 pièces (`4 + 1 + 1`), la programmation dynamique 2 (`3 + 3`). Le glouton coûte O(k) après tri, la programmation dynamique O(montant × k).

## 10.8 Glouton ou programmation dynamique ?

**Exercice 10.8.1**

Pour chaque problème, dites si le glouton suffit ou si la programmation dynamique est nécessaire, en justifiant : sac à dos fractionnaire, sac à dos 0/1, sélection d'activités, plus longue sous-séquence commune, rendu de monnaie (système quelconque), arbre couvrant minimal.

**Correction**

| Problème | Glouton ou programmation dynamique ? |
| --- | --- |
| Sac à dos fractionnaire | **Glouton** (tri par rapport valeur/poids) : on peut prendre des fractions. |
| Sac à dos 0/1 | **Programmation dynamique** : le glouton échoue (exercice 10.5.3). |
| Sélection d'activités | **Glouton** (tri par heure de fin), prouvé par échange. |
| Plus longue sous-séquence commune | **Programmation dynamique** : les sous-problèmes se chevauchent, pas de choix local sûr. |
| Rendu de monnaie (système quelconque) | **Programmation dynamique** : le glouton n'est correct que pour les systèmes canoniques. |
| Arbre couvrant minimal | **Glouton** (Kruskal, Prim) : propriété de la coupe. |

---

# 11. Retour sur trace (*backtracking*)

## 11.1 Principe

**Exercice 11.1.1**

Expliquez en quelques phrases la différence entre la force brute et le retour sur trace. Qu'est-ce que l'**élagage** ?

**Correction**

- La **force brute** génère **toutes** les configurations candidates complètes, puis teste chacune.
- Le **retour sur trace** construit la solution **pas à pas** : après chaque choix partiel, il vérifie les contraintes et, dès qu'une impasse est détectée, il **revient en arrière** (annule le dernier choix) pour en essayer un autre. Il évite ainsi d'explorer toutes les configurations qui prolongeraient une configuration déjà invalide.
- L'**élagage** est la coupure d'une branche entière de l'arbre d'exploration dès qu'on sait qu'elle ne peut mener à aucune solution (contrainte déjà violée, objectif inatteignable, borne dépassée).

**Exercice 11.1.2**

Dessinez l'arbre d'exploration pour le choix de 2 éléments parmi `{1, 2, 3}` (avec ordre croissant imposé), en marquant les branches élaguées.

**Correction**

Choix de 2 éléments parmi `{1, 2, 3}`, en imposant l'ordre croissant :

```text
[]
├── [1]
│   ├── [1, 2]   solution
│   └── [1, 3]   solution
├── [2]
│   └── [2, 3]   solution
└── [3]          branche élaguée : aucun élément plus grand ne reste,
                 impossible d'atteindre 2 éléments
```

Sans l'ordre croissant, on explorerait aussi `[2, 1]`, `[3, 1]`, `[3, 2]`, `[1, 1]`, etc. : l'ordre imposé élague ces branches.

## 11.2 Schéma général

**Exercice 11.2.1**

Écrivez le schéma général d'un retour sur trace (choisir, explorer, annuler) sous forme de pseudo-code, puis adaptez-le pour énumérer tous les mots binaires de longueur `n`.

**Correction**

**Schéma général** :

```text
PROCEDURE Explorer(solution_partielle)
  SI solution_partielle est complète ALORS
      enregistrer (ou afficher) la solution
      RETOURNER
  POUR chaque choix c possible à cette étape FAIRE
      SI c est valide (compatible avec solution_partielle) ALORS
          ajouter c à solution_partielle        // choisir
          Explorer(solution_partielle)          // explorer
          retirer c de solution_partielle       // annuler (retour sur trace)
```

**Mots binaires de longueur `n`** :

```python
def mots_binaires(n):
    resultat, mot = [], []

    def explorer():
        if len(mot) == n:
            resultat.append("".join(mot))
            return
        for c in "01":
            mot.append(c)        # choisir
            explorer()           # explorer
            mot.pop()            # annuler

    explorer()
    return resultat


print(mots_binaires(3))
# ['000', '001', '010', '011', '100', '101', '110', '111']
```

**Exercice 11.2.2**

Écrivez un retour sur trace qui énumère tous les mots de longueur `n` sur l'alphabet `{a, b, c}` sans deux lettres identiques consécutives.

**Correction**

La contrainte de validité est « la nouvelle lettre est différente de la dernière lettre choisie ».

```python
def mots_sans_repetition(n, alphabet="abc"):
    resultat, mot = [], []

    def explorer():
        if len(mot) == n:
            resultat.append("".join(mot))
            return
        for c in alphabet:
            if mot and mot[-1] == c:        # élagage
                continue
            mot.append(c)
            explorer()
            mot.pop()

    explorer()
    return resultat


print(mots_sans_repetition(2))
# ['ab', 'ac', 'ba', 'bc', 'ca', 'cb']
print(len(mots_sans_repetition(4)))   # 3 * 2**3 = 24
```

Le nombre de mots est `3 × 2ⁿ⁻¹` (3 choix pour la première lettre, 2 pour les suivantes).

## 11.3 Exemple : sous-ensembles et permutations

**Exercice 11.3.1**

Écrivez `sous_ensembles(t)` par retour sur trace. Combien de sous-ensembles pour `n = 10` ? Retrouvez le résultat avec `itertools`.

**Correction**

```python
from itertools import chain, combinations


def sous_ensembles(t):
    resultat, courant = [], []

    def explorer(i):
        if i == len(t):
            resultat.append(courant[:])
            return
        explorer(i + 1)              # sans t[i]
        courant.append(t[i])         # avec t[i]
        explorer(i + 1)
        courant.pop()

    explorer(0)
    return resultat


print(sous_ensembles([1, 2, 3]))
# [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]

n = 10
print(len(sous_ensembles(list(range(n)))))    # 1024 = 2**10
via_itertools = list(chain.from_iterable(combinations(range(n), r) for r in range(n + 1)))
print(len(via_itertools))                      # 1024
```

Pour `n = 10`, il y a `2¹⁰ = 1024` sous-ensembles. Chaque élément est « pris » ou « non pris ».

**Exercice 11.3.2**

Écrivez `permutations(t)` par retour sur trace. Combien d'appels récursifs pour `n = 4` ?

**Correction**

```python
def permutations(t):
    resultat, courant = [], []
    utilise = [False] * len(t)

    def explorer():
        if len(courant) == len(t):
            resultat.append(courant[:])
            return
        for i in range(len(t)):
            if not utilise[i]:
                utilise[i] = True
                courant.append(t[i])
                explorer()
                courant.pop()
                utilise[i] = False

    explorer()
    return resultat


print(len(permutations([1, 2, 3, 4])))   # 24
```

Nombre d'appels récursifs (nœuds de l'arbre d'exploration) pour `n = 4` : `1 + 4 + 12 + 24 + 24 = ` **65** appels (profondeurs 0 à 4 : `n!/(n − k)!` nœuds à la profondeur `k`).

**Exercice 11.3.3**

Écrivez `combinaisons(t, k)` qui renvoie toutes les combinaisons de `k` éléments. Comparez avec `itertools.combinations`.

**Correction**

```python
import itertools


def combinaisons(t, k):
    resultat, courant = [], []

    def explorer(debut):
        if len(courant) == k:
            resultat.append(courant[:])
            return
        for i in range(debut, len(t)):
            if len(t) - i < k - len(courant):      # élagage : pas assez d'éléments restants
                break
            courant.append(t[i])
            explorer(i + 1)
            courant.pop()

    explorer(0)
    return resultat


t = [1, 2, 3, 4]
print(combinaisons(t, 2))
# [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
print(combinaisons(t, 2) == [list(c) for c in itertools.combinations(t, 2)])   # True
```

Il y a `C(n, k)` combinaisons.

**Exercice 11.3.4**

Écrivez `permutations_uniques(t)` pour une liste contenant des doublons (par exemple `[1, 1, 2]`), sans générer deux fois la même permutation.

**Correction**

On trie la liste et, à un même niveau de l'arbre, on **ne retient qu'une fois chaque valeur** : on saute un élément égal au précédent si ce dernier n'a pas été utilisé dans le chemin courant.

```python
def permutations_uniques(t):
    t = sorted(t)
    resultat, courant = [], []
    utilise = [False] * len(t)

    def explorer():
        if len(courant) == len(t):
            resultat.append(courant[:])
            return
        for i in range(len(t)):
            if utilise[i]:
                continue
            if i > 0 and t[i] == t[i - 1] and not utilise[i - 1]:
                continue                       # doublon déjà exploré à ce niveau
            utilise[i] = True
            courant.append(t[i])
            explorer()
            courant.pop()
            utilise[i] = False

    explorer()
    return resultat


print(permutations_uniques([1, 1, 2]))   # [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
```

**Exercice 11.3.5**

Écrivez `sous_ensembles_somme(t, cible)` : tous les sous-ensembles dont la somme vaut `cible`, avec élagage (les éléments sont positifs).

**Correction**

Les éléments étant positifs, on trie par ordre croissant : dès que la somme courante dépasse la cible, on coupe la branche (et toutes les suivantes du même niveau).

```python
def sous_ensembles_somme(t, cible):
    t = sorted(t)
    resultat, courant = [], []

    def explorer(debut, reste):
        if reste == 0:
            resultat.append(courant[:])
            return
        for i in range(debut, len(t)):
            if t[i] > reste:                 # élagage : tous les suivants sont plus grands
                break
            courant.append(t[i])
            explorer(i + 1, reste - t[i])
            courant.pop()

    explorer(0, cible)
    return resultat


print(sous_ensembles_somme([3, 34, 4, 12, 5, 2], 9))   # [[2, 3, 4], [4, 5]]
```

**Exercice 11.3.6**

Générez toutes les chaînes de `n` paires de parenthèses bien formées. Combien y en a-t-il pour `n = 4` ?

**Correction**

On place `(` tant qu'il en reste à placer, et `)` seulement s'il y a plus de `(` ouvertes que de `)` fermées.

```python
def parentheses(n):
    resultat = []

    def explorer(s, ouvertes, fermees):
        if len(s) == 2 * n:
            resultat.append(s)
            return
        if ouvertes < n:
            explorer(s + "(", ouvertes + 1, fermees)
        if fermees < ouvertes:
            explorer(s + ")", ouvertes, fermees + 1)

    explorer("", 0, 0)
    return resultat


print(parentheses(3))
# ['((()))', '(()())', '(())()', '()(())', '()()()']
print(len(parentheses(4)))   # 14
```

Pour `n = 4`, il y en a **14**, le quatrième nombre de Catalan `C₄ = C(8, 4)/5`.

## 11.4 Problème des N reines

**Exercice 11.4.1**

Pour `n = 4`, déroulez à la main le retour sur trace (ligne par ligne) et trouvez les solutions.

**Correction**

Les reines sont placées ligne par ligne ; on note la colonne choisie à chaque ligne.

- Ligne 0, colonne 0 :
  - ligne 1 : colonnes 0 et 1 attaquées (colonne, diagonale) ; colonne 2 acceptée. Ligne 2 : colonnes 0, 2 (colonne), 1 et 3 (diagonales de la reine en ligne 1) toutes attaquées : **impasse**, retour sur trace.
  - ligne 1, colonne 3 : ligne 2, colonne 1 acceptée ; ligne 3 : colonne 0 (colonne), 1 (colonne), 2 (diagonale avec la ligne 2), 3 (colonne) : **impasse**. Ligne 2, colonnes 0, 2, 3 : attaquées. Retour sur trace : la colonne 0 de la ligne 0 n'a aucune solution.
- Ligne 0, colonne 1 : ligne 1, colonne 3 ; ligne 2, colonne 0 ; ligne 3, colonne 2 : **solution** `[1, 3, 0, 2]`.
- Ligne 0, colonne 2 : par symétrie, ligne 1 colonne 0 ; ligne 2 colonne 3 ; ligne 3 colonne 1 : **solution** `[2, 0, 3, 1]`.
- Ligne 0, colonne 3 : symétrique de la colonne 0, aucune solution.

Les deux solutions pour `n = 4` :

```text
. Q . .        . . Q .
. . . Q        Q . . .
Q . . .        . . . Q
. . Q .        . Q . .
```

**Exercice 11.4.2**

Implémentez `n_reines(n)` qui renvoie toutes les solutions, puis le nombre de solutions pour `n = 1` à `8`.

**Correction**

```python
def n_reines(n):
    solutions, positions = [], []

    def attaque(r, c):
        for r2, c2 in enumerate(positions):
            if c2 == c or abs(c2 - c) == r - r2:
                return True
        return False

    def explorer(r):
        if r == n:
            solutions.append(positions[:])
            return
        for c in range(n):
            if not attaque(r, c):
                positions.append(c)
                explorer(r + 1)
                positions.pop()

    explorer(0)
    return solutions


print(n_reines(4))                              # [[1, 3, 0, 2], [2, 0, 3, 1]]
print([len(n_reines(n)) for n in range(1, 9)])
# [1, 0, 0, 2, 10, 4, 40, 92]
```

Nombre de solutions pour `n = 1` à `8` : `1, 0, 0, 2, 10, 4, 40, 92`.

**Exercice 11.4.3**

Optimisez le test de conflit en O(1) avec trois ensembles (colonnes, diagonales, anti-diagonales).

**Correction**

On mémorise les colonnes occupées, les diagonales (`r − c` constant) et les anti-diagonales (`r + c` constant) dans trois ensembles : le test de conflit devient O(1).

```python
def n_reines_rapide(n):
    solutions, positions = [], []
    colonnes, diag, anti = set(), set(), set()

    def explorer(r):
        if r == n:
            solutions.append(positions[:])
            return
        for c in range(n):
            if c in colonnes or (r - c) in diag or (r + c) in anti:
                continue
            colonnes.add(c)
            diag.add(r - c)
            anti.add(r + c)
            positions.append(c)
            explorer(r + 1)
            positions.pop()
            colonnes.remove(c)
            diag.remove(r - c)
            anti.remove(r + c)

    explorer(0)
    return solutions


print(len(n_reines_rapide(8)))   # 92
```

**Exercice 11.4.4**

Combien de solutions pour `n = 8` ? Combien d'entre elles sont distinctes à rotation et symétrie près ? *(défi)*

**Correction**

Pour `n = 8`, il y a **92 solutions**. En identifiant celles qui se déduisent l'une de l'autre par rotation (de 90°, 180°, 270°) ou par symétrie (miroir), on obtient **12 solutions distinctes**.

```python
def transformations(sol):
    n = len(sol)
    pts = list(enumerate(sol))
    resultats = []
    for _ in range(4):
        pts = [(c, n - 1 - r) for r, c in pts]                 # rotation de 90 degrés
        for p in (pts, [(r, n - 1 - c) for r, c in pts]):      # et son miroir
            s = [0] * n
            for r, c in p:
                s[r] = c
            resultats.append(tuple(s))
    return resultats


canoniques = {min(transformations(s)) for s in n_reines_rapide(8)}
print(len(canoniques))    # 12
```

On remplace chaque solution par le plus petit représentant de ses 8 images (4 rotations, avec ou sans miroir) et on compte les représentants distincts.

## 11.5 Solveur de Sudoku

**Exercice 11.5.1**

Écrivez `est_valide(grille, ligne, colonne, valeur)` pour une grille 9×9.

**Correction**

```python
def est_valide(grille, ligne, colonne, valeur):
    for k in range(9):
        if grille[ligne][k] == valeur or grille[k][colonne] == valeur:
            return False
    l0, c0 = 3 * (ligne // 3), 3 * (colonne // 3)
    for i in range(l0, l0 + 3):
        for j in range(c0, c0 + 3):
            if grille[i][j] == valeur:
                return False
    return True
```

La fonction vérifie qu'aucune case de la même ligne, de la même colonne ni du même bloc 3×3 ne contient déjà `valeur`. Les cases vides valent 0.

**Exercice 11.5.2**

Écrivez un solveur de Sudoku par retour sur trace. Testez-le sur une grille de votre choix et mesurez le nombre de retours en arrière.

**Correction**

```python
compteur = {"retours": 0}


def resoudre(grille):
    for ligne in range(9):
        for colonne in range(9):
            if grille[ligne][colonne] == 0:
                for valeur in range(1, 10):
                    if est_valide(grille, ligne, colonne, valeur):
                        grille[ligne][colonne] = valeur
                        if resoudre(grille):
                            return True
                        grille[ligne][colonne] = 0            # annuler
                        compteur["retours"] += 1
                return False                                  # aucune valeur ne convient
    return True                                               # grille pleine : résolue


grille = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]
print(resoudre(grille), compteur)    # True {'retours': 4157}
print(grille[0])                      # [5, 3, 4, 6, 7, 8, 9, 1, 2]
```

Sur cette grille classique, le solveur effectue environ **4157 retours en arrière**.

**Exercice 11.5.3**

Améliorez-le avec l'heuristique « case la plus contrainte d'abord » (celle qui a le moins de valeurs possibles). Quel gain observez-vous ?

**Correction**

On choisit la case vide qui possède le **moins de candidats** (heuristique MRV, *minimum remaining values*) : les choix forcés sont traités en premier et les impasses sont détectées tôt.

```python
def candidats(grille, l, c):
    return [v for v in range(1, 10) if est_valide(grille, l, c, v)]


def resoudre_mrv(grille):
    meilleur = None
    for l in range(9):
        for c in range(9):
            if grille[l][c] == 0:
                cand = candidats(grille, l, c)
                if meilleur is None or len(cand) < len(meilleur[2]):
                    meilleur = (l, c, cand)
    if meilleur is None:
        return True
    l, c, cand = meilleur
    for v in cand:
        grille[l][c] = v
        if resoudre_mrv(grille):
            return True
        grille[l][c] = 0
        compteur["retours"] += 1
    return False
```

Gain observé : sur la grille de l'exercice précédent, le nombre de retours passe de **4157 à 0** (chaque case choisie a une valeur forcée) ; sur des grilles très difficiles (peu d'indices), on passe typiquement de plusieurs centaines de milliers de retours à quelques milliers. Le coût de sélection d'une case est plus élevé, mais l'élagage compense largement.

## 11.6 Autres problèmes classiques

**Exercice 11.6.1**

Rat dans un labyrinthe : écrivez un programme qui trouve un chemin du coin supérieur gauche au coin inférieur droit d'une grille de 0 (libre) et 1 (mur).

**Correction**

```python
def chemin_labyrinthe(grille):
    n, m = len(grille), len(grille[0])
    visite = [[False] * m for _ in range(n)]
    chemin = []

    def explorer(i, j):
        if not (0 <= i < n and 0 <= j < m) or grille[i][j] == 1 or visite[i][j]:
            return False
        visite[i][j] = True
        chemin.append((i, j))
        if (i, j) == (n - 1, m - 1):
            return True
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if explorer(i + di, j + dj):
                return True
        chemin.pop()                      # impasse : retour sur trace
        return False

    return chemin if explorer(0, 0) else None


labyrinthe = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 0, 0],
]
print(chemin_labyrinthe(labyrinthe))
# [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (3, 3)]
```

On marque les cases visitées pour ne pas boucler. Ce chemin n'est pas forcément le plus court (pour cela, utiliser un BFS).

**Exercice 11.6.2**

Coloration de graphe : écrivez `colorier(graphe, k)` qui cherche une coloration avec `k` couleurs.

**Correction**

```python
def colorier(graphe, k):
    """graphe : liste d'adjacence. Renvoie une liste de couleurs ou None."""
    n = len(graphe)
    couleur = [-1] * n

    def explorer(sommet):
        if sommet == n:
            return True
        for c in range(k):
            if all(couleur[v] != c for v in graphe[sommet]):
                couleur[sommet] = c
                if explorer(sommet + 1):
                    return True
                couleur[sommet] = -1
        return False

    return couleur if explorer(0) else None


triangle_plus_un = [[1, 2], [0, 2], [0, 1, 3], [2]]
print(colorier(triangle_plus_un, 3))   # [0, 1, 2, 0]
print(colorier(triangle_plus_un, 2))   # None (le triangle exige 3 couleurs)
```

**Exercice 11.6.3**

Somme de sous-ensemble : déterminez s'il existe un sous-ensemble de `[3, 34, 4, 12, 5, 2]` dont la somme vaut 9.

**Correction**

Il existe un sous-ensemble de `[3, 34, 4, 12, 5, 2]` de somme 9 : par exemple `{4, 5}` ou `{2, 3, 4}`.

```python
def somme_sous_ensemble(t, cible):
    def explorer(i, reste):
        if reste == 0:
            return True
        if i == len(t) or reste < 0:
            return False
        return explorer(i + 1, reste - t[i]) or explorer(i + 1, reste)

    return explorer(0, cible)


print(somme_sous_ensemble([3, 34, 4, 12, 5, 2], 9))    # True
print(somme_sous_ensemble([3, 34, 4, 12, 5, 2], 30))   # False
```

**Exercice 11.6.4**

Chemin hamiltonien : écrivez un retour sur trace qui cherche un chemin passant exactement une fois par chaque sommet d'un graphe.

**Correction**

```python
def chemin_hamiltonien(graphe):
    n = len(graphe)
    visite = [False] * n
    chemin = []

    def explorer(sommet):
        visite[sommet] = True
        chemin.append(sommet)
        if len(chemin) == n:
            return True
        for v in graphe[sommet]:
            if not visite[v] and explorer(v):
                return True
        chemin.pop()                      # retour sur trace
        visite[sommet] = False
        return False

    for depart in range(n):
        if explorer(depart):
            return chemin
    return None


g = [[1, 3], [0, 2, 3], [1, 3], [0, 1, 2]]
print(chemin_hamiltonien(g))   # [0, 1, 2, 3]
```

Pire cas O(n!) ; on essaie chaque sommet de départ.

**Exercice 11.6.5**

Recherche de mots dans une grille : étant donné une grille de lettres et un mot, déterminez si le mot s'écrit en se déplaçant de case en case (voisines horizontalement ou verticalement), sans réutiliser une case.

**Correction**

```python
def mot_dans_grille(grille, mot):
    n, m = len(grille), len(grille[0])

    def explorer(i, j, k):
        if k == len(mot):
            return True
        if not (0 <= i < n and 0 <= j < m) or grille[i][j] != mot[k]:
            return False
        sauvegarde = grille[i][j]
        grille[i][j] = "#"                 # case marquée : non réutilisable
        trouve = (explorer(i + 1, j, k + 1) or explorer(i - 1, j, k + 1) or
                  explorer(i, j + 1, k + 1) or explorer(i, j - 1, k + 1))
        grille[i][j] = sauvegarde          # annuler le marquage
        return trouve

    return any(explorer(i, j, 0) for i in range(n) for j in range(m))


g = [list("ABCE"), list("SFCS"), list("ADEE")]
print(mot_dans_grille(g, "ABCCED"))   # True
print(mot_dans_grille(g, "ABCB"))     # False (la case B ne peut pas être réutilisée)
```

**Exercice 11.6.6** *(défi)*

Parcours du cavalier : écrivez un programme qui trouve un tour complet sur un échiquier 6×6 avec l'heuristique de Warnsdorff.

**Correction**

On utilise l'heuristique de Warnsdorff : à chaque saut, on essaie d'abord la case destination qui a le **moins de mouvements ultérieurs possibles**. On la combine avec un retour sur trace pour garantir la complétude.

```python
def tour_cavalier(n, depart=(0, 0)):
    mouvements = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
    echiquier = [[-1] * n for _ in range(n)]

    def voisins(x, y):
        return [(x + dx, y + dy) for dx, dy in mouvements
                if 0 <= x + dx < n and 0 <= y + dy < n and echiquier[x + dx][y + dy] == -1]

    def explorer(x, y, k):
        echiquier[x][y] = k
        if k == n * n - 1:
            return True
        for a, b in sorted(voisins(x, y), key=lambda p: len(voisins(*p))):
            if explorer(a, b, k + 1):
                return True
        echiquier[x][y] = -1
        return False

    return echiquier if explorer(*depart, 0) else None


for ligne in tour_cavalier(6):
    print(ligne)
```

Sortie typique (numéro du saut dans chaque case) :

```text
[0, 31, 8, 17, 2, 33]
[9, 18, 1, 32, 27, 16]
[30, 7, 28, 15, 34, 3]
[19, 10, 35, 26, 23, 14]
[6, 29, 12, 21, 4, 25]
[11, 20, 5, 24, 13, 22]
```

Sans l'heuristique, la recherche pure par retour sur trace est beaucoup trop longue dès 6×6 ; avec elle, un tour est trouvé presque instantanément.

## 11.7 Complexité et comparaison

**Exercice 11.7.1**

Donnez la complexité dans le pire cas pour : énumérer les sous-ensembles, énumérer les permutations, résoudre les `n` reines naïvement. Expliquez pourquoi l'élagage ne change pas le pire cas.

**Correction**

Complexités dans le pire cas :

- **Sous-ensembles** : `2ⁿ` sous-ensembles, soit **O(n · 2ⁿ)** en comptant la copie de chacun.
- **Permutations** : `n!` permutations, soit **O(n · n!)**.
- **`n` reines naïves** (n'importe quelle colonne dans chaque ligne, test à la fin) : **O(nⁿ)** configurations ; avec la contrainte « une reine par ligne et par colonne », **O(n!)**.

L'élagage **ne change pas le pire cas** : il ne réduit l'arbre que pour les instances où des contraintes se déclenchent tôt. Il existe des instances où aucune branche ne peut être coupée avant d'atteindre le fond (par exemple, une somme de sous-ensemble dont la cible n'est jamais dépassée et jamais atteinte). La borne supérieure reste donc exponentielle ; l'élagage améliore seulement le comportement typique, parfois de plusieurs ordres de grandeur.

**Exercice 11.7.2**

Ajoutez de la mémoïsation au problème de la somme de sous-ensemble (état `(indice, reste)`). Que devient la complexité ? Quel nom donne-t-on alors à la technique ?

**Correction**

```python
from functools import cache


def somme_sous_ensemble_memo(t, cible):
    @cache
    def f(i, reste):
        if reste == 0:
            return True
        if i == len(t) or reste < 0:
            return False
        return f(i + 1, reste - t[i]) or f(i + 1, reste)

    return f(0, cible)


print(somme_sous_ensemble_memo([3, 34, 4, 12, 5, 2], 9))   # True
```

Le nombre d'états `(i, reste)` distincts est au plus `n × (cible + 1)`, chacun traité en O(1) : la complexité devient **O(n · cible)** (pseudo-polynomiale) au lieu de O(2ⁿ). La technique s'appelle la **programmation dynamique** (en version descendante, ou **mémoïsation**).

**Exercice 11.7.3**

Remplissez le tableau comparatif (exploration, retour en arrière, sous-problèmes répétés, optimalité) pour retour sur trace, glouton et programmation dynamique, sans consulter le cours.

**Correction**

| Technique | Exploration | Retour en arrière | Sous-problèmes répétés | Optimalité |
| --- | --- | --- | --- | --- |
| Retour sur trace | exploration systématique de l'arbre des choix, avec élagage | **oui** (annulation des choix) | **recalculés** à chaque fois (aucune mémorisation) | solution exacte (toutes les solutions ou l'optimum), mais coût exponentiel |
| Glouton | **un seul chemin** : un choix local à chaque étape | **non** (les choix sont définitifs) | sans objet (aucun sous-problème revisité) | optimal **seulement** si le problème a la propriété du choix glouton |
| Programmation dynamique | tous les sous-problèmes, chacun une seule fois | **non** (calcul dans un ordre défini, ou récursion mémoïsée) | **mémorisés** et réutilisés | optimal, si le problème a une sous-structure optimale |

---

# 12. Technique des deux pointeurs

## 12.1 Principe

**Exercice 12.1.1**

Décrivez les deux grandes variantes de la technique (pointeurs aux extrémités, pointeurs rapide et lent). Donnez un problème pour chaque variante.

**Correction**

**Variante 1 : pointeurs aux extrémités (qui convergent).** Un pointeur au début, un à la fin ; on les rapproche selon une condition, généralement sur un tableau **trié** ou symétrique. Problème : trouver deux éléments d'un tableau trié de somme donnée (ou tester un palindrome).

**Variante 2 : pointeurs rapide et lent (qui avancent dans le même sens).** Les deux pointeurs partent du début ; l'un avance plus vite que l'autre (ou l'un sert à lire, l'autre à écrire). Problème : détecter un cycle dans une liste chaînée (lièvre et tortue de Floyd), ou supprimer les doublons d'un tableau trié en place.

## 12.2 Somme de deux nombres dans un tableau trié

**Exercice 12.2.1**

Écrivez `deux_somme_trie(t, cible)` qui renvoie un couple d'indices `(i, j)` avec `i < j` tels que `t[i] + t[j] == cible`, en O(n) temps et O(1) espace.

**Correction**

```python
def deux_somme_trie(t, cible):
    i, j = 0, len(t) - 1
    while i < j:
        s = t[i] + t[j]
        if s == cible:
            return (i, j)
        if s < cible:
            i += 1            # il faut une somme plus grande
        else:
            j -= 1            # il faut une somme plus petite
    return None


print(deux_somme_trie([1, 3, 4, 6, 8, 11], 10))   # (2, 3)
print(deux_somme_trie([1, 3, 4, 6, 8, 11], 20))   # None
```

Temps O(n), espace O(1).

**Exercice 12.2.2**

Déroulez à la main votre algorithme sur `t = [1, 3, 4, 6, 8, 11]` et `cible = 10`, puis `cible = 20`.

**Correction**

Pour `t = [1, 3, 4, 6, 8, 11]` :

**Cible 10** :

| `i` | `j` | `t[i] + t[j]` | Décision |
| --- | --- | --- | --- |
| 0 | 5 | 1 + 11 = 12 | trop grand : `j = 4` |
| 0 | 4 | 1 + 8 = 9 | trop petit : `i = 1` |
| 1 | 4 | 3 + 8 = 11 | trop grand : `j = 3` |
| 1 | 3 | 3 + 6 = 9 | trop petit : `i = 2` |
| 2 | 3 | 4 + 6 = 10 | trouvé : `(2, 3)` |

**Cible 20** : les sommes successives valent `12, 14, 15, 17, 19` (avec `j = 5` fixé et `i` de 0 à 4), toutes inférieures à 20 ; `i` atteint `j` et l'algorithme renvoie `None`.

**Exercice 12.2.3**

Justifiez la correction : pourquoi peut-on écarter un des deux pointeurs lorsque la somme est trop grande ou trop petite ?

**Correction**

Invariant : si une solution existe, elle est dans `[i, j]`.

- Si `t[i] + t[j] > cible`, alors `t[j]` ne peut s'associer avec aucun élément `t[k]` avec `k ≥ i` : en effet `t[k] ≥ t[i]`, donc `t[k] + t[j] ≥ t[i] + t[j] > cible`. Les éléments d'indice `< i` ont déjà été écartés. On peut donc éliminer `j`.
- Symétriquement, si `t[i] + t[j] < cible`, alors `t[i] + t[k] ≤ t[i] + t[j] < cible` pour tout `k ≤ j` : `t[i]` ne peut s'associer à rien, on élimine `i`.

À chaque étape on élimine un indice sans perdre de solution : au plus `n − 1` étapes.

**Exercice 12.2.4**

Adaptez l'algorithme pour compter le nombre de paires distinctes de somme `cible` dans un tableau trié avec doublons.

**Correction**

Après avoir trouvé une paire, on saute **toutes les copies** des deux valeurs pour ne compter qu'une fois chaque paire de valeurs.

```python
def compter_paires(t, cible):
    i, j, compte = 0, len(t) - 1, 0
    while i < j:
        s = t[i] + t[j]
        if s < cible:
            i += 1
        elif s > cible:
            j -= 1
        else:
            compte += 1
            a, b = t[i], t[j]
            while i < j and t[i] == a:
                i += 1
            while i < j and t[j] == b:
                j -= 1
    return compte


print(compter_paires([1, 1, 2, 3, 3, 4, 5], 6))   # 3 : (1,5), (2,4), (3,3)
```

Complexité O(n).

## 12.3 Autres exemples

**Exercice 12.3.1**

Écrivez `est_palindrome(s)` qui ignore la casse et les caractères non alphanumériques. Testez : `"A man, a plan, a canal: Panama"`.

**Correction**

```python
def est_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


print(est_palindrome("A man, a plan, a canal: Panama"))   # True
print(est_palindrome("race a car"))                        # False
```

Complexité O(n), espace O(1).

**Exercice 12.3.2**

Écrivez `supprimer_doublons_tries(t)` en place, qui renvoie la nouvelle longueur.

**Correction**

Le pointeur `lecture` parcourt le tableau ; le pointeur `ecriture` marque la fin de la partie sans doublons.

```python
def supprimer_doublons_tries(t):
    if not t:
        return 0
    ecriture = 1
    for lecture in range(1, len(t)):
        if t[lecture] != t[ecriture - 1]:
            t[ecriture] = t[lecture]
            ecriture += 1
    return ecriture


t = [1, 1, 2, 2, 2, 3]
n = supprimer_doublons_tries(t)
print(n, t[:n])    # 3 [1, 2, 3]
```

Temps O(n), espace O(1).

**Exercice 12.3.3**

Écrivez `trois_somme(t)` qui renvoie tous les triplets distincts de somme nulle. Quelle est la complexité ?

**Correction**

On trie, on fixe le premier élément `t[i]`, puis on cherche deux éléments de somme `−t[i]` avec deux pointeurs, en sautant les doublons.

```python
def trois_somme(t):
    t = sorted(t)
    resultat = []
    n = len(t)
    for i in range(n - 2):
        if i > 0 and t[i] == t[i - 1]:
            continue                       # doublon pour le premier élément
        g, d = i + 1, n - 1
        while g < d:
            s = t[i] + t[g] + t[d]
            if s < 0:
                g += 1
            elif s > 0:
                d -= 1
            else:
                resultat.append([t[i], t[g], t[d]])
                g += 1
                d -= 1
                while g < d and t[g] == t[g - 1]:
                    g += 1
    return resultat


print(trois_somme([-1, 0, 1, 2, -1, -4]))   # [[-1, -1, 2], [-1, 0, 1]]
```

Complexité : O(n log n) pour le tri plus O(n²) pour la boucle, soit **O(n²)**.

**Exercice 12.3.4**

Écrivez `aire_max_conteneur(h)` (« Container With Most Water »). Pourquoi déplacer le pointeur sur la plus petite hauteur est-il correct ?

**Correction**

```python
def aire_max_conteneur(h):
    i, j, meilleur = 0, len(h) - 1, 0
    while i < j:
        meilleur = max(meilleur, (j - i) * min(h[i], h[j]))
        if h[i] < h[j]:
            i += 1
        else:
            j -= 1
    return meilleur


print(aire_max_conteneur([1, 8, 6, 2, 5, 4, 8, 3, 7]))   # 49
```

**Pourquoi déplacer le pointeur de la plus petite hauteur** : l'aire est limitée par la plus petite des deux hauteurs. Si on déplaçait le pointeur de la plus grande, la largeur diminuerait et la hauteur resterait limitée par la plus petite : l'aire ne pourrait pas augmenter. En revanche, la plus petite barre, associée à n'importe quelle autre barre à l'intérieur (moins large), donne une aire inférieure ou égale à l'actuelle : on peut donc l'écarter sans perdre l'optimum. Complexité O(n).

**Exercice 12.3.5**

Écrivez `fusion_triee(a, b)` qui fusionne deux tableaux triés avec deux pointeurs, puis `intersection_triee(a, b)`.

**Correction**

```python
def fusion_triee(a, b):
    i = j = 0
    resultat = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            resultat.append(a[i])
            i += 1
        else:
            resultat.append(b[j])
            j += 1
    return resultat + a[i:] + b[j:]


def intersection_triee(a, b):
    i = j = 0
    resultat = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            if not resultat or resultat[-1] != a[i]:
                resultat.append(a[i])
            i += 1
            j += 1
    return resultat


print(fusion_triee([1, 3, 5], [2, 3, 6]))          # [1, 2, 3, 3, 5, 6]
print(intersection_triee([1, 2, 2, 3], [2, 2, 4])) # [2]
```

Les deux sont en O(n + m).

**Exercice 12.3.6**

Écrivez `deplacer_zeros(t)` qui déplace tous les zéros à la fin en conservant l'ordre des autres éléments, en place.

**Correction**

```python
def deplacer_zeros(t):
    ecriture = 0
    for lecture in range(len(t)):
        if t[lecture] != 0:
            t[ecriture], t[lecture] = t[lecture], t[ecriture]
            ecriture += 1
    return t


print(deplacer_zeros([0, 1, 0, 3, 12]))   # [1, 3, 12, 0, 0]
```

Les éléments non nuls conservent leur ordre relatif. Temps O(n), espace O(1), nombre d'écritures minimal.

**Exercice 12.3.7**

Écrivez `trier_couleurs(t)` qui trie en place un tableau ne contenant que des 0, des 1 et des 2, en un seul parcours (drapeau hollandais, trois pointeurs).

**Correction**

Trois pointeurs : `bas` (frontière des 0), `i` (élément examiné), `haut` (frontière des 2).

```python
def trier_couleurs(t):
    bas, i, haut = 0, 0, len(t) - 1
    while i <= haut:
        if t[i] == 0:
            t[bas], t[i] = t[i], t[bas]
            bas += 1
            i += 1
        elif t[i] == 2:
            t[i], t[haut] = t[haut], t[i]
            haut -= 1                     # on ne fait pas avancer i : l'élément échangé est à examiner
        else:
            i += 1
    return t


print(trier_couleurs([2, 0, 2, 1, 1, 0]))   # [0, 0, 1, 1, 2, 2]
```

Invariant : `t[:bas]` contient des 0, `t[bas:i]` des 1, `t[haut + 1:]` des 2. Un seul parcours, O(n), O(1) d'espace.

### Détection de cycle (lièvre et tortue de Floyd)

**Exercice 12.3.8**

Écrivez `a_un_cycle(tete)`. Pourquoi les deux pointeurs finissent-ils par se rencontrer s'il y a un cycle ?

**Correction**

```python
class Noeud:
    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant


def a_un_cycle(tete):
    lent = rapide = tete
    while rapide is not None and rapide.suivant is not None:
        lent = lent.suivant
        rapide = rapide.suivant.suivant
        if lent is rapide:
            return True
    return False
```

**Pourquoi ils se rencontrent** : s'il n'y a pas de cycle, `rapide` atteint la fin. S'il y en a un, les deux pointeurs finissent par y entrer. À l'intérieur du cycle, `rapide` gagne **une case** sur `lent` à chaque tour : la distance qui les sépare, mesurée dans le sens de parcours, diminue de 1 à chaque étape (modulo la longueur du cycle), donc elle atteint 0 en moins de `c` étapes (`c` = longueur du cycle) : les deux pointeurs se rencontrent. Temps O(n), espace O(1).

**Exercice 12.3.9** *(défi)*

Écrivez `debut_du_cycle(tete)` qui renvoie le premier nœud du cycle, ou `None`.

**Correction**

Après la rencontre, on remet `lent` en tête et on avance **les deux pointeurs d'un pas à la fois** : ils se rejoignent au début du cycle.

```python
def debut_du_cycle(tete):
    lent = rapide = tete
    while rapide is not None and rapide.suivant is not None:
        lent = lent.suivant
        rapide = rapide.suivant.suivant
        if lent is rapide:
            lent = tete
            while lent is not rapide:
                lent = lent.suivant
                rapide = rapide.suivant
            return lent
    return None
```

**Preuve** : soit `a` la distance de la tête au début du cycle, `b` la distance du début du cycle au point de rencontre, `c` la longueur du cycle. Quand ils se rencontrent, `lent` a parcouru `a + b` et `rapide` `2(a + b)`. La différence `a + b` est un multiple de `c` : `a + b = k·c`, donc `a = k·c − b`. Partant du point de rencontre, avancer de `a` pas revient donc au début du cycle, tout comme partir de la tête. Les deux pointeurs se retrouvent exactement au début du cycle.

**Exercice 12.3.10**

Détectez un doublon dans un tableau de `n + 1` entiers compris entre `1` et `n` en O(1) espace en interprétant le tableau comme une liste chaînée. *(défi)*

**Correction**

On interprète le tableau comme une liste chaînée : l'élément à l'indice `i` pointe vers l'indice `t[i]`. Comme il y a `n + 1` valeurs dans `[1, n]`, au moins deux indices pointent vers la même case : cela crée un **cycle**, dont l'entrée est la valeur dupliquée.

```python
def trouver_doublon(t):
    lent = rapide = t[0]
    while True:
        lent = t[lent]
        rapide = t[t[rapide]]
        if lent == rapide:
            break
    lent = t[0]
    while lent != rapide:
        lent = t[lent]
        rapide = t[rapide]
    return lent


print(trouver_doublon([1, 3, 4, 2, 2]))   # 2
print(trouver_doublon([3, 1, 3, 4, 2]))   # 3
```

Temps O(n), espace O(1), sans modifier le tableau.

## 12.4 Quand l'utiliser ?

**Exercice 12.4.1**

Pour chaque énoncé, dites si les deux pointeurs conviennent : chercher une paire de somme donnée dans un tableau non trié, dans un tableau trié, trouver le milieu d'une liste chaînée, trouver le plus long sous-tableau de somme nulle avec des valeurs négatives, vérifier un palindrome.

**Correction**

| Énoncé | Deux pointeurs ? |
| --- | --- |
| Paire de somme donnée, tableau **non trié** | Pas directement : il faut trier d'abord (O(n log n), et l'on perd les indices d'origine), ou utiliser un **dictionnaire** en O(n). |
| Paire de somme donnée, tableau **trié** | **Oui** (pointeurs aux extrémités). |
| Milieu d'une liste chaînée | **Oui** (pointeurs rapide et lent). |
| Plus long sous-tableau de somme nulle avec valeurs négatives | **Non** : la somme n'est pas monotone quand on étend ou réduit la fenêtre ; on utilise les **sommes préfixes** avec un dictionnaire. |
| Vérifier un palindrome | **Oui** (pointeurs aux extrémités). |

---

# 13. Fenêtre glissante

## 13.1 Principe

**Exercice 13.1.1**

Distinguez fenêtre de taille fixe et fenêtre de taille variable. Que maintient-on d'une itération à l'autre pour éviter de tout recalculer ?

**Correction**

- **Fenêtre de taille fixe** : la fenêtre a toujours `k` éléments ; à chaque pas on ajoute le nouvel élément à droite et on retire celui qui sort à gauche.
- **Fenêtre de taille variable** : la fenêtre s'agrandit à droite tant qu'une condition le permet et rétrécit à gauche quand elle est violée (ou satisfaite, selon que l'on cherche la plus longue ou la plus courte).

On maintient d'une itération à l'autre un **état** de la fenêtre (somme, compteurs de caractères, ensemble d'éléments, deque d'indices...) qu'on met à jour en O(1) lors de l'entrée et de la sortie d'un élément, au lieu de recalculer sur toute la fenêtre.

## 13.2 Taille fixe : somme maximale de `k` éléments consécutifs

**Exercice 13.2.1**

Écrivez `somme_max_k(t, k)` en O(n). Testez sur `[2, 1, 5, 1, 3, 2]` avec `k = 3`.

**Correction**

```python
def somme_max_k(t, k):
    fenetre = sum(t[:k])
    meilleur = fenetre
    for i in range(k, len(t)):
        fenetre += t[i] - t[i - k]       # entre t[i], sort t[i - k]
        meilleur = max(meilleur, fenetre)
    return meilleur


print(somme_max_k([2, 1, 5, 1, 3, 2], 3))   # 9 (5 + 1 + 3)
```

Complexité O(n) au lieu de O(n·k) en recalculant chaque somme.

**Exercice 13.2.2**

Écrivez `moyennes_glissantes(t, k)` qui renvoie la moyenne de chaque fenêtre de taille `k`.

**Correction**

```python
def moyennes_glissantes(t, k):
    fenetre = sum(t[:k])
    moyennes = [fenetre / k]
    for i in range(k, len(t)):
        fenetre += t[i] - t[i - k]
        moyennes.append(fenetre / k)
    return moyennes


print(moyennes_glissantes([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
# [2.2, 2.8, 2.4, 3.6, 2.8]
```

**Exercice 13.2.3**

Combien de voyelles contient au maximum une sous-chaîne de longueur `k` d'une chaîne donnée ?

**Correction**

```python
def max_voyelles(s, k):
    voyelles = set("aeiouy")
    courant = sum(1 for c in s[:k] if c in voyelles)
    meilleur = courant
    for i in range(k, len(s)):
        courant += (s[i] in voyelles) - (s[i - k] in voyelles)
        meilleur = max(meilleur, courant)
    return meilleur


print(max_voyelles("abciiidef", 3))   # 3 (la sous-chaîne "iii")
```

(Ici `y` est compté comme voyelle ; on peut le retirer de l'ensemble selon la convention choisie.) Complexité O(n).

## 13.3 Taille variable : plus longue sous-chaîne sans répétition

**Exercice 13.3.1**

Écrivez `plus_longue_sans_repetition(s)`. Testez : `"abcabcbb"`, `"bbbbb"`, `"pwwkew"`, `""`.

**Correction**

```python
def plus_longue_sans_repetition(s):
    dernier = {}
    gauche = meilleur = 0
    for droite, c in enumerate(s):
        if c in dernier and dernier[c] >= gauche:
            gauche = dernier[c] + 1           # on saute après l'occurrence précédente
        dernier[c] = droite
        meilleur = max(meilleur, droite - gauche + 1)
    return meilleur


for mot in ("abcabcbb", "bbbbb", "pwwkew", ""):
    print(repr(mot), plus_longue_sans_repetition(mot))
# 'abcabcbb' 3 ; 'bbbbb' 1 ; 'pwwkew' 3 ; '' 0
```

**Exercice 13.3.2**

Déroulez votre algorithme sur `"abcabcbb"` en notant la fenêtre `[gauche, droite]` à chaque étape.

**Correction**

Déroulement sur `"abcabcbb"` (`dernier[c]` est l'indice de la dernière occurrence de `c`) :

| `droite` | Caractère | `gauche` après mise à jour | Fenêtre `[gauche, droite]` | Longueur |
| --- | --- | --- | --- | --- |
| 0 | a | 0 | `[0, 0]` = "a" | 1 |
| 1 | b | 0 | `[0, 1]` = "ab" | 2 |
| 2 | c | 0 | `[0, 2]` = "abc" | 3 |
| 3 | a | 1 (a vu en 0) | `[1, 3]` = "bca" | 3 |
| 4 | b | 2 (b vu en 1) | `[2, 4]` = "cab" | 3 |
| 5 | c | 3 (c vu en 2) | `[3, 5]` = "abc" | 3 |
| 6 | b | 5 (b vu en 4) | `[5, 6]` = "cb" | 2 |
| 7 | b | 7 (b vu en 6) | `[7, 7]` = "b" | 1 |

Le meilleur est 3.

**Exercice 13.3.3**

Quelle est la complexité ? Pourquoi est-elle linéaire alors que le pointeur gauche avance dans une boucle imbriquée ?

**Correction**

Complexité **O(n)** en temps (et O(min(n, taille de l'alphabet)) en espace).

Le pointeur `droite` avance `n` fois, et le pointeur `gauche` **n'avance jamais en arrière** : il vaut au plus `n` à la fin. Même si on écrit le rétrécissement dans une boucle `while` imbriquée, le nombre total d'avances de `gauche` sur toute l'exécution est borné par `n`. Le coût est donc amorti : au plus `2n` opérations au total, et non `n²`.

## 13.4 Taille variable : plus petit sous-tableau de somme ≥ S (valeurs positives)

**Exercice 13.4.1**

Écrivez `plus_petit_sous_tableau(t, S)` renvoyant la longueur minimale, ou 0 s'il n'existe pas. Testez sur `[2, 3, 1, 2, 4, 3]` avec `S = 7`.

**Correction**

```python
def plus_petit_sous_tableau(t, S):
    gauche = somme = 0
    meilleur = float("inf")
    for droite, x in enumerate(t):
        somme += x
        while somme >= S:                       # on rétrécit tant que la condition tient
            meilleur = min(meilleur, droite - gauche + 1)
            somme -= t[gauche]
            gauche += 1
    return 0 if meilleur == float("inf") else meilleur


print(plus_petit_sous_tableau([2, 3, 1, 2, 4, 3], 7))   # 2 (le sous-tableau [4, 3])
print(plus_petit_sous_tableau([1, 1, 1], 10))           # 0
```

**Exercice 13.4.2**

Pourquoi la fenêtre glissante échoue-t-elle si le tableau contient des valeurs négatives ? Donnez un contre-exemple.

**Correction**

L'algorithme repose sur la **monotonie** : ajouter un élément fait croître la somme et en retirer un la fait décroître. Avec des valeurs négatives, ce n'est plus vrai : la fenêtre peut contenir un élément négatif qui « tire » la somme vers le bas, alors qu'il serait utile de le retirer pour atteindre `S`, mais l'algorithme ne rétrécit que lorsque la somme est déjà ≥ `S`.

Contre-exemple : `t = [-1, 4, 2]` et `S = 6`. Le sous-tableau `[4, 2]` a pour somme 6 (longueur 2), mais la fenêtre qui part du début a pour sommes `-1`, `3`, `5` : jamais ≥ 6, donc l'algorithme renvoie 0 alors que la bonne réponse est 2. Il faut utiliser des sommes préfixes avec une structure appropriée (par exemple une deque monotone).

## 13.5 Maximum de chaque fenêtre : file monotone *(ajout)*

**Exercice 13.5.1**

Écrivez `maximum_fenetres(t, k)` en O(n) avec une `deque` qui stocke des indices à valeurs décroissantes. Testez sur `[1, 3, -1, -3, 5, 3, 6, 7]` avec `k = 3`.

**Correction**

On garde dans la deque des **indices dont les valeurs sont décroissantes** ; la tête est toujours l'indice du maximum de la fenêtre.

```python
from collections import deque


def maximum_fenetres(t, k):
    d = deque()                 # indices, valeurs décroissantes
    resultat = []
    for i, x in enumerate(t):
        while d and t[d[-1]] <= x:      # les plus petits ne seront jamais maximum
            d.pop()
        d.append(i)
        if d[0] <= i - k:               # la tête sort de la fenêtre
            d.popleft()
        if i >= k - 1:
            resultat.append(t[d[0]])
    return resultat


print(maximum_fenetres([1, 3, -1, -3, 5, 3, 6, 7], 3))   # [3, 3, 5, 5, 6, 7]
```

**Exercice 13.5.2**

Expliquez pourquoi chaque élément est inséré et retiré au plus une fois. Adaptez l'algorithme pour calculer le **minimum** de chaque fenêtre.

**Correction**

Chaque indice est ajouté **une fois** à la queue de la deque et retiré **au plus une fois** (soit par la queue quand un plus grand arrive, soit par la tête quand il sort de la fenêtre). Le nombre total d'opérations est donc au plus `2n` : **O(n)**.

Pour le **minimum**, on inverse la comparaison : on garde des valeurs **croissantes** en retirant par la queue tant que `t[d[-1]] >= x`.

```python
def minimum_fenetres(t, k):
    d, resultat = deque(), []
    for i, x in enumerate(t):
        while d and t[d[-1]] >= x:
            d.pop()
        d.append(i)
        if d[0] <= i - k:
            d.popleft()
        if i >= k - 1:
            resultat.append(t[d[0]])
    return resultat


print(minimum_fenetres([1, 3, -1, -3, 5, 3, 6, 7], 3))   # [-1, -3, -3, -3, 3, 3]
```

## 13.6 Autres problèmes classiques

**Exercice 13.6.1**

Trouvez toutes les positions de départ des anagrammes d'un motif `p` dans un texte `s` (fenêtre de taille fixe et compteurs).

**Correction**

Fenêtre de taille `len(p)` ; on compare les compteurs de la fenêtre à ceux du motif.

```python
from collections import Counter


def positions_anagrammes(s, p):
    m = len(p)
    cible = Counter(p)
    fenetre = Counter(s[:m])
    resultat = [0] if fenetre == cible and len(s) >= m else []
    for i in range(m, len(s)):
        fenetre[s[i]] += 1                    # entre
        sortant = s[i - m]
        fenetre[sortant] -= 1                 # sort
        if fenetre[sortant] == 0:
            del fenetre[sortant]
        if fenetre == cible:
            resultat.append(i - m + 1)
    return resultat


print(positions_anagrammes("cbaebabacd", "abc"))   # [0, 6]
```

Complexité O(n × taille de l'alphabet), soit O(n) pour un alphabet fixe.

**Exercice 13.6.2**

Écrivez `plus_long_avec_k_distincts(t, k)` : la longueur du plus long sous-tableau contenant au plus `k` valeurs distinctes.

**Correction**

```python
def plus_long_avec_k_distincts(t, k):
    compteur = {}
    gauche = meilleur = 0
    for droite, x in enumerate(t):
        compteur[x] = compteur.get(x, 0) + 1
        while len(compteur) > k:              # trop de valeurs distinctes : on rétrécit
            y = t[gauche]
            compteur[y] -= 1
            if compteur[y] == 0:
                del compteur[y]
            gauche += 1
        meilleur = max(meilleur, droite - gauche + 1)
    return meilleur


print(plus_long_avec_k_distincts([1, 2, 1, 2, 3], 2))   # 4
print(plus_long_avec_k_distincts("eceba", 2))            # 3
```

Complexité O(n).

**Exercice 13.6.3**

Écrivez `fenetre_minimale(s, t)` : la plus petite sous-chaîne de `s` contenant tous les caractères de `t` (avec multiplicité). *(défi)*

**Correction**

On élargit à droite jusqu'à couvrir tous les caractères de `t` (avec multiplicité), puis on rétrécit à gauche tant que la fenêtre reste valide.

```python
from collections import Counter


def fenetre_minimale(s, t):
    if not t or len(t) > len(s):
        return ""
    besoin = Counter(t)
    manquants = len(t)                   # nombre de caractères encore à couvrir
    gauche = 0
    meilleur = (float("inf"), 0, 0)
    for droite, c in enumerate(s):
        if besoin[c] > 0:
            manquants -= 1
        besoin[c] -= 1
        if manquants == 0:               # fenêtre valide : on la rétrécit
            while besoin[s[gauche]] < 0:
                besoin[s[gauche]] += 1
                gauche += 1
            if droite - gauche + 1 < meilleur[0]:
                meilleur = (droite - gauche + 1, gauche, droite)
            besoin[s[gauche]] += 1       # on abandonne s[gauche] pour chercher une autre fenêtre
            manquants += 1
            gauche += 1
    return "" if meilleur[0] == float("inf") else s[meilleur[1]:meilleur[2] + 1]


print(fenetre_minimale("ADOBECODEBANC", "ABC"))   # BANC
```

Complexité O(|s| + |t|).

**Exercice 13.6.4**

Fruits dans des paniers : un tableau représente des arbres, chacun portant un type de fruit ; deux paniers acceptent chacun un seul type. Trouvez la plus longue suite d'arbres consécutifs cueillables.

**Correction**

Il s'agit de la plus longue sous-liste contenant **au plus 2 valeurs distinctes** : c'est exactement l'exercice précédent avec `k = 2`.

```python
def fruits(arbres):
    return plus_long_avec_k_distincts(arbres, 2)


print(fruits([1, 2, 1]))          # 3
print(fruits([0, 1, 2, 2]))       # 3
print(fruits([1, 2, 3, 2, 2]))    # 4
```

**Exercice 13.6.5**

Plus longue sous-chaîne avec remplacement : on peut remplacer au plus `k` caractères ; quelle est la plus longue sous-chaîne composée d'un même caractère ?

**Correction**

La fenêtre `[gauche, droite]` est valide si `(taille de la fenêtre) − (fréquence du caractère le plus fréquent) ≤ k` : les autres caractères sont remplacés. On élargit toujours, on rétrécit quand la fenêtre n'est plus valide.

```python
def remplacement_caracteres(s, k):
    compteur = {}
    gauche = frequence_max = meilleur = 0
    for droite, c in enumerate(s):
        compteur[c] = compteur.get(c, 0) + 1
        frequence_max = max(frequence_max, compteur[c])
        if (droite - gauche + 1) - frequence_max > k:
            compteur[s[gauche]] -= 1
            gauche += 1
        meilleur = max(meilleur, droite - gauche + 1)
    return meilleur


print(remplacement_caracteres("AABABBA", 1))   # 4
print(remplacement_caracteres("ABAB", 2))       # 4
```

On n'a pas besoin de diminuer `frequence_max` quand la fenêtre rétrécit : la taille de la fenêtre ne peut augmenter que si une fréquence plus grande est atteinte. Complexité O(n).

---

# 14. Sommes préfixes et tableaux de différences

## 14.1 Sommes préfixes

**Exercice 14.1.1**

Écrivez `prefixes(t)` qui renvoie le tableau `P` de longueur `n + 1` avec `P[0] = 0`, puis `somme_intervalle(P, l, r)` en O(1) pour la somme de `t[l..r]` (bornes incluses).

**Correction**

`P[0] = 0` et `P[i + 1] = P[i] + t[i]` : `P[i]` est la somme des `i` premiers éléments. La somme de `t[l..r]` vaut `P[r + 1] − P[l]`.

```python
def prefixes(t):
    P = [0] * (len(t) + 1)
    for i, x in enumerate(t):
        P[i + 1] = P[i] + x
    return P


def somme_intervalle(P, l, r):
    return P[r + 1] - P[l]


t = [3, 1, 4, 1, 5, 9, 2, 6]
P = prefixes(t)
print(somme_intervalle(P, 2, 5))   # 19
```

Précalcul en O(n), puis chaque requête en O(1).

**Exercice 14.1.2**

Pour `t = [3, 1, 4, 1, 5, 9, 2, 6]`, calculez à la main `P` puis les sommes des intervalles `[0, 3]`, `[2, 5]` et `[4, 7]`.

**Correction**

Pour `t = [3, 1, 4, 1, 5, 9, 2, 6]` :

`P = [0, 3, 4, 8, 9, 14, 23, 25, 31]`

| Intervalle | Calcul | Résultat | Vérification |
| --- | --- | --- | --- |
| `[0, 3]` | `P[4] − P[0] = 9 − 0` | **9** | 3 + 1 + 4 + 1 |
| `[2, 5]` | `P[6] − P[2] = 23 − 4` | **19** | 4 + 1 + 5 + 9 |
| `[4, 7]` | `P[8] − P[4] = 31 − 9` | **22** | 5 + 9 + 2 + 6 |

**Exercice 14.1.3**

On répond à `q = 10⁵` requêtes sur un tableau de taille `10⁵`. Comparez le coût total avec et sans sommes préfixes.

**Correction**

- **Sans sommes préfixes** : chaque requête parcourt jusqu'à `n` éléments, soit `q × n = 10⁵ × 10⁵ = 10¹⁰` opérations, de l'ordre de 17 minutes en Python.
- **Avec sommes préfixes** : un précalcul en O(n) puis `q` requêtes en O(1), soit environ `n + q = 2 × 10⁵` opérations, de l'ordre de la dizaine de millisecondes.

Le gain est de l'ordre de 50 000.

**Exercice 14.1.4**

Calculez l'indice d'équilibre d'un tableau : un indice `i` tel que la somme des éléments à gauche est égale à celle des éléments à droite.

**Correction**

À l'indice `i`, la somme à gauche est `gauche` et la somme à droite vaut `total − gauche − t[i]`.

```python
def indice_equilibre(t):
    total = sum(t)
    gauche = 0
    for i, x in enumerate(t):
        if gauche == total - gauche - x:
            return i
        gauche += x
    return -1


print(indice_equilibre([1, 7, 3, 6, 5, 6]))   # 3 (1 + 7 + 3 = 5 + 6 = 11)
print(indice_equilibre([1, 2, 3]))            # -1
```

Complexité O(n), espace O(1) (on n'a pas besoin du tableau complet des préfixes).

**Exercice 14.1.5**

Écrivez `produit_sauf_soi(t)` : pour chaque indice, le produit de tous les autres éléments, sans division, en O(n) (préfixes et suffixes de produits).

**Correction**

`resultat[i]` = (produit des éléments à gauche de `i`) × (produit des éléments à droite de `i`).

```python
def produit_sauf_soi(t):
    n = len(t)
    resultat = [1] * n
    p = 1
    for i in range(n):                 # préfixes de produits
        resultat[i] = p
        p *= t[i]
    p = 1
    for i in range(n - 1, -1, -1):     # suffixes de produits
        resultat[i] *= p
        p *= t[i]
    return resultat


print(produit_sauf_soi([1, 2, 3, 4]))   # [24, 12, 8, 6]
print(produit_sauf_soi([1, 0, 3]))      # [0, 3, 0]
```

Fonctionne avec des zéros (contrairement à la division). Temps O(n), espace supplémentaire O(1) hors résultat.

### Sous-tableaux de somme `k` (avec valeurs négatives possibles)

**Exercice 14.1.6**

Écrivez `nombre_sous_tableaux_somme(t, k)` avec un dictionnaire de fréquences de préfixes. Testez sur `[1, 2, 3, -2, 5]` avec `k = 3`.

**Correction**

Un sous-tableau `t[i..j]` a pour somme `k` si `P[j + 1] − P[i] = k`, soit `P[i] = P[j + 1] − k`. On parcourt les préfixes en comptant combien de fois chaque valeur de préfixe est apparue.

```python
def nombre_sous_tableaux_somme(t, k):
    frequences = {0: 1}            # le préfixe vide
    somme = compte = 0
    for x in t:
        somme += x
        compte += frequences.get(somme - k, 0)
        frequences[somme] = frequences.get(somme, 0) + 1
    return compte


print(nombre_sous_tableaux_somme([1, 2, 3, -2, 5], 3))   # 4
```

Les 4 sous-tableaux sont `[1, 2]`, `[3]`, `[2, 3, -2]` et `[-2, 5]`. Complexité O(n) en moyenne.

**Exercice 14.1.7**

Écrivez `plus_long_sous_tableau_somme_nulle(t)` en O(n).

**Correction**

On mémorise la **première** position de chaque valeur de préfixe ; si la même valeur réapparaît, la somme entre les deux positions est nulle.

```python
def plus_long_sous_tableau_somme_nulle(t):
    premiere = {0: -1}
    somme = meilleur = 0
    for i, x in enumerate(t):
        somme += x
        if somme in premiere:
            meilleur = max(meilleur, i - premiere[somme])
        else:
            premiere[somme] = i
    return meilleur


print(plus_long_sous_tableau_somme_nulle([15, -2, 2, -8, 1, 7, 10, 23]))   # 5 ([-2, 2, -8, 1, 7])
```

Complexité O(n).

**Exercice 14.1.8**

Comptez le nombre de sous-tableaux dont la somme est divisible par `k`. *(défi)*

**Correction**

Deux préfixes `P[i]` et `P[j]` donnent un sous-tableau de somme divisible par `k` si et seulement si `P[i] ≡ P[j] (mod k)`. Il suffit de compter les paires de préfixes de même reste.

```python
def sous_tableaux_divisibles(t, k):
    frequences = {0: 1}
    somme = compte = 0
    for x in t:
        somme = (somme + x) % k             # en Python, le reste est toujours positif
        compte += frequences.get(somme, 0)
        frequences[somme] = frequences.get(somme, 0) + 1
    return compte


print(sous_tableaux_divisibles([4, 5, 0, -2, -3, 1], 5))   # 7
```

Complexité O(n).

### Version 2D

**Exercice 14.1.9**

Écrivez `prefixes_2d(grille)` et `somme_rectangle(P, r1, c1, r2, c2)` en O(1). Écrivez la formule d'inclusion-exclusion utilisée.

**Correction**

Formule d'inclusion-exclusion pour le tableau `P` de taille `(n + 1) × (m + 1)` :

- construction : `P[i + 1][j + 1] = g[i][j] + P[i][j + 1] + P[i + 1][j] − P[i][j]` ;
- requête : `somme(r1, c1, r2, c2) = P[r2 + 1][c2 + 1] − P[r1][c2 + 1] − P[r2 + 1][c1] + P[r1][c1]`.

```python
def prefixes_2d(grille):
    n, m = len(grille), len(grille[0])
    P = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            P[i + 1][j + 1] = grille[i][j] + P[i][j + 1] + P[i + 1][j] - P[i][j]
    return P


def somme_rectangle(P, r1, c1, r2, c2):
    return P[r2 + 1][c2 + 1] - P[r1][c2 + 1] - P[r2 + 1][c1] + P[r1][c1]


g = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
P = prefixes_2d(g)
print(somme_rectangle(P, 1, 1, 2, 2))   # 28 (5 + 6 + 8 + 9)
```

On ajoute le grand rectangle, on retire les deux bandes (haut et gauche), et on rajoute le coin retiré deux fois.

**Exercice 14.1.10**

Trouvez le carré de côté `k` de somme maximale dans une grille.

**Correction**

Pour chaque coin supérieur gauche `(i, j)`, la somme du carré `k × k` s'obtient en O(1) avec `somme_rectangle`.

```python
def carre_max(grille, k):
    P = prefixes_2d(grille)
    n, m = len(grille), len(grille[0])
    meilleur = float("-inf")
    for i in range(n - k + 1):
        for j in range(m - k + 1):
            meilleur = max(meilleur, somme_rectangle(P, i, j, i + k - 1, j + k - 1))
    return meilleur


print(carre_max([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2))   # 28
```

Complexité O(n·m) après le précalcul O(n·m), contre O(n·m·k²) en recalculant chaque carré.

## 14.2 Tableau de différences

**Exercice 14.2.1**

Écrivez `appliquer_mises_a_jour(n, mises_a_jour)` où chaque mise à jour `(l, r, v)` ajoute `v` à `t[l..r]`, en O(n + q). Testez avec `n = 5` et les mises à jour `(1, 3, 2)`, `(2, 4, 3)`, `(0, 1, -1)`.

**Correction**

Pour une mise à jour `(l, r, v)` : `d[l] += v` et `d[r + 1] -= v`. Le tableau final s'obtient par sommes préfixes de `d`.

```python
def appliquer_mises_a_jour(n, mises_a_jour):
    d = [0] * (n + 1)
    for l, r, v in mises_a_jour:
        d[l] += v
        d[r + 1] -= v
    t, courant = [], 0
    for i in range(n):
        courant += d[i]
        t.append(courant)
    return t


print(appliquer_mises_a_jour(5, [(1, 3, 2), (2, 4, 3), (0, 1, -1)]))
# [-1, 1, 5, 5, 3]
```

Détail : `d = [-1, 2, 4, 0, -2, -3]`, dont les sommes préfixes valent `-1, 1, 5, 5, 3`. Complexité O(n + q), au lieu de O(n·q).

**Exercice 14.2.2**

Expliquez le lien entre le tableau de différences et les sommes préfixes (opération réciproque).

**Correction**

Le tableau de différences `D[i] = t[i] − t[i − 1]` (avec `D[0] = t[0]`) est la « dérivée discrète » de `t`, et les sommes préfixes en sont l'« intégrale » : `t[i] = D[0] + ... + D[i]`. Les deux opérations sont **réciproques** : calculer les sommes préfixes du tableau de différences redonne `t`, et calculer les différences successives des sommes préfixes redonne `t` aussi. C'est pourquoi une addition sur un intervalle devient deux modifications ponctuelles de `D`.

**Exercice 14.2.3**

Covoiturage : une voiture de capacité `C` effectue des trajets `(passagers, départ, arrivée)`. Déterminez si tous les trajets peuvent être effectués.

**Correction**

Les passagers sont à bord sur `[départ, arrivée)` : on ajoute `passagers` en `départ` et on les retire en `arrivée`. La capacité est respectée si les sommes préfixes ne dépassent jamais `C`.

```python
def covoiturage(trajets, capacite):
    maxi = max(arrivee for _, _, arrivee in trajets)
    d = [0] * (maxi + 2)
    for passagers, depart, arrivee in trajets:
        d[depart] += passagers
        d[arrivee] -= passagers
    charge = 0
    for x in d:
        charge += x
        if charge > capacite:
            return False
    return True


print(covoiturage([(2, 1, 5), (3, 3, 7)], 4))   # False (5 passagers entre 3 et 5)
print(covoiturage([(2, 1, 5), (3, 3, 7)], 5))   # True
```

Complexité O(n + longueur de la route).

**Exercice 14.2.4**

Écrivez la version 2D du tableau de différences pour ajouter une valeur à un rectangle, et appliquez-la à une liste de rectangles.

**Correction**

Pour ajouter `v` au rectangle `(r1, c1)` à `(r2, c2)` : quatre modifications ponctuelles, puis on calcule les sommes préfixes 2D.

```python
def appliquer_rectangles(n, m, rectangles):
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for r1, c1, r2, c2, v in rectangles:
        D[r1][c1] += v
        D[r1][c2 + 1] -= v
        D[r2 + 1][c1] -= v
        D[r2 + 1][c2 + 1] += v
    t = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            haut = t[i - 1][j] if i > 0 else 0
            gauche = t[i][j - 1] if j > 0 else 0
            diag = t[i - 1][j - 1] if i > 0 and j > 0 else 0
            t[i][j] = D[i][j] + haut + gauche - diag
    return t


for ligne in appliquer_rectangles(3, 4, [(0, 0, 1, 1, 5), (1, 1, 2, 3, 2)]):
    print(ligne)
# [5, 5, 0, 0]
# [5, 7, 2, 2]
# [0, 2, 2, 2]
```

Complexité O(n·m + q).

## 14.3 Applications

**Exercice 14.3.1**

Pour une chaîne de `10⁵` lettres, répondez à `10⁵` requêtes « combien de fois la lettre `c` apparaît-elle dans `[l, r]` ? » à l'aide de 26 tableaux de préfixes.

**Correction**

On construit 26 tableaux de préfixes, un par lettre : `P[c][i]` = nombre d'occurrences de la lettre `c` dans `s[:i]`.

```python
def preparer(s):
    n = len(s)
    P = [[0] * (n + 1) for _ in range(26)]
    for i, ch in enumerate(s):
        for c in range(26):
            P[c][i + 1] = P[c][i]
        P[ord(ch) - ord("a")][i + 1] += 1
    return P


def occurrences(P, lettre, l, r):
    c = ord(lettre) - ord("a")
    return P[c][r + 1] - P[c][l]


P = preparer("abracadabra")
print(occurrences(P, "a", 0, 10))   # 5
print(occurrences(P, "b", 2, 9))    # 1
```

Précalcul O(26·n) (environ 2,6 × 10⁶ opérations pour `n = 10⁵`), mémoire O(26·n), chaque requête en O(1) : les 10⁵ requêtes coûtent 10⁵ opérations au lieu de 10¹⁰.

**Exercice 14.3.2**

Pour chaque application, indiquez la technique la plus adaptée (préfixes, différences, ou préfixes + dictionnaire) : moyenne d'un intervalle, réservations qui se chevauchent, sous-tableau de somme `k`, dessin de rectangles sur une grille, nombre d'occurrences d'une lettre dans un intervalle.

**Correction**

| Application | Technique |
| --- | --- |
| Moyenne d'un intervalle | **préfixes** (somme divisée par la longueur) |
| Réservations qui se chevauchent | **différences** (on ajoute 1 au début, on retire 1 à la fin, le maximum des préfixes donne le chevauchement) |
| Sous-tableau de somme `k` | **préfixes + dictionnaire** |
| Dessin de rectangles sur une grille | **différences 2D** |
| Occurrences d'une lettre dans un intervalle | **préfixes** (un tableau par lettre) |

**Exercice 14.3.3**

Si le tableau est modifié entre les requêtes, les sommes préfixes ne suffisent plus. Quelle structure du chapitre 23 utiliser ? Quel est le coût d'une mise à jour avec les sommes préfixes ?

**Correction**

Si le tableau est modifié, les sommes préfixes ne suffisent plus : modifier `t[i]` oblige à recalculer tous les préfixes d'indice supérieur, soit **O(n)** par mise à jour. On utilise un **arbre de Fenwick** ou un **arbre de segments** (chapitre 23), qui supportent la mise à jour d'un point et la somme d'un intervalle en **O(log n)** chacun.

---

# 15. Recherche binaire sur la réponse

## 15.1 Principe

**Exercice 15.1.1**

Qu'est-ce qu'une fonction de décision monotone ? Donnez un exemple de problème dont la fonction de décision est monotone et un exemple où elle ne l'est pas.

**Correction**

Une fonction de décision `valide(x)` est **monotone** si elle est fausse pour toutes les valeurs jusqu'à un seuil, puis vraie à partir de ce seuil (ou l'inverse) : dès qu'elle devient vraie, elle le reste.

- **Exemple monotone** : « le bateau de capacité `c` peut-il livrer tous les colis en `D` jours ? » : si `c` convient, toute capacité supérieure convient aussi.
- **Exemple non monotone** : « `x` est-il un nombre premier ? » (ou « `x` est-il un carré parfait ? ») : la réponse alterne entre vrai et faux, on ne peut pas éliminer une moitié de l'intervalle.

## 15.2 Modèle : plus petite valeur valide

**Exercice 15.2.1**

Écrivez le modèle générique `plus_petite_valeur(bas, haut, est_valide)` qui renvoie la plus petite valeur `x` de `[bas, haut]` telle que `est_valide(x)` est vrai, en supposant que `est_valide` est faux puis vrai.

**Correction**

Invariant : la réponse est dans `[bas, haut]` et `est_valide(haut)` est vrai.

```python
def plus_petite_valeur(bas, haut, est_valide):
    while bas < haut:
        milieu = (bas + haut) // 2
        if est_valide(milieu):
            haut = milieu           # milieu convient : la réponse est ≤ milieu
        else:
            bas = milieu + 1        # milieu ne convient pas : la réponse est > milieu
    return bas


print(plus_petite_valeur(0, 100, lambda x: x * x >= 50))   # 8
```

Complexité : O(log(haut − bas)) appels à `est_valide`.

**Exercice 15.2.2**

Utilisez-le pour calculer la racine carrée entière `⌊√n⌋` sans fonction mathématique.

**Correction**

`⌊√n⌋` est la plus grande valeur `x` telle que `x² ≤ n`, c'est-à-dire (la plus petite valeur telle que `x² > n`) moins 1.

```python
def racine_entiere(n):
    return plus_petite_valeur(0, n + 1, lambda x: x * x > n) - 1


print(racine_entiere(0), racine_entiere(15), racine_entiere(16), racine_entiere(10**12))
# 0 3 4 1000000
```

Complexité O(log n).

**Exercice 15.2.3**

« Première mauvaise version » : les versions `1..n` sont bonnes jusqu'à une version à partir de laquelle toutes sont mauvaises. Trouvez la première mauvaise version avec le moins d'appels possible à `est_mauvaise(v)`.

**Correction**

La fonction de décision `est_mauvaise(v)` est monotone (faux puis vrai). On cherche la plus petite version mauvaise dans `[1, n]` :

```python
def premiere_mauvaise_version(n, est_mauvaise):
    return plus_petite_valeur(1, n, est_mauvaise)
```

Le nombre d'appels à `est_mauvaise` est au plus `⌈log₂ n⌉` (par exemple 20 appels pour `n = 10⁶`), contre `n` en parcours linéaire.

## 15.3 Exemple : expédier des colis en D jours

**Exercice 15.3.1**

Des colis de poids `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` doivent être expédiés dans l'ordre en 5 jours. Quelle est la capacité minimale du bateau ? Écrivez la fonction de décision, puis la recherche binaire.

**Correction**

La capacité minimale est **15**.

```python
def jours_necessaires(poids, capacite):
    jours, charge = 1, 0
    for p in poids:
        if charge + p > capacite:        # on ouvre un nouveau jour
            jours += 1
            charge = 0
        charge += p
    return jours


def capacite_minimale(poids, D):
    return plus_petite_valeur(max(poids), sum(poids),
                              lambda c: jours_necessaires(poids, c) <= D)


print(capacite_minimale([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))   # 15
```

Avec la capacité 15 : jours `[1,2,3,4,5]` (15), `[6,7]` (13), `[8]`, `[9]`, `[10]`, soit exactement 5 jours. Avec 14, il faudrait 6 jours.

**Exercice 15.3.2**

Quelles bornes choisir pour `bas` et `haut` ? Justifiez chacune.

**Correction**

- `bas = max(poids)` : le bateau doit au moins pouvoir porter le colis le plus lourd, sinon aucun jour ne peut l'accueillir.
- `haut = sum(poids)` : une capacité égale au poids total permet de tout expédier en **1 jour**, donc en au plus `D` jours (`D ≥ 1`) : `haut` est toujours valide, ce qui garantit l'invariant.

**Exercice 15.3.3**

Quelle est la complexité en fonction de `n` (nombre de colis) et de la somme des poids `S` ?

**Correction**

Il y a `O(log S)` itérations de recherche binaire (l'intervalle `[max(poids), S]` a une longueur au plus `S`), et chaque test de la fonction de décision parcourt les `n` colis en O(n). Complexité totale : **O(n log S)**.

## 15.4 Exemple : vitesse minimale pour manger toutes les bananes

**Exercice 15.4.1**

Des piles de bananes `[3, 6, 7, 11]` doivent être mangées en `H = 8` heures, à raison d'une pile par heure au plus (on mange `k` bananes par heure dans une seule pile). Quelle est la vitesse minimale `k` ? Écrivez la solution.

**Correction**

La vitesse minimale est **4** bananes par heure.

```python
def vitesse_minimale(piles, H):
    def valide(k):
        return sum((p + k - 1) // k for p in piles) <= H      # heures nécessaires

    return plus_petite_valeur(1, max(piles), valide)


print(vitesse_minimale([3, 6, 7, 11], 8))   # 4
```

Vérification : à `k = 4`, les piles demandent `1 + 2 + 2 + 3 = 8` heures ; à `k = 3`, elles demandent `1 + 2 + 3 + 4 = 10 > 8`. Complexité O(n log(max piles)).

**Exercice 15.4.2**

Diviser un tableau en `m` sous-tableaux contigus de façon à minimiser la plus grande somme parmi les sous-tableaux : écrivez la solution par recherche binaire sur la réponse.

**Correction**

On cherche la plus petite valeur `s` telle qu'on puisse découper le tableau en au plus `m` sous-tableaux contigus de somme ≤ `s`. La fonction de décision est monotone en `s`.

```python
def partition_min_max(t, m):
    def valide(s):
        morceaux, courant = 1, 0
        for x in t:
            if courant + x > s:
                morceaux += 1
                courant = 0
            courant += x
        return morceaux <= m

    return plus_petite_valeur(max(t), sum(t), valide)


print(partition_min_max([7, 2, 5, 10, 8], 2))   # 18 ([7, 2, 5] et [10, 8])
```

Complexité O(n log(somme)).

## 15.5 Schémas fréquents

**Exercice 15.5.1**

Pour chaque problème, dites s'il faut chercher à gauche ou à droite quand la valeur testée est valide :

1. minimiser la capacité maximale d'un camion ;
2. maximiser la distance minimale entre des vaches placées dans des stalles ;
3. la plus petite durée pour terminer des tâches ;
4. la plus grande longueur de ruban coupée en `k` morceaux égaux.

**Correction**

1. **Minimiser la capacité maximale d'un camion** : on cherche la plus petite valeur valide ; quand la valeur testée est valide, on cherche **à gauche** (valeurs plus petites : `haut = milieu`).
2. **Maximiser la distance minimale entre des vaches** : on cherche la plus grande valeur valide ; quand la valeur testée est valide, on cherche **à droite** (`bas = milieu`, avec un milieu arrondi vers le haut).
3. **Plus petite durée pour terminer des tâches** : plus petite valeur valide, donc **à gauche**.
4. **Plus grande longueur de ruban coupée en `k` morceaux égaux** : plus grande valeur valide, donc **à droite**.

**Exercice 15.5.2**

Placer `c` vaches dans des stalles aux positions `[1, 2, 8, 4, 9]` de manière à maximiser la plus petite distance entre deux vaches (`c = 3`). Écrivez la solution.

**Correction**

On cherche la plus grande distance `d` telle que l'on puisse placer 3 vaches avec un écart ≥ `d`. Test glouton : placer la première vache à la position minimale, puis chaque suivante à la première stalle située à au moins `d` de la précédente.

```python
def distance_maximale(positions, c):
    positions = sorted(positions)

    def valide(d):
        compte, derniere = 1, positions[0]
        for p in positions[1:]:
            if p - derniere >= d:
                compte += 1
                derniere = p
        return compte >= c

    bas, haut = 1, positions[-1] - positions[0]
    while bas < haut:
        milieu = (bas + haut + 1) // 2         # milieu arrondi vers le haut
        if valide(milieu):
            bas = milieu
        else:
            haut = milieu - 1
    return bas


print(distance_maximale([1, 2, 8, 4, 9], 3))   # 3
```

Avec `d = 3`, on place les vaches en 1, 4 et 8. Avec `d = 4`, on ne peut en placer que 2 (en 1 et 8, puis aucune stalle à 12 ou plus).

**Exercice 15.5.3**

Des ouvriers doivent peindre `n` planches de longueurs données, chaque ouvrier peignant une suite contiguë ; minimisez le temps total pour `k` ouvriers.

**Correction**

C'est le même problème que le découpage en `k` sous-tableaux contigus de somme maximale minimale (exercice 15.4.2) : le temps total est la charge du peintre le plus chargé (si peindre une unité de longueur prend un temps unitaire).

```python
def temps_peinture(planches, k):
    return partition_min_max(planches, k)


print(temps_peinture([10, 20, 30, 40], 2))   # 60 ([10, 20, 30] et [40])
print(temps_peinture([10, 20, 30, 40], 3))   # 40
```

Complexité O(n log(somme)).

## 15.6 Réels : recherche binaire flottante

**Exercice 15.6.1**

Calculez `∛x` par recherche binaire flottante avec un nombre fixe d'itérations. Combien d'itérations faut-il pour une précision de `10⁻⁹` sur `[0, 1000]` ?

**Correction**

```python
def racine_cubique(x, iterations=100):
    bas, haut = 0.0, max(1.0, x)
    for _ in range(iterations):
        milieu = (bas + haut) / 2
        if milieu ** 3 < x:
            bas = milieu
        else:
            haut = milieu
    return (bas + haut) / 2


print(racine_cubique(27))     # 3.0 (à l'arrondi flottant près)
print(racine_cubique(1000))   # 10.0
```

Chaque itération divise la longueur de l'intervalle par 2. Pour passer de 1000 à moins de `10⁻⁹` il faut `2ᵏ ≥ 10¹²`, soit **`k = 40` itérations** (`2⁴⁰ ≈ 1,1 × 10¹²`).

**Exercice 15.6.2**

Pourquoi préfère-t-on un nombre fixe d'itérations à une condition `haut - bas > eps` ? Donnez un cas où la seconde peut boucler indéfiniment.

**Correction**

Avec une condition `haut - bas > eps`, la boucle peut ne **jamais se terminer** : les flottants ont une précision limitée. Quand `bas` et `haut` sont grands, l'écart minimal entre deux flottants consécutifs (l'ulp) peut dépasser `eps`. Par exemple, avec `bas` autour de `10⁹` l'ulp vaut environ `10⁻⁷`, donc avec `eps = 10⁻⁹` le milieu `(bas + haut) / 2` finit par être égal à `bas` ou à `haut` et l'intervalle ne rétrécit plus : boucle infinie.

Un **nombre fixe d'itérations** (par exemple 100) garantit la terminaison et une précision maximale pour le type flottant, indépendamment de l'ordre de grandeur des valeurs.

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

**Correction**

Les trois erreurs :

1. **Borne basse** : `bas` doit valoir `max(poids)` et non 0 (une capacité inférieure au colis le plus lourd est impossible, et la fonction de décision n'a pas de sens pour 0).
2. **Cas valide** : quand `milieu` est valide, on cherche une capacité plus petite, donc `haut = milieu` (et non `bas = milieu`, qui ferait chercher plus grand et peut boucler indéfiniment).
3. **Cas invalide** : quand `milieu` est invalide, la réponse est strictement supérieure, donc `bas = milieu + 1` (et non `haut = milieu - 1`).

On corrige aussi l'appel manquant des paramètres de `est_valide`.

```python
def plus_petite_capacite(poids, jours):
    bas, haut = max(poids), sum(poids)
    while bas < haut:
        milieu = (bas + haut) // 2
        if jours_necessaires(poids, milieu) <= jours:    # est_valide(milieu)
            haut = milieu
        else:
            bas = milieu + 1
    return bas
```

**Exercice 15.7.2**

Listez les quatre vérifications à faire avant d'appliquer une recherche binaire sur la réponse.

**Correction**

Quatre vérifications avant d'appliquer la recherche binaire sur la réponse :

1. **Monotonie** : la fonction de décision est bien monotone (faux puis vrai, ou l'inverse) sur tout l'intervalle.
2. **Bornes** : `bas` et `haut` encadrent la réponse, et `haut` (ou `bas` selon le cas) est une valeur valide, de façon à respecter l'invariant.
3. **Fonction de décision** : elle est correcte et rapide (typiquement en O(n) avec un parcours glouton), car elle est appelée `O(log(étendue))` fois.
4. **Mise à jour sans erreur d'un** : le choix du milieu (arrondi bas ou haut) est cohérent avec les mises à jour (`haut = milieu` / `bas = milieu + 1` pour minimiser ; `bas = milieu` avec milieu arrondi haut pour maximiser), afin que la boucle se termine et renvoie la bonne borne (et le bon type : entier ou flottant).

---

# 16. Algorithmes de théorie des nombres

## 16.1 Crible d'Ératosthène

**Exercice 16.1.1**

Déroulez à la main le crible d'Ératosthène pour `N = 50`. Quels nombres sont barrés à chaque étape ?

**Correction**

Crible d'Ératosthène pour `N = 50` : on part des nombres de 2 à 50 et, pour chaque nombre `p` non barré avec `p² ≤ 50` (donc `p ≤ 7`), on barre ses multiples à partir de `p²`.

| `p` | Multiples barrés (à partir de `p²`) |
| --- | --- |
| 2 | 4, 6, 8, 10, 12, ..., 50 (tous les nombres pairs sauf 2) |
| 3 | 9, 15, 21, 27, 33, 39, 45 (les autres multiples de 3 sont déjà barrés) |
| 5 | 25, 35 (30, 40, 45, 50 sont déjà barrés) |
| 7 | 49 |

Comme `11² = 121 > 50`, on s'arrête. Les nombres non barrés sont les **15 nombres premiers** `2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47`.

**Exercice 16.1.2**

Implémentez `crible(N)` qui renvoie la liste des nombres premiers `≤ N`. Quelle est la complexité en temps et en espace ?

**Correction**

```python
from math import isqrt


def crible(N):
    if N < 2:
        return []
    est_premier = bytearray([1]) * (N + 1)
    est_premier[0] = est_premier[1] = 0
    for p in range(2, isqrt(N) + 1):
        if est_premier[p]:
            est_premier[p * p::p] = bytearray(len(range(p * p, N + 1, p)))
    return [i for i in range(N + 1) if est_premier[i]]


print(crible(50))
print(len(crible(10**6)))   # 78498
```

Complexité en temps : **O(N log log N)** (la somme `N/2 + N/3 + N/5 + ...` sur les nombres premiers vaut `N log log N`). Complexité en espace : **O(N)**.

**Exercice 16.1.3**

Pourquoi peut-on commencer le marquage des multiples de `p` à `p²` ?

**Correction**

Un multiple de `p` de la forme `k × p` avec `k < p` possède un facteur premier plus petit que `p` (un diviseur de `k`) : il a donc déjà été barré lors du passage de ce plus petit facteur premier. Le premier multiple de `p` qui n'a pas encore été barré est donc `p × p = p²`. Commencer à `p²` évite des opérations inutiles.

**Exercice 16.1.4**

Combien de nombres premiers y a-t-il en dessous de 10⁶ ? Vérifiez avec votre crible et comparez avec l'approximation `N / ln N`.

**Correction**

```python
import math

premiers = crible(10**6)
print(len(premiers))                      # 78498
print(10**6 / math.log(10**6))            # environ 72382
```

Il y a **78 498** nombres premiers inférieurs à 10⁶. L'approximation `N / ln N` donne environ 72 382, soit une sous-estimation d'environ 8 % ; une meilleure approximation est l'intégrale logarithmique `Li(N)`, qui donne environ 78 627.

**Exercice 16.1.5** *(défi)*

Implémentez un crible segmenté qui liste les nombres premiers dans l'intervalle `[L, R]` pour `R` jusqu'à 10¹² et `R − L ≤ 10⁶`.

**Correction**

On calcule d'abord les nombres premiers jusqu'à `√R` (au plus `10⁶` pour `R ≤ 10¹²`) avec le crible simple, puis on barre leurs multiples dans le segment `[L, R]`.

```python
from math import isqrt


def crible_segmente(L, R):
    petits = crible(isqrt(R))
    segment = bytearray([1]) * (R - L + 1)
    for p in petits:
        debut = max(p * p, ((L + p - 1) // p) * p)     # premier multiple de p >= L
        if debut > R:
            continue
        segment[debut - L::p] = bytearray(len(range(debut - L, R - L + 1, p)))
    return [L + i for i, v in enumerate(segment) if v and L + i >= 2]


print(crible_segmente(90, 130))              # [97, 101, 103, 107, 109, 113, 127]
print(crible_segmente(10**12, 10**12 + 100))
# [1000000000039, 1000000000061, 1000000000063, 1000000000091]
```

Mémoire : O(√R + (R − L)), temps : O((R − L) log log R + √R log log √R). On ne stocke jamais les `10¹²` entiers.

## 16.2 Factorisation

**Exercice 16.2.1**

Écrivez `factoriser(n)` par divisions successives. Factorisez `360`, `97`, `1001`.

**Correction**

```python
def factoriser(n):
    facteurs = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            facteurs[d] = facteurs.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        facteurs[n] = facteurs.get(n, 0) + 1     # reste : un facteur premier
    return facteurs


print(factoriser(360))    # {2: 3, 3: 2, 5: 1}   soit 2³ × 3² × 5
print(factoriser(97))     # {97: 1}              97 est premier
print(factoriser(1001))   # {7: 1, 11: 1, 13: 1} soit 7 × 11 × 13
```

Complexité O(√n).

**Exercice 16.2.2**

Construisez un tableau `plus_petit_facteur` par crible, puis factorisez en O(log n) un nombre inférieur à `N`.

**Correction**

On construit, par un crible, le **plus petit facteur premier** de chaque entier jusqu'à `N`, puis on factorise en suivant les plus petits facteurs.

```python
def plus_petit_facteur(N):
    spf = list(range(N + 1))
    for p in range(2, isqrt(N) + 1):
        if spf[p] == p:                         # p est premier
            for m in range(p * p, N + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf


def factoriser_rapide(n, spf):
    facteurs = {}
    while n > 1:
        p = spf[n]
        facteurs[p] = facteurs.get(p, 0) + 1
        n //= p
    return facteurs


spf = plus_petit_facteur(10**6)
print(factoriser_rapide(360, spf))    # {2: 3, 3: 2, 5: 1}
```

Précalcul O(N log log N), puis chaque factorisation en **O(log n)** (au plus `log₂ n` facteurs).

**Exercice 16.2.3**

Écrivez `nombre_de_diviseurs(n)` et `somme_des_diviseurs(n)` à partir de la décomposition en facteurs premiers. Calculez-les pour `360`.

**Correction**

Si `n = p₁^e₁ × ... × p_k^e_k` : le nombre de diviseurs est `(e₁ + 1) × ... × (e_k + 1)` et leur somme est `∏ (p^(e+1) − 1) / (p − 1)`.

```python
def nombre_de_diviseurs(n):
    resultat = 1
    for e in factoriser(n).values():
        resultat *= e + 1
    return resultat


def somme_des_diviseurs(n):
    resultat = 1
    for p, e in factoriser(n).items():
        resultat *= (p ** (e + 1) - 1) // (p - 1)
    return resultat


print(nombre_de_diviseurs(360))   # 24
print(somme_des_diviseurs(360))   # 1170
```

Pour `360 = 2³ × 3² × 5` : `4 × 3 × 2 = 24` diviseurs, et une somme égale à `15 × 13 × 6 = 1170`.

**Exercice 16.2.4**

Combien de diviseurs possède `10!` ? Quel est le plus petit entier ayant exactement 12 diviseurs ?

**Correction**

- `10! = 3 628 800 = 2⁸ × 3⁴ × 5² × 7` (exposant de 2 : `5 + 2 + 1 = 8`, de 3 : `3 + 1 = 4`, de 5 : 2, de 7 : 1). Nombre de diviseurs : `9 × 5 × 3 × 2 = ` **270**.
- Plus petit entier ayant exactement 12 diviseurs : les décompositions possibles de 12 en produit de `(e + 1)` sont `12`, `6 × 2`, `4 × 3`, `3 × 2 × 2`. On associe les plus grands exposants aux plus petits premiers : `2¹¹ = 2048`, `2⁵ × 3 = 96`, `2³ × 3² = 72`, `2² × 3 × 5 = ` **60**. Le plus petit est **60** (diviseurs : 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60).

## 16.3 Arithmétique modulaire

**Exercice 16.3.1**

Calculez à la main `(123456789 × 987654321) mod 1000` en utilisant les propriétés de la congruence, puis vérifiez avec Python.

**Correction**

Modulo 1000, seuls comptent les trois derniers chiffres de chaque facteur : `123456789 ≡ 789` et `987654321 ≡ 321`.

`789 × 321 = 253 269`, donc `(123456789 × 987654321) mod 1000 = ` **269**.

```python
print((123456789 * 987654321) % 1000)   # 269
```

On utilise `(a × b) mod m = ((a mod m) × (b mod m)) mod m`.

### Exponentiation rapide : `a^b mod m` en O(log b)

**Exercice 16.3.2**

Implémentez `puissance_mod(a, b, m)` sans utiliser `pow`. Déroulez-la à la main pour `3^13 mod 7`.

**Correction**

```python
def puissance_mod(a, b, m):
    resultat = 1
    a %= m
    while b > 0:
        if b & 1:                       # bit courant de l'exposant égal à 1
            resultat = resultat * a % m
        a = a * a % m                   # a devient a², puis a⁴, a⁸...
        b >>= 1
    return resultat


print(puissance_mod(3, 13, 7))   # 3
```

À la main pour `3¹³ mod 7` (`13 = 1101` en binaire) :

| Exposant restant `b` | Bit | `a` | `résultat` |
| --- | --- | --- | --- |
| 13 | 1 | 3 | 1 × 3 = 3 |
| 6 | 0 | 3² = 9 ≡ 2 | 3 |
| 3 | 1 | 2² = 4 | 3 × 4 = 12 ≡ 5 |
| 1 | 1 | 4² = 16 ≡ 2 | 5 × 2 = 10 ≡ 3 |

Résultat : **3**. (Vérification : `3⁶ ≡ 1 (mod 7)` donc `3¹³ = 3¹² × 3 ≡ 3`.) Complexité O(log b).

**Exercice 16.3.3**

Calculez le dernier chiffre de `7^(10^9)` sans calculer la puissance. *(défi)*

**Correction**

Les derniers chiffres des puissances de 7 sont `7, 9, 3, 1`, puis se répètent avec une période de 4 (`7⁴ = 2401`). Il suffit donc de connaître `10⁹ mod 4`. Comme 100 est divisible par 4, `10⁹ ≡ 0 (mod 4)` : l'exposant correspond à la fin du cycle, donc le dernier chiffre est celui de `7⁴`, soit **1**.

```python
print(pow(7, 10**9, 10))   # 1
```

### Inverse modulaire

**Exercice 16.3.4**

Calculez à la main l'inverse de 3 modulo 11 et de 7 modulo 26.

**Correction**

On cherche `x` tel que `a × x ≡ 1 (mod m)`.

- Inverse de 3 modulo 11 : `3 × 4 = 12 ≡ 1 (mod 11)`, donc l'inverse est **4**.
- Inverse de 7 modulo 26 : par Euclide étendu, `26 = 3 × 7 + 5`, `7 = 1 × 5 + 2`, `5 = 2 × 2 + 1`, d'où `1 = 15 × 7 − 4 × 26`. On vérifie `7 × 15 = 105 = 4 × 26 + 1`, donc l'inverse est **15**.

**Exercice 16.3.5**

Implémentez l'inverse modulaire de deux manières : avec l'algorithme d'Euclide étendu, et avec le petit théorème de Fermat pour un modulo premier. Comparez avec `pow(a, -1, m)`.

**Correction**

```python
def inverse_euclide(a, m):
    g, x, _ = euclide_etendu(a, m)         # fonction de l'exercice 7.1.5
    if g != 1:
        raise ValueError("pas d'inverse : a et m ne sont pas premiers entre eux")
    return x % m


def inverse_fermat(a, p):
    """p doit être premier : a^(p-1) ≡ 1 donc a^(-1) ≡ a^(p-2)."""
    return pow(a, p - 2, p)


print(inverse_euclide(7, 26), pow(7, -1, 26))                    # 15 15
print(inverse_fermat(3, 11), inverse_euclide(3, 11), pow(3, -1, 11))   # 4 4 4
```

L'algorithme d'Euclide étendu fonctionne pour tout module `m` premier avec `a` ; la méthode de Fermat exige un module premier. `pow(a, -1, m)` (Python 3.8 et plus) calcule l'inverse directement et lève `ValueError` s'il n'existe pas.

**Exercice 16.3.6**

Quand l'inverse de `a` modulo `m` n'existe-t-il pas ? Donnez un exemple.

**Correction**

L'inverse de `a` modulo `m` n'existe pas quand `pgcd(a, m) ≠ 1`. En effet, `a x ≡ 1 (mod m)` signifie `a x + m y = 1`, ce qui exige que `pgcd(a, m)` divise 1.

Exemple : `6` modulo `9` (`pgcd = 3`) : les multiples de 6 modulo 9 valent `0, 6, 3, 0, 6, 3...`, jamais 1. De même, `2` modulo `4` n'a pas d'inverse.

### Binôme de Newton modulo un premier

**Exercice 16.3.7**

Calculez `C(n, k) mod p` pour `n ≤ 10⁶` et `p = 10⁹ + 7` avec des tableaux de factorielles et d'inverses de factorielles.

**Correction**

On précalcule les factorielles et les inverses des factorielles modulo `p`, puis `C(n, k) = n! × (k!)⁻¹ × ((n − k)!)⁻¹ mod p`.

```python
MOD = 10**9 + 7


def preparer_factorielles(N):
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv = [1] * (N + 1)
    inv[N] = pow(fact[N], MOD - 2, MOD)          # inverse de N! (Fermat)
    for i in range(N, 0, -1):
        inv[i - 1] = inv[i] * i % MOD            # (i-1)!⁻¹ = i!⁻¹ × i
    return fact, inv


def C(n, k, fact, inv):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv[k] % MOD * inv[n - k] % MOD


fact, inv = preparer_factorielles(10**6)
print(C(10, 3, fact, inv))        # 120
print(C(10**6, 500000, fact, inv))
```

Précalcul en O(N), chaque coefficient en O(1).

**Exercice 16.3.8**

Calculez le nombre de chemins dans une grille `m × n` (déplacements droite et bas uniquement) modulo `10⁹ + 7`.

**Correction**

Une grille `m × n` demande `m − 1` déplacements vers le bas et `n − 1` vers la droite, dans n'importe quel ordre : on choisit les positions des déplacements vers le bas parmi `m + n − 2` : `C(m + n − 2, m − 1)`.

```python
def chemins_grille(m, n, fact, inv):
    return C(m + n - 2, m - 1, fact, inv)


print(chemins_grille(3, 7, fact, inv))   # 28
print(chemins_grille(3, 2, fact, inv))   # 3
```

## 16.4 Autres outils

**Exercice 16.4.1**

Calculez `φ(36)`, `φ(97)` et `φ(100)` à la main, puis avec la fonction `phi` du cours. Vérifiez le théorème d'Euler pour `a = 7`, `m = 10`.

**Correction**

Formule : `φ(n) = n × ∏ (1 − 1/p)` sur les facteurs premiers `p` de `n`.

- `φ(36) = 36 × (1/2) × (2/3) = ` **12** (`36 = 2² × 3²`).
- `φ(97) = ` **96** (97 est premier).
- `φ(100) = 100 × (1/2) × (4/5) = ` **40** (`100 = 2² × 5²`).

```python
def phi(n):
    resultat, m, p = n, n, 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            resultat -= resultat // p
        p += 1
    if m > 1:
        resultat -= resultat // m
    return resultat


print(phi(36), phi(97), phi(100))   # 12 96 40
```

**Théorème d'Euler** pour `a = 7`, `m = 10` : `pgcd(7, 10) = 1` et `φ(10) = 4`, donc `7⁴ = 2401 ≡ 1 (mod 10)`, ce qui est bien vérifié.

**Exercice 16.4.2**

Théorème des restes chinois : résolvez le système `x ≡ 2 (mod 3)`, `x ≡ 3 (mod 5)`, `x ≡ 2 (mod 7)`. Écrivez un programme générique pour deux congruences à modules premiers entre eux.

**Correction**

**À la main** : `x ≡ 2 (mod 3)` et `x ≡ 3 (mod 5)` : les solutions de la première sont `2, 5, 8, 11, 14...` ; `8 ≡ 3 (mod 5)`, donc `x ≡ 8 (mod 15)`. Puis `8 + 15t ≡ 2 (mod 7)` : `1 + t ≡ 2`, soit `t ≡ 1`, donc `x = 23`. La solution est **x ≡ 23 (mod 105)**. Vérification : `23 mod 3 = 2`, `23 mod 5 = 3`, `23 mod 7 = 2`.

**Programme** (deux congruences à modules premiers entre eux) :

```python
def restes_chinois(a1, m1, a2, m2):
    """Renvoie x modulo m1*m2 tel que x ≡ a1 (mod m1) et x ≡ a2 (mod m2)."""
    g, u, v = euclide_etendu(m1, m2)          # m1*u + m2*v = 1
    assert g == 1
    t = ((a2 - a1) * u) % m2                  # m1 * t ≡ a2 - a1 (mod m2)
    return (a1 + m1 * t) % (m1 * m2)


x = restes_chinois(2, 3, 3, 5)       # 8 (modulo 15)
x = restes_chinois(x, 15, 2, 7)      # 23 (modulo 105)
print(x)                              # 23
```

**Exercice 16.4.3**

Calculez `fib(10¹⁸) mod (10⁹ + 7)` par exponentiation de matrices. Quelle est la complexité ?

**Correction**

On utilise la matrice `[[1, 1], [1, 0]]` : sa puissance `n`-ième contient `fib(n)` en position `[0][1]`.

```python
MOD = 10**9 + 7


def mult_mat(A, B):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
             (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
             (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]]


def puissance_mat(A, n):
    R = [[1, 0], [0, 1]]
    while n:
        if n & 1:
            R = mult_mat(R, A)
        A = mult_mat(A, A)
        n >>= 1
    return R


def fib_mod(n):
    return puissance_mat([[1, 1], [1, 0]], n)[0][1]


print(fib_mod(10))        # 55
print(fib_mod(10**18))    # 209783453
```

Complexité : **O(log n)** produits de matrices 2 × 2 (soit environ 60 pas pour `n = 10¹⁸`, chacun avec 8 multiplications).

**Exercice 16.4.4**

Calculez les nombres de Catalan `C₀` à `C₁₀` par la formule `Cₙ = C(2n, n) / (n + 1)`. Combien y a-t-il de façons de parenthéser correctement 5 paires de parenthèses ?

**Correction**

```python
from math import comb

catalan = [comb(2 * n, n) // (n + 1) for n in range(11)]
print(catalan)
# [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796]
```

`C₀` à `C₁₀` : `1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796`. Le nombre de façons de parenthéser correctement 5 paires de parenthèses est `C₅ = ` **42**.

## 16.5 Test de primalité de Miller-Rabin *(ajout)*

**Exercice 16.5.1**

Écrivez `n − 1 = 2ˢ · d` avec `d` impair pour `n = 561`, `n = 97` et `n = 1009`.

**Correction**

On divise `n − 1` par 2 tant qu'il est pair.

- `n = 561` : `n − 1 = 560 = 2⁴ × 35`, donc `s = 4` et `d = 35`.
- `n = 97` : `n − 1 = 96 = 2⁵ × 3`, donc `s = 5` et `d = 3`.
- `n = 1009` : `n − 1 = 1008 = 2⁴ × 63`, donc `s = 4` et `d = 63`.

**Exercice 16.5.2**

Expliquez pourquoi 561 (nombre de Carmichael) trompe le test de Fermat mais pas Miller-Rabin.

**Correction**

561 = 3 × 11 × 17 est un **nombre de Carmichael** : pour tout `a` premier avec 561, `a⁵⁶⁰ ≡ 1 (mod 561)`. Il passe donc le test de Fermat pour toutes les bases premières avec lui, bien qu'il soit composé.

Miller-Rabin examine en plus la suite des carrés successifs `a^d, a^(2d), ..., a^(2^(s−1) d)` : si `n` est premier, l'un des termes vaut `n − 1` (ou `a^d ≡ 1`), car `±1` sont les seules racines carrées de 1 modulo un premier. Avec `a = 2` et `561 − 1 = 2⁴ × 35` :

`2³⁵ ≡ 263`, `263² ≡ 166`, `166² ≡ 67`, `67² ≡ 1 (mod 561)`.

On atteint 1 à partir de `67`, qui n'est ni `1` ni `560 = −1` : `67` est une racine carrée **non triviale** de 1, ce qui prouve que 561 est composé. Pour tout composé impair, au moins 3/4 des bases sont des témoins de compositude.

**Exercice 16.5.3**

Implémentez Miller-Rabin avec un ensemble de témoins déterministes pour `n < 3 × 10¹⁸`. Testez-le sur des nombres premiers connus (`10⁹ + 7`, `998244353`) et sur des composés (`561`, `10⁹ + 1`).

**Correction**

Pour `n < 3,3 × 10²⁴` (donc en particulier `n < 3 × 10¹⁸`), les 12 premières bases premières `2, 3, ..., 37` forment un ensemble de témoins déterministe.

```python
BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def miller_rabin(n):
    if n < 2:
        return False
    for p in BASES:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in BASES:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False               # a est un témoin : n est composé
    return True


print(miller_rabin(10**9 + 7))     # True
print(miller_rabin(998244353))     # True
print(miller_rabin(561))           # False
print(miller_rabin(10**9 + 1))     # False (= 7 × 11 × 13 × 19 × 52579)
```

Complexité O(k log² n) pour `k` bases.

**Exercice 16.5.4**

Quelle est la probabilité d'erreur du test probabiliste avec `k` témoins aléatoires ? Quelle valeur de `k` choisir pour descendre sous `2⁻⁶⁴` ?

**Correction**

Pour un nombre composé, au moins 3/4 des bases sont des témoins : une base aléatoire échoue (ne détecte pas la compositude) avec une probabilité au plus `1/4`. Avec `k` bases indépendantes, la probabilité d'erreur est au plus **`4⁻ᵏ`**.

Pour descendre sous `2⁻⁶⁴` : `4⁻ᵏ = 2⁻²ᵏ ≤ 2⁻⁶⁴` impose `k ≥ 32`. (En pratique, la borne `1/4` est très pessimiste pour des nombres aléatoires.)

---

# 17. Hachage

## 17.1 Principe

**Exercice 17.1.1**

Qu'est-ce qu'une fonction de hachage ? Quelles propriétés doit-elle posséder pour être utilisable dans une table de hachage ?

**Correction**

Une **fonction de hachage** associe à une clé de taille quelconque un entier de taille fixe, utilisé (modulo la taille de la table) comme indice. Propriétés attendues :

1. **Déterministe** : la même clé donne toujours le même hachage.
2. **Rapide à calculer** (idéalement en temps proportionnel à la taille de la clé).
3. **Uniforme** : les hachages se répartissent également sur les cases, pour minimiser les collisions.
4. **Compatible avec l'égalité** : si `a == b`, alors `h(a) == h(b)` (la réciproque est fausse : c'est une collision).
5. Pour les structures de Python : la clé doit être **immuable** (son hachage ne doit pas changer).

**Exercice 17.1.2**

Soit la fonction de hachage `h(mot) = somme des codes ASCII mod 7`. Calculez `h` pour `"chat"`, `"chien"`, `"rat"` et `"tac"`. Que remarquez-vous ?

**Correction**

Hachage `h(mot) = (somme des codes ASCII) mod 7` :

| Mot | Somme des codes | `h` |
| --- | --- | --- |
| `chat` | 99 + 104 + 97 + 116 = 416 | `416 mod 7 = 3` |
| `chien` | 99 + 104 + 105 + 101 + 110 = 519 | `519 mod 7 = 1` |
| `rat` | 114 + 97 + 116 = 327 | `327 mod 7 = 5` |
| `tac` | 116 + 97 + 99 = 312 | `312 mod 7 = 4` |

Aucune collision ici, mais cette fonction est **mauvaise** : elle ignore l'ordre des lettres, donc tous les anagrammes entrent en collision (`tac`, `cat` et `act` donnent tous 4), et elle n'utilise que 7 valeurs possibles.

## 17.2 Les structures en Python

**Exercice 17.2.1**

Quels types peuvent servir de clé de dictionnaire ? Expliquez pourquoi `{[1, 2]: "a"}` provoque une erreur et proposez une correction.

**Correction**

Une clé de dictionnaire doit être **hachable**, c'est-à-dire immuable : `int`, `float`, `str`, `bool`, `None`, `tuple` dont tous les éléments sont hachables, `frozenset`.

`{[1, 2]: "a"}` déclenche `TypeError: unhashable type: 'list'` : une liste est modifiable, son contenu (donc son hachage) pourrait changer après insertion et la table ne retrouverait plus la clé. Solution : utiliser un tuple, `{(1, 2): "a"}`.

**Exercice 17.2.2**

Écrivez un programme qui calcule l'union, l'intersection, la différence et la différence symétrique de deux ensembles d'entiers, d'abord avec des opérateurs, puis avec des boucles et un dictionnaire.

**Correction**

```python
a, b = {1, 2, 3, 4}, {3, 4, 5}
print(a | b, a & b, a - b, a ^ b)
# {1, 2, 3, 4, 5} {3, 4} {1, 2} {1, 2, 5}
```

Sans opérateurs sur les ensembles, en utilisant des dictionnaires comme tables de hachage :

```python
def union(a, b):
    d = {}
    for x in a:
        d[x] = True
    for x in b:
        d[x] = True
    return list(d)


def intersection(a, b):
    db = dict.fromkeys(b)
    return [x for x in dict.fromkeys(a) if x in db]


def difference(a, b):
    db = dict.fromkeys(b)
    return [x for x in dict.fromkeys(a) if x not in db]


def difference_symetrique(a, b):
    return difference(a, b) + difference(b, a)
```

Chaque test d'appartenance est en O(1) en moyenne, donc chaque fonction est en O(n + m).

**Exercice 17.2.3**

Écrivez `frequences(s)` qui renvoie le dictionnaire des occurrences de chaque caractère d'une chaîne, sans utiliser `Counter`.

**Correction**

```python
def frequences(s):
    f = {}
    for c in s:
        f[c] = f.get(c, 0) + 1
    return f


print(frequences("abracadabra"))   # {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
```

Équivalent : `collections.Counter(s)`. Complexité O(n).

## 17.3 Gestion des collisions

**Exercice 17.3.1**

On insère les clés `10, 22, 31, 4, 15, 28, 17, 88, 59` dans une table de taille 11 avec `h(k) = k mod 11`. Dessinez la table obtenue avec le chaînage séparé, puis avec le sondage linéaire.

**Correction**

Fonction `h(k) = k mod 11` : `10 → 10`, `22 → 0`, `31 → 9`, `4 → 4`, `15 → 4`, `28 → 6`, `17 → 6`, `88 → 0`, `59 → 4`.

**Chaînage séparé** :

| Case | Contenu |
| --- | --- |
| 0 | 22 → 88 |
| 4 | 4 → 15 → 59 |
| 6 | 28 → 17 |
| 9 | 31 |
| 10 | 10 |
| 1, 2, 3, 5, 7, 8 | vides |

**Sondage linéaire** (insertion dans l'ordre donné) : `10` va en 10, `22` en 0, `31` en 9, `4` en 4, `15` (case 4 occupée) en 5, `28` en 6, `17` (6 occupée) en 7, `88` (0 occupée) en 1, `59` (4, 5, 6, 7 occupées) en 8.

| Case | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Clé | 22 | 88 | | | 4 | 15 | 28 | 17 | 59 | 31 | 10 |

**Exercice 17.3.2**

Implémentez une table de hachage avec chaînage séparé (`inserer`, `chercher`, `supprimer`) et redimensionnement lorsque le facteur de charge dépasse 0,75.

**Correction**

```python
class TableHachage:
    def __init__(self, capacite=8):
        self.capacite = capacite
        self.taille = 0
        self.cases = [[] for _ in range(capacite)]

    def _indice(self, cle):
        return hash(cle) % self.capacite

    def inserer(self, cle, valeur):
        case = self.cases[self._indice(cle)]
        for i, (c, _) in enumerate(case):
            if c == cle:
                case[i] = (cle, valeur)        # mise à jour
                return
        case.append((cle, valeur))
        self.taille += 1
        if self.taille / self.capacite > 0.75:  # facteur de charge trop élevé
            self._redimensionner()

    def chercher(self, cle, defaut=None):
        for c, v in self.cases[self._indice(cle)]:
            if c == cle:
                return v
        return defaut

    def supprimer(self, cle):
        case = self.cases[self._indice(cle)]
        for i, (c, _) in enumerate(case):
            if c == cle:
                del case[i]
                self.taille -= 1
                return True
        return False

    def _redimensionner(self):
        anciennes = self.cases
        self.capacite *= 2
        self.cases = [[] for _ in range(self.capacite)]
        self.taille = 0
        for case in anciennes:
            for cle, valeur in case:
                self.inserer(cle, valeur)       # les indices changent : on réinsère


t = TableHachage()
for i in range(100):
    t.inserer(i, i * i)
print(t.capacite, t.taille, t.chercher(7))   # 256 100 49
```

Le doublement de la capacité rend l'insertion en **O(1) amorti** (même argument que pour le tableau dynamique).

**Exercice 17.3.3**

Pourquoi la suppression est-elle plus délicate avec l'adressage ouvert ? Quelle technique (marqueurs de suppression) utilise-t-on ?

**Correction**

Dans un tableau à adressage ouvert, une recherche s'arrête à la première case **vide** rencontrée. Si l'on vide une case lors d'une suppression, on interrompt la suite de sondage d'éléments insérés plus tard après une collision : ils deviennent introuvables.

Technique : placer un marqueur spécial, appelé **pierre tombale** (*tombstone*). La recherche continue au-delà d'une pierre tombale, l'insertion peut la réutiliser, et on reconstruit périodiquement la table (re-hachage) quand il y en a trop.

## 17.4 Complexité

**Exercice 17.4.1**

Quelle est la complexité moyenne et la complexité au pire des opérations d'une table de hachage ? Donnez une situation où l'on atteint le pire cas.

**Correction**

- **En moyenne** : O(1) pour la recherche, l'insertion et la suppression, avec une bonne fonction de hachage et un facteur de charge borné.
- **Au pire cas** : O(n), quand toutes les clés tombent dans la même case (fonction de hachage constante, ou clés choisies par un adversaire : attaque par collisions), la table se réduisant à une liste.

**Exercice 17.4.2**

Définissez le facteur de charge. Comment évolue le coût moyen d'une recherche en fonction de celui-ci pour le chaînage ?

**Correction**

Le facteur de charge est `α = n / m` (nombre d'éléments sur nombre de cases). Avec chaînage et hachage uniforme, la longueur moyenne d'une liste est `α` :

- recherche **réussie** : environ `1 + α/2` comparaisons en moyenne ;
- recherche **infructueuse** : environ `1 + α` comparaisons.

Le coût est donc en `O(1 + α)` : il croît linéairement avec `α`. On garde `α` borné (par exemple ≤ 0,75) en redimensionnant la table, ce qui maintient un coût O(1).

## 17.5 Problèmes classiques

### Deux sommes

**Exercice 17.5.1**

Écrivez `deux_sommes(t, cible)` en O(n) avec un dictionnaire (valeur → indice). Testez sur `[2, 7, 11, 15]` avec `cible = 9`.

**Correction**

```python
def deux_sommes(t, cible):
    vus = {}                           # valeur -> indice
    for i, x in enumerate(t):
        if cible - x in vus:
            return (vus[cible - x], i)
        vus[x] = i
    return None


print(deux_sommes([2, 7, 11, 15], 9))   # (0, 1)
```

Temps O(n) en moyenne, espace O(n). Contrairement à l'approche à deux pointeurs, le tableau n'a pas besoin d'être trié et l'on conserve les indices d'origine.

**Exercice 17.5.2**

Écrivez `quatre_sommes_comptage(a, b, c, d)` qui compte les quadruplets `(i, j, k, l)` avec `a[i] + b[j] + c[k] + d[l] == 0` en O(n²). *(défi)*

**Correction**

On compte les sommes de paires `a[i] + b[j]` dans un dictionnaire, puis on cherche l'opposé de chaque somme `c[k] + d[l]`.

```python
from collections import Counter


def quatre_sommes_comptage(a, b, c, d):
    ab = Counter(x + y for x in a for y in b)
    return sum(ab.get(-(x + y), 0) for x in c for y in d)


print(quatre_sommes_comptage([1, 2], [-2, -1], [-1, 2], [0, 2]))   # 2
```

Complexité **O(n²)** en temps et en espace, au lieu de O(n⁴) pour quatre boucles imbriquées.

### Regrouper les anagrammes

**Exercice 17.5.3**

Écrivez `regrouper_anagrammes(mots)`. Testez sur `["eat", "tea", "tan", "ate", "nat", "bat"]`. Proposez deux clés possibles (mot trié, tuple de comptages) et comparez leurs coûts.

**Correction**

Deux mots sont anagrammes s'ils ont le même tri de lettres (ou le même comptage de lettres) : on l'utilise comme clé.

```python
from collections import defaultdict


def regrouper_anagrammes(mots):
    groupes = defaultdict(list)
    for mot in mots:
        groupes["".join(sorted(mot))].append(mot)
    return list(groupes.values())


print(regrouper_anagrammes(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

Coût : O(n · k log k) pour `n` mots de longueur `k`. En utilisant un tuple de 26 compteurs comme clé, on passe à O(n · k).

### Plus longue suite consécutive

**Exercice 17.5.4**

Écrivez `plus_longue_suite(t)` : la longueur de la plus longue suite d'entiers consécutifs (par exemple `[100, 4, 200, 1, 3, 2]` donne 4), en O(n).

**Correction**

On met tous les nombres dans un ensemble et on ne démarre une suite que depuis un nombre `x` tel que `x − 1` n'est pas dans l'ensemble (début de suite).

```python
def plus_longue_suite(t):
    ensemble = set(t)
    meilleur = 0
    for x in ensemble:
        if x - 1 not in ensemble:          # début d'une suite
            longueur = 1
            while x + longueur in ensemble:
                longueur += 1
            meilleur = max(meilleur, longueur)
    return meilleur


print(plus_longue_suite([100, 4, 200, 1, 3, 2]))   # 4 (1, 2, 3, 4)
```

Chaque élément est parcouru au plus deux fois (une fois comme élément de départ éventuel, une fois dans une suite) : **O(n)** en moyenne, contre O(n log n) avec un tri.

### Autres

**Exercice 17.5.5**

Écrivez `premier_caractere_unique(s)` et `contient_doublon(t)`.

**Correction**

```python
from collections import Counter


def premier_caractere_unique(s):
    compte = Counter(s)
    for i, c in enumerate(s):
        if compte[c] == 1:
            return i
    return -1


def contient_doublon(t):
    vus = set()
    for x in t:
        if x in vus:
            return True
        vus.add(x)
    return False


print(premier_caractere_unique("leetcode"))     # 0
print(premier_caractere_unique("aabb"))         # -1
print(contient_doublon([1, 2, 3, 1]))           # True
```

Les deux fonctions sont en O(n).

**Exercice 17.5.6**

Deux chaînes `s` et `t` sont isomorphes si l'on peut remplacer les caractères de `s` pour obtenir `t` (même correspondance, sans fusion de deux caractères distincts). Écrivez le test avec deux dictionnaires.

**Correction**

Deux chaînes sont isomorphes s'il existe une correspondance **bijective** entre leurs caractères. On vérifie les deux sens avec deux dictionnaires.

```python
def sont_isomorphes(s, t):
    if len(s) != len(t):
        return False
    s_vers_t, t_vers_s = {}, {}
    for a, b in zip(s, t):
        if s_vers_t.setdefault(a, b) != b or t_vers_s.setdefault(b, a) != a:
            return False
    return True


print(sont_isomorphes("egg", "add"))     # True
print(sont_isomorphes("foo", "bar"))     # False
print(sont_isomorphes("badc", "baba"))   # False (deux lettres différentes vers la même)
```

**Exercice 17.5.7**

Détectez un cycle dans un graphe orienté à l'aide d'un ensemble des sommets visités, ou dans une séquence de nombres (par exemple la suite des sommes des carrés des chiffres d'un nombre : « nombre heureux »).

**Correction**

**Nombre heureux** : on remplace `n` par la somme des carrés de ses chiffres ; la suite atteint 1 ou boucle. On détecte la boucle grâce à l'ensemble des valeurs déjà vues.

```python
def est_heureux(n):
    vus = set()
    while n != 1 and n not in vus:
        vus.add(n)
        n = sum(int(c) ** 2 for c in str(n))
    return n == 1


print([k for k in range(1, 50) if est_heureux(k)])
# [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49]
```

**Cycle dans un graphe orienté** : un simple ensemble des sommets visités suffit quand chaque sommet a **un seul** successeur (comme ci-dessus). Dans un graphe quelconque, on utilise deux ensembles : les sommets **terminés** et les sommets **en cours de visite** (sur le chemin courant) ; un cycle existe si l'on retrouve un sommet en cours.

```python
def a_un_cycle(graphe):
    termines, en_cours = set(), set()

    def visiter(u):
        en_cours.add(u)
        for v in graphe.get(u, []):
            if v in en_cours:
                return True
            if v not in termines and visiter(v):
                return True
        en_cours.remove(u)
        termines.add(u)
        return False

    return any(u not in termines and visiter(u) for u in graphe)


print(a_un_cycle({0: [1], 1: [2], 2: [0]}))   # True
print(a_un_cycle({0: [1, 2], 1: [2], 2: []})) # False
```

## 17.6 Outils du module `collections`

**Exercice 17.6.1**

Avec `Counter`, trouvez les trois mots les plus fréquents d'un texte et le nombre d'occurrences de chacun.

**Correction**

```python
from collections import Counter

texte = "le chat et le chien et le chat"
print(Counter(texte.split()).most_common(3))
# [('le', 3), ('chat', 2), ('et', 2)]
```

`Counter` est un dictionnaire spécialisé dans le comptage ; `most_common(k)` renvoie les `k` éléments les plus fréquents (les égalités sont classées par ordre d'apparition).

**Exercice 17.6.2**

Avec `defaultdict(list)`, construisez un index inversé : pour chaque mot, la liste des numéros de lignes où il apparaît.

**Correction**

```python
from collections import defaultdict


def index_inverse(documents):
    index = defaultdict(set)
    for numero, texte in enumerate(documents):
        for mot in texte.lower().split():
            index[mot].add(numero)
    return index


docs = ["le chat dort", "le chien dort", "le chat mange"]
index = index_inverse(docs)
print(sorted(index["chat"]))                       # [0, 2]
print(sorted(index["chat"] & index["dort"]))       # [0]  (documents contenant les deux mots)
```

`defaultdict` crée automatiquement l'ensemble vide à la première apparition d'un mot. La recherche d'un mot est en O(1), et l'intersection d'ensembles répond aux requêtes « et ».

**Exercice 17.6.3**

Avec `frozenset`, regroupez des ensembles égaux dans un dictionnaire. Pourquoi `set` ne peut-il pas être une clé ?

**Correction**

Un `set` est **modifiable**, donc non hachable : il ne peut pas servir de clé. Un `frozenset` est immuable et hachable ; il peut servir de clé.

```python
groupes = {}
groupes[frozenset({"a", "b"})] = "groupe 1"
groupes[frozenset({"b", "a"})] = "groupe 2"      # même ensemble : même clé
print(groupes)                                    # {frozenset({'a', 'b'}): 'groupe 2'}
# groupes[{"a", "b"}] = 1   -> TypeError: unhashable type: 'set'
```

L'égalité de `frozenset` ne tient pas compte de l'ordre.

## 17.7 Hachage d'objets et autres usages

**Exercice 17.7.1**

Définissez une classe `Point` utilisable comme clé de dictionnaire, avec `__eq__` et `__hash__` cohérents. Que se passe-t-il si l'on définit `__eq__` sans `__hash__` ?

**Correction**

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, autre):
        return isinstance(autre, Point) and (self.x, self.y) == (autre.x, autre.y)

    def __hash__(self):
        return hash((self.x, self.y))


points = {Point(1, 2), Point(1, 2), Point(3, 4)}
print(len(points))   # 2
```

Si l'on définit `__eq__` **sans** `__hash__`, Python met automatiquement `__hash__ = None` : les instances deviennent non hachables (`TypeError: unhashable type`) et ne peuvent plus être placées dans un `set` ou servir de clé. Règle : deux objets égaux doivent avoir le même hachage ; on hache le tuple des attributs qui interviennent dans `__eq__`, et l'objet ne doit pas être modifié tant qu'il est dans la table.

**Exercice 17.7.2**

Calculez les empreintes SHA-256 de deux chaînes qui ne diffèrent que d'un caractère avec `hashlib`. Que constatez-vous ? Pourquoi ne faut-il pas utiliser SHA-256 seul pour stocker des mots de passe ?

**Correction**

```python
import hashlib

for s in ("bonjour", "bonjouR"):
    print(s, hashlib.sha256(s.encode()).hexdigest())
# bonjour 2cb4b1431b84ec15d35ed83bb927e27e8967d75f4bcd9cc4b25c8d879ae23e18
# bonjouR ec75b313deb712ec321fa929354c66cf647e0feaac802ef0b7473f9d35edd890
```

Un changement d'une seule lettre produit un condensat **entièrement différent** (effet d'avalanche) : on ne peut pas deviner la ressemblance des entrées.

Pour des **mots de passe**, le SHA-256 seul est inadapté : il est très rapide, donc un attaquant teste des milliards de candidats par seconde (processeurs graphiques), et sans **sel** des tables précalculées (tables arc-en-ciel) fonctionnent, de même qu'une base de données où deux utilisateurs ont le même mot de passe laisse voir le même condensat. On utilise une fonction de dérivation **lente et salée** : `bcrypt`, `scrypt`, `Argon2` ou `hashlib.pbkdf2_hmac` avec un sel aléatoire par utilisateur.

**Exercice 17.7.3** *(défi)*

Implémentez un filtre de Bloom avec `m` bits et `k` fonctions de hachage. Quelles erreurs peut-il commettre : faux positifs, faux négatifs, ou les deux ?

**Correction**

```python
import hashlib


class FiltreBloom:
    def __init__(self, m, k):
        self.m, self.k = m, k
        self.bits = bytearray(m)                  # un octet par bit, pour la simplicité

    def _indices(self, element):
        for i in range(self.k):
            h = hashlib.sha256(f"{i}:{element}".encode()).digest()
            yield int.from_bytes(h[:8], "big") % self.m

    def ajouter(self, element):
        for i in self._indices(element):
            self.bits[i] = 1

    def peut_contenir(self, element):
        return all(self.bits[i] for i in self._indices(element))


f = FiltreBloom(10_000, 4)
for mot in ("chat", "chien", "souris"):
    f.ajouter(mot)
print(f.peut_contenir("chat"))      # True
print(f.peut_contenir("lapin"))     # False (très probablement)
```

Garanties : **jamais de faux négatif** (un élément ajouté est toujours reconnu) ; **faux positifs possibles** (un élément absent peut avoir tous ses `k` bits à 1 à cause d'autres éléments). La probabilité de faux positif est d'environ `(1 − e^(−k n/m))^k`. On ne peut pas supprimer d'élément (mettre un bit à 0 en affecterait d'autres). Mémoire : `m` bits, très inférieure à celle d'un ensemble.

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

**Correction**

Problèmes de la fonction :

1. **Clé non hachable** : `traiter([1, 2])` appelle `point in cache` avec une liste : `TypeError: unhashable type: 'list'`. Il faut convertir en `tuple`.
2. **Cache global sans limite** : la mémoire croît indéfiniment ; on utilise `functools.lru_cache(maxsize=...)` ou on borne le cache.
3. L'état global n'est pas sûr avec plusieurs fils d'exécution.

```python
from functools import lru_cache


@lru_cache(maxsize=1024)
def traiter_tuple(point):                 # point : tuple hachable
    return sum(c * c for c in point)      # calcul coûteux simulé


def traiter(point):
    return traiter_tuple(tuple(point))    # conversion en clé hachable


print(traiter([1, 2]), traiter([1, 2]))   # 5 5 (le second appel vient du cache)
```

**Exercice 17.8.2**

Pourquoi ne faut-il pas s'appuyer sur l'ordre d'itération d'un `set` ? Quelle est la garantie offerte par `dict` ?

**Correction**

L'ordre d'itération d'un `set` n'est **pas défini** : il dépend des valeurs de hachage et de l'historique des insertions et suppressions. En outre, pour les chaînes, Python **randomise** le hachage à chaque exécution (variable `PYTHONHASHSEED`) : l'ordre peut varier d'un lancement à l'autre. Il ne faut jamais s'appuyer dessus.

À l'inverse, depuis Python 3.7, un `dict` **conserve l'ordre d'insertion** : c'est une garantie du langage. Si l'on a besoin d'un ensemble ordonné, on peut utiliser `dict.fromkeys(...)` ou trier le résultat.

---

# Niveau avancé

---

# 18. Programmation dynamique

## 18.1 Principe

**Exercice 18.1.1**

Dessinez l'arbre d'appels de `fib(6)` et repérez les sous-problèmes qui se répètent. Combien de fois `fib(2)` est-il calculé ?

**Correction**

Arbre d'appels de `fib(6)` (avec les cas de base `fib(0)` et `fib(1)`) :

```text
fib(6)
├── fib(5)
│   ├── fib(4)
│   │   ├── fib(3)
│   │   │   ├── fib(2)
│   │   │   │   ├── fib(1)
│   │   │   │   └── fib(0)
│   │   │   └── fib(1)
│   │   └── fib(2)
│   │       ├── fib(1)
│   │       └── fib(0)
│   └── fib(3)
│       ├── fib(2)
│       │   ├── fib(1)
│       │   └── fib(0)
│       └── fib(1)
└── fib(4)
    ├── fib(3)
    │   ├── fib(2)
    │   │   ├── fib(1)
    │   │   └── fib(0)
    │   └── fib(1)
    └── fib(2)
        ├── fib(1)
        └── fib(0)
```

Nombre de calculs de chaque sous-problème : `fib(6)` : 1, `fib(5)` : 1, `fib(4)` : 2, `fib(3)` : 3, **`fib(2)` : 5**, `fib(1)` : 8, `fib(0)` : 5. Les mêmes sous-problèmes sont recalculés de nombreuses fois : ils **se chevauchent**. `fib(2)` est calculé **5 fois**.

**Exercice 18.1.2**

Distinguez les deux propriétés nécessaires à la programmation dynamique : sous-structure optimale et sous-problèmes qui se chevauchent. Donnez un problème qui a la première mais pas la seconde.

**Correction**

- **Sous-structure optimale** : une solution optimale du problème se construit à partir de solutions optimales de sous-problèmes (par exemple le plus court chemin passant par un sommet contient des plus courts chemins).
- **Sous-problèmes qui se chevauchent** : les mêmes sous-problèmes réapparaissent plusieurs fois dans la récursion. C'est ce qui rend la **mémorisation** utile : on calcule chaque sous-problème une seule fois.

Un problème qui a la première propriété mais pas la seconde : le **tri fusion** (ou la recherche binaire, ou le tri rapide). La solution se compose de solutions des deux moitiés, mais ces moitiés sont **disjointes** : aucun sous-problème n'est jamais rencontré deux fois, la mémorisation n'apporterait rien et l'approche « diviser pour régner » suffit.

## 18.2 Démarche en 5 étapes

**Exercice 18.2.1**

Montée d'escaliers : on peut monter 1 ou 2 marches à la fois. Combien de façons de monter `n` marches ? Appliquez les cinq étapes (état, transition, cas de base, ordre de calcul, réponse), puis codez la solution.

**Correction**

**Les cinq étapes** pour `n` marches :

1. **État** : `dp[i]` = nombre de façons de monter jusqu'à la marche `i`.
2. **Transition** : la dernière montée est de 1 ou de 2 marches : `dp[i] = dp[i − 1] + dp[i − 2]`.
3. **Cas de base** : `dp[0] = 1` (une façon de ne rien faire) et `dp[1] = 1`.
4. **Ordre de calcul** : `i` croissant de 2 à `n`.
5. **Réponse** : `dp[n]`.

```python
def escaliers(n):
    if n <= 1:
        return 1
    a, b = 1, 1                      # dp[0], dp[1]
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


print([escaliers(n) for n in range(9)])   # [1, 1, 2, 3, 5, 8, 13, 21, 34]
```

On retrouve la suite de Fibonacci décalée (`dp[n] = fib(n + 1)`). Temps O(n), espace O(1).

**Exercice 18.2.2**

Même question avec des pas de 1, 2 ou 3 marches, puis avec des marches interdites (une liste d'indices que l'on ne peut pas toucher).

**Correction**

**Pas de 1, 2 ou 3** : `dp[i] = dp[i − 1] + dp[i − 2] + dp[i − 3]` (en ne comptant que les indices ≥ 0).

```python
def escaliers3(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = sum(dp[i - k] for k in (1, 2, 3) if i - k >= 0)
    return dp[n]


print([escaliers3(n) for n in range(9)])   # [1, 1, 2, 4, 7, 13, 24, 44, 81]
```

**Marches interdites** : si la marche `i` est interdite, `dp[i] = 0` (on ne peut pas s'y poser), sinon la transition ne change pas.

```python
def escaliers_interdit(n, interdites):
    interdites = set(interdites)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if i in interdites:
            continue                      # dp[i] reste à 0
        dp[i] = sum(dp[i - k] for k in (1, 2) if i - k >= 0)
    return dp[n]


print(escaliers_interdit(5, [3]))      # 2
print(escaliers_interdit(6, [2, 4]))   # 1
```

**Exercice 18.2.3**

Énoncez pour chacun des problèmes suivants l'état `dp[...]` et la transition, sans coder : plus longue sous-suite croissante, sac à dos 0/1, distance d'édition.

**Correction**

| Problème | État | Transition | Cas de base |
| --- | --- | --- | --- |
| **Plus longue sous-suite croissante** | `dp[i]` = longueur de la plus longue sous-suite croissante **se terminant** en `t[i]` | `dp[i] = 1 + max(dp[j])` pour `j < i` avec `t[j] < t[i]` (et 1 si aucun `j`) | `dp[i] = 1` ; réponse `max(dp)` |
| **Sac à dos 0/1** | `dp[i][w]` = valeur maximale avec les `i` premiers objets et une capacité `w` | `dp[i][w] = max(dp[i − 1][w], dp[i − 1][w − pᵢ] + vᵢ)` (le second terme seulement si `pᵢ ≤ w`) | `dp[0][w] = 0` ; réponse `dp[n][C]` |
| **Distance d'édition** | `dp[i][j]` = distance entre `a[:i]` et `b[:j]` | si `a[i − 1] = b[j − 1]` : `dp[i − 1][j − 1]`, sinon `1 + min(dp[i − 1][j], dp[i][j − 1], dp[i − 1][j − 1])` | `dp[i][0] = i`, `dp[0][j] = j` ; réponse `dp[|a|][|b|]` |

## 18.3 Descendante (mémoïsation) ou ascendante (tabulation)

**Exercice 18.3.1**

Implémentez la suite de Tribonacci (`T(n) = T(n−1) + T(n−2) + T(n−3)`, `T(0) = 0`, `T(1) = T(2) = 1`) en descendante, en ascendante avec tableau, puis en ascendante avec mémoire O(1).

**Correction**

```python
import functools


# 1. Descendante (mémoïsation)
def tribonacci_desc(n):
    @functools.cache
    def T(k):
        if k == 0:
            return 0
        if k <= 2:
            return 1
        return T(k - 1) + T(k - 2) + T(k - 3)

    return T(n)


# 2. Ascendante avec tableau
def tribonacci_tab(n):
    dp = [0] * max(n + 1, 3)
    dp[1] = dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]


# 3. Ascendante avec mémoire O(1)
def tribonacci_o1(n):
    a, b, c = 0, 1, 1                # T(0), T(1), T(2)
    for _ in range(n):
        a, b, c = b, c, a + b + c
    return a


print([tribonacci_o1(n) for n in range(11)])
# [0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149]
```

Les trois versions donnent les mêmes valeurs ; temps O(n) dans tous les cas, espace O(n), O(n) et O(1) respectivement.

**Exercice 18.3.2**

Comparez les avantages et inconvénients de la descendante et de l'ascendante (profondeur de récursion, nombre de sous-problèmes calculés, optimisation de mémoire).

**Correction**

| Critère | Descendante (mémoïsation) | Ascendante (tabulation) |
| --- | --- | --- |
| **Profondeur de récursion** | égale à la profondeur du problème (risque de `RecursionError` pour `n` grand) | aucune récursion |
| **Sous-problèmes calculés** | seulement ceux qui sont **réellement nécessaires** (utile si l'espace d'états est vaste mais peu visité) | **tous** les sous-problèmes, dans l'ordre |
| **Optimisation de mémoire** | difficile : le cache garde tout | facile : on ne conserve que les dernières lignes ou valeurs utiles (O(1), ou deux lignes) |
| **Facilité d'écriture** | proche de la récurrence mathématique ; peu de réflexion sur l'ordre | demande de déterminer l'ordre de calcul des états |
| **Constantes** | surcoût des appels de fonctions et du dictionnaire | boucles simples, plus rapides |

**Exercice 18.3.3**

Pourquoi `functools.cache` est-il pratique mais parfois insuffisant (limite de récursion, mémoire) ? Quelle solution adopter pour `n = 10⁵` ?

**Correction**

`functools.cache` est pratique : un décorateur suffit pour mémoïser. Mais il est parfois insuffisant :

- **limite de récursion** : pour `n = 10⁵`, la récursion dépasse la limite par défaut (1000) et provoque une `RecursionError` ; relever la limite fait courir un risque de plantage de l'interpréteur ;
- **mémoire** : le cache conserve toutes les valeurs calculées (et les arguments), sans élimination ; il peut devenir très gros.

Pour `n = 10⁵` on adopte la version **ascendante itérative** (tableau, ou deux ou trois variables si la récurrence n'utilise que les dernières valeurs) : pas de récursion, mémoire contrôlée.

## 18.4 Problèmes 1D

### Rendu de monnaie (minimum de pièces)

**Exercice 18.4.1**

Écrivez `monnaie_min(pieces, montant)` qui renvoie le nombre minimal de pièces, ou `-1` si c'est impossible. Testez avec `[1, 3, 4]` et `6`, puis `[2]` et `3`.

**Correction**

```python
from math import inf


def monnaie_min(pieces, montant):
    dp = [0] + [inf] * montant           # dp[m] = nombre minimal de pièces pour m
    for m in range(1, montant + 1):
        for p in pieces:
            if p <= m and dp[m - p] + 1 < dp[m]:
                dp[m] = dp[m - p] + 1
    return -1 if dp[montant] == inf else dp[montant]


print(monnaie_min([1, 3, 4], 6))   # 2  (3 + 3)
print(monnaie_min([2], 3))         # -1 (impossible)
```

Temps O(montant × nombre de pièces), espace O(montant). Contrairement au glouton (qui donnerait 3 pièces pour `[1, 3, 4]` et 6), la programmation dynamique est correcte pour tout système.

**Exercice 18.4.2**

Modifiez-la pour renvoyer la liste des pièces utilisées.

**Correction**

On mémorise, pour chaque montant, la dernière pièce utilisée dans une solution optimale, puis on remonte.

```python
def monnaie_pieces(pieces, montant):
    dp = [0] + [inf] * montant
    choix = [None] * (montant + 1)
    for m in range(1, montant + 1):
        for p in pieces:
            if p <= m and dp[m - p] + 1 < dp[m]:
                dp[m] = dp[m - p] + 1
                choix[m] = p
    if dp[montant] == inf:
        return None
    resultat, m = [], montant
    while m > 0:
        resultat.append(choix[m])
        m -= choix[m]
    return resultat


print(monnaie_pieces([1, 3, 4], 6))       # [3, 3]
print(monnaie_pieces([1, 5, 6, 9], 11))   # [5, 6]
print(monnaie_pieces([2], 3))             # None
```

**Exercice 18.4.3**

Écrivez `nombre_de_facons(pieces, montant)` qui compte les façons distinctes de former le montant (l'ordre des pièces ne compte pas). Que se passe-t-il si l'on permute les deux boucles ?

**Correction**

On compte les combinaisons : on boucle d'abord sur les **pièces**, puis sur les montants, de sorte que chaque combinaison soit comptée une seule fois, dans l'ordre des pièces.

```python
def nombre_de_facons(pieces, montant):
    dp = [1] + [0] * montant              # dp[0] = 1 : une façon de former 0
    for p in pieces:                      # boucle externe : les pièces
        for m in range(p, montant + 1):
            dp[m] += dp[m - p]
    return dp[montant]


print(nombre_de_facons([1, 2, 5], 5))   # 4 : 5 ; 2+2+1 ; 2+1+1+1 ; 1+1+1+1+1
```

**Si l'on permute les deux boucles** (montants à l'extérieur, pièces à l'intérieur), on compte les **séquences ordonnées** (les permutations d'une même combinaison sont comptées séparément) :

```python
def nombre_de_sequences(pieces, montant):
    dp = [1] + [0] * montant
    for m in range(1, montant + 1):
        for p in pieces:
            if p <= m:
                dp[m] += dp[m - p]
    return dp[montant]


print(nombre_de_sequences([1, 2, 5], 5))   # 9 (par exemple 1+2+2, 2+1+2 et 2+2+1 sont distincts)
```

### Voleur de maisons (*House Robber*)

**Exercice 18.4.4**

Écrivez `voleur(t)` : montant maximal volé sans prendre deux maisons adjacentes. Testez avec `[2, 7, 9, 3, 1]`.

**Correction**

État : `dp[i]` = montant maximal volé avec les `i` premières maisons. Transition : `dp[i] = max(dp[i − 1], dp[i − 2] + t[i − 1])` (on ne prend pas la maison `i`, ou on la prend et on saute la précédente). Comme on n'utilise que les deux dernières valeurs, deux variables suffisent.

```python
def voleur(t):
    a, b = 0, 0                    # dp[i-2], dp[i-1]
    for x in t:
        a, b = b, max(b, a + x)
    return b


print(voleur([2, 7, 9, 3, 1]))   # 12  (2 + 9 + 1)
```

**Exercice 18.4.5**

Variante circulaire : la première et la dernière maison sont voisines. Adaptez votre solution.

**Correction**

Dans la variante circulaire, la première et la dernière maison ne peuvent pas être prises ensemble : on résout deux problèmes linéaires (sans la première maison, puis sans la dernière) et l'on garde le meilleur.

```python
def voleur_circulaire(t):
    if len(t) == 1:
        return t[0]
    return max(voleur(t[1:]), voleur(t[:-1]))


print(voleur_circulaire([2, 3, 2]))      # 3
print(voleur_circulaire([1, 2, 3, 1]))   # 4
```

Temps O(n), espace O(1).

### Sous-tableau de somme maximale (Kadane)

**Exercice 18.4.6**

Écrivez `kadane(t)` en O(n). Testez avec `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`.

**Correction**

`courant` = meilleure somme d'un sous-tableau **se terminant** à l'indice courant : on étend le précédent ou on repart de zéro.

```python
def kadane(t):
    meilleur = courant = t[0]
    for x in t[1:]:
        courant = max(x, courant + x)
        meilleur = max(meilleur, courant)
    return meilleur


print(kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # 6 ([4, -1, 2, 1])
```

Temps O(n), espace O(1).

**Exercice 18.4.7**

Modifiez-le pour renvoyer aussi les bornes du sous-tableau, puis pour gérer un tableau ne contenant que des valeurs négatives.

**Correction**

On mémorise le début du sous-tableau courant. En initialisant `meilleur` et `courant` avec le **premier élément** (et non 0), le cas où tous les éléments sont négatifs est géré : on renvoie le plus grand élément (le moins négatif).

```python
def kadane_bornes(t):
    meilleur = courant = t[0]
    debut = 0
    bornes = (0, 0)
    for i in range(1, len(t)):
        if t[i] > courant + t[i]:         # repartir de t[i]
            courant = t[i]
            debut = i
        else:
            courant += t[i]
        if courant > meilleur:
            meilleur = courant
            bornes = (debut, i)
    return meilleur, bornes


print(kadane_bornes([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # (6, (3, 6))
print(kadane_bornes([-3, -1, -2]))                      # (-1, (1, 1))
```

(Initialiser `meilleur` à 0 donnerait à tort 0 pour un tableau entièrement négatif.)

**Exercice 18.4.8**

Sous-tableau de produit maximal : adaptez Kadane en gardant à la fois le produit maximal et minimal en cours. *(défi)*

**Correction**

Quand on multiplie par un nombre négatif, le plus petit produit devient le plus grand et inversement : on garde donc **à la fois** le produit maximal et le produit minimal des sous-tableaux se terminant en `i`.

```python
def produit_max(t):
    maxi = mini = meilleur = t[0]
    for x in t[1:]:
        candidats = (x, maxi * x, mini * x)
        maxi, mini = max(candidats), min(candidats)
        meilleur = max(meilleur, maxi)
    return meilleur


print(produit_max([2, 3, -2, 4]))   # 6
print(produit_max([-2, 0, -1]))     # 0
print(produit_max([-2, 3, -4]))     # 24
```

Temps O(n), espace O(1).

### Plus longue sous-suite croissante (LIS)

**Exercice 18.4.9**

Écrivez `lis_quadratique(t)` en O(n²). Testez avec `[10, 9, 2, 5, 3, 7, 101, 18]`.

**Correction**

```python
def lis_quadratique(t):
    if not t:
        return 0
    dp = [1] * len(t)
    for i in range(len(t)):
        for j in range(i):
            if t[j] < t[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


print(lis_quadratique([10, 9, 2, 5, 3, 7, 101, 18]))   # 4
```

Une plus longue sous-suite est `[2, 3, 7, 101]` (ou `[2, 5, 7, 101]`). Temps O(n²), espace O(n).

**Exercice 18.4.10**

Écrivez `lis_rapide(t)` en O(n log n) avec `bisect`. Pourquoi le tableau auxiliaire n'est-il pas forcément une sous-suite valide ?

**Correction**

On maintient un tableau `q` où `q[k]` est la plus petite valeur terminant une sous-suite croissante de longueur `k + 1`. Ce tableau est toujours trié : on place chaque élément par recherche binaire.

```python
import bisect


def lis_rapide(t):
    q = []
    for x in t:
        i = bisect.bisect_left(q, x)       # première position avec q[i] >= x
        if i == len(q):
            q.append(x)                    # prolonge la plus longue sous-suite
        else:
            q[i] = x                       # améliore la fin d'une sous-suite
    return len(q)


print(lis_rapide([10, 9, 2, 5, 3, 7, 101, 18]))   # 4
```

Évolution de `q` : `[10]`, `[9]`, `[2]`, `[2, 5]`, `[2, 3]`, `[2, 3, 7]`, `[2, 3, 7, 101]`, `[2, 3, 7, 18]`. Complexité **O(n log n)**.

**Pourquoi `q` n'est pas forcément une sous-suite valide** : `q[k]` n'est qu'une **valeur de fin** pour chaque longueur ; on remplace des valeurs sans conserver l'ordre des positions. Exemple avec `[3, 4, 1]` : `q` devient `[3]`, `[3, 4]`, puis `[1, 4]`. Or `[1, 4]` n'est pas une sous-suite de `[3, 4, 1]` (le 1 vient après le 4). La **longueur** de `q` est correcte, mais pas son contenu.

**Exercice 18.4.11**

Reconstituez une plus longue sous-suite croissante (et pas seulement sa longueur).

**Correction**

Pour reconstruire, on mémorise pour chaque indice son prédécesseur.

```python
def lis_sequence(t):
    n = len(t)
    dp, parent = [1] * n, [-1] * n
    for i in range(n):
        for j in range(i):
            if t[j] < t[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
    i = max(range(n), key=lambda k: dp[k])     # fin d'une plus longue sous-suite
    resultat = []
    while i != -1:
        resultat.append(t[i])
        i = parent[i]
    return resultat[::-1]


print(lis_sequence([10, 9, 2, 5, 3, 7, 101, 18]))   # [2, 5, 7, 101]
```

(Version O(n log n) : on stocke aussi, pour chaque position dans `q`, l'indice de l'élément, et le prédécesseur de chaque élément est l'élément en `q[i − 1]` au moment de son insertion.)

## 18.5 Problèmes 2D

### Sac à dos 0/1

**Exercice 18.5.1**

Remplissez à la main le tableau DP du sac à dos 0/1 pour les objets `(valeur, poids)` : `(1, 1)`, `(4, 3)`, `(5, 4)`, `(7, 5)` et une capacité de 7.

**Correction**

Objets `(valeur, poids)` : `(1, 1)`, `(4, 3)`, `(5, 4)`, `(7, 5)`, capacité 7. `dp[i][w]` = valeur maximale avec les `i` premiers objets et la capacité `w`.

| `i` \ `w` | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 (aucun objet) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 (objet `(1, 1)`) | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 (objet `(4, 3)`) | 0 | 1 | 1 | 4 | 5 | 5 | 5 | 5 |
| 3 (objet `(5, 4)`) | 0 | 1 | 1 | 4 | 5 | 6 | 6 | 9 |
| 4 (objet `(7, 5)`) | 0 | 1 | 1 | 4 | 5 | 7 | 8 | 9 |

La valeur maximale est `dp[4][7] = ` **9**. Exemple de calcul : `dp[3][7] = max(dp[2][7], dp[2][7 − 4] + 5) = max(5, 4 + 5) = 9`. Solution : objets 2 et 3 (poids `3 + 4 = 7`, valeur `4 + 5 = 9`).

**Exercice 18.5.2**

Implémentez `sac_a_dos(objets, capacite)` en O(n · C), puis optimisez la mémoire à un tableau 1D (attention au sens de parcours des capacités).

**Correction**

```python
def sac_a_dos(objets, capacite):
    n = len(objets)
    dp = [[0] * (capacite + 1) for _ in range(n + 1)]
    for i, (valeur, poids) in enumerate(objets, 1):
        for w in range(capacite + 1):
            dp[i][w] = dp[i - 1][w]
            if poids <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - poids] + valeur)
    return dp[n][capacite]


def sac_a_dos_1d(objets, capacite):
    dp = [0] * (capacite + 1)
    for valeur, poids in objets:
        for w in range(capacite, poids - 1, -1):      # capacités décroissantes
            dp[w] = max(dp[w], dp[w - poids] + valeur)
    return dp[capacite]


objets = [(1, 1), (4, 3), (5, 4), (7, 5)]
print(sac_a_dos(objets, 7), sac_a_dos_1d(objets, 7))   # 9 9
```

Temps O(n · C). Espace O(n · C) puis O(C). **Sens de parcours** : en 1D, il faut parcourir les capacités **de la plus grande à la plus petite** : ainsi `dp[w − poids]` provient encore de la ligne précédente (l'objet n'est pas déjà pris). En sens croissant, `dp[w − poids]` aurait déjà pris en compte l'objet courant, ce qui le ferait utiliser plusieurs fois (sac à dos non borné).

**Exercice 18.5.3**

Partition en deux sous-ensembles de même somme : écrivez `partition_egale(t)`.

**Correction**

Une partition en deux sous-ensembles de même somme existe si et seulement si la somme totale `S` est paire et s'il existe un sous-ensemble de somme `S/2` : c'est un sac à dos booléen.

```python
def partition_egale(t):
    s = sum(t)
    if s % 2 == 1:
        return False
    cible = s // 2
    dp = [True] + [False] * cible
    for x in t:
        for m in range(cible, x - 1, -1):
            dp[m] = dp[m] or dp[m - x]
    return dp[cible]


print(partition_egale([1, 5, 11, 5]))   # True  ([11] et [1, 5, 5])
print(partition_egale([1, 2, 3, 5]))    # False
```

Temps O(n · S), espace O(S).

**Exercice 18.5.4**

Pourquoi O(n · C) n'est-il pas un temps polynomial au sens strict ? Quel nom donne-t-on à cette complexité ?

**Correction**

La complexité `O(n · C)` est **polynomiale en la valeur numérique** de `C`, mais pas en la **taille de l'entrée** : `C` s'écrit avec `log₂ C` bits. Si l'on ajoute un bit à la description de `C`, sa valeur double, et donc le temps aussi : le temps est **exponentiel en la taille de l'encodage** de `C`. On parle de complexité **pseudo-polynomiale**. Le problème du sac à dos est NP-difficile : on ne connaît pas d'algorithme polynomial en la taille de l'entrée.

### Plus longue sous-séquence commune (LCS)

**Exercice 18.5.5**

Remplissez à la main le tableau LCS pour `"AGGTAB"` et `"GXTXAYB"`.

**Correction**

`a = "AGGTAB"` (lignes), `b = "GXTXAYB"` (colonnes). `T[i][j]` est la longueur de la plus longue sous-séquence commune de `a[:i]` et `b[:j]`. Règle : si `a[i − 1] = b[j − 1]`, `T[i][j] = T[i − 1][j − 1] + 1`, sinon `max(T[i − 1][j], T[i][j − 1])`.

| | | G | X | T | X | A | Y | B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **A** | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 |
| **G** | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| **G** | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| **T** | 0 | 1 | 1 | 2 | 2 | 2 | 2 | 2 |
| **A** | 0 | 1 | 1 | 2 | 2 | 3 | 3 | 3 |
| **B** | 0 | 1 | 1 | 2 | 2 | 3 | 3 | 4 |

La longueur de la LCS est `T[6][7] = ` **4** ; la sous-séquence est `"GTAB"`.

**Exercice 18.5.6**

Écrivez `lcs(a, b)` renvoyant la longueur, puis `lcs_texte(a, b)` renvoyant une sous-séquence commune la plus longue par remontée dans le tableau.

**Correction**

```python
def lcs(a, b):
    T = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])
    return T[-1][-1]


def lcs_texte(a, b):
    T = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])
    i, j, resultat = len(a), len(b), []
    while i > 0 and j > 0:                     # remontée depuis le coin
        if a[i - 1] == b[j - 1]:
            resultat.append(a[i - 1])
            i -= 1
            j -= 1
        elif T[i - 1][j] >= T[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(resultat))


print(lcs("AGGTAB", "GXTXAYB"), lcs_texte("AGGTAB", "GXTXAYB"))   # 4 GTAB
print(lcs_texte("ABCBDAB", "BDCABA"))                              # BCBA (longueur 4)
```

Temps et espace O(|a| · |b|).

**Exercice 18.5.7**

Écrivez `plus_longue_sous_chaine_commune(a, b)` (sous-chaîne contiguë, et non plus sous-séquence).

**Correction**

Pour une sous-chaîne **contiguë**, on remet à 0 dès que les caractères diffèrent : `T[i][j]` est la longueur de la plus longue sous-chaîne commune **se terminant** en `a[i − 1]` et `b[j − 1]`.

```python
def plus_longue_sous_chaine_commune(a, b):
    meilleur, fin = 0, 0
    precedente = [0] * (len(b) + 1)
    for i in range(1, len(a) + 1):
        courante = [0] * (len(b) + 1)
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                courante[j] = precedente[j - 1] + 1
                if courante[j] > meilleur:
                    meilleur, fin = courante[j], i
        precedente = courante
    return a[fin - meilleur:fin]


print(plus_longue_sous_chaine_commune("abcdxyz", "xyzabcd"))   # abcd
```

Temps O(|a| · |b|), espace O(|b|).

### Distance d'édition (Levenshtein)

**Exercice 18.5.8**

Calculez à la main la distance d'édition entre `"kitten"` et `"sitting"` en remplissant le tableau.

**Correction**

`D[i][j]` est la distance d'édition entre `kitten[:i]` et `sitting[:j]` ; `D[i][0] = i`, `D[0][j] = j`, et `D[i][j] = D[i − 1][j − 1]` si les lettres sont égales, sinon `1 + min(D[i − 1][j], D[i][j − 1], D[i − 1][j − 1])`.

| | | s | i | t | t | i | n | g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| **k** | 1 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| **i** | 2 | 2 | 1 | 2 | 3 | 4 | 5 | 6 |
| **t** | 3 | 3 | 2 | 1 | 2 | 3 | 4 | 5 |
| **t** | 4 | 4 | 3 | 2 | 1 | 2 | 3 | 4 |
| **e** | 5 | 5 | 4 | 3 | 2 | 2 | 3 | 4 |
| **n** | 6 | 6 | 5 | 4 | 3 | 3 | 2 | 3 |

La distance d'édition est `D[6][7] = ` **3**.

**Exercice 18.5.9**

Implémentez `distance_edition(a, b)`, puis optimisez la mémoire à deux lignes. Écrivez enfin la liste des opérations à effectuer.

**Correction**

```python
def distance_edition(a, b):
    D = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a) + 1):
        D[i][0] = i
    for j in range(len(b) + 1):
        D[0][j] = j
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            D[i][j] = min(D[i - 1][j] + 1,                        # suppression
                          D[i][j - 1] + 1,                        # insertion
                          D[i - 1][j - 1] + (a[i - 1] != b[j - 1]))   # remplacement
    return D[-1][-1]


def distance_edition_2_lignes(a, b):
    precedente = list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        courante = [i] + [0] * len(b)
        for j in range(1, len(b) + 1):
            courante[j] = min(precedente[j] + 1,
                              courante[j - 1] + 1,
                              precedente[j - 1] + (a[i - 1] != b[j - 1]))
        precedente = courante
    return precedente[-1]


print(distance_edition("kitten", "sitting"), distance_edition_2_lignes("kitten", "sitting"))   # 3 3
```

Pour **lister les opérations**, on conserve le tableau complet et on remonte depuis `D[|a|][|b|]` :

```python
def operations(a, b):
    D = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a) + 1):
        D[i][0] = i
    for j in range(len(b) + 1):
        D[0][j] = j
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] + 1,
                          D[i - 1][j - 1] + (a[i - 1] != b[j - 1]))
    i, j, ops = len(a), len(b), []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and a[i - 1] == b[j - 1] and D[i][j] == D[i - 1][j - 1]:
            i, j = i - 1, j - 1                                   # lettres égales
        elif i > 0 and j > 0 and D[i][j] == D[i - 1][j - 1] + 1:
            ops.append(f"remplacer {a[i - 1]!r} par {b[j - 1]!r} (position {i - 1})")
            i, j = i - 1, j - 1
        elif i > 0 and D[i][j] == D[i - 1][j] + 1:
            ops.append(f"supprimer {a[i - 1]!r} (position {i - 1})")
            i -= 1
        else:
            ops.append(f"insérer {b[j - 1]!r} (après la position {i - 1})")
            j -= 1
    return ops[::-1]


for op in operations("kitten", "sitting"):
    print(op)
# remplacer 'k' par 's' (position 0)
# remplacer 'e' par 'i' (position 4)
# insérer 'g' (après la position 5)
```

Soit : `kitten → sitten → sittin → sitting`. Temps O(|a| · |b|), espace O(min(|a|, |b|)) pour la distance seule.

**Exercice 18.5.10**

Écrivez un correcteur orthographique simple : pour un mot donné, renvoyer les mots d'un dictionnaire à distance d'édition minimale.

**Correction**

```python
def corrections(mot, dictionnaire):
    meilleure, resultats = float("inf"), []
    for candidat in dictionnaire:
        d = distance_edition_2_lignes(mot, candidat)
        if d < meilleure:
            meilleure, resultats = d, [candidat]
        elif d == meilleure:
            resultats.append(candidat)
    return meilleure, resultats


dico = ["chat", "chats", "char", "chien", "chant", "plat"]
print(corrections("chet", dico))   # (1, ['chat'])
print(corrections("chas", dico))   # (1, ['chat', 'chats', 'char'])
```

Complexité O(|dictionnaire| × |mot| × longueur moyenne). Pour un grand dictionnaire, on pré-filtre par longueur (`|longueur| ≤ distance maximale`) ou on utilise un trie avec distance bornée.

### Chemins dans une grille

**Exercice 18.5.11**

Écrivez `chemins(m, n)` : nombre de chemins du coin supérieur gauche au coin inférieur droit avec déplacements droite / bas.

**Correction**

`dp[i][j] = dp[i − 1][j] + dp[i][j − 1]` (on arrive d'en haut ou de la gauche) ; première ligne et première colonne égales à 1.

```python
def chemins(m, n):
    dp = [1] * n                       # première ligne
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]


print(chemins(3, 7))   # 28
print(chemins(3, 2))   # 3
```

Temps O(m·n), espace O(n). Le résultat est aussi `C(m + n − 2, m − 1)`.

**Exercice 18.5.12**

Même question avec des obstacles dans la grille, puis calculez le chemin de **coût minimal** pour une grille de coûts.

**Correction**

**Avec obstacles** (1 = obstacle) : `dp[i][j] = 0` si la case est un obstacle, sinon `dp[i − 1][j] + dp[i][j − 1]`.

```python
def chemins_obstacles(grille):
    m, n = len(grille), len(grille[0])
    dp = [0] * n
    dp[0] = 1 if grille[0][0] == 0 else 0
    for i in range(m):
        for j in range(n):
            if grille[i][j] == 1:
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j - 1]
    return dp[-1]


print(chemins_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))   # 2
```

**Chemin de coût minimal** : `dp[i][j] = coût[i][j] + min(dp[i − 1][j], dp[i][j − 1])`.

```python
def cout_minimal(g):
    m, n = len(g), len(g[0])
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = g[0][0]
            else:
                haut = dp[i - 1][j] if i > 0 else float("inf")
                gauche = dp[i][j - 1] if j > 0 else float("inf")
                dp[i][j] = g[i][j] + min(haut, gauche)
    return dp[-1][-1]


print(cout_minimal([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))   # 7 (1 → 3 → 1 → 1 → 1)
```

### Autres classiques

**Exercice 18.5.13**

Écrivez un programme pour chacun des problèmes suivants :

1. plus longue sous-chaîne palindromique ;
2. découpage de tige (prix par longueur, longueur totale `n`) ;
3. plus grand carré composé uniquement de 1 dans une grille binaire ;
4. produit de chaînes de matrices (coût minimal de multiplication) ;
5. nombre de façons de décoder une chaîne de chiffres (`"12"` : `"AB"` ou `"L"`).

**Correction**

**1. Plus longue sous-chaîne palindromique** (expansion autour de chaque centre, O(n²)) :

```python
def plus_longue_palindrome(s):
    meilleur = ""
    for c in range(len(s)):
        for gauche, droite in ((c, c), (c, c + 1)):       # centre impair, centre pair
            while gauche >= 0 and droite < len(s) and s[gauche] == s[droite]:
                gauche -= 1
                droite += 1
            if droite - gauche - 1 > len(meilleur):
                meilleur = s[gauche + 1:droite]
    return meilleur


print(plus_longue_palindrome("babad"), plus_longue_palindrome("cbbd"))   # bab bb
```

(La version par tableau `dp[i][j] = (s[i] == s[j]) and dp[i + 1][j − 1]` est aussi en O(n²).)

**2. Découpage de tige** : `dp[i] = max(prix[l − 1] + dp[i − l])` pour `1 ≤ l ≤ i`.

```python
def decoupage_tige(prix, n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for l in range(1, min(i, len(prix)) + 1):
            dp[i] = max(dp[i], prix[l - 1] + dp[i - l])
    return dp[n]


print(decoupage_tige([1, 5, 8, 9, 10, 17, 17, 20], 8))   # 22 (2 + 6 : 5 + 17)
```

**3. Plus grand carré de 1** : `dp[i][j]` = côté du plus grand carré dont le coin inférieur droit est `(i, j)` ; si la case vaut 1, `dp[i][j] = 1 + min(dp[i − 1][j], dp[i][j − 1], dp[i − 1][j − 1])`.

```python
def plus_grand_carre(g):
    m, n = len(g), len(g[0])
    dp = [[0] * n for _ in range(m)]
    meilleur = 0
    for i in range(m):
        for j in range(n):
            if g[i][j] == 1:
                dp[i][j] = 1 if i == 0 or j == 0 else 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                meilleur = max(meilleur, dp[i][j])
    return meilleur


print(plus_grand_carre([[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]))   # 2
```

**4. Produit de chaînes de matrices** : `dp[i][j]` = coût minimal pour multiplier les matrices `i` à `j` ; `dp[i][j] = min(dp[i][k] + dp[k + 1][j] + d[i − 1]·d[k]·d[j])` pour `i ≤ k < j`.

```python
def chaine_matrices(d):
    n = len(d) - 1                                # n matrices, la matrice i est d[i-1] x d[i]
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for longueur in range(2, n + 1):
        for i in range(1, n - longueur + 2):
            j = i + longueur - 1
            dp[i][j] = float("inf")
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + d[i - 1] * d[k] * d[j])
    return dp[1][n]


print(chaine_matrices([10, 30, 5, 60]))       # 4500
print(chaine_matrices([40, 20, 30, 10, 30]))  # 26000
```

Temps O(n³), espace O(n²).

**5. Nombre de façons de décoder** : `dp[i]` = nombre de décodages des `i` premiers chiffres. On ajoute `dp[i − 1]` si le chiffre `s[i − 1]` n'est pas `"0"` (lettre seule), et `dp[i − 2]` si le nombre formé par `s[i − 2]` et `s[i − 1]` est compris entre 10 et 26 (lettre sur deux chiffres).

```python
def decoder(s):
    if not s or s[0] == "0":
        return 0
    a, b = 1, 1                                   # dp[i-2], dp[i-1]
    for i in range(1, len(s)):
        c = 0
        if s[i] != "0":
            c += b
        if 10 <= int(s[i - 1:i + 1]) <= 26:
            c += a
        a, b = b, c
    return b


print(decoder("12"), decoder("226"), decoder("06"), decoder("10"))   # 2 3 0 1
```

**Exercice 18.5.14**

Sur l'arbre binaire de votre choix, calculez par DP sur les arbres le poids maximal d'un ensemble de sommets sans deux sommets adjacents (ensemble indépendant de poids maximal).

**Correction**

Pour chaque nœud, on calcule deux valeurs : le poids maximal **en prenant** le nœud (alors ses enfants sont exclus) et **sans le prendre** (alors chaque enfant est libre).

```python
class Noeud:
    def __init__(self, poids, gauche=None, droite=None):
        self.poids, self.gauche, self.droite = poids, gauche, droite


def ensemble_independant(n):
    """Renvoie (poids max en prenant n, poids max sans prendre n)."""
    if n is None:
        return 0, 0
    pris_g, libre_g = ensemble_independant(n.gauche)
    pris_d, libre_d = ensemble_independant(n.droite)
    pris = n.poids + libre_g + libre_d
    libre = max(pris_g, libre_g) + max(pris_d, libre_d)
    return pris, libre


racine = Noeud(3, Noeud(4, Noeud(1), Noeud(3)), Noeud(5, None, Noeud(1)))
print(max(ensemble_independant(racine)))   # 9 (4 + 5 : les deux enfants de la racine)
```

Dans cet arbre, la racine (3) a pour enfants 4 (de feuilles 1 et 3) et 5 (de feuille droite 1). Le meilleur ensemble est `{4, 5}` de poids 9. Complexité O(n).

**Exercice 18.5.15** *(défi)*

DP par chiffres : combien d'entiers de `1` à `N` ne contiennent pas le chiffre `4` ?

**Correction**

On construit les nombres chiffre par chiffre (de gauche à droite) avec l'état `(position, serré)`, où `serré` indique que le préfixe est égal à celui de `N` (donc le chiffre suivant est borné par celui de `N`).

```python
import functools


def sans_quatre(N):
    s = str(N)
    L = len(s)

    @functools.cache
    def f(pos, serre):
        if pos == L:
            return 1                                  # un nombre complet (peut être 0)
        limite = int(s[pos]) if serre else 9
        total = 0
        for d in range(limite + 1):
            if d == 4:
                continue
            total += f(pos + 1, serre and d == limite)
        return total

    return f(0, True) - 1                             # on retire 0


print(sans_quatre(100))      # 81
print(sans_quatre(10**6))    # 531441 (= 9⁶)
```

Vérification par force brute : `sum(1 for i in range(1, 101) if "4" not in str(i)) = 81`. Il y a au plus `L × 2 × 10` transitions : le calcul est en O(L) pour `N` à `L` chiffres, donc il tient pour `N = 10¹⁸`.

## 18.6 DP avec masque de bits

**Exercice 18.6.1**

Pour un ensemble de 4 éléments, listez les masques de `0000` à `1111` et le sous-ensemble correspondant. Écrivez des fonctions : tester si `i ∈ S`, ajouter `i`, retirer `i`, compter les éléments, énumérer les sous-ensembles d'un masque.

**Correction**

Convention : le bit `i` du masque vaut 1 si l'élément `i` appartient au sous-ensemble.

| Masque | Sous-ensemble | Masque | Sous-ensemble |
| --- | --- | --- | --- |
| `0000` | `{}` | `1000` | `{3}` |
| `0001` | `{0}` | `1001` | `{0, 3}` |
| `0010` | `{1}` | `1010` | `{1, 3}` |
| `0011` | `{0, 1}` | `1011` | `{0, 1, 3}` |
| `0100` | `{2}` | `1100` | `{2, 3}` |
| `0101` | `{0, 2}` | `1101` | `{0, 2, 3}` |
| `0110` | `{1, 2}` | `1110` | `{1, 2, 3}` |
| `0111` | `{0, 1, 2}` | `1111` | `{0, 1, 2, 3}` |

```python
def contient(S, i):
    return (S >> i) & 1 == 1


def ajouter(S, i):
    return S | (1 << i)


def retirer(S, i):
    return S & ~(1 << i)


def compter(S):
    return bin(S).count("1")               # ou S.bit_count() en Python 3.10+


def sous_ensembles(S):
    """Énumère tous les sous-masques de S (S inclus, 0 inclus)."""
    s = S
    while True:
        yield s
        if s == 0:
            break
        s = (s - 1) & S


print([format(s, "04b") for s in sous_ensembles(0b1011)])
# ['1011', '1010', '1001', '1000', '0011', '0010', '0001', '0000']
```

Un masque à `k` bits à 1 a `2ᵏ` sous-masques ; l'énumération de tous les sous-masques de tous les masques coûte `3ⁿ` au total.

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

**Correction**

`dp[masque][dernier]` = longueur minimale d'un chemin qui part de la ville 0, visite exactement les villes de `masque` et finit en `dernier`. Le bit `i` du masque correspond à la ville `i`. Voici les états atteignables :

| Masque (villes visitées) | `dernier = 0` | `dernier = 1` | `dernier = 2` | `dernier = 3` |
| --- | --- | --- | --- | --- |
| `0001` | 0 | | | |
| `0011` | | 10 | | |
| `0101` | | | 15 | |
| `1001` | | | | 20 |
| `0111` | | 50 (`0→2→1`) | 45 (`0→1→2`) | |
| `1011` | | 45 (`0→3→1`) | | 35 (`0→1→3`) |
| `1101` | | | 50 (`0→3→2`) | 45 (`0→2→3`) |
| `1111` | | 70 | 65 | 75 |

Fermeture du cycle (retour à la ville 0) : `70 + d(1, 0) = 80`, `65 + d(2, 0) = 80`, `75 + d(3, 0) = 95`. Le minimum est **80**, atteint par les tournées `0 → 1 → 3 → 2 → 0` (10 + 25 + 30 + 15) et son inverse `0 → 2 → 3 → 1 → 0`.

**Exercice 18.6.3**

Implémentez `tsp(distances)` avec `dp[masque][dernier]`. Quelles sont les complexités en temps et en espace ? Jusqu'à quel `n` est-ce praticable ?

**Correction**

```python
from math import inf


def tsp(distances):
    n = len(distances)
    dp = [[inf] * n for _ in range(1 << n)]
    dp[1][0] = 0                                    # on part de la ville 0
    for masque in range(1 << n):
        for dernier in range(n):
            if dp[masque][dernier] == inf or not (masque >> dernier) & 1:
                continue
            for suivant in range(n):
                if not (masque >> suivant) & 1:
                    nouveau = masque | (1 << suivant)
                    cout = dp[masque][dernier] + distances[dernier][suivant]
                    if cout < dp[nouveau][suivant]:
                        dp[nouveau][suivant] = cout
    complet = (1 << n) - 1
    return min(dp[complet][d] + distances[d][0] for d in range(1, n))


D = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
print(tsp(D))   # 80
```

Complexités : temps **O(2ⁿ · n²)**, espace **O(2ⁿ · n)**. C'est praticable jusqu'à `n` d'environ 15 à 20 (en Python, `n ≈ 15` ; en langage compilé, `n ≈ 20 à 23`) ; au-delà, il faut des heuristiques ou des méthodes approchées. La force brute en O(n!) s'arrête vers `n ≈ 11`.

**Exercice 18.6.4**

Affectation de tâches : `n` ouvriers, `n` tâches, une matrice de coûts. Trouvez l'affectation de coût minimal par DP sur les masques.

**Correction**

`dp[masque]` = coût minimal pour affecter les `popcount(masque)` premiers ouvriers aux tâches du masque. L'ouvrier suivant est celui d'indice `popcount(masque)`.

```python
def affectation(couts):
    n = len(couts)
    dp = [inf] * (1 << n)
    dp[0] = 0
    for masque in range(1 << n):
        i = bin(masque).count("1")                  # prochain ouvrier à affecter
        if i >= n or dp[masque] == inf:
            continue
        for tache in range(n):
            if not (masque >> tache) & 1:
                nouveau = masque | (1 << tache)
                dp[nouveau] = min(dp[nouveau], dp[masque] + couts[i][tache])
    return dp[(1 << n) - 1]


couts = [[9, 2, 7, 8], [6, 4, 3, 7], [5, 8, 1, 8], [7, 6, 9, 4]]
print(affectation(couts))   # 13 (2 + 6 + 1 + 4)
```

Temps O(2ⁿ · n), espace O(2ⁿ). (L'algorithme hongrois résout ce problème en O(n³).)

## 18.7 Reconstituer la solution

**Exercice 18.7.1**

Pour chacun des problèmes suivants, ajoutez une structure de « parents » (ou une remontée dans le tableau) afin de reconstituer une solution optimale : rendu de monnaie, sac à dos 0/1, LCS, plus court chemin dans une grille.

**Correction**

**Rendu de monnaie** : on mémorise la dernière pièce utilisée (`choix[m]`) et on remonte (exercice 18.4.2).

**Sac à dos 0/1** : on garde le tableau complet et on remonte depuis `dp[n][C]` : si `dp[i][w] ≠ dp[i − 1][w]`, l'objet `i` est pris et on retire son poids.

```python
def sac_a_dos_objets(objets, capacite):
    n = len(objets)
    dp = [[0] * (capacite + 1) for _ in range(n + 1)]
    for i, (valeur, poids) in enumerate(objets, 1):
        for w in range(capacite + 1):
            dp[i][w] = dp[i - 1][w]
            if poids <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - poids] + valeur)
    w, pris = capacite, []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            pris.append(i - 1)
            w -= objets[i - 1][1]
    return dp[n][capacite], pris[::-1]


print(sac_a_dos_objets([(1, 1), (4, 3), (5, 4), (7, 5)], 7))   # (9, [1, 2])
```

**LCS** : remontée dans le tableau (exercice 18.5.6).

**Plus court chemin dans une grille** (coût minimal vers le coin inférieur droit) : on remonte en choisissant à chaque case le voisin (haut ou gauche) qui a fourni la valeur minimale.

```python
def chemin_minimal(g):
    m, n = len(g), len(g[0])
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = g[0][0]
            else:
                haut = dp[i - 1][j] if i > 0 else float("inf")
                gauche = dp[i][j - 1] if j > 0 else float("inf")
                dp[i][j] = g[i][j] + min(haut, gauche)
    i, j, chemin = m - 1, n - 1, [(m - 1, n - 1)]
    while (i, j) != (0, 0):
        if i > 0 and (j == 0 or dp[i - 1][j] <= dp[i][j - 1]):
            i -= 1
        else:
            j -= 1
        chemin.append((i, j))
    return dp[-1][-1], chemin[::-1]


print(chemin_minimal([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
# (7, [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)])
```

Pour cette grille, le chemin est : droite, droite, bas, bas, de coût `1 + 3 + 1 + 1 + 1 = 7`.

## 18.8 Conseils

**Exercice 18.8.1**

Pour chaque problème, définissez l'état, la transition, les cas de base et la complexité :

1. « Mots les plus longs » : la plus longue chaîne de mots où chacun s'obtient du précédent en ajoutant une lettre.
2. Nombre de façons d'atteindre la somme `S` avec `n` dés à `f` faces.
3. Gain maximal en achetant et vendant une action avec au plus `k` transactions.

**Correction**

**1. Mots les plus longs (chaîne de mots).** Trier les mots par longueur. *État* : `dp[w]` = longueur de la plus longue chaîne se terminant par le mot `w`. *Transition* : `dp[w] = 1 + max(dp[p])` pour chaque mot `p` obtenu en supprimant une lettre de `w` et présent dans l'ensemble des mots. *Base* : `dp[w] = 1` si aucun prédécesseur. *Réponse* : `max(dp)`. *Complexité* : O(n · L²) pour `n` mots de longueur au plus `L` (L suppressions, chacune coûtant O(L) pour former le mot), plus O(n log n) de tri.

**2. Nombre de façons d'obtenir la somme `S` avec `n` dés à `f` faces.** *État* : `dp[i][s]` = nombre de façons d'obtenir la somme `s` avec `i` dés. *Transition* : `dp[i][s] = Σ dp[i − 1][s − k]` pour `k` de 1 à `f` (avec `s − k ≥ 0`). *Base* : `dp[0][0] = 1`, `dp[0][s > 0] = 0`. *Réponse* : `dp[n][S]`. *Complexité* : O(n · S · f) en temps, ramenée à O(n · S) avec des sommes préfixes ; espace O(S) avec deux lignes.

**3. Gain maximal avec au plus `k` transactions.** *État* : `dp[t][i]` = gain maximal avec au plus `t` transactions en ne considérant que les `i + 1` premiers jours. *Transition* : `dp[t][i] = max(dp[t][i − 1], prix[i] + max_{j < i}(dp[t − 1][j] − prix[j]))` ; on maintient ce maximum au fur et à mesure. *Base* : `dp[0][i] = 0` et `dp[t][0] = 0`. *Réponse* : `dp[k][n − 1]`. *Complexité* : O(k · n) en temps, O(n) en espace ; si `k ≥ n / 2`, il suffit d'un algorithme glouton en O(n) (on additionne toutes les hausses).

**Exercice 18.8.2**

Dans quels cas doit-on essayer la programmation dynamique ? Dans quels cas un algorithme glouton ou une recherche binaire sont-ils plus adaptés ?

**Correction**

**Essayer la programmation dynamique** quand :

- le problème demande un **optimum** (minimum, maximum) ou un **dénombrement** ;
- il possède une **sous-structure optimale** ;
- les sous-problèmes **se chevauchent** (la récursion naïve est exponentielle) ;
- l'espace des états est de taille raisonnable (polynomiale, ou exponentielle mais petite comme les masques de bits).

**Un algorithme glouton** est plus adapté quand le problème a la **propriété du choix glouton** (sélection d'activités, sac à dos fractionnaire, Huffman, arbre couvrant minimal) : plus simple et plus rapide, mais il faut une preuve d'exactitude.

**Une recherche binaire** est plus adaptée quand on cherche une valeur seuil avec une **fonction de décision monotone** (capacité minimale, vitesse minimale) : la réponse n'est pas construite par combinaison de sous-problèmes mais par encadrement.

---

# 19. Algorithmes sur les graphes

## 19.1 Représentation

**Exercice 19.1.1**

Pour le graphe non orienté ayant les arêtes `(0,1), (0,2), (1,2), (1,3), (3,4)` (5 sommets), donnez la liste d'adjacence, la matrice d'adjacence et le degré de chaque sommet.

**Correction**

Graphe non orienté, 5 sommets, arêtes `(0,1), (0,2), (1,2), (1,3), (3,4)`.

**Liste d'adjacence** :

```text
0 : [1, 2]
1 : [0, 2, 3]
2 : [0, 1]
3 : [1, 4]
4 : [3]
```

**Matrice d'adjacence** (symétrique) :

```text
    0  1  2  3  4
0 [ 0, 1, 1, 0, 0 ]
1 [ 1, 0, 1, 1, 0 ]
2 [ 1, 1, 0, 0, 0 ]
3 [ 0, 1, 0, 0, 1 ]
4 [ 0, 0, 0, 1, 0 ]
```

**Degrés** : `deg(0) = 2`, `deg(1) = 3`, `deg(2) = 2`, `deg(3) = 2`, `deg(4) = 1`. La somme vaut 10 = 2 × 5 arêtes (lemme des poignées de main).

**Exercice 19.1.2**

Écrivez `construire_graphe(n, aretes, oriente=False)` qui construit une liste d'adjacence, puis une version pondérée où chaque entrée contient `(voisin, poids)`.

**Correction**

```python
def construire_graphe(n, aretes, oriente=False):
    """aretes : (u, v) ou (u, v, poids). Liste d'adjacence ; voisins ou (voisin, poids)."""
    graphe = [[] for _ in range(n)]
    for arete in aretes:
        u, v = arete[0], arete[1]
        if len(arete) > 2:
            graphe[u].append((v, arete[2]))
            if not oriente:
                graphe[v].append((u, arete[2]))
        else:
            graphe[u].append(v)
            if not oriente:
                graphe[v].append(u)
    return graphe


print(construire_graphe(5, [(0, 1), (0, 2), (1, 2), (1, 3), (3, 4)]))
# [[1, 2], [0, 2, 3], [0, 1], [1, 4], [3]]
print(construire_graphe(3, [(0, 1, 5), (1, 2, 2)]))
# [[(1, 5)], [(0, 5), (2, 2)], [(1, 2)]]
print(construire_graphe(3, [(0, 1), (1, 2)], oriente=True))
# [[1], [2], []]
```

Dans le cas orienté, on n'ajoute que l'arc `u → v`.

**Exercice 19.1.3**

Comparez liste et matrice d'adjacence en espace, en test d'existence d'une arête et en parcours des voisins. Pour quelle densité de graphe la matrice est-elle préférable ?

**Correction**

| Critère | Liste d'adjacence | Matrice d'adjacence |
| --- | --- | --- |
| **Espace** | O(n + m) | O(n²) |
| **Test d'existence d'une arête `(u, v)`** | O(deg(u)) (O(1) avec des ensembles) | **O(1)** |
| **Parcours des voisins de `u`** | **O(deg(u))** | O(n) |
| **Ajout d'une arête** | O(1) | O(1) |

La matrice est préférable pour les graphes **denses** (`m` proche de `n²`), ou quand on teste très souvent l'existence d'arêtes, ou pour de petits graphes. Pour les graphes **peu denses** (la plupart des cas pratiques : `m = O(n)`), la liste est bien plus économe et parcourt les voisins plus vite.

**Exercice 19.1.4**

Écrivez `degres(graphe)` pour un graphe orienté (degré entrant et sortant de chaque sommet). Vérifiez que la somme des degrés sortants vaut le nombre d'arêtes.

**Correction**

```python
def degres(graphe):
    n = len(graphe)
    entrants = [0] * n
    sortants = [len(voisins) for voisins in graphe]
    for u in range(n):
        for v in graphe[u]:
            entrants[v] += 1
    return entrants, sortants


g = construire_graphe(4, [(0, 1), (0, 2), (1, 2), (2, 3)], oriente=True)
entrants, sortants = degres(g)
print(entrants, sortants)           # [0, 1, 2, 1] [2, 1, 1, 0]
print(sum(sortants), sum(entrants)) # 4 4 : le nombre d'arcs
```

Chaque arc contribue à un degré sortant (pour son origine) et à un degré entrant (pour sa destination) : `Σ deg⁺ = Σ deg⁻ = m`.

## 19.2 Parcours en largeur (BFS)

**Exercice 19.2.1**

Déroulez à la main un BFS depuis le sommet 0 sur le graphe de l'exercice 19.1.1, en notant le contenu de la file à chaque étape.

**Correction**

BFS depuis le sommet 0 (voisins parcourus dans l'ordre de la liste) :

| Étape | Sommet extrait | Voisins nouvellement découverts | File après l'étape |
| --- | --- | --- | --- |
| initial | | | `[0]` |
| 1 | 0 | 1, 2 | `[1, 2]` |
| 2 | 1 | 3 (0 et 2 déjà vus) | `[2, 3]` |
| 3 | 2 | aucun | `[3]` |
| 4 | 3 | 4 | `[4]` |
| 5 | 4 | aucun | `[]` |

Ordre de visite : `0, 1, 2, 3, 4`. Distances depuis 0 : `[0, 1, 1, 2, 3]`.

**Exercice 19.2.2**

Implémentez `bfs(graphe, source)` qui renvoie la liste des distances (en nombre d'arêtes) depuis `source`, ou `-1` pour les sommets inaccessibles.

**Correction**

```python
from collections import deque


def bfs(graphe, source):
    distances = [-1] * len(graphe)
    distances[source] = 0
    file = deque([source])
    while file:
        u = file.popleft()
        for v in graphe[u]:
            if distances[v] == -1:               # non visité
                distances[v] = distances[u] + 1
                file.append(v)
    return distances


g = construire_graphe(5, [(0, 1), (0, 2), (1, 2), (1, 3), (3, 4)])
print(bfs(g, 0))                                              # [0, 1, 1, 2, 3]
print(bfs(construire_graphe(5, [(0, 1), (2, 3)]), 0))         # [0, 1, -1, -1, -1]
```

Complexité O(n + m). Le BFS donne les plus courts chemins en **nombre d'arêtes**.

**Exercice 19.2.3**

Modifiez-le pour reconstituer un plus court chemin entre deux sommets (tableau des parents).

**Correction**

On mémorise le parent de chaque sommet à sa découverte, puis on remonte de la destination vers la source.

```python
def plus_court_chemin(graphe, source, cible):
    parent = [-1] * len(graphe)
    vu = [False] * len(graphe)
    vu[source] = True
    file = deque([source])
    while file:
        u = file.popleft()
        if u == cible:
            break
        for v in graphe[u]:
            if not vu[v]:
                vu[v] = True
                parent[v] = u
                file.append(v)
    if not vu[cible]:
        return None
    chemin = [cible]
    while chemin[-1] != source:
        chemin.append(parent[chemin[-1]])
    return chemin[::-1]


print(plus_court_chemin(g, 0, 4))   # [0, 1, 3, 4]
```

**Exercice 19.2.4**

Labyrinthe : dans une grille de `0` (libre) et `1` (mur), trouvez la longueur du plus court chemin entre deux cases avec des déplacements dans 4 directions, puis dans 8 directions.

**Correction**

Le BFS sur la grille : les voisins d'une case sont les cases libres adjacentes (4 directions, ou 8 en ajoutant les diagonales).

```python
from collections import deque


def plus_court_chemin_grille(grille, depart, arrivee, huit=False):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    if huit:
        directions += [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    m, n = len(grille), len(grille[0])
    if grille[depart[0]][depart[1]] == 1 or grille[arrivee[0]][arrivee[1]] == 1:
        return -1
    distance = {depart: 0}
    file = deque([depart])
    while file:
        i, j = file.popleft()
        if (i, j) == arrivee:
            return distance[(i, j)]
        for di, dj in directions:
            a, b = i + di, j + dj
            if 0 <= a < m and 0 <= b < n and grille[a][b] == 0 and (a, b) not in distance:
                distance[(a, b)] = distance[(i, j)] + 1
                file.append((a, b))
    return -1


grille = [[0, 0, 0, 0],
          [1, 1, 0, 1],
          [0, 0, 0, 0],
          [0, 1, 1, 0]]
print(plus_court_chemin_grille(grille, (0, 0), (3, 3)))              # 6
print(plus_court_chemin_grille(grille, (0, 0), (3, 3), huit=True))   # 4
```

Complexité O(m · n).

**Exercice 19.2.5**

Orange pourrie : dans une grille, certaines oranges sont pourries et contaminent leurs voisines chaque minute. En combien de minutes toutes les oranges sont-elles pourries (ou `-1`) ? *(BFS multi-sources)*

**Correction**

BFS **multi-sources** : on place toutes les oranges pourries dans la file au départ (à l'instant 0), puis on propage minute par minute.

```python
from collections import deque


def oranges_pourries(grille):
    m, n = len(grille), len(grille[0])
    file, frais = deque(), 0
    for i in range(m):
        for j in range(n):
            if grille[i][j] == 2:
                file.append((i, j, 0))
            elif grille[i][j] == 1:
                frais += 1
    minutes = 0
    while file:
        i, j, minutes = file.popleft()
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            a, b = i + di, j + dj
            if 0 <= a < m and 0 <= b < n and grille[a][b] == 1:
                grille[a][b] = 2
                frais -= 1
                file.append((a, b, minutes + 1))
    return -1 if frais > 0 else minutes


print(oranges_pourries([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))   # 4
print(oranges_pourries([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))   # -1 (une orange isolée)
print(oranges_pourries([[0, 2]]))                            # 0
```

Complexité O(m · n). (Valeurs : 0 = vide, 1 = orange fraîche, 2 = orange pourrie.)

**Exercice 19.2.6**

Échelle de mots : transformez un mot en un autre en changeant une lettre à la fois, chaque mot intermédiaire devant appartenir à un dictionnaire. Trouvez la plus courte séquence.

**Correction**

Les mots sont les sommets ; deux mots sont voisins s'ils diffèrent d'une lettre. Le plus court chemin en nombre de mots se trouve par BFS.

```python
from collections import deque


def echelle_de_mots(debut, fin, dictionnaire):
    mots = set(dictionnaire)
    if fin not in mots:
        return []
    parent = {debut: None}
    file = deque([debut])
    while file:
        u = file.popleft()
        if u == fin:
            chemin = []
            while u is not None:
                chemin.append(u)
                u = parent[u]
            return chemin[::-1]
        for i in range(len(u)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                v = u[:i] + c + u[i + 1:]
                if v in mots and v not in parent:
                    parent[v] = u
                    file.append(v)
    return []


print(echelle_de_mots("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
# ['hit', 'hot', 'dot', 'dog', 'cog']
```

Complexité O(N · L · 26) pour `N` mots de longueur `L` (chaque mot teste ses `26 L` variantes en O(L)).

## 19.3 Parcours en profondeur (DFS)

**Exercice 19.3.1**

Déroulez à la main un DFS depuis le sommet 0 sur le graphe de l'exercice 19.1.1, avec les voisins parcourus dans l'ordre croissant. Notez l'ordre de visite.

**Correction**

DFS depuis 0, voisins dans l'ordre croissant :

1. visite 0 (voisins `1, 2`) ; on descend dans 1 ;
2. visite 1 (voisins `0, 2, 3`) : 0 est déjà visité, on descend dans 2 ;
3. visite 2 (voisins `0, 1`) : tous visités, retour à 1 ;
4. retour dans 1, on descend dans 3 ;
5. visite 3 (voisins `1, 4`) : on descend dans 4 ;
6. visite 4 (voisin 3 visité) : retour, retour, retour.

Ordre de visite : `0, 1, 2, 3, 4`.

**Exercice 19.3.2**

Écrivez `dfs_recursif` et `dfs_iteratif` (avec une pile explicite). Pourquoi la version itérative est-elle préférable pour un graphe de 10⁶ sommets en Python ?

**Correction**

```python
def dfs_recursif(graphe, source):
    visite, ordre = set(), []

    def explorer(u):
        visite.add(u)
        ordre.append(u)
        for v in graphe[u]:
            if v not in visite:
                explorer(v)

    explorer(source)
    return ordre


def dfs_iteratif(graphe, source):
    visite, ordre = set(), []
    pile = [source]
    while pile:
        u = pile.pop()
        if u in visite:
            continue
        visite.add(u)
        ordre.append(u)
        for v in reversed(graphe[u]):          # pour respecter l'ordre des voisins
            if v not in visite:
                pile.append(v)
    return ordre


print(dfs_recursif(g, 0), dfs_iteratif(g, 0))   # [0, 1, 2, 3, 4] [0, 1, 2, 3, 4]
```

Pour un graphe de 10⁶ sommets, la version **récursive** peut atteindre une profondeur de 10⁶ (par exemple un chemin) : elle dépasse la limite de récursion de Python (1000 par défaut) et peut faire planter l'interpréteur si on la relève. La version **itérative** utilise une pile explicite sur le tas, limitée seulement par la mémoire.

**Exercice 19.3.3**

Écrivez `composantes_connexes(graphe)` qui renvoie la liste des composantes d'un graphe non orienté.

**Correction**

```python
def composantes_connexes(graphe):
    vu = [False] * len(graphe)
    composantes = []
    for depart in range(len(graphe)):
        if not vu[depart]:
            composante, pile = [], [depart]
            vu[depart] = True
            while pile:
                u = pile.pop()
                composante.append(u)
                for v in graphe[u]:
                    if not vu[v]:
                        vu[v] = True
                        pile.append(v)
            composantes.append(sorted(composante))
    return composantes


print(composantes_connexes(construire_graphe(6, [(0, 1), (1, 2), (3, 4)])))
# [[0, 1, 2], [3, 4], [5]]
```

Complexité O(n + m).

### Applications

**Exercice 19.3.4**

Nombre d'îles : dans une grille de `'1'` (terre) et `'0'` (eau), comptez les îles. Calculez aussi l'aire de la plus grande.

**Correction**

On parcourt la grille ; à chaque case de terre non visitée on lance un DFS qui marque toute l'île et compte sa surface.

```python
def iles(grille):
    m, n = len(grille), len(grille[0])
    vu = [[False] * n for _ in range(m)]
    nombre, plus_grande = 0, 0
    for i in range(m):
        for j in range(n):
            if grille[i][j] == "1" and not vu[i][j]:
                nombre += 1
                aire, pile = 0, [(i, j)]
                vu[i][j] = True
                while pile:
                    a, b = pile.pop()
                    aire += 1
                    for da, db in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        x, y = a + da, b + db
                        if 0 <= x < m and 0 <= y < n and grille[x][y] == "1" and not vu[x][y]:
                            vu[x][y] = True
                            pile.append((x, y))
                plus_grande = max(plus_grande, aire)
    return nombre, plus_grande


print(iles([list("11000"), list("11000"), list("00100"), list("00011")]))   # (3, 4)
```

Il y a 3 îles, et la plus grande a une aire de 4. Complexité O(m · n).

**Exercice 19.3.5**

Détection de cycle dans un graphe non orienté, puis dans un graphe orienté (trois états : non visité, en cours, terminé).

**Correction**

**Graphe non orienté** : un cycle existe si le DFS rencontre un sommet déjà visité qui n'est **pas le parent** du sommet courant.

```python
def cycle_non_oriente(graphe):
    vu = set()

    def explorer(u, parent):
        vu.add(u)
        for v in graphe[u]:
            if v == parent:
                continue
            if v in vu or explorer(v, u):
                return True
        return False

    return any(s not in vu and explorer(s, -1) for s in range(len(graphe)))
```

**Graphe orienté** : trois états (0 = non visité, 1 = en cours, 2 = terminé). Un arc vers un sommet **en cours** révèle un cycle (arc arrière).

```python
def cycle_oriente(graphe):
    etat = [0] * len(graphe)

    def explorer(u):
        etat[u] = 1
        for v in graphe[u]:
            if etat[v] == 1:
                return True                   # arc arrière
            if etat[v] == 0 and explorer(v):
                return True
        etat[u] = 2
        return False

    return any(etat[s] == 0 and explorer(s) for s in range(len(graphe)))


print(cycle_non_oriente(g))                                                   # True (0-1-2)
print(cycle_non_oriente(construire_graphe(4, [(0, 1), (1, 2), (2, 3)])))      # False
print(cycle_oriente(construire_graphe(3, [(0, 1), (1, 2), (2, 0)], True)))    # True
print(cycle_oriente(construire_graphe(3, [(0, 1), (1, 2), (0, 2)], True)))    # False
```

Les deux sont en O(n + m). (Dans un graphe orienté, tester seulement « déjà visité » est insuffisant : un sommet déjà terminé n'implique pas de cycle.)

**Exercice 19.3.6**

Test de bipartition : écrivez `est_biparti(graphe)` par coloration à deux couleurs avec DFS ou BFS.

**Correction**

Un graphe est biparti si ses sommets peuvent être colorés avec 2 couleurs sans que deux voisins aient la même couleur (de façon équivalente : il n'a aucun cycle de longueur impaire).

```python
from collections import deque


def est_biparti(graphe):
    couleur = [-1] * len(graphe)
    for depart in range(len(graphe)):
        if couleur[depart] != -1:
            continue
        couleur[depart] = 0
        file = deque([depart])
        while file:
            u = file.popleft()
            for v in graphe[u]:
                if couleur[v] == -1:
                    couleur[v] = 1 - couleur[u]
                    file.append(v)
                elif couleur[v] == couleur[u]:
                    return False
    return True


print(est_biparti(g))                                                           # False (triangle 0-1-2)
print(est_biparti(construire_graphe(4, [(0, 1), (1, 2), (2, 3), (3, 0)])))      # True (cycle de longueur 4)
```

Complexité O(n + m).

**Exercice 19.3.7**

Trouvez tous les chemins entre deux sommets d'un DAG.

**Correction**

Dans un DAG, il n'y a pas de cycle : un DFS avec retour sur trace suffit, sans marquage des sommets visités.

```python
def tous_les_chemins(dag, source, cible):
    resultat, chemin = [], [source]

    def explorer(u):
        if u == cible:
            resultat.append(chemin[:])
            return
        for v in dag[u]:
            chemin.append(v)
            explorer(v)
            chemin.pop()

    explorer(source)
    return resultat


dag_exemple = construire_graphe(4, [(0, 1), (0, 2), (1, 3), (2, 3), (1, 2)], oriente=True)
print(tous_les_chemins(dag_exemple, 0, 3))
# [[0, 1, 3], [0, 1, 2, 3], [0, 2, 3]]
```

Le nombre de chemins peut être exponentiel (jusqu'à `2ⁿ⁻²`), donc le temps l'est aussi dans le pire cas.

**Exercice 19.3.8**

Clonage de graphe : écrivez une fonction qui copie en profondeur un graphe représenté par des nœuds avec une liste de voisins.

**Correction**

```python
class NoeudGraphe:
    def __init__(self, valeur, voisins=None):
        self.valeur = valeur
        self.voisins = voisins or []


def cloner_graphe(noeud):
    if noeud is None:
        return None
    copies = {}                                  # original -> copie

    def copier(u):
        if u in copies:
            return copies[u]                     # déjà copié : évite les boucles infinies
        copie = NoeudGraphe(u.valeur)
        copies[u] = copie
        for v in u.voisins:
            copie.voisins.append(copier(v))
        return copie

    return copier(noeud)


a, b, c = NoeudGraphe(1), NoeudGraphe(2), NoeudGraphe(3)
a.voisins, b.voisins, c.voisins = [b, c], [a], [a]
copie = cloner_graphe(a)
print(copie is not a, [x.valeur for x in copie.voisins], copie.voisins[0].voisins[0] is copie)
# True [2, 3] True
```

Le dictionnaire `copies` garantit qu'un nœud n'est copié qu'une fois, même dans un graphe avec cycles. Complexité O(n + m).

## 19.4 Tri topologique (graphes orientés acycliques)

**Exercice 19.4.1**

Donnez deux tris topologiques valides pour le DAG d'arêtes `5→2, 5→0, 4→0, 4→1, 2→3, 3→1` (6 sommets).

**Correction**

Arêtes `5→2, 5→0, 4→0, 4→1, 2→3, 3→1`. Un tri topologique place chaque sommet avant tous ses successeurs. Deux ordres valides :

- `[4, 5, 0, 2, 3, 1]` ;
- `[5, 4, 2, 0, 3, 1]` (ou encore `[5, 2, 3, 4, 0, 1]`).

Vérification pour le premier : `5` avant `2` et `0` ; `4` avant `0` et `1` ; `2` avant `3` ; `3` avant `1`.

**Exercice 19.4.2**

Implémentez le tri topologique de deux manières : par DFS (ordre inverse des sorties) et par l'algorithme de Kahn (degrés entrants).

**Correction**

```python
from collections import deque


def tri_topologique_dfs(graphe):
    etat = [0] * len(graphe)
    sortie = []

    def explorer(u):
        etat[u] = 1
        for v in graphe[u]:
            if etat[v] == 1:
                raise ValueError("le graphe contient un cycle")
            if etat[v] == 0:
                explorer(v)
        etat[u] = 2
        sortie.append(u)                         # ajouté après tous ses successeurs

    for s in range(len(graphe)):
        if etat[s] == 0:
            explorer(s)
    return sortie[::-1]                          # ordre inverse des sorties


def tri_topologique_kahn(graphe):
    n = len(graphe)
    entrants = [0] * n
    for u in range(n):
        for v in graphe[u]:
            entrants[v] += 1
    file = deque(i for i in range(n) if entrants[i] == 0)
    ordre = []
    while file:
        u = file.popleft()
        ordre.append(u)
        for v in graphe[u]:
            entrants[v] -= 1
            if entrants[v] == 0:
                file.append(v)
    return ordre if len(ordre) == n else None    # None : cycle


dag = construire_graphe(6, [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)], oriente=True)
print(tri_topologique_dfs(dag))     # [5, 4, 2, 3, 1, 0]
print(tri_topologique_kahn(dag))    # [4, 5, 2, 0, 3, 1]
```

Les deux sont en O(n + m) et fournissent des ordres différents, tous valides.

**Exercice 19.4.3**

Cours à suivre : `n` cours, des prérequis `(a, b)` signifiant « suivre `b` avant `a` ». Déterminez s'il est possible de tous les suivre, et dans quel ordre.

**Correction**

On construit une arête `b → a` pour chaque prérequis `(a, b)` ; on peut tout suivre si et seulement si le graphe est acyclique, et un tri topologique donne un ordre.

```python
def ordre_des_cours(n, prerequis):
    graphe = [[] for _ in range(n)]
    for a, b in prerequis:
        graphe[b].append(a)                      # b avant a
    return tri_topologique_kahn(graphe)


print(ordre_des_cours(4, [(1, 0), (2, 0), (3, 1), (3, 2)]))   # [0, 1, 2, 3]
print(ordre_des_cours(2, [(1, 0), (0, 1)]))                   # None (cycle : impossible)
```

Complexité O(n + m).

**Exercice 19.4.4**

Comment détecter un cycle avec l'algorithme de Kahn ? Quelle est la complexité ?

**Correction**

Dans l'algorithme de Kahn, on retire à chaque étape un sommet de degré entrant 0. Si le graphe contient un cycle, aucun sommet du cycle ne devient jamais de degré entrant nul : il **reste des sommets non traités** à la fin. La détection est donc : **le nombre de sommets extraits est strictement inférieur à `n`**.

Complexité : **O(n + m)** (chaque sommet entre une fois dans la file et chaque arête est examinée une fois).

**Exercice 19.4.5**

Ordre alphabétique d'un langage extraterrestre : étant donné une liste de mots triés dans cet ordre, reconstituez un ordre possible de l'alphabet. *(défi)*

**Correction**

Pour deux mots consécutifs de la liste, la **première lettre différente** donne une contrainte `x avant y`. On construit un graphe de contraintes sur les lettres, puis on le trie topologiquement. Cas particulier : si un mot est suivi de l'un de ses propres préfixes (plus court), la liste est invalide.

```python
from collections import defaultdict, deque


def ordre_alphabet(mots):
    successeurs = defaultdict(set)
    entrants = {c: 0 for mot in mots for c in mot}
    for a, b in zip(mots, mots[1:]):
        for x, y in zip(a, b):
            if x != y:
                if y not in successeurs[x]:
                    successeurs[x].add(y)
                    entrants[y] += 1
                break
        else:
            if len(a) > len(b):                  # "abc" avant "ab" : impossible
                return ""
    file = deque(c for c in entrants if entrants[c] == 0)
    ordre = []
    while file:
        u = file.popleft()
        ordre.append(u)
        for v in successeurs[u]:
            entrants[v] -= 1
            if entrants[v] == 0:
                file.append(v)
    return "".join(ordre) if len(ordre) == len(entrants) else ""


print(ordre_alphabet(["wrt", "wrf", "er", "ett", "rftt"]))   # wertf
print(ordre_alphabet(["z", "x", "z"]))                       # "" (contradiction)
```

Complexité O(C + L) où `C` est le nombre total de caractères et `L` le nombre de lettres distinctes ; l'ordre n'est pas unique en général.

## 19.5 Arbre couvrant de poids minimal (MST)

### Union-Find (ensembles disjoints)

**Exercice 19.5.1**

Implémentez la structure `UnionFind` avec compression de chemins et union par rang (`trouver`, `unir`, `meme_ensemble`). Déroulez-la à la main pour les unions `(0,1), (2,3), (1,3), (4,5)` sur 6 éléments.

**Correction**

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rang = [0] * n
        self.nombre = n                          # nombre d'ensembles

    def trouver(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]     # compression de chemin
            x = self.parent[x]
        return x

    def unir(self, a, b):
        a, b = self.trouver(a), self.trouver(b)
        if a == b:
            return False
        if self.rang[a] < self.rang[b]:                      # union par rang
            a, b = b, a
        self.parent[b] = a
        if self.rang[a] == self.rang[b]:
            self.rang[a] += 1
        self.nombre -= 1
        return True

    def meme_ensemble(self, a, b):
        return self.trouver(a) == self.trouver(b)
```

Déroulement à la main sur 6 éléments (au départ `parent = [0, 1, 2, 3, 4, 5]`, `rang = [0, 0, 0, 0, 0, 0]`) :

| Union | Racines | Action | `parent` | `rang` |
| --- | --- | --- | --- | --- |
| `(0, 1)` | 0 et 1 (rangs égaux) | 1 sous 0, `rang[0] = 1` | `[0, 0, 2, 3, 4, 5]` | `[1, 0, 0, 0, 0, 0]` |
| `(2, 3)` | 2 et 3 | 3 sous 2, `rang[2] = 1` | `[0, 0, 2, 2, 4, 5]` | `[1, 0, 1, 0, 0, 0]` |
| `(1, 3)` | racines 0 et 2 (rangs égaux) | 2 sous 0, `rang[0] = 2` | `[0, 0, 0, 2, 4, 5]` | `[2, 0, 1, 0, 0, 0]` |
| `(4, 5)` | 4 et 5 | 5 sous 4, `rang[4] = 1` | `[0, 0, 0, 2, 4, 4]` | `[2, 0, 1, 0, 1, 0]` |

À la fin il reste 2 ensembles : `{0, 1, 2, 3}` et `{4, 5}`. Un appel `trouver(3)` compresserait ensuite le chemin `3 → 2 → 0` en `3 → 0`. Les opérations coûtent O(α(n)) amorti (quasi constant).

**Exercice 19.5.2**

Utilisez-la pour compter les composantes connexes d'un graphe donné par une liste d'arêtes, puis pour détecter la première arête qui crée un cycle.

**Correction**

```python
def nombre_composantes(n, aretes):
    uf = UnionFind(n)
    for a, b in aretes:
        uf.unir(a, b)
    return uf.nombre


def premiere_arete_cyclique(n, aretes):
    uf = UnionFind(n)
    for a, b in aretes:
        if not uf.unir(a, b):                    # déjà dans le même ensemble : cycle
            return (a, b)
    return None


print(nombre_composantes(6, [(0, 1), (1, 2), (3, 4)]))                    # 3
print(premiere_arete_cyclique(4, [(0, 1), (1, 2), (2, 3), (3, 0)]))       # (3, 0)
```

Les deux sont en O(m · α(n)), soit quasi linéaire.

**Exercice 19.5.3**

Comptage d'îles dynamique : des cases de terre sont ajoutées une à une dans une grille ; après chaque ajout, donnez le nombre d'îles avec Union-Find. *(défi)*

**Correction**

On ajoute chaque case de terre comme une nouvelle île (nombre + 1), puis on l'unit à ses voisines déjà terre ; chaque union **réussie** fusionne deux îles (nombre − 1).

```python
def iles_dynamiques(m, n, positions):
    uf = UnionFind(m * n)
    terre, resultat, nombre = set(), [], 0
    for i, j in positions:
        if (i, j) in terre:                       # case déjà ajoutée
            resultat.append(nombre)
            continue
        terre.add((i, j))
        nombre += 1
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            a, b = i + di, j + dj
            if (a, b) in terre and uf.unir(i * n + j, a * n + b):
                nombre -= 1
        resultat.append(nombre)
    return resultat


print(iles_dynamiques(3, 3, [(0, 0), (0, 1), (1, 2), (2, 1), (1, 1)]))
# [1, 1, 2, 3, 1]
```

Complexité O(k · α(m·n)) pour `k` ajouts, bien meilleure que de recompter à chaque fois en O(k · m · n).

### Algorithme de Kruskal (glouton, trie les arêtes)

**Exercice 19.5.4**

Appliquez Kruskal à la main au graphe pondéré d'arêtes `(A,B,4), (A,C,3), (B,C,1), (B,D,2), (C,D,4), (C,E,2), (D,E,3)` : notez l'ordre d'examen et le poids total de l'arbre.

**Correction**

Arêtes triées par poids (en conservant l'ordre d'apparition pour les égalités) :
`(B,C,1), (B,D,2), (C,E,2), (A,C,3), (D,E,3), (A,B,4), (C,D,4)`.

| Ordre | Arête | Décision | Justification |
| --- | --- | --- | --- |
| 1 | `B–C` (1) | **acceptée** | B et C étaient dans des ensembles distincts |
| 2 | `B–D` (2) | **acceptée** | D relié au composant `{B, C}` |
| 3 | `C–E` (2) | **acceptée** | E relié au composant `{B, C, D}` |
| 4 | `A–C` (3) | **acceptée** | A relié au composant `{B, C, D, E}` |
| 5 | `D–E` (3) | rejetée | D et E déjà connectés (cycle) |
| 6 | `A–B` (4) | rejetée | cycle |
| 7 | `C–D` (4) | rejetée | cycle |

Arbre couvrant : `B–C, B–D, C–E, A–C`, de poids total **8** (1 + 2 + 2 + 3), avec 4 arêtes pour 5 sommets.

**Exercice 19.5.5**

Implémentez `kruskal(n, aretes)`. Quelle est la complexité ? Que renvoie-t-il si le graphe n'est pas connexe ?

**Correction**

```python
def kruskal(n, aretes):
    uf = UnionFind(n)
    arbre, poids_total = [], 0
    for u, v, poids in sorted(aretes, key=lambda a: a[2]):
        if uf.unir(u, v):
            arbre.append((u, v, poids))
            poids_total += poids
    return poids_total, arbre


indice = {c: i for i, c in enumerate("ABCDE")}
aretes = [(indice[a], indice[b], w) for a, b, w in
          [("A", "B", 4), ("A", "C", 3), ("B", "C", 1), ("B", "D", 2),
           ("C", "D", 4), ("C", "E", 2), ("D", "E", 3)]]
print(kruskal(5, aretes))
# (8, [(1, 2, 1), (1, 3, 2), (2, 4, 2), (0, 2, 3)])
```

Complexité : **O(m log m)** (tri des arêtes), soit O(m log n), les opérations Union-Find étant quasi constantes. Si le graphe n'est **pas connexe**, Kruskal renvoie une **forêt couvrante minimale** (un arbre couvrant minimal par composante) : le nombre d'arêtes retenues est inférieur à `n − 1`, ce qui permet de détecter l'absence de connexité.

### Algorithme de Prim (glouton, fait grossir un arbre)

**Exercice 19.5.6**

Appliquez Prim à la main au même graphe, en partant de `A`.

**Correction**

Prim depuis `A` : on fait grossir l'arbre en ajoutant à chaque étape l'arête de poids minimal reliant l'arbre à un sommet extérieur.

| Étape | Arbre | Arêtes candidates (vers l'extérieur) | Choix |
| --- | --- | --- | --- |
| 1 | `{A}` | `A–B (4)`, `A–C (3)` | `A–C (3)` |
| 2 | `{A, C}` | `A–B (4)`, `C–B (1)`, `C–D (4)`, `C–E (2)` | `C–B (1)` |
| 3 | `{A, B, C}` | `B–D (2)`, `C–D (4)`, `C–E (2)` | `B–D (2)` |
| 4 | `{A, B, C, D}` | `C–E (2)`, `D–E (3)` | `C–E (2)` |

Arbre : `A–C, C–B, B–D, C–E`, de poids **8** : le même poids que Kruskal (les arbres couvrants minimaux peuvent différer quand il y a des égalités, mais pas leur poids).

**Exercice 19.5.7**

Implémentez `prim(graphe)` avec un tas. Quand préférer Prim à Kruskal ?

**Correction**

```python
import heapq


def prim(graphe):
    """graphe : liste d'adjacence pondérée [(voisin, poids)]. Renvoie (poids, arêtes) ou None."""
    n = len(graphe)
    visite = [False] * n
    tas = [(0, 0, -1)]                           # (poids, sommet, parent)
    total, arbre = 0, []
    while tas:
        poids, u, parent = heapq.heappop(tas)
        if visite[u]:
            continue
        visite[u] = True
        total += poids
        if parent >= 0:
            arbre.append((parent, u, poids))
        for v, w in graphe[u]:
            if not visite[v]:
                heapq.heappush(tas, (w, v, u))
    return (total, arbre) if len(arbre) == n - 1 else None   # None : graphe non connexe


gp = construire_graphe(5, aretes)
print(prim(gp))   # (8, [(0, 2, 3), (2, 1, 1), (1, 3, 2), (2, 4, 2)])
```

Complexité **O(m log n)** avec un tas binaire. Prim est préférable à Kruskal pour les graphes **denses** (avec une version en tableau, il est en O(n²), ce qui bat O(m log m) quand `m ≈ n²`), ou quand le graphe est donné par une liste d'adjacence ou implicite (sans liste d'arêtes triable). Kruskal est plus simple quand on dispose déjà d'une liste d'arêtes et que le graphe est peu dense.

**Exercice 19.5.8**

Réseau de connexions : étant donné des points du plan, reliez-les tous au coût minimal (distance de Manhattan). Comment modéliser ? Quelle complexité ?

**Correction**

**Modélisation** : chaque point est un sommet, et chaque paire de points est reliée par une arête de poids égal à la distance de Manhattan `|x₁ − x₂| + |y₁ − y₂|` : c'est un graphe **complet**. On cherche son arbre couvrant minimal.

```python
def reseau_cout_minimal(points):
    n = len(points)
    distance = [float("inf")] * n
    visite = [False] * n
    distance[0] = 0
    total = 0
    for _ in range(n):
        u = min((i for i in range(n) if not visite[i]), key=lambda i: distance[i])
        visite[u] = True
        total += distance[u]
        for v in range(n):
            if not visite[v]:
                w = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                if w < distance[v]:
                    distance[v] = w
    return total


print(reseau_cout_minimal([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))   # 20
```

Complexité : Prim en version « tableau » est en **O(n²)** et mémoire O(n) (sans construire les `n(n − 1)/2` arêtes). Avec Kruskal, il faudrait générer et trier `O(n²)` arêtes, soit O(n² log n).

## 19.6 Exercices recommandés

**Exercice 19.6.1**

Résolvez les cinq problèmes suivants et donnez pour chacun l'algorithme choisi et sa complexité : nombre d'îles, cours à suivre (tri topologique), clonage de graphe, plus court chemin dans une grille, réseau de connexions au coût minimal (MST).

**Correction**

| Problème | Algorithme choisi | Complexité |
| --- | --- | --- |
| Nombre d'îles | parcours (DFS ou BFS) de la grille, ou Union-Find | O(m · n) |
| Cours à suivre | tri topologique (algorithme de Kahn ou DFS à trois états) | O(n + m) |
| Clonage de graphe | DFS ou BFS avec un dictionnaire original → copie | O(n + m) |
| Plus court chemin dans une grille | BFS (grille non pondérée) | O(m · n) |
| Réseau de connexions au coût minimal | arbre couvrant minimal : Prim en O(n²) (graphe complet) ou Kruskal | O(n²) (Prim) ou O(n² log n) (Kruskal) |

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

**Correction**

| Situation | Algorithme |
| --- | --- |
| 1. Graphe non pondéré, source unique | **BFS** (O(n + m)) |
| 2. Poids positifs, source unique | **Dijkstra** (O((n + m) log n)) |
| 3. Poids pouvant être négatifs, source unique | **Bellman-Ford** (O(n · m)) |
| 4. Toutes les paires, petit graphe (`n ≤ 400`) | **Floyd-Warshall** (O(n³)) |
| 5. Poids égaux à 0 ou 1 | **BFS 0-1** avec une deque (O(n + m)) |
| 6. Graphe orienté acyclique pondéré | **Programmation dynamique sur DAG** : tri topologique puis relaxation (O(n + m), poids négatifs permis) |
| 7. Détection d'un cycle de poids négatif | **Bellman-Ford** (une `n`-ième passe qui améliore encore une distance), ou Floyd-Warshall (diagonale négative) |

## 20.2 Dijkstra

**Exercice 20.2.1**

Déroulez à la main Dijkstra depuis `A` sur le graphe orienté `A→B (7), A→C (9), A→F (14), B→C (10), B→D (15), C→D (11), C→F (2), D→E (6), F→E (9)`. Notez le tableau des distances et l'ordre d'extraction.

**Correction**

Graphe orienté : `A→B (7), A→C (9), A→F (14), B→C (10), B→D (15), C→D (11), C→F (2), D→E (6), F→E (9)`.

| Étape | Sommet extrait (distance) | A | B | C | D | E | F |
| --- | --- | --- | --- | --- | --- | --- | --- |
| initial | | 0 | ∞ | ∞ | ∞ | ∞ | ∞ |
| 1 | A (0) | 0 | 7 | 9 | ∞ | ∞ | 14 |
| 2 | B (7) | 0 | 7 | 9 | 22 | ∞ | 14 |
| 3 | C (9) | 0 | 7 | 9 | 20 | ∞ | 11 |
| 4 | F (11) | 0 | 7 | 9 | 20 | 20 | 11 |
| 5 | D (20) | 0 | 7 | 9 | 20 | 20 | 11 |
| 6 | E (20) | 0 | 7 | 9 | 20 | 20 | 11 |

Détail : à l'étape 2, `B → C` donnerait `17 > 9` (inchangé) et `B → D` donne `22` ; à l'étape 3, `C → D` donne `20 < 22` et `C → F` donne `11 < 14` ; à l'étape 4, `F → E` donne `20` ; à l'étape 5, `D → E` donnerait `26 > 20`.

Ordre d'extraction : `A (0), B (7), C (9), F (11), D (20), E (20)` (D et E sont à égalité).

**Exercice 20.2.2**

Implémentez `dijkstra(graphe, source)` avec `heapq` et gestion des entrées obsolètes. Quelle est la complexité ?

**Correction**

```python
import heapq
from math import inf


def dijkstra(graphe, source):
    """graphe : dict sommet -> liste de (voisin, poids). Renvoie (distances, parents)."""
    dist = {u: inf for u in graphe}
    dist[source] = 0
    parent = {source: None}
    tas = [(0, source)]
    while tas:
        d, u = heapq.heappop(tas)
        if d > dist[u]:                       # entrée obsolète : une meilleure existe déjà
            continue
        for v, poids in graphe[u]:
            if d + poids < dist[v]:
                dist[v] = d + poids
                parent[v] = u
                heapq.heappush(tas, (dist[v], v))
    return dist, parent


G = {"A": [("B", 7), ("C", 9), ("F", 14)], "B": [("C", 10), ("D", 15)],
     "C": [("D", 11), ("F", 2)], "D": [("E", 6)], "E": [], "F": [("E", 9)]}
dist, parent = dijkstra(G, "A")
print(dist)   # {'A': 0, 'B': 7, 'C': 9, 'D': 20, 'E': 20, 'F': 11}
```

Les entrées **obsolètes** sont celles qui restent dans le tas après qu'une meilleure distance a été trouvée (`heapq` ne permet pas de diminuer une clé) : on les ignore à l'extraction avec le test `d > dist[u]`.

Complexité : au plus `m` insertions dans un tas de taille O(m), soit **O((n + m) log n)** (en notant `log m ≤ 2 log n`).

**Exercice 20.2.3**

Reconstituez le plus court chemin de `A` à `E` avec un tableau des prédécesseurs.

**Correction**

Le tableau des prédécesseurs `parent` est rempli lors des relaxations ; on remonte depuis la cible.

```python
def chemin(parent, source, cible):
    if cible not in parent:
        return None                            # inaccessible
    resultat = [cible]
    while resultat[-1] != source:
        resultat.append(parent[resultat[-1]])
    return resultat[::-1]


print(chemin(parent, "A", "E"), dist["E"])   # ['A', 'C', 'F', 'E'] 20
```

Le plus court chemin de `A` à `E` est `A → C → F → E` (9 + 2 + 9 = 20), de longueur 20 (le chemin `A → C → D → E` vaut aussi 9 + 11 + 6 = 26 : plus long).

**Exercice 20.2.4**

Donnez un contre-exemple (petit graphe avec une arête négative) pour lequel Dijkstra renvoie une distance fausse. Expliquez quelle hypothèse de la preuve est violée.

**Correction**

Graphe : `A→B (2)`, `A→C (3)`, `C→B (−2)`. Le plus court chemin de `A` à `B` est `A → C → B`, de longueur `3 − 2 = 1`.

Dijkstra (avec des sommets « définitifs ») extrait d'abord `A`, fixe `B = 2` et `C = 3`, puis extrait `B` (distance 2, déclarée définitive). Il extrait ensuite `C` mais ne peut plus modifier `B` : il renvoie `B = 2` au lieu de **1**.

```python
def dijkstra_sommets_figes(graphe, source):
    dist = {u: inf for u in graphe}
    dist[source] = 0
    figes, tas = set(), [(0, source)]
    while tas:
        d, u = heapq.heappop(tas)
        if u in figes:
            continue
        figes.add(u)
        for v, w in graphe[u]:
            if v not in figes and d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(tas, (d + w, v))
    return dist


print(dijkstra_sommets_figes({"A": [("B", 2), ("C", 3)], "B": [], "C": [("B", -2)]}, "A"))
# {'A': 0, 'B': 2, 'C': 3}   (B devrait valoir 1)
```

**Hypothèse violée** : la preuve de Dijkstra affirme que, lorsqu'un sommet est extrait avec la plus petite distance provisoire `d`, aucun autre chemin ne peut être plus court, car tout chemin passant par un sommet non encore extrait a une distance au moins `d` et **ne peut que grandir** en ajoutant des arêtes de poids positif. Avec une arête négative, un détour par un sommet de distance plus élevée peut devenir plus court. (La variante à « entrées obsolètes » sans sommets figés peut parfois retomber sur la bonne réponse, mais elle perd sa complexité : elle peut devenir exponentielle.)

**Exercice 20.2.5**

Fiabilité de réseau : dans un réseau, la probabilité qu'un message passe par une arête est donnée ; trouvez le chemin de probabilité maximale entre deux nœuds. Comment se ramener à un plus court chemin ?

**Correction**

La fiabilité d'un chemin est le **produit** des probabilités de ses arêtes ; on cherche à le **maximiser**. Comme `log` est croissante et `log(p₁ p₂ ...) = Σ log pᵢ`, maximiser le produit revient à maximiser `Σ log pᵢ`, soit à **minimiser `Σ (−log pᵢ)`**. Chaque poids `−log p` est positif (car `0 < p ≤ 1`) : Dijkstra s'applique. On retrouve la probabilité par `exp(−distance)`.

```python
import math


def fiabilite_maximale(n, aretes, source, cible):
    graphe = [[] for _ in range(n)]
    for u, v, p in aretes:
        graphe[u].append((v, -math.log(p)))
        graphe[v].append((u, -math.log(p)))
    dist = [math.inf] * n
    dist[source] = 0
    tas = [(0, source)]
    while tas:
        d, u = heapq.heappop(tas)
        if d > dist[u]:
            continue
        for v, w in graphe[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(tas, (dist[v], v))
    return math.exp(-dist[cible])


print(round(fiabilite_maximale(3, [(0, 1, 0.9), (1, 2, 0.9), (0, 2, 0.7)], 0, 2), 4))
# 0.81 (le chemin 0 → 1 → 2 : 0,9 × 0,9 = 0,81 > 0,7)
```

(On peut aussi appliquer directement Dijkstra avec un tas-max sur le produit, car multiplier par `p ≤ 1` ne peut que diminuer la fiabilité.)

**Exercice 20.2.6**

Délai de propagation : étant donnés des temps de transmission entre nœuds, calculez le temps nécessaire pour qu'un signal émis depuis un nœud atteigne tous les autres.

**Correction**

Le signal atteint un nœud au bout du plus court chemin depuis la source ; il atteint **tous** les nœuds au bout du **maximum** des plus courtes distances (si un nœud est inaccessible, la réponse est `-1`).

```python
def delai_propagation(temps, n, source):
    """temps : liste de (u, v, t) avec des nœuds numérotés de 1 à n."""
    graphe = [[] for _ in range(n + 1)]
    for u, v, t in temps:
        graphe[u].append((v, t))
    dist = [math.inf] * (n + 1)
    dist[source] = 0
    tas = [(0, source)]
    while tas:
        d, u = heapq.heappop(tas)
        if d > dist[u]:
            continue
        for v, t in graphe[u]:
            if d + t < dist[v]:
                dist[v] = d + t
                heapq.heappush(tas, (dist[v], v))
    pire = max(dist[1:])
    return -1 if pire == math.inf else pire


print(delai_propagation([(2, 1, 1), (2, 3, 1), (3, 4, 1)], 4, 2))   # 2
print(delai_propagation([(1, 2, 1)], 2, 2))                          # -1 (le nœud 1 est inaccessible)
```

Complexité O((n + m) log n).

## 20.3 Bellman-Ford

**Exercice 20.3.1**

Déroulez Bellman-Ford à la main sur le graphe d'arêtes `S→A (4), S→B (5), A→B (−3), B→C (4), A→C (6)`.

**Correction**

Graphe : `S→A (4), S→B (5), A→B (−3), B→C (4), A→C (6)`, avec 4 sommets : au plus `n − 1 = 3` passes. Départ : `dist = {S: 0, A: ∞, B: ∞, C: ∞}`.

**Passe 1** (arêtes dans l'ordre donné) :

| Arête | Calcul | Résultat |
| --- | --- | --- |
| `S→A (4)` | `0 + 4 = 4 < ∞` | `A = 4` |
| `S→B (5)` | `0 + 5 = 5 < ∞` | `B = 5` |
| `A→B (−3)` | `4 − 3 = 1 < 5` | `B = 1` |
| `B→C (4)` | `1 + 4 = 5 < ∞` | `C = 5` |
| `A→C (6)` | `4 + 6 = 10 > 5` | inchangé |

Après la passe 1 : `S = 0, A = 4, B = 1, C = 5`.

**Passe 2** : aucune arête ne produit d'amélioration (`S→B : 5 > 1`, `A→B : 1`, `B→C : 5`, `A→C : 10`). On s'arrête.

Distances finales : `A = 4`, `B = 1` (via `S → A → B`, plus court que l'arête directe de poids 5), `C = 5` (via `S → A → B → C`).

**Exercice 20.3.2**

Implémentez `bellman_ford(n, aretes, source)` avec détection de cycle de poids négatif. Quelle est la complexité ?

**Correction**

```python
from math import inf


def bellman_ford(n, aretes, source):
    """aretes : liste de (u, v, poids). Renvoie (distances, cycle_negatif)."""
    dist = [inf] * n
    dist[source] = 0
    for _ in range(n - 1):
        modifie = False
        for u, v, w in aretes:
            if dist[u] != inf and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                modifie = True
        if not modifie:                       # arrêt anticipé
            break
    cycle_negatif = any(dist[u] != inf and dist[u] + w < dist[v] for u, v, w in aretes)
    return dist, cycle_negatif


S, A, B, C = 0, 1, 2, 3
aretes = [(S, A, 4), (S, B, 5), (A, B, -3), (B, C, 4), (A, C, 6)]
print(bellman_ford(4, aretes, S))                                    # ([0, 4, 1, 5], False)
print(bellman_ford(3, [(0, 1, 1), (1, 2, -3), (2, 1, 1)], 0))        # ([0, -3, -4], True)
```

La détection : si une `n`-ième passe améliore encore une distance, il existe un cycle de poids négatif accessible depuis la source. Complexité **O(n · m)** (au plus `n` passes sur les `m` arêtes).

**Exercice 20.3.3**

Montrez qu'il suffit de `n − 1` relaxations de toutes les arêtes pour obtenir les distances en l'absence de cycle négatif.

**Correction**

Sans cycle de poids négatif, un plus court chemin est **simple** (sans sommet répété : supprimer un cycle de poids ≥ 0 ne l'allonge pas), donc il contient au plus `n − 1` arêtes.

**Récurrence** : après la passe `i`, `dist[v] ≤` (poids du plus court chemin de la source à `v` utilisant **au plus `i` arêtes**).
- Pour `i = 0` : `dist[source] = 0` et les autres valent `∞` : vrai.
- Si c'est vrai après la passe `i − 1`, soit `P` un plus court chemin de la source à `v` d'au plus `i` arêtes, et `u → v` sa dernière arête : le sous-chemin jusqu'à `u` a au plus `i − 1` arêtes, donc `dist[u] ≤ poids(P) − w(u, v)` avant la passe `i`. La relaxation de `u → v` lors de la passe `i` garantit `dist[v] ≤ dist[u] + w(u, v) ≤ poids(P)`.

Après `n − 1` passes, `dist[v]` est donc au plus le poids du plus court chemin (au plus `n − 1` arêtes), et il ne peut pas être plus petit (on ne produit que des poids de chemins réels) : c'est la distance exacte.

**Exercice 20.3.4**

Arbitrage de devises : étant donné des taux de change, détectez une suite d'échanges qui augmente le capital. Montrez que cela équivaut à chercher un cycle négatif (avec des logarithmes). *(défi)*

**Correction**

Un cycle d'échanges `c₀ → c₁ → ... → c₀` multiplie le capital par `r₁ × r₂ × ... × r_k`. Il y a arbitrage si ce produit est **> 1**. En prenant le logarithme : `Σ log rᵢ > 0`, soit `Σ (−log rᵢ) < 0`. Il suffit donc de donner à chaque arête le poids `−log r` : un arbitrage correspond exactement à un **cycle de poids négatif**.

```python
import math


def arbitrage(n, taux):
    """taux : liste de (devise_source, devise_cible, taux)."""
    aretes = [(u, v, -math.log(r)) for u, v, r in taux]
    dist = [0.0] * n                         # source virtuelle reliée à tous (poids 0)
    for _ in range(n - 1):
        for u, v, w in aretes:
            if dist[u] + w < dist[v] - 1e-12:
                dist[v] = dist[u] + w
    return any(dist[u] + w < dist[v] - 1e-12 for u, v, w in aretes)


print(arbitrage(3, [(0, 1, 0.9), (1, 2, 0.9), (2, 0, 1.3)]))   # True  (0,9 × 0,9 × 1,3 = 1,053)
print(arbitrage(3, [(0, 1, 0.9), (1, 2, 0.9), (2, 0, 1.2)]))   # False (0,972 < 1)
```

On initialise toutes les distances à 0 (équivalent à une source virtuelle reliée à toutes les devises), de sorte que tout cycle négatif est détecté. La tolérance `1e-12` évite les faux positifs liés aux arrondis flottants. Complexité O(n · m).

**Exercice 20.3.5**

Prix le moins cher avec au plus `k` escales : modifiez Bellman-Ford pour limiter le nombre d'arêtes du chemin.

**Correction**

On limite le nombre d'arêtes du chemin à `k + 1` (pour `k` escales) en effectuant **exactement `k + 1` passes**, chacune partant d'une **copie** du tableau précédent : ainsi chaque passe étend les chemins d'**une seule arête**.

```python
def prix_minimal(n, vols, depart, arrivee, k):
    dist = [inf] * n
    dist[depart] = 0
    for _ in range(k + 1):
        nouveau = dist[:]                          # on lit l'ancien, on écrit le nouveau
        for u, v, prix in vols:
            if dist[u] != inf and dist[u] + prix < nouveau[v]:
                nouveau[v] = dist[u] + prix
        dist = nouveau
    return -1 if dist[arrivee] == inf else dist[arrivee]


vols = [(0, 1, 100), (1, 2, 100), (2, 0, 100), (1, 3, 600), (2, 3, 200)]
print(prix_minimal(4, vols, 0, 3, 1))   # 700 (0 → 1 → 3)
print(prix_minimal(4, vols, 0, 3, 2))   # 400 (0 → 1 → 2 → 3)
print(prix_minimal(4, vols, 0, 3, 0))   # -1  (aucun vol direct)
```

Sans la copie, une même passe pourrait enchaîner plusieurs arêtes, et la limite sur le nombre d'escales ne serait plus respectée. Complexité O(k · m).

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

**Correction**

Matrice initiale (`∞` = pas d'arête) :

```text
      0   1   2   3
  0   0   5   ∞  10
  1   ∞   0   3   ∞
  2   ∞   ∞   0   1
  3   ∞   ∞   ∞   0
```

On teste, pour chaque `k`, si passer par `k` améliore `d[i][j]`.

- **`k = 0`** : personne n'a d'arc entrant vers 0 (colonne 0 : `∞`), aucune amélioration.
- **`k = 1`** : seul `0` atteint `1` (distance 5). `d[0][2] = 5 + 3 = 8 < ∞` : mise à jour. `d[0][3]` : `5 + ∞`, inchangé.
- **`k = 2`** : `0` (distance 8) et `1` (distance 3) atteignent 2, et `2 → 3` vaut 1. `d[0][3] = min(10, 8 + 1) = 9` ; `d[1][3] = 3 + 1 = 4`.
- **`k = 3`** : le sommet 3 n'a aucun arc sortant : aucune amélioration.

Matrice finale :

```text
      0   1   2   3
  0   0   5   8   9
  1   ∞   0   3   4
  2   ∞   ∞   0   1
  3   ∞   ∞   ∞   0
```

**Exercice 20.4.2**

Implémentez `floyd_warshall(distances)`. Pourquoi l'ordre des trois boucles est-il important (l'indice intermédiaire `k` doit être la boucle extérieure) ?

**Correction**

```python
from math import inf


def floyd_warshall(distances):
    n = len(distances)
    d = [ligne[:] for ligne in distances]
    for k in range(n):                       # sommet intermédiaire : boucle EXTÉRIEURE
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    return d


M = [[0, 5, inf, 10], [inf, 0, 3, inf], [inf, inf, 0, 1], [inf, inf, inf, 0]]
for ligne in floyd_warshall(M):
    print(ligne)
```

Complexité O(n³) en temps, O(n²) en espace (on peut travailler sur place).

**Pourquoi `k` doit être la boucle extérieure** : l'invariant est « après le traitement de `k`, `d[i][j]` est la longueur du plus court chemin dont les sommets intermédiaires sont dans `{0, ..., k}` ». La mise à jour utilise `d[i][k]` et `d[k][j]`, qui doivent déjà valoir leurs distances avec intermédiaires dans `{0, ..., k − 1}` **pour toutes** les paires. Si `k` est la boucle intérieure, on utilise des valeurs `d[i][k]` et `d[k][j]` pas encore finalisées, et chaque paire `(i, j)` n'est considérée qu'une fois : des chemins sont manqués.

Contre-exemple avec l'ordre `i, j, k` : graphe à 4 sommets avec les arcs `1→3`, `3→2`, `2→0` (poids 1). Le chemin `1 → 3 → 2 → 0` a pour longueur 3. En traitant la ligne `i = 1`, la colonne `j = 0` est examinée **avant** `j = 2` : `d[1][2]` (qui vaut 2 via 3) n'est pas encore calculé, et `d[1][0]` reste `∞`. Avec `k` à l'extérieur, `d[1][0] = 3` est correctement trouvé.

**Exercice 20.4.3**

Adaptez-le pour calculer la fermeture transitive d'un graphe (existence d'un chemin entre toutes les paires).

**Correction**

C'est l'**algorithme de Warshall** : on remplace `min` et `+` par `ou` et `et` sur des booléens.

```python
def fermeture_transitive(adjacence):
    n = len(adjacence)
    atteint = [[bool(adjacence[i][j]) or i == j for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                atteint[i][j] = atteint[i][j] or (atteint[i][k] and atteint[k][j])
    return atteint


print(fermeture_transitive([[0, 1, 0], [0, 0, 1], [0, 0, 0]]))
# [[True, True, True], [False, True, True], [False, False, True]]
```

Complexité O(n³) (ou O(n³ / 64) avec des opérations sur des mots binaires).

**Exercice 20.4.4**

Ville la plus proche : à partir de `n` villes et de routes pondérées, trouvez la ville qui a le moins de voisines à distance `≤ seuil` (en cas d'égalité, le plus grand indice).

**Correction**

On calcule toutes les distances avec Floyd-Warshall, puis, pour chaque ville, on compte les villes à distance `≤ seuil`. On garde la ville de plus petit compte ; en cas d'égalité, la dernière rencontrée (indice le plus grand) grâce à `<=`.

```python
def ville_la_plus_proche(n, routes, seuil):
    d = [[inf] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    for u, v, w in routes:
        d[u][v] = d[v][u] = w
    d = floyd_warshall(d)
    meilleure, minimum = None, inf
    for i in range(n):
        voisines = sum(1 for j in range(n) if j != i and d[i][j] <= seuil)
        if voisines <= minimum:                  # <= : plus grand indice en cas d'égalité
            minimum, meilleure = voisines, i
    return meilleure


print(ville_la_plus_proche(4, [(0, 1, 3), (1, 2, 1), (1, 3, 4), (2, 3, 1)], 4))   # 3
print(ville_la_plus_proche(5, [(0, 1, 2), (0, 4, 8), (1, 2, 3), (1, 4, 2), (2, 3, 1), (3, 4, 1)], 2))   # 0
```

Complexité O(n³).

**Exercice 20.4.5**

Reconstituez les chemins en conservant une matrice des « sommets suivants ».

**Correction**

On conserve une matrice `suivant[i][j]` : le premier sommet à emprunter pour aller de `i` à `j`. Quand passer par `k` améliore `d[i][j]`, on pose `suivant[i][j] = suivant[i][k]`.

```python
def floyd_warshall_chemins(distances):
    n = len(distances)
    d = [ligne[:] for ligne in distances]
    suivant = [[j if d[i][j] != inf and i != j else None for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    suivant[i][j] = suivant[i][k]
    return d, suivant


def reconstituer(suivant, i, j):
    if suivant[i][j] is None and i != j:
        return None                              # pas de chemin
    chemin = [i]
    while i != j:
        i = suivant[i][j]
        chemin.append(i)
    return chemin


d, suivant = floyd_warshall_chemins(M)
print(reconstituer(suivant, 0, 3), d[0][3])   # [0, 1, 2, 3] 9
print(reconstituer(suivant, 3, 0))            # None
```

Un chemin se reconstitue en O(longueur du chemin).

## 20.5 BFS 0-1

**Exercice 20.5.1**

Implémentez `bfs_01(graphe, source)` avec une `deque` : les arêtes de poids 0 sont ajoutées à gauche, celles de poids 1 à droite. Quelle est la complexité ?

**Correction**

```python
from collections import deque


def bfs_01(graphe, source):
    """graphe[u] : liste de (v, w) avec w valant 0 ou 1."""
    dist = [inf] * len(graphe)
    dist[source] = 0
    file = deque([source])
    while file:
        u = file.popleft()
        for v, w in graphe[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if w == 0:
                    file.appendleft(v)            # même distance : en tête de file
                else:
                    file.append(v)                # distance +1 : en queue de file
    return dist


print(bfs_01([[(1, 0), (2, 1)], [(2, 1), (3, 1)], [(3, 0)], []], 0))   # [0, 0, 1, 1]
```

La file reste triée par distance (au plus deux valeurs consécutives à la fois). Complexité **O(n + m)**, meilleure que Dijkstra en O((n + m) log n).

**Exercice 20.5.2**

Dans une grille où certaines cases contiennent des obstacles que l'on peut franchir au coût de 1 (les cases libres coûtant 0), trouvez le nombre minimal d'obstacles à franchir pour aller du coin supérieur gauche au coin inférieur droit.

**Correction**

Entrer dans une case coûte 0 si elle est libre, 1 si c'est un obstacle : c'est un BFS 0-1 sur la grille.

```python
def obstacles_minimum(grille):
    m, n = len(grille), len(grille[0])
    dist = [[inf] * n for _ in range(m)]
    dist[0][0] = grille[0][0]
    file = deque([(0, 0)])
    while file:
        i, j = file.popleft()
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            a, b = i + di, j + dj
            if 0 <= a < m and 0 <= b < n:
                w = grille[a][b]                 # 0 : libre, 1 : obstacle
                if dist[i][j] + w < dist[a][b]:
                    dist[a][b] = dist[i][j] + w
                    if w == 0:
                        file.appendleft((a, b))
                    else:
                        file.append((a, b))
    return dist[-1][-1]


print(obstacles_minimum([[0, 0, 0], [1, 1, 0], [0, 0, 0]]))   # 0 (on contourne par la droite)
print(obstacles_minimum([[0, 1, 1], [1, 1, 0], [1, 1, 0]]))   # 2
```

Complexité O(m · n).

## 20.6 SPFA (Bellman-Ford avec file)

**Exercice 20.6.1**

Implémentez SPFA avec une file et un tableau `dans_la_file`. Comment détecter un cycle négatif ?

**Correction**

SPFA (*Shortest Path Faster Algorithm*) ne retraite que les sommets dont la distance vient d'être améliorée.

```python
def spfa(n, aretes, source):
    graphe = [[] for _ in range(n)]
    for u, v, w in aretes:
        graphe[u].append((v, w))
    dist = [inf] * n
    dist[source] = 0
    dans_la_file = [False] * n
    entrees = [0] * n                             # nombre de fois où chaque sommet est mis en file
    file = deque([source])
    dans_la_file[source] = True
    entrees[source] = 1
    while file:
        u = file.popleft()
        dans_la_file[u] = False
        for v, w in graphe[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if not dans_la_file[v]:
                    entrees[v] += 1
                    if entrees[v] >= n:           # cycle négatif détecté
                        return None
                    file.append(v)
                    dans_la_file[v] = True
    return dist


print(spfa(4, [(0, 1, 4), (0, 2, 5), (1, 2, -3), (2, 3, 4), (1, 3, 6)], 0))   # [0, 4, 1, 5]
print(spfa(3, [(0, 1, 1), (1, 2, -3), (2, 1, 1)], 0))                         # None
```

**Détection d'un cycle négatif** : sans cycle négatif, un sommet n'est mis en file qu'un nombre borné de fois (au plus `n − 1`) ; si un sommet entre `n` fois dans la file (ou si le chemin le plus court trouvé jusqu'à lui contient `n` arêtes), il y a un cycle négatif.

**Exercice 20.6.2**

Quel est son pire cas ? Pourquoi est-il souvent rapide en pratique mais n'offre pas de garantie meilleure que Bellman-Ford ?

**Correction**

Le **pire cas** de SPFA est **O(n · m)**, comme Bellman-Ford : des graphes bien choisis (certaines grilles ou des graphes construits exprès) obligent à réinsérer un très grand nombre de fois les sommets dans la file.

Il est souvent **rapide en pratique** car il ne relaxe que les arêtes sortantes des sommets dont la distance a changé, au lieu de parcourir toutes les arêtes à chaque passe ; sur beaucoup de graphes aléatoires ou creux le comportement observé est proche de O(m). Mais cela ne vient d'aucune garantie théorique : l'ordre FIFO ne contrôle pas le nombre de réinsertions, donc rien n'améliore la borne de Bellman-Ford. Quand les poids sont positifs, Dijkstra est préférable.

## 20.7 A\* *(ajout)*

**Exercice 20.7.1**

Qu'est-ce qu'une heuristique **admissible** ? **cohérente** ? Pourquoi la distance de Manhattan est-elle admissible sur une grille à déplacements dans 4 directions ?

**Correction**

- Une heuristique `h` est **admissible** si elle ne **surestime jamais** le coût réel restant : `h(n) ≤ h*(n)` (coût optimal de `n` à l'objectif). A\* avec une heuristique admissible trouve un chemin optimal.
- Elle est **cohérente** (ou monotone) si, pour toute arête `(u, v)` de poids `w`, `h(u) ≤ w + h(v)` (inégalité triangulaire), et `h(objectif) = 0`. Toute heuristique cohérente est admissible ; avec une heuristique cohérente, A\* n'a jamais besoin de rouvrir un sommet déjà fermé, et `f = g + h` est croissante le long des chemins.

**Manhattan sur une grille à 4 directions** : chaque déplacement modifie **soit** la ligne **soit** la colonne de 1 case, donc il faut au moins `|Δlig| + |Δcol|` déplacements pour atteindre l'objectif, chacun coûtant 1 (au moins) : la distance de Manhattan est inférieure ou égale au coût réel (les obstacles ne peuvent que l'augmenter). Elle est aussi cohérente : un pas fait varier `h` d'au plus 1 = le coût de l'arête.

**Exercice 20.7.2**

Implémentez A\* sur une grille avec la distance de Manhattan. Comparez le nombre de cases explorées avec Dijkstra sur plusieurs grilles aléatoires.

**Correction**

```python
import heapq


def astar(grille, depart, arrivee, h):
    """Renvoie (longueur du chemin, nombre de cases explorées)."""
    m, n = len(grille), len(grille[0])
    dist = {depart: 0}
    tas = [(h(depart), 0, depart)]
    fermes, explorees = set(), 0
    while tas:
        f, d, u = heapq.heappop(tas)
        if u in fermes:
            continue
        fermes.add(u)
        explorees += 1
        if u == arrivee:
            return d, explorees
        i, j = u
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            a, b = i + di, j + dj
            if 0 <= a < m and 0 <= b < n and grille[a][b] == 0:
                nd = d + 1
                if nd < dist.get((a, b), float("inf")):
                    dist[(a, b)] = nd
                    heapq.heappush(tas, (nd + h((a, b)), nd, (a, b)))
    return -1, explorees


def manhattan(arrivee):
    return lambda u: abs(u[0] - arrivee[0]) + abs(u[1] - arrivee[1])
```

Comparaison : `h = lambda u: 0` donne Dijkstra. Sur 30 grilles aléatoires de 50 × 50 avec 20 % d'obstacles (départ en haut à gauche, arrivée en bas à droite), dont 22 admettent un chemin, on a observé en moyenne environ **1 990 cases explorées** pour Dijkstra et environ **1 280** pour A\* avec Manhattan (soit environ 35 % de moins), avec **exactement les mêmes longueurs de chemin**. Le gain augmente avec la taille de la grille et diminue quand il y a beaucoup d'obstacles (l'heuristique est alors moins informative).

**Exercice 20.7.3**

Que devient A\* avec `h = 0` ? Que se passe-t-il avec une heuristique non admissible ?

**Correction**

- Avec **`h = 0`**, `f = g` : A\* se comporte exactement comme **Dijkstra** (exploration dans toutes les directions par distance croissante). L'heuristique nulle est admissible et cohérente, donc le résultat est optimal.
- Avec une heuristique **non admissible** (qui surestime), A\* peut écarter un chemin optimal parce que `f` paraît trop grand : il explore moins de sommets et est plus rapide, mais le chemin renvoyé n'est **plus garanti optimal**. On l'exploite volontairement dans A\* pondéré (`f = g + ε·h`, `ε > 1`), pour échanger de l'optimalité contre de la vitesse.

**Exercice 20.7.4**

Quelle heuristique choisir si les déplacements en diagonale sont autorisés au même coût que les déplacements orthogonaux ? Et avec un coût de `√2` pour la diagonale ?

**Correction**

- **Diagonales au même coût que les déplacements orthogonaux (coût 1)** : chaque pas réduit au mieux `|Δlig|` et `|Δcol|` de 1 simultanément. L'heuristique est la **distance de Tchebychev** : `h = max(|Δlig|, |Δcol|)`.
- **Diagonale de coût `√2`** : l'heuristique est la **distance octile** : on fait `min(|Δlig|, |Δcol|)` diagonales et le reste en lignes droites :

`h = (|Δlig| + |Δcol|) + (√2 − 2) × min(|Δlig|, |Δcol|)`, soit `max + (√2 − 1) × min`.

Manhattan serait **non admissible** dans les deux cas : il surestimerait (une diagonale compte 2 pas pour Manhattan alors qu'elle coûte 1 ou `√2`).

## 20.8 Plus courts chemins dans un DAG

**Exercice 20.8.1**

Écrivez `plus_court_chemin_dag(graphe, source)` : tri topologique puis relaxation dans l'ordre. Quelle est la complexité ? Fonctionne-t-il avec des poids négatifs ?

**Correction**

```python
from collections import deque
from math import inf


def plus_court_chemin_dag(graphe, source):
    """graphe[u] : liste de (v, poids), orienté et acyclique."""
    n = len(graphe)
    entrants = [0] * n
    for u in range(n):
        for v, _ in graphe[u]:
            entrants[v] += 1
    file = deque(i for i in range(n) if entrants[i] == 0)
    ordre = []
    while file:                                    # tri topologique (Kahn)
        u = file.popleft()
        ordre.append(u)
        for v, _ in graphe[u]:
            entrants[v] -= 1
            if entrants[v] == 0:
                file.append(v)
    dist = [inf] * n
    dist[source] = 0
    for u in ordre:                                # relaxation dans l'ordre topologique
        if dist[u] != inf:
            for v, w in graphe[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    return dist


dag = [[(1, 2), (2, 6)], [(2, -3), (3, 5)], [(3, 1)], []]
print(plus_court_chemin_dag(dag, 0))   # [0, 2, -1, 0]
```

Complexité **O(n + m)**. Il fonctionne **avec des poids négatifs** : l'absence de cycle et l'ordre topologique garantissent que, lorsqu'un sommet est traité, tous ses prédécesseurs l'ont été et sa distance est définitive (comme le montre l'arête `1 → 2` de poids `−3` dans l'exemple).

**Exercice 20.8.2**

Écrivez `plus_long_chemin_dag(graphe)` et utilisez-le pour calculer la durée minimale d'un projet dont les tâches ont des durées et des dépendances (chemin critique).

**Correction**

Le plus long chemin s'obtient avec la même méthode en maximisant (relaxation par `max`) ; c'est un problème facile sur un DAG (il est NP-difficile dans un graphe quelconque).

```python
def plus_long_chemin_dag(graphe):
    """Longueur du plus long chemin d'un DAG pondéré (poids sur les arêtes)."""
    n = len(graphe)
    entrants = [0] * n
    for u in range(n):
        for v, _ in graphe[u]:
            entrants[v] += 1
    file = deque(i for i in range(n) if entrants[i] == 0)
    dist = [0] * n
    while file:
        u = file.popleft()
        for v, w in graphe[u]:
            dist[v] = max(dist[v], dist[u] + w)
            entrants[v] -= 1
            if entrants[v] == 0:
                file.append(v)
    return max(dist)
```

**Chemin critique d'un projet** : les durées sont portées par les tâches. Pour chaque tâche, `fin[v] = durée[v] + max(fin[p])` sur ses prédécesseurs `p` (0 s'il n'y en a pas). La durée minimale du projet est `max(fin)`, et le chemin critique est obtenu en remontant les prédécesseurs qui réalisent le maximum.

```python
def duree_projet(durees, dependances):
    """dependances : liste de (a, b) : la tâche a doit être terminée avant b."""
    n = len(durees)
    graphe = [[] for _ in range(n)]
    entrants = [0] * n
    for a, b in dependances:
        graphe[a].append(b)
        entrants[b] += 1
    file = deque(i for i in range(n) if entrants[i] == 0)
    debut, fin, pred = [0] * n, [0] * n, [-1] * n
    for i in file:
        fin[i] = durees[i]
    while file:
        u = file.popleft()
        for v in graphe[u]:
            if fin[u] > debut[v]:
                debut[v], pred[v] = fin[u], u
            entrants[v] -= 1
            if entrants[v] == 0:
                fin[v] = debut[v] + durees[v]
                file.append(v)
    derniere = max(range(n), key=lambda i: fin[i])
    critique, u = [], derniere
    while u != -1:
        critique.append(u)
        u = pred[u]
    return fin[derniere], critique[::-1]


# Tâches A..E de durées 3, 2, 4, 2, 3 ; A et B avant C ; C avant D et E
print(duree_projet([3, 2, 4, 2, 3], [(0, 2), (1, 2), (2, 3), (2, 4)]))
# (10, [0, 2, 4]) : durée 10, chemin critique A → C → E
```

Complexité O(n + m).

## 20.9 Conseils de choix

**Exercice 20.9.1**

Une carte routière comporte 10⁶ sommets et 3 × 10⁶ arêtes pondérées positives, et l'on doit répondre à 10³ requêtes « distance entre deux sommets ». Quel algorithme choisir ? Que changer si l'on a 10⁶ requêtes ?

**Correction**

**Avec 10³ requêtes** : un **Dijkstra** (tas binaire) par requête, avec arrêt dès que la cible est extraite, coûte O((n + m) log n), soit de l'ordre de 4 × 10⁶ × 20 opérations par requête : environ 10⁸ au pire, 10¹¹ au total en Python (trop lent), de l'ordre de quelques minutes en langage compilé. On réduit le travail en utilisant **Dijkstra bidirectionnel** ou **A\*** avec une heuristique (coordonnées géographiques, distance à vol d'oiseau ou points de repère ALT) : seule une petite fraction du graphe est explorée.

**Avec 10⁶ requêtes** : même avec A\*, c'est trop. Il faut **précalculer** : une structure comme les **hiérarchies de contraction** (*contraction hierarchies*), les **étiquettes de concentrateurs** (*hub labeling*) ou les **nœuds de transit**, qui répondent à chaque requête en quelques microsecondes à quelques millisecondes après un précalcul. Floyd-Warshall est exclu (`n³ = 10¹⁸`, et `n² = 10¹²` distances ne tiennent pas en mémoire). Si les requêtes partagent peu de sources distinctes, un Dijkstra complet par source regroupe plusieurs requêtes.

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

**Correction**

| Algorithme | Poids négatifs ? | Complexité | Cas d'usage |
| --- | --- | --- | --- |
| BFS | Non applicable (graphe non pondéré, tous les poids valent 1) | O(n + m) | plus court chemin en nombre d'arêtes, labyrinthes, réseaux sociaux |
| BFS 0-1 | Non (poids 0 ou 1 uniquement) | O(n + m) | grilles avec coûts 0/1, nombre minimal de changements |
| Dijkstra | **Non** (poids ≥ 0) | O((n + m) log n) | routage, GPS, réseaux à poids positifs |
| Bellman-Ford | **Oui** (et détecte les cycles négatifs) | O(n · m) | poids négatifs, arbitrage, limitation du nombre d'arêtes |
| Floyd-Warshall | **Oui** (sans cycle négatif) | O(n³) | toutes les paires pour un petit graphe (`n ≤ 400`), fermeture transitive |
| A\* | Non (poids ≥ 0, heuristique admissible) | dépend de l'heuristique ; au pire comme Dijkstra | une seule paire source-cible avec une bonne heuristique (cartes, jeux, grilles) |

---

# 21. Composantes fortement connexes

## 21.1 Définition

**Exercice 21.1.1**

Définissez « composante fortement connexe ». Pour le graphe orienté `0→1, 1→2, 2→0, 1→3, 3→4, 4→5, 5→3, 6→5, 6→7, 7→6`, listez à la main les composantes fortement connexes.

**Correction**

**Définition** : dans un graphe orienté, une **composante fortement connexe** (CFC) est un ensemble maximal de sommets tel que, pour toute paire `(u, v)` de l'ensemble, il existe un chemin de `u` vers `v` **et** un chemin de `v` vers `u`. Les CFC partitionnent l'ensemble des sommets.

Graphe : `0→1, 1→2, 2→0, 1→3, 3→4, 4→5, 5→3, 6→5, 6→7, 7→6`.

- `0 → 1 → 2 → 0` est un cycle : **`{0, 1, 2}`** est une composante.
- `3 → 4 → 5 → 3` est un cycle : **`{3, 4, 5}`** est une composante.
- `6 → 7 → 6` est un cycle : **`{6, 7}`** est une composante.

Les arcs `1→3`, `6→5` relient des composantes différentes dans un seul sens : on ne peut pas revenir de `{3, 4, 5}` vers `{0, 1, 2}` ni vers `{6, 7}`. Il y a donc **3 composantes** : `{0, 1, 2}`, `{3, 4, 5}`, `{6, 7}`.

**Exercice 21.1.2**

Dessinez le graphe des composantes (condensation) du graphe précédent. Montrez qu'il est toujours acyclique.

**Correction**

**Graphe de condensation** : un sommet par composante, et un arc `C₁ → C₂` s'il existe un arc entre un sommet de `C₁` et un sommet de `C₂`.

```text
{0, 1, 2}  ───(1→3)───►  {3, 4, 5}  ◄───(6→5)───  {6, 7}
```

**Il est toujours acyclique** : supposons un cycle de composantes `C₁ → C₂ → ... → C_k → C₁`. Alors, pour tous sommets `u` de `C_i` et `v` de `C_j`, on peut aller de `u` à `v` en suivant le cycle (en passant à l'intérieur de chaque composante, qui est fortement connexe) et de `v` à `u` de même. Tous ces sommets seraient donc mutuellement accessibles et appartiendraient à une **même** composante, ce qui contredit la maximalité des composantes `C₁, ..., C_k` (supposées distinctes).

### Applications

**Exercice 21.1.3**

Citez trois applications des composantes fortement connexes (par exemple dépendances cycliques entre modules, analyse de liens web, 2-SAT) et décrivez en une phrase ce qu'on y calcule.

**Correction**

1. **Dépendances cycliques entre modules ou paquets** : chaque composante de plus d'un sommet est un groupe de modules qui dépendent circulairement les uns des autres ; on calcule ces groupes pour les détecter et pour déterminer un ordre de compilation de la condensation.
2. **Analyse de liens web** (graphe des pages et des hyperliens) : on calcule les ensembles de pages mutuellement accessibles (le « noyau » fortement connexe du web) pour étudier la structure du réseau et alimenter des classements.
3. **2-SAT** : on construit le graphe des implications entre littéraux ; la formule est satisfaisable si et seulement si aucun littéral n'est dans la même composante que sa négation, et les composantes donnent aussi une affectation.

On peut aussi citer l'analyse de programmes (blocs de code qui s'appellent mutuellement), les chaînes de Markov (classes communicantes) ou le regroupement de comptes dans des réseaux sociaux.

## 21.2 Algorithme de Kosaraju (deux parcours)

**Exercice 21.2.1**

Déroulez Kosaraju à la main sur le graphe de l'exercice 21.1.1 : premier parcours (ordre de fin), graphe transposé, second parcours.

**Correction**

Kosaraju sur `0→1, 1→2, 2→0, 1→3, 3→4, 4→5, 5→3, 6→5, 6→7, 7→6` (voisins parcourus dans l'ordre de la liste, sommets de départ dans l'ordre croissant).

**Premier parcours (DFS sur le graphe d'origine), ordre de fin** :

- DFS depuis 0 : `0 → 1 → 2` ; `2` (voisin 0 déjà visité) finit en premier ; retour dans 1, on explore `3 → 4 → 5` ; `5` (voisin 3 visité) finit, puis `4`, puis `3`, puis `1`, puis `0`.
- DFS depuis 6 (sommet non visité) : `6 → 5` (visité), `6 → 7` ; `7` finit, puis `6`.

Ordre de fin : **`2, 5, 4, 3, 1, 0, 7, 6`**.

**Graphe transposé** (on inverse tous les arcs) :

```text
0 : [2]      1 : [0]      2 : [1]      3 : [1, 5]
4 : [3]      5 : [4, 6]   6 : [7]      7 : [6]
```

**Second parcours** sur le transposé, en prenant les sommets par ordre de fin **décroissant** : `6, 7, 0, 1, 3, 4, 5, 2` :

| Départ | Sommets atteints dans le transposé (non encore visités) | Composante |
| --- | --- | --- |
| 6 | `6 → 7` | **`{6, 7}`** |
| 7 | déjà visité | |
| 0 | `0 → 2 → 1` | **`{0, 1, 2}`** |
| 1 | déjà visité | |
| 3 | `3 → 1` (visité), `3 ← 5` : `5 → 4` (4 → 3 visité), `5 → 6` (visité) | **`{3, 4, 5}`** |
| 4, 5, 2 | déjà visités | |

On obtient les trois composantes `{6, 7}`, `{0, 1, 2}`, `{3, 4, 5}`.

**Exercice 21.2.2**

Implémentez `kosaraju(graphe)` qui renvoie la liste des composantes. Quelle est la complexité ?

**Correction**

```python
def kosaraju(graphe):
    n = len(graphe)

    # 1. Premier parcours : ordre de fin (DFS itératif)
    visite = [False] * n
    fin = []
    for depart in range(n):
        if visite[depart]:
            continue
        visite[depart] = True
        pile = [(depart, iter(graphe[depart]))]
        while pile:
            u, voisins = pile[-1]
            for v in voisins:
                if not visite[v]:
                    visite[v] = True
                    pile.append((v, iter(graphe[v])))
                    break
            else:                                  # tous les voisins explorés
                pile.pop()
                fin.append(u)

    # 2. Graphe transposé
    transpose = [[] for _ in range(n)]
    for u in range(n):
        for v in graphe[u]:
            transpose[v].append(u)

    # 3. Second parcours, par ordre de fin décroissant
    visite = [False] * n
    composantes = []
    for depart in reversed(fin):
        if visite[depart]:
            continue
        visite[depart] = True
        composante, pile = [], [depart]
        while pile:
            u = pile.pop()
            composante.append(u)
            for v in transpose[u]:
                if not visite[v]:
                    visite[v] = True
                    pile.append(v)
        composantes.append(sorted(composante))
    return composantes


aretes = [(0, 1), (1, 2), (2, 0), (1, 3), (3, 4), (4, 5), (5, 3), (6, 5), (6, 7), (7, 6)]
graphe = [[] for _ in range(8)]
for u, v in aretes:
    graphe[u].append(v)
print(kosaraju(graphe))   # [[6, 7], [0, 1, 2], [3, 4, 5]]
```

Complexité : deux parcours et une transposition, soit **O(n + m)** en temps et en espace. Les composantes sont produites dans l'**ordre topologique** du graphe de condensation (sources d'abord).

**Exercice 21.2.3**

Pourquoi le second parcours doit-il être effectué sur le graphe **transposé** et dans l'ordre **décroissant** des temps de fin ?

**Correction**

- **Pourquoi le transposé** : dans le graphe d'origine, un parcours lancé depuis un sommet d'une composante « source » (qui a des arcs vers d'autres composantes) déborderait vers les composantes en aval et les mélangerait. Dans le **transposé**, les arcs entre composantes sont inversés : en démarrant dans une composante « source » de l'original, qui devient un puits dans le transposé, on **ne peut pas en sortir** et l'on visite exactement la composante. Les chemins à l'intérieur d'une composante sont conservés par la transposition (une CFC est identique dans `G` et `Gᵀ`).
- **Pourquoi l'ordre de fin décroissant** : le sommet de plus grand temps de fin appartient à une composante **source** du graphe de condensation (le DFS ne peut avoir terminé ce sommet qu'après avoir exploré tout ce qui est accessible, donc sa composante n'a pas de composante antérieure qui l'atteindrait). En traitant les sommets dans cet ordre, chaque nouveau départ se trouve dans une composante dont toutes les composantes « en aval » dans le transposé (c'est-à-dire en amont dans `G`) sont déjà visitées : le parcours s'arrête aux frontières de la composante.

## 21.3 Algorithme de Tarjan (un seul parcours)

**Exercice 21.3.1**

Déroulez Tarjan sur le graphe de l'exercice 21.1.1 : notez, pour chaque sommet, `indice` et `bas_lien` (low-link), et l'état de la pile.

**Correction**

Tarjan attribue à chaque sommet un `indice` (ordre de découverte) et un `bas_lien` : le plus petit `indice` accessible depuis le sous-arbre de DFS du sommet, par un arc arrière ou transversal vers un sommet **encore sur la pile**. Un sommet est la **racine** d'une composante si `bas_lien = indice`.

Déroulement (DFS depuis 0, puis depuis 6) :

| Événement | Pile après l'événement |
| --- | --- |
| découverte de 0 (`indice` 0) | `[0]` |
| découverte de 1 (`indice` 1) | `[0, 1]` |
| découverte de 2 (`indice` 2) ; l'arc `2→0` : 0 est sur la pile, `bas_lien(2) = 0` | `[0, 1, 2]` |
| 2 terminé (`bas_lien = 0 ≠ 2`, pas une racine) ; `bas_lien(1) = 0` | `[0, 1, 2]` |
| découverte de 3 (`indice` 3), puis 4 (`indice` 4), puis 5 (`indice` 5) | `[0, 1, 2, 3, 4, 5]` |
| arc `5→3` : 3 est sur la pile, `bas_lien(5) = 3` ; 5 terminé, puis 4 terminé (`bas_lien = 3`) | `[0, 1, 2, 3, 4, 5]` |
| 3 terminé : `bas_lien(3) = 3 = indice` : **racine**, on dépile jusqu'à 3 : **`{3, 4, 5}`** | `[0, 1, 2]` |
| 1 terminé (`bas_lien = 0`) puis 0 terminé : `bas_lien(0) = 0 = indice` : **racine**, on dépile : **`{0, 1, 2}`** | `[]` |
| découverte de 6 (`indice` 6) ; l'arc `6→5` ignore 5 (déjà terminé, hors pile) ; découverte de 7 (`indice` 7) | `[6, 7]` |
| arc `7→6` : 6 est sur la pile, `bas_lien(7) = 6` ; 7 terminé (pas racine) | `[6, 7]` |
| 6 terminé : `bas_lien(6) = 6 = indice` : **racine**, on dépile : **`{6, 7}`** | `[]` |

Valeurs finales :

| Sommet | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `indice` | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| `bas_lien` | 0 | 0 | 0 | 3 | 3 | 3 | 6 | 6 |

Les composantes sont produites dans l'ordre `{3, 4, 5}`, `{0, 1, 2}`, `{6, 7}` : **ordre topologique inverse** de la condensation (les puits d'abord).

**Exercice 21.3.2**

Implémentez `tarjan(graphe)`. Quelle est la complexité en temps et en espace ?

**Correction**

```python
import sys


def tarjan(graphe):
    sys.setrecursionlimit(max(10_000, 2 * len(graphe) + 100))
    n = len(graphe)
    indice = [-1] * n
    bas_lien = [0] * n
    sur_la_pile = [False] * n
    pile, composantes = [], []
    compteur = [0]

    def parcourir(u):
        indice[u] = bas_lien[u] = compteur[0]
        compteur[0] += 1
        pile.append(u)
        sur_la_pile[u] = True
        for v in graphe[u]:
            if indice[v] == -1:                       # arc d'arbre
                parcourir(v)
                bas_lien[u] = min(bas_lien[u], bas_lien[v])
            elif sur_la_pile[v]:                      # arc arrière vers la pile
                bas_lien[u] = min(bas_lien[u], indice[v])
        if bas_lien[u] == indice[u]:                  # u est la racine d'une composante
            composante = []
            while True:
                w = pile.pop()
                sur_la_pile[w] = False
                composante.append(w)
                if w == u:
                    break
            composantes.append(sorted(composante))

    for depart in range(n):
        if indice[depart] == -1:
            parcourir(depart)
    return composantes


print(tarjan(graphe))   # [[3, 4, 5], [0, 1, 2], [6, 7]]
```

Complexité : **O(n + m)** en temps (un seul parcours, chaque sommet empilé et dépilé une fois) et **O(n)** en espace pour les tableaux et la pile (plus la pile de récursion de profondeur O(n) ; on peut écrire une version itérative pour les grands graphes, comme pour Kosaraju).

**Exercice 21.3.3**

Quand un sommet est-il la racine d'une composante fortement connexe ? Que contient la pile à ce moment ?

**Correction**

Un sommet `u` est la racine d'une composante fortement connexe lorsque, à la fin de son exploration, **`bas_lien[u] == indice[u]`** : aucun sommet de son sous-arbre de DFS n'a d'arc vers un sommet découvert avant lui et encore sur la pile, donc `u` est le premier sommet découvert de sa composante.

À ce moment, la **pile** contient, au-dessus de `u` (jusqu'au sommet de la pile) et y compris `u`, **exactement les sommets de la composante de `u`** : tous ceux qui ont été découverts depuis `u`, qui sont encore sur la pile (donc non encore assignés à une composante) et qui sont dans le sous-arbre de `u`. On dépile jusqu'à `u` pour former la composante. Les sommets sous `u` dans la pile appartiennent à des composantes en cours, découvertes avant `u`.

## 21.4 Kosaraju ou Tarjan ?

**Exercice 21.4.1**

Comparez les deux algorithmes (nombre de parcours, graphe transposé, ordre des composantes produites, simplicité de l'implémentation).

**Correction**

| Critère | Kosaraju | Tarjan |
| --- | --- | --- |
| **Nombre de parcours** | 2 (un sur `G`, un sur `Gᵀ`) | 1 |
| **Graphe transposé** | oui : il faut le construire (mémoire et temps supplémentaires) | non |
| **Ordre des composantes** | ordre topologique de la condensation (sources d'abord) | ordre topologique **inverse** (puits d'abord) |
| **Simplicité** | conceptuellement simple (deux DFS) ; implémentation courte | plus subtile (indices, `bas_lien`, pile et test d'appartenance à la pile) |
| **Complexité** | O(n + m) | O(n + m), avec une constante plus petite |

Les deux sont corrects et linéaires. Kosaraju est plus facile à justifier ; Tarjan est plus économe (un seul parcours, pas de transposée).

**Exercice 21.4.2**

Étant donné un graphe orienté, déterminez le nombre minimal d'arcs à ajouter pour le rendre fortement connexe (à partir du graphe de condensation : sources et puits). *(défi)*

**Correction**

On calcule le graphe de condensation (un DAG). On compte ses **sources** (composantes sans arc entrant) `s` et ses **puits** (sans arc sortant) `p`. S'il n'y a qu'une composante, la réponse est 0 ; sinon la réponse est **`max(s, p)`**.

**Pourquoi** : chaque source a besoin d'un arc entrant et chaque puits d'un arc sortant ; un arc ajouté peut supprimer au plus une source et un puits, donc il faut au moins `max(s, p)` arcs. Réciproquement, il existe toujours une façon d'ajouter exactement `max(s, p)` arcs qui rend le graphe fortement connexe (théorème d'Eswaran et Tarjan).

```python
def arcs_a_ajouter(graphe):
    composantes = tarjan(graphe)
    if len(composantes) == 1:
        return 0
    numero = {}
    for i, comp in enumerate(composantes):
        for sommet in comp:
            numero[sommet] = i
    k = len(composantes)
    entrants, sortants = [0] * k, [0] * k
    for u in range(len(graphe)):
        for v in graphe[u]:
            if numero[u] != numero[v]:
                sortants[numero[u]] += 1
                entrants[numero[v]] += 1
    sources = sum(1 for c in range(k) if entrants[c] == 0)
    puits = sum(1 for c in range(k) if sortants[c] == 0)
    return max(sources, puits)


print(arcs_a_ajouter(graphe))   # 2
```

Pour le graphe de l'exercice 21.1.1 : les sources sont `{0, 1, 2}` et `{6, 7}` (`s = 2`) et le seul puits est `{3, 4, 5}` (`p = 1`) : il faut **2 arcs**. Par exemple `3 → 6` (le puits vers une source) et `7 → 0` (une source vers l'autre) : on obtient le cycle de composantes `{0, 1, 2} → {3, 4, 5} → {6, 7} → {0, 1, 2}`, fortement connexe. Complexité O(n + m).

---

# 22. Flots dans les réseaux

## 22.1 Définition

**Exercice 22.1.1**

On donne le réseau `s→a (10), s→b (5), a→b (15), a→t (5), b→t (10)` et le flot `s→a : 8, s→b : 3, a→b : 3, a→t : 5, b→t : 6`. Vérifiez les deux contraintes (capacité et conservation du flot) et calculez la valeur du flot.

**Correction**

Réseau : `s→a (10), s→b (5), a→b (15), a→t (5), b→t (10)`. Flot : `s→a : 8, s→b : 3, a→b : 3, a→t : 5, b→t : 6`.

**Contrainte de capacité** (`0 ≤ f(e) ≤ c(e)`) :

| Arc | Flot | Capacité | OK ? |
| --- | --- | --- | --- |
| `s→a` | 8 | 10 | oui |
| `s→b` | 3 | 5 | oui |
| `a→b` | 3 | 15 | oui |
| `a→t` | 5 | 5 | oui (saturé) |
| `b→t` | 6 | 10 | oui |

**Conservation du flot** (entrant = sortant pour les sommets autres que `s` et `t`) :

- sommet `a` : entrant `8`, sortant `3 + 5 = 8` : oui ;
- sommet `b` : entrant `3 + 3 = 6`, sortant `6` : oui.

Le flot est donc valide. **Valeur du flot** = flot sortant de `s` = `8 + 3 = ` **11** (égal au flot entrant dans `t` : `5 + 6 = 11`).

**Exercice 22.1.2**

Donnez la définition d'une **coupe** `(S, T)` et de sa capacité. Calculez la capacité de la coupe `S = {s, a}` dans le réseau précédent.

**Correction**

Une **coupe** `(S, T)` d'un réseau est une partition des sommets en deux ensembles avec `s ∈ S` et `t ∈ T`. Sa **capacité** est la somme des capacités des arcs qui vont de `S` vers `T` (les arcs de `T` vers `S` ne comptent pas).

Pour `S = {s, a}` et `T = {b, t}` : les arcs de `S` vers `T` sont `s→b (5)`, `a→b (15)` et `a→t (5)`, d'où une capacité de `5 + 15 + 5 = ` **25**.

(Le flot maximal de ce réseau vaut 15, égal à la capacité de la coupe `S = {s}` : `10 + 5`.)

**Exercice 22.1.3**

Énoncez le théorème flot maximal / coupe minimale.

**Correction**

**Théorème flot maximal / coupe minimale** : dans un réseau, la valeur d'un flot maximal est égale à la capacité d'une coupe minimale. Plus précisément, pour tout flot `f` et toute coupe `(S, T)`, `valeur(f) ≤ capacité(S, T)`, et le maximum du flot égale le minimum de la capacité. Par ailleurs, un flot est maximal si et seulement s'il n'existe aucun chemin augmentant dans son réseau résiduel.

## 22.2 Réseau résiduel et arêtes inverses

**Exercice 22.2.1**

Construisez le réseau résiduel pour le flot de l'exercice 22.1.1. Trouvez un chemin augmentant s'il en existe un.

**Correction**

Pour chaque arc `(u, v)` de capacité `c` et de flot `f`, le réseau résiduel contient l'arc `u→v` de capacité résiduelle `c − f` (s'il est strictement positif) et l'arc inverse `v→u` de capacité `f` (s'il est strictement positif).

| Arc d'origine (flot / capacité) | Arc résiduel avant | Arc résiduel inverse |
| --- | --- | --- |
| `s→a` (8 / 10) | `s→a : 2` | `a→s : 8` |
| `s→b` (3 / 5) | `s→b : 2` | `b→s : 3` |
| `a→b` (3 / 15) | `a→b : 12` | `b→a : 3` |
| `a→t` (5 / 5) | aucun (saturé) | `t→a : 5` |
| `b→t` (6 / 10) | `b→t : 4` | `t→b : 6` |

**Chemin augmentant** : `s → a → b → t` de capacités résiduelles `2, 12, 4`, de goulot **2** : on augmente le flot à `11 + 2 = 13`. Il reste ensuite `s→b : 2` et `b→t : 2` : le chemin `s → b → t` apporte 2 de plus, soit **15** au total, qui est le flot maximal (coupe `S = {s}` de capacité 15).

**Exercice 22.2.2**

Pourquoi faut-il ajouter des arêtes inverses ? Donnez un exemple de réseau où un algorithme glouton sans arêtes inverses est bloqué sur un flot non maximal.

**Correction**

Les **arêtes inverses** permettent d'**annuler** (en partie) un flot déjà envoyé : sans elles, une mauvaise décision prise au début ne pourrait jamais être corrigée.

Exemple : `s→a (1), s→b (1), a→b (1), a→t (1), b→t (1)` ; le flot maximal vaut 2 (`s → a → t` et `s → b → t`).

- Un algorithme glouton choisit d'abord le chemin `s → a → b → t` et envoie 1. Les arcs `s→a`, `a→b` et `b→t` sont saturés.
- Il reste `s→b` (libre) et `a→t` (libre), mais `b` n'a plus de sortie et `a` n'est plus atteint depuis `s` : **plus aucun chemin** de `s` à `t`. Il s'arrête sur un flot de valeur 1, non maximal.
- Avec les arêtes inverses, le réseau résiduel contient `b→a` (capacité 1, qui annule le flux de `a→b`) : le chemin `s → b → a → t` est augmentant et porte le flot à 2.

## 22.3 Ford-Fulkerson et Edmonds-Karp

**Exercice 22.3.1**

Appliquez Edmonds-Karp à la main à `s→a (16), s→c (13), a→b (12), a→c (10), c→a (4), c→d (14), b→c (9), b→t (20), d→b (7), d→t (4)`. Notez chaque chemin augmentant (par BFS) et la valeur du flot après chacun.

**Correction**

Réseau : `s→a (16), s→c (13), a→b (12), a→c (10), c→a (4), c→d (14), b→c (9), b→t (20), d→b (7), d→t (4)`. À chaque étape, le BFS cherche un plus court chemin (en nombre d'arcs) dans le réseau résiduel, en parcourant les voisins dans l'ordre donné.

| Itération | Chemin augmentant | Goulot | Valeur du flot |
| --- | --- | --- | --- |
| 1 | `s → a → b → t` (capacités `16, 12, 20`) | 12 | **12** |
| 2 | `s → c → d → t` (capacités `13, 14, 4`) | 4 | **16** |
| 3 | `s → c → d → b → t` (résiduels `9, 10, 7, 8`) | 7 | **23** |

Après l'itération 3, plus aucun chemin n'existe : le flot maximal vaut **23**.

**Exercice 22.3.2**

Implémentez Edmonds-Karp avec une liste d'adjacence d'arêtes et d'arêtes inverses. Quelle est sa complexité ? Pourquoi Ford-Fulkerson avec DFS peut-il être mal comporté sur des capacités irrationnelles ou très grandes ?

**Correction**

```python
from collections import deque


class Reseau:
    """Réseau de flot : chaque arête est stockée avec son arête inverse (indices e et e ^ 1)."""

    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]      # adj[u] : indices d'arêtes sortantes
        self.vers = []                          # vers[e] : extrémité de l'arête e
        self.cap = []                           # cap[e] : capacité résiduelle de l'arête e

    def ajouter(self, u, v, capacite):
        self.adj[u].append(len(self.vers))
        self.vers.append(v)
        self.cap.append(capacite)
        self.adj[v].append(len(self.vers))      # arête inverse, de capacité 0
        self.vers.append(u)
        self.cap.append(0)

    def edmonds_karp(self, source, puits):
        flot = 0
        while True:
            parent = [-1] * self.n              # arête utilisée pour atteindre chaque sommet
            parent[source] = -2
            file = deque([source])
            while file and parent[puits] == -1:
                u = file.popleft()
                for e in self.adj[u]:
                    v = self.vers[e]
                    if self.cap[e] > 0 and parent[v] == -1:
                        parent[v] = e
                        file.append(v)
            if parent[puits] == -1:
                return flot                      # plus de chemin augmentant
            goulot, v = float("inf"), puits
            while v != source:
                e = parent[v]
                goulot = min(goulot, self.cap[e])
                v = self.vers[e ^ 1]
            v = puits
            while v != source:
                e = parent[v]
                self.cap[e] -= goulot
                self.cap[e ^ 1] += goulot
                v = self.vers[e ^ 1]
            flot += goulot


noms = ["s", "a", "b", "c", "d", "t"]
idx = {c: i for i, c in enumerate(noms)}
aretes = [("s", "a", 16), ("s", "c", 13), ("a", "b", 12), ("a", "c", 10), ("c", "a", 4),
          ("c", "d", 14), ("b", "c", 9), ("b", "t", 20), ("d", "b", 7), ("d", "t", 4)]
reseau = Reseau(6)
for u, v, c in aretes:
    reseau.ajouter(idx[u], idx[v], c)
print(reseau.edmonds_karp(idx["s"], idx["t"]))   # 23
```

**Complexité d'Edmonds-Karp** : **O(V · E²)** : chaque augmentation coûte O(E) (BFS), et le nombre d'augmentations est au plus `O(V · E)` car la distance de `s` à tout sommet dans le réseau résiduel ne diminue jamais et chaque arête est critique (saturée) au plus `V/2` fois.

**Ford-Fulkerson avec DFS** choisit un chemin quelconque : avec des capacités entières, le nombre d'augmentations peut atteindre la **valeur du flot** (pseudo-polynomial, voir l'exercice suivant) ; avec des capacités **irrationnelles**, la méthode peut ne **jamais terminer** et même converger vers une valeur qui n'est pas le flot maximal (exemple de Zwick, où les augmentations successives diminuent comme les puissances du nombre d'or). Avec de très grandes capacités entières (10⁹), un mauvais choix de chemins peut demander jusqu'à 2 × 10⁹ augmentations.

**Exercice 22.3.3**

Construisez un petit réseau de 4 sommets sur lequel Ford-Fulkerson avec un mauvais choix de chemins nécessite de très nombreuses itérations (capacités de 1000 autour d'une arête de capacité 1).

**Correction**

Réseau à 4 sommets : `s→a (1000), s→b (1000), a→b (1), a→t (1000), b→t (1000)`. Le flot maximal vaut 2000 (`s→a→t` : 1000 et `s→b→t` : 1000).

Ford-Fulkerson avec un **mauvais choix** de chemins alterne :

1. chemin `s → a → b → t` (goulot 1, à cause de `a→b`) : flot 1 ;
2. chemin `s → b → a → t`, qui utilise l'arête inverse `b→a` (capacité résiduelle 1) : le goulot est encore 1 : flot 2 ;
3. de nouveau `s → a → b → t` (la capacité `a→b` a été restituée par l'annulation) : flot 3, et ainsi de suite.

Chaque augmentation n'ajoute que **1** : il faut **2000 itérations** au lieu de 2 pour un choix judicieux (`s → a → t` puis `s → b → t`). Avec des capacités de `10⁹` au lieu de 1000, on aurait `2 × 10⁹` itérations. Edmonds-Karp (BFS) choisit d'abord les chemins de 2 arcs `s → a → t` et `s → b → t` et termine en 2 augmentations.

## 22.4 Dinic

**Exercice 22.4.1**

Construisez à la main le graphe de niveaux (BFS) puis un flot bloquant pour le réseau de l'exercice 22.3.1.

**Correction**

Pour le réseau de l'exercice 22.3.1, le **graphe de niveaux** est obtenu par BFS depuis `s` (niveau = nombre minimal d'arcs) : `s : 0`, `a : 1`, `c : 1`, `b : 2`, `d : 2`, `t : 3`.

On ne garde que les arcs qui vont du niveau `k` au niveau `k + 1` : `s→a`, `s→c`, `a→b`, `c→d`, `b→t`, `d→t`. (Les arcs `a→c`, `c→a` (même niveau), `b→c` et `d→b` (niveau décroissant ou égal) sont écartés.)

**Flot bloquant** (phase 1) :

- chemin `s → a → b → t` : goulot `min(16, 12, 20) = 12`, d'où 12 ;
- chemin `s → c → d → t` : goulot `min(13, 14, 4) = 4`, d'où 4 ;
- il ne reste aucun chemin dans le graphe de niveaux : `a→b` est saturé (le chemin par `a` est bloqué) et `d→t` est saturé (le chemin par `d` est bloqué).

Flot bloquant de valeur **16**. En phase 2, le BFS dans le réseau résiduel donne `s : 0`, `a : 1` (capacité 4), `c : 1` (capacité 9), `d : 2` (`c→d` : 10), `b : 3` (`d→b : 7`), `t : 4` (`b→t : 8`) ; le chemin `s → c → d → b → t` a un goulot de **7** : flot total `16 + 7 = 23`. La phase 3 ne trouve plus de chemin vers `t` : le flot maximal est **23**.

**Exercice 22.4.2**

Implémentez Dinic avec BFS de niveaux et DFS avec pointeurs d'arêtes courantes. Quel rôle joue le pointeur « courant » ?

**Correction**

```python
class ReseauDinic(Reseau):
    def dinic(self, source, puits):
        flot = 0
        while True:
            # 1. BFS : niveaux dans le réseau résiduel
            niveau = [-1] * self.n
            niveau[source] = 0
            file = deque([source])
            while file:
                u = file.popleft()
                for e in self.adj[u]:
                    v = self.vers[e]
                    if self.cap[e] > 0 and niveau[v] < 0:
                        niveau[v] = niveau[u] + 1
                        file.append(v)
            if niveau[puits] < 0:
                return flot
            # 2. Flot bloquant : DFS avec pointeur d'arête courante
            courant = [0] * self.n

            def dfs(u, pousse):
                if u == puits:
                    return pousse
                while courant[u] < len(self.adj[u]):
                    e = self.adj[u][courant[u]]
                    v = self.vers[e]
                    if self.cap[e] > 0 and niveau[v] == niveau[u] + 1:
                        d = dfs(v, min(pousse, self.cap[e]))
                        if d > 0:
                            self.cap[e] -= d
                            self.cap[e ^ 1] += d
                            return d
                    courant[u] += 1               # cette arête est inutile pour cette phase
                return 0

            while True:
                d = dfs(source, float("inf"))
                if d == 0:
                    break
                flot += d


r = ReseauDinic(6)
for u, v, c in aretes:
    r.ajouter(idx[u], idx[v], c)
print(r.dinic(idx["s"], idx["t"]))   # 23
```

**Rôle du pointeur courant** (`courant[u]`) : il mémorise la prochaine arête de `u` à essayer. Quand une arête est saturée, ou mène à un cul-de-sac (aucun chemin vers `t` dans le graphe de niveaux), on avance le pointeur et l'on **ne la réexamine plus jamais** pendant la phase. Chaque arête n'est ainsi parcourue qu'un nombre borné de fois : un flot bloquant coûte **O(V · E)** au lieu d'un nombre exponentiel de tentatives redondantes. Le nombre de phases est au plus `V − 1` (la distance `s`–`t` augmente strictement à chaque phase), d'où **O(V² · E)** au total.

**Exercice 22.4.3**

Comparez expérimentalement Edmonds-Karp et Dinic sur des réseaux aléatoires de taille croissante.

**Correction**

Protocole : générer des réseaux (aléatoires, ou en grille avec une source à gauche et un puits à droite), copier le même réseau dans les deux algorithmes, vérifier que les valeurs de flot sont identiques, et chronométrer.

```python
import random
import time


def reseau_grille(L, C, cmax):
    n = L * C + 2
    s, t = L * C, L * C + 1
    aretes = []
    for i in range(L):
        aretes.append((s, i * C, random.randint(1, cmax)))
        aretes.append((i * C + C - 1, t, random.randint(1, cmax)))
        for j in range(C):
            u = i * C + j
            if j + 1 < C:
                aretes.append((u, u + 1, random.randint(1, cmax)))
            if i + 1 < L:
                aretes.append((u, u + C, random.randint(1, cmax)))
                aretes.append((u + C, u, random.randint(1, cmax)))
    return n, aretes, s, t


for L in (10, 20, 30, 40):
    n, ar, s, t = reseau_grille(L, L, 100)
    resultats = []
    for methode in ("edmonds_karp", "dinic"):
        r = ReseauDinic(n)
        for u, v, c in ar:
            r.ajouter(u, v, c)
        debut = time.time()
        flot = getattr(r, methode)(s, t)
        resultats.append((flot, round(time.time() - debut, 3)))
    print(n, len(ar), resultats)
```

Résultats typiques (grilles `L × L`) :

| Sommets | Arcs | Edmonds-Karp | Dinic |
| --- | --- | --- | --- |
| 100 | 290 | 0,002 s | 0,002 s |
| 400 | 1 180 | 0,020 s | 0,011 s |
| 900 | 2 670 | 0,085 s | 0,031 s |
| 1 600 | 4 760 | 0,297 s | 0,085 s |

Les flots sont identiques ; Dinic devient de plus en plus avantageux avec la taille (environ 3,5 fois plus rapide pour 1 600 sommets) car il fait un seul BFS par phase pour plusieurs chemins augmentants. Sur des réseaux aléatoires peu denses et petits, les deux sont comparables.

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

**Correction**

| Algorithme | Complexité | Remarque |
| --- | --- | --- |
| Ford-Fulkerson (DFS) | **O(E · \|f\*\|)** (capacités entières) | pseudo-polynomial ; peut ne pas terminer avec des capacités irrationnelles |
| Edmonds-Karp | **O(V · E²)** | Ford-Fulkerson avec des chemins de longueur minimale (BFS) ; indépendant des capacités |
| Dinic | **O(V² · E)** | au plus `V − 1` phases, chacune avec un flot bloquant en O(V · E) |
| Dinic sur réseau unitaire | **O(E · √V)** (jusqu'à O(E · min(V^(2/3), E^(1/2))) pour des capacités unitaires générales) | chaque sommet a une capacité entrante ou sortante de 1 |
| Hopcroft-Karp (couplage biparti) | **O(E · √V)** | cas particulier de Dinic sur le réseau unitaire du couplage |

## 22.6 Applications

**Exercice 22.6.1**

Couplage biparti maximum : modélisez par un flot, puis résolvez avec votre implémentation le problème suivant : 4 candidats et 4 postes ; le candidat 1 peut occuper les postes A et B, le candidat 2 les postes B et C, le candidat 3 le poste A, le candidat 4 les postes C et D.

**Correction**

**Modèle** : une source `s`, un sommet par candidat, un sommet par poste, un puits `t`.

- `s → candidat` de capacité 1 (un candidat occupe un seul poste) ;
- `candidat → poste` de capacité 1 si le candidat peut occuper ce poste ;
- `poste → t` de capacité 1 (un poste n'a qu'un titulaire).

Le flot maximal est la taille du couplage maximum ; les arcs candidat → poste portant un flot de 1 donnent les affectations.

```python
# Sommets : 0 = source, 1 à 4 = candidats, 5 à 8 = postes A à D, 9 = puits
r = ReseauDinic(10)
postes = {"A": 5, "B": 6, "C": 7, "D": 8}
possibles = {1: ["A", "B"], 2: ["B", "C"], 3: ["A"], 4: ["C", "D"]}
for candidat in range(1, 5):
    r.ajouter(0, candidat, 1)
for candidat, liste in possibles.items():
    for poste in liste:
        r.ajouter(candidat, postes[poste], 1)
for numero in postes.values():
    r.ajouter(numero, 9, 1)
print(r.dinic(0, 9))        # 4
for candidat, liste in possibles.items():
    for poste in liste:
        for e in r.adj[candidat]:
            if r.vers[e] == postes[poste] and e % 2 == 0 and r.cap[e] == 0:
                print(candidat, poste)
# 1 B ; 2 C ; 3 A ; 4 D
```

Le couplage maximum a donc la taille **4** (tout le monde est affecté) : candidat 1 → B, candidat 2 → C, candidat 3 → A, candidat 4 → D. Le candidat 3 n'ayant que le poste A, le candidat 1 doit prendre B, d'où C pour le candidat 2 et D pour le 4.

**Exercice 22.6.2**

Coupe minimale : après un flot maximal, identifiez les sommets atteignables depuis `s` dans le réseau résiduel et listez les arêtes de la coupe minimale pour le réseau de l'exercice 22.3.1.

**Correction**

Après le flot maximal (23), on cherche les sommets atteignables depuis `s` dans le réseau résiduel : on trouve **`S = {s, a, c, d}`** ; `b` et `t` ne sont plus atteignables (les arcs `a→b`, `d→b` et `d→t` sont saturés).

Arêtes de la coupe minimale (de `S` vers `T = {b, t}`) :

| Arc | Capacité |
| --- | --- |
| `a→b` | 12 |
| `d→b` | 7 |
| `d→t` | 4 |

Capacité de la coupe : `12 + 7 + 4 = ` **23**, égale à la valeur du flot maximal, comme l'affirme le théorème flot-max / coupe-min. (L'arc `b→c` va de `T` vers `S` : il ne compte pas dans la capacité de la coupe.)

**Exercice 22.6.3**

Chemins disjoints : calculez le nombre maximal de chemins disjoints par les arêtes entre deux sommets d'un graphe orienté. Adaptez ensuite le modèle pour des chemins disjoints par les sommets (division des sommets).

**Correction**

**Chemins disjoints par les arêtes** : on donne la capacité 1 à chaque arc ; le flot maximal de `s` à `t` est le nombre maximal de chemins deux à deux sans arc commun (théorème de Menger).

**Chemins disjoints par les sommets** : on **divise** chaque sommet `v` en `v_entrée → v_sortie` de capacité 1 (sauf `s` et `t`, de capacité infinie) ; un arc `u → v` devient `u_sortie → v_entrée` de capacité 1. Un chemin ne peut alors traverser un sommet qu'une fois.

```python
INF = 10**9


def chemins_disjoints_aretes(n, aretes, s, t):
    r = ReseauDinic(n)
    for u, v in aretes:
        r.ajouter(u, v, 1)
    return r.dinic(s, t)


def chemins_disjoints_sommets(n, aretes, s, t):
    r = ReseauDinic(2 * n)                       # v_entrée = v, v_sortie = v + n
    for v in range(n):
        r.ajouter(v, v + n, INF if v in (s, t) else 1)
    for u, v in aretes:
        r.ajouter(u + n, v, 1)
    return r.dinic(s, t + n)


# s=0, a=1, b=2, m=3, c=4, d=5, t=6 : les chemins passent tous par m
aretes = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (3, 5), (4, 6), (5, 6)]
print(chemins_disjoints_aretes(7, aretes, 0, 6))     # 2
print(chemins_disjoints_sommets(7, aretes, 0, 6))    # 1
```

Dans cet exemple, on peut trouver 2 chemins disjoints par les arêtes (`0→1→3→4→6` et `0→2→3→5→6`), qui partagent le sommet `3` ; par les sommets, il n'y en a qu'un seul.

**Exercice 22.6.4**

Affectation de tâches : `n` ouvriers, `m` tâches, chaque ouvrier peut effectuer un sous-ensemble de tâches et accepte au plus `c` tâches. Modélisez par un flot.

**Correction**

**Modèle** :

- source `s → ouvrier i` de capacité **`c`** (l'ouvrier accepte au plus `c` tâches) ;
- `ouvrier i → tâche j` de capacité 1 si `i` peut faire `j` ;
- `tâche j → t` de capacité 1 (chaque tâche est réalisée une seule fois).

Le flot maximal est le nombre maximal de tâches pouvant être affectées ; si sa valeur est `m`, toutes les tâches peuvent être exécutées, et les arcs `ouvrier → tâche` portant 1 donnent l'affectation.

```python
def affectation_taches(n, m, peut, c):
    """peut[i] : liste des tâches que l'ouvrier i sait faire (tâches numérotées 0 à m-1)."""
    r = ReseauDinic(n + m + 2)
    s, t = n + m, n + m + 1
    for i in range(n):
        r.ajouter(s, i, c)
    for i, taches in peut.items():
        for j in taches:
            r.ajouter(i, n + j, 1)
    for j in range(m):
        r.ajouter(n + j, t, 1)
    return r.dinic(s, t)


print(affectation_taches(2, 4, {0: [0, 1, 2], 1: [1, 2, 3]}, 2))   # 4 (chacun fait 2 tâches)
print(affectation_taches(2, 4, {0: [0, 1, 2], 1: [1, 2, 3]}, 1))   # 2 (au plus une tâche chacun)
```

**Exercice 22.6.5**

Sélection de projets : chaque projet a un profit (positif ou négatif) et des dépendances. Modélisez par une coupe minimale pour maximiser le profit total. *(défi)*

**Correction**

**Modèle (problème de fermeture de profit maximal)** : pour chaque projet `p` de profit `g_p` :

- si `g_p > 0` : arc `s → p` de capacité `g_p` ;
- si `g_p < 0` : arc `p → t` de capacité `−g_p` ;
- pour chaque dépendance « `p` exige `q` » : arc `p → q` de capacité **infinie** (choisir `p` oblige à choisir `q`).

Une coupe finie `(S, T)` correspond à une sélection (les projets de `S`, côté source) qui respecte les dépendances (un arc infini ne peut pas aller de `S` vers `T`). Sa capacité vaut : `(somme des profits positifs non sélectionnés) + (somme des coûts des projets négatifs sélectionnés)`. Donc :

**profit maximal = (somme des profits positifs) − (capacité de la coupe minimale)**, et les projets sélectionnés sont ceux atteignables depuis `s` dans le réseau résiduel final.

```python
def selection_projets(profits, dependances):
    n = len(profits)
    r = ReseauDinic(n + 2)
    s, t = n, n + 1
    total_positif = 0
    for p, g in enumerate(profits):
        if g > 0:
            r.ajouter(s, p, g)
            total_positif += g
        elif g < 0:
            r.ajouter(p, t, -g)
    for p, q in dependances:
        r.ajouter(p, q, INF)                      # p exige q
    coupe = r.dinic(s, t)
    atteints, file = {s}, deque([s])
    while file:
        u = file.popleft()
        for e in r.adj[u]:
            if r.cap[e] > 0 and r.vers[e] not in atteints:
                atteints.add(r.vers[e])
                file.append(r.vers[e])
    return total_positif - coupe, sorted(x for x in atteints if x < n)


print(selection_projets([10, -6], [(0, 1)]))
# (4, [0, 1]) : le projet 0 (+10) exige le projet 1 (-6) : profit 4
print(selection_projets([5, -8, 6, -1], [(0, 1), (2, 1), (2, 3)]))
# (2, [0, 1, 2, 3])
```

**Exercice 22.6.6**

Expliquez ce qui distingue un flot à coût minimal d'un flot maximal, et pourquoi les algorithmes de flot ordinaires ne le résolvent pas directement.

**Correction**

- Un **flot maximal** cherche la plus grande **quantité** transportée de `s` à `t`, sans se préoccuper du chemin emprunté.
- Un **flot à coût minimal** associe à chaque arête un coût unitaire `a(e)` et cherche, parmi les flots d'une valeur donnée (ou parmi les flots maximaux), celui de **coût total `Σ a(e) · f(e)` minimal**.

Les algorithmes de flot ordinaires ne le résolvent pas directement : plusieurs flots maximaux de même valeur ont des coûts très différents, et Ford-Fulkerson, Edmonds-Karp ou Dinic choisissent leurs chemins sans tenir compte des coûts. Exemple : deux routes parallèles de `s` à `t`, de capacité 1, de coûts 1 et 5 ; pour envoyer 1 unité, tout chemin donne un flot maximal, mais seul celui de coût 1 est optimal.

Il faut un algorithme dédié : **plus courts chemins successifs** (on augmente le long du chemin de coût minimal du réseau résiduel, par Bellman-Ford ou Dijkstra avec potentiels, les arêtes inverses ayant un coût `−a(e)`), ou **annulation de cycles de coût négatif**, ou le **simplexe pour réseaux**. Applications : affectation de coût minimal, transport, ordonnancement.

---

# 23. Arbres de segments et arbres de Fenwick

## 23.1 Le problème

**Exercice 23.1.1**

On veut gérer un tableau de `n` éléments avec deux opérations : modifier un élément, et calculer la somme d'un intervalle. Donnez le coût de chaque opération avec un simple tableau, avec des sommes préfixes, puis avec un arbre de Fenwick. Pour `q` opérations mélangées, quelle solution choisir ?

**Correction**

| Opération | Tableau simple | Sommes préfixes | Arbre de Fenwick |
| --- | --- | --- | --- |
| Modifier un élément | **O(1)** | O(n) (il faut recalculer les préfixes suivants) | **O(log n)** |
| Somme d'un intervalle | O(n) | **O(1)** | **O(log n)** |
| `q` opérations mélangées | O(q · n) | O(q · n) | **O(q log n)** |

Avec des opérations mélangées, le tableau simple et les sommes préfixes coûtent tous deux O(n) pour l'une des deux opérations ; l'**arbre de Fenwick** (ou l'arbre de segments) équilibre les deux en O(log n) : c'est le bon choix. Si le tableau ne change jamais, les sommes préfixes sont meilleures (O(1) par requête) ; s'il n'y a que des modifications et une seule requête à la fin, le tableau simple suffit.

## 23.2 Arbre de Fenwick (*Binary Indexed Tree*, BIT)

**Exercice 23.2.1**

Pour `n = 8`, donnez, pour chaque indice `i` de 1 à 8, la plage `(i − (i & −i), i]` couverte par `BIT[i]`.

**Correction**

`BIT[i]` couvre la plage `(i − (i & −i), i]`, où `i & −i` est la plus petite puissance de 2 présente dans `i` (le bit de poids faible) :

| `i` | Binaire | `i & −i` | Plage couverte | Taille |
| --- | --- | --- | --- | --- |
| 1 | `0001` | 1 | `(0, 1]` | 1 |
| 2 | `0010` | 2 | `(0, 2]` | 2 |
| 3 | `0011` | 1 | `(2, 3]` | 1 |
| 4 | `0100` | 4 | `(0, 4]` | 4 |
| 5 | `0101` | 1 | `(4, 5]` | 1 |
| 6 | `0110` | 2 | `(4, 6]` | 2 |
| 7 | `0111` | 1 | `(6, 7]` | 1 |
| 8 | `1000` | 8 | `(0, 8]` | 8 |

**Exercice 23.2.2**

Implémentez `Fenwick(n)` avec `ajouter(i, delta)`, `prefixe(i)` et `somme(l, r)`. Testez sur un tableau aléatoire en comparant avec un calcul direct.

**Correction**

```python
import random


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.t = [0] * (n + 1)                 # indices de 1 à n

    def ajouter(self, i, delta):
        while i <= self.n:
            self.t[i] += delta
            i += i & -i                        # prochain nœud qui couvre i

    def prefixe(self, i):
        resultat = 0
        while i > 0:
            resultat += self.t[i]
            i -= i & -i                        # on retire le bit de poids faible
        return resultat

    def somme(self, l, r):
        return self.prefixe(r) - self.prefixe(l - 1)


a = [random.randint(-50, 50) for _ in range(200)]
f = Fenwick(200)
for i, x in enumerate(a, 1):
    f.ajouter(i, x)
for _ in range(500):
    l = random.randint(1, 200)
    r = random.randint(l, 200)
    assert f.somme(l, r) == sum(a[l - 1:r])
for _ in range(200):                           # modifications puis vérifications
    i, d = random.randint(1, 200), random.randint(-9, 9)
    a[i - 1] += d
    f.ajouter(i, d)
    l = random.randint(1, 200)
    r = random.randint(l, 200)
    assert f.somme(l, r) == sum(a[l - 1:r])
print("tests réussis")
```

Les indices vont de 1 à `n`. `prefixe(i)` additionne les plages `(i − lowbit, i]` successives jusqu'à 0 ; `ajouter` met à jour tous les nœuds dont la plage contient `i`.

**Exercice 23.2.3**

Construisez l'arbre de Fenwick d'un tableau donné en O(n). Quelle est la complexité d'un `ajouter` et d'un `prefixe` ?

**Correction**

**Construction en O(n)** : on copie le tableau dans `t[1..n]`, puis chaque nœud `i` transmet sa valeur à son parent `i + (i & −i)`.

```python
def fenwick_depuis(tableau):
    f = Fenwick(len(tableau))
    f.t[1:] = tableau
    for i in range(1, f.n + 1):
        j = i + (i & -i)                       # parent de i dans l'arbre
        if j <= f.n:
            f.t[j] += f.t[i]
    return f


print(fenwick_depuis([3, 2, -1, 6, 5, 4, -3, 3]).t)
# [0, 3, 5, -1, 10, 5, 9, -3, 19]
```

Chaque indice est traité une fois en O(1) : construction en **O(n)**, contre O(n log n) en appelant `ajouter` pour chaque élément.

**Complexités** : `ajouter` et `prefixe` sont tous deux en **O(log n)** : chaque pas modifie `i` en ajoutant ou en retirant le bit de poids faible, ce qui fait au plus `⌊log₂ n⌋ + 1` pas.

**Exercice 23.2.4**

Comptage d'inversions : écrivez `inversions(t)` en O(n log n) avec un arbre de Fenwick (après compression des valeurs).

**Correction**

Pour chaque élément (de gauche à droite), le nombre d'inversions où il joue le rôle de plus petit élément à droite est le nombre d'éléments déjà vus qui lui sont **strictement supérieurs** : `(éléments déjà vus) − (éléments déjà vus ≤ x)`. On compresse d'abord les valeurs en rangs de 1 à `k`.

```python
def inversions(t):
    valeurs = sorted(set(t))
    rang = {v: i + 1 for i, v in enumerate(valeurs)}     # compression des valeurs
    f = Fenwick(len(valeurs))
    total = 0
    for i, x in enumerate(t):
        total += i - f.prefixe(rang[x])                  # déjà vus strictement plus grands
        f.ajouter(rang[x], 1)
    return total


print(inversions([5, 1, 4, 2, 8]))   # 4
print(inversions([3, 2, 1]))         # 3
print(inversions([2, 2, 1]))         # 2 (les égalités ne comptent pas)
```

Complexité **O(n log n)** (tri pour la compression, puis `n` opérations en O(log n)).

**Exercice 23.2.5**

Rang : pour chaque élément d'un tableau, calculez le nombre d'éléments strictement plus petits situés à sa droite.

**Correction**

On parcourt le tableau **de droite à gauche** : à chaque position, le nombre d'éléments strictement plus petits déjà vus (donc à droite) est `prefixe(rang − 1)`.

```python
def plus_petits_a_droite(t):
    valeurs = sorted(set(t))
    rang = {v: i + 1 for i, v in enumerate(valeurs)}
    f = Fenwick(len(valeurs))
    resultat = [0] * len(t)
    for i in range(len(t) - 1, -1, -1):
        resultat[i] = f.prefixe(rang[t[i]] - 1)
        f.ajouter(rang[t[i]], 1)
    return resultat


print(plus_petits_a_droite([5, 2, 6, 1]))   # [2, 1, 1, 0]
print(plus_petits_a_droite([2, 0, 1]))      # [2, 0, 0]
```

Complexité O(n log n).

**Exercice 23.2.6**

Écrivez la recherche du `k`-ième plus petit élément dans un Fenwick de comptages (descente binaire en O(log n)). *(défi)*

**Correction**

Dans un Fenwick de comptages (`t[x]` = nombre d'occurrences de `x` dans une plage), on trouve la position du `k`-ième élément par une **descente binaire** : on construit la plus grande position `pos` dont le préfixe est strictement inférieur à `k`, en testant les puissances de 2 de la plus grande à la plus petite.

```python
class Comptage:
    def __init__(self, n):
        self.n = n
        self.f = Fenwick(n)
        self.plus_haut_bit = 1 << (n.bit_length() - 1)

    def ajouter(self, x):
        self.f.ajouter(x, 1)

    def supprimer(self, x):
        self.f.ajouter(x, -1)

    def kieme(self, k):
        """k-ième plus petit élément (k à partir de 1)."""
        pos, pas = 0, self.plus_haut_bit
        while pas:
            suivant = pos + pas
            if suivant <= self.n and self.f.t[suivant] < k:
                pos = suivant
                k -= self.f.t[suivant]          # on saute la plage entière
            pas >>= 1
        return pos + 1


c = Comptage(100)
for x in (5, 3, 8, 3, 10):
    c.ajouter(x)
print([c.kieme(k) for k in range(1, 6)])   # [3, 3, 5, 8, 10]
c.supprimer(3)
print([c.kieme(k) for k in range(1, 5)])   # [3, 5, 8, 10]
```

Complexité **O(log n)** (au lieu de O(log² n) avec une recherche binaire sur `prefixe`).

## 23.3 Arbre de segments (*Segment Tree*)

**Exercice 23.3.1**

Dessinez l'arbre de segments (sommes) pour `[2, 4, 5, 7, 1, 3]` et déroulez la requête sur l'intervalle `[1, 4]` en indiquant les nœuds visités.

**Correction**

Arbre de segments (sommes) pour `[2, 4, 5, 7, 1, 3]` (indices 0 à 5) ; chaque nœud indique son intervalle et sa somme :

```text
                         [0..5] : 22
                  /                       \
           [0..2] : 11                 [3..5] : 11
           /        \                   /        \
     [0..1] : 6    [2..2] : 5     [3..4] : 8    [5..5] : 3
      /     \                      /     \
 [0..0]:2  [1..1]:4           [3..3]:7  [4..4]:1
```

**Requête sur `[1, 4]`** (somme attendue : `4 + 5 + 7 + 1 = 17`) :

| Nœud visité | Intervalle | Situation | Action |
| --- | --- | --- | --- |
| racine | `[0..5]` | recouvre partiellement `[1, 4]` | on descend |
| gauche | `[0..2]` | partiel | on descend |
| `[0..1]` | `[0, 1]` | partiel | on descend |
| `[0..0]` | `[0, 0]` | hors de `[1, 4]` | renvoie 0 |
| `[1..1]` | `[1, 1]` | **inclus** | renvoie 4 |
| `[2..2]` | `[2, 2]` | **inclus** | renvoie 5 |
| droite | `[3..5]` | partiel | on descend |
| `[3..4]` | `[3, 4]` | **inclus** | renvoie 8 |
| `[5..5]` | `[5, 5]` | hors | renvoie 0 |

Résultat : `4 + 5 + 8 = ` **17**. Au plus 4 nœuds par niveau sont visités, d'où le coût O(log n).

**Exercice 23.3.2**

Implémentez un arbre de segments avec `construire`, `modifier(i, valeur)` et `requete(l, r)` pour la somme. Quelle est la complexité de chaque opération ?

**Correction**

```python
class ArbreSegments:
    def __init__(self, tableau, operation=lambda x, y: x + y, neutre=0):
        self.n = len(tableau)
        self.op, self.neutre = operation, neutre
        self.t = [neutre] * (4 * self.n)
        self._construire(tableau, 1, 0, self.n - 1)

    def _construire(self, tableau, noeud, l, r):
        if l == r:
            self.t[noeud] = tableau[l]
            return
        m = (l + r) // 2
        self._construire(tableau, 2 * noeud, l, m)
        self._construire(tableau, 2 * noeud + 1, m + 1, r)
        self.t[noeud] = self.op(self.t[2 * noeud], self.t[2 * noeud + 1])

    def modifier(self, i, valeur, noeud=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if l == r:
            self.t[noeud] = valeur
            return
        m = (l + r) // 2
        if i <= m:
            self.modifier(i, valeur, 2 * noeud, l, m)
        else:
            self.modifier(i, valeur, 2 * noeud + 1, m + 1, r)
        self.t[noeud] = self.op(self.t[2 * noeud], self.t[2 * noeud + 1])

    def requete(self, a, b, noeud=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if a > r or b < l:                       # hors de l'intervalle
            return self.neutre
        if a <= l and r <= b:                    # entièrement inclus
            return self.t[noeud]
        m = (l + r) // 2
        return self.op(self.requete(a, b, 2 * noeud, l, m),
                       self.requete(a, b, 2 * noeud + 1, m + 1, r))


st = ArbreSegments([2, 4, 5, 7, 1, 3])
print(st.requete(1, 4))      # 17
st.modifier(2, 10)
print(st.requete(1, 4))      # 22
```

Complexités : `construire` en **O(n)**, `modifier` en **O(log n)**, `requete` en **O(log n)** ; mémoire O(n) (tableau de taille `4n`).

**Exercice 23.3.3**

Adaptez-le pour le **minimum** d'un intervalle, puis pour le **maximum** et sa position. Quelle propriété doit vérifier l'opération (associativité, élément neutre) ?

**Correction**

Il suffit de changer l'opération et l'élément neutre :

```python
INF = float("inf")
tableau = [5, 2, 8, 1, 9, 3]

minimum = ArbreSegments(tableau, min, INF)           # minimum : neutre = +infini
maximum = ArbreSegments(tableau, max, -INF)          # maximum : neutre = -infini
print(minimum.requete(0, 3), maximum.requete(2, 5))  # 1 9
```

**Maximum et position** : on stocke des couples `(valeur, −indice)` pour que, à valeur égale, `max` retienne le plus petit indice.

```python
class ArbreMaxPosition:
    def __init__(self, tableau):
        self.arbre = ArbreSegments([(x, -i) for i, x in enumerate(tableau)],
                                   max, (-INF, 0))

    def requete(self, l, r):
        valeur, moins_indice = self.arbre.requete(l, r)
        return valeur, -moins_indice


print(ArbreMaxPosition([3, 9, 2, 9, 1]).requete(0, 4))   # (9, 1)
```

**Propriété requise** : l'opération doit être **associative** (`(a ∘ b) ∘ c = a ∘ (b ∘ c)`) pour que le regroupement par intervalles donne le même résultat, et posséder un **élément neutre** `e` (`a ∘ e = e ∘ a = a`) renvoyé pour les intervalles hors de la requête : c'est un monoïde. La commutativité n'est pas nécessaire tant que l'on combine les résultats dans l'ordre (gauche puis droite). On peut ainsi traiter somme, min, max, PGCD, produit modulaire, et ET/OU/XOR binaires.

**Exercice 23.3.4**

Écrivez une version itérative (ascendante) de l'arbre de segments avec un tableau de taille `2n`.

**Correction**

Version **ascendante** : les feuilles sont stockées aux indices `n` à `2n − 1`, le parent de `i` est `i // 2`.

```python
class ArbreSegmentsIteratif:
    def __init__(self, tableau, operation=lambda x, y: x + y, neutre=0):
        self.n = len(tableau)
        self.op, self.neutre = operation, neutre
        self.t = [neutre] * self.n + list(tableau)
        for i in range(self.n - 1, 0, -1):
            self.t[i] = operation(self.t[2 * i], self.t[2 * i + 1])

    def modifier(self, i, valeur):
        i += self.n
        self.t[i] = valeur
        while i > 1:
            i //= 2
            self.t[i] = self.op(self.t[2 * i], self.t[2 * i + 1])

    def requete(self, l, r):
        """Opération sur l'intervalle [l, r] (bornes incluses)."""
        l += self.n
        r += self.n + 1
        gauche = droite = self.neutre
        while l < r:
            if l & 1:
                gauche = self.op(gauche, self.t[l])
                l += 1
            if r & 1:
                r -= 1
                droite = self.op(self.t[r], droite)     # ordre préservé : opérations non commutatives
            l //= 2
            r //= 2
        return self.op(gauche, droite)


a = ArbreSegmentsIteratif([2, 4, 5, 7, 1, 3])
print(a.requete(1, 4))                                   # 17
b = ArbreSegmentsIteratif([5, 2, 8, 1, 9, 3], min, float("inf"))
print(b.requete(0, 3))                                   # 1
```

Mémoire `2n` (au lieu de `4n`), pas de récursion, constantes plus petites ; mêmes complexités O(log n).

**Exercice 23.3.5**

Gardez dans chaque nœud un quadruplet (somme, meilleur préfixe, meilleur suffixe, meilleur sous-tableau) pour répondre à des requêtes « sous-tableau de somme maximale dans `[l, r]` ». *(défi)*

**Correction**

Chaque nœud stocke `(somme, meilleur préfixe, meilleur suffixe, meilleur sous-tableau)`. La fusion de deux nœuds `A` (gauche) et `B` (droite) :

- `somme = A.somme + B.somme`
- `préfixe = max(A.préfixe, A.somme + B.préfixe)`
- `suffixe = max(B.suffixe, B.somme + A.suffixe)`
- `meilleur = max(A.meilleur, B.meilleur, A.suffixe + B.préfixe)`

Une feuille de valeur `x` vaut `(x, x, x, x)` (le sous-tableau doit être non vide).

```python
def fusion(a, b):
    if a is None:
        return b
    if b is None:
        return a
    sa, pa, sua, ma = a
    sb, pb, sub, mb = b
    return (sa + sb, max(pa, sa + pb), max(sub, sb + sua), max(ma, mb, sua + pb))


class ArbreSousTableau:
    def __init__(self, tableau):
        self.n = len(tableau)
        self.t = [None] * (4 * self.n)
        self._construire(tableau, 1, 0, self.n - 1)

    def _construire(self, tableau, noeud, l, r):
        if l == r:
            x = tableau[l]
            self.t[noeud] = (x, x, x, x)
            return
        m = (l + r) // 2
        self._construire(tableau, 2 * noeud, l, m)
        self._construire(tableau, 2 * noeud + 1, m + 1, r)
        self.t[noeud] = fusion(self.t[2 * noeud], self.t[2 * noeud + 1])

    def requete(self, a, b, noeud=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if a > r or b < l:
            return None                          # neutre : « rien »
        if a <= l and r <= b:
            return self.t[noeud]
        m = (l + r) // 2
        return fusion(self.requete(a, b, 2 * noeud, l, m),
                      self.requete(a, b, 2 * noeud + 1, m + 1, r))


arbre = ArbreSousTableau([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(arbre.requete(0, 8)[3])    # 6   (le sous-tableau [4, -1, 2, 1])
print(arbre.requete(0, 2)[3])    # 1
```

Chaque requête est en **O(log n)** et chaque modification en O(log n) (on recalcule les quadruplets des ancêtres).

## 23.4 Propagation paresseuse (*Lazy Propagation*)

**Exercice 23.4.1**

Pourquoi une mise à jour d'intervalle naïve (modifier chaque élément) est-elle trop lente ? Expliquez le principe de la propagation paresseuse en quelques phrases.

**Correction**

Avec une mise à jour d'intervalle naïve, on modifie chacun des `r − l + 1` éléments, puis on remonte les sommes : **O(n log n)** par mise à jour dans le pire cas (ou O(n) en reconstruisant), donc `q` mises à jour coûtent O(q · n log n), beaucoup trop pour `n, q ≈ 10⁵`.

**Propagation paresseuse** : quand un nœud est entièrement couvert par la mise à jour, on ne descend pas : on met à jour sa valeur agrégée (par exemple `somme += v × longueur`) et on y dépose une **étiquette en attente** (*lazy tag*) qui signifie « cette modification n'a pas encore été transmise aux enfants ». L'étiquette est **poussée** vers les enfants uniquement lorsqu'une opération ultérieure doit descendre dans ce nœud. Ainsi chaque mise à jour et chaque requête touchent O(log n) nœuds.

**Exercice 23.4.2**

Implémentez un arbre de segments avec propagation paresseuse pour : « ajouter `v` à tous les éléments de `[l, r]` » et « somme de `[l, r]` ».

**Correction**

```python
class ArbreParesseux:
    """Ajout sur intervalle et somme sur intervalle."""

    def __init__(self, tableau):
        self.n = len(tableau)
        self.t = [0] * (4 * self.n)
        self.etiquette = [0] * (4 * self.n)        # ajout en attente pour les enfants
        self._construire(tableau, 1, 0, self.n - 1)

    def _construire(self, tableau, noeud, l, r):
        if l == r:
            self.t[noeud] = tableau[l]
            return
        m = (l + r) // 2
        self._construire(tableau, 2 * noeud, l, m)
        self._construire(tableau, 2 * noeud + 1, m + 1, r)
        self.t[noeud] = self.t[2 * noeud] + self.t[2 * noeud + 1]

    def _appliquer(self, noeud, l, r, x):
        self.t[noeud] += x * (r - l + 1)
        self.etiquette[noeud] += x

    def _pousser(self, noeud, l, r):
        if self.etiquette[noeud]:
            m = (l + r) // 2
            self._appliquer(2 * noeud, l, m, self.etiquette[noeud])
            self._appliquer(2 * noeud + 1, m + 1, r, self.etiquette[noeud])
            self.etiquette[noeud] = 0

    def ajouter(self, a, b, x, noeud=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if a > r or b < l:
            return
        if a <= l and r <= b:
            self._appliquer(noeud, l, r, x)
            return
        self._pousser(noeud, l, r)
        m = (l + r) // 2
        self.ajouter(a, b, x, 2 * noeud, l, m)
        self.ajouter(a, b, x, 2 * noeud + 1, m + 1, r)
        self.t[noeud] = self.t[2 * noeud] + self.t[2 * noeud + 1]

    def somme(self, a, b, noeud=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if a > r or b < l:
            return 0
        if a <= l and r <= b:
            return self.t[noeud]
        self._pousser(noeud, l, r)
        m = (l + r) // 2
        return self.somme(a, b, 2 * noeud, l, m) + self.somme(a, b, 2 * noeud + 1, m + 1, r)


p = ArbreParesseux([1, 2, 3, 4, 5])
p.ajouter(1, 3, 10)
print(p.somme(0, 4), p.somme(2, 3))    # 45 27
```

Test réussi contre une simulation naïve sur des centaines d'opérations aléatoires. Complexité **O(log n)** par opération.

**Exercice 23.4.3**

Adaptez-le pour : « affecter la valeur `v` à tous les éléments de `[l, r]` » et « somme de `[l, r]` ». Quelle différence dans la composition des étiquettes paresseuses ?

**Correction**

Pour l'**affectation** (`tous les éléments de [l, r] prennent la valeur v`), l'étiquette stocke la valeur à affecter, et l'on doit pouvoir distinguer « pas d'étiquette » (`None`) de « affecter 0 ». La somme du nœud devient `v × longueur`.

```python
class ArbreAffectation:
    def __init__(self, tableau):
        self.n = len(tableau)
        self.t = [0] * (4 * self.n)
        self.etiquette = [None] * (4 * self.n)     # None : aucune affectation en attente
        self._construire(tableau, 1, 0, self.n - 1)

    def _construire(self, tableau, noeud, l, r):
        if l == r:
            self.t[noeud] = tableau[l]
            return
        m = (l + r) // 2
        self._construire(tableau, 2 * noeud, l, m)
        self._construire(tableau, 2 * noeud + 1, m + 1, r)
        self.t[noeud] = self.t[2 * noeud] + self.t[2 * noeud + 1]

    def _appliquer(self, noeud, l, r, x):
        self.t[noeud] = x * (r - l + 1)
        self.etiquette[noeud] = x                    # écrase toute étiquette antérieure

    def _pousser(self, noeud, l, r):
        if self.etiquette[noeud] is not None:
            m = (l + r) // 2
            self._appliquer(2 * noeud, l, m, self.etiquette[noeud])
            self._appliquer(2 * noeud + 1, m + 1, r, self.etiquette[noeud])
            self.etiquette[noeud] = None

    def affecter(self, a, b, x, noeud=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if a > r or b < l:
            return
        if a <= l and r <= b:
            self._appliquer(noeud, l, r, x)
            return
        self._pousser(noeud, l, r)
        m = (l + r) // 2
        self.affecter(a, b, x, 2 * noeud, l, m)
        self.affecter(a, b, x, 2 * noeud + 1, m + 1, r)
        self.t[noeud] = self.t[2 * noeud] + self.t[2 * noeud + 1]

    def somme(self, a, b, noeud=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if a > r or b < l:
            return 0
        if a <= l and r <= b:
            return self.t[noeud]
        self._pousser(noeud, l, r)
        m = (l + r) // 2
        return self.somme(a, b, 2 * noeud, l, m) + self.somme(a, b, 2 * noeud + 1, m + 1, r)


q = ArbreAffectation([1, 2, 3, 4, 5])
q.affecter(1, 3, 7)
print(q.somme(0, 4))    # 1 + 7 + 7 + 7 + 5 = 27
```

**Différence dans la composition des étiquettes** : pour l'**ajout**, deux étiquettes successives se **cumulent** (`x₁ + x₂`), l'opération est commutative et l'étiquette neutre est 0. Pour l'**affectation**, la plus **récente écrase** l'ancienne (la composition de « affecter `a` » puis « affecter `b` » est « affecter `b` ») ; il faut un marqueur spécial pour l'absence d'étiquette. Si l'on mélange ajouts et affectations, la composition est plus délicate : un ajout après une affectation devient une affectation de `valeur + x`, tandis qu'une affectation après un ajout efface l'ajout.

**Exercice 23.4.4**

Écrivez le cas particulier d'un arbre de Fenwick avec mise à jour d'intervalle et requête de point (via le tableau de différences).

**Correction**

Avec un Fenwick sur le **tableau de différences** `d[i] = a[i] − a[i − 1]`, ajouter `x` sur `[l, r]` revient à `d[l] += x` et `d[r + 1] −= x` ; la valeur d'un point `a[i]` est le préfixe `d[1] + ... + d[i]`.

```python
class FenwickAjoutIntervalle:
    def __init__(self, n):
        self.f = Fenwick(n + 1)

    def ajouter_intervalle(self, l, r, x):
        self.f.ajouter(l, x)
        self.f.ajouter(r + 1, -x)

    def valeur(self, i):
        return self.f.prefixe(i)


fr = FenwickAjoutIntervalle(10)
fr.ajouter_intervalle(2, 5, 3)
fr.ajouter_intervalle(4, 8, 2)
print([fr.valeur(i) for i in range(1, 11)])
# [0, 3, 3, 5, 5, 2, 2, 2, 0, 0]
```

Mise à jour d'intervalle et requête de point en **O(log n)** chacune. (Pour la somme d'un intervalle avec ajout sur intervalle, on utilise deux Fenwick, ou un arbre de segments avec propagation paresseuse.)

## 23.5 Fenwick ou arbre de segments ?

**Exercice 23.5.1**

Pour chacun des besoins suivants, choisissez la structure et justifiez : somme de préfixe avec mises à jour de points, minimum d'intervalle avec mises à jour, somme d'intervalle avec ajout sur intervalle, comptage d'inversions, maximum d'intervalle statique avec de très nombreuses requêtes.

**Correction**

| Besoin | Structure | Justification |
| --- | --- | --- |
| Somme de préfixe avec mises à jour de points | **Fenwick** | plus court à écrire, constantes plus petites, O(log n) |
| Minimum d'intervalle avec mises à jour | **Arbre de segments** | le minimum n'est pas inversible : on ne peut pas le calculer par différence de préfixes (le Fenwick ne convient pas) |
| Somme d'intervalle avec ajout sur intervalle | **Arbre de segments avec propagation paresseuse** (ou deux Fenwick) | mises à jour et requêtes d'intervalle en O(log n) |
| Comptage d'inversions | **Fenwick** | une suite d'`ajouter` et de `prefixe` après compression des valeurs ; code très court |
| Maximum d'intervalle statique, très nombreuses requêtes | **Table creuse** (*sparse table*) | précalcul O(n log n), puis O(1) par requête (aucune modification) |

## 23.6 Applications

**Exercice 23.6.1**

Implémentez une table creuse (*sparse table*) pour le minimum d'un intervalle en O(1) après un précalcul en O(n log n).

**Correction**

`creuse[j][i]` contient le minimum de l'intervalle de longueur `2ʲ` qui commence en `i`. Pour un intervalle `[l, r]` de longueur `L`, on prend `k = ⌊log₂ L⌋` et on combine **deux** intervalles de longueur `2ᵏ` (qui se recouvrent, ce qui est sans effet pour un minimum).

```python
class TableCreuse:
    def __init__(self, tableau):
        n = len(tableau)
        self.log = [0] * (n + 2)
        for i in range(2, n + 2):
            self.log[i] = self.log[i // 2] + 1
        self.t = [tableau[:]]
        j = 1
        while (1 << j) <= n:
            precedent = self.t[-1]
            demi = 1 << (j - 1)
            self.t.append([min(precedent[i], precedent[i + demi])
                           for i in range(n - (1 << j) + 1)])
            j += 1

    def minimum(self, l, r):
        k = self.log[r - l + 1]
        return min(self.t[k][l], self.t[k][r - (1 << k) + 1])


print(TableCreuse([5, 2, 8, 1, 9, 3]).minimum(1, 4))   # 1
```

Précalcul en **O(n log n)** (temps et mémoire), requête en **O(1)**. Ne fonctionne que pour des opérations **idempotentes** (`min`, `max`, `pgcd`), pas pour la somme (le recouvrement compterait deux fois certains éléments), et le tableau est **statique**.

**Exercice 23.6.2**

Décomposition en racine carrée : implémentez une structure qui supporte la mise à jour d'un point et la somme d'un intervalle en O(√n). Comparez-la au Fenwick.

**Correction**

On découpe le tableau en blocs de taille `b ≈ √n` et on stocke la somme de chaque bloc. Une mise à jour modifie un élément et la somme de son bloc : O(1). Une requête additionne les éléments isolés aux deux extrémités (au plus `2b`) et les sommes de blocs entiers (au plus `n / b`) : **O(√n)**.

```python
import math


class RacineCarree:
    def __init__(self, tableau):
        self.a = tableau[:]
        self.n = len(tableau)
        self.b = max(1, math.isqrt(self.n))
        self.blocs = [0] * ((self.n + self.b - 1) // self.b)
        for i, x in enumerate(tableau):
            self.blocs[i // self.b] += x

    def modifier(self, i, valeur):
        self.blocs[i // self.b] += valeur - self.a[i]
        self.a[i] = valeur

    def somme(self, l, r):
        total = 0
        while l <= r and l % self.b != 0:                 # éléments isolés à gauche
            total += self.a[l]
            l += 1
        while l + self.b - 1 <= r:                        # blocs entiers
            total += self.blocs[l // self.b]
            l += self.b
        while l <= r:                                     # éléments isolés à droite
            total += self.a[l]
            l += 1
        return total
```

Comparaison pour `n = 20 000` et 20 000 opérations (une modification et une requête chacune) : environ **0,05 s** pour le Fenwick contre environ **0,25 s** pour la racine carrée (soit un facteur 5 à 6 en faveur du Fenwick, qui augmente avec `n` car `log n ≪ √n`). La décomposition en racine carrée reste utile quand l'opération n'est pas facile à exprimer avec un Fenwick ou un arbre de segments.

**Exercice 23.6.3**

Rangs et statistiques d'ordre : maintenez un multi-ensemble d'entiers de `[1, 10⁵]` avec `ajouter(x)`, `supprimer(x)` et `kieme(k)`.

**Correction**

Un Fenwick de comptages sur `[1, 10⁵]` : `ajouter(x)` incrémente la case `x`, `supprimer(x)` la décrémente, et `kieme(k)` fait la descente binaire.

```python
class MultiEnsemble:
    def __init__(self, n=10**5):
        self.c = Comptage(n)                 # classe de l'exercice 23.2.6

    def ajouter(self, x):
        self.c.ajouter(x)

    def supprimer(self, x):
        self.c.supprimer(x)

    def kieme(self, k):
        return self.c.kieme(k)


m = MultiEnsemble()
for x in (50, 7, 7, 99999, 3):
    m.ajouter(x)
print([m.kieme(k) for k in range(1, 6)])   # [3, 7, 7, 50, 99999]
m.supprimer(7)
print(m.kieme(2))                           # 50
```

Les trois opérations sont en **O(log n)** (soit environ 17 pas pour `n = 10⁵`). On suppose que `supprimer` n'est appelé que pour une valeur présente.

**Exercice 23.6.4**

Requêtes hors ligne : on connaît à l'avance `q` requêtes « nombre d'éléments distincts dans `[l, r]` ». Expliquez comment les trier par borne droite et utiliser un Fenwick pour y répondre en `O((n + q) log n)`. *(défi)*

**Correction**

On traite les requêtes **hors ligne**, triées par borne droite `r` croissante, en balayant le tableau de gauche à droite avec un Fenwick qui contient un `1` à la **dernière occurrence** (jusqu'à la position courante) de chaque valeur distincte.

Pour chaque position `i` de 1 à `n`, avec `x = t[i]` :

1. si `x` est déjà apparu à la position `p`, on retire son ancienne marque : `ajouter(p, −1)` ;
2. on pose la marque courante : `ajouter(i, +1)` et on retient `dernier[x] = i` ;
3. on répond à toutes les requêtes `(l, r)` avec `r = i` par `somme(l, i)`.

**Justification** : après le traitement de la position `r`, une valeur présente dans `t[l..r]` a sa dernière occurrence (au plus `r`) en une position `≥ l` : elle contribue exactement une fois à la somme sur `[l, r]` ; une valeur absente de `[l, r]` a sa dernière occurrence avant `l` (ou jamais), et ne contribue pas. La somme compte donc les valeurs distinctes de `[l, r]`.

```python
def elements_distincts(t, requetes):
    n = len(t)
    f = Fenwick(n)
    dernier = {}
    reponses = [0] * len(requetes)
    ordre = sorted(range(len(requetes)), key=lambda q: requetes[q][1])
    p = 0
    for i in range(1, n + 1):
        x = t[i - 1]
        if x in dernier:
            f.ajouter(dernier[x], -1)
        f.ajouter(i, 1)
        dernier[x] = i
        while p < len(ordre) and requetes[ordre[p]][1] == i:
            q = ordre[p]
            l, r = requetes[q]
            reponses[q] = f.somme(l, r)
            p += 1
    return reponses


print(elements_distincts([1, 2, 1, 3, 2, 1], [(1, 3), (2, 5), (1, 6), (4, 4)]))
# [2, 3, 3, 1]
```

Complexité : tri des requêtes en O(q log q), puis `n` mises à jour et `q` requêtes de Fenwick en O(log n) chacune : **O((n + q) log n)**. Le résultat a été comparé à un calcul direct sur des cas aléatoires.

---

# 24. Algorithmes sur les chaînes

## 24.1 Recherche de motif naïve

**Exercice 24.1.1**

Implémentez `recherche_naive(texte, motif)` qui renvoie toutes les positions d'occurrence. Quelle est la complexité dans le pire cas ?

**Correction**

```python
def recherche_naive(texte, motif):
    n, m = len(texte), len(motif)
    positions = []
    for i in range(n - m + 1):
        j = 0
        while j < m and texte[i + j] == motif[j]:
            j += 1
        if j == m:
            positions.append(i)
    return positions


print(recherche_naive("abracadabra", "abra"))   # [0, 7]
print(recherche_naive("aaaa", "aa"))            # [0, 1, 2]
```

Complexité dans le pire cas : **O(n · m)** (jusqu'à `m` comparaisons pour chacune des `n − m + 1` positions). Sur des textes « normaux », les décalages échouent presque immédiatement et le coût observé est proche de O(n).

**Exercice 24.1.2**

Donnez un texte et un motif de tailles `n` et `m` pour lesquels l'algorithme naïf effectue environ `n · m` comparaisons.

**Correction**

Texte `"a" * n` et motif `"a" * (m − 1) + "b"` : à chaque position, les `m − 1` premiers caractères correspondent, et c'est seulement le dernier (`b` contre `a`) qui échoue. Il y a donc `(n − m + 1)` positions de départ et `m` comparaisons chacune, soit environ **`n · m`** comparaisons au total (de l'ordre de `n² / 4` pour `m ≈ n / 2`).

Exemple concret : texte de 200 000 `a` et motif de 50 `a` suivis d'un `b` : environ 10⁷ comparaisons ; la recherche naïve en Python prend de l'ordre de 0,5 s contre 0,02 s pour KMP.

## 24.2 Algorithme de Knuth-Morris-Pratt (KMP)

**Exercice 24.2.1**

Calculez à la main la table des préfixes (fonction d'échec) pour les motifs `"ababaca"` et `"aabaaab"`.

**Correction**

La **table des préfixes** (fonction d'échec) `pi[i]` est la longueur du plus long préfixe propre du motif qui est aussi suffixe de `motif[0..i]`.

**`"ababaca"`** :

| `i` | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Lettre | a | b | a | b | a | c | a |
| `pi[i]` | 0 | 0 | 1 | 2 | 3 | 0 | 1 |

Explications : `pi[2] = 1` (`"a"`), `pi[3] = 2` (`"ab"`), `pi[4] = 3` (`"aba"`) ; en `i = 5` (`c`), aucun suffixe de `"ababac"` n'est un préfixe : 0 ; en `i = 6`, `"a"` : 1.

**`"aabaaab"`** :

| `i` | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Lettre | a | a | b | a | a | a | b |
| `pi[i]` | 0 | 1 | 0 | 1 | 2 | 2 | 3 |

Explications : `pi[1] = 1` (`"a"`) ; `pi[2] = 0` ; `pi[3] = 1`, `pi[4] = 2` (`"aa"`) ; en `i = 5`, le préfixe `"aab"` ne prolonge pas `"aa"` (`b ≠ a`), on retombe sur `"a"` puis `"aa"` : `pi[5] = 2` ; en `i = 6`, `"aab"` prolonge `"aa"` : `pi[6] = 3`.

**Exercice 24.2.2**

Implémentez la construction de la table puis `kmp(texte, motif)`. Déroulez la recherche de `"abab"` dans `"abababcabab"` en notant les décalages.

**Correction**

```python
def table_prefixes(motif):
    pi = [0] * len(motif)
    k = 0
    for i in range(1, len(motif)):
        while k > 0 and motif[i] != motif[k]:
            k = pi[k - 1]                      # on retombe sur un bord plus court
        if motif[i] == motif[k]:
            k += 1
        pi[i] = k
    return pi


def kmp(texte, motif):
    pi = table_prefixes(motif)
    k, positions = 0, []
    for i, c in enumerate(texte):
        while k > 0 and c != motif[k]:
            k = pi[k - 1]
        if c == motif[k]:
            k += 1
        if k == len(motif):                    # occurrence complète
            positions.append(i - k + 1)
            k = pi[k - 1]
    return positions


print(table_prefixes("ababaca"))                 # [0, 0, 1, 2, 3, 0, 1]
print(kmp("abababcabab", "abab"))                # [0, 2, 7]
```

**Déroulement** pour `"abab"` dans `"abababcabab"` (`pi = [0, 0, 1, 2]`, `k` = nombre de caractères du motif déjà appariés) :

| `i` | Caractère | `k` après lecture | Événement |
| --- | --- | --- | --- |
| 0 à 3 | `a b a b` | 1, 2, 3, 4 | `k = 4` : occurrence en **0** ; `k ← pi[3] = 2` (décalage de `4 − 2 = 2`) |
| 4 | `a` | 3 | motif[2] = `a` : on continue |
| 5 | `b` | 4 | occurrence en `5 − 3 = ` **2** ; `k ← pi[3] = 2` |
| 6 | `c` | | `c ≠ motif[2] = a` : `k ← pi[1] = 0` ; `c ≠ motif[0]` : `k = 0` |
| 7 | `a` | 1 | |
| 8 | `b` | 2 | |
| 9 | `a` | 3 | |
| 10 | `b` | 4 | occurrence en `10 − 3 = ` **7** |

Occurrences aux positions **0, 2 et 7**. Le motif est décalé de `k − pi[k − 1]` positions à chaque échec ou occurrence, sans jamais reculer dans le texte.

**Exercice 24.2.3**

Expliquez pourquoi KMP ne revient jamais en arrière dans le texte. Pourquoi la complexité est-elle O(n + m) ?

**Correction**

**Pourquoi KMP ne revient jamais en arrière** : quand `k` caractères du motif ont été appariés et que le caractère suivant ne correspond pas, la table des préfixes indique la longueur `pi[k − 1]` du plus long préfixe du motif qui est aussi un suffixe de ce qui vient d'être lu : on sait donc déjà que ces `pi[k − 1]` derniers caractères du texte correspondent au début du motif. Il suffit de reprendre la comparaison avec `motif[pi[k − 1]]` sur le **même caractère du texte**. Aucun caractère du texte déjà lu n'a besoin d'être relu : l'indice `i` du texte ne fait qu'augmenter.

**Pourquoi O(n + m)** : le calcul de la table est en O(m) et la recherche en O(n), par un argument d'**amortissement** : `k` augmente d'au plus 1 à chaque caractère du texte (donc au plus `n` au total) ; chaque itération de la boucle `while` diminue strictement `k`, mais `k` ne peut pas être diminué plus de fois qu'il n'a été augmenté. Le nombre total d'itérations de `while` est donc au plus `n`, d'où une recherche en O(n). Le même raisonnement donne O(m) pour la table.

**Exercice 24.2.4**

Utilisez la table des préfixes pour trouver la plus petite période d'une chaîne (le plus petit `p` tel que la chaîne soit une répétition d'un bloc de longueur `p`).

**Correction**

Soit `n` la longueur de `s` et `p = n − pi[n − 1]`. Si `p` divise `n`, la plus petite période (taille du bloc répété) vaut `p` ; sinon la chaîne n'est pas une répétition d'un bloc plus court et la période est `n`.

```python
def plus_petite_periode(s):
    n = len(s)
    p = n - table_prefixes(s)[-1]
    return p if n % p == 0 else n


print(plus_petite_periode("abcabcabc"))   # 3
print(plus_petite_periode("abab"))        # 2
print(plus_petite_periode("aaaa"))        # 1
print(plus_petite_periode("abcab"))       # 5 (5 n'est pas divisible par 3)
print(plus_petite_periode("abcd"))        # 4
```

Justification : `pi[n − 1]` est la longueur du plus long bord de `s` ; `n − pi[n − 1]` est la plus petite période au sens large (`s[i] = s[i + p]`), et `s` est une répétition exacte d'un bloc si et seulement si `p` divise `n`.

**Exercice 24.2.5**

Déterminez si une chaîne `b` est une rotation d'une chaîne `a` en utilisant une seule recherche de motif.

**Correction**

`b` est une rotation de `a` si et seulement si `len(a) == len(b)` et `b` est une sous-chaîne de `a + a` : une seule recherche de motif (KMP) en O(n).

```python
def est_rotation(a, b):
    return len(a) == len(b) and kmp(a + a, b) != []


print(est_rotation("abcde", "cdeab"))   # True
print(est_rotation("abcde", "abced"))   # False
```

La vérification de la longueur évite les faux positifs (par exemple `b` plus court que `a`). Complexité O(n).

## 24.3 Algorithme de Rabin-Karp

**Exercice 24.3.1**

Soit un texte composé de chiffres `"2359023141526739921"` et un motif `"31415"`. Avec une base 10 et un module 13, calculez à la main le hachage du motif puis le hachage de chaque fenêtre en utilisant la mise à jour glissante. Combien de fausses correspondances (collisions) rencontrez-vous ?

**Correction**

Texte `"2359023141526739921"`, motif `"31415"`, base 10, module 13. Hachage du motif : `31415 mod 13 = 7`.

Pour la fenêtre suivante, mise à jour glissante : `h' = ((h − chiffre_sortant × 10⁴) × 10 + chiffre_entrant) mod 13`, avec `10⁴ mod 13 = 3` (`10000 = 13 × 769 + 3`).

| Décalage | Fenêtre | Hachage | Résultat |
| --- | --- | --- | --- |
| 0 | `23590` | 8 | ≠ 7 |
| 1 | `35902` | 9 | ≠ 7 |
| 2 | `59023` | 3 | ≠ 7 |
| 3 | `90231` | 11 | ≠ 7 |
| 4 | `02314` | 0 | ≠ 7 |
| 5 | `23141` | 1 | ≠ 7 |
| 6 | `31415` | **7** | **occurrence réelle** (vérification caractère par caractère : succès) |
| 7 | `14152` | 8 | ≠ 7 |
| 8 | `41526` | 4 | ≠ 7 |
| 9 | `15267` | 5 | ≠ 7 |
| 10 | `52673` | 10 | ≠ 7 |
| 11 | `26739` | 11 | ≠ 7 |
| 12 | `67399` | **7** | **fausse correspondance** (collision : `67399 mod 13 = 7`) |
| 13 | `73992` | 9 | ≠ 7 |
| 14 | `39921` | 11 | ≠ 7 |

On rencontre donc **1 fausse correspondance** (au décalage 12) ; elle est éliminée par la vérification directe des caractères. L'occurrence véritable est au décalage **6**.

**Exercice 24.3.2**

Implémentez `rabin_karp(texte, motif)`. Pourquoi faut-il vérifier la correspondance caractère par caractère quand les hachages sont égaux ?

**Correction**

```python
def rabin_karp(texte, motif, base=256, module=(1 << 61) - 1):
    n, m = len(texte), len(motif)
    if m > n:
        return []
    puissance = pow(base, m - 1, module)            # base^(m-1) pour retirer le premier caractère
    h_motif = h_fenetre = 0
    for i in range(m):
        h_motif = (h_motif * base + ord(motif[i])) % module
        h_fenetre = (h_fenetre * base + ord(texte[i])) % module
    positions = []
    for s in range(n - m + 1):
        if h_motif == h_fenetre and texte[s:s + m] == motif:    # vérification
            positions.append(s)
        if s < n - m:                                           # fenêtre glissante
            h_fenetre = ((h_fenetre - ord(texte[s]) * puissance) * base + ord(texte[s + m])) % module
    return positions


print(rabin_karp("abracadabra", "abra"))   # [0, 7]
```

**Pourquoi vérifier** : deux chaînes différentes peuvent avoir le même hachage (collision), comme `67399` et `31415` modulo 13. Sans vérification caractère par caractère, on renverrait de fausses occurrences. La vérification n'a lieu que lorsque les hachages sont égaux ; elle coûte O(m) mais est rarement déclenchée pour de mauvaises raisons. Complexité attendue O(n + m), pire cas O(n · m) si de très nombreuses collisions se produisent.

**Exercice 24.3.3**

Adaptez-le à la recherche **simultanée** de plusieurs motifs de même longueur.

**Correction**

Pour plusieurs motifs de **même longueur `m`**, on stocke leurs hachages dans une table (dictionnaire) associant chaque hachage à la liste des motifs correspondants ; à chaque fenêtre, une seule consultation de table remplace `k` comparaisons.

```python
from collections import defaultdict


def rabin_karp_multiple(texte, motifs, base=256, module=(1 << 61) - 1):
    m = len(motifs[0])
    table = defaultdict(list)
    for motif in motifs:
        h = 0
        for c in motif:
            h = (h * base + ord(c)) % module
        table[h].append(motif)
    puissance = pow(base, m - 1, module)
    h_fenetre = 0
    for i in range(m):
        h_fenetre = (h_fenetre * base + ord(texte[i])) % module
    resultats = []
    for s in range(len(texte) - m + 1):
        for motif in table.get(h_fenetre, []):
            if texte[s:s + m] == motif:
                resultats.append((s, motif))
        if s < len(texte) - m:
            h_fenetre = ((h_fenetre - ord(texte[s]) * puissance) * base + ord(texte[s + m])) % module
    return resultats


print(rabin_karp_multiple("abracadabra", ["abr", "cad", "dab", "xyz"]))
# [(0, 'abr'), (4, 'cad'), (6, 'dab'), (7, 'abr')]
```

Complexité attendue O(n + k · m) pour `k` motifs de même longueur. (Pour des motifs de longueurs différentes, on utilise Aho-Corasick, voir 24.6.4.)

**Exercice 24.3.4**

Détection de doublons de sous-chaînes : trouvez la plus longue sous-chaîne qui apparaît au moins deux fois dans une chaîne (recherche binaire sur la longueur + hachage). *(défi)*

**Correction**

On cherche la plus grande longueur `L` telle qu'une sous-chaîne de longueur `L` apparaisse au moins deux fois. Cette propriété est **monotone** (si une sous-chaîne de longueur `L` se répète, ses préfixes de longueur `L − 1` aussi) : on fait une recherche binaire sur `L`, et pour chaque `L` on parcourt les fenêtres avec un hachage glissant, en stockant les hachages dans un dictionnaire.

```python
import random


def plus_longue_sous_chaine_repetee(s):
    n = len(s)
    q1, q2 = (1 << 61) - 1, 10**9 + 7
    base = random.randint(300, 10**6)

    def existe(L):
        """Renvoie (position d'une première occurrence + 1) si une sous-chaîne de longueur L se répète."""
        vus = {}
        h1 = h2 = 0
        H1, H2 = pow(base, L - 1, q1), pow(base, L - 1, q2)
        for i in range(L):
            h1 = (h1 * base + ord(s[i])) % q1
            h2 = (h2 * base + ord(s[i])) % q2
        for i in range(n - L + 1):
            cle = (h1, h2)
            if cle in vus:
                return vus[cle] + 1
            vus[cle] = i
            if i < n - L:
                h1 = ((h1 - ord(s[i]) * H1) * base + ord(s[i + L])) % q1
                h2 = ((h2 - ord(s[i]) * H2) * base + ord(s[i + L])) % q2
        return 0

    bas, haut, meilleure = 1, n - 1, ""
    while bas <= haut:
        milieu = (bas + haut) // 2
        position = existe(milieu)
        if position:
            meilleure = s[position - 1:position - 1 + milieu]
            bas = milieu + 1
        else:
            haut = milieu - 1
    return meilleure


print(plus_longue_sous_chaine_repetee("banana"))         # ana
print(plus_longue_sous_chaine_repetee("abracadabra"))    # abra
print(repr(plus_longue_sous_chaine_repetee("abcd")))     # ''
```

Complexité attendue **O(n log n)** (`log n` étapes de recherche binaire, chacune en O(n)). Deux modules rendent les collisions négligeables. (Les occurrences peuvent se chevaucher, comme `ana` dans `banana`.) Le résultat a été comparé à une recherche exhaustive sur des chaînes aléatoires.

**Exercice 24.3.5**

Quelle est la probabilité de collision pour un module de l'ordre de 10⁹ ? Pourquoi utilise-t-on parfois deux modules ?

**Correction**

Avec un module `q ≈ 10⁹`, la probabilité que deux chaînes **fixes** différentes aient le même hachage est de l'ordre de `1 / q ≈ 10⁻⁹`. Mais cette probabilité s'applique **par comparaison** : pour une recherche d'un motif dans un texte de `n = 10⁶` fenêtres, on s'attend à `n / q ≈ 10⁻³` faux positifs (que la vérification élimine). Pour des algorithmes qui comparent **toutes les paires** de sous-chaînes (par exemple le plus long facteur répété avec `n ≈ 10⁵` sous-chaînes), il y a environ `n² / 2 = 5 × 10⁹` paires : par le paradoxe des anniversaires, des collisions sont **presque certaines** avec un seul module de 10⁹.

On utilise donc **deux modules** indépendants (ou un module de 61 bits comme `2⁶¹ − 1`) : la probabilité de collision devient de l'ordre de `10⁻¹⁸`, négligeable même pour des milliards de comparaisons. On choisit aussi une **base aléatoire** pour empêcher un adversaire de construire des collisions (attaque sur un hachage à paramètres fixes).

## 24.4 Algorithme Z

**Exercice 24.4.1**

Calculez à la main le tableau Z de `"aabcaabxaaz"` et de `"aaaaa"`.

**Correction**

Le tableau Z : `Z[i]` est la longueur du plus long préfixe commun entre `s` et `s[i:]` (par convention `Z[0] = n`).

**`"aabcaabxaaz"`** (n = 11) :

| `i` | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Lettre | a | a | b | c | a | a | b | x | a | a | z |
| `Z[i]` | 11 | 1 | 0 | 0 | 3 | 1 | 0 | 0 | 2 | 1 | 0 |

Détail : `Z[4] = 3` car `"aabxaaz"` commence par `"aab"` mais ensuite `x ≠ c` ; `Z[8] = 2` (`"aaz"` partage `"aa"` avec `"aab..."`) ; `Z[1] = 1`, `Z[5] = 1`, `Z[9] = 1` (un seul `a` en commun).

**`"aaaaa"`** : `Z = [5, 4, 3, 2, 1]`.

**Exercice 24.4.2**

Implémentez `z_algorithme(s)`, puis la recherche de motif `z_algorithme(motif + "#" + texte)`. Pourquoi le séparateur `#` est-il nécessaire ?

**Correction**

```python
def z_algorithme(s):
    n = len(s)
    Z = [0] * n
    Z[0] = n
    gauche = droite = 0                       # fenêtre [gauche, droite) : la plus à droite déjà appariée avec un préfixe
    for i in range(1, n):
        if i < droite:
            Z[i] = min(droite - i, Z[i - gauche])        # on réutilise l'information
        while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
            Z[i] += 1
        if i + Z[i] > droite:
            gauche, droite = i, i + Z[i]
    return Z


def recherche_z(texte, motif):
    m = len(motif)
    Z = z_algorithme(motif + "#" + texte)
    return [i - m - 1 for i in range(m + 1, len(Z)) if Z[i] == m]


print(z_algorithme("aabcaabxaaz"))          # [11, 1, 0, 0, 3, 1, 0, 0, 2, 1, 0]
print(recherche_z("abracadabra", "abra"))   # [0, 7]
```

**Pourquoi le séparateur `#`** : il doit être un caractère absent du motif et du texte. Il garantit que `Z[i] ≤ m` pour tous les `i` situés dans la partie texte : une correspondance avec le préfixe ne peut pas continuer au-delà du séparateur, donc elle ne se confond pas avec le texte. Sans séparateur, une valeur de `Z` pourrait dépasser `m` en recouvrant le début du texte concaténé, ce qui fausserait le test `Z[i] == m` (et les positions). Complexité O(n + m) (même argument d'amortissement que KMP, avec la fenêtre `[gauche, droite)`).

**Exercice 24.4.3**

Utilisez le tableau Z pour calculer le nombre de sous-chaînes distinctes d'une chaîne, ou la plus petite période d'une chaîne.

**Correction**

**Nombre de sous-chaînes distinctes** : on ajoute les caractères un par un ; pour le préfixe `t = s[:k]`, les nouvelles sous-chaînes sont celles qui se terminent par le dernier caractère et qui n'ont pas déjà été vues. En inversant `t`, ces sous-chaînes deviennent des préfixes de `t` inversé, et le nombre de celles qui sont déjà apparues est `max(Z[1:])`. Le nombre de nouvelles sous-chaînes vaut donc `k − max(Z_inversé[1:])`.

```python
def nombre_sous_chaines_distinctes(s):
    total = 0
    for k in range(1, len(s) + 1):
        inverse = s[:k][::-1]
        Z = z_algorithme(inverse)
        total += k - (max(Z[1:]) if k > 1 else 0)
    return total


print(nombre_sous_chaines_distinctes("aab"))    # 5 : a, aa, aab, ab, b
print(nombre_sous_chaines_distinctes("abab"))   # 7
```

Complexité **O(n²)** (un tableau Z par préfixe) ; une structure comme le tableau des suffixes donne O(n log n).

**Plus petite période** : le plus petit `p` divisant `n` tel que `Z[p] == n − p` (le suffixe commençant en `p` est un préfixe).

```python
def periode_z(s):
    Z = z_algorithme(s)
    n = len(s)
    for p in range(1, n):
        if n % p == 0 and Z[p] == n - p:
            return p
    return n


print(periode_z("abcabcabc"), periode_z("abcd"))   # 3 4
```

**Exercice 24.4.4**

Comptez, pour chaque préfixe d'une chaîne, combien de fois il apparaît dans la chaîne. *(défi)*

**Correction**

`Z[i] ≥ l` signifie que le préfixe de longueur `l` apparaît à la position `i`. Le nombre d'occurrences du préfixe de longueur `l` est donc le nombre d'indices `i` (y compris `i = 0`) avec `Z[i] ≥ l` : on compte les valeurs de `Z` puis on fait des **sommes de suffixes**.

```python
def occurrences_des_prefixes(s):
    Z = z_algorithme(s)
    n = len(s)
    frequence = [0] * (n + 2)
    for valeur in Z:
        frequence[valeur] += 1
    comptes = [0] * (n + 2)
    for longueur in range(n, 0, -1):                 # somme de suffixes
        comptes[longueur] = comptes[longueur + 1] + frequence[longueur]
    return comptes[1:n + 1]


print(z_algorithme("ababa"))               # [5, 0, 3, 0, 1]
print(occurrences_des_prefixes("ababa"))   # [3, 2, 2, 1, 1]
```

Pour `"ababa"` : `"a"` apparaît 3 fois, `"ab"` 2 fois, `"aba"` 2 fois, `"abab"` et `"ababa"` 1 fois. Complexité O(n).

## 24.5 Trie (arbre préfixe)

**Exercice 24.5.1**

Dessinez le trie obtenu en insérant `["tea", "ten", "to", "inn", "in", "i"]` et marquez les fins de mots.

**Correction**

Insertion de `["tea", "ten", "to", "inn", "in", "i"]` ; le symbole `*` marque une fin de mot :

```text
(racine)
├── t
│   ├── e
│   │   ├── a *      "tea"
│   │   └── n *      "ten"
│   └── o *          "to"
└── i *              "i"
    └── n *          "in"
        └── n *      "inn"
```

Les nœuds marqués correspondent aux mots `tea`, `ten`, `to`, `i`, `in`, `inn`. Le nœud `te` n'est pas une fin de mot.

**Exercice 24.5.2**

Implémentez un `Trie` avec `inserer`, `contient`, `commence_par` et `completions`. Quelle est la complexité de chaque opération ?

**Correction**

```python
class Trie:
    def __init__(self):
        self.enfants = {}
        self.fin = False
        self.compte = 0                         # utilisé à l'exercice 24.5.3

    def inserer(self, mot):
        noeud = self
        for c in mot:
            noeud = noeud.enfants.setdefault(c, Trie())
            noeud.compte += 1
        noeud.fin = True

    def _noeud(self, prefixe):
        noeud = self
        for c in prefixe:
            if c not in noeud.enfants:
                return None
            noeud = noeud.enfants[c]
        return noeud

    def contient(self, mot):
        noeud = self._noeud(mot)
        return noeud is not None and noeud.fin

    def commence_par(self, prefixe):
        return self._noeud(prefixe) is not None

    def completions(self, prefixe):
        noeud, resultat = self._noeud(prefixe), []
        if noeud is None:
            return resultat

        def parcourir(n, acc):
            if n.fin:
                resultat.append("".join(acc))
            for c in sorted(n.enfants):
                acc.append(c)
                parcourir(n.enfants[c], acc)
                acc.pop()

        parcourir(noeud, list(prefixe))
        return resultat


t = Trie()
for mot in ["tea", "ten", "to", "inn", "in", "i"]:
    t.inserer(mot)
print(t.contient("tea"), t.contient("te"), t.commence_par("te"))   # True False True
print(t.completions("te"), t.completions("i"))                       # ['tea', 'ten'] ['i', 'in', 'inn']
```

Complexités (avec `L` la longueur du mot ou du préfixe) : `inserer`, `contient` et `commence_par` en **O(L)**, indépendamment du nombre de mots stockés ; `completions` en **O(L + taille du sous-arbre parcouru)**, c'est-à-dire proportionnel au nombre de caractères des mots renvoyés. Espace O(total des caractères) dans le pire cas.

**Exercice 24.5.3**

Ajoutez un compteur à chaque nœud pour répondre à « combien de mots du dictionnaire commencent par ce préfixe ? » en O(L).

**Correction**

On ajoute à chaque nœud un compteur : le **nombre de mots qui passent par ce nœud** (incrémenté à chaque insertion). Le nombre de mots commençant par un préfixe est la valeur du compteur du nœud atteint en suivant le préfixe : O(L).

```python
def nombre_de_mots_avec_prefixe(trie, prefixe):
    noeud = trie._noeud(prefixe)
    return noeud.compte if noeud is not None else 0


t = Trie()                                     # la classe de l'exercice 24.5.2 (avec le champ compte)
for mot in ["tea", "ten", "to", "inn", "in", "i"]:
    t.inserer(mot)
print(nombre_de_mots_avec_prefixe(t, "t"))     # 3 (tea, ten, to)
print(nombre_de_mots_avec_prefixe(t, "in"))    # 2 (in, inn)
print(nombre_de_mots_avec_prefixe(t, "z"))     # 0
```

Si les mots peuvent être insérés plusieurs fois, on incrémente toujours les compteurs ; pour compter des mots **distincts**, on ne les incrémente que si le mot n'était pas déjà présent. Coût : O(L), indépendant de la taille du dictionnaire.

**Exercice 24.5.4**

Autocomplétion : étant donné un dictionnaire avec une fréquence par mot, renvoyez les 3 mots les plus fréquents commençant par un préfixe donné.

**Correction**

Dans chaque nœud, on conserve la liste des **3 meilleurs mots** (par fréquence) qui passent par ce nœud, mise à jour à l'insertion ; une suggestion coûte alors O(L).

```python
class TrieFrequences:
    def __init__(self):
        self.enfants = {}
        self.meilleurs = []                     # liste de (-fréquence, mot), au plus 3 éléments

    def inserer(self, mot, frequence):
        noeud = self
        for c in mot:
            noeud = noeud.enfants.setdefault(c, TrieFrequences())
            noeud.meilleurs = sorted(noeud.meilleurs + [(-frequence, mot)])[:3]

    def suggestions(self, prefixe):
        noeud = self
        for c in prefixe:
            if c not in noeud.enfants:
                return []
            noeud = noeud.enfants[c]
        return [mot for _, mot in noeud.meilleurs]


t = TrieFrequences()
for mot, f in [("apple", 50), ("app", 100), ("application", 20),
               ("apply", 70), ("banana", 5), ("apt", 30)]:
    t.inserer(mot, f)
print(t.suggestions("ap"))     # ['app', 'apply', 'apple']
print(t.suggestions("b"))      # ['banana']
print(t.suggestions("z"))      # []
```

Variante sans listes dans les nœuds : parcourir tous les mots du sous-arbre du préfixe et garder les 3 plus fréquents avec `heapq.nlargest` : O(L + taille du sous-arbre) par requête, plus lent mais moins gourmand en mémoire.

**Exercice 24.5.5**

Recherche de mots dans une grille : étant donné une grille de lettres et une liste de mots, trouvez tous les mots présents, en utilisant un trie pour élaguer le retour sur trace. *(défi)*

**Correction**

On construit un trie des mots à chercher, puis on explore la grille par retour sur trace (déplacements dans 4 directions, sans réutiliser une case) en **suivant le trie en même temps** : dès que le préfixe courant n'est pas dans le trie, on coupe la branche.

```python
def mots_dans_la_grille(grille, mots):
    racine = {}
    for mot in mots:
        noeud = racine
        for c in mot:
            noeud = noeud.setdefault(c, {})
        noeud["$"] = mot                         # fin de mot : on mémorise le mot lui-même
    trouves = set()
    m, n = len(grille), len(grille[0])

    def explorer(i, j, noeud):
        c = grille[i][j]
        if c not in noeud:
            return                               # élagage : aucun mot ne commence ainsi
        suivant = noeud[c]
        if "$" in suivant:
            trouves.add(suivant["$"])
        grille[i][j] = "#"                       # case marquée comme utilisée
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            a, b = i + di, j + dj
            if 0 <= a < m and 0 <= b < n and grille[a][b] != "#":
                explorer(a, b, suivant)
        grille[i][j] = c                         # retour sur trace

    for i in range(m):
        for j in range(n):
            explorer(i, j, racine)
    return sorted(trouves)


grille = [list("oaan"), list("etae"), list("ihkr"), list("iflv")]
print(mots_dans_la_grille(grille, ["oath", "pea", "eat", "rain"]))   # ['eat', 'oath']
```

Sans le trie, il faudrait relancer une recherche complète pour chaque mot (O(`k` · `m` · `n` · 4ᴸ)). Avec le trie, toutes les recherches partagent leurs préfixes et les branches sans issue sont coupées immédiatement ; le coût est borné par O(`m` · `n` · 4ᴸ) au pire cas mais très inférieur en pratique.

**Exercice 24.5.6**

Plus grand XOR de deux nombres d'une liste : utilisez un trie binaire des écritures en bits. *(défi)*

**Correction**

On insère les écritures binaires (sur le même nombre de bits `B`) des nombres dans un trie binaire ; pour chaque `x`, on cherche dans le trie le nombre qui maximise `x XOR y` en prenant à chaque niveau, quand c'est possible, le bit **opposé** à celui de `x` (un bit à 1 dans le résultat vaut davantage que tous les bits de poids inférieurs réunis).

```python
def plus_grand_xor(t):
    bits = max(t).bit_length() or 1
    racine = {}
    for x in t:
        noeud = racine
        for i in range(bits - 1, -1, -1):
            noeud = noeud.setdefault((x >> i) & 1, {})
    meilleur = 0
    for x in t:
        noeud, courant = racine, 0
        for i in range(bits - 1, -1, -1):
            b = (x >> i) & 1
            if (1 - b) in noeud:                 # on peut mettre un 1 dans le résultat
                courant |= 1 << i
                noeud = noeud[1 - b]
            else:
                noeud = noeud[b]
        meilleur = max(meilleur, courant)
    return meilleur


print(plus_grand_xor([3, 10, 5, 25, 2, 8]))   # 28 (5 XOR 25)
```

Complexité **O(n · B)** (B = nombre de bits, par exemple 32), soit O(n), contre O(n²) pour la comparaison de toutes les paires.

**Exercice 24.5.7**

Routage IP : expliquez comment un trie binaire permet de trouver le préfixe le plus long correspondant à une adresse.

**Correction**

Un **trie binaire** stocke les préfixes du routage (chaque préfixe est une suite de bits, par exemple le préfixe `10` de longueur 2). Chaque nœud correspondant à un préfixe de la table porte la **route** associée. Pour une adresse (32 bits en IPv4), on descend dans le trie bit par bit et on **mémorise la dernière route rencontrée** : à la fin de la descente (ou quand le chemin disparaît), cette dernière route est celle du **préfixe le plus long** qui correspond à l'adresse (règle du *longest prefix match*).

```python
class RoutageIP:
    def __init__(self):
        self.racine = {}

    def ajouter(self, prefixe_bits, route):
        noeud = self.racine
        for b in prefixe_bits:
            noeud = noeud.setdefault(b, {})
        noeud["route"] = route

    def chercher(self, adresse_bits):
        noeud = self.racine
        meilleure = noeud.get("route")               # route par défaut éventuelle
        for b in adresse_bits:
            if b not in noeud:
                break
            noeud = noeud[b]
            if "route" in noeud:
                meilleure = noeud["route"]
        return meilleure


r = RoutageIP()
r.ajouter("", "défaut")
r.ajouter("10", "A")
r.ajouter("1011", "B")
print(r.chercher("10110001"), r.chercher("10010000"), r.chercher("01000000"))
# B A défaut
```

Coût d'une recherche : **O(longueur de l'adresse en bits)** (32 pour IPv4), indépendamment du nombre de préfixes. Les routeurs utilisent des variantes compressées (arbres de Patricia) ou du matériel dédié.

## 24.6 Autres outils

**Exercice 24.6.1**

Algorithme de Manacher : calculez à la main les rayons de palindromes pour `"abacaba"`. Utilisez-les pour trouver la plus longue sous-chaîne palindromique.

**Correction**

Pour chaque centre `i`, `d1[i]` est le nombre de palindromes **de longueur impaire** centrés en `i` (rayon, centre compris) et `d2[i]` le nombre de palindromes **de longueur paire** centrés entre `i − 1` et `i`.

Pour `"abacaba"` (`a b a c a b a`) :

| `i` | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Lettre | a | b | a | c | a | b | a |
| `d1[i]` | 1 | 2 | 1 | 4 | 1 | 2 | 1 |
| `d2[i]` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Détail : en `i = 1`, `s[0] = s[2]` donne le palindrome `"aba"` (rayon 2) ; en `i = 3`, on étend `c`, `aca`, `bacab`, `abacaba` (rayon 4) ; en `i = 4, 5, 6`, Manacher réutilise par symétrie les valeurs des centres 2, 1, 0 sans nouvelle comparaison (cette réutilisation du plus grand palindrome déjà trouvé `[0, 6]` rend l'algorithme linéaire). Il n'y a aucun palindrome de longueur paire : `d2` est nul.

La plus longue sous-chaîne palindromique correspond à `max(2 · d1[i] − 1, 2 · d2[i])` : ici `2 · 4 − 1 = 7` en `i = 3`, donc c'est la chaîne entière **`"abacaba"`**.

```python
def manacher(s):
    n = len(s)
    d1, d2 = [0] * n, [0] * n
    gauche, droite = 0, -1
    for i in range(n):
        k = 1 if i > droite else min(d1[gauche + droite - i], droite - i + 1)
        while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
            k += 1
        d1[i] = k
        if i + k - 1 > droite:
            gauche, droite = i - k + 1, i + k - 1
    gauche, droite = 0, -1
    for i in range(n):
        k = 0 if i > droite else min(d2[gauche + droite - i + 1], droite - i + 1)
        while i - k - 1 >= 0 and i + k < n and s[i - k - 1] == s[i + k]:
            k += 1
        d2[i] = k
        if i + k - 1 > droite:
            gauche, droite = i - k, i + k - 1
    return d1, d2


def plus_longue_palindrome(s):
    d1, d2 = manacher(s)
    debut, longueur = 0, 0
    for i in range(len(s)):
        if 2 * d1[i] - 1 > longueur:
            debut, longueur = i - d1[i] + 1, 2 * d1[i] - 1
        if 2 * d2[i] > longueur:
            debut, longueur = i - d2[i], 2 * d2[i]
    return s[debut:debut + longueur]


print(manacher("abacaba"))                  # ([1, 2, 1, 4, 1, 2, 1], [0, 0, 0, 0, 0, 0, 0])
print(plus_longue_palindrome("abacaba"), plus_longue_palindrome("cbbd"))   # abacaba bb
```

Complexité **O(n)**.

**Exercice 24.6.2**

Calculez à la main le tableau des suffixes et le tableau LCP de `"banana"`. Utilisez-les pour trouver la plus longue sous-chaîne répétée.

**Correction**

Suffixes de `"banana"` : `0 : banana`, `1 : anana`, `2 : nana`, `3 : ana`, `4 : na`, `5 : a`. Triés par ordre lexicographique :

| Rang | Suffixe | Indice de départ | LCP avec le suffixe précédent |
| --- | --- | --- | --- |
| 0 | `a` | 5 | |
| 1 | `ana` | 3 | 1 (`a`) |
| 2 | `anana` | 1 | 3 (`ana`) |
| 3 | `banana` | 0 | 0 |
| 4 | `na` | 4 | 0 |
| 5 | `nana` | 2 | 2 (`na`) |

**Tableau des suffixes** : `SA = [5, 3, 1, 0, 4, 2]`. **Tableau LCP** (entre suffixes consécutifs du tri) : `[1, 3, 0, 0, 2]` (la première case, sans suffixe précédent, est 0 par convention).

**Plus longue sous-chaîne répétée** : toute sous-chaîne qui apparaît deux fois est un préfixe commun de deux suffixes ; les suffixes les plus proches dans l'ordre trié sont ceux qui partagent le plus long préfixe, donc il suffit de prendre le **maximum du tableau LCP** : ici `3`, obtenu entre `anana` et `ana` : la sous-chaîne répétée est **`"ana"`** (aux positions 1 et 3, avec chevauchement).

```python
def tableau_suffixes(s):
    return sorted(range(len(s)), key=lambda i: s[i:])


def lcp(a, b):
    k = 0
    while k < len(a) and k < len(b) and a[k] == b[k]:
        k += 1
    return k


s = "banana"
sa = tableau_suffixes(s)
valeurs = [lcp(s[sa[i - 1]:], s[sa[i]:]) for i in range(1, len(sa))]
print(sa, valeurs)                           # [5, 3, 1, 0, 4, 2] [1, 3, 0, 0, 2]
meilleur = max(range(len(valeurs)), key=lambda i: valeurs[i])
print(s[sa[meilleur + 1]:sa[meilleur + 1] + valeurs[meilleur]])   # ana
```

Cette construction par tri est en O(n² log n) ; l'algorithme de doublement de préfixes donne O(n log n), et l'algorithme de Kasai calcule le LCP en O(n).

**Exercice 24.6.3**

Implémentez le hachage polynomial avec précalcul des préfixes et des puissances, afin de comparer deux sous-chaînes en O(1). Utilisez-le pour tester si deux sous-chaînes de même longueur sont égales, sur 10⁵ requêtes.

**Correction**

On précalcule `h[i]` = hachage du préfixe `s[:i]` et `p[i] = base^i` ; le hachage de `s[l:r]` vaut `(h[r] − h[l] · p[r − l]) mod q`.

```python
import random


class HachagePolynomial:
    def __init__(self, s, base=None, module=(1 << 61) - 1):
        self.q = module
        self.base = base or random.randint(10**5, module - 1)      # base aléatoire
        n = len(s)
        self.h = [0] * (n + 1)
        self.p = [1] * (n + 1)
        for i, c in enumerate(s):
            self.h[i + 1] = (self.h[i] * self.base + ord(c)) % module
            self.p[i + 1] = self.p[i] * self.base % module

    def sous_chaine(self, l, r):
        """Hachage de s[l:r] en O(1)."""
        return (self.h[r] - self.h[l] * self.p[r - l]) % self.q

    def egales(self, i, j, longueur):
        return self.sous_chaine(i, i + longueur) == self.sous_chaine(j, j + longueur)


texte = "".join(random.choice("ab") for _ in range(2000))
H = HachagePolynomial(texte)
for _ in range(10_000):                           # comparaison avec le calcul direct
    L = random.randint(1, 50)
    i, j = random.randint(0, 2000 - L), random.randint(0, 2000 - L)
    assert H.egales(i, j, L) == (texte[i:i + L] == texte[j:j + L])
print("10 000 requêtes vérifiées")
```

Précalcul en O(n), puis **chaque requête en O(1)** : pour 10⁵ requêtes, le coût total est de l'ordre de 10⁵ opérations, contre O(10⁵ · L) pour des comparaisons directes. Avec un module de 61 bits, la probabilité d'erreur par comparaison est de l'ordre de `n / 2⁶¹`, négligeable.

**Exercice 24.6.4**

Décrivez le fonctionnement d'Aho-Corasick sur l'ensemble de motifs `{"he", "she", "his", "hers"}` : construction du trie, liens d'échec, puis recherche dans le texte `"ushers"`. *(défi)*

**Correction**

Aho-Corasick recherche **simultanément** plusieurs motifs en un seul parcours du texte, en O(n + total des longueurs des motifs + nombre d'occurrences).

**1. Trie des motifs** `{he, she, his, hers}` (les nœuds sont numérotés dans l'ordre d'insertion) :

```text
0 (racine)
├── h (1)
│   ├── e (2) *he
│   │   └── r (8)
│   │       └── s (9) *hers
│   └── i (6)
│       └── s (7) *his
└── s (3)
    └── h (4)
        └── e (5) *she
```

**2. Liens d'échec** : le lien d'échec d'un nœud pointe vers le plus long suffixe propre de son chemin qui est aussi un chemin du trie (comme la table de KMP). Ils se calculent par BFS.

| Nœud | Chemin | Lien d'échec | Explication |
| --- | --- | --- | --- |
| 1 | `h` | racine | |
| 3 | `s` | racine | |
| 2 | `he` | racine | `e` n'est pas un nœud |
| 4 | `sh` | 1 (`h`) | le suffixe `h` existe |
| 6 | `hi` | racine | |
| 5 | `she` | 2 (`he`) | le suffixe `he` existe |
| 7 | `his` | 3 (`s`) | le suffixe `s` existe |
| 8 | `her` | racine | |
| 9 | `hers` | 3 (`s`) | le suffixe `s` existe |

On propage aussi les **sorties** : le nœud 5 (`she`) émet `she` et, par son lien d'échec vers `he`, également `he`.

**3. Recherche dans `"ushers"`** (`u s h e r s`) :

| Caractère | État | Événement |
| --- | --- | --- |
| `u` | racine | pas de transition |
| `s` | 3 (`s`) | |
| `h` | 4 (`sh`) | |
| `e` | 5 (`she`) | **sorties : `she` (position 1) et `he` (position 2)** |
| `r` | 8 (`her`) | pas de fils `r` sous `she` : lien d'échec vers `he`, puis transition `r` vers `her` |
| `s` | 9 (`hers`) | **sortie : `hers` (position 2)** |

Occurrences : `she` en 1, `he` en 2, `hers` en 2.

```python
from collections import deque


class AhoCorasick:
    def __init__(self, motifs):
        self.transitions = [{}]
        self.echec = [0]
        self.sorties = [[]]
        for mot in motifs:
            noeud = 0
            for c in mot:
                if c not in self.transitions[noeud]:
                    self.transitions.append({})
                    self.echec.append(0)
                    self.sorties.append([])
                    self.transitions[noeud][c] = len(self.transitions) - 1
                noeud = self.transitions[noeud][c]
            self.sorties[noeud].append(mot)
        file = deque(self.transitions[0].values())
        while file:
            u = file.popleft()
            for c, v in self.transitions[u].items():
                k = self.echec[u]
                while k and c not in self.transitions[k]:
                    k = self.echec[k]
                self.echec[v] = self.transitions[k].get(c, 0)
                self.sorties[v] = self.sorties[v] + self.sorties[self.echec[v]]
                file.append(v)

    def chercher(self, texte):
        noeud, resultats = 0, []
        for i, c in enumerate(texte):
            while noeud and c not in self.transitions[noeud]:
                noeud = self.echec[noeud]
            noeud = self.transitions[noeud].get(c, 0)
            for mot in self.sorties[noeud]:
                resultats.append((i - len(mot) + 1, mot))
        return resultats


print(AhoCorasick(["he", "she", "his", "hers"]).chercher("ushers"))
# [(1, 'she'), (2, 'he'), (2, 'hers')]
```

**Exercice 24.6.5**

Rappelez la définition de la distance d'édition. Calculez-la pour `"intention"` et `"execution"`.

**Correction**

La **distance d'édition** (de Levenshtein) entre deux chaînes est le nombre minimal d'opérations élémentaires (insertion, suppression, remplacement d'un caractère, chacune de coût 1) pour transformer l'une en l'autre. Avec `D[i][j]` la distance entre `a[:i]` et `b[:j]` : `D[i][0] = i`, `D[0][j] = j`, et `D[i][j] = min(D[i − 1][j] + 1, D[i][j − 1] + 1, D[i − 1][j − 1] + (a[i − 1] ≠ b[j − 1]))`.

Tableau pour `"intention"` (lignes) et `"execution"` (colonnes) :

| | | e | x | e | c | u | t | i | o | n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| **i** | 1 | 1 | 2 | 3 | 4 | 5 | 6 | 6 | 7 | 8 |
| **n** | 2 | 2 | 2 | 3 | 4 | 5 | 6 | 7 | 7 | 7 |
| **t** | 3 | 3 | 3 | 3 | 4 | 5 | 5 | 6 | 7 | 8 |
| **e** | 4 | 3 | 4 | 3 | 4 | 5 | 6 | 6 | 7 | 8 |
| **n** | 5 | 4 | 4 | 4 | 4 | 5 | 6 | 7 | 7 | 7 |
| **t** | 6 | 5 | 5 | 5 | 5 | 5 | 5 | 6 | 7 | 8 |
| **i** | 7 | 6 | 6 | 6 | 6 | 6 | 6 | 5 | 6 | 7 |
| **o** | 8 | 7 | 7 | 7 | 7 | 7 | 7 | 6 | 5 | 6 |
| **n** | 9 | 8 | 8 | 8 | 8 | 8 | 8 | 7 | 6 | 5 |

La distance d'édition est `D[9][9] = ` **5** : ce sont 5 remplacements aux mêmes positions : `i → e`, `n → x`, `t → e`, `e → c`, `n → u` (les 4 derniers caractères `tion` sont déjà égaux). (Si le remplacement coûtait 2, comme dans certaines conventions, la distance serait 8.)

## 24.7 Comparaison des recherches de motif

**Exercice 24.7.1**

Complétez le tableau :

| Algorithme | Précalcul | Recherche | Remarque |
| --- | --- | --- | --- |
| Naïf | | | |
| KMP | | | |
| Rabin-Karp | | | |
| Z | | | |

**Correction**

| Algorithme | Précalcul | Recherche | Remarque |
| --- | --- | --- | --- |
| Naïf | aucun | O(n · m) au pire, souvent proche de O(n) | très simple ; rapide pour de courts motifs ; pire cas sur des textes répétitifs |
| KMP | O(m) (table des préfixes) | **O(n)** | garantie déterministe, pas de retour en arrière dans le texte |
| Rabin-Karp | O(m) | O(n + m) en moyenne, O(n · m) au pire (collisions) | hachage glissant ; adapté à la recherche de **plusieurs motifs** de même longueur et aux comparaisons de sous-chaînes |
| Z | O(n + m) (tableau Z de `motif # texte`) | O(n + m) | simple et déterministe ; utile aussi pour les périodes et les préfixes |

**Exercice 24.7.2**

Pour chaque situation, choisissez l'algorithme et justifiez : un motif très court recherché une seule fois, un texte énorme avec un motif de 10⁵ caractères, la recherche de 1000 motifs simultanés, la détection de plagiat par sous-chaînes communes.

**Correction**

- **Motif très court recherché une seule fois** : la **recherche naïve** (ou directement `str.find`) : le précalcul de KMP ou le hachage de Rabin-Karp ne se rentabilisent pas, et le coût est proche de O(n).
- **Texte énorme avec un motif de 10⁵ caractères** : **KMP** (ou l'algorithme Z) pour la garantie O(n + m) : le naïf risque O(n · m) = 10¹⁴ au pire ; Rabin-Karp fonctionne aussi mais reste probabiliste.
- **Recherche de 1000 motifs simultanés** : **Aho-Corasick**, en un seul parcours du texte (O(n + somme des longueurs + occurrences)) ; Rabin-Karp multiple convient si les motifs ont la même longueur.
- **Détection de plagiat par sous-chaînes communes** : **hachage polynomial** (Rabin-Karp) avec recherche binaire sur la longueur, ou hachage de k-grammes (empreintes, *winnowing*) ; pour une garantie exacte, un tableau ou un automate des suffixes.

**Exercice 24.7.3**

Chronométrez `str.find`, la recherche naïve, KMP et Rabin-Karp sur un texte aléatoire de 10⁶ caractères. Commentez.

**Correction**

```python
import random
import time

random.seed(3)
texte = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(10**6))
motif = texte[-30:]


def toutes_positions(texte, motif):              # str.find, appelé en boucle
    resultat, i = [], texte.find(motif)
    while i != -1:
        resultat.append(i)
        i = texte.find(motif, i + 1)
    return resultat


for nom, f in (("str.find", toutes_positions), ("naïve", recherche_naive),
               ("KMP", kmp), ("Rabin-Karp", rabin_karp)):
    debut = time.time()
    positions = f(texte, motif)
    print(nom, round(time.time() - debut, 3), "s", positions)
```

Résultats typiques pour un texte aléatoire de 10⁶ caractères (alphabet de 26 lettres) :

| Méthode | Temps |
| --- | --- |
| `str.find` | environ 0,001 s |
| Recherche naïve | environ 0,06 s |
| KMP | environ 0,05 s |
| Rabin-Karp | environ 0,24 s |

Commentaires : `str.find` est écrit en C avec des optimisations (Boyer-Moore-Horspool et variantes) et domine de loin. Sur un texte aléatoire, la recherche naïve s'arrête presque tout de suite à chaque position, et se comporte comme O(n) ; KMP est aussi linéaire, avec un coût un peu plus faible ici. Rabin-Karp est le plus lent à cause du calcul de hachage à chaque caractère (opérations sur grands entiers). La différence apparaît dans le **pire cas** : pour un texte de 200 000 `a` et un motif `a`×50 suivi de `b`, la recherche naïve prend environ 0,56 s, contre 0,02 s pour KMP et 0,001 s pour `str.find` : seuls les algorithmes à garantie linéaire résistent aux textes répétitifs.

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

**Correction**

**1. Ancêtre commun le plus bas (LCA).** Dans un arbre enraciné, le LCA de deux nœuds `u` et `v` est le nœud le plus profond qui est ancêtre (ou égal) de `u` et de `v`. Méthode simple : on remonte le plus profond des deux jusqu'à la même profondeur, puis on remonte les deux ensemble jusqu'à ce qu'ils coïncident (O(h) par requête) ; avec le saut binaire ou une tournée d'Euler et une table creuse, on obtient O(log n) ou O(1) par requête.

Arbre de 7 nœuds : racine `1` ; enfants de `1` : `2, 3` ; enfants de `2` : `4, 5` ; enfants de `3` : `6, 7`.

| Requête | Résultat | Justification |
| --- | --- | --- |
| `LCA(4, 5)` | `2` | 4 et 5 sont les deux enfants de 2 |
| `LCA(4, 6)` | `1` | 4 est dans le sous-arbre de 2, 6 dans celui de 3 : le premier ancêtre commun est la racine |
| `LCA(6, 7)` | `3` | enfants de 3 |
| `LCA(2, 4)` | `2` | 2 est ancêtre de 4 |

```python
parent = {1: None, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 3}
profondeur = {1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 2}


def lca(u, v):
    while profondeur[u] > profondeur[v]:
        u = parent[u]
    while profondeur[v] > profondeur[u]:
        v = parent[v]
    while u != v:
        u, v = parent[u], parent[v]
    return u


print(lca(4, 5), lca(4, 6), lca(6, 7), lca(2, 4))   # 2 1 3 2
```

**2. Enveloppe convexe (parcours de Graham).** L'enveloppe convexe d'un ensemble de points est le plus petit polygone convexe qui les contient tous. Graham : on choisit le point le plus bas (puis le plus à gauche), on trie les autres par angle polaire autour de lui, puis on parcourt en maintenant une pile : tant que les deux derniers points de la pile et le nouveau point ne forment pas un **virage à gauche** (produit vectoriel `> 0`), on dépile. Complexité O(n log n).

Points : `(0,3), (1,1), (2,2), (4,4), (0,0), (1,2), (3,1), (3,3)`. Point de départ : `(0,0)`. Tri par angle (à angle égal, par distance) : `(3,1), (1,1), (2,2), (3,3), (4,4), (1,2), (0,3)`.

| Point traité | Action | Pile après |
| --- | --- | --- |
| `(3,1)` | empiler | `(0,0), (3,1)` |
| `(1,1)` | empiler | `(0,0), (3,1), (1,1)` |
| `(2,2)` | virage à droite en `(1,1)` : dépiler `(1,1)`, puis empiler | `(0,0), (3,1), (2,2)` |
| `(3,3)` | dépiler `(2,2)` (virage à droite), puis empiler | `(0,0), (3,1), (3,3)` |
| `(4,4)` | dépiler `(3,3)`, puis empiler | `(0,0), (3,1), (4,4)` |
| `(1,2)` | empiler | `(0,0), (3,1), (4,4), (1,2)` |
| `(0,3)` | dépiler `(1,2)` (virage à droite), puis empiler | `(0,0), (3,1), (4,4), (0,3)` |

Enveloppe : **`(0,0), (3,1), (4,4), (0,3)`** (dans le sens antihoraire).

```python
import math


def produit_vectoriel(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def graham(points):
    depart = min(points, key=lambda p: (p[1], p[0]))
    autres = sorted((p for p in points if p != depart),
                    key=lambda p: (math.atan2(p[1] - depart[1], p[0] - depart[0]),
                                   (p[0] - depart[0]) ** 2 + (p[1] - depart[1]) ** 2))
    pile = [depart]
    for p in autres:
        while len(pile) > 1 and produit_vectoriel(pile[-2], pile[-1], p) <= 0:
            pile.pop()
        pile.append(p)
    return pile


print(graham([(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]))
# [(0, 0), (3, 1), (4, 4), (0, 3)]
```

**3. Nombres de Grundy pour le jeu de Nim à deux tas (3 et 5).** Le nombre de Grundy d'une position est le plus petit entier naturel (mex) absent de l'ensemble des nombres de Grundy des positions atteignables ; une position est perdante pour le joueur qui doit jouer si et seulement si son nombre de Grundy est 0. Pour un seul tas de taille `n`, on atteint les positions `0, ..., n − 1`, donc `G(n) = mex{0, ..., n − 1} = n`. Pour une somme de jeux, le nombre de Grundy est le **XOR** des nombres de Grundy : `G(3, 5) = 3 XOR 5 = 011 XOR 101 = 110 = ` **6**. Il est non nul : la position est **gagnante** pour le premier joueur. Coup gagnant : il faut ramener le XOR à 0 ; `5 XOR 6 = 3 < 5` : réduire le tas de 5 à 3 (retirer 2), ce qui donne `(3, 3)` de XOR 0 (on vérifie par un calcul direct du mex que `G(a, b) = a XOR b` pour tous les `a, b ≤ 8`).

**4. Nombre de Catalan `C₅`.** `Cₙ = C(2n, n) / (n + 1)` compte, entre autres, les mots de parenthèses bien formés à `n` paires, les arbres binaires à `n` nœuds, les triangulations d'un polygone à `n + 2` côtés. Ici `C₅ = C(10, 5) / 6 = 252 / 6 = ` **42**. (Suite : 1, 1, 2, 5, 14, 42, 132...)

**5. Circuit eulérien.** Un circuit eulérien passe **une fois et une seule** par chaque arête et revient à son point de départ. **Conditions d'existence** : pour un graphe non orienté, tous les sommets de degré non nul sont dans la même composante connexe **et** tous les degrés sont **pairs** ; pour un graphe orienté, tous les sommets ont un degré entrant égal au degré sortant et les arêtes sont dans une seule composante fortement connexe.

Exemple : deux triangles qui partagent le sommet 0, avec les arêtes `(0,1), (1,2), (2,0), (0,3), (3,4), (4,0)`. Degrés : `0 : 4`, `1, 2, 3, 4 : 2`, tous pairs, graphe connexe : le circuit existe, par exemple `0 → 1 → 2 → 0 → 3 → 4 → 0`. Algorithme de Hierholzer en O(n + m) :

```python
def circuit_eulerien(n, aretes):
    graphe = [[] for _ in range(n)]
    for i, (u, v) in enumerate(aretes):
        graphe[u].append((v, i))
        graphe[v].append((u, i))
    utilisee = [False] * len(aretes)
    pile, circuit = [0], []
    while pile:
        u = pile[-1]
        while graphe[u] and utilisee[graphe[u][-1][1]]:
            graphe[u].pop()
        if graphe[u]:
            v, i = graphe[u].pop()
            utilisee[i] = True
            pile.append(v)
        else:
            circuit.append(pile.pop())
    return circuit[::-1]


print(circuit_eulerien(5, [(0, 1), (1, 2), (2, 0), (0, 3), (3, 4), (4, 0)]))
# [0, 4, 3, 0, 2, 1, 0]
```

**6. Instance de 2-SAT à 4 variables.** Une formule 2-CNF est un ET de clauses de deux littéraux. Chaque clause `(a ∨ b)` équivaut aux implications `¬a → b` et `¬b → a`. La formule est **satisfaisable si et seulement si aucune variable n'est dans la même composante fortement connexe que sa négation**.

Instance : `(x₁ ∨ x₂) ∧ (¬x₁ ∨ x₃) ∧ (¬x₂ ∨ ¬x₃) ∧ (x₃ ∨ x₄) ∧ (¬x₄ ∨ ¬x₁)`.

Graphe d'implications (10 arcs) :

| Clause | Implications |
| --- | --- |
| `x₁ ∨ x₂` | `¬x₁ → x₂`, `¬x₂ → x₁` |
| `¬x₁ ∨ x₃` | `x₁ → x₃`, `¬x₃ → ¬x₁` |
| `¬x₂ ∨ ¬x₃` | `x₂ → ¬x₃`, `x₃ → ¬x₂` |
| `x₃ ∨ x₄` | `¬x₃ → x₄`, `¬x₄ → x₃` |
| `¬x₄ ∨ ¬x₁` | `x₄ → ¬x₁`, `x₁ → ¬x₄` |

Composantes fortement connexes : **`{x₁, x₃, ¬x₂, ¬x₄}`** (cycle `x₁ → x₃ → ¬x₂ → x₁`, plus `x₁ → ¬x₄ → x₃`) et **`{¬x₁, x₂, ¬x₃, x₄}`**. Aucune variable n'est avec sa négation : la formule est satisfaisable. On peut prendre vrais les littéraux d'une composante (en prenant, avec Tarjan, ceux dont la composante est numérotée avant celle de leur négation) : `x₁ = V`, `x₂ = F`, `x₃ = V`, `x₄ = F`. Vérification : `(V∨F) ∧ (F∨V) ∧ (V∨F) ∧ (V∨F) ∧ (V∨F)` est vrai. (Contre-exemple d'instance insatisfaisable : `(x ∨ y) ∧ (x ∨ ¬y) ∧ (¬x ∨ y) ∧ (¬x ∨ ¬y)`, où `x` et `¬x` tombent dans la même composante.)

**Exercice 25.1.2**

Jeu de Nim : écrivez une fonction qui décide si le joueur qui commence gagne avec les tas donnés (XOR des tailles) et indique un coup gagnant.

**Correction**

**Théorème de Bouton** : le premier joueur gagne si et seulement si le **XOR** des tailles des tas est non nul. Pour jouer, il choisit un tas `t` tel que `t XOR X < t` (où `X` est le XOR total) et le réduit à `t XOR X`.

```python
def nim(tas):
    """Renvoie (gagnant ?, coup) où coup = (indice du tas, nombre d'objets à retirer)."""
    x = 0
    for t in tas:
        x ^= t
    if x == 0:
        return False, None                      # position perdante pour qui doit jouer
    for i, t in enumerate(tas):
        if t ^ x < t:
            return True, (i, t - (t ^ x))


print(nim([3, 5]))          # (True, (1, 2)) : retirer 2 objets du tas 1 (de 5 à 3)
print(nim([1, 2, 3]))       # (False, None)  : 1 XOR 2 XOR 3 = 0
print(nim([4, 5, 6, 7]))    # (False, None)
```

Preuve : depuis une position de XOR 0, tout coup change un seul tas, donc le XOR devient non nul ; depuis une position de XOR non nul, il existe un coup qui le ramène à 0. La position terminale (tous les tas vides) a un XOR 0 : celui qui rend toujours le XOR nul gagne. Complexité O(n).

**Exercice 25.1.3**

Écrivez un petit moteur de minimax avec élagage alpha-bêta pour le morpion. Comptez le nombre de positions explorées avec et sans élagage.

**Correction**

```python
LIGNES = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


def gagnant(b):
    for a, c, d in LIGNES:
        if b[a] != "." and b[a] == b[c] == b[d]:
            return b[a]
    return None


compteur = [0]


def minimax(b, joueur):
    compteur[0] += 1
    g = gagnant(b)
    if g:
        return 1 if g == "X" else -1
    if "." not in b:
        return 0
    valeurs = []
    for i in range(9):
        if b[i] == ".":
            b[i] = joueur
            valeurs.append(minimax(b, "O" if joueur == "X" else "X"))
            b[i] = "."
    return max(valeurs) if joueur == "X" else min(valeurs)


def alpha_beta(b, joueur, alpha, beta):
    compteur[0] += 1
    g = gagnant(b)
    if g:
        return 1 if g == "X" else -1
    if "." not in b:
        return 0
    if joueur == "X":                              # joueur maximisant
        v = -2
        for i in range(9):
            if b[i] == ".":
                b[i] = "X"
                v = max(v, alpha_beta(b, "O", alpha, beta))
                b[i] = "."
                alpha = max(alpha, v)
                if alpha >= beta:                  # coupure bêta
                    break
        return v
    v = 2                                          # joueur minimisant
    for i in range(9):
        if b[i] == ".":
            b[i] = "O"
            v = min(v, alpha_beta(b, "X", alpha, beta))
            b[i] = "."
            beta = min(beta, v)
            if alpha >= beta:                      # coupure alpha
                break
    return v


compteur[0] = 0
print(minimax(["."] * 9, "X"), compteur[0])             # 0 549946
compteur[0] = 0
print(alpha_beta(["."] * 9, "X", -2, 2), compteur[0])   # 0 18297
```

Valeur du jeu : `0` (partie nulle avec un jeu parfait). **Positions explorées depuis la grille vide** (en essayant les cases dans l'ordre 0 à 8) : **549 946** pour le minimax simple, contre **18 297** avec l'élagage alpha-bêta, soit environ 30 fois moins, pour le même résultat. Le gain dépend de l'ordre dans lequel on essaie les coups (meilleur ordre, plus de coupures).

**Exercice 25.1.4**

Écrivez l'exponentiation de matrices et utilisez-la pour calculer le `n`-ième terme de la suite `u₀ = 0`, `u₁ = 1`, `uₙ = 3uₙ₋₁ − uₙ₋₂`, modulo `10⁹ + 7`.

**Correction**

La récurrence `uₙ = 3uₙ₋₁ − uₙ₋₂` s'écrit `(uₙ, uₙ₋₁)ᵀ = A · (uₙ₋₁, uₙ₋₂)ᵀ` avec `A = [[3, −1], [1, 0]]` : donc `(uₙ, uₙ₋₁)ᵀ = Aⁿ⁻¹ · (u₁, u₀)ᵀ = Aⁿ⁻¹ · (1, 0)ᵀ`, et `uₙ` est le coefficient en haut à gauche de `Aⁿ⁻¹`. L'exponentiation rapide donne O(log n) produits de matrices 2 × 2.

```python
MOD = 10**9 + 7


def produit(A, B):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]]


def puissance_matrice(A, n):
    resultat = [[1, 0], [0, 1]]
    while n:
        if n & 1:
            resultat = produit(resultat, A)
        A = produit(A, A)
        n >>= 1
    return resultat


def u(n):
    if n == 0:
        return 0
    return puissance_matrice([[3, MOD - 1], [1, 0]], n - 1)[0][0]       # -1 ≡ MOD - 1


print([u(n) for n in range(10)])   # [0, 1, 3, 8, 21, 55, 144, 377, 987, 2584]
print(u(10**18))                    # 700290221
```

Les termes sont `0, 1, 3, 8, 21, 55, ...` : on reconnaît `uₙ = F₂ₙ` (termes pairs de Fibonacci), ce qui a été vérifié numériquement. `u(10¹⁸) mod (10⁹ + 7) = 700290221`, calculé en environ 60 produits de matrices.

**Exercice 25.1.5**

Inclusion-exclusion : combien d'entiers de `1` à `1000` ne sont divisibles ni par 2, ni par 3, ni par 5 ?

**Correction**

Soit `A₂`, `A₃`, `A₅` les ensembles des entiers de 1 à 1000 divisibles par 2, 3 et 5. Par inclusion-exclusion :

`|A₂ ∪ A₃ ∪ A₅| = |A₂| + |A₃| + |A₅| − |A₂ ∩ A₃| − |A₂ ∩ A₅| − |A₃ ∩ A₅| + |A₂ ∩ A₃ ∩ A₅|`

avec `|A₂| = 500`, `|A₃| = 333`, `|A₅| = 200`, `|A₆| = 166`, `|A₁₀| = 100`, `|A₁₅| = 66`, `|A₃₀| = 33` :

`500 + 333 + 200 − 166 − 100 − 66 + 33 = 734`.

Nombre d'entiers ni divisibles par 2, ni par 3, ni par 5 : `1000 − 734 = ` **266**.

Vérification : `sum(1 for k in range(1, 1001) if k % 2 and k % 3 and k % 5)` donne 266. (Autre calcul : `1000 × (1/2) × (2/3) × (4/5) ≈ 266,7`, ce qui est cohérent.)

**Exercice 25.1.6**

Implémentez une transformée de Fourier rapide (FFT) ou une NTT pour multiplier deux polynômes de degré `10⁵`. Comparez avec la multiplication naïve en O(n²). *(défi)*

**Correction**

On utilise la **transformée en nombres entiers (NTT)** modulo `998244353 = 119 × 2²³ + 1`, de racine primitive 3 : c'est une FFT exacte sur des entiers, sans erreur d'arrondi. La multiplication de deux polynômes se fait en trois étapes : transformer les deux polynômes (complétés par des zéros jusqu'à une puissance de 2), multiplier terme à terme, transformer en sens inverse. Complexité **O(n log n)**.

```python
MODULO = 998244353
RACINE = 3


def ntt(a, inverse=False):
    n = len(a)
    j = 0
    for i in range(1, n):                         # permutation par inversion de bits
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    longueur = 2
    while longueur <= n:
        w = pow(RACINE, (MODULO - 1) // longueur, MODULO)
        if inverse:
            w = pow(w, MODULO - 2, MODULO)
        for i in range(0, n, longueur):
            wn = 1
            for k in range(i, i + longueur // 2):
                x = a[k]
                y = a[k + longueur // 2] * wn % MODULO
                a[k] = (x + y) % MODULO
                a[k + longueur // 2] = (x - y) % MODULO
                wn = wn * w % MODULO
        longueur <<= 1
    if inverse:
        n_inverse = pow(n, MODULO - 2, MODULO)
        for i in range(n):
            a[i] = a[i] * n_inverse % MODULO


def multiplier(p, q):
    taille = 1
    while taille < len(p) + len(q) - 1:
        taille <<= 1
    fa = p + [0] * (taille - len(p))
    fb = q + [0] * (taille - len(q))
    ntt(fa)
    ntt(fb)
    c = [x * y % MODULO for x, y in zip(fa, fb)]
    ntt(c, inverse=True)
    return c[:len(p) + len(q) - 1]


def multiplication_naive(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i + j] = (r[i + j] + x * y) % MODULO
    return r
```

Le résultat de `multiplier` coïncide avec `multiplication_naive` sur des polynômes aléatoires (vérification sur des polynômes de degré 300).

Comparaison de temps (Python pur) :

| Degré | Naïve O(n²) | NTT O(n log n) |
| --- | --- | --- |
| 1 000 | 0,20 s | 0,013 s |
| 2 000 | 0,64 s | 0,030 s |
| 4 000 | 2,4 s | 0,088 s |
| 100 000 | de l'ordre de 25 minutes (extrapolé : 10¹⁰ opérations) | environ 3,6 s |

La multiplication naïve devient impraticable pour le degré `10⁵`, alors que la NTT l'effectue en quelques secondes (et en une fraction de seconde en langage compilé ou avec NumPy). Les coefficients du produit sont ici calculés modulo `998244353` ; une FFT en nombres complexes donnerait des résultats exacts pour des petits coefficients entiers, au prix d'erreurs d'arrondi sur les grandes valeurs.

## 25.2 Complexité et difficulté : P, NP et au-delà *(ajout)*

**Exercice 25.2.1**

Classez chaque problème parmi P, NP-complet ou NP-difficile (sans être dans NP), et justifiez brièvement : tri, plus court chemin dans un graphe à poids positifs, SAT, voyageur de commerce (version optimisation), sac à dos (version décision), cycle hamiltonien, flot maximal, coloration d'un graphe avec 3 couleurs.

**Correction**

| Problème | Classe | Justification |
| --- | --- | --- |
| **Tri** | **P** | algorithmes en O(n log n) |
| **Plus court chemin (poids positifs)** | **P** | Dijkstra, O((n + m) log n) |
| **SAT** | **NP-complet** | théorème de Cook-Levin : dans NP (le certificat est une affectation vérifiable en temps polynomial) et tout problème de NP s'y réduit |
| **Voyageur de commerce (optimisation)** | **NP-difficile** | la version décision (« existe-t-il une tournée de longueur ≤ K ? ») est NP-complète ; la version optimisation n'est pas un problème de décision, donc n'est pas dans NP au sens strict |
| **Sac à dos (décision)** | **NP-complet** | dans NP (le certificat est le sous-ensemble) ; réduction depuis la somme de sous-ensemble ; résoluble en temps **pseudo-polynomial** O(n · C) par programmation dynamique |
| **Cycle hamiltonien** | **NP-complet** | certificat = le cycle ; réduction depuis la couverture de sommets |
| **Flot maximal** | **P** | Edmonds-Karp, Dinic (polynomiaux) |
| **3-coloration d'un graphe** | **NP-complet** | certificat = la coloration ; réduction depuis 3-SAT (alors que la 2-coloration est dans P, par BFS) |

**Exercice 25.2.2**

Écrivez un **vérificateur** polynomial pour chacun des problèmes de décision suivants : somme de sous-ensemble (certificat : le sous-ensemble), cycle hamiltonien (certificat : la suite de sommets), coloration (certificat : la coloration). Quelle est la complexité de chaque vérificateur ?

**Correction**

Un **vérificateur** reçoit une instance et un certificat et répond oui ou non en temps polynomial.

```python
def verifier_somme_sous_ensemble(t, cible, indices):
    """Certificat : la liste des indices choisis."""
    return (len(set(indices)) == len(indices)
            and all(0 <= i < len(t) for i in indices)
            and sum(t[i] for i in indices) == cible)


def verifier_cycle_hamiltonien(n, aretes, chemin):
    """Certificat : la suite des sommets du cycle."""
    existantes = {frozenset(e) for e in aretes}
    return (len(chemin) == n
            and set(chemin) == set(range(n))                         # chaque sommet une seule fois
            and all(frozenset((chemin[i], chemin[(i + 1) % n])) in existantes
                    for i in range(n)))                              # arêtes consécutives, retour compris


def verifier_coloration(aretes, couleurs, k):
    """Certificat : couleurs[v] pour chaque sommet v."""
    return (all(0 <= c < k for c in couleurs)
            and all(couleurs[u] != couleurs[v] for u, v in aretes))


print(verifier_somme_sous_ensemble([3, 34, 4, 12, 5, 2], 9, [2, 4]))              # True (4 + 5)
print(verifier_cycle_hamiltonien(4, [(0, 1), (1, 2), (2, 3), (3, 0)], [0, 1, 2, 3]))   # True
print(verifier_coloration([(0, 1), (1, 2), (2, 0)], [0, 1, 2], 3))                 # True
print(verifier_coloration([(0, 1), (1, 2), (2, 0)], [0, 1, 0], 3))                 # False
```

Complexités : somme de sous-ensemble **O(n)** ; cycle hamiltonien **O(n + m)** (avec un ensemble d'arêtes) ; coloration **O(n + m)**. Ces vérifications sont toutes polynomiales, alors qu'on ne connaît pas d'algorithme polynomial pour **trouver** les certificats.

**Exercice 25.2.3**

Qu'est-ce qu'une réduction polynomiale ? Décrivez une réduction du problème de l'ensemble indépendant maximum au problème de la clique, ou de la couverture de sommets à l'ensemble indépendant.

**Correction**

Une **réduction polynomiale** de `A` vers `B` est une fonction `f`, calculable en temps polynomial, telle que, pour toute instance `x` de `A`, `x` est une instance « oui » de `A` si et seulement si `f(x)` est une instance « oui » de `B`. Si `B` est dans P, alors `A` aussi ; réciproquement, si `A` est NP-difficile, `B` l'est aussi. On l'utilise pour **propager la difficulté** d'un problème NP-difficile connu vers un nouveau problème.

**Ensemble indépendant vers clique** : un ensemble `S` de sommets est indépendant dans `G` si et seulement si c'est une clique dans le **graphe complémentaire** `Ḡ` (mêmes sommets, arêtes exactement là où `G` n'en a pas). Donc `G` possède un ensemble indépendant de taille `k` si et seulement si `Ḡ` possède une clique de taille `k` ; le complémentaire se construit en O(n²).

**Couverture de sommets vers ensemble indépendant** : `S` est une couverture de sommets (chaque arête a une extrémité dans `S`) si et seulement si `V \ S` est un ensemble indépendant. Donc `G` a une couverture de taille `≤ k` si et seulement si `G` a un ensemble indépendant de taille `≥ n − k`.

```python
import itertools


def complementaire(n, aretes):
    existantes = {frozenset(e) for e in aretes}
    return [(u, v) for u in range(n) for v in range(u + 1, n) if frozenset((u, v)) not in existantes]


def est_clique(S, aretes):
    E = {frozenset(e) for e in aretes}
    return all(frozenset(p) in E for p in itertools.combinations(S, 2))


def est_independant(S, aretes):
    E = {frozenset(e) for e in aretes}
    return all(frozenset(p) not in E for p in itertools.combinations(S, 2))


n = 6
aretes = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 5), (0, 3)]
co = complementaire(n, aretes)
print(all(est_independant(S, aretes) == est_clique(S, co)
          for r in range(n + 1) for S in itertools.combinations(range(n), r)))   # True
```

**Exercice 25.2.4**

Pour un problème NP-difficile, on peut utiliser un algorithme exact exponentiel, une approximation, une heuristique ou un solveur. Associez à chaque approche un exemple concret : DP par masques, couverture de sommets par arêtes d'un couplage maximal (2-approximation), recuit simulé, solveur SAT.

**Correction**

| Approche | Exemple concret | Caractéristique |
| --- | --- | --- |
| **Algorithme exact exponentiel** | **Programmation dynamique par masques** (Held-Karp) pour le voyageur de commerce en O(2ⁿ · n²) | solution optimale garantie, praticable jusqu'à `n ≈ 20` |
| **Approximation** | **Couverture de sommets par les arêtes d'un couplage maximal** : on prend les deux extrémités de chaque arête d'un couplage maximal | **2-approximation** : la solution est au plus deux fois l'optimal, en temps linéaire |
| **Heuristique** | **Recuit simulé** (ou algorithmes génétiques, recherche locale) : exploration aléatoire avec acceptation probabiliste de mauvaises solutions | pas de garantie de qualité, mais de bons résultats pratiques (tournées, emplois du temps) |
| **Solveur** | **Solveur SAT** (apprentissage de clauses CDCL, par exemple MiniSat, Z3) : on encode le problème en formule booléenne | résout en pratique des instances industrielles à des millions de variables (vérification, planification) |

Exemple de 2-approximation pour la couverture de sommets :

```python
def couverture_approchee(aretes):
    couverture = set()
    for u, v in aretes:
        if u not in couverture and v not in couverture:     # arête non couverte : couplage
            couverture |= {u, v}                             # on prend les deux extrémités
    return couverture


aretes = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 5), (0, 3)]
print(couverture_approchee(aretes))   # {0, 1, 2, 3, 4, 5} : 6 sommets, l'optimum en a 3
```

**Pourquoi c'est une 2-approximation** : les arêtes choisies forment un couplage (elles n'ont pas de sommet commun) ; toute couverture optimale doit contenir au moins une extrémité de chacune d'elles, donc `OPT ≥ |couplage|`, alors que notre solution a `2 · |couplage|` sommets. Ici, on atteint exactement le facteur 2.

**Exercice 25.2.5**

Que signifie « P = NP ? » Quelles conséquences pratiques aurait une réponse positive pour la cryptographie et l'optimisation ?

**Correction**

**« P = NP ? »** demande si tout problème dont une solution peut être **vérifiée** en temps polynomial (la classe NP) peut aussi être **résolu** en temps polynomial (la classe P). On sait que `P ⊆ NP` ; on ignore si l'inclusion est stricte. C'est l'un des sept problèmes du millénaire de l'institut Clay (un million de dollars). La majorité des spécialistes pense que `P ≠ NP`.

**Conséquences d'une réponse positive** (avec un algorithme polynomial **efficace en pratique**) :

- **Cryptographie** : la plupart des systèmes à clé publique et des chiffrements symétriques reposent sur la difficulté de trouver une clé ou une solution alors qu'on peut vérifier facilement : retrouver la clé est un problème de NP. Avec P = NP, on pourrait les casser : RSA (factorisation), signatures, fonctions de hachage (trouver une pré-image).
- **Optimisation** : des problèmes aujourd'hui intraitables (voyageur de commerce, ordonnancement, repliement de protéines, conception de circuits, vérification de programmes) deviendraient résolubles exactement ; même la découverte automatique de preuves mathématiques de longueur raisonnable serait possible.

Nuance : une preuve non constructive, ou un algorithme polynomial de degré énorme (par exemple `n¹⁰⁰`), n'aurait pas ces effets pratiques.

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

**Correction**

| N° | Technique | Justification |
| --- | --- | --- |
| 1 | **Recherche binaire** | le tableau est trié : on élimine la moitié des candidats à chaque pas (O(log n)) |
| 2 | **Recherche binaire sur la réponse** | la fonction « ce débit suffit-il ? » est monotone et testable en O(n) |
| 3 | **Deux pointeurs** | tableau trié : on fait converger les deux extrémités en O(n) |
| 4 | **Fenêtre glissante** (avec un dictionnaire de dernières positions) | la fenêtre grandit à droite et rétrécit à gauche en O(n) |
| 5 | **Sommes préfixes** | tableau fixe : chaque requête en O(1) après un précalcul O(n) |
| 6 | **Arbre de Fenwick** (ou arbre de segments) | mises à jour de points et sommes d'intervalle en O(log n) |
| 7 | **Hachage** (dictionnaire dont la clé est le mot trié, ou le comptage des lettres) | deux anagrammes ont la même clé |
| 8 | **Glouton** (tri par heure de fin) | sélection d'activités : le choix glouton est prouvé optimal |
| 9 | **Programmation dynamique** (tableau LCS) | sous-problèmes qui se chevauchent sur les préfixes des deux textes |
| 10 | **Retour sur trace** (avec élagage des colonnes et diagonales) | on construit la solution case par case et on abandonne les branches en conflit |
| 11 | **BFS** | graphe non pondéré : le BFS donne le plus court chemin en nombre d'arêtes |
| 12 | **Dijkstra** | poids positifs, source unique, O((n + m) log n) |
| 13 | **Bellman-Ford** | accepte les poids négatifs et détecte les cycles négatifs |
| 14 | **Floyd-Warshall** | toutes les paires pour `n = 300` : `300³ = 2,7 × 10⁷` opérations |
| 15 | **Tri topologique** | ordre compatible avec les dépendances d'un graphe orienté acyclique (Kahn ou DFS) |
| 16 | **Arbre couvrant minimal** (Kruskal ou Prim) | relier tous les sommets au coût minimal |
| 17 | **Union-Find** | maintien de composantes avec des unions, quasi O(1) amorti par opération |
| 18 | **Composantes fortement connexes** (Tarjan ou Kosaraju) | pages qui se référencent mutuellement = ensembles mutuellement accessibles |
| 19 | **Flot maximal / couplage biparti** (Dinic ou Hopcroft-Karp) | chaque étudiant à au plus un projet, selon les compatibilités |
| 20 | **KMP** (ou algorithme Z, ou `str.find`) | recherche de motif en O(n + m), sans retour en arrière dans le texte |

**Exercice 25.3.2**

Inventez un énoncé pour chacune des lignes suivantes du tableau de synthèse, sans reprendre les exemples du cours : glouton, programmation dynamique, recherche binaire sur la réponse, retour sur trace, Fenwick.

**Correction**

Voici un énoncé original pour chacune des techniques :

**Glouton (tri et deux pointeurs).** « Un club de kayak dispose de bateaux biplaces dont la charge maximale est `L`. Chaque bateau transporte au plus deux personnes, et `n` personnes de poids donnés doivent traverser le lac. Quel est le nombre minimal de bateaux ? » *Solution* : trier, puis apparier la personne la plus lourde restante avec la plus légère si leur somme est ≤ `L`, sinon la plus lourde part seule ; O(n log n).

**Programmation dynamique.** « Un texte sans espaces `s` et un dictionnaire de mots sont donnés. De combien de façons peut-on découper `s` en une suite de mots du dictionnaire ? » *Solution* : `dp[i]` = nombre de découpages du préfixe `s[:i]`, avec `dp[0] = 1` et `dp[i] = Σ dp[j]` pour les `j < i` tels que `s[j:i]` est dans le dictionnaire ; O(n · L) avec `L` la longueur maximale d'un mot.

**Recherche binaire sur la réponse.** « Une scierie reçoit `n` planches de longueurs `ℓ₁, ..., ℓₙ` et doit produire au moins `m` tasseaux de même longueur entière, en coupant chaque planche en autant de tasseaux que possible. Quelle est la plus grande longueur de tasseau réalisable ? » *Solution* : le nombre de tasseaux `Σ ⌊ℓᵢ / x⌋` est décroissant en `x` ; on cherche le plus grand `x` avec `Σ ⌊ℓᵢ / x⌋ ≥ m` par recherche binaire, O(n log max ℓ).

**Retour sur trace.** « Générer tous les mots de passe de longueur `n` écrits avec les lettres `a-z` où deux voyelles ne sont jamais consécutives. » *Solution* : exploration lettre par lettre en élaguant les branches où la nouvelle lettre est une voyelle et la précédente aussi ; le nombre de mots est donné par une récurrence, mais on les énumère explicitement.

**Fenwick.** « Un cinéma de `n` sièges numérotés enregistre en direct des réservations et des annulations, et un responsable demande à tout moment combien de sièges sont occupés entre les numéros `l` et `r`. » *Solution* : un arbre de Fenwick de 0/1 où `ajouter(i, +1)` réserve, `ajouter(i, −1)` annule, et `somme(l, r)` répond ; O(log n) par opération.

## 25.4 Conseils de progression

**Exercice 25.4.1**

Écrivez un **test de stress** : pour un problème de votre choix (par exemple la somme maximale d'un sous-tableau), implémentez une solution naïve et une solution optimisée, générez des entrées aléatoires de petite taille et comparez les sorties jusqu'à trouver une divergence.

**Correction**

On compare une solution **lente mais évidemment correcte** (force brute) à la solution **rapide**, sur des milliers d'entrées aléatoires de petite taille (où les cas limites apparaissent vite), et on s'arrête à la première divergence en affichant l'entrée.

```python
import random


def sous_tableau_naif(t):                      # O(n²) : référence
    return max(sum(t[i:j + 1]) for i in range(len(t)) for j in range(i, len(t)))


def kadane(t):                                 # O(n) : solution testée
    meilleur = courant = t[0]
    for x in t[1:]:
        courant = max(x, courant + x)
        meilleur = max(meilleur, courant)
    return meilleur


def test_de_stress(reference, solution, essais=10_000, taille_max=8, valeur_max=5):
    for essai in range(1, essais + 1):
        t = [random.randint(-valeur_max, valeur_max)
             for _ in range(random.randint(1, taille_max))]
        a, b = reference(t[:]), solution(t[:])
        if a != b:
            print(f"Divergence à l'essai {essai} : entrée {t}, attendu {a}, obtenu {b}")
            return False
    print(f"{essais} essais : aucune divergence")
    return True


test_de_stress(sous_tableau_naif, kadane)      # 10000 essais : aucune divergence
```

Pour voir le test en action, on essaie une version fautive qui initialise `meilleur` à 0 au lieu du premier élément :

```python
def kadane_fautif(t):
    meilleur = courant = 0
    for x in t:
        courant = max(x, courant + x)
        meilleur = max(meilleur, courant)
    return meilleur


random.seed(5)
test_de_stress(sous_tableau_naif, kadane_fautif)
# Divergence à l'essai 7 : entrée [-3], attendu -3, obtenu 0
```

Le test trouve en quelques essais un cas limite (tableau entièrement négatif) que l'on avait oublié. Bonnes pratiques : fixer la graine pour reproduire, commencer par de très petites tailles, faire varier la plage des valeurs (beaucoup de doublons, valeurs négatives, zéros), puis réduire l'entrée fautive au plus petit exemple qui diverge.

**Exercice 25.4.2**

Choisissez un schéma parmi : deux pointeurs, fenêtre glissante, préfixes, hachage, recherche binaire sur la réponse. Rédigez un mini-fichier de révision comprenant : un énoncé type, la fiche des cas limites, la complexité attendue, et un exemple de code commenté.

**Correction**

Mini-fichier de révision pour la **fenêtre glissante**.

**Énoncé type** : « Étant donné une chaîne `s` et un entier `k`, quelle est la longueur de la plus longue sous-chaîne qui contient au plus `k` caractères distincts ? » (variantes : plus courte fenêtre dont la somme est ≥ `S`, plus longue sous-chaîne sans répétition, anagrammes dans un texte).

**Reconnaître le schéma** : on cherche un sous-tableau ou une sous-chaîne **contigus** vérifiant une condition qui reste vraie quand on **retire** un élément (monotonie), et dont l'état se met à jour en O(1) quand un élément entre ou sort.

**Fiche des cas limites** :

- chaîne vide, ou `k = 0` (résultat 0) ;
- `k` supérieur au nombre de caractères distincts (toute la chaîne) ;
- tous les caractères identiques ;
- `k = 1` ;
- fenêtre qui touche le début ou la fin ;
- valeurs négatives (la fenêtre glissante par somme n'est plus valable : voir sommes préfixes).

**Complexité attendue** : **O(n)** en temps (chaque pointeur avance au plus `n` fois : analyse amortie), **O(k)** en espace (dictionnaire des compteurs).

**Exemple de code commenté** :

```python
def plus_longue_avec_k_distincts(s, k):
    compteur = {}                                   # état de la fenêtre : caractère -> occurrences
    gauche = meilleur = 0
    for droite, c in enumerate(s):                  # on agrandit la fenêtre à droite
        compteur[c] = compteur.get(c, 0) + 1
        while len(compteur) > k:                    # condition violée : on rétrécit à gauche
            sortant = s[gauche]
            compteur[sortant] -= 1
            if compteur[sortant] == 0:
                del compteur[sortant]               # un caractère distinct de moins
            gauche += 1
        meilleur = max(meilleur, droite - gauche + 1)
    return meilleur


assert plus_longue_avec_k_distincts("eceba", 2) == 3     # "ece"
assert plus_longue_avec_k_distincts("aa", 1) == 2
assert plus_longue_avec_k_distincts("", 3) == 0
assert plus_longue_avec_k_distincts("abc", 0) == 0
```

**Pièges** : oublier de supprimer la clé quand son compteur tombe à 0 (le test `len(compteur)` serait faux) ; mettre à jour `meilleur` avant d'avoir restauré la condition ; erreur d'un sur la longueur (`droite − gauche + 1`).

**Exercice 25.4.3**

Établissez un plan de progression sur 8 semaines : pour chaque semaine, un thème du cours, trois problèmes à résoudre et un critère pour juger que le thème est maîtrisé.

**Correction**

Plan de progression sur 8 semaines (environ 6 à 8 heures par semaine). Les problèmes sont à choisir sur la plateforme de votre choix ; les critères permettent de décider si l'on passe à la suite.

| Semaine | Thème | Trois problèmes | Critère de maîtrise |
| --- | --- | --- | --- |
| 1 | Complexité, tableaux, tris et recherche binaire | recherche binaire d'une valeur ; recherche de la première et de la dernière occurrence ; tri par un critère composé | donner de tête la complexité de n'importe quelle boucle imbriquée ; écrire la recherche binaire sans erreur d'un en moins de 5 minutes |
| 2 | Deux pointeurs et fenêtre glissante | somme de deux éléments dans un tableau trié ; plus longue sous-chaîne sans répétition ; plus petit sous-tableau de somme ≥ `S` | reconnaître le schéma à la lecture de l'énoncé ; 3 problèmes sur 3 résolus en O(n) |
| 3 | Sommes préfixes, hachage et dictionnaires | sous-tableaux de somme `k` ; regroupement d'anagrammes ; plus longue suite d'entiers consécutifs | expliquer pourquoi le dictionnaire de préfixes évite O(n²) ; traiter 10⁵ requêtes en O(1) |
| 4 | Récursivité, diviser pour régner et retour sur trace | `n` reines ; sous-ensembles et permutations ; sous-tableau de somme maximale (version récursive) | écrire un retour sur trace avec élagage ; résoudre une récurrence par le théorème maître |
| 5 | Algorithmes gloutons | sélection d'activités ; rendu de monnaie (et contre-exemple) ; code de Huffman | prouver un choix glouton par un argument d'échange ; savoir quand le glouton échoue |
| 6 | Programmation dynamique | rendu de monnaie ; plus longue sous-suite croissante ; distance d'édition | décrire état, transition, cas de base et ordre de calcul **avant** d'écrire le code ; réduire la mémoire à une ou deux lignes |
| 7 | Graphes : parcours et plus courts chemins | nombre d'îles (BFS ou DFS) ; ordre des cours (tri topologique) ; plus court chemin avec Dijkstra | choisir BFS, Dijkstra ou Bellman-Ford selon les poids ; coder Dijkstra avec un tas sans consulter la documentation |
| 8 | Graphes avancés et structures : Union-Find, arbres couvrants, Fenwick, chaînes | composantes connexes avec Union-Find ; arbre couvrant minimal ; comptage d'inversions ou KMP | résoudre un problème inédit de chaque type en moins de 45 minutes ; réussir un petit concours chronométré à la fin de la semaine |

Chaque semaine, refaire en fin de séance les problèmes ratés (révision espacée) et ajouter un test de stress (exercice 25.4.1) pour au moins un problème.

## 25.5 Ressources

**Exercice 25.5.1**

Choisissez une plateforme d'entraînement (par exemple LeetCode, Codeforces, AtCoder, Kattis, France-IOI, Project Euler) et résolvez un problème pour chacun des trois niveaux du cours. Pour chaque problème, rédigez l'énoncé reformulé, la méthode retenue, la complexité et les cas limites testés.

**Correction**

Plateforme choisie : **LeetCode**. Trois problèmes, de difficulté croissante.

**Niveau débutant : « Two Sum » (problème n° 1).**

- *Énoncé reformulé* : un tableau d'entiers et une cible `T` étant donnés, renvoyer les indices de deux éléments distincts dont la somme vaut `T` (on garantit une solution).
- *Méthode retenue* : un dictionnaire qui associe chaque valeur déjà vue à son indice ; pour chaque `x`, on regarde si `T − x` est dans le dictionnaire (exercice 17.5.1).
- *Complexité* : temps **O(n)**, espace **O(n)** (contre O(n²) pour deux boucles).
- *Cas limites testés* : deux éléments égaux (`[3, 3]`, cible 6), valeurs négatives, zéros (`[0, 4, 0]`, cible 0), tableau de deux éléments, interdiction de réutiliser le même indice.

**Niveau intermédiaire : « Number of Islands » (problème n° 200).**

- *Énoncé reformulé* : dans une grille de `'1'` (terre) et `'0'` (eau), compter les îles, une île étant un groupe de cases de terre connectées horizontalement ou verticalement.
- *Méthode retenue* : parcours en profondeur itératif (ou BFS) qui marque les cases visitées ; on lance un parcours à chaque case de terre non visitée (exercice 19.3.4).
- *Complexité* : temps **O(m · n)**, espace O(m · n) dans le pire cas (pile, tableau des cases visitées).
- *Cas limites testés* : grille vide, grille entièrement d'eau, grille entièrement de terre (une seule île), une seule ligne ou une seule colonne, cases en diagonale (qui ne sont pas connectées).

**Niveau avancé : « Cheapest Flights Within K Stops » (problème n° 787).**

- *Énoncé reformulé* : `n` villes, des vols orientés avec un prix ; trouver le prix minimal pour aller de la ville source à la ville destination en faisant au plus `k` escales (au plus `k + 1` vols), ou `-1` si c'est impossible.
- *Méthode retenue* : Bellman-Ford limité à `k + 1` passes, chacune lisant le tableau de la passe précédente (copie), car Dijkstra ordinaire ne respecte pas la contrainte sur le nombre d'arêtes (exercice 20.3.5).
- *Complexité* : temps **O(k · m)** pour `m` vols, espace O(n).
- *Cas limites testés* : `k = 0` (vol direct uniquement), destination inaccessible, source égale à la destination, vols formant un cycle, trajet moins cher mais avec trop d'escales, plusieurs vols entre les deux mêmes villes.

**Exercice 25.5.2**

Avec un outil de visualisation d'algorithmes (par exemple VisuAlgo ou Python Tutor), exécutez pas à pas un tri, un parcours de graphe et un algorithme de plus court chemin, puis comparez la trace obtenue avec celle que vous avez faite à la main dans les exercices correspondants.

**Correction**

Avec **VisuAlgo** (ou **Python Tutor** pour les programmes), on exécute pas à pas les trois algorithmes en reprenant exactement les mêmes entrées que dans les exercices manuels, puis on compare.

| Algorithme | Entrée à reprendre | Trace manuelle à comparer | Points à vérifier |
| --- | --- | --- | --- |
| **Tri** (bulles, sélection ou insertion) | `[5, 1, 4, 2, 8]` ou `[12, 11, 13, 5, 6]` | exercices 5.2.1, 5.3.1, 5.4.1 | nombre de passes, échanges effectués à chaque passe, état du tableau après chaque passe, arrêt anticipé du tri à bulles |
| **Parcours de graphe** (BFS, DFS) | le graphe à 5 sommets de l'exercice 19.1.1 | exercices 19.2.1 et 19.3.1 | contenu de la file ou de la pile à chaque étape, ordre de visite, distances |
| **Plus court chemin** (Dijkstra) | le graphe de l'exercice 20.2.1 (source A) | exercice 20.2.1 | distances provisoires après chaque extraction, ordre d'extraction, prédécesseurs |

**Comment comparer** : noter, pour chaque étape, l'état de la structure de données (tableau, file, tas) et le comparer ligne à ligne avec la trace manuelle. Les différences viennent presque toujours de :

- l'**ordre de parcours des voisins** (liste d'adjacence dans l'ordre croissant ou ordre d'insertion) ;
- la **gestion des égalités** (deux sommets à la même distance dans Dijkstra, deux éléments égaux dans un tri) ;
- une convention différente (numérotation à partir de 0 ou de 1, test `<` contre `<=`).

Quand la trace diffère, il faut identifier **la première étape** où elles divergent : c'est elle qui révèle l'erreur de raisonnement ou de calcul, de votre côté ou dans l'hypothèse (par exemple l'ordre des voisins) retenue par l'outil.

---

<div align="center">

*Bon courage et bon voyage au pays des algorithmes !*

</div>
