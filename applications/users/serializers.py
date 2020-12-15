from .models import usuario
###########################
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = (
            'id',
            'email',
            'password',
            'RFC',
            'username',
            'CURP',
            'is_superuser',
        )
    def validated_email(self, data):
        correo = usuario.objects.filter(email=data)
        if len(correo) != 0:
            print("++++++++++++++duplicado++++++++++++++++++")
            raise serializers.ValidationError("email duplicado")
        else:
            return data


##############################################
class Loginserializer(serializers.Serializer):

    email = serializers.EmailField(max_length=30)
    password = serializers.CharField(required=True)



