from celery import shared_task
from django.core.mail import send_mail
from MyCeleryProject import settings
from celery.signals import task_prerun,task_postrun


@shared_task(bind=True)
def mail_func(self,**kwargs):
    # operation
    users = [] # include the email list
    for user in users:
        mail_subject = "Hi! Celery Testing"
        message = "This is a Celery Testing mail. Please ignore this."
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user],
            fail_silently=True,
        )
    return "Mail Sent"


@task_prerun.connect
def rcv_task_prerun(task_id, task, *args, **kwargs):
    print("--------------Inside pre run ----------------")
    print(f'task.name: {task.name}')


@task_postrun.connect
def rcv_task_postrun(sender=None, state=None, **kwargs):
    print("--------------Inside post run ----------------")
    execute = kwargs.get('kwargs', {}).get('execute')
    print(f"kwargs: {kwargs}")
    print(f"execute: {execute}")
    print(f"state: {state}")
    if execute and state == 'SUCCESS':
        print("Task Succeeded Received on Post run")
