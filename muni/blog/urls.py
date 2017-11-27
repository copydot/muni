from django.conf.urls import include, url
from . import views

urlpatterns = [
   
    url(r'^$', views.lista_publicaciones),
    url(r'^publicacion/(?P<pk>[0-9]+)/$', views.detalle_publicacion, name='detalle_publicacion'),
    url(r'^publicacion/nueva/$', views.nueva_publicacion, name='nueva_publicacion'),
]