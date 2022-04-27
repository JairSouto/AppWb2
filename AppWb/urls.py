from django.urls import path 
from AppWb import views


urlpatterns = [
 
    path('', views.inicio),
    path('empleados',views.empleados, name='Empleados'),
    path('TiposDTrabajo', views.TiposDTrabajo),
    path('Materiales',views.TiposDmateriales),
]
