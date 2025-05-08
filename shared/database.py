import sqlite3

DB_NAME = "shared/cupons.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Permite acessar os campos como dicionário
    return conn

def initialize_db():
    with get_db_connection() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS cupom (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL,
            discount REAL NOT NULL,
            type TEXT NOT NULL,
            expiration_date TEXT NOT NULL,
            usage_limit INTEGER NOT NULL
        )
        """)
        conn.commit()
