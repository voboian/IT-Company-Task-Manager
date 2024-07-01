from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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


class PositionListView(LoginRequiredMixin, ListView):
    model = Position
    context_object_name = "positions_list"
    template_name = "taskmanager/position_list.html"
    paginate_by = 5


class TaskTypeListView(LoginRequiredMixin, ListView):
    model = TaskType
    context_object_name = "task_types_list"
    template_name = "taskmanager/task_types_list.html"
    paginate_by = 5


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks_list"
    template_name = "taskmanager/tasks_list.html"
    paginate_by = 5


class WorkerListView(LoginRequiredMixin, ListView):
    model = Worker
    context_object_name = "workers_list"
    template_name = "taskmanager/workers_list.html"
    paginate_by = 5
