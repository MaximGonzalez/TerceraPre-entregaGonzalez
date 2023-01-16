from django import forms

class crear_posteo(forms.Form):
    titulo = forms.CharField(label="Titulo del posteo", max_length=64)
    contenido = forms.CharField(label="Contenido del posteo", widget=forms.Textarea, max_length=256)