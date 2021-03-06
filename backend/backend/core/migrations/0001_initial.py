# Generated by Django 4.0.1 on 2022-01-12 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id_asignatura', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta_Estudiante',
            fields=[
                ('id_cuenta', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=10)),
                ('id_estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id_asistencia', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('id_asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.asignatura')),
                ('rut_estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estudiante')),
            ],
        ),
    ]
