from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from .models import User
from .managers import UserManager
from .serializers import UserSerializer

########
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

class listUserAdmin(ModelViewSet): 
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()



class createUserAdmin(ModelViewSet): 
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        serializer = UserSerializer
        return Response({"status": "Administrador creado"}, status=status.HTTP_200_OK)

class deleteUser(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request):
        id = self.get_queryset()
        instance = User.objects.get(id=id)
        instance.delete()
        return Response({"status": "Usuario eliminado"}, status=status.HTTP_200_OK)

class edittUserAdmin(ModelViewSet): 
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request):
        instance = User.objects.get(id=request.data['id'])
        instance.email = ''
        instance.save()
        serializer = UserSerializer
        return Response({"status": "Administrador editado"}, status=status.HTTP_200_OK)













