from rest_framework import routers
from .api import PersonaViewSet


router = routers.DefaultRouter()

router.register('api/personas', PersonaViewSet, 'personas')

urlpatterns = router.urls