from django.db import models
from api.enums import ConflictTypeEnum  

class ScheduleConflict(models.Model):
    type = models.CharField(max_length=10, choices=ConflictTypeEnum.choices)
    description = models.TextField()
    related_schedule = models.ForeignKey('schedules.Schedule', on_delete=models.CASCADE, null=True, blank=True)
    resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {'Resolved' if self.resolved else 'Pending'}"
