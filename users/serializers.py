from rest_framework import serializers
from users.models import User
from api.enums import RoleEnum
from rest_framework import serializers
from users.models import User

class RegisterStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password_hash', 'institution_name']
        extra_kwargs = {
            'password_hash': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            institution_name=validated_data.get('institution_name'),
            role=RoleEnum.STUDENT
        )
        user.set_password(validated_data['password_hash'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Usuario no encontrado.")

        if not user.check_password(data['password']):
            raise serializers.ValidationError("Contraseña incorrecta.")

        return {
            "username": user.username,
            "email": user.email,
            "role": user.role,
            "institution_name": user.institution_name
        }
    

class RegisterTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password_hash', 'institution_name']
        extra_kwargs = {
            'password_hash': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            institution_name=validated_data.get('institution_name'),
            role=RoleEnum.TEACHER
        )
        user.set_password(validated_data['password_hash'])
        user.save()
        return user
