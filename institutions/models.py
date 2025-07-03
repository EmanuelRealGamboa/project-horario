from django.db import models
from api.enums import InstitutionTypeEnum, ShiftEnum

class Institution(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    responsible = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=InstitutionTypeEnum.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=50)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    grade = models.IntegerField()
    room = models.ForeignKey('schedules.Room', on_delete=models.SET_NULL, null=True, blank=True)
    shift = models.CharField(max_length=15, choices=ShiftEnum.choices, default=ShiftEnum.MORNING)

    def __str__(self):
        return self.name
