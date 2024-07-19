from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('about/',views.about, name="about"),
    path('hello/<str:username>',views.hello, name="hola"),
    path('projects/',views.projects, name="proyecto"),
    path('projects/<int:id>',views.project_datail, name="detalle"),
    path('tasks/',views.tasks, name="tarea"),
    path('createTask/',views.createTask, name="nuevaTarea"),
    path('createProject/',views.createProject, name="nuevoProyecto"),
]