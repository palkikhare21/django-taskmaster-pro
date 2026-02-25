from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def home(request):
    # Handle adding a new task from the homepage
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('home')
    
    # Fetch all tasks to display
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect('home')

# If you still want the complete functionality
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('home')