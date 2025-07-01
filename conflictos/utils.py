from django.db.models import Q
from horarios.models import Horario
from conflictos.models import ConflictoHorario

def detectar_conflictos(horario):
    conflictos_creados = []

    conflictos = [
        {
            'tipo': 'PROFESOR',
            'query': Q(profesor=horario.profesor)
        },
        {
            'tipo': 'GRUPO',
            'query': Q(grupo=horario.grupo)
        },
        {
            'tipo': 'SALON',
            'query': Q(salon=horario.salon)
        },
    ]

    for conflicto in conflictos:
        existe = Horario.objects.filter(
            conflicto['query'],
            dia_semana=horario.dia_semana,
            bloque_horario=horario.bloque_horario
        ).exclude(id=horario.id).exists()

        if existe:
            descripcion = f"Conflicto de {conflicto['tipo'].lower()} en el día {horario.dia_semana}, bloque {horario.bloque_horario}"
            conflicto_obj = ConflictoHorario.objects.create(
                tipo=conflicto['tipo'],
                descripcion=descripcion,
                horario_relacionado=horario
            )
            conflictos_creados.append(conflicto_obj)

    return conflictos_creados
