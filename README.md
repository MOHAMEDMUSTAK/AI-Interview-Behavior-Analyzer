# AI Interview Behavior Analyzer

## Overview
AI Interview Behavior Analyzer is a real-time computer vision application that monitors user focus and attention during a simulated interview session. The system uses face detection and behavioral tracking logic to calculate a dynamic focus score and generate session analytics.

## Features
- Real-time webcam-based face detection
- Focus score calculation based on facial alignment
- Attention status detection (Focused / Looking Away / No Face)
- Live focus score graph
- Session performance summary
- Behavioral analytics dashboard

## Tech Stack
- Python
- Streamlit
- OpenCV
- NumPy
- Pandas

## How It Works
The system uses OpenCV's Haar Cascade classifier to detect faces from webcam frames. It evaluates facial alignment relative to screen center to estimate attention level. A dynamic focus score is calculated and tracked over time, producing real-time analytics and a final session performance summary.

## How to Run
1. Install dependencies:
   pip install -r requirements.txt
2. Run the application:
   streamlit run app.py
3. Enable camera and start session.

## Use Cases
- AI-based interview monitoring
- Smart proctoring systems
- Behavioral attention tracking
- Human-computer interaction research

## Future Improvements
- Eye tracking integration
- Head pose estimation
- ML-based behavior scoring
- Emotion detection
- PDF session report export

## Author
Mohamed Mustak M
