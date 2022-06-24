from asyncio import ProactorEventLoop
import datetime

from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Curso, Estudiante, Profesor
from .forms import NuevoCurso

from django.db.models import Q
from .forms import NuevoProfesor
from .forms import NuevoEstudiante
# Create your views here.

def inicio(request):

    nombre = "Juan"
    hoy = datetime.datetime.now()
    notas = [4,9,7,8,5,10]

    return render(request,"ProyectoCoderApp/index.html",{"mi_nombre":nombre,"dia_hora":hoy,"notas":notas})

def crear_curso(request):
    if request.method == "POST":
        formulario = NuevoCurso(request.POST)
        if formulario.is_valid():
            info_curso = formulario.cleaned_data
  
            curso = Curso(nombre=info_curso["nombre"], comision=info_curso["comision"])
            curso.save() # guardamos en la bd
            return redirect("cursos")
        
        else:

            return render(request,"ProyectoCoderApp/formulario_curso.html",{"form":formulario})
    

    else: # get y otros

        formularioVacio = NuevoCurso()

        return render(request,"ProyectoCoderApp/formulario_curso.html",{"form":formularioVacio})


def agregar_profesor(request): #VISTA PARA AGREGAR PROFESORES

    if request.method == "POST":

        formulario = NuevoProfesor(request.POST)
        if formulario.is_valid():
            info_profesor = formulario.cleaned_data
            profesor = Profesor(nombre=info_profesor["nombre"], profesion=info_profesor["profesion"])
            profesor.save() # guardamos en la bd al profesor
            return redirect("profesores")
        else:
            return render(request, r"ProyectoCoderApp\formulario_profesor.html",{"form":formulario})
    else: # get y otros
        formularioVacio = NuevoProfesor()
        return render(request, r"ProyectoCoderApp\formulario_profesor.html",{"form":formularioVacio})

def agregar_estudiante (request): #VISTA PARA AGREGAR ESTUDIANTES

    if request.method == "POST":

        formulario = NuevoEstudiante(request.POST)
        if formulario.is_valid():
            info_estudiante = formulario.cleaned_data
            estudiante = Estudiante(nombre=info_estudiante["nombre"], apellido=info_estudiante["apellido"])
            estudiante.save() # guardamos en la bd al profesor
            return redirect("estudiantes")
        else:
            return render(request, r"ProyectoCoderApp\formulario_estudiante.html",{"form":formulario})
    else: # get y otros
        formularioVacio = NuevoEstudiante()
        return render(request, r"ProyectoCoderApp\formulario_estudiante.html",{"form":formularioVacio})


def buscar_comision(request):

    if request.method == "POST":

        comision = request.POST["comision"]
        
        comisiones = Curso.objects.filter( Q(nombre__icontains=comision) | Q(comision__icontains=comision) ).values()
        # User.objects.filter(Q(income__gte=5000) | Q(income__isnull=True))

        return render(request,"ProyectoCoderApp/buscar_comision.html",{"comisiones":comisiones})

    else: # get y otros

        comisiones =  [] 
        
        return render(request,"ProyectoCoderApp/buscar_comision.html",{"comisiones":comisiones})

def buscar_estudiante (request):

    if request.method == "POST":

        estudiante = request.POST["estudiante"]
        
        estudiantes = Estudiante.objects.filter(estudiante__icontains=estudiante)
        
        return render(request, r"C:\Users\Samsung\Desktop\ENTREGABLE\djangocoder-master\ProyectoCoder\ProyectoCoderApp\templates\ProyectoCoderApp\buscar_estudiante.html",{"estudiantes":estudiantes})

    else: 

        estudiantes =  []  
        
        return render(request,r"C:\Users\Samsung\Desktop\ENTREGABLE\djangocoder-master\ProyectoCoder\ProyectoCoderApp\templates\ProyectoCoderApp\buscar_estudiante.html",{"estudiantes":estudiantes})


def buscar_profesor(request):
    if request.method == "POST":

        profesor = request.POST["profesor"]
        
        profesores = Profesor.objects.filter( Q(nombre__icontains=profesor) | Q(comision__icontains=profesor) ).values()
        
        return render(request, r"C:\Users\Samsung\Desktop\ENTREGABLE\djangocoder-master\ProyectoCoder\ProyectoCoderApp\templates\ProyectoCoderApp\buscar_profesor.html",{"profesores":profesores})

    else:

        profesores =  []  
        
        return render(request, r"C:\Users\Samsung\Desktop\ENTREGABLE\djangocoder-master\ProyectoCoder\ProyectoCoderApp\templates\ProyectoCoderApp\buscar_profesor.html",{"profesores":profesores})


def profesores(request): #AGREGAMOS EN LA VIEW LA LISTA DE PROFESORES QUE SE VAN AGREGANDO

    profesores = Profesor.objects.all()

    return render(request,"ProyectoCoderApp\profesores.html",{"profesores":profesores})

def estudiantes(request):

    estudiantes = Estudiante.objects.all()

    return render(request,"ProyectoCoderApp\estudiantes.html",{"estudiantes":estudiantes})

def cursos(request):
    # return HttpResponse("Vista de cursos")

    cursos = Curso.objects.all()

    return render(request,"ProyectoCoderApp/cursos.html",{"cursos":cursos})


def base(request):
    return render(request,"ProyectoCoderApp/base.html",{})

def entregables(request):
    return HttpResponse("Vista de entregables")