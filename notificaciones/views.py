from rest_framework import viewsets
from notificaciones.models import Notificacion
from notificaciones.serializers import NotificacionSerializer

class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer
