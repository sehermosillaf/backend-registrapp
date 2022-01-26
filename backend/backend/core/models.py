from django.db import models

# Create your models here.

#Student Models

class Estudiante(models.Model):
    id = models.IntegerField(primary_key=True)
    rut=models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Cuenta_Estudiante(models.Model):
    id_cuenta = models.IntegerField(primary_key=True)
    id_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username


class Asignatura(models.Model):
    id_asignatura=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=20)
    def __str__(self):
        return self.nombre

class Asistencia(models.Model):
    id_asistencia = models.IntegerField(primary_key=True)
    fecha= models.DateField()
    rut_estudiante=models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    id_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    def __str__(self):
        return self.fecha






