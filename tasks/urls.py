from django.urls import path
from tasks.views import (
    index, PositionListView,
    TaskTypeListView,
    WorkerListView,
    TaskListView,
    TaskDetailView,
    WorkerDetailView,
    TaskCreateView,
    TaskTypeCreateView,
    PositionCreateView,
    WorkerCreateView, TaskUpdateView, WorkerUpdateView, WorkerDeleteView, TaskDeleteView, TaskTypeUpdateView,
    TaskTypeDeleteView, PositionUpdateView, PositionDeleteView, toggle_assign_to_task, TagListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("position/", PositionListView.as_view(), name="position-list"),
    path("position/create", PositionCreateView.as_view(), name="position-create"),
    path("position/<int:pk>/update", PositionUpdateView.as_view(), name="position-update"),
    path("position/<int:pk>/delete", PositionDeleteView.as_view(), name="position-delete"),
    path("tasks-types/", TaskTypeListView.as_view(), name="tasks-type-list"),
    path("tasks-types/create", TaskTypeCreateView.as_view(), name="tasks-type-create"),
    path("tasks-types/<int:pk>/update", TaskTypeUpdateView.as_view(), name="tasks-type-update"),
    path("tasks-types/<int:pk>/delete", TaskTypeDeleteView.as_view(), name="tasks-type-delete"),
    path("tasks/", TaskListView.as_view(), name="tasks-list"),
    path("tasks/create", TaskCreateView.as_view(), name="tasks-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="tasks-detail"),
    path("tasks/<int:pk>/update", TaskUpdateView.as_view(), name="tasks-update"),
    path("tasks/<int:pk>/delete", TaskDeleteView.as_view(), name="tasks-delete"),
    path(
        "tasks/<int:pk>/toggle-assign/",
        toggle_assign_to_task,
        name="toggle-task-assign",
    ),
    path("workers/", WorkerListView.as_view(), name="workers-list"),
    path("workers/create", WorkerCreateView.as_view(), name="workers-create"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="workers-detail"),
    path("workers/<int:pk>/update", WorkerUpdateView.as_view(), name="workers-update"),
    path("workers/<int:pk>/delete", WorkerDeleteView.as_view(), name="workers-delete"),
    path("tags/", TagListView.as_view(), name="tags-list"),

]

app_name = "tasks"
