from django.contrib import admin
from .models import ConflictoHorario

@admin.register(ConflictoHorario)
class ConflictoHorarioAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'descripcion', 'resuelto', 'horario_relacionado', 'creado_en')
    search_fields = ('descripcion',)
    list_filter = ('tipo', 'resuelto')

