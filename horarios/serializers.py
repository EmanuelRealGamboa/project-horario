from rest_framework import serializers
from .models import Materia, Salon, Horario, DisponibilidadProfesor
from conflictos.utils import detectar_conflictos
from notificaciones.utils import notificar_conflictos

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__'

class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = '__all__'

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'

    def create(self, validated_data):
        horario = super().create(validated_data)
        conflictos = detectar_conflictos(horario)
        notificar_conflictos(conflictos)
        return horario

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        conflictos = detectar_conflictos(instance)
        notificar_conflictos(conflictos)
        return instance

class DisponibilidadProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisponibilidadProfesor
        fields = '__all__'
