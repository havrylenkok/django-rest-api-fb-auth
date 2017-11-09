`cd djangorestapifbauth`

`psql`

`create database dbname;`

`mkvirtualenv djangorestapifbauth
workon djangorestapifbauth`

`pip install -r requirements.txt`

create djangorestapifbauth/settings_local.py with database connection info:
~~~~~

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbname',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

# IG configuration
SOCIAL_AUTH_INSTAGRAM_KEY = ''
SOCIAL_AUTH_INSTAGRAM_SECRET = ''

ALLOWED_HOSTS = ['localhost']

~~~~~~

`python manage.py migrate`

`python manage.py runserver`

open browser on `localhost:8000`

For auth client_id key use client_id from admin/DJANGO OAUTH TOOLKIT application.
