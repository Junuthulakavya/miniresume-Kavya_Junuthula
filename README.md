# miniresume-Kavya_Junuthula
# Mini Resume Collector Application

## Python Version Used
Python 3.10

## Installation Steps

1. Clone the repository
git clone https://github.com/your-username/miniresume-your-full-name.git

2. Navigate to project folder
cd miniresume-your-full-name

3. Create virtual environment
python -m venv venv

4. Activate virtual environment
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

5. Install dependencies
pip install -r requirements.txt

## Run the Application

python manage.py runserver

Server runs at:
http://127.0.0.1:8000/

## API Endpoints

### Health Check
GET /health/

Response:
200 OK
{
    "status": "healthy"
}

### Submit Resume
POST /resumes/

Request Body:
{
    "full_name": "John Doe",
    "email": "john@example.com",
    "phone": "+919876543210",
    "skills": ["Python", "Django"],
    "experience": 3
}

Response:
201 Created
{
    "message": "Resume submitted successfully",
    "data": {
        ...
    }
}

### List Resumes
GET /resumes/list/

Response:
200 OK
{
    "count": 1,
    "resumes": [...]
}
