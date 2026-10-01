Resume Analyzer

A Django-based Resume Analyzer that extracts candidate details from PDF resumes, compares resume skills with a given job description, calculates a match score, identifies matched and missing skills, and stores analysis history.

Features
Upload resume in PDF format
Extract resume text using PyMuPDF
Extract candidate name, email, and phone number
Enter a job description
Identify required technical skills from the job description
Compare resume skills with job requirements
Calculate resume-job match percentage
Display matched and missing skills
Categorize the result as Excellent, Good, Needs Improvement, or Bad Match
Store analysis results in the database
View previous resume analyses
View detailed analysis results
Delete analysis history
Dashboard with total analyses, average score, and highest score
Django admin panel
Responsive web interface
Technologies Used
Python
Django
PyMuPDF
SQLite
HTML5
CSS3
Django ORM
Git
GitHub
Project Structure
resume-analyzer/
│
├── analyzer/
│   ├── migrations/
│   ├── templates/
│   │   └── analyzer/
│   │       ├── home.html
│   │       ├── history.html
│   │       └── analysis_detail.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── resume_analyzer/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
How the Project Works
1. Upload Resume

The user uploads a resume in PDF format.

2. Extract Resume Text

PyMuPDF extracts readable text from the uploaded PDF.

3. Extract Candidate Details

The application searches the extracted text for:

Candidate name
Email address
Phone number
4. Enter Job Description

The user enters the job description for the position they are applying for.

5. Identify Required Skills

The application checks the job description for predefined technical skills such as:

Python
Django
SQL
MySQL
REST API
JSON
HTML
CSS
JavaScript
React
Git
GitHub
CRUD
ORM
OOP
JWT
MongoDB
FastAPI
Flask
6. Compare Resume and Job Description

The application checks which required skills are present in the extracted resume text.

7. Calculate Match Score

The score is calculated based on the percentage of required skills found in the resume.

Match Score =
Matched Skills / Required Skills × 100
8. Display Result

The application displays:

Candidate information
Match percentage
Matched skills
Missing skills
Job description
Extracted resume text
9. Store Analysis

The result is stored using Django ORM so that previous analyses can be viewed later.

Match Categories
Score	Category
85% and above	Excellent Match
75% – 84%	Good Match
60% – 74%	Needs Improvement
Below 60%	Bad Match
Installation
Step 1: Clone the Repository
git clone https://github.com/Nelakurthy/resume-analyzer.git
Step 2: Open the Project
cd resume-analyzer
Step 3: Create Virtual Environment
python -m venv venv
Step 4: Activate Virtual Environment
Windows PowerShell
.\venv\Scripts\Activate.ps1

If PowerShell activation is restricted, use the virtual environment Python directly:

.\venv\Scripts\python.exe -m pip install -r requirements.txt
Step 5: Install Dependencies
pip install -r requirements.txt
Step 6: Apply Migrations
python manage.py migrate
Step 7: Create Admin User

This step is optional.

python manage.py createsuperuser

Enter the requested username, email, and password.

Step 8: Run the Development Server
python manage.py runserver
Step 9: Open the Application

Open the following address in your browser:

http://127.0.0.1:8000/
Using the Application
Open the home page.
Upload a PDF resume.
Enter the job description.
Click Analyze Resume.
View the match score.
Check matched skills.
Check missing skills.
Open the full analysis if required.
Visit History to view previous analyses.
Delete an analysis when it is no longer required.
Admin Panel

The Django admin panel can be accessed at:

http://127.0.0.1:8000/admin/

Use the superuser credentials created with:

python manage.py createsuperuser

The admin panel allows stored resume analyses to be managed.

Database

The project uses SQLite for development.

The main model stores:

Candidate name
Email
Phone
Job description
Match score
Matched skills
Missing skills
Extracted resume text
Analysis date
Important Notes
Only PDF resumes are accepted.
Scanned/image-only PDFs may not provide extractable text.
The skill matching system currently uses predefined technical skills.
The match score is a rule-based comparison and should be treated as an application-assistance metric rather than an automated hiring decision.
db.sqlite3, venv, and uploaded media files are excluded from Git using .gitignore.
Future Enhancements
AI-based resume analysis
Resume keyword recommendations
Job recommendation system
Skill gap recommendations
Resume improvement suggestions
Support for DOCX resumes
User authentication
Multiple resume comparison
Advanced NLP-based skill extraction
Resume download/report generation
Author

Saptharshi Reddy Nelakurthi
