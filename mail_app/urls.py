from django.urls import path, include
from . import views
urlpatterns = [
    path('send-mail/',views.send_mail_task,name="send-mail"),
]
