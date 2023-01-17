from django import forms
from datetime import date


class crear_usuario(forms.Form):
    usuario = forms.CharField(max_length=64)
    contrasenia = forms.CharField(max_length=64)
    mail = forms.EmailField()
    nombre = forms.CharField(max_length=64)
    apellido = forms.CharField(max_length=64)
    fecha_nacimiento = forms.DateField(widget=forms.SelectDateWidget(years=range(date.today().year-100, date.today().year)))

class crear_posteo(forms.Form):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese el título'}), max_length=64)
    contenido = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Ingrese el contenido'}), max_length=256)