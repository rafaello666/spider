# spiderfoot/db.py

import sqlite3

class SpiderFootDb:
    """
    Zarządza bazą danych w SpiderFoot, umożliwia zapis wyników do SQLite.
    """

    def __init__(self, db_name="spiderfoot.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self._connect()

    def _connect(self):
        """Łączy się z bazą danych SQLite."""
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        """Tworzy tabelę, jeśli nie istnieje."""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS scan_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            target TEXT,
            result TEXT,
            timestamp TEXT
        )''')
        self.connection.commit()

    def insert_result(self, target, result, timestamp):
        """Wstawia wynik skanowania do bazy danych."""
        self.cursor.execute("INSERT INTO scan_results (target, result, timestamp) VALUES (?, ?, ?)",
                            (target, result, timestamp))
        self.connection.commit()

    def get_results(self):
        """Zwraca wszystkie wyniki skanowania z bazy danych."""
        self.cursor.execute("SELECT * FROM scan_results")
        return self.cursor.fetchall()

    def close(self):
        """Zamyka połączenie z bazą danych."""
        self.connection.close()
