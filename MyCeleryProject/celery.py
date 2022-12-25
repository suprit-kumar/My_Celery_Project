from __future__ import absolute_import,unicode_literals

import os

from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyCeleryProject.settings')

app = Celery('MyCeleryProject')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')
app.config_from_object(settings, namespace='CELERY')


app.conf.beat_schedule = {
    # #Scheduler Name
    # 'print-message-ten-seconds': {
    #     # Task Name (Name Specified in Decorator)
    #     'task': 'print_msg_main',
    #     # Schedule
    #     'schedule': 10.0,
    #     # Function Arguments
    #     'args': ("Hello",)
    # },
}





# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')