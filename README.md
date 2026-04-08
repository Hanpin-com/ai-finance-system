# AI Finance System

## Overview
AI Finance System is a personal finance web application built with Flask and SQLite.

This project is designed as a portfolio project for internship and job applications. It demonstrates backend development, database design, routing, CRUD operations, and full-stack application flow.

The current version focuses on financial profile onboarding, expense tracking, dashboard summaries, category analysis, and weekly reporting.

---

## Current Features

- User onboarding flow
- Financial profile setup
- Add expense records
- View recent expenses
- Edit expense records
- Delete expense records
- Dashboard summary
- Category analysis
- Weekly report with rule-based financial analysis
- SQLite-based data storage
- Flask backend routing and logic

---

## CRUD Functionality

### Create
- Create a financial profile through onboarding
- Add new expense records

### Read
- View profile and expense summaries on the dashboard
- View weekly spending report
- View category totals and recent expenses

### Update
- Edit existing expense records

### Delete
- Delete expense records from the dashboard or report page

---

## System Architecture

### Frontend
- HTML templates:
  - `onboarding.html`
  - `dashboard.html`
  - `add_expense.html`
  - `edit_expense.html`
  - `report.html`
- CSS styling with `style.css`

### Backend
- Flask (Python)
- Handles routing, form submission, CRUD logic, and report generation

### Database
- SQLite
- Initialized through `init_db.py`

### Application Flow
User enters profile information → profile is stored in SQLite → user adds expenses → Flask processes requests → dashboard and report pages render updated financial data

---

## Tech Stack

- Python
- Flask
- SQLite
- HTML
- CSS

---

## Project Structure

```
ai-finance-system/
├── app.py
├── init_db.py
├── requirements.txt
├── finance.db
├── templates/
│   ├── onboarding.html
│   ├── dashboard.html
│   ├── add_expense.html
│   ├── edit_expense.html
│   └── report.html
└── static/
    └── style.css
```

## Getting Started

```mardown
### 1. Clone the repository

git clone https://github.com/Hanpin-com/ai-finance-system.git
cd ai-finance-system

### 2. Install dependencies
pip install -r requirements.txt

### 3. Initialize the database
python init_db.py

### 4. Run the application
python app.py

### 5. Open in browser
http://127.0.0.1:5000/
```

---

# 🧩 7️⃣ Demo Flow

```markdown
## Demo Flow

1. First-time user is redirected to onboarding
2. User saves financial profile
3. User accesses dashboard
4. User adds expenses
5. Dashboard updates summary and category analysis
6. User can edit or delete expense records
7. Weekly report shows recent spending and rule-based analysis 

## Project Purpose

This project is not intended for monetization.

It is built as a portfolio project to demonstrate:

- Flask backend development
- SQLite database design
- CRUD implementation
- financial data workflow
- practical web app architecture

## Current Status

🚧 In Progress

The current version includes:

onboarding flow
expense CRUD
dashboard UI
category analysis
weekly report

Next planned improvements:

login / logout / sign-up
better analytics and charts
stronger user-based data separation
future AI-based financial insights
deployment

## Future Improvements

- Add data analytics features  
- Introduce machine learning models for insights  
- Improve UI/UX design  
- Deploy to cloud platform  
```

## Author

Han-Pin Hung