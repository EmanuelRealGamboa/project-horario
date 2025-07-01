from django.urls import path, include
from rest_framework.routers import DefaultRouter
from horarios.views import (
    MateriaViewSet, SalonViewSet, HorarioViewSet, DisponibilidadProfesorViewSet
)

router = DefaultRouter()
router.register(r'materias', MateriaViewSet)
router.register(r'salones', SalonViewSet)
router.register(r'horarios', HorarioViewSet)
router.register(r'disponibilidad-profesores', DisponibilidadProfesorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
