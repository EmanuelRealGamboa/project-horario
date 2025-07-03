from .models import ScheduleConflict
from django.contrib import admin

@admin.register(ScheduleConflict)
class ScheduleConflictAdmin(admin.ModelAdmin):
    list_display = ('type', 'description', 'resolved', 'related_schedule', 'created_at')
    search_fields = ('description',)
    list_filter = ('type', 'resolved')
