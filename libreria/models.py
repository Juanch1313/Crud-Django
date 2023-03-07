from django.db import models

# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=30, verbose_name='Título')
    imagen = models.ImageField(upload_to='imagenes/', null=True, verbose_name='Imagen')
    descripcion = models.TextField(max_length=50, null=True, verbose_name='Descripción')
    
    def __str__(self) -> str:
        return f"Titulo: {self.titulo} - Descripcion: {self.descripcion}"
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()