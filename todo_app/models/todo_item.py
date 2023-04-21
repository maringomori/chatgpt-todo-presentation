from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    parent_task = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subtasks')

    def __str__(self):
        return self.title
