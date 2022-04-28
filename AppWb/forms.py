from django import forms

class EquiposFormularios(forms.Form):
    nombre=forms.CharField(max_length=30)

    seguidores=forms.IntegerField()
