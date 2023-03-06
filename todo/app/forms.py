from django import forms
from app.models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=40, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Todo', 'aria-label': 'Todo',
               'aria-describedby': 'add-btn'}
    ))

    class Meta:
        model = Task
        fields = ['title']
