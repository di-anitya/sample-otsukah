#!/bin/sh
SCRIPT_DIR=$(cd $(dirname $0); pwd)

python ${SCRIPT_DIR}/anitya/manage.py migrate
python ${SCRIPT_DIR}/anitya/manage.py runserver
