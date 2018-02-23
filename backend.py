import sqlite3
import random

class Database:

    def __init__(self):
        self.conn = sqlite3.connect('lista_dan.db')
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS dania (id INTEGER PRIMARY KEY, danie TEXT)")
        self.conn.commit()

    def draw(self):
        self.cur.execute('SELECT COUNT (*) FROM dania')
        rows_amount = self.cur.fetchall()
        x = rows_amount[0][0]
        random_id = random.randint(1, x)
        self.cur.execute("SELECT * FROM dania WHERE id=?", (random_id,))
        row = self.cur.fetchall()
        return row

    def all(self):
        self.cur.execute("SELECT * FROM dania ORDER BY danie")
        rows = self.cur.fetchall()
        return rows

    def insert(self, danie):
        self.cur.execute("INSERT INTO dania VALUES (NULL,?)", (danie,))
        self.conn.commit()

    def delete(self, id):
        self.cur.execute("DELETE FROM dania WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

#connect()