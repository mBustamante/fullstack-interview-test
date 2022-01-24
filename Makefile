
serve:
	docker-compose up --build

build:
	docker-compose build

up:
	docker-compose up -d

bash:
	docker-compose exec web-api bash

stop:
	docker-compose down

restart:
	docker-compose restart

start: ## start project
	@make build
	@make up

shell:
	docker-compose exec web-api python manage.py shell

makemigrations:
	docker-compose exec web-api python manage.py makemigrations

migrate:
	docker-compose exec web-api python manage.py migrate

createsuperuser:
	docker-compose exec web-api python manage.py createsuperuser

collectstatic:
	docker-compose exec web-api python manage.py collectstatic