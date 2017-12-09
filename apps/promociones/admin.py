from django.contrib import admin
# Register your models here.
from .models import Articulo

#admin.site.register(Articulo):
#	list_display = ('nombre_articulo','presentacion','precio_venta','precio_promo','fecha_terminacion','descripcion','imagen_articulo')
	
admin.site.register(Articulo)