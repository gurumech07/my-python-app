Guru's-to-do App
A simple Flask web application for managing tasks with SQLite persistence, featuring add/edit/delete/complete functionality. Includes full GitHub Actions CI/CD pipeline with linting, tests, SonarQube analysis, and Docker Hub deployment.​

Features
Add tasks with title and optional description

Mark tasks as complete/incomplete

Edit existing tasks

Delete tasks

Responsive UI with flash messages

SQLite database (no external DB setup required)

Quick Start
bash
# Clone and enter project
git clone <your-repo-url>
cd my-python-app

# Create & activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py
Open http://127.0.0.1:5000 in your browser.

Docker
bash
# Pull from Docker Hub (after CI/CD runs)
docker pull YOUR_USERNAME/my-todo-app:latest

# Run
docker run -p 5000:5000 gurumech07/my-todo-app:latest
CI/CD Pipeline
Automated GitHub Actions workflows:

Workflow	Trigger	Jobs
python-ci.yml	Push/PR to main	flake8 linting, pytest
docker-hub.yml	Push to main	Build & push Docker image
SonarQube	Push/PR	Code quality analysis
Project Structure
text

my-python-app/
├── app.py              # Flask app factory
├── config.py           # Configuration
├── models.py           # SQLAlchemy Task model
├── views.py            # Route handlers (blueprint)
├── test_app.py         # Basic smoke tests
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker image
├── instance/
│   └── todo.db         # SQLite DB (gitignored)
├── templates/          # Jinja2 HTML
│   ├── base.html
│   ├── index.html
│   └── edit_task.html
└── static/
    ├── style.css
    └── app.js

Tech Stack
Backend: Flask 3.0+, SQLAlchemy, SQLite

Frontend: HTML5, CSS3, vanilla JavaScript

CI/CD: GitHub Actions, flake8, pytest, SonarQube

Container: Docker Hub

Environment Variables
Variable	Purpose	Default
SECRET_KEY	Flask session security	dev-secret-key-change-me
DATABASE_URL	DB connection	sqlite:///instance/todo.db
GitHub Secrets Required
For Docker Hub deployment:

DOCKERHUB_USERNAME

DOCKERHUB_TOKEN

For SonarQube/SonarCloud:

SONAR_TOKEN

Development
bash
# Activate venv
source venv/bin/activate

# Add dev deps
pip install pytest flake8 python-dotenv[dev]

# Run tests
pytest

# Lint
flake8 .

# Run with debug
FLASK_ENV=development python app.py
License
MIT License - see LICENSE file or create one. Free to use, modify, and distribute.
