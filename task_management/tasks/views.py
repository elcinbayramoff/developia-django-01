from django.shortcuts import render
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
    
    context = {'tasks':DATABASE}
    
    return render(request, 'tasks/task.html', context=context)

def task_specific(request, task_id):
    value = DATABASE.get(task_id)
    
    if value != None:
        context = {
            "id":task_id,
            "title": DATABASE.get(task_id)['title'],
            "description": DATABASE.get(task_id)['description'],
            "status": DATABASE.get(task_id)['status'],
            "category": DATABASE.get(task_id)['category'],
            "deadline": DATABASE.get(task_id)['deadline']
        }
    else:
        context = {
            'id' : task_id
        }
    return render(request, 'tasks/tasks_specific.html', context = context)