from django.contrib import admin
from .models import Usuario, Profesor

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_usuario', 'correo', 'rol', 'institucion', 'creado_en')
    search_fields = ('nombre_usuario', 'correo')
    list_filter = ('rol', 'institucion')

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'institucion')
    search_fields = ('nombre', 'correo')
    list_filter = ('institucion',)
