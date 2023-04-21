from rest_framework import generics
from .models import TodoItem
from .serializers import TodoItemSerializer

class TodoItemAPIView(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class UnfinishedTodosAPIView(generics.ListAPIView):
    queryset = TodoItem.objects.filter(completed=False)
    serializer_class = TodoItemSerializer

class FinishedTodosAPIView(generics.ListAPIView):
    queryset = TodoItem.objects.filter(completed=True)
    serializer_class = TodoItemSerializer

class SubtaskListAPIView(generics.ListAPIView):
    serializer_class = TodoItemSerializer

    def get_queryset(self):
        parent_task_id = self.kwargs['parent_task_id']
        print(parent_task_id)
        return TodoItem.objects.filter(parent_task_id=parent_task_id) 
    