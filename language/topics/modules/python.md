# 🐍 Python : les modules essentiels de la bibliothèque standard

> Aide-mémoire illustré avec des exemples prêts à copier. Les exemples ciblent **Python 3.11+** ; lorsqu'une fonctionnalité demande une version plus récente, c'est indiqué.

## 📑 Sommaire

1. [Expressions régulières (`re`)](#1-expressions-régulières-re)
2. [Le module `os`](#2-le-module-os)
3. [`pathlib` : chemins orientés objet](#3-pathlib--chemins-orientés-objet)
4. [Dates et heures (`datetime`)](#4-dates-et-heures-datetime)
5. [Le module `json`](#5-le-module-json)
6. [Gestionnaires de contexte (`with`)](#6-gestionnaires-de-contexte-with)
7. [Comprendre et utiliser les API](#7-comprendre-et-utiliser-les-api)
8. [Programmation asynchrone (`asyncio`)](#8-programmation-asynchrone-asyncio)
9. [Aide-mémoire final](#9-aide-mémoire-final)

---

## 1. Expressions régulières (`re`)

### Qu'est-ce qu'une expression régulière ?

Une **expression régulière** (*RegEx*) est une suite de caractères qui décrit un **motif de recherche**. Elle sert à chercher, valider, extraire ou remplacer du texte. En Python, tout passe par le module standard `re`.

```python
import re
```

### Fonctions principales

| Fonction            | Description                                                        |
| ------------------- | ------------------------------------------------------------------ |
| `re.match()`        | Cherche le motif **au début** de la chaîne                         |
| `re.search()`       | Cherche le motif **n'importe où** dans la chaîne (première trouvaille) |
| `re.fullmatch()`    | Le motif doit correspondre à **toute** la chaîne                   |
| `re.findall()`      | Retourne la liste de toutes les correspondances sans chevauchement |
| `re.finditer()`     | Retourne un itérateur d'objets *Match*                             |
| `re.sub()`          | Remplace les correspondances                                       |
| `re.split()`        | Découpe la chaîne selon le motif                                   |
| `re.compile()`      | Précompile un motif pour le réutiliser                             |
| `re.escape()`       | Échappe tous les caractères spéciaux d'un texte littéral           |

```python
import re

re.match(r"abc", "abcdef")    # <re.Match object; span=(0, 3), match='abc'>
re.match(r"def", "abcdef")    # None : "def" n'est pas au début
re.search(r"def", "abcdef")   # <re.Match object; span=(3, 6), match='def'>
re.fullmatch(r"abc", "abcdef")  # None : la chaîne entière ne correspond pas
```

### Syntaxe de base

> 💡 Utilisez toujours des **chaînes brutes** (`r"..."`) : le backslash s'écrit alors une seule fois (`\d`, et non `\\d`).

| Symbole         | Description                                            |
| --------------- | ------------------------------------------------------ |
| `.`             | N'importe quel caractère sauf le retour à la ligne     |
| `^`             | Début de la chaîne                                     |
| `$`             | Fin de la chaîne                                       |
| `*`             | 0 répétition ou plus                                   |
| `+`             | 1 répétition ou plus                                   |
| `?`             | 0 ou 1 répétition                                      |
| `{n}`           | Exactement *n* répétitions                             |
| `{n,m}`         | Entre *n* et *m* répétitions                           |
| `[abc]`         | Classe de caractères (un caractère parmi a, b ou c)    |
| `[^abc]`        | Classe **négative** (tout sauf a, b ou c)              |
| `a\|b`          | Alternative : « a » **ou** « b »                       |
| `(...)`         | Groupe capturant                                       |
| `(?:...)`       | Groupe **non** capturant                               |
| `(?P<nom>...)`  | Groupe nommé                                           |
| `\b`            | Frontière de mot                                       |
| `\`             | Échappe un caractère spécial (`\.` pour un vrai point) |
| `*?`, `+?`, `??`| Versions **paresseuses** (non gourmandes)              |

```python
re.search(r"^a", "abc")    # Correspond : "a" est au début
re.search(r"c$", "abc")    # Correspond : "c" est à la fin
re.search(r"a$", "abc")    # None : "a" n'est pas à la fin
```

### Classes de caractères prédéfinies

| Classe | Description                                  |
| ------ | -------------------------------------------- |
| `\d`   | Chiffre (`[0-9]`)                            |
| `\D`   | Tout sauf un chiffre                         |
| `\w`   | Caractère de mot (lettres, chiffres, `_`)    |
| `\W`   | Tout sauf un caractère de mot                |
| `\s`   | Espace blanc (espace, tabulation, saut de ligne…) |
| `\S`   | Tout sauf un espace blanc                    |

> ℹ️ Sur une chaîne `str`, `\d` et `\w` sont compatibles **Unicode** (ils reconnaissent aussi « é » ou les chiffres d'autres alphabets). Ajoutez `re.ASCII` pour restreindre à l'ASCII.

```python
re.findall(r"\d", "abc123def")   # ['1', '2', '3']
re.findall(r"\w", "abc 123")     # ['a', 'b', 'c', '1', '2', '3']
```

### Gourmand ou paresseux ?

Par défaut, les quantificateurs sont **gourmands** : ils capturent le plus possible.

```python
texte = "<a><b>"
re.findall(r"<.+>", texte)    # ['<a><b>']      (gourmand)
re.findall(r"<.+?>", texte)   # ['<a>', '<b>']  (paresseux)
```

### Drapeaux (*flags*)

Les drapeaux modifient le comportement de la recherche. On les combine avec `|`.

| Drapeau         | Abréviation | Effet                                                  |
| --------------- | ----------- | ------------------------------------------------------ |
| `re.IGNORECASE` | `re.I`      | Insensible à la casse                                  |
| `re.MULTILINE`  | `re.M`      | `^` et `$` s'appliquent à chaque ligne                 |
| `re.DOTALL`     | `re.S`      | `.` correspond aussi au retour à la ligne              |
| `re.VERBOSE`    | `re.X`      | Autorise espaces et commentaires dans le motif         |
| `re.ASCII`      | `re.A`      | `\w`, `\d`, `\s`… limités à l'ASCII                    |

```python
re.search(r"bonjour", "Bonjour", re.IGNORECASE)   # Correspond quelle que soit la casse
re.findall(r"^\w+", "un\ndeux", re.MULTILINE)     # ['un', 'deux']
```

### Exemples utiles

**Trouver tous les nombres d'une chaîne**

```python
re.findall(r"\d+", "abc123def456")   # ['123', '456']
```

**Extraire les composantes d'une date**

```python
date_str = "2025-05-01"
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", date_str)
if m:
    annee, mois, jour = m.groups()
    print(f"Année : {annee}, mois : {mois}, jour : {jour}")
```

**Utiliser des groupes nommés (plus lisible)**

```python
m = re.search(r"(?P<annee>\d{4})-(?P<mois>\d{2})-(?P<jour>\d{2})", "2025-05-01")
if m:
    print(m["annee"], m.group("mois"), m.groupdict())
    # 2025 05 {'annee': '2025', 'mois': '05', 'jour': '01'}
```

**Valider une adresse e-mail (version simple)**

```python
motif_email = r"[\w.-]+@[\w.-]+\.\w{2,}"
est_valide = re.fullmatch(motif_email, "user@example.com") is not None
print(est_valide)   # True
```

> ⚠️ Ce motif convient pour un contrôle rapide, mais il ne couvre pas toute la norme des adresses e-mail. Pour une validation stricte, envoyez un message de confirmation.

**Remplacer du texte**

```python
re.sub(r"cat", "dog", "one cat, two cats")
# 'one dog, two dogs'

# Avec des références arrière : AAAA-MM-JJ → JJ/MM/AAAA
re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1", "2025-05-01")
# '01/05/2025'

# Avec une fonction de remplacement
re.sub(r"\d+", lambda m: str(int(m.group()) * 2), "3 pommes, 5 poires")
# '6 pommes, 10 poires'
```

**Découper une chaîne**

```python
re.split(r"[,;]\s*", "a, b;c,  d")   # ['a', 'b', 'c', 'd']
```

### L'objet *Match*

Un objet *Match* est retourné lorsqu'un motif correspond (sinon, la fonction renvoie `None`). Il contient la position, le texte trouvé et les groupes capturés.

| Méthode                 | Rôle                                           |
| ----------------------- | ---------------------------------------------- |
| `.group()` / `.group(n)`| Correspondance complète ou groupe numéro *n*   |
| `.groups()`             | Tous les groupes, sous forme de tuple          |
| `.groupdict()`          | Les groupes nommés, sous forme de dictionnaire |
| `.start()`, `.end()`    | Positions de début et de fin                   |
| `.span()`               | Tuple `(début, fin)`                           |

```python
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", "Date : 2025-05-01")
if m:
    print(m.group())    # '2025-05-01'
    print(m.group(1))   # '2025'
    print(m.groups())   # ('2025', '05', '01')
    print(m.span())     # (7, 17)
```

### Précompiler un motif

Quand un motif est utilisé plusieurs fois, compilez-le une seule fois :

```python
motif = re.compile(r"\d+")
motif.findall("a1 b22 c333")   # ['1', '22', '333']
motif.sub("#", "a1 b22")       # 'a# b#'
```

### Motifs complexes avec `re.VERBOSE`

```python
motif_tel = re.compile(r"""
    ^(?:\+33|0)      # indicatif : +33 ou 0
    \s?[1-9]         # premier chiffre (1 à 9)
    (?:[\s.-]?\d{2}){4}   # quatre paires de chiffres
    $
""", re.VERBOSE)

motif_tel.match("06 12 34 56 78")   # Correspond
```

### ✅ Bonnes pratiques

- **Chaînes brutes** (`r"..."`) : évitent que Python interprète les backslashes.
- **`re.compile()`** : pour tout motif réutilisé plusieurs fois.
- **`re.escape()`** : pour insérer du texte saisi par l'utilisateur dans un motif.
- **`re.VERBOSE`** : pour rendre lisibles les motifs complexes (avec commentaires).
- **Tester les cas limites** : chaîne vide, caractères spéciaux, accents, très longs textes.
- **Éviter les motifs imbriqués trop gourmands** (ex. `(a+)+`) qui peuvent provoquer un ralentissement catastrophique (*ReDoS*) sur des entrées malveillantes.
- **Ne pas tout résoudre par une regex** : pour du HTML ou du JSON, préférez un véritable analyseur.

---

## 2. Le module `os`

### Qu'est-ce que `os` ?

Le module `os` donne accès aux fonctionnalités **dépendantes du système d'exploitation** : système de fichiers, variables d'environnement, processus, etc.

```python
import os
```

> 💡 Pour manipuler des chemins et des fichiers au quotidien, `pathlib` (section 3) est aujourd'hui l'approche recommandée. `os` reste utile pour les variables d'environnement, les processus et le code existant.

### 2.1 Travailler avec le système de fichiers

**Répertoire de travail**

```python
print(os.getcwd())   # ex. : /home/utilisateur/projet
os.chdir("/tmp")     # Change de répertoire
print(os.getcwd())   # /tmp
```

> 💡 Pour un changement **temporaire** de répertoire, utilisez `contextlib.chdir()` (Python 3.11+, voir [section 6](#6-gestionnaires-de-contexte-with)).

**Lister le contenu d'un dossier**

```python
print(os.listdir())          # Dossier courant
print(os.listdir("/etc"))    # Contenu de /etc

# Plus efficace : scandir() donne directement les infos de chaque entrée
with os.scandir(".") as entrees:
    for e in entrees:
        print(e.name, "(dossier)" if e.is_dir() else "(fichier)")
```

**Créer et supprimer des dossiers**

```python
os.mkdir("dossier_test")                    # Un seul dossier
os.makedirs("dir/subdir", exist_ok=True)    # Dossiers imbriqués, sans erreur s'ils existent

os.rmdir("dossier_test")      # Supprime un dossier VIDE
os.removedirs("dir/subdir")   # Supprime les dossiers vides imbriqués
```

> ⚠️ Pour supprimer un dossier **non vide**, utilisez `shutil.rmtree("dossier")` (irréversible).

**Créer, renommer et supprimer des fichiers**

```python
# Créer un fichier
with open("fichier.txt", "w", encoding="utf-8") as f:
    f.write("Bonjour")

os.rename("fichier.txt", "renomme.txt")   # Renommer
os.remove("renomme.txt")                  # Supprimer
```

> ℹ️ `os.replace(src, dst)` renomme en **écrasant** la destination de façon fiable sur tous les systèmes. Pour copier ou déplacer entre disques, utilisez `shutil.copy()` et `shutil.move()`.

### 2.2 Informations sur les fichiers et les chemins

**Chemins absolus et relatifs**

```python
print(os.path.abspath("fichier.txt"))   # Chemin absolu
print(os.path.relpath("/etc/passwd"))   # Chemin relatif au répertoire courant
```

**Tests d'existence**

```python
print(os.path.exists("fichier.txt"))   # Existe ?
print(os.path.isfile("fichier.txt"))   # Est un fichier ?
print(os.path.isdir("mon_dossier"))    # Est un dossier ?
```

**Assembler et découper des chemins**

```python
chemin = os.path.join("dossier", "sous_dossier", "fichier.txt")
print(chemin)   # dossier/sous_dossier/fichier.txt (ou avec \ sous Windows)

tete, queue = os.path.split(chemin)
print(tete, queue)   # dossier/sous_dossier  fichier.txt

nom, extension = os.path.splitext("rapport.pdf")
print(nom, extension)   # rapport  .pdf
```

**Métadonnées**

```python
from datetime import datetime

infos = os.stat("fichier.txt")
print("Taille :", infos.st_size, "octets")
print("Dernière modification :", datetime.fromtimestamp(infos.st_mtime))
```

### 2.3 Variables d'environnement

```python
print(os.environ["HOME"])        # KeyError si la variable n'existe pas
print(os.environ.get("PATH"))    # Plus sûr : renvoie None si absente
print(os.getenv("MA_VAR", "valeur par défaut"))   # Avec valeur par défaut
```

**Définir et supprimer**

```python
os.environ["MA_VAR"] = "valeur"
print(os.environ["MA_VAR"])

del os.environ["MA_VAR"]
```

> 🔐 Les variables d'environnement sont l'endroit idéal pour stocker des **secrets** (clés d'API, mots de passe) plutôt que de les écrire en dur dans le code. Les modifications faites via `os.environ` ne durent que le temps du programme et de ses sous-processus.

### 2.4 Exécuter des commandes système

```python
os.system("echo Bonjour depuis le shell")
```

> ⚠️ **Attention** : `os.system` est à éviter, notamment avec des données venant d'un utilisateur (risque d'injection de commandes). Préférez le module `subprocess` :

```python
import subprocess

resultat = subprocess.run(
    ["echo", "Bonjour"],   # Liste d'arguments, sans passer par le shell
    capture_output=True,
    text=True,
    check=True,            # Lève une exception si la commande échoue
)
print(resultat.stdout)
```

### 2.5 Constantes et informations système

```python
print(os.name)         # 'posix' (Linux/macOS) ou 'nt' (Windows)
print(os.sep)          # '/' sous Unix, '\\' sous Windows
print(os.linesep)      # '\n' sous Unix, '\r\n' sous Windows
print(os.cpu_count())  # Nombre de processeurs logiques
print(os.getpid())     # Identifiant du processus courant
```

### 2.6 Parcourir une arborescence

```python
for dirpath, dirnames, filenames in os.walk("."):
    print(f"Dossier : {dirpath}")
    for fichier in filenames:
        print(f"  Fichier : {fichier}")
```

> Pratique pour analyser un dossier de manière **récursive**.

### 2.7 Permissions et droits d'accès

```python
os.chmod("fichier.txt", 0o644)   # rw-r--r-- (Unix)

print(os.access("fichier.txt", os.R_OK))   # Lisible ?
print(os.access("fichier.txt", os.W_OK))   # Modifiable ?
```

---

## 3. `pathlib` : chemins orientés objet

### Qu'est-ce que `pathlib` ?

`pathlib` est une bibliothèque **orientée objet** pour manipuler les chemins du système de fichiers. Elle est aujourd'hui l'approche **recommandée** et remplace avantageusement la plupart des usages de `os.path`.

> Introduit dans Python 3.4. Depuis Python 3.6, `Path` est accepté partout où une fonction attend un chemin (`open()`, `os`, `shutil`…).

```python
from pathlib import Path
```

### 3.1 Créer des objets `Path`

```python
p = Path("exemple.txt")               # Chemin relatif
maison = Path.home()                  # Dossier personnel
absolu = Path("/usr/bin/python")      # Chemin absolu
courant = Path.cwd()                  # Répertoire de travail
```

### 3.2 Tester l'existence

```python
p = Path("exemple.txt")

print(p.exists())    # Le fichier ou dossier existe ?
print(p.is_file())   # C'est un fichier ?
print(p.is_dir())    # C'est un dossier ?
```

### 3.3 Lire et écrire des fichiers

```python
p = Path("data.txt")

p.write_text("Bonjour le monde !", encoding="utf-8")   # Écrire
print(p.read_text(encoding="utf-8"))                   # Lire
```

> 💡 Indiquez toujours `encoding="utf-8"` : le comportement par défaut dépend du système. Pour du contenu binaire, utilisez `write_bytes()` et `read_bytes()`. Pour de gros fichiers, utilisez `with p.open() as f:`.

### 3.4 Créer des dossiers et des fichiers

```python
Path("mon_dossier").mkdir(exist_ok=True)

# Dossiers imbriqués
Path("parent/enfant/petit_enfant").mkdir(parents=True, exist_ok=True)

# Créer un fichier vide (ou mettre à jour sa date de modification)
Path("vide.txt").touch()
```

### 3.5 Renommer et supprimer

```python
p = Path("ancien_nom.txt")
p = p.rename("nouveau_nom.txt")   # Retourne le nouveau Path

p.unlink()                        # Supprime le fichier
p.unlink(missing_ok=True)         # Sans erreur s'il n'existe déjà plus (3.8+)
```

> ⚠️ `.rmdir()` ne supprime que les dossiers **vides**. Pour un dossier non vide : `shutil.rmtree()`.

### 3.6 Parcourir les dossiers

```python
# Contenu direct d'un dossier
for element in Path(".").iterdir():
    print(element)

# Filtrer avec un motif
for fichier in Path(".").glob("*.py"):
    print(fichier)

# Récursivement
for fichier in Path(".").rglob("*.txt"):
    print(fichier)
```

> 💡 Depuis Python 3.12, `Path.walk()` offre le même comportement que `os.walk()` en version objet.

### 3.7 Décomposer un chemin

```python
p = Path("/usr/local/bin/script.py")

print(p.name)      # 'script.py'
print(p.stem)      # 'script'
print(p.suffix)    # '.py'
print(p.parent)    # /usr/local/bin
print(p.parts)     # ('/', 'usr', 'local', 'bin', 'script.py')

# Modifier une partie
print(p.with_suffix(".txt"))       # /usr/local/bin/script.txt
print(p.with_name("autre.py"))     # /usr/local/bin/autre.py
```

### 3.8 Assembler des chemins avec `/`

```python
p = Path("dossier")
nouveau = p / "sous_dossier" / "fichier.txt"
print(nouveau)   # dossier/sous_dossier/fichier.txt
```

### 3.9 Métadonnées et permissions

```python
p = Path("fichier.txt")

print(p.stat().st_size)    # Taille en octets
print(p.stat().st_mtime)   # Date de dernière modification (timestamp)

p.chmod(0o644)             # rw-r--r-- (Unix)
```

### 3.10 Chemins absolus et relatifs

```python
p = Path("fichier.txt")

print(p.resolve())                        # Chemin absolu (résout aussi les liens symboliques)
print(p.resolve().relative_to(Path.cwd()))  # Chemin relatif au répertoire courant
```

### 3.11 Correspondance `os` / `pathlib`

| Tâche                      | `os` / `os.path`                    | `pathlib`                        |
| -------------------------- | ----------------------------------- | -------------------------------- |
| Répertoire courant         | `os.getcwd()`                       | `Path.cwd()`                     |
| Dossier personnel          | `os.path.expanduser("~")`           | `Path.home()`                    |
| Assembler des chemins      | `os.path.join(a, b)`                | `Path(a) / b`                    |
| Existe ?                   | `os.path.exists(p)`                 | `p.exists()`                     |
| Est un fichier ?           | `os.path.isfile(p)`                 | `p.is_file()`                    |
| Nom du fichier             | `os.path.basename(p)`               | `p.name`                         |
| Dossier parent             | `os.path.dirname(p)`                | `p.parent`                       |
| Extension                  | `os.path.splitext(p)[1]`            | `p.suffix`                       |
| Chemin absolu              | `os.path.abspath(p)`                | `p.resolve()`                    |
| Lister un dossier          | `os.listdir(p)`                     | `p.iterdir()`                    |
| Créer des dossiers         | `os.makedirs(p, exist_ok=True)`     | `p.mkdir(parents=True, exist_ok=True)` |
| Supprimer un fichier       | `os.remove(p)`                      | `p.unlink()`                     |
| Parcours récursif          | `os.walk(p)`                        | `p.rglob("*")` ou `p.walk()`     |

### Avantages par rapport à `os.path`

- Syntaxe plus claire, **orientée objet**
- Compatible multiplateforme (gère `/` et `\` automatiquement)
- Plus lisible, grâce à l'opérateur `/`
- Lecture et écriture de fichiers intégrées (`read_text`, `write_text`)

---

## 4. Dates et heures (`datetime`)

Le module `datetime` fournit des classes pour manipuler les dates, les heures et les durées.

### Classes principales

| Classe      | Description                              |
| ----------- | ---------------------------------------- |
| `date`      | Année, mois, jour                        |
| `time`      | Heure, minute, seconde, microseconde     |
| `datetime`  | Combine `date` et `time`                 |
| `timedelta` | Représente une **durée** (une différence) |
| `timezone`  | Gère les décalages horaires fixes (UTC±n) |

### Dates

```python
from datetime import date

aujourdhui = date.today()      # Date du jour
d = date(2025, 5, 1)           # Date précise

print(d.year, d.month, d.day)  # 2025 5 1
print(d.weekday())             # 3 → jeudi (0 = lundi, 6 = dimanche)
```

### Heures

```python
from datetime import time

t = time(14, 30, 45)
print(t.hour, t.minute, t.second)   # 14 30 45
```

### Dates et heures combinées

```python
from datetime import datetime

maintenant = datetime.now()          # Date et heure locales actuelles
dt = datetime(2025, 5, 1, 14, 30)    # Date et heure précises

print(maintenant.year, maintenant.hour, maintenant.minute)
```

### Formater en texte avec `strftime()`

```python
maintenant = datetime.now()
texte = maintenant.strftime("%d/%m/%Y %H:%M:%S")   # ex. : 01/05/2025 14:30:45
```

| Code | Signification              | Exemple  |
| ---- | -------------------------- | -------- |
| `%Y` | Année (4 chiffres)         | 2025     |
| `%y` | Année (2 chiffres)         | 25       |
| `%m` | Mois (01–12)               | 05       |
| `%d` | Jour (01–31)               | 01       |
| `%H` | Heure, format 24 h (00–23) | 14       |
| `%M` | Minute (00–59)             | 30       |
| `%S` | Seconde (00–59)            | 45       |
| `%A` | Nom du jour                | Thursday |
| `%B` | Nom du mois                | May      |

> ℹ️ `%A` et `%B` dépendent de la **locale** du système (langue). Pour du texte localisé de façon fiable, utilisez une bibliothèque comme `Babel`.

### Convertir du texte en date avec `strptime()`

```python
dt = datetime.strptime("2025-05-01 14:30", "%Y-%m-%d %H:%M")
```

### Format ISO 8601 (recommandé pour échanger des dates)

```python
dt = datetime(2025, 5, 1, 14, 30)

print(dt.isoformat())                              # '2025-05-01T14:30:00'
print(datetime.fromisoformat("2025-05-01T14:30"))  # 2025-05-01 14:30:00
```

### Calculs avec `timedelta`

```python
from datetime import datetime, timedelta

dans_une_semaine = datetime.now() + timedelta(days=7)
il_y_a_une_heure = datetime.now() - timedelta(hours=1)

# Durée entre deux dates
delta = datetime(2025, 5, 1) - datetime(2024, 5, 1)
print(delta.days)              # 365
print(delta.total_seconds())   # 31536000.0
```

### Fuseaux horaires

Il existe deux sortes de `datetime` :

- **naïf** : sans information de fuseau (`datetime.now()`) ;
- **averti** (*aware*) : avec un fuseau horaire (`tzinfo`).

> ⚠️ On ne peut pas comparer ou soustraire un `datetime` naïf et un `datetime` averti (`TypeError`).

**Décalage fixe avec `timezone`**

```python
from datetime import datetime, timedelta, timezone

tz = timezone(timedelta(hours=3))   # UTC+3
dt = datetime(2025, 5, 1, 14, 0, tzinfo=tz)
print(dt.isoformat())               # 2025-05-01T14:00:00+03:00
```

**Heure UTC actuelle**

```python
maintenant_utc = datetime.now(timezone.utc)
```

> ⚠️ `datetime.utcnow()` et `datetime.utcfromtimestamp()` sont **dépréciés depuis Python 3.12** : ils renvoient un datetime *naïf* source d'erreurs. Utilisez `datetime.now(timezone.utc)`.

**Fuseaux nommés avec `zoneinfo` (Python 3.9+)**

Le module `zoneinfo` gère les vrais fuseaux (heure d'été comprise).

```python
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

paris = datetime(2025, 7, 1, 12, 0, tzinfo=ZoneInfo("Europe/Paris"))
print(paris.isoformat())                              # 2025-07-01T12:00:00+02:00
print(paris.astimezone(ZoneInfo("Indian/Antananarivo")))  # 2025-07-01 13:00:00+03:00
print(paris.astimezone(timezone.utc))                 # 2025-07-01 10:00:00+00:00
```

> 💡 Sous Windows, installez le paquet `tzdata` (`pip install tzdata`) si les fuseaux sont introuvables.

---

## 5. Le module `json`

Le module `json` permet de travailler avec des données **JSON** (*JavaScript Object Notation*), un format très utilisé pour les API, les fichiers de configuration et l'échange de données.

```python
import json
```

### Vue d'ensemble

| Fonction        | Direction                  | Source / destination |
| --------------- | -------------------------- | -------------------- |
| `json.dumps()`  | Python → JSON              | **chaîne** (*string*) |
| `json.dump()`   | Python → JSON              | **fichier**          |
| `json.loads()`  | JSON → Python              | **chaîne**           |
| `json.load()`   | JSON → Python              | **fichier**          |

> 💡 Mnémotechnique : le **`s`** de `dumps`/`loads` signifie *string*.

### Python → chaîne JSON (`json.dumps`)

```python
data = {
    "name": "Alice",
    "age": 30,
    "is_admin": False,
    "skills": ["Python", "Machine Learning"],
}

json_string = json.dumps(data)
print(json_string)
```

**Résultat** (sur une seule ligne) :

```json
{"name": "Alice", "age": 30, "is_admin": false, "skills": ["Python", "Machine Learning"]}
```

### Écrire dans un fichier (`json.dump`)

```python
with open("user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
```

### Lire depuis une chaîne (`json.loads`)

```python
json_data = '{"name": "Bob", "age": 25}'
python_obj = json.loads(json_data)
print(python_obj["name"])   # Bob
```

### Lire depuis un fichier (`json.load`)

```python
with open("user.json", encoding="utf-8") as f:
    user = json.load(f)
    print(user["skills"])
```

### Affichage lisible et options utiles

```python
print(json.dumps(data, indent=4))
```

```json
{
    "name": "Alice",
    "age": 30,
    "is_admin": false,
    "skills": [
        "Python",
        "Machine Learning"
    ]
}
```

| Option                 | Effet                                                              |
| ---------------------- | ------------------------------------------------------------------ |
| `indent=4`             | Indente le résultat pour le rendre lisible                         |
| `sort_keys=True`       | Trie les clés par ordre alphabétique                               |
| `ensure_ascii=False`   | Conserve les caractères accentués (`é`) au lieu de `\u00e9`        |
| `separators=(",", ":")`| JSON compact, sans espaces                                         |
| `default=fonction`     | Fonction appelée pour les objets non sérialisables                 |

### Correspondance des types Python ↔ JSON

| Type Python        | Type JSON       |
| ------------------ | --------------- |
| `dict`             | objet (*object*) |
| `list`, `tuple`    | tableau (*array*) |
| `str`              | chaîne (*string*) |
| `int`, `float`     | nombre (*number*) |
| `True` / `False`   | `true` / `false` |
| `None`             | `null`          |

> ⚠️ Les clés d'un objet JSON sont toujours des **chaînes** : `{1: "a"}` devient `{"1": "a"}`. De même, un `tuple` revient sous forme de `list` après un aller-retour.

### Erreurs courantes

- **`TypeError: Object of type X is not JSON serializable`** → certains objets (`datetime`, `set`, classes personnalisées…) nécessitent un traitement spécial (voir ci-dessous).
- **`json.JSONDecodeError`** → le texte n'est pas du JSON valide (virgule en trop, apostrophes au lieu de guillemets doubles…).

```python
try:
    json.loads("{'name': 'Bob'}")   # Invalide : il faut des guillemets doubles
except json.JSONDecodeError as e:
    print(f"JSON invalide : {e}")
```

### Sérialisation personnalisée

```python
import json
from datetime import datetime

def serialiseur(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, set):
        return sorted(obj)
    raise TypeError(f"Type non sérialisable : {type(obj).__name__}")

data = {"cree_le": datetime.now(), "tags": {"python", "json"}}
print(json.dumps(data, default=serialiseur, indent=2))
```

---

## 6. Gestionnaires de contexte (`with`)

Un **gestionnaire de contexte** garantit qu'une ressource (fichier, connexion, verrou…) est **correctement libérée**, même si une erreur survient. On l'utilise avec l'instruction `with`.

```python
# Le fichier est fermé automatiquement à la sortie du bloc, erreur ou non
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Bonjour")
```

Équivalent (plus lourd) sans `with` :

```python
f = open("notes.txt", "w", encoding="utf-8")
try:
    f.write("Bonjour")
finally:
    f.close()
```

### Gestionnaires de contexte prêts à l'emploi

```python
import contextlib
import os
import tempfile

# Plusieurs ressources dans un seul with
with open("source.txt", encoding="utf-8") as src, open("copie.txt", "w", encoding="utf-8") as dst:
    dst.write(src.read())

# Dossier temporaire supprimé automatiquement
with tempfile.TemporaryDirectory() as dossier:
    print("Dossier temporaire :", dossier)

# Changer temporairement de répertoire (Python 3.11+)
with contextlib.chdir("/tmp"):
    print(os.getcwd())   # /tmp
print(os.getcwd())       # Retour au répertoire d'origine

# Ignorer une exception précise
with contextlib.suppress(FileNotFoundError):
    os.remove("fichier_inexistant.txt")
```

### Créer le sien avec `@contextmanager`

```python
import time
from contextlib import contextmanager

@contextmanager
def chronometre(nom):
    debut = time.perf_counter()
    try:
        yield                       # Le code du bloc `with` s'exécute ici
    finally:
        duree = time.perf_counter() - debut
        print(f"{nom} : {duree:.3f} s")

with chronometre("Calcul"):
    sum(range(10_000_000))
```

### Créer le sien avec une classe

```python
class Connexion:
    def __enter__(self):
        print("Ouverture")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Fermeture")
        return False   # False : l'exception éventuelle n'est pas masquée

with Connexion() as c:
    print("Travail en cours")
```

### Contextes asynchrones

Pour les ressources asynchrones (sessions réseau, bases de données), on utilise `async with` (voir [section 8](#8-programmation-asynchrone-asyncio)) :

```python
async with aiohttp.ClientSession() as session:
    ...
```

> ✅ **Règle d'or** : dès qu'une ressource doit être fermée (fichier, session HTTP, connexion, verrou), utilisez `with`.

---

## 7. Comprendre et utiliser les API

### Qu'est-ce qu'une API ?

**API** signifie *Application Programming Interface* (interface de programmation). Elle permet à deux programmes ou systèmes de **communiquer** entre eux.

> **Exemple** : une API météo permet à votre script Python de récupérer la température actuelle de votre ville depuis un serveur sur Internet.

### 7.1 Consommer une API avec `requests`

`requests` est la bibliothèque **tierce** la plus répandue pour faire des requêtes HTTP (elle ne fait *pas* partie de la bibliothèque standard).

```bash
pip install requests
```

**Requête GET**

```python
import requests

reponse = requests.get("https://api.github.com/users/octocat", timeout=10)
reponse.raise_for_status()   # Lève une exception si le code est 4xx ou 5xx
data = reponse.json()

print("Nom :", data["name"])
print("Dépôts publics :", data["public_repos"])
```

> ⏱ Précisez toujours un **`timeout`** : sans lui, `requests` peut attendre indéfiniment.

**Paramètres d'URL**

```python
reponse = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "python", "per_page": 3},   # → ?q=python&per_page=3
    timeout=10,
)
```

**Requête POST (envoi de JSON)**

```python
url = "https://httpbin.org/post"
payload = {"username": "alice", "message": "Bonjour"}

reponse = requests.post(url, json=payload, timeout=10)
print(reponse.json())
```

**En-têtes (ex. authentification)**

```python
import os

cle_api = os.environ["API_KEY"]   # Ne jamais écrire une clé en dur dans le code !
headers = {"Authorization": f"Bearer {cle_api}"}

reponse = requests.get("https://api.example.com/data", headers=headers, timeout=10)
```

**Gérer les erreurs proprement**

```python
try:
    reponse = requests.get("https://api.example.com/data", timeout=10)
    reponse.raise_for_status()
    print(reponse.json())
except requests.exceptions.HTTPError as e:
    print("Erreur HTTP :", e.response.status_code)
except requests.exceptions.Timeout:
    print("Délai dépassé")
except requests.exceptions.RequestException as e:
    print("Erreur réseau :", e)
```

**Réutiliser la connexion avec une `Session`**

Pour plusieurs requêtes vers le même serveur, une `Session` (gestionnaire de contexte) est plus rapide et permet de partager les en-têtes.

```python
with requests.Session() as session:
    session.headers.update({"Accept": "application/json"})
    for utilisateur in ("octocat", "torvalds"):
        r = session.get(f"https://api.github.com/users/{utilisateur}", timeout=10)
        print(r.json()["login"])
```

### 7.2 Créer une API simple avec Flask

```bash
pip install flask
```

**Exemple : une API REST minimale**

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Données d'exemple
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
]

# GET : tous les utilisateurs
@app.get("/users")
def get_users():
    return jsonify(users)

# GET : un utilisateur par son identifiant
@app.get("/users/<int:user_id>")
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user is None:
        return jsonify({"erreur": "Utilisateur introuvable"}), 404
    return jsonify(user)

# POST : créer un utilisateur
@app.post("/users")
def add_user():
    donnees = request.get_json(silent=True)
    if not donnees or "name" not in donnees:
        return jsonify({"erreur": "Le champ 'name' est requis"}), 400

    nouvel_id = max((u["id"] for u in users), default=0) + 1
    nouvel_utilisateur = {"id": nouvel_id, "name": donnees["name"]}
    users.append(nouvel_utilisateur)
    return jsonify(nouvel_utilisateur), 201

if __name__ == "__main__":
    app.run(debug=True)   # Mode développement uniquement
```

Lancer le serveur (mode développement) :

```bash
flask --app app run --debug
```

> ⚠️ Le mode `debug` ne doit **jamais** être activé en production. Pour déployer, utilisez un serveur WSGI comme `gunicorn`.

**Tester l'API**

- `curl` dans le terminal :
  ```bash
  curl -X POST http://127.0.0.1:5000/users \
       -H "Content-Type: application/json" \
       -d '{"name": "Chloé"}'
  ```
- Postman ou Insomnia
- JavaScript dans le navigateur (`fetch`)
- Un autre script Python avec `requests`

### 7.3 Alternative moderne : FastAPI

**FastAPI** est très populaire pour créer des API : il est **asynchrone**, valide automatiquement les données (via *Pydantic*) et génère une documentation interactive sur `/docs`.

```bash
pip install fastapi uvicorn
```

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
users = {1: "Alice", 2: "Bob"}

class NouvelUtilisateur(BaseModel):
    name: str

@app.get("/users/{user_id}")
async def lire_utilisateur(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")
    return {"id": user_id, "name": users[user_id]}

@app.post("/users", status_code=201)
async def creer_utilisateur(utilisateur: NouvelUtilisateur):
    nouvel_id = max(users, default=0) + 1
    users[nouvel_id] = utilisateur.name
    return {"id": nouvel_id, "name": utilisateur.name}
```

```bash
uvicorn main:app --reload
```

### 7.4 Principales méthodes HTTP

| Méthode  | Usage                                  |
| -------- | -------------------------------------- |
| `GET`    | Lire des données                       |
| `POST`   | Créer une nouvelle ressource           |
| `PUT`    | Remplacer entièrement une ressource    |
| `PATCH`  | Modifier partiellement une ressource   |
| `DELETE` | Supprimer une ressource                |

### 7.5 Codes de statut

Les codes sont regroupés par famille : **2xx** succès, **3xx** redirection, **4xx** erreur du client, **5xx** erreur du serveur.

| Code | Signification                  |
| ---- | ------------------------------ |
| 200  | OK                             |
| 201  | Créé (*Created*)               |
| 204  | Pas de contenu                 |
| 400  | Requête invalide               |
| 401  | Non authentifié                |
| 403  | Accès interdit                 |
| 404  | Introuvable                    |
| 422  | Données non traitables (validation) |
| 429  | Trop de requêtes               |
| 500  | Erreur interne du serveur      |
| 503  | Service indisponible           |

---

## 8. Programmation asynchrone (`asyncio`)

### Qu'est-ce que la programmation asynchrone ?

La **programmation asynchrone** permet à un programme d'avancer sur plusieurs tâches **sans attendre** qu'une opération lente (requête réseau, lecture de fichier…) soit terminée avant de continuer.

**Avantages :**

- Exécution **non bloquante**
- Meilleures performances pour les tâches limitées par les entrées/sorties (*I/O-bound*)
- Code souvent plus simple que les threads pour ces cas d'usage

> ℹ️ L'asynchrone n'accélère **pas** les calculs lourds (CPU-bound). Pour ceux-ci, utilisez `multiprocessing` ou `concurrent.futures.ProcessPoolExecutor`.

### 8.1 Synchrone vs asynchrone

**Version synchrone**

```python
import time

def fetch_data():
    time.sleep(2)
    return "Données reçues"

print(fetch_data())
print("Terminé")
```

⏱ Résultat (≈ 2 secondes) :

```
Données reçues
Terminé
```

**Version asynchrone**

```python
import asyncio

async def fetch_data():
    await asyncio.sleep(2)
    return "Données reçues"

async def main():
    resultat = await fetch_data()
    print(resultat)
    print("Terminé")

asyncio.run(main())
```

> Pour une seule tâche, le résultat est identique. L'intérêt apparaît quand on **attend plusieurs tâches en même temps** (voir ci-dessous).

### 8.2 Vocabulaire clé

| Terme                     | Signification                                                    |
| ------------------------- | ---------------------------------------------------------------- |
| `async def`               | Définit une **coroutine** (fonction asynchrone)                  |
| `await`                   | Suspend la coroutine jusqu'à la fin d'un objet *awaitable*       |
| `asyncio.run()`           | Point d'entrée : lance la coroutine principale                   |
| `asyncio.sleep()`         | Pause **non bloquante**                                          |
| `asyncio.gather()`        | Exécute plusieurs awaitables en parallèle et rassemble les résultats |
| `asyncio.create_task()`   | Planifie une coroutine pour qu'elle s'exécute en arrière-plan    |
| `asyncio.TaskGroup`       | Groupe de tâches avec gestion structurée des erreurs (3.11+)     |
| `asyncio.timeout()`       | Limite le temps d'attente d'un bloc (3.11+)                      |
| `asyncio.to_thread()`     | Exécute une fonction bloquante dans un thread (3.9+)             |

### 8.3 Exécuter plusieurs tâches en même temps avec `gather`

```python
import asyncio

async def tache(nom, delai):
    print(f"Début de {nom}")
    await asyncio.sleep(delai)
    print(f"Fin de {nom}")
    return nom

async def main():
    resultats = await asyncio.gather(
        tache("A", 2),
        tache("B", 1),
        tache("C", 3),
    )
    print(resultats)   # ['A', 'B', 'C'] : l'ordre des arguments est conservé

asyncio.run(main())
```

Résultat :

```
Début de A
Début de B
Début de C
Fin de B
Fin de A
Fin de C
['A', 'B', 'C']
```

> ⏱ Durée totale : ≈ 3 secondes au lieu de 6.

Pour qu'une erreur dans une tâche n'annule pas les autres, ajoutez `return_exceptions=True` : les exceptions sont alors renvoyées dans la liste de résultats.

### 8.4 `TaskGroup` : la méthode moderne (Python 3.11+)

`TaskGroup` est un gestionnaire de contexte asynchrone : il attend la fin de **toutes** les tâches, et si l'une échoue, il **annule les autres** proprement.

```python
async def main():
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(tache("A", 2))
        t2 = tg.create_task(tache("B", 1))
    # Ici, toutes les tâches sont terminées
    print(t1.result(), t2.result())
```

Les erreurs sont regroupées dans un `ExceptionGroup`, qu'on gère avec `except*` :

```python
try:
    async with asyncio.TaskGroup() as tg:
        tg.create_task(tache_qui_echoue())
except* ValueError as groupe:
    print("Erreurs de valeur :", groupe.exceptions)
```

### 8.5 `asyncio.create_task()`

Planifie une coroutine pour qu'elle s'exécute indépendamment :

```python
async def main():
    t1 = asyncio.create_task(tache("A", 2))
    t2 = asyncio.create_task(tache("B", 3))
    print("Tâches créées")
    await t1
    await t2
```

> ⚠️ **Conservez toujours une référence** à la tâche créée (variable, liste…). Sinon, elle risque d'être supprimée par le ramasse-miettes avant d'avoir fini.

### 8.6 Limiter le temps d'attente

```python
async def main():
    try:
        async with asyncio.timeout(2):   # Python 3.11+
            await asyncio.sleep(10)
    except TimeoutError:
        print("Trop long, abandon")
```

### 8.7 Mélanger code synchrone et asynchrone

Une coroutine peut appeler une fonction ordinaire. Mais une fonction **bloquante** (ex. `time.sleep`, `requests.get`) fige toute la boucle d'événements : toutes les autres tâches s'arrêtent.

```python
import asyncio
import time

def bloquante():
    time.sleep(2)            # Bloque tout le programme si appelée directement
    return "fini"

async def main():
    # Exécutée dans un thread : la boucle reste disponible
    resultat = await asyncio.to_thread(bloquante)
    print(resultat)

asyncio.run(main())
```

À l'inverse, pour appeler du code asynchrone depuis du code synchrone, passez par `asyncio.run()`.

### 8.8 Exemple concret : récupérer des pages web en parallèle

Avec `aiohttp` (`pip install aiohttp`). On crée **une seule session** partagée par toutes les requêtes, via `async with` :

```python
import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as reponse:
        return await reponse.text()

async def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://api.github.com",
    ]
    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        resultats = await asyncio.gather(*(fetch(session, url) for url in urls))

    for resultat in resultats:
        print(resultat[:100])   # Affiche les 100 premiers caractères

asyncio.run(main())
```

### 8.9 Erreurs courantes

| Erreur                                                        | Cause                                                              |
| ------------------------------------------------------------- | ------------------------------------------------------------------ |
| `RuntimeWarning: coroutine '...' was never awaited`           | `await` oublié devant l'appel d'une coroutine                      |
| `RuntimeError: asyncio.run() cannot be called from a running event loop` | `asyncio.run()` appelé alors qu'une boucle tourne déjà (ex. Jupyter) : utilisez directement `await main()` |
| `RuntimeError: Event loop is closed`                          | Utilisation d'une boucle déjà fermée (souvent liée à Windows ou à un double `run`) |
| `TypeError: object X can't be used in 'await' expression`     | `await` appliqué à autre chose qu'un awaitable (fonction ordinaire) |

---

## 9. Aide-mémoire final

| Je veux…                                        | J'utilise                                   |
| ----------------------------------------------- | ------------------------------------------- |
| Chercher, valider ou remplacer du texte         | `re`                                        |
| Lire une variable d'environnement               | `os.environ.get()` / `os.getenv()`          |
| Manipuler des fichiers et des chemins           | `pathlib.Path`                              |
| Copier, déplacer ou supprimer un dossier entier | `shutil`                                    |
| Lancer une commande système                     | `subprocess.run()`                          |
| Manipuler des dates, durées et fuseaux          | `datetime`, `timedelta`, `zoneinfo`         |
| Lire/écrire des données structurées             | `json`                                      |
| Garantir la fermeture d'une ressource           | `with` / `contextlib`                       |
| Appeler une API (synchrone)                     | `requests` (avec `timeout`)                 |
| Appeler beaucoup d'API en parallèle             | `asyncio` + `aiohttp`                       |
| Créer une API                                   | Flask (simple) ou FastAPI (moderne, async)  |
