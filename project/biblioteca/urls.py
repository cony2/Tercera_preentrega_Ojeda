
from django.contrib import admin
from django.urls import path
from . import views

app_name = "biblioteca"

urlpatterns = [
    path("", views.home, name="index"),
    path ("crear/libro", views.crear_libro, name="crear-libro"),
    path("crear/categoria", views.crear_categoria, name="crear-categoria"),
    path("crear/compra", views.crear_compra, name="crear-compra")

   
]
