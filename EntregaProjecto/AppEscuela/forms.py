from django import forms

class CursoFormulario(forms.Form):

    curso = forms.CharField(required=True)
    grupo = forms.CharField(required=True)