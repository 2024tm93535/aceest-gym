# Aceest Gym Management System – CI/CD Pipeline

## Project Overview

The Aceest Gym Management System is a backend application built using Flask that manages gym member information such as age, height, weight, membership type, and membership expiry date.

This project demonstrates the implementation of DevOps practices using Continuous Integration and Continuous Deployment (CI/CD). The repository integrates automated testing, containerization, and pipeline automation using tools such as Jenkins, GitHub Actions, and Docker.

The goal of this project is to automate the process of building, testing, and validating application code whenever changes are pushed to the repository.

---

## Repository Structure


aceest-gym/
├── aceest_gym/
│ ├── init.py
│ ├── app/
│ │ ├── init.py
│ │ └── app.py
│ └── routes.py
├── test/
│ └── test_app.py
├── requirements.txt
├── Dockerfile
├── README.md
├── Jenkinsfile
└── .github/
└── workflows/
└── main.yml


---

## API Endpoints

| Route     | Method | Description                  | Sample Response                          |
|-----------|--------|-----------------------------|------------------------------------------|
| `/`       | GET    | Check API status            | `{"message": "ACEest Gym DevOps API running"}` |
| `/status` | GET    | Check system health         | `{"status": "ok"}`                        |

**Example Request:**

```bash
curl http://localhost:5000/
Local Setup Instructions

Follow these steps to run the application locally:

Clone the Repository

git clone https://github.com/2024tm93535/aceest-gym.git
cd aceest-gym

Create Virtual Environment (Optional)

python -m venv venv
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

Run the Application

flask run

The application will start on:

http://localhost:5000
Running Tests Manually

Automated tests are included using Pytest.

Run tests with:

pytest

Example Output:

tests/test_app.py
1 passed

This confirms that the application functionality is validated through automated testing.

Docker Setup

The project includes a Dockerfile to containerize the application.

Build Docker Image:

docker build -t aceest-gym .

Run Docker Container:

docker run -p 5000:5000 aceest-gym

The application will be available at:

http://localhost:5000

Docker Optimization:

Base image: python:3.10-slim for smaller image size

Dependencies installed using --no-cache-dir

Working directory set to /app

Exposed port 5000 for Flask

Environment variables for Flask factory app:

FLASK_APP=aceest_gym.app.app:create_app

FLASK_RUN_HOST=0.0.0.0

FLASK_ENV=production

Version Control Workflow

Feature development is done on separate branches

Commits are descriptive and logically structured:

Add Flask route for status endpoint

Add Pytest coverage for home endpoint

Add Dockerfile for containerization

Merges to the main branch occur after tests pass

Testing Coverage

Pytest framework is used for unit testing

Core tests cover:

Home endpoint /

Status endpoint /status

Fixtures (Flask test client) are used for consistent testing

Tests run automatically in GitHub Actions CI workflow

Example Test:

def test_home(client):
    rv = client.get("/")
    assert rv.status_code == 200
    assert rv.get_json() == {"message": "ACEest Gym DevOps API running"}
CI/CD Pipeline Overview
GitHub Actions Integration

Triggered on every push or pull request

Steps:

Checkout repository

Setup Python environment

Install dependencies

Run Pytest

Build Docker image using official Docker Action

Jenkins Pipeline Integration

Jenkins pipeline configured to automate project build verification

Pipeline workflow:

Developer Push Code
       ↓
GitHub Repository
       ↓
Jenkins Pipeline Trigger
       ↓
Checkout Source Code
       ↓
Run Build Steps
       ↓
Pipeline Execution Result

Ensures builds succeed and code quality is validated after every change

System Architecture

The CI/CD architecture consists of three major layers:

Source Control Layer: GitHub repository hosting the project code

Automation Layer: GitHub Actions and Jenkins monitor repository changes and trigger pipelines

Execution Layer: Pipeline stages execute dependency installation, test execution, and build verification

Architecture Flow:

Developer
   ↓
GitHub Repository
   ↓
CI Pipeline (GitHub Actions)
   ↓
Automated Tests
   ↓
Jenkins Pipeline
   ↓
Build Validation
Future Improvements

Automatic Docker image publishing to DockerHub

Deployment to cloud environments

Integration with monitoring tools

Automated production deployment

Security scanning and vulnerability checks

Conclusion

This project demonstrates a professional CI/CD pipeline for a Flask-based application using modern DevOps tools. The integration of GitHub, Jenkins, automated testing, and Docker enables a reliable and automated development workflow.