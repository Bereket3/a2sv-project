from django.db import models


class TaskModel(models.Model):
    """
    model schima for creating tasks
    """
    title = models.CharField(max_length = 200)
    description = models.TextField()
    due_date = models.DateTimeField(blank = True, null = True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True) 


    def __str__(self) -> str:
        return self.title