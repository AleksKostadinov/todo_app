from django.urls import path

from app.views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, TaskDeleteCompleted

urlpatterns = [
    path('', TaskList.as_view(), name='index'),
    path('detail/<int:pk>/', TaskDetail.as_view(), name='detail'),
    path('create/', TaskCreate.as_view(), name='create'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='delete'),
    path('delete_completed/', TaskDeleteCompleted.as_view(), name='delete_completed'),
]
