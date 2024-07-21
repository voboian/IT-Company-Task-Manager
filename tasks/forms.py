from datetime import datetime, date

from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from tasks.models import Worker, Task, Tag


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
        )


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        fields = (
            "name",
            "description",
            "deadline",
            "priority",
            "is_completed",
            "task_type",
            "assignees",
            "tags",
        )

    def clean_deadline(self) -> datetime:
        task_deadline = self.cleaned_data["deadline"]

        if task_deadline < date.today():
            raise ValidationError("Please, select date in future")

        return task_deadline


class WorkerSearchForm(forms.Form):
    username = forms.CharField(max_length=255, required=False, label="Username")
    first_name = forms.CharField(
        max_length=255,
        required=False,
        label="First Name"
    )
    last_name = forms.CharField(
        max_length=255,
        required=False,
        label="Last Name"
    )
    email = forms.EmailField(required=False, label="Email")


class TaskSearchForm(forms.Form):
    name = forms.CharField(max_length=255, required=False, label="Name")
    description = forms.CharField(
        max_length=255,
        required=False,
        label="Description"
    )
    priority = forms.ChoiceField(
        choices=Task.PRIORITY_CHOICES,
        required=False,
        label="Priority"
    )


class TaskTypeSearchForm(forms.Form):
    name = forms.CharField(max_length=255, required=False, label="Name")


class PositionSearchForm(forms.Form):
    name = forms.CharField(max_length=255, required=False, label="Name")
