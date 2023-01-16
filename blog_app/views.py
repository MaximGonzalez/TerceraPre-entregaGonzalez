from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from blog_app.models import *
#from blog_app.forms import *

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
    return render(
        request=request,
        template_name='blog_app/posteos.html',
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


def crear_post(request):
    return render(
        request=request,
        template_name='blog_app/crear_post.html',
    )