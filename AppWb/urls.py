from django.urls import path 
from AppWb import views


urlpatterns = [
 
    path('', views.inicio, name='Inicio'),
    path('asociados',views.asociados, name='Asociados'),
    path('equipos', views.equipos, name='Equipos'),
    path('cursos',views.cursos, name='Cursos'),
    path('equiposFormularios',views.equiposFormularios, name='EquiposFormularios'),
]
