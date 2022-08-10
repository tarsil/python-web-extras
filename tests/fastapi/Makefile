.DEFAULT_GOAL := help

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean: clean_pyc ## Clean all PYC in the system

.PHONY: clean_pyc
clean_pyc: ## Cleans all *.pyc in the system
	find . -type f -name "*.pyc" -delete || true

.PHONY: requirements
requirements: ## Installs the requirements
	pip install -r requirements/requirements.txt

.PHONY: requirements-dev
requirements-dev: ## Installs the requirements for dev
	pip install -r requirements/requirements-dev.txt

.PHONY: docker-no-log
docker-no-logs: ##  Starts the docker compose without stdout logs
	docker-compose up -d

.PHONY: docker-stop
docker-stop: ## Stops the docker containers
	docker-compose stop

.PHONY: run
run: ## Starts the local server with production settings
	FASTAPI_SETTINGS_MODULE='core.configs.settings' python -m src.serve

.PHONY: run-dev
run-dev: ## Starts the local server
	FASTAPI_SETTINGS_MODULE='core.configs.development.settings' python -m src.serve

.PHONY: run-custom
run-custom: ## Starts the server by passing a custom settings file `FLASK_SETTINGS_FILENAME`
	FASTAPI_SETTINGS_MODULE=$(FASTAPI_SETTINGS_MODULE) python -m src.serve

.PHONY: test
test: ## Runs the local tests with nose
	FASTAPI_SETTINGS_MODULE='core.configs.testing.settings' pytest -s $(TESTONLY) $(DB)

.PHONY: mypy
mypy: ## Runs the typing analyser
	mypy src/

ifndef VERBOSE
.SILENT:
endif