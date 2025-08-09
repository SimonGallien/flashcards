from database import init_db
from insert_data import insert_data
from queries import *

if __name__ == "__main__":
    init_db()
    insert_data()
    create_card(
        "A quoi sert PRAGMA foreign_keys en SQLite ?",
        "A activer la vérification des clés étrangères.",
        0.5,
        2,  # 2 = SQLite
    )
    create_card(
        "Quelle commande permet d'afficher toutes les tables d'une base SQLite ?",
        "SELECT name FROM sqlite_master WHERE type='table';",
        0.5,
        2,  # 2 = SQLite
    )
