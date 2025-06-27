from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profesor, Disponibilidad, Curso, Aula, Horario, Solicitud

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ProfesorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profesor
        fields = ['id', 'user', 'departamento']

class DisponibilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disponibilidad
        fields = ['id', 'profesor', 'dia_semana', 'hora_inicio', 'hora_fin', 'tipo']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nombre']

class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = ['id', 'nombre']

class HorarioSerializer(serializers.ModelSerializer):
    curso = CursoSerializer()
    aula = AulaSerializer()

    class Meta:
        model = Horario
        fields = ['id', 'profesor', 'curso', 'aula', 'dia_semana', 'hora_inicio', 'hora_fin']

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ['id', 'profesor', 'motivo', 'estado', 'creado']
