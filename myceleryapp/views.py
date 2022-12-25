from django.http import HttpResponse
from django.shortcuts import render
from .tasks import loop_task
# Create your views here.

def check_loop_task(request):
    # Calling celery task
    print("Inside check loop task")
    loop_task.delay()
    return HttpResponse("Done")

