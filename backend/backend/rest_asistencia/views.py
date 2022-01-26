from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt
from core.models import Asistencia
from .serializers import AsistenciaSerializer
# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])

def getAsistencia(request):
    if request.method == 'GET':
        asistencia = Asistencia.objects.all()
        serializer = AsistenciaSerializer(asistencia, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AsistenciaSerializer(data=data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
