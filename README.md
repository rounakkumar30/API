

# 📄 Python Intern Assignment

**Candidate:** Rounak  
**Assignment:** Python Backend, Database, Virtual Android System & Networking

---

## 📝 Table of Contents

- [Overview](#overview)
- [Folder Structure](#folder-structure)
- [Task 1 - Backend Development](#task-1---backend-development)
- [Task 2 - Database Management](#task-2---database-management)
- [Task 3 - Virtual Android System Simulation](#task-3---virtual-android-system-simulation)
- [Task 4 - Basic Networking](#task-4---basic-networking)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Submission Structure](#submission-structure)

---

## 🚀 Overview

This repository contains solutions for the Python Internship Assignment consisting of:

✅ REST API using Django  
✅ SQLite Database Integration  
✅ Virtual Android System Simulation  
✅ Networking script to connect virtual system with API

---

## 📂 Folder Structure

```
Rounak_PythonInternAssignment/
├── app_manager/                     # Task 1 & Task 2
│   ├── app_manager/                 # Django project files
│   ├── apps/                        # Django app files
│   │   ├── templates/               # Home page HTML
│   │   ├── sample_data.sql          # Sample data SQL
│   │   ├── sample_data.json         # Sample data JSON
│   │   ├── models.py                # Database model
│   │   ├── serializers.py           # DRF serializers
│   │   ├── views.py                 # API Views
│   │   └── urls.py                  # API URLs
│   └── db.sqlite3                   # SQLite Database
│
├── virtual_android/                 # Task 3
│   └── scripts/
│       └── virtual_android.py       # Android System Simulation
│
├── networking/                      # Task 4
│   └── send_device_info.py          # Networking Script
│
├── requirements.txt                 # Project dependencies
└── README.md                        # Instructions
```

---

## 🟢 Task 1 - Backend Development

A Django REST API to manage app details.

### Endpoints

| Method | Endpoint             | Description                     |
|:-----:|:--------------------:|:-------------------------------:|
| POST | `/add-app/`          | Add new app details            |
| GET  | `/get-app/{id}/`     | Retrieve app details by ID     |
| DELETE | `/delete-app/{id}/` | Delete app by ID               |

### API Home Page

Access via:  
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

This page provides clickable links and documentation.

---

## 🗃️ Task 2 - Database Management

- **Database:** SQLite (File: `db.sqlite3`)
- **Schema:** Defined in `apps/models.py`
- **Sample Data:**  
  - `sample_data.sql`
  - `sample_data.json`

You can load sample data using:

```bash
sqlite3 db.sqlite3 < apps/sample_data.sql
```

(Use Command Prompt or Bash for redirection)

---

## 🤖 Task 3 - Virtual Android System Simulation

**Script:** `virtual_android/scripts/virtual_android.py`

### Features

- Creates a virtual Android environment (Simulated)
- Displays terminal-like interface
- Installs a sample app
- Retrieves and logs:
  - OS Version
  - Device Model
  - Available Memory

### How to Run

```bash
python virtual_android/scripts/virtual_android.py
```

### Sample System Info (Logged)

```
Device Model: VirtualPhone X1
OS Version: Android 11 (Simulated)
Available Memory: 4096 MB
Sample App Installed: ChatApp.apk
```

---

## 🌐 Task 4 - Basic Networking

**Script:** `networking/send_device_info.py`

### Functionality

- Establishes HTTP connection with backend API (`/add-app/`)
- Sends mock Android device data
- Receives and logs server response

### How to Run

Ensure Django server is running:

```bash
python app_manager/manage.py runserver
```

Then execute:

```bash
python networking/send_device_info.py
```

### How it Works

The script collects simulated system info and makes a **POST request** to the API endpoint `/add-app/`. The server response is logged to the console.

---

## 📥 Requirements

Dependencies listed in `requirements.txt`:

```
Django>=3.0
djangorestframework
requests
```

Install:

```bash
pip install -r requirements.txt
```

---

## ⚙️ How to Run (Quick Guide)

1. **Clone & Navigate**

```bash
git clone https://github.com/your-repo/Rounak_PythonInternAssignment.git
cd Rounak_PythonInternAssignment
```

2. **Create Virtual Environment (Optional)**

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Run API**

```bash
cd app_manager
python manage.py migrate
python manage.py runserver
```

5. **Run Android Simulation**

```bash
python virtual_android/scripts/virtual_android.py
```

6. **Run Networking Script**

```bash
python networking/send_device_info.py
```

---

