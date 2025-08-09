import sqlite3

DB_PATH = "flashcards.db"


# Fonctions CRUD pour les Flashcards
def create_card(question, reponse, probabilite, id_theme):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Activer la vérification des clés étrangères (désactivée par défaut en SQLite)
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Vérifier si la question existe déjà
    cursor.execute(
        "SELECT COUNT(*) FROM cards WHERE question = ?", (question,)
    )
    if cursor.fetchone()[0] > 0:
        print("Cette carte existe déjà, insertion ignorée.")
        conn.close()
        return

    cursor.execute(
        """
        INSERT INTO cards(question, reponse, probabilite, id_theme) VALUES
        (?, ?, ?, ?)
        """,
        (question, reponse, probabilite, id_theme),
    )
    conn.commit()
    conn.close()


def get_card(id):
    conn = sqlite3.connect("flashcards.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM cards
        WHERE cardID = ?
        """,
        (id,),
    )
    card_select = cursor.fetchone()
    conn.close()
    return card_select


def update_card(cardID, question, reponse, probabilite, id_theme):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Activer la vérification des clés étrangères (désactivée par défaut en SQLite)
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Vérifier si la question existe déjà
    cursor.execute("SELECT 1 FROM cards WHERE cardID = ?", (cardID,))
    if cursor.fetchone() is None:
        print("Cette carte n'existe pas, mise à jour ignorée.")
        conn.close()
        return

    cursor.execute(
        """
        UPDATE cards
        SET question = ?, reponse = ?, probabilite = ?, id_theme = ?
        WHERE cardID = ?
        """,
        (question, reponse, probabilite, id_theme, cardID),
    )
    conn.commit()
    conn.close()
    print("Carte mise à jour avec succès.")
