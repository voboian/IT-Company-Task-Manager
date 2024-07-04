from django.test import TestCase
from django.urls import reverse
from tasks.models import TaskType, Position, Worker, Task
from django.utils import timezone
from datetime import timedelta


class TaskListViewTest(TestCase):
    def setUp(self):
        self.task_type = TaskType.objects.create(name="Bug Fix")
        self.position = Position.objects.create(name="Developer")
        self.worker = Worker.objects.create_user(username='testuser', password='password', position=self.position)
        self.task = Task.objects.create(
            name="Fix login bug",
            description="Fix the bug in login functionality",
            deadline=timezone.now() + timedelta(days=1),
            priority="High",
            task_type=self.task_type,
        )
        self.task.assignees.add(self.worker)

        self.client.login(username='testuser', password='password')

    def test_task_list_view(self):
        response = self.client.get(reverse('tasks:tasks-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_list.html')
        self.assertContains(response, self.task.name)


class WorkerDetailViewTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")
        self.worker = Worker.objects.create_user(username='testuser', password='password', position=self.position)

        self.client.login(username='testuser', password='password')

    def test_worker_detail_view(self):
        response = self.client.get(reverse('tasks:workers-detail', kwargs={'pk': self.worker.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/worker_detail.html')
        self.assertContains(response, self.worker.username)
