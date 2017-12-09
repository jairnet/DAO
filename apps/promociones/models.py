from django.db import models

# Create your models here.

class Articulo(models.Model):
	nombre_articulo = models.CharField(max_length=50)
	presentacion = models.CharField(max_length=50)
	precio_venta = models.FloatField(max_length=50)
	precio_promo = models.FloatField(max_length=50)
	fecha_terminacion = models.DateField()
	descripcion = models.TextField(max_length=100)
	imagen_articulo = models.FileField(upload_to='imagenes/')

	class Meta:
		ordering = ["nombre_articulo"]
		verbose_name_plural = "Articulos"

	def __str__(self): # __unicode__ en Python 2
		return self.nombre_articulo