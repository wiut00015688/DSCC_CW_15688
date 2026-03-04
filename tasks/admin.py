from django.contrib import admin
from .models import Task, Category, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'category', 'status', 'priority', 'due_date']
    list_filter = ['status', 'priority', 'category']
    search_fields = ['title', 'description']
    filter_horizontal = ['assigned_to']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'task', 'created_at']
