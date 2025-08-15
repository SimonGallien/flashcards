import sqlite3
from datetime import datetime

DB_PATH = "flashcards.db"


########################################################################
################## Fonctions CRUD pour les flashcards ##################
########################################################################


def create_card(question, reponse, probabilite, id_theme):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            # Activer la vérification des clés étrangères (désactivée par défaut en SQLite)
            c.execute("PRAGMA foreign_keys = ON;")

            # Vérifier si la question existe déjà
            c.execute(
                "SELECT COUNT(*) FROM cards WHERE question = ?", (question,)
            )
            if c.fetchone()[0] > 0:
                print("\nCette carte existe déjà, insertion ignorée.")
                return

            c.execute(
                """
                INSERT INTO cards(question, reponse, probabilite, id_theme) VALUES
                (?, ?, ?, ?)
                """,
                (question, reponse, probabilite, id_theme),
            )
            print("\nCarte créé avec succès.")
    except sqlite3.Error as e:
        print(f"Une erreur s'est produite {e}")


def get_card(id):
    try:
        with sqlite3.connect("flashcards.db") as conn:
            c = conn.cursor()
            c.execute(
                """
                SELECT * FROM cards
                WHERE cardID = ?
                """,
                (id,),
            )
            card_select = c.fetchone()
            print("\nCarte récupérée avec succès en utilisant son id.")
            return card_select
    except sqlite3.Error as e:
        print(f"Une erreur s'est produite {e}")


def update_card(cardID, question, reponse, probabilite, id_theme):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Activer la vérification des clés étrangères (désactivée par défaut en SQLite)
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Vérifier si la question existe déjà
    cursor.execute("SELECT 1 FROM cards WHERE cardID = ?", (cardID,))
    if cursor.fetchone() is None:
        print("\nCette carte n'existe pas, mise à jour ignorée.")
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
    c.execute(
        "PRAGMA foreign_keys = ON;"
    )  # indispensable pour activer les clés étrangères
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


def get_all_themes():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        """
        SELECT * FROM themes
        """
    )
    all_themes = c.fetchall()
    conn.close()
    print("Tout les thèmes sont récupérés.")
    return all_themes


#####################################################################
################## Fonctions pour les statistiques ##################
#####################################################################


def update_stats(is_correct):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # Vérification de l'existence d'une entrée pour la date du jour
    today = datetime.now().strftime("%Y-%m-%d")
    c.execute(
        """
        SELECT statID, bonnes_reponses, mauvaises_reponses, date FROM stats
        WHERE date = ?
        """,
        (today,),
    )
    stats = c.fetchone()

    if stats is not None:  # Si une date du jour existe
        statID = stats[0]
        bonnes_reponses = stats[1]
        mauvaises_reponses = stats[2]

        # MAJ les bonnes/mauvaises réponses
        if is_correct:
            bonnes_reponses += 1
        else:
            mauvaises_reponses += 1
        c.execute(
            """
            UPDATE stats
            SET bonnes_reponses = ?, mauvaises_reponses = ?
            WHERE statID = ?
            """,
            (bonnes_reponses, mauvaises_reponses, statID),
        )

    else:  # Si une date du jour n'existe pas
        bonnes_reponses = 1 if is_correct else 0
        mauvaises_reponses = 0 if is_correct else 1

        c.execute(
            """
            INSERT INTO stats (bonnes_reponses, mauvaises_reponses, date)
            VALUES (?, ?, ?)
            """,
            (bonnes_reponses, mauvaises_reponses, today),
        )

    conn.commit()
    conn.close()


def update_card_probability(cardID, is_correct):
    try:
        # Connexion à la BDD
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            # Récupère la probabilité actuelle
            c.execute(
                """
                SELECT probabilite FROM cards
                WHERE cardID = ?
                """,
                (cardID,),
            )
            resultat = c.fetchone()
            # Test si la carte existe
            if resultat is None:
                print(
                    f"La carte avec l'ID {cardID} n'existe pas, opération annulée."
                )
                return
            probabilite = resultat[0]
            # Calcul de la nouvelle probabilité
            if is_correct:
                nouvelle_probabilite = max(0.1, min(probabilite * 0.9, 1.0))
            else:
                nouvelle_probabilite = max(0.1, min(probabilite * 1.1, 1.0))
            # Mise à jour de la nouvelle probabilité dans la BDD
            c.execute(
                """
                UPDATE cards
                SET probabilite = ?
                WHERE cardID = ?
                """,
                (nouvelle_probabilite, cardID),
            )
            print("Probabilité de la carte mise à jour avec succès.")
    except sqlite3.Error as e:
        print(f"Une erreur s'est produite {e}")


def get_stats():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        """
        SELECT * FROM stats
        """
    )
    stats = c.fetchall()
    conn.close()
    return stats
