#!/bin/sh

python manage.py collectstatic --no-input
python manage.py migrate --no-input

gunicorn --bind :8000 --workers 2 sensor_api.asgi:application -k uvicorn.workers.UvicornWorker
