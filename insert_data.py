import sqlite3


def insert_data():
    # Créer une connexion à la base de données
    conn = sqlite3.connect("flashcards.db")
    cursor = conn.cursor()

    print("Connexion à la base de données réussie")

    # Insérer les thèmes si la table est vide
    cursor.execute("SELECT COUNT(*) FROM themes")
    if cursor.fetchone()[0] == 0:
        cursor.execute(
            """
            INSERT INTO themes (themeID, theme) VALUES
            (1, 'Python'),
            (2, 'SQLite'),
            (3, 'Git/Github'),
            (4, 'DataViz'),
            (5, 'EDA'),
            (6, 'ML Supervisé'),
            (7, 'ML Non Supervisé'),
            (8, 'Evaluations des modèles de ML'),
            (9, 'Optimisation des modèles de ML'),
            (10, 'Statistiques & Probabilités'),
            (11, 'Maths appliquées au ML'),
            (12, 'Outils & Workflow')
        """
        )
        print("Thèmes insérés avec succès.")
    else:
        print("Les thèmes existent déjà, aucune insertion effectuée.")

    conn.commit()
    conn.close()
    print("Connexion à la base de données fermée")
