from rest_framework import viewsets
from conflictos.models import ConflictoHorario
from conflictos.serializers import ConflictoHorarioSerializer

class ConflictoHorarioViewSet(viewsets.ModelViewSet):
    queryset = ConflictoHorario.objects.all()
    serializer_class = ConflictoHorarioSerializer
