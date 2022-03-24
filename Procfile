web: gunicorn guardian_plus.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
python manage.py migrate
