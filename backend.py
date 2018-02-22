import sqlite3
import random


def draw():
    conn = sqlite3.connect('lista_dan.db')
    cur = conn.cursor()
    cur.execute('SELECT COUNT (*) FROM dania')
    rows_amount = cur.fetchall()
    x = rows_amount[0][0]
    random_id = random.randint(1, x)
    cur.execute("SELECT * FROM dania WHERE id=?", (random_id,))
    row = cur.fetchall()
    conn.close()
    return row

def connect():
    conn = sqlite3.connect('lista_dan.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS dania (id INTEGER PRIMARY KEY, danie TEXT)")
    conn.commit()
    conn.close()


def all():
    conn = sqlite3.connect('lista_dan.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM dania ORDER BY danie")
    rows = cur.fetchall()
    conn.close()
    return rows


def insert(danie):
    conn = sqlite3.connect('lista_dan.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO dania VALUES (NULL,?)", (danie,))
    conn.commit()
    conn.close()


def delete(id):
    conn = sqlite3.connect('lista_dan.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM dania WHERE id=?", (id,))
    conn.commit()
    conn.close()

connect()