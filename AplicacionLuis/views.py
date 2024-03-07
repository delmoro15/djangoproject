from django.shortcuts import render
from django.http import HttpResponse
from AplicacionLuis.models import *
from AplicacionLuis.forms import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
def familiares (request):
    
    familiar1= Familiares(nombre= "Luis", apellido= "Lopez Lopez", edad= 28)
    familiar1.save()

    familiar2= Familiares(nombre= "Pedro", apellido= "Lopez Obrador", edad= 14)
    familiar2.save()

    familiar3= Familiares(nombre= "Ramon", apellido= "Lopez Cantero", edad= 24)
    familiar3.save()

    info = {"nombre1": familiar1.nombre, "nombre2": familiar2.nombre,"nombre3": familiar3.nombre, "apellido1": familiar1.apellido, "apellido2": familiar2.apellido, "apellido3": familiar3.apellido, "edad1": familiar1.edad, "edad2": familiar2.edad, "edad3": familiar3.edad }
    return render(request, "inicio.html", info)


def crear_curso (request):

    if request.method == "POST":

        curso= Curso(nombre=["nombre"], comision=["comision"])
        curso.save()
        return render(request, "crear_curso.html")
    
    return render(request, "index.html")

def hola (request):

    todos_familiares = Familiares.objects.all()

    return render(request, "hola.html", {"total":todos_familiares})

#iniciar sesion

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