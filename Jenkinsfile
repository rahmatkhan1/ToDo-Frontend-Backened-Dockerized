pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/<tumhara-username>/<flask-repo>.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Flask App') {
            steps {
                sh '''
                pkill -f flask || true
                nohup venv/bin/python app.py > flask.log 2>&1 &
                '''
            }
        }
    }
}
