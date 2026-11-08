# Entrega 1 – Semana 3
## Implementación de contenedores Docker y comunicación entre servicios

<p align="center">
  <img src="https://img.shields.io/badge/Politécnico%20Grancolombiano-Integración%20Continua-003366?style=for-the-badge" alt="Politécnico Grancolombiano">
  <img src="https://img.shields.io/badge/Docker-Implementado-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/GitHub-Repositorio-181717?style=for-the-badge&logo=github" alt="GitHub">
  <img src="https://img.shields.io/badge/Estado-Exitoso-success?style=for-the-badge" alt="Estado exitoso">
</p>

## 1. Introducción

La primera entrega del proyecto universitario de Integración Continua tiene como propósito implementar una arquitectura basada en contenedores Docker, permitiendo la ejecución independiente de dos servicios de software y estableciendo una comunicación entre ellos.

Para desarrollar esta actividad se creó un proyecto compuesto por dos aplicaciones web desarrolladas en Python utilizando el framework Flask. Cada aplicación se ejecuta dentro de su propio contenedor Docker y dispone de endpoints HTTP que permiten comprobar su funcionamiento.

La comunicación entre los servicios se establece mediante una red virtual de tipo `bridge`, administrada a través de Docker Compose.

Adicionalmente, se utiliza GitHub como repositorio central para almacenar y administrar el código fuente, los archivos de configuración y la documentación del proyecto.

## 2. Objetivos

### 2.1. Objetivo general

Implementar una arquitectura de software basada en dos contenedores Docker independientes, estableciendo mecanismos de comunicación entre ellos y documentando el proceso de construcción, configuración, ejecución y validación.

### 2.2. Objetivos específicos

- Configurar un repositorio GitHub para administrar el proyecto.
- Preparar el entorno de desarrollo utilizando Python y Docker.
- Desarrollar dos servicios independientes mediante Flask.
- Crear los Dockerfile correspondientes a cada servicio.
- Construir las imágenes Docker.
- Configurar Docker Compose para administrar los contenedores.
- Establecer una red interna para permitir la comunicación entre los servicios.
- Implementar solicitudes HTTP para intercambiar información.
- Ejecutar pruebas que permitan comprobar el funcionamiento de los dos contenedores.

## 3. Herramientas y tecnologías utilizadas

| Herramienta | Aplicación |
|---|---|
| Git | Control de versiones. |
| GitHub | Administración del repositorio. |
| Python 3.12 | Lenguaje de programación. |
| Flask 3.1.1 | Desarrollo de las API REST. |
| Requests 2.32.4 | Comunicación HTTP entre servicios. |
| Docker | Construcción y ejecución de contenedores. |
| Docker Compose | Administración de los servicios. |
| Visual Studio Code | Desarrollo y edición del código. |

## 4. Arquitectura implementada

Se desarrolló una arquitectura compuesta por dos servicios independientes:

**Servicio 1 – API principal**

Es el encargado de proporcionar información mediante endpoints HTTP. Recibe solicitudes y devuelve respuestas en formato JSON.

**Servicio 2 – API consumidora**

Es el encargado de realizar solicitudes HTTP al Servicio 1, procesar las respuestas recibidas y proporcionar los resultados a través de sus propios endpoints.

### 4.1. Diagrama de arquitectura

```text
                   USUARIO
                      |
                      v
                DOCKER COMPOSE
                      |
             RED: red-integracion
                      |
             +--------+--------+
             |                 |
             v                 v
      +-------------+   +-------------+
      |  SERVICIO 1 |   |  SERVICIO 2 |
      |             |   |             |
      | Flask API   |   | Flask API   |
      | Puerto 5000 |   | Puerto 5001 |
      |             |   |             |
      +------+------+   +------+------+
             |                 |
             |<----------------|
             |    HTTP GET     |
             |                 |
             v                 v
       Respuesta JSON    Procesamiento
                              |
                              v
                       Respuesta JSON
```

La comunicación interna utiliza el nombre del servicio definido en Docker Compose:

```text
http://servicio-1:5000
```

Esto permite que el Servicio 2 encuentre al Servicio 1 mediante la resolución DNS interna de Docker, sin necesidad de utilizar direcciones IP fijas.

### 4.2. Configuración de puertos

| Servicio | Puerto interno | Puerto externo |
|---|---:|---:|
| Servicio 1 | 5000 | 5000 |
| Servicio 2 | 5001 | 5001 |

## 5. Desarrollo de los servicios

### 5.1. Servicio 1 – API principal

Se implementó una aplicación Flask encargada de proporcionar información a los demás componentes del proyecto.

Sus endpoints principales son:

