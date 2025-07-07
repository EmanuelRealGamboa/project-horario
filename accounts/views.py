
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentRegisterSerializer, StudentLoginSerializer
from django.contrib.auth import login, logout

class StudentRegisterView(APIView):
    def post(self, request):
        serializer = StudentRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Registro exitoso'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentLoginView(APIView):
    def post(self, request):
        serializer = StudentLoginSerializer(data=request.data)
        if serializer.is_valid():
            login(request, serializer.instance)
            return Response({'msg': 'Login exitoso', 'data': serializer.validated_data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'msg': 'Logout exitoso'}, status=status.HTTP_200_OK)
