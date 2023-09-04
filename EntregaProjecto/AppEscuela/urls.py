from django.urls import path
from AppEscuela.views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<grupo>', curso),
    path('lista-cursos', lista_cursos),
    path('', inicio),
    path('cursos/', cursos),
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
    path('curso-formulario/', curso_formulario, name="CursoFormulario"),

]