`cd instagramauthdemo`

`psql

create database instagramauthdemo;`

`mkvirtualenv instagramauthdemo
workon instagramauthdemo`

`pip install -r requirements.txt`

create instagramauthdemo/settings_local.py with database connection info:
~~~~~

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'instagramauthdemo',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

# Facebook configuration
SOCIAL_AUTH_FACEBOOK_KEY = ''
SOCIAL_AUTH_FACEBOOK_SECRET = ''

~~~~~~

`python manage.py migrate`

`python manage.py runserver`

open browser on `localhost:8000`

For auth client_id key use client_id from admin/DJANGO OAUTH TOOLKIT application.
