# 🎴 Projet Flashcards – SQLite + Python

Le but de ce projet est de construire une application de flashcards. Ce type d’application permet à
l’utilisateur de créer des cartes mentales, avec une information ou question par carte, et d’essayer
de répondre à la question ou d’expliquer le concept. La subtilité est que, l’apparition des cartes
dépend de si vous arrivez à avoir la bonne réponse. Plus serez à l’aise avec un concept, moins la
carte apparaitra, et au contraire, plus vous avez du mal avec un concept, et plus la carte apparaitra
fréquemment.

## 📌 Remarques
Ce projet est en cours de développement. Le README sera mis à jour régulièrement.

---

## 🚀 Fonctionnalités
- Création automatique des tables (`themes`, `stats`, `cards`)

---

## 🛠️ Installation

### Prérequis

- Python 3.13 (géré via [pyenv](https://github.com/pyenv/pyenv))
- [Poetry](https://python-poetry.org/)

### Étapes

```bash
# 1. Installer la version Python si elle n’est pas encore disponible
pyenv install 3.13.5

# 2. (Facultatif) Vérifier que .python-version est bien pris en compte
pyenv local

# 3. Installer les dépendances avec Poetry
poetry install

# 4. Démarrer le programme dans l’environnement virtuel
poetry run python main.py