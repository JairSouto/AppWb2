from django.http import HttpResponse
from django.shortcuts import render

from AppWb.models import Empleados

# Create your views here.
def inicio(request):
    return render(request,'AppWb/inicio.html')
def empleados(request):
  return render(request,'AppWb/empleos.html')

def TiposDTrabajo(request):
     return render(request,'AppWb/TiposDTrabajo')

def TiposDmateriales(request):
    return render(request,'AppWb/TiposDmateriales.html')