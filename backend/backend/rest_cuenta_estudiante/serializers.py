from rest_framework import serializers
from core.models import Cuenta_Estudiante

class Cuenta_Estudiante_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta_Estudiante
        fields = ['id_cuenta',
                  'id_estudiante',
                  'username',
                  'password' 
                  ]