from rest_framework import serializers
from core.models import Asistencia

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Asistencia
        fields=['id_asistencia', 
                'fecha',
                'rut_estudiante',
                'id_asignatura',
                ]