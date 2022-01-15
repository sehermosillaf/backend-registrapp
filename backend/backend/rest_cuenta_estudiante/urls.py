from django.urls import path
from rest_cuenta_estudiante.views import getCuenta

urlpatterns = [
    path('getCuenta', getCuenta, name="getCuenta")
]
