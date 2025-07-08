from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterStudentSerializer, LoginSerializer, RegisterTeacherSerializer
from .permissions import IsAdminUserRole  

class RegisterStudentView(APIView):
    permission_classes = [AllowAny]  

    def post(self, request):
        serializer = RegisterStudentSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'msg': 'Registro exitoso',
                'username': user.username,
                'email': user.email,
                'role': user.role
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]  

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterTeacherView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUserRole]  

    def post(self, request):
        serializer = RegisterTeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Maestro registrado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
