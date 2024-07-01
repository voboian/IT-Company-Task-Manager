from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Position, Worker, TaskType, Task


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", )
    list_filter = ("name",)


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    list_filter = UserAdmin.list_filter + ("position",)
    fieldsets = UserAdmin.fieldsets + (("Additional Info", {"fields": ("position",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Personal Info", {"fields": ("first_name", "last_name", "email")}),
        ("Additional Info", {"fields": ("position",)}),
    )


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "name",

    )
    list_filter = (
        "name",
    )
    search_fields = ("name",)
