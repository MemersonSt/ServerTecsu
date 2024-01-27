from rest_framework import generics
from .serializers import TransactionSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction, Students, User


class TransactionCreateView(generics.CreateAPIView):
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            representante = request.data['cedula_representante']
            studiante = request.data['cedula_estudiante']
            # Obtener el estudiante
            estudent = Students.objects.filter(cedula_estudiante=studiante).first()
            if not estudent:
                return Response({"cedula_estudiante": ["Estudiante no encontrado."]}, status=status.HTTP_400_BAD_REQUEST)

            # Obtener el usuario
            user = User.objects.filter(numero_identidad=representante).first()
            if not user:
                return Response({"cedula_representante": ["Usuario no encontrado."]}, status=status.HTTP_400_BAD_REQUEST)

            # validamos que el estudiante este asociado al usuario
            if estudent.Representative != user:
                return Response({"error": ["Estudiante no asociado al usuario."]}, status=status.HTTP_400_BAD_REQUEST)

            balance = float(estudent.balance)  # Obtener el balance del estudiantes
            amount = float(request.data['amount'])  # Obtener el monto de la transacción
            new_balance = balance + amount  # Calcula el nuevo balance
            estudent.balance = new_balance  # Asigna el nuevo balance al estudiante
            estudent.save()  # Guarda el estudiantes
            # Guardar la transacción
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = Transaction.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = TransactionSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



