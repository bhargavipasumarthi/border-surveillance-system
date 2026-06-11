import streamlit as st
import pandas as pd
import sqlite3
import os
import cv2
from streamlit_autorefresh import st_autorefresh
st.subheader("🖥️ System Status")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("🟢 Detection Engine Online")

with col2:
    st.success("🟢 Database Connected")

with col3:
    st.success("🟢 Dashboard Active")
from datetime import datetime

st.caption(
    f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
)    
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""

st.markdown(
    hide_st_style,
    unsafe_allow_html=True
)
st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
}

h1, h2, h3 {
    color: white;
}

[data-testid="stMetricValue"] {
    color: #00FF7F;
}

[data-testid="stSidebar"] {
    background-color: #161B22;
}

</style>
""", unsafe_allow_html=True)
st.set_page_config(
    page_title="Border Surveillance",
    layout="wide"
)
st_autorefresh(
    interval=5000,
    key="dashboardrefresh"
)
st.markdown("""
<style>

[data-testid="metric-container"] {
    background-color: #161B22;
    border: 1px solid #30363D;
    padding: 15px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
# 🚨 Border Surveillance Command Center
### AI-Powered Multi-Zone Intrusion Detection System
""")
st.subheader("🎥 Live Surveillance Feed")
video_placeholder = st.empty()
if os.path.exists("latest_frame.jpg"):
    video_placeholder.image(
        "latest_frame.jpg",
        caption="Live Surveillance Feed",
        use_container_width=True
    )
st.sidebar.title("Control Panel")

st.sidebar.success("System Status: ONLINE")

st.sidebar.info(
    """
    Active Modules:
    - YOLO Detection
    - Object Tracking
    - Threat Analysis
    - Evidence Capture
    - Database Logging
    """
)

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
    

# Search Panel
    st.subheader("Search Events")

    search_id = st.text_input("Enter Object ID")

    if search_id:
        filtered_df = df[
            df["object_id"].astype(str) == search_id
        ]

        st.dataframe(filtered_df)
    # Statistics
    total_intrusions = len(df)

    low_count = len(
        df[df["threat_level"] == "LOW"]
    )    
    st.subheader("Recent Alerts")

    st.dataframe(
        df.tail(5),
        use_container_width=True
    )

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
    df["threat_level"] = (
    df["threat_level"]
    .fillna("UNKNOWN")
    .str.upper()
)

    threat_counts = (
        df["threat_level"]
        .value_counts()
)

    zone_counts = (
    df["event"]
    .replace({
        "Entered Zone A": "Zone A",
        "Entered Zone B": "Zone B",
        "Entered Zone C": "Zone C",
        "Entered Restricted Zone": "Restricted"
    })
    .value_counts()
)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Threat Distribution")
        st.bar_chart(threat_counts)

    with col2:
        st.subheader("Zone Activity")
        st.bar_chart(zone_counts)

    st.subheader("Intrusion Timeline")

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    timeline = (
        df.set_index("timestamp")
          .resample("1min")
          .size()
)

    st.line_chart(timeline)
except Exception as e:
    st.error(f"Database Error: {e}")

# Evidence Images

st.subheader("📄 Incident Report")

if os.path.exists("Incident_Report.pdf"):

    with open(
        "Incident_Report.pdf",
        "rb"
    ) as pdf_file:

        st.download_button(
            label="Download Incident Report",
            data=pdf_file,
            file_name="Incident_Report.pdf",
            mime="application/pdf"
        )
st.subheader("📸 Latest Evidence")

if os.path.exists("evidence"):

    images = sorted(
        os.listdir("evidence"),
        reverse=True
    )

    cols = st.columns(3)

for i, image in enumerate(images[:9]):

    with cols[i % 3]:

        st.image(
            f"evidence/{image}",
            caption=image,
            use_container_width=True
        )
if high_count > 0:
    st.error(f"🔴 HIGH Threat Events: {high_count}")

if medium_count > 0:
    st.warning(f"🟠 MEDIUM Threat Events: {medium_count}")

if low_count > 0:
    st.success(f"🟢 LOW Threat Events: {low_count}")        