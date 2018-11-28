from . import views 
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .views import eliminarMascotas, editarMascotas

urlpatterns=[
    url(r'^index/$|^$', views.index,name="index"),
    url(r'^login/$', views.ingresar, name="login"),
    url(r'^registrate/$', views.registrate, name="registrate"),
    url(r'^registroExitoso/$', views.registro, name="registroExitoso"),
    url(r'^salir/$', views.salir, name="logout"),
    url(r'^mascotas/$', views.mascotas, name="mascotas"),
    url(r'^editarMascotas/(?P<idMascota>\d+)/$', editarMascotas, name="editarMascotas"),
    url(r'^eliminarMascotas/(?P<idMascota>\d+)/$', eliminarMascotas, name="eliminarMascotas"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)