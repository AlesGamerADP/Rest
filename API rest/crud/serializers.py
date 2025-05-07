from rest_framework import serializers
from .models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'  # Serializa todos los campos del modelo Persona
        # fields = ['id', 'nombre', 'apellido', 'edad', 'email', 'telefono']  # O puedes especificar los campos manualmente
        read_only_fields = ['id']  # Solo lectura para el campo id