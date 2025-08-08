pipeline {
    agent { label 'docker' }

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
                    // Логинимся в Harbor
                    sh "docker login -u ${DOCKER_CREDENTIALS_USR} -p ${DOCKER_CREDENTIALS_PSW} 192.168.56.106"

                    // Тегируем образ
                    sh "docker tag sattvika/vishva:${BUILD_NUMBER} 192.168.56.106/sattvika/vishva:${BUILD_NUMBER}"

                    // Пушим образ
                    sh "docker push 192.168.56.106/sattvika/vishva:${BUILD_NUMBER}"
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

