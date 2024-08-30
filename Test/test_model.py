from django.contrib.auth import get_user_model
from django.test import TestCase

from tasks.models import TaskType, Position


class ModelTests(TestCase):
    def test_task_type_str(self):
        name = "TestTaskType"
        task_type = TaskType.objects.create(
            name=name,
        )

        self.assertEqual(str(task_type), name)

    def test_position_str(self):
        name = "TestPosition"
        position = Position.objects.create(
            name=name,
        )

        self.assertEqual(str(position), name)

    def test_worker_create(self):
        username = "janedoe"
        password = "password"
        first_name = "Jane"
        last_name = "Doe"
        position = Position.objects.create(name="QA")
        worker = get_user_model().objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            position=position,
        )

        self.assertEqual(worker.username, username)
        self.assertTrue(worker.check_password(password))
        self.assertEqual(worker.first_name, first_name)
        self.assertEqual(worker.last_name, last_name)
        self.assertEqual(worker.position, position)
