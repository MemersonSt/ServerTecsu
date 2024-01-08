from rest_framework import serializers
from .models import Transaction
from apps.Users.models import User, Estudents
from rest_framework.response import Response
from rest_framework import status


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)

    # se modifica el is_valid para validar que el estudiante exista en modelo Estudents de la app Users
    # def is_valid(self, raise_exception=False):
    #     # se obtiene el dato del campo code_student
    #     code_student = self.initial_data.get('code_student')
    #     # se obtiene el dato del campo identidad
    #     identidad = self.initial_data.get('identidad')
    #
    #     # se valida que el estudiante exista en el modelo Estudents de la app Users
    #     estudent = Estudents.objects.filter(code_student=code_student).first()
    #     if not estudent:
    #         return Response({"code_student": ["Estudiante no encontrado."]}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     # se valida que el usuario exista en el modelo User de la app Users
    #     user = User.objects.filter(numero_identidad=identidad).first()
    #     if not user:
    #         return Response({"numero_identidad": ["Usuario no encontrado."]}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     return super(TransactionSerializer, self).is_valid(raise_exception=raise_exception)
