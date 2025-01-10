from django.shortcuts import render, redirect
from .models import Category, Task
from django.http import HttpResponse


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

def home(request):
    return render(request, 'tasks/home.html')


def tasks(request):
    
    tasks = Task.objects.all()
    print(tasks)
    
    context = {'tasks':tasks}
    
    return render(request, 'tasks/task.html', context=context)

def task_specific(request, task_id):
    value = DATABASE.get(task_id)
    categories = Category.objects.all()
    if value != None:
        context = {
            "id":task_id,
            "title": DATABASE.get(task_id)['title'],
            "description": DATABASE.get(task_id)['description'],
            "status": DATABASE.get(task_id)['status'],
            "category": DATABASE.get(task_id)['category'],
            "deadline": DATABASE.get(task_id)['deadline'],
            'categories': categories
        }
    else:
        context = {
            'id' : task_id
        }
    return render(request, 'tasks/tasks_specific.html', context = context)


"""
POST
GET
UPDATE
DELETE
PATCH

"""
def task_create(request): # V
    if request.method == 'POST':
        title1 = request.POST['title']
        description = request.POST['description']
        category = request.POST['category']
        deadline = request.POST['deadline']
        status = request.POST['status']
        category_obj = Category.objects.get(id=category)
        Task.objects.create(title=title1, description=description, category=category_obj, deadline=deadline, status=status)
        return redirect('tasks')    
    
    categories = Category.objects.all() #M
    return render(request, 'tasks/task_create.html', {'categories': categories})