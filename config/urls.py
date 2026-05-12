from django.contrib import admin
from django.urls import path

from todos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create'),
    path('toggle/<int:pk>/', views.todo_toggle, name='todo_toggle'),
    path('delete/<int:pk>/', views.todo_delete, name='todo_delete'),
]
