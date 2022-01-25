from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt
from core.models import Cuenta_Estudiante, Estudiante
from .serializers import Cuenta_Estudiante_Serializer
from .serializers import EstudianteSerializer

# Create your views here.
@csrf_exempt
@api_view(['POST'])
def getCuenta(request):
        cuenta_estudiante = Cuenta_Estudiante.objects.get(
            username=request.data.get("username"),
            password=request.data.get("password")
        )
        serializer = Cuenta_Estudiante_Serializer(cuenta_estudiante)

        return Response(serializer.data)

@api_view(['POST'])
def createUser(request):

    #https://stackoverflow.com/questions/16857450/how-to-register-users-in-django-rest-framework
        
        # estudiante = {}
        # estudiante['id'] = request.data.get('id')
        # estudiante['rut'] = request.data.get('rut')
        # estudiante['first_name'] = request.data.get('first_name')
        # estudiante['last_name'] = request.data.get('last_name')
        # estudiante['email'] = request.data.get('email')
        # estudiante_serializer = EstudianteSerializer(estudiante)
        # return Response(estudiante_serializer.data)





@api_view(['POST'])
def genAsistencia(request): 


@api_view(['GET'])
def getAsistencias(request, id):




