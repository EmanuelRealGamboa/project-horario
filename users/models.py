from django.db import models
from api.enums import RoleEnum
from django.contrib.auth.hashers import make_password, check_password


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)
    role = models.CharField(
        max_length=10,
        choices=RoleEnum.choices,
        default=RoleEnum.STUDENT 
    )
    institution_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    def set_password(self, raw_password):
        self.password_hash = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password_hash)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    availability = models.JSONField()
    institution_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username
