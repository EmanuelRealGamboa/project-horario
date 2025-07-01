from django.urls import path, include
from rest_framework.routers import DefaultRouter
from instituciones.views import InstitucionViewSet, GrupoViewSet

router = DefaultRouter()
router.register(r'instituciones', InstitucionViewSet)
router.register(r'grupos', GrupoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
