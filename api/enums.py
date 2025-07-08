from django.db import models

class RoleEnum(models.TextChoices):
    ADMIN = 'ADMIN', 'Administrator'
    TEACHER = 'TEACHER', 'Teacher'
    STUDENT = 'STUDENT', 'Student'

class InstitutionTypeEnum(models.TextChoices):
    PUBLIC = 'PUBLIC', 'Public'
    PRIVATE = 'PRIVATE', 'Private'

class ShiftEnum(models.TextChoices):
    MORNING = 'MORNING', 'Morning'
    AFTERNOON = 'AFTERNOON', 'Afternoon'
    NIGHT = 'NIGHT', 'Night'

class RoomTypeEnum(models.TextChoices):
    LAB = 'LAB', 'Lab'
    CLASSROOM = 'CLASSROOM', 'Classroom'
    OTHER = 'OTHER', 'Other'

class DayOfWeekEnum(models.TextChoices):
    MONDAY = 'MONDAY', 'Monday'
    TUESDAY = 'TUESDAY', 'Tuesday'
    WEDNESDAY = 'WEDNESDAY', 'Wednesday'
    THURSDAY = 'THURSDAY', 'Thursday'
    FRIDAY = 'FRIDAY', 'Friday'
    SATURDAY = 'SATURDAY', 'Saturday'
    SUNDAY = 'SUNDAY', 'Sunday'

class ConflictTypeEnum(models.TextChoices):
    SCHEDULE = 'SCHEDULE', 'Schedule'
    TEACHER = 'TEACHER', 'Teacher'
    ROOM = 'ROOM', 'Room'























