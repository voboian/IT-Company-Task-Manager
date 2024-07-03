from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from tasks.forms import WorkerCreationForm, WorkerChangeForm, TaskForm
from tasks.models import Task, Worker, Position, TaskType, Tag


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
        queryset = Position.objects.all().order_by("name")
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
        queryset = TaskType.objects.all().order_by("name")
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
        queryset = Task.objects.select_related("task_type").prefetch_related("assignees").order_by("name")
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
    form_class = TaskForm
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
        workers = context["workers_list"]
        for worker in workers:
            completed_tasks = worker.tasks.filter(is_completed=True)
            not_completed_tasks = worker.tasks.filter(is_completed=False)

            worker.completed_tasks_count = completed_tasks.count()
            worker.not_completed_tasks_count = not_completed_tasks.count()

        return context

    def get_queryset(self):
        queryset = Worker.objects.select_related("position").order_by("username")
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


@login_required
def toggle_assign_to_task(request, pk):
    worker = Worker.objects.get(id=request.user.id)
    if (
        Task.objects.get(id=pk) in worker.tasks.all()
    ):
        worker.tasks.remove(pk)
    else:
        worker.tasks.add(pk)
    return HttpResponseRedirect(reverse_lazy("tasks:tasks-detail", args=[pk]))


class TagListView(ListView):
    model = Tag
    context_object_name = "tags_list"
    template_name = "tasks/tags_list.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_value = self.request.GET.get("name", "")

        context["segment"] = ["search", "tags"]
        context["search_name"] = "name"
        context["search_value"] = search_value if search_value else ""
        context["search_placeholder"] = "Search tag"

        return context

    def get_queryset(self):
        queryset = Tag.objects.all().order_by("name").prefetch_related("tasks")
        search_value = self.request.GET.get("name", "")

        if search_value:
            queryset = queryset.filter(name__icontains=search_value)

        return queryset
