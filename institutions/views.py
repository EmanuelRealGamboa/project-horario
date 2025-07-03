from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from institutions.models import Institution, Group
from institutions.serializers import InstitutionSerializer, GroupSerializer

class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    permission_classes = [IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
