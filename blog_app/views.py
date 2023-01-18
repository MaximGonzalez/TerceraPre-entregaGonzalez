from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse
from blog_app.models import *
from blog_app.forms import *

# Create your views here.


def inicio(request):
    contexto = {'posteos' : Post.objects.all()}
    return render(
        request=request,
        template_name='blog_app/inicio.html',
        context=contexto,
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
    contexto = {'comentarios' : Comentario.objects.all()}
    return render(
        request=request,
        template_name='blog_app/comentarios.html',
        context=contexto,
    )



def crear_posteos(request):
    if request.method == 'GET':
        contexto = {'formulario_post' : Crear_posteo}
        return render(
        request,
        template_name='blog_app/crear_post.html',
        context=contexto
        )
    else:
        print(request.POST)
        Post.objects.create(titulo = request.POST["titulo"], contenido = request.POST["contenido"])
        contexto = {'formulario_post' : Crear_posteo}
        return render(
        request,
        template_name='blog_app/crear_post.html',
        context=contexto
        )



def crear_usuarios(request):
    if request.method == 'GET':
        contexto = {'formulario_usuario' : Crear_usuario}
        return render(
        request,
        template_name='blog_app/crear_usuario.html',
        context=contexto
        )
    else:
        print(request.POST)
        form = Crear_usuario(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            usuario = Usuario(usuario = data["usuario"], contrasenia = data["contrasenia"], mail = data["mail"], nombre = data["nombre"], apellido = data["apellido"], fecha_nacimiento = data['fecha_nacimiento'])
            usuario.save()
            url_exitosa = reverse('usuarios')
        return redirect(url_exitosa)



def crear_posteos(request):
    if request.method == 'GET':
        contexto = {'formulario_post' : Crear_posteo}
        return render(
        request,
        template_name='blog_app/crear_post.html',
        context=contexto
        )
    else:
        print(request.POST)
        formulario = Crear_posteo(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            posteo = Post(titulo = data["titulo"], contenido = data["contenido"], usuario = data["usuario"])
            posteo.save()
            url_exitosa = reverse('inicio')
        return redirect(url_exitosa)



def buscar_posteos(request):
    if request.method == 'GET':
        return render(
        request,
        template_name='blog_app/crear_post.html',
        )
    else:
        print(request.POST)
        data = request.POST
        posteos = Post.objects.filter(titulo__contains=data['titulo'])
        contexto = {'posteos' : posteos}
        return render(
        request,
        template_name='blog_app/buscar_posteos.html',
        context=contexto
        )



def crear_comentario(request):
    if request.method == 'GET':
        contexto = {'formulario_comentario' : Crear_comentario}
        return render(
        request,
        template_name='blog_app/crear_comentario.html',
        context=contexto
        )
    else:
        print(request.POST)
        formulario = Crear_comentario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            comentario = Comentario(texto = data["texto"])
            comentario.save()
            url_exitosa = reverse('inicio')
        return redirect(url_exitosa)
