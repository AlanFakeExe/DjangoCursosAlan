from django.shortcuts import render
from .models import Cursos

# Create your views here.
def cursosP(request):   

    cursos= Cursos.objects.all()
    return render(request, "cursosApp/cursos.html", {"cursos": cursos})

def inicio(request):
    return render(request, "cursosApp/inicio.html")

def contacto(request):
    return render(request, "cursosApp/contacto.html")
