import streamlit as st
import cv2
import numpy as np
import time
import pandas as pd
st.set_page_config(page_title="AI Interview Behavior Analyzer", layout="centered")
st.title("AI Interview Behavior Analyzer")
st.write("Real-time focus tracking with analytics dashboard.")
run = st.checkbox("Start Camera")
FRAME_WINDOW = st.image([])
chart = st.empty()
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
cap = cv2.VideoCapture(0)
focus_score = 100
focus_history = []
start_time = time.time()
while run:
    ret, frame = cap.read()
    if not ret:
        st.error("Failed to access camera.")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    height, width, _ = frame.shape
    center_x = width // 2
    if len(faces) == 0:
        focus_score -= 0.5
        status = "No Face"
    else:
        for (x, y, w, h) in faces:
            face_center_x = x + w // 2
            distance_from_center = abs(face_center_x - center_x)

            if distance_from_center > 100:
                focus_score -= 0.3
                status = "Looking Away"
            else:
                focus_score += 0.2
                status = "Focused"
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, status, (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    focus_score = max(0, min(100, focus_score))
    focus_history.append(focus_score)
    cv2.putText(frame, f"Focus Score: {int(focus_score)}",
                (20, height-20), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)
    FRAME_WINDOW.image(frame, channels="BGR")

    # Update graph
    df = pd.DataFrame(focus_history, columns=["Focus Score"])
    chart.line_chart(df)

cap.release()

# -----------------------------
# Session Summary
# -----------------------------
if focus_history:
    avg_focus = sum(focus_history) / len(focus_history)

    st.subheader("Session Summary")

    st.write(f"Average Focus Score: {round(avg_focus, 2)}")

    if avg_focus > 75:
        st.success("Overall Performance: High Focus")
    elif avg_focus > 50:
        st.warning("Overall Performance: Moderate Focus")
    else:
        st.error("Overall Performance: Low Focus")
