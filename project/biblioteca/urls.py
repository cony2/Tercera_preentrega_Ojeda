
from django.contrib import admin
from django.urls import path
from . import views

app_name = "biblioteca"

urlpatterns = [
    path("", views.home, name="index"),
    # path('/crear', views.libro_crear, name='crear-libro')
]
