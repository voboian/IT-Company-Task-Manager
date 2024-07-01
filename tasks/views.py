from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView

from tasks.models import Task, Worker, Position, TaskType


@login_required
def index(request):
    num_tasks = Task.objects.count()
    num_workers = Worker.objects.count()
    num_positions = Position.objects.count()
    num_task_types = TaskType.objects.count()
    context = {
        "num_tasks": num_tasks,
        "num_workers": num_workers,
        "num_positions": num_positions,
        "num_task_types": num_task_types,
    }

    return render(request, "taskmanager/index.html", context=context)


class TaskListView(ListView):
    model = Task
