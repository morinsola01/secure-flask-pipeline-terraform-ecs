pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository
                git url: 'https://github.com/morinsola01/secure-flask-pipeline-terraform-ecs.git', branch: 'main'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('Local SonarQube') {
                    sh 'sonar-scanner'
                }
            }
        }
        stage('Test') {
            steps {
                // Run unit tests with pytest
                sh 'pytest'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
