import sqlite3

class Database:
    def __init__(self, db_name='high_scores.db'):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute(
                "CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY, score INTEGER)"
            )

    def insert_score(self, score):
        with self.connection:
            self.connection.execute(
                "INSERT INTO scores (score) VALUES (?)", (score,)
            )

    def get_high_scores(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT score FROM scores ORDER BY score DESC")
        return cursor.fetchall()
