from django.shortcuts import render
from html5lib import serialize
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt
from core.models import Cuenta_Estudiante
from .serializers import Cuenta_Estudiante_Serializer

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




# def getCuenta(request):
#     if request.method == 'POST':
#         cuenta_estudiante = Cuenta_Estudiante.objects.filter(username="username", password="password")
#         serializer = Cuenta_Estudiante_Serializer(cuenta_estudiante, many=True)
#         return Response(serializer.data)


