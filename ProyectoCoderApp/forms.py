from django import forms


class NuevoCurso(forms.Form):

    nombre = forms.CharField(max_length=30,label="Curso")
    comision = forms.IntegerField(min_value=0)

class NuevoProfesor(forms.Form):
    nombre = forms.CharField(max_length=30, label="Nombre")
    profesion = forms.CharField(max_length=30, label="Profesion")

class NuevoEstudiante(forms.Form):
    nombre = forms.CharField(max_length=30, label= "Nombre")
    apellido = forms.CharField(max_length=30, label= "Apellido")


