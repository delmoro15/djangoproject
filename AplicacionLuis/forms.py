from django import forms

class CursoFormulario(forms.Form):

    curso = forms.CharField()
    comision = forms.IntegerField()

class EstudiantesFormulario(forms.Form):
    
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField()
    email= forms.EmailField()

class FamiliaresFormulario(forms.Form):

    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    edad= forms.IntegerField()