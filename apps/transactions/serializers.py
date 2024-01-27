from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)

    def validate(self, data):
        if data['cedula_representante'] == '':
            raise serializers.ValidationError('El número de identidad es requerido')
        if data['cedula_estudiante'] == '':
            raise serializers.ValidationError('El código del estudiante es requerido')
        if data['amount'] == '':
            raise serializers.ValidationError('El monto es requerido')
        if data['amount'] < 0:
            raise serializers.ValidationError('El monto debe ser mayor a 0')

        return data
