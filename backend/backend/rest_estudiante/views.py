from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt
from core.models import Estudiante
from .serializers import EstudianteSerializer
# Create your views here.

@csrf_exempt
@api_view(['GET'])

def getEstudiante(request):
    if request.method == 'GET':
        estudiante = Estudiante.objects.all()
        serializer = EstudianteSerializer(estudiante, many=True)
        return Response(serializer.data)
    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = EstudianteSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def crearEstudiante(request):
    try:
        estudiantetmp = None
        estudiante = {}
        estudiante['id'] = request.data.get("id")
        estudiante['rut'] = request.data.get("rut")
        estudiante['first_name'] = request.data.get("first_name")
        estudiante['last_name'] = request.data.get("last_name")
        estudiante['email'] = request.data.get("email")

        estudiante = estudiante.JSONParser().parse(request)
        estudianteSerializer = EstudianteSerializer(estudiantetmp ,data= estudiante ) 
        if estudianteSerializer.is_valid():
            EstudianteSerializer.save()
        return Response(status.HTTP_201_CREATED)

    except Exception as e:
        return Response(e,status.HTTP_404_NOT_FOUND)



