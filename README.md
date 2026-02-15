# miniresume-Kavya_Junuthula

This is a REST API built using Django and Django REST Framework to collect candidate resume details.

The application:
- Accepts resume data via API
- Performs input validation
- Stores data in memory (no database persistence)
- Exposes structured REST endpoints

---

## Python Version Used

Python 3.10

---

## Installation Steps

1. Clone the repository

git clone https://github.com/your-username/miniresume-Kavya_Junuthula.git

2. Navigate into the project folder

cd miniresume-your-full-name

3. Create a virtual environment

python -m venv venv

4. Activate the virtual environment

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

5. Install dependencies

pip install -r requirements.txt

---

## Steps to Run the Application

Run the Django development server:

python manage.py runserver

The application will run at:

http://127.0.0.1:8000/

---

## Example API Request and Response

### 1. Health Check

Request:

GET /health/

Response (200 OK):

{
    "status": "healthy"
}

---

### 2. Submit Resume

Request:

POST /resumes/

Request Body (JSON):

{
    "full_name": "Kavya junuthula",
    "email": "Kavya@example.com",
    "phone": "+919876543210",
    "skills": ["Python", "Django"],
    "experience": 3
}

Response (201 Created):

{
    "message": "Resume submitted successfully",
    "data": {
        "full_name": "Kavya",
        "email": "Kavya@example.com",
        "phone": "+919876543210",
        "skills": ["Python", "Django"],
        "experience": 3
    }
}

---

### 3. List Resumes

Request:

GET /resumes/list/

Response (200 OK):

{
    "count": 1,
    "resumes": [
        {
            "full_name": "Kavya",
            "email": "Kavya@example.com",
            "phone": "+919876543210",
            "skills": ["Python", "Django"],
            "experience": 3
        }
    ]
}

