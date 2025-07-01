from django.contrib import admin
from .models import Notificacion

@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display = ('asunto', 'destinatario', 'rol_destinatario', 'enviado_en')
    search_fields = ('asunto', 'mensaje')
    list_filter = ('rol_destinatario', 'enviado_en')
