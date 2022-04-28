from django.urls import path 
from AppWb import views


urlpatterns = [
 
    path('', views.inicio),
    path('asociados',views.asociados, name='Empleados'),
    path('equipos', views.equipos),
    path('cursos',views.cursos),
]
