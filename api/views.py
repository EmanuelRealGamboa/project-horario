from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.permissions import BasePermission
from .models import (
    Institucion, Usuario, Profesor, Materia, Salon,
    Grupo, Horario, Notificacion, RegistroActividad
)
from .serializers import (
    InstitucionSerializer, UsuarioSerializer, ProfesorSerializer,
    MateriaSerializer, SalonSerializer, GrupoSerializer,
    HorarioSerializer, NotificacionSerializer, RegistroActividadSerializer
)

class IsAdminPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.rol == 'ADMIN'

class InstitucionViewSet(viewsets.ModelViewSet):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer
    permission_classes = [IsAuthenticated, IsAdminPermission]

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
  

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    permission_classes = [IsAuthenticated]

class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
    permission_classes = [IsAuthenticated]

class SalonViewSet(viewsets.ModelViewSet):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer
    permission_classes = [IsAuthenticated]

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    permission_classes = [IsAuthenticated]

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    permission_classes = [IsAuthenticated]

class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer
    permission_classes = [IsAuthenticated]

class RegistroActividadViewSet(viewsets.ModelViewSet):
    queryset = RegistroActividad.objects.all()
    serializer_class = RegistroActividadSerializer
    permission_classes = [IsAuthenticated]



def registrar_actividad(usuario, accion, descripcion):
    RegistroActividad.objects.create(
        usuario=usuario,
        accion=accion,
        descripcion=descripcion
    )

def perform_create(self, serializer):
    instance = serializer.save()
    registrar_actividad(self.request.user, "Creación de institución", f"Se creó la institución {instance.nombre}")
    


