from django.shortcuts import render, get_object_or_404
###################################
from .models import usuario
from .managers import UserManager
from .serializers import UserSerializer, Loginserializer
######################################
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.views import APIView
######################################
from django.core.mail import send_mail
######################################

class UserSet(viewsets.GenericViewSet):

    
    queryset = usuario.objects.all()
    serializer_class = UserSerializer


    

 

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_nuevo = serializer.create(serializer.validated_data)
        ########################################
        nombre = serializer.data.get('username')
        RFC = serializer.data.get('RFC')
        ########################################
        ########################################
        send_mail('prueba', "Hola "+ nombre + " te haz registrado, tu RFC es : " + RFC , 'pruebadecuenta4826@gmail.com', [user_nuevo], fail_silently=False)
        return Response ({"status": "Usuario Creado, se le informara al correo proporcionado "}, status=status.HTTP_200_OK)

class DeleteUser(viewsets.ModelViewSet):

    queryset = usuario.objects.all()
    serializer_class = UserSerializer


    def delete(self, request):
        id = self.get_queryset()
        instance = usuario.objects.get(id=id)
        instance.delete()
        return Response ({"status": "Usuario eliminado"}, status=status.HTTP_200_OK)



    # def put(self, request):
    #     instance = usuario.objects.get(id=request.data['id'])
    #     instance.email = ''
    #     instance.save()
    #     serializer = UserManager
    #     return Response ({"status": "Usuario editado"},status=status.HTTP_200_OK) 


#############################################################




class login(viewsets.GenericViewSet):
    queryset = usuario.objects.all()
    serializer_class = Loginserializer

    def create(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        try:
            user = usuario.objects.get(email=email,password=password)
        except usuario.DoesNotExist:
            return Response ("email o contraseña incorrecta")




        token, created = Token.objects.get_or_create(user=user)
        
        return Response ("token es : " + token.key )












