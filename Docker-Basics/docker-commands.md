# Docker Commands

## Images
- docker images → list images
- docker pull nginx → download image

## Containers
- docker ps → running containers
- docker ps -a → all containers
- docker run nginx → start container
- docker stop <id> → stop container
- docker rm <id> → remove container

## Build
- docker build -t appname . → build image

## Logs
- docker logs <container_id>