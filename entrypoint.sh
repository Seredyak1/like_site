#!/bin/bash

python /code/manage.py collectstatic --no-input
python /code/manage.py migrate
gunicorn likesite.wsgi:application --workers 3 --bind 0.0.0.0:8000
