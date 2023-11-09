from django.urls import path
from . import views

urlpatterns = [
    path('',views.todo_index,name='todo_index'),
    path('todo/<int:pk>',views.todo_detail,name='todo_detail')
    
]