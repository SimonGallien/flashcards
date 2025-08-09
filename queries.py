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
