#!/bin/sh
SCRIPT_DIR=$(cd $(dirname $0); pwd)

pip install -r ${SCRIPT_DIR}/requirements.txt

sh ${SCRIPT_DIR}/initialize.sh
