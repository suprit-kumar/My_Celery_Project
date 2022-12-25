from django.shortcuts import render
from django.http import HttpResponse
from .tasks import mail_func
# Create your views here.

def send_mail_task(request):
    print("Sending mail")
    mail_func.delay()
    return HttpResponse("Mail Sent")