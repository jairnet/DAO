from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from datetime import datetime, date, time, timedelta
import calendar

from .models import Articulo
# Create your views here.

class Promociones(ListView):
	model = Articulo
	template_name = "promociones/promociones.html"