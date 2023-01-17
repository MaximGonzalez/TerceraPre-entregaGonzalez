from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from blog_app.models import *
from blog_app.forms import *

# Create your views here.
def inicio(request):
    return render(
        request=request,
        template_name='blog_app/base.html',
    )


def usuarios(request):
    contexto = {'usuarios' : Usuario.objects.all()}
    return render(
        request=request,
        template_name='blog_app/usuarios.html',
        context=contexto,
    )


def posteos(request):
    contexto = {'posteos' : Post.objects.all()}
    return render(
        request=request,
        template_name='blog_app/posteos.html',
        context=contexto,
    )


def comentarios(request):
    return render(
        request=request,
        template_name='blog_app/comentarios.html',
    )


def about(request):
    return render(
        request=request,
        template_name='blog_app/about.html',
    )


def crear_posteos(request):
    if request.method == 'GET':
        contexto = {'formulario_post' : crear_posteo}
        return render(
        request,
        template_name='blog_app/crear_post.html',
        context=contexto
        )
    else:
        print(request.POST)
        Post.objects.create(titulo = request.POST["titulo"], contenido = request.POST["contenido"])
        contexto = {'formulario_post' : crear_posteo}
        return render(
        request,
        template_name='blog_app/crear_post.html',
        context=contexto
        )

def crear_usuarios(request):
    if request.method == 'GET':
        contexto = {'formulario_usuario' : crear_usuario}
        return render(
        request,
        template_name='blog_app/crear_usuario.html',
        context=contexto
        )
    else:
        print(request.POST)
        form = crear_usuario(request.POST)
        if form.is_valid():
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
        Usuario.objects.create(usuario = request.POST["usuario"], contrasenia = request.POST["contrasenia"], mail = request.POST["mail"], nombre = request.POST["nombre"], apellido = request.POST["apellido"], fecha_nacimiento = fecha_nacimiento,)
        contexto = {'formulario_usuario' : crear_usuario}
        return render(
        request,
        template_name='blog_app/crear_usuario.html',
        context=contexto
        )