from django.db import models
from users.models import User
from api.enums import RoleEnum

class Notification(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    recipient_role = models.CharField(max_length=10, choices=RoleEnum.choices)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
