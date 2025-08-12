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
    card = get_card(1)
    if card:
        print(
            f"ID: {card[0]}\nQuestion: {card[1]}\nRéponse: {card[2]}\nProbabilité : {card[3]}\nID Thème : {card[4]}"
        )
    else:
        print("Carte introuvable.")

    update_card(
        3,  # cardID
        "Que fait la méthode .append() en Python ?",  # question
        "Elle ajoute un élément à la fin d'une liste.",  # réponse
        0.5,  # probabilité
        1,  # id_theme (Python)
    )

    # delete_card(1)

    allCards = get_all_cards()
    for card in allCards:
        print(
            f"cardID : {card[0]}\n  question : {card[1]}\n  réponse : {card[2]}\n  probabilité : {card[3]}\n  id_theme : {card[4]}\n"
        )

    number_of_cards = get_number_of_cards()
    print(f"Nombres de carte dans la base : {number_of_cards}")

    cards_by_theme = get_cards_by_theme(1)
    for card in cards_by_theme:
        print(card)

    # create_theme("PyTorch")

    theme = get_theme(6)
    print(f"Thème : {theme}")

    update_theme(25, "Keras")

    delete_theme(1)

    all_themes = get_all_themes()
    for theme in all_themes:
        print(theme)

    update_stats(True)
    update_stats(False)
    update_stats(True)
    update_stats(False)
