web: gunicorn app.wsgi:application
release: python manage.py migrate
release: python manage.py addquestions
release: python manage.py createsuperuser