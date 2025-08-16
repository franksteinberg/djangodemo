"""
URL configuration for djangodemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', views.health, name='health'),
    path('', views.todo_list, name='todo_list'),  # Home page with TODO list
    path('add/', views.todo_add, name='todo_add'),  # Add new TODO
    path('edit/<int:todo_id>/', views.todo_edit, name='todo_edit'),  # Edit TODO
    path('delete/<int:todo_id>/', views.todo_delete, name='todo_delete'),  # Delete TODO
]
