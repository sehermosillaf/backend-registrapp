from rest_framework import serializers
from core.models import Asignatura

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Asignatura
        fields=['id_asignatura',
                'nombre']