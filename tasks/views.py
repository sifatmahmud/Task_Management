from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task, TaskDetail, Project
from datetime import date, timedelta
from django.utils import timezone
from django.db.models import Q, Count, Max, Min, Avg


def manager_dashboard(request):
    return render(request, "dashboard/manager_dashboard.html")

def user_dashboard(request):
    return render(request, "dashboard/user_dashboard.html")

def test(request):
    names = ["Mahmud", "Sifat", "Rifat", "Jon"]
    count = 0
    for name in names:
        count+=1
    context = {
        "names": names,
        "age": 23,
        "count": count
    }
    return render(request, 'test.html', context)

def create_task(request):
    form = TaskModelForm() # for GET

    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'task_form.html', {"form":form, 'message':"Task added successfully"})

    context = {"form": form}
    return render(request, "task_form.html", context)





def show_task(request):
    # Show the tasks which are assigned to a specific employee
    # employee = Employee.objects.get(id=1)
    # tasks = employee.tasks.all()
    # return render(request, 'show_task.html', {'tasks': tasks})

    # Show all employees working on a specific project
    # project = Project.objects.get(id=3)
    # employees = Employee.objects.filter(tasks__project=project).distinct()
    # return render(request, 'show_task.html', {'employees': employees})

    # Get all tasks that are due today
    # tasks = Task.objects.filter(due_date=date.today())
    # return render(request, 'show_task.html', {'tasks': tasks})


    # Show all tasks with a priority higher than 'low'
    # tasks = TaskDetail.objects.exclude(priority='L')
    # return render(request, 'show_task.html', {'tasks': tasks})


    # employee = Employee.objects.get(id=2)
    # tasks_count = employee.tasks.all().count()
    # return render(request, 'show_task.html', {'tasks_count': tasks_count})


    # recent_task = Task.objects.order_by('created_at').first()
    # return render(request, 'show_task.html', {'recent_task': recent_task})



    # projects = Project.objects.annotate(task_count = Count('task')).filter(task_count = 2)
    # return render(request, 'show_task.html', {'projects': projects})

    # now = timezone.now()
    # one_week_ago = now - timedelta(days=7)
    # overdue_tasks = Task.objects.filter(is_completed=False, due_date__lt=one_week_ago)
    # return render(request, 'show_task.html', {'tasks': overdue_tasks})


    # employees_with_task_count = Employee.objects.annotate(total_tasks=Count('tasks'))
    # return render(request, 'show_task.html', {'emps': employees_with_task_count})


    tasks = Task.objects.exclude(status='PENDING')
    return render(request, 'show_task.html', {'tasks': tasks})