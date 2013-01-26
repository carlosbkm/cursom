# -*- coding: utf-8 -*-
from django import forms
from cursom.apps.productos.models import Categoria

class AgregarForm(forms.Form):
	nombre = forms.CharField(widget = forms.TextInput(), required=True)
	categoria = forms.ModelChoiceField(Categoria.objects.all(), required=True)
	descripcion = forms.CharField(widget = forms.Textarea(), label="Descripción", required=True)
