from rest_framework import serializers
from .models import User, Estudents


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'name',
            'last_name',
            'numero_identidad',
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

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'name',
            'last_name',
            'numero_identidad',
        )


class EstudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudents
        fields = (
            'id',
            'code_students',
            'name',
            'last_name',
            'balance',
            'Representative',
        )


class VincularSerializer(serializers.Serializer):
    numero_identidad = serializers.CharField(max_length=20)
    code_students = serializers.IntegerField()
