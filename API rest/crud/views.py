from rest_framework import permissions, viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Persona
from .serializers import PersonaSerializer

# --------------------------------------------------------
# ViewSet principal para manejar todas las operaciones CRUD
# --------------------------------------------------------
class PersonaViewSet(viewsets.ModelViewSet):
    """
    ViewSet que permite listar, crear, actualizar y eliminar objetos Persona.
    No requiere autenticación para acceder.
    """
    queryset = Persona.objects.all()  # Todos los registros de Persona
    permission_classes = [permissions.AllowAny]  # Acceso público sin autenticación
    serializer_class = PersonaSerializer  # Serializador para convertir objetos a JSON

# --------------------------------------------------------------------
# Vista para filtrar personas por campos específicos usando filtros
# --------------------------------------------------------------------
class FilterPersona(generics.ListAPIView):
    """
    Permite filtrar personas por nombre y correo electrónico.
    Usa DjangoFilterBackend para aplicar filtros directamente en la URL.
    Ejemplo: /api/filter_personas/?nombre=Juan&email=juan@example.com
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'email']  # Campos disponibles para filtrar

# ----------------------------------------------------------------------
# Vista para realizar búsqueda simple por nombre o email (modo LIKE)
# ----------------------------------------------------------------------
class PersonaListView(generics.ListAPIView):
    """
    Permite buscar personas mediante coincidencias parciales.
    Ejemplo: /api/list_personas/?search=ana buscará en nombre y email.
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'email']

# ------------------------------------------------------------
# Vista para obtener los detalles de una persona por su ID
# ------------------------------------------------------------
class PersonaDetailView(generics.RetrieveAPIView):
    """
    Devuelve los detalles completos de una persona específica por ID.
    Ejemplo: /api/persona/5/
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    lookup_field = 'id'  # Campo por el que se buscará

# ------------------------------------------------------------
# Vista para actualizar una persona existente
# ------------------------------------------------------------
class PersonaUpdateView(generics.UpdateAPIView):
    """
    Actualiza información parcial o completa de una persona.
    Solo acepta métodos PUT o PATCH.
    Ejemplo: /api/persona/update/5/
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    lookup_field = 'id'

# ------------------------------------------------------------
# Vista para eliminar una persona por su ID
# ------------------------------------------------------------
class PersonaDeleteView(generics.DestroyAPIView):
    """
    Elimina una persona de la base de datos.
    Ejemplo: /api/persona/delete/3/
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    lookup_field = 'id'

# ------------------------------------------------------------
# Vista para contar cuántas personas existen en total
# ------------------------------------------------------------
class PersonaCountView(generics.GenericAPIView):
    """
    Retorna el número total de personas registradas.
    Ejemplo: /api/persona/count/
    """
    def get(self, request, *args, **kwargs):
        total_personas = Persona.objects.count()
        return Response({'total_personas': total_personas})

# ------------------------------------------------------------
# Vista para crear una nueva persona en la base de datos
# ------------------------------------------------------------
class PersonaCreateView(generics.CreateAPIView):
    """
    Permite registrar una nueva persona.
    Ejemplo: POST en /api/persona/create/ con los datos necesarios.
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
