# rest framework import
from rest_framework.serializers import ModelSerializer


# Project import
from .models import TaskModel


class Taskserializer(ModelSerializer):
    """
    serializer for the task model
    """
    
    class Meta:
        model = TaskModel
        fields = [
            'title',
            'description',
            'due_date'
        ]
    