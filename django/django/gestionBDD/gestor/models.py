from django.db import models

# Create your models here.
class cliente(models.Model):
    nombre=models.CharField(max_length=30, blank=False, default="nulo")
    direccion=models.CharField(max_length=50, blank=False, default="nulo")
    email=models.EmailField(max_length=30, unique=True, blank=False, default="nulo")
    telefono=models.CharField(max_length=30, blank=False, default="nulo")
    password=models.CharField(max_length=15, blank=False, default="nulo")

class articulo(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()
    
class pedido(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
    