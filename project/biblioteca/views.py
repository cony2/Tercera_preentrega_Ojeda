from django.shortcuts import render, redirect
from . import models


def home(request):
    libros = models.Libro.objects.all()
    context = {"libros": libros}

    return render(request, "biblioteca/index.html", context)

from . import forms

def crear_libro(request):
    if request.method == "POST":
        form = forms.LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("biblioteca:index")
    else:
        form = forms.LibroForm()
    return render(request, "biblioteca/crear_libros.html", {"form": form})
    

def crear_categoria(request):
    if request.method == "POST":
        formulario = forms.CategoriaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("biblioteca:index")
    else:
        formulario = forms.CategoriaForm()
    return render(request, "biblioteca/crear_categoria.html", {"formulario": formulario})

def crear_compra(request):
    if request.method == "POST":
        formulario = forms.CompraForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("biblioteca:index")
    else:
        formulario = forms.CompraForm()
    return render(request, "biblioteca/crear_compra.html", {"formulario": formulario})