| Endpoint | Método | Función |
|---|---|---|
| `/` | GET | Verificar el funcionamiento del servicio. |
| `/api/info` | GET | Consultar información del servicio. |
| `/api/saludo` | GET | Proporcionar una respuesta para el Servicio 2. |
| `/health` | GET | Comprobar el estado de salud del contenedor. |

La respuesta del endpoint `/api/saludo` permite demostrar que el servicio se encuentra disponible y puede responder solicitudes HTTP.

### 5.2. Servicio 2 – API consumidora

Se desarrolló una segunda aplicación Flask que utiliza la biblioteca Requests para establecer comunicación con el Servicio 1.

Sus endpoints principales son:

| Endpoint | Método | Función |
|---|---|---|
| `/` | GET | Verificar el funcionamiento del servicio. |
| `/api/comunicacion` | GET | Realizar una solicitud al Servicio 1. |
| `/health` | GET | Comprobar el estado de salud del contenedor. |

El endpoint `/api/comunicacion` realiza una solicitud HTTP al endpoint `/api/saludo` del Servicio 1.

Cuando recibe una respuesta satisfactoria, devuelve un objeto JSON con la información obtenida.

También se implementó un mecanismo de manejo de excepciones para controlar posibles errores de comunicación.

## 6. Implementación de Docker

### 6.1. Construcción de imágenes

Se crearon dos archivos Dockerfile independientes, uno para cada servicio.

Ambos utilizan como imagen base:

```dockerfile
FROM python:3.12-slim
```

Esta imagen permite ejecutar las aplicaciones Python utilizando una distribución ligera.

Los Dockerfile realizan las siguientes operaciones:

1. Seleccionan la imagen base de Python.
2. Configuran el directorio de trabajo.
3. Copian e instalan las dependencias.
4. Incorporan el código fuente de cada servicio.
5. Exponen el puerto correspondiente.
6. Configuran el comando de ejecución de la aplicación.

### 6.2. Administración mediante Docker Compose

Se implementó el archivo `docker-compose.yml` en la raíz del proyecto.

Este archivo permite administrar los dos servicios desde una única configuración.

Entre sus principales características se encuentran:

- Construcción independiente de las imágenes.
- Configuración de los puertos de acceso.
- Creación de una red compartida.
- Definición de variables de entorno.
- Configuración de comprobaciones de salud.
- Establecimiento del orden de inicio de los servicios.
- Reinicio automático de los contenedores cuando corresponde.

### 6.3. Red de comunicación

Se configuró una red Docker de tipo `bridge` denominada:

```text
red-integracion
```

Los dos contenedores se encuentran conectados a esta red, permitiendo el intercambio de información mediante sus nombres de servicio.

La variable de entorno utilizada por el Servicio 2 es:

```yaml
SERVICIO_1_URL: http://servicio-1:5000
```

De esta manera, la dirección del Servicio 1 puede configurarse sin modificar directamente el código fuente.

## 7. Instalación y ejecución

### 7.1. Clonar el repositorio

Se descarga el proyecto desde GitHub:

```bash
git clone https://github.com/SebastianMartinezLesmes/U_Integracion-Continua.git

cd U_Integracion-Continua
```

### 7.2. Verificar Docker

Se comprueba que Docker y Docker Compose se encuentren instalados:

```bash
docker --version

docker compose version
```

### 7.3. Construir las imágenes

Se ejecuta el siguiente comando desde la raíz del proyecto:

```bash
docker compose build
```

Este procedimiento construye las imágenes correspondientes a los dos servicios utilizando sus respectivos Dockerfile.

### 7.4. Ejecutar los contenedores

Una vez finalizada la construcción, se inician los servicios:

```bash
docker compose up -d
```

Docker Compose crea la red configurada y ejecuta los contenedores.

### 7.5. Verificar los contenedores

Para consultar el estado de los servicios:

```bash
docker compose ps
```

Se verifica que los dos contenedores se encuentren en estado de ejecución y que sus comprobaciones de salud sean satisfactorias.

### 7.6. Consultar los registros

Para revisar los registros generados por las aplicaciones:

```bash
docker compose logs
```

Este comando permite identificar posibles errores y verificar el comportamiento de los servicios.

## 8. Pruebas de funcionamiento

Una vez ejecutados los contenedores, se realizaron pruebas para verificar el funcionamiento independiente de cada aplicación y la comunicación entre ellas.

### 8.1. Prueba del Servicio 1

Se accedió a la siguiente dirección:

```text
http://localhost:5000/
```

**Resultado esperado:** respuesta JSON indicando que el Servicio 1 se encuentra funcionando correctamente.

Posteriormente, se consultó:

```text
http://localhost:5000/api/info
```

Se obtuvo la información correspondiente a la API principal.

