import sqlite3

DB_NAME = "notes.db"


def connect():
    return sqlite3.connect(DB_NAME)

# Tabloları oluştur
def create_tables():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL,
        date TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

# Not ekle
def add_note(content, date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (content, date) VALUES (?, ?)", (content, date))
    conn.commit()
    conn.close()

# Notları al
def get_notes_by_date(date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes WHERE date = ?", (date,))
    notes = cursor.fetchall()
    conn.close()
    return notes
