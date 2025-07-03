from django.contrib import admin
from .models import User, Teacher

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'institution', 'created_at')
    search_fields = ('username', 'email')
    list_filter = ('role', 'institution')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'institution')
    search_fields = ('name', 'email')
    list_filter = ('institution',)
