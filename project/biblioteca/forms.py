from django import forms
from . import models




class LibroForm(forms.ModelForm):
    class Meta:
        model = models.Libro
        fields = "__all__"


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = "__all__"

class CompraForm(forms.ModelForm):
    class Meta:
        model = models.Compra
        fields = "__all__"






# class LibroBuscarFormulario(forms.Form):
#     id_articulo = forms.CharField(max_length=100)