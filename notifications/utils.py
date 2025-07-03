from users.models import User
from notifications.models import Notification

def notify_conflicts(conflicts):
    for conflict in conflicts:
        admins = User.objects.filter(
            role='ADMIN',
            institution=conflict.related_schedule.group.institution
        )
        for admin in admins:
            Notification.objects.create(
                subject=f"Conflict detected: {conflict.type}",
                message=conflict.description,
                recipient=admin,
                recipient_role='ADMIN'
            )
