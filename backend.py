#Class that communicate with database in sqlite

import sqlite3
import random

class Database:

    def __init__(self):
        self.conn = sqlite3.connect('lista_dan.db')
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS dania (id INTEGER PRIMARY KEY, danie TEXT, skladniki TEXT)")
        self.conn.commit()

    def draw(self):
        self.cur.execute('SELECT MAX(id) FROM dania')
        rows_amount = self.cur.fetchall()
        x = rows_amount[0][0]
        if not x:
            return 'Baza pomysłów jest pusta'
        row = False
        while not row:
            random_id = random.randint(0, x)
            self.cur.execute("SELECT * FROM dania WHERE id=?", (random_id,))
            row = self.cur.fetchall()
        return row

    def all(self):
        self.cur.execute("SELECT * FROM dania ORDER BY danie")
        rows = self.cur.fetchall()
        if not rows:
            return ['Baza pomysłów jest pusta']
        return rows

    def show_ingredients(self, danie):
        self.cur.execute("SELECT skladniki FROM dania WHERE danie=?", (danie,))
        row = self.cur.fetchall()
        print(row)
        return row

    def insert(self, danie, skladniki):
        self.cur.execute("INSERT INTO dania VALUES (NULL,?,?)", (danie, skladniki))
        self.conn.commit()

    def delete(self, danie):
        self.cur.execute("DELETE FROM dania WHERE danie=?", (danie,))
        self.conn.commit()

    def check(self, danie):
        self.cur.execute("SELECT 1 WHERE EXISTS (SELECT danie FROM dania WHERE danie=?)", (danie,))
        result = self.cur.fetchone()
        print(result)
        return result

    def __del__(self):
        self.conn.close()
