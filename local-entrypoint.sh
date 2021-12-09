#!/bin/sh

#cd portal
pwd
pip install -r portal/requirements.txt 
python -W ignore portal/manage.py migrate
python -W ignore portal/manage.py migrate --run-syncdb
python -W ignore portal/manage.py createsuperuser
python -W ignore portal/manage.py collectstatic --noinput
#cp local_settings_sample.py local_settings.py
#sed --in-place "s/^SECRET_KEY = .*/SECRET_KEY = 'sarasa'/" local_settings.py
# Then exec the container's main process (what's set as CMD in the Dockerfile).
exec "$@"
