
pipeline {
    agent any

    options {
        timestamps()
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Obteniendo codigo del repositorio'
                checkout scm
            }
        }

        stage('Validacion') {
            steps {
                echo 'Validando herramientas y configuracion'

                sh 'docker --version'
                sh 'docker compose version'
                sh 'docker compose config -q'
            }
        }

        stage('Construccion') {
            steps {
                echo 'Construyendo imagenes Docker'
                sh 'docker compose build'
            }
        }

        stage('Ejecucion') {
            steps {
                echo 'Iniciando servicios'
                sh 'docker compose up -d --wait'
            }
        }

        stage('Pruebas de integracion') {
            steps {
                echo 'Comprobando disponibilidad de los servicios'

                sh '''
                    docker compose exec -T servicio-1 \
                    python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"

                    docker compose exec -T servicio-2 \
                    python -c "import urllib.request; urllib.request.urlopen('http://localhost:5001/health')"

                    docker compose exec -T servicio-2 \
                    python -c "import urllib.request; urllib.request.urlopen('http://localhost:5001/api/comunicacion')"
                '''
            }
        }
    }

    post {
        success {
            echo 'Integracion continua completada correctamente'
        }

        failure {
            echo 'Se produjo un error en el pipeline'
        }

        always {
            echo 'Finalizando ejecucion y limpiando contenedores'
            sh 'docker compose down --remove-orphans || true'
        }
    }
}
