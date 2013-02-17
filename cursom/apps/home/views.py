# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from cursom.apps.productos.models import Producto
from django.contrib.auth.decorators import login_required
from cursom.apps.productos.forms import AgregarForm, ActualizarForm
from django.http import HttpResponseRedirect

def index(request):
	producto = Producto.objects.filter(disponible=True).order_by('-id');
	ctx = {'producto':producto}
	return render_to_response('home/index.html', ctx ,context_instance = RequestContext(request))

@login_required
def agregar(request):
	form = AgregarForm
	

	if request.method == "POST":
		form = AgregarForm(request.POST)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			descripcion = form.cleaned_data['descripcion']
			categoria = form.cleaned_data['categoria'].id

			p = Producto()
			p.nombre = nombre
			p.descripcion = descripcion
			p.categoria_id = categoria
			p.usuario_id = request.user.id
			p.save()
			return HttpResponseRedirect('/')


			
	ctx = {'form':form}
	return render_to_response('home/agregar.html', ctx ,context_instance = RequestContext(request))

@login_required
def actualizar(request, id_p):
	dato = get_object_or_404(Producto, id=id_p)
	p = Producto.objects.get(id=id_p)
	form = ActualizarForm(instance=p)
	if request.method == "POST":
		#Aquí decimos a Django que estamos actualizando y no insertando
		form = ActualizarForm(request.POST, instance=p)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')

	ctx = {'form':form}
	return render_to_response('home/actualizar.html', ctx, context_instance = RequestContext(request))
