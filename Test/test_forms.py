from django.contrib.auth import get_user_model
from django.db.models.functions import datetime
from django.test import TestCase
from django.urls import reverse

from tasks.models import TaskType, Task


class TaskTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="admin",
            password="password",
        )
        self.client.force_login(self.user)
        self.task_type = TaskType.objects.create(name="New task")

    def test_delete_task(self):
        task = Task.objects.create(
            name="Task name",
            description="Task description",
            deadline=datetime.datetime.now().date(),
            is_completed=False,
            priority=3,
            task_type=self.task_type
        )
        response = self.client.post(
            reverse("tasks:tasks-delete", kwargs={"pk": task.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Task.objects.filter(id=task.id).exists()
        )

    def test_toggle_task_assign(self):
        task = Task.objects.create(
            name="Task name",
            description="Task description",
            deadline=datetime.datetime.now().date(),
            is_completed=False,
            priority=3,
            task_type=self.task_type
        )

        response_add = self.client.post(
            reverse("tasks:toggle-task-assign", kwargs={"pk": self.user.id})
        )
        task.refresh_from_db()
        self.assertEqual(response_add.status_code, 302)
        self.assertEqual(task.assignees.count(), 1)

        response_remove = self.client.post(
            reverse("tasks:toggle-task-assign", kwargs={"pk": self.user.id})
        )
        task.refresh_from_db()
        self.assertEqual(response_remove.status_code, 302)
        self.assertEqual(task.assignees.count(), 0)
