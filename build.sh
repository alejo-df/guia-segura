#!/usr/bin/env bash
# build.sh - Script de construccion para Render

set -o errexit

pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
