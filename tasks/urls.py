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
    path("task-types/", TaskTypeListView.as_view(), name="task-type-list"),
    path("task/", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("worker/", WorkerListView.as_view(), name="worker-list"),
    path("worker/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),

]

app_name = "tasks"
