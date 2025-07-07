from rest_framework import serializers
from .models import User, Teacher

#class UserSerializer(serializers.ModelSerializer):
  #  password = serializers.CharField(write_only=True, required=True)

   # class Meta:
    #    model = User
     #   fields = ['id', 'username', 'email', 'password', 'role', 'institution', 'created_at']

    #def create(self, validated_data):
     #   password = validated_data.pop('password')
      #  user = User(**validated_data)
       # user.password_hash = password  # Solo si no usas AbstractUser
        #user.save()
        #return user

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
