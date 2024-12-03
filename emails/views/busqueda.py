
       

from rest_framework.generics import ListAPIView
from rest_framework.exceptions import ValidationError
from ..models import Correo
from ..serializers import CorreoSerializer
from django.db.models import Q
from datetime import datetime

class BuscarCorreoAPIView(ListAPIView):
    serializer_class = CorreoSerializer

    def get_queryset(self):
        queryset = Correo.objects.all()

        filtros = self.request.query_params

        if not filtros or not any(filtros.values()):
            return {}  # Retorna un diccionario vacío si no hay filtros
        
        contenido = filtros.get('contenido', None)
        if contenido:
            queryset = queryset.filter(Q(destinatario__icontains=contenido) | Q(emisor__icontains=contenido) | Q(contenido__icontains=contenido))

        
        destinatario = filtros.get('destinatario', None)
        if destinatario:
            queryset = queryset.filter(destinatario__icontains=destinatario)

        emisor = filtros.get('emisor', None)
        if emisor:
            queryset = queryset.filter(emisor__icontains=emisor)

        # Filtros por fecha
        fecha_inicio = filtros.get('fecha_inicio', None)
        if fecha_inicio:
            try:
                fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
                queryset = queryset.filter(fecha__gte=fecha_inicio)
            except ValueError:
                raise ValidationError("El formato de 'fecha_inicio' debe ser 'YYYY-MM-DD'")

        fecha_fin = filtros.get('fecha_fin', None)
        if fecha_fin:
            try:
                fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
                queryset = queryset.filter(fecha__lte=fecha_fin)
            except ValueError:
                raise ValidationError("El formato de 'fecha_fin' debe ser 'YYYY-MM-DD'")

        # Filtro por empresa (busca por ID)
        empresa = filtros.get('empresa', None)
        if empresa:
            if empresa.isdigit():  # Asegura que el filtro sea un número (ID)
                queryset = queryset.filter(empresa_id=empresa)
            else:
                raise ValidationError("El parámetro 'empresa' debe ser un ID numérico de la empresa.")

        # Paginación manual
        page_size = filtros.get('size', 10)  # Por defecto, 10 resultados por página
        page = filtros.get('page', 1)         # Página actual (por defecto, página 1)

        # Se calcula el rango para la paginación
        start = (int(page) - 1) * int(page_size)
        end = int(page) * int(page_size)

        queryset = queryset[start:end]

        return queryset