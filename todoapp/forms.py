from django import forms
from .models import tasks
from django.contrib.auth.models import User

#Forms here
class addTask(forms.ModelForm):
    class Meta:
        model = tasks
        fields = ['task_name','priority','due_date','notes']

class user_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name','username','email','password']