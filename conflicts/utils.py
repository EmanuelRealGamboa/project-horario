from django.db.models import Q
from schedules.models import Schedule
from conflicts.models import ScheduleConflict

def detect_conflicts(schedule):
    created_conflicts = []

    conflicts = [
        {
            'type': 'TEACHER',
            'query': Q(teacher=schedule.teacher)
        },
        {
            'type': 'GROUP',
            'query': Q(group=schedule.group)
        },
        {
            'type': 'ROOM',
            'query': Q(room=schedule.room)
        },
    ]

    for conflict in conflicts:
        exists = Schedule.objects.filter(
            conflict['query'],
            day_of_week=schedule.day_of_week,
            time_block=schedule.time_block
        ).exclude(id=schedule.id).exists()

        if exists:
            description = f"{conflict['type'].capitalize()} conflict on {schedule.day_of_week}, block {schedule.time_block}"
            conflict_obj = ScheduleConflict.objects.create(
                type=conflict['type'],
                description=description,
                related_schedule=schedule
            )
            created_conflicts.append(conflict_obj)

    return created_conflicts
