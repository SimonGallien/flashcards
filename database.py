import sqlite3


def init_db():
    # Créer une connexion à la base de données
    conn = sqlite3.connect("flashcards.db")

    # Créer un curseur pour exécuter les requêtes SQL
    cursor = conn.cursor()

    # Activer la vérification des contraintes FOREIGN KEY (désactivée par défaut en SQLite)
    cursor.execute("PRAGMA foreign_keys = ON;")

    print("Connexion à la base de données réussie")

    # Création des tables et insertion des thèmes par défaut
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS themes (
            themeID INTEGER PRIMARY KEY,
            theme TEXT
        );
        """
    )

    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS stats (
            statID INTEGER PRIMARY KEY,
            bonne_reponses INTEGER,
            mauvaise_reponses INTEGER,
            date DATE
        );
        """
    )

    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS cards (
            cardID INTEGER PRIMARY KEY,
            question TEXT,
            reponse TEXT,
            probabilite REAL,
            id_theme INTEGER, 
            FOREIGN KEY(id_theme) REFERENCES themes(themeID) ON DELETE RESTRICT
        );
        """
    )

    # Valider les modifications
    conn.commit()
    print("Tables créées avec succès")

    conn.close()
    print("Connexion à la base de données fermée")
