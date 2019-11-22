from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_create),
    path('users/<int:pk>/', views.user_detail),
]