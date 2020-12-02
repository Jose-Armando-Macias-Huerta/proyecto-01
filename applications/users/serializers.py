from .models import User
from rest_framework import serializers
from .managers import UserManager

#
#

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('__all__')


    #def create(self, validated_data):
        #return UserManager(**validated_data)

    #def update(self, instance, validated_data):
        #instance.email = validated_data.get('email',instance.email)
        #instance.RFC = validated_data.get('RFC',instance.RFC)
        #instance.password = validated_data.get('password',instance.password)
        #instance.NombreCompleto = validated_data.get('NombreCompleto',instance.NombreCompleto)
        #instance.CURP = validated_data.get('CURP',instance.email)
        #return instance


