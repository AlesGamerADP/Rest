from rest_framework import serializers
from .models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Persona.

    Este serializador convierte las instancias del modelo Persona a un formato que puede ser fácilmente
    renderizado en JSON o en otro formato, así como también convierte datos enviados a través de la API
    en instancias de modelo Persona.

    La clase `Meta` define los campos que serán serializados y algunas opciones adicionales.
    """
    
    class Meta:
        model = Persona  # Define que este serializador corresponde al modelo Persona
        fields = '__all__'  # Incluye todos los campos del modelo Persona para ser serializados
        # fields = ['id', 'nombre', 'apellido', 'edad', 'email', 'telefono']  # Alternativamente, puedes especificar los campos manualmente
        read_only_fields = ['id']  # Hace que el campo 'id' sea de solo lectura, no será modificado en las solicitudes PUT/PATCH

    def __init__(self, *args, **kwargs):
        """
        Constructor personalizado para el serializador PersonaSerializer.

        Permite hacer que ciertos campos sean requeridos o no según el método HTTP de la solicitud:
        - Para las solicitudes POST (creación), los campos 'nombre', 'apellido', 'email' y 'telefono' son requeridos.
        - Para las solicitudes PUT/PATCH (actualización), esos campos no son requeridos.

        La validación de campos es controlada por este constructor en función del tipo de solicitud.
        """
        # Llamamos al constructor de la clase padre para asegurarnos de que las inicializaciones de campos por defecto se realicen correctamente.
        super().__init__(*args, **kwargs)

        # Verificamos el método HTTP de la solicitud para decidir si los campos son requeridos o no.
        if self.context['request'].method == 'POST':
            # Para las solicitudes de tipo POST (creación), hacemos que los campos sean obligatorios.
            self.fields['nombre'].required = True
            self.fields['apellido'].required = True
            self.fields['email'].required = True
            self.fields['telefono'].required = True
        else:
            # Para las solicitudes PUT/PATCH (actualización), los campos no son requeridos.
            self.fields['nombre'].required = False
            self.fields['apellido'].required = False
            self.fields['edad'].required = False
            self.fields['email'].required = False
            self.fields['telefono'].required = False
