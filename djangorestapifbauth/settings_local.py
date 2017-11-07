DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangorestfbdemo',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

# Facebook configuration
SOCIAL_AUTH_FACEBOOK_KEY = '128069727890777'
SOCIAL_AUTH_FACEBOOK_SECRET = 'fd4fc57cab15960b583b1c0a996995ba'