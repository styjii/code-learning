"""
Catalogue des pages de cours.

Source unique de vérité pour :
- les routes (``language/urls.py``),
- la conversion Markdown -> HTML (``webapp/services.py``),
- l'accueil et le sélecteur de langage (``language/catalog.py``).

``PAGE_CONFIG`` reste exposé sous sa forme historique ``{clé: (fichier.md, titre)}``.
"""

from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass(frozen=True)
class Page:
    key: str          # identifiant d'URL, ex. "frameworks/django"
    file: str         # fichier Markdown dans language/topics/
    title: str        # titre affiché
    category: str     # clé de CATEGORIES
    icon: str         # chemin statique de l'icône
    color: str        # couleur d'accent du langage
    description: str  # phrase d'accroche pour les cartes
    runnable: bool = False  # blocs de code exécutables (bouton « Exécuter ») dans cette page


CATEGORIES: List[Tuple[str, str, str]] = [
    ("topics", "Langages & outils", "Les guides complets, du niveau débutant à l'avancé."),
    ("frameworks", "Frameworks", "Construire des applications complètes."),
    ("modules", "Modules", "Bibliothèques et modules essentiels."),
    ("database", "Bases de données", "Stocker, interroger et administrer ses données."),
    ("system", "Terminal & système", "Commandes et scripts pour maîtriser son environnement."),
    ("exercises", "Exercices", "S'entraîner avec des défis progressifs."),
    ("solutions", "Corrigés", "Les solutions commentées des exercices."),
    ("projects", "Projets", "Mettre en pratique avec des projets concrets."),
]

