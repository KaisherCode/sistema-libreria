from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Libro(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100, verbose_name='Título')
    imagen=models.ImageField(upload_to='imagenes/',null=True, verbose_name='Imágen')
    descripcion=models.TextField(verbose_name='Descripción', null=True)

def _str_(self):
    fila = "Título: " + self.titulo + " - " + "Descripción:" + self.descripcion
    return fila

    def delete(self,using=None,keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()