from django.contrib import admin
from todolist.models import *


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "task",
        "done"
    ]
    list_filter = [
        'done'
    ]


admin.site.register(tasklist, TaskAdmin)
