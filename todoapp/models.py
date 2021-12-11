from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class custom_user(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE , null=True)

    def __str__(self):
        return self.username

class tasks(models.Model):
    user = models.ForeignKey(custom_user,on_delete=models.CASCADE, null=True)
    task_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, null=True, blank= True)
    priority = models.CharField(max_length=100)
    due_date = models.DateField()
    is_completed = models.BooleanField("Completed" , default=False)
    notes = models.TextField()

    def __str__(self):
        return self.task_name





