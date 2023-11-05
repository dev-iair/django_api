#!/bin/bash

cd /app/django_api  
gunicorn django_api.wsgi:application -c gunicorn_config.py