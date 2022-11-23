from django.urls import path, include
from miappfamilia.views import *

urlpatterns = [
    
    path('inicio/', inicio),
    path('pantalones/', pantalones),
    path('camisas/', camisas),
      
]   

