Aceest Gym Management System – CI/CD Pipeline

🚀 Project Overview

The Aceest Gym Management System is a Flask-based backend application that manages gym member information, including:

Age, height, weight

Membership type

Membership expiry date

This project demonstrates modern DevOps practices with Continuous Integration (CI) and Continuous Deployment (CD) using GitHub Actions, Jenkins, and Docker.
The goal is to automate building, testing, and validating application code whenever changes are pushed to the repository.

📂 Repository Structure
aceest-gym/
├── aceest_gym/
│   ├── __init__.py
│   ├── app/
│   │   ├── __init__.py
│   │   └── app.py
│   └── routes.py
├── test/
│   └── test_app.py
├── requirements.txt
├── Dockerfile
├── README.md
├── Jenkinsfile
└── .github/
    └── workflows/
        └── main.yml
🔗 API Endpoints
Route	Method	Description	Sample Response
/	GET	Check API status	{"message": "ACEest Gym DevOps API running"}
/status	GET	Check system health	{"status": "ok"}

Example Request:

curl http://localhost:5000/
💻 Local Setup Instructions
1. Clone the Repository
git clone https://github.com/2024tm93535/aceest-gym.git
cd aceest-gym
2. Create Virtual Environment (Optional)
python -m venv venv
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Run the Application
flask run

Access the app at: http://localhost:5000

✅ Running Tests

The project uses Pytest for automated testing.

pytest

Example Output:

tests/test_app.py
1 passed
🐳 Docker Setup
Build Docker Image
docker build -t aceest-gym .
Run Docker Container
docker run -p 5000:5000 aceest-gym

Access at: http://localhost:5000

Docker Optimization

Base image: python:3.10-slim (smaller size)

Dependencies installed with --no-cache-dir

Working directory: /app

Exposed port: 5000

Environment variables:

FLASK_APP=aceest_gym.app.app:create_app
FLASK_RUN_HOST=0.0.0.0
FLASK_ENV=production
🌿 Version Control Workflow

Feature development: Separate branches

Commit messages: Descriptive and structured

Example:

Add Flask route for status endpoint

Add Pytest coverage for home endpoint

Add Dockerfile for containerization

Merges to main branch occur only after tests pass

🧪 Testing Coverage

Core endpoints tested:

Home endpoint /

Status endpoint /status

Fixtures (Flask test client) used for consistent testing

Tests run automatically in GitHub Actions CI workflow

Example Test:

def test_home(client):
    rv = client.get("/")
    assert rv.status_code == 200
    assert rv.get_json() == {"message": "ACEest Gym DevOps API running"}
⚙️ CI/CD Pipeline Overview
GitHub Actions

Triggered on every push or pull request:

Checkout repository

Setup Python environment

Install dependencies

Run Pytest

Build Docker image using official Docker Action

Jenkins Pipeline

Automates project build verification:

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

Ensures builds succeed and code quality is validated after every change.

🏗 System Architecture

Layers:

Source Control: GitHub repository

Automation: GitHub Actions & Jenkins pipelines

Execution: Dependency installation, test execution, build verification

Flow:

Developer → GitHub Repository → CI Pipeline (GitHub Actions) 
→ Automated Tests → Jenkins Pipeline → Build Validation
🔮 Future Improvements

Automatic Docker image publishing to DockerHub

Deployment to cloud environments

Integration with monitoring tools

Automated production deployment

Security scanning & vulnerability checks

📌 Conclusion

This project demonstrates a professional CI/CD pipeline for a Flask-based application.
The integration of GitHub, Jenkins, automated testing, and Docker enables a reliable, automated, and modern development workflow.
