from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status  # Documentacion code status
from .models import User
from .serializers import UserSerializer, UserListSerializer
from rest_framework.authtoken.views import ObtainAuthToken


# Create your views here.
class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={
            'request': request})  # Un serializador ya definido en ObtainAuthToken. user y password
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            print(user)

        return Response({'message': 'hola desde response'}, status=status.HTTP_200_OK)




