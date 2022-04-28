

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
            equipos.save()

            return render(request,"AppWb/inicio.html")
    else:
        miFormulario= EquiposFormularios()
    return render(request,'AppWb/equiposFormularios.html', {'miFormulario':miFormulario})
def busquedaSeguidores(request):
    return render(request, 'AppWb/busquedaSeguidores.html')

def buscar(request):
    if request.GET['seguidores']:
        seguidores=request.GET['seguidores']
        equipos=Equipos.objects.filter(seguidores__icontains=seguidores)
        return render(request, "AppWb/resultadoBusqueda.html",{'equipos':equipos, 'seguidores':seguidores})
   # respuesta =f"Estoy este numero de seguidores :{request.GET['seguidores']}"#
    else:
        respuesta ="No enviaste Datos"
        return HttpResponse(respuesta)

