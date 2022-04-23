all:
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

build: ## Build images and run the containers
	@[ -f .env ] || cp .env.example .env
	@[ -f postgres/.env ] || cp postgres/.env.example postgres/.env
	@docker-compose build
	@docker-compose up -d

create-db: ## Reset demo-data to postgres container
	@docker-compose exec postgres chown -R postgres /backup
	@docker-compose exec --user="postgres" postgres /bin/bash -c "psql -c 'DROP DATABASE sisnatdb'" || true
	@docker-compose exec --user="postgres" postgres /bin/bash -c "psql -c 'CREATE DATABASE sisnatdb ENCODING 'UTF8' TEMPLATE template0'" || true
	@docker-compose exec backend python manage.py migrate
	@docker-compose exec backend python manage.py createsuperuser

up: ## Start containers and run the project in dev mode
	@docker-compose start
	@docker-compose exec backend /deploy/run.sh

down: ## Stop containers
	@docker-compose stop

remove: ## Rmove all containers
	@docker-compose down

cmd: ## Command line of backend project
	@docker-compose exec backend /bin/bash

django-shell: ## Run Django Shell
	@docker-compose exec backend python manage.py shell

restart: ## Restart all containers
	@docker-compose restart

psql: ## Attach to psql inside postgres container
	@docker-compose exec --user postgres postgres psql sisnatdb

psql-cmd: ## Command line inside postgres container
	@docker-compose exec --user postgres postgres /bin/bash

.DEFAULT_GOAL := help