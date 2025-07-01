from django.db import models
from usuarios.models import Usuario
from api.enums import RolEnum

class Notificacion(models.Model):
    asunto = models.CharField(max_length=255)
    mensaje = models.TextField()
    rol_destinatario = models.CharField(max_length=10, choices=RolEnum.choices)
    destinatario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    enviado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.asunto