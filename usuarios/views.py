from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from usuarios.models import Usuario, Profesor
from usuarios.serializers import UsuarioSerializer, ProfesorSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    permission_classes = [IsAuthenticated]
