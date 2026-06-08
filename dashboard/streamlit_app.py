import pandas as pd
import streamlit as st
from pathlib import Path

# Page Configuration
st.set_page_config(
    page_title="Trust & Safety Abuse Detection Dashboard",
    layout="wide"
)

# File Paths
CLASSIFIED_PATH = Path("data/outputs/classified_comments.csv")
SUMMARY_PATH = Path("data/outputs/moderation_summary.csv")
ABUSE_PATH = Path("data/outputs/abuse_distribution.csv")

# Load Data
df = pd.read_csv(CLASSIFIED_PATH)
summary = pd.read_csv(SUMMARY_PATH)
abuse_df = pd.read_csv(ABUSE_PATH)

# Dashboard Title
st.title("🛡️ Trust & Safety Abuse Detection Dashboard")
st.write(
    "LLM-inspired moderation pipeline for abuse detection, risk prioritization, and moderation analytics."
)

# Metrics
total_comments = len(df)
high_risk = (df["risk_priority"] == "high").sum()
medium_risk = (df["risk_priority"] == "medium").sum()
low_risk = (df["risk_priority"] == "low").sum()

# Sidebar
st.sidebar.header("Moderation Summary")
st.sidebar.metric("Total Comments", total_comments)
st.sidebar.metric("High Risk", high_risk)
st.sidebar.metric("Medium Risk", medium_risk)
st.sidebar.metric("Low Risk", low_risk)

# Main Metrics Row
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Comments", total_comments)
col2.metric("High Risk", high_risk)
col3.metric("Medium Risk", medium_risk)
col4.metric("Low Risk", low_risk)

# Risk Distribution
st.subheader("Risk Priority Distribution")
st.bar_chart(summary.set_index("risk_priority"))

# Abuse Category Distribution
abuse_chart = abuse_df[abuse_df["abuse_type"] != "clean"]

st.subheader("Abuse Category Distribution")
st.bar_chart(abuse_chart.set_index("abuse_type"))

# Sample Results
st.subheader("Sample Moderation Results")
st.dataframe(df.head(100), use_container_width=True)

# High Risk Content Review
high_risk_df = df[df["risk_priority"] == "high"]

st.subheader("High-Risk Content Review")
st.dataframe(high_risk_df.head(20), use_container_width=True)