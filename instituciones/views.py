from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from instituciones.models import Institucion, Grupo
from instituciones.serializers import InstitucionSerializer, GrupoSerializer

class InstitucionViewSet(viewsets.ModelViewSet):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer
    permission_classes = [IsAuthenticated]

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    permission_classes = [IsAuthenticated]
