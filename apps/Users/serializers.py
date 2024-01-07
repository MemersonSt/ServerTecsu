from rest_framework import serializers
from .models import User, Estudents


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'name',
            'last_name'
        )


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['groups', 'user_permissions', 'is_staff', 'is_active', 'is_superuser', 'last_login']

    # Una funciona que encripta las constraseñas y nos retorna un usuario con la constraseña encriptada
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    # Una funcion que se llama para listar mostrando solo datos seleccionados en vez de todos
    def to_representation(self, instance):
        return {
            'id': instance['id'],  # se accede a la clave del valor con ['valor requerido']
            # Se puede cambiar el username a usuario sin necesidad cambiar el original
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password']
        }


class EstudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudents
        fields = '__all__'




