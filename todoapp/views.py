from django.shortcuts import render, redirect, reverse
from django.views import generic
from .models import tasks
from .forms import addTask,user_form
from django.contrib import messages
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

class index_view(generic.ListView):
    context_object_name = 'task_list'
    template_name = 'todoapp/index.html'

    def get_queryset(self):
        return tasks.objects.all()

class detail_view(generic.DetailView):
    model = tasks
    template_name = 'todoapp/details.html'

def form_view(request):
    form = addTask()

    if (request.method == 'POST'):
        form = addTask(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, ('Task has been added!'))
        else:
            print(form.errors)
            messages.error(request, ('Failed to add the Task'))
        
    return render(request,'todoapp/tasks_form.html',{'form':form})

class taskDelete(generic.DeleteView):
    model = tasks
    success_url = reverse_lazy('todoapp:home')

def mark_complete(request,tasks_id):
    task = tasks.objects.get(pk=tasks_id)
    if task.is_completed == False:
        task.is_completed = True
    else:
        task.is_completed = True
    task.save()
    return redirect('todoapp:home')

class taskEdit(generic.UpdateView):
    model = tasks
    fields = ['task_name','priority','due_date','is_completed','notes']

    def get_success_url(self):
        return reverse('todoapp:home')

def register(request):
    registered =False

    form = user_form()
    
    if request.method == 'POST':
        form = user_form(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            registered =True
        else:
            print(form.errors)

    context= {'form':form, 'registered':registered}
    return render(request,'todoapp/register.html',context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('todoapp:home'))
            else:
                return HttpResponse("Account is not active.")
        else:
            return HttpResponse("Login failed.")
    else:
        context = {}
        return render(request,'todoapp/login.html',context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('todoapp:home'))