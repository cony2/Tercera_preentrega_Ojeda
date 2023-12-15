from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo
    
class Compra(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_compra = models.DateField()


    def __str__(self):
        return f"Compra de '{self.libro}'"