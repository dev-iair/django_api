#!/bin/bash

cd /app  
gunicorn django_api.wsgi:application -c gunicorn_config.py