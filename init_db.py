import sqlite3

def init_database():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    # User profile table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_profile (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        monthly_income REAL,
        fixed_expenses REAL,
        saving_status TEXT,
        main_goal TEXT,
        goal_amount REAL,
        goal_timeline TEXT,
        pain_point TEXT,
        overspend_category TEXT,
        advice_style TEXT
    )
    """)

    # Expenses table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        amount REAL,
        category TEXT,
        note TEXT
    )
    """)

    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    init_database()