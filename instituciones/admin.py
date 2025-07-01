from django.contrib import admin
from .models import Institucion, Grupo

@admin.register(Institucion)
class InstitucionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono', 'correo', 'responsable', 'tipo')
    search_fields = ('nombre', 'correo')
    list_filter = ('tipo',)

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'grado', 'institucion', 'salon')
    search_fields = ('nombre',)
    list_filter = ('grado', 'institucion')
