pipeline {

    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/2024tm93535/aceest-gym.git'
            }
        }

        stage('Build Step') {
            steps {
                sh 'echo "Building Aceest Gym Project..."'
            }
        }

        stage('Finish') {
            steps {
                sh 'echo "Pipeline executed successfully!"'
            }
        }

    }

}