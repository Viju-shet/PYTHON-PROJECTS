from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        new_task = Task(title=request.POST['title'])
        new_task.save()
        return redirect('task_list')
    return render(request, 'todo/add_task.html')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.title = request.POST['title']
        task.save()
        return redirect('task_list')

    return render(request, 'todo/edit_task.html', {'task': task})

