#!/bin/sh

python manage.py collectstatic --noinput
python manage.py migrate --no-input

gunicorn --bind :8000 --workers 2 sensor_api.asgi:application -k uvicorn.workers.UvicornWorker
