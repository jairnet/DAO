from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView

from .models import Archivo
# Create your views here.

class Index(ListView):
	model = Archivo
	template_name = "documentos/index.html"