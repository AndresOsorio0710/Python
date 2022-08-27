from django.contrib import admin

from task_app.models import Task


class TaskAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description']
    list_display = ['name','type']
    list_filter = ['type']
    list_per_page = 5

# Register your models here.
admin.site.register(Task,TaskAdmin)
