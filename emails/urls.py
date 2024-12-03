from django.urls import path
from .views.registro import RegistrarCorreoAPIView
from .views.busqueda import BuscarCorreoAPIView

urlpatterns = [
    path('correos/registrar/', RegistrarCorreoAPIView.as_view(), name='registrar_correo'),
    path('correos/buscar/', BuscarCorreoAPIView.as_view(), name='buscar_correo'),
]