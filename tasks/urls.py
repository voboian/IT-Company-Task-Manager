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
    WorkerCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("position/", PositionListView.as_view(), name="position-list"),
    path("position/create", PositionCreateView.as_view(), name="position-create"),
    path("tasks-types/", TaskTypeListView.as_view(), name="tasks-type-list"),
    path("tasks-types/create", TaskTypeCreateView.as_view(), name="tasks-type-create"),
    path("tasks/", TaskListView.as_view(), name="tasks-list"),
    path("tasks/create", TaskCreateView.as_view(), name="tasks-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="tasks-detail"),
    path("workers/", WorkerListView.as_view(), name="workers-list"),
    path("workers/create", WorkerCreateView.as_view(), name="workers-create"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="workers-detail"),

]

app_name = "tasks"
