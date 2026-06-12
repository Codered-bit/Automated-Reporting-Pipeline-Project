Automated Reporting Pipeline (SQL + Python + Streamlit)

## 🧠 Overview

This project simulates a real institutional reporting system used in education or registry environments. It demonstrates how raw student data can be transformed into automated KPI reports using SQL, Python, and visualised through a Streamlit dashboard.

The pipeline covers:

- Data ingestion

- SQL-based analytics

- Automated reporting generation

- Interactive dashboard deployment

---

## 🎯 Objectives

- Build a relational dataset using SQLite

- Run SQL queries to generate institutional KPIs

- Automate report generation using Python

- Export structured datasets for reporting

- Visualise insights in a Streamlit dashboard

---

## 🏗️ Architecture

CSV Dataset → SQLite Database → SQL Queries → Python Automation → CSV Reports → Streamlit Dashboard

---

## 📁 Project Structure

automated-reporting-pipeline/
│
├── data/
│   └── students_raw.csv
│
├── database/
│   └── setup.sql
│
├── scripts/
│   ├── load_data.py
│   ├── generate_report.py
│
├── outputs/
│   ├── department_kpi.csv
│   ├── risk_report.csv
│   ├── trend_report.csv
│
├── app.py
├── requirements.txt
└── README.md

---

## 📊 Key Metrics Generated

### 1. Department KPI Summary
- Total students per department
- Average attendance rate
- Average academic performance

### 2. Risk Segmentation
- High Risk: final grade < 50
- Medium Risk: 50–65
- Low Risk: > 65

### 3. Performance Trends
- Attendance vs grade comparison at department level

---

## ⚙️ Technologies Used

- Python (Pandas, SQLite3)
- SQL (Aggregation, CASE statements, GROUP BY)
- Streamlit (Dashboard UI)
- Matplotlib / Seaborn (Visualisation)

---

## 🚀 How to Run the Project

### 1. Clone repository
```bash
git clone https://github.com/yourusername/automated-reporting-pipeline.git
cd automated-reporting-pipeline

Install dependencies > pip install -r requirements.txt
Load Database > python scripts/load_data.py
Report > python scripts/generate_report.py
Dashboard > streamlit run app.py

Key Insights

* Departments show variation in average academic performance
* Attendance is positively correlated with final grade
* Risk segmentation identifies at-risk student groups for intervention
* Automated reporting reduces manual KPI generation effort

⸻

💡 Business Value

This system simulates an institutional reporting pipeline that can be used by:

* Higher education registry teams
* Academic performance analysts
* Institutional research departments

It reduces manual reporting effort while improving consistency and accuracy of KPI reporting.

⸻

What I Aim to Demonstrate with this Project

* SQL data aggregation and transformation
* Python automation for reporting workflows
* Data pipeline design thinking
* KPI definition and institutional reporting logic
* Dashboard development using Streamlit

⸻

 My Future Improvements (suggeations are welcome)

* Integration with PostgreSQL for scalable storage
* Scheduled automation using cron or Airflow
* Role-based dashboard access
* Real-time data ingestion pipeline
