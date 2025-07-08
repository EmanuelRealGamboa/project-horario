from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from conflicts.models import ScheduleConflict
from conflicts.serializers import ScheduleConflictSerializer

class ScheduleConflictViewSet(viewsets.ModelViewSet):
    queryset = ScheduleConflict.objects.all()
    serializer_class = ScheduleConflictSerializer
    permission_classes = [IsAuthenticated] 
