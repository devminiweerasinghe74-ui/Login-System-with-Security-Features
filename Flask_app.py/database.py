import sqlite3

def connect_db():
    conn = sqlite3.connect("users.db")
    return conn


def create_table():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        locked INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()