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
    path('api/filter_personas/', FilterPersona.as_view(), name='filter_personas'),
    
    # Búsqueda de personas usando SearchFilter
    path('api/list_personas/', PersonaListView.as_view(), name='list_personas'),
    
    # Obtener los detalles de una persona específica (por ID)
    path('api/persona/<int:id>/', PersonaDetailView.as_view(), name='persona_detail'),
    
    # Actualizar datos de una persona existente
    path('api/persona/update/<int:id>/', PersonaUpdateView.as_view(), name='persona_update'),
    
    # Eliminar una persona del sistema
    path('api/persona/delete/<int:id>/', PersonaDeleteView.as_view(), name='persona_delete'),
    
    # Contar cuántas personas existen en la base de datos
    path('api/persona/count/', PersonaCountView.as_view(), name='persona_count'),
    
    # Crear una nueva persona
    path('api/persona/create/', PersonaCreateView.as_view(), name='persona_create'),
]

# -------------------------------------------------------
# Añadir automáticamente las rutas generadas por el router
# -------------------------------------------------------
urlpatterns += router.urls
