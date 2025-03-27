📄 Python Intern Assignment - App Manager API & Android Simulation
By: Rounak

📌 Overview
This project consists of four tasks as part of a Python development assessment. It includes backend API development, database management, Android system simulation, and basic networking.

🗂️ Project Structure
pgsql
Copy
Edit
Rounak_PythonInternAssignment/
├── app_manager/
│   ├── app_manager/
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── apps/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── sample_data.sql
│   │   ├── sample_data.json
│   │   └── templates/
│   │       └── home.html
│   └── db.sqlite3
│
├── virtual_android/
│   └── scripts/
│       └── virtual_android.py
│
├── networking/
│   └── send_device_info.py
│
├── requirements.txt
└── README.md
🚀 Task 1: Backend Development (Django REST API)
🔗 API Endpoints
Method	Endpoint	Description
POST	/add-app/	Add new app details
GET	/get-app/{id}/	Retrieve app details by ID
DELETE	/delete-app/{id}/	Delete app details by ID
Home Page:
Visit: http://127.0.0.1:8000/
The home page contains information and clickable links to all API endpoints.

📝 API Setup
Create Virtual Environment:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # For Windows
source venv/bin/activate  # For Mac/Linux
Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run Migrations:

bash
Copy
Edit
cd app_manager
python manage.py migrate
Run the Server:

bash
Copy
Edit
python manage.py runserver
🗃️ Task 2: Database Management
Database: SQLite

File: app_manager/db.sqlite3

Schema: Defined in apps/models.py

🔄 Load Sample Data:
You can load the sample data using:

bash
Copy
Edit
sqlite3 db.sqlite3 < apps/sample_data.sql
(If using PowerShell, run in Git Bash or Command Prompt as < operator is not supported in PowerShell)

🤖 Task 3: Virtual Android System Simulation
Python script simulating an Android environment and system information.

📄 File:
virtual_android/scripts/virtual_android.py

🔥 Features:
Simulates Android System

Displays Terminal

Installs Sample App

Retrieves & Logs System Info

▶️ Run:
bash
Copy
Edit
python virtual_android/scripts/virtual_android.py
🌐 Task 4: Basic Networking
Python script to establish HTTP connection & send device info to backend.

📄 File:
networking/send_device_info.py

🔥 Features:
Sends mock Android data (Device ID, OS Info) to /add-app/ API

Logs server response

▶️ Run:
Make sure Django server is running and then:

bash
Copy
Edit
python networking/send_device_info.py
✅ Requirements
All dependencies are listed in requirements.txt

shell
Copy
Edit
Django>=3.0
djangorestframework
requests
Install using:

bash
Copy
Edit
pip install -r requirements.txt
📥 Submission Guidelines
All code files are provided in this repository.

Proper documentation and comments added in the code.

Folder name: Rounak_PythonInternAssignment

