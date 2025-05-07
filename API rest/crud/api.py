from .models import Persona
from rest_framework import viewsets, permissions
from .serializers import PersonaSerializer


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    permission_class = [permissions.AllowAny]
    serializer_class = PersonaSerializer