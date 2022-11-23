from django.shortcuts import render
from miappfamilia.models import Datos_familia
from miappfamilia.models import pantalones
from miappfamilia.models import camisas
from django.template import loader
from django.http import HttpResponse



def inicio(request):
    return render(request, "miappfamilia/index.html")

def familia(request):
    return render(request, "miappfamilia/temp_familia.html")

def pantalones(request):
    return HttpResponse("Producto Pantalones")
    

def camisas(request):
    return HttpResponse("Producto Camisas")

