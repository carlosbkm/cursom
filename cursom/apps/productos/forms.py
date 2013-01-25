# -*- coding: utf-8 -*-
from django import forms
from cursom.apps.productos.models import Categoria

choicess = ((categoria.id, categoria.nombre) for categoria in Categoria.objects.all())

class AgregarForm(forms.Form):
	nombre = forms.CharField(widget = forms.TextInput(), required=True)
	categoria = forms.ChoiceField(choices=choicess, label="Categoría", required=True)
	descripcion = forms.CharField(widget = forms.Textarea(), label="Descripción", required=True)
