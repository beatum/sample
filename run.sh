#!/usr/bin/env bash

python manage.py rqworker & python manage.py rqscheduler & python manage.py rqjobs & python manage.py runserver 0.0.0.0:8000