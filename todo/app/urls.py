from django.urls import path

from app.views import TaskList

urlpatterns = [
    path('', TaskList.as_view(), name='index'),
]
