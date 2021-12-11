from django.urls import path
from . import views

app_name = 'todoapp'

urlpatterns = [
    path('',views.index_view.as_view() , name ='home'),
    path('details/<int:pk>/', views.detail_view.as_view(), name ='details'),
    path('addtask/', views.form_view, name ='addTask'),
    path('<int:pk>/delete', views.taskDelete.as_view(), name ='delete'),
    path('isComplete/<int:tasks_id>/', views.mark_complete, name ='complete'),
    path('edit/<int:pk>/', views.taskEdit.as_view(), name ='edit'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]
