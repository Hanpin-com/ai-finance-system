import sqlite3
import os

DATABASE = "finance.db"


def init_database(reset=False):
    if reset and os.path.exists(DATABASE):
        os.remove(DATABASE)
        print("Old database removed.")

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # -------------------------
    # User Profile Table
    # -------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_profile (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        monthly_income REAL NOT NULL,
        fixed_expenses REAL NOT NULL,
        saving_status TEXT,
        main_goal TEXT,
        goal_amount REAL,
        goal_timeline TEXT,
        pain_point TEXT,
        overspend_category TEXT,
        advice_style TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # -------------------------
    # Expenses Table
    # -------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        note TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

    print("Database initialized successfully.")


if __name__ == "__main__":
    init_database(reset=True)