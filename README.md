# Proyecto Universitario | Integración Continua

<p align="center">
  <img src="https://img.shields.io/badge/Politécnico_Grancolombiano-Integración_Continua-003366?style=for-the-badge" alt="Politécnico Grancolombiano">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Docker-Containers-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/GitHub-Actions-181717?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions">
</p>

<p align="center">
  <strong>Desarrollo, contenerización y automatización de aplicaciones mediante prácticas de Integración Continua (CI) y Entrega Continua (CD).</strong>
</p>

---

## Descripción del proyecto

Este repositorio contiene el desarrollo de un proyecto académico orientado a la aplicación de principios, herramientas y prácticas de **Integración Continua (CI) y Entrega Continua (CD)** en el ciclo de vida del software.

La solución se desarrolla progresivamente a través de tres entregas académicas, integrando tecnologías para el control de versiones, la contenerización de aplicaciones, la comunicación entre servicios, la automatización de procesos y la validación del software.

La implementación inicial utiliza **Python, Flask, Docker y Docker Compose**, mediante dos servicios independientes que se comunican a través de una red interna de contenedores. Adicionalmente, se incorpora **GitHub Actions** para automatizar procesos de construcción y validación del proyecto.

**Repositorio:** [SebastianMartinezLesmes/U_Integracion-Continua](https://github.com/SebastianMartinezLesmes/U_Integracion-Continua)

## Tabla de contenido

- [Objetivos](#-objetivos)
- [Arquitectura del proyecto](#-arquitectura-del-proyecto)
- [Tecnologías utilizadas](#-tecnologías-utilizadas)
- [Entregas académicas](#-entregas-académicas)
- [Estructura del repositorio](#-estructura-del-repositorio)
- [Requisitos previos](#-requisitos-previos)
- [Instalación y ejecución](#-instalación-y-ejecución)
- [Servicios disponibles](#-servicios-disponibles)
- [Integración continua](#-integración-continua)
- [Pruebas y validaciones](#-pruebas-y-validaciones)
- [Documentación y evidencias](#-documentación-y-evidencias)
- [Buenas prácticas](#-buenas-prácticas)
- [Integrantes](#-integrantes)
- [Referencias](#-referencias)

---

## 🎯 Objetivos

### Objetivo general

Desarrollar una solución de software que permita demostrar la aplicación de prácticas de Integración Continua y Entrega Continua, mediante la implementación progresiva de herramientas de desarrollo, contenerización, automatización y validación.

### Objetivos específicos

- Administrar el código fuente mediante Git y GitHub.
- Diseñar aplicaciones independientes que puedan ejecutarse en contenedores.
- Implementar la comunicación entre servicios utilizando Docker.
- Automatizar la construcción y validación del proyecto.
- Incorporar herramientas y procesos de integración continua.
- Verificar el funcionamiento de los componentes mediante pruebas.
- Documentar la arquitectura, configuraciones, procedimientos y resultados de cada entrega.

---

## 🏗️ Arquitectura del proyecto

La solución parte de una arquitectura distribuida compuesta por dos servicios independientes desarrollados en Python con Flask.

Cada servicio dispone de su propia imagen y contenedor Docker. Ambos se conectan mediante una red virtual de Docker Compose, permitiendo la comunicación entre ellos a través de solicitudes HTTP.

### Componentes principales

| Componente | Responsabilidad |
|---|---|
| Servicio 1 | API principal que expone información y respuestas HTTP. |
| Servicio 2 | API consumidora que realiza solicitudes al Servicio 1. |
| Docker | Construcción y ejecución de los contenedores. |
| Docker Compose | Administración de los servicios y su infraestructura. |
| Red Docker | Comunicación interna entre los contenedores. |
| GitHub | Administración y almacenamiento del código fuente. |
| GitHub Actions | Automatización de procesos de integración continua. |

### Diagrama de arquitectura

```text
                    DESARROLLO
                        |
                        v
                 REPOSITORIO GITHUB
                        |
                        v
                GITHUB ACTIONS (CI)
                        |
              BUILD Y VALIDACIONES
                        |
                        v
                 DOCKER COMPOSE
                        |
                 RED-INTEGRACION
                        |
             +----------+----------+
             |                     |
             v                     v
      +-------------+       +-------------+
      |  SERVICIO 1 | <---> |  SERVICIO 2 |
      |             | HTTP  |             |
      | Flask :5000 |       | Flask :5001 |
      +-------------+       +-------------+
             |                     |
             v                     v
          API PRINCIPAL       API CONSUMIDORA
```

### Flujo de comunicación

1. El Servicio 1 inicia y expone sus endpoints HTTP.
2. El Servicio 2 inicia dentro de la misma red Docker.
3. El Servicio 2 realiza una solicitud HTTP al endpoint del Servicio 1.
4. El Servicio 1 procesa la solicitud y devuelve una respuesta JSON.
5. El Servicio 2 recibe la respuesta y la presenta mediante su propio endpoint.

Esta arquitectura permite demostrar la comunicación entre aplicaciones independientes y establecer una base para la incorporación de procesos automatizados.

---

## 🧰 Tecnologías utilizadas

| Tecnología | Aplicación |
|---|---|
| Python 3.12 | Lenguaje de programación. |
| Flask 3.1.1 | Desarrollo de servicios web y API REST. |
| Requests 2.32.4 | Comunicación HTTP entre servicios. |
| Git | Control de versiones. |
| GitHub | Repositorio remoto y administración del código. |
| Docker | Contenerización de las aplicaciones. |
| Docker Compose | Orquestación de los contenedores. |
| GitHub Actions | Automatización de procesos CI. |
| Jenkins | Herramienta contemplada dentro del contexto académico de CI/CD. |
| Travis CI | Herramienta contemplada dentro del contexto académico de CI/CD. |

*La incorporación efectiva de Jenkins, Travis CI u otras herramientas dependerá de los requisitos de las entregas correspondientes.*

---

## 📚 Entregas académicas

El proyecto se organiza en tres etapas que permiten desarrollar y ampliar progresivamente la solución.

### Entrega 1 — Contenerización y comunicación entre servicios

<sub>Implementación inicial</sub>

Esta etapa establece la infraestructura básica del proyecto mediante la creación de dos aplicaciones independientes y su ejecución en contenedores Docker.

**Actividades implementadas:**

- Creación del repositorio en GitHub.
- Organización de la estructura del proyecto.
- Desarrollo de dos servicios utilizando Python y Flask.
- Creación de un Dockerfile para cada servicio.
- Configuración de Docker Compose.
- Construcción de las imágenes Docker.
- Creación de una red para la comunicación entre contenedores.
- Implementación de solicitudes HTTP entre los servicios.
- Configuración de endpoints de comprobación de estado.
- Documentación del procedimiento y de las evidencias.

**Resultado esperado:** disponer de dos servicios independientes ejecutándose en contenedores Docker y con capacidad de intercambiar información.

**Documentación:** [`docs/entrega-1/README.md`](docs/entrega-1/README.md)

### Entrega 2 — Evolución e integración de herramientas

<sub>Etapa de ampliación</sub>

Esta etapa estará orientada a ampliar la solución desarrollada inicialmente, incorporando las herramientas, configuraciones y procedimientos definidos en el segundo enunciado académico.

**Líneas de trabajo:**

- Revisar y conservar la arquitectura inicial.
- Incorporar los componentes adicionales requeridos.
- Integrar las herramientas de automatización correspondientes.
- Configurar los procesos necesarios para construir y validar la aplicación.
- Realizar pruebas sobre los componentes integrados.
- Documentar las configuraciones y los resultados.

**Documentación:** [`docs/entrega-2/`](docs/entrega-2/)

*Los requisitos específicos se incorporarán una vez contrastados con el enunciado oficial de esta entrega.*

### Entrega 3 — Consolidación del proyecto

<sub>Etapa de finalización</sub>

La última etapa estará enfocada en consolidar la solución y completar los procesos de automatización, integración y validación establecidos en el tercer enunciado académico.

**Líneas de trabajo:**

- Consolidar la arquitectura final.
- Completar las configuraciones de integración continua y entrega continua.
- Automatizar los procesos solicitados.
- Ejecutar y verificar las pruebas correspondientes.
- Validar el funcionamiento conjunto de los componentes.
- Documentar los resultados y las evidencias finales.

**Documentación:** [`docs/entrega-3/`](docs/entrega-3/)

*Los requisitos y criterios de aceptación se definirán de acuerdo con el enunciado oficial de la tercera entrega.*

---

## 📁 Estructura del repositorio

La organización del proyecto separa el código fuente, la configuración de infraestructura, los procesos de automatización y la documentación académica.

```text
U_Integracion-Continua/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── docker/
│   ├── servicio-1/
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   │
│   └── servicio-2/
│       ├── Dockerfile
│       └── requirements.txt
│
├── src/
│   ├── servicio-1/
│   │   ├── __init__.py
│   │   └── app.py
│   │
│   └── servicio-2/
│       ├── __init__.py
│       └── app.py
│
├── docs/
│   ├── entrega-1/
│   │   ├── README.md
│   │   └── imagenes/
│   │
│   ├── entrega-2/
│   │   └── imagenes/
│   │
│   └── entrega-3/
│       └── imagenes/
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

### Descripción de directorios

| Directorio o archivo | Descripción |
|---|---|
| `.github/workflows/` | Configuración de los workflows de GitHub Actions. |
| `docker/` | Dockerfiles y dependencias de cada servicio. |
| `src/` | Código fuente de las aplicaciones. |
| `docs/` | Documentación y evidencias de las entregas. |
| `docker-compose.yml` | Configuración de los servicios y la red Docker. |
| `.gitignore` | Exclusión de archivos innecesarios o sensibles. |
| `README.md` | Documentación general del proyecto. |

---

## ⚙️ Requisitos previos

Antes de ejecutar el proyecto, se recomienda contar con las siguientes herramientas:

| Requisito | Descripción |
|---|---|
| Git | Instalado y configurado. |
| GitHub | Cuenta con acceso al repositorio. |
| Docker Desktop | Para Windows y macOS, o Docker Engine en Linux. |
| Docker Compose | Disponible mediante el comando `docker compose`. |
| Editor de código | Se recomienda Visual Studio Code. |

**Verificar las instalaciones:**

```bash
git --version
docker --version
docker compose version
```

---

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/SebastianMartinezLesmes/U_Integracion-Continua.git
```

Ingresar al directorio:

```bash
cd U_Integracion-Continua
```

### 2. Construir las imágenes

Desde la raíz del proyecto:

```bash
docker compose build
```

Este comando construye las imágenes correspondientes a los dos servicios utilizando sus respectivos Dockerfiles.

### 3. Iniciar los contenedores

```bash
docker compose up -d
```

La opción `-d` permite ejecutar los servicios en segundo plano.

### 4. Verificar el estado de los servicios

```bash
docker compose ps
```

Los dos servicios deben aparecer en ejecución y sus comprobaciones de estado deben alcanzar el estado saludable (`healthy`).

### 5. Consultar los registros

```bash
docker compose logs
```

Para consultar los registros de un servicio específico:

```bash
docker compose logs servicio-1
docker compose logs servicio-2
```

### 6. Detener los servicios

```bash
docker compose down
```

Este comando detiene y elimina los contenedores creados por Docker Compose, conservando las imágenes construidas.

---

## 🌐 Servicios disponibles

Una vez iniciados los contenedores, los servicios pueden consultarse desde el navegador o mediante herramientas como Postman y curl.

### Servicio 1 — API principal

<sub>Puerto 5000</sub>

| Endpoint | Método | Descripción |
|---|---|---|
| `/` | GET | Información general del servicio. |
| `/api/info` | GET | Información descriptiva y fecha de ejecución. |
| `/api/saludo` | GET | Respuesta utilizada para comprobar la comunicación. |
| `/health` | GET | Estado de salud del servicio. |

**Dirección local:**

```text
http://localhost:5000
```

### Servicio 2 — API consumidora

<sub>Puerto 5001</sub>

| Endpoint | Método | Descripción |
|---|---|---|
| `/` | GET | Información general del servicio. |
| `/api/comunicacion` | GET | Consume el endpoint del Servicio 1 y devuelve su respuesta. |
| `/health` | GET | Estado de salud del servicio. |

**Dirección local:**

```text
http://localhost:5001
```

### Comprobar la comunicación entre servicios

Ejecutar:

```bash
curl http://localhost:5001/api/comunicacion
```

La respuesta esperada tendrá una estructura similar a la siguiente:

```json
{
  "estado": "Exitoso",
  "servicio_origen": "Servicio 2",
  "servicio_destino": "Servicio 1",
  "respuesta_servicio_1": {
    "servicio": "Servicio 1",
    "mensaje": "Hola desde el Servicio 1",
    "respuesta": "Comunicación entre contenedores exitosa"
  }
}
```

*El ejemplo representa la respuesta esperada cuando ambos servicios están disponibles y la comunicación HTTP funciona correctamente.*

---

## 🔄 Integración continua

El proyecto incorpora GitHub Actions como mecanismo de automatización de procesos de integración continua.

El workflow se encuentra en:

```text
.github/workflows/ci.yml
```

### Funcionamiento del proceso CI

El workflow está configurado para ejecutarse ante los siguientes eventos:

- `push`: cuando se envían cambios a las ramas configuradas.
- `pull_request`: cuando se generan solicitudes de integración hacia las ramas configuradas.
- `workflow_dispatch`: cuando se inicia manualmente desde GitHub Actions.

### Etapas del workflow

| Etapa | Función |
|---|---|
| Checkout | Obtiene el código fuente del repositorio. |
| Verificación | Comprueba la disponibilidad de Docker y Docker Compose. |
| Validación | Verifica la configuración de Docker Compose. |
| Build | Construye las imágenes de los servicios. |
| Ejecución | Inicia los contenedores. |
| Verificación | Comprueba que los servicios estén ejecutándose. |
| Logs | Recopila los registros para facilitar el diagnóstico. |
| Cleanup | Detiene y elimina los contenedores al finalizar. |

El objetivo es reducir las validaciones manuales y detectar errores durante el proceso de integración del código.

---

## 🧪 Pruebas y validaciones

Las pruebas permiten comprobar que la infraestructura y los servicios funcionan de acuerdo con lo establecido en la arquitectura.

| Prueba | Resultado esperado |
|---|---|
| Construcción de imágenes | Las imágenes Docker se generan correctamente. |
| Inicio de contenedores | Los dos servicios se ejecutan. |
| Healthcheck Servicio 1 | El servicio responde correctamente. |
| Healthcheck Servicio 2 | El servicio responde correctamente. |
| Comunicación HTTP | El Servicio 2 recibe información del Servicio 1. |
| Integración con Docker Compose | Los servicios funcionan dentro de la misma red. |
| Workflow CI | Las etapas configuradas finalizan correctamente. |

Los resultados definitivos deben respaldarse con las ejecuciones y evidencias obtenidas durante las pruebas.

---

## 📸 Documentación y evidencias

La documentación académica se organiza por entregas para facilitar el seguimiento de las actividades y la revisión de los resultados.

| Entrega | Documentación | Evidencias |
|---|---|---|
| Entrega 1 | `docs/entrega-1/README.md` | Configuración Docker, contenedores, comunicación y pruebas. |
| Entrega 2 | `docs/entrega-2/` | Configuraciones, automatizaciones y resultados correspondientes. |
| Entrega 3 | `docs/entrega-3/` | Integración final, pipelines y pruebas correspondientes. |

Las capturas de pantalla deben mostrar resultados reales y estar acompañadas de una breve descripción del procedimiento realizado.

---

## 🔐 Buenas prácticas

Durante el desarrollo se aplican las siguientes recomendaciones:

1. Mantener el código fuente organizado y versionado.
2. Utilizar commits descriptivos.
3. Separar el código fuente de la configuración de infraestructura.
4. Evitar almacenar credenciales y secretos en el repositorio.
5. Utilizar variables de entorno para configuraciones sensibles o variables.
6. Mantener los servicios independientes y con responsabilidades definidas.
7. Verificar los cambios antes de integrarlos.
8. Documentar las configuraciones y los procedimientos.
9. Conservar evidencias de las pruebas realizadas.
10. Mantener actualizadas las dependencias y herramientas del proyecto.

---

## 👨‍💻 Integrantes

| Integrante | Responsabilidad |
|---|---|
| Sebastian Martinez Lesmes | Desarrollo, configuración e integración del proyecto. |
 
*Actualizar esta sección si participan otros integrantes.*

---

## 📖 Referencias

- [GitHub Docs](https://docs.github.com/es)
- [Git Documentation](https://git-scm.com/doc)
- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Python Documentation](https://docs.python.org/3/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Requests Documentation](https://requests.readthedocs.io/)
- [GitHub Actions Documentation](https://docs.github.com/es/actions)
- [Jenkins Documentation](https://www.jenkins.io/doc/)
- [Travis CI Documentation](https://docs.travis-ci.com/)

---

## Conclusión

Este proyecto constituye una implementación académica orientada a comprender y aplicar los principios de Integración Continua y Entrega Continua dentro del desarrollo de software.

A partir de una arquitectura basada en servicios independientes, Docker y Docker Compose, se establece una base técnica que permite incorporar progresivamente herramientas de automatización, integración y validación.

La organización del repositorio, la documentación de cada entrega y la ejecución de pruebas permiten mantener un proceso de desarrollo estructurado, verificable y preparado para evolucionar hacia una solución de CI/CD más completa.

---

<p align="center">
  <strong>Proyecto Universitario | Integración Continua</strong>
  <br>
  Politécnico Grancolombiano
  <br><br>
  <a href="https://github.com/SebastianMartinezLesmes/U_Integracion-Continua">Ver repositorio en GitHub</a>
</p>