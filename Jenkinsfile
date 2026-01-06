pipeline {
    agent any

    environment {
        IMAGE_NAME = "boycott-app"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/eya-amri/boycott-app.git', credentialsId: 'github-credential'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Unit Tests') {
            steps {
                sh '''
                . venv/bin/activate
                export PYTHONPATH=$PYTHONPATH:$(pwd)
                pytest
                '''
            }
        }

        stage('Dependency Security Scan (Safety)') {
            steps {
                sh '''
                . venv/bin/activate
                pip install --upgrade pip
                pip install safety
                safety check || true
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Docker Image Scan (Trivy)') {
            steps {
                sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy image --severity HIGH,CRITICAL $IMAGE_NAME'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline sécurisé terminé avec succès'
        }
        failure {
            echo '❌ Échec du pipeline (tests ou sécurité)'
        }
    }
}
