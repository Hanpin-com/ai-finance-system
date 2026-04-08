# AI Finance System

## Overview
AI Finance System is a personal finance web application built with Flask and SQLite.

The goal of this project is to demonstrate backend development, database design, and full-stack application flow for internship and job opportunities.

This project is currently in progress and will be extended with analytics and AI-based finance insights.

## Features

### Current Features
- User onboarding flow
- Add income and expense records
- Dashboard overview
- Monthly report page
- SQLite-based data storage
- Flask backend routing and logic

### Planned Features (Future)
- Spending analytics
- Category insights
- Trend visualization
- AI-based financial recommendations

## System Architecture

### Frontend
- HTML templates (onboarding, dashboard, add expense, report)
- CSS for styling

### Backend
- Flask (Python)
- Handles routing, logic, and request processing

### Database
- SQLite
- Initialized via `init_db.py`

### Application Flow
User → Form Input → Flask Route → SQLite → Dashboard / Report Rendering

## Tech Stack

- Python (Flask)
- SQLite
- HTML / CSS

## Project Structure
```ai-finance-system/
│
├── app.py # Main Flask application
├── init_db.py # Database initialization script
├── finance.db # SQLite database
├── requirements.txt # Dependencies
│
├── templates/ # HTML templates
│ ├── onboarding.html
│ ├── dashboard.html
│ ├── add_expense.html
│ ├── report.html
│
├── static/
│ └── style.css # Stylesheet
```

## Getting Started

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

---

# 🧩 7️⃣ Demo Flow

```markdown
## Demo Flow

1. User completes onboarding  
2. User adds income or expense  
3. Data is stored in SQLite database  
4. Dashboard displays summary  
5. Report page shows financial overview  

## Project Purpose

This project is not intended for monetization.

It is designed as a portfolio project to demonstrate:
- Backend development (Flask)
- Database design (SQLite)
- Full-stack application flow
- Practical problem-solving

## Current Status

🚧 In Progress

The core structure and main pages are implemented.

Currently improving:
- Data flow between pages
- UI/UX consistency
- Project documentation

## Future Improvements

- Add data analytics features  
- Introduce machine learning models for insights  
- Improve UI/UX design  
- Deploy to cloud platform  

## Author

Han-Pin Hung