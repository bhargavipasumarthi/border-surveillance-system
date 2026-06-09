import streamlit as st
import pandas as pd
import os

st.title("🚨 Border Surveillance Dashboard")

# Events

try:
    df = pd.read_csv("events.csv")

    st.subheader("Event Log")
    st.dataframe(df)

    st.metric(
        "Total Intrusions",
        len(df)
    )

except:
    st.warning("No events found")


# Evidence Images

st.subheader("Evidence Images")

if os.path.exists("evidence"):

    images = sorted(
        os.listdir("evidence"),
        reverse=True
    )

    for image in images[:5]:

        st.image(
            f"evidence/{image}",
            caption=image
        )