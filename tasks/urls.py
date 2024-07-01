from django.urls import path
from tasks.views import index, PositionListView, TaskTypeListView, WorkerListView, TaskListView

urlpatterns = [
    path("", index, name="index"),
    path(
        "position/",
        PositionListView.as_view(),
        name="position-list"
    ),
    path("task-types/", TaskTypeListView.as_view(), name="task-type-list"),
    path("task/", TaskListView.as_view(), name="task-list"),
    path("worker/", WorkerListView.as_view(), name="worker-list"),

]

app_name = "tasks"
