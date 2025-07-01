from django.db import models

# ENUMS
class RolEnum(models.TextChoices):
    ADMIN = 'ADMIN', 'Administrador'
    PROFESOR = 'PROFESOR', 'Profesor'
    ALUMNO = 'ALUMNO', 'Alumno'

class TipoInstitucionEnum(models.TextChoices):
    PUBLICA = 'PUBLICA', 'Pública'
    PRIVADA = 'PRIVADA', 'Privada'

class TurnoEnum(models.TextChoices):
    MATUTINO = 'MATUTINO', 'Matutino'
    VESPERTINO = 'VESPERTINO', 'Vespertino'
    NOCTURNO = 'NOCTURNO', 'Nocturno'

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



class TipoConflictoEnum(models.TextChoices):
    HORARIO = 'HORARIO', 'Horario'
    PROFESOR = 'PROFESOR', 'Profesor'
    SALON = 'SALON', 'Salón'



























