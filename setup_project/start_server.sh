#!/bin/bash
cd ../server
source server_venv/bin/activate
python manage.py runserver 8000
