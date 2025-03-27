import requests
import json

# Backend API URL
API_URL = "http://127.0.0.1:8000/add-app/"

# Mock Data from Virtual Android System
mock_data = {
    "app_name": "Virtual Device",
    "version": "11.0",
    "description": "Device ID: emulator-5554, OS: Android 11, Memory: 2GB"
}

def send_data():
    try:
        print("[*] Sending device info to server...")
        response = requests.post(API_URL, data=json.dumps(mock_data), headers={"Content-Type": "application/json"})
        print(f"[✓] Server Response: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    send_data()
