#!/bin/sh
SCRIPT_DIR=$(cd $(dirname $0); pwd)

TARGETS=(accounts infrastructures deployments testings monitorings)

for TARGET in ${TARGETS[@]}; do
  rm -rf ${SCRIPT_DIR}/anitya/${TARGET}/migrations
done

rm -f ${SCRIPT_DIR}/anitya/db.sqlite3

for TARGET in ${TARGETS[@]}; do
  python ${SCRIPT_DIR}/anitya/manage.py makemigrations ${TARGET}
done

python ${SCRIPT_DIR}/anitya/manage.py migrate

python ${SCRIPT_DIR}/anitya/manage.py loaddata ${SCRIPT_DIR}/anitya/accounts/fixtures/user.json
python ${SCRIPT_DIR}/anitya/manage.py loaddata ${SCRIPT_DIR}/anitya/infrastructures/fixtures/driver.json
python ${SCRIPT_DIR}/anitya/manage.py loaddata ${SCRIPT_DIR}/anitya/infrastructures/fixtures/physical.json
python ${SCRIPT_DIR}/anitya/manage.py loaddata ${SCRIPT_DIR}/anitya/infrastructures/fixtures/virtual.json
