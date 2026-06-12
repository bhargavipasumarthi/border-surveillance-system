import webview
import subprocess
import time

# Start Streamlit dashboard
subprocess.Popen(
    [
        "streamlit",
        "run",
        "dashboard.py",
        "--server.headless",
        "true"
    ]
)

# Wait for Streamlit to start
time.sleep(5)

# Create desktop app window
webview.create_window(
    "🛡 Border Surveillance Command Center",
    "http://localhost:8501",
    width=1400,
    height=900
)

webview.start()