from django.db import models
from instituciones.models import Institucion, Grupo
from usuarios.models import Profesor
from api.enums import DiaSemanaEnum, TipoSalonEnum

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    horas = models.IntegerField()
    descripcion = models.TextField(blank=True)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Salon(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20, choices=TipoSalonEnum.choices)
    capacidad = models.IntegerField()
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Horario(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=10, choices=DiaSemanaEnum.choices)
    bloque_horario = models.CharField(max_length=20)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.grupo.nombre} - {self.dia_semana} - {self.bloque_horario}"

class DisponibilidadProfesor(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=10, choices=DiaSemanaEnum.choices)
    bloque_horario = models.CharField(max_length=20)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.profesor.nombre} - {self.dia_semana} - {self.bloque_horario}"
