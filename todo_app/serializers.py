from rest_framework import serializers
from .models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    subtasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = TodoItem
        fields = ('id', 'title', 'description', 'completed', 'parent_task', 'subtasks')
