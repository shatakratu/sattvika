pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/shatakratu/sattvika.git'
                sh "docker build -t sattvika/vishva:${BUILD_NUMBER} ."
            }
        }

        stage('Push to Harbor') {
            environment {
                DOCKER_CREDENTIALS = credentials('harbor')
            }
            steps {
                script {
                    sh "docker login -u ${DOCKER_CREDENTIALS_USR} -p ${DOCKER_CREDENTIALS_PSW} 10.1.1.1"
                    sh "docker tag sattvika/vishva:${BUILD_NUMBER} 10.1.1.1/sattvika/vishva:${BUILD_NUMBER}"
                    sh "docker push 10.1.1.1/sattvika/vishva:${BUILD_NUMBER}"
                }
            }
        }

        stage('Trigger GitHub Push') {
            steps {
                build job: 'push_image_tag_git', wait: true, parameters: [
                    string(name: 'Build_Number_Image', value: "${BUILD_NUMBER}")
                ]
            }
        }
    }
}

