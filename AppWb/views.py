
from django.http import HttpResponse
from django.shortcuts import render

from AppWb.forms import EquiposFormularios
from AppWb.models import Equipos


# Create your views here.
def inicio(request):
    return render(request,'AppWb/inicio.html')
def asociados(request):
  return render(request,'AppWb/asociados.html')

def equipos(request):
     return render(request,'AppWb/equipos.html')

def cursos(request):
    return render(request,'AppWb/cursos.html')

def equiposFormularios(request):
    if request.method=='POST':
        miFormulario= EquiposFormularios(request.POST)
        print(miFormulario)


        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            equipos=Equipos(nombre=informacion['nombre'], seguidores=informacion['seguidores'],)
            

            return render(request,"AppWb/inicio.html")
    else:
        miFormulario= EquiposFormularios()
    return render(request,'AppWb/equiposFormularios.html', {'miFormulario':miFormulario})
