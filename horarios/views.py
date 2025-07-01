from rest_framework import viewsets
from horarios.models import Materia, Salon, Horario, DisponibilidadProfesor
from horarios.serializers import (
    MateriaSerializer, SalonSerializer, HorarioSerializer, DisponibilidadProfesorSerializer
)

class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

class SalonViewSet(viewsets.ModelViewSet):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class DisponibilidadProfesorViewSet(viewsets.ModelViewSet):
    queryset = DisponibilidadProfesor.objects.all()
    serializer_class = DisponibilidadProfesorSerializer
