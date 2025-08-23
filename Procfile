web: python manage.py migrate && python manage.py collectstatic --noinput && gunicorn backend_analytics_server.wsgi:application --bind 0.0.0.0:$PORT --log-file -
