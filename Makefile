install:
	poetry install

dev:
	poetry run fastapi dev app/main.py

lint:
	poetry run flake8 app
