from django.db import models

class Familiares(models.Model):

    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    edad= models.IntegerField()
    def __str__(self):

        return f"{self.nombre} -- {self.apellido}"

class Curso(models.Model):
    
    nombre= models.CharField(max_length=30)
    comision = models.IntegerField()
    def __str__(self):

        return f"{self.nombre} -- {self.comision}"