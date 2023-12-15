from django.shortcuts import render
from .forms import LibroBuscarFormulario, LibroFormulario
from . import models


def home(request):
    libros = models.Libro.objects.all()
    context = {"libros": libros}

    return render(request, "biblioteca/index.html", context)

def crear_libros_varios(request):
    pass
    

