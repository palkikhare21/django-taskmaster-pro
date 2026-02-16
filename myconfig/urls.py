from django.contrib import admin
from django.urls import path
# We import all 3 functions from your views here
from todo.views import home, complete_task, delete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    
    # These are the "Actions" for your tasks
    path('complete/<int:task_id>/', complete_task, name='complete_task'),
    path('delete/<int:pk>/', delete_task, name='delete_task'),
]