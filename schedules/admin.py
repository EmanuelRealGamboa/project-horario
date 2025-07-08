from django.contrib import admin
from .models import Subject, Room, Schedule, TeacherAvailability

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'area', 'hours')  
    search_fields = ('name',)
    list_filter = () 

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'capacity')  
    search_fields = ('name',)
    list_filter = ('type',)  

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('subject', 'teacher', 'room', 'day_of_week', 'time_block')  
    search_fields = ('subject__name', 'teacher__name')
    list_filter = ('day_of_week', 'time_block', 'teacher')  

@admin.register(TeacherAvailability)
class TeacherAvailabilityAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'day_of_week', 'time_block', 'available')
    search_fields = ('teacher__name',)
    list_filter = ('day_of_week', 'available')
