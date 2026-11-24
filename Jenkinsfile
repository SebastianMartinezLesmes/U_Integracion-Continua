
pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
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
                echo 'Iniciando servicios sin eliminar contenedores existentes'
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

        stage('Verificacion final') {
            steps {
                echo 'Verificando que los contenedores permanezcan activos'
                sh 'docker compose ps'
            }
        }
    }

    post {
        success {
            echo 'Integracion continua completada correctamente'
            echo 'Los contenedores permanecen activos'
        }

        failure {
            echo 'Se produjo un error en el pipeline'
            echo 'Los contenedores no seran eliminados automaticamente'
        }

        always {
            echo 'Finalizando pipeline sin detener ni eliminar contenedores'
            sh 'docker compose ps'
        }
    }
}