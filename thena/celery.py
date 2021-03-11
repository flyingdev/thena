import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'thena.settings')

app = Celery('thena')

app.config_from_object('django.conf.settings', namespace='CELERY')

app.autodiscover_tasks()
