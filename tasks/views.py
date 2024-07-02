from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from tasks.forms import WorkerCreationForm, WorkerChangeForm, TaskForm
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
    template_name = "tasks/positions_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        search_value = self.request.GET.get("name", "")

        context["segment"] = ["search", "positions"]
        context["search_name"] = "name"
        context["search_value"] = search_value if search_value else ""
        context["search_placeholder"] = "Search position"

        return context

    def get_queryset(self):
        queryset = Position.objects.all()
        search_value = self.request.GET.get("name", "")

        if search_value:
            queryset = queryset.filter(name__icontains=search_value)

        return queryset


class PositionCreateView(LoginRequiredMixin, CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("tasks:position-list")
    template_name = "tasks/positions_form.html"


class PositionUpdateView(LoginRequiredMixin, UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("tasks:position-list")
    template_name = "tasks/positions_form.html"


class PositionDeleteView(LoginRequiredMixin, DeleteView):
    model = Position
    success_url = reverse_lazy("tasks:position-list")
    template_name = "tasks/positions_confirm_delete.html"


class TaskTypeListView(LoginRequiredMixin, ListView):
    model = TaskType
    context_object_name = "task_types_list"
    template_name = "tasks/tasks_types_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        search_value = self.request.GET.get("name", "")

        context["segment"] = ["search", "task_types"]
        context["search_name"] = "name"
        context["search_value"] = search_value if search_value else ""
        context["search_placeholder"] = "Search task type"

        return context

    def get_queryset(self):
        queryset = TaskType.objects.all()
        search_value = self.request.GET.get("name", "")

        if search_value:
            queryset = queryset.filter(name__icontains=search_value)

        return queryset


class TaskTypeCreateView(LoginRequiredMixin, CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("tasks:tasks-type-list")
    template_name = "tasks/tasks_types_form.html"


class TaskTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("tasks:tasks-type-list")
    template_name = "tasks/tasks_types_form.html"


class TaskTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = TaskType
    success_url = reverse_lazy("tasks:tasks-type-list")
    template_name = "tasks/tasks_types_confirm_delete.html"


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks_list"
    template_name = "tasks/tasks_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        search_value = self.request.GET.get("name", "")

        context["segment"] = ["search", "tasks"]
        context["search_name"] = "name"
        context["search_value"] = search_value if search_value else ""
        context["search_placeholder"] = "Search task"

        return context

    def get_queryset(self):
        queryset = Task.objects.select_related("task_type").prefetch_related("assignees")
        search_value = self.request.GET.get("name", "")

        if search_value:
            queryset = queryset.filter(name__icontains=search_value)

        return queryset


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:tasks-list")
    template_name = "tasks/tasks_form.html"


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:tasks-list")
    template_name = "tasks/tasks_form.html"


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:tasks-list")
    template_name = "tasks/tasks_confirm_delete.html"


class WorkerListView(LoginRequiredMixin, ListView):
    model = Worker
    context_object_name = "workers_list"
    template_name = "tasks/workers_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        search_value = self.request.GET.get("username", "")

        context["segment"] = ["search", "workers"]
        context["search_name"] = "username"
        context["search_value"] = search_value if search_value else ""
        context["search_placeholder"] = "Search worker"

        return context

    def get_queryset(self):
        queryset = Worker.objects.select_related("position")
        search_value = self.request.GET.get("username", "")

        if search_value:
            queryset = queryset.filter(username__icontains=search_value)

        return queryset


class WorkerDetailView(LoginRequiredMixin, DetailView):
    model = Worker
    queryset = Worker.objects.prefetch_related("tasks")


class WorkerCreateView(LoginRequiredMixin, CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("tasks:workers-list")
    template_name = "tasks/workers_form.html"


class WorkerUpdateView(LoginRequiredMixin, UpdateView):
    model = Worker
    form_class = WorkerChangeForm
    success_url = reverse_lazy("tasks:workers-list")
    template_name = "tasks/workers_form.html"


class WorkerDeleteView(LoginRequiredMixin, DeleteView):
    model = Worker
    success_url = reverse_lazy("tasks:workers-list")
    template_name = "tasks/workers_confirm_delete.html"
