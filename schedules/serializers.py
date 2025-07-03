from rest_framework import serializers
from .models import Subject, Room, Schedule, TeacherAvailability
from conflicts.utils import detect_conflicts
from notifications.utils import notify_conflicts

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

    def create(self, validated_data):
        schedule = super().create(validated_data)
        conflicts = detect_conflicts(schedule)
        notify_conflicts(conflicts)
        return schedule

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        conflicts = detect_conflicts(instance)
        notify_conflicts(conflicts)
        return instance

class TeacherAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherAvailability
        fields = '__all__'
