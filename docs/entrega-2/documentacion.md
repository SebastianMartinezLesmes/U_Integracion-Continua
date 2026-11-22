# DOCUMENTACIÓN TÉCNICA – SEGUNDA ENTREGA
## Implementación de Jenkins como gestor de operaciones

**Proyecto:** U_Integracion-Continua  
**Institución:** Politécnico Grancolombiano  
**Integrantes:** Juan Martinez Lesmes, Duban José Vargas Salas y Edward Reyes Corredor  
**Año:** 2026

---

# 1. Introducción

El presente documento describe el proceso de construcción, configuración y ejecución de la segunda entrega del proyecto de Integración Continua, cuyo objetivo es implementar **Jenkins como gestor de operaciones**.

La solución utiliza dos servicios desarrollados en Python con Flask, ejecutados mediante contenedores Docker y conectados a través de una red interna.

En esta segunda entrega se busca incorporar Jenkins para automatizar las actividades de construcción, ejecución y validación del proyecto, permitiendo comprobar que los servicios funcionan correctamente y que existe comunicación entre ellos.

La implementación utiliza las siguientes tecnologías:

- **Python y Flask:** desarrollo de los servicios web.
- **Docker:** creación y ejecución de contenedores.
- **Docker Compose:** administración de los servicios y su infraestructura.
- **Git y GitHub:** control de versiones y almacenamiento del código.
- **Jenkins:** automatización y administración del pipeline de integración continua.

# 2. Objetivos

## 2.1. Objetivo general

Implementar Jenkins como gestor de operaciones para automatizar la construcción, ejecución y validación de los servicios que conforman el proyecto de integración continua.

## 2.2. Objetivos específicos

1. Configurar Jenkins para obtener el código fuente desde un repositorio GitHub.
2. Automatizar la construcción de las imágenes Docker.
3. Gestionar el inicio y ejecución de los contenedores.
4. Implementar pruebas automatizadas para verificar la disponibilidad de los servicios.
5. Comprobar la comunicación entre los dos servicios Flask.
6. Documentar los procedimientos de configuración, ejecución y validación del proyecto.

# 3. Arquitectura del proyecto

El proyecto está compuesto por dos servicios independientes que se comunican mediante una red interna de Docker Compose.

| Componente | Descripción | Puerto |
|---|---|---|
| Servicio 1 | API principal que recibe y procesa solicitudes | 5000 |
| Servicio 2 | API que consume los recursos del Servicio 1 | 5001 |
| Jenkins | Gestor de operaciones y automatización | 8080 |
| Docker | Plataforma de contenedores | N/A |
| GitHub | Repositorio de código fuente | N/A |

## 3.1. Comunicación entre servicios

El Servicio 2 realiza solicitudes HTTP al Servicio 1 utilizando la dirección interna:

`http://servicio-1:5000`

Esta comunicación se realiza mediante la red Docker denominada:

`red-integracion`

Es importante tener en cuenta que, cuando un contenedor necesita comunicarse con otro, debe utilizar el nombre del servicio definido en Docker Compose y no `localhost`.

## 3.2. Flujo de funcionamiento

El flujo general de la solución es:

1. El desarrollador publica los cambios en GitHub.
2. Jenkins obtiene el código fuente del repositorio.
3. Jenkins valida la configuración de Docker Compose.
4. Jenkins construye las imágenes de los servicios.
5. Docker inicia los contenedores.
6. Jenkins ejecuta las pruebas de disponibilidad.
7. Se verifica la comunicación entre los servicios.
8. Jenkins presenta el resultado de la ejecución.

# 4. Requisitos previos

Para construir y ejecutar el proyecto se necesitan las siguientes herramientas:

| Herramienta | Función |
|---|---|
| Windows 10/11 | Sistema operativo |
| Docker Desktop | Administración del motor Docker |
| Docker Compose | Orquestación de contenedores |
| Python 3.12 | Lenguaje utilizado por los servicios |
| Git | Control de versiones |
| GitHub | Repositorio remoto |
| Jenkins | Automatización del proceso |

## 4.1. Verificar las instalaciones

Abrir PowerShell y ejecutar:

```powershell
git --version
docker --version
docker compose version
docker info