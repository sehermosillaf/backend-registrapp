from django.urls import path
from rest_cuenta_estudiante.views import getCuenta, createAccount


urlpatterns = [
    path('getCuenta', getCuenta, name="getCuenta"),
    path('crearCuenta', createAccount, name="createAccount"),
]
