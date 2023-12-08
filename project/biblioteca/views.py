from django.shortcuts import render
from .forms import LibroBuscarFormulario, LibroFormulario


def home(request):
    return render(request, "biblioteca/index.html")


def libro_crear(request):
    if request.method == "GET":
        # Mostrar formulario
        context = {"form":LibroFormulario()}
        return render(request, "biblioteca/formulario_avanzado.html")
    else:
        # Procesar formulario
        pass  # Agregar aquí la lógica para procesar el formulario