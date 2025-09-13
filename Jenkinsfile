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
        dir('Frontend') {
            // Retry up to 3 times in case of network issues
            retry(3) {
                sh '''
                    # Set npm registry to the official one (bypass mirror/proxy issues)
                    npm config set registry https://registry.npmjs.org/

                    # Optional: increase network timeout
                    npm config set fetch-retries 5
                    npm config set fetch-retry-factor 2
                    npm config set fetch-retry-mintimeout 20000
                    npm config set fetch-retry-maxtimeout 120000

                    npm install
                '''
            }
        }
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
