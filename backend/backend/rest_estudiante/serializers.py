from rest_framework import serializers
from core.models import Estudiante

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estudiante
        fields=['id', 
                'rut',
                'first_name',
                'last_name',
                 'email'
                ]
        