MANAGE := poetry run python3 manage.py

start:
	poetry run python3 manage.py runserver 0.0.0.0:8000

test:
	@poetry run pytest

setup: db-clean install migrate

install:
	@poetry install

db-clean:
	@rm db.sqlite3 || true

migrate:
	@$(MANAGE) migrate

makemigrations:
	@$(MANAGE) makemigrations

shell:
	@$(MANAGE) shell_plus --ipython

lint:
	@poetry run flake8 task_manager

tests-cov:
	poetry run pytest --cov=task_manager --cov-report xml

.PHONY: start test setup install clean migrate makemigrations shell lint tests-cov