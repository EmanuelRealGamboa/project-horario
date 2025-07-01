from django.contrib import admin
from .models import Materia, Salon, Horario, DisponibilidadProfesor

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'area', 'horas', 'institucion')
    search_fields = ('nombre',)
    list_filter = ('institucion',)

@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'capacidad', 'institucion')
    search_fields = ('nombre',)
    list_filter = ('tipo', 'institucion')

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('materia', 'profesor', 'grupo', 'salon', 'dia_semana', 'bloque_horario')
    search_fields = ('materia__nombre', 'profesor__nombre', 'grupo__nombre')
    list_filter = ('dia_semana', 'bloque_horario', 'profesor', 'grupo')

@admin.register(DisponibilidadProfesor)
class DisponibilidadProfesorAdmin(admin.ModelAdmin):
    list_display = ('profesor', 'dia_semana', 'bloque_horario', 'disponible')
    search_fields = ('profesor__nombre',)
    list_filter = ('dia_semana', 'disponible')
