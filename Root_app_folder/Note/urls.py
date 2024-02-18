# django imports
from django.urls import path


# project view applications
from .views import (
    ListAndCreateTaskAPIView,
    UpdateListAndDeleteApiView
)


urlpatterns = [
    path('', ListAndCreateTaskAPIView.as_view(), name='list-task'),
    path('<str:id>', UpdateListAndDeleteApiView.as_view(), name='update-task'),
]