from django import forms
from .models import Task

class NewTask(forms.ModelForm):
    #name = forms.CharField(required=True, max_length=45)
    #description = forms.CharField(required=True, max_length=100)


    class Meta:
        model = Task
        exclude = ('isDone', 'Task name:', 'Task description:')