from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from notificaciones.models import Notificacion
from notificaciones.serializers import NotificacionSerializer

class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer
    permission_classes = [IsAuthenticated]
