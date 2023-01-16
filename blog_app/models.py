from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.

class Usuario(models.Model):
    usuario = models.CharField(max_length=64)
    contrasenia = models.CharField(max_length=64)
    mail = models.EmailField()
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    fecha_nacimiento = models.DateTimeField()


class Post(models.Model):
    titulo = models.CharField(max_length=64)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)

class Comentario(models.Model):
    texto = models.CharField(max_length=256)
    fecha_publicacion = models.DateTimeField()