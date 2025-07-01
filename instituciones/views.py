from rest_framework import viewsets
from instituciones.models import Institucion, Grupo
from instituciones.serializers import InstitucionSerializer, GrupoSerializer

class InstitucionViewSet(viewsets.ModelViewSet):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
