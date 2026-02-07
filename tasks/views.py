from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task
# Create your views here.


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
    # retrive all data from tasks model
    tasks = Task.objects.all()

    # retrive a specific task
    task_3 = Task.objects.get(pk=1)

    return render(request, 'show_task.html', {'tasks':tasks, 'task_3': task_3})