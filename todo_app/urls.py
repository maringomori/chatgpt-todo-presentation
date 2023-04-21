from django.urls import path
from .views import TodoItemAPIView, UnfinishedTodosAPIView, FinishedTodosAPIView, SubtaskListAPIView

urlpatterns = [
    path('todos/', TodoItemAPIView.as_view(), name='todo-list'),
    path('todos/unfinished/', UnfinishedTodosAPIView.as_view(), name='unfinished-todos'),
    path('todos/finished/', FinishedTodosAPIView.as_view(), name='finished-todos'),
    path('todos/<int:parent_task_id>/subtasks/', SubtaskListAPIView.as_view(), name='subtask-list')
]
