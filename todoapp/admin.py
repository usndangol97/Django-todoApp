from django.contrib import admin
from .models import tasks,custom_user
# Register your models here.
admin.site.register(tasks)
admin.site.register(custom_user)