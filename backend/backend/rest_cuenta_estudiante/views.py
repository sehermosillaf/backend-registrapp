from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt
from core.models import Cuenta_Estudiante, Estudiante
from .serializers import Cuenta_Estudiante_Serializer
\

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
def createAccount(request):
   
    #https://stackoverflow.com/questions/16857450/how-to-register-users-in-django-rest-framework
        cuentatmp = None
        cuentaEstudiante = {}
        cuentaEstudiante['username'] = request.data.get('username')
        cuentaEstudiante['password'] = request.data.get('password')
        cuenta_estudiante_serializer = Cuenta_Estudiante_Serializer(cuentatmp, data = cuentaEstudiante)
        if cuentaEstudiante.is_valid():
            CuentaNueva = cuenta_estudiante_serializer.save()
            return Response(status.HTTP_201_CREATED)
  





# @api_view(['POST'])
# def genAsistencia(request): 


# @api_view(['GET'])
# def getAsistencias(request, id):




