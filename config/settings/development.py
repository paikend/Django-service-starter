from .base import *


ALLOWED_HOSTS = ['*']

# redirect URL
REDIRECT_URL = 'http://localhost:3000'


# email setiing
with open('etc/email.txt') as email:
    EMAIL_HOST_USER = email.readline().strip()
    EMAIL_HOST_PASSWORD = email.readline().strip()

# django-debug-toolbar
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
INTERNAL_IPS = ['127.0.0.1']

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

with open('etc/dev_db.txt') as db_info:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': db_info.read().strip(),
            'USER': db_info.read().strip(),
            'PASSWORD': db_info.read().strip(),
            'HOST': db_info.read().strip(),
            'PORT': db_info.read().strip(),
            'ATOMIC_REQUESTS': True,
        }
    }

# enable http oauth token transport in requests-oauthlib
# WARNING: only set for dev env
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


# drf-yasg
INSTALLED_APPS += ['drf_yasg']
