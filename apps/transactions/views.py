from rest_framework import generics
from .serializers import TransactionSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction, Students, User
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator


@method_decorator(permission_required('transactions.add_transaction', raise_exception=True), name='dispatch')
class TransactionCreateView(generics.CreateAPIView):
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=False)  # maldita viana que por estar en True no me dejaba buscar y me daba error

            identidad = request.data['numero_identidad']
            code_student = request.data['code_student']
            # Obtener el estudiante
            estudent = Students.objects.filter(code_students=code_student).first()
            if not estudent:
                return Response({"code_student": ["Estudiante no encontrado."]}, status=status.HTTP_400_BAD_REQUEST)

            # Obtener el usuario
            user = User.objects.filter(numero_identidad=identidad).first()
            if not user:
                return Response({"numero_identidad": ["Usuario no encontrado."]}, status=status.HTTP_400_BAD_REQUEST)

            # validamos que el estudiante este asociado al usuario
            if estudent.User != user:
                return Response({"code_student": ["Estudiante no asociado al usuario."]}, status=status.HTTP_400_BAD_REQUEST)

            balance = estudent.balance  # Obtener el balance del estudiante
            balance = float(balance)
            # Obtener el monto de la transacción
            amount = request.data['amount']
            # Convertir el monto a decimal
            amount = float(amount)
            new_balance = balance + amount  # Calcula el nuevo balance
            estudent.balance = new_balance
            estudent.save()

            # Guardar la transacción
            serializer.save()
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = Transaction.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = TransactionSerializer(queryset, many=True)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)

