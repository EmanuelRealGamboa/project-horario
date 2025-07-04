from rest_framework import serializers
from .models import ScheduleConflict

class ScheduleConflictSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleConflict
        fields = '__all__'
