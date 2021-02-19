from .base import *


ALLOWED_HOSTS = ["*"]

# redirect URL
REDIRECT_URL = "http://localhost:3000"


# email setiing
EMAIL_HOST_USER = os.getenv("EMAIL", "test@admin.com")
EMAIL_HOST_PASSWORD = os.getenv("PASSWORD", "admin")

# django-debug-toolbar
INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
INTERNAL_IPS = ["127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DB_NAME", "testdatabase"),
        "USER": os.getenv("DB_USER", "root"),
        "PASSWORD": os.getenv("DB_PASSWORD", "admin12345"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
        "ATOMIC_REQUESTS": True,
    }
}

# enable http oauth token transport in requests-oauthlib
# WARNING: only set for dev env
import os

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


# drf-yasg
INSTALLED_APPS += ["drf_yasg"]
