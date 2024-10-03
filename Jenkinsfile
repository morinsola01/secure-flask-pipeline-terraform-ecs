pipeline {
    agent any
    
    stages {
        stage('Clone repository') {
            steps {
                git url: 'https://github.com/morinsola01/secure-flask-pipeline-terraform-ecs.git', branch: 'main'
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('SonarQube analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarQubeScanner';
                    withSonarQubeEnv('SonarQube') { 
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }
        
        stage('OWASP ZAP DAST Scan') {
            steps {
                zapStart zapHome: '/path/to/zap'
                zapAttack target: 'http://your-app-url'
                zapReport reportFile: 'zap-report.html'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up...'
            cleanWs()
        }
    }
}
