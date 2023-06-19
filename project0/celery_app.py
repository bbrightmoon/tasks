import os
import time

from celery.signals import setup_logging
from celery import Celery


app = Celery('celery')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project0.settings.base')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@setup_logging.connect
def config_loggers(*args, **kwargs):
    from logging.config import dictConfig
    from django.conf import settings

    dictConfig(settings.LOGGING)
