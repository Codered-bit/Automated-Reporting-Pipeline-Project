import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="Automated Reporting Dashboard", layout="wide")

st.title("📊 Institutional Reporting Dashboard")
st.markdown("Automated KPI reports generated from SQL + Python pipeline")

# -------------------------
# LOAD DATA
# -------------------------
dept_kpi = pd.read_csv("outputs/department_kpi.csv")
risk_report = pd.read_csv("outputs/risk_report.csv")
trend_report = pd.read_csv("outputs/trend_report.csv")

# -------------------------
# KPI SUMMARY SECTION
# -------------------------
st.header("Department Performance Overview")

st.dataframe(dept_kpi)

col1, col2, col3 = st.columns(3)

col1.metric("Top Department Avg Grade", round(dept_kpi["avg_grade"].max(), 2))
col2.metric("Avg Attendance (All)", round(dept_kpi["avg_attendance"].mean(), 2))
col3.metric("Total Departments", dept_kpi["department"].nunique())

# -------------------------
# VISUAL 1: AVERAGE GRADE BY DEPARTMENT
# -------------------------
st.subheader("Average Grade by Department")

fig1, ax1 = plt.subplots()
sns.barplot(data=dept_kpi, x="department", y="avg_grade", ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)

# -------------------------
# VISUAL 2: RISK DISTRIBUTION
# -------------------------
st.subheader("Student Risk Distribution")

risk_summary = risk_report.groupby("risk_category")["total_students"].sum().reset_index()

fig2, ax2 = plt.subplots()
sns.barplot(data=risk_summary, x="risk_category", y="total_students", ax=ax2)
st.pyplot(fig2)

# -------------------------
# VISUAL 3: ATTENDANCE VS PERFORMANCE
# -------------------------
st.subheader("Attendance vs Performance Trend")

fig3, ax3 = plt.subplots()
sns.scatterplot(data=trend_report, x="avg_attendance", y="avg_grade", ax=ax3)
ax3.set_title("Department-level correlation")
st.pyplot(fig3)

# -------------------------
# FILTER SECTION
# -------------------------
st.header("Department Drilldown")

selected_dept = st.selectbox("Select Department", dept_kpi["department"].unique())

filtered = dept_kpi[dept_kpi["department"] == selected_dept]

st.write("Selected Department KPI")
st.dataframe(filtered)

st.metric("Avg Grade", round(filtered["avg_grade"].values[0], 2))
st.metric("Avg Attendance", round(filtered["avg_attendance"].values[0], 2))
st.metric("Total Students", int(filtered["total_students"].values[0]))
