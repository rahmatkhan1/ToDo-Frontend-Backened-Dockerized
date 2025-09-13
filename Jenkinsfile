pipeline {
    agent any
    stages {
        stage('Install Flask Dependencies') {
            steps {
                sh '''
                  cd Backend
                  python3 -m venv venv
                  . venv/bin/activate
                  pip install -r requirements.txt
                '''
            }
        }

        stage('Run Flask with PM2') {
            steps {
                sh '''
                  cd Backend
                  pm2 start app.py --name flask-backend --interpreter python3 || pm2 restart flask-backend
                '''
            }
        }

        stage('Install Frontend Dependencies') {
            steps {
                sh '''
                  cd Frontend
                  npm install
                '''
            }
        }

        stage('Run Frontend with PM2') {
            steps {
                sh '''
                  cd Frontend
                  pm2 start server.js --name express-frontend --interpreter node || pm2 restart express-frontend
                '''
            }
        }
    }
}
