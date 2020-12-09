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
            'NombreCompleto',
            'CURP',
            'is_superuser',
        )



