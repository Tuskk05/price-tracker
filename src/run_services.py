import subprocess
import os

# API command in port 8000
api_command = [
    "uvicorn", 
    "src.api.main:app", 
    "--host", "0.0.0.0", 
    "--port", "8000"
]

# Dashboard command in port 8501
dashboard_command = [
    "streamlit", 
    "run", 
    "src/dashboard/app.py", 
    "--server.port=8501", 
    "--server.address=0.0.0.0"
]

print("Starting Price Tracker Services...")

# Execute processes at the same time
api_process = subprocess.Popen(api_command)
dashboard_process = subprocess.Popen(dashboard_command)

# Wait until one finishes
try:
    api_process.wait()
    dashboard_process.wait()
except KeyboardInterrupt:
    print("Stopping services...")
    api_process.terminate()
    dashboard_process.terminate()