import sqlite3

DB_NAME = "notes.db"

def connect():
    return sqlite3.connect(DB_NAME)

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
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fixed_dates (
        date TEXT PRIMARY KEY
    )
    """)

    conn.commit()
    conn.close()

def add_note(content, date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (content, date) VALUES (?, ?)", (content, date))
    conn.commit()
    conn.close()

def get_notes_by_date(date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id, content FROM notes WHERE date = ?", (date,))
    notes = cursor.fetchall()
    conn.close()
    return notes

def update_note(note_id, new_content):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE notes SET content = ? WHERE id = ?", (new_content, note_id))
    conn.commit()
    conn.close()

def delete_note(note_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()
