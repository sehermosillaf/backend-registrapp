from django.urls import path
from rest_asignatura.views import getAsignatura

urlpatterns = [
    path('getAsignatura', getAsignatura, name="getAsignatura")
]
