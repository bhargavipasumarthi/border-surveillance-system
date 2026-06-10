import streamlit as st
import pandas as pd
import sqlite3
import os

st.title("🚨 Border Surveillance Command Center")

# Connect to database
try:
    conn = sqlite3.connect("events.db")

    df = pd.read_sql_query(
        "SELECT * FROM events",
        conn
    )

    conn.close()

    st.subheader("Event Log")
    st.dataframe(df)

    # Statistics
    total_intrusions = len(df)

    low_count = len(
        df[df["threat_level"] == "LOW"]
    )

    medium_count = len(
        df[df["threat_level"] == "MEDIUM"]
    )

    high_count = len(
        df[df["threat_level"] == "HIGH"]
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Intrusions",
            total_intrusions
        )

    with col2:
        st.metric(
            "LOW Threats",
            low_count
        )

    with col3:
        st.metric(
            "MEDIUM Threats",
            medium_count
        )

    with col4:
        st.metric(
            "HIGH Threats",
            high_count
        )

except Exception as e:
    st.error(f"Database Error: {e}")

# Evidence Images

st.subheader("📸 Latest Evidence")

if os.path.exists("evidence"):

    images = sorted(
        os.listdir("evidence"),
        reverse=True
    )

    for image in images[:10]:

        st.image(
            f"evidence/{image}",
            caption=image,
            use_container_width=True
        )