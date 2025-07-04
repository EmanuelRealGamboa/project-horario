from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.models import User, Teacher
from users.serializers import UserSerializer, TeacherSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]
