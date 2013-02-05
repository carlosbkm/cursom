# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from cursom.apps.productos.models import Categoria
from cursom.apps.productos.models import Producto

class AgregarForm(forms.Form):
	nombre = forms.CharField(widget = forms.TextInput(), required=True)
	categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), required=True, label="Categoría")
	descripcion = forms.CharField(widget = forms.Textarea(), label="Descripción", required=True)

class ActualizarForm(ModelForm):
	class Meta:
		model = Producto
		#Campos que se mostraran
		fields = ('nombre','categoria','descripcion',)
		# exclude = ('usuario', 'disponible',) <- Datos que se excluirán. Sirve de la misma manera las dos formas