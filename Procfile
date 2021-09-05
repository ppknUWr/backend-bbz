prepare: cd src && python3 manage.py makemigrations && python3 manage.py migrate
web: cd src && gunicorn bbz_project.wsgi --log-file - 
