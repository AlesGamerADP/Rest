from django.urls import path
from rest_framework import routers
from .views import (
    PersonaViewSet,
    FilterPersona,
    PersonaListView,
    PersonaDetailView,
    PersonaUpdateView,
    PersonaDeleteView,
    PersonaCountView,
    PersonaCreateView
)

# -------------------------------------------------------
# Crear un router para manejar las rutas del ViewSet
# -------------------------------------------------------
router = routers.DefaultRouter()

# Registrar el ViewSet de Persona en el router
# Esto automáticamente crea rutas para listar, crear, obtener, actualizar y eliminar personas
router.register('api/personas', PersonaViewSet, 'personas')

# -------------------------------------------------------
# Rutas definidas manualmente para vistas basadas en clases
# -------------------------------------------------------
urlpatterns = [
    # Filtro de personas usando DjangoFilterBackend
    path('api/personas/filter_personas/', FilterPersona.as_view(), name='filter_personas'),
    
    # Búsqueda de personas usando SearchFilter
    path('api/personas/list_personas/', PersonaListView.as_view(), name='list_personas'),
    
    # Obtener los detalles de una persona específica (por ID)
    path('api/personas/<int:id>/', PersonaDetailView.as_view(), name='persona_detail'),
    
    # Actualizar datos de una persona existente
    path('api/personas/update/<int:id>/', PersonaUpdateView.as_view(), name='persona_update'),
    
    # Eliminar una persona del sistema
    path('api/personas/delete/<int:id>/', PersonaDeleteView.as_view(), name='persona_delete'),
    
    # Contar cuántas personas existen en la base de datos
    path('api/personas/count/', PersonaCountView.as_view(), name='persona_count'),
    
    # Crear una nueva persona
    path('api/personas/create/', PersonaCreateView.as_view(), name='persona_create'),
]

# -------------------------------------------------------
# Añadir automáticamente las rutas generadas por el router
# -------------------------------------------------------
urlpatterns += router.urls
