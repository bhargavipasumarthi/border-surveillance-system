import streamlit as st
import cv2

st.title("LIVE DASHBOARD TEST")

video_placeholder = st.empty()

cap = cv2.VideoCapture("test.mp4")

while cap.isOpened():

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    video_placeholder.image(
        frame,
        channels="RGB"
    )

cap.release()