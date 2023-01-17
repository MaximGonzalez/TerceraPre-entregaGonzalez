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
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.usuario}"


class Post(models.Model):
    titulo = models.CharField(max_length=64)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default='1')

class Comentario(models.Model):
    texto = models.CharField(max_length=256)
    fecha_publicacion = models.DateTimeField()