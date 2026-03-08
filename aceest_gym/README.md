Aceest Gym Management System – CI/CD Pipeline
Project Overview

The Aceest Gym Management System is a backend application built using Flask that manages gym member information such as age, height, weight, membership type, and membership expiry date.

This project demonstrates the implementation of DevOps practices using Continuous Integration and Continuous Deployment (CI/CD). The repository integrates automated testing, containerization, and pipeline automation using tools such as Jenkins, GitHub Actions, and Docker.

The goal of this project is to automate the process of building, testing, and validating application code whenever changes are pushed to the repository.

Repository Structure
aceest-gym
│
├── app
|   └──app.py
├── requirements.txt
├── Dockerfile
├── README.md 
│
├── tests
│   └── test_app.py
│
├── .github
│   └── workflows
│       └── ci.yml
│
└── Jenkinsfile

Local Setup Instructions

Follow these steps to run the application locally.

1. Clone the Repository
git clone https://github.com/2024tm93535/aceest-gym.git
cd aceest-gym
2. Create Virtual Environment (Optional)
python -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Run the Application
python app.py

The application will start on:

http://localhost:5000
Running Tests Manually

The project includes automated tests using Pytest.

Run tests with:

pytest

Expected output:

tests/test_app.py
1 passed

This confirms the application functionality is validated through automated testing.

Docker Setup

The project includes a Dockerfile to containerize the application.

Build Docker Image
docker build -t aceest-gym .
Run Docker Container
docker run -p 5000:5000 aceest-gym

The application will be available at:

http://localhost:5000

Using Docker ensures that the application runs consistently across different environments.

CI/CD Pipeline Overview

The project implements Continuous Integration using both GitHub Actions and Jenkins.

GitHub Actions Integration

Whenever code is pushed to the repository:

The workflow defined in .github/workflows/ci.yml is triggered.

The pipeline checks out the repository.

Python environment is configured.

Project dependencies are installed.

Automated tests are executed using Pytest.

This ensures that every code change is automatically validated.

Jenkins Pipeline Integration

A CI pipeline is configured in Jenkins to automate project build verification.

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

Jenkins pulls the repository and executes the pipeline stages defined in the Jenkinsfile.

This helps ensure that the project builds successfully after every change.

System Architecture

The CI/CD architecture for the project consists of three major layers:

Source Control Layer

The project source code is hosted on GitHub, which acts as the central repository.

Automation Layer

Automation tools such as Jenkins and GitHub Actions monitor the repository and trigger pipelines.

Execution Layer

Pipeline stages perform tasks such as dependency installation, test execution, and build verification.

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

This architecture ensures continuous validation of the application code.

Future Improvements

The CI/CD pipeline can be extended with the following improvements:

Automatic Docker image publishing

Deployment to cloud environments

Integration with monitoring tools

Automated production deployment

Security scanning and vulnerability checks

Conclusion

This project demonstrates the implementation of a CI/CD pipeline for a Flask-based application using modern DevOps tools. The integration of GitHub, Jenkins, automated testing, and Docker enables a reliable and automated development workflow.

By implementing these practices, software delivery becomes faster, more reliable, and easier to maintain.