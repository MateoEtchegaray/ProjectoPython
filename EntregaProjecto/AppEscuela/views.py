from django.http import HttpResponse
from django.shortcuts import render
from.models import Curso
from.forms import CursoFormulario


# Create your views here.

def curso(req, nombre , grupo):


    curso = Curso(nombre = nombre, grupo = grupo)
    curso.save()


    return HttpResponse(f"<p>Curso: {curso.nombre} - Grupo: {curso.grupo} agregado! </p>")


def lista_cursos(req):

    lista = Curso.objects.all()

    return render(req, "lista_cursos.html" , {"lista_cursos" : lista}) 


def inicio(req):

    return render(req, "inicio.html")

def cursos(req):


    return HttpResponse('cursos.html')

def profesores(req):


    return HttpResponse('profesores.html')

def estudiantes(req):


    return HttpResponse('estudiantes.html')

def entregables(req):


    return HttpResponse('entregables.html')

def curso_formulario(req):

    if req.method == 'POST': 
    
        curso = Curso(nombre=req.Post["curso"], grupo=req.POST["grupo"])
        curso.save()    
        return render(req, 'inicio.html', {"mensaje": "Curso creado con exito"})
    return render(req, "curso_formulario.html")