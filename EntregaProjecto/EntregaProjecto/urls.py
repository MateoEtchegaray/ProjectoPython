from django.contrib import admin
from django.urls import path, include
from AppEscuela.views import curso, lista_cursos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app-escuela/', include('AppEscuela.urls') )
    
]
