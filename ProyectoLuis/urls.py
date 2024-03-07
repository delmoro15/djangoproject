"""
URL configuration for ProyectoLuis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AplicacionLuis.views import *
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio.html', inicio),
    path('crear_curso.html', crear_curso,name="CrearCurso"),
    path('aplicacion_luis/', include('AplicacionLuis.urls')),
    path('registro/inicio_sesion.html',iniciar_sesion) ,
    path('crear_estudiante.html', crear_estudiantes,name="CrearEstudiantes"),
    path('ver_curso.html', ver_cursos),
    path('ver_estudiante.html', ver_estudiantes),
    path('', inicio)]
    
