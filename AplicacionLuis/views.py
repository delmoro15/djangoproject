from django.shortcuts import render
from django.http import HttpResponse
from AplicacionLuis.models import *
from AplicacionLuis.forms import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login

def inicio (request):

    return render(request, "inicio.html")

#cursos

def crear_curso (request):

    if request.method == "POST":

        formulario1= CursoFormulario(request.POST)

        if formulario1.is_valid():
            info= formulario1.cleaned_data
            curso = Curso(nombre=info["curso"], comision=info["comision"])
            curso.save()
            return render(request, "inicio.html")
    
        return render(request, "crear_curso.html")
    else:
        formulario1= CursoFormulario()

    return render(request, "crear_curso.html",{"form1":formulario1})

def ver_cursos (request):

    cursos= Curso.objects.all()
    contexto = {"cursos":cursos}
    
    return render(request, "ver_curso.html", contexto)

#estudiantes:

def crear_estudiantes (request):

    if request.method == "POST":

        formulario1= EstudiantesFormulario(request.POST)

        if formulario1.is_valid():
            info= formulario1.cleaned_data
            estudiante = Estudiantes(nombre=info["nombre"], apellido=info["apellido"],email=info["email"])
            estudiante.save()
            return render(request, "inicio.html")
    
        return render(request, "crear_estudiante.html")
    else:
        formulario1= EstudiantesFormulario()

    return render(request, "crear_estudiante.html",{"form1":formulario1})

def ver_estudiantes (request):
    Estudiantes1= Estudiantes.objects.all()
    contexto = {"estudiantes":Estudiantes1}
    
    return render(request, "ver_estudiante.html", contexto)


#iniciar sesion falta terminar!!

def iniciar_sesion(request):

    if request.method == "POST":

        formulario = AuthenticationForm(request.POST)

        if formulario.is_valid():

            info_dic = formulario.cleaned_data

            usuario = authenticate(username=info_dic["username"], password=info_dic["password"])
            
            if usuario is not None:
                login(request,usuario)
                return render(request,"inicio.html", f"Bienvenido {usuario}")

        else:
            return render (request, "inicio.html", {"mensaje": " Error en el inicio"})
        
    else:
        return render(request,"registro/inicio_sesion.html")