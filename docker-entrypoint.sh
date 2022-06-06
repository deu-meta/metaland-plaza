#!/bin/bash

# wait until db ready
/wait-for-it.sh -t 0 $MTL_PLAZA_DB_HOST:$MTL_PLAZA_DB_PORT

if [ -z "$MTL_PLAZA_PORT" ]; then
    export MTL_PLAZA_PORT=8000
fi

if [ -z "$MTL_PLAZA_BIND_ADDRESS" ]; then
    export MTL_PLAZA_BIND_ADDRESS=0.0.0.0
fi

command_args=$@
if [ -z "$command_args" ]; then
    command_args="runserver $MTL_PLAZA_BIND_ADDRESS:$MTL_PLAZA_PORT"
fi

# if something get wrong, do not run server
python manage.py migrate --noinput || exit 1

# important! last line should be exec, so the process can receive SIGTERM from docker stop.
exec python manage.py $command_args