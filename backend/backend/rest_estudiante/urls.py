from django.urls import path
from rest_estudiante.views import getEstudiante


urlpatterns = [
    path('getEstudiante', getEstudiante, name="getEstudiante")
    ]