from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView

from .models import Archivo, PuntosVenta
# Create your views here.

class Index(ListView):
	model = Archivo
	template_name = "documentos/index.html"

class NuestraEmpresa(ListView):
	model = Archivo
	template_name = "documentos/nuestra_empresa.html"	

class Nosotros(ListView):
	model = Archivo
	template_name = "documentos/nosotros.html"

class Puntos(ListView):
	model = PuntosVenta
	template_name = "documentos/puntos.html"	