_PAGES: List[Page] = [
    # --- Langages & outils ---
    Page("css", "css.md", "CSS", "topics", "icons/css.svg", "#26ade4",
         "Mise en page, Flexbox, Grid, animations et CSS moderne."),
    Page("javascript", "javascript.md", "JavaScript", "topics", "icons/javascript.svg", "#f7df1e",
         "Le langage du web : de la syntaxe aux API du navigateur.", runnable=True),
    Page("typescript", "typescript.md", "TypeScript", "topics", "icons/typescript.svg", "#3178c6",
         "JavaScript avec un système de types pour des applications fiables.", runnable=True),
    Page("python", "python.md", "Python", "topics", "icons/python.svg", "#3776ab",
         "Du premier print() à la programmation orientée objet moderne.", runnable=True),
    Page("php", "php.md", "PHP", "topics", "icons/php.svg", "#777bb4",
         "Le langage côté serveur pour créer des sites dynamiques."),
    Page("c", "language-c.md", "Langage C", "topics", "icons/c.svg", "#5c6bc0",
         "Le langage fondamental de la programmation système."),
    Page("cpp", "language-cpp.md", "Langage C++", "topics", "icons/cpp.svg", "#00599c",
         "Du C++ moderne (C++17 à C++26) : POO, STL, fichiers et compilation."),
    Page("git", "git.md", "Git", "topics", "icons/git.svg", "#f05032",
         "Versionner son code et collaborer sans stress."),
    Page("algorithm", "algorithm.md", "Algorithmique", "topics", "icons/algorithm.svg", "#8b5cf6",
         "Tris, recherche, récursivité, structures de données."),
    # --- Frameworks ---
    Page("frameworks/angular", "frameworks/angular.md", "Angular", "frameworks", "icons/angular.svg", "#dd0031",
         "Le framework de Google pour des applications web robustes."),
    Page("frameworks/django", "frameworks/django.md", "Django", "frameworks", "icons/django.svg", "#44b78b",
         "Le framework Python « batteries included » pour le web."),
    Page("frameworks/laravel", "frameworks/laravel.md", "Laravel", "frameworks", "icons/laravel.svg", "#ff2d20",
         "Le framework PHP élégant pour des applications web modernes."),
    Page("frameworks/react", "frameworks/react.md", "React", "frameworks", "icons/react.svg", "#61dafb",
         "La bibliothèque pour créer des interfaces : du premier composant aux Server Components."),
    Page("frameworks/vuejs", "frameworks/vuejs.md", "Vue.js", "frameworks", "icons/vue.svg", "#41b883",
         "Le framework progressif pour des interfaces réactives, avec Vue 3 et TypeScript."),
    # --- Modules ---
    Page("modules/python", "modules/python.md", "Modules Python", "modules", "icons/python.svg", "#3776ab",
         "Les modules essentiels de la bibliothèque standard."),
    Page("modules/bs4", "modules/bs4.md", "BeautifulSoup", "modules", "icons/python.svg", "#43a047",
         "Extraire des données de pages HTML avec bs4."),
    Page("modules/c", "modules/c-module.md", "Modules C", "modules", "icons/c-module.svg", "#5c6bc0",
         "Organiser un projet C : en-têtes, bibliothèques et compilation."),
    Page("modules/cpp", "modules/cpp-module.md", "Modules C++", "modules", "icons/cpp-module.svg", "#00599c",
         "Structurer un projet C++ : espaces de noms, bibliothèques et modules C++20."),
    Page("modules/flask", "modules/flask.md", "Flask", "modules", "icons/flask.svg", "#38bdf8",
         "Le micro-framework web Python, simple et extensible."),
    Page("modules/pandas", "modules/pandas.md", "Pandas", "modules", "icons/pandas.svg", "#e70488",
         "Manipuler et analyser des données tabulaires en Python."),
    Page("modules/numpy", "modules/numpy.md", "NumPy", "modules", "icons/numpy.svg", "#4dabcf",
         "Le calcul scientifique avec les tableaux multidimensionnels."),
    # --- Bases de données ---
    Page("database/sqlite3", "database/sqlite3.md", "SQLite3", "database", "icons/sqlite3.svg", "#0f80cc",
         "La base SQL embarquée, sans serveur, dans un simple fichier."),
    Page("database/mysql", "database/mysql.md", "MySQL", "database", "icons/mysql.svg", "#00758f",
         "Le SGBD relationnel open source le plus répandu."),
    Page("database/postgresql", "database/postgresql.md", "PostgreSQL", "database", "icons/postgresql.svg", "#336791",
         "La base relationnelle avancée, robuste et extensible."),
    # --- Terminal & système ---
    Page("system/linux-commands", "system/linux-commands.md", "Commandes Linux", "system", "icons/linux.svg", "#fcc624",
         "Bash et Zsh : naviguer, manipuler les fichiers et administrer."),
    Page("system/windows-commands", "system/windows-commands.md", "Commandes Windows", "system", "icons/windows.svg", "#0078d4",
         "CMD et PowerShell : les commandes essentielles sous Windows."),
    Page("system/bash-scripts", "system/bash-scripts.md", "Scripts Bash", "system", "icons/bash.svg", "#4eaa25",
         "Automatiser des tâches avec des scripts shell Bash."),
    Page("system/zsh-scripts", "system/zsh-scripts.md", "Scripts Zsh", "system", "icons/zsh.svg", "#f15a24",
         "Scripts et configuration avancée avec Zsh."),
    # --- Exercices ---
    Page("exercises/javascript", "exercises/javascript.md", "Exercices JavaScript", "exercises",
         "icons/javascript.svg", "#f7df1e", "Défis de fonctions, variables, conditions et boucles."),
    Page("exercises/typescript", "exercises/typescript.md", "Exercices TypeScript", "exercises",
         "icons/typescript.svg", "#3178c6", "Typage, génériques et types avancés en pratique."),
    Page("exercises/python", "exercises/python.md", "Exercices Python", "exercises",
         "icons/python.svg", "#3776ab", "Exercices pratiques et mise en application des connaissances en Python."),
    Page("exercises/php", "exercises/php.md", "Exercices PHP", "exercises",
     "icons/php.svg", "#777bb4", "Exercices pratiques pour renforcer les connaissances en PHP et maîtriser le développement web côté serveur."),
    Page("exercises/c", "exercises/language-c.md", "Exercices C", "exercises",
         "icons/c.svg", "#5c6bc0", "Exercices et mini-projets en langage C."),
    Page("exercises/algorithm", "exercises/algorithm.md", "Exercices d'algorithmique", "exercises",
         "icons/algorithm.svg", "#8b5cf6", "Problèmes classiques, résolus avec Python."),
    # --- Corrigés ---
    Page("solutions/javascript", "solutions/javascript.md", "Corrigés JavaScript", "solutions",
         "icons/javascript.svg", "#f7df1e", "Solutions commentées des défis JavaScript."),
    Page("solutions/typescript", "solutions/typescript.md", "Corrigés TypeScript", "solutions",
         "icons/typescript.svg", "#3178c6", "Solutions commentées des exercices TypeScript."),
    Page("solutions/c", "solutions/language-c.md", "Corrigés C", "solutions",
         "icons/c.svg", "#5c6bc0", "Solutions commentées des exercices C."),
    Page("solutions/algorithm", "solutions/algorithm.md", "Corrigés d'algorithmique", "solutions",
         "icons/algorithm.svg", "#8b5cf6", "Solutions commentées des problèmes d'algorithmique."),
    # --- Projets ---
    Page("projects/javascript", "projects/javascript.md", "Projets JavaScript", "projects",
         "icons/javascript.svg", "#f7df1e", "Des projets en ligne de commande avec Node.js."),
    Page("projects/c", "projects/language-c.md", "Projets C", "projects",
         "icons/c.svg", "#5c6bc0", "Des projets complets en langage C."),
]

PAGES: Dict[str, Page] = {page.key: page for page in _PAGES}

# Formes historiques, conservées pour compatibilité.
PAGE_CONFIG: Dict[str, Tuple[str, str]] = {p.key: (p.file, p.title) for p in _PAGES}
ICON_PATHS: Dict[str, str] = {p.key: p.icon for p in _PAGES}
