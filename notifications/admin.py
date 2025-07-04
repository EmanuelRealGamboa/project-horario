from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('subject', 'recipient', 'recipient_role', 'sent_at')
    search_fields = ('subject', 'message')
    list_filter = ('recipient_role', 'sent_at')
