MANAGE := poetry run python3 manage.py
PORT := 8000

dev:
	poetry run python3 manage.py runserver 0.0.0.0:8000

start:
	python3 manage.py migrate
	gunicorn task_manager.wsgi --bind 0.0.0.0:$(PORT)

test:
	@$(MANAGE) test

setup: db-clean install migrate

install:
	@poetry install

db-clean:
	@rm db.sqlite3 || true

migrate:
	@$(MANAGE) migrate

makemigrations:
	@$(MANAGE) makemigrations

lint:
	@poetry run flake8 task_manager

tests-cov:
	poetry run pytest --cov=task_manager --cov-report xml

.PHONY: start test setup install clean migrate makemigrations shell lint tests-cov dev
