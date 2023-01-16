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
    return render(
        request=request,
        template_name='blog_app/usuarios.html',
    )


def posteos(request):
    contexto = {'posteos' : Post.objects.all()}
    return render(
        request=request,
        template_name='blog_app/posteos.html',
        context=contexto
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

