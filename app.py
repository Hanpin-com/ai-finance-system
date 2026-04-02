from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)
DATABASE = "finance.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    conn = get_db_connection()

    profile = conn.execute("SELECT * FROM user_profile ORDER BY id DESC LIMIT 1").fetchone()

    expenses = conn.execute("""
        SELECT * FROM expenses
        ORDER BY date DESC, id DESC
        LIMIT 5
    """).fetchall()

    total_spending = conn.execute("""
        SELECT COALESCE(SUM(amount), 0) AS total
        FROM expenses
    """).fetchone()["total"]

    # Weekly spending
    seven_days_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    weekly_total = conn.execute("""
        SELECT COALESCE(SUM(amount), 0) AS total
        FROM expenses
        WHERE date >= ?
    """, (seven_days_ago,)).fetchone()["total"]

    # Top category
    top_category_row = conn.execute("""
        SELECT category, SUM(amount) as total
        FROM expenses
        GROUP BY category
        ORDER BY total DESC
        LIMIT 1
    """).fetchone()

    top_category = top_category_row["category"] if top_category_row else "No data"

    conn.close()

    return render_template(
        "dashboard.html",
        profile=profile,
        expenses=expenses,
        total_spending=total_spending,
        weekly_total=weekly_total,
        top_category=top_category
    )


@app.route("/onboarding", methods=["GET", "POST"])
def onboarding():
    if request.method == "POST":
        monthly_income = request.form["monthly_income"]
        fixed_expenses = request.form["fixed_expenses"]
        saving_status = request.form["saving_status"]
        main_goal = request.form["main_goal"]
        goal_amount = request.form["goal_amount"]
        goal_timeline = request.form["goal_timeline"]
        pain_point = request.form["pain_point"]
        overspend_category = request.form["overspend_category"]
        advice_style = request.form["advice_style"]

        conn = get_db_connection()
        conn.execute("""
            INSERT INTO user_profile (
                monthly_income,
                fixed_expenses,
                saving_status,
                main_goal,
                goal_amount,
                goal_timeline,
                pain_point,
                overspend_category,
                advice_style
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            monthly_income,
            fixed_expenses,
            saving_status,
            main_goal,
            goal_amount,
            goal_timeline,
            pain_point,
            overspend_category,
            advice_style
        ))
        conn.commit()
        conn.close()

        return redirect(url_for("home"))

    return render_template("onboarding.html")


@app.route("/add-expense", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        date = request.form["date"]
        amount = request.form["amount"]
        category = request.form["category"]
        note = request.form["note"]

        conn = get_db_connection()
        conn.execute("""
            INSERT INTO expenses (date, amount, category, note)
            VALUES (?, ?, ?, ?)
        """, (date, amount, category, note))
        conn.commit()
        conn.close()

        return redirect(url_for("home"))

    return render_template("add_expense.html")


@app.route("/report")
def report():
    conn = get_db_connection()

    profile = conn.execute("SELECT * FROM user_profile ORDER BY id DESC LIMIT 1").fetchone()

    seven_days_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

    weekly_expenses = conn.execute("""
        SELECT * FROM expenses
        WHERE date >= ?
        ORDER BY date DESC, id DESC
    """, (seven_days_ago,)).fetchall()

    category_totals = conn.execute("""
        SELECT category, SUM(amount) AS total
        FROM expenses
        WHERE date >= ?
        GROUP BY category
        ORDER BY total DESC
    """, (seven_days_ago,)).fetchall()

    weekly_total = conn.execute("""
        SELECT COALESCE(SUM(amount), 0) AS total
        FROM expenses
        WHERE date >= ?
    """, (seven_days_ago,)).fetchone()["total"]

    top_category = category_totals[0]["category"] if category_totals else "No data"

    # Temporary rule-based analysis (before AI API integration)
    if profile:
        analysis = (
            f"Your main financial goal is '{profile['main_goal']}'. "
            f"In the past 7 days, you spent ${weekly_total:.2f}. "
            f"Your highest spending category was '{top_category}'. "
        )

        if profile["overspend_category"] == top_category:
            analysis += (
                f"This matches the category you identified as hardest to control. "
                f"Try reducing spending in '{top_category}' next week to better support your goal."
            )
        else:
            analysis += (
                f"Your top category this week was different from your expected weak area. "
                f"This may be a good sign, but you should still review your spending habits carefully."
            )
    else:
        analysis = "No profile found yet. Please complete onboarding first."

    conn.close()

    return render_template(
        "report.html",
        profile=profile,
        weekly_expenses=weekly_expenses,
        category_totals=category_totals,
        weekly_total=weekly_total,
        analysis=analysis
    )


if __name__ == "__main__":
    app.run(debug=True)