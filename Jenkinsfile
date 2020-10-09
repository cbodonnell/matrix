pipeline {
    agent any
    environment {
        EXAMPLE_VAR = 'example environment variable'
    }
    stages {
        stage('build') {
            steps {
                echo 'building...'
                sh 'sudo chmod +x ./scripts/build && ./scripts/build'
            }
        }
        stage('test') {
            steps {
                echo 'testing...'
            }
        }
        stage('deploy') {
            steps {
                echo 'deploying...'
            }
        }
    }
    post {
        cleanup {
            deleteDir()
        }
    }
}