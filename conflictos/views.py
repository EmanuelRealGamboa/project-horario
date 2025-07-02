from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from conflictos.models import ConflictoHorario
from conflictos.serializers import ConflictoHorarioSerializer

class ConflictoHorarioViewSet(viewsets.ModelViewSet):
    queryset = ConflictoHorario.objects.all()
    serializer_class = ConflictoHorarioSerializer
    permission_classes = [IsAuthenticated]

