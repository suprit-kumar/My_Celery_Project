from django.shortcuts import render
from django.http import HttpResponse
from .tasks import mail_func
# Create your views here.
from django_celery_beat.models import PeriodicTask,IntervalSchedule,CrontabSchedule
import string
import random
import json
def send_mail_task(request):
    print("Sending mail")
    mail_func.delay()
    return HttpResponse("Mail Sent")


def schedule_mail(request):
    name = id_generator()
    # schedule,created = CrontabSchedule.objects.get_or_create(hour=22,minute=34)
    schedule,created = IntervalSchedule.objects.get_or_create(every=2,period=IntervalSchedule.MINUTES)
    task = PeriodicTask.objects.create(
        # crontab=schedule,
        interval=schedule,
        name=f"schedule_task_{name}",
        task= "mail_app.tasks.mail_func",
        kwargs = json.dumps({"execute":"Something.."})
    )
    return HttpResponse("Mail Scheduled")

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))