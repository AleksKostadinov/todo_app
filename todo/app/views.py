from django.views.generic import ListView

from app.models import Task


class TaskList(ListView):
    model = Task
    template_name = 'app/index.html'
    context_object_name = 'tasks'

