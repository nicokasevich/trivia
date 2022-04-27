web: gunicorn app.wsgi:application
release: python3 manage.py migrate
release: python3 manage.py addquestions
release: python3 manage.py createsuperuser