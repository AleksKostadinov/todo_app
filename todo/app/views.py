from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View, FormView

from app.forms import TaskForm
from app.models import Task


class TaskLoginView(LoginView):
    template_name = 'app/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')


# class TaskLogoutView(LogoutView):
#     next_page = 'login'

class RegisterView(FormView):
    template_name = 'app/register.html'
    # A form that creates a user:
    form_class = UserCreationForm
    # boolean flag that indicates whether or not authenticated users should be redirected to the 'success_url':
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    # is called when the form is successfully submitted and validated.
    # It saves the user object and logs them in using Django's built-in login() function:
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        # return super(RegisterView, self).form_valid(form)
        return super().form_valid(form)

    # is called when the view is accessed with an HTTP GET request.
    # If the user is already authenticated, he will be redirected to the 'success_url':
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        # return super(RegisterView, self).get(*args, **kwargs)
        return super().get(*args, **kwargs)

    # the get() method in this code is used for checking authentication and rendering the registration form,
    # while the form_valid() method is used for handling the form submission and saving the new user object


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'app/index.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        # Filter tasks by current user
        return Task.objects.filter(user=self.request.user)

    # Use context in navbar.html to show tasks to logged user and their counts
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = context['tasks'].filter(user=self.request.user,complete=False).count()

        # Add form to context
        context['form'] = TaskForm()

        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'app/detail.html'
    context_object_name = 'task'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = context['task']
        if not task.description:
            context['description'] = 'No description'
        return context


class TaskCreate(LoginRequiredMixin, CreateView):
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
        return super().form_valid(form)

    # is a method that gets called when the form is submitted via POST.
    # It gets the form, checks if it's valid, and either calls form_valid or form_invalid depending on the result
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)

        return self.form_invalid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('index')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'app/delete.html'
    success_url = reverse_lazy('index')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    # def get_queryset(self):
    #     owner = self.request.user
    #     return self.model.objects.filter(user=owner)


class TaskDeleteCompleted(LoginRequiredMixin, View):

    @staticmethod
    def post(request, *args, **kwargs):
        # Get all completed tasks for the user who owns them
        completed_tasks = Task.objects.filter(user=request.user, complete=True)
        # Delete completed tasks
        completed_tasks.delete()
        # Redirect to the task list page
        return redirect('index')
