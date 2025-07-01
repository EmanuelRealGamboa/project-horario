from django.db import models
from instituciones.models import Institucion
from api.enums import RolEnum



class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    contrasena_hash = models.CharField(max_length=255)
    rol = models.CharField(max_length=10, choices=RolEnum.choices)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_usuario


class Profesor(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.EmailField()
    disponibilidad = models.JSONField()
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre