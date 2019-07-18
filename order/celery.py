from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'likesite.settings')

app = Celery('like_site', broker=settings.BROKER_URL)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.timezone = settings.TIME_ZONE
app.conf.beat_schedule = {
    'send-report-every-9-oclock': {
        'task': 'order.tasks.send_report_for_open_order',
        'schedule': crontab(minute='25', hour='11'),
    },
}
