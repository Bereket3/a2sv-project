# rest framework import
from rest_framework import generics

# project import
from .serializer import Taskserializer, TaskModel


class ListAndCreateTaskAPIView(generics.ListAPIView, generics.CreateAPIView):
    """
    will perform the following tasks

        * create an instance of task object
        * list all task objects in the database
    """
    queryset = TaskModel.objects.all()
    serializer_class = Taskserializer


class UpdateListAndDeleteApiView(generics.UpdateAPIView, generics.RetrieveAPIView, generics.DestroyAPIView):
    """
    Will perform the following tasks

        * update using id of the instance
        * delete using id 
        * get instance by id and return it
    
    in the request it search for
        * title
        * description 
        * due to date (optional)
    """
    lookup_field = 'id'
    queryset = TaskModel
    serializer_class = Taskserializer