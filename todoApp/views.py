from django.shortcuts import render
from todoApp.forms import NewTask
from todoApp.models import Task
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request, 'home.html')

def todo(request):
    if request.method == "POST":
        form = NewTask(request.POST)
        if form.is_valid():
            newTaskAdded = form.save(commit=False)
            newTaskAdded.save()
            return HttpResponseRedirect('/to-do-list')
    else:

        form = NewTask()
        return render(request, 'todo.html', {'tasks' : Task.objects.all(), 'form': form})

def practice(request):
    return render(request, 'practice.html', )