# Resume Analyzer

A simple web application that analyzes resumes against a job description and calculates an ATS score.

## Features

- Upload resume (PDF)
- Enter job description
- Extract relevant skills
- Calculate ATS score
- Show matched and missing skills

## Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Django (Python)
- Library: PyPDF2

## Project Structure

resumind-ai/
│
├── analyzer/
│   ├── templates/
│   │   └── index.html
│   ├── views.py
│   ├── urls.py
│
├── backend/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
├── db.sqlite3

## How to Run

1. Clone the repository
2. Create virtual environment
3. Install dependencies
4. Run server
5. Open in browser
http://127.0.0.1:8000/

## API Endpoint

POST /upload/

Inputs:
- file (resume PDF)
- job_description (text)

Output:
- ats_score
- matched_skills
- missing_skills

## Future Improvements

- Support for DOCX resumes
- Better NLP-based skill extraction
- UI improvements
- Deployment
