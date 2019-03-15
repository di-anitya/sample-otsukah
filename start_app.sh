#!/bin/sh

python anitya/manage.py migrate
python anitya/manage.py runserver
