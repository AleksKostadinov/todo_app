from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View

from app.forms import TaskForm
from app.models import Task


class TaskList(ListView):
    model = Task
    template_name = 'app/index.html'
    context_object_name = 'tasks'

    # Use context in navbar.html to show tasks to logged user and their counts
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        # Add form to context
        context['form'] = TaskForm()

        return context


class TaskDetail(DetailView):
    model = Task
    template_name = 'app/detail.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = context['task']
        if not task.description:
            context['description'] = 'No description'
        return context


class TaskCreate(CreateView):
    # specifies the model to use for creating new tasks
    model = Task
    # specifies the fields to include in the form for creating new tasks. In this case, it only includes the title field
    fields = ['title']
    # specifies the template to use for rendering the view. In this case, it's using the index.html template
    template_name = 'app/index.html'
    # specifies the URL to redirect to after a successful form submission. In this case, it redirects to the index URL
    success_url = reverse_lazy('index')

    # is a method that gets called when the form is valid.
    # It sets the user field of the Task instance to the current user before saving it to the database.
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

    # is a method that gets called when the form is submitted via POST.
    # It gets the form, checks if it's valid, and either calls form_valid or form_invalid depending on the result
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class TaskUpdate(UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('index')


class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'app/delete.html'
    success_url = reverse_lazy('index')

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)


class TaskDeleteCompleted(View):
    @staticmethod
    def post(request, *args, **kwargs):
        # Get all completed tasks
        completed_tasks = Task.objects.filter(complete=True)
        # Delete completed tasks
        completed_tasks.delete()
        # Redirect to the task list page
        return redirect('index')


