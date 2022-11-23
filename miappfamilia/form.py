from django import forms

class camisasFormulario(forms.Form):
    
    nombre = forms.CharField()
    talle = forms.IntegerField()
    color = forms.CharField()
    
class pantalonesFormulario(forms.Form):    
    nombre = forms.CharField()
    talle = forms.IntegerField()
    color = forms.CharField()
    
class familiaFormulario(forms.Form):
    Nombre = forms.CharField()
    Edad = forms.IntegerField
    Fecha_Nac = forms.IntegerField()
    Cargo = forms.CharField()
    