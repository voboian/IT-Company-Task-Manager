from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from tasks.admin import PositionAdmin, TagAdmin
from tasks.models import Position, Tag


class PositionTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin.user", password="Qwerty12345!"
        )

        self.site = AdminSite()

        self.client.force_login(self.admin_user)

        self.position = Position.objects.create(name="Developer",)

        self.position_admin = PositionAdmin(Position, self.site)

    def test_position_name_listed(self) -> None:
        url = reverse("admin:tasks_position_changelist")

        res = self.client.get(url)

        self.assertContains(res, self.position.name)

    def test_search_by_name(self) -> None:
        self.assertIn("name", self.position_admin.search_fields)


class TagTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin.user", password="Qwerty12345!"
        )

        self.site = AdminSite()

        self.tag = Tag.objects.create(name="qwe", )

        self.tag_admin = TagAdmin(Tag, self.site)

    def test_search_by_name(self) -> None:
        self.assertIn("name", self.tag_admin.search_fields)
