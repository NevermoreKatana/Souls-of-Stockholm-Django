docker-build:
	docker-compose up --build

install:
	./build.sh

start-dev:
	poetry run python manage.py runserver

secretkey:
	poetry run python -c 'from django.utils.crypto import get_random_string; print(get_random_string(40))'

start-production:
	poetry run gunicorn -b 0.0.0.0:8000 souls_of_stockholm.wsgi:application

migration:
	poetry run python manage.py migrate

make lint:
	poetry run flake8 souls_of_stockholm