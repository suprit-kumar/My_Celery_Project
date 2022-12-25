from django.urls import path
from . import views
urlpatterns = [
    path('', views.check_loop_task,name='loop-task'),

]
