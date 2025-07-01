from django.db import models
from api.enums import TipoConflictoEnum

class ConflictoHorario(models.Model):
    tipo = models.CharField(max_length=10, choices=TipoConflictoEnum.choices)
    descripcion = models.TextField()
    horario_relacionado = models.ForeignKey('horarios.Horario', on_delete=models.CASCADE, null=True, blank=True)
    resuelto = models.BooleanField(default=False)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {'Resuelto' if self.resuelto else 'Pendiente'}"