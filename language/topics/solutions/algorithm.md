# ✅ Corrigés : exercices d'algorithmique (Python)

> Pour chaque exercice : **l'idée**, le **pseudo-code**, l'**implémentation Python 3.11+** avec ses tests (`assert`), et l'**analyse de complexité**. Tous les blocs de code ont été **exécutés et vérifiés**.
>
> 💡 Essayez d'abord l'exercice seul : ces corrigés ne sont pas la seule bonne réponse.

## 📑 Sommaire

[1](#exercice-1--le-plus-grand-nombre) · [2](#exercice-2--palindrome) · [3](#exercice-3--le-deuxième-plus-grand-nombre) · [4](#exercice-4--le-nombre-manquant) · [5](#exercice-5--éléments-communs) · [6](#exercice-6--rotation-dun-tableau) · [7](#exercice-7--premier-caractère-unique) · [8](#exercice-8--fusion-de-deux-tableaux-triés) · [9](#exercice-9--plus-longue-sous-suite-croissante) · [10](#exercice-10--somme-de-deux-nombres) · [11](#exercice-11--recherche-dichotomique) · [12](#exercice-12--parenthèses-bien-formées) · [13](#exercice-13--suite-de-fibonacci)

---

## Exercice 1 : le plus grand nombre

**Idée** : partir du **premier élément** (pas de `0`, à cause des négatifs) et le remplacer dès qu'on rencontre plus grand.

```text
ALGORITHME plus_grand
ENTRÉE : liste non vide de nombres
DÉBUT
    maximum ← liste[0]
    POUR CHAQUE n DANS liste (à partir du 2e) FAIRE
        SI n > maximum ALORS maximum ← n
    RETOURNER maximum
FIN
```

```python
def plus_grand(nombres: list[int]) -> int:
    maximum = nombres[0]
    for n in nombres[1:]:
        if n > maximum:
            maximum = n
    return maximum


assert plus_grand([3, 5, 7, 2, 8, 1]) == 8
assert plus_grand([-4, -2, -9]) == -2
assert plus_grand([42]) == 42
```

**Complexité** : temps `O(n)`, mémoire `O(1)` (la copie `nombres[1:]` coûte `O(n)` ; on peut l'éviter avec `iter` et `next`).

---

## Exercice 2 : palindrome

**Idée** : ne garder que les lettres et chiffres, en minuscules, puis comparer à l'envers.

```text
ALGORITHME est_palindrome
DÉBUT
    caractères ← [minuscule(c) POUR c DANS texte SI c est alphanumérique]
    RETOURNER caractères = inverse(caractères)
FIN
```

```python
import unicodedata


def est_palindrome(texte: str) -> bool:
    car = [c.casefold() for c in texte if c.isalnum()]
    return car == car[::-1]


assert est_palindrome("A man a plan a canal Panama")
assert est_palindrome("A man, a plan, a canal, Panama")
assert est_palindrome("racecar")
assert not est_palindrome("hello")
assert est_palindrome("")


# 🟣 Bonus 1 : deux indices, sans copie inversée (mémoire O(1))
def est_palindrome_2p(texte: str) -> bool:
    i, j = 0, len(texte) - 1
    while i < j:
        if not texte[i].isalnum():
            i += 1
        elif not texte[j].isalnum():
            j -= 1
        elif texte[i].casefold() != texte[j].casefold():
            return False
        else:
            i += 1
            j -= 1
    return True


assert est_palindrome_2p("A man, a plan, a canal, Panama")
assert not est_palindrome_2p("hello")


# 🟣 Bonus 2 : accents (« é » devient « e » + accent combinant, que isalnum() écarte)
def est_palindrome_accents(texte: str) -> bool:
    decompose = unicodedata.normalize("NFD", texte)
    car = [c.casefold() for c in decompose if c.isalnum()]
    return car == car[::-1]


assert est_palindrome_accents("Été")
assert est_palindrome_accents("Ésope reste ici et se repose")
```

**Complexité** : `O(n)` en temps ; `O(n)` en mémoire pour la version simple, `O(1)` pour les deux indices.

---

## Exercice 3 : le deuxième plus grand nombre

**Idée** : un seul parcours avec deux variables. Un nombre égal au maximum **ne compte pas** comme deuxième (il faut une valeur *distincte*). On part de `None` pour gérer les négatifs.

```text
ALGORITHME deuxieme_plus_grand
DÉBUT
    premier ← aucun ; deuxieme ← aucun
    POUR CHAQUE n DANS liste FAIRE
        SI premier est vide OU n > premier ALORS
            deuxieme ← premier ; premier ← n
        SINON SI n ≠ premier ET (deuxieme est vide OU n > deuxieme) ALORS
            deuxieme ← n
    RETOURNER deuxieme
FIN
```

```python
def deuxieme_plus_grand(nombres: list[int]) -> int:
    premier = deuxieme = None
    for n in nombres:
        if premier is None or n > premier:
            deuxieme = premier
            premier = n
        elif n != premier and (deuxieme is None or n > deuxieme):
            deuxieme = n
    return deuxieme


assert deuxieme_plus_grand([12, 35, 1, 10, 34, 1]) == 34
assert deuxieme_plus_grand([1, 2, 3, 4, 5]) == 4
assert deuxieme_plus_grand([5, 5, 3]) == 3
assert deuxieme_plus_grand([-5, -1, -9]) == -5


# Version courte (O(n log n)) pour comparer :
def deuxieme_plus_grand_tri(nombres: list[int]) -> int:
    return sorted(set(nombres))[-2]


assert deuxieme_plus_grand_tri([12, 35, 1, 10, 34, 1]) == 34
```

**Complexité** : `O(n)` en temps et `O(1)` en mémoire (contre `O(n log n)` pour la version avec tri).

---

## Exercice 4 : le nombre manquant

**Idée** : trois approches, toutes en `O(n)`.

```text
SOMME : manquant ← n(n+1)/2 − somme(liste)
XOR   : manquant ← XOR de 1..n  XOR  XOR de la liste
```

```python
def manquant_somme(nombres: list[int], n: int) -> int:
    return n * (n + 1) // 2 - sum(nombres)


def manquant_xor(nombres: list[int], n: int) -> int:
    resultat = 0
    for i in range(1, n + 1):
        resultat ^= i
    for x in nombres:
        resultat ^= x
    return resultat


def manquant_ensemble(nombres: list[int], n: int) -> int:
    return (set(range(1, n + 1)) - set(nombres)).pop()


for f in (manquant_somme, manquant_xor, manquant_ensemble):
    assert f([1, 2, 4, 5, 6], 6) == 3
    assert f([3, 7, 1, 2, 8, 4, 5], 8) == 6
    assert f([2], 2) == 1
```

**Complexité** : somme et XOR `O(n)` / `O(1)` ; ensemble `O(n)` / `O(n)`. Dans un langage à entiers de taille fixe (C), la somme peut déborder : le XOR n'a pas ce défaut.

---

## Exercice 5 : éléments communs

**Idée** : transformer les listes en **ensembles** (suppression des doublons, test d'appartenance en `O(1)`), puis faire l'intersection.

```text
ALGORITHME elements_communs
DÉBUT
    A ← ensemble(liste1) ; B ← ensemble(liste2)
    RETOURNER A ∩ B
FIN
```

```python
def elements_communs(liste1: list[int], liste2: list[int]) -> list[int]:
    return list(set(liste1) & set(liste2))


assert sorted(elements_communs([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])) == [4, 5]
assert elements_communs([10, 20, 30, 40], [50, 60, 70, 80]) == []
assert elements_communs([1, 2, 2, 1], [2, 2]) == [2]
assert sorted(elements_communs([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]


# Version naïve O(n × m), pour comparer
def elements_communs_naif(liste1: list[int], liste2: list[int]) -> list[int]:
    resultat = []
    for x in liste1:
        if x in liste2 and x not in resultat:   # « in liste » coûte O(n)
            resultat.append(x)
    return resultat


assert sorted(elements_communs_naif([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]
```

**Complexité** : `O(n + m)` avec des ensembles, contre `O(n × m)` pour la version naïve.

---

## Exercice 6 : rotation d'un tableau

**Idée** : méthode des **trois inversions** (en place, mémoire `O(1)`). Pour `[1,2,3,4,5]` et `k = 2` : on inverse tout (`[5,4,3,2,1]`), puis les `k` premiers (`[4,5,3,2,1]`), puis les autres (`[4,5,1,2,3]`).

```text
ALGORITHME pivoter(tableau, k)
DÉBUT
    SI tableau est vide ALORS RETOURNER
    k ← k MODULO longueur ; SI k = 0 ALORS RETOURNER
    inverser(tableau, 0, n−1) ; inverser(tableau, 0, k−1) ; inverser(tableau, k, n−1)
FIN
```

```python
def _inverser(t: list[int], i: int, j: int) -> None:
    while i < j:
        t[i], t[j] = t[j], t[i]
        i += 1
        j -= 1


def pivoter(tableau: list[int], k: int) -> None:
    n = len(tableau)
    if n == 0:
        return
    k %= n
    if k == 0:
        return
    _inverser(tableau, 0, n - 1)
    _inverser(tableau, 0, k - 1)
    _inverser(tableau, k, n - 1)


for entree, k, attendu in [
    ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
    ([1, 2, 3, 4, 5], 4, [2, 3, 4, 5, 1]),
    ([1, 2, 3], 7, [3, 1, 2]),
    ([1, 2, 3], 0, [1, 2, 3]),
    ([], 5, []),
]:
    t = list(entree)
    pivoter(t, k)
    assert t == attendu, (entree, k, t)
```

**Complexité** : `O(n)` en temps, `O(1)` en mémoire. Le raccourci `t[:] = t[-k:] + t[:-k]` est correct mais crée des listes temporaires (`O(n)` de mémoire).

---

## Exercice 7 : premier caractère unique

**Idée** : deux parcours. Le premier compte les occurrences, le second cherche le premier caractère dont le compteur vaut 1.

```text
ALGORITHME premier_caractere_unique
DÉBUT
    compteur ← occurrences de chaque caractère
    POUR CHAQUE c DANS texte (dans l'ordre) FAIRE
        SI compteur[c] = 1 ALORS RETOURNER c
    RETOURNER aucun
FIN
```

```python
from collections import Counter


def premier_caractere_unique(texte: str) -> str | None:
    compteur = Counter(texte)
    for c in texte:
        if compteur[c] == 1:
            return c
    return None


assert premier_caractere_unique("swiss") == "w"
assert premier_caractere_unique("hello") == "h"
assert premier_caractere_unique("aabbcc") is None
assert premier_caractere_unique("aA") == "a"   # sensible à la casse
assert premier_caractere_unique("") is None
```

**Complexité** : `O(n)` en temps, `O(k)` en mémoire (`k` = nombre de caractères distincts).

---

## Exercice 8 : fusion de deux tableaux triés

**Idée** : deux pointeurs. On prend toujours le plus petit des deux éléments courants, puis on recopie le reste de l'autre tableau.

```text
ALGORITHME fusionner(a, b)
DÉBUT
    i ← 0 ; j ← 0 ; résultat ← []
    TANT QUE i < |a| ET j < |b| FAIRE
        SI a[i] ≤ b[j] ALORS ajouter a[i] ; i ← i+1
        SINON ajouter b[j] ; j ← j+1
    ajouter le reste de a (depuis i) et le reste de b (depuis j)
    RETOURNER résultat
FIN
```

```python
def fusionner(arr1: list[int], arr2: list[int]) -> list[int]:
    i = j = 0
    resultat = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:       # « <= » garde l'ordre d'origine (tri stable)
            resultat.append(arr1[i])
            i += 1
        else:
            resultat.append(arr2[j])
            j += 1
    resultat.extend(arr1[i:])
    resultat.extend(arr2[j:])
    return resultat


assert fusionner([1, 3, 5, 7], [2, 4, 6, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
assert fusionner([1, 10, 20], [5, 15, 25]) == [1, 5, 10, 15, 20, 25]
assert fusionner([], [1, 2]) == [1, 2]
assert fusionner([1, 1], [1]) == [1, 1, 1]

# 🟣 Bonus : la bibliothèque standard fait la même chose, paresseusement
import heapq

assert list(heapq.merge([1, 3, 5, 7], [2, 4, 6, 8])) == [1, 2, 3, 4, 5, 6, 7, 8]
```

**Complexité** : `O(n + m)` en temps et en mémoire de sortie.

---

## Exercice 9 : plus longue sous-suite croissante

**Idée (programmation dynamique, `O(n²)`)** : `longueur[i]` est la longueur de la meilleure sous-suite **se terminant à l'indice `i`**. On teste tous les `j < i` avec `t[j] < t[i]`. Le tableau `precedent[i]` mémorise d'où l'on vient, pour **reconstruire** la sous-suite.

```text
ALGORITHME LIS
DÉBUT
    POUR i DE 0 À n−1 FAIRE
        longueur[i] ← 1 ; précédent[i] ← −1
        POUR j DE 0 À i−1 FAIRE
            SI t[j] < t[i] ET longueur[j] + 1 > longueur[i] ALORS
                longueur[i] ← longueur[j] + 1 ; précédent[i] ← j
    fin ← indice du maximum de longueur
    remonter la chaîne des précédents depuis fin, puis inverser
FIN
```

```python
def plus_longue_sous_suite_croissante(tableau: list[int]) -> list[int]:
    if not tableau:
        return []
    n = len(tableau)
    longueur = [1] * n
    precedent = [-1] * n
    for i in range(n):
        for j in range(i):
            if tableau[j] < tableau[i] and longueur[j] + 1 > longueur[i]:
                longueur[i] = longueur[j] + 1
                precedent[i] = j
    fin = max(range(n), key=longueur.__getitem__)
    resultat = []
    while fin != -1:
        resultat.append(tableau[fin])
        fin = precedent[fin]
    return resultat[::-1]


assert plus_longue_sous_suite_croissante([10, 22, 9, 33, 21, 50, 41, 60, 80]) == [10, 22, 33, 50, 60, 80]
assert plus_longue_sous_suite_croissante([3, 10, 2, 1, 20]) == [3, 10, 20]
assert plus_longue_sous_suite_croissante([]) == []
assert plus_longue_sous_suite_croissante([5, 4, 3]) in ([5], [4], [3])
```

### 🟣 Bonus : version `O(n log n)` avec `bisect`

`valeurs[k]` est la plus petite valeur finale possible d'une sous-suite croissante de longueur `k + 1`. Ce tableau reste trié, on peut donc y chercher par dichotomie.

```python
from bisect import bisect_left


def lis_n_log_n(tableau: list[int]) -> list[int]:
    valeurs: list[int] = []          # plus petites fins de sous-suites, triées
    indices: list[int] = []          # indices correspondants dans `tableau`
    precedent = [-1] * len(tableau)
    for i, x in enumerate(tableau):
        pos = bisect_left(valeurs, x)    # strictement croissant : bisect_left
        if pos == len(valeurs):
            valeurs.append(x)
            indices.append(i)
        else:
            valeurs[pos] = x
            indices[pos] = i
        precedent[i] = indices[pos - 1] if pos > 0 else -1
    resultat = []
    k = indices[-1] if indices else -1
    while k != -1:
        resultat.append(tableau[k])
        k = precedent[k]
    return resultat[::-1]


for t in ([10, 22, 9, 33, 21, 50, 41, 60, 80], [3, 10, 2, 1, 20], [5, 4, 3], [2, 2, 2]):
    r = lis_n_log_n(t)
    assert len(r) == len(plus_longue_sous_suite_croissante(t))
    assert all(a < b for a, b in zip(r, r[1:]))
```

**Complexité** : `O(n²)` en temps pour la première version, `O(n log n)` pour la seconde ; `O(n)` en mémoire.

---

## Exercice 10 : somme de deux nombres

**Idée** : parcourir la liste en mémorisant dans un **dictionnaire** les valeurs déjà vues (`valeur → indice`). Pour chaque `x`, on cherche si `cible − x` a déjà été vu.

```text
ALGORITHME deux_sommes
DÉBUT
    vus ← dictionnaire vide
    POUR i, x DANS liste FAIRE
        SI (cible − x) EST DANS vus ALORS RETOURNER (vus[cible − x], i)
        vus[x] ← i
    RETOURNER aucun
FIN
```

```python
def deux_sommes(nombres: list[int], cible: int) -> tuple[int, int] | None:
    vus: dict[int, int] = {}
    for i, x in enumerate(nombres):
        if cible - x in vus:
            return vus[cible - x], i
        vus[x] = i
    return None


assert deux_sommes([2, 7, 11, 15], 9) == (0, 1)
assert deux_sommes([3, 2, 4], 6) == (1, 2)
assert deux_sommes([1, 2], 10) is None
assert deux_sommes([3, 3], 6) == (0, 1)      # deux éléments distincts de même valeur
assert deux_sommes([5], 10) is None          # un élément ne se réutilise pas
```

**Complexité** : `O(n)` en temps et en mémoire (contre `O(n²)` pour deux boucles imbriquées).

---

## Exercice 11 : recherche dichotomique

**Idée** : on garde un intervalle `[bas, haut]` où la valeur peut se trouver, et on le **divise par deux** à chaque étape en comparant avec l'élément du milieu.

```text
ALGORITHME recherche_dichotomique
DÉBUT
    bas ← 0 ; haut ← n − 1
    TANT QUE bas ≤ haut FAIRE
        milieu ← (bas + haut) DIV 2
        SI t[milieu] = valeur ALORS RETOURNER milieu
        SI t[milieu] < valeur ALORS bas ← milieu + 1
        SINON haut ← milieu − 1
    RETOURNER −1
FIN
```

```python
from bisect import bisect_left


def recherche_dichotomique(tableau_trie: list[int], valeur: int) -> int:
    bas, haut = 0, len(tableau_trie) - 1
    while bas <= haut:
        milieu = (bas + haut) // 2       # pas de dépassement en Python (voir note)
        if tableau_trie[milieu] == valeur:
            return milieu
        if tableau_trie[milieu] < valeur:
            bas = milieu + 1
        else:
            haut = milieu - 1
    return -1


assert recherche_dichotomique([1, 3, 5, 7, 9], 7) == 3
assert recherche_dichotomique([1, 3, 5, 7, 9], 4) == -1
assert recherche_dichotomique([], 1) == -1
assert recherche_dichotomique([1, 3, 5, 7, 9], 1) == 0
assert recherche_dichotomique([1, 3, 5, 7, 9], 9) == 4


# Avec la bibliothèque standard
def recherche_bisect(tableau_trie: list[int], valeur: int) -> int:
    i = bisect_left(tableau_trie, valeur)
    return i if i < len(tableau_trie) and tableau_trie[i] == valeur else -1


assert recherche_bisect([1, 3, 5, 7, 9], 7) == 3
assert recherche_bisect([1, 3, 5, 7, 9], 4) == -1
```

> 💡 En C ou en Java, `(bas + haut) / 2` peut déborder ; on écrit `bas + (haut - bas) / 2`.

**Complexité** : `O(log n)` en temps, `O(1)` en mémoire.

---

## Exercice 12 : parenthèses bien formées

**Idée** : une **pile**. Une ouvrante est empilée ; une fermante doit correspondre à l'ouvrante au sommet de la pile. À la fin, la pile doit être vide.

```text
ALGORITHME est_bien_parenthese
DÉBUT
    pile ← vide
    POUR CHAQUE c DANS texte FAIRE
        SI c est une ouvrante ALORS empiler c
        SINON SI c est une fermante ALORS
            SI pile vide OU sommet ≠ ouvrante associée à c ALORS RETOURNER faux
            dépiler
    RETOURNER (pile est vide)
FIN
```

```python
def est_bien_parenthese(texte: str) -> bool:
    paires = {")": "(", "]": "[", "}": "{"}
    pile: list[str] = []
    for c in texte:
        if c in paires.values():
            pile.append(c)
        elif c in paires:
            if not pile or pile.pop() != paires[c]:
                return False
    return not pile


assert est_bien_parenthese("([]{})")
assert not est_bien_parenthese("([)]")
assert not est_bien_parenthese("((")
assert est_bien_parenthese("")
assert not est_bien_parenthese(")(")
assert est_bien_parenthese("a(b[c]{d})e")   # les autres caractères sont ignorés
```

**Complexité** : `O(n)` en temps, `O(n)` en mémoire dans le pire cas.

---

## Exercice 13 : suite de Fibonacci

```python
from functools import cache


# 1. Récursive naïve : O(2^n), car on recalcule les mêmes sous-problèmes
def fib_naive(n: int) -> int:
    return n if n < 2 else fib_naive(n - 1) + fib_naive(n - 2)


# 2. Avec mémoïsation : O(n)
@cache
def fib_memo(n: int) -> int:
    return n if n < 2 else fib_memo(n - 1) + fib_memo(n - 2)


# 3. Itérative : O(n) en temps, O(1) en mémoire
def fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


for f in (fib_naive, fib_memo, fibonacci):
    assert f(0) == 0
    assert f(1) == 1
    assert f(10) == 55
assert fib_memo(50) == fibonacci(50) == 12586269025
```

**Questions**

- **Pourquoi la version naïve est-elle lente ?** `fib_naive(40)` appelle `fib_naive(2)` des dizaines de millions de fois : l'arbre d'appels double à peu près à chaque niveau, d'où `O(2ⁿ)`.
- **Et pour un grand `n` en récursif ?** Python limite la profondeur de récursion (1000 par défaut) : `fib_memo(5000)` lève `RecursionError`. La version itérative n'a pas cette limite.

---

## 🧪 Lancer tous les tests

Copiez les blocs `python` dans un fichier : si aucune `AssertionError` n'apparaît, tout est correct. Pour des tests plus propres, regroupez-les dans des fonctions `test_...` et lancez `pytest`.

## 🧾 Récapitulatif

| # | Technique clé | Complexité |
| :-: | --- | --- |
| 1 | Parcours, valeur initiale = 1ᵉʳ élément | `O(n)` |
| 2 | Filtrage, comparaison avec l'inverse, deux indices | `O(n)` |
| 3 | Deux variables, valeur distincte | `O(n)` |
| 4 | Somme, XOR, ensembles | `O(n)` |
| 5 | Ensembles | `O(n + m)` |
| 6 | Trois inversions, modulo | `O(n)`, mémoire `O(1)` |
| 7 | `Counter`, deux parcours | `O(n)` |
| 8 | Deux pointeurs | `O(n + m)` |
| 9 | Programmation dynamique, puis `bisect` | `O(n²)` puis `O(n log n)` |
| 10 | Dictionnaire (table de hachage) | `O(n)` |
| 11 | Diviser pour régner | `O(log n)` |
| 12 | Pile | `O(n)` |
| 13 | Mémoïsation, itération | `O(2ⁿ)` puis `O(n)` |
