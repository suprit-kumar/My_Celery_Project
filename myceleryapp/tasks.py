from celery import shared_task
from celery.signals import task_prerun,task_postrun

@shared_task(bind=True)
def loop_task(self):
    # operation
    for i in range(10):
        print(i)
    return "Done"