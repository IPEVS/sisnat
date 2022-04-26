#!/bin/bash

if [[ $1 = 'prod' ]]
then
    python /deploy/sisnat/manage.py compilemessages
    python /deploy/sisnat/manage.py collectstatic --no-input
    python /deploy/sisnat/manage.py migrate
    cd /deploy/sisnat
    uwsgi --http 0.0.0.0:8000 --module sisnat.wsgi --processes=5
else
    python /deploy/sisnat/manage.py compilemessages
    python /deploy/sisnat/manage.py migrate
    python /deploy/sisnat/manage.py runserver 0.0.0.0:8000
fi