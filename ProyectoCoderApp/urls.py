from django.urls import path

from .views import *

urlpatterns = [
    # URLS de ProyectoCoderApp
    path('', inicio, name="inicio"),
    path('agregar_profesor/', agregar_profesor, name= "agregar_profesor"),
    path('agregar_estudiante', agregar_estudiante, name= "agregar_estudiante"),
    path('profesores/', profesores, name="profesores"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('cursos/', cursos, name="cursos"),
    path('crear_curso/', crear_curso, name="crear_curso"),
    path('buscar_comision/', buscar_comision, name="buscar_comision"),
    path('buscar_profesor/', buscar_profesor, name='buscar_profesor'),
    path('buscar_estudiante/', buscar_estudiante, name='buscar_estudiante'),
    path('entregables/', entregables, name="entregables"),


    
    # path('base/', base),
]