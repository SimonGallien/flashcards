import sqlite3

DB_PATH = "flashcards.db"


########################################################################
################## Fonctions CRUD pour les flashcards ##################
########################################################################


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


def delete_card(cardID):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM cards WHERE cardID = ?", (cardID,))
    if cursor.fetchone() is None:
        print("Cette carte n'existe pas, suppression ignorée.")
        conn.close()
        return
    cursor.execute(
        """
        DELETE FROM cards
        WHERE cardID = ?
        """,
        (cardID,),
    )
    conn.commit()
    conn.close()
    print("Carte supprimée avec succès.")


def get_all_cards():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cards")
    cards = cursor.fetchall()
    conn.close()
    print("Cartes récupérées avec succès.")
    return cards


def get_number_of_cards():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT COUNT(*) FROM cards
        """
    )
    number_of_cards = cursor.fetchone()[0]
    conn.close()
    print("Nombre de cartes récupéré avec succès.")
    return number_of_cards


def get_cards_by_theme(id_theme):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM cards
        WHERE id_theme = ?
        """,
        (id_theme,),
    )
    cards_by_theme = cursor.fetchall()
    conn.close()
    print("Cartes récupérées avec succès.")
    return cards_by_theme


####################################################################
################## Fonctions CRUD pour les thèmes ##################
####################################################################


def create_theme(theme):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO themes(theme)
        VALUES (?)
        """,
        (theme,),
    )
    conn.commit()
    conn.close()
    print("Thème ajouté avec succès.")


def get_theme(id_theme):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT theme
        FROM themes
        WHERE themeID = ?
        """,
        (id_theme,),
    )
    theme = cursor.fetchone()
    conn.close()
    if theme is None:
        print("Cette id_theme n'existe pas, requête ignorée.")
        return None
    print("Thème récupéré avec succès.")
    return theme[0]


def update_theme(themeID, theme):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Vérifier si le themeID existe déjà
    cursor.execute("SELECT 1 FROM themes WHERE themeID = ?", (themeID,))
    if cursor.fetchone() is None:
        print("Cet ID n'existe pas, mise à jour ignorée.")
        conn.close()
        return
    cursor.execute(
        """
        UPDATE themes
        SET theme = ?
        WHERE themeID = ?
        """,
        (theme, themeID),
    )
    conn.commit()
    conn.close()
    print("Mise à jour du thème effectuée.")


def delete_theme(id_theme):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # Check if id_theme exist
    c.execute("SELECT 1 FROM themes WHERE themeID = ?", (id_theme,))
    if c.fetchone() is None:
        print("Cet id de thème n'existe pas, suppression annumlée.")
        conn.close()
        return
    c.execute(
        """
        DELETE FROM themes
        WHERE themeID = ?
        """,
        (id_theme,),
    )
    conn.commit()
    conn.close()
    print("Suppression du thème réussi.")
