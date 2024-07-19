from django.http import HttpResponse
from .models import Project, Task  #para hacer consulta de Project y Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject

#con el comando en consola
#python manage.py runserver para correr el programa

# Create your views here.
def index(request):
    title = 'Django course'
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    username = 'kronuz'
    return render(request, 'about.html', {
        'username' : username
    })

def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)

#llamamos la lista de proyectos y la almacenamos en projects
def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html',{
        'projects': projects
    })

#del Modelo Task haremos consulta de multiples objectos obteniendolos con el metodo get por id
def tasks(request):
    #Task.objects.get(id=id)
    #task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html',{
        'tasks': tasks
    })

def createTask(request):
    if request.method == 'GET':
        return render(request, 'tasks/createTask.html',{
        'form': CreateNewTask()
    })
    else:
        Task.objects.create(title=request.POST['title'],description=request.POST['descripcion'], project_id=2)
        return redirect('/tasks/')

def createProject(request):
    if request.method == 'GET':
        return render(request, 'projects/createProject.html',{
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('/projects/')
    
def project_datail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks= Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html',{
        'project':project,
        'tasks': tasks
    })   