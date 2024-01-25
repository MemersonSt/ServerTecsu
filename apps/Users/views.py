from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  # Documentacion code status
from .serializers import (
    UserCreateSerializer,
    UserTokenSerializer,
    UserListSerializer,
    UserDetailSerializer,
    EstudentsSerializer,
    EstudentsDetailSerializer,
    VincularSerializer,
)
from .models import Students, User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist
import logging


# Create your views here.
class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={
            'request': request})  # Un serializador ya definido en ObtainAuthToken. user y password
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                # print(user.students_set.all())
                user_serializer = UserTokenSerializer(user)
                # print(user_serializer.data.get('students'))
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
        try:
            if request.user.is_authenticated:
                token = Token.objects.get(user=request.user)
                token.delete()
                return Response({'message': 'Sesión cerrada correctamente'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Usuario no autenticado'}, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as e:
            logging.warning(f'Token no encontrado: {e}')
            return Response({'message': 'Token no encontrado'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.error(f'Error al cerrar sesión: {e}')
            return Response({'message': 'No se pudo cerrar la sesión'}, status=status.HTTP_400_BAD_REQUEST)


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


class UserDetail(CreateAPIView):
    serializer_class = UserDetailSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)  # Obtenemos los datos del request
            serializer.is_valid(raise_exception=True)

            numero_identidad = serializer.validated_data['numero_identidad']  # Obtenemos el numero de identidad

            user = User.objects.filter(numero_identidad=numero_identidad).first()  # Obtenemos el usuario
            user_serializer = UserCreateSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'message': 'No existe el usuario'}, status=status.HTTP_404_NOT_FOUND)


class UserUpdate(UpdateAPIView):
    serializer_class = UserCreateSerializer

    def get_queryset(self):
        return User.objects.all()

    def put(self, request, *args, **kwargs):
        user = self.get_queryset().get(pk=kwargs['pk'])
        if user:
            user_serializer = self.serializer_class(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)


class UserList(ListAPIView):
    serializer_class = UserListSerializer

    def get_queryset(self):
        return User.objects.all()

    def get(self, request, *args, **kwargs):
        users = self.get_queryset()
        users_serializer = self.serializer_class(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)


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


class EstudentDetail(CreateAPIView):
    serializer_class = EstudentsDetailSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)  # Obtenemos los datos del request
            serializer.is_valid(raise_exception=True)

            code_students = serializer.validated_data['code_students']  # Obtenemos el codigo del estudiante


            estudent = Students.objects.filter(code_students=code_students).first()  # Obtenemos el estudiante
            print(estudent)
            estudent_serializer = EstudentsSerializer(estudent)
            return Response(estudent_serializer.data, status=status.HTTP_200_OK)
        except Students.DoesNotExist:
            return Response({'message': 'No existe el estudiante'}, status=status.HTTP_404_NOT_FOUND)


class EstudentUpdate(UpdateAPIView):
    serializer_class = EstudentsSerializer

    def get_queryset(self):
        return Students.objects.all()  # Obtenemos todos los estudiantes

    def put(self, request, *args, **kwargs):
        estudent = self.get_queryset().get(pk=kwargs['pk'])
        if estudent:
            estudent_serializer = self.serializer_class(estudent, data=request.data)
            if estudent_serializer.is_valid():
                estudent_serializer.save()
                return Response(estudent_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(estudent_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Estudiante no encontrado'}, status=status.HTTP_404_NOT_FOUND)


class EstudentDelete(DestroyAPIView):
    serializer_class = EstudentsSerializer

    def get_queryset(self):
        return Students.objects.all()

    def delete(self, request, *args, **kwargs):
        estudent = self.get_queryset().get(pk=kwargs['pk'])
        if estudent:
            estudent.delete()
            return Response({'message': 'Estudiante eliminado correctamente'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Estudiante no encontrado'}, status=status.HTTP_400_BAD_REQUEST)


class EstudentList(ListAPIView):
    serializer_class = EstudentsSerializer

    def get_queryset(self):
        return Students.objects.all()

    def get(self, request, *args, **kwargs):
        estudents = self.get_queryset()
        estudents_serializer = self.serializer_class(estudents, many=True)
        return Response(estudents_serializer.data, status=status.HTTP_200_OK)


# Vincular estudiante a usuario ManyToMany
class VincularEstudiante(CreateAPIView):
    serializer_class = VincularSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  # Obtenemos los datos del request
        serializer.is_valid(raise_exception=True)  # Validamos los datos

        Identidad = serializer.validated_data['numero_identidad']  # Obtenemos el numero de identidad
        code_students = serializer.validated_data['code_students']  # Obtenemos el codigo del estudiante
        try:
            #  user = User.objects.get(pk=user_id)  # Obtenemos el usuario
            user = User.objects.filter(numero_identidad=Identidad).first()  # Obtenemos el usuario
            estudent = Students.objects.filter(code_students=code_students).first()  # Obtenemos el estudiante

            estudent.User = user  # Asignamos el representante al estudiante

            estudent.save()  # Me olvide de guardar el usuario XD

            return Response({'message': 'Estudiante vinculado correctamente'}, status=status.HTTP_201_CREATED)

        except:
            return Response({'message': 'Error al vincular el estudiante'}, status=status.HTTP_400_BAD_REQUEST)

