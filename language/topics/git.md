<div align="center">

# Git — Guide complet

**Du premier `git init` aux workflows d'équipe avancés**

*Mis à jour pour Git 2.55 (2026)*

</div>

---

## Sommaire

1. [Introduction et installation](#1-introduction-et-installation)
2. [Bases de Git (niveau débutant)](#2-bases-de-git-niveau-débutant)
3. [Branches et étiquettes](#3-branches-et-étiquettes)
4. [Dépôts distants et collaboration](#4-dépôts-distants-et-collaboration)
5. [Annuler des modifications et gérer l'historique](#5-annuler-des-modifications-et-gérer-lhistorique)
6. [Branches et fusions avancées](#6-branches-et-fusions-avancées)
7. [Fonctionnement interne et configuration](#7-fonctionnement-interne-et-configuration)
8. [Workflows de collaboration](#8-workflows-de-collaboration)
9. [Outils et astuces](#9-outils-et-astuces)
10. [Interfaces graphiques, plateformes et CI/CD](#10-interfaces-graphiques-plateformes-et-cicd)
11. [Sécurité et bonnes pratiques](#11-sécurité-et-bonnes-pratiques)
12. [Aide-mémoire](#12-aide-mémoire)

> **Légende** : les sections marquées *(ajout)* complètent le guide d'origine ; les mentions *(à jour)* signalent une pratique moderne qui remplace une ancienne.

> **Conventions des exemples** : les valeurs entre chevrons (`<hash>`, `<url>`, `<fichier>`) sont à remplacer par vos propres valeurs ; lorsqu'un bloc présente plusieurs variantes d'une même commande, elles sont indépendantes (à lire comme « l'une ou l'autre »).

---

# 1. Introduction et installation

## 1.1 Qu'est-ce que Git ?

**Git** est un système de **gestion de versions décentralisé** (*DVCS*), créé par **Linus Torvalds en 2005** pour développer le noyau Linux.

- Chaque développeur possède une **copie complète** du dépôt, avec tout l'historique.
- Il permet à plusieurs personnes de travailler sur le même code **sans écraser** le travail des autres.
- Il rend les branches et les fusions **rapides et peu coûteuses**.

**Pourquoi l'utiliser ?**

| Avantage | Détail |
| --- | --- |
| Historique | Chaque modification est conservée et datée |
| Collaboration | Travail en parallèle, relectures, *pull requests* |
| Retour arrière | Retrouver une version antérieure en cas de bug |
| Expérimentation | Tester une idée dans une branche sans risque |
| Hors-ligne | Presque toutes les opérations fonctionnent sans réseau |

> **Remarque** : **Git ≠ GitHub.** Git est l'outil ; GitHub, GitLab, Bitbucket, etc. sont des services qui hébergent des dépôts Git.

## 1.2 Installer Git

Vérifiez toujours l'installation avec :

```bash
git --version
```

### Windows

1. Téléchargez l'installateur sur [git-scm.com/download/win](https://git-scm.com/download/win), ou utilisez :

```powershell
winget install --id Git.Git -e --source winget
```

2. Suivez l'assistant et choisissez votre terminal (**Git Bash** est courant).

### macOS

```bash
brew install git            # recommandé (version à jour)
xcode-select --install      # alternative : outils en ligne de commande Xcode
```

> **Attention** : Le Git fourni par Apple est souvent plus ancien que la dernière version.

### Linux

```bash
# Debian / Ubuntu
sudo apt update && sudo apt install git

# Fedora / CentOS / RHEL
sudo dnf install git

# Arch
sudo pacman -S git
```

## 1.3 Configurer Git (`git config`)

Renseignez votre identité : elle apparaît dans chaque commit.

```bash
git config --global user.name "Votre Nom"
git config --global user.email "vous@exemple.com"
```

### Réglages recommandés *(à jour)*

```bash
git config --global init.defaultBranch main     # branche initiale = main
git config --global pull.rebase false           # fusion au pull (true : rebase)
git config --global core.editor "code --wait"   # éditeur (VS Code)
git config --global color.ui auto
git config --global push.autoSetupRemote true   # git push crée la branche distante au besoin
git config --global rerere.enabled true         # mémorise les résolutions de conflits
```

| Option | Rôle |
| --- | --- |
| `user.name`, `user.email` | Identité de l'auteur |
| `core.editor` | Éditeur pour les messages de commit |
| `merge.tool`, `diff.tool` | Outils de fusion / de comparaison |
| `init.defaultBranch` | Nom de la branche créée par `git init` |
| `pull.rebase` | Stratégie de `git pull` (fusion ou rebase) |
| `core.autocrlf` | Fins de ligne (`true` sous Windows, `input` sous Linux/macOS) |

Afficher la configuration : `git config --list --show-origin`.

### Niveaux de configuration

| Niveau | Option | Fichier |
| --- | --- | --- |
| Système | `--system` | `/etc/gitconfig` |
| Global (utilisateur) | `--global` | `~/.gitconfig` |
| Local (dépôt) | *(par défaut)* `--local` | `.git/config` |

Le niveau le plus précis l'emporte : **local > global > système**.

## 1.4 Architecture : les trois zones de Git

Git organise vos fichiers en **trois zones** :

| Zone | Rôle |
| --- | --- |
| **Répertoire de travail** (*working directory*) | Vos fichiers actuels, que vous éditez |
| **Index / zone de préparation** (*staging area*) | Modifications sélectionnées pour le prochain commit |
| **Dépôt** (*repository*, dossier `.git`) | Historique des commits enregistrés |

```text
Répertoire de travail ──git add──▶ Index ──git commit──▶ Dépôt local ──git push──▶ Dépôt distant
        ▲                                                       │
        └───────────── git restore / git checkout ◀─────────────┘
```

## 1.5 Authentification : SSH, HTTPS et GitHub CLI

Pour dialoguer avec un dépôt distant sans retaper vos identifiants, trois méthodes existent.

> **Attention** : Les **mots de passe de compte** ne sont plus acceptés par GitHub pour Git (depuis 2021) : utilisez une clé SSH, un **jeton d'accès personnel** (*PAT*) ou un gestionnaire d'identifiants.

### Option A — Clés SSH (recommandé)

**1. Vérifier les clés existantes**

```bash
ls -al ~/.ssh
```

**2. Générer une clé** (Ed25519 est le choix actuel, plus sûr et plus court que RSA)

```bash
ssh-keygen -t ed25519 -C "vous@exemple.com"
```

Si Ed25519 n'est pas disponible : `ssh-keygen -t rsa -b 4096 -C "vous@exemple.com"`. Définissez une **phrase secrète** (*passphrase*).

**3. Ajouter la clé à `ssh-agent`**

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

**4. Enregistrer la clé publique** sur la plateforme

```bash
cat ~/.ssh/id_ed25519.pub     # copiez le résultat
```

GitHub : *Settings → SSH and GPG keys → New SSH key*. GitLab : *Preferences → SSH Keys*.

**5. Tester la connexion**

```bash
ssh -T git@github.com
```

### Option B — HTTPS avec gestionnaire d'identifiants

**Git Credential Manager** (inclus avec Git pour Windows) stocke vos identifiants de façon sécurisée et gère l'authentification par navigateur.

```bash
# Windows
git config --global credential.helper manager

# macOS
git config --global credential.helper osxkeychain
```

### Option C — GitHub CLI *(ajout)*

```bash
gh auth login      # authentification guidée (navigateur ou jeton)
gh auth setup-git  # configure Git pour utiliser cette authentification
```

---

# 2. Bases de Git (niveau débutant)

## 2.1 Créer un dépôt (`git init`)

```bash
mkdir monprojet
cd monprojet
git init
```

Cela crée un dossier caché **`.git`** contenant toutes les données du dépôt. Pour forcer le nom de la branche : `git init -b main`.

## 2.2 Cloner un dépôt (`git clone`)

```bash
git clone https://github.com/utilisateur/depot.git               # via HTTPS (crée le dossier depot)
git clone git@github.com:utilisateur/depot.git depot-ssh         # via SSH, dans un dossier distinct
git clone https://github.com/utilisateur/depot.git mon-dossier   # dans un dossier au nom choisi
```

Cela crée un dossier contenant les fichiers **et tout l'historique**.

### Variantes utiles *(ajout)*

| Commande | Effet |
| --- | --- |
| `git clone --depth 1 <url>` | Clone **superficiel** : seulement le dernier commit (rapide) |
| `git clone --filter=blob:none <url>` | Clone **partiel** : télécharge les fichiers à la demande |
| `git clone --branch <nom> <url>` | Clone une branche précise |
| `git clone --recurse-submodules <url>` | Inclut les sous-modules |

## 2.3 Voir l'état (`git status`)

```bash
git status          # état complet
git status -s       # version courte
```

Affiche les fichiers **non suivis**, **modifiés** et **prêts à être validés**.

## 2.4 Préparer les changements (`git add`)

```bash
git add fichier.txt      # un fichier
git add dossier/         # un dossier
git add .                # tout (nouveaux, modifiés, supprimés) dans le dossier courant
git add -u               # seulement les fichiers DÉJÀ suivis (modifiés / supprimés)
git add -p               # choisir interactivement les morceaux (hunks) à indexer
```

> **Astuce** : `git add -p` permet de réaliser des commits **petits et cohérents** même quand vous avez modifié plusieurs choses à la fois.

### Supprimer et renommer

```bash
git rm fichier.txt              # supprime le fichier et indexe la suppression
git rm --cached secret.env      # arrête de suivre le fichier mais le garde sur le disque
git mv ancien.txt nouveau.txt   # renomme / déplace
```

## 2.5 Valider les changements (`git commit`)

```bash
git commit -m "Ajoute les fichiers initiaux du projet"
git commit                       # ouvre l'éditeur pour un message détaillé
git commit -am "Corrige le calcul"   # add -u + commit (fichiers déjà suivis seulement)
git commit --amend               # modifie le DERNIER commit (message et/ou contenu)
```

### Rédiger de bons messages de commit

```text
type(portée): résumé court à l'impératif (≤ 50 caractères)

Corps facultatif : explique le POURQUOI du changement,
pas seulement le quoi. Ligne de 72 caractères maximum.
```

La convention **Conventional Commits** est très répandue :

| Type | Usage |
| --- | --- |
| `feat` | Nouvelle fonctionnalité |
| `fix` | Correction de bug |
| `docs` | Documentation |
| `refactor` | Réécriture sans changement de comportement |
| `test` | Ajout / modification de tests |
| `chore` | Maintenance, outils |

> **Attention** : **Ne réécrivez** (`--amend`) **jamais** un commit déjà poussé et partagé.

## 2.6 Consulter l'historique (`git log`)

Le journal affiche les commits **du plus récent au plus ancien**, avec hash, auteur, date et message.

```bash
git log
git log --oneline                    # un commit par ligne
git log -3 --oneline                 # les 3 derniers
git log --graph --oneline --all      # graphe des branches
git log --author="Alice"             # par auteur
git log --since="2 weeks ago"        # par date
git log -S"fonction"                 # commits qui ajoutent/suppriment ce texte
git log -p -- fichier.txt               # historique détaillé d'un fichier
git log --stat                       # fichiers modifiés par commit
git show <hash>                      # détail d'un commit
```

## 2.7 Ignorer des fichiers (`.gitignore`)

Le fichier `.gitignore`, à la racine du dépôt, liste ce que Git **ne doit pas suivre** (dépendances, fichiers de build, journaux, secrets…).

```gitignore
# Dossier des dépendances
node_modules/

# Tous les fichiers .log
*.log

# Variables d'environnement (secrets !)
.env

# Tout le contenu de build, sauf un fichier précis
build/*
!build/.gitkeep
```

| Motif | Signification |
| --- | --- |
| `*.log` | Tous les fichiers `.log` |
| `dossier/` | Un dossier et son contenu |
| `/fichier` | Uniquement à la racine |
| `**/temp` | Dans tous les sous-dossiers |
| `!fichier` | **Exception** (ne pas ignorer) |

> **Attention** : `.gitignore` n'agit pas sur les fichiers **déjà suivis**. Pour les retirer : `git rm --cached <fichier>`.
>
> **Astuce** : Modèles prêts à l'emploi : [github.com/github/gitignore](https://github.com/github/gitignore). Ignore global personnel : `git config --global core.excludesFile ~/.gitignore_global`.

## 2.8 Exemple de workflow complet

```bash
git init                                   # 1. initialiser
git status                                 # 2. vérifier l'état
echo "Hello Git" > README.md               # 3. créer un fichier
git add README.md                          # 4. indexer
git commit -m "Ajoute le README"           # 5. valider
git log --oneline                          # 6. consulter l'historique
```

---

# 3. Branches et étiquettes

## 3.1 Comprendre les branches

Une **branche** est un **pointeur léger et mobile vers un commit**. Elle permet de travailler sur une fonctionnalité ou une correction **en isolation**, sans toucher au code principal.

- La branche par défaut s'appelle aujourd'hui **`main`** (historiquement `master`).
- Créer une branche est quasi instantané : Git ne copie pas les fichiers.
- **`HEAD`** indique la branche (ou le commit) sur lequel vous travaillez.

## 3.2 Créer, lister et changer de branche

```bash
git branch                      # liste (* = branche courante)
git branch -a                   # locales + distantes
git branch -vv                  # avec le dernier commit et la branche suivie
git branch feature/login        # crée (sans basculer)
```

### Changer de branche *(à jour)*

Depuis **Git 2.23**, deux commandes spécialisées remplacent les usages multiples de `git checkout` :

| Action | Commande moderne | Ancienne commande |
| --- | --- | --- |
| Changer de branche | `git switch feature/login` | `git checkout feature/login` |
| Créer et basculer | `git switch -c feature/login` | `git checkout -b feature/login` |
| Revenir à la branche précédente | `git switch -` | `git checkout -` |
| Restaurer un fichier | `git restore fichier` | `git checkout -- fichier` |

> `git checkout` fonctionne toujours, mais **`switch`** et **`restore`** sont plus clairs et moins risqués.

## 3.3 Fusionner des branches (`git merge`)

On se place sur la branche **destinataire**, puis on fusionne l'autre :

```bash
git switch main
git merge feature/login
```

| Type de fusion | Description |
| --- | --- |
| **Avance rapide** (*fast-forward*) | `main` n'a pas bougé : Git avance simplement le pointeur, sans commit de fusion |
| **Fusion à trois points** | Les deux branches ont divergé : Git crée un **commit de fusion** |
| `git merge --no-ff` | Force un commit de fusion (garde la trace de la branche) |
| `git merge --squash` | Condense toutes les modifications en **un seul** commit à valider soi-même |
| `git merge --abort` | Annule une fusion en cours (conflits) |

En cas de conflit, voir la [section 6.1](#61-résoudre-les-conflits-de-fusion).

## 3.4 Supprimer des branches

```bash
git branch -d feature/login     # suppression sûre (refuse si non fusionnée)
git branch -D feature/login     # suppression forcée (perte possible)
git push origin --delete feature/login    # supprime la branche distante
git fetch --prune                         # nettoie les références distantes obsolètes
```

## 3.5 Étiquettes (*tags*) pour marquer des versions

Une **étiquette** est un pointeur **fixe** vers un commit, souvent utilisé pour les versions (`v1.0.0`). Suivez le **versionnement sémantique** : `MAJEUR.MINEUR.CORRECTIF`.

| Type | Description | Commande |
| --- | --- | --- |
| **Légère** | Simple pointeur | `git tag v1.0` |
| **Annotée** (recommandée) | Objet complet : auteur, date, message, signature possible | `git tag -a v1.0 -m "Première version stable"` |

```bash
git tag                          # lister
git tag -a v1.0 -m "Version 1.0"             # étiqueter le commit courant
git tag -a v0.9 <hash> -m "Version 0.9"      # étiqueter un ancien commit
git show v1.0                    # détails
git push origin v1.0             # pousser une étiquette
git push origin --tags           # pousser toutes les étiquettes
git push origin --delete v1.0    # supprimer côté distant
git tag -d v1.0                  # supprimer en local
```

> Les étiquettes **ne sont pas poussées automatiquement**.

## 3.6 Exemple de workflow

```bash
git switch -c feature/signup              # créer et basculer
echo "<h1>Inscription</h1>" > inscription.html   # créer un fichier
git add . && git commit -m "Ajoute la page d'inscription"
git switch main                           # revenir à main
git merge feature/signup                  # fusionner
git branch -d feature/signup              # supprimer la branche locale
git tag -a v1.0 -m "Version 1.0"          # étiqueter la release
git push origin main --tags               # pousser branche et étiquettes (nécessite un dépôt distant : voir la section 4)
```

---

# 4. Dépôts distants et collaboration

## 4.1 Ajouter un dépôt distant (`git remote`)

Un **dépôt distant** (*remote*) est une version du projet hébergée ailleurs. Le nom conventionnel du principal est **`origin`**.

```bash
git remote add origin https://github.com/utilisateur/monprojet.git
git remote -v                                                  # lister
git remote set-url origin https://github.com/utilisateur/nouveau-nom.git   # changer l'URL
git remote rename origin principal                             # renommer
git remote rename principal origin                             # revenir au nom conventionnel
git remote remove origin                                       # supprimer (inutile si vous poursuivez les exemples)
```

## 4.2 Récupérer sans fusionner (`git fetch`)

Télécharge commits et références **sans modifier** vos branches locales.

```bash
git fetch origin
git fetch --all --prune
git log HEAD..origin/main --oneline    # voir ce qui est arrivé
```

## 4.3 Récupérer et intégrer (`git pull`)

`git pull` = **`git fetch` + intégration** (fusion ou rebase).

```bash
git pull                      # branche suivie
git pull origin main
git pull --rebase             # rejoue vos commits au-dessus (historique linéaire)
git pull --ff-only            # refuse tout sauf une avance rapide (le plus sûr)
```

> **Astuce** : Pour fixer votre préférence : `git config --global pull.rebase true` (rebase) ou `git config --global pull.ff only` (avance rapide uniquement).

## 4.4 Envoyer des changements (`git push`)

```bash
git push origin main
git push -u origin ma-branche     # -u : mémorise la branche distante (suivi)
git push                          # ensuite, simplement
```

### Forcer un envoi : à manier avec précaution

```bash
git push --force-with-lease       # forcer SEULEMENT si personne n'a poussé entre-temps
# git push --force                # écrase aveuglément le travail des autres
```

Ne forcez que sur **vos propres branches** (par exemple après un rebase).

## 4.5 Forks et *pull requests*

Sur GitHub, les contributeurs externes **dupliquent** (*fork*) le dépôt, travaillent dans leur copie, puis proposent leurs changements par une **pull request** (PR ; *merge request* sur GitLab).

```bash
# 1. Forkez le dépôt via l'interface web, puis clonez VOTRE fork
git clone https://github.com/vous/projet.git
cd projet

# 2. Ajoutez le dépôt d'origine comme remote « upstream »
git remote add upstream https://github.com/proprietaire/projet.git

# 3. Synchronisez régulièrement
git fetch upstream
git switch main
git merge upstream/main          # ou : git rebase upstream/main
git push origin main

# 4. Travaillez dans une branche, poussez-la sur votre fork
git switch -c feature/ma-contribution
# ...modifiez des fichiers...
git add . && git commit -m "Décrit la contribution"
git push -u origin feature/ma-contribution
# 5. Ouvrez la pull request depuis l'interface web
```

### Avec GitHub CLI *(ajout)*

```bash
gh repo fork proprietaire/projet --clone   # fork + clone (remote « upstream » configuré)
cd projet
git switch -c feature/ma-contribution
# ...modifiez des fichiers...
git add . && git commit -m "Décrit la contribution"
gh pr create --fill              # crée la PR depuis la branche courante (propose de la pousser)
gh pr checkout 123               # récupère la PR n° 123 en local (pour la relire)
gh pr merge 123 --squash         # fusionne la PR n° 123 (si vous avez les droits)
```

## 4.6 Suivi des branches distantes

```bash
git branch -a                                  # locales + distantes
git branch -vv                                 # branche suivie par chaque branche
git branch --set-upstream-to=origin/main       # définir le suivi
git switch feature/chat                        # crée la branche locale qui suit origin/feature/chat
```

## 4.7 Exemple de workflow

```bash
git remote add origin https://github.com/utilisateur/monprojet.git
git push -u origin main                 # premier envoi
git pull --rebase                       # plus tard : récupérer les nouveautés
git switch -c feature/chat
git push -u origin feature/chat         # publier une nouvelle branche
```

---

# 5. Annuler des modifications et gérer l'historique

> **Règle d'or** : avant de défaire quelque chose, demandez-vous *« ce commit est-il déjà poussé ? »*.
> - **Non poussé** → vous pouvez réécrire l'historique (`reset`, `amend`, `rebase`).
> - **Déjà poussé / partagé** → utilisez `git revert` (nouveau commit inverse).

## 5.1 Voir les différences (`git diff`)

```bash
git diff                    # modifications NON indexées (travail vs index)
git diff --staged           # modifications indexées (index vs dernier commit)
git diff HEAD               # tout depuis le dernier commit
git diff main..feature      # entre deux branches
git diff abc123 def456      # entre deux commits
git diff --stat             # résumé (fichiers et nombre de lignes)
git diff --word-diff        # différences mot à mot
```

## 5.2 Désindexer un fichier *(à jour)*

```bash
git add index.html
git restore --staged index.html       # moderne (Git 2.23+)
# git reset HEAD index.html           # ancienne syntaxe, équivalente
```

Le fichier reste modifié dans le répertoire de travail, mais n'est plus indexé.

## 5.3 Annuler des modifications locales *(à jour)*

```bash
git restore index.html                # moderne
# git checkout -- index.html          # ancienne syntaxe
git restore .                         # tous les fichiers
git restore -p fichier                # choisir morceau par morceau
git restore --source=HEAD~2 fichier   # restaurer depuis un ancien commit
```

> **Irréversible** : les modifications non validées sont définitivement perdues.

## 5.4 Corriger le dernier commit

```bash
git add oubli.txt
git commit --amend --no-edit          # ajoute le fichier oublié au dernier commit
git commit --amend -m "Nouveau message"
```

## 5.5 Annuler un commit en sécurité (`git revert`)

Crée un **nouveau commit** qui inverse les effets d'un commit précédent. Sans danger pour l'historique partagé.

```bash
git revert <hash>
git revert HEAD --no-edit             # annule le dernier commit sans ouvrir l'éditeur
git revert -m 1 <hash-de-fusion>      # annuler un commit de FUSION (garde le parent 1)
```

## 5.6 Revenir en arrière (`git reset`)

Déplace la branche courante vers un autre commit.

| Mode | HEAD | Index | Répertoire de travail |
| --- | --- | --- | --- |
| `--soft` | déplacé | conservé | conservé |
| `--mixed` *(défaut)* | déplacé | réinitialisé | conservé |
| `--hard` | déplacé | réinitialisé | **écrasé** |

```bash
git reset --soft HEAD~1     # annule le commit, garde tout indexé
git reset HEAD~1            # annule le commit, garde les changements non indexés
git reset --hard HEAD~1     # annule le commit ET supprime les changements
git reset --hard origin/main  # aligne sur le distant (perd le travail local)
```

> **Attention** : N'utilisez pas `--hard` sur une branche partagée. En cas d'erreur, `git reflog` peut vous sauver (voir [9.3](#93-retrouver-des-commits-perdus-git-reflog)).

### `reset` ou `revert` ?

| | `git reset` | `git revert` |
| --- | --- | --- |
| Effet | Supprime des commits de l'historique | Ajoute un commit inverse |
| Historique partagé | Dangereux | Sûr |
| Usage | Travail local non poussé | Annuler un commit publié |

## 5.7 Mettre de côté (`git stash`)

Sauvegarde temporairement vos modifications non validées pour changer de contexte.

```bash
git stash                          # met de côté (fichiers suivis)
git stash push -m "travail en cours"   # avec un message
git stash -u                       # inclut aussi les fichiers non suivis
git stash list                     # liste
git stash show -p stash@{0}        # voir le contenu
git stash apply                    # réapplique (garde le stash)
git stash pop                      # réapplique ET supprime
git stash branch nouvelle-branche  # crée une branche à partir du stash
git stash drop stash@{0}           # supprime un stash
git stash clear                    # supprime tous les stashes
```

## 5.8 Nettoyer les fichiers non suivis (`git clean`)

```bash
git clean -n          # simulation : montre ce qui serait supprimé
git clean -f          # supprime les fichiers non suivis
git clean -fd         # + les dossiers non suivis
git clean -fdx        # + les fichiers ignorés (très destructeur)
git clean -i          # mode interactif
```

> Toujours faire un `-n` d'abord. Les fichiers supprimés ne passent pas par la corbeille.

## 5.9 Récapitulatif : « Je veux annuler… »

| Situation | Solution |
| --- | --- |
| Une modification non indexée | `git restore <fichier>` |
| Un fichier que j'ai indexé | `git restore --staged <fichier>` |
| Le dernier commit (non poussé), en gardant le travail | `git reset --soft HEAD~1` |
| Le dernier commit, avec correction du message | `git commit --amend` |
| Un commit déjà poussé | `git revert <hash>` |
| Tout le travail local non validé | `git restore .` / `git stash` |
| Un `reset --hard` malheureux | `git reflog` puis `git reset --hard <hash>` |

## 5.10 Exemple de workflow

```bash
git diff                       # inspecter
git add .
git commit -m "Travail en cours"
git reset --soft HEAD~1        # oups : annuler le commit en gardant les changements
git stash                      # changer de contexte
git switch -c autre-branche   # créer une autre branche
# ... travailler, committer ...
git switch -                  # revenir à la branche précédente
git stash pop                  # reprendre
```

---

# 6. Branches et fusions avancées

## 6.1 Résoudre les conflits de fusion

Un **conflit** survient quand Git ne peut pas combiner automatiquement des modifications (typiquement les **mêmes lignes** modifiées dans deux branches).

```bash
git switch main
git merge feature
# CONFLICT (content): Merge conflict in fichier.txt
```

Git marque les zones concernées dans le fichier :

```text
<<<<<<< HEAD
Changement venant de main
=======
Changement venant de feature
>>>>>>> feature
```

### Étapes de résolution

1. **Ouvrez** le fichier et choisissez/combinez le bon contenu ; **supprimez les marqueurs** `<<<<<<<`, `=======`, `>>>>>>>`.
2. **Marquez** le fichier comme résolu : `git add fichier.txt`.
3. **Finalisez** : `git commit` (ou `git merge --continue`).

```bash
git status                       # liste les fichiers en conflit
git merge --abort                # abandonner et revenir à l'état d'avant
git checkout --ours fichier      # garder VOTRE version (branche courante)
git checkout --theirs fichier    # garder la version de l'AUTRE branche
git mergetool                    # ouvrir un outil graphique
```

> **Astuce** : **`git rerere`** (*reuse recorded resolution*) mémorise vos résolutions et les réapplique automatiquement : `git config --global rerere.enabled true`.
>
> **Astuce** : Outils visuels : VS Code, Meld, KDiff3, GitKraken. Réglez `git config --global merge.conflictStyle zdiff3` pour afficher aussi l'ancêtre commun.

## 6.2 Rebaser (`git rebase`)

Le **rebase** rejoue vos commits **par-dessus** une autre base, pour obtenir un historique **linéaire**.

```bash
git switch feature
git rebase main
```

```text
Avant :
main:     A───B───C
               \
feature:        D───E

Après `git rebase main` (sur feature) :
main:     A───B───C
                   \
feature:            D'──E'      (D' et E' sont de NOUVEAUX commits)
```

| | `merge` | `rebase` |
| --- | --- | --- |
| Historique | Fidèle (garde les branches) | Linéaire et propre |
| Commits | Conservés tels quels | **Réécrits** (nouveaux hashs) |
| Risque | Faible | Élevé sur du code partagé |

> **Règle d'or du rebase : ne rebasez jamais des commits déjà poussés et utilisés par d'autres.**

En cas de conflit pendant un rebase :

```bash
# résolvez, puis :
git add fichier
git rebase --continue
git rebase --skip      # ignorer ce commit
git rebase --abort     # tout annuler
```

Après un rebase d'une branche déjà poussée (la vôtre uniquement) :

```bash
git push --force-with-lease
```

## 6.3 Rebase interactif (`git rebase -i`)

Permet de **réordonner, reformuler, fusionner, supprimer** des commits.

```bash
git rebase -i HEAD~3
```

```text
pick 1a2b3c1 Premier commit
pick 4d5e6f2 Deuxième commit
pick 7a8b9c3 Troisième commit
```

| Commande | Effet |
| --- | --- |
| `pick` | Garder le commit tel quel |
| `reword` | Garder, mais modifier le message |
| `edit` | S'arrêter pour modifier le commit |
| `squash` | Fusionner avec le précédent (combine les messages) |
| `fixup` | Fusionner avec le précédent (ignore ce message) |
| `drop` | Supprimer le commit |

### Correction automatique avec `--fixup` *(ajout)*

```bash
git commit --fixup <hash>         # crée un commit « fixup! » rattaché au commit visé
git rebase -i --autosquash main   # les réordonne et les fusionne automatiquement
```

## 6.4 Picorer un commit (`git cherry-pick`)

Applique **un commit précis** d'une branche sur une autre.

```bash
git switch main
git cherry-pick 9c8a7b6
git cherry-pick A^..B             # une plage de commits
git cherry-pick -x <hash>         # ajoute la référence du commit d'origine au message
git cherry-pick --abort
```

Cas typique : reporter un **correctif urgent** sur une branche de maintenance.

## 6.5 Écraser des commits (*squash*)

Regrouper plusieurs commits en un seul avant de fusionner.

```bash
# Méthode 1 : rebase interactif (squash / fixup)
git rebase -i HEAD~3

# Méthode 2 : reset doux + nouveau commit
git reset --soft HEAD~3
git commit -m "Fonctionnalité complète"

# Méthode 3 : à la fusion
git merge --squash feature && git commit
```

Les plateformes (GitHub, GitLab) proposent aussi **« Squash and merge »** à la fusion d'une PR.

## 6.6 Plusieurs répertoires de travail (`git worktree`) *(ajout)*

Permet d'avoir **plusieurs branches extraites en même temps**, dans des dossiers différents, sans cloner à nouveau ni mettre de côté votre travail.

```bash
git worktree add -b hotfix/1.2 ../correctif-urgent    # nouvelle branche dans un nouveau dossier lié au dépôt
git worktree list
git worktree remove ../correctif-urgent
```

## 6.7 Exemple de workflow

```bash
# Option A : fusionner feature dans main
git switch main && git merge feature

# Option B : rebaser feature sur main à jour, puis fusionner (avance rapide)
git switch feature && git rebase main
git switch main && git merge feature

# Reporter un correctif sur une autre branche
git switch hotfix && git cherry-pick abc1234

# Écraser les 2 derniers commits (ouvre l'éditeur)
git rebase -i HEAD~2
```

---

# 7. Fonctionnement interne et configuration

## 7.1 Le modèle d'objets de Git

Git est avant tout un **système de fichiers adressable par contenu** : chaque élément est un **objet** identifié par son **hash**, stocké dans `.git/objects`.

| Objet | Rôle |
| --- | --- |
| **Blob** | Contenu d'un fichier (sans nom ni métadonnées) |
| **Tree** (arbre) | Un dossier : liste des noms, avec références vers des blobs ou d'autres arbres |
| **Commit** | Instantané : pointe vers un arbre, et contient auteur, date, message et **commits parents** |
| **Tag annoté** | Objet qui pointe vers un autre objet (souvent un commit) avec métadonnées |

```text
commit ──▶ tree (racine) ──▶ blob (README.md)
   │                    └──▶ tree (src/) ──▶ blob (main.py)
   └──▶ commit parent
```

### Hash : SHA-1 et SHA-256

Historiquement, Git identifie les objets par **SHA-1** (40 caractères hexadécimaux). Git prend aussi en charge **SHA-256** (`git init --object-format=sha256`) et prévoit d'en faire le défaut dans **Git 3.0**.

### Explorer les objets

```bash
git cat-file -t <hash>        # type de l'objet
git cat-file -p <hash>        # contenu
git hash-object fichier.txt   # calcule le hash d'un fichier
git ls-tree HEAD              # contenu d'un arbre
```

## 7.2 Références et `HEAD`

- Une **référence** (*ref*) est un nom lisible qui pointe vers un hash : `refs/heads/main` (branches), `refs/tags/v1.0` (étiquettes), `refs/remotes/origin/main` (branches distantes).
- **`HEAD`** est une **référence symbolique** qui pointe normalement vers la **branche courante** (et non directement vers un commit).

```bash
cat .git/HEAD
# ref: refs/heads/main

git rev-parse HEAD           # hash du commit courant
```

### Raccourcis de révision

| Notation | Signification |
| --- | --- |
| `HEAD~1` ou `HEAD~` | Parent du commit courant |
| `HEAD~3` | Trois générations en arrière |
| `HEAD^2` | Second parent (utile pour une fusion) |
| `main@{yesterday}` | Où était `main` hier (via le reflog) |
| `abc123^{tree}` | Arbre associé |

### *Detached HEAD* (HEAD détaché)

Quand vous extrayez directement un commit ou une étiquette (`git switch --detach v1.0`), `HEAD` ne pointe plus vers une branche : vos nouveaux commits n'appartiendront à **aucune branche**. Pour les conserver : `git switch -c ma-branche`.

## 7.3 Hooks Git

Les **hooks** sont des scripts exécutés automatiquement à certains moments du cycle de vie de Git.

| Hook | Déclenchement | Usage typique |
| --- | --- | --- |
| `pre-commit` | Avant de créer le commit | Lint, formatage, tests rapides |
| `prepare-commit-msg` | Avant l'ouverture de l'éditeur | Pré-remplir le message |
| `commit-msg` | Après la saisie du message | Valider le format du message |
| `pre-push` | Avant l'envoi | Lancer les tests complets |
| `post-merge` | Après une fusion | Réinstaller les dépendances |
| `pre-rebase` | Avant un rebase | Bloquer certains rebases |

### Utilisation

```sh
#!/bin/sh
# Contenu du fichier .git/hooks/pre-commit
npm run lint || exit 1      # un code de sortie ≠ 0 bloque le commit
```

```bash
chmod +x .git/hooks/pre-commit
```

> **Attention** : Le dossier `.git/hooks` **n'est pas versionné** : les hooks ne sont pas partagés par défaut.

### Partager des hooks avec l'équipe *(ajout)*

```bash
git config core.hooksPath .githooks     # utiliser un dossier versionné du dépôt
```

Ou utilisez des outils dédiés : **pre-commit** (Python), **Husky** (JavaScript), **Lefthook**. Les versions récentes de Git (2.54+) permettent aussi de déclarer des hooks directement dans la configuration, et (2.55) de les exécuter en parallèle ; consultez `git help config`.

On peut contourner un hook ponctuellement avec `git commit --no-verify` (à éviter).

## 7.4 Alias Git

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.sw switch
git config --global alias.cm "commit -m"
git config --global alias.lg "log --graph --oneline --decorate --all"
git config --global alias.undo "reset --soft HEAD~1"
```

Utilisation : `git st`, `git lg`, `git cm "message"`.

## 7.5 Niveaux de configuration

Voir [1.3](#13-configurer-git-git-config) : **système** (`/etc/gitconfig`), **global** (`~/.gitconfig`) et **local** (`.git/config`). Il existe aussi la configuration conditionnelle :

```ini
# ~/.gitconfig : une autre identité pour les projets professionnels
[includeIf "gitdir:~/travail/"]
    path = ~/.gitconfig-travail
```

## 7.6 Sous-modules (`git submodule`)

Un **sous-module** inclut un dépôt Git dans un autre, à un **commit précis**.

```bash
git submodule add https://github.com/user/lib.git libs/lib
git commit -m "Ajoute le sous-module lib"

git clone --recurse-submodules <url>          # cloner avec les sous-modules
git submodule update --init --recursive       # les initialiser après un clone simple
git submodule update --remote                 # les mettre à jour vers la dernière version distante
```

> Les sous-modules ajoutent de la complexité. Pour de simples dépendances, préférez un gestionnaire de paquets (npm, pip, Cargo…). Alternative : **`git subtree`**.

## 7.7 Fichiers `.gitattributes` *(ajout)*

Le fichier `.gitattributes` définit un comportement par type de fichier.

```gitattributes
# Normalise les fins de ligne
* text=auto eol=lf

# Fichier binaire
*.png binary

# Géré par Git LFS
*.psd filter=lfs diff=lfs merge=lfs -text

# Compté comme documentation par GitHub Linguist
docs/*.md linguist-documentation
```

## 7.8 Exemple de workflow

```bash
git config --global alias.st status          # alias
echo '#!/bin/sh' > .git/hooks/pre-commit     # hook
echo 'echo "Vérifications avant commit"' >> .git/hooks/pre-commit   # remplacez par votre linter (npm run lint, etc.)
chmod +x .git/hooks/pre-commit
git submodule add https://github.com/user/lib.git libs/lib    # sous-module
git commit -am "Ajoute le sous-module lib"
```

---

# 8. Workflows de collaboration

## 8.1 Workflow centralisé

Tout le monde travaille **directement sur une seule branche** (`main`). Courant dans les petites équipes ou en transition depuis SVN.

```text
[développeur] → pull → modifier → commit → push → [main]
```

```bash
git clone https://github.com/org/depot.git
cd depot
git pull --rebase
# ...modifications...
git add . && git commit -m "Corrige une faute de frappe"
git push origin main
```

| Avantages | Inconvénients |
| --- | --- |
| Très simple | Risque de conflits |
| Idéal pour petites équipes | Aucune isolation des fonctionnalités |

## 8.2 Workflow par branches de fonctionnalité (*GitHub flow*)

Chaque fonctionnalité ou correction est développée dans **une branche dédiée**, fusionnée dans `main` après **relecture**.

```text
main ──●────────●────────●──▶
        \      /  \      /
         feature/login   feature/signup
```

```bash
git switch main && git pull
git switch -c feature/navbar            # 1. branche
# ...modifications des fichiers...
git add . && git commit -m "Ajoute la barre de navigation"
git push -u origin feature/navbar       # 2. publier
# 3. ouvrir une pull request  → 4. relecture + CI → 5. fusion → 6. suppression de la branche
```

| Avantages | Inconvénients |
| --- | --- |
| Développement parallèle sûr | Un peu plus de discipline |
| Revue de code, historique propre | |

## 8.3 Gitflow

Modèle de branches **structuré**, adapté aux produits à **versions livrées** (logiciels installés, cycles de release planifiés).

```text
main        ●───────────────●──────────────●   (versions étiquetées)
             \             / \            /
develop       ●──●──●──●──●───●──●──●────●
                  \    /      \      /
              feature/*     release/*  hotfix/* (depuis main)
```

| Branche | Rôle |
| --- | --- |
| `main` | Code stable en production |
| `develop` | Intégration des fonctionnalités |
| `feature/*` | Nouvelles fonctionnalités (depuis `develop`) |
| `release/*` | Stabilisation avant livraison |
| `hotfix/*` | Correctifs urgents sur la production (depuis `main`) |

```bash
git switch -c develop main
git switch -c feature/paiement develop
# ...développement et commits sur la fonctionnalité...
# fin de fonctionnalité
git switch develop && git merge --no-ff feature/paiement
# préparer une release
git switch -c release/1.0 develop
```

> **Attention** : L'auteur même du modèle recommande de **ne pas l'utiliser** pour les applications web livrées en continu : préférez GitHub flow ou le trunk-based development.

## 8.4 Workflow par fork

Standard du **logiciel libre** : le contributeur n'a pas les droits en écriture sur le dépôt principal.

```text
dépôt d'origine → fork → clone → branche → push → pull request → revue → fusion
```

Voir [4.5](#45-forks-et-pull-requests) pour les commandes (remote `upstream`, synchronisation, PR).

## 8.5 Développement sur tronc commun (*trunk-based*) *(ajout)*

Tous les développeurs intègrent **très fréquemment** (au moins une fois par jour) dans `main`, via des branches **très courtes** ou directement. Les fonctionnalités inachevées sont masquées par des **drapeaux de fonctionnalité** (*feature flags*). Ce modèle s'appuie fortement sur la **CI/CD** et les tests automatisés ; il est utilisé par de nombreuses grandes équipes.

## 8.6 Comparaison

| Workflow | Idéal pour | Avantages | Inconvénients |
| --- | --- | --- | --- |
| Centralisé | Petites équipes | Simplicité | Pas d'isolation, conflits |
| Branches de fonctionnalité | Équipes de toute taille | Structure claire, revues | Un peu plus complexe |
| Gitflow | Releases planifiées | Rôles de branches clairs | Lourd, excessif pour le web |
| Fork | Open source | Contributions découplées | Synchronisation à gérer |
| Trunk-based | Livraison continue | Intégration rapide, peu de branches longues | Exige CI solide et feature flags |

## 8.7 Bonnes pratiques de collaboration *(ajout)*

- **Petites PR**, ciblées, avec une description claire (*quoi* et *pourquoi*).
- Protégez `main` (**branch protection / rulesets**) : revue obligatoire, CI verte, pas de *force push*.
- Un **`CONTRIBUTING.md`** et un fichier **`CODEOWNERS`** précisent les règles et les relecteurs.
- Mettez à jour votre branche (`git pull --rebase` ou `git merge main`) avant la revue.
- Supprimez les branches fusionnées.

---

# 9. Outils et astuces

## 9.1 Qui a modifié cette ligne ? (`git blame`)

```bash
git blame app.js
git blame -L 10,20 app.js        # lignes 10 à 20 seulement
git blame -w -C app.js           # ignore les espaces ; suit le code déplacé/copié
```

```text
f0a1234 (Alice 2026-09-01) const server = http.createServer();
c9b4567 (Bob   2026-09-05) server.listen(3000);
```

Pour ignorer des commits de reformatage massif : `git blame --ignore-revs-file .git-blame-ignore-revs`.

## 9.2 Trouver le commit fautif (`git bisect`)

Recherche **dichotomique** du commit qui a introduit un bug.

```bash
git bisect start
git bisect bad                    # le commit actuel est mauvais
git bisect good v1.0              # un commit antérieur connu comme bon
# Git extrait un commit au milieu : testez, puis répondez
git bisect good                   # ou : git bisect bad
# ...répétez jusqu'à identification du commit fautif
git bisect reset                  # revenir à l'état initial
```

### Automatiser *(ajout)*

```bash
git bisect start HEAD v1.0
git bisect run pytest tests/test_bug.py    # le code de sortie décide : 0 = bon, ≠ 0 = mauvais
```

## 9.3 Retrouver des commits perdus (`git reflog`)

Le **reflog** journalise tous les déplacements de `HEAD` et des branches **en local** (conservé environ 90 jours par défaut). Il sauve de nombreuses erreurs : `reset --hard`, rebase raté, branche supprimée…

```bash
git reflog
```

```text
fe3a5d4 HEAD@{0}: reset: moving to HEAD~1
c34ab91 HEAD@{1}: commit: Ajoute la fonctionnalité
```

```bash
git switch -c recuperation c34ab91     # recréer une branche sur le commit perdu
git reset --hard c34ab91               # ou revenir directement dessus
```

### Exemple : se remettre d'un mauvais `reset`

```bash
git reset --hard HEAD~1     # un commit perdu
git reflog                  # retrouver son hash
git reset --hard c34ab91    # restauré
```

## 9.4 Patches (`git format-patch`, `git apply`, `git am`)

```bash
git format-patch -1 HEAD            # crée un fichier 0001-....patch pour le dernier commit
git format-patch main..feature      # un fichier .patch par commit
git format-patch -1 HEAD --stdout > changements.patch   # un seul fichier, nom choisi
git apply changements.patch         # applique les modifications (sans commit)
git am changements.patch            # ou : applique en recréant le commit (auteur conservé)
```

Utile pour envoyer des changements par e-mail ou hors plateforme.

## 9.5 Fichiers volumineux avec Git LFS

**Problème** : Git gère mal les gros fichiers binaires (images, vidéos, jeux de données) : le dépôt devient énorme.
**Solution** : **Git LFS** (*Large File Storage*) remplace ces fichiers par de petits **pointeurs** et stocke le contenu à part.

```bash
git lfs install                  # une seule fois par machine
git lfs track "*.psd"            # écrit dans .gitattributes
git add .gitattributes
git add design.psd
git commit -m "Ajoute le fichier PSD via LFS"
git lfs ls-files                 # fichiers gérés par LFS
```

> **Attention** : Vérifiez les quotas de stockage de votre plateforme. Autre option : conserver les gros fichiers hors de Git (stockage objet, DVC pour les données ML).

## 9.6 Rechercher dans le code et l'historique *(ajout)*

```bash
git grep "TODO"                       # recherche dans les fichiers suivis
git grep -n "ma_fonction" v1.0        # dans une version donnée
git log -S"mot_de_passe" --oneline    # commits qui ajoutent ou retirent cette chaîne
git log -G"regex" --oneline           # idem avec une expression régulière
git log --follow -- chemin/fichier    # historique d'un fichier à travers les renommages
```

## 9.7 Grands dépôts et performances *(ajout)*

| Technique | Commande |
| --- | --- |
| Clone superficiel | `git clone --depth 1 <url>` |
| Clone partiel | `git clone --filter=blob:none <url>` |
| Extraction partielle | `git sparse-checkout set dossier/` |
| Maintenance automatique | `git maintenance start` |
| Compactage manuel | `git gc` |

## 9.8 Exemple : retrouver un bug avec bisect

```bash
git bisect start
git bisect bad                # le commit actuel contient le bug
git bisect good abc1234       # un commit où tout fonctionnait
git bisect good               # ... testez et répétez (good / bad)
git bisect reset
```

---

# 10. Interfaces graphiques, plateformes et CI/CD

## 10.1 Interfaces graphiques (GUI)

| Outil | Points forts | Plateformes |
| --- | --- | --- |
| **GitHub Desktop** | Simple, intégré à GitHub, idéal pour débuter | Windows, macOS |
| **Sourcetree** | Branches, stash, résolution de conflits | Windows, macOS |
| **GitKraken** | Interface soignée, graphe, intégrations | Windows, macOS, Linux |
| **Fork** | Rapide, outil de fusion visuel | Windows, macOS |
| **Git intégré à VS Code** | Commit, diff, branches, résolution de conflits | Toutes |
| **lazygit** | Interface en terminal, très efficace | Toutes |
| **JetBrains (IntelliJ, PyCharm…)** | Intégration Git complète | Toutes |

**VS Code** : panneau *Source Control* (`Ctrl+Shift+G`) pour indexer, valider, changer de branche ; conflits affichés avec *Accept Current / Incoming / Both*.

> **Astuce** : Même avec une interface graphique, **apprenez la ligne de commande** : elle donne un contrôle complet et reste indispensable sur les serveurs.

## 10.2 Plateformes d'hébergement

| Plateforme | Description | Fonctionnalités notables |
| --- | --- | --- |
| **GitHub** | La plus populaire (open source et privé) | PR, Issues, **GitHub Actions**, Discussions, Pages, Codespaces |
| **GitLab** | Plateforme DevOps complète, auto-hébergeable | CI/CD intégrée, Merge Requests, registre de conteneurs |
| **Bitbucket** | Intégré à l'écosystème Atlassian (Jira) | Pipelines, revue de code |
| **Azure DevOps** | Offre entreprise de Microsoft | Repos, Boards, Pipelines |
| **Gitea / Forgejo** | Légers, auto-hébergeables, libres | **Codeberg** est une instance publique de Forgejo |

## 10.3 Intégration continue (CI/CD)

La **CI/CD** exécute automatiquement tests et déploiements à chaque `push` ou *pull request*.

### Exemple : GitHub Actions

Fichier `.github/workflows/test.yml` :

```yaml
name: Tests
on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - name: Installer Python
        uses: actions/setup-python@v6
        with:
          python-version: "3.14"        # entre guillemets (3.10 sans guillemets serait lu comme 3.1)
      - name: Installer les dépendances
        run: pip install -r requirements.txt pytest
      - name: Lancer les tests
        run: pytest
```

GitHub exécute ce workflow à chaque `push` sur `main` et à chaque PR.

> **Astuce** : Vérifiez régulièrement la **dernière version majeure** des actions (`checkout`, `setup-*`) ; les anciennes finissent par être dépréciées. Pour plus de sécurité, **épinglez** les actions tierces sur un **hash de commit**.
> GitLab CI (`.gitlab-ci.yml`), Bitbucket Pipelines et Azure Pipelines offrent des mécanismes équivalents.

## 10.4 Héberger un site statique avec GitHub Pages

1. Poussez votre site (HTML/CSS/JS) dans votre dépôt.
2. *Settings → Pages* : choisissez la **source** :
   - **Déployer depuis une branche** (`main` ou `gh-pages`, dossier `/` ou `/docs`), ou
   - **GitHub Actions** (pour générer le site avec Jekyll, Hugo, Vite, etc.).
3. Le site est publié à l'adresse `https://utilisateur.github.io/nom-du-depot`.

GitLab Pages, Cloudflare Pages ou Netlify proposent des services comparables.

---

# 11. Sécurité et bonnes pratiques

*(Section ajoutée : ces sujets manquaient dans le guide d'origine.)*

## 11.1 Signer ses commits

La signature prouve qu'un commit provient bien de vous (badge **« Verified »** sur GitHub). Depuis Git 2.34, **vos clés SSH peuvent signer** : plus besoin de GPG.

```bash
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true      # signer tous les commits
git config --global tag.gpgsign true
```

Ajoutez ensuite la même clé publique dans GitHub comme **« Signing key »**.

## 11.2 Ne jamais committer de secrets

Mots de passe, jetons d'API, clés privées, fichiers `.env` : **à ne jamais versionner**.

- Placez-les dans `.gitignore` et utilisez des variables d'environnement ou un gestionnaire de secrets.
- Activez les analyses de secrets (GitHub *secret scanning* et *push protection*) ou des outils comme **gitleaks** / **trufflehog**, idéalement dans un hook `pre-commit`.

### Si un secret a été poussé

1. **Révoquez-le / changez-le immédiatement** : il doit être considéré comme compromis.
2. Supprimez-le de l'historique avec **`git filter-repo`** (successeur recommandé de `git filter-branch`, déprécié) ou **BFG Repo-Cleaner**.
3. Forcez l'envoi et demandez à vos collègues de recloner.

```bash
pip install git-filter-repo
git filter-repo --path secrets.env --invert-paths
git remote add origin <url>     # git filter-repo retire le remote par sécurité
git push --force --all
git push --force --tags
```

## 11.3 Bonnes pratiques générales

| Pratique | Pourquoi |
| --- | --- |
| Commits **petits et atomiques** | Faciles à relire, à annuler, à bisecter |
| Messages **clairs** (*pourquoi*, pas seulement *quoi*) | Historique exploitable |
| `git status` / `git diff --staged` **avant chaque commit** | Éviter d'inclure des fichiers par erreur |
| **Tirer** (`pull`) avant de pousser | Moins de conflits |
| Ne pas réécrire l'historique partagé | Évite de casser le travail des autres |
| Utiliser `--force-with-lease` plutôt que `--force` | Sécurité |
| Un `.gitignore` dès le début du projet | Dépôt propre |
| Protéger `main` et exiger des revues | Qualité |
| Sauvegarder : un dépôt distant **est** une sauvegarde | Résilience |

## 11.4 Problèmes courants

| Symptôme | Cause / solution |
| --- | --- |
| `fatal: not a git repository` | Vous n'êtes pas dans un dépôt : `cd` ou `git init` |
| `rejected … non-fast-forward` | Le distant a avancé : `git pull --rebase` puis `git push` |
| `Permission denied (publickey)` | Clé SSH non enregistrée / non chargée dans `ssh-agent` |
| `Your local changes would be overwritten` | Validez, mettez de côté (`git stash`) ou annulez vos changements |
| `detached HEAD` | `git switch -c nouvelle-branche` pour conserver votre travail |
| Fichier ajouté au `.gitignore` toujours suivi | `git rm --cached <fichier>` |
| Mauvais auteur dans les commits | `git config user.name` et `git config user.email`, puis `git commit --amend --reset-author` |

---

# 12. Aide-mémoire

## 12.1 Commandes essentielles

| Besoin | Commande |
| --- | --- |
| Initialiser / cloner | `git init` · `git clone <url>` |
| État | `git status -s` |
| Indexer | `git add <fichier>` · `git add -p` |
| Valider | `git commit -m "message"` |
| Historique | `git log --oneline --graph --all` |
| Différences | `git diff` · `git diff --staged` |
| Nouvelle branche | `git switch -c <nom>` |
| Changer de branche | `git switch <nom>` |
| Fusionner | `git merge <branche>` |
| Rebaser | `git rebase <base>` |
| Récupérer | `git fetch` · `git pull --rebase` |
| Envoyer | `git push` · `git push -u origin <branche>` |
| Désindexer | `git restore --staged <fichier>` |
| Annuler des changements | `git restore <fichier>` |
| Annuler un commit publié | `git revert <hash>` |
| Mettre de côté | `git stash` · `git stash pop` |
| Étiqueter | `git tag -a v1.0 -m "message"` |
| Retrouver du perdu | `git reflog` |
| Trouver un bug | `git bisect` |

## 12.2 Nouveautés à connaître

| Version | Apport notable |
| --- | --- |
| 2.23 | `git switch` et `git restore` |
| 2.34 | Signature des commits avec des clés SSH |
| 2.37+ | `push.autoSetupRemote` |
| 2.54 – 2.55 | Hooks configurables et exécutés en parallèle, commande `git history` (réécriture simplifiée de l'historique) |
| **Git 3.0** *(à venir)* | Branche par défaut `main`, SHA-256 par défaut, format de références `reftable`, Rust requis |

> **À noter** : Vérifiez les détails exacts dans les notes de version sur [git-scm.com](https://git-scm.com/) (dernière version stable au moment de la rédaction : **2.55**).

## 12.3 Ressources

- Livre officiel gratuit **Pro Git** (en français) : <https://git-scm.com/book/fr/v2>
- Documentation de référence : <https://git-scm.com/docs>
- Apprendre en jouant : <https://learngitbranching.js.org/?locale=fr_FR>
- Modèles `.gitignore` : <https://github.com/github/gitignore>
- Conventional Commits : <https://www.conventionalcommits.org/fr>

---

<div align="center">

*Bon versionnement !*

</div>