### 8.2. Prueba del Servicio 2

Se accedió a:

```text
http://localhost:5001/
```

**Resultado esperado:** respuesta JSON indicando que el Servicio 2 se encuentra funcionando correctamente.

### 8.3. Prueba de comunicación entre contenedores

Esta prueba constituye el objetivo principal de la primera entrega.

Se realizó una solicitud al siguiente endpoint:

```text
http://localhost:5001/api/comunicacion
```

El Servicio 2 recibió la solicitud y ejecutó internamente una petición HTTP hacia:

```text
http://servicio-1:5000/api/saludo
```

El Servicio 1 procesó la petición y devolvió una respuesta JSON.

El Servicio 2 recibió dicha información y generó la siguiente respuesta:

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

**Resultado:** la comunicación HTTP entre los dos contenedores se realizó correctamente y el Servicio 2 pudo procesar la información proporcionada por el Servicio 1.

### 8.4. Prueba de estado de salud

Se verificaron los siguientes endpoints:

```text
http://localhost:5000/health
http://localhost:5001/health
```

Ambos servicios devolvieron una respuesta satisfactoria, permitiendo comprobar su disponibilidad.

## 9. Resultados obtenidos

Después de implementar la arquitectura y ejecutar las pruebas correspondientes, se obtuvieron los siguientes resultados:

| Actividad | Resultado |
|---|---|
| Creación del repositorio GitHub | Satisfactorio |
| Configuración del entorno Docker | Satisfactorio |
| Construcción de la imagen del Servicio 1 | Satisfactorio |
| Construcción de la imagen del Servicio 2 | Satisfactorio |
| Ejecución del primer contenedor | Satisfactorio |
| Ejecución del segundo contenedor | Satisfactorio |
| Configuración de la red Docker | Satisfactorio |
| Acceso independiente a los servicios | Satisfactorio |
| Comunicación HTTP entre contenedores | Satisfactorio |
| Validación de los endpoints de salud | Satisfactorio |

La implementación permitió comprobar que dos aplicaciones independientes pueden ejecutarse en contenedores separados y comunicarse mediante una red interna administrada por Docker.

## 10. Evidencias del desarrollo

Las evidencias visuales del procedimiento se almacenan en el directorio:

```text
docs/entrega-1/imagenes/
```

Se recomienda incluir las siguientes capturas:

| Evidencia | Descripción |
|---|---|
| `01-repositorio.png` | Repositorio del proyecto en GitHub. |
| `02-estructura.png` | Organización de los archivos y directorios. |
| `03-docker-version.png` | Versión de Docker y Docker Compose. |
| `04-build.png` | Construcción satisfactoria de las imágenes. |
| `05-contenedores.png` | Contenedores ejecutándose mediante Docker Compose. |
| `06-red-docker.png` | Red de comunicación configurada. |
| `07-servicio-1.png` | Respuesta del Servicio 1. |
| `08-servicio-2.png` | Respuesta del Servicio 2. |
| `09-comunicacion.png` | Respuesta satisfactoria de la comunicación entre servicios. |
| `10-healthchecks.png` | Comprobación del estado de salud de los contenedores. |

Las capturas deben corresponder a las ejecuciones reales del proyecto y permitir identificar claramente los resultados obtenidos.

## 11. Conclusiones

Durante el desarrollo de esta primera entrega se implementó una arquitectura de software compuesta por dos servicios independientes, utilizando Docker como herramienta de contenerización.

La utilización de Docker Compose facilitó la administración de los contenedores, la configuración de los puertos y la creación de una red interna para establecer la comunicación entre las aplicaciones.

Asimismo, mediante Flask y Requests se desarrollaron dos API REST que permitieron demostrar el intercambio de información entre contenedores a través de solicitudes HTTP.

Se comprobó que ambos servicios podían ejecutarse de manera independiente y que el Servicio 2 podía consumir correctamente los endpoints proporcionados por el Servicio 1.

Finalmente, la implementación permitió establecer una base técnica para continuar con las siguientes entregas del proyecto, incorporando progresivamente nuevos mecanismos de automatización e integración continua.

## 12. Referencias

- [GitHub Documentation](https://docs.github.com/es)
- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Python Documentation](https://docs.python.org/3/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Requests Documentation](https://requests.readthedocs.io/)

## 13. Información del proyecto

**Institución:** Politécnico Grancolombiano.

**Módulo:** Integración Continua.

**Entrega:** Primera entrega – Semana 3.

**Repositorio:** [U_Integracion-Continua](https://github.com/SebastianMartinezLesmes/U_Integracion-Continua)

**Estado de la implementación:** Finalizada, con resultados satisfactorios en las pruebas descritas.