from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from tasks.models import Task, Worker, Position, TaskType


@login_required
def index(request):
    num_tasks = Task.objects.count()
    num_workers = Worker.objects.count()
    num_positions = Position.objects.count()
    num_task_types = TaskType.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_tasks": num_tasks,
        "num_workers": num_workers,
        "num_positions": num_positions,
        "num_task_types": num_task_types,
        "num_visits": num_visits + 1,
    }

    return render(request, "tasks/index.html", context=context)


class PositionListView(LoginRequiredMixin, ListView):
    model = Position
    context_object_name = "positions_list"
    template_name = "tasks/position_list.html"
    paginate_by = 5


class TaskTypeListView(LoginRequiredMixin, ListView):
    model = TaskType
    context_object_name = "task_types_list"
    template_name = "tasks/task_types_list.html"
    paginate_by = 5


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks_list"
    template_name = "tasks/tasks_list.html"
    paginate_by = 5


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task


class WorkerListView(LoginRequiredMixin, ListView):
    model = Worker
    context_object_name = "workers_list"
    template_name = "tasks/workers_list.html"
    paginate_by = 5


class WorkerDetailView(LoginRequiredMixin, DetailView):
    model = Worker
    queryset = Worker.objects.prefetch_related("tasks")



