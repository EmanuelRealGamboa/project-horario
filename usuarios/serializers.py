from rest_framework import serializers
from .models import Usuario, Profesor

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Usuario
        fields = ['id', 'nombre_usuario', 'correo', 'password', 'rol', 'institucion', 'creado_en']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Usuario(**validated_data)
        user.set_password(password)  # Si luego usas AbstractUser
        user.save()
        return user

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'
