from django.urls import path
from rest_asistencia.views import getAsistencia


urlpatterns = [
    path('getAsistencia', getAsistencia, name="getAsistencia")
    ]