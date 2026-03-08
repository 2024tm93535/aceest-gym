# ACEest Fitness & Gym DevOps Project

## Overview

This project demonstrates a DevOps CI/CD pipeline for a Gym Management Flask API using MongoDB.

Technologies used:

- Flask
- MongoDB
- Docker
- GitHub Actions
- Jenkins
- Pytest

## Local Setup

Install dependencies

pip install -r requirements.txt

Run application

python app/app.py

## Run Tests

pytest

## Docker Deployment

docker-compose up --build

## CI/CD

GitHub Actions automatically runs:

1. Build stage
2. Test stage
3. Docker build stage

Jenkins performs secondary build validation from the GitHub repository.

Desktop Client

This project includes a Tkinter desktop application located in:

desktop_client/gym_client.py

It interacts with the Flask API to:

- Register gym members
- View members
- Calculate BMI