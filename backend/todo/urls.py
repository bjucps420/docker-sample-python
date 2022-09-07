from django.urls import path

from . import views

urlpatterns = [
    path('api/todo/list', views.todo_list, name='list_todos'),
]