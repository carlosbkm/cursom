from django.conf.urls import patterns, include, url

urlpatterns = patterns('cursom.apps.home.views',
	url(r'^$', 'index', name="index"),
	url(r'^agregar/', 'agregar', name="agregar"),
	url(r'^actualizar/(?P<id_p>.*)/$','actualizar', name="actualizar"),
)