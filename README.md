# 🚨 Border Surveillance Command Center

AI-Powered Multi-Zone Intrusion Detection and Threat Monitoring System

## Overview

The Border Surveillance Command Center is an AI-based security monitoring system that detects, tracks, classifies, and logs intrusions in restricted zones. The system uses YOLO object detection, ByteTrack object tracking, threat classification, evidence capture, database logging, and a real-time Streamlit dashboard.

## Features

* Real-time object detection using YOLOv8
* Multi-object tracking using ByteTrack
* Multi-zone surveillance (Zone A, Zone B, Zone C)
* Threat classification (LOW, MEDIUM, HIGH)
* Automatic evidence screenshot capture
* SQLite database logging
* CSV event logging
* Real-time dashboard analytics
* Threat distribution visualization
* Zone activity monitoring
* Intrusion timeline tracking
* Search by Object ID
* Auto-refresh dashboard
* PDF incident report generation

## Technology Stack

### AI & Computer Vision

* Python
* YOLOv8
* OpenCV
* Supervision
* ByteTrack

### Data & Storage

* SQLite
* CSV Logging
* Pandas

### Dashboard

* Streamlit

### Reporting

* ReportLab

## Project Structure

border_project/

├── dashboard.py

├── zone_test.py

├── threat_engine.py

├── db_logger.py

├── report_generator.py

├── events.db

├── events.csv

├── Incident_Report.pdf

├── evidence/

└── README.md

## Workflow

1. Camera or video feed is captured.
2. YOLO detects objects.
3. ByteTrack assigns object IDs.
4. Objects entering surveillance zones are identified.
5. Threat level is calculated.
6. Evidence screenshot is saved.
7. Event is logged into SQLite database.
8. Dashboard updates automatically.
9. Incident reports can be downloaded as PDF.

## Dashboard Features

* Intrusion Statistics
* Threat Distribution Chart
* Zone Activity Chart
* Recent Alerts
* Search Events
* Evidence Gallery
* PDF Report Download

## Future Enhancements

* Email Alerts
* SMS Notifications
* Face Recognition
* Cloud Deployment
* Mobile Application
* Live Video Streaming

## Author

BTech Computer Science Student

AI & Machine Learning Enthusiast
