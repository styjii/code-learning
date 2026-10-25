<div align="center">

# BeautifulSoup — Guide complet

**Analyser HTML et XML, extraire des données et faire du *web scraping* avec Python**

*Mis à jour pour Beautiful Soup 4.13 – 4.15 (octobre 2026)*

</div>

---

## Sommaire

1. [Introduction](#1-introduction)
2. [Installation et parseurs](#2-installation-et-parseurs)
3. [Créer un objet `BeautifulSoup`](#3-créer-un-objet-beautifulsoup)
4. [Les objets de l'arbre](#4-les-objets-de-larbre)
5. [Navigation de base et attributs](#5-navigation-de-base-et-attributs)
6. [Recherche et filtrage : `find()` et `find_all()`](#6-recherche-et-filtrage--find-et-find_all)
7. [Sélecteurs CSS : `select()`](#7-sélecteurs-css--select)
8. [Parcourir l'arbre](#8-parcourir-larbre)
9. [Extraire des données : recettes](#9-extraire-des-données--recettes)
10. [Modifier l'arbre](#10-modifier-larbre)
11. [Sortie et formatage](#11-sortie-et-formatage)
12. [Éléments spéciaux et HTML mal formé](#12-éléments-spéciaux-et-html-mal-formé)
13. [Récupérer des pages : `requests`, `httpx` et pages dynamiques](#13-récupérer-des-pages--requests-httpx-et-pages-dynamiques)
14. [Scraper de façon responsable](#14-scraper-de-façon-responsable)
15. [Projet complet : citations avec pagination](#15-projet-complet--citations-avec-pagination)
16. [Performances et optimisation](#16-performances-et-optimisation)
17. [Sujets avancés : XML, encodages, typage](#17-sujets-avancés--xml-encodages-typage)
18. [Erreurs courantes et débogage](#18-erreurs-courantes-et-débogage)
19. [Alternatives, aide-mémoire et ressources](#19-alternatives-aide-mémoire-et-ressources)

> **Légende** : *(ajout)* = notion absente du guide d'origine ; *(à jour)* = correction ou pratique moderne remplaçant une ancienne.
>
> **Convention pour les exemples** : chaque section commence par un extrait autonome (imports et données compris). Les extraits suivants d'une même section se lisent comme les cellules d'un notebook et réutilisent ses variables (`soup`, `html`…). Installation préalable : `pip install beautifulsoup4 lxml html5lib requests`.

---

# 1. Introduction

## 1.1 Qu'est-ce que BeautifulSoup ?

**Beautiful Soup** (paquet `beautifulsoup4`, import `bs4`) est une bibliothèque Python qui **analyse du HTML ou du XML** — même **mal formé** — et construit un **arbre d'objets** que l'on peut **parcourir, rechercher et modifier** facilement.

> Beautiful Soup **n'effectue pas de requêtes réseau** et **n'exécute pas de JavaScript** : il analyse un texte déjà obtenu (via `requests`, `httpx`, un navigateur piloté, un fichier…). Il s'associe à un **parseur** (`html.parser`, `lxml`, `html5lib`) qui fait le travail de découpage.

## 1.2 Cas d'usage

| Usage | Exemple |
| --- | --- |
| **Web scraping** | Annonces, prix, titres d'actualités, tableaux |
| **Extraction depuis du HTML/XML approximatif** | Pages anciennes, e-mails HTML, exports |
| **Nettoyage et transformation de balisage** | Supprimer des balises, réécrire des liens |
| **Analyse de documents** | Flux RSS/Atom, sitemaps XML, fichiers de configuration XML |
| **Tests** | Vérifier le HTML produit par une application |

## 1.3 Versions et état du projet *(à jour)*

| Version | Date | À retenir |
| --- | --- | --- |
| 4.12 | 2023 | API **`soup.css`** (accès à Soup Sieve), nouveaux outils CSS |
| **4.13.0** | **février 2025** | **Annotations de types** sur toute l'API publique, nouvelle classe **`ElementFilter`**, `SoupStrainer` refondu, **nombreuses dépréciations** (noms hérités en camelCase : `findAll`, `findNext`, `replaceWith`…) |
| 4.14 – **4.15** | 2025 – 2026 | Corrections et améliorations ; les anciens noms **fonctionnent encore** mais émettent un `DeprecationWarning` |

Autres points :

- Les noms hérités de Beautiful Soup 3 et du début de la v4 (`findAll`, `findChildren`, `renderContents`, `replaceWith`, `nextSibling`…) sont **dépréciés** : utilisez la forme en `snake_case` (`find_all`, `.children`, `decode_contents`, `replace_with`, `next_sibling`).
- L'argument **`text=`** de `find()` / `find_all()` est déprécié : utilisez **`string=`**.
- Python **3.7 minimum** (versions récentes : Python 3.9 et plus recommandé).

```python
import bs4
print(bs4.__version__)
```

## 1.4 Bien choisir son outil *(ajout)*

| Besoin | Outil |
| --- | --- |
| Extraire des données d'un **HTML statique** | **Beautiful Soup** (+ `requests` / `httpx`) |
| Page construite par **JavaScript** | **Playwright** / **Selenium** (puis Beautiful Soup sur `page.content()`) ; ou appeler directement l'**API** utilisée par la page |
| **Gros crawl** (milliers de pages, files, reprise, export) | **Scrapy** |
| Très **rapide** / **XPath** | **`lxml`** (`lxml.html`), **`parsel`**, **`selectolax`** |
| **Tableaux HTML → DataFrame** | **`pandas.read_html()`** |
| Existe une **API officielle ou un export** | **L'utiliser plutôt que scraper** |

> **Avant de scraper**, vérifiez les **conditions d'utilisation**, le fichier **`robots.txt`**, la législation sur les **données personnelles** (RGPD) et le **droit d'auteur** : voir [section 14](#14-scraper-de-façon-responsable).

---

# 2. Installation et parseurs

## 2.1 Installation

```bash
pip install beautifulsoup4                    # (ou : uv add beautifulsoup4)
pip install lxml html5lib                     # parseurs optionnels
```

> Le paquet s'appelle **`beautifulsoup4`** (et non `bs4`, ni `BeautifulSoup`, qui correspond à l'ancienne version 3). On l'**importe** pourtant avec `from bs4 import BeautifulSoup`.

Travaillez dans un **environnement virtuel** (`python -m venv .venv`) et épinglez vos versions (`requirements.txt`, `uv.lock`).

## 2.2 Les parseurs

| Parseur | Argument | Points forts | Limites |
| --- | --- | --- | --- |
| **`html.parser`** | `"html.parser"` | **Intégré** à Python, aucune installation, assez correct | Moins rapide que `lxml` ; traite moins bien certains HTML très cassés |
| **`lxml`** | `"lxml"` | **Très rapide**, tolérant, **ajoute** `<html><body>` si absents | Dépendance C (installation via *wheel*) |
| **`lxml-xml`** / **`xml`** | `"xml"` | **Seul** parseur XML de Beautiful Soup | Strict (XML bien formé), nécessite `lxml` |
| **`html5lib`** | `"html5lib"` | Analyse **comme un navigateur** (spécification HTML5), le plus **tolérant** | **Le plus lent**, dépendance Python pure |

### Comparaison

| | `html.parser` | `lxml` | `html5lib` |
| --- | --- | --- | --- |
| Vitesse | Moyenne | **Rapide** | Lente |
| Tolérance aux erreurs | Moyenne | Bonne | **Maximale** (comme un navigateur) |
| Installation | Aucune | `pip install lxml` | `pip install html5lib` |
| Structure complétée | Non (fragment conservé) | Oui (`html`/`body`) | Oui (`html`/`head`/`body`) |
| XML | Non | Oui (`"xml"`) | Non |

### Le même HTML cassé, trois résultats

```python
# Nécessite : pip install beautifulsoup4 lxml html5lib
from bs4 import BeautifulSoup

mauvais = "<div><p>Paragraphe<p>Autre<b>gras</div>"

for parseur in ("html.parser", "lxml", "html5lib"):
    print(f"{parseur:12} →", BeautifulSoup(mauvais, parseur))

# html.parser  → <div><p>Paragraphe<p>Autre<b>gras</b></p></p></div>             (paragraphes IMBRIQUÉS)
# lxml         → <html><body><div><p>Paragraphe</p><p>Autre<b>gras</b></p></div></body></html>
# html5lib     → <html><head></head><body><div><p>Paragraphe</p><p>Autre<b>gras</b></p></div></body></html>
```

> **Conséquence** : l'arbre dépend du parseur ; si votre code fonctionne avec l'un et pas avec l'autre, c'est souvent une **différence de réparation du HTML**. **Précisez toujours le parseur** (sinon Beautiful Soup choisit lui-même et peut afficher un avertissement) et gardez le même en développement et en production.

## 2.3 Quel parseur choisir ?

| Situation | Choix |
| --- | --- |
| Usage général, performances | **`lxml`** |
| Aucune dépendance autorisée | `html.parser` |
| HTML **très** défectueux, rendu « comme Chrome » | `html5lib` |
| Documents **XML** | `"xml"` |

---

# 3. Créer un objet `BeautifulSoup`

## 3.1 Syntaxe de base

```python
from bs4 import BeautifulSoup

html = """
<html><head><title>Page de test</title></head>
<body><h1>Titre principal</h1><p>Bonjour, monde !</p></body></html>
"""

soup = BeautifulSoup(html, "lxml")             # (marquage, parseur)
print(soup.title.string)                        # Page de test
print(soup.h1.text)                             # Titre principal
```

Le premier argument peut être une **chaîne** (`str`), des **octets** (`bytes`) ou un **fichier ouvert**.

## 3.2 Depuis un fichier

```python
from pathlib import Path

from bs4 import BeautifulSoup

html = "<html><head><title>Page de test</title></head><body><h1>Titre principal</h1></body></html>"
Path("exemple.html").write_text(html, encoding="utf-8")        # crée le fichier utilisé ci-dessous

with open("exemple.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "lxml")                            # on peut passer l'objet fichier directement
print(soup.title.string)                                       # Page de test

# Ou en octets : Beautiful Soup détecte lui-même l'encodage (meta charset, BOM, heuristiques)
with open("exemple.html", "rb") as f:
    soup = BeautifulSoup(f.read(), "lxml")
print(soup.h1.string)                                          # Titre principal
```

## 3.3 Depuis le web

```python
import requests
from bs4 import BeautifulSoup

reponse = requests.get("https://example.com", timeout=10)      # toujours un délai d'expiration
reponse.raise_for_status()                                      # lève une exception pour les codes 4xx / 5xx

soup = BeautifulSoup(reponse.content, "lxml")                   # passer .content (octets) : meilleure détection d'encodage
print(soup.title.string)                                        # Example Domain
```

> **`reponse.content`** (octets) plutôt que `reponse.text` : Beautiful Soup lit l'encodage déclaré dans le document (`<meta charset>`) alors que `requests` peut se tromper quand l'en-tête HTTP est absent (il se rabat parfois sur `ISO-8859-1`). Voir [17.2](#172-encodages).

## 3.4 Paramètres utiles du constructeur

| Paramètre | Rôle |
| --- | --- |
| `features` | Parseur (`"lxml"`, `"html.parser"`, `"html5lib"`, `"xml"`) |
| `from_encoding` | Imposer l'encodage d'un document en octets |
| `parse_only` | Ne construire qu'une **partie** de l'arbre (`SoupStrainer`, section 16) |
| `multi_valued_attributes` | Contrôler les attributs à valeurs multiples (`class`) ; `None` pour les garder en chaîne |
| `element_classes` | Classes personnalisées pour les balises |
| `attribute_dict_class` | Type de dictionnaire des attributs (4.13) |

```python
from bs4 import BeautifulSoup

html = '<p class="a b">Texte</p>'

soup = BeautifulSoup(html, "lxml", multi_valued_attributes=None)       # class reste une chaîne
print(soup.p["class"])                                                  # a b
```

---

# 4. Les objets de l'arbre

Beautiful Soup transforme le document en **arbre** composé de quatre sortes d'objets principales.

| Objet | Description | Exemple |
| --- | --- | --- |
| **`BeautifulSoup`** | L'**objet racine** (le document entier) ; se comporte comme un `Tag` | `soup` |
| **`Tag`** | Une **balise** HTML/XML (nom, attributs, enfants) | `<a href="…">` |
| **`NavigableString`** | Un **texte** à l'intérieur d'une balise (se comporte comme une `str` Python) | `"Bonjour"` |
| **`Comment`** et autres chaînes spéciales | Commentaires, `CData`, `Doctype`, instructions de traitement… | `<!-- … -->` |

```python
from bs4 import BeautifulSoup, Tag, NavigableString, Comment

soup = BeautifulSoup('<p class="intro">Salut <b>toi</b><!-- note --></p>', "lxml")
p = soup.p

print(type(soup).__name__, type(p).__name__)                  # BeautifulSoup Tag
print([type(x).__name__ for x in p.contents])                 # ['NavigableString', 'Tag', 'Comment']
print(isinstance(p.contents[0], NavigableString))             # True
print(p.name, p.attrs)                                        # p {'class': ['intro']}
```

> **Les enfants d'une balise sont de deux types** : des `Tag` **et** des chaînes (`NavigableString`, y compris les **retours à la ligne** entre balises). Une grande partie des confusions de débutants vient de là.

---

# 5. Navigation de base et attributs

## 5.1 Accéder aux balises comme des attributs

```python
from bs4 import BeautifulSoup

html = """
<html>
  <head><title>Page d'exemple</title></head>
  <body>
    <h1>Titre principal</h1>
    <p class="intro">Premier paragraphe.</p>
    <p>Second paragraphe.</p>
  </body>
</html>
"""
soup = BeautifulSoup(html, "lxml")

print(soup.title)               # <title>Page d'exemple</title>
print(soup.title.name)          # title
print(soup.title.string)        # Page d'exemple
print(soup.body.h1)             # <h1>Titre principal</h1>
print(soup.p)                   # le PREMIER <p> seulement : <p class="intro">Premier paragraphe.</p>
```

> `soup.p` ne renvoie que la **première** balise de ce nom, et **`None`** s'il n'y en a pas : `soup.table.tr` lève alors `AttributeError: 'NoneType' object has no attribute 'tr'`. Pour plusieurs balises ou une recherche sûre : `find()` / `find_all()` / `select()`.

## 5.2 Propriétés courantes d'une balise

```python
from bs4 import BeautifulSoup

a = BeautifulSoup('<a href="https://example.com" class="lien externe" id="accueil">Accueil</a>', "lxml").a

print(a.name)                   # a
print(a.attrs)                  # {'href': 'https://example.com', 'class': ['lien', 'externe'], 'id': 'accueil'}
print(a["href"])                # https://example.com        → KeyError si l'attribut est absent
print(a.get("target"))          # None                       → sûr
print(a.get("target", "_self")) # _self
print(a.get("class"))           # ['lien', 'externe']        → attribut à VALEURS MULTIPLES : liste
print(a.has_attr("id"))         # True
print(a.get_attribute_list("class"))      # toujours une liste (utile pour traiter un attribut uniformément)
```

### Attributs à valeurs multiples

`class`, `rel`, `rev`, `accept-charset`, `headers`, `accesskey`, `dropzone` sont des **listes** (HTML : valeurs séparées par des espaces) :

```python
print(a["class"])               # ['lien', 'externe']
print(" ".join(a["class"]))     # lien externe
```

## 5.3 Contenu textuel

| Propriété / méthode | Résultat |
| --- | --- |
| `.string` | Le texte de la balise **s'il n'y en a qu'un seul** (balise sans enfant ou avec un seul enfant) ; sinon **`None`** |
| `.text` | **Tout** le texte contenu (descendants compris), concaténé |
| `.get_text()` | Idem, avec options (`separator`, `strip`) |
| `.strings` / `.stripped_strings` | **Générateurs** des morceaux de texte (bruts / nettoyés) |

```python
from bs4 import BeautifulSoup

div = BeautifulSoup("<div><p>Bonjour <b>le monde</b></p></div>", "lxml").div

print(div.string)                       # None   (plusieurs enfants)
print(div.p.string)                     # None   (le <p> a deux enfants : un texte et <b>)
print(div.b.string)                     # le monde
print(div.text)                         # Bonjour le monde
print(div.get_text(" ", strip=True))    # Bonjour le monde
print(list(div.stripped_strings))       # ['Bonjour', 'le monde']
```

> `.text` d'un document inclut le contenu des balises `<script>` et `<style>` : retirez-les avant (`for t in soup(["script", "style"]): t.decompose()`).

## 5.4 Raccourci d'appel

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup("<p>Texte</p><a href='/x'>Lien</a><script>var x = 1;</script>", "lxml")

print(soup("a"))                        # équivaut à soup.find_all("a")
print(soup(["a", "script"]))            # plusieurs noms de balises
```

---

# 6. Recherche et filtrage : `find()` et `find_all()`

## 6.1 Les deux méthodes

| Méthode | Renvoie | Si rien |
| --- | --- | --- |
| `find(...)` | **La première** balise correspondante | `None` |
| `find_all(...)` | **Toutes** les correspondances (objet `ResultSet`, sous-classe de `list`) | Liste **vide** |

```python
import re

from bs4 import BeautifulSoup

html = """
<html><body>
  <div class="item">Objet 1</div>
  <div class="item promo">Objet 2</div>
  <div class="pied">Pied de page</div>
  <a href="/a">A</a> <a>sans lien</a> <a href="https://exemple.fr/b">B</a>
</body></html>
"""
soup = BeautifulSoup(html, "lxml")

premier = soup.find("div", class_="item")
tous = soup.find_all("div", class_="item")
print(premier.text)                                  # Objet 1
print([d.text for d in tous])                        # ['Objet 1', 'Objet 2']
```

Signature : `find_all(name, attrs, recursive, string, limit, **kwargs)`.

## 6.2 Les filtres

| Filtre | Exemple | Sélectionne… |
| --- | --- | --- |
| **Nom** (chaîne) | `find_all("a")` | Balises `<a>` |
| **Liste** | `find_all(["h1", "h2", "h3"])` | L'une de ces balises |
| **Expression régulière** | `find_all(re.compile("^h[1-6]$"))` | Noms correspondant au motif |
| **`True`** | `find_all(True)` · `find_all("a", href=True)` | Toutes les balises · balises **ayant** l'attribut |
| **Fonction** | `find_all(ma_fonction)` | Balises pour lesquelles la fonction renvoie `True` |
| **`string=`** | `find_all(string="Objet 1")` | **Textes** (et non balises) correspondants |

### Par attributs

```python
print(soup.find_all("a", href=True))                          # <a> ayant un href
print(soup.find_all("a", attrs={"href": "/a"}))               # attrs= pour les noms non valides en Python
print(soup.find("div", class_="pied"))
print(soup.find_all(attrs={"data-id": "42"}))                 # attributs data-* (liste vide ici : aucun élément n'en a)
print(soup.find_all("a", href=re.compile(r"^https://")))      # valeur par expression régulière
print(soup.find_all("a", href=lambda v: v and v.endswith(".pdf")))     # valeur par fonction
```

### La classe CSS : `class_`

`class` est un mot réservé de Python : on écrit **`class_`** (ou `attrs={"class": …}`).

```python
print(soup.find_all("div", class_="item"))             # a la classe « item » (parmi d'autres) : 2 résultats
print(soup.find_all("div", class_="item promo"))       # correspond EXACTEMENT à la chaîne « item promo » (ordre compris)
print(soup.find_all("div", class_=["item", "pied"]))   # l'une OU l'autre : 3 résultats
```

> Pour plusieurs classes simultanées, préférez un **sélecteur CSS** : `soup.select("div.item.promo")` (plus fiable).

### Par fonction (et `lambda`)

```python
def a_classe_sans_id(balise):
    return balise.has_attr("class") and not balise.has_attr("id")


print(soup.find_all(a_classe_sans_id))
print(soup.find_all(lambda t: t.name == "a" and len(t.attrs) == 0))
```

### Par texte et expression régulière

```python
import re

print(soup.find_all(string=re.compile("Objet")))           # chaînes (NavigableString) contenant « Objet »
print(soup.find_all("div", string="Objet 1"))              # balises dont le .string vaut exactement ce texte
print(soup.find_all("div", string=re.compile(r"Objet \d")))
print(soup.find_all(re.compile("^d")))                     # balises dont le nom commence par « d »
```

> **À jour** : `find_all(text=…)` est **déprécié** ; écrivez `string=…`.

## 6.3 Options de recherche

```python
print(soup.find_all("a", limit=2))                    # s'arrête après 2 résultats
print(soup.body.find_all("div", recursive=False))     # uniquement les ENFANTS DIRECTS (pas les descendants)
```

## 6.4 Rechercher dans une direction

`find()` / `find_all()` existent aussi **relatifs à un élément** :

| Méthode | Recherche dans… |
| --- | --- |
| `find_parent("div")` · `find_parents("div")` | Les **ancêtres** |
| `find_next_sibling("p")` · `find_next_siblings("p")` | Les **frères suivants** |
| `find_previous_sibling("p")` · `find_previous_siblings("p")` | Les **frères précédents** |
| `find_next("p")` · `find_all_next("p")` | **Tout ce qui suit** dans le document (ordre de lecture) |
| `find_previous("p")` · `find_all_previous("p")` | **Tout ce qui précède** |

```python
from bs4 import BeautifulSoup

html = """
<section>
  <h2>Prix</h2>
  <p>12 euros</p>
  <table><tr><td>Détail</td></tr></table>
</section>
"""
soup = BeautifulSoup(html, "lxml")

titre = soup.find("h2", string="Prix")
valeur = titre.find_next_sibling("p")              # le paragraphe juste après un titre repéré
tableau = titre.find_next("table")
section = titre.find_parent("section")

print(valeur.get_text())                            # 12 euros
print(tableau.get_text(strip=True))                 # Détail
print(section.name)                                 # section
```

> Les anciens noms en camelCase (`findAll`, `findNext`, `findParent`, `findNextSibling`…) sont **dépréciés** : n'utilisez que les noms en `snake_case`.

## 6.5 `find()` ou `select()` ?

| | `find` / `find_all` | `select` / `select_one` |
| --- | --- | --- |
| Syntaxe | Arguments Python | **Sélecteurs CSS** (comme dans les DevTools) |
| Plusieurs classes, relations | Verbeux | Concis |
| Filtres par **fonction / expression régulière** | Oui | Limité (`:-soup-contains`) |
| Recherche **relative** (frères, ancêtres) | Oui, méthodes dédiées | via combinateurs |
| Lisibilité des cas courants | Bonne | **Excellente** (copiable depuis le navigateur) |

---

# 7. Sélecteurs CSS : `select()`

## 7.1 `select()` et `select_one()`

Beautiful Soup s'appuie sur la bibliothèque **Soup Sieve**, qui implémente une très grande partie des sélecteurs CSS (niveaux 1 à 4).

| Méthode | Renvoie | Si rien |
| --- | --- | --- |
| `select(sel)` | **Liste** de toutes les balises correspondantes | `[]` |
| `select_one(sel)` | La **première** balise | `None` |

```python
from bs4 import BeautifulSoup

html = """
<div class="conteneur">
  <p id="premier">Bonjour</p>
  <p class="surligne">Monde</p>
  <a href="#">Lien</a>
</div>
"""
soup = BeautifulSoup(html, "lxml")

print([p.text for p in soup.select("p")])             # ['Bonjour', 'Monde']
print(soup.select_one("p").text)                      # Bonjour
print(soup.select_one(".surligne").text)              # Monde
print(soup.select_one("#premier").text)               # Bonjour
```

> **Astuce** : dans les DevTools du navigateur, clic droit sur un élément → *Copier* → *Copier le sélecteur*, puis ajustez-le (les sélecteurs générés sont souvent trop précis et fragiles).

## 7.2 Sélecteurs de base et combinateurs

| Sélecteur | Sélectionne |
| --- | --- |
| `p` | Toutes les balises `<p>` |
| `.classe` | Éléments avec cette classe |
| `#id` | L'élément avec cet identifiant |
| `*` | Tous les éléments |
| `div p` | `<p>` **descendants** (à tout niveau) de `<div>` |
| `div > p` | `<p>` **enfants directs** de `<div>` |
| `h2 + p` | `<p>` **immédiatement après** un `<h2>` (frère adjacent) |
| `h2 ~ p` | **Tous** les `<p>` frères **suivant** un `<h2>` |
| `a, b` | Les éléments de l'un **ou** l'autre sélecteur |

```python
print(soup.select("div p"))
print(soup.select("div > p"))
print(soup.select("p + a"))
print(soup.select("div.conteneur > p.surligne"))        # combinaisons
```

## 7.3 Sélecteurs d'attributs

| Sélecteur | Signification |
| --- | --- |
| `[attr]` | L'attribut existe |
| `[attr="v"]` | Valeur **exacte** |
| `[attr~="v"]` | Contient le **mot** `v` (séparé par des espaces) |
| `[attr\|="v"]` | Vaut `v` ou commence par `v-` (ex. langues) |
| `[attr^="v"]` | **Commence** par `v` |
| `[attr$="v"]` | **Se termine** par `v` |
| `[attr*="v"]` | **Contient** `v` |
| `[attr="v" i]` | Comparaison **insensible à la casse** |

```python
from bs4 import BeautifulSoup

html = """
<a href="https://exemple.fr/a">Sécurisé</a>
<a href="/doc/guide.pdf">Guide</a>
<img src="/img/logo.png" data-id="7">
"""
soup = BeautifulSoup(html, "lxml")

print(soup.select("a[href]"))                       # <a> avec un href
print(soup.select('a[href^="https://"]'))           # liens sécurisés
print(soup.select('a[href$=".pdf"]'))               # liens vers des PDF
print(soup.select('img[src*="logo"]'))
print(soup.select("[data-id]"))
```

## 7.4 Pseudo-classes prises en charge *(à jour : bien plus que « limité »)*

L'original indiquait un support « limité » ; **Soup Sieve** gère en réalité de nombreuses pseudo-classes :

| Catégorie | Pseudo-classes |
| --- | --- |
| **Position** | `:first-child`, `:last-child`, `:only-child`, `:nth-child(2n+1)`, `:nth-last-child()`, `:first-of-type`, `:last-of-type`, `:nth-of-type()`, `:only-of-type` |
| **Logiques** | **`:not()`**, **`:is()`** (`:matches()`, `:any()`), **`:where()`**, **`:has()`** |
| **Contenu** | **`:-soup-contains("texte")`**, `:-soup-contains-own("texte")`, `:empty`, `:root` |
| **États HTML** | `:checked`, `:disabled`, `:enabled`, `:required`, `:optional`, `:read-only`, `:link`, `:any-link`… |
| **Autres** | `:lang()`, `:dir()`, `:defined`… |

> Les pseudo-classes **dynamiques** (`:hover`, `:focus`, `:visited`, `:active`…) ne s'appliquent pas à un document statique.

```python
from bs4 import BeautifulSoup

html = """
<ul><li>Un</li><li class="cache">Deux</li><li>Trois</li></ul>
<table><tr><td>1</td></tr><tr><td>2</td></tr><tr><td>3</td></tr></table>
<div><img src="a.png"></div><div><p>Sans image</p></div>
<p>Bonjour Monde</p>
<h2>Prix</h2><p>10 euros</p>
"""
soup = BeautifulSoup(html, "lxml")

print(soup.select("li:first-child"))
print(soup.select("tr:nth-child(odd)"))
print(soup.select("li:not(.cache)"))
print(soup.select("div:has(> img)"))                         # <div> qui contient directement une <img>
print(soup.select("p:-soup-contains('Monde')"))              # <p> contenant le texte « Monde »
print(soup.select("h2:-soup-contains-own('Prix') + p"))
```

> **À jour** : `:contains()` est **déprécié** (avertissement `FutureWarning`) ; utilisez **`:-soup-contains()`**.

## 7.5 L'interface `soup.css` *(ajout, 4.12+)*

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup('<p id="premier">Bonjour</p><p class="surligne">Monde</p>', "lxml")

print(soup.css.select("p.surligne"))              # équivaut à soup.select(...)
print(soup.css.select_one("#premier"))
print(list(soup.css.iselect("p")))                # ITÉRATEUR (évite de construire la liste complète)
print(soup.body.css.filter("p"))                  # filtre les ENFANTS directs qui correspondent
print(soup.p.css.match("#premier"))               # cet élément correspond-il au sélecteur ?
print(soup.css.escape("a:b"))                     # échappe un identifiant à utiliser dans un sélecteur
print(soup.select("p", limit=1))                  # limiter le nombre de résultats
```

> `select()` appelé sur une **balise** cherche dans ses **descendants** : `soup.select_one("table").select("tr > td")`.

## 7.6 Espaces de noms (XML)

```python
from bs4 import BeautifulSoup

xml_texte = """<?xml version="1.0" encoding="UTF-8"?>
<notice xmlns:dc="http://purl.org/dc/elements/1.1/">
  <dc:title>Le Petit Prince</dc:title>
</notice>"""

xml = BeautifulSoup(xml_texte, "xml")             # nécessite lxml
print(xml.select("dc|title", namespaces={"dc": "http://purl.org/dc/elements/1.1/"}))
```

---

# 8. Parcourir l'arbre

## 8.1 Enfants et descendants

| Propriété | Type | Contenu |
| --- | --- | --- |
| `.contents` | **liste** | Enfants **directs** (balises et textes) |
| `.children` | **itérateur** | Enfants directs (pour une boucle) |
| `.descendants` | **itérateur** | **Tous** les descendants (enfants, petits-enfants…) |
| `.strings` / `.stripped_strings` | itérateurs | Tous les **textes** descendants (bruts / sans espaces en bordure) |

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup("<div><p>Premier</p><p>Second</p>Texte</div>", "lxml")
div = soup.div

print(div.contents)                         # [<p>Premier</p>, <p>Second</p>, 'Texte']
for enfant in div.children:
    print(repr(enfant))

for descendant in div.descendants:          # <p>, 'Premier', <p>, 'Second', 'Texte'
    print(repr(descendant))

print(list(div.stripped_strings))           # ['Premier', 'Second', 'Texte']
```

> Pour ne garder que les **balises** parmi les enfants : `[e for e in div.children if e.name]` ou `div.find_all(recursive=False)`.

## 8.2 Parents

| Propriété | Contenu |
| --- | --- |
| `.parent` | Le **parent direct** (`None` pour la racine) |
| `.parents` | Itérateur sur **tous les ancêtres**, jusqu'à la racine |

```python
p = soup.p
print(p.parent.name)                        # div
print([a.name for a in p.parents])          # ['div', 'body', 'html', '[document]']
```

## 8.3 Frères (*siblings*)

| Propriété | Contenu |
| --- | --- |
| `.next_sibling` / `.previous_sibling` | Le nœud **suivant / précédent** de même niveau (**balise ou texte**) |
| `.next_siblings` / `.previous_siblings` | Itérateurs sur **tous** les frères suivants / précédents |

```python
from bs4 import BeautifulSoup

html = "<ul>\n  <li>A</li>\n  <li>B</li>\n</ul>"
li = BeautifulSoup(html, "html.parser").li

print(repr(li.next_sibling))                # '\n  '   ← un TEXTE (retour à la ligne), pas la balise suivante !
print(li.next_sibling.next_sibling)         # <li>B</li>
print(li.find_next_sibling("li"))           # <li>B</li> : saute les textes, plus robuste
```

> **Piège classique** : les espaces et retours à la ligne entre balises sont des **nœuds texte**. Préférez **`find_next_sibling()`** à `.next_sibling`.

## 8.4 Ordre du document : `.next_element` / `.previous_element`

Ils suivent l'**ordre d'analyse** du document (balise ouvrante, texte, balise suivante…), indépendamment de la hiérarchie :

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup("<a><b>x</b></a><c>y</c>", "html.parser")
print(soup.b.next_element)                  # x
print(soup.b.next_element.next_element)     # <c>y</c>
for e in soup.b.next_elements:
    print(repr(e))
```

---

# 9. Extraire des données : recettes

*(Section ajoutée : exemples concrets d'extraction. Tous les extraits de cette section partagent le document `html` et l'objet `soup` définis en 9.1.)*

## 9.1 Liens et URL absolues

```python
from urllib.parse import urljoin

from bs4 import BeautifulSoup

html = """
<html><head>
  <title>Boutique</title>
  <meta name="description" content="Catalogue de papeterie">
  <meta property="og:image" content="https://exemple.fr/img/couverture.jpg">
  <link rel="canonical" href="https://exemple.fr/articles/">
  <script type="application/ld+json">{"@type": "Organization", "name": "Papeterie Exemple"}</script>
</head><body>
  <nav><a href="/accueil">Accueil</a> <a href="../contact">Contact</a></nav>
  <ul class="produits"><li>Stylo</li><li>Cahier</li></ul>
  <table id="prix">
    <thead><tr><th>Produit</th><th>Prix</th></tr></thead>
    <tbody>
      <tr><td>Stylo</td><td>1,50 €</td></tr>
      <tr><td>Cahier</td><td>3,20 €</td></tr>
    </tbody>
  </table>
  <div class="produit"><h2 class="nom">Stylo</h2><span class="prix">1,50 €</span><a href="/produits/stylo">Voir</a></div>
  <div class="produit"><h2 class="nom">Cahier</h2><a href="/produits/cahier">Voir</a></div>
  <form id="connexion" action="/login" method="post">
    <input type="hidden" name="csrf" value="abc123"><input type="text" name="email">
  </form>
  <img src="img/logo.png">
</body></html>
"""
soup = BeautifulSoup(html, "lxml")

base = "https://exemple.fr/articles/"
liens = []
for a in soup.select("a[href]"):
    liens.append({
        "texte": a.get_text(strip=True),
        "url": urljoin(base, a["href"]),             # transforme « ../page » ou « /page » en URL complète
    })

images = [urljoin(base, img["src"]) for img in soup.select("img[src]")]
print(liens)
print(images)
```

## 9.2 Listes

```python
produits = [li.get_text(strip=True) for li in soup.select("ul.produits > li")]
print(produits)                                       # ['Stylo', 'Cahier']
```

## 9.3 Tableaux HTML

```python
tableau = soup.select_one("table#prix")
entetes = [th.get_text(strip=True) for th in tableau.select("thead th")]

lignes = []
for tr in tableau.select("tbody tr"):
    cellules = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
    lignes.append(dict(zip(entetes, cellules)))                # liste de dictionnaires

print(lignes[0])                                                # {'Produit': 'Stylo', 'Prix': '1,50 €'}
```

Raccourci pour obtenir des **DataFrames** pandas :

```python
from io import StringIO

import pandas as pd

tables = pd.read_html(StringIO(str(soup)))          # liste de DataFrames (nécessite lxml ou html5lib)
print(tables[0])
```

## 9.4 Un bloc répété (cartes de produits)

```python
resultats = []
for carte in soup.select("div.produit"):
    nom = carte.select_one("h2.nom")
    prix = carte.select_one("span.prix")
    lien = carte.select_one("a[href]")
    resultats.append({
        "nom": nom.get_text(strip=True) if nom else None,           # toujours tester None
        "prix": prix.get_text(strip=True) if prix else None,
        "url": urljoin(base, lien["href"]) if lien else None,
    })
print(resultats)
```

> **Motif robuste** : bouclez sur le **conteneur** de chaque élément, puis cherchez les champs **à l'intérieur** (pas de listes parallèles qui se décalent si un champ manque).

## 9.5 Texte propre

```python
import re

texte = soup.get_text(separator="\n", strip=True)


def nettoyer(t: str) -> str:
    return re.sub(r"\s+", " ", t).strip()            # réduit tous les espaces / sauts de ligne


print(nettoyer(texte)[:80])

prix = float(re.sub(r"[^\d,]", "", "1 234,50 €").replace(",", "."))      # 1234.5
print(prix)
```

## 9.6 Métadonnées de la page

```python
titre = soup.title.string if soup.title else None

description = soup.find("meta", attrs={"name": "description"})
description = description["content"] if description else None

og_image = soup.select_one('meta[property="og:image"]')
og_image = og_image["content"] if og_image else None

canonique = soup.select_one('link[rel="canonical"]')
canonique = canonique.get("href") if canonique else None

print(titre, description, og_image, canonique, sep="\n")
```

## 9.7 Données structurées (JSON-LD et données intégrées)

De nombreux sites embarquent leurs données en **JSON** : c'est souvent **plus fiable** que d'extraire le HTML.

```python
import json

for script in soup.select('script[type="application/ld+json"]'):
    try:
        donnees = json.loads(script.string)
    except (json.JSONDecodeError, TypeError):
        continue
    if isinstance(donnees, dict):
        print(donnees.get("@type"), donnees.get("name"))      # Organization Papeterie Exemple
```

Cherchez aussi `<script id="__NEXT_DATA__">`, `window.__INITIAL_STATE__`, les microdata (`itemprop`)… et l'onglet **Réseau** des DevTools : la page appelle peut-être une **API JSON** directement utilisable (méthode la plus propre).

## 9.8 Formulaires

```python
formulaire = soup.select_one("form#connexion")
action = formulaire.get("action")
champs = {i.get("name"): i.get("value", "") for i in formulaire.select("input[name]")}      # champs cachés (jetons CSRF…)
print(action, champs)                                 # /login {'csrf': 'abc123', 'email': ''}
```

---

# 10. Modifier l'arbre

Beautiful Soup permet de **modifier** le document (nettoyage, transformation) puis de le réécrire.

## 10.1 Modifier texte et attributs

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup('<a href="/x" class="a">Lien</a>', "html.parser")
a = soup.a

a.string = "Nouveau texte"                  # remplace tout le contenu
a["href"] = "https://exemple.fr"            # modifier / ajouter un attribut
a["class"] = ["lien", "externe"]            # attribut à valeurs multiples : liste
del a["class"]                              # supprimer un attribut
a.name = "span"                             # renommer la balise
print(soup)
```

## 10.2 Créer et ajouter des éléments

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup("<div><p>Premier</p></div>", "html.parser")
div = soup.div

nouveau = soup.new_tag("p", attrs={"class": "note"})        # new_tag(nom, attrs=…, **attributs)
nouveau.string = "Second"
div.append(nouveau)                                          # ajoute À LA FIN

div.insert(0, soup.new_tag("h1"))                            # insère à une position
div.h1.string = "Titre"

texte = soup.new_string("du texte libre")
div.append(texte)

div.extend([soup.new_tag("hr"), soup.new_tag("br")])         # plusieurs d'un coup
div.p.insert_before(soup.new_tag("span"))                    # avant / après un élément
div.p.insert_after(soup.new_tag("span"))
print(div.prettify())
```

## 10.3 Supprimer

| Méthode | Effet |
| --- | --- |
| `.extract()` | **Retire** l'élément de l'arbre et le **renvoie** (réutilisable) |
| `.decompose()` | **Détruit** l'élément et ses descendants (libère la mémoire ; **inutilisable** ensuite) |
| `.clear()` | Vide le **contenu** mais garde la balise |
| `.unwrap()` | Supprime la balise mais **garde son contenu** |

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup("<div><p>A</p><p>B</p></div>", "html.parser")

retire = soup.p.extract()              # <p>A</p>  (peut être réinséré ailleurs)
soup.p.decompose()                     # supprime <p>B</p> définitivement
print(soup)                            # <div></div>
```

### Nettoyage typique avant extraction de texte

```python
html = "<body><nav>Menu</nav><p>Bonjour</p><script>var x = 1;</script><footer>Pied</footer></body>"
soup = BeautifulSoup(html, "html.parser")

for balise in soup(["script", "style", "noscript", "nav", "footer"]):
    balise.decompose()
texte = soup.get_text(" ", strip=True)
print(texte)                                          # Bonjour
```

> Ne modifiez pas un résultat d'itération **pendant** qu'on le parcourt dans une boucle sur `.descendants` ; construisez d'abord la liste (`for t in list(soup.find_all("b")): …`) ou utilisez `find_all` (qui renvoie une liste complète).

## 10.4 Remplacer, envelopper, dérouler

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup("<div><a href='/x'>Lien</a></div>", "html.parser")

p = soup.new_tag("p")
p.string = "texte"
soup.div.append(p)

p.replace_with(soup.new_tag("span"))            # remplace par un autre élément (ou une chaîne)

p = soup.new_tag("p")
p.string = "x"
soup.div.append(p)
p.wrap(soup.new_tag("section"))                 # <section><p>x</p></section>
soup.section.unwrap()                           # retire <section>, garde <p>

for lien in soup.find_all("a"):
    lien.replace_with(lien.get_text())          # remplace les liens par leur texte
print(soup)                                     # <div>Lien<span></span><p>x</p></div>
```

## 10.5 Remplacer du texte

```python
import re

from bs4 import BeautifulSoup

soup = BeautifulSoup("<p>un ancien texte, un ancien mot</p>", "html.parser")

for noeud in soup.find_all(string=re.compile("ancien")):
    noeud.replace_with(noeud.replace("ancien", "nouveau"))       # NavigableString.replace_with
print(soup)                                                      # <p>un nouveau texte, un nouveau mot</p>
```

## 10.6 Fusionner les textes adjacents

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup("<p>Bonjour</p>", "html.parser")
soup.p.append(" le")
soup.p.append(" monde")
print(soup.p.contents)                # ['Bonjour', ' le', ' monde'] : trois chaînes
soup.smooth()                         # après de nombreuses modifications : fusionne les NavigableString voisines
print(soup.p.contents)                # ['Bonjour le monde']
```

---

# 11. Sortie et formatage

## 11.1 Conversions de base

| Méthode | Résultat |
| --- | --- |
| `str(soup)` / `soup.decode()` | **Chaîne** (`str`) HTML/XML |
| `soup.prettify()` | Chaîne **indentée** (lecture / débogage) |
| `soup.encode("utf-8")` | **Octets** (`bytes`) |
| `soup.decode_contents()` / `.encode_contents()` | Contenu **intérieur** sans la balise englobante |
| `soup.get_text()` | **Texte** seulement |

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup("<div><p>Bonjour</p><p>Monde</p></div>", "lxml")

print(soup.prettify())
# <html>
# <body>
# <div>
# <p>
# Bonjour
# </p>
# …

html_str = str(soup)                       # str
html_oct = soup.encode("utf-8")            # bytes
print(type(html_str).__name__, type(html_oct).__name__)       # str bytes
print(soup.div.decode_contents())          # <p>Bonjour</p><p>Monde</p>
```

> **Correction** : `.decode()` d'un objet **Beautiful Soup** renvoie une **chaîne** ; il ne faut pas le confondre avec `bytes.decode()` (`soup.encode().decode("utf-8")` fait appel à celui de `bytes`).
> `prettify()` ajoute **un retour à la ligne et une indentation autour de chaque texte** : ne l'utilisez pas pour reconstruire du HTML à diffuser (il peut modifier les espaces significatifs).

## 11.2 `get_text()` en détail

```python
from bs4 import BeautifulSoup

html = "<div><p> Bonjour </p><p> Monde </p></div>"
soup = BeautifulSoup(html, "html.parser")

print(repr(soup.get_text()))                           # ' Bonjour  Monde '
print(repr(soup.get_text(strip=True)))                 # 'BonjourMonde'    (textes collés !)
print(repr(soup.get_text(" ", strip=True)))            # 'Bonjour Monde'   séparateur + strip
print(repr(soup.get_text("\n", strip=True)))           # 'Bonjour\nMonde'
```

> `get_text(strip=True)` **sans séparateur** colle les morceaux (« BonjourMonde ») : donnez presque toujours un **`separator`**.

## 11.3 Formateurs (échappement des caractères)

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup("<p>Café &amp; croissants &lt;3</p>", "html.parser")

print(soup.decode(formatter="minimal"))     # (défaut) échappe seulement &, <, >
print(soup.decode(formatter="html"))        # entités HTML nommées : é → &eacute;
print(soup.decode(formatter="html5"))
print(soup.decode(formatter=None))          # AUCUN échappement (attention : peut produire du HTML invalide)
from bs4.formatter import HTMLFormatter
print(soup.prettify(formatter=HTMLFormatter(indent=2)))       # taille d'indentation personnalisée (2 espaces)
print(soup.decode(formatter=HTMLFormatter(entity_substitution=None)))    # équivalent de formatter=None
```

## 11.4 Enregistrer dans un fichier

```python
with open("sortie.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())

# Ou en octets :
with open("sortie.html", "wb") as f:
    f.write(soup.encode("utf-8"))
```

> Beautiful Soup n'est **pas un assainisseur de sécurité** : pour **nettoyer du HTML** non fiable (protection XSS), utilisez **`nh3`** (ou `bleach`, en maintenance), pas une liste de balises à `decompose()`.

---

# 12. Éléments spéciaux et HTML mal formé

## 12.1 Chaînes spéciales

| Classe | Représente |
| --- | --- |
| `NavigableString` | Texte ordinaire |
| `Comment` | `<!-- commentaire -->` |
| `CData` | `<![CDATA[ … ]]>` (XML) |
| `ProcessingInstruction` | `<?xml … ?>` |
| `Declaration`, `Doctype` | `<!DOCTYPE html>` |
| `Script`, `Stylesheet`, `TemplateString` | Texte des balises `<script>`, `<style>`, `<template>` (4.9+) |

```python
from bs4 import BeautifulSoup, Comment, Doctype

html = "<!DOCTYPE html><div><!-- Ceci est un commentaire --><p>Bonjour</p></div>"
soup = BeautifulSoup(html, "html.parser")

print([type(x).__name__ for x in soup.contents])                 # ['Doctype', 'Tag']

commentaires = soup.find_all(string=lambda t: isinstance(t, Comment))
for c in commentaires:
    print("Commentaire :", c.strip())
    c.extract()                                                     # supprimer le commentaire

for noeud in soup.contents:
    if isinstance(noeud, Doctype):
        print("Doctype :", noeud)                                    # html
```

> **Astuce** : les commentaires conditionnels et le contenu **commenté** (`<!-- <div>…</div> -->`) contiennent parfois des données : réanalysez le texte du commentaire avec un nouveau `BeautifulSoup`.

## 12.2 `NavigableString`

Les textes sont des `NavigableString` (sous-classe de `str`) : on les manipule comme des chaînes **et** on peut remonter vers leur parent.

```python
texte = soup.p.string
print(type(texte).__name__, texte.parent.name)                    # NavigableString p
texte.replace_with("Salut")
print(soup)
```

> Copier un texte hors de l'arbre : `str(texte)` (sinon il garde une référence vers l'arbre entier, ce qui consomme de la mémoire).

## 12.3 HTML mal formé

Beautiful Soup **répare** le HTML selon le **parseur** (voir [2.2](#22-les-parseurs)) :

```python
from bs4 import BeautifulSoup

casse = "<div><p>Paragraphe <b>gras <i>italique</p></div>"
print(BeautifulSoup(casse, "html.parser").prettify())      # balises refermées automatiquement
print(BeautifulSoup(casse, "html5lib").prettify())         # arbre conforme à HTML5, comme un navigateur
```

Outil de diagnostic : voir `bs4.diagnose` en [18.3](#183-diagnostiquer).

---

# 13. Récupérer des pages : `requests`, `httpx` et pages dynamiques

## 13.1 `requests` : l'essentiel

```bash
pip install requests
```

```python
import requests
from bs4 import BeautifulSoup

session = requests.Session()                                   # réutilise la connexion TCP, conserve les cookies
session.headers.update({"User-Agent": "MonRobot/1.0 (+https://exemple.fr/robot; contact@exemple.fr)"})

reponse = session.get("https://example.com/", timeout=(3.05, 10))      # (connexion, lecture)
reponse.raise_for_status()                                               # exceptions pour 4xx / 5xx
soup = BeautifulSoup(reponse.content, "lxml")
```

### Codes de statut

```python
import sys

import requests

reponse = requests.get("https://example.com/introuvable", timeout=10)

if reponse.status_code == 200:
    print("Page récupérée")
elif reponse.status_code == 404:
    print("Page introuvable", file=sys.stderr)
elif reponse.status_code == 429:
    print("Trop de requêtes : ralentir (en-tête Retry-After)", file=sys.stderr)
elif reponse.status_code in (403, 401):
    print("Accès refusé ou authentification requise", file=sys.stderr)
else:
    print(f"Statut inattendu : {reponse.status_code}", file=sys.stderr)
```

| Code | Signification | Réaction |
| --- | --- | --- |
| 200 | OK | Analyser |
| 301 / 302 | Redirection | `requests` suit automatiquement |
| 403 | Interdit | Ne pas contourner : vérifier les règles d'accès |
| 404 | Introuvable | Ignorer / consigner |
| **429** | Trop de requêtes | **Ralentir**, respecter `Retry-After` |
| 5xx | Erreur serveur | Nouvelle tentative avec attente croissante |

## 13.2 En-têtes et User-Agent *(à jour)*

> **Correction** : l'ancien conseil « se faire passer pour un navigateur » (copier une chaîne `Mozilla/5.0 … Chrome/58`) est **déconseillé** : cette chaîne est périmée (ancienne version) et **trompeuse**. **Identifiez-vous honnêtement** (nom du robot + contact) ; si un site bloque les robots, respectez ce choix ou demandez l'autorisation, ou cherchez une API.

```python
import requests

url = "https://example.com/"
entetes = {
    "User-Agent": "MonRobot/1.0 (+https://exemple.fr/robot; contact@exemple.fr)",
    "Accept-Language": "fr-FR,fr;q=0.9",
}
reponse = requests.get(url, headers=entetes, timeout=10)
print(reponse.status_code)
```

## 13.3 Nouvelles tentatives et résilience

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(total=3, backoff_factor=1.0, status_forcelist=[429, 500, 502, 503, 504], respect_retry_after_header=True)
session.mount("https://", HTTPAdapter(max_retries=retry))
session.mount("http://", HTTPAdapter(max_retries=retry))

reponse = session.get("https://example.com/", timeout=10)
print(reponse.status_code)
```

## 13.4 Cache local *(ajout)*

Évitez de **retélécharger** les mêmes pages pendant la mise au point :

```python
import requests_cache                                            # pip install requests-cache

session = requests_cache.CachedSession("cache_scraping", expire_after=3600)
reponse = session.get("https://example.com/", timeout=10)
print(reponse.from_cache)                                        # False au premier appel, True ensuite
```

## 13.5 `httpx` : HTTP/2 et asynchrone *(ajout)*

```python
from __future__ import annotations

import asyncio

import httpx                                                     # pip install httpx
from bs4 import BeautifulSoup


async def titre(client: httpx.AsyncClient, url: str) -> str | None:
    r = await client.get(url)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, "lxml")                      # l'analyse reste synchrone et liée au processeur
    return soup.title.string if soup.title else None


async def main(urls):
    limite = asyncio.Semaphore(5)                                # limiter la concurrence
    async with httpx.AsyncClient(timeout=10, headers={"User-Agent": "MonRobot/1.0"}) as client:
        async def un(url):
            async with limite:
                await asyncio.sleep(0.5)                         # politesse entre les requêtes
                return await titre(client, url)
        return await asyncio.gather(*(un(u) for u in urls), return_exceptions=True)


print(asyncio.run(main(["https://example.com", "https://example.org"])))
```

## 13.6 Pages générées par JavaScript

Si le contenu **n'apparaît pas** dans `reponse.text` mais s'affiche dans le navigateur, il est construit par **JavaScript**. Trois solutions, **de la meilleure à la dernière** :

1. **Trouver l'API** : onglet *Réseau* → *Fetch/XHR* des DevTools ; appelez directement l'URL JSON (plus rapide et plus stable).
2. **Données intégrées** : JSON-LD, `__NEXT_DATA__` (voir [9.7](#97-données-structurées-json-ld-et-données-intégrées)).
3. **Navigateur piloté** : **Playwright** (recommandé) ou Selenium, puis Beautiful Soup sur le HTML rendu.

```python
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright           # pip install playwright && playwright install chromium

with sync_playwright() as p:
    navigateur = p.chromium.launch()
    page = navigateur.new_page()
    page.goto("https://quotes.toscrape.com/js/", wait_until="networkidle")      # citations générées par JavaScript
    page.wait_for_selector("div.quote")                    # attendre l'élément voulu
    soup = BeautifulSoup(page.content(), "lxml")
    navigateur.close()

print(len(soup.select("div.quote")))                       # 10
```

## 13.7 Flux de travail type

1. **Inspecter** la page (DevTools) : où sont les données ? statiques, JSON, JavaScript ?
2. **Récupérer** avec `requests` / `httpx` (délais, erreurs, politesse).
3. **Analyser** avec Beautiful Soup (`select`, `find_all`).
4. **Nettoyer et valider** les données (types, valeurs manquantes).
5. **Gérer** pagination, connexion, limites de débit.
6. **Stocker** (CSV, JSON, SQLite, base de données).
7. **Surveiller** : les sites changent, prévoyez des **tests** et des **alertes** quand la structure évolue.

---

# 14. Scraper de façon responsable

*(Section ajoutée.)*

## 14.1 Cadre juridique et éthique

| Point | À vérifier |
| --- | --- |
| **Conditions d'utilisation** | Beaucoup de sites interdisent le scraping automatisé |
| **`robots.txt`** | Indique les zones autorisées aux robots (`https://site/robots.txt`) |
| **Données personnelles (RGPD)** | Collecter des données de personnes exige une **base légale** et de la **transparence** |
| **Droit d'auteur / base de données** | Les contenus et bases de données peuvent être protégés |
| **API officielle** | À préférer à toute extraction |
| **Authentification** | Ne contournez ni connexion, ni CAPTCHA, ni protections techniques |

> Ceci **n'est pas un avis juridique** : en cas de projet commercial ou de données sensibles, consultez un juriste.

## 14.2 Respecter `robots.txt` avec la bibliothèque standard

```python
import sys
from urllib import robotparser

rp = robotparser.RobotFileParser()
rp.set_url("https://quotes.toscrape.com/robots.txt")
rp.read()

agent = "MonRobot"
if rp.can_fetch(agent, "https://quotes.toscrape.com/page/2/"):
    print("Autorisé")
else:
    print("Interdit par robots.txt", file=sys.stderr)

delai = rp.crawl_delay(agent)                               # délai demandé par le site (ou None)
print(delai)
```

## 14.3 Bonnes pratiques de politesse

- **Identifiez** votre robot (User-Agent honnête + moyen de contact).
- **Ralentissez** : une requête **toutes les 1 à 5 secondes**, moins en heures de pointe ; respectez `Crawl-delay` et `Retry-After`.
- **Mettez en cache** et ne redemandez pas la même page.
- Limitez la **concurrence** ; arrêtez-vous en cas de `429` / `503` répétés.
- Ne collectez **que le nécessaire** et conservez-le **de façon sécurisée**.
- Préférez les **heures creuses** pour de gros volumes.

---

# 15. Projet complet : citations avec pagination

*(Section ajoutée : un exemple de bout en bout sur un site conçu pour s'entraîner : [quotes.toscrape.com](https://quotes.toscrape.com).)*

```python
"""Collecte les citations de https://quotes.toscrape.com et les enregistre en JSON et CSV."""
from __future__ import annotations

import csv
import json
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

URL_DEPART = "https://quotes.toscrape.com/"
ENTETES = {"User-Agent": "ExempleScraping/1.0 (apprentissage ; contact@exemple.fr)"}


def telecharger(session: requests.Session, url: str) -> BeautifulSoup:
    reponse = session.get(url, headers=ENTETES, timeout=10)
    reponse.raise_for_status()
    return BeautifulSoup(reponse.content, "lxml")


def extraire_citations(soup: BeautifulSoup) -> list[dict]:
    citations = []
    for bloc in soup.select("div.quote"):                               # un bloc par citation
        texte = bloc.select_one("span.text")
        auteur = bloc.select_one("small.author")
        if texte is None or auteur is None:                              # robustesse si la structure change
            continue
        citations.append({
            "texte": texte.get_text(strip=True),
            "auteur": auteur.get_text(strip=True),
            "tags": [t.get_text(strip=True) for t in bloc.select("div.tags a.tag")],
        })
    return citations


def page_suivante(soup: BeautifulSoup, url_courante: str) -> str | None:
    lien = soup.select_one("li.next > a[href]")
    return urljoin(url_courante, lien["href"]) if lien else None


def main() -> None:
    toutes: list[dict] = []
    url: str | None = URL_DEPART
    with requests.Session() as session:
        while url:
            print(f"→ {url}")
            soup = telecharger(session, url)
            toutes.extend(extraire_citations(soup))
            url = page_suivante(soup, url)
            time.sleep(1)                                                # politesse

    with open("citations.json", "w", encoding="utf-8") as f:
        json.dump(toutes, f, ensure_ascii=False, indent=2)

    with open("citations.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["texte", "auteur", "tags"])
        w.writeheader()
        for c in toutes:
            w.writerow({**c, "tags": ", ".join(c["tags"])})

    print(f"{len(toutes)} citations enregistrées.")


if __name__ == "__main__":
    main()
```

Pistes d'amélioration : journalisation (`logging`), reprise après erreur, base **SQLite**, tests unitaires sur des **pages HTML enregistrées** (sans réseau), DataFrame pandas pour l'analyse.

---

# 16. Performances et optimisation

## 16.1 Choisir le bon parseur

`lxml` est généralement **le plus rapide** ; `html5lib` le plus lent. Mesurez sur **vos** pages (`timeit`).

```python
import timeit

from bs4 import BeautifulSoup

html = "<div>" + "<p>Texte <a href='/x'>lien</a></p>" * 2000 + "</div>"

for p in ("html.parser", "lxml", "html5lib"):
    print(p, timeit.timeit(lambda: BeautifulSoup(html, p), number=5))
```

## 16.2 Ne parser qu'une partie : `SoupStrainer` *(à jour)*

`SoupStrainer` indique à Beautiful Soup de **ne construire que les éléments voulus** : moins de mémoire et de temps. À utiliser via **`parse_only`**.

```python
from bs4 import BeautifulSoup, SoupStrainer

html = """
<a href="/a">A</a><a>sans lien</a>
<div class="produit">Stylo</div><div class="pied">Pied</div>
"""

seulement_liens = SoupStrainer("a", href=True)                    # nom + attributs
soup = BeautifulSoup(html, "lxml", parse_only=seulement_liens)
for lien in soup.find_all("a"):
    print(lien["href"])

seulement_produits = SoupStrainer("div", attrs={"class": "produit"})
soup = BeautifulSoup(html, "lxml", parse_only=seulement_produits)
print(soup.find_all("div"))
```

> **À jour (4.13)** : `SoupStrainer` a été **refondu** autour de la nouvelle classe **`ElementFilter`** (importable depuis `bs4`) ; certaines propriétés (`SoupStrainer.text`, `.string`) sont dépréciées. Les cas d'usage simples ci-dessus **fonctionnent toujours**. Notez aussi :
> - `parse_only` **ne fonctionne pas avec `html5lib`** (qui construit toujours l'arbre complet) ;
> - les valeurs d'attributs sont transmises sous forme de **chaînes brutes** pendant l'analyse initiale (une classe `"a b"` n'est pas encore une liste).

## 16.3 Réduire la consommation mémoire

- Utilisez `SoupStrainer`, ou extrayez **tout de suite** les données puis **supprimez** l'arbre (`soup.decompose()` ; `del soup`).
- Copiez les textes en `str(...)` (une `NavigableString` garde une référence vers tout l'arbre).
- Pour des **fichiers énormes** (centaines de Mo) : **`lxml.etree.iterparse`** (analyse en flux), hors du cadre de Beautiful Soup.
- Préférez `soup.css.iselect()` / `find_all(limit=…)` quand vous ne voulez que les premiers résultats.

## 16.4 Éviter le travail inutile

- **Analysez chaque document une seule fois** ; réutilisez l'objet (ou mettez le résultat en cache).
- Définissez le sélecteur **le plus précis** possible ; évitez `find_all(True)` sur de gros documents.
- Compilez vos expressions régulières (`re.compile`) hors des boucles.
- **Parallélisez** les téléchargements (asynchrone / threads) mais pas forcément l'analyse (liée au processeur : `concurrent.futures.ProcessPoolExecutor` pour beaucoup de pages).

## 16.5 Quand Beautiful Soup ne suffit plus

| Besoin | Solution |
| --- | --- |
| Millions d'éléments, vitesse maximale | **`selectolax`** (moteur Lexbor, très rapide), **`lxml.html`** + XPath |
| Crawl à grande échelle | **Scrapy** |
| Sélecteurs CSS **et** XPath | **`parsel`** |

---

# 17. Sujets avancés : XML, encodages, typage

## 17.1 Travailler avec du XML

```python
from bs4 import BeautifulSoup

xml = """<?xml version="1.0" encoding="UTF-8"?>
<catalogue xmlns:dc="http://purl.org/dc/elements/1.1/">
  <livre id="1"><dc:title>Le Petit Prince</dc:title><prix devise="EUR">9.90</prix></livre>
  <livre id="2"><dc:title>Candide</dc:title><prix devise="EUR">7.50</prix></livre>
</catalogue>"""

soup = BeautifulSoup(xml, "xml")                                  # nécessite lxml ; équivaut à "lxml-xml"
for livre in soup.find_all("livre"):
    print(livre["id"], livre.find("dc:title").text, livre.prix["devise"], livre.prix.text)
```

- Le parseur XML est **sensible à la casse**, **strict** et conserve les **espaces de noms** (`dc:title`).
- Flux **RSS / Atom** : `BeautifulSoup(contenu, "xml")` puis `find_all("item")` / `find_all("entry")`.
- Pour du XML **volumineux ou structuré**, **`lxml.etree`** ou **`xml.etree.ElementTree`** (plus adaptés) ; pour du XML **non fiable**, utilisez **`defusedxml`** (protection contre les attaques XXE / « billion laughs »).

## 17.2 Encodages

Beautiful Soup convertit tout en **Unicode** en interne (`str`) et produit du **UTF-8** par défaut.

```python
from bs4 import BeautifulSoup

octets = "<p>Café</p>".encode("iso-8859-1")

soup = BeautifulSoup(octets, "lxml")
print(soup.original_encoding)                       # encodage détecté (None si on a passé une str)

soup = BeautifulSoup(octets, "lxml", from_encoding="iso-8859-1")      # imposer l'encodage si la détection se trompe
print(soup.p.text)                                  # Café
```

| Source | Bon réflexe |
| --- | --- |
| **`requests`** | Passer **`reponse.content`** (octets). `reponse.text` utilise l'encodage deviné par `requests` (en-tête `Content-Type` ; à défaut, `ISO-8859-1` pour le texte) |
| Forcer l'encodage de `requests` | `reponse.encoding = reponse.apparent_encoding` avant `.text` |
| Fichiers | Ouvrir en `"rb"` (octets) ou avec `encoding="utf-8"` explicite |
| Sorties | Écrire en `utf-8` (`ensure_ascii=False` pour le JSON) |

```python
from bs4 import UnicodeDammit

octets = "Café crème".encode("windows-1252")

dammit = UnicodeDammit(octets, ["utf-8", "windows-1252"])         # détection / conversion à la demande
print(dammit.unicode_markup, dammit.original_encoding)             # Café crème windows-1252
```

> Pour les caractères « bizarres » (mojibake `Ã©`) : mauvais encodage deviné ; essayez `from_encoding=` ou la bibliothèque **`ftfy`**.

## 17.3 Multilingue et Unicode

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup("<p>こんにちは — مرحبا — Привет</p>", "html.parser")
print(soup.p.text)                                  # texte Unicode préservé
```

Assurez-vous que **terminal, éditeur et fichiers de sortie** sont en **UTF-8** (sous Windows : `PYTHONUTF8=1` ou Windows Terminal).

## 17.4 Typage statique *(ajout, 4.13+)*

Depuis la 4.13, Beautiful Soup est **entièrement annoté**. Conséquence : un vérificateur de types (**mypy**, **Pyright**) sait que `find()` renvoie `Tag | NavigableString | None`, ce qui provoque des erreurs « *objet possiblement None* ».

```python
from bs4 import BeautifulSoup, Tag

html = '<h1>Titre</h1><a href="/accueil">Accueil</a>'
soup = BeautifulSoup(html, "lxml")

titre = soup.find("h1")
if isinstance(titre, Tag):                 # restreint le type
    print(titre.get_text(strip=True))

# Pour les sélecteurs CSS : select_one renvoie Tag | None
lien = soup.select_one("a[href]")
if lien is not None:
    href = lien.get("href")                # str | list[str] | None  (attribut potentiellement multi-valeurs)
    if isinstance(href, str):
        print(href)


# Fonction utilitaire
def requis(parent: Tag, selecteur: str) -> Tag:
    el = parent.select_one(selecteur)
    if el is None:
        raise ValueError(f"Élément introuvable : {selecteur}")
    return el


print(requis(soup, "h1").get_text())
```

## 17.5 Autres fonctionnalités avancées

| Fonctionnalité | Description |
| --- | --- |
| **Classes personnalisées** | `BeautifulSoup(..., element_classes={Tag: MaClasse})` |
| **`ElementFilter` (4.13)** | API de **bas niveau** pour filtrer l'arbre : `soup.descendants` + `ElementFilter.filter()` |
| **Copie d'arbre** | `copy.copy(tag)` ou `copy.deepcopy(soup)` |
| **Sérialisation** | `pickle` d'un `BeautifulSoup` (déconseillé : préférez `str(soup)`) |
| **Avertissements** | Activez `warnings.simplefilter("error")` en développement pour voir les dépréciations |
| **Combiner avec lxml / XPath** | `from lxml import etree; etree.HTML(str(soup)).xpath("//a/@href")` |
| **HTML → Markdown / texte** | `markdownify`, `html2text` |

---

# 18. Erreurs courantes et débogage

## 18.1 Erreurs fréquentes

| Symptôme | Cause | Solution |
| --- | --- | --- |
| `AttributeError: 'NoneType' object has no attribute …` | `find()` / `soup.balise` n'a **rien trouvé** | Tester `is None`, vérifier le sélecteur et le parseur, afficher `soup.prettify()` |
| `find_all()` renvoie `[]` | Contenu **chargé par JavaScript**, mauvais sélecteur, mauvaise casse, parseur différent | Comparer avec « Afficher le code source » (pas l'inspecteur !) ; voir [13.6](#136-pages-générées-par-javascript) |
| `KeyError: 'href'` | Attribut absent | `tag.get("href")` ou `select("a[href]")` |
| `.string` vaut `None` | La balise a **plusieurs enfants** | `.get_text()` |
| `.next_sibling` renvoie `'\n'` | Nœud texte entre balises | `find_next_sibling()` |
| `class` n'est pas une chaîne | Attribut multi-valeurs : liste | `" ".join(tag["class"])` ou `multi_valued_attributes=None` |
| `FeatureNotFound: Couldn't find a tree builder…` | Parseur non installé | `pip install lxml` / `html5lib` |
| Textes collés (« BonjourMonde ») | `get_text(strip=True)` sans séparateur | `get_text(" ", strip=True)` |
| Caractères illisibles (`Ã©`) | Mauvais encodage | Passer `reponse.content`, `from_encoding=` |
| Résultats différents selon la machine | Parseur par défaut différent | **Toujours préciser** le parseur |
| `403` / contenu vide | Blocage anti-robots, JavaScript | Voir sections 13 et 14 ; API officielle |

> **« L'inspecteur » n'est pas « le code source »** : les DevTools montrent le DOM **après** JavaScript ; Beautiful Soup reçoit le HTML **brut** du serveur. Comparez avec `view-source:` ou `curl`.

## 18.2 Avertissements fréquents

| Avertissement | Signification |
| --- | --- |
| `GuessedAtParserWarning` | Vous n'avez pas précisé le parseur : ajoutez `"lxml"` |
| `MarkupResemblesLocatorWarning` | Vous avez passé une **URL** ou un **nom de fichier** au lieu du contenu |
| `DeprecationWarning` (`findAll`, `text=`…) | Anciennes API : remplacer (`find_all`, `string=`) |
| `FutureWarning` (`:contains`) | Utiliser `:-soup-contains` |
| `XMLParsedAsHTMLWarning` | Document XML analysé avec un parseur HTML : utiliser `"xml"` |

## 18.3 Diagnostiquer

```python
from bs4 import BeautifulSoup
from bs4.diagnose import diagnose, lxml_trace

html = "<div><p>Paragraphe<p>Autre</div>"
soup = BeautifulSoup(html, "lxml")

diagnose(html)                         # essaie tous les parseurs et affiche les différences
print(soup.prettify()[:2000])          # regarder l'arbre RÉELLEMENT construit
lxml_trace(html)                       # affiche les événements vus par lxml
```

Autres techniques : tester d'abord avec un **petit extrait** enregistré dans un fichier ; comparer `html.parser` / `lxml` / `html5lib` ; afficher `len(soup.find_all(...))` à chaque étape.

## 18.4 Tester son code d'extraction

Enregistrez d'abord une page de référence (une seule fois), puis testez sans réseau. Le module `mon_scraper` est le script de la [section 15](#15-projet-complet--citations-avec-pagination) enregistré sous `mon_scraper.py`.

```bash
mkdir -p tests/pages
curl -o tests/pages/page1.html https://quotes.toscrape.com/
pip install pytest
```

```python
# tests/test_extraction.py (pytest) : sans réseau, sur une page HTML enregistrée
from pathlib import Path
from bs4 import BeautifulSoup
from mon_scraper import extraire_citations

def test_extraire_citations():
    html = Path("tests/pages/page1.html").read_bytes()
    soup = BeautifulSoup(html, "lxml")
    citations = extraire_citations(soup)
    assert len(citations) == 10
    assert citations[0]["auteur"] == "Albert Einstein"
```

---

# 19. Alternatives, aide-mémoire et ressources

## 19.1 Comparaison des outils d'analyse HTML

| Outil | Style | Points forts | Quand l'utiliser |
| --- | --- | --- | --- |
| **Beautiful Soup** | `find`, CSS | Simple, tolérant, très documenté | Apprentissage, scripts, HTML irrégulier |
| **lxml** | XPath, CSS | **Très rapide**, XPath complet | Gros volumes, besoins XPath |
| **parsel** | CSS + XPath | API élégante (utilisée par Scrapy) | Extraction souple |
| **selectolax** | CSS | **Le plus rapide** | Performances critiques |
| **Scrapy** | Framework | Crawl, files, middleware, export | Projets de grande taille |
| **Playwright / Selenium** | Navigateur | JavaScript, interactions | Sites dynamiques |
| **pandas.read_html** | Tableaux | DataFrames directs | Tableaux simples |

## 19.2 Aide-mémoire

| Je veux… | Code |
| --- | --- |
| Créer l'objet | `BeautifulSoup(contenu, "lxml")` |
| Première balise / toutes | `soup.find("a")` · `soup.find_all("a")` |
| Par classe / id / attribut | `find_all("div", class_="x")` · `find(id="y")` · `find_all(attrs={"data-k": "v"})` |
| Sélecteur CSS | `soup.select("div.x > a[href]")` · `soup.select_one("#y")` |
| Attribut | `tag["href"]` · `tag.get("href")` |
| Texte | `tag.get_text(" ", strip=True)` |
| Parent / enfants / frères | `.parent` · `.children` · `find_next_sibling("p")` |
| Rechercher un texte | `find_all(string=re.compile("mot"))` · `select("p:-soup-contains('mot')")` |
| Supprimer | `tag.decompose()` · `tag.extract()` · `tag.unwrap()` |
| Créer / ajouter | `soup.new_tag("p")` · `parent.append(tag)` |
| Afficher joliment | `soup.prettify()` |
| URL absolue | `urljoin(base, tag["href"])` |
| Limiter l'analyse | `BeautifulSoup(html, "lxml", parse_only=SoupStrainer("a"))` |

## 19.3 Les 10 règles d'or du scraping avec Beautiful Soup

1. **Précisez toujours le parseur** (`lxml` de préférence).
2. Passez **`reponse.content`** (octets), pas `reponse.text`.
3. **Testez `None`** après chaque `find()` / `select_one()`.
4. Préférez **`select()`** pour les cas courants et `find_next_sibling()` à `.next_sibling`.
5. Bouclez sur les **blocs conteneurs**, puis extrayez les champs à l'intérieur.
6. Mettez toujours un **`timeout`**, vérifiez **`raise_for_status()`**, utilisez une **`Session`**.
7. **Identifiez votre robot**, respectez **`robots.txt`**, **ralentissez** et **mettez en cache**.
8. Cherchez d'abord une **API / JSON** avant de scraper le HTML.
9. **Séparez** le téléchargement de l'extraction et testez l'extraction sur des **pages enregistrées**.
10. Anticipez le **changement de structure** des sites : tests, journaux, alertes.

## 19.4 Ressources

- **Documentation officielle (traduite en plusieurs langues)** : <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>
- **Soup Sieve** (sélecteurs CSS) : <https://facelessuser.github.io/soupsieve/>
- **lxml** : <https://lxml.de> · **Playwright** : <https://playwright.dev/python/> · **Scrapy** : <https://scrapy.org>
- **Sites d'entraînement** : <https://quotes.toscrape.com> · <https://books.toscrape.com>
- **robots.txt** : <https://www.robotstxt.org>

---

<div align="center">

*Bon scraping, et soyez courtois avec les serveurs !*

</div>
