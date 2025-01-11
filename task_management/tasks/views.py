from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Task
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
#Tasks
DATABASE = {
    1: {
        "title": "Complete project report",
        "description": "Finalize and submit the quarterly project report.",
        "status": "Pending",
        "category": "Work",
        "deadline": "2024-12-30"
    },
    2: {
        "title": "Buy groceries",
        "description": "Purchase milk, eggs, bread, and vegetables.",
        "status": "In Progress",
        "category": "Personal",
        "deadline": "2024-12-26"
    },
    3: {
        "title": "Call plumber",
        "description": "Schedule a call to fix the leaking pipe in the bathroom.",
        "status": "Completed",
        "category": "Home",
        "deadline": "2024-12-22"
    },
    4: {
        "title": "Prepare for interview",
        "description": "Research the company and practice common interview questions.",
        "status": "Pending",
        "category": "Work",
        "deadline": "2024-12-28"
    },
    5: {
        "title": "Exercise",
        "description": "Go for a 30-minute run around the park.",
        "status": "In Progress",
        "category": "Health",
        "deadline": "2024-12-25"
    }
}


# DATABASE[2]
@login_required
def home(request):
    return render(request, 'tasks/home.html')

@login_required
def tasks(request):
    # print('------',request.user.email)
    tasks = Task.objects.filter(owner=request.user)    
    context = {'tasks':tasks}
    
    return render(request, 'tasks/task.html', context=context)

#Editing
@login_required
def task_specific(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        
        category = request.POST['category']
        
        task.deadline = request.POST['deadline']
        task.status = request.POST['status']
        
        category_obj = Category.objects.get(id=category)
        task.category = category_obj
        task.save()
        return redirect('tasks')
    
    categories = Category.objects.all()
    return render(request, 'tasks/tasks_specific.html', {'task': task, 'categories':categories})


"""
POST
GET
UPDATE
DELETE
PATCH

"""
@login_required
def task_create(request): # V
    if request.method == 'POST':
        title1 = request.POST['title']
        description = request.POST['description']
        category = request.POST['category'] # 5 3 6
        deadline = request.POST['deadline']
        status = request.POST['status']
        category_obj = Category.objects.get(id=category)
        Task.objects.create(title=title1, description=description, category=category_obj, deadline=deadline, status=status)
        return redirect('tasks')    
    

    categories = Category.objects.all() #M
    return render(request, 'tasks/task_create.html', {'categories': categories})

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id) #primary key
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    return render(request, 'tasks/task_delete.html', {'task': task})