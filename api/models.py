from django.db import models
from django.contrib.auth.models import User

class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departamento = models.CharField(max_length=100)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Disponibilidad(models.Model):
    PRESENCIAL = 'Presencial'
    VIRTUAL = 'Virtual'
    TIPO_CHOICES = [
        (PRESENCIAL, 'Presencial'),
        (VIRTUAL, 'Virtual'),
    ]

    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='disponibilidades')
    dia_semana = models.CharField(max_length=10)  # e.g. 'Lunes'
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    def __str__(self):
        return f"{self.profesor} - {self.dia_semana} {self.hora_inicio}-{self.hora_fin}"

class Curso(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Aula(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Horario(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='horarios')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=10)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.dia_semana}: {self.curso} by {self.profesor}"

class Solicitud(models.Model):
    PENDIENTE = 'Pendiente'
    APROBADA = 'Aprobada'
    RECHAZADA = 'Rechazada'
    ESTADO_CHOICES = [
        (PENDIENTE, 'Pendiente'),
        (APROBADA, 'Aprobada'),
        (RECHAZADA, 'Rechazada'),
    ]

    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='solicitudes')
    motivo = models.TextField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default=PENDIENTE)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitud {self.id} - {self.profesor} - {self.estado}"
