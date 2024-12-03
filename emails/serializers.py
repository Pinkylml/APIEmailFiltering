from rest_framework import serializers
from .models import Correo

class CorreoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correo
        fields = ['destinatario', 'emisor', 'fecha', 'empresa', 'codigo_unico_smtp']
