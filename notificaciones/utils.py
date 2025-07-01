from usuarios.models import Usuario
from notificaciones.models import Notificacion

def notificar_conflictos(conflictos):
    for conflicto in conflictos:
        admins = Usuario.objects.filter(
            rol='ADMIN',
            institucion=conflicto.horario_relacionado.grupo.institucion
        )
        for admin in admins:
            Notificacion.objects.create(
                asunto=f"Conflicto detectado: {conflicto.tipo}",
                mensaje=conflicto.descripcion,
                destinatario=admin,
                rol_destinatario='ADMIN'
            )
