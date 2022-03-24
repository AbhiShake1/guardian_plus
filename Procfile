web: gunicorn fyp_music_app_backend_nischal.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
python manage.py migrate
