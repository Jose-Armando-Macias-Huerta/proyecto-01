from django.shortcuts import render
###################################

from .models import usuario
from .managers import UserManager
from .serializers import UserSerializer
######################################
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status


class User(ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return usuario.objects.all()


class UserCreate(ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        serializer = UserSerializer
        return Response({"status": "Usuario Creado"}, status=status.HTTP_200_OK)


class DeleteUser(ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = UserSerializer

    def delete(self, request):
        id = self.get_queryset()
        instance = usuario.objects.get(id=id)
        instance.delete()
        return Response({"status": "Usuario eliminado"}, status=status.HTTP_200_OK)


class EditUser(ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = UserSerializer

    def put(self, request):
        instance = usuario.objects.get(id=request.data['id'])
        instance.email = ''
        instance.save()
        serializer = UserManager
        return Response({"status": "Usuario editado"}, status=status.HTTP_200_OK)












