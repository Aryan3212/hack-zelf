# django_db_task/celery.py

import os
from celery import Celery

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 
    'hack_zelf.settings'
)

app = Celery('hack_aggregator')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()