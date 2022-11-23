from django.shortcuts import render
from miappfamilia.models import Datos_familia
from miappfamilia.models import pantalones
from miappfamilia.models import camisas
from django.template import loader
from django.http import HttpResponse



def inicio(request):
    return render(request, "miappfamilia/index.html")

def pantalones(request):
    return render(request, "miappfamilia/pantalones.html")  

def camisas(request):
    return HttpResponse("Producto Camisas")

