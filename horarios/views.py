from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from horarios.models import Materia, Salon, Horario, DisponibilidadProfesor
from horarios.serializers import (
    MateriaSerializer, SalonSerializer, HorarioSerializer, DisponibilidadProfesorSerializer
)

class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
    permission_classes = [IsAuthenticated]

class SalonViewSet(viewsets.ModelViewSet):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer
    permission_classes = [IsAuthenticated]

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    permission_classes = [IsAuthenticated]

class DisponibilidadProfesorViewSet(viewsets.ModelViewSet):
    queryset = DisponibilidadProfesor.objects.all()
    serializer_class = DisponibilidadProfesorSerializer
    permission_classes = [IsAuthenticated]
