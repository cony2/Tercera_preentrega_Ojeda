from django import forms

class LibroFormulario(forms.Form):
    id_articulo = forms.CharField(max_length=100)
    titulo = forms.CharField(max_length=100)
    #autor = forms.ForeignKey(Autor, on_delete=models.CASCADE)


class LibroBuscarFormulario(forms.Form):
    id_articulo = forms.CharField(max_length=100)