from django.shortcuts import render, redirect
from .models import ToDoTask
# Create your views here.
def todo_list(request):
    tasks = ToDoTask.objects.all()
    return render(request, 'Todo_app/todo_list.html', {'tasks':tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        ToDoTask.objects.create(title=title)
        return redirect('todo_List')

def delete_task(request, task_id):
    task = ToDoTask.objects.get(id = task_id)
    task.delete()
    return redirect('todo_List')