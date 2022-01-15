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
@api_view(['GET','POST'])


def getCuenta(request):
    if request.method == 'GET':
        cuenta_estudiante = Cuenta_Estudiante.objects.all()
        serializer = Cuenta_Estudiante_Serializer(cuenta_estudiante, many=True)
        return Response(serializer.data)


