import sqlite3

DB_NAME = "notes.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = connect()
    cursor = conn.cursor()
    
    # Create the notes table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL,
        date TEXT NOT NULL
    )
    """)

    # Create the fixed_dates table to track fixed dates
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
    cursor.execute("SELECT * FROM notes WHERE date = ?", (date,))
    notes = cursor.fetchall()
    conn.close()
    return notes

# Check if a date is fixed
def check_if_fixed(date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM fixed_dates WHERE date = ?", (date,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

# Add a date to the fixed dates table
def add_fixed(date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO fixed_dates (date) VALUES (?)", (date,))
    conn.commit()
    conn.close()

# Remove a date from the fixed dates table
def remove_fixed(date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM fixed_dates WHERE date = ?", (date,))
    conn.commit()
    conn.close()
