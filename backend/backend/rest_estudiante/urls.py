from django.urls import path
from rest_estudiante.views import crearEstudiante, getEstudiante


urlpatterns = [
    path('getEstudiante', getEstudiante, name="getEstudiante"),
    path('crearEstudiante', crearEstudiante, name="crearCuenta")
    ]