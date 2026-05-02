import sqlite3

DB_PATH = "bot.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id TEXT UNIQUE
    )
    """)

    conn.commit()
    conn.close()
