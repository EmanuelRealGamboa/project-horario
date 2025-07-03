from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import SignupSerializer
from .models import User
import random

# Simulación de almacenamiento de códigos (usa Redis o DB en producción)
verification_codes = {}

class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            code = random.randint(100000, 999999)
            verification_codes[user.email] = code
            print(f"[SIMULADO] Código enviado a {user.email} o {user.phone_number}: {code}")
            return Response({'message': 'Código enviado. Verifica tu cuenta.'}, status=201)
        return Response(serializer.errors, status=400)

class VerifyCodeView(APIView):
    def post(self, request):
        email = request.data.get('email')
        code = int(request.data.get('code'))

        if verification_codes.get(email) == code:
            user = User.objects.get(email=email)
            user.is_active = True
            user.is_verified = True
            user.save()
            del verification_codes[email]
            return Response({'message': 'Cuenta verificada con éxito'}, status=200)
        return Response({'error': 'Código inválido'}, status=400)

class SigninView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)

        if user and user.is_active:
            code = random.randint(100000, 999999)
            verification_codes[email] = code
            print(f"[SIMULADO] Código 2FA enviado a {email}: {code}")
            return Response({'message': 'Código 2FA enviado. Verifica para continuar.'}, status=200)
        return Response({'error': 'Credenciales inválidas'}, status=400)

class Confirm2FAView(APIView):
    def post(self, request):
        email = request.data.get('email')
        code = int(request.data.get('code'))

        if verification_codes.get(email) == code:
            user = User.objects.get(email=email)
            del verification_codes[email]
            return Response({'message': 'Inicio de sesión exitoso'}, status=200)
        return Response({'error': 'Código 2FA incorrecto'}, status=400)