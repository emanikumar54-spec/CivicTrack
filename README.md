# CivicTrack
### Intelligent Public Infrastructure Complaint Prioritisation System

CivicTrack is a Python-based web application designed to help manage public infrastructure complaints. It allows citizens to submit complaints, automatically calculates priority scores, and enables administrators to manage and track complaint resolution.

## Features

- **Complaint Submission:** Submit complaints about road damage, drainage issues, and other infrastructure problems.
- **Automated Prioritisation:** Calculate complaint priority using severity, affected population, safety impact, and complaint category.
- **Complaint Tracking:** Track complaints using their unique complaint ID.
- **Admin Dashboard:** View, filter, search, update, and delete complaints.
- **Analytics Dashboard:** Visualise complaint statistics and export complaint data as CSV.
- **Database Management:** Store complaint records using SQLite.
- **Admin Authentication:** Restrict administrative features through login authentication.

## Technology Stack

- Python
- Streamlit
- SQLite
- Pandas
- Matplotlib

## Project Structure

```text
CivicTrack/
│
├── app.py
├── auth.py
├── database.py
├── priority_engine.py
├── style.py
│
├── pages/
│   ├── 1_Submit_Complaint.py
│   ├── 2_Admin_Dashboard.py
│   ├── 3_Track_Complaints.py
│   └── 4_Analytics.py
│
├── database/
│   └── civictrack.db
│
├── .streamlit/
│   └── secrets.toml
│
├── test_database.py
├── test_priority.py
├── test_system.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd CivicTrack
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure admin credentials

Create `.streamlit/secrets.toml` and configure the credentials expected by the authentication module.

Do not upload real passwords or secret values to GitHub.

### 6. Run the application

```bash
streamlit run app.py
```

## Running Tests

Run the automated system tests:

```bash
python -m unittest test_system -v
```

Run individual module checks:

```bash
python test_database.py
python test_priority.py
```

## Priority Calculation

CivicTrack uses a rule-based scoring system that considers:

- Complaint severity
- Number of people affected
- Safety impact
- Complaint category

The resulting score determines the complaint priority level.

## Project Objective

The objective of CivicTrack is to support more organised public infrastructure complaint management through structured reporting, priority-based classification, and transparent complaint tracking.

## Developer

Developed as a Python-based software project.
