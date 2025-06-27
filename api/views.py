from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from .models import Profesor, Disponibilidad, Horario, Solicitud
from .serializers import (
    ProfesorSerializer, DisponibilidadSerializer,
    HorarioSerializer, SolicitudSerializer
)

class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user and hasattr(user, 'profesor'):
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'role': 'maestro'})
        return Response({'error': 'Credenciales inválidas o rol incorrecto.'},
                        status=status.HTTP_401_UNAUTHORIZED)

class ProfesorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    permission_classes = [permissions.IsAuthenticated]

class DisponibilidadViewSet(viewsets.ModelViewSet):
    queryset = Disponibilidad.objects.all()
    serializer_class = DisponibilidadSerializer
    permission_classes = [permissions.IsAuthenticated]

class HorarioViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HorarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Horario.objects.filter(profesor__user=self.request.user)

class SolicitudViewSet(viewsets.ModelViewSet):
    serializer_class = SolicitudSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Solicitud.objects.filter(profesor__user=self.request.user)

    @action(detail=True, methods=['post'])
    def cancelar(self, request, pk=None):
        solicitud = self.get_object()
        motivo = request.data.get('motivo')
        solicitud.estado = Solicitud.PENDIENTE
        solicitud.motivo = motivo
        solicitud.save()
        # TODO: integrar servicio de envío de SMS aquí
        return Response({'status': 'cancelación solicitada y SMS enviado'})
