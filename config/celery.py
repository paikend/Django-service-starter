from __future__ import absolute_import, unicode_literals
import os
from django.apps import apps
from django.conf import settings
import django
from celery import Celery

if ("DJANGO_SETTINGS_MODULE" in os.environ) and (
    os.environ["DJANGO_SETTINGS_MODULE"] == "config.settings.prod"
):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.prod")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")

app = Celery("config", backend="redis://", broker="redis://localhost:6379/0")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
