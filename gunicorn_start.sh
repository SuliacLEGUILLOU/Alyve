#!/bin/bash

NAME="alyve"
DJANGODIR=/home/alysson/Development/alyve
SOCKFILE=/home/alysson/Development/alyve/gunicorn.sock
USER=alysson
GROUP=alysson
NUM_WORKERS=3
DJANGO_SETTING_MODULE=alyve.settings
DJANGO_WSGI_MODULE=alyve.wsgi

echo "Starting $NAME as $(whoami)"

cd $DJANGODIR
source ../virtualenvs/blog/bin/activate

export DJANGO_SETTING_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

gunicorn ${DJANGO_WSGI_MODULE}:application \
    --name $NAME \
    --workers $NUM_WORKERS \
    --user=$USER --group=$GROUP \
    --bind=unix:$SOCKFILE \
    --log-level=debug \
    --log-file=-
