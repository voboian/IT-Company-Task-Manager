from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Worker


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Worker
        fields = (
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "email",
            "position"
        )


class WorkerChangeForm(UserChangeForm):
    class Meta:
        model = Worker
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "position",
            "is_active",
            "is_staff",
            "is_superuser",
            "user_permissions")
