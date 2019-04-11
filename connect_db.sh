#!/bin/sh

SCRIPT_DIR=$(cd $(dirname $0); pwd)

sqlite3 ${SCRIPT_DIR}/anitya/db.sqlite3
