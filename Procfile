web: gunicorn backend-bbz.wsgi --log-file - --log-level debug
python3 manage.py collectstatic --noinput
manage.py migrate