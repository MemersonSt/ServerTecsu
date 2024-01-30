from rest_framework import serializers
from .models import User, Students

# ESTUDIANTE
class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = (
            'id',
            'cedula_estudiante',
            'uid',
            'name',
            'last_name',
            'balance',
            'Representative',
        )

    def validate(self, data):
        if data['cedula_estudiante'] == Students.cedula_estudiante:
            raise serializers.ValidationError('La cédula del estudiante ya existe')
        if data['name'] == '':
            raise serializers.ValidationError('El nombre del estudiante es requerido')
        if data['last_name'] == '':
            raise serializers.ValidationError('El apellido del estudiante es requerido')
        if data['cedula_estudiante'] == Students.cedula_estudiante:
            raise serializers.ValidationError('La cédula del estudiante ya existe')
        if data['uid'] == Students.uid:
            raise serializers.ValidationError('El uid del estudiante ya existe')

        return data

class UserTokenSerializer(serializers.ModelSerializer):
    students = StudentsSerializer(source='students_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'name',
            'last_name',
            'students',
        )

# USUARIO
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['groups', 'user_permissions', 'is_staff', 'is_active', 'is_superuser', 'last_login']

    # Una funciona que encripta las constraseñas y nos retorna un usuario con la constraseña encriptada
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def validate(self, data):
        if data['numero_identidad'] == '':
            raise serializers.ValidationError('El número de identidad es requerido')
        if data['username'] == User.username:
            raise serializers.ValidationError('El nombre de usuario ya existe')
        if data['numero_identidad'] == User.numero_identidad:
            raise serializers.ValidationError('El número de identidad ya existe')

        return data


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'numero_identidad',
            'password',
            'name',
            'last_name',
        )



#Para buscar un usuario y estudiante por su numero de identidad
class UserDetailSerializer(serializers.Serializer):
    numero_identidad = serializers.CharField(max_length=20)

    def validate(self, data):
        if data['numero_identidad'] == '':
            raise serializers.ValidationError('El número de identidad es requerido')
        return data

class EstudentsDetailSerializer(serializers.Serializer):
    cedula_estudiante = serializers.CharField(max_length=20)

    def validate(self, data):
        if data['cedula_estudiante'] == '':
            raise serializers.ValidationError('La cédula del estudiante es requerida')
        return data


# VINCULAR
class VincularSerializer(serializers.Serializer):
    numero_identidad = serializers.CharField(max_length=20)
    cedula_estudiante = serializers.CharField(max_length=20)
