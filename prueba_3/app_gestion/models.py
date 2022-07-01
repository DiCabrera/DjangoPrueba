from django.db import models

# Create your models here.
class Persona(models.Model):
    rut=models.CharField(max_length=9)
    nombre=models.CharField(max_length=50)
    appaterno=models.CharField(max_length=50)
    apmaterno=models.CharField(max_length=50)
    edad=models.IntegerField()
    nom_vacuna=models.CharField(max_length=50)
    fecha=models.DateField()