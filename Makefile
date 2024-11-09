#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = mlops_homework
PYTHON_VERSION = 3.10
PYTHON_INTERPRETER = python
DOCKER_COMPOSE_FILE = docker-compose.yml

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Установка зависимостей через Poetry
.PHONY: install
install:
	poetry install

## Активировать виртуальное окружение Poetry
.PHONY: shell
shell:
	poetry shell

## Создание .env файла с настройками MinIO
.PHONY: env
env:
	echo "MINIO_ROOT_USER=admin" >> .env
	echo "MINIO_ROOT_PASSWORD=password" >> .env

#################################################################################
# DOCKER RULES                                                                  #
#################################################################################

## Собрать и запустить контейнеры Docker
.PHONY: docker-up
docker-up:
	docker-compose -f $(DOCKER_COMPOSE_FILE) up --build

## Остановить контейнеры Docker
.PHONY: docker-down
docker-down:
	docker-compose -f $(DOCKER_COMPOSE_FILE) down

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys; \
lines = '\n'.join([line for line in sys.stdin]); \
matches = re.findall(r'\n## (.*)\n[\s\S]+?\n([a-zA-Z_-]+):', lines); \
print('Доступные команды:\n'); \
print('\n'.join(['{:25}{}'.format(*reversed(match)) for match in matches]))
endef
export PRINT_HELP_PYSCRIPT

help:
	@$(PYTHON_INTERPRETER) -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)
