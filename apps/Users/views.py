from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  # Documentacion code status
from .serializers import UserCreateSerializer, UserTokenSerializer, EstudentsSerializer
from .models import Estudents
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


# Create your views here.
class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={
            'request': request})  # Un serializador ya definido en ObtainAuthToken. user y password
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de sesión exitoso'
                    }, status=status.HTTP_201_CREATED)
                else:
                    token.delete()
                    token = Token.objects.create(user=user)
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de sesión exitoso'
                    }, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Usuario no activo'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'message': 'Usuario o contraseña incorrectos'}, status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    def post(self, request, *args, **kwargs):
        token = Token.objects.filter(user=request.user).first()
        if token:
            token.delete()
        return Response({'message': 'Sesión cerrada correctamente'}, status=status.HTTP_200_OK)


class UserCreate(CreateAPIView):
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'Usuario creado correctamente',
                'user': user_serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ESTUDIANTE
class EstudentCreate(CreateAPIView):
    serializer_class = EstudentsSerializer

    def post(self, request, *args, **kwargs):
        estudent_serializer = self.serializer_class(data=request.data)
        if estudent_serializer.is_valid():
            estudent_serializer.save()
            return Response({
                'message': 'Estudiante creado correctamente',
                'estudent': estudent_serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(estudent_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EstudentUpdate(UpdateAPIView):
    serializer_class = EstudentsSerializer

    def put(self, request, *args, **kwargs):
        estudent = self.queryset.get(pk=kwargs['pk'])
        if estudent:
            estudent_serializer = self.serializer_class(estudent, data=request.data)
            if estudent_serializer.is_valid():
                estudent_serializer.save()
                return Response(estudent_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(estudent_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EstudentDelete(DestroyAPIView):
    serializer_class = EstudentsSerializer

    def delete(self, request, *args, **kwargs):
        estudent = self.queryset.get(pk=kwargs['pk'])
        if estudent:
            estudent.delete()
            return Response({'message': 'Estudiante eliminado correctamente'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Estudiante no encontrado'}, status=status.HTTP_400_BAD_REQUEST)


class EstudentList(ListAPIView):
    serializer_class = EstudentsSerializer

    def get(self, request, *args, **kwargs):
        estudents = self.queryset.all()
        estudents_serializer = self.serializer_class(estudents, many=True)
        return Response(estudents_serializer.data, status=status.HTTP_200_OK)
