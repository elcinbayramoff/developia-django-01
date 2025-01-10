"""
Base url = 127.0.0.1:8000/


127.0.0.1:8000/ -> Home 

127.0.0.1:8000/tasks -> Tasklar

127.0.0.1:8000/tasks/3 -> spesifik task
"""
from django.urls import path
from .views import home, tasks, task_specific, task_create
urlpatterns = [
    path('', home, name='home'),
    path('tasks', tasks, name='tasks'),
    path('tasks/<int:task_id>', task_specific, name='task_specific'),
    path('tasks/new', task_create, name='task_create'),
]