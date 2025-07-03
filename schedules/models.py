from django.db import models
from institutions.models import Institution, Group
from users.models import Teacher
from api.enums import DayOfWeekEnum, RoomTypeEnum

class Subject(models.Model):
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    hours = models.IntegerField()
    description = models.TextField(blank=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=RoomTypeEnum.choices)
    capacity = models.IntegerField()
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10, choices=DayOfWeekEnum.choices)
    time_block = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.group.name} - {self.day_of_week} - {self.time_block}"

class TeacherAvailability(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10, choices=DayOfWeekEnum.choices)
    time_block = models.CharField(max_length=20)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.teacher.name} - {self.day_of_week} - {self.time_block}"
