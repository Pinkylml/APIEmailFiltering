from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Empresa, Correo
from ..serializers import CorreoSerializer

class RegistrarCorreoAPIView(APIView):
    def post(self, request):
        data = request.data
        print("data",data)
        
        empresa_nombre = data.get('empresa')
        print("Nombre de la empresa:", empresa_nombre)

        try:
            empresa = Empresa.objects.get(nombre=empresa_nombre)
             
        except Empresa.DoesNotExist:
            return Response({"error": "La empresa no está registrada en el catálogo"}, status=status.HTTP_400_BAD_REQUEST)
        data['empresa'] = empresa.id
        serializer = CorreoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Correo registrado exitosamente"}, status=status.HTTP_201_CREATED)
        else:
            print("Serializador no válido:", serializer.errors)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
