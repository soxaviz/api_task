from django.contrib import admin
from .models import Task, Comment

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'status',)
