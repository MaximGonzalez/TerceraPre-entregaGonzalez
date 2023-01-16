from django.contrib import admin, staticfiles
from django.urls import path
from .views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("usuarios/", usuarios, name="usuarios"),
    path("posteos/", posteos, name="posteos"),
    path("comentarios/", comentarios, name="comentarios"),
    path("about/", about, name="about"),
    path("crearpost/", crear_posteos, name="crear_post"),
]