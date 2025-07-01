from rest_framework import serializers
from .models import ConflictoHorario

class ConflictoHorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConflictoHorario
        fields = '__all__'
