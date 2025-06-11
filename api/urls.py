from django.urls import path, include
from rest_framework import routers
from .views import (
    InstitucionViewSet, UsuarioViewSet, ProfesorViewSet, MateriaViewSet,
    SalonViewSet, GrupoViewSet, HorarioViewSet, NotificacionViewSet,
    RegistroActividadViewSet
)

router = routers.DefaultRouter()
router.register(r'instituciones', InstitucionViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'profesores', ProfesorViewSet)
router.register(r'materias', MateriaViewSet)
router.register(r'salones', SalonViewSet)
router.register(r'grupos', GrupoViewSet)
router.register(r'horarios', HorarioViewSet)
router.register(r'notificaciones', NotificacionViewSet)
router.register(r'registros-actividad', RegistroActividadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
