from django.db import models

# Create your models here.

class Archivo(models.Model):

	TIPO_ARCHIVO = (
		('GDG','Gestion Directiva'),
		('SIC','Sistema Integrado de Calidad'),
		('COM','Compras'),
		('LOG','Logistica'),
		('COM','Comercial'),
		('SER','Servicio al Cliente'),
		('APO','Apoyo'),
		)
	tipo = models.CharField(max_length=20, choices=TIPO_ARCHIVO)
	nombre = models.CharField(max_length=50)
	fecha = models.DateField()
	descripcion = models.TextField(max_length=100)
	archive = models.FileField(upload_to='docuemntos/')

	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "Archivos"

	def __str__(self): # __unicode__ en Python 2
		return self.nombre
	