from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def inicio(request):
    return render(request,'AppWb/inicio.html')
def asociados(request):
  return render(request,'AppWb/asociados.html')

def equipos(request):
     return render(request,'AppWb/equipos.html')

def cursos(request):
    return render(request,'AppWb/cursos.html')