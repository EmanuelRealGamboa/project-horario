from django.db import models
from api.enums import TipoInstitucionEnum, TurnoEnum

class Institucion(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    responsable = models.CharField(max_length=255)
    tipo = models.CharField(max_length=10, choices=TipoInstitucionEnum.choices)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Grupo(models.Model):
    nombre = models.CharField(max_length=50)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    grado = models.IntegerField()
    salon = models.ForeignKey('horarios.Salon', on_delete=models.SET_NULL, null=True, blank=True)
    turno = models.CharField(max_length=15, choices=TurnoEnum.choices, default=TurnoEnum.MATUTINO)

    def __str__(self):
        return self.nombre
