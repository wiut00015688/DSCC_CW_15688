# Task Manager App

A fully functional task management web application built with Django, containerized with Docker, and deployed using modern DevOps practices.

## Features

- User authentication (register, login, logout)
- Create, view, edit and delete tasks (CRUD)
- Filter tasks by status and category
- Add comments to tasks
- Task priority and status tracking
- Admin panel for managing all data
- Responsive Bootstrap UI

## Technologies Used

- Backend: Django 5.1.4, Python 3.11
- Database: PostgreSQL 15
- Web Server: Nginx, Gunicorn
- Containerization: Docker, Docker Compose
- CI/CD: GitHub Actions
- Container Registry: Docker Hub
- Cloud: Eskiz Server
- SSL: Let's Encrypt

## Database Schema

- User (Django built-in) — authentication
- Category — task categories (one-to-many with Task)
- Task — main model with status, priority, due date (many-to-one with User and Category, many-to-many with assigned users)
- Comment — comments on tasks (many-to-one with Task and User)

## Local Setup Instructions

### Prerequisites
- Python 3.11+
- Docker Desktop
- Git

### Steps

1. Clone the repository:
`bash
git clone https://github.com/YOURUSERNAME/task_manager.git
cd task_manager
Create virtual environment:
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
Install dependencies:
pip install -r requirements.txt
Create .env file:
SECRET_KEY=your-secret-key
DEBUG=True
USE_SQLITE=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=taskmanager
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
Run migrations:
python manage.py migrate
Create superuser:
python manage.py createsuperuser
Run the server:
python manage.py runserver
Visit http://127.0.0.1:8000Docker Setup
Make sure Docker Desktop is running
Build and run all services:
docker-compose up --build
Visit http://localhost
Deployment Instructions
SSH into your server
Clone the repository
Create .env file with production values
Run:
docker-compose up -dEnvironment Variables
Variable
Description
Example
SECRET_KEY
Django secret key
django-insecure-...
DEBUG
Debug mode
False
ALLOWED_HOSTS
Allowed hosts
yourdomain.uz,localhost
DB_NAME
Database name
taskmanager
DB_USER
Database user
postgres
DB_PASSWORD
Database password
yourpassword
DB_HOST
Database host
db
DB_PORT
Database port
5432
USE_SQLITE
Use SQLite locally
False
CI/CD Pipeline
The GitHub Actions pipeline automatically:
Runs flake8 code quality checks
Runs all 13 tests against PostgreSQL
Builds Docker image
Pushes image to Docker Hub
Deploys to server via SSH
GitHub Secrets Required
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
SSH_HOST
SSH_USERNAME
SSH_PRIVATE_KEY
Screenshots
Home Page
�
Load image
Dashboard
�
Load image
Task List
�
Load image
Test Credentials
Username: testuser
Password: testpass123
Author
Name: YOUR NAME
Student ID: YOUR ID