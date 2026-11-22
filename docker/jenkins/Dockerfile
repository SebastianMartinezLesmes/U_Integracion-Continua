FROM docker:cli AS docker-cli

FROM jenkins/jenkins:lts-jdk21

USER root

# Incorporar Docker CLI y Docker Compose
COPY --from=docker-cli /usr/local/bin/docker /usr/local/bin/docker

COPY --from=docker-cli \
    /usr/local/libexec/docker/cli-plugins/docker-compose \
    /usr/local/lib/docker/cli-plugins/docker-compose

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

ENV DOCKER_CONFIG=/root/.docker