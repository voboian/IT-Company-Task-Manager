from django.urls import path
from tasks.views import index, PositionListView, TaskTypeListView, WorkerListView, TaskListView, TaskDetailView, \
    WorkerDetailView

urlpatterns = [
    path("", index, name="index"),
    path(
        "position/",
        PositionListView.as_view(),
        name="position-list"
    ),
    path("tasks-types/", TaskTypeListView.as_view(), name="tasks-type-list"),
    path("tasks/", TaskListView.as_view(), name="tasks-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="tasks-detail"),
    path("workers/", WorkerListView.as_view(), name="workers-list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="workers-detail"),

]

app_name = "tasks"
