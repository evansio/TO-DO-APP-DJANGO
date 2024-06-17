from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/new/', views.task_create, name='task_create'),
    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('task/<int:pk>/toggle/', views.task_toggle_complete, name='task_toggle_complete'),  # Nueva ruta para marcar tareas como completadas
    path('register/', views.register, name='register'),  # Ruta para la página de registro
    path('logout/', views.logout_view, name='logout'),  # Ruta para cerrar sesión
]
