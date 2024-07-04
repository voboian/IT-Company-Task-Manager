from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Position, Worker, TaskType, Task, Tag


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal info",
            {"fields": ("first_name", "last_name", "email", "position")}
        ),
        (
            "Permissions",
            {"fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions"
            )}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2"),
        }),
        ("Personal info", {
            "classes": ("wide",),
            "fields": ("first_name", "last_name", "email", "position"),
        }),
    )
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "position",
        "is_staff"
    )
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "task_type",
        "priority",
        "deadline",
        "is_completed",
        "display_tags"
    )
    list_filter = ("task_type", "priority", "is_completed")
    search_fields = ("name", "description")
    filter_horizontal = ("assignees", "tags")

    fieldsets = (
        (None, {"fields": ("name", "description")}),
        (
            "Details",
            {"fields": ("task_type", "priority", "deadline", "is_completed")}
        ),
        ("Assignees", {"fields": ("assignees",)}),
        ("Tags", {"fields": ("tags",)}),
    )

    def display_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])

    display_tags.short_description = "Tags"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
