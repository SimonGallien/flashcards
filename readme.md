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

- Initialisation automatique de la base SQLite
- Création des tables : `themes`, `stats`, `cards`
- Activation des contraintes `FOREIGN KEY` (SQLite)
- Insertion des **thèmes par défaut** :
  - Python
  - SQLite
  - Git/GitHub
  - Data visualisation
  - EDA
  - ML supervisé
  - ML non supervisé
  - Évaluation des modèles
  - Optimisation des modèles
  - Statistiques & probabilités
  - Maths appliquées au ML
  - Outils & workflow
- CRUD pour les cartes :
  - `create_card()` → ajouter une carte
  - `get_card()` → récupérer une carte par ID
  
---

### 📌 À venir

- **CRUD complet pour les cartes** :
  - `update_card()` → modifier une carte existante
  - `delete_card()` → supprimer une carte
  - `get_all_cards()` → lister toutes les cartes
  - `get_number_of_cards()` → obtenir le nombre total de cartes
  - `get_cards_by_theme()` → filtrer par thème
- **CRUD complet pour les thèmes** :
  -`create_theme(theme)` → créer un thème
  -`get_theme(id_theme)` → récupérer un thème
  -`update_theme(id_theme, theme)` → modifier un theme existant
  -`delete_theme(id_theme)` → supprimer un thème
  -`get_all_themes()` → récupérer tous les thèmes
- **CRUD complet pour les statistiques** :
  -`update_stats(is_correct)` → mettre à jour la base stats suivant les indications ci-dessous
  -`update_card_probability(cardID, is_correct)` → mettre à jour la probabilité d'apparition d'une carte
  -`get_stats()` → récupérer les statistiques au travers du temps
- **Interface graphique** :
  -`Interface graphique avec streamlit`

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