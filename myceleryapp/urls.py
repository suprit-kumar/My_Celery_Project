from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('loop_task/', views.check_loop_task,name='loop-task'),

]
