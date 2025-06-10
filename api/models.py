from django.db import models

# ENUMS auxiliares
class RolEnum(models.TextChoices):
    ADMIN = 'ADMIN', 'Administrador'
    PROFESOR = 'PROFESOR', 'Profesor'
    ALUMNO = 'ALUMNO', 'Alumno'

class TipoInstitucionEnum(models.TextChoices):
    PUBLICA = 'PUBLICA', 'Pública'
    PRIVADA = 'PRIVADA', 'Privada'

class TipoSalonEnum(models.TextChoices):
    LABORATORIO = 'LABORATORIO', 'Laboratorio'
    AULA = 'AULA', 'Aula'
    OTRO = 'OTRO', 'Otro'

class DiaSemanaEnum(models.TextChoices):
    LUNES = 'LUNES', 'Lunes'
    MARTES = 'MARTES', 'Martes'
    MIERCOLES = 'MIERCOLES', 'Miércoles'
    JUEVES = 'JUEVES', 'Jueves'
    VIERNES = 'VIERNES', 'Viernes'
    SABADO = 'SABADO', 'Sábado'
    DOMINGO = 'DOMINGO', 'Domingo'

# MODELOS

class Institucion(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    responsable = models.CharField(max_length=255)
    tipo = models.CharField(max_length=10, choices=TipoInstitucionEnum.choices)
    creado_en = models.DateTimeField(auto_now_add=True)

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    contrasena_hash = models.CharField(max_length=255)
    rol = models.CharField(max_length=10, choices=RolEnum.choices)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(auto_now_add=True)

class Profesor(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.EmailField()
    disponibilidad = models.JSONField()
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    clave = models.CharField(max_length=20)
    area = models.CharField(max_length=100)
    horas = models.IntegerField()
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)

class Salon(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20, choices=TipoSalonEnum.choices)
    capacidad = models.IntegerField()
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)

class Grupo(models.Model):
    nombre = models.CharField(max_length=50)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    grado = models.IntegerField()
    salon = models.ForeignKey(Salon, on_delete=models.SET_NULL, null=True, blank=True)

class Horario(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=10, choices=DiaSemanaEnum.choices)
    bloque_horario = models.CharField(max_length=20)
    creado_en = models.DateTimeField(auto_now_add=True)

class Notificacion(models.Model):
    asunto = models.CharField(max_length=255)
    mensaje = models.TextField()
    rol_destinatario = models.CharField(max_length=10, choices=RolEnum.choices)
    destinatario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    enviado_en = models.DateTimeField(auto_now_add=True)

class RegistroActividad(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    accion = models.CharField(max_length=255)
    descripcion = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)
