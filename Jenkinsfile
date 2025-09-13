pipeline {
    agent any

   
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/rahmatkhan1/ToDo-Frontend-Backened-Dockerized.git'
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

        stage('Run Flask with PM2') {
            steps {
                sh '''
                # Install pm2 if not already installed
                sudo npm install -g pm2 || true
                
                # Start or restart the Flask app
                . venv/bin/activate
                pm2 start app.py --name flask-backend --interpreter python3 || pm2 restart flask-backend
                pm2 save
                '''
            }
        }
    }
}
