Уважаемый ревьюер!

Для удобства ниже команды для запуска проекта:

$ docker-compose -f docker-compose.prod.yml up -d --build
$ docker-compose -f docker-compose.prod.yml exec db psql -U USERNAME -d DBNAME
    CREATE SCHEMA content;
$ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
$ docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear

Так же, наставники сказали, что переменные окружения вы сгенерите самостоятельно.
На всякий случай описание ниже:

.env.dev
DB_ENGINE=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
DJANGO_SK=
DEBUG=
ALLOWED_HOSTS=
DATABASE=

.env.prod
DEBUG=0
DJANGO_SK=
ALLOWED_HOSTS=
DB_ENGINE=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
DATABASE=

.env.prod.db
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=