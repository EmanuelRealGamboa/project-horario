from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    LoginView,
    ProfesorViewSet,
    DisponibilidadViewSet,
    HorarioViewSet,
    SolicitudViewSet
)

router = DefaultRouter()
router.register(r'profesores', ProfesorViewSet, basename='profesor')
router.register(r'disponibilidades', DisponibilidadViewSet)
router.register(r'horarios', HorarioViewSet, basename='horario')
router.register(r'solicitudes', SolicitudViewSet, basename='solicitud')

urlpatterns = [
    path('api/login/', LoginView.as_view(), name='api-login'),
    path('api/', include(router.urls)),
]